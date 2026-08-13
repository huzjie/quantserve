# -*- coding: utf-8 -*-
"""Inference engine adapter: llamacpp."""
from .base import Engine, _fmt_gpus


class LlamacppEngine(Engine):
    name = "llamacpp"
    binary = "llama-server"
    _supports_moe = False
    _note = 'llama.cpp — GGUF 单二进制，CPU/GPU 通用'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("llama-server -m {{model_path}} --host {{host}} --port {{port}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
