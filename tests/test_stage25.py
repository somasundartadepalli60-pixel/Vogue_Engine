"""Inventory audit regression tests."""
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.audit import InventoryAuditor

@pytest.fixture
def auditor(tmp_path):
    wardrobe = WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    return wardrobe, InventoryAuditor(wardrobe)

def test_snapshot_and_missing(auditor):
    wardrobe, audit = auditor
    garment = wardrobe.add('Jacket','outerwear','black')
    snapshot = audit.start('October inventory')
    assert snapshot['total'] == 1 and snapshot['missing'] == 1
    assert snapshot['items'][0]['garment_id'] == garment['id']
    assert audit.list()[0]['total'] == 1

def test_confirm_and_reverse(auditor):
    wardrobe,audit=auditor
    garment=wardrobe.add('Shirt','top','white')
    id_=audit.start('Physical check')['id']
    assert audit.confirm(id_,garment['id'])['missing'] == 0
    assert audit.confirm(id_,garment['id'],False)['missing'] == 1

def test_snapshot_immutable_when_inventory_changes(auditor):
    wardrobe,audit=auditor
    first=wardrobe.add('Coat','outerwear','blue')
    id_=audit.start('Baseline')['id']
    wardrobe.add('New shoes','shoes','red')
    wardrobe.delete(first['id'])
    result=audit.get(id_)
    assert result['total'] == 1
    assert result['items'][0]['still_in_wardrobe'] == 0

def test_integrity_clean(auditor):
    wardrobe,audit=auditor
    wardrobe.add('Hat','accessory','green')
    result=audit.integrity()
    assert result['ok'] and result['garment_count']==1

def test_validation(auditor):
    wardrobe,audit=auditor
    with pytest.raises(ValueError): audit.start(' ')
    with pytest.raises(LookupError): audit.get(999)
    id_=audit.start('Empty')['id']
    with pytest.raises(LookupError): audit.confirm(id_,123)
