# 多节点部署

跨节点部署大模型需要高速互联（InfiniBand / 400G RoCE）。

```bash
# 每节点 8×H100，2 节点 = 16 卡
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen3.8-2.4T-A95B \
  --tensor-parallel-size 16 \
  --max-model-len 131072
```
