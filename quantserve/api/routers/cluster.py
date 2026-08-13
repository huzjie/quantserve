# -*- coding: utf-8 -*-
from fastapi import APIRouter

from ...cluster import detect_gpus, ParallelPlanner, TopologyPlanner
from ...registry import get_registry

router = APIRouter(prefix="/cluster", tags=["cluster"])


@router.get("/gpus")
def gpus():
    return {"gpus": [g.to_dict() for g in detect_gpus()]}


@router.post("/plan")
def plan(req: dict):
    model = get_registry().get(req["model_id"])
    gpus = detect_gpus()
    if not gpus:
        return {"ok": False, "summary": "no GPU detected"}
    res = ParallelPlanner().plan(model, gpus, bits=req.get("bits", 8.0))
    topo = TopologyPlanner().plan(gpus)
    return {"plan": res.to_dict(), "topology": topo}
