"""Stage 39 trip comparison and dashboard smoke tests."""
from datetime import date
from fastapi.testclient import TestClient
from vogue_engine.wardrobe.api import WardrobeStore
from vogue_engine.wardrobe.travel import TravelStore
from vogue_engine.dashboards.router import app


def test_compare_trips(tmp_path):
    wardrobe=WardrobeStore(tmp_path/'wardrobe.sqlite3')
    travel=TravelStore(wardrobe)
    first=travel.create('First','City A',date(2026,11,1),date(2026,11,3))
    second=travel.create('Second','City B',date(2026,11,4),date(2026,11,6))
    result=travel.compare_trips(first['id'],second['id'])
    assert result['first']['total']==0
    assert result['second']['total']==0
    assert result['shared']==result['first_only']==result['second_only']==[]


def test_compare_unknown_trip(tmp_path):
    travel=TravelStore(WardrobeStore(tmp_path/'wardrobe.sqlite3'))
    try:
        travel.compare_trips(1234,5678)
    except LookupError:
        pass
    else:
        raise AssertionError('Expected LookupError')


def test_stage39_dashboard():
    response=TestClient(app).get('/wardrobe/travel/templates')
    assert response.status_code==200
    assert 'Packing templates' in response.text
    assert '/seasonal-plan' in response.text
