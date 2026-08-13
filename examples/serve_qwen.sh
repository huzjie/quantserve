#!/usr/bin/env bash
# 用 vLLM 部署 Qwen3.8-2.4T-A95B（官方 Recipe：8×H100 或更多）
set -e

MODEL_DIR="${MODEL_DIR:-$HOME/.quantserve/models/Qwen/Qwen3.8-2.4T-A95B}"
TP="${TP:-8}"

python -m vllm.entrypoints.openai.api_server \
  --model "$MODEL_DIR" \
  --tensor-parallel-size "$TP" \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --served-model-name qwen3.8-2.4t-a95b
