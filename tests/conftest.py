"""
Pytest Fixtures: Synthetic 3D MediaPipe FaceMesh Landmark Arrays and Image Buffers.
Enables reliable, deterministic testing of geometric and photometric algorithms.
"""
import pytest
import numpy as np
import cv2

from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML


@pytest.fixture
def synthetic_canonical_mesh() -> np.ndarray:
    """
    Returns a standardized, affine-aligned 468-point landmark array
    calibrated to a balanced Oval facial profile.
    """
    mesh = np.zeros((468, 3), dtype=np.float32)

    # Sagittal axis
    mesh[FML.TRICHION] = np.array([0.50, 0.12, 0.0])
    mesh[FML.GLABELLA] = np.array([0.50, 0.25, 0.0])
    mesh[FML.SELLION] = np.array([0.50, 0.32, 0.0])
    mesh[FML.NOSE_TIP] = np.array([0.50, 0.48, 0.0])
    mesh[FML.SUBNASALE] = np.array([0.50, 0.54, 0.0])
    mesh[FML.STOMION] = np.array([0.50, 0.65, 0.0])
    mesh[FML.MENTON] = np.array([0.50, 0.85, 0.0])

    # Bizygomatic width (Symmetric cheekbones)
    mesh[FML.ZYGOMATIC_LEFT] = np.array([0.75, 0.45, 0.0])
    mesh[FML.ZYGOMATIC_RIGHT] = np.array([0.25, 0.45, 0.0])

    # Bigonial width (Mandibular jaw angles)
    mesh[FML.GONION_LEFT] = np.array([0.69, 0.68, 0.0])
    mesh[FML.GONION_RIGHT] = np.array([0.31, 0.68, 0.0])

    # Temple / Forehead boundaries
    mesh[FML.TEMPLE_LEFT] = np.array([0.70, 0.22, 0.0])
    mesh[FML.TEMPLE_RIGHT] = np.array([0.30, 0.22, 0.0])
    mesh[FML.FOREHEAD_LEFT_CREST] = np.array([0.62, 0.16, 0.0])
    mesh[FML.FOREHEAD_RIGHT_CREST] = np.array([0.38, 0.16, 0.0])

    # Mid-jaw line points
    mesh[FML.JAW_LINE_LEFT_MID] = np.array([0.62, 0.77, 0.0])
    mesh[FML.JAW_LINE_RIGHT_MID] = np.array([0.38, 0.77, 0.0])

    # Ocular anchors
    mesh[FML.LEFT_EYE_OUTER] = np.array([0.66, 0.35, 0.0])
    mesh[FML.LEFT_EYE_INNER] = np.array([0.56, 0.35, 0.0])
    mesh[FML.RIGHT_EYE_INNER] = np.array([0.44, 0.35, 0.0])
    mesh[FML.RIGHT_EYE_OUTER] = np.array([0.34, 0.35, 0.0])

    # Cheek Sampling polygons
    for idx in FML.CHEEK_SAMPLE_RIGHT:
        mesh[idx] = np.array([0.35, 0.50, 0.0])
    for idx in FML.CHEEK_SAMPLE_LEFT:
        mesh[idx] = np.array([0.65, 0.50, 0.0])
    for idx in FML.FOREHEAD_SAMPLE:
        if idx != FML.TRICHION:
            mesh[idx] = np.array([0.50, 0.18, 0.0])

    return mesh


@pytest.fixture
def synthetic_face_image() -> np.ndarray:
    """
    Creates a synthetic 400x400 BGR face image with warm golden skin tone,
    dark hair region, and distinct iris regions.
    """
    img = np.zeros((400, 400, 3), dtype=np.uint8)

    # Base warm golden skin tone (BGR: ~60, 160, 210)
    img[:] = (120, 170, 220)

    # Hair region (Top 15%, dark brown/black: BGR: 20, 25, 30)
    img[0:60, :] = (20, 25, 30)

    # Iris regions (approximate eyes)
    cv2.circle(img, (140, 140), 10, (15, 20, 25), -1)
    cv2.circle(img, (260, 140), 10, (15, 20, 25), -1)

    return img
