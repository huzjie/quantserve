#!/usr/bin/env bash
# 用 SGLang 部署 DeepSeek V4 Pro（官方推荐）
set -e

MODEL_DIR="${MODEL_DIR:-$HOME/.quantserve/models/deepseek-ai/DeepSeek-V4-Pro}"
TP="${TP:-8}"

python -m sglang.launch_server \
  --model-path "$MODEL_DIR" \
  --tp "$TP" \
  --mem-fraction-static 0.85 \
  --context-length 131072
