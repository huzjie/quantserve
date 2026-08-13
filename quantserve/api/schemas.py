# -*- coding: utf-8 -*-
"""Pydantic request/response schemas."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class DownloadRequest(BaseModel):
    model_id: str
    mirror: str = "auto"


class QuantizeRequest(BaseModel):
    model_id: str
    method: Optional[str] = None
    budget_gb: Optional[float] = None
    target_size_gb: Optional[float] = None


class PlanRequest(BaseModel):
    model_id: str
    bits: float = 8.0


class CostRequest(BaseModel):
    model_id: str
    monthly_tokens_m: float = 100.0
    gpus: int = 1
    gpu_capex: float = 20000.0


class ServeRequest(BaseModel):
    model_id: str
    engine: str = "vllm"
    port: int = 8000
    gpus: Optional[int] = None
