"""
VogueEngine Core™ - Enterprise Personal Style, Facial Morphometrics, and Wardrobe Engine.
High-throughput, client/server-side deterministic style permutation and facial analysis.
"""

__version__ = "1.0.0"

from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Season, Undertone, ContrastLevel, ColorimetricProfile
from vogue_engine.core.vision.pipeline import VisionAnalysisPipeline, VisionAnalysisResult
from vogue_engine.core.engine.combinatorial import StylePermutationDispatcher
from vogue_engine.core.engine.schemas.style_payload import MasterVogueStyleReport
from vogue_engine.dashboards.router import app

__all__ = [
    "__version__",
    "FaceShape",
    "FacialGeometryMetrics",
    "Season",
    "Undertone",
    "ContrastLevel",
    "ColorimetricProfile",
    "VisionAnalysisPipeline",
    "VisionAnalysisResult",
    "StylePermutationDispatcher",
    "MasterVogueStyleReport",
    "app",
]
