"""
Unified 13-Domain Response Contract and Master Vogue Report Schema.
Strictly structures outputs for luxury magazine presentation (90% visuals / 10% text).
"""
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

from vogue_engine.core.engine.schemas.layout import GridCoordinate, VisualSwatch
from vogue_engine.core.engine.schemas.vectors import BetterWorseComparison


# ---------------- 13 Core Domain Schemas ----------------

class DomainRating(BaseModel):
    """Domain 1: Rating and Structural Harmony."""
    symmetry_quotient: float = Field(..., ge=0.0, le=100.0)
    proportional_harmony_index: float = Field(..., ge=0.0, le=100.0)
    contrast_balance_score: float = Field(..., ge=0.0, le=100.0)
    overall_editorial_rating: float = Field(..., ge=0.0, le=100.0)
    radar_tensor: Dict[str, float]


class DomainColor(BaseModel):
    """Domain 2: Color and Seasonal Harmony."""
    palette_title: str
    season: str
    primary_swatches: List[VisualSwatch]
    avoid_swatches: List[VisualSwatch]
    neutral_anchors: List[VisualSwatch]
    swatch_mosaic_coordinates: List[GridCoordinate]


class DomainOutfits(BaseModel):
    """Domain 3: Outfits and Editorial Capsules."""
    capsule_title: str
    silhouette_balancing_rule: str
    recommended_outfits: List[Dict[str, Any]]
    visual_board_layout: GridCoordinate


class DomainFaceShape(BaseModel):
    """Domain 4: Face Shape Morphometrics."""
    classification: str
    secondary_profile: str
    morphometric_overlay_svg: str
    geometric_proportions: Dict[str, float]
    framing_strategy: str


class DomainHair(BaseModel):
    """Domain 5: Hair Architecture."""
    editorial_cuts: List[str]
    volume_distribution_map: str
    parting_vector: str
    avoids: List[str]
    comparisons: List[BetterWorseComparison]


class DomainEyewear(BaseModel):
    """Domain 6: Eyewear and Optical Geometry."""
    optimal_frame_geometries: List[str]
    bridge_placement_rule: str
    rim_gauge_weight: str
    acetate_color_swatches: List[str]
    comparisons: List[BetterWorseComparison]


class DomainBeard(BaseModel):
    """Domain 7: Beard & Mandibular Sculpting."""
    jawline_sculpt_rule: str
    length_grade_mm: Optional[int]
    fade_geometry: str
    cheekline_profile: str


class DomainAccessories(BaseModel):
    """Domain 8: Accessories and Metallurgy."""
    metal_undertone_match: str
    jewelry_scale_gauge: str
    hat_brim_geometry: str
    neckwear_proportions: str


class DomainPatterns(BaseModel):
    """Domain 9: Pattern Scales and Geometries."""
    recommended_scale: str
    print_contrast: str
    optimal_motifs: List[str]
    avoid_motifs: List[str]


class DomainFootwear(BaseModel):
    """Domain 10: Footwear and Proportions."""
    toe_box_geometry: str
    silhouette_anchor_weight: str
    leather_finishes: List[str]


class DomainCoreStyle(BaseModel):
    """Domain 11: Core Style Archetype."""
    primary_archetype: str
    secondary_archetype: str
    aesthetic_anchors: List[str]
    editorial_headline: str


class DomainScorecard(BaseModel):
    """Domain 12: Comprehensive Metric Scorecard."""
    domain_scores_normalized: Dict[str, int]
    primary_strengths: List[str]
    optimization_priorities: List[str]


class DomainShoppingChecklist(BaseModel):
    """Domain 13: Curated Capsule Shopping Checklist."""
    priority_acquisition_matrix: List[Dict[str, Any]]
    seasonal_investment_pieces: List[str]


class MasterVogueStyleReport(BaseModel):
    """
    Unified 13-Domain Response Contract adhering to 90% visuals / 10% text luxury magazine ratio.
    """
    report_uuid: str
    timestamp: str
    rating: DomainRating
    color: DomainColor
    outfits: DomainOutfits
    face_shape: DomainFaceShape
    hair: DomainHair
    eyewear: DomainEyewear
    beard: DomainBeard
    accessories: DomainAccessories
    patterns: DomainPatterns
    footwear: DomainFootwear
    core_style: DomainCoreStyle
    scorecard: DomainScorecard
    shopping_checklist: DomainShoppingChecklist
