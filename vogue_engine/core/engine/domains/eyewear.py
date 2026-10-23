"""Domain 6: Eyewear and Optical Geometry."""
from vogue_engine.core.engine.schemas.style_payload import DomainEyewear
from vogue_engine.core.engine.schemas.vectors import BetterWorseComparison
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Undertone, ColorimetricProfile

class EyewearDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics, photo: ColorimetricProfile) -> DomainEyewear:
        shape = geom.primary_shape
        undertone = photo.undertone

        acetates = (
            ["Vintage Champagne Tortoise", "Warm Cognac Horn", "Amber Havana"]
            if undertone == Undertone.WARM
            else ["Smoky Translucent Charcoal", "Polished Black Onyx", "Ice Crystal Grey"]
        )

        configs = {
            FaceShape.ROUND: {
                "frames": ["Architectural Rectangular", "Square Wayfarer", "Geometric D-Frame"],
                "bridge": "High-Set Straight Bridge (Elongates Nose)",
                "rim": "Bold Heavy Gauge (4.5mm - 6.0mm)",
                "opt_rule": "Sharp angular corners add definition to soft circular cheeklines.",
                "sub_reason": "Circular rim profiles mirror and amplify facial spherical curves.",
            },
            FaceShape.SQUARE: {
                "frames": ["Curved Crown Panto", "Soft Oval Titanium", "Teardrop Aviator"],
                "bridge": "Mid-Set Keyhole Bridge",
                "rim": "Medium-to-Fine Gauge (2.5mm - 3.5mm)",
                "opt_rule": "Curvilinear frames visually soften rigid mandibular corners.",
                "sub_reason": "Boxy rectangular frames double down on severe right-angled jawlines.",
            },
            FaceShape.OBLONG: {
                "frames": ["Tall Geometric P3", "Oversized Square", "Broad Pilot Frames"],
                "bridge": "Low-Set Horizontal Bridge (Shortens Vertical Axis)",
                "rim": "Substantial Heavy Acetate",
                "opt_rule": "Deep vertical lens dimensions break and balance long facial height.",
                "sub_reason": "Narrow shallow wireframes accentuate long vertical proportions.",
            },
            FaceShape.HEART: {
                "frames": ["Lightweight Rimless", "Bottom-Heavy Clubmaster", "Soft Rounded Pantos"],
                "bridge": "Low-Profile Saddle Bridge",
                "rim": "Fine Ultra-Light Titanium (1.5mm - 2.0mm)",
                "opt_rule": "Lightweight top rim prevents adding visual weight to broad forehead.",
                "sub_reason": "Heavy exaggerated browline frames overwhelm delicate chin area.",
            },
            FaceShape.DIAMOND: {
                "frames": ["Classic Horn-Rimmed Clubmaster", "Curved Cat-Eye/Oval", "Geometric Rounded Wire"],
                "bridge": "Keyhole Bridge",
                "rim": "Medium Gauge Upper Accent",
                "opt_rule": "Prominent browline frames widen narrow forehead above zygomatic arches.",
                "sub_reason": "Narrow angular frames clash with high, prominent cheekbones.",
            },
            FaceShape.TRIANGLE: {
                "frames": ["Heavy Browline / Clubmaster", "Wide Rectangular Aviator", "Bold Wayfarer"],
                "bridge": "High-Set Accent Bridge",
                "rim": "Heavy Top Rim / Semi-Rimless Bottom",
                "opt_rule": "Dramatic upper-rim styling broadens temples to balance wide jaw.",
                "sub_reason": "Bottom-heavy round glasses draw all visual focus to the mandibular base.",
            },
            FaceShape.OVAL: {
                "frames": ["Universal Wellington", "Geometric Hexagonal", "Crown Panto Classic"],
                "bridge": "Standard Proportional Bridge",
                "rim": "Medium Balanced Gauge (3.0mm - 4.5mm)",
                "opt_rule": "Frame width matching exact cheekbone width preserves natural symmetry.",
                "sub_reason": "Grossly oversized frames spill beyond facial perimeter, spoiling balance.",
            },
        }

        cfg = configs.get(shape, configs[FaceShape.OVAL])

        return DomainEyewear(
            optimal_frame_geometries=cfg["frames"],
            bridge_placement_rule=cfg["bridge"],
            rim_gauge_weight=cfg["rim"],
            acetate_color_swatches=acetates,
            comparisons=[
                BetterWorseComparison(
                    category="Optical Frame Geometry",
                    optimal_visual_asset_id=f"eye_{shape.value.lower()}_opt",
                    optimal_rule=cfg["opt_rule"],
                    suboptimal_visual_asset_id=f"eye_{shape.value.lower()}_sub",
                    suboptimal_reason=cfg["sub_reason"],
                    visual_impact_rating=9.6
                )
            ]
        )
