"""Domain 4: Face Shape Morphometrics."""
from vogue_engine.core.engine.schemas.style_payload import DomainFaceShape
from vogue_engine.core.vision.geometry import FacialGeometryMetrics
from vogue_engine.core.vision.morphometrics import MorphometricVisualizer

class FaceShapeDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, svg_overlay: str = "") -> DomainFaceShape:
        if not svg_overlay:
            svg_overlay = f"<svg viewBox='0 0 100 100'><text x='10' y='50' fill='#D4AF37'>{geom.primary_shape.value}</text></svg>"

        framing = {
            "Oval": "Maintain natural symmetry; avoid artificial vertical exaggeration.",
            "Round": "Introduce angular vertical lines and crown height to elongate facial axis.",
            "Square": "Diffuse mandibular boxiness with sweeping curvilinear forms and soft textures.",
            "Heart": "Balance prominent forehead width with textured chin fullness and wider collars.",
            "Diamond": "Highlight sculptural zygomatic cheekbones while widening forehead and chin presence.",
            "Oblong": "Break vertical plane with horizontal lapel lines, lower bridges, and side hair volume.",
            "Triangle": "Expand upper-third temple volume to counterbalance dominant mandibular base."
        }

        return DomainFaceShape(
            classification=geom.primary_shape.value,
            secondary_profile=geom.secondary_shape.value,
            morphometric_overlay_svg=svg_overlay,
            geometric_proportions={
                "LengthToWidth": geom.length_to_width_ratio,
                "JawToCheek": geom.jaw_to_zygomatic_ratio,
                "ForeheadToCheek": geom.forehead_to_zygomatic_ratio,
                "MandibularAngle": geom.mandibular_angle_degrees,
            },
            framing_strategy=framing.get(geom.primary_shape.value, "Harmonize facial proportions.")
        )
