# -*- coding: utf-8 -*-
"""Inference engine adapter: transformers."""
from .base import Engine, _fmt_gpus


class TransformersEngine(Engine):
    name = "transformers"
    binary = "python"
    _supports_moe = True
    _note = 'Transformers — HF 原生 pipeline，调试/研究'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("python -m quantserve.engines.transformers_serve --model {{model_path}} --host {{host}} --port {{port}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
