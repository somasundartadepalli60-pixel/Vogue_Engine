"""
Autumn Seasonal Matrix.
Deep, warm, earthy luxury color palettes and visual swatch configurations.
"""
from vogue_engine.core.engine.schemas.layout import VisualSwatch, GridCoordinate

AUTUMN_SWATCHES = {
    "primary": [
        VisualSwatch(
            hex_code="#8B4513", 
            pantone_ref="PANTONE 18-1140 TCX", 
            role="Deep Rust Cognac (Base)", 
            visual_weight=0.45, 
            layout=GridCoordinate(x=5.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#556B2F", 
            pantone_ref="PANTONE 19-0515 TCX", 
            role="Dark Olive Moss (Anchor)", 
            visual_weight=0.35, 
            layout=GridCoordinate(x=28.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#D27D2D", 
            pantone_ref="PANTONE 16-1255 TCX", 
            role="Rich Amber Ochre (Accent)", 
            visual_weight=0.20, 
            layout=GridCoordinate(x=51.0, y=10.0, width=20.0, height=20.0)
        ),
    ],
    "neutrals": [
        VisualSwatch(
            hex_code="#2B2625", 
            pantone_ref="PANTONE 19-0812 TCX", 
            role="Bitter Chocolate Espresso", 
            visual_weight=0.60, 
            layout=GridCoordinate(x=5.0, y=35.0, width=30.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#F5E6D3", 
            pantone_ref="PANTONE 11-0107 TCX", 
            role="Raw Silk Ecru", 
            visual_weight=0.40, 
            layout=GridCoordinate(x=38.0, y=35.0, width=30.0, height=15.0)
        ),
    ],
    "avoid": [
        VisualSwatch(
            hex_code="#00FFFF", 
            pantone_ref="PANTONE 12-4401 TCX", 
            role="Harsh Cyan (Drains Warmth)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=5.0, y=55.0, width=20.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#FF007F", 
            pantone_ref="PANTONE 18-2133 TCX", 
            role="Electric Magenta (Severe Discordance)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=28.0, y=55.0, width=20.0, height=15.0)
        ),
    ]
}
