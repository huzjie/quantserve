# -*- coding: utf-8 -*-
"""GPU inventory via nvidia-smi (subprocess)."""
from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass, asdict


@dataclass
class GPU:
    index: int = 0
    name: str = ""
    memory_mb: int = 0
    compute_capability: str = ""

    @property
    def memory_gb(self) -> float:
        return self.memory_mb / 1024.0

    def to_dict(self) -> dict:
        return asdict(self)


def detect_gpus() -> list:
    """Return a list of GPUs, or [] if none / nvidia-smi missing."""
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return []
    try:
        out = subprocess.run(
            [nvidia_smi, "--query-gpu=index,name,memory.total,compute_cap",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10,
        )
    except Exception:
        return []
    if out.returncode != 0:
        return []
    gpus = []
    for line in out.stdout.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            continue
        gpus.append(GPU(index=int(parts[0]), name=parts[1],
                        memory_mb=int(parts[2]), compute_capability=parts[3]))
    return gpus


def detect_gpus_json() -> str:
    return json.dumps([g.to_dict() for g in detect_gpus()])
