from quantserve.cluster import ParallelPlanner, GPU
from quantserve.registry import get_registry


def _gpus(n, gb=80):
    return [GPU(index=i, name="H100", memory_mb=int(gb * 1024)) for i in range(n)]


def test_plan_dense():
    m = get_registry().get("qwen/qwen3.8-27b")
    res = ParallelPlanner().plan(m, _gpus(4, 80), bits=8)
    assert res.ok


def test_plan_moe_insufficient():
    m = get_registry().get("qwen/qwen3.8-2.4t-a95b")
    res = ParallelPlanner().plan(m, _gpus(1, 24), bits=8)
    assert not res.ok
