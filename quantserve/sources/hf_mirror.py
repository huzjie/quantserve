# -*- coding: utf-8 -*-
from .base import Source, FileSpec


class HfMirrorSource(Source):
    """hf-mirror.com — 中国大陆镜像，速度更快。"""

    name = "hf-mirror"

    def files(self, model) -> list:
        base = f"https://hf-mirror.com/{model.hf_id or model.id}/resolve/main"
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
