# -*- coding: utf-8 -*-
"""Inference engine adapter: tokenspeed."""
from .base import Engine, _fmt_gpus


class TokenspeedEngine(Engine):
    name = "tokenspeed"
    binary = "tokenspeed"
    _supports_moe = True
    _note = 'TokenSpeed — 专为 Qwen3.8 深度优化的自托管引擎'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("tokenspeed serve --model {{model_path}} --host {{host}} --port {{port}} {{tp}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
