"""
Photometric and Colorimetric Analysis Engine.
Calculates CIELAB skin tone, Individual Typology Angle (ITA°),
undertone classification, and facial contrast ratios.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Dict, Any
import cv2
import numpy as np

from vogue_engine.configs.color_spaces import ColorSpaceConstants
from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML


class Season(str, Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    AUTUMN = "Autumn"
    WINTER = "Winter"


class Undertone(str, Enum):
    WARM = "Warm"
    COOL = "Cool"
    NEUTRAL = "Neutral"


class ContrastLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass(frozen=True)
class ColorimetricProfile:
    ita_angle: float
    undertone: Undertone
    contrast_level: ContrastLevel
    season: Season
    skin_lab_mean: Tuple[float, float, float]
    iris_luminance: float
    hair_luminance: float
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ita_angle": self.ita_angle,
            "undertone": self.undertone.value,
            "contrast_level": self.contrast_level.value,
            "season": self.season.value,
            "skin_lab_mean": {
                "L": self.skin_lab_mean[0],
                "a": self.skin_lab_mean[1],
                "b": self.skin_lab_mean[2],
            },
            "iris_luminance": self.iris_luminance,
            "hair_luminance": self.hair_luminance,
            "confidence": self.confidence,
        }


class PhotometricEngine:
    """
    Extracts dermatologically precise skin undertone, Individual Typology Angle (ITA°),
    and root-mean-square (RMS) facial contrast without cloud vision dependencies.
    """

    @classmethod
    def analyze_image(
        cls, 
        bgr_image: np.ndarray, 
        landmarks: np.ndarray
    ) -> ColorimetricProfile:
        """
        Analyzes an RGB/BGR image and normalized landmarks to extract photometrics.
        """
        if bgr_image is None or bgr_image.size == 0:
            raise ValueError("Invalid image buffer supplied to PhotometricEngine.")
        if landmarks.ndim != 2 or landmarks.shape[0] < 468:
            raise ValueError("Landmarks array must contain at least 468 points.")

        h, w = bgr_image.shape[:2]
        pixel_landmarks = (landmarks[:, :2] * np.array([w, h])).astype(np.int32)

        # 1. Extract Masked Skin Regions (Cheeks + Forehead) to avoid vascular flush/lip/eye pixels
        mask = np.zeros((h, w), dtype=np.uint8)
        for poly_indices in [FML.CHEEK_SAMPLE_RIGHT, FML.CHEEK_SAMPLE_LEFT, FML.FOREHEAD_SAMPLE]:
            poly_pts = pixel_landmarks[poly_indices]
            # Clip polygon coordinates to image boundaries
            poly_pts[:, 0] = np.clip(poly_pts[:, 0], 0, w - 1)
            poly_pts[:, 1] = np.clip(poly_pts[:, 1], 0, h - 1)
            cv2.fillConvexPoly(mask, poly_pts, 255)

        # Convert to CIELAB
        lab_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2LAB).astype(np.float32)
        # In OpenCV, 8-bit LAB has L in [0, 255], a in [0, 255], b in [0, 255]
        # Standardize: L* in [0, 100], a* in [-128, +127], b* in [-128, +127]
        skin_pixels_lab = lab_image[mask == 255]
        if len(skin_pixels_lab) == 0:
            # Fallback to central region if polygon was too small
            center_y, center_x = h // 2, w // 2
            skin_pixels_lab = lab_image[center_y-10:center_y+10, center_x-10:center_x+10].reshape(-1, 3)

        mean_l = float(np.mean(skin_pixels_lab[:, 0]) * (100.0 / 255.0))
        mean_a = float(np.mean(skin_pixels_lab[:, 1]) - 128.0)
        mean_b = float(np.mean(skin_pixels_lab[:, 2]) - 128.0)

        # 2. Individual Typology Angle (ITA°)
        # ITA° = [ArcTan((L* - 50) / b*)] * (180 / π)
        ita = float(np.arctan2((mean_l - 50.0), max(mean_b, 1e-4)) * (180.0 / np.pi))

        # 3. Undertone calculation
        # Warm: positive b* dominance (golden/yellow tone).
        # Cool: low/negative b* or high a* (pinkish / blue undertone).
        undertone_ratio = mean_b / (abs(mean_a) + 1e-5)
        if undertone_ratio > ColorSpaceConstants.UNDERTONE_WARM_RATIO_MIN:
            undertone = Undertone.WARM
        elif undertone_ratio < ColorSpaceConstants.UNDERTONE_COOL_RATIO_MAX:
            undertone = Undertone.COOL
        else:
            undertone = Undertone.NEUTRAL

        # 4. Measure Hair & Iris Luminance for Contrast Computation
        trich_pt = pixel_landmarks[FML.TRICHION]
        hair_y_start = max(0, trich_pt[1] - int(h * 0.08))
        hair_y_end = max(0, trich_pt[1])
        hair_x_start = max(0, trich_pt[0] - 20)
        hair_x_end = min(w, trich_pt[0] + 20)

        hair_sample_box = lab_image[hair_y_start:hair_y_end, hair_x_start:hair_x_end]
        if hair_sample_box.size > 0:
            hair_l = float(np.mean(hair_sample_box[:, :, 0]) * (100.0 / 255.0))
        else:
            hair_l = 25.0

        eye_pt = pixel_landmarks[FML.LEFT_EYE_INNER]
        iris_sample = lab_image[
            max(0, eye_pt[1]-5):min(h, eye_pt[1]+5),
            max(0, eye_pt[0]-5):min(w, eye_pt[0]+5)
        ]
        if iris_sample.size > 0:
            iris_l = float(np.mean(iris_sample[:, :, 0]) * (100.0 / 255.0))
        else:
            iris_l = 30.0

        # Contrast index: Spread between facial skin luminance and darkest ocular/hair feature
        luminance_spread = abs(mean_l - min(hair_l, iris_l))
        if luminance_spread >= ColorSpaceConstants.CONTRAST_HIGH_MIN:
            contrast = ContrastLevel.HIGH
        elif luminance_spread >= ColorSpaceConstants.CONTRAST_MEDIUM_MIN:
            contrast = ContrastLevel.MEDIUM
        else:
            contrast = ContrastLevel.LOW

        # 5. Deterministic Seasonal Assignment Matrix
        season = cls._determine_season(undertone, mean_l, contrast)

        return ColorimetricProfile(
            ita_angle=round(ita, 2),
            undertone=undertone,
            contrast_level=contrast,
            season=season,
            skin_lab_mean=(round(mean_l, 2), round(mean_a, 2), round(mean_b, 2)),
            iris_luminance=round(iris_l, 2),
            hair_luminance=round(hair_l, 2),
            confidence=0.95,
        )

    @staticmethod
    def _determine_season(undertone: Undertone, l_star: float, contrast: ContrastLevel) -> Season:
        """
        Seasonal matrix mapper based on undertone, luminance, and contrast.
        - Spring: Warm + Bright / High Lightness
        - Autumn: Warm + Deep / Rich / Low Lightness or High Contrast
        - Summer: Cool + Soft / Muted / Light
        - Winter: Cool + Vivid / Deep / High Contrast
        """
        if undertone == Undertone.WARM:
            if l_star > 60.0 and contrast != ContrastLevel.HIGH:
                return Season.SPRING
            else:
                return Season.AUTUMN
        elif undertone == Undertone.COOL:
            if contrast == ContrastLevel.HIGH or l_star < 52.0:
                return Season.WINTER
            else:
                return Season.SUMMER
        else:  # Neutral
            if contrast == ContrastLevel.HIGH:
                return Season.WINTER
            elif contrast == ContrastLevel.MEDIUM:
                return Season.AUTUMN
            else:
                return Season.SUMMER
