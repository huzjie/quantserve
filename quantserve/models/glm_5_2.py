# -*- coding: utf-8 -*-
"""Built-in model profile: GLM-5.2."""

PROFILE = {
    "id": "zhipu/glm-5.2",
    "name": "GLM-5.2",
    "family": "zhipu",
    "total_params_b": 500.0,
    "active_params_b": 20.0,
    "architecture": "moe",
    "num_experts": 256,
    "experts_per_token": 8,
    "context_length": 131072,
    "max_context_length": 131072,
    "bf16_size_gb": 1000.0,
    "hf_id": "zai-org/GLM-5.2",
    "modelscope_id": "ZhipuAI/GLM-5.2",
    "ollama_tag": "",
    "license": "MIT",
    "tags": ['zhipu', 'moe'],
    "note": '智谱旗舰。',
}
