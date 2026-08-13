# -*- coding: utf-8 -*-
"""Inference engine adapter: vllm."""
from .base import Engine, _fmt_gpus


class VllmEngine(Engine):
    name = "vllm"
    binary = "vllm"
    _supports_moe = True
    _note = 'vLLM — 生产级高吞吐，Qwen3.8/DeepSeek 官方 Recipe 首选'

    def supports_moe(self) -> bool:
        return self._supports_moe

    def build_command(self, model, quant, host="127.0.0.1", port=8000,
                      gpus=None, extra=None) -> list:
        model_path = "{model_path}".format()
        tp = " ".join(_fmt_gpus(gpus))
        extra_s = " ".join(extra or [])
        return ("python -m vllm.entrypoints.openai.api_server --model {{model_path}} --host {{host}} --port {{port}} {{tp}} {{extra}}"
                .format(model_path=model.path, host=host, port=port,
                        tp=tp, extra=extra_s)).split()
