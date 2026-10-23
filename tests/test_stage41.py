from fastapi.testclient import TestClient
from vogue_engine.dashboards.router import app
from vogue_engine.wardrobe.outfit_dashboard_api import save_recommendation, SaveRecommendation
from fastapi import HTTPException
from unittest.mock import patch

client = TestClient(app)

def test_dashboard_available():
    response = client.get('/wardrobe/outfit-engine')
    assert response.status_code == 200
    assert 'Outfit Studio' in response.text
    assert '/recommendations' in response.text

def test_save_rejects_duplicates():
    with __import__('pytest').raises(HTTPException) as exc:
        save_recommendation(SaveRecommendation(garment_ids=[1,1,2],name='test'))
    assert exc.value.status_code == 422

def test_save_rejects_missing_garments():
    with patch('vogue_engine.wardrobe.outfit_dashboard_api.store') as mocked:
        mocked.return_value.list.return_value = []
        with __import__('pytest').raises(HTTPException) as exc:
            save_recommendation(SaveRecommendation(garment_ids=[1,2,3],name='test'))
        assert exc.value.status_code == 404

def test_save_valid_combination():
    garments=[dict(id=i,name=str(i),category=cat,color=color,season='all',occasion='casual') for i,cat,color in [(1,'shirt','white'),(2,'jeans','navy'),(3,'shoes','black')]]
    with patch('vogue_engine.wardrobe.outfit_dashboard_api.store') as mocked:
        mocked.return_value.list.return_value=garments
        mocked.return_value.create_outfit.return_value={'id':9,'name':'My Look'}
        result=save_recommendation(SaveRecommendation(garment_ids=[1,2,3],name='My Look'))
        assert result['id']==9
        mocked.return_value.create_outfit.assert_called_once()
