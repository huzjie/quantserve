# -*- coding: utf-8 -*-
"""`quantserve cost <model> --tokens N` — 本地 vs 云端成本对比。"""
from ..cost import CostCalculator
from ..registry import get_registry


def add_parser(sub):
    p = sub.add_parser("cost", help="本地部署 vs 云端调用成本对比")
    p.add_argument("model", help="模型 ID")
    p.add_argument("--tokens", type=float, default=100.0,
                   help="月 token 用量（百万）")
    p.add_argument("--gpus", type=int, default=1)
    p.add_argument("--gpu-capex", type=float, default=20000.0)
    p.set_defaults(func=run)


def run(args, config):
    model = get_registry().get(args.model)
    calc = CostCalculator(config.get("pricing", {}))
    r = calc.compare(model.id, args.tokens, args.gpus, args.gpu_capex)
    print(f"模型: {model.name}")
    print(f"月用量: {r.monthly_tokens_m:.0f}M tokens")
    print(f"本地部署: ${r.local_monthly_usd:.0f}/月")
    print(f"云端调用: ${r.cloud_monthly_usd:.0f}/月")
    print(f"回本用量: {r.breakeven_tokens_m:.0f}M tokens/月" if r.breakeven_tokens_m < 1e9 else "云端无价/本地唯一")
    print(f"结论: {r.recommendation}")
    return 0
