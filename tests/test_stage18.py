import pytest
from vogue_engine.wardrobe.bulk_photos import BulkPhotoService
from vogue_engine.wardrobe.photos import PhotoLibrary

def test_bulk_captions_and_delete(tmp_path):
    lib=PhotoLibrary(root=tmp_path/'images',database=tmp_path/'db.sqlite3')
    with lib.connect() as db:
        db.execute('CREATE TABLE garments(id INTEGER PRIMARY KEY)')
        db.execute('INSERT INTO garments(id) VALUES (1)')
        db.execute("INSERT INTO garment_photos(garment_id,digest,caption) VALUES (1,'a','one'),(1,'b','two')")
        db.commit()
    service=BulkPhotoService(lib)
    assert service.update_captions([1,2],'new')=={'updated':2}
    assert all(p['caption']=='new' for p in lib.list())
    with pytest.raises(LookupError):service.delete([1,99])
    assert len(lib.list())==2
    assert service.delete([1,2])=={'deleted':2}
    assert lib.list()==[]

def test_bulk_validation(tmp_path):
    lib=PhotoLibrary(root=tmp_path/'images',database=tmp_path/'db.sqlite3')
    service=BulkPhotoService(lib)
    for ids in [[],[1,1],[0],[True],list(range(1,102))]:
        with pytest.raises(ValueError):service.validate_ids(ids)
