"""Stage 36 dashboard smoke tests."""
from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app


def test_dashboard_route_registered():
    assert '/wardrobe/maintenance' in {route.path for route in app.routes}


def test_dashboard_serves_ui():
    response = TestClient(app).get('/wardrobe/maintenance')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert 'Garment Care &amp; Maintenance' not in response.text
    assert 'Garment Care & Maintenance' in response.text


def test_dashboard_contains_existing_maintenance_endpoints():
    content = TestClient(app).get('/wardrobe/maintenance').text
    assert '/api/v1/wardrobe/maintenance' in content
    assert '/api/v1/wardrobe/garments' in content
    assert 'Care recommendations' in content
