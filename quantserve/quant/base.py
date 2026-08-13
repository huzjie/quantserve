# -*- coding: utf-8 -*-
"""Quantization method base + shared size/bandwidth math."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class QuantResult:
    method: str
    bits: float
    original_gb: float
    quantized_gb: float
    compression_ratio: float       # original / quantized
    est_memory_gb: float           # runtime memory for inference
    est_throughput_tps: float = 0.0
    note: str = ""

    def to_dict(self) -> dict:
        return {
            "method": self.method, "bits": self.bits,
            "original_gb": round(self.original_gb, 2),
            "quantized_gb": round(self.quantized_gb, 2),
            "compression_ratio": round(self.compression_ratio, 2),
            "est_memory_gb": round(self.est_memory_gb, 2),
            "est_throughput_tps": round(self.est_throughput_tps, 2),
            "note": self.note,
        }


class QuantMethod:
    name = "base"
    bits = 16.0

    def quantized_size(self, original_gb: float) -> float:
        """Estimate on-disk size after quantization."""
        return original_gb * (self.bits / 16.0)

    def runtime_memory(self, model) -> float:
        """Estimate GPU/CPU memory (GB) to run the quantized model.

        Active params drive memory for MoE; total params for dense.
        """
        params_b = model.active_params_b if model.architecture == "moe" else model.total_params_b
        # bytes per param for this precision + ~20% overhead for activations/kv
        mem = params_b * 1e9 * (self.bits / 8) / 1e9
        return mem * 1.2

    def plan(self, model, spec=None) -> QuantResult:
        orig = model.bf16_size_gb
        size = self.quantized_size(orig)
        if spec is not None and spec.target_size_gb:
            size = min(size, spec.target_size_gb)
        return QuantResult(
            method=self.name, bits=self.bits, original_gb=orig,
            quantized_gb=size,
            compression_ratio=(orig / size) if size > 0 else 0.0,
            est_memory_gb=self.runtime_memory(model),
            note=self.describe(),
        )

    def describe(self) -> str:
        return f"{self.name} ({self.bits}-bit)"


class Fp16Method(QuantMethod):
    name = "fp16"
    bits = 16.0

    def describe(self):
        return "fp16 — 无损精度，标准部署格式"


class Fp8Method(QuantMethod):
    name = "fp8"
    bits = 8.0

    def describe(self):
        return "fp8 — 体积减半，需 H100/H20/Ada 等硬件支持"


class Int8Method(QuantMethod):
    name = "int8"
    bits = 8.0

    def describe(self):
        return "int8 — 动态量化，CPU 友好，精度损失极小"


class Int4Method(QuantMethod):
    name = "int4"
    bits = 4.0

    def describe(self):
        return "int4 (GPTQ) — 体积 1/4，需校准数据集"


class AwqMethod(QuantMethod):
    name = "awq"
    bits = 4.0

    def describe(self):
        return "awq — 激活感知量化，4-bit 精度更稳，无需反向传播"


class GgufMethod(QuantMethod):
    name = "gguf"
    bits = 4.0

    def describe(self):
        return "gguf — llama.cpp/Ollama 格式，Q4_K_M，CPU 可跑"


class OneBitMethod(QuantMethod):
    name = "onedbit"
    bits = 1.58

    def describe(self):
        return "onedbit — 动态 1-bit 分层选择性量化（Unsloth 式），体积压缩约 91%"


class MixedMethod(QuantMethod):
    name = "mixed"
    bits = 6.0

    def describe(self):
        return "mixed — 注意力层 fp16 + FFN 层低比特，混合精度"
