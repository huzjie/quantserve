"""QuantServe 异步 SDK 示例。"""
import asyncio
from quantserve.sdk.async_client import AsyncQuantServeClient


async def main():
    c = AsyncQuantServeClient("http://127.0.0.1:8000")
    health = await c.health()
    models = await c.list_models(keyword="deepseek")
    print(health, models["count"])


if __name__ == "__main__":
    asyncio.run(main())
