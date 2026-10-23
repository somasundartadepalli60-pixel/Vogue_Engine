"""
Unified Dual Dashboard Router and Application Factory.
Provides strict routing isolation between User Reports and Admin Overrides.
"""
import uuid
from typing import Optional
from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from vogue_engine.dashboards.user import user_router, REPORT_CACHE
from vogue_engine.dashboards.admin import admin_router, crypto_manager
from vogue_engine.core.vision.pipeline import VisionAnalysisPipeline
from vogue_engine.core.engine.combinatorial import StylePermutationDispatcher

app = FastAPI(
    title="VogueEngine Core™",
    description="Enterprise Open-Source Personal Style, Facial Analysis, and Wardrobe Engine",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers
app.include_router(user_router)
app.include_router(admin_router)

# Stage 1: offline wardrobe inventory and outfit planner
from vogue_engine.wardrobe.api import router as wardrobe_router
app.include_router(wardrobe_router)

# Vision Pipeline Instance
pipeline = VisionAnalysisPipeline()


@app.get("/health", tags=["Telemetry"])
async def health_check():
    return {
        "status": "HEALTHY",
        "service": "VogueEngine Core",
        "engine_strategy": "Deterministic Combinatorial Matrix (252 States)",
        "domains_supported": 13,
        "active_cached_reports": len(REPORT_CACHE),
    }


@app.post("/api/v1/analyze", tags=["Vision Analysis Pipeline"])
async def analyze_image_endpoint(
    file: UploadFile = File(..., description="Facial portrait image (JPEG/PNG)"),
    generate_admin_token: bool = Form(default=True, description="Return an admin override token"),
):
    """
    Client/Server-side image analysis.
    Executes MediaPipe landmark detection, geometric calculations, photometric colorimetry,
    and combinatorial style compilation across all 13 domains.
    """
    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Empty file upload.")

    try:
        # Run vision analysis pipeline
        vision_result = pipeline.process_image(image_bytes)

        # Generate unique report identifier
        report_uuid = str(uuid.uuid4())

        # Compile style report across all 13 domains
        report = StylePermutationDispatcher.compile_report(
            report_uuid=report_uuid,
            geom=vision_result.geometry,
            photo=vision_result.photometrics,
            svg_overlay=vision_result.svg_overlay,
        )

        # Store in cache
        REPORT_CACHE[report_uuid] = report
        from vogue_engine.dashboards.report_store import ReportStore
        ReportStore().save(report)

        response = {
            "report_uuid": report_uuid,
            "user_dashboard_url": f"/dashboard/report/{report_uuid}",
            "classification": {
                "face_shape": vision_result.geometry.primary_shape.value,
                "season": vision_result.photometrics.season.value,
                "undertone": vision_result.photometrics.undertone.value,
                "contrast": vision_result.photometrics.contrast_level.value,
                "symmetry_score": vision_result.geometry.bilateral_symmetry_score,
            },
        }

        if generate_admin_token:
            admin_token = crypto_manager.generate_admin_token(
                report_uuid=report_uuid,
                permissions=["review", "override"]
            )
            response["admin_override_url"] = f"/admin/review/{report_uuid}?token={admin_token}"
            response["admin_token"] = admin_token

        return JSONResponse(content=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

# Stage 2: offline backup, calendar, search and local dashboard
from pathlib import Path
from fastapi.responses import FileResponse
from vogue_engine.wardrobe.stage2 import router as wardrobe_stage2_router
app.include_router(wardrobe_stage2_router)

@app.get('/wardrobe', include_in_schema=False)
def wardrobe_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'index.html')

# Stage 3: local privacy endpoints
from vogue_engine.dashboards.privacy import router as privacy_router
app.include_router(privacy_router)

# Stage 4: local wardrobe wear history and analytics
from vogue_engine.wardrobe.analytics import router as wardrobe_analytics_router
app.include_router(wardrobe_analytics_router)

@app.get('/wardrobe/insights', include_in_schema=False)
def wardrobe_insights():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage4.html')

# Stage 5: offline personalized styling and seasonal coverage
from vogue_engine.wardrobe.personalization import router as personalization_router
app.include_router(personalization_router)

@app.get('/wardrobe/style', include_in_schema=False)
def wardrobe_style_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage5.html')

# Stage 6: offline inventory organization
from vogue_engine.wardrobe.organization_api import router as organization_router
app.include_router(organization_router)

# Stage 7: offline purchase tracking and wardrobe budgets
from vogue_engine.wardrobe.finance_api import router as finance_router
app.include_router(finance_router)

from vogue_engine.wardrobe.care_api import router as care_router
app.include_router(care_router)

# Stage 9: offline travel packing and outfit scheduling
from vogue_engine.wardrobe.travel_api import router as travel_router
app.include_router(travel_router)

# Stage 10: offline garment lifecycle and sustainability reporting
from vogue_engine.wardrobe.sustainability_api import router as sustainability_router
app.include_router(sustainability_router)

# Stage 11: offline outfit calendar, availability, and forecasting.
from vogue_engine.wardrobe.calendar_api import router as calendar_router
app.include_router(calendar_router)

# Stage 12: explainable recommendations and offline feedback.
from vogue_engine.wardrobe.recommendation import router as recommendation_router
app.include_router(recommendation_router)

# Stage 13: local visual recommendation studio
@app.get('/wardrobe/recommendations', include_in_schema=False)
def recommendation_studio():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage13.html')

# Stage 14: local garment photo gallery
from vogue_engine.wardrobe.photos_api import router as photos_router
app.include_router(photos_router)

@app.get('/wardrobe/photos', include_in_schema=False)
def photos_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage14.html')

# Stage 15: offline image color palettes and visual search
from vogue_engine.wardrobe.color_api import router as color_router
app.include_router(color_router)

# Stage 16: offline, explainable photo metadata suggestions
from vogue_engine.wardrobe.metadata_api import router as metadata_router
app.include_router(metadata_router)

# Stage 17: local perceptual image similarity and duplicate candidate discovery
from vogue_engine.wardrobe.similarity_api import router as similarity_router
app.include_router(similarity_router)

# Stage 18: offline visual organization and bulk photo management
from vogue_engine.wardrobe.bulk_photos_api import router as bulk_photos_router
app.include_router(bulk_photos_router)

@app.get('/wardrobe/organize', include_in_schema=False)
def wardrobe_photo_organizer():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage18.html')

# Stage 19: offline garment measurement and fit profiles
from vogue_engine.wardrobe.measurements_api import router as measurements_router
app.include_router(measurements_router)

# Stage 20: browser-based measurement management (no external assets).
@app.get('/wardrobe/measurements', include_in_schema=False)
def wardrobe_measurements_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage20.html')

# Stage 21: offline alterations and tailoring history.
from vogue_engine.wardrobe.alterations_api import router as alterations_router
app.include_router(alterations_router)

# Stage 22: local tailoring dashboard.
@app.get('/wardrobe/tailoring', include_in_schema=False)
def tailoring_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage22.html')

# Stage 23: local garment lending and borrowing.
from vogue_engine.wardrobe.lending_api import router as lending_router
app.include_router(lending_router)


# Stage 24: offline lending calendar and activity dashboard.
@app.get('/wardrobe/lending', include_in_schema=False)
def lending_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage24.html')

# Stage 25: local wardrobe inventory audits and integrity reporting
from vogue_engine.wardrobe.audit_api import router as audit_router
app.include_router(audit_router)

# Stage 26: local inventory audit dashboard
@app.get('/wardrobe/audits', include_in_schema=False)
def audit_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage26.html')

# Stage 27: local SQLite backup and guarded restore operations.
from vogue_engine.wardrobe.backups_api import router as backups_router
app.include_router(backups_router)

# Stage 28: browser-based local backup and restore management.
@app.get('/wardrobe/backups', include_in_schema=False)
def wardrobe_backups_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage28.html')

# Stage 29: local JSON/CSV archive export and validated garment import.
from vogue_engine.wardrobe.portability_api import router as portability_router
app.include_router(portability_router)

# Stage 30: browser-based, offline portable import/export dashboard.
from pathlib import Path as _Stage30Path
from fastapi.responses import HTMLResponse as _Stage30HTMLResponse

@app.get('/wardrobe/portability', response_class=_Stage30HTMLResponse, tags=['Wardrobe Portability'])
def wardrobe_portability_dashboard():
    dashboard = _Stage30Path(__file__).resolve().parent.parent / 'wardrobe' / 'portable_dashboard.html'
    return _Stage30HTMLResponse(dashboard.read_text(encoding='utf-8'))

# Stage 31: local, append-only activity history for wardrobe changes.
from vogue_engine.wardrobe.activity_api import router as activity_router
app.include_router(activity_router)

# Stage 32: local activity timeline, comparison view, and analytics dashboard.
@app.get('/wardrobe/activity', include_in_schema=False)
def wardrobe_activity_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage32.html')

# Stage 33: offline, opt-in wardrobe reminders and notification history.
from vogue_engine.wardrobe.reminders_api import router as reminders_router
app.include_router(reminders_router)

# Stage 34: offline reminder management dashboard.
@app.get('/wardrobe/reminders', include_in_schema=False)
def wardrobe_reminders_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage34.html')

# Stage 35: local maintenance plans, cleaning history, and rule-based recommendations.
from vogue_engine.wardrobe.maintenance_api import router as maintenance_router
app.include_router(maintenance_router)

# Stage 36: offline garment care calendar and maintenance dashboard.
@app.get('/wardrobe/maintenance', include_in_schema=False)
def wardrobe_maintenance_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage36.html')

# Stage 37: offline trip packing and travel wardrobe dashboard.
@app.get('/wardrobe/travel', include_in_schema=False)
def wardrobe_travel_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage37.html')

# Stage 39: local travel template management and trip comparison.
@app.get('/wardrobe/travel/templates', include_in_schema=False)
def wardrobe_travel_templates_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage39.html')

# Stage 40: offline, explainable outfit combinations and color scoring.
from vogue_engine.wardrobe.outfit_engine_api import router as outfit_engine_router
app.include_router(outfit_engine_router)

# Stage 41: offline interactive outfit recommendations and guarded saving.
from vogue_engine.wardrobe.outfit_dashboard_api import router as outfit_dashboard_router
app.include_router(outfit_dashboard_router)

@app.get('/wardrobe/outfit-engine', include_in_schema=False)
def outfit_engine_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage41.html')

# Stage 42: local outfit ratings, favorites and feedback-aware ranking.
from vogue_engine.wardrobe.outfit_feedback_api import router as outfit_feedback_router
app.include_router(outfit_feedback_router)

# Stage 43: interactive outfit feedback gallery and analytics.
@app.get('/wardrobe/outfit-feedback', include_in_schema=False)
def outfit_feedback_dashboard():
    return FileResponse(Path(__file__).resolve().parent.parent / 'wardrobe' / 'static' / 'stage43.html')
