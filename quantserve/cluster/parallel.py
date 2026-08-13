# -*- coding: utf-8 -*-
"""MoE / dense parallel strategy planner (TP / EP / DP).

Deterministic, mirrors the official deployment recipes for Qwen3.8 /
DeepSeek V4 class models. Key insight: for a MoE model, ALL experts must
reside in memory (only a subset *activates* per token), so the memory
constraint is driven by TOTAL parameters, split across TP × EP.
"""
from __future__ import annotations

from math import ceil

from ..schema import PlanResult


class ParallelPlanner:
    def plan(self, model, gpus: list, bits: float = 8.0) -> PlanResult:
        n = len(gpus)
        if n == 0:
            return PlanResult(ok=False, summary="no GPU detected; "
                              "use `--cpu` engine (ollama/llamacpp).")

        mem = min(g.memory_gb for g in gpus)
        usable = mem * 0.90          # leave headroom for activations/kv-cache

        # resident parameters (GB at target precision): 1B params @ 1 byte = 1 GB
        total = model.total_params_b or model.active_params_b
        total_gb = total * (bits / 8.0)
        active_gb = (model.active_params_b or total) * (bits / 8.0)

        best = None  # (per_device_gb, -tp, tp, ep, dp, per_device)
        for tp in (1, 2, 4, 8, 16):
            if tp > n:
                continue
            for ep in (1, 2, 4, 8, 16):
                if tp * ep > n:
                    break
                if n % (tp * ep) != 0:
                    continue
                dp = n // (tp * ep)
                per_device = total_gb / (tp * ep)
                if per_device <= usable:
                    # prefer lower per-device footprint, then larger TP
                    score = (per_device, -tp)
                    if best is None or score < best[0]:
                        best = (score, tp, ep, dp, per_device)

        if best is None:
            min_gpus = max(1, ceil(total_gb / usable))
            return PlanResult(
                ok=False,
                summary=(f"{model.name}: {total:.0f}B 参数 @ {bits}bit 需 "
                         f"~{total_gb:.0f}GB 权重，至少需要 {min_gpus} 块 "
                         f"{mem:.0f}GB GPU（当前 {n} 块）。建议更低比特量化 "
                         f"或增加 GPU。"),
                details={"total_weight_gb": round(total_gb, 0),
                         "required_gpus": min_gpus, "available_gpus": n,
                         "bits": bits},
                warnings=["VRAM insufficient for resident parameters."],
            )

        _, tp, ep, dp, per_device = best
        summary = (f"{model.name}: TP={tp}, EP={ep}, DP={dp} on {n} GPUs "
                   f"({mem:.0f}GB each); 权重 {total_gb:.0f}GB, 每卡 "
                   f"~{per_device:.1f}GB, 激活 {active_gb:.0f}GB.")
        return PlanResult(
            ok=True, summary=summary,
            details={"tensor_parallel": tp, "expert_parallel": ep,
                     "data_parallel": dp, "gpu_count": n,
                     "vram_per_gpu_gb": mem,
                     "total_weight_gb": round(total_gb, 0),
                     "per_device_gb": round(per_device, 1)},
            commands=[f"--tensor-parallel-size {tp}",
                      f"--expert-parallel-size {ep}"] if ep > 1 else
                     [f"--tensor-parallel-size {tp}"],
        )
