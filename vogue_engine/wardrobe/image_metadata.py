"""Explainable, offline garment photo metadata suggestions.

This is a heuristic analyzer, NOT a trained garment classifier. Its category
suggestions rely on optional user captions; pixels provide color and geometry.
"""
from __future__ import annotations
import re
from collections import Counter
from pathlib import Path
from PIL import Image, ImageOps
from .color_analysis import palette_for_image

CATEGORIES = {
    "shirt": ("shirt", "tshirt", "t-shirt", "tee", "blouse", "top"),
    "trousers": ("trouser", "trousers", "pants", "jeans", "chinos"),
    "dress": ("dress", "gown", "frock"),
    "skirt": ("skirt",),
    "jacket": ("jacket", "coat", "blazer", "hoodie"),
    "footwear": ("shoe", "shoes", "sneaker", "sneakers", "boots", "boot", "sandal"),
    "accessory": ("belt", "hat", "cap", "scarf", "bag", "watch"),
}
SEASONS = {"winter": ("wool", "thermal", "winter", "coat", "fleece"),
           "summer": ("summer", "linen", "cotton", "shorts"),
           "rainy": ("rain", "waterproof", "raincoat")}

def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+(?:-[a-z]+)?", (text or "").lower()))

def caption_suggestions(caption: str) -> dict:
    words = _tokens(caption)
    scores = {category: len(words.intersection(terms)) for category, terms in CATEGORIES.items()}
    best = max(scores, key=scores.get)
    category = best if scores[best] else None
    season = next((name for name, terms in SEASONS.items() if words.intersection(terms)), None)
    return {"category": category, "season": season,
            "category_confidence": "caption_keyword" if category else "unknown",
            "evidence": sorted(words.intersection(CATEGORIES.get(category, ()))) if category else []}

def suggest_photo(path: str | Path, caption: str = "") -> dict:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image)
        width, height = image.size
        if not width or not height:
            raise ValueError("Invalid image dimensions")
        geometry = {"width": width, "height": height,
                    "orientation": "portrait" if height > width else "landscape" if width > height else "square"}
    palette = palette_for_image(path, 5)
    return {"suggestions": caption_suggestions(caption), "geometry": geometry,
            "palette": palette, "method": "caption_keywords_and_image_colors",
            "limitations": "Garment category is inferred only from caption keywords; no trained visual classifier is bundled."}
