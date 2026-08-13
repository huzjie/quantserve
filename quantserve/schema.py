# -*- coding: utf-8 -*-
"""Core data models (dataclasses)."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional


@dataclass
class ModelProfile:
    """A downloadable open-weight model definition."""
    id: str                       # e.g. "qwen/qwen3.8-2.4t-a95b"
    name: str
    family: str                   # qwen / deepseek / nemotron / ...
    total_params_b: float         # billion params (total)
    active_params_b: float        # billion params activated per token (MoE)
    architecture: str             # "moe" | "dense"
    num_experts: int = 0
    experts_per_token: int = 0
    context_length: int = 32768
    max_context_length: int = 32768
    bf16_size_gb: float = 0.0     # weights on disk (bf16), approximate
    hf_id: str = ""
    modelscope_id: str = ""
    ollama_tag: str = ""
    license: str = "Apache-2.0"
    tags: List[str] = field(default_factory=list)
    note: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class QuantSpec:
    """A quantization method + target configuration."""
    method: str                   # fp8 / int8 / int4 / awq / gguf / onedbit / mixed / none
    bits: float = 16.0
    group_size: int = 128
    layer_selective: bool = False
    target_size_gb: Optional[float] = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class EngineSpec:
    """An inference engine description."""
    name: str
    supported_architectures: List[str] = field(default_factory=list)
    supports_moe: bool = False
    supports_streaming: bool = True
    openai_compatible: bool = True
    note: str = ""


@dataclass
class PlanResult:
    """Output of a parallel/quant/cost planning step."""
    ok: bool = True
    summary: str = ""
    details: Dict = field(default_factory=dict)
    commands: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "summary": self.summary,
            "details": self.details,
            "commands": self.commands,
            "warnings": self.warnings,
        }
