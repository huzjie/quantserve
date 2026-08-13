# -*- coding: utf-8 -*-
"""`quantserve plan <model>` — GPU 并行策略规划。"""
import json

from ..cluster import detect_gpus, ParallelPlanner, TopologyPlanner
from ..registry import get_registry


def add_parser(sub):
    p = sub.add_parser("plan", help="规划 MoE/密集模型的并行部署策略")
    p.add_argument("model", help="模型 ID")
    p.add_argument("--bits", type=float, default=8.0, help="量化比特")
    p.add_argument("--json", action="store_true", dest="as_json")
    p.set_defaults(func=run)


def run(args, config):
    model = get_registry().get(args.model)
    gpus = detect_gpus()
    if not gpus:
        print("❌ 未检测到 GPU（nvidia-smi 不可用）。可改用 CPU 引擎：")
        print("   quantserve serve %s --engine ollama" % model.id)
        return 1
    print(f"检测到 {len(gpus)} 块 GPU：")
    for g in gpus:
        print(f"  [{g.index}] {g.name}  {g.memory_gb:.0f}GB  CC={g.compute_capability}")
    planner = ParallelPlanner()
    res = planner.plan(model, gpus, bits=args.bits)
    topo = TopologyPlanner().plan(gpus)
    print("\n" + res.summary)
    print("互联拓扑: " + topo["recommendation"])
    if args.as_json:
        print(json.dumps({"plan": res.to_dict(), "topology": topo},
                         ensure_ascii=False, indent=2))
    return 0 if res.ok else 1
