# -*- coding: utf-8 -*-
"""TCO calculator: self-host (local open-weight) vs cloud API."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CostReport:
    model_id: str
    monthly_tokens_m: float          # millions of tokens / month
    local_monthly_usd: float
    cloud_monthly_usd: float
    breakeven_tokens_m: float        # usage at which cloud cost == local cost
    recommendation: str

    def to_dict(self) -> dict:
        return {
            "model_id": self.model_id,
            "monthly_tokens_m": self.monthly_tokens_m,
            "local_monthly_usd": round(self.local_monthly_usd, 2),
            "cloud_monthly_usd": round(self.cloud_monthly_usd, 2),
            "breakeven_tokens_m": round(self.breakeven_tokens_m, 2),
            "recommendation": self.recommendation,
        }


class CostCalculator:
    def __init__(self, pricing_cfg=None):
        self.cfg = pricing_cfg or {}

    def _gpu(self):
        return self.cfg.get("gpu_hour_usd", 2.0)

    def _power(self):
        return (self.cfg.get("power_kw", 0.5)
                * self.cfg.get("electricity_usd_kwh", 0.12)
                * 24 * 30)  # monthly power per GPU

    def _amortize(self, gpu_capex=20000.0, gpus=1):
        return gpu_capex * gpus / self.cfg.get("amortize_months", 24)

    def local_monthly(self, gpus=1, gpu_capex=20000.0) -> float:
        """Local cost = amortized hardware + power + ~10% ops."""
        base = self._amortize(gpu_capex, gpus) + self._power() * gpus
        return base * 1.10

    def cloud_monthly(self, model_id, monthly_tokens_m, ratio_in=0.8) -> float:
        from .pricing import CLOUD_PRICING
        p = CLOUD_PRICING.get(model_id)
        if not p:
            return 0.0
        in_tok = monthly_tokens_m * ratio_in
        out_tok = monthly_tokens_m * (1 - ratio_in)
        return in_tok * p["in"] + out_tok * p["out"]

    def compare(self, model_id, monthly_tokens_m, gpus=1, gpu_capex=20000.0,
                cloud_price=None) -> CostReport:
        local = self.local_monthly(gpus, gpu_capex)
        if cloud_price is not None:
            cloud = monthly_tokens_m * cloud_price
        else:
            cloud = self.cloud_monthly(model_id, monthly_tokens_m)

        # blended price per million tokens (out-weighted, typical ~80/20 in/out)
        price_per_m = cloud / monthly_tokens_m if monthly_tokens_m > 0 else 0.0
        # usage at which cloud cost catches up to the fixed local cost
        breakeven_tokens = (local / price_per_m) if price_per_m > 0 else float("inf")

        if cloud <= 0:
            rec = "该模型无公开云价，建议本地/私有化部署。"
        elif local <= cloud:
            rec = (f"本地部署每月 ${local:.0f}，云端 ${cloud:.0f}；本地每月省 "
                   f"${cloud - local:.0f}。")
        else:
            rec = (f"当前 {monthly_tokens_m:.0f}M tokens/月 用量下云端更省 "
                   f"(${cloud:.0f} vs 本地 ${local:.0f})；当用量达到约 "
                   f"{breakeven_tokens:.0f}M tokens/月 时本地部署开始回本。")
        return CostReport(model_id, monthly_tokens_m, local, cloud,
                          breakeven_tokens, rec)
