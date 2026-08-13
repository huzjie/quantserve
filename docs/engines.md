# 推理引擎

| 引擎 | MoE | 特点 |
|------|-----|------|
| vLLM | ✅ | 生产级高吞吐，官方 Recipe 首选 |
| SGLang | ✅ | RadixAttention 前缀缓存 |
| TokenSpeed | ✅ | Qwen3.8 深度优化 |
| LMDeploy | ✅ | 国产卡兼容好 |
| Ollama | ✅ | 零配置本地运行 |
| llama.cpp | ❌ | GGUF 单二进制 CPU/GPU |
| TRT-LLM | ❌ | NVIDIA 极致优化 |
| Transformers | ✅ | 研究/调试 |
