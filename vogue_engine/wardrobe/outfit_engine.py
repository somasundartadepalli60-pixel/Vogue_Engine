"""Stage 40: deterministic, offline, explainable wardrobe outfit ranking."""
from __future__ import annotations
from itertools import product

GROUPS = (
    {'top', 'shirt', 'tshirt', 't-shirt', 'blouse', 'sweater', 'hoodie'},
    {'bottom', 'pants', 'trousers', 'skirt', 'jeans', 'shorts'},
    {'shoes', 'footwear', 'sneakers', 'boots', 'sandals'},
)
NEUTRALS = {'black', 'white', 'grey', 'gray', 'beige', 'cream', 'navy', 'brown'}
COLOR_PAIRS = {
    frozenset(('blue', 'orange')), frozenset(('red', 'green')),
    frozenset(('purple', 'yellow')), frozenset(('navy', 'white')),
    frozenset(('black', 'white')), frozenset(('blue', 'beige')),
    frozenset(('brown', 'cream')), frozenset(('olive', 'cream')),
}
FORMAL = {'formal', 'business', 'office', 'wedding'}


def color_compatibility(a: str, b: str) -> tuple[int, str]:
    """Return a symmetric score and a plain-language explanation."""
    a, b = a.strip().lower(), b.strip().lower()
    if not a or not b:
        return 0, 'Unknown color'
    if a == b:
        return 5, 'Coordinated monochrome colors'
    if frozenset((a, b)) in COLOR_PAIRS:
        return 12, 'Complementary color pairing'
    if a in NEUTRALS or b in NEUTRALS:
        return 8, 'Versatile neutral pairing'
    return 1, 'Distinct accent colors'


def recommend_combinations(garments: list[dict], occasion='casual', season='all', limit=10,
                           exclude_ids: list[int] | None = None) -> list[dict]:
    """Build top/bottom/shoe sets with stable ranking and bounded work.

    The scoring is heuristic, not a claim about personal taste or color science.
    """
    if not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    occasion, season = occasion.strip().lower(), season.strip().lower()
    excluded = set(exclude_ids or [])
    eligible = [g for g in garments if g['id'] not in excluded and
                (season == 'all' or g.get('season', 'all').lower() in ('all', season)) and
                (occasion == 'all' or g.get('occasion', 'casual').lower() in ('all', 'casual', occasion))]
    groups = [[g for g in eligible if g.get('category', '').lower() in cats][:60] for cats in GROUPS]
    if any(not group for group in groups):
        return []
    ranked = []
    for trio in product(*groups):
        if len({g['id'] for g in trio}) != 3:
            continue
        pairs = [(trio[0], trio[1]), (trio[0], trio[2]), (trio[1], trio[2])]
        pair_scores = [color_compatibility(a.get('color', ''), b.get('color', '')) for a, b in pairs]
        color_score = sum(score for score, _ in pair_scores)
        favorites = sum(bool(g.get('favorite')) for g in trio)
        rotation = sum(min(max(int(g.get('wears', 0)), 0), 20) for g in trio)
        matches = sum(g.get('occasion', '').lower() == occasion for g in trio)
        occasion_bonus = matches * (7 if occasion in FORMAL else 4)
        score = max(0, min(100, 40 + color_score + favorites * 5 + occasion_bonus - rotation // 3))
        reasons = sorted({reason for _, reason in pair_scores})
        if favorites:
            reasons.append(f'{favorites} favorite garment(s)')
        if matches:
            reasons.append(f'{matches} occasion match(es)')
        ranked.append({'garment_ids': [g['id'] for g in trio], 'garments': list(trio),
                       'score': score, 'color_score': color_score,
                       'occasion_score': occasion_bonus, 'rotation_penalty': rotation // 3,
                       'reasons': reasons})
    ranked.sort(key=lambda x: (-x['score'], x['garment_ids']))
    return ranked[:limit]
