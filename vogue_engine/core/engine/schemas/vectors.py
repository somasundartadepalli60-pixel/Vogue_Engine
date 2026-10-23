"""
Better vs Worse Comparative Visual Vector Schemas.
Pairs optimal stylistic solutions directly against sub-optimal choices with visual weightings.
"""
from pydantic import BaseModel, Field

class BetterWorseComparison(BaseModel):
    """Direct visual comparative layout object pairing optimal vs. sub-optimal styling."""
    category: str = Field(..., description="e.g., Eyewear Frame Angle, Hairline Framing, Lapel Width")
    optimal_visual_asset_id: str = Field(..., description="ID / path of recommended visual overlay")
    optimal_rule: str = Field(..., description="Actionable concise design rule")
    suboptimal_visual_asset_id: str = Field(..., description="ID / path of unharmonious visual choice")
    suboptimal_reason: str = Field(..., description="Morphometric reason for discordance")
    visual_impact_rating: float = Field(..., ge=1.0, le=10.0, description="Severity score 1.0 to 10.0")
