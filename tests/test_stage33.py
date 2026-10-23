"""Stage 33 reminder persistence, status, filtering and preferences."""
import pytest
from datetime import datetime, timedelta, timezone
from vogue_engine.wardrobe.reminders import ReminderStore

@pytest.fixture
def reminders(tmp_path): return ReminderStore(tmp_path/'wardrobe.sqlite3')

def future(hours=2): return (datetime.now(timezone.utc)+timedelta(hours=hours)).isoformat()

def test_create_and_read(reminders):
    item=reminders.create('Wash coat','laundry',future(),garment_id=2)
    assert reminders.get(item['id'])['garment_id']==2
    assert item['status']=='pending'

def test_filter_and_pagination(reminders):
    reminders.create('A','laundry',future())
    reminders.create('B','repair',future())
    assert reminders.list(kind='laundry')['total']==1
    assert len(reminders.list(limit=1)['items'])==1

def test_complete_and_reopen(reminders):
    item=reminders.create('A','custom',future())
    assert reminders.set_status(item['id'],'completed')['completed_at']
    assert reminders.set_status(item['id'],'pending')['completed_at'] is None

def test_notifications_and_disable(reminders):
    reminders.create('Soon','custom',future(1))
    reminders.create('Later','custom',future(100))
    assert reminders.notifications()['count']==1
    reminders.set_preferences(False,24)
    assert reminders.notifications()['count']==0

def test_overdue(reminders):
    reminders.create('Late','laundry',future(-2))
    assert reminders.notifications()['items'][0]['overdue'] is True

def test_reject_bad_inputs(reminders):
    with pytest.raises(ValueError): reminders.create('Bad','laundry','2026-10-23T10:00:00')
    with pytest.raises(ValueError): reminders.create('Bad','unknown',future())
    with pytest.raises(ValueError): reminders.set_preferences(True,0)
    with pytest.raises(LookupError): reminders.get(999)

def test_persistence(tmp_path):
    path=tmp_path/'data.db'
    first=ReminderStore(path).create('Keep','outfit_plan',future())
    assert ReminderStore(path).get(first['id'])['title']=='Keep'
