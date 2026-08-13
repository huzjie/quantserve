from quantserve.engines import list_engines, get_engine
from quantserve.registry import get_registry


def test_list_engines():
    engines = list_engines()
    assert len(engines) >= 7
    names = [e.name for e in engines]
    assert "vllm" in names


def test_build_command():
    m = get_registry().get("qwen/qwen3.8-27b")
    e = get_engine("vllm")
    cmd = e.build_command(m, None, gpus=8)
    assert "--tensor-parallel-size" in cmd
