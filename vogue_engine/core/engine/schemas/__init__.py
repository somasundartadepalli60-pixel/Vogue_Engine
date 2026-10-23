"""Schemas package initialization."""
from vogue_engine.core.engine.schemas.layout import GridCoordinate, VisualSwatch
from vogue_engine.core.engine.schemas.vectors import BetterWorseComparison
from vogue_engine.core.engine.schemas.style_payload import (
    DomainRating,
    DomainColor,
    DomainOutfits,
    DomainFaceShape,
    DomainHair,
    DomainEyewear,
    DomainBeard,
    DomainAccessories,
    DomainPatterns,
    DomainFootwear,
    DomainCoreStyle,
    DomainScorecard,
    DomainShoppingChecklist,
    MasterVogueStyleReport,
)

__all__ = [
    "GridCoordinate",
    "VisualSwatch",
    "BetterWorseComparison",
    "DomainRating",
    "DomainColor",
    "DomainOutfits",
    "DomainFaceShape",
    "DomainHair",
    "DomainEyewear",
    "DomainBeard",
    "DomainAccessories",
    "DomainPatterns",
    "DomainFootwear",
    "DomainCoreStyle",
    "DomainScorecard",
    "DomainShoppingChecklist",
    "MasterVogueStyleReport",
]
