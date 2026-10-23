from datetime import date
import pytest
from fastapi import HTTPException
from vogue_engine.wardrobe import api,analytics
from vogue_engine.wardrobe.storage import WardrobeStore

def test_wear_history_and_analytics(tmp_path,monkeypatch):
    db=WardrobeStore(str(tmp_path/'test.sqlite3'))
    monkeypatch.setattr(api,'store',lambda:db)
    monkeypatch.setattr(analytics,'store',lambda:db)
    shirt=db.add('Shirt','top','white');pants=db.add('Pants','bottom','black')
    outfit=db.create_outfit('Work',[shirt['id'],pants['id']])
    entry=analytics.log_wear(analytics.WearEntry(outfit_id=outfit['id'],day=date(2026,10,23)))
    assert analytics.analytics()['logged_outfit_wears']==1
    assert db.get(shirt['id'])['wears']==1
    assert len(analytics.wear_log(limit=100))==1
    with pytest.raises(HTTPException) as exc:
        analytics.log_wear(analytics.WearEntry(outfit_id=outfit['id'],day=date(2026,10,23)))
    assert exc.value.status_code==409
    analytics.undo_wear(entry['id'])
    assert db.get(shirt['id'])['wears']==0
    assert analytics.analytics()['logged_outfit_wears']==0

def test_invalid_outfit(tmp_path,monkeypatch):
    db=WardrobeStore(str(tmp_path/'test.sqlite3'))
    monkeypatch.setattr(analytics,'store',lambda:db)
    with pytest.raises(HTTPException) as exc:
        analytics.log_wear(analytics.WearEntry(outfit_id=999,day=date(2026,10,23)))
    assert exc.value.status_code==404
