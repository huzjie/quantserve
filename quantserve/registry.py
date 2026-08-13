# -*- coding: utf-8 -*-
"""Model registry: built-in profiles + optional local manifest."""
from __future__ import annotations

import json
from pathlib import Path

from .exceptions import NotFoundError
from .schema import ModelProfile


def _builtin_profiles():
    import pkgutil
    import importlib
    from . import models as models_pkg

    profiles = {}
    for m in pkgutil.iter_modules(models_pkg.__path__):
        if m.name.startswith("_"):
            continue
        mod = importlib.import_module(f"quantserve.models.{m.name}")
        prof = getattr(mod, "PROFILE", None)
        if prof:
            p = ModelProfile(**prof) if isinstance(prof, dict) else prof
            profiles[p.id] = p
    return profiles


class Registry:
    def __init__(self):
        self._builtin = _builtin_profiles()

    def list(self) -> list:
        return sorted(self._builtin.values(), key=lambda p: p.id)

    def get(self, model_id: str) -> ModelProfile:
        if model_id in self._builtin:
            return self._builtin[model_id]
        # fuzzy: match by name / hf_id / modelscope_id / tag
        for p in self._builtin.values():
            if model_id in (p.name, p.hf_id, p.modelscope_id, p.ollama_tag):
                return p
        raise NotFoundError(f"unknown model '{model_id}'. run `quantserve list`.")

    def search(self, keyword: str) -> list:
        kw = keyword.lower()
        return [p for p in self._builtin.values()
                if kw in p.id.lower() or kw in p.name.lower()
                or kw in p.family.lower() or any(kw in t for t in p.tags)]


_registry = None


def get_registry() -> Registry:
    global _registry
    if _registry is None:
        _registry = Registry()
    return _registry
