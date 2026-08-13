# -*- coding: utf-8 -*-
from .base import Source, FileSpec


class HuggingFaceSource(Source):
    name = "huggingface"

    def files(self, model) -> list:
        base = f"https://huggingface.co/{model.hf_id or model.id}/resolve/main"
        # A realistic open-weight model ships multiple shards + config + tokenizer.
        specs = [
            FileSpec(f"{base}/config.json", "config.json"),
            FileSpec(f"{base}/tokenizer.json", "tokenizer.json"),
            FileSpec(f"{base}/tokenizer_config.json", "tokenizer_config.json"),
        ]
        # shard count scales with model size (~10GB per shard for bf16)
        shards = max(1, int(model.bf16_size_gb / 10) + 1)
        for i in range(1, shards + 1):
            specs.append(FileSpec(
                f"{base}/model-{i:05d}-of-{shards:05d}.safetensors",
                f"model-{i:05d}-of-{shards:05d}.safetensors",
            ))
        return specs
