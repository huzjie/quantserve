# -*- coding: utf-8 -*-
"""Calibration dataset helpers for GPTQ/AWQ-style post-training quantization.

Provides a synthetic + file-based calibration loader so quantization tooling
has a deterministic, reproducible activation sample.
"""
from __future__ import annotations

DEFAULT_SAMPLES = [
    "The quick brown fox jumps over the lazy dog.",
    "量化是把浮点权重映射到低比特整数的过程。",
    "Open-weight models enable private on-premise deployment.",
    "Mixture-of-experts activates a subset of experts per token.",
    "本地化部署大幅降低推理成本并保护数据隐私。",
]


def load_calibration(path=None, n=128):
    """Return up to `n` calibration strings (file lines or built-in samples)."""
    if path:
        with open(path, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        return lines[:n]
    # cycle built-in samples to reach n
    out = []
    while len(out) < n:
        out.extend(DEFAULT_SAMPLES)
    return out[:n]
