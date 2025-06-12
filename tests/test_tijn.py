import io
from contextlib import redirect_stdout

from src import vault


def test_handle_set_then_get():
    store = {}
    vault.handle_set(store, ["set", "gh", "tijn", "tijn"])
    f = io.StringIO()
    with redirect_stdout(f):
        vault.handle_get(store, ["get", "gh"])
    out = f.getvalue()
    assert "tijn" in out and "tijn" in out


# extra 1
def test_handle_set_overwrite():
    s = {}
    vault.handle_set(s, ["set", "svc", "u1", "p1"])
    vault.handle_set(s, ["set", "svc", "u2", "p2"])
    assert s["svc"]["username"] == "u2"


# extra 2
def test_handle_get_unknown_service(capsys):
    vault.handle_get({}, ["get", "abc"])
    captured = capsys.readouterr()
    assert "not found" in captured.out.lower()
