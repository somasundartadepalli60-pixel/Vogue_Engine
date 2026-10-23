"""Domain 8: Accessories and Metallurgy."""
from vogue_engine.core.engine.schemas.style_payload import DomainAccessories
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Undertone, ColorimetricProfile

class AccessoriesDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainAccessories:
        metal = (
            "18K Brushed Yellow Gold, Polished Brass, Warm Rose Gold"
            if photo.undertone == Undertone.WARM
            else (
                "High-Luster Platinum, 925 Sterling Silver, White Gold"
                if photo.undertone == Undertone.COOL
                else "Mixed Metallurgy: Brushed Titanium & 14K Champagne Gold"
            )
        )

        shape = geom.primary_shape
        if shape in [FaceShape.SQUARE, FaceShape.OBLONG]:
            scale = "Substantial Bold Gauge / Structured Hardware (42mm-44mm Timepieces)"
            neckwear = "Spread or Semi-Cutaway Collar / 3.5\" Italian Silk Tie"
            hat = "Medium-to-Wide Structured Brim Fedora"
        elif shape in [FaceShape.ROUND, FaceShape.HEART]:
            scale = "Refined Micro-Precision Minimalist (38mm-40mm Slim Timepieces)"
            neckwear = "Forward Point Collar / 2.75\" Slim Silk or Knit Tie"
            hat = "Asymmetric Snap Brim or Structured Panama"
        else:
            scale = "Proportional Classic Scale (40mm Luxury Timepiece)"
            neckwear = "Classic Semi-Spread Collar / 3.0\" Standard Tie"
            hat = "Balanced Classic Fedora / Soft Trilby"

        return DomainAccessories(
            metal_undertone_match=metal,
            jewelry_scale_gauge=scale,
            hat_brim_geometry=hat,
            neckwear_proportions=neckwear,
        )
