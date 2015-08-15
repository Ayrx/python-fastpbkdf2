import pytest

from fastpbkdf2 import pbkdf2_hmac


def test_unsupported_algorithm():
    with pytest.raises(ValueError):
        pbkdf2_hmac("foo", b"password", b"salt", 1)
