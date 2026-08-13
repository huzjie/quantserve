# -*- coding: utf-8 -*-
"""Built-in model profile: DeepSeek V4."""

PROFILE = {
    "id": "deepseek/deepseek-v4",
    "name": "DeepSeek V4",
    "family": "deepseek",
    "total_params_b": 685.0,
    "active_params_b": 37.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1370.0,
    "hf_id": "deepseek-ai/DeepSeek-V4",
    "modelscope_id": "deepseek-ai/DeepSeek-V4",
    "ollama_tag": "deepseek-v4",
    "license": "MIT",
    "tags": ['deepseek', 'moe', 'reasoning'],
    "note": '满血版 V4 基座。',
}
