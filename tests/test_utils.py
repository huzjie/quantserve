from quantserve.utils.fs import human_size


def test_human_size():
    assert human_size(0) == "0.0B"
    assert "GB" in human_size(5 * 1024 ** 3)
