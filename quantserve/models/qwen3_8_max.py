# -*- coding: utf-8 -*-
"""Built-in model profile: Qwen3.8-Max."""

PROFILE = {
    "id": "qwen/qwen3.8-max",
    "name": "Qwen3.8-Max",
    "family": "qwen",
    "total_params_b": 2400.0,
    "active_params_b": 95.0,
    "architecture": "moe",
    "num_experts": 512,
    "experts_per_token": 10,
    "context_length": 262144,
    "max_context_length": 1010000,
    "bf16_size_gb": 4900.0,
    "hf_id": "Qwen/Qwen3.8-Max",
    "modelscope_id": "Qwen/Qwen3.8-Max",
    "ollama_tag": "qwen3.8-max",
    "license": "Apache-2.0",
    "tags": ['qwen', 'moe', 'cloud'],
    "note": '云端版，基于 A95B 开放权重 + 生产增强。',
}
