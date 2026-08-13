# -*- coding: utf-8 -*-
"""Inference engine adapter: ollama."""
from .base import Engine, _fmt_gpus


class OllamaEngine(Engine):
    name = "ollama"
    binary = "ollama"
    _supports_moe = True
    _note = 'Ollama — 零配置本地运行，CPU/Apple Silicon 友好'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("ollama serve --host {{host}} --port {{port}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
