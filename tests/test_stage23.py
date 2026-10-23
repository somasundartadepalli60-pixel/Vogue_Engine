"""Stage 23 lending workflow regression tests."""
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.lending import LendingStore

@pytest.fixture
def setup(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    garment=wardrobe.add('Jacket','outerwear','blue')
    return LendingStore(wardrobe),garment['id']

def test_create_and_return(setup):
    svc,gid=setup
    loan=svc.create(gid,'lent','Alex','2026-10-01','2026-10-10')
    assert svc.summary('2026-10-11')['overdue']==1
    assert svc.return_loan(loan['id'],'2026-10-12')['returned_at']=='2026-10-12'
    assert svc.summary('2026-10-13')['active']==0
    assert [x['event'] for x in svc.history(loan['id'])]==['created','returned']

def test_duplicate_active_loan_rejected(setup):
    svc,gid=setup
    svc.create(gid,'lent','Alex','2026-10-01','2026-10-10')
    with pytest.raises(ValueError,match='active loan'):
        svc.create(gid,'borrowed','Taylor','2026-10-02','2026-10-12')

def test_invalid_dates_and_direction(setup):
    svc,gid=setup
    with pytest.raises(ValueError): svc.create(gid,'lent','Alex','2026-10-12','2026-10-01')
    with pytest.raises(ValueError): svc.create(gid,'unknown','Alex','2026-10-01','2026-10-12')

def test_extend_and_filter(setup):
    svc,gid=setup
    loan=svc.create(gid,'borrowed','Alex','2026-10-01','2026-10-10')
    svc.extend(loan['id'],'2026-10-20')
    assert svc.list(overdue_only=True,today='2026-10-15')==[]
    assert len(svc.list(direction='borrowed',active_only=True))==1
    assert svc.history(loan['id'])[-1]['event']=='due_date_changed'

def test_cannot_return_twice(setup):
    svc,gid=setup
    loan=svc.create(gid,'lent','Alex','2026-10-01','2026-10-10')
    svc.return_loan(loan['id'],'2026-10-09')
    with pytest.raises(ValueError,match='already returned'):
        svc.return_loan(loan['id'],'2026-10-09')
