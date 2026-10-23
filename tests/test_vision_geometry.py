"""
Unit Tests for Facial Geometry Engine and Morphometrics.
Validates numerical stability, scale-invariance, bilateral symmetry tensors,
and the 7-morphology discrete classification hyperplane.
"""
import pytest
import numpy as np

from vogue_engine.core.vision.geometry import FacialGeometryEngine, FaceShape
from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML


class TestFacialGeometry:

    def test_canonical_oval_metrics(self, synthetic_canonical_mesh):
        """Verifies that the canonical baseline mesh evaluates as an Oval with high symmetry."""
        metrics = FacialGeometryEngine.calculate_metrics(synthetic_canonical_mesh)
        assert metrics.primary_shape == FaceShape.OVAL
        assert metrics.bilateral_symmetry_score >= 95.0
        assert 1.35 <= metrics.length_to_width_ratio <= 1.55
        assert 0.70 <= metrics.jaw_to_zygomatic_ratio <= 0.85

    def test_scale_invariance(self, synthetic_canonical_mesh):
        """Scaling landmark coordinates (e.g., zoom in/out) must not alter proportional ratios."""
        scaled_mesh = synthetic_canonical_mesh * 2.5
        orig_metrics = FacialGeometryEngine.calculate_metrics(synthetic_canonical_mesh)
        scaled_metrics = FacialGeometryEngine.calculate_metrics(scaled_mesh)

        assert pytest.approx(orig_metrics.length_to_width_ratio, rel=1e-3) == scaled_metrics.length_to_width_ratio
        assert pytest.approx(orig_metrics.jaw_to_zygomatic_ratio, rel=1e-3) == scaled_metrics.jaw_to_zygomatic_ratio
        assert pytest.approx(orig_metrics.forehead_to_zygomatic_ratio, rel=1e-3) == scaled_metrics.forehead_to_zygomatic_ratio
        assert orig_metrics.primary_shape == scaled_metrics.primary_shape

    def test_translation_invariance_for_symmetry(self, synthetic_canonical_mesh):
        """Rigid translation of entire mesh must preserve symmetry score."""
        translated_mesh = synthetic_canonical_mesh.copy()
        translated_mesh += np.array([0.15, 0.25, 0.0], dtype=np.float32)

        orig_metrics = FacialGeometryEngine.calculate_metrics(synthetic_canonical_mesh)
        trans_metrics = FacialGeometryEngine.calculate_metrics(translated_mesh)

        assert pytest.approx(orig_metrics.bilateral_symmetry_score, abs=0.5) == trans_metrics.bilateral_symmetry_score

    def test_asymmetric_distortion(self, synthetic_canonical_mesh):
        """Displacing one cheekbone laterally must significantly lower symmetry score."""
        distorted = synthetic_canonical_mesh.copy()
        distorted[FML.ZYGOMATIC_LEFT][0] += 0.15

        metrics = FacialGeometryEngine.calculate_metrics(distorted)
        assert metrics.bilateral_symmetry_score < 80.0

    @pytest.mark.parametrize("target_shape, l_mod, cheek_w, jaw_w, forehead_w", [
        (FaceShape.ROUND, 0.60, 0.62, 0.44, 0.44),     # Short, broad cheekbones
        (FaceShape.OBLONG, 1.05, 0.46, 0.41, 0.41),    # Long vertical axis
        (FaceShape.SQUARE, 0.66, 0.58, 0.56, 0.54),    # Equal width jaw and temples
        (FaceShape.HEART, 0.78, 0.55, 0.30, 0.56),     # Wide forehead, narrow jaw
        (FaceShape.DIAMOND, 0.82, 0.66, 0.35, 0.36),   # Cheekbones wider than forehead & jaw
        (FaceShape.TRIANGLE, 0.76, 0.50, 0.58, 0.38),  # Jaw wider than cheeks and forehead
    ])
    def test_discrete_shape_classifications(
        self, synthetic_canonical_mesh, target_shape, l_mod, cheek_w, jaw_w, forehead_w
    ):
        """Ensures the 7 discrete morphologic shapes are correctly classified at centroids."""
        m = synthetic_canonical_mesh.copy()
        m[FML.MENTON] = np.array([0.5, 0.12 + l_mod, 0.0])
        m[FML.ZYGOMATIC_LEFT] = np.array([0.5 + cheek_w / 2, 0.45, 0.0])
        m[FML.ZYGOMATIC_RIGHT] = np.array([0.5 - cheek_w / 2, 0.45, 0.0])
        m[FML.GONION_LEFT] = np.array([0.5 + jaw_w / 2, 0.68, 0.0])
        m[FML.GONION_RIGHT] = np.array([0.5 - jaw_w / 2, 0.68, 0.0])
        m[FML.TEMPLE_LEFT] = np.array([0.5 + forehead_w / 2, 0.22, 0.0])
        m[FML.TEMPLE_RIGHT] = np.array([0.5 - forehead_w / 2, 0.22, 0.0])

        metrics = FacialGeometryEngine.calculate_metrics(m)
        assert metrics.primary_shape == target_shape
