# -*- coding: utf-8 -*-
"""Built-in model profile: DeepSeek-R1."""

PROFILE = {
    "id": "deepseek/deepseek-r1",
    "name": "DeepSeek-R1",
    "family": "deepseek",
    "total_params_b": 671.0,
    "active_params_b": 37.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1340.0,
    "hf_id": "deepseek-ai/DeepSeek-R1",
    "modelscope_id": "deepseek-ai/DeepSeek-R1",
    "ollama_tag": "deepseek-r1",
    "license": "MIT",
    "tags": ['deepseek', 'reasoning', 'moe'],
    "note": '推理模型里程碑。',
}
