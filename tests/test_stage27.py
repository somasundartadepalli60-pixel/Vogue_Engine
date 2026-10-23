"""Stage 27 offline backup and recovery tests."""
import sqlite3
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.backups import BackupManager

@pytest.fixture
def setup(tmp_path):
    store = WardrobeStore(str(tmp_path / 'wardrobe.sqlite3'))
    return store, BackupManager(store.path, str(tmp_path / 'backups'))

def test_create_and_verify(setup):
    store, backups = setup
    store.add('Coat', 'outerwear', 'navy')
    item = backups.create('Before changes')
    assert backups.verify(item['id'])['valid']
    assert backups.preview(item['id'])['backup']['row_counts']['garments'] == 1

def test_restore_requires_confirmation(setup):
    store, backups = setup
    item = backups.create()
    with pytest.raises(ValueError, match='confirmation'):
        backups.restore(item['id'])

def test_restore_and_recovery(setup):
    store, backups = setup
    store.add('Shirt', 'top', 'white')
    item = backups.create()
    store.add('Trousers', 'bottom', 'black')
    result = backups.restore(item['id'], confirm=True)
    assert len(store.list()) == 1
    assert backups.verify(result['recovery_backup_id'])['contents']['row_counts']['garments'] == 2

def test_checksum_tampering(setup):
    _, backups = setup
    item = backups.create()
    db_path, _ = backups._paths(item['id'])
    with db_path.open('ab') as f:
        f.write(b'tamper')
    with pytest.raises(ValueError, match='checksum'):
        backups.verify(item['id'])

def test_reject_path_traversal(setup):
    _, backups = setup
    with pytest.raises(ValueError):
        backups.verify('../outside')

def test_list_and_delete(setup):
    _, backups = setup
    item = backups.create('Snapshot')
    assert any(x['id'] == item['id'] for x in backups.list())
    backups.delete(item['id'])
    assert backups.list() == []
