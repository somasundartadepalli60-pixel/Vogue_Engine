"""Domain 1: Rating and Structural Harmony."""
from vogue_engine.core.engine.schemas.style_payload import DomainRating
from vogue_engine.core.vision.geometry import FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import ColorimetricProfile, ContrastLevel

class RatingDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainRating:
        symmetry = geom.bilateral_symmetry_score
        harmony = round(max(0.0, min(100.0, 100.0 - abs(geom.length_to_width_ratio - 1.45) * 45.0)), 1)
        contrast_score = 94.0 if photo.contrast_level == ContrastLevel.HIGH else (86.0 if photo.contrast_level == ContrastLevel.MEDIUM else 80.0)
        overall = round((symmetry * 0.35) + (harmony * 0.35) + (contrast_score * 0.30), 1)

        radar = {
            "Symmetry": symmetry,
            "Harmony": harmony,
            "Contrast": contrast_score,
            "Structure": round(float(np_clip_angle(geom.mandibular_angle_degrees)), 1),
            "Photometrics": round(photo.confidence * 100.0, 1),
        }

        return DomainRating(
            symmetry_quotient=symmetry,
            proportional_harmony_index=harmony,
            contrast_balance_score=contrast_score,
            overall_editorial_rating=overall,
            radar_tensor=radar,
        )

def np_clip_angle(angle: float) -> float:
    # 90 degrees is ideal square, 120 is soft round, normalize to 70-100 scale
    val = 100.0 - abs(angle - 105.0) * 0.8
    return max(60.0, min(99.0, val))
