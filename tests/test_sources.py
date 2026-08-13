from quantserve.registry import get_registry
from quantserve.sources import SOURCES


def test_hf_files():
    m = get_registry().get("qwen/qwen3.8-27b")
    files = SOURCES["huggingface"]().files(m)
    assert any("safetensors" in f.filename for f in files)


def test_modelscope_files():
    m = get_registry().get("qwen/qwen3.8-2.4t-a95b")
    files = SOURCES["modelscope"]().files(m)
    assert len(files) > 2
