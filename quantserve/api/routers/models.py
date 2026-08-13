# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException

from ...registry import get_registry
from ...exceptions import NotFoundError

router = APIRouter(prefix="/models", tags=["models"])


@router.get("")
def list_models(keyword: str = None):
    reg = get_registry()
    models = reg.search(keyword) if keyword else reg.list()
    return {"count": len(models), "models": [m.to_dict() for m in models]}


@router.get("/{model_id}")
def get_model(model_id: str):
    try:
        return get_registry().get(model_id).to_dict()
    except NotFoundError:
        raise HTTPException(404, f"model '{model_id}' not found")
