# -*- coding: utf-8 -*-
"""Built-in model profile: Gemma 3 27B."""

PROFILE = {
    "id": "google/gemma-3-27b",
    "name": "Gemma 3 27B",
    "family": "google",
    "total_params_b": 27.0,
    "active_params_b": 27.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 54.0,
    "hf_id": "google/gemma-3-27b",
    "modelscope_id": "AI-ModelScope/gemma-3-27b",
    "ollama_tag": "gemma3:27b",
    "license": "Gemma License",
    "tags": ['google', 'dense', 'multimodal'],
    "note": 'Google 开放模型，多模态。',
}
