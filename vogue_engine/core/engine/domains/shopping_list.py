"""Domain 13: Curated Capsule Shopping Checklist."""
from vogue_engine.core.engine.schemas.style_payload import DomainShoppingChecklist
from vogue_engine.core.vision.geometry import FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ColorimetricProfile

class ShoppingListDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainShoppingChecklist:
        season = photo.season.value
        shape = geom.primary_shape.value

        acquisitions = [
            {
                "rank": 1,
                "domain": "Eyewear",
                "item": f"Handcrafted Acetate Frames ({shape} Harmonized)",
                "priority": "Tier 1: Immediate Structural Impact",
                "specification": "Custom bridge height matching pupillary axis"
            },
            {
                "rank": 2,
                "domain": "Outerwear",
                "item": f"Double-Faced Cashmere Overcoat in {season} Neutral Anchor",
                "priority": "Tier 1: Primary Foundation",
                "specification": "Structured shoulders to balance facial frame"
            },
            {
                "rank": 3,
                "domain": "Footwear",
                "item": "Goodyear-Welted Calfskin Oxford / Chelsea Boots",
                "priority": "Tier 2: Silhouette Grounding",
                "specification": "Burnished hand finish matching belt leather"
            },
            {
                "rank": 4,
                "domain": "Knitwear",
                "item": f"Fine-Gauge Silk-Cashmere Polo in {season} Primary Swatch",
                "priority": "Tier 2: Mid-Layer Harmonization",
                "specification": "Structured ribbed hemline"
            }
        ]

        investments = [
            f"Bespoke Flannel 2-Piece Suit calibrated for {shape} morphology",
            f"Heavyweight Cashmere Turtleneck in primary {season} tone",
            f"Luxury Horology Accent in {photo.undertone.value}-calibrated metal alloy"
        ]

        return DomainShoppingChecklist(
            priority_acquisition_matrix=acquisitions,
            seasonal_investment_pieces=investments,
        )
