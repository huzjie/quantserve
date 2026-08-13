# -*- coding: utf-8 -*-
"""Built-in model profile: Mixtral 8x7B."""

PROFILE = {
    "id": "mistral/mixtral-8x7b",
    "name": "Mixtral 8x7B",
    "family": "mistral",
    "total_params_b": 47.0,
    "active_params_b": 13.0,
    "architecture": "moe",
    "num_experts": 8,
    "experts_per_token": 2,
    "context_length": 32768,
    "max_context_length": 32768,
    "bf16_size_gb": 94.0,
    "hf_id": "mistralai/Mixtral-8x7B",
    "modelscope_id": "mistralai/Mixtral-8x7B",
    "ollama_tag": "mixtral",
    "license": "Apache-2.0",
    "tags": ['mistral', 'moe', 'small'],
    "note": '经典 8 专家小 MoE。',
}
