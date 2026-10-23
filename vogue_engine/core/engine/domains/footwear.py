"""Domain 10: Footwear and Proportions."""
from vogue_engine.core.engine.schemas.style_payload import DomainFootwear
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ColorimetricProfile

class FootwearDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainFootwear:
        shape = geom.primary_shape

        if shape in [FaceShape.SQUARE, FaceShape.OBLONG]:
            toe = "Chiseled Soft-Square / Architectural English Toe"
            anchor = "Substantial Double Goodyear Welt (Balances Linear Strength)"
            finishes = ["Museum Calfskin Espresso", "Waxed Shell Cordovan", "Pebble-Grain Oxblood"]
        elif shape in [FaceShape.ROUND, FaceShape.HEART]:
            toe = "Classic Elegant Almond Toe"
            anchor = "Sleek Beveled Blake Stitch / Slim Leather Sole"
            finishes = ["Burnished French Calfskin", "Silky Suede Castoro", "Patent Leather Black"]
        else:
            toe = "Balanced Soft Round / Classic Almond"
            anchor = "Single Goodyear Welt / Clean Waist"
            finishes = ["Hand-Patinated Box Calf", "Polished Dark Chocolate Calf", "Navy Nubuck"]

        return DomainFootwear(
            toe_box_geometry=toe,
            silhouette_anchor_weight=anchor,
            leather_finishes=finishes,
        )
