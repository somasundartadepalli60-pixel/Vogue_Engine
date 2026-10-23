"""
Administrative Review & Runtime Override Dashboard.
Statelessly isolates admin mutations using HMAC-SHA256 signature verification.
Path: /admin/review/{uuid}?token={token}
      /admin/override/{uuid}?token={token}
"""
from typing import Optional, Dict, Any
from fastapi import APIRouter, Path, Query, Body, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from vogue_engine.dashboards.crypto import StatelessTokenManager
from vogue_engine.dashboards.user import REPORT_CACHE, get_report_or_404
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Season, Undertone, ContrastLevel, ColorimetricProfile
from vogue_engine.core.engine.combinatorial import StylePermutationDispatcher

admin_router = APIRouter(prefix="/admin", tags=["Admin Auditing & Overrides"])
crypto_manager = StatelessTokenManager()


class AdminOverrideRequest(BaseModel):
    override_face_shape: Optional[FaceShape] = None
    override_season: Optional[Season] = None
    override_undertone: Optional[Undertone] = None
    override_contrast: Optional[ContrastLevel] = None
    curator_notes: str = Field(..., max_length=500, description="Audit trail rationale")


@admin_router.get("/review/{uuid}")
async def inspect_report_telemetry(
    uuid: str = Path(..., pattern=r"^[0-9a-fA-F-]{36}$"),
    token: str = Query(..., description="Cryptographically signed HMAC-SHA256 token")
):
    """
    Exposes raw geometric and photometric telemetry for audit and verification.
    Requires a valid HMAC token containing 'review' permissions.
    """
    auth = crypto_manager.verify_admin_token(report_uuid=uuid, token=token)
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Token invalid, expired, or signature verification failed."
        )

    if "review" not in auth.get("perms", []):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Token lacks 'review' claim."
        )

    report = get_report_or_404(uuid)
    if not report:
        raise HTTPException(status_code=404, detail=f"Report UUID '{uuid}' not found.")

    return {
        "status": "AUTHORIZATION_GRANTED",
        "actor_subject": auth.get("sub"),
        "role": auth.get("role"),
        "permissions": auth.get("perms"),
        "telemetry": {
            "calculated_face_shape": report.face_shape.classification,
            "calculated_season": report.color.season,
            "symmetry_score": report.rating.symmetry_quotient,
            "overall_rating": report.rating.overall_editorial_rating,
            "full_report": report.model_dump(),
        }
    }


@admin_router.post("/override/{uuid}")
async def apply_admin_override(
    uuid: str = Path(..., pattern=r"^[0-9a-fA-F-]{36}$"),
    token: str = Query(..., description="Cryptographically signed HMAC-SHA256 token"),
    overrides: AdminOverrideRequest = Body(...)
):
    """
    Applies admin overrides and recalculates all 13 downstream domains deterministically.
    Stateless: Uses HMAC token verification without database lookup.
    """
    auth = crypto_manager.verify_admin_token(report_uuid=uuid, token=token)
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Token signature invalid or expired."
        )

    if "override" not in auth.get("perms", []):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Token lacks 'override' permission."
        )

    current_report = get_report_or_404(uuid)
    if not current_report:
        raise HTTPException(status_code=404, detail="Target report not found.")

    # Determine overridden geometry
    target_shape = overrides.override_face_shape or FaceShape(current_report.face_shape.classification)
    geom = FacialGeometryMetrics(
        length_to_width_ratio=current_report.face_shape.geometric_proportions.get("LengthToWidth", 1.45),
        jaw_to_zygomatic_ratio=current_report.face_shape.geometric_proportions.get("JawToCheek", 0.76),
        forehead_to_zygomatic_ratio=current_report.face_shape.geometric_proportions.get("ForeheadToCheek", 0.82),
        jaw_to_forehead_ratio=0.92,
        bilateral_symmetry_score=current_report.rating.symmetry_quotient,
        mandibular_angle_degrees=current_report.face_shape.geometric_proportions.get("MandibularAngle", 105.0),
        primary_shape=target_shape,
        secondary_shape=FaceShape.OVAL,
        confidence=0.98,
    )

    # Determine overridden photometrics
    target_season = overrides.override_season or Season(current_report.color.season)
    target_undertone = overrides.override_undertone or Undertone.WARM
    target_contrast = overrides.override_contrast or ContrastLevel.MEDIUM

    photo = ColorimetricProfile(
        ita_angle=35.0,
        undertone=target_undertone,
        contrast_level=target_contrast,
        season=target_season,
        skin_lab_mean=(65.0, 12.0, 18.0),
        iris_luminance=28.0,
        hair_luminance=18.0,
        confidence=0.98,
    )

    # Deterministically recompile all 13 domains under new parameters
    new_report = StylePermutationDispatcher.compile_report(
        report_uuid=uuid,
        geom=geom,
        photo=photo,
        svg_overlay=current_report.face_shape.morphometric_overlay_svg
    )

    # Update cache
    REPORT_CACHE[uuid] = new_report

    return {
        "status": "MUTATION_SUCCESSFUL",
        "report_uuid": uuid,
        "curator_notes": overrides.curator_notes,
        "updated_domains": {
            "face_shape": new_report.face_shape.classification,
            "season": new_report.color.season,
            "optimal_frame": new_report.eyewear.optimal_frame_geometries[0],
            "recommended_cut": new_report.hair.editorial_cuts[0],
            "archetype": new_report.core_style.primary_archetype,
        }
    }
