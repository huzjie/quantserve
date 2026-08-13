# -*- coding: utf-8 -*-
"""Terminal output helpers (no third-party deps)."""
import sys


def progress_bar(done: int, total: int, width: int = 40, label: str = "") -> str:
    if total <= 0:
        return f"{label} {done}"
    pct = done / total
    filled = int(width * pct)
    bar = "█" * filled + "░" * (width - filled)
    return f"\r{label} [{bar}] {pct*100:5.1f}% ({done}/{total})"


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"{prompt} {suffix} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return default
    if not ans:
        return default
    return ans in ("y", "yes")
