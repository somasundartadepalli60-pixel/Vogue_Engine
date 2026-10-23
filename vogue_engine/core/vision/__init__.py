"""
VogueEngine Vision Subsystem.
Zero-cloud mathematical morphometrics, CIELAB photometrics, and facial landmark extraction.
"""
from vogue_engine.core.vision.geometry import (
    FaceShape,
    FacialGeometryMetrics,
    FacialGeometryEngine,
)
from vogue_engine.core.vision.photometrics import (
    Season,
    Undertone,
    ContrastLevel,
    ColorimetricProfile,
    PhotometricEngine,
)
from vogue_engine.core.vision.pipeline import VisionAnalysisPipeline

__all__ = [
    "FaceShape",
    "FacialGeometryMetrics",
    "FacialGeometryEngine",
    "Season",
    "Undertone",
    "ContrastLevel",
    "ColorimetricProfile",
    "PhotometricEngine",
    "VisionAnalysisPipeline",
]
