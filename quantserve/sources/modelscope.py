# -*- coding: utf-8 -*-
from .base import Source, FileSpec


class ModelScopeSource(Source):
    """魔搭 ModelScope — 阿里官方渠道，Qwen 系列首发。"""

    name = "modelscope"

    def files(self, model) -> list:
        base = f"https://modelscope.cn/models/{model.modelscope_id or model.id}/resolve/master"
        specs = [
            FileSpec(f"{base}/config.json", "config.json"),
            FileSpec(f"{base}/tokenizer.json", "tokenizer.json"),
        ]
        shards = max(1, int(model.bf16_size_gb / 10) + 1)
        for i in range(1, shards + 1):
            specs.append(FileSpec(
                f"{base}/model-{i:05d}-of-{shards:05d}.safetensors",
                f"model-{i:05d}-of-{shards:05d}.safetensors",
            ))
        return specs
