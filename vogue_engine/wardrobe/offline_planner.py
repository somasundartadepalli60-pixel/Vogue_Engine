"""Dependency-free, deterministic outfit planner for local use."""
from dataclasses import dataclass
from itertools import product

CATEGORIES = ("top", "bottom", "shoes")
NEUTRALS = frozenset(("black", "white", "gray", "grey", "beige", "navy", "brown"))

@dataclass(frozen=True)
class Garment:
    name: str
    category: str
    color: str
    seasons: tuple[str, ...] = ()
    occasions: tuple[str, ...] = ()

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Garment name cannot be empty")
        if self.category not in CATEGORIES:
            raise ValueError(f"Unsupported category: {self.category}")
        if not self.color.strip():
            raise ValueError("Garment color cannot be empty")


def score_outfit(items: tuple[Garment, ...], season: str = "", occasion: str = "") -> int:
    """Return a reproducible score between zero and one hundred."""
    if len(items) != 3 or {item.category for item in items} != set(CATEGORIES):
        raise ValueError("Outfit requires one top, bottom, and pair of shoes")
    score = 40
    for item in items:
        if season and (not item.seasons or season in item.seasons):
            score += 10
        if occasion and (not item.occasions or occasion in item.occasions):
            score += 10
    colors = [item.color.lower() for item in items]
    score += 15 if len(set(colors)) <= 2 else 0
    score += 15 if sum(color in NEUTRALS for color in colors) >= 2 else 0
    return min(100, score)


def recommend(garments: list[Garment], season: str = "", occasion: str = "", limit: int = 10):
    """Rank valid combinations by score, with stable lexical tie-breaking."""
    if limit < 1 or limit > 1000:
        raise ValueError("limit must be between 1 and 1000")
    groups = [[g for g in garments if g.category == cat] for cat in CATEGORIES]
    ranked = []
    for items in product(*groups):
        score = score_outfit(items, season, occasion)
        ranked.append((score, items))
    ranked.sort(key=lambda entry: (-entry[0], tuple(i.name.casefold() for i in entry[1])))
    return ranked[:limit]
