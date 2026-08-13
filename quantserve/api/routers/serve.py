# -*- coding: utf-8 -*-
from fastapi import APIRouter

from ...engines import list_engines, get_engine

router = APIRouter(prefix="/serve", tags=["serve"])


@router.get("/engines")
def engines():
    return {"engines": [
        {"name": e.name, "available": e.available, "supports_moe": e.supports_moe(),
         "note": e._note} for e in list_engines()
    ]}


@router.post("/command")
def command(req: dict):
    from ...registry import get_registry
    model = get_registry().get(req["model_id"])
    engine = get_engine(req.get("engine", "vllm"))
    cmd = engine.build_command(model, None, port=req.get("port", 8000),
                               gpus=req.get("gpus"))
    return {"command": " ".join(cmd), "engine": engine.name}
