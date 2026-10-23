"""
Summer Seasonal Matrix.
Cool, soft, muted, powdery pastel and slate luxury color swatches.
"""
from vogue_engine.core.engine.schemas.layout import VisualSwatch, GridCoordinate

SUMMER_SWATCHES = {
    "primary": [
        VisualSwatch(
            hex_code="#4682B4", 
            pantone_ref="PANTONE 17-4032 TCX", 
            role="Soft Powder Steel Blue (Base)", 
            visual_weight=0.45, 
            layout=GridCoordinate(x=5.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#C9A0DC", 
            pantone_ref="PANTONE 15-3817 TCX", 
            role="Muted Wisteria Lavender (Anchor)", 
            visual_weight=0.35, 
            layout=GridCoordinate(x=28.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#708090", 
            pantone_ref="PANTONE 18-3918 TCX", 
            role="Slate Mineral Blue (Accent)", 
            visual_weight=0.20, 
            layout=GridCoordinate(x=51.0, y=10.0, width=20.0, height=20.0)
        ),
    ],
    "neutrals": [
        VisualSwatch(
            hex_code="#778899", 
            pantone_ref="PANTONE 16-4408 TCX", 
            role="Polished Platinum Dove Grey", 
            visual_weight=0.60, 
            layout=GridCoordinate(x=5.0, y=35.0, width=30.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#F0F8FF", 
            pantone_ref="PANTONE 11-4001 TCX", 
            role="Crisp Frost Ice White", 
            visual_weight=0.40, 
            layout=GridCoordinate(x=38.0, y=35.0, width=30.0, height=15.0)
        ),
    ],
    "avoid": [
        VisualSwatch(
            hex_code="#FF4500", 
            pantone_ref="PANTONE 17-1463 TCX", 
            role="Fiery Orange-Red (Clashes with Cool Undertone)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=5.0, y=55.0, width=20.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#8B4513", 
            pantone_ref="PANTONE 18-1140 TCX", 
            role="Warm Cognac Rust (Creates Dull Muddy Appearance)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=28.0, y=55.0, width=20.0, height=15.0)
        ),
    ]
}
