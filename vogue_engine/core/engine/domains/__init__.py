"""
13 Core Luxury Domains Package.
Each domain maps deterministic inputs into granular 90% visual editorial outputs.
"""
from vogue_engine.core.engine.domains.rating import RatingDomainCalculator
from vogue_engine.core.engine.domains.color import ColorDomainCalculator
from vogue_engine.core.engine.domains.outfits import OutfitsDomainCalculator
from vogue_engine.core.engine.domains.face_shape import FaceShapeDomainCalculator
from vogue_engine.core.engine.domains.hair import HairDomainCalculator
from vogue_engine.core.engine.domains.eyewear import EyewearDomainCalculator
from vogue_engine.core.engine.domains.beard import BeardDomainCalculator
from vogue_engine.core.engine.domains.accessories import AccessoriesDomainCalculator
from vogue_engine.core.engine.domains.patterns import PatternsDomainCalculator
from vogue_engine.core.engine.domains.footwear import FootwearDomainCalculator
from vogue_engine.core.engine.domains.core_style import CoreStyleDomainCalculator
from vogue_engine.core.engine.domains.scorecard import ScorecardDomainCalculator
from vogue_engine.core.engine.domains.shopping_list import ShoppingListDomainCalculator

__all__ = [
    "RatingDomainCalculator",
    "ColorDomainCalculator",
    "OutfitsDomainCalculator",
    "FaceShapeDomainCalculator",
    "HairDomainCalculator",
    "EyewearDomainCalculator",
    "BeardDomainCalculator",
    "AccessoriesDomainCalculator",
    "PatternsDomainCalculator",
    "FootwearDomainCalculator",
    "CoreStyleDomainCalculator",
    "ScorecardDomainCalculator",
    "ShoppingListDomainCalculator",
]
