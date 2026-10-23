"""Stage 34 local reminder dashboard smoke and route tests."""
from pathlib import Path
from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app

PAGE = Path(__file__).resolve().parents[1] / 'vogue_engine' / 'wardrobe' / 'static' / 'stage34.html'

def test_dashboard_file_and_accessible_controls():
    html = PAGE.read_text(encoding='utf-8')
    for marker in ['Notification center', 'Reminder calendar', 'Manage reminders', 'Reminder preferences', 'aria-live="polite"']:
        assert marker in html

def test_dashboard_has_local_api_and_no_remote_dependencies():
    html = PAGE.read_text(encoding='utf-8')
    assert '/api/v1/wardrobe/reminders' in html
    assert 'https://' not in html and 'http://' not in html
    assert 'setInterval' in html

def test_reminder_dashboard_route():
    response = TestClient(app).get('/wardrobe/reminders')
    assert response.status_code == 200
    assert 'Wardrobe Reminders' in response.text
