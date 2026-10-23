"""Domain 7: Beard & Mandibular Sculpting."""
from vogue_engine.core.engine.schemas.style_payload import DomainBeard
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics

class BeardDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics) -> DomainBeard:
        shape = geom.primary_shape
        angle = geom.mandibular_angle_degrees

        if shape in [FaceShape.ROUND, FaceShape.OBLONG]:
            rule = (
                "Grow dense, angular length at the menton chin point (8-10mm); tightly fade or razor cheek lines."
                if shape == FaceShape.ROUND
                else "Keep beard trimmed short on chin (3-4mm); maintain fuller sideburns and cheek density to widen profile."
            )
            length = 8 if shape == FaceShape.ROUND else 4
            fade = "Low Skin Drop Fade from Tragus" if shape == FaceShape.ROUND else "Full Parallel Blend"
            cheek = "Crisp Linear Sharp Angle" if shape == FaceShape.ROUND else "Natural Soft Horizontal"
        elif shape == FaceShape.SQUARE:
            rule = "Trim chin into a soft rounded goatee or maintain clean 3-day stubble; soften 90° gonion corners."
            length = 4
            fade = "Gentle Scissor Taper"
            cheek = "Subtle Curve softening bone prominence"
        elif shape == FaceShape.HEART:
            rule = "Full, dense boxed beard along entire mandibular jawline to build weight below narrow chin."
            length = 7
            fade = "Medium Taper"
            cheek = "Low Straight Cheekline"
        elif shape == FaceShape.DIAMOND:
            rule = "Classic full beard or heavy stubble to broaden chin and jaw perimeter."
            length = 6
            fade = "Natural Fade"
            cheek = "Medium Natural Line"
        elif shape == FaceShape.TRIANGLE:
            rule = "Clean-shaven or tight micro-stubble (1-2mm); avoid bulk that accentuates broad bigonial width."
            length = 2
            fade = "Ultra-Close Taper"
            cheek = "Crisp Diagonal"
        else:  # Oval
            rule = "Follow natural mandibular jawline angle; maintains versatile designer stubble or classic boxed contour."
            length = 5
            fade = "Uniform Classic Taper"
            cheek = "Sharp Defined Natural Arc"

        return DomainBeard(
            jawline_sculpt_rule=rule,
            length_grade_mm=length,
            fade_geometry=fade,
            cheekline_profile=cheek,
        )
