"""Stage 2 isolated database tests."""
import pytest
from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app
from vogue_engine.wardrobe.api import store
from vogue_engine.wardrobe.storage import WardrobeStore

@pytest.fixture
def client(tmp_path):
    store.cache_clear()
    store.__wrapped__  # store is a cached dependency
    import vogue_engine.wardrobe.api as api
    original=api.store
    isolated=WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    app.dependency_overrides[original]=lambda:isolated
    # Stage 1 calls store() directly, so replace its cache with test path.
    original.cache_clear()
    original.__wrapped__.__defaults__ if False else None
    import vogue_engine.wardrobe.stage2 as stage2
    stage2.store=lambda:isolated
    api.store=lambda:isolated
    yield TestClient(app)
    api.store=original
    stage2.store=original
    app.dependency_overrides.clear()


def test_import_export_search(client):
    backup={'format':'vogue-wardrobe-v1','garments':[{'name':'Blue Jeans','category':'bottom','color':'blue'}]}
    r=client.post('/api/v1/wardrobe/import/json',json=backup)
    assert r.status_code==200 and r.json()['imported']==1
    assert client.get('/api/v1/wardrobe/search?q=Jeans').json()['total']==1
    assert client.get('/api/v1/wardrobe/export/json').json()['garments'][0]['name']=='Blue Jeans'
    assert 'Blue Jeans' in client.get('/api/v1/wardrobe/export/csv').text


def test_calendar(client):
    g=client.post('/api/v1/wardrobe/garments',json={'name':'Shirt','category':'top','color':'white'}).json()
    o=client.post('/api/v1/wardrobe/outfits',json={'name':'Work','garment_ids':[g['id']]}).json()
    payload={'day':'2026-11-01','outfit_id':o['id'],'note':'Meeting'}
    assert client.put('/api/v1/wardrobe/calendar',json=payload).status_code==200
    assert client.get('/api/v1/wardrobe/calendar').json()[0]['note']=='Meeting'
    assert client.delete('/api/v1/wardrobe/calendar/2026-11-01').status_code==200
    assert client.get('/api/v1/wardrobe/calendar').json()==[]


def test_local_dashboard(client):
    r=client.get('/wardrobe')
    assert r.status_code==200 and 'My Wardrobe' in r.text
