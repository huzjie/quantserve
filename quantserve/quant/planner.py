# -*- coding: utf-8 -*-
"""Quantization planner: recommend a method for a target hardware budget."""
from __future__ import annotations

from .base import (
    QuantMethod, Fp16Method, Fp8Method, Int8Method, Int4Method,
    AwqMethod, GgufMethod, OneBitMethod, MixedMethod,
)

ALL_METHODS = {
    "fp16": Fp16Method(),
    "fp8": Fp8Method(),
    "int8": Int8Method(),
    "int4": Int4Method(),
    "awq": AwqMethod(),
    "gguf": GgufMethod(),
    "onedbit": OneBitMethod(),
    "mixed": MixedMethod(),
}


class QuantPlanner:
    def __init__(self):
        self.methods = ALL_METHODS

    def list_methods(self) -> list:
        return [m.describe() for m in self.methods.values()]

    def plan_all(self, model) -> list:
        """Return every method's estimate for a model."""
        return [m.plan(model) for m in self.methods.values()]

    def recommend(self, model, budget_gb: float | None = None,
                  target_size_gb: float | None = None):
        """Pick the highest-precision method that fits the budget."""
        results = self.plan_all(model)
        fits = results
        if budget_gb is not None:
            fits = [r for r in fits if r.est_memory_gb <= budget_gb]
        if target_size_gb is not None:
            fits = [r for r in fits if r.quantized_gb <= target_size_gb]
        if not fits:
            return None, results
        # highest bits that still fits
        best = max(fits, key=lambda r: r.bits)
        return best, results
