# -*- coding: utf-8 -*-
"""Built-in model profile: DeepSeek-V3."""

PROFILE = {
    "id": "deepseek/deepseek-v3",
    "name": "DeepSeek-V3",
    "family": "deepseek",
    "total_params_b": 671.0,
    "active_params_b": 37.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1340.0,
    "hf_id": "deepseek-ai/DeepSeek-V3",
    "modelscope_id": "deepseek-ai/DeepSeek-V3",
    "ollama_tag": "deepseek-v3",
    "license": "MIT",
    "tags": ['deepseek', 'moe'],
    "note": 'MoE 开源标杆。',
}
