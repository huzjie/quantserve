# -*- coding: utf-8 -*-
"""Async download jobs (in-process thread pool, no external queue)."""
from __future__ import annotations

import threading
import uuid

from fastapi import APIRouter

from ...downloader import Downloader
from ...config import load_config

router = APIRouter(prefix="/jobs", tags=["jobs"])

_JOBS = {}
_LOCK = threading.Lock()


@router.post("/download")
def start_download(req: dict):
    job_id = uuid.uuid4().hex[:12]
    with _LOCK:
        _JOBS[job_id] = {"status": "queued", "model_id": req.get("model_id")}

    def _run():
        with _LOCK:
            _JOBS[job_id]["status"] = "running"
        try:
            files = Downloader(load_config()).download(
                req.get("model_id"), mirror=req.get("mirror", "auto"))
            with _LOCK:
                _JOBS[job_id] = {"status": "done", "files": files}
        except Exception as e:
            with _LOCK:
                _JOBS[job_id] = {"status": "failed", "error": str(e)}

    threading.Thread(target=_run, daemon=True).start()
    return {"job_id": job_id, "status": "queued"}


@router.get("/{job_id}")
def get_job(job_id: str):
    with _LOCK:
        job = _JOBS.get(job_id)
    if not job:
        return {"error": "not found"}
    return {"job_id": job_id, **job}


@router.get("")
def list_jobs():
    with _LOCK:
        return {"jobs": [{"job_id": k, **v} for k, v in _JOBS.items()]}
