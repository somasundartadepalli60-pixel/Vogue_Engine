import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.measurements import MeasurementStore, validated

@pytest.fixture
def setup(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'measurements.sqlite3'))
    return wardrobe, MeasurementStore(wardrobe)

def test_profiles_update_and_delete(setup):
    _,s=setup
    p=s.profile('Everyday',{'chest':96,'waist':80},'M')
    assert p['measurements']['chest']==96
    assert len(s.profiles())==1
    updated=s.profile('Everyday',{'chest':98},'L')
    assert updated['id']==p['id'] and updated['measurements']=={'chest':98}
    assert s.delete_profile(p['id'])
    assert s.get_profile(p['id']) is None

def test_measurement_history_and_fit(setup):
    w,s=setup
    garment=w.add('Blue shirt','shirt','blue')
    profile=s.profile('Person',{'chest':95,'waist':80})
    first=s.record(garment['id'],{'chest':97,'waist':84},'2026-01-01','M')
    latest=s.record(garment['id'],{'chest':101,'waist':85},'2026-02-01','L')
    assert [x['id'] for x in s.history(garment['id'])]==[latest['id'],first['id']]
    result=s.compare(garment['id'],profile['id'],ease_cm=3)
    assert result['status']=='meets_requested_ease'
    assert result['dimensions'][0]['difference_cm']==6
    assert s.delete_event(latest['id'])
    assert s.compare(garment['id'],profile['id'],ease_cm=3)['status']=='below_requested_ease'

def test_missing_dimensions_and_missing_records(setup):
    w,s=setup
    g=w.add('Coat','outerwear','black')
    p=s.profile('Person',{'inseam':70})
    with pytest.raises(LookupError): s.compare(g['id'],p['id'])
    s.record(g['id'],{'chest':120},'2026-01-01')
    assert s.compare(g['id'],p['id'])['status']=='insufficient_data'
    with pytest.raises(LookupError): s.record(999,{'chest':100},'2026-01-01')

def test_validation(setup):
    _,s=setup
    for values in ({},{'unknown':10},{'chest':float('nan')},{'waist':-3},{'hip':True},{'chest':401}):
        with pytest.raises(ValueError): validated(values)
    with pytest.raises(ValueError): s.profile('',{'chest':90})
    with pytest.raises(LookupError): s.compare(999,999)

def test_cascade_garment_delete(setup):
    w,s=setup
    g=w.add('Shirt','top','white')
    s.record(g['id'],{'chest':100},'2026-01-01')
    w.delete(g['id'])
    assert s.history(g['id'])==[]
