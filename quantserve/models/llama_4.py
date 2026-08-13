# -*- coding: utf-8 -*-
"""Built-in model profile: Llama 4."""

PROFILE = {
    "id": "meta/llama-4",
    "name": "Llama 4",
    "family": "meta",
    "total_params_b": 400.0,
    "active_params_b": 16.0,
    "architecture": "moe",
    "num_experts": 128,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 800.0,
    "hf_id": "meta-llama/Llama-4",
    "modelscope_id": "meta-llama/Llama-4",
    "ollama_tag": "llama4",
    "license": "Llama License",
    "tags": ['meta', 'moe', 'llama'],
    "note": 'Meta 旗舰 MoE 开源模型。',
}
