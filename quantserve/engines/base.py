# -*- coding: utf-8 -*-
"""Inference engine base class: builds a launch command for a model."""
from __future__ import annotations

import shutil


class Engine:
    name = "base"
    binary = ""

    def __init__(self):
        self.binary = self._find_binary()

    def _find_binary(self) -> str:
        return shutil.which(self.binary) or ""

    @property
    def available(self) -> bool:
        return bool(self.binary)

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra: list | None = None) -> list:
        raise NotImplementedError

    def supports_moe(self) -> bool:
        return False


def _fmt_gpus(gpus):
    if not gpus:
        return []
    if isinstance(gpus, int):
        return [f"--tensor-parallel-size", str(gpus)]
    return [f"--tensor-parallel-size", str(len(gpus))]
