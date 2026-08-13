# -*- coding: utf-8 -*-
"""`quantserve doctor` — 环境诊断。"""
import shutil

from ..cluster import detect_gpus
from ..engines import list_engines


def add_parser(sub):
    p = sub.add_parser("doctor", help="诊断环境（GPU/引擎/磁盘）")
    p.set_defaults(func=run)


def _ok(b):
    return "✅" if b else "❌"


def run(args, config):
    print("QuantServe 环境诊断")
    print("-" * 40)
    gpus = detect_gpus()
    print(f"GPU: {_ok(bool(gpus))} 检测到 {len(gpus)} 块")
    for g in gpus:
        print(f"     [{g.index}] {g.name} {g.memory_gb:.0f}GB")
    print()
    print("推理引擎:")
    for e in list_engines():
        print(f"  {_ok(e.available)} {e.name:12s} {e._note}")
    print()
    for tool in ("git", "docker", "nvidia-smi", "python"):
        print(f"  {_ok(bool(shutil.which(tool)))} {tool}")
    print()
    print("目录:")
    for label, d in (("models", config.models_dir),
                     ("quantized", config.quantized_dir),
                     ("cache", config.cache_dir)):
        print(f"  {label}: {d}")
    return 0
