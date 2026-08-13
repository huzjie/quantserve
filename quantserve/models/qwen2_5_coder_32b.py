# -*- coding: utf-8 -*-
"""Built-in model profile: Qwen2.5-Coder-32B."""

PROFILE = {
    "id": "alibaba/qwen2.5-coder-32b",
    "name": "Qwen2.5-Coder-32B",
    "family": "qwen",
    "total_params_b": 32.0,
    "active_params_b": 32.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 64.0,
    "hf_id": "Qwen/Qwen2.5-Coder-32B",
    "modelscope_id": "Qwen/Qwen2.5-Coder-32B",
    "ollama_tag": "qwen2.5-coder:32b",
    "license": "Apache-2.0",
    "tags": ['qwen', 'code', 'dense'],
    "note": '编程专用密集模型。',
}
