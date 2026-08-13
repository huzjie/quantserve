# -*- coding: utf-8 -*-
"""API-key auth for the gateway (constant-time compare)."""
import hmac

API_KEY_HEADER = "Authorization"


def check_auth(provided: str, expected: str | None) -> bool:
    if expected is None:
        return True
    return hmac.compare_digest(provided or "", expected)


def bearer(header: str) -> str:
    if not header:
        return ""
    if header.lower().startswith("bearer "):
        return header[7:].strip()
    return header.strip()
