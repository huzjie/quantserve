# -*- coding: utf-8 -*-
from .base import Source
from .huggingface import HuggingFaceSource
from .hf_mirror import HfMirrorSource
from .modelscope import ModelScopeSource
from .ollama import OllamaSource

SOURCES = {
    "huggingface": HuggingFaceSource,
    "hf-mirror": HfMirrorSource,
    "modelscope": ModelScopeSource,
    "ollama": OllamaSource,
}

__all__ = ["Source", "SOURCES", "HuggingFaceSource", "HfMirrorSource",
           "ModelScopeSource", "OllamaSource"]
