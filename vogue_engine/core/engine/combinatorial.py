"""
Style Permutation Combinatorial Dispatcher.
Executes deterministic combinatorial mapping across:
4 Seasons × 3 Skin Undertones × 3 Contrast Levels × 7 Face Shapes (252 States)
Compiling into all 13 core luxury magazine domains.
"""
from datetime import datetime, timezone
from typing import Optional

from vogue_engine.core.vision.geometry import FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ColorimetricProfile
from vogue_engine.core.engine.schemas.style_payload import MasterVogueStyleReport
from vogue_engine.core.engine.domains import (
    RatingDomainCalculator,
    ColorDomainCalculator,
    OutfitsDomainCalculator,
    FaceShapeDomainCalculator,
    HairDomainCalculator,
    EyewearDomainCalculator,
    BeardDomainCalculator,
    AccessoriesDomainCalculator,
    PatternsDomainCalculator,
    FootwearDomainCalculator,
    CoreStyleDomainCalculator,
    ScorecardDomainCalculator,
    ShoppingListDomainCalculator,
)


class StylePermutationDispatcher:
    """
    Enterprise-scale, client/server-side deterministic style compiler.
    Eliminates external LLM/vision inference variance by hardcoding
    proportional and chromatic aesthetic principles into discrete vector responses.
    """

    @classmethod
    def compile_report(
        cls,
        report_uuid: str,
        geom: FacialGeometryMetrics,
        photo: ColorimetricProfile,
        svg_overlay: str = "",
    ) -> MasterVogueStyleReport:
        """
        Compiles the complete 13-domain Master Vogue Style Report.
        """
        # Domain 1: Rating
        domain_rating = RatingDomainCalculator.calculate(geom, photo)

        # Domain 2: Color
        domain_color = ColorDomainCalculator.calculate(photo)

        # Domain 3: Outfits
        domain_outfits = OutfitsDomainCalculator.calculate(geom, photo)

        # Domain 4: Face Shape
        domain_face_shape = FaceShapeDomainCalculator.calculate(geom, svg_overlay)

        # Domain 5: Hair
        domain_hair = HairDomainCalculator.calculate(geom)

        # Domain 6: Eyewear
        domain_eyewear = EyewearDomainCalculator.calculate(geom, photo)

        # Domain 7: Beard
        domain_beard = BeardDomainCalculator.calculate(geom)

        # Domain 8: Accessories
        domain_accessories = AccessoriesDomainCalculator.calculate(geom, photo)

        # Domain 9: Patterns
        domain_patterns = PatternsDomainCalculator.calculate(geom, photo)

        # Domain 10: Footwear
        domain_footwear = FootwearDomainCalculator.calculate(geom, photo)

        # Domain 11: Core Style
        domain_core_style = CoreStyleDomainCalculator.calculate(geom, photo)

        # Domain 12: Scorecard
        domain_scorecard = ScorecardDomainCalculator.calculate(geom, photo)

        # Domain 13: Shopping Checklist
        domain_shopping = ShoppingListDomainCalculator.calculate(geom, photo)

        return MasterVogueStyleReport(
            report_uuid=report_uuid,
            timestamp=datetime.now(timezone.utc).isoformat(),
            rating=domain_rating,
            color=domain_color,
            outfits=domain_outfits,
            face_shape=domain_face_shape,
            hair=domain_hair,
            eyewear=domain_eyewear,
            beard=domain_beard,
            accessories=domain_accessories,
            patterns=domain_patterns,
            footwear=domain_footwear,
            core_style=domain_core_style,
            scorecard=domain_scorecard,
            shopping_checklist=domain_shopping,
        )
