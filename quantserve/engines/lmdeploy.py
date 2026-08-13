# -*- coding: utf-8 -*-
"""Inference engine adapter: lmdeploy."""
from .base import Engine, _fmt_gpus


class LmdeployEngine(Engine):
    name = "lmdeploy"
    binary = "lmdeploy"
    _supports_moe = True
    _note = 'LMDeploy — TurboMind 引擎，国产卡兼容好'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("lmdeploy serve api_server {{model_path}} --server-port {{port}} {{tp}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
