"""
Comprehensive 252-Permutation Combinatorial Coverage Pipeline.
Tests all permutations: 7 Face Shapes × 4 Seasons × 3 Undertones × 3 Contrast Levels.
Ensures zero runtime errors, complete 13-domain generation, valid visual coordinates,
and strict schema validation across the master matrix.
"""
import pytest
import itertools
import re

from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Season, Undertone, ContrastLevel, ColorimetricProfile
from vogue_engine.core.engine.combinatorial import StylePermutationDispatcher
from vogue_engine.core.engine.schemas.style_payload import MasterVogueStyleReport

HEX_REGEX = re.compile(r"^#[0-9a-fA-F]{6}$")


class TestCombinatorialGrid:

    @pytest.fixture(scope="class")
    def all_252_permutations(self):
        """Generates all 252 Cartesian product tuples."""
        shapes = list(FaceShape)
        seasons = list(Season)
        undertones = list(Undertone)
        contrasts = list(ContrastLevel)
        perms = list(itertools.product(shapes, seasons, undertones, contrasts))
        assert len(perms) == 252
        return perms

    def test_full_permutation_matrix_integrity(self, all_252_permutations):
        """
        Iterates over all 252 permutations and validates:
        1. No exceptions or null references.
        2. All 13 core luxury domains populated.
        3. Color hex codes strictly valid.
        4. Coordinate systems constrained within [0.0, 100.0].
        5. Better vs. Worse comparison vectors present with positive impact ratings.
        """
        for shape, season, undertone, contrast in all_252_permutations:
            mock_geom = FacialGeometryMetrics(
                length_to_width_ratio=1.45,
                jaw_to_zygomatic_ratio=0.76,
                forehead_to_zygomatic_ratio=0.82,
                jaw_to_forehead_ratio=0.92,
                bilateral_symmetry_score=94.5,
                mandibular_angle_degrees=105.0,
                primary_shape=shape,
                secondary_shape=FaceShape.OVAL,
                confidence=0.95,
            )

            mock_photo = ColorimetricProfile(
                ita_angle=32.0,
                undertone=undertone,
                contrast_level=contrast,
                season=season,
                skin_lab_mean=(64.0, 12.0, 16.0),
                iris_luminance=26.0,
                hair_luminance=16.0,
                confidence=0.94,
            )

            report = StylePermutationDispatcher.compile_report(
                report_uuid=f"test-{shape.value}-{season.value}-{undertone.value}-{contrast.value}",
                geom=mock_geom,
                photo=mock_photo,
                svg_overlay="<svg></svg>",
            )

            assert isinstance(report, MasterVogueStyleReport)

            # Domain 1: Rating
            assert 0.0 <= report.rating.symmetry_quotient <= 100.0
            assert 0.0 <= report.rating.overall_editorial_rating <= 100.0
            assert len(report.rating.radar_tensor) >= 4

            # Domain 2: Color
            assert report.color.season == season.value
            assert len(report.color.primary_swatches) >= 3
            assert len(report.color.neutral_anchors) >= 2
            assert len(report.color.avoid_swatches) >= 2
            for sw in report.color.primary_swatches + report.color.neutral_anchors + report.color.avoid_swatches:
                assert HEX_REGEX.match(sw.hex_code)
                assert 0.0 <= sw.layout.x <= 100.0
                assert 0.0 <= sw.layout.y <= 100.0
                assert 0.0 < sw.layout.width <= 100.0
                assert 0.0 < sw.layout.height <= 100.0

            # Domain 3: Outfits
            assert len(report.outfits.recommended_outfits) >= 2
            assert 0.0 <= report.outfits.visual_board_layout.width <= 100.0

            # Domain 4: Face Shape
            assert report.face_shape.classification == shape.value
            assert report.face_shape.framing_strategy != ""

            # Domain 5: Hair
            assert len(report.hair.editorial_cuts) >= 2
            assert len(report.hair.comparisons) >= 1
            assert report.hair.comparisons[0].visual_impact_rating >= 1.0

            # Domain 6: Eyewear
            assert len(report.eyewear.optimal_frame_geometries) >= 1
            assert len(report.eyewear.comparisons) >= 1

            # Domain 7: Beard
            assert report.beard.jawline_sculpt_rule != ""
            assert report.beard.length_grade_mm is not None

            # Domain 8: Accessories
            assert report.accessories.metal_undertone_match != ""
            assert report.accessories.jewelry_scale_gauge != ""

            # Domain 9: Patterns
            assert report.patterns.recommended_scale != ""
            assert len(report.patterns.optimal_motifs) >= 2

            # Domain 10: Footwear
            assert report.footwear.toe_box_geometry != ""
            assert len(report.footwear.leather_finishes) >= 2

            # Domain 11: Core Style
            assert report.core_style.primary_archetype != ""
            assert len(report.core_style.aesthetic_anchors) >= 2

            # Domain 12: Scorecard
            assert len(report.scorecard.domain_scores_normalized) >= 5
            assert len(report.scorecard.primary_strengths) >= 2

            # Domain 13: Shopping Checklist
            assert len(report.shopping_checklist.priority_acquisition_matrix) >= 3
            assert len(report.shopping_checklist.seasonal_investment_pieces) >= 2
