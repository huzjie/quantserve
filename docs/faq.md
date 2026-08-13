# FAQ

**Q: 我的机器没有 GPU 能跑吗？**
A: 可以。用 Ollama / llama.cpp 引擎跑 GGUF 量化小模型（如 Gemma 3 4B、Qwen3.8-27B）。

**Q: 下载太慢？**
A: 设置 `--mirror hf-mirror`（国内）或 `--mirror modelscope`（Qwen 系列首发）。

**Q: 如何部署 2.4T 的 Qwen3.8？**
A: `quantserve plan qwen/qwen3.8-2.4t-a95b` 查看并行建议，通常需 8×H100(80GB)+。

**Q: 是否强制第三方依赖？**
A: 否。核心 CLI/规划/成本/下载均为标准库实现；仅控制面 API 可选装 FastAPI。
