# -*- coding: utf-8 -*-
"""Built-in model profile: Gemma 3 4B."""

PROFILE = {
    "id": "google/gemma-3-4b",
    "name": "Gemma 3 4B",
    "family": "google",
    "total_params_b": 4.0,
    "active_params_b": 4.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 8.0,
    "hf_id": "google/gemma-3-4b",
    "modelscope_id": "AI-ModelScope/gemma-3-4b",
    "ollama_tag": "gemma3:4b",
    "license": "Gemma License",
    "tags": ['google', 'dense', 'edge'],
    "note": '小模型，本地 CPU 友好。',
}
