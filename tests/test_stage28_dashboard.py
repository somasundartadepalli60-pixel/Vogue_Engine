"""Stage 28 dashboard integration checks."""
from pathlib import Path
from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app


def test_backup_dashboard_route():
    response = TestClient(app).get('/wardrobe/backups')
    assert response.status_code == 200
    assert 'Wardrobe Backup & Recovery' in response.text


def test_backup_dashboard_has_confirmation_and_preview():
    path = Path(__file__).resolve().parents[1] / 'vogue_engine/wardrobe/static/stage28.html'
    html = path.read_text(encoding='utf-8')
    assert 'RESTORE' in html
    assert '/preview' in html
    assert '/verify' in html
    assert 'textContent' in html
