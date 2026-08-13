# -*- coding: utf-8 -*-
"""Stdlib HTTP client for the QuantServe control plane."""
from __future__ import annotations

import json
import urllib.request
import urllib.error


class QuantServeClient:
    def __init__(self, base_url="http://127.0.0.1:8000", token=None):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _req(self, method, path, payload=None):
        url = self.base_url + path
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json")
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')}")

    def health(self):
        return self._req("GET", "/healthz")

    def list_models(self, keyword=None):
        q = f"?keyword={keyword}" if keyword else ""
        return self._req("GET", f"/models{q}")

    def get_model(self, model_id):
        return self._req("GET", f"/models/{model_id}")

    def estimate_quant(self, model_id, budget_gb=None, target_size_gb=None):
        q = []
        if budget_gb:
            q.append(f"budget_gb={budget_gb}")
        if target_size_gb:
            q.append(f"target_size_gb={target_size_gb}")
        return self._req("GET", f"/quantize/{model_id}?{'&'.join(q)}")

    def list_engines(self):
        return self._req("GET", "/serve/engines")

    def plan(self, model_id, bits=8.0):
        return self._req("POST", "/cluster/plan", {"model_id": model_id, "bits": bits})

    def compare_cost(self, model_id, monthly_tokens_m=100.0, gpus=1, gpu_capex=20000.0):
        return self._req("POST", "/cost/compare", {
            "model_id": model_id, "monthly_tokens_m": monthly_tokens_m,
            "gpus": gpus, "gpu_capex": gpu_capex})

    def start_download(self, model_id, mirror="auto"):
        return self._req("POST", "/jobs/download", {"model_id": model_id, "mirror": mirror})

    def get_job(self, job_id):
        return self._req("GET", f"/jobs/{job_id}")
