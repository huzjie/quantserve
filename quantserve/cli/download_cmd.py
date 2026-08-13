# -*- coding: utf-8 -*-
"""`quantserve download <model> [--mirror ...] [--dest ...]`"""
from ..downloader import Downloader


def add_parser(sub):
    p = sub.add_parser("download", help="下载开源模型权重（多源+断点续传）")
    p.add_argument("model", help="模型 ID")
    p.add_argument("--mirror", default=None,
                   help="auto|hf-mirror|modelscope|huggingface")
    p.add_argument("--dest", default=None, help="目标目录")
    p.set_defaults(func=run)


def run(args, config):
    d = Downloader(config)
    files = d.download(args.model, dest_dir=args.dest, mirror=args.mirror)
    print(f"\n✅ 下载完成，{len(files)} 个文件")
    return 0
