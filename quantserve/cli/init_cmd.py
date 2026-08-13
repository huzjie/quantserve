# -*- coding: utf-8 -*-
"""`quantserve init` — 生成 config.yaml 模板。"""
from pathlib import Path

from ..config import default_config_text


def add_parser(sub):
    p = sub.add_parser("init", help="生成配置文件模板")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=run)


def run(args, config):
    target = Path("config.yaml")
    if target.exists() and not args.force:
        print(f"config.yaml 已存在（--force 覆盖）")
        return 1
    target.write_text(default_config_text(), encoding="utf-8")
    print(f"✅ 已生成 {target}")
    return 0
