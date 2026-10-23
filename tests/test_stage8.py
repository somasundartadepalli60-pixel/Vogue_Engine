import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.care import CareStore

@pytest.fixture
def sample(tmp_path):
    w=WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    g=w.add('Linen shirt','shirt','white')
    return w,g,CareStore(w)

def test_configure_and_reminders(sample):
    _,g,c=sample
    result=c.configure(g['id'],last_washed='2026-10-01',wash_interval_days=7)
    assert result['next_wash']=='2026-10-08'
    assert c.reminders('2026-10-07')==[]
    assert c.reminders('2026-10-09')[0]['overdue']

def test_record_wash_updates_reminder(sample):
    _,g,c=sample
    c.configure(g['id'],wash_interval_days=5)
    c.record(g['id'],'wash','2026-10-10')
    assert c.get(g['id'])['next_wash']=='2026-10-15'
    assert len(c.history(g['id']))==1

def test_older_event_does_not_regress_latest_wash(sample):
    _,g,c=sample
    c.configure(g['id'])
    c.record(g['id'],'wash','2026-10-20')
    c.record(g['id'],'dry_clean','2026-10-01')
    assert c.get(g['id'])['last_washed']=='2026-10-20'

def test_condition_and_analytics(sample):
    _,g,c=sample
    c.configure(g['id'],condition='needs_repair')
    c.record(g['id'],'repair','2026-10-10')
    assert c.overview()['care_events']==1
    assert c.overview()['conditions'][0]['condition']=='needs_repair'

def test_validation(sample):
    _,g,c=sample
    with pytest.raises(ValueError): c.configure(g['id'],condition='broken')
    with pytest.raises(ValueError): c.configure(g['id'],wash_interval_days=0)
    c.configure(g['id'])
    with pytest.raises(ValueError): c.record(g['id'],'unknown','2026-10-10')
    with pytest.raises(LookupError): c.record(999,'wash','2026-10-10')

def test_cascade(sample):
    w,g,c=sample
    c.configure(g['id']);c.record(g['id'],'wash','2026-10-10')
    w.delete(g['id'])
    assert c.get(g['id']) is None and c.history(g['id'])==[]
