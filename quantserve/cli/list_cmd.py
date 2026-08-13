# -*- coding: utf-8 -*-
"""`quantserve list [keyword]`"""
from ..registry import get_registry


def add_parser(sub):
    p = sub.add_parser("list", help="列出内置模型")
    p.add_argument("keyword", nargs="?", help="模糊搜索关键字")
    p.set_defaults(func=run)


def run(args, config):
    reg = get_registry()
    models = reg.search(args.keyword) if args.keyword else reg.list()
    if not models:
        print("(无匹配模型)")
        return 1
    print(f"{'ID':40s} {'NAME':28s} {'ARCH':7s} {'TOTAL':>8s} {'ACTIVE':>8s} {'SIZE':>8s}")
    for m in models:
        size = f"{m.bf16_size_gb:.0f}GB" if m.bf16_size_gb else "-"
        total = f"{m.total_params_b:.0f}B" if m.total_params_b else "-"
        active = f"{m.active_params_b:.0f}B" if m.active_params_b else "-"
        print(f"{m.id:40s} {m.name:28s} {m.architecture:7s} {total:>8s} "
              f"{active:>8s} {size:>8s}")
    print(f"\n共 {len(models)} 个模型")
    return 0
