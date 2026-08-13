# -*- coding: utf-8 -*-
"""Engine registry (auto-discovers adapters in this package)."""
from __future__ import annotations

import importlib
import pkgutil

from .base import Engine


_ENGINES = None


def _discover() -> dict:
    import quantserve.engines as _pkg
    engines = {}
    for m in pkgutil.iter_modules(_pkg.__path__):
        if m.name in ("base", "registry"):
            continue
        mod = importlib.import_module(f"quantserve.engines.{m.name}")
        for attr in dir(mod):
            if attr.endswith("Engine") and attr != "Engine":
                cls = getattr(mod, attr)
                if isinstance(cls, type) and issubclass(cls, Engine):
                    inst = cls()
                    engines[inst.name] = inst
    return engines


def list_engines() -> list:
    global _ENGINES
    if _ENGINES is None:
        _ENGINES = _discover()
    return sorted(_ENGINES.values(), key=lambda e: e.name)


def get_engine(name: str) -> Engine:
    global _ENGINES
    if _ENGINES is None:
        _ENGINES = _discover()
    if name not in _ENGINES:
        from ..exceptions import EngineError
        raise EngineError(f"unknown engine '{name}'. available: "
                          f"{', '.join(sorted(_ENGINES))}")
    return _ENGINES[name]
