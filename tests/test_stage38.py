from datetime import date
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.travel import TravelStore

@pytest.fixture
def context(tmp_path):
    store = WardrobeStore(str(tmp_path / 'trip.db'))
    travel = TravelStore(store)
    trip = travel.create('Conference','Pune',date(2026,11,1),date(2026,11,4),'winter','formal')
    return store, travel, trip['id']

def test_template_roundtrip(context):
    store, travel, trip = context
    garment = store.add('Blue shirt','tops','blue')
    travel.add_item(trip,garment['id'])
    template = travel.save_template('Work trip',trip)
    assert travel.list_templates()[0]['items'] == 1
    second = travel.create('Again','Pune',date(2026,12,1),date(2026,12,3))['id']
    assert travel.apply_template(second,template['id'])['total'] == 1
    assert travel.apply_template(second,template['id'])['total'] == 1
    assert travel.delete_template(template['id'])

def test_template_validation(context):
    _, travel, trip = context
    with pytest.raises(ValueError): travel.save_template(' ',trip)
    travel.save_template('Reusable',trip)
    with pytest.raises(ValueError): travel.save_template('Reusable',trip)
    with pytest.raises(LookupError): travel.apply_template(trip,999)
    with pytest.raises(LookupError): travel.save_template('Bad',999)

def test_seasonal_plan_offline(context):
    store, travel, trip = context
    store.add('Jacket','outerwear','black',season='winter',occasion='formal')
    result = travel.seasonal_plan(trip)
    assert result['days'] == 4
    assert result['suggestions'][0]['garment']['name'] == 'Jacket'
    assert result['weather_source'].startswith('none')
    with pytest.raises(ValueError): travel.seasonal_plan(trip,0)
    with pytest.raises(LookupError): travel.seasonal_plan(999)
