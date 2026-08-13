# -*- coding: utf-8 -*-
"""Integrity verification helpers."""
import hashlib
from pathlib import Path


def _hash_file(path, algo):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256(path) -> str:
    return _hash_file(path, "sha256")


def md5(path) -> str:
    return _hash_file(path, "md5")


def verify(path, expected: str, algo: str = "sha256") -> bool:
    """Verify a file against an expected hex digest.  Empty expected -> skip."""
    if not expected:
        return True
    actual = _hash_file(Path(path), algo)
    return actual.lower() == expected.lower()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
