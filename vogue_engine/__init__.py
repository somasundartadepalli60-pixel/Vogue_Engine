"""
VogueEngine Core™ - Enterprise Personal Style, Facial Morphometrics, and Wardrobe Engine.
High-throughput, client/server-side deterministic style permutation and facial analysis.
"""

from __future__ import annotations

import importlib

__version__ = "1.0.0"

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

_IMPORT_MAP = {
    "FaceShape": ("vogue_engine.core.vision.geometry", "FaceShape"),
    "FacialGeometryMetrics": ("vogue_engine.core.vision.geometry", "FacialGeometryMetrics"),
    "Season": ("vogue_engine.core.vision.photometrics", "Season"),
    "Undertone": ("vogue_engine.core.vision.photometrics", "Undertone"),
    "ContrastLevel": ("vogue_engine.core.vision.photometrics", "ContrastLevel"),
    "ColorimetricProfile": ("vogue_engine.core.vision.photometrics", "ColorimetricProfile"),
    "VisionAnalysisPipeline": ("vogue_engine.core.vision.pipeline", "VisionAnalysisPipeline"),
    "VisionAnalysisResult": ("vogue_engine.core.vision.pipeline", "VisionAnalysisResult"),
    "StylePermutationDispatcher": ("vogue_engine.core.engine.combinatorial", "StylePermutationDispatcher"),
    "MasterVogueStyleReport": ("vogue_engine.core.engine.schemas.style_payload", "MasterVogueStyleReport"),
    "app": ("vogue_engine.dashboards.router", "app"),
}


def __getattr__(name: str):
    if name not in _IMPORT_MAP:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attribute_name = _IMPORT_MAP[name]
    module = importlib.import_module(module_name)
    value = getattr(module, attribute_name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))
