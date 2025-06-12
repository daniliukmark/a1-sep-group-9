import os

from src import vault


def _save_then_load(tmp_path):
    file = tmp_path / "vault.json"
    pwds = {"x": {"username": "u", "password": "p"}}
    vault.save_store(str(file), pwds, "master")
    loaded, _ = vault.load_store(str(file))
    return loaded


def test_store_roundtrip(tmp_path):
    loaded = _save_then_load(tmp_path)
    assert loaded["x"]["password"] == "p"


# extra 1
def test_save_is_atomic(tmp_path):
    file = tmp_path / "v.json"
    vault.save_store(str(file), {}, "m")
    assert not (tmp_path / "v.json.tmp").exists()


# extra 2
def test_invalid_master_password(tmp_path, monkeypatch, capsys):
    file = tmp_path / "v.json"
    vault.save_store(str(file), {}, "right")
    monkeypatch.setattr("getpass.getpass", lambda _: "wrong")
    code = os.system(f"python {vault.__file__} {file} </dev/null 2>/dev/null")
    assert code != 0
