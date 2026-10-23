import pytest
from vogue_engine.wardrobe.outfit_feedback import FeedbackStore, signature, apply_feedback


def test_signature_is_order_independent():
    assert signature([3, 1, 2]) == signature([2, 3, 1]) == '1,2,3'

@pytest.mark.parametrize('ids', [[1, 1, 2], [1, 2], [-1, 2, 3], [True, 2, 3]])
def test_signature_rejects_bad_ids(ids):
    with pytest.raises(ValueError):
        signature(ids)

def test_feedback_roundtrip(tmp_path):
    db = FeedbackStore(str(tmp_path / 'wardrobe.db'))
    assert db.save([1, 2, 3], 5, True, 'Great')['rating'] == 5
    assert db.save([3, 2, 1], 2, False)['rating'] == 2
    assert len(db.list()) == 1
    assert db.delete([2, 1, 3])
    assert not db.list()

def test_feedback_persists(tmp_path):
    path = str(tmp_path / 'wardrobe.db')
    FeedbackStore(path).save([1, 2, 3], 4)
    assert FeedbackStore(path).list()[0]['rating'] == 4

def test_feedback_validation(tmp_path):
    db = FeedbackStore(str(tmp_path / 'wardrobe.db'))
    with pytest.raises(ValueError):
        db.save([1, 2, 3], 6)
    with pytest.raises(ValueError):
        db.save([1, 2, 3], 3, notes='x' * 501)

def test_personalized_ranking():
    items = [{'garment_ids':[1,2,3], 'score':60, 'reasons':[]},
             {'garment_ids':[4,5,6], 'score':65, 'reasons':[]}]
    result = apply_feedback(items, [{'signature':'1,2,3', 'rating':5, 'favorite':1}])
    assert result[0]['garment_ids'] == [1,2,3]
    assert result[0]['score'] == 78
    assert items[0]['score'] == 60
