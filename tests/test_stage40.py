from fastapi.testclient import TestClient
from vogue_engine.wardrobe.outfit_engine import color_compatibility, recommend_combinations
from vogue_engine.dashboards.router import app


def garment(i, category, color, **kwargs):
    return dict(id=i, name=f'Item {i}', category=category, color=color, season='all', occasion='casual', **kwargs)


def test_symmetric_colors():
    assert color_compatibility('White', 'navy') == color_compatibility('navy', 'WHITE')


def test_recommendations_sorted_and_explainable():
    items = [garment(1, 'shirt', 'white'), garment(2, 'jeans', 'navy'),
             garment(3, 'sneakers', 'black'), garment(4, 'shirt', 'purple')]
    results = recommend_combinations(items)
    assert len(results) == 2
    assert results[0]['score'] >= results[1]['score']
    assert results[0]['reasons']
    assert len(set(results[0]['garment_ids'])) == 3


def test_missing_group_returns_empty():
    assert recommend_combinations([garment(1, 'shirt', 'white')]) == []


def test_season_filter_and_exclusion():
    items = [garment(1, 'shirt', 'white'), garment(2, 'jeans', 'navy'), garment(3, 'sneakers', 'black')]
    assert recommend_combinations(items, exclude_ids=[2]) == []
    assert len(recommend_combinations(items, season='winter')) == 1


def test_invalid_limit():
    import pytest
    with pytest.raises(ValueError):
        recommend_combinations([], limit=0)


def test_color_endpoint():
    response = TestClient(app).get('/api/v1/wardrobe/outfit-engine/colors', params={'first':'black', 'second':'white'})
    assert response.status_code == 200
    assert response.json()['score'] > 0


def test_recommendation_endpoint():
    response = TestClient(app).get('/api/v1/wardrobe/outfit-engine/recommendations', params={'limit':3})
    assert response.status_code == 200
    assert isinstance(response.json()['recommendations'], list)
