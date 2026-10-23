"""Stage 31 activity history regression tests."""
import sqlite3
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.activity import ActivityJournal

@pytest.fixture
def journal_and_store(tmp_path):
    path = str(tmp_path / 'wardrobe.sqlite3')
    store = WardrobeStore(path)
    journal = ActivityJournal(path)
    return journal, store

def test_insert_is_logged(journal_and_store):
    journal, store = journal_and_store
    garment = store.add('Jacket','outerwear','blue')
    events = journal.list(entity_type='garment',entity_id=garment['id'])
    assert len(events) == 1 and events[0]['action'] == 'created'
    assert events[0]['details']['name'] == 'Jacket'

def test_update_is_logged(journal_and_store):
    journal, store = journal_and_store
    garment = store.add('Shirt','top','white')
    store.update(garment['id'],color='black')
    event = journal.list(action='updated')[0]
    assert event['details']['before']['color'] == 'white'
    assert event['details']['after']['color'] == 'black'

def test_delete_is_logged(journal_and_store):
    journal, store = journal_and_store
    garment = store.add('Hat','accessory','red')
    store.delete(garment['id'])
    assert journal.list(action='deleted')[0]['entity_id'] == garment['id']

def test_summary(journal_and_store):
    journal, store = journal_and_store
    store.add('Jeans','bottom','blue')
    result = journal.summary()
    assert result['total'] == 1
    assert result['by_action'][0]['count'] == 1

def test_manual_event(journal_and_store):
    journal, _ = journal_and_store
    item = journal.record('inventory','audit_started',details={'count':2})
    assert journal.get(item['id'])['details']['count'] == 2

def test_invalid_action(journal_and_store):
    journal, _ = journal_and_store
    with pytest.raises(ValueError):
        journal.record('inventory','not allowed!')

def test_pagination(journal_and_store):
    journal, store = journal_and_store
    for i in range(3): store.add(f'Item {i}','top','red')
    assert len(journal.list(limit=2)) == 2
    assert len(journal.list(limit=2,offset=2)) == 1
