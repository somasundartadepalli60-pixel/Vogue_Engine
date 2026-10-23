from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.audit import InventoryAuditor
import pytest

@pytest.fixture
def setup(tmp_path):
    w=WardrobeStore(str(tmp_path/'audit.sqlite3'))
    return w,InventoryAuditor(w)

def test_compare_verification_changes(setup):
    w,a=setup
    g=w.add('Blue jacket','outerwear','blue')
    first=a.start('first')['id']
    second=a.start('second')['id']
    a.confirm(second,g['id'])
    result=a.compare(first,second)
    assert len(result['newly_confirmed'])==1
    assert result['earlier_confirmed']==0 and result['later_confirmed']==1

def test_compare_snapshot_added_removed(setup):
    w,a=setup
    old=w.add('Old','top','red')
    first=a.start('first')['id']
    w.delete(old['id'])
    new=w.add('New','top','green')
    second=a.start('second')['id']
    result=a.compare(first,second)
    assert [x['garment_id'] for x in result['removed']]==[old['id']]
    assert [x['garment_id'] for x in result['added']]==[new['id']]

def test_compare_unknown_audit(setup):
    _,a=setup
    with pytest.raises(LookupError):a.compare(999,1000)

def test_dashboard_present():
    from pathlib import Path
    page=Path(__file__).resolve().parents[1]/'vogue_engine/wardrobe/static/stage26.html'
    assert 'Wardrobe inventory audits' in page.read_text()
