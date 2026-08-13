# 故障排查

| 症状 | 原因 | 解决 |
|------|------|------|
| `nvidia-smi` 不可用 | 未装驱动 | 安装驱动 / 改用 CPU 引擎 |
| 下载超时 | 网络受限 | 切换 `--mirror` |
| 显存不足 | 模型过大 | 用 `quantserve quantize --budget` 选低比特 |
| 引擎未找到 | 未安装 | `pip install vllm` 或换 `--engine ollama` |
