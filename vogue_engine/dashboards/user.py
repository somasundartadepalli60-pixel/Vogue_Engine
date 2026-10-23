"""
User Report Dashboard.
Renders read-only luxury magazine layouts (90% visuals / 10% narrative rail).
Path: /dashboard/report/{uuid}
"""
from typing import Dict, Optional
from fastapi import APIRouter, Path, Query, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse

from vogue_engine.core.engine.schemas.style_payload import MasterVogueStyleReport

user_router = APIRouter(prefix="/dashboard", tags=["User Luxury Dashboard"])

# Shared in-memory / cache registry for stateless demonstration
REPORT_CACHE: Dict[str, MasterVogueStyleReport] = {}

def get_report_or_404(uuid: str) -> MasterVogueStyleReport:
    report = REPORT_CACHE.get(uuid)
    if report is None:
        from .report_store import ReportStore
        report = ReportStore().get(uuid)
        if report is not None:
            REPORT_CACHE[uuid] = report
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"VogueEngine report '{uuid}' not found or session expired."
        )
    return report

@user_router.get("/report/{uuid}", response_class=HTMLResponse)
async def view_user_report(
    uuid: str = Path(..., pattern=r"^[0-9a-fA-F-]{36}$", description="Report UUIDv4"),
    format: Optional[str] = Query(None, description="Set to 'json' for raw structured contract")
):
    """
    Renders the luxury editorial report adhering to the 90% visuals / 10% narrative rule.
    """
    report = get_report_or_404(uuid)

    if format == "json":
        return JSONResponse(content=report.model_dump())

    # Build High-End Magazine HTML
    swatches_html = ""
    for sw in report.color.primary_swatches:
        swatches_html += f"""
        <div class="swatch-tile" style="left: {sw.layout.x}%; top: {sw.layout.y}%; width: {sw.layout.width}%; height: {sw.layout.height}%; background-color: {sw.hex_code};">
            <div class="swatch-meta">
                <span class="swatch-hex">{sw.hex_code}</span>
                <span class="swatch-pantone">{sw.pantone_ref}</span>
                <span class="swatch-role">{sw.role}</span>
            </div>
        </div>
        """

    for sw in report.color.neutral_anchors:
        swatches_html += f"""
        <div class="swatch-tile neutral" style="left: {sw.layout.x}%; top: {sw.layout.y}%; width: {sw.layout.width}%; height: {sw.layout.height}%; background-color: {sw.hex_code};">
            <div class="swatch-meta">
                <span class="swatch-hex">{sw.hex_code}</span>
                <span class="swatch-role">{sw.role}</span>
            </div>
        </div>
        """

    avoid_html = "".join([
        f"<span class='avoid-badge' style='background:{sw.hex_code};'>{sw.role}</span>"
        for sw in report.color.avoid_swatches
    ])

    outfit_cards = "".join([
        f"""
        <div class="outfit-card">
            <h4>{outfit['style']}</h4>
            <ul>
                {''.join([f'<li>{c}</li>' for c in outfit['components']])}
            </ul>
        </div>
        """ for outfit in report.outfits.recommended_outfits
    ])

    shopping_items = "".join([
        f"""
        <div class="shopping-row">
            <span class="rank">#{item['rank']}</span>
            <span class="cat">{item['domain']}</span>
            <span class="desc">{item['item']}</span>
            <span class="prio">{item['priority']}</span>
        </div>
        """ for item in report.shopping_checklist.priority_acquisition_matrix
    ])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VogueEngine Core | Portfolio #{report.report_uuid[:8]}</title>
        <style>
            :root {{
                --bg: #0D0D0D;
                --surface: #151515;
                --gold: #D4AF37;
                --rose-gold: #B76E79;
                --cream: #F8F5F0;
                --muted: #A0A0A0;
                --border: rgba(212, 175, 55, 0.25);
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
                background-color: var(--bg);
                color: var(--cream);
                font-family: 'Bodoni MT', 'Didot', 'Cinzel', Georgia, serif;
                padding: 40px;
                min-height: 100vh;
            }}
            .editorial-page {{
                max-width: 1500px;
                margin: 0 auto;
                border: 1px solid var(--border);
                padding: 40px;
                background-color: var(--surface);
                box-shadow: 0 20px 60px rgba(0,0,0,0.8);
            }}
            header {{
                display: flex;
                justify-content: space-between;
                align-items: baseline;
                border-bottom: 2px solid var(--gold);
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            h1.masthead {{
                font-size: 3.2rem;
                letter-spacing: 0.35rem;
                text-transform: uppercase;
                color: var(--gold);
            }}
            .sub-masthead {{
                font-family: 'Helvetica Neue', sans-serif;
                font-size: 0.85rem;
                letter-spacing: 0.15rem;
                color: var(--muted);
                text-transform: uppercase;
            }}
            .magazine-grid {{
                display: grid;
                grid-template-columns: 8fr 4fr;
                gap: 40px;
            }}
            /* 90% Visual Canvas Area */
            .visual-canvas {{
                position: relative;
                min-height: 750px;
                background: #080808;
                border: 1px solid #222;
                overflow: hidden;
            }}
            .canvas-header {{
                padding: 15px 25px;
                background: #111;
                font-family: 'Helvetica Neue', sans-serif;
                font-size: 0.75rem;
                letter-spacing: 0.1rem;
                color: var(--gold);
                border-bottom: 1px solid #222;
                display: flex;
                justify-content: space-between;
            }}
            .swatch-tile {{
                position: absolute;
                border: 1px solid rgba(255,255,255,0.15);
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
                display: flex;
                align-items: flex-end;
                padding: 12px;
            }}
            .swatch-tile:hover {{
                transform: scale(1.04);
                z-index: 20;
                box-shadow: 0 10px 30px rgba(0,0,0,0.9);
                border-color: var(--gold);
            }}
            .swatch-meta {{
                background: rgba(0,0,0,0.75);
                backdrop-filter: blur(8px);
                padding: 6px 10px;
                font-family: 'Helvetica Neue', monospace;
                font-size: 0.7rem;
                display: flex;
                flex-direction: column;
                gap: 2px;
            }}
            .swatch-hex {{ font-weight: bold; color: #fff; }}
            .swatch-pantone {{ color: var(--gold); }}
            .swatch-role {{ color: var(--muted); }}
            
            .overlay-container {{
                position: absolute;
                right: 20px;
                bottom: 20px;
                width: 260px;
                height: 260px;
                border: 1px solid var(--border);
                background: rgba(13, 13, 13, 0.85);
                backdrop-filter: blur(10px);
                padding: 10px;
            }}

            /* 10% Narrative Rail */
            .narrative-rail {{
                font-family: 'Helvetica Neue', 'Inter', sans-serif;
                font-size: 0.88rem;
                line-height: 1.65;
                color: #C0C0C0;
                display: flex;
                flex-direction: column;
                gap: 28px;
            }}
            .section-tag {{
                font-family: 'Cinzel', serif;
                font-size: 1.1rem;
                color: var(--gold);
                margin-bottom: 8px;
                text-transform: uppercase;
                letter-spacing: 0.1rem;
                border-left: 2px solid var(--gold);
                padding-left: 10px;
            }}
            .metric-badge {{
                display: inline-block;
                background: #202020;
                color: var(--cream);
                padding: 4px 10px;
                border-radius: 2px;
                font-size: 0.8rem;
                font-weight: bold;
                border: 1px solid #333;
            }}
            .avoid-container {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }}
            .avoid-badge {{
                padding: 4px 8px;
                font-size: 0.7rem;
                color: #fff;
                border-radius: 2px;
                text-shadow: 0 1px 2px #000;
            }}
            .outfit-grid {{ display: flex; flex-direction: column; gap: 12px; margin-top: 8px; }}
            .outfit-card {{
                background: #101010;
                border: 1px solid #222;
                padding: 12px;
            }}
            .outfit-card h4 {{ color: var(--gold); font-size: 0.82rem; margin-bottom: 4px; }}
            .outfit-card ul {{ padding-left: 18px; font-size: 0.78rem; color: var(--muted); }}
            .shopping-row {{
                display: flex;
                justify-content: space-between;
                font-size: 0.78rem;
                padding: 6px 0;
                border-bottom: 1px solid #222;
            }}
            .shopping-row .rank {{ color: var(--gold); font-weight: bold; }}
            .shopping-row .cat {{ color: var(--muted); }}
            .shopping-row .desc {{ color: #eee; flex: 1; padding: 0 10px; }}
            .shopping-row .prio {{ color: var(--rose-gold); font-size: 0.7rem; }}
        </style>
    </head>
    <body>
        <div class="editorial-page">
            <header>
                <div>
                    <h1 class="masthead">VogueEngine</h1>
                    <div class="sub-masthead">Haute Couture Personal Style Matrix // Vol. 26</div>
                </div>
                <div style="text-align: right;">
                    <div class="sub-masthead">PORTFOLIO REF: #{report.report_uuid[:12]}</div>
                    <div style="color: var(--gold); font-size: 0.9rem;">{report.core_style.primary_archetype}</div>
                </div>
            </header>

            <div class="magazine-grid">
                <!-- 90% Visual Area -->
                <div class="visual-canvas">
                    <div class="canvas-header">
                        <span>SEASONAL COLOR SPECTRUM // {report.color.season.upper()} ({report.color.palette_title})</span>
                        <span>FACIAL SYMMETRY: {report.rating.symmetry_quotient}%</span>
                    </div>

                    {swatches_html}

                    <div class="overlay-container">
                        <div style="font-size: 0.65rem; color: var(--gold); margin-bottom: 4px; font-family: monospace;">MORPHOMETRIC WIREFRAME</div>
                        {report.face_shape.morphometric_overlay_svg}
                    </div>
                </div>

                <!-- 10% Narrative Rail -->
                <div class="narrative-rail">
                    <div>
                        <div class="section-tag">01 / Morphometric Profile</div>
                        <p>Classified as <strong>{report.face_shape.classification}</strong> (Secondary: {report.face_shape.secondary_profile}). Mandibular angle calculated at <strong>{report.face_shape.geometric_proportions.get('MandibularAngle', 105)}°</strong>.</p>
                        <p style="margin-top:6px; color:var(--muted);">{report.face_shape.framing_strategy}</p>
                    </div>

                    <div>
                        <div class="section-tag">02 / Eyewear Mandate</div>
                        <p>Frames: <strong>{report.eyewear.optimal_frame_geometries[0]}</strong></p>
                        <p style="color: var(--muted); font-size: 0.8rem;">Bridge: {report.eyewear.bridge_placement_rule} | Gauge: {report.eyewear.rim_gauge_weight}</p>
                    </div>

                    <div>
                        <div class="section-tag">03 / Hair Architecture</div>
                        <p>Top Cut: <strong>{report.hair.editorial_cuts[0]}</strong></p>
                        <p style="color: var(--muted); font-size: 0.8rem;">Parting: {report.hair.parting_vector} | Volume: {report.hair.volume_distribution_map}</p>
                    </div>

                    <div>
                        <div class="section-tag">04 / Discordant Chromas (Avoid)</div>
                        <div class="avoid-container">
                            {avoid_html}
                        </div>
                    </div>

                    <div>
                        <div class="section-tag">05 / Editorial Outfits</div>
                        <div class="outfit-grid">
                            {outfit_cards}
                        </div>
                    </div>

                    <div>
                        <div class="section-tag">06 / Acquisition Priorities</div>
                        <div style="margin-top:8px;">
                            {shopping_items}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
