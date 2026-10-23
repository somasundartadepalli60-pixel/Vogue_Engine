from io import BytesIO
from PIL import Image
import pytest
from vogue_engine.wardrobe.color_analysis import rgb_to_hex, hex_to_rgb, palette_for_image, color_distance, search_photos
from vogue_engine.wardrobe.photos import PhotoLibrary


def test_color_conversion():
    assert rgb_to_hex((255, 0, 128)) == "#ff0080"
    assert hex_to_rgb("#ff0080") == (255, 0, 128)

@pytest.mark.parametrize("bad", ["red", "#gg0000", "#fff", "123456"])
def test_bad_color(bad):
    with pytest.raises(ValueError): hex_to_rgb(bad)

def test_palette(tmp_path):
    path = tmp_path / "image.png"
    Image.new("RGB", (30, 30), (240, 10, 10)).save(path)
    palette = palette_for_image(path)
    assert palette[0]["percentage"] > 99
    assert color_distance("#ff0000", "#ff0000") == 0

def test_missing_photo_search(tmp_path):
    database = tmp_path / "data.sqlite3"
    lib = PhotoLibrary(tmp_path / "images", database)
    assert search_photos(lib, "#123456") == []

def test_bad_limit(tmp_path):
    lib = PhotoLibrary(tmp_path / "images", tmp_path / "data.sqlite3")
    with pytest.raises(ValueError): search_photos(lib, "#ffffff", 0)
