import base64
import os

from src.vault import derive_key


def test_derive_key_deterministic():
    salt = os.urandom(16)
    key1 = derive_key("secret", salt)
    key2 = derive_key("secret", salt)
    assert key1 == key2


# extra 1
def test_derive_key_changes_with_password():
    salt = os.urandom(16)
    assert derive_key("a", salt) != derive_key("b", salt)


# extra 2
def test_derive_key_length():
    key = derive_key("pw", b"0" * 16)
    assert len(base64.urlsafe_b64decode(key)) == 32
