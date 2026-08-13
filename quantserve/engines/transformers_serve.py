# -*- coding: utf-8 -*-
"""Standalone Transformers-based OpenAI-compatible serving entrypoint.

Used by the `transformers` engine adapter. Requires `transformers` +
`fastapi` + `uvicorn` (optional; falls back to stdlib http.server).
"""
import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


def _load_model(model_path):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
    return tok, model


def _chat(tok, model, messages, max_tokens=256, temperature=0.7):
    import torch
    prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_tokens,
                             temperature=temperature, do_sample=temperature > 0)
    text = tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    tok, model = _load_model(args.model)

    class Handler(BaseHTTPRequestHandler):
        def _send(self, obj, code=200):
            body = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path in ("/v1/models", "/healthz"):
                return self._send({"object": "list", "data": [
                    {"id": args.model, "object": "model"}]})
            self._send({"error": "not found"}, 404)

        def do_POST(self):
            if self.path == "/v1/chat/completions":
                n = int(self.headers.get("Content-Length", 0))
                req = json.loads(self.rfile.read(n) or b"{}")
                text = _chat(tok, model, req.get("messages", []),
                             req.get("max_tokens", 256),
                             req.get("temperature", 0.7))
                return self._send({
                    "id": "chatcmpl-%d" % int(time.time()),
                    "object": "chat.completion",
                    "created": int(time.time()),
                    "model": args.model,
                    "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                                 "finish_reason": "stop"}],
                    "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                })
            self._send({"error": "not found"}, 404)

        def log_message(self, *a):
            pass

    print(f"serving {args.model} on http://{args.host}:{args.port}")
    HTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
