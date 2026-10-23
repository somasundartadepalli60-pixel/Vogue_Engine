from datetime import date
import csv
import io
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.travel import TravelStore

@pytest.fixture
def planner(tmp_path):
    store=WardrobeStore(str(tmp_path/'travel.db'))
    return store,TravelStore(store)

def test_summary_empty(planner):
    _,travel=planner
    trip=travel.create('Weekend','City',date(2026,10,24),date(2026,10,26))
    summary=travel.packing_summary(trip['id'])
    assert (summary['days'],summary['total'],summary['percent_packed'])==(3,0,0)

def test_summary_packing_and_csv(planner):
    store,travel=planner
    trip=travel.create('Holiday','Beach',date(2026,10,24),date(2026,10,25))
    a=store.add('Linen shirt','tops','white')
    b=store.add('Shorts','bottoms','blue')
    travel.add_item(trip['id'],a['id']);travel.add_item(trip['id'],b['id'])
    travel.set_packed(trip['id'],a['id'],True)
    summary=travel.packing_summary(trip['id'])
    assert summary['packed']==1 and summary['remaining']==1 and summary['percent_packed']==50.0
    assert summary['categories']['tops']=={'total':1,'packed':1}
    rows=list(csv.DictReader(io.StringIO(travel.packing_csv(trip['id']))))
    assert len(rows)==2 and {r['packed'] for r in rows}=={'yes','no'}

def test_summary_unknown_trip(planner):
    _,travel=planner
    with pytest.raises(LookupError): travel.packing_summary(999)
    with pytest.raises(LookupError): travel.packing_csv(999)
