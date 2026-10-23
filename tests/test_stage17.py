import io
import pytest
from PIL import Image
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.photos import PhotoLibrary
from vogue_engine.wardrobe.similarity import SimilaritySearch, compare, fingerprint

@pytest.fixture
def setup(tmp_path):
    db = tmp_path / 'wardrobe.sqlite3'
    store = WardrobeStore(str(db))
    first = store.add('Blue shirt', 'tops', 'blue')['id']
    second = store.add('Red shirt', 'tops', 'red')['id']
    lib = PhotoLibrary(tmp_path / 'photos', db)
    def upload(garment, color):
        stream = io.BytesIO()
        Image.new('RGB', (48, 48), color).save(stream, 'PNG')
        return lib.add(garment, stream.getvalue())
    return lib, first, second, upload

def test_identical_fingerprint(setup):
    lib, first, second, upload = setup
    a = upload(first, 'blue')
    b = upload(second, 'blue')
    assert compare(fingerprint(lib.path_for(a['id'])), fingerprint(lib.path_for(b['id']))) == 1

def test_search_ranking_and_excludes_self(setup):
    lib, first, second, upload = setup
    a = upload(first, 'blue')
    b = upload(second, 'blue')
    c = upload(second, 'red')
    result = SimilaritySearch(lib).search(a['id'])
    assert result['results'][0]['photo_id'] == b['id']
    assert a['id'] not in [item['photo_id'] for item in result['results']]

def test_missing_photo(setup):
    lib, *_ = setup
    with pytest.raises(LookupError):
        SimilaritySearch(lib).search(12345)

def test_invalid_ranges(setup):
    lib, *_ = setup
    with pytest.raises(ValueError):
        SimilaritySearch(lib).duplicate_candidates(minimum=2)
    with pytest.raises(ValueError):
        SimilaritySearch(lib).search(1, limit=0)

def test_duplicate_candidates(setup):
    lib, first, second, upload = setup
    a = upload(first, 'blue')
    b = upload(second, 'blue')
    result = SimilaritySearch(lib).duplicate_candidates()
    assert result['total_pairs'] == 1
    assert result['pairs'][0]['exact_duplicate']

def test_exclude_same_garment(setup):
    lib, first, second, upload = setup
    a = upload(first, 'blue')
    upload(first, 'red')
    b = upload(second, 'green')
    result = SimilaritySearch(lib).search(a['id'], include_same_garment=False)
    assert [item['photo_id'] for item in result['results']] == [b['id']]
