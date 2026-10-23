"""Stage 11 integration tests using isolated SQLite databases."""
from datetime import date
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.calendar import CalendarStore

@pytest.fixture
def sample(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    first=wardrobe.add('Shirt','top','blue')['id']
    second=wardrobe.add('Jeans','bottom','black')['id']
    outfit=wardrobe.create_outfit('Everyday',[first,second])['id']
    return CalendarStore(wardrobe),first,second,outfit

def test_schedule_and_agenda(sample):
    cal,_,_,outfit=sample
    cal.schedule(date(2026,11,1),'morning',outfit,'Work')
    assert cal.agenda(date(2026,11,1),date(2026,11,2))[0]['note']=='Work'

def test_unavailable_garment(sample):
    cal,first,_,outfit=sample
    cal.block(first,date(2026,11,1),date(2026,11,3),'Laundry')
    with pytest.raises(ValueError): cal.schedule(date(2026,11,2),'day',outfit)
    assert cal.schedule(date(2026,11,2),'day',outfit,force=True)['conflicts']

def test_same_day_conflict(sample):
    cal,_,_,outfit=sample
    cal.schedule(date(2026,11,1),'morning',outfit)
    with pytest.raises(ValueError): cal.schedule(date(2026,11,1),'evening',outfit)

def test_reschedule_same_slot(sample):
    cal,_,_,outfit=sample
    cal.schedule(date(2026,11,1),'day',outfit)
    cal.schedule(date(2026,11,1),'day',outfit,'Updated')
    assert len(cal.agenda(date(2026,11,1),date(2026,11,1)))==1

def test_forecast(sample):
    cal,first,second,outfit=sample
    cal.schedule(date(2026,11,1),'day',outfit)
    result=cal.forecast(date(2026,11,1),7)
    assert result['scheduled_outfits']==1
    assert {r['garment_id'] for r in result['garment_usage']}=={first,second}

def test_remove_block_and_schedule(sample):
    cal,first,_,outfit=sample
    block=cal.block(first,date(2026,11,1),date(2026,11,1),'Repair')
    assert cal.unblock(block['id'])
    assert not cal.conflicts(date(2026,11,1),outfit)

def test_invalid_ranges(sample):
    cal,first,_,_=sample
    with pytest.raises(ValueError): cal.block(first,date(2026,11,2),date(2026,11,1),'Repair')
    with pytest.raises(ValueError): cal.forecast(date(2026,11,1),0)
    with pytest.raises(ValueError): cal.agenda(date(2026,11,2),date(2026,11,1))

def test_delete_schedule(sample):
    cal,_,_,outfit=sample
    cal.schedule(date(2026,11,1),'day',outfit)
    assert cal.unschedule(date(2026,11,1),'day')
    assert not cal.unschedule(date(2026,11,1),'day')
