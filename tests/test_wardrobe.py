import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.planner import suggest_outfits

@pytest.fixture
def wardrobe(tmp_path):return WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))

def test_crud_filters_and_statistics(wardrobe):
    item=wardrobe.add('Oxford','top','white',season='winter')
    assert wardrobe.get(item['id'])['name']=='Oxford'
    assert len(wardrobe.list(season='winter'))==1
    assert wardrobe.list(season='summer')==[]
    assert wardrobe.update(item['id'],favorite=True,wears=2)['favorite']==1
    assert wardrobe.statistics()['total_wears']==2
    assert wardrobe.delete(item['id'])
    assert wardrobe.get(item['id']) is None

def test_outfits_and_cascade(wardrobe):
    a=wardrobe.add('Shirt','top','white')
    b=wardrobe.add('Jeans','bottom','blue')
    outfit=wardrobe.create_outfit('Daily',[a['id'],b['id']])
    assert len(wardrobe.outfits()[0]['garments'])==2
    wardrobe.delete(a['id'])
    assert len(wardrobe.outfits()[0]['garments'])==1
    with pytest.raises(ValueError):wardrobe.create_outfit('Invalid',[999])

def test_planner(wardrobe):
    for name,cat,color in [('White tee','top','white'),('Blue jeans','bottom','blue'),('Black shoes','shoes','black')]:
        wardrobe.add(name,cat,color)
    result=suggest_outfits(wardrobe.list())
    assert len(result)==1
    assert len(result[0]['garment_ids'])==3
    with pytest.raises(ValueError):suggest_outfits([],limit=0)

def test_reject_invalid(wardrobe):
    with pytest.raises(ValueError):wardrobe.add(' ','top','red')
    with pytest.raises(ValueError):wardrobe.update(1,unrecognized=True)
    with pytest.raises(ValueError):wardrobe.create_outfit('x',[])
