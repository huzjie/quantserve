# QuantServe 架构

## 总体分层

```
┌─────────────────────────────────────────────────┐
│  CLI (quantserve)  │  Web 控制台  │  Python SDK   │
├─────────────────────────────────────────────────┤
│  FastAPI 控制面 (api/)  +  stdlib 网关 (serve/)  │
├─────────────────────────────────────────────────┤
│  registry 模型库 / sources 多源 / downloader 下载 │
│  quant 量化规划  │  engines 引擎适配  │  cluster 并行│
│  cost 成本对比   │  checksum 校验                │
├─────────────────────────────────────────────────┤
│  Python 标准库内核（零强制第三方依赖）             │
└─────────────────────────────────────────────────┘
```

## 核心模块

| 模块 | 职责 |
|------|------|
| `registry.py` | 内置模型 profile 自动发现与检索 |
| `sources/` | HuggingFace / hf-mirror / ModelScope / Ollama 多源 URL 构造 |
| `downloader.py` | 多线程 + 断点续传 + 校验和 |
| `quant/` | 8 种量化方案的大小/显存/吞吐估算与推荐 |
| `engines/` | vLLM / SGLang / TokenSpeed / Ollama / llama.cpp / TRT-LLM / LMDeploy / Transformers 适配 |
| `cluster/` | GPU 探测 + TP/EP/DP 并行规划 + 拓扑 |
| `cost/` | 本地 vs 云端 TCO 对比 |
| `serve/` | 零依赖 OpenAI 兼容网关 + 鉴权 + SSE |
