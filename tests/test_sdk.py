from quantserve.sdk.client import QuantServeClient


def test_url_join():
    c = QuantServeClient("http://127.0.0.1:8000")
    assert c.base_url == "http://127.0.0.1:8000"
