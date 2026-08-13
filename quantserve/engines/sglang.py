# -*- coding: utf-8 -*-
"""Inference engine adapter: sglang."""
from .base import Engine, _fmt_gpus


class SglangEngine(Engine):
    name = "sglang"
    binary = "python"
    _supports_moe = True
    _note = 'SGLang — RadixAttention 前缀缓存，长上下文/多轮极快'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("python -m sglang.launch_server --model-path {{model_path}} --host {{host}} --port {{port}} {{tp}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
