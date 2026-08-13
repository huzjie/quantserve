from quantserve.checksum import sha256_bytes, verify
import tempfile, os


def test_sha256_bytes():
    assert len(sha256_bytes(b"hello")) == 64


def test_verify_ok():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"hello")
        path = f.name
    assert verify(path, sha256_bytes(b"hello"))
    os.unlink(path)
