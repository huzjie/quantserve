# -*- coding: utf-8 -*-
"""Built-in model profile: MiniMax H3."""

PROFILE = {
    "id": "minimax/h3",
    "name": "MiniMax H3",
    "family": "minimax",
    "total_params_b": 560.0,
    "active_params_b": 22.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1120.0,
    "hf_id": "MiniMaxAI/MiniMax-H3",
    "modelscope_id": "MiniMaxAI/MiniMax-H3",
    "ollama_tag": "",
    "license": "MiniMax",
    "tags": ['minimax', 'moe'],
    "note": 'MiniMax 旗舰。',
}
