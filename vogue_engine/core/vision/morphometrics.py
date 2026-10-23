"""
Facial Morphometrics and SVG Contour Projection Utilities.
Generates SVG overlay matrices, proportional radar tensors, and affine normalizations.
"""
from typing import Dict, Any, List
import numpy as np

from vogue_engine.configs.landmark_indices import FaceMeshLandmarks as FML
from vogue_engine.core.vision.geometry import FacialGeometryMetrics, FaceShape


class MorphometricVisualizer:
    """Renders mathematical SVG overlays and normalized coordinate boundaries."""

    @staticmethod
    def generate_svg_overlay(landmarks: np.ndarray, shape: FaceShape) -> str:
        """
        Creates a lightweight luxury SVG markup overlay depicting the geometric
        wireframe directly on normalized 0-100 coordinates.
        """
        # Outer jawline contour indices
        contour_indices = [
            10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
            397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
            172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109, 10
        ]
        
        path_elements = []
        for i, idx in enumerate(contour_indices):
            if idx < len(landmarks):
                x = round(float(landmarks[idx][0]) * 100.0, 2)
                y = round(float(landmarks[idx][1]) * 100.0, 2)
                prefix = "M" if i == 0 else "L"
                path_elements.append(f"{prefix} {x} {y}")

        contour_d = " ".join(path_elements) + " Z"

        # Glabella to Menton Sagittal Midline
        g_x = round(float(landmarks[FML.GLABELLA][0]) * 100.0, 2)
        g_y = round(float(landmarks[FML.GLABELLA][1]) * 100.0, 2)
        m_x = round(float(landmarks[FML.MENTON][0]) * 100.0, 2)
        m_y = round(float(landmarks[FML.MENTON][1]) * 100.0, 2)
        midline_d = f"M {g_x} {g_y} L {m_x} {m_y}"

        # Cheekbone Bi-Zygomatic Transverse line
        zl_x = round(float(landmarks[FML.ZYGOMATIC_LEFT][0]) * 100.0, 2)
        zl_y = round(float(landmarks[FML.ZYGOMATIC_LEFT][1]) * 100.0, 2)
        zr_x = round(float(landmarks[FML.ZYGOMATIC_RIGHT][0]) * 100.0, 2)
        zr_y = round(float(landmarks[FML.ZYGOMATIC_RIGHT][1]) * 100.0, 2)
        transverse_d = f"M {zl_x} {zl_y} L {zr_x} {zr_y}"

        svg = (
            f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' class='vogue-morphometric-overlay'>"
            f"<path d='{contour_d}' fill='none' stroke='#D4AF37' stroke-width='0.75' stroke-dasharray='2,1' opacity='0.85'/>"
            f"<path d='{midline_d}' stroke='#F8F5F0' stroke-width='0.5' stroke-opacity='0.6'/>"
            f"<path d='{transverse_d}' stroke='#D4AF37' stroke-width='0.5' stroke-opacity='0.75'/>"
            f"<circle cx='{zl_x}' cy='{zl_y}' r='1.2' fill='#D4AF37'/>"
            f"<circle cx='{zr_x}' cy='{zr_y}' r='1.2' fill='#D4AF37'/>"
            f"<circle cx='{m_x}' cy='{m_y}' r='1.2' fill='#D4AF37'/>"
            f"<text x='5' y='95' fill='#D4AF37' font-size='3.5' font-family='monospace'>{shape.value.upper()} PROFILE</text>"
            f"</svg>"
        )
        return svg
