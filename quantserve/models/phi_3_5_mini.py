# -*- coding: utf-8 -*-
"""Built-in model profile: Phi-3.5 Mini."""

PROFILE = {
    "id": "microsoft/phi-3.5-mini",
    "name": "Phi-3.5 Mini",
    "family": "microsoft",
    "total_params_b": 3.8,
    "active_params_b": 3.8,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 7.6,
    "hf_id": "microsoft/Phi-3.5-mini-instruct",
    "modelscope_id": "AI-ModelScope/Phi-3.5-mini",
    "ollama_tag": "phi3.5",
    "license": "MIT",
    "tags": ['microsoft', 'dense', 'edge'],
    "note": '极小模型，边缘友好。',
}
