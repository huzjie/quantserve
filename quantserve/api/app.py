# -*- coding: utf-8 -*-
"""FastAPI application factory (optional dependency)."""
from __future__ import annotations


def create_app():
    try:
        from fastapi import FastAPI
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "FastAPI not installed. Run: pip install quantserve[api]"
        ) from e

    app = FastAPI(
        title="QuantServe API",
        version="0.1.0",
        description="开源大模型本地化部署与量化推理平台 — 控制面 API",
    )

    from .routers import health, models, jobs, quantize, serve, cluster, cost
    for r in (health, models, jobs, quantize, serve, cluster, cost):
        app.include_router(r.router)

    return app


app = None


def get_app():
    global app
    if app is None:
        app = create_app()
    return app
