import io
import json
import sqlite3
import zipfile
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe import portability as p

@pytest.fixture
def wardrobe(tmp_path):
    path = str(tmp_path / 'wardrobe.sqlite3')
    store = WardrobeStore(path)
    store.add('Blue shirt', 'tops', 'blue')
    return path

def test_json_export(wardrobe):
    result = json.loads(p.json_bytes(wardrobe))
    assert result['format'] == 'vogue-wardrobe-v1'
    assert result['tables']['garments'][0]['name'] == 'Blue shirt'

def test_csv_export(wardrobe):
    assert b'Blue shirt' in p.csv_bytes(wardrobe)
    with pytest.raises(ValueError): p.csv_bytes(wardrobe, 'sqlite_master')

def test_zip_export(wardrobe):
    with zipfile.ZipFile(io.BytesIO(p.archive_bytes(wardrobe))) as z:
        assert set(z.namelist()) == {'wardrobe.json','garments.csv','outfits.csv','outfit_garments.csv'}

def test_preview_and_confirmed_import(wardrobe):
    data = p.json_bytes(wardrobe)
    assert p.preview_import(data)['garment_count'] == 1
    with pytest.raises(ValueError): p.import_garments(wardrobe, data)
    assert p.import_garments(wardrobe, data, confirm=True)['imported'] == 1
    assert len(WardrobeStore(wardrobe).list()) == 2

def test_invalid_import_rejected(wardrobe):
    for data in (b'not json', b'{}', b'{"format":"vogue-wardrobe-v1","tables":{"garments":[{}]}}'):
        with pytest.raises(ValueError): p.preview_import(data)

def test_import_limit():
    with pytest.raises(ValueError): p.validate_import(b'x' * (p.MAX_IMPORT_BYTES + 1))
