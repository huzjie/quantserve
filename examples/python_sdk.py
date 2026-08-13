"""QuantServe Python SDK 使用示例。"""
from quantserve.sdk import QuantServeClient

client = QuantServeClient("http://127.0.0.1:8000")

# 1. 健康检查
print(client.health())

# 2. 列出模型
print(client.list_models(keyword="qwen"))

# 3. 量化估算（Qwen3.8-2.4T 在 80GB×8 预算下）
est = client.estimate_quant("qwen/qwen3.8-2.4t-a95b", budget_gb=640)
print(est["recommended"])

# 4. 并行规划
plan = client.plan("qwen/qwen3.8-2.4t-a95b", bits=8)
print(plan["plan"]["summary"])

# 5. 成本对比
cost = client.compare_cost("deepseek/deepseek-v4-pro", monthly_tokens_m=500)
print(cost)
