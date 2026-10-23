from vogue_engine.wardrobe.measurement_trends import summarize_history
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.measurements import MeasurementStore


def test_trend_sorts_and_calculates_change(tmp_path):
    store = MeasurementStore(WardrobeStore(str(tmp_path / 'fit.db')))
    garment = store.wardrobe.add('Coat', 'outerwear', 'navy')
    store.record(garment['id'], {'chest': 105}, '2026-04-01')
    store.record(garment['id'], {'chest': 101, 'waist': 82}, '2026-02-01')
    summary = summarize_history(store.history(garment['id']))
    assert summary['events'] == 2
    assert summary['dimensions']['chest']['change_cm'] == 4
    assert summary['dimensions']['waist']['change_cm'] == 0
    assert [p['date'] for p in summary['dimensions']['chest']['points']] == ['2026-02-01', '2026-04-01']


def test_empty_trend():
    assert summarize_history([]) == {'events': 0, 'dimensions': {}}


def test_dashboard_route_exists():
    from vogue_engine.dashboards.router import app
    paths = {route.path for route in app.routes}
    assert '/wardrobe/measurements' in paths
    assert '/api/v1/wardrobe/measurements/garments/{garment_id}/trends' in paths
