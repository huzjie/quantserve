# -*- coding: utf-8 -*-
"""`quantserve serve <model> [--engine ...] [--port ...]`"""
from ..engines import get_engine
from ..serve.gateway import Gateway


def add_parser(sub):
    p = sub.add_parser("serve", help="启动推理服务（多引擎）")
    p.add_argument("model", help="模型 ID")
    p.add_argument("--engine", default=None, help="vllm|sglang|ollama|llamacpp|...")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--gpus", type=int, default=None, help="张量并行卡数")
    p.add_argument("--gateway", action="store_true",
                   help="启动 OpenAI 兼容网关（加鉴权）")
    p.add_argument("--auth-token", default=None)
    p.set_defaults(func=run)


def run(args, config):
    from ..registry import get_registry
    model = get_registry().get(args.model)
    engine = get_engine(args.engine or config.get("default_engine", "vllm"))
    if not engine.available:
        print(f"⚠️  引擎 '{engine.name}' 二进制未找到；显示将执行的命令：")
    cmd = engine.build_command(model, None, port=args.port, gpus=args.gpus)
    print(" ".join(cmd))
    if args.gateway:
        print("\n启动网关（Ctrl+C 退出）...")
        gw = Gateway(upstream=f"http://127.0.0.1:{args.port}",
                     auth_token=args.auth_token or
                     config.get("api", {}).get("auth_token"))
        try:
            gw.serve(config.get("api", {}).get("host", "127.0.0.1"),
                     config.get("api", {}).get("port", 8000))
        except KeyboardInterrupt:
            print("\n已停止")
    elif engine.available:
        import subprocess
        subprocess.run(cmd)
    return 0
