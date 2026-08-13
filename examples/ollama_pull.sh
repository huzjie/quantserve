#!/usr/bin/env bash
# 用 Ollama 本地拉取并运行小模型（CPU 也可）
set -e
ollama pull qwen3.8:27b
ollama run qwen3.8:27b
