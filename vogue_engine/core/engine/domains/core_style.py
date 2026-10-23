"""Domain 11: Core Style Archetype."""
from vogue_engine.core.engine.schemas.style_payload import DomainCoreStyle
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Season, ContrastLevel, ColorimetricProfile

class CoreStyleDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainCoreStyle:
        shape = geom.primary_shape
        season = photo.season

        archetype_map = {
            (FaceShape.SQUARE, Season.WINTER): ("Architectural Avant-Garde", "Dramatic Minimalist"),
            (FaceShape.SQUARE, Season.AUTUMN): ("Rugged Sartorialist", "Heritage Architectural"),
            (FaceShape.OVAL, Season.SUMMER): ("Classic Continental Elegance", "Effortless Sprezzatura"),
            (FaceShape.OVAL, Season.SPRING): ("Luminous Modern Classic", "Dynamic Casual Luxe"),
            (FaceShape.ROUND, Season.WINTER): ("Monochromatic Modernist", "Sharp Urban Sartorial"),
            (FaceShape.HEART, Season.AUTUMN): ("Bohemian Sartorialist", "Warm Layered Luxe"),
            (FaceShape.DIAMOND, Season.SPRING): ("Sculptural Contemporary", "Refined High-Contrast"),
            (FaceShape.OBLONG, Season.WINTER): ("High-Tailored Formalist", "Architectural Minimalist"),
        }

        prim, sec = archetype_map.get(
            (shape, season),
            ("Architectural Modern Sartorialist", "Refined Classic Elegance")
        )

        anchors = [
            "Precision Proportions",
            "Harmonized Chromatic Anchors",
            "Sculptural Silhouette Balancing"
        ]

        headline = f"The {prim}: Volumetric Precision and Curated Tonalism"

        return DomainCoreStyle(
            primary_archetype=prim,
            secondary_archetype=sec,
            aesthetic_anchors=anchors,
            editorial_headline=headline,
        )
