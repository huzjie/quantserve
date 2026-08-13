# -*- coding: utf-8 -*-
"""Configuration loading with YAML (PyYAML preferred) + mini-YAML fallback."""
from __future__ import annotations

import json
import os
from pathlib import Path

from ._yaml import load as mini_yaml_load
from .exceptions import ConfigError

DEFAULTS = {
    "home": "~/.quantserve",
    "models_dir": "~/.quantserve/models",
    "quantized_dir": "~/.quantserve/quantized",
    "cache_dir": "~/.quantserve/cache",
    "mirror": "auto",           # auto | hf-mirror | modelscope | huggingface
    "max_concurrency": 4,
    "chunk_size_mb": 64,
    "verify_checksum": True,
    "default_engine": "vllm",
    "api": {"host": "127.0.0.1", "port": 8000, "auth_token": None},
    "pricing": {
        "gpu_hour_usd": 2.0,
        "power_kw": 0.5,
        "electricity_usd_kwh": 0.12,
        "amortize_months": 24,
    },
}


def _try_pyyaml(path: Path):
    try:
        import yaml  # noqa
    except Exception:
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _deep_merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def _expand(path: str) -> str:
    return os.path.expanduser(os.path.expandvars(path))


class Config:
    def __init__(self, data: dict | None = None):
        self._data = _deep_merge(DEFAULTS, data or {})

    def __getitem__(self, key):
        return self._data[key]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def as_dict(self):
        return self._data

    # -- convenience paths ------------------------------------------------
    @property
    def models_dir(self) -> str:
        return _expand(self._data["models_dir"])

    @property
    def quantized_dir(self) -> str:
        return _expand(self._data["quantized_dir"])

    @property
    def cache_dir(self) -> str:
        return _expand(self._data["cache_dir"])

    def ensure_dirs(self):
        for d in (self.models_dir, self.quantized_dir, self.cache_dir):
            Path(d).mkdir(parents=True, exist_ok=True)


def load_config(path: str | None = None) -> Config:
    """Load config from an explicit path, or auto-discover, else defaults."""
    candidates = []
    if path:
        candidates.append(Path(path))
    candidates += [
        Path.cwd() / "quantserve.yaml",
        Path.cwd() / "config.yaml",
        Path.home() / ".config" / "quantserve" / "config.yaml",
        Path.home() / ".quantserve" / "config.yaml",
    ]
    for cand in candidates:
        if cand.exists():
            data = _try_pyyaml(cand)
            if data is None:
                with open(cand, "r", encoding="utf-8") as f:
                    data = mini_yaml_load(f.read())
            if not isinstance(data, dict):
                raise ConfigError(f"config {cand} did not parse to a mapping")
            return Config(data)
    return Config()


def default_config_text() -> str:
    return """# QuantServe 配置示例 — 复制为 config.yaml 后按需修改
home: ~/.quantserve
models_dir: ~/.quantserve/models
quantized_dir: ~/.quantserve/quantized
cache_dir: ~/.quantserve/cache

# 权重下载镜像: auto | hf-mirror | modelscope | huggingface
mirror: auto

max_concurrency: 4
chunk_size_mb: 64
verify_checksum: true
default_engine: vllm

api:
  host: 127.0.0.1
  port: 8000
  auth_token: null

pricing:
  gpu_hour_usd: 2.0
  power_kw: 0.5
  electricity_usd_kwh: 0.12
  amortize_months: 24
"""
