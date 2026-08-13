# -*- coding: utf-8 -*-
"""QuantServe — 开源大模型本地化部署与量化推理平台。

针对 2026-08 开源旗舰模型权重集中开放（Qwen3.8-2.4T-A95B / DeepSeek V4 Pro /
Nemotron 3.5 Lightning 等）提供：多源权重下载、量化压缩规划、多引擎推理服务、
MoE 并行策略规划与本地/云端成本对比。
"""

from .version import __version__

__all__ = ["__version__"]
