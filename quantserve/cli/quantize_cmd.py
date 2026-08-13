# -*- coding: utf-8 -*-
"""`quantserve quantize <model> [--method ...] [--budget GB] [--target GB]`"""
from ..registry import get_registry
from ..quant.planner import QuantPlanner


def add_parser(sub):
    p = sub.add_parser("quantize", help="量化规划与估算")
    p.add_argument("model", help="模型 ID")
    p.add_argument("--method", default=None,
                   help="fp16|fp8|int8|int4|awq|gguf|onedbit|mixed")
    p.add_argument("--budget", type=float, default=None, help="显存预算(GB)")
    p.add_argument("--target", type=float, default=None, help="目标磁盘(GB)")
    p.set_defaults(func=run)


def run(args, config):
    model = get_registry().get(args.model)
    planner = QuantPlanner()
    results = planner.plan_all(model)
    print(f"model: {model.name}  (bf16 {model.bf16_size_gb}GB)")
    print(f"{'method':8s} {'bits':>6s} {'disk':>9s} {'mem':>9s} {'ratio':>6s}")
    for r in results:
        print(f"{r.method:8s} {r.bits:>6.1f} {r.quantized_gb:>8.1f}GB "
              f"{r.est_memory_gb:>8.1f}GB {r.compression_ratio:>6.2f}x")
    if args.budget or args.target:
        best, _ = planner.recommend(model, budget_gb=args.budget,
                                    target_size_gb=args.target)
        if best:
            print(f"\n✅ 推荐方案: {best.note}")
        else:
            print("\n❌ 无方案满足预算约束，请放宽预算或换更小模型")
            return 1
    return 0
