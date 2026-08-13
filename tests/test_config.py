from quantserve.config import Config, load_config


def test_defaults():
    c = Config()
    assert c.get("mirror") == "auto"
    assert c.get("default_engine") == "vllm"


def test_merge():
    c = Config({"mirror": "hf-mirror"})
    assert c["mirror"] == "hf-mirror"
    assert c.get("default_engine") == "vllm"
