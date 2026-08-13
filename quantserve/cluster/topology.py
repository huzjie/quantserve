# -*- coding: utf-8 -*-
"""NVLINK / PCIe topology hints for multi-GPU deployment."""
from __future__ import annotations


class TopologyPlanner:
    def plan(self, gpus: list) -> dict:
        n = len(gpus)
        if n <= 1:
            return {"gpus": n, "interconnect": "single-gpu",
                    "recommendation": "单卡即可，无需互联优化"}
        # heuristic: 8x H100/A100/H20 通常带 NVLink；消费卡走 PCIe
        names = " ".join(g.name for g in gpus).lower()
        has_nvlink = any(k in names for k in ("h100", "a100", "h200", "b200", "h20"))
        inter = "nvlink" if has_nvlink else "pcie"
        rec = ("NVLink 全互联可用，TP=8 无损" if has_nvlink
               else "PCIe 互联，TP 建议 ≤ 4 以降低通信开销")
        return {"gpus": n, "interconnect": inter, "recommendation": rec}
