# -*- coding: utf-8 -*-
"""Network helpers (stdlib)."""
from __future__ import annotations

import json
import urllib.request


def fetch_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "quantserve"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_file(url: str, dest: str, chunk_size: int = 1024 * 1024) -> int:
    """Stream a URL to dest, returning bytes written."""
    written = 0
    req = urllib.request.Request(url, headers={"User-Agent": "quantserve"})
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
        while True:
            chunk = resp.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            written += len(chunk)
    return written
