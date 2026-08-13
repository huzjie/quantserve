# -*- coding: utf-8 -*-
"""Multi-source weight downloader with resume + checksum + concurrency."""
from __future__ import annotations

import os
import threading
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .checksum import verify
from .exceptions import ChecksumError, DownloadError
from .registry import get_registry
from .sources import SOURCES
from .utils.fs import human_size
from .utils.terminal import progress_bar


class Downloader:
    def __init__(self, config):
        self.config = config
        self._done = 0
        self._lock = threading.Lock()

    def _source(self, mirror: str):
        if mirror == "auto":
            # prefer hf-mirror (CN) then modelscope then huggingface
            order = ["hf-mirror", "modelscope", "huggingface"]
        else:
            order = [mirror]
        for name in order:
            if name in SOURCES:
                return SOURCES[name]()
        return SOURCES["huggingface"]()

    def download(self, model_id: str, dest_dir: str | None = None,
                 mirror: str = "auto") -> list:
        model = get_registry().get(model_id)
        dest = Path(dest_dir or os.path.join(self.config.models_dir, model.id))
        dest.mkdir(parents=True, exist_ok=True)

        source = self._source(mirror or self.config.get("mirror", "auto"))
        files = source.files(model)
        print(f"[download] {model.name} via {source.name} -> {dest}")
        print(f"[download] {len(files)} file(s), ~{model.bf16_size_gb:.0f}GB total")

        results = []
        workers = self.config.get("max_concurrency", 4)
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(self._one, f, dest): f for f in files}
            for fut in as_completed(futs):
                f = futs[fut]
                try:
                    path = fut.result()
                    results.append(path)
                except Exception as e:
                    print(f"\n[download] FAILED {f.filename}: {e}")
                    raise DownloadError(f"failed to download {f.filename}: {e}")
        print(f"\n[download] complete: {len(results)} file(s) in {dest}")
        return results

    def _one(self, f, dest: Path):
        target = dest / f.filename
        chunk = self.config.get("chunk_size_mb", 64) * 1024 * 1024
        # resume support
        existing = target.stat().st_size if target.exists() else 0
        headers = {"User-Agent": "quantserve"}
        if existing > 0:
            headers["Range"] = f"bytes={existing}-"
        req = urllib.request.Request(f.url, headers=headers)
        mode = "ab" if existing > 0 else "wb"
        with urllib.request.urlopen(req, timeout=120) as resp, \
             open(target, mode) as out:
            total = int(resp.headers.get("Content-Length", 0) or 0) + existing
            while True:
                data = resp.read(chunk)
                if not data:
                    break
                out.write(data)
                with self._lock:
                    self._done += 1
                print(progress_bar(self._done * chunk, total,
                                   label=f"{f.filename}"), end="", flush=True)
        if f.sha256:
            if not verify(target, f.sha256):
                raise ChecksumError(f"sha256 mismatch for {f.filename}")
        return str(target)
