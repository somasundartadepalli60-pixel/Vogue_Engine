"""Domain 3: Outfits and Editorial Capsules."""
from vogue_engine.core.engine.schemas.style_payload import DomainOutfits
from vogue_engine.core.engine.schemas.layout import GridCoordinate
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ContrastLevel, ColorimetricProfile

class OutfitsDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainOutfits:
        shape = geom.primary_shape
        if shape in [FaceShape.ROUND, FaceShape.TRIANGLE]:
            rule = "Broaden shoulder lines with structured roped sleeve heads to counterbalance lower facial volume."
        elif shape in [FaceShape.SQUARE, FaceShape.OBLONG]:
            rule = "Soft unconstructed Neapolitan shoulder drape to soften linear facial geometry."
        elif shape == FaceShape.HEART:
            rule = "Wider lapels and relaxed straight-leg trousers to anchor narrow lower-third."
        else:
            rule = "Proportional tailored silhouette maintaining natural shoulder balance."

        outfits = [
            {
                "style": "Editorial Formal",
                "components": [
                    "Structured Wool Gabardine Blazer",
                    "High-Count Poplin Spread Collar Shirt",
                    "Forward Pleat High-Rise Trousers"
                ],
                "visual_asset_id": f"formal_{shape.value.lower()}_01"
            },
            {
                "style": "Contemporary Sartorial",
                "components": [
                    "Textured Knit Long-Sleeve Polo",
                    "Tailored Flannel Drawstring Trousers",
                    "Suede Chelsea Boots"
                ],
                "visual_asset_id": f"casual_{shape.value.lower()}_01"
            }
        ]

        return DomainOutfits(
            capsule_title=f"The Proportion Portfolio: {shape.value} Silhouette",
            silhouette_balancing_rule=rule,
            recommended_outfits=outfits,
            visual_board_layout=GridCoordinate(x=5.0, y=5.0, width=90.0, height=85.0)
        )
