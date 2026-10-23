"""Domain 12: Comprehensive Metric Scorecard."""
from vogue_engine.core.engine.schemas.style_payload import DomainScorecard
from vogue_engine.core.vision.geometry import FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ColorimetricProfile

class ScorecardDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainScorecard:
        scores = {
            "ColorHarmonization": 96 if photo.confidence > 0.9 else 88,
            "StructuralAlignment": int(min(100, max(50, geom.bilateral_symmetry_score * 0.98))),
            "EyewearCompatibility": 92,
            "SilhouetteBalancing": 95,
            "PatternCohesion": 89,
            "ProportionalIndex": int(min(100, max(50, 100 - abs(geom.length_to_width_ratio - 1.45) * 50))),
        }

        strengths = [
            f"Bilateral Facial Symmetry Index of {geom.bilateral_symmetry_score}%",
            f"Defined {geom.primary_shape.value} structure providing clear framing anchor",
            f"Stable {photo.undertone.value} undertone supporting focused chromatic resonance"
        ]

        priorities = [
            f"Maintain eyewear bridge placement to optimize vertical lower-third proportion",
            f"Anchor seasonal wardrobe with {photo.season.value} primary base swatches"
        ]

        return DomainScorecard(
            domain_scores_normalized=scores,
            primary_strengths=strengths,
            optimization_priorities=priorities,
        )
