# -*- coding: utf-8 -*-
"""Built-in model profile: Kimi K3."""

PROFILE = {
    "id": "moonshot/kimi-k3",
    "name": "Kimi K3",
    "family": "moonshot",
    "total_params_b": 2800.0,
    "active_params_b": 120.0,
    "architecture": "moe",
    "num_experts": 512,
    "experts_per_token": 12,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 5600.0,
    "hf_id": "moonshotai/Kimi-K3",
    "modelscope_id": "moonshotai/Kimi-K3",
    "ollama_tag": "",
    "license": "MIT",
    "tags": ['moonshot', 'moe', '2.8t'],
    "note": '2.8T 参数 MoE。',
}
