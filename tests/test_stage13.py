"""Stage 13 visual studio smoke checks."""
from pathlib import Path

def test_dashboard_exists_and_is_offline():
    path = Path(__file__).resolve().parents[1] / 'vogue_engine/wardrobe/static/stage13.html'
    html = path.read_text()
    assert 'Outfit Recommendation Studio' in html
    assert '/api/v1/wardrobe/recommendation/suggestions' in html
    assert '/api/v1/wardrobe/recommendation/feedback' in html
    assert 'https://' not in html and 'http://' not in html
    assert '.env' not in html

def test_route_registered():
    from vogue_engine.dashboards.router import app
    assert any(getattr(route, 'path', None) == '/wardrobe/recommendations' for route in app.routes)
