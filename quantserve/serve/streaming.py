# -*- coding: utf-8 -*-
"""Server-sent events (SSE) streaming helpers."""
import json
import time


def sse_chunk(data: dict) -> str:
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"


def sse_done() -> str:
    return "data: [DONE]\n\n"


def token_event(content: str, model: str, ts: int) -> dict:
    return {
        "id": "chatcmpl-stream", "object": "chat.completion.chunk",
        "created": ts, "model": model,
        "choices": [{"index": 0, "delta": {"content": content},
                     "finish_reason": None}],
    }
