# -*- coding: utf-8 -*-
"""Built-in model profile: Qwen3.8-2.4T-A95B."""

PROFILE = {
    "id": "qwen/qwen3.8-2.4t-a95b",
    "name": "Qwen3.8-2.4T-A95B",
    "family": "qwen",
    "total_params_b": 2400.0,
    "active_params_b": 95.0,
    "architecture": "moe",
    "num_experts": 512,
    "experts_per_token": 10,
    "context_length": 262144,
    "max_context_length": 1010000,
    "bf16_size_gb": 4900.0,
    "hf_id": "Qwen/Qwen3.8-2.4T-A95B",
    "modelscope_id": "Qwen/Qwen3.8-2.4T-A95B",
    "ollama_tag": "qwen3.8:2.4t",
    "license": "Apache-2.0",
    "tags": ['qwen', 'moe', 'flagship', 'open-weights', '2.4t'],
    "note": '阿里首次开源 Max 级旗舰权重（2026-08-13），总参数 2.4T、每 token 激活 95B，MoE 512 专家。',
}
