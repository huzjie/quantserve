# -*- coding: utf-8 -*-
"""Cloud inference pricing (USD per million tokens) — snapshot 2026-08.

Open-weight models also carry a self-host cost computed by the calculator.
"""
CLOUD_PRICING = {
    "qwen/qwen3.8-max": {"in": 0.28, "out": 0.84, "provider": "Alibaba"},
    "deepseek/deepseek-v4-pro": {"in": 0.27, "out": 1.10, "provider": "DeepSeek"},
    "deepseek/deepseek-v4": {"in": 0.27, "out": 1.10, "provider": "DeepSeek"},
    "xai/grok-4.6": {"in": 2.00, "out": 6.00, "provider": "xAI"},
    "anthropic/claude-sonnet": {"in": 3.00, "out": 15.00, "provider": "Anthropic"},
    "openai/gpt-5.6-sol": {"in": 3.00, "out": 15.00, "provider": "OpenAI"},
}
