from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app
from vogue_engine.wardrobe.outfit_feedback_api import feedback_store

def test_dashboard_is_available():
    response = TestClient(app).get('/wardrobe/outfit-feedback')
    assert response.status_code == 200
    assert 'Outfit Feedback Studio' in response.text

def test_analytics_schema():
    response = TestClient(app).get('/api/v1/wardrobe/outfit-feedback/analytics')
    assert response.status_code == 200
    body = response.json()
    assert set(body['rating_counts']) == {'1','2','3','4','5'}
    assert body['total'] >= body['favorites']

def test_dashboard_contains_rating_controls():
    html = TestClient(app).get('/wardrobe/outfit-feedback').text
    assert 'favoritesOnly' in html
    assert 'Star rating' in html
    assert 'Delete feedback' in html
