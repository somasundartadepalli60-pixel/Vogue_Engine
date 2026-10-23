import pytest
from vogue_engine.wardrobe.personalization import Preferences, personalized_suggestions, save_preferences, read_preferences
from vogue_engine.wardrobe import personalization
from vogue_engine.wardrobe.storage import WardrobeStore

@pytest.fixture
def local_store(tmp_path, monkeypatch):
    instance = WardrobeStore(str(tmp_path / 'test.sqlite3'))
    monkeypatch.setattr(personalization, 'store', lambda: instance)
    return instance

def test_preferences_roundtrip(local_store):
    saved = save_preferences(Preferences(preferred_colors=[' NAVY ', 'navy'], season='winter'))
    assert saved['preferred_colors'] == ['navy']
    assert read_preferences() == saved

def test_conflicting_colors_rejected():
    with pytest.raises(ValueError):
        Preferences(preferred_colors=['red'], avoided_colors=['RED']).normalized()

def test_unknown_season_rejected():
    with pytest.raises(ValueError):
        Preferences(season='monsoon').normalized()

def test_avoided_colors_removed(local_store):
    items = [local_store.add('Top','top','red'), local_store.add('Other Top','top','navy'), local_store.add('Pants','bottom','white'), local_store.add('Shoes','shoes','black')]
    results = personalized_suggestions(items, Preferences(avoided_colors=['red'],preferred_colors=['navy']).normalized())
    assert results and all(items[0]['id'] not in r['garment_ids'] for r in results)
    assert any('preferred color' in reason for reason in results[0]['reasons'])

def test_limit_validation():
    with pytest.raises(ValueError):
        personalized_suggestions([], Preferences().normalized(), limit=101)

def test_empty_wardrobe():
    assert personalized_suggestions([], Preferences().normalized()) == []
