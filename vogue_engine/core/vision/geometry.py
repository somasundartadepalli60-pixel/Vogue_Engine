"""
Facial Geometry, Vector Metrics, and Morphometric Classification Engine.
Calculates scale-invariant proportions, symmetry scores, and shape classifications
directly from 3D facial landmark matrices.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Dict, Any
import numpy as np

from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML


class FaceShape(str, Enum):
    OVAL = "Oval"
    ROUND = "Round"
    SQUARE = "Square"
    HEART = "Heart"
    DIAMOND = "Diamond"
    OBLONG = "Oblong"
    TRIANGLE = "Triangle"


@dataclass(frozen=True)
class FacialGeometryMetrics:
    length_to_width_ratio: float
    jaw_to_zygomatic_ratio: float
    forehead_to_zygomatic_ratio: float
    jaw_to_forehead_ratio: float
    bilateral_symmetry_score: float
    mandibular_angle_degrees: float
    primary_shape: FaceShape
    secondary_shape: FaceShape
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "length_to_width_ratio": self.length_to_width_ratio,
            "jaw_to_zygomatic_ratio": self.jaw_to_zygomatic_ratio,
            "forehead_to_zygomatic_ratio": self.forehead_to_zygomatic_ratio,
            "jaw_to_forehead_ratio": self.jaw_to_forehead_ratio,
            "bilateral_symmetry_score": self.bilateral_symmetry_score,
            "mandibular_angle_degrees": self.mandibular_angle_degrees,
            "primary_shape": self.primary_shape.value,
            "secondary_shape": self.secondary_shape.value,
            "confidence": self.confidence,
        }


class FacialGeometryEngine:
    """
    Computes scale-invariant Euclidean vector metrics, affine-normalized bilateral
    symmetry tensors, and discrete morphologic classifications from 3D landmarks.
    """

    @staticmethod
    def euclidean_distance(pt1: np.ndarray, pt2: np.ndarray) -> float:
        """Calculates 3D Euclidean distance between two landmark coordinate vectors."""
        return float(np.linalg.norm(pt1 - pt2))

    @classmethod
    def calculate_metrics(cls, landmarks: np.ndarray) -> FacialGeometryMetrics:
        """
        Processes normalized MediaPipe (468+, 3) landmark array.
        Computes scale-invariant facial proportions, mandibular angle,
        and bilateral sagittal symmetry.
        """
        if landmarks.ndim != 2 or landmarks.shape[0] < 468:
            raise ValueError(f"Expected landmark array of shape (N>=468, 3), got {landmarks.shape}")

        # Coordinate vectors of primary morphometric anchors
        menton = landmarks[FML.MENTON]
        trichion = landmarks[FML.TRICHION]
        zyg_l = landmarks[FML.ZYGOMATIC_LEFT]
        zyg_r = landmarks[FML.ZYGOMATIC_RIGHT]
        gon_l = landmarks[FML.GONION_LEFT]
        gon_r = landmarks[FML.GONION_RIGHT]
        temple_l = landmarks[FML.TEMPLE_LEFT]
        temple_r = landmarks[FML.TEMPLE_RIGHT]

        # Key anatomical dimensions
        face_length = cls.euclidean_distance(trichion, menton)
        bizygomatic_width = cls.euclidean_distance(zyg_l, zyg_r)
        bigonial_width = cls.euclidean_distance(gon_l, gon_r)
        forehead_width = cls.euclidean_distance(temple_l, temple_r)

        # Scale-Invariant Proportional Ratios
        lwr = face_length / max(bizygomatic_width, 1e-6)
        jzr = bigonial_width / max(bizygomatic_width, 1e-6)
        fzr = forehead_width / max(bizygomatic_width, 1e-6)
        jfr = bigonial_width / max(forehead_width, 1e-6)

        # Mandibular Angle Calculation (Gonion-R to Menton to Gonion-L)
        v_l = gon_l[:2] - menton[:2]
        v_r = gon_r[:2] - menton[:2]
        denom = (np.linalg.norm(v_l) * np.linalg.norm(v_r)) + 1e-8
        cosine_angle = np.dot(v_l, v_r) / denom
        mandibular_angle = float(np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0))))

        # Bilateral Symmetry Tensor across Sagittal Axis (Glabella -> Menton)
        sagittal_p1 = landmarks[FML.GLABELLA][:2]
        sagittal_p2 = landmarks[FML.MENTON][:2]
        sagittal_vec = sagittal_p2 - sagittal_p1
        sag_length = np.linalg.norm(sagittal_vec)
        if sag_length < 1e-6:
            sagittal_norm = np.array([0.0, 1.0])
        else:
            sagittal_norm = sagittal_vec / sag_length
        sagittal_normal = np.array([-sagittal_norm[1], sagittal_norm[0]])

        bilateral_pairs = [
            (FML.ZYGOMATIC_LEFT, FML.ZYGOMATIC_RIGHT),
            (FML.GONION_LEFT, FML.GONION_RIGHT),
            (FML.TEMPLE_LEFT, FML.TEMPLE_RIGHT),
            (FML.LEFT_EYE_OUTER, FML.RIGHT_EYE_OUTER),
            (FML.JAW_LINE_LEFT_MID, FML.JAW_LINE_RIGHT_MID),
            (FML.FOREHEAD_LEFT_CREST, FML.FOREHEAD_RIGHT_CREST),
        ]

        pair_deviations = []
        for idx_l, idx_r in bilateral_pairs:
            pt_l = landmarks[idx_l][:2] - sagittal_p1
            pt_r = landmarks[idx_r][:2] - sagittal_p1
            dist_l = abs(float(np.dot(pt_l, sagittal_normal)))
            dist_r = abs(float(np.dot(pt_r, sagittal_normal)))
            max_dist = max(dist_l, dist_r, 1e-6)
            pair_deviations.append(abs(dist_l - dist_r) / max_dist)

        # Weighted combination of mean and maximum localized bilateral deviation
        composite_deviation = 0.4 * float(np.mean(pair_deviations)) + 0.6 * float(np.max(pair_deviations))
        symmetry_score = float(np.clip(100.0 * (1.0 - composite_deviation), 0.0, 100.0))

        # Discrete Face Shape Morphometric Classifier
        primary, secondary, conf = cls._classify_morphology(
            lwr=lwr, jzr=jzr, fzr=fzr, jfr=jfr, angle=mandibular_angle
        )

        return FacialGeometryMetrics(
            length_to_width_ratio=round(lwr, 4),
            jaw_to_zygomatic_ratio=round(jzr, 4),
            forehead_to_zygomatic_ratio=round(fzr, 4),
            jaw_to_forehead_ratio=round(jfr, 4),
            bilateral_symmetry_score=round(symmetry_score, 2),
            mandibular_angle_degrees=round(mandibular_angle, 2),
            primary_shape=primary,
            secondary_shape=secondary,
            confidence=round(conf, 3),
        )

    @staticmethod
    def _classify_morphology(
        lwr: float, jzr: float, fzr: float, jfr: float, angle: float
    ) -> Tuple[FaceShape, FaceShape, float]:
        """
        Deterministic, rule-based hyperplane morphology classifier.
        Eliminates external neural API drift by operating directly on geometric ratios.
        """
        scores: Dict[FaceShape, float] = {}

        # 1. OBLONG / RECTANGLE: High vertical index (LWR > 1.50)
        scores[FaceShape.OBLONG] = (
            max(0.0, (lwr - 1.48) * 4.5) +
            max(0.0, 1.0 - abs(jzr - 0.85) * 3.0) +
            max(0.0, 1.0 - abs(fzr - 0.85) * 3.0)
        )

        # 2. TRIANGLE / PEAR: Jaw visibly wider than cheekbones and forehead (JZR > 0.90, JFR > 1.05)
        scores[FaceShape.TRIANGLE] = (
            max(0.0, (jzr - 0.88) * 6.0) +
            max(0.0, (jfr - 1.05) * 5.0) +
            max(0.0, (0.85 - fzr) * 3.5)
        )

        # 3. HEART / INVERTED TRIANGLE: Wide forehead, narrow tapering jaw (FZR - JZR > 0.12)
        fzr_jzr_diff = fzr - jzr
        scores[FaceShape.HEART] = (
            max(0.0, (fzr_jzr_diff - 0.10) * 8.0) +
            max(0.0, (0.75 - jzr) * 4.5) +
            max(0.0, (fzr - 0.80) * 3.5)
        )

        # 4. DIAMOND: Cheekbones dramatically wider than both forehead and jaw, with balanced taper
        taper_balance = max(0.0, 0.15 - abs(fzr - jzr)) * 6.0
        scores[FaceShape.DIAMOND] = (
            max(0.0, (0.78 - fzr) * 5.5) +
            max(0.0, (0.75 - jzr) * 5.5) +
            taper_balance
        )

        # 5. SQUARE: Equal length-to-width (LWR < 1.35), broad jaw (JZR >= 0.82) and broad forehead
        scores[FaceShape.SQUARE] = (
            max(0.0, (1.35 - lwr) * 4.0) +
            max(0.0, (jzr - 0.80) * 6.5) +
            max(0.0, (fzr - 0.78) * 4.5)
        )

        # 6. ROUND: Equal length-to-width (LWR < 1.30), softer jaw (JZR < 0.80), cheek dominance
        scores[FaceShape.ROUND] = (
            max(0.0, (1.30 - lwr) * 4.5) +
            max(0.0, (0.80 - jzr) * 5.0) +
            max(0.0, (0.82 - fzr) * 3.5)
        )

        # 7. OVAL: Canonical balance (LWR ~ 1.45, JZR ~ 0.76, FZR ~ 0.82)
        scores[FaceShape.OVAL] = (
            max(0.0, 1.0 - abs(lwr - 1.45) * 3.5) +
            max(0.0, 1.0 - abs(jzr - 0.76) * 4.0) +
            max(0.0, 1.0 - abs(fzr - 0.82) * 4.0)
        )

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        primary = ranked[0][0]
        secondary = ranked[1][0]

        total_score = sum(s for _, s in ranked) + 1e-6
        confidence = float(np.clip(ranked[0][1] / total_score * 1.85, 0.45, 0.99))

        return primary, secondary, confidence
