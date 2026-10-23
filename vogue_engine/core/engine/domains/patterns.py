"""Domain 9: Pattern Scales and Geometries."""
from vogue_engine.core.engine.schemas.style_payload import DomainPatterns
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ContrastLevel, ColorimetricProfile

class PatternsDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainPatterns:
        contrast = photo.contrast_level

        if contrast == ContrastLevel.HIGH:
            scale = "Macro High-Definition"
            print_contrast = "High Graphic Contrast (Black/White, Navy/Ecru)"
            motifs = ["Bold Chalkstripe", "High-Def Windowpane", "Architectural Glen Plaid", "Graphic Houndstooth"]
            avoids = ["Muted Blurred Florals", "Low-Contrast Melange Solids"]
        elif contrast == ContrastLevel.MEDIUM:
            scale = "Meso Balanced Scale"
            print_contrast = "Medium Dynamic Contrast"
            motifs = ["Subtle Prince of Wales", "Textured Herringbone", "Micro-Gingham", "Birdseye Weave"]
            avoids = ["Extreme Stark Color Blocking", "Hyper-Busy Neon Prints"]
        else:  # Low
            scale = "Micro-Texture / Tonal"
            print_contrast = "Soft Tonal Low Contrast"
            motifs = ["Hopsack Weave", "Sharkskin", "Fine Pinpoint", "Tone-on-Tone Shadow Stripes"]
            avoids = ["Vivid Geometric Blocks", "High-Contrast Checkerboards"]

        return DomainPatterns(
            recommended_scale=scale,
            print_contrast=print_contrast,
            optimal_motifs=motifs,
            avoid_motifs=avoids,
        )
