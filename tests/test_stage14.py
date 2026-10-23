import io
import pytest
from PIL import Image
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.photos import PhotoLibrary

@pytest.fixture
def gallery(tmp_path):
    db=tmp_path/'wardrobe.sqlite3'
    garment=WardrobeStore(str(db)).add('Jacket','outerwear','blue')
    return PhotoLibrary(tmp_path/'photos', db),garment['id']

def picture(color='red'):
    image=Image.new('RGB',(32,32),color)
    buffer=io.BytesIO()
    image.save(buffer,format='PNG')
    return buffer.getvalue()

def test_upload_and_list(gallery):
    lib,gid=gallery
    photo=lib.add(gid,picture(),'Front view')
    assert lib.list(gid)[0]['id']==photo['id']
    assert lib.path_for(photo['id']).is_file()

def test_deduplication(gallery):
    lib,gid=gallery
    assert lib.add(gid,picture())['id']==lib.add(gid,picture())['id']

def test_reject_invalid_image(gallery):
    lib,gid=gallery
    with pytest.raises(ValueError):lib.add(gid,b'not an image')

def test_reject_missing_garment(gallery):
    lib,_=gallery
    with pytest.raises(LookupError):lib.add(999,picture())

def test_edit_and_remove(gallery):
    lib,gid=gallery
    photo=lib.add(gid,picture())
    assert lib.update_caption(photo['id'],'Side')['caption']=='Side'
    path=lib.path_for(photo['id'])
    assert lib.remove(photo['id']) is True
    assert not path.exists()
    assert lib.remove(photo['id']) is False

def test_size_limit(gallery):
    lib,gid=gallery
    with pytest.raises(ValueError):lib.add(gid,b'x'*(8*1024*1024+1))
