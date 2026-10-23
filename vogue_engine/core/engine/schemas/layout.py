"""
Luxury Layout Grid and Coordinate Schemas.
Enforces the 90% visuals / 10% text ratio across all domains.
"""
from pydantic import BaseModel, Field

class GridCoordinate(BaseModel):
    """Normalized 0-100 canvas coordinates for editorial visual placement."""
    x: float = Field(..., ge=0.0, le=100.0, description="Horizontal top-left anchor percentage")
    y: float = Field(..., ge=0.0, le=100.0, description="Vertical top-left anchor percentage")
    width: float = Field(..., ge=0.0, le=100.0, description="Bounding width percentage")
    height: float = Field(..., ge=0.0, le=100.0, description="Bounding height percentage")
    z_index: int = Field(default=1, description="Z-index stack order")


class VisualSwatch(BaseModel):
    """High-density color swatch block for luxury palettes."""
    hex_code: str = Field(..., pattern=r"^#[0-9a-fA-F]{6}$", description="Hexadecimal color string")
    pantone_ref: str = Field(..., description="Pantone TCX / Fashion & Home reference")
    role: str = Field(..., description="e.g., Anchor Neutral, Accent Glow, Contrast Statement")
    visual_weight: float = Field(..., ge=0.0, le=1.0, description="Relative area prominence (0.0 to 1.0)")
    layout: GridCoordinate
