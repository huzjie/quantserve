# QuantServe — 开源大模型本地化部署与量化推理平台

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](LICENSE)
[![Zero Deps](https://img.shields.io/badge/Core-Zero%20Deps-orange)](requirements.txt)
[![Open Weights](https://img.shields.io/badge/Target-Open%20Weights-8A2BE2)]()

**把开源旗舰大模型带回家：下载 · 量化 · 并行规划 · 多引擎推理 · 成本对比，一站式搞定。**

</div>

---

## 📌 为什么是现在

2026-08-13 是「开源旗舰模型权重集中开放」的历史性一天：

- **阿里首次开源 Max 级旗舰权重** — `Qwen3.8-2.4T-A95B`：总参数 2.4 万亿、每 token 激活 95B、512 专家 MoE、原生 262K 上下文（可扩至 101 万）。
- **DeepSeek V4 Pro（0813 版）**：DeepSWE 编程 Agent 基准从 12.8 跃升至 62.7，开源编程能力直逼闭源一线。
- **NVIDIA Nemotron 3.5 Lightning**：单 GPU 可跑的 Agent 专用蒸馏模型。
- **Unsloth 动态 1-bit 分层选择性量化**：把 Qwen3.8-2.4T 的 4.9TB 权重压缩至 397GB（缩减 91%）。

开源模型正从「追赶」走向「围剿」闭源。但把一台 2.4T 的 MoE 模型真正部署到本地/私有环境，仍然门槛极高：**权重从哪下、怎么量化才不炸显存、TP/EP 怎么切、用 vLLM 还是 SGLang、本地到底比云端省多少**——这就是 QuantServe 要解决的完整链路。

## 🎯 它是什么

**QuantServe** 是一套面向开源旗舰模型（Qwen3.8 / DeepSeek V4 / Nemotron 等）的**本地化部署与量化推理平台**，覆盖从「下载权重」到「对外服务」再到「成本核算」的全流程。核心内核**零第三方依赖**（纯 Python 标准库），控制面 API 与 Web 控制台按需启用。

## 🚀 核心能力

| 能力 | 说明 |
|------|------|
| 🗂️ **模型库** | 15+ 内置开源/闭源模型 profile（Qwen3.8 / DeepSeek V4 / Nemotron / Llama 4 / Gemma 3 / Mistral / Phi-4 / Grok 4.6 等），一键检索 |
| ⬇️ **多源下载** | HuggingFace / hf-mirror.com / ModelScope 魔搭 / Ollama 四源切换 + 多线程 + 断点续传 + sha256 校验 |
| ⚖️ **量化规划** | 8 种量化方案（fp16/fp8/int8/GPTQ/AWQ/GGUF/1-bit 动态/混合）的体积、显存、压缩比、吞吐估算与预算推荐 |
| 🧩 **多引擎推理** | vLLM / SGLang / TokenSpeed / LMDeploy / Ollama / llama.cpp / TRT-LLM / Transformers 8 引擎适配，自动生成启动命令 |
| 🖥️ **MoE 并行规划** | 根据 GPU 数量/显存自动规划 TP（张量并行）/ EP（专家并行）/ DP（数据并行），直击 2.4T MoE 部署 |
| 💰 **成本对比** | 本地私有化部署 vs 云端调用 TCO 计算器（硬件摊销 + 电费 vs 按 token 计费），给出回本周期 |
| 🌐 **OpenAI 兼容网关** | 零依赖 HTTP 网关，鉴权 + /healthz + /v1/models + SSE 流式，无缝对接现有应用 |
| 🖥️ **Web 控制台** | React 控制台：模型库 / 量化估算 / 集群规划 / 成本对比 |
| 📦 **部署资产** | Docker / docker-compose / Kubernetes / Helm / GitHub Actions CI |

## ⚡ 快速开始

```bash
# 1. 安装
git clone https://github.com/huzjie/quantserve.git
cd quantserve
pip install -e .

# 2. 环境诊断
quantserve doctor

# 3. 查看可部署的模型
quantserve list

# 4. 量化规划（无需下载权重）
quantserve quantize qwen/qwen3.8-2.4t-a95b --budget 640

# 5. MoE 并行部署规划
quantserve plan deepseek/deepseek-v4-pro

# 6. 本地 vs 云端成本对比
quantserve cost deepseek/deepseek-v4-pro --tokens 500

# 7. 下载 + 部署
quantserve download qwen/qwen3.8-27b --mirror hf-mirror
quantserve serve qwen/qwen3.8-27b --engine ollama
```

## 🧭 项目结构

```
quantserve/
├── quantserve/            # Python 核心包（零强制依赖）
│   ├── cli/               #   CLI：list/download/quantize/plan/cost/serve/doctor/init
│   ├── sources/           #   多源权重 URL 适配
│   ├── models/            #   15+ 内置模型 profile
│   ├── quant/             #   8 种量化方案估算引擎
│   ├── engines/           #   8 引擎适配器
│   ├── cluster/           #   GPU 探测 + TP/EP/DP 并行规划
│   ├── cost/              #   TCO 成本计算器
│   ├── serve/             #   零依赖 OpenAI 兼容网关
│   ├── api/               #   FastAPI 控制面（可选）
│   └── sdk/               #   Python / 异步 SDK
├── web/                   # React + Vite + TypeScript 控制台
├── deploy/                # K8s + Helm
├── docs/                  # 完整中文文档
├── examples/              # 配置与脚本示例
├── Dockerfile             # 多阶段构建
└── .github/               # CI / CodeQL / dependabot
```

## 🛠️ 技术栈

- **后端**：Python 3.10+（标准库内核），FastAPI + Pydantic + Uvicorn（可选控制面）
- **前端**：React 18 + TypeScript + Vite + Recharts
- **部署**：Docker / docker-compose / Kubernetes / Helm
- **CI**：GitHub Actions（多 Python 版本 + 离线冒烟 + Ruff）

## 📖 文档

- [架构设计](docs/architecture.md)
- [快速开始](docs/quickstart.md)
- [部署指南](docs/deployment.md)
- [量化指南](docs/quantization-guide.md)
- [推理引擎](docs/engines.md)
- [成本模型](docs/cost-model.md)
- [MoE 并行](docs/moe-parallel.md)
- [API 参考](docs/api-reference.md)
- [CLI 参考](docs/cli-reference.md)

## 🤝 贡献

欢迎提交 Issue 与 PR。请先阅读 [贡献指南](.github/ISSUE_TEMPLATE/bug_report.md) 了解规范。

## 📄 许可证

[Apache-2.0](LICENSE)

---

<div align="center">

**⭐ 如果这个项目帮你把大模型带回家，点个 Star 支持一下！**

*由 AI Daily Agent 每日热点驱动 · 2026-08-13*

</div>
