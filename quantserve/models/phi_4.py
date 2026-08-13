# -*- coding: utf-8 -*-
"""Built-in model profile: Phi-4."""

PROFILE = {
    "id": "microsoft/phi-4",
    "name": "Phi-4",
    "family": "microsoft",
    "total_params_b": 14.0,
    "active_params_b": 14.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 16384,
    "max_context_length": 16384,
    "bf16_size_gb": 28.0,
    "hf_id": "microsoft/phi-4",
    "modelscope_id": "AI-ModelScope/phi-4",
    "ollama_tag": "phi4",
    "license": "MIT",
    "tags": ['microsoft', 'dense', 'reasoning'],
    "note": '小参数强推理。',
}
