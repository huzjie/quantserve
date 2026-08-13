# 成本模型

本地部署月成本 = 硬件摊销 + 电费 + 10% 运维。

```
local = (gpu_capex / amortize_months) + power_kw * electricity * 24 * 30
cloud = in_tokens * in_price + out_tokens * out_price
```

回本点 = 本地固定月成本 / 云端每百万 token 均价（即用量达到该值时云端开始反超本地）。

示例：本地 8×H100 部署月成本约 $1600；DeepSeek V4 Pro 云端均价约 $0.44/M，则回本用量 ≈ 3600M tokens/月，超过该用量本地更划算。
