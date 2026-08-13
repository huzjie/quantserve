# -*- coding: utf-8 -*-
"""Source abstraction: turns a ModelProfile into a list of file URLs."""
from __future__ import annotations


class Source:
    name = "base"

    def files(self, model) -> list:
        raise NotImplementedError


class FileSpec:
    def __init__(self, url: str, filename: str, size_bytes: int = 0,
                 sha256: str = ""):
        self.url = url
        self.filename = filename
        self.size_bytes = size_bytes
        self.sha256 = sha256

    def __repr__(self):
        return f"<FileSpec {self.filename} {self.size_bytes}b>"
