"""Deterministic, offline perceptual image similarity for garment photos.

Uses a difference hash for structural similarity and an RGB histogram for color.
No pretrained models, network access, API keys, or environment files are needed.
"""
from __future__ import annotations
from functools import lru_cache
from PIL import Image, ImageOps
from .photos import PhotoLibrary


def fingerprint(path):
    """Return a 64-bit difference hash and a normalized 48-bin color histogram."""
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert('RGB')
        gray = image.convert('L').resize((9, 8), Image.Resampling.LANCZOS)
        pixels = list(gray.getdata())
        bits = 0
        for y in range(8):
            for x in range(8):
                bits = (bits << 1) | int(pixels[y * 9 + x] > pixels[y * 9 + x + 1])
        reduced = image.resize((64, 64), Image.Resampling.BILINEAR)
        bins = [0] * 48
        for r, g, b in reduced.getdata():
            bins[r // 16] += 1
            bins[16 + g // 16] += 1
            bins[32 + b // 16] += 1
        scale = 64 * 64 * 3
        return bits, tuple(v / scale for v in bins)


def compare(first, second):
    """Similarity in [0,1], blending shape and color; heuristic, not garment identity."""
    hash_a, hist_a = first
    hash_b, hist_b = second
    shape = 1 - ((hash_a ^ hash_b).bit_count() / 64)
    color = sum(min(a, b) for a, b in zip(hist_a, hist_b))
    return round(0.6 * shape + 0.4 * color, 6)


class SimilaritySearch:
    def __init__(self, library: PhotoLibrary):
        self.library = library

    def search(self, photo_id: int, limit: int = 10, minimum: float = 0.0, include_same_garment: bool = True):
        if not 1 <= limit <= 100:
            raise ValueError('limit must be between 1 and 100')
        if not 0 <= minimum <= 1:
            raise ValueError('minimum must be between 0 and 1')
        target = self.library.get(photo_id)
        if target is None:
            raise LookupError('Photo not found')
        reference = fingerprint(self.library.path_for(photo_id))
        results = []
        for photo in self.library.list():
            if photo['id'] == photo_id:
                continue
            if not include_same_garment and photo['garment_id'] == target['garment_id']:
                continue
            path = self.library.path_for(photo['id'])
            if not path.is_file():
                continue
            score = compare(reference, fingerprint(path))
            if score >= minimum:
                results.append({'photo_id': photo['id'], 'garment_id': photo['garment_id'],
                                'caption': photo['caption'], 'score': score,
                                'exact_duplicate': photo['digest'] == target['digest']})
        results.sort(key=lambda result: (-result['score'], result['photo_id']))
        return {'query_photo_id': photo_id, 'results': results[:limit], 'total_matches': len(results),
                'method': '64-bit difference hash and 48-bin RGB histogram (heuristic)'}

    def duplicate_candidates(self, minimum: float = 0.95, limit: int = 100):
        if not 0 <= minimum <= 1 or not 1 <= limit <= 100:
            raise ValueError('minimum must be 0..1 and limit must be 1..100')
        photos = self.library.list()
        signatures = {}
        for photo in photos:
            path = self.library.path_for(photo['id'])
            if path.is_file():
                signatures[photo['id']] = fingerprint(path)
        matches = []
        for index, left in enumerate(photos):
            for right in photos[index + 1:]:
                if left['id'] not in signatures or right['id'] not in signatures:
                    continue
                score = compare(signatures[left['id']], signatures[right['id']])
                if score >= minimum:
                    matches.append({'photo_ids': [left['id'], right['id']], 'score': score,
                                    'exact_duplicate': left['digest'] == right['digest']})
        matches.sort(key=lambda row: (-row['score'], row['photo_ids']))
        return {'pairs': matches[:limit], 'total_pairs': len(matches)}
