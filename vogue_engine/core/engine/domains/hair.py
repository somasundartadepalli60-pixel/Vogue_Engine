"""Domain 5: Hair Architecture."""
from vogue_engine.core.engine.schemas.style_payload import DomainHair
from vogue_engine.core.engine.schemas.vectors import BetterWorseComparison
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics

class HairDomainCalculator:
    @staticmethod
    def calculate(geom: FacialGeometryMetrics) -> DomainHair:
        shape = geom.primary_shape
        rules = {
            FaceShape.ROUND: {
                "cuts": ["Vertical Pompadour Fade", "Textured Ivy League Quiff", "High Taper Volume Crop"],
                "vol": "Heavy Crown Elevation / Tight Lateral Taper",
                "part": "Deep 75/25 Asymmetric Part",
                "avoid": ["Full Blunt Bangs", "Rounded Mushroom Crops"],
                "opt_rule": "Vertical lift adds necessary length to circular facial boundaries.",
                "sub_reason": "Lateral volume expands cheek width, aggravating roundness.",
            },
            FaceShape.SQUARE: {
                "cuts": ["Soft Textured Side Part", "Classic Scissor Taper", "Messy Textured Fringe"],
                "vol": "Even Lateral and Crown Distribution",
                "part": "Diagonal Natural Parting",
                "avoid": ["Severe Box Buzz Cuts", "Blunt Geometric Fringes"],
                "opt_rule": "Textured layers soften rigid 90-degree mandibular angles.",
                "sub_reason": "Sharp square lines intensify facial hardness.",
            },
            FaceShape.OBLONG: {
                "cuts": ["Low Classic Side Part", "Medium Scissor Cut with Side Flow", "Textured French Crop with Low Fringe"],
                "vol": "Lateral Side Fullness / Minimal Crown Lift",
                "part": "Horizontal Low Part",
                "avoid": ["High Volume Quiffs", "Shaved Undercuts"],
                "opt_rule": "Side width shortens vertical facial elongation.",
                "sub_reason": "High crown volume visually exaggerates long facial index.",
            },
            FaceShape.HEART: {
                "cuts": ["Mid-Length Textured Waves", "Curtain Fringe with Side Flow", "Longer Scissor Taper"],
                "vol": "Lower Lateral Density to fill chin region",
                "part": "Center or Soft 60/40 Part",
                "avoid": ["High Slicked Back Pomp", "Heavy Forehead Volume"],
                "opt_rule": "Side movement down to jawline balances narrow chin.",
                "sub_reason": "Crown volume widens an already prominent forehead.",
            },
            FaceShape.DIAMOND: {
                "cuts": ["Textured Flow Cut", "Swept Back Medium Length", "Faux Hawk with Tapered Sides"],
                "vol": "Forehead and Chin Width Expansion",
                "part": "Soft Diagonal Flow",
                "avoid": ["Extreme High Skin Fades", "Heavy Side Bulk over Cheekbones"],
                "opt_rule": "Forehead fullness balances dominant zygomatic cheekbones.",
                "sub_reason": "Exposing narrow forehead while leaving cheeks bare creates harsh diamond geometry.",
            },
            FaceShape.TRIANGLE: {
                "cuts": ["Textured Pompadour", "Layered Medium Scissor Cut", "Voluminous Side Sweep"],
                "vol": "Maximum Temple and Forehead Width",
                "part": "High Side Part",
                "avoid": ["Tapered Cuts that narrow the temples", "Chin-Length Bobs"],
                "opt_rule": "Adding width at temples balances heavy bigonial jaw width.",
                "sub_reason": "Slick flat sides make the jaw appear disproportionately wide.",
            },
            FaceShape.OVAL: {
                "cuts": ["Universal Classic Side Sweep", "Slick Back Scissor Cut", "Textured Crop"],
                "vol": "Natural Proportional Distribution",
                "part": "Natural Directional Fall",
                "avoid": ["Heavy Full Fringes that obscure facial symmetry"],
                "opt_rule": "Open forehead showcases balanced facial oval.",
                "sub_reason": "Overly dense bangs shorten and distort ideal oval balance.",
            },
        }

        cfg = rules.get(shape, rules[FaceShape.OVAL])

        return DomainHair(
            editorial_cuts=cfg["cuts"],
            volume_distribution_map=cfg["vol"],
            parting_vector=cfg["part"],
            avoids=cfg["avoid"],
            comparisons=[
                BetterWorseComparison(
                    category="Hairline Framing",
                    optimal_visual_asset_id=f"hair_{shape.value.lower()}_opt",
                    optimal_rule=cfg["opt_rule"],
                    suboptimal_visual_asset_id=f"hair_{shape.value.lower()}_sub",
                    suboptimal_reason=cfg["sub_reason"],
                    visual_impact_rating=9.2
                )
            ]
        )
