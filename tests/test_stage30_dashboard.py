"""Stage 30 browser dashboard integration checks."""
from pathlib import Path
from vogue_engine.dashboards.router import wardrobe_portability_dashboard


def test_portability_dashboard_contains_local_export_links():
    response = wardrobe_portability_dashboard()
    html = response.body.decode('utf-8')
    assert '/api/v1/wardrobe/portable/archive.zip' in html
    assert '/api/v1/wardrobe/portable/export.json' in html
    assert 'outfit_garments' in html


def test_portability_dashboard_requires_preview_and_confirmation():
    response = wardrobe_portability_dashboard()
    html = response.body.decode('utf-8')
    assert 'import/preview' in html
    assert 'import/commit?confirm=true' in html
    assert 'id="commit" disabled' in html
    assert 'textContent' in html  # untrusted imported data is not inserted as HTML


def test_dashboard_is_bundled():
    path = Path(__file__).resolve().parents[1] / 'vogue_engine' / 'wardrobe' / 'portable_dashboard.html'
    assert path.is_file()
