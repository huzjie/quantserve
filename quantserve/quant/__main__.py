# -*- coding: utf-8 -*-
"""`python -m quantserve.quant <model> [--budget GB]` quick planner."""
import argparse
import json

from ..registry import get_registry
from .planner import QuantPlanner


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model")
    ap.add_argument("--budget", type=float, default=None, help="GPU memory budget (GB)")
    ap.add_argument("--target", type=float, default=None, help="target disk size (GB)")
    args = ap.parse_args()

    model = get_registry().get(args.model)
    planner = QuantPlanner()
    best, results = planner.recommend(model, budget_gb=args.budget,
                                      target_size_gb=args.target)
    print(f"model: {model.name}  (bf16 {model.bf16_size_gb} GB)")
    for r in results:
        mark = " *" if (best and r.method == best.method) else ""
        print(f"  {r.method:8s} {r.bits:>5.2f}b  disk={r.quantized_gb:>9.1f}GB  "
              f"mem={r.est_memory_gb:>9.1f}GB  ratio={r.compression_ratio:>5.2f}x{mark}")
    if best:
        print(f"\nrecommended: {best.method} ({best.note})")


if __name__ == "__main__":
    main()
