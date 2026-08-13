# -*- coding: utf-8 -*-
from .base import QuantMethod
from .planner import QuantPlanner

METHODS = {
    "none": None,
    "fp16": "fp16",
    "fp8": "fp8",
    "int8": "int8",
    "int4": "int4",
    "awq": "awq",
    "gguf": "gguf",
    "onedbit": "onedbit",
    "mixed": "mixed",
}

__all__ = ["QuantMethod", "QuantPlanner", "METHODS"]
