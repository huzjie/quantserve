# -*- coding: utf-8 -*-
"""Typed wrappers for SDK responses."""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ModelInfo:
    id: str
    name: str
    family: str
    total_params_b: float
    active_params_b: float
    architecture: str
    bf16_size_gb: float

    @classmethod
    def from_dict(cls, d):
        return cls(**{k: d.get(k) for k in cls.__dataclass_fields__})
