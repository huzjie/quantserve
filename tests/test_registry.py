from quantserve.registry import get_registry
from quantserve.exceptions import NotFoundError


def test_registry_has_models():
    reg = get_registry()
    assert len(reg.list()) >= 15


def test_get_qwen():
    m = get_registry().get("qwen/qwen3.8-2.4t-a95b")
    assert m.architecture == "moe"
    assert m.num_experts == 512


def test_search():
    reg = get_registry()
    assert len(reg.search("qwen")) > 0


def test_unknown_model():
    try:
        get_registry().get("no/such-model")
        assert False
    except NotFoundError:
        pass
