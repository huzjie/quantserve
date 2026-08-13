# -*- coding: utf-8 -*-
"""Built-in model profile: Qwen2.5-72B-Instruct."""

PROFILE = {
    "id": "qwen/qwen2.5-72b",
    "name": "Qwen2.5-72B-Instruct",
    "family": "qwen",
    "total_params_b": 72.0,
    "active_params_b": 72.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 144.0,
    "hf_id": "Qwen/Qwen2.5-72B-Instruct",
    "modelscope_id": "Qwen/Qwen2.5-72B-Instruct",
    "ollama_tag": "qwen2.5:72b",
    "license": "Apache-2.0",
    "tags": ['qwen', 'dense'],
    "note": '经典 72B 密集模型。',
}
