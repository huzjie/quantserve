# -*- coding: utf-8 -*-
"""Simple placement scheduler: assign models to GPU nodes by VRAM."""
from __future__ import annotations


def place(models, gpus):
    """First-fit-decreasing placement by active-param memory footprint."""
    slots = [{"gpu": g, "used": 0.0, "models": []} for g in gpus]
    items = sorted(models, key=lambda m: -m.active_params_b)
    for m in items:
        need = m.active_params_b * 1e9 / 1e9 * 1.25  # rough GB
        placed = False
        for s in sorted(slots, key=lambda s: s["used"]):
            if s["gpu"].memory_gb - s["used"] >= need:
                s["used"] += need
                s["models"].append(m.id)
                placed = True
                break
        if not placed:
            return {"ok": False, "reason": f"{m.id} 无法放置"}
    return {
        "ok": True,
        "assignments": [
            {"gpu_index": s["gpu"].index, "used_gb": round(s["used"], 1),
             "models": s["models"]} for s in slots if s["models"]
        ],
    }
