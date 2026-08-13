# -*- coding: utf-8 -*-
from fastapi import APIRouter

from ...cost import CostCalculator
from ...config import load_config
from ...registry import get_registry

router = APIRouter(prefix="/cost", tags=["cost"])


@router.post("/compare")
def compare(req: dict):
    model = get_registry().get(req["model_id"])
    calc = CostCalculator(load_config().get("pricing", {}))
    r = calc.compare(model.id, req.get("monthly_tokens_m", 100.0),
                     req.get("gpus", 1), req.get("gpu_capex", 20000.0))
    return r.to_dict()
