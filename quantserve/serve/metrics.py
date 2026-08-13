# -*- coding: utf-8 -*-
"""In-process metrics registry (Prometheus text format)."""
from __future__ import annotations

import threading
import time


class Metrics:
    def __init__(self):
        self._lock = threading.Lock()
        self._counters = {}
        self._gauges = {}
        self._hist = {}

    def inc(self, name, n=1):
        with self._lock:
            self._counters[name] = self._counters.get(name, 0) + n

    def set(self, name, v):
        with self._lock:
            self._gauges[name] = v

    def observe(self, name, v):
        with self._lock:
            self._hist.setdefault(name, []).append(v)

    def render(self) -> str:
        with self._lock:
            lines = []
            for k, v in self._counters.items():
                lines.append(f"{k} {v}")
            for k, v in self._gauges.items():
                lines.append(f"{k} {v}")
            for k, vs in self._hist.items():
                if vs:
                    lines.append(f"{k}_count {len(vs)}")
                    lines.append(f"{k}_sum {sum(vs)}")
            return "\n".join(lines) + "\n"


GLOBAL = Metrics()
