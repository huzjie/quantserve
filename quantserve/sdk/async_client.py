# -*- coding: utf-8 -*-
"""Async client built on asyncio + urllib (thread executor)."""
from __future__ import annotations

import asyncio

from .client import QuantServeClient


class AsyncQuantServeClient(QuantServeClient):
    async def _call(self, fn, *args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: fn(*args, **kwargs))

    async def health(self):
        return await self._call(super().health)

    async def list_models(self, keyword=None):
        return await self._call(super().list_models, keyword)

    async def estimate_quant(self, model_id, **kw):
        return await self._call(super().estimate_quant, model_id, **kw)
