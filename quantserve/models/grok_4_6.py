# -*- coding: utf-8 -*-
"""Built-in model profile: Grok 4.6."""

PROFILE = {
    "id": "xai/grok-4.6",
    "name": "Grok 4.6",
    "family": "xai",
    "total_params_b": 700.0,
    "active_params_b": 36.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1400.0,
    "hf_id": "",
    "modelscope_id": "",
    "ollama_tag": "grok-4.6",
    "license": "Proprietary",
    "tags": ['xai', 'moe', 'closed'],
    "note": '闭源（同日发布），列作对比基准。',
}
