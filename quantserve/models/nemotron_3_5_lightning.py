# -*- coding: utf-8 -*-
"""Built-in model profile: Nemotron 3.5 Lightning."""

PROFILE = {
    "id": "nvidia/nemotron-3.5-lightning",
    "name": "Nemotron 3.5 Lightning",
    "family": "nvidia",
    "total_params_b": 12.0,
    "active_params_b": 12.0,
    "architecture": "dense",
    "num_experts": 0,
    "experts_per_token": 0,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 24.0,
    "hf_id": "nvidia/Nemotron-3.5-Lightning",
    "modelscope_id": "AI-ModelScope/Nemotron-3.5-Lightning",
    "ollama_tag": "nemotron-3.5-lightning",
    "license": "NVIDIA Open",
    "tags": ['nvidia', 'dense', 'agent', 'edge'],
    "note": '单 GPU 可跑的 Agent 专用蒸馏模型。',
}
