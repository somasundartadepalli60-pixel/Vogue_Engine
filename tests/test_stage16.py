from PIL import Image
from vogue_engine.wardrobe.image_metadata import caption_suggestions, suggest_photo

def test_caption_category():
    result = caption_suggestions("Blue cotton shirt")
    assert result["category"] == "shirt"
    assert result["season"] == "summer"

def test_unknown_caption():
    assert caption_suggestions("beautiful blue item")["category"] is None

def test_no_false_visual_classification(tmp_path):
    path = tmp_path / "photo.png"
    Image.new("RGB", (40, 80), "blue").save(path)
    result = suggest_photo(path)
    assert result["suggestions"]["category"] is None
    assert result["geometry"]["orientation"] == "portrait"
    assert result["palette"]

def test_explicit_keyword(tmp_path):
    path = tmp_path / "shoe.png"
    Image.new("RGB", (40, 40), "red").save(path)
    assert suggest_photo(path, "Red sneakers")["suggestions"]["category"] == "footwear"
