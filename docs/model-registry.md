# 模型库

内置 25 个模型 profile，字段：

- `id`：唯一标识
- `architecture`：`moe` / `dense`
- `total_params_b` / `active_params_b`：总参数与激活参数（十亿）
- `bf16_size_gb`：bf16 权重体积
- `hf_id` / `modelscope_id` / `ollama_tag`：多源标识

自定义模型：在 `quantserve/models/` 新增一个模块，导出 `PROFILE` dict 即可自动发现。
