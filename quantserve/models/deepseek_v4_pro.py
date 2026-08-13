# -*- coding: utf-8 -*-
"""Built-in model profile: DeepSeek V4 Pro (0813)."""

PROFILE = {
    "id": "deepseek/deepseek-v4-pro",
    "name": "DeepSeek V4 Pro (0813)",
    "family": "deepseek",
    "total_params_b": 685.0,
    "active_params_b": 37.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1370.0,
    "hf_id": "deepseek-ai/DeepSeek-V4-Pro",
    "modelscope_id": "deepseek-ai/DeepSeek-V4-Pro",
    "ollama_tag": "deepseek-v4-pro",
    "license": "MIT",
    "tags": ['deepseek', 'moe', 'coding-agent'],
    "note": '0813 版本：DeepSWE 12.8→62.7，编程 Agent 能力跃升。',
}
