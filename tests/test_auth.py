from quantserve.serve.auth import check_auth, bearer


def test_check_auth():
    assert check_auth("abc", "abc")
    assert not check_auth("abc", "xyz")
    assert check_auth("", None)


def test_bearer():
    assert bearer("Bearer tok123") == "tok123"
    assert bearer("raw") == "raw"
