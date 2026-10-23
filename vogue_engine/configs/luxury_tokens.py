"""
Luxury Editorial Layout Tokens.
Specifies 90% Visual / 10% Narrative layout coordinate systems,
golden ratio typography scales, color swatch geometries, and editorial canvas parameters.
"""

class LuxuryLayoutTokens:
    # Editorial Magazine Visual-to-Text Ratios
    VISUAL_CANVAS_COLUMNS = 8
    NARRATIVE_RAIL_COLUMNS = 4
    GRID_TOTAL_COLUMNS = 12

    # Canvas Coordinate Normalization
    CANVAS_MIN_PERCENT = 0.0
    CANVAS_MAX_PERCENT = 100.0

    # Editorial Color Tokens
    COLOR_BACKGROUND_DARK = "#0D0D0D"
    COLOR_CANVAS_SURFACE = "#151515"
    COLOR_GOLD_ACCENT = "#D4AF37"
    COLOR_ROSE_GOLD = "#B76E79"
    COLOR_CREAM_TEXT = "#F8F5F0"
    COLOR_MUTED_SILVER = "#A0A0A0"
    COLOR_BORDER_SUBTLE = "rgba(212, 175, 55, 0.25)"

    # Typography Font Stacks
    FONT_HEADLINE = "'Bodoni MT', 'Didot', 'Cinzel', serif"
    FONT_BODY_TEXT = "'Helvetica Neue', 'Inter', -apple-system, sans-serif"
    FONT_MONO_METRIC = "'SF Mono', 'Roboto Mono', Menlo, monospace"

    # Default Coordinates for Domain Cards
    COORDINATES_HERO_CANVAS = {"x": 5.0, "y": 8.0, "width": 60.0, "height": 84.0}
    COORDINATES_NARRATIVE_SIDEBAR = {"x": 68.0, "y": 8.0, "width": 27.0, "height": 84.0}
    COORDINATES_FOOTER_METRICS = {"x": 5.0, "y": 93.0, "width": 90.0, "height": 5.0}
