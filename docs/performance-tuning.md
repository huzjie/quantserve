# 性能调优

- **吞吐**：提高 DP 副本数；开启 continuous batching（vLLM 默认）
- **延迟**：降低 TP 以减小通信；开启前缀缓存（SGLang RadixAttention）
- **显存**：`--gpu-memory-utilization 0.90`；激活检查点
- **长上下文**：vLLM `--max-model-len` 与 `--enable-chunked-prefill`
