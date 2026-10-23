"""Stage 32 activity dashboard smoke and regression tests."""
from pathlib import Path
from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app


def test_activity_dashboard_served():
    response = TestClient(app).get('/wardrobe/activity')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert 'Event timeline' in response.text
    assert 'Change comparison' in response.text


def test_dashboard_uses_local_endpoints():
    page = (Path(__file__).resolve().parents[1] / 'vogue_engine/wardrobe/static/stage32.html').read_text()
    assert '/api/v1/wardrobe/activity' in page
    assert 'https://' not in page and 'http://' not in page
    assert 'innerHTML' not in page


def test_dashboard_has_filters_and_navigation():
    page = (Path(__file__).resolve().parents[1] / 'vogue_engine/wardrobe/static/stage32.html').read_text()
    for field in ('entity_type','entity_id','action','since','until','limit'):
        assert f'name="{field}"' in page
    assert 'id="previous"' in page and 'id="next"' in page
