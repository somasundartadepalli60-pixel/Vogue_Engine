"""Stage 6 persistence, search, and integrity tests."""
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.organization import OrganizationStore

@pytest.fixture
def data(tmp_path):
    db=WardrobeStore(str(tmp_path/'test.sqlite3'))
    org=OrganizationStore(db)
    a=db.add('Blue Shirt','top','blue',season='summer')
    b=db.add('Black Jeans','bottom','black',season='all')
    return db,org,a,b

def test_collections_and_items(data):
    db,org,a,b=data
    c=org.create_collection('Travel','Packing')
    assert org.collections()[0]['item_count']==0
    org.set_collection_items(c['id'],[a['id'],b['id']])
    assert len(org.collection_items(c['id']))==2
    assert org.collections()[0]['item_count']==2

def test_invalid_items_rollback(data):
    db,org,a,b=data
    c=org.create_collection('Work')
    org.set_collection_items(c['id'],[a['id']])
    with pytest.raises(ValueError): org.set_collection_items(c['id'],[99999])
    assert len(org.collection_items(c['id']))==1
    with pytest.raises(ValueError): org.set_collection_items(c['id'],[a['id'],a['id']])

def test_tags_search(data):
    db,org,a,b=data
    assert org.set_tags(a['id'],['Formal','Travel','formal'])==['formal','travel']
    assert org.search(tag='formal')['total']==1
    assert org.search(query='Blue')['items'][0]['id']==a['id']
    assert org.search(query='%')['total']==0
    assert org.tags()[0]['garment_count']==1

def test_pagination_filters(data):
    db,org,a,b=data
    assert org.search(limit=1)['total']==2
    assert len(org.search(limit=1,offset=1)['items'])==1
    assert org.search(color='blue')['total']==1
    assert org.search(season='winter')['total']==1
    assert org.search(max_wears=0)['total']==2
    with pytest.raises(ValueError): org.search(sort='DROP TABLE garments')

def test_cascade_and_reopen(data):
    db,org,a,b=data
    c=org.create_collection('Favorites')
    org.set_collection_items(c['id'],[a['id']]);org.set_tags(a['id'],['keep'])
    reopened=OrganizationStore(WardrobeStore(db.path))
    assert len(reopened.collection_items(c['id']))==1
    db.delete(a['id'])
    assert reopened.collection_items(c['id'])==[]
    assert reopened.tags()==[]

def test_breakdown(data):
    db,org,a,b=data
    report=org.breakdown()
    assert report['total']==2 and report['unworn']==2
    assert report['by_color']=={'black':1,'blue':1}
