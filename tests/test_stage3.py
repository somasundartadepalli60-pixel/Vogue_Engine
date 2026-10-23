import pytest
from vogue_engine.dashboards.report_store import ReportStore
from vogue_engine.dashboards import privacy
from fastapi import HTTPException

def test_report_store_empty_and_delete(tmp_path):
    store = ReportStore(tmp_path / 'reports.sqlite3')
    assert store.list() == []
    assert store.get('missing') is None
    assert store.delete('missing') is False
    assert store.clear() == 0

def test_passphrase_setup_and_verification(tmp_path, monkeypatch):
    monkeypatch.setattr(privacy, 'SETTINGS_PATH', tmp_path / 'auth.sqlite3')
    assert privacy.setup(privacy.Passphrase(passphrase='a-long-local-passphrase')) == {'configured': True}
    privacy.require_auth('a-long-local-passphrase')
    with pytest.raises(HTTPException) as error:
        privacy.require_auth('incorrect')
    assert error.value.status_code == 401
    with pytest.raises(HTTPException) as error:
        privacy.setup(privacy.Passphrase(passphrase='another-long-passphrase'))
    assert error.value.status_code == 409
