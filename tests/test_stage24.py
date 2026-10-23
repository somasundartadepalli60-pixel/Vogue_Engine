"""Stage 24 regression coverage for calendar and lending insights."""
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.lending import LendingStore
from vogue_engine.wardrobe.lending_analytics import build_lending_insights

@pytest.fixture
def sample(tmp_path):
    wardrobe = WardrobeStore(str(tmp_path/'wardrobe.db'))
    first = wardrobe.add('Jacket','outerwear','navy')
    second = wardrobe.add('Shirt','top','white')
    service = LendingStore(wardrobe)
    service.create(first['id'],'lent','Alex','2026-10-01','2026-10-10')
    service.create(second['id'],'borrowed','Taylor','2026-10-02','2026-10-27')
    return service

def test_insights_overdue_and_upcoming(sample):
    result=build_lending_insights(sample,'2026-10-23',10)
    assert result['totals']=={'all':2,'active':2,'overdue':1,'upcoming':1,'returned':0}
    assert [x['date'] for x in result['calendar']]==['2026-10-10','2026-10-27']

def test_return_updates_insights(sample):
    sample.return_loan(1,'2026-10-12')
    result=build_lending_insights(sample,'2026-10-23')
    assert result['totals']['overdue']==0
    assert result['totals']['returned']==1

def test_activity_and_contacts(sample):
    result=build_lending_insights(sample,'2026-10-23')
    assert result['monthly_activity']==[{'month':'2026-10','loans':2}]
    assert len(result['frequent_contacts'])==2

@pytest.mark.parametrize('days',[0,-1,367])
def test_invalid_days(sample,days):
    with pytest.raises(ValueError): build_lending_insights(sample,'2026-10-23',days)
