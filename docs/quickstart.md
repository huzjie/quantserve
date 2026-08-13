# 快速开始

## 1. 安装

```bash
git clone https://github.com/huzjie/quantserve.git
cd quantserve
pip install -e .
```

## 2. 生成配置

```bash
quantserve init      # 生成 config.yaml
quantserve doctor    # 环境诊断
```

## 3. 列出可部署模型

```bash
quantserve list
```

## 4. 量化规划（无需下载权重）

```bash
quantserve quantize qwen/qwen3.8-2.4t-a95b --budget 640
```

## 5. 并行部署规划

```bash
quantserve plan deepseek/deepseek-v4-pro
```

## 6. 成本对比

```bash
quantserve cost deepseek/deepseek-v4-pro --tokens 500
```

## 7. 启动服务

```bash
quantserve serve qwen/qwen3.8-27b --engine ollama
```
