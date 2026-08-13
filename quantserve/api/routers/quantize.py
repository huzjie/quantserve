# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException

from ...registry import get_registry
from ...quant.planner import QuantPlanner
from ...exceptions import NotFoundError

router = APIRouter(prefix="/quantize", tags=["quantize"])


@router.get("/{model_id}")
def estimate(model_id: str, budget_gb: float = None, target_size_gb: float = None):
    try:
        model = get_registry().get(model_id)
    except NotFoundError:
        raise HTTPException(404, "model not found")
    planner = QuantPlanner()
    results = planner.plan_all(model)
    out = [r.to_dict() for r in results]
    if budget_gb or target_size_gb:
        best, _ = planner.recommend(model, budget_gb, target_size_gb)
        return {"model": model.id, "results": out,
                "recommended": best.method if best else None}
    return {"model": model.id, "results": out}
