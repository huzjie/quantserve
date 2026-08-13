# -*- coding: utf-8 -*-
"""Logging configuration (stdlib-only)."""
import logging
import sys

_FMT = "%(asctime)s %(levelname)-7s [%(name)s] %(message)s"


def setup_logging(level="INFO", stream=None):
    """Configure the root logger with a clean console format."""
    root = logging.getLogger()
    if getattr(root, "_q_configured", False):
        return root
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    if not root.handlers:
        h = logging.StreamHandler(stream or sys.stderr)
        h.setFormatter(logging.Formatter(_FMT))
        root.addHandler(h)
    root._q_configured = True
    return root


def get_logger(name="quantserve"):
    return logging.getLogger(name)
