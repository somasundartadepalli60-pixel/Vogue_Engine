from datetime import date
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.travel import TravelStore

@pytest.fixture
def setup(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'travel.sqlite3'))
    travel=TravelStore(wardrobe)
    trip=travel.create('Weekend','Goa',date(2026,11,1),date(2026,11,3),'summer','casual')
    shirt=wardrobe.add('Blue shirt','top','blue','summer','casual')
    return wardrobe,travel,trip,shirt

def test_trip_persistence(setup):
    wardrobe,travel,trip,_=setup
    assert TravelStore(wardrobe).get(trip['id'])['destination']=='Goa'
    assert len(travel.list())==1

def test_checklist_and_pack(setup):
    _,travel,trip,shirt=setup
    travel.add_item(trip['id'],shirt['id'])
    assert travel.checklist(trip['id'])['packed']==0
    assert travel.set_packed(trip['id'],shirt['id'],True)['packed']==1
    assert travel.remove_item(trip['id'],shirt['id'])

def test_recommendations(setup):
    _,travel,trip,shirt=setup
    assert travel.recommendations(trip['id'])[0]['garment']['id']==shirt['id']
    travel.add_item(trip['id'],shirt['id'])
    assert travel.recommendations(trip['id'])==[]

def test_invalid_dates(setup):
    _,travel,_,_=setup
    with pytest.raises(ValueError): travel.create('x','y',date(2026,12,2),date(2026,12,1))

def test_outfit_schedule(setup):
    wardrobe,travel,trip,shirt=setup
    outfit=wardrobe.create_outfit('Beach',[shirt['id']])
    scheduled=travel.schedule_outfit(trip['id'],date(2026,11,2),outfit['id'])
    assert scheduled[0]['outfit_name']=='Beach'
    with pytest.raises(ValueError): travel.schedule_outfit(trip['id'],date(2026,11,9),outfit['id'])

def test_delete_trip(setup):
    _,travel,trip,_=setup
    assert travel.delete(trip['id'])
    assert travel.get(trip['id']) is None
