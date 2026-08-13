# API 参考

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /healthz | 健康检查 |
| GET | /models | 模型列表 |
| GET | /models/{id} | 模型详情 |
| GET | /quantize/{id} | 量化估算 |
| GET | /serve/engines | 引擎列表 |
| GET | /cluster/gpus | GPU 列表 |
| POST | /cluster/plan | 并行规划 |
| POST | /cost/compare | 成本对比 |
| POST | /jobs/download | 发起下载任务 |
| GET | /jobs/{id} | 任务状态 |
