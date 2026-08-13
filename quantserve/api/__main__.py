# -*- coding: utf-8 -*-
"""`python -m quantserve.api` — run the control plane with uvicorn."""
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    import uvicorn
    uvicorn.run("quantserve.api.app:get_app", host=args.host, port=args.port,
                factory=True)


if __name__ == "__main__":
    main()
