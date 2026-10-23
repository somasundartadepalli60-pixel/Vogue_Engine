"""Tests for Stage 12 recommendation ranking and persistence."""
import pytest
from vogue_engine.wardrobe.recommendation import rank_outfits, signature, save_feedback, feedback_counts, list_feedback, delete_feedback
from vogue_engine.wardrobe.api import store


def sample():
    return [
        {'id': 1, 'name': 'Shirt', 'category': 'top', 'color': 'white', 'season': 'all', 'occasion': 'casual', 'wears': 0, 'favorite': 1},
        {'id': 2, 'name': 'Jeans', 'category': 'bottom', 'color': 'black', 'season': 'all', 'occasion': 'casual', 'wears': 2, 'favorite': 0},
        {'id': 3, 'name': 'Shoes', 'category': 'shoes', 'color': 'blue', 'season': 'all', 'occasion': 'casual', 'wears': 0, 'favorite': 0},
    ]


def preferences():
    return {'preferred_colors': ['white'], 'avoided_colors': [], 'preferred_categories': [], 'prefer_favorites': True, 'prioritize_unworn': True}


def test_signature_sorted():
    assert signature([3, 1, 2]) == '1,2,3'


@pytest.mark.parametrize('ids', [[1, 1, 2], [0, 2, 3], [1, 2], [True, 2, 3]])
def test_invalid_signature(ids):
    with pytest.raises(ValueError):
        signature(ids)


def test_explainable_scoring():
    result = rank_outfits(sample(), preferences(), {}, limit=1)
    assert result[0]['garment_ids'] == [1, 2, 3]
    assert sum(result[0]['score_breakdown'].values()) >= result[0]['score']
    assert result[0]['reasons']


def test_feedback_changes_score():
    base = rank_outfits(sample(), preferences(), {}, limit=1)[0]['score']
    liked = rank_outfits(sample(), preferences(), {'1,2,3': {'liked': 1}}, limit=1)[0]['score']
    disliked = rank_outfits(sample(), preferences(), {'1,2,3': {'disliked': 2}}, limit=1)[0]['score']
    assert liked >= base > disliked


def test_avoided_color():
    prefs = preferences()
    prefs['avoided_colors'] = ['white']
    assert rank_outfits(sample(), prefs, {}, limit=1) == []


def test_season_filter():
    garments = sample()
    garments[0]['season'] = 'winter'
    assert rank_outfits(garments, preferences(), {}, season='summer') == []


def test_invalid_limit():
    with pytest.raises(ValueError):
        rank_outfits(sample(), preferences(), {}, limit=0)


def test_feedback_persistence(tmp_path, monkeypatch):
    from vogue_engine.wardrobe.storage import WardrobeStore
    from vogue_engine.wardrobe import recommendation
    local = WardrobeStore(str(tmp_path / 'feedback.sqlite3'))
    for garment in sample():
        local.add(garment['name'], garment['category'], garment['color'])
    monkeypatch.setattr(recommendation, 'store', lambda: local)
    record = save_feedback([3, 1, 2], 'liked', 'Nice combination')
    assert feedback_counts()['1,2,3']['liked'] == 1
    assert list_feedback(50)[0]['garment_ids'] == [1, 2, 3]
    assert delete_feedback(record['id']) == {'deleted': True}
    assert feedback_counts() == {}


def test_unknown_garment(tmp_path, monkeypatch):
    from vogue_engine.wardrobe.storage import WardrobeStore
    from vogue_engine.wardrobe import recommendation
    monkeypatch.setattr(recommendation, 'store', lambda: WardrobeStore(str(tmp_path / 'empty.sqlite3')))
    with pytest.raises(ValueError):
        save_feedback([1, 2, 3], 'liked')
