"""
Unit Tests for Photometrics and CIELAB Color Science Engine.
Validates skin sampling, ITA° calculation, undertone ratios, and contrast tiers.
"""
import pytest
import numpy as np
import cv2

from vogue_engine.core.vision.photometrics import (
    PhotometricEngine,
    Season,
    Undertone,
    ContrastLevel,
)
from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML


class TestPhotometrics:

    def test_photometric_extraction_baseline(self, synthetic_face_image, synthetic_canonical_mesh):
        """Validates that a warm golden synthetic face yields Warm Undertone and valid ITA."""
        profile = PhotometricEngine.analyze_image(synthetic_face_image, synthetic_canonical_mesh)

        assert profile.undertone in [Undertone.WARM, Undertone.NEUTRAL]
        assert isinstance(profile.season, Season)
        assert isinstance(profile.contrast_level, ContrastLevel)
        assert -90.0 <= profile.ita_angle <= 90.0
        assert 0.0 <= profile.skin_lab_mean[0] <= 100.0

    def test_cool_undertone_detection(self, synthetic_canonical_mesh):
        """Creates an image with cool/pinkish undertone (low b*, higher a*)."""
        img = np.zeros((400, 400, 3), dtype=np.uint8)
        # BGR with strong blue/red components to produce pink/cool skin
        img[:] = (200, 160, 210)
        img[0:60, :] = (10, 10, 10)  # Dark hair

        profile = PhotometricEngine.analyze_image(img, synthetic_canonical_mesh)
        assert profile.undertone == Undertone.COOL

    def test_high_contrast_assignment(self, synthetic_canonical_mesh):
        """Creates an image with very light skin (L*~90) and pitch-black hair (L*~5)."""
        img = np.zeros((400, 400, 3), dtype=np.uint8)
        img[:] = (240, 240, 240)  # Very light
        img[0:60, :] = (0, 0, 0)     # Jet black hair

        profile = PhotometricEngine.analyze_image(img, synthetic_canonical_mesh)
        assert profile.contrast_level == ContrastLevel.HIGH
        assert profile.season in [Season.WINTER, Season.SPRING]
