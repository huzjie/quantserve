# -*- coding: utf-8 -*-
from .base import Source, FileSpec


class OllamaSource(Source):
    """Ollama registry — single GGUF blob, simplest path for local CPU/GPU."""

    name = "ollama"

    def files(self, model) -> list:
        tag = model.ollama_tag or model.id.split("/")[-1]
        return [FileSpec(f"https://ollama.com/library/{tag}", f"{tag}.gguf")]
