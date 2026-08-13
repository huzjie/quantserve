# -*- coding: utf-8 -*-
"""Built-in model profile: Qwen3.5-Max."""

PROFILE = {
    "id": "qwen/qwen3.5-max",
    "name": "Qwen3.5-Max",
    "family": "qwen",
    "total_params_b": 2400.0,
    "active_params_b": 95.0,
    "architecture": "moe",
    "num_experts": 512,
    "experts_per_token": 10,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 4900.0,
    "hf_id": "Qwen/Qwen3.5-Max",
    "modelscope_id": "Qwen/Qwen3.5-Max",
    "ollama_tag": "qwen3.5-max",
    "license": "Apache-2.0",
    "tags": ['qwen', 'moe'],
    "note": '上一代旗舰。',
}
