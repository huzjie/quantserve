from quantserve.cluster.scheduler import place
from quantserve.cluster import GPU
from quantserve.registry import get_registry


def test_place_ok():
    gpus = [GPU(0, "H100", 81920), GPU(1, "H100", 81920)]
    models = [get_registry().get("qwen/qwen3.8-27b"),
              get_registry().get("google/gemma-3-4b")]
    r = place(models, gpus)
    assert r["ok"]
