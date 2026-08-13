# -*- coding: utf-8 -*-
"""Stdlib OpenAI-compatible gateway.

A zero-dependency HTTP server that fronts a running engine's own
OpenAI-compatible endpoint, adding auth + /healthz + /v1/models.
"""
from __future__ import annotations

import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .auth import check_auth, bearer
from .streaming import sse_chunk, sse_done, token_event


class Gateway:
    def __init__(self, upstream="http://127.0.0.1:8001", auth_token=None):
        self.upstream = upstream.rstrip("/")
        self.auth_token = auth_token

    def _proxy(self, path: str, body: bytes | None, headers: dict):
        url = self.upstream + path
        req = urllib.request.Request(url, data=body, method="POST")
        for k, v in headers.items():
            if k.lower() in ("host", "content-length"):
                continue
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                return resp.status, resp.read(), dict(resp.headers)
        except urllib.error.HTTPError as e:
            return e.code, e.read(), dict(e.headers)

    def handler(self):
        gw = self

        class H(BaseHTTPRequestHandler):
            def _send(self, code, body: bytes, ctype="application/json"):
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def _auth_fail(self):
                self._send(401, b'{"error":"unauthorized"}')

            def _check(self) -> bool:
                if gw.auth_token is None:
                    return True
                return check_auth(bearer(self.headers.get("Authorization", "")),
                                  gw.auth_token)

            def do_GET(self):
                if self.path == "/healthz":
                    return self._send(200, b'{"status":"ok"}')
                if self.path == "/v1/models":
                    st, body, _ = gw._proxy("/v1/models", None, {})
                    return self._send(st, body)
                self._send(404, b'{"error":"not found"}')

            def do_POST(self):
                if not self._check():
                    return self._auth_fail()
                n = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(n) if n else None
                hdrs = {k: v for k, v in self.headers.items()}
                st, resp, _ = gw._proxy(self.path, body, hdrs)
                self._send(st, resp)

            def log_message(self, *a):
                pass

        return H

    def serve(self, host="127.0.0.1", port=8000):
        srv = ThreadingHTTPServer((host, port), self.handler())
        print(f"QuantServe gateway listening on http://{host}:{port} "
              f"-> upstream {self.upstream}")
        srv.serve_forever()
