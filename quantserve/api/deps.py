# -*- coding: utf-8 -*-
"""FastAPI dependency wiring."""
from ..config import load_config
from ..registry import get_registry


def get_config():
    return load_config()


def get_registry_dep():
    return get_registry()
