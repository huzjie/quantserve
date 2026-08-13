from quantserve.registry import get_registry
from quantserve.quant.planner import QuantPlanner


def test_plan_all():
    m = get_registry().get("qwen/qwen3.8-2.4t-a95b")
    results = QuantPlanner().plan_all(m)
    assert len(results) == 8
    for r in results:
        assert r.quantized_gb <= r.original_gb


def test_recommend_fits_budget():
    m = get_registry().get("qwen/qwen3.8-27b")
    best, _ = QuantPlanner().recommend(m, budget_gb=40)
    assert best is not None


def test_onedbit_compression():
    m = get_registry().get("qwen/qwen3.8-2.4t-a95b")
    from quantserve.quant.base import OneBitMethod
    r = OneBitMethod().plan(m)
    assert r.compression_ratio > 8
