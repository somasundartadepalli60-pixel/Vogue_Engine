"""
Spring Seasonal Matrix.
Warm, radiant, light, and golden-infused luxury color swatches.
"""
from vogue_engine.core.engine.schemas.layout import VisualSwatch, GridCoordinate

SPRING_SWATCHES = {
    "primary": [
        VisualSwatch(
            hex_code="#FF7F50", 
            pantone_ref="PANTONE 16-1546 TCX", 
            role="Living Coral Nectar (Base)", 
            visual_weight=0.45, 
            layout=GridCoordinate(x=5.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#40E0D0", 
            pantone_ref="PANTONE 15-5217 TCX", 
            role="Vibrant Aquamarine (Anchor)", 
            visual_weight=0.35, 
            layout=GridCoordinate(x=28.0, y=10.0, width=20.0, height=20.0)
        ),
        VisualSwatch(
            hex_code="#FFD700", 
            pantone_ref="PANTONE 14-0848 TCX", 
            role="Warm Champagne Gold (Accent)", 
            visual_weight=0.20, 
            layout=GridCoordinate(x=51.0, y=10.0, width=20.0, height=20.0)
        ),
    ],
    "neutrals": [
        VisualSwatch(
            hex_code="#C2B280", 
            pantone_ref="PANTONE 14-1118 TCX", 
            role="Warm Sand Dune", 
            visual_weight=0.60, 
            layout=GridCoordinate(x=5.0, y=35.0, width=30.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#FFFDD0", 
            pantone_ref="PANTONE 11-0105 TCX", 
            role="Luminous Buttercream", 
            visual_weight=0.40, 
            layout=GridCoordinate(x=38.0, y=35.0, width=30.0, height=15.0)
        ),
    ],
    "avoid": [
        VisualSwatch(
            hex_code="#1C1C1C", 
            pantone_ref="PANTONE 19-4007 TCX", 
            role="Stark Jet Black (Overpowers Golden Radiance)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=5.0, y=55.0, width=20.0, height=15.0)
        ),
        VisualSwatch(
            hex_code="#4B0082", 
            pantone_ref="PANTONE 19-3638 TCX", 
            role="Heavy Muted Indigo (Drab and Sinking)", 
            visual_weight=0.50, 
            layout=GridCoordinate(x=28.0, y=55.0, width=20.0, height=15.0)
        ),
    ]
}
