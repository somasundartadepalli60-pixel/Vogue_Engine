"""Deterministic local image palette extraction and similarity search."""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from PIL import Image


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0,min(255,int(c))):02x}" for c in rgb)


def hex_to_rgb(value):
    if not isinstance(value, str) or len(value) != 7 or not value.startswith("#"):
        raise ValueError("Expected a six-digit hex color such as #ff8800")
    try:
        return tuple(int(value[i:i+2], 16) for i in (1,3,5))
    except ValueError as exc:
        raise ValueError("Invalid hex color") from exc


def palette_for_image(path, count=5):
    """Find common colors after resizing and adaptive palette quantization."""
    if not 1 <= count <= 12:
        raise ValueError("count must be between 1 and 12")
    with Image.open(path) as source:
        image = source.convert("RGB")
        image.thumbnail((160, 160))
        quantized = image.quantize(colors=min(16, max(6, count * 2)), method=Image.Quantize.MEDIANCUT)
        colors = quantized.getpalette()
        totals = quantized.getcolors(maxcolors=256) or []
        totals.sort(reverse=True)
        pixels = sum(amount for amount, _ in totals)
        results = []
        for amount, index in totals[:count]:
            rgb = tuple(colors[index*3:index*3+3])
            results.append({"hex": rgb_to_hex(rgb), "rgb": list(rgb), "percentage": round(100 * amount / pixels, 2)})
        return results


def color_distance(first, second):
    """Weighted RGB distance; heuristic, not perceptual Delta E."""
    a, b = hex_to_rgb(first), hex_to_rgb(second)
    return round(sum(weight*(x-y)**2 for x,y,weight in zip(a,b,(0.30,0.59,0.11)))**0.5, 3)


def search_photos(library, color, limit=20, garment_id=None):
    hex_to_rgb(color)
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    matches = []
    for photo in library.list(garment_id):
        path = library.path_for(photo["id"])
        if not path.is_file():
            continue
        palette = palette_for_image(path)
        distance = min(color_distance(color, item["hex"]) for item in palette)
        matches.append({"photo": photo, "distance": distance, "palette": palette})
    return sorted(matches, key=lambda item: (item["distance"], item["photo"]["id"]))[:limit]
