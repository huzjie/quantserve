# -*- coding: utf-8 -*-
"""`quantserve` CLI entry point."""
import argparse

from ..version import __version__
from ..logging import setup_logging
from ..config import load_config
from . import (list_cmd, download_cmd, quantize_cmd, serve_cmd,
               plan_cmd, cost_cmd, doctor_cmd, init_cmd)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="quantserve",
        description="QuantServe — 开源大模型本地化部署与量化推理平台",
    )
    p.add_argument("--config", help="配置文件路径")
    p.add_argument("--verbose", action="store_true", help="调试日志")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    list_cmd.add_parser(sub)
    download_cmd.add_parser(sub)
    quantize_cmd.add_parser(sub)
    serve_cmd.add_parser(sub)
    plan_cmd.add_parser(sub)
    cost_cmd.add_parser(sub)
    doctor_cmd.add_parser(sub)
    init_cmd.add_parser(sub)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    setup_logging(level="DEBUG" if args.verbose else "INFO")
    config = load_config(args.config)
    config.ensure_dirs()
    return args.func(args, config)


if __name__ == "__main__":
    raise SystemExit(main())
