from src import vault


def test_handle_list_empty(capsys):
    vault.handle_list({})
    assert "no passwords" in capsys.readouterr().out.lower()


# extra 1
def test_handle_list_sorted(capsys):
    store = {"b": {}, "a": {}, "c": {}}
    vault.handle_list(store)
    out = capsys.readouterr().out
    assert out.strip().splitlines()[-3:] == ["  - a", "  - b", "  - c"]


# extra 2
def test_handle_del():
    s = {"svc": {}}
    vault.handle_del(s, ["del", "svc"])
    assert not s
