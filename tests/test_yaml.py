from quantserve._yaml import load


def test_nested():
    d = load("a:\n  b: 1\n  c: [1, 2, 3]\nlist:\n  - x\n  - y\n")
    assert d["a"]["b"] == 1
    assert d["a"]["c"] == [1, 2, 3]
    assert d["list"] == ["x", "y"]


def test_scalars():
    d = load("s: hello\ni: 42\nf: 3.14\nb: true\nn: null\n")
    assert d["s"] == "hello"
    assert d["i"] == 42
    assert d["f"] == 3.14
    assert d["b"] is True
    assert d["n"] is None
