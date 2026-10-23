"""
Winter Seasonal Matrix.
Cool, vivid, high-contrast jewel tones and stark monochrome swatches.
"""
from vogue_engine.core.engine.schemas.layout import VisualSwatch, GridCoordinate

WINTER_SWATCHES = {
    "primary": [
        VisualSwatch(
            hex_code="#0B1B3D", 
            pantone_ref="PANTONE 19-3952 TCX", 
            role="Midnight Imperial Navy (Base)", 
            visual_weight=0.45, 
            layout=GridCoordinate(x=5.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#800020", 
            pantone_ref="PANTONE 19-1725 TCX", 
            role="Burgundy Bordeaux (Anchor)", 
            visual_weight=0.35, 
            layout=GridCoordinate(x=28.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#0047AB", 
            pantone_ref="PANTONE 19-4052 TCX", 
            role="Cobalt Royal Blue (Accent)", 
            visual_weight=0.20, 
            layout=GridCoordinate(x=51.0, y=10.0, width=20.0, height=20.0)
        ),
    ],
    "neutrals": [
        VisualSwatch(
            hex_code="#000000", 
            pantone_ref="PANTONE 19-4008 TCX", 
            role="Absolute Pitch Onyx", 
            visual_weight=0.60, 
            layout=GridCoordinate(x=5.0, y=35.0, width=30.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#FFFFFF", 
            pantone_ref="PANTONE 11-0601 TCX", 
            role="Optical Pure White", 
            visual_weight=0.40, 
            layout=GridCoordinate(x=38.0, y=35.0, width=30.0, height=15.0)
        ),
    ],
    "avoid": [
        VisualSwatch(
            hex_code="#D2B48C", 
            pantone_ref="PANTONE 16-1334 TCX", 
            role="Muted Muddy Tan (Muddies Cool Contrast)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=5.0, y=55.0, width=20.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#CC7722", 
            pantone_ref="PANTONE 16-1253 TCX", 
            role="Dull Ochre (Sallows Winter Skin)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=28.0, y=55.0, width=20.0, height=15.0)
        ),
    ]
}
