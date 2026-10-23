import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.finance import FinanceStore,minor_units

@pytest.fixture
def ledger(tmp_path):
    w=WardrobeStore(str(tmp_path/'wardrobe.db'))
    return w,FinanceStore(w)

def test_purchase_and_cost_per_wear(ledger):
    w,f=ledger
    g=w.add('Blue shirt','shirt','blue')
    p=f.set_purchase(g['id'],'999.99','2026-10-23','Local shop')
    assert p['amount']==999.99 and p['cost_per_wear'] is None
    w.update(g['id'],wears=3)
    assert f.get_purchase(g['id'])['cost_per_wear']==333.33

def test_budget_and_summary(ledger):
    w,f=ledger
    g=w.add('Shirt','top','red')
    f.set_purchase(g['id'],'750','2026-10-23')
    assert f.set_budget('2026-10','1000')['remaining']==250
    assert f.set_budget('2026-10','500')['over_budget'] is True

def test_purchase_upsert(ledger):
    w,f=ledger; g=w.add('Shirt','top','red')
    f.set_purchase(g['id'],'50','2026-01-01')
    f.set_purchase(g['id'],'75','2026-02-01')
    assert len(f.purchases())==1 and f.purchases('2026-02')[0]['amount']==75

def test_delete_cascades(ledger):
    w,f=ledger;g=w.add('Shirt','top','red')
    f.set_purchase(g['id'],'20','2026-01-01');w.delete(g['id'])
    assert f.purchases()==[]

def test_invalid_inputs(ledger):
    _,f=ledger
    for value in ('NaN','-1','Infinity','nope'):
        with pytest.raises(ValueError): minor_units(value)
    with pytest.raises(ValueError): f.set_budget('2026-99','100')
    with pytest.raises(ValueError): f.set_budget('2026-01','100','USD')
    with pytest.raises(LookupError): f.set_purchase(999,'10','2026-01-01')

def test_overview(ledger):
    w,f=ledger;g=w.add('Jacket','outerwear','black');w.update(g['id'],wears=2)
    f.set_purchase(g['id'],'1200','2026-01-02')
    assert f.overview()['best_value'][0]['cost_per_wear']==600
