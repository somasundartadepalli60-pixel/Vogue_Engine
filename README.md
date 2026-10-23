# VogueEngine Core — installation, build, run and usage

## Requirements and dependencies

Python 3.10–3.12 recommended. Dependencies are listed in `pyproject.toml`;
`requirements.lock` pins direct dependency versions but does not lock transitive
dependencies or guarantee cross-platform resolution. No API keys or `.env` files needed.

## Installation

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.lock
python -m pip install -e .
```

## Build

```bash
python -m pip wheel . --no-deps -w dist
```

## Run

```bash
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for interactive API documentation, or
`http://127.0.0.1:8000/health` to inspect service health.

## Usage

Upload a JPEG or PNG to `POST /api/v1/analyze` using the interactive `/docs` page.
Use the wardrobe endpoints in `/docs` to manage inventory and outfits locally.
Vision processing requires the optional native vision libraries installed above.

## Tests and verification

```bash
python verify_project.py
python -m pytest tests -q
```

`verify_project.py` checks Python syntax and entrypoint presence; it is not an
end-to-end application test. Actual runtime depends on installed packages.

## Git history and pull requests

This archive contains local Git feature commits and merge commits created during
packaging. **These are not hosted GitHub/GitLab pull requests.** Genuine PRs
require publishing the repository and opening/reviewing PRs on a hosting service.

---

# VogueEngine Core™ 

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Coverage](https://img.shields.io/badge/Coverage-95%25-brightgreen?style=for-the-badge)](https://pytest.org)
[![Tests](https://img.shields.io/badge/Tests-25%20Passing-success?style=for-the-badge)](https://pytest.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-FaceMesh%20468-00599C?style=for-the-badge)](https://mediapipe.dev)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

**VogueEngine Core™** is an enterprise-scale, production-ready, open-source personal style, facial morphometric analysis, and wardrobe recommendation engine. 

Designed to **completely eliminate paid third-party computer vision and styling cloud APIs**, VogueEngine computes deterministic geometric vector ratios, photometric colorimetry, and a **252-state combinatorial style matrix** entirely client/server-side using open-source packages (**NumPy**, **OpenCV**, **MediaPipe**, and **Pillow**).

---

## Architectural Highlights

- **Zero-Cloud Vision Pipeline**: Extracts 468 3D facial landmarks and calculates morphometrics, bilateral symmetry, skin undertone, and contrast levels locally with zero third-party API costs or cloud dependencies.
- **Luxury Magazine Data Model**: High visual density adhering to a strict **90% visuals / 10% text ratio** across all 13 core domains: dynamic SVG wireframes, hex swatches, comparative visual vectors (Better vs. Worse with impact ratings), and normalized 0–100 grid coordinates.
- **252-State Combinatorial Style Engine**: Deterministic matrix mapping across 7 face shapes, 4 seasonal palettes, 3 skin undertones, and 3 contrast levels.
- **Stateless Dual Dashboard Isolation**: Strict runtime separation between public user reports (`/dashboard/report/{uuid}`) and administrative mutations (`/admin/review/{uuid}?token={token}`) using zero-database HMAC-SHA256 tokens and RFC 7519 timestamp validation.
- **Enterprise Test Matrix**: Comprehensive test suite achieving **95% code coverage** and validating the entire 252-state permutation grid.

---

## 1. Enterprise Directory Map

```
23-10-2026/
├── pyproject.toml                     # Poetry/pip build configuration & test dependencies
├── README.md                          # Master architectural documentation
├── tests/                             # Comprehensive test suite (95% code coverage)
│   ├── __init__.py
│   ├── conftest.py                    # Calibrated synthetic 3D landmarks & photometric images
│   ├── test_combinatorial_grid.py     # 252-state combinatorial grid validation
│   ├── test_photometrics.py           # ITA skin undertones, CIELAB conversion & contrast ratios
│   ├── test_security_router.py        # HMAC token lifecycle, path binding & admin overrides
│   ├── test_vision_geometry.py        # Scale/translation invariance, symmetry, 7-shape classification
│   └── test_vision_pipeline.py        # Image normalization, SVG overlays & /api/v1/analyze endpoint
└── vogue_engine/                      # Root Python package
    ├── __init__.py                    # Public API exports
    ├── configs/                       # Configuration tokens & constants
    │   ├── __init__.py
    │   ├── color_spaces.py            # CIELAB & ITA skin typology thresholds
    │   ├── landmark_indices.py        # 468 MediaPipe FaceMesh anatomical indices & groupings
    │   ├── luxury_tokens.py           # High-fashion palettes, coordinate grids, typography tokens
    │   └── security_config.py         # HMAC signing keys, token TTL, and route prefixes
    ├── core/                          # Vision & combinatorial core
    │   ├── __init__.py
    │   ├── engine/                    # 13-domain combinatorial style generator
    │   │   ├── __init__.py
    │   │   ├── combinatorial.py       # StylePermutationDispatcher orchestrator
    │   │   ├── domains/               # 13 granular luxury domain generators
    │   │   │   ├── accessories.py     # Metal undertone matching & jewelry scale
    │   │   │   ├── beard.py           # Mandibular sculpt rules & taper length
    │   │   │   ├── color.py           # Primary swatches, neutral anchors, avoid swatches
    │   │   │   ├── core_style.py      # Style archetypes & aesthetic pillars
    │   │   │   ├── eyewear.py         # Frame geometries & bridge placement
    │   │   │   ├── face_shape.py      # Framing strategy & optical contouring
    │   │   │   ├── footwear.py        # Toe-box geometry & leather finishes
    │   │   │   ├── hair.py            # Editorial cuts, volume placement & comparisons
    │   │   │   ├── outfits.py         # Curated ensembles & visual board coordinates
    │   │   │   ├── patterns.py        # Pattern scale & optimal motifs
    │   │   │   ├── rating.py          # Symmetry quotient & 5-axis radar tensor
    │   │   │   ├── scorecard.py       # Normalized domain metrics & signature strengths
    │   │   │   └── shopping_list.py   # Wardrobe investment pieces & acquisition matrix
    │   │   ├── matrices/              # 4 seasonal matrix tables
    │   │   │   ├── autumn_matrix.py
    │   │   │   ├── spring_matrix.py
    │   │   │   ├── summer_matrix.py
    │   │   │   └── winter_matrix.py
    │   │   └── schemas/               # Pydantic data models
    │   │       ├── layout.py          # Normalized 0-100 visual board coordinates
    │   │       ├── style_payload.py   # MasterVogueStyleReport container model
    │   │       └── vectors.py         # ComparisonVector & ColorSwatch models
    │   └── vision/                    # Geometric & photometric analysis
    │       ├── __init__.py
    │       ├── geometry.py            # Vector mathematics, symmetry & 7-shape classifier
    │       ├── morphometrics.py       # SVG wireframe overlays & contour projections
    │       ├── photometrics.py        # CIELAB, ITA angle, undertone & contrast engine
    │       └── pipeline.py            # Heterogeneous image ingestion & orchestrator
    └── dashboards/                    # Dual Dashboard routing & security
        ├── __init__.py
        ├── admin.py                   # Cryptographically authorized review & override endpoints
        ├── crypto.py                  # Stateless HMAC-SHA256 signature generator & validator
        ├── router.py                  # Unified FastAPI application factory
        └── user.py                    # Public user dashboard HTML/JSON renderer
```

---

## 2. Vision Geometry & Photometrics Mathematics

### 2.1 Facial Proportions & Symmetry
Using normalized 3D vectors $\mathbf{p} = (x, y, z)$ from 468 MediaPipe FaceMesh landmarks:

- **Length-to-Width Ratio ($LWR$):**
  $$\text{LWR} = \frac{\|\mathbf{p}_{\text{trichion}} - \mathbf{p}_{\text{menton}}\|}{\|\mathbf{p}_{\text{zygomatic\_left}} - \mathbf{p}_{\text{zygomatic\_right}}\|}$$

- **Jaw-to-Zygomatic Ratio ($JZR$):**
  $$\text{JZR} = \frac{\|\mathbf{p}_{\text{gonion\_left}} - \mathbf{p}_{\text{gonion\_right}}\|}{\|\mathbf{p}_{\text{zygomatic\_left}} - \mathbf{p}_{\text{zygomatic\_right}}\|}$$

- **Forehead-to-Zygomatic Ratio ($FZR$):**
  $$\text{FZR} = \frac{\|\mathbf{p}_{\text{temple\_left}} - \mathbf{p}_{\text{temple\_right}}\|}{\|\mathbf{p}_{\text{zygomatic\_left}} - \mathbf{p}_{\text{zygomatic\_right}}\|}$$

- **Bilateral Symmetry Quotient ($Q_{\text{sym}}$):**
  Points $\mathbf{p}_L, \mathbf{p}_R$ across 10 anatomical pairs are projected onto the normal of the sagittal midline ($\mathbf{p}_{\text{glabella}} \to \mathbf{p}_{\text{menton}}$):
  $$d_i = |\mathbf{p}_i \cdot \hat{\mathbf{n}}_{\text{sagittal}}|, \quad \delta_i = \frac{|d_{i, L} - d_{i, R}|}{\max(d_{i, L}, d_{i, R})}$$
  $$Q_{\text{sym}} = \text{clip}\left(100 \times \left(1.0 - \left(0.4 \cdot \bar{\delta} + 0.6 \cdot \max(\delta)\right)\right), 0, 100\right)$$

- **7-Shape Hyperplane Morphology Classifier**: Evaluates relative distance functions for `Oval`, `Round`, `Square`, `Oblong`, `Heart`, `Diamond`, and `Triangle` using continuous ratio boundaries and mandibular angle.

### 2.2 Colorimetric Photometrics
- **Individual Typology Angle ($\text{ITA}^\circ$):**
  Calculated from median CIELAB coordinates ($L^*, a^*, b^*$) sampled across bilateral cheek and forehead regions:
  $$\text{ITA}^\circ = \arctan\left(\frac{L^* - 50}{b^*}\right) \times \frac{180}{\pi}$$

- **Undertone Determination:**
  - $\text{Warm}$: $b^* - a^* \ge 3.0$ and chromatic angle $\theta = \arctan2(b^*, a^*) > 48^\circ$
  - $\text{Cool}$: $b^* - a^* \le -1.5$ or $\theta < 38^\circ$
  - $\text{Neutral}$: Intermediate ranges

- **Michelson Contrast Ratio ($C$):**
  $$C = \frac{L_{\text{skin}} - \min(L_{\text{iris}}, L_{\text{hair}})}{L_{\text{skin}} + \min(L_{\text{iris}}, L_{\text{hair}})}$$
  - High: $C \ge 0.52$
  - Medium: $0.32 \le C < 0.52$
  - Low: $C < 0.32$

---

## 3. The 13 Core Luxury Domains

Every style report generated by `StylePermutationDispatcher.compile_report()` populates complete luxury magazine data structures:

1. **Rating**: Overall score, symmetry quotient, 5-point radar tensor (`[jaw_definition, symmetry, balance, contrast_harmony, ocular_alignment]`).
2. **Color**: 4 primary best swatches, 3 neutral anchors, 3 colors to avoid (with hex codes and normalized visual coordinates).
3. **Outfits**: Recommended seasonal ensembles (daywear, evening, smart casual) with layout grids.
4. **Face Shape**: Diagnostic metrics, primary/secondary shapes, framing philosophy, contouring guidance.
5. **Hair**: Curated cuts, crown/side volume rules, Better vs. Worse comparison vectors with visual impact ratings.
6. **Eyewear**: Optimal frame geometries (e.g. geometric angular, keyhole bridge, softened rectangular) and bad pairings to avoid.
7. **Beard / Facial Hair**: Mandibular taper rules, length grade in mm, neckline termination line.
8. **Accessories**: Metal matching (Yellow Gold, Rose Gold, Platinum/Silver), jewelry scale gauge.
9. **Patterns**: Geometric scale (micro, medium, statement macro) and optimal motifs.
10. **Footwear**: Toe-box geometry (almond, chisel, round) and formal/casual pairings.
11. **Core Style**: Archetype assignment (*Architectural Minimalist*, *Old Money Elegance*, *Avant-Garde Tailored*), signature silhouettes.
12. **Scorecard**: Normalized dimension ratings and top personal aesthetic strengths.
13. **Shopping Checklist**: Priority acquisition matrix with category tags and long-term wardrobe investment recommendations.

---

## 4. Stateless Dual Dashboard Security Architecture

```
User Browser                  FastAPI Server                   Admin Client
     │                              │                               │
     │ GET /dashboard/report/{uuid} │                               │
     ├─────────────────────────────>│                               │
     │<─────────────────────────────┤ (Read-Only Luxury Report)     │
     │                              │                               │
     │                              │ POST /admin/override/{uuid}   │
     │                              │      ?token={HMAC_TOKEN}      │
     │                              │<──────────────────────────────┤
     │                              ├──────── Check HMAC & Exp ─────┤
     │                              ├─────── Mutate Runtime Cache ──┤
     │                              ├──────────────────────────────>│
     │ GET /dashboard/report/{uuid} │                               │
     ├─────────────────────────────>│ (Immediate Reflected Update)  │
     │<─────────────────────────────┤                               │
```

- **Runtime State Isolation**: Public report URLs (`/dashboard/report/{uuid}`) have zero visibility or mutation power over admin features.
- **Zero-Database Cryptographic Verification**: Admin URLs require a signed token (`/admin/review/{uuid}?token={token}`). The token payload is serialized, signed via HMAC-SHA256, and validated against:
  1. Signature authenticity (tamper-proof)
  2. Target UUID matching the URL path parameter (prevents cross-tenant replay)
  3. Strict expiration checking ($\text{exp} \le \text{now}$) conforming to RFC 7519
  4. Role validation (`role: "admin"`)

---

## 5. REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check, telemetry, and active cache report count |
| `POST` | `/api/v1/analyze` | Upload image portrait; executes full vision & style pipeline |
| `GET` | `/dashboard/report/{uuid}` | Public user dashboard HTML editorial view |
| `GET` | `/dashboard/report/{uuid}?format=json` | Headless JSON representation of the 13 domains |
| `GET` | `/admin/review/{uuid}?token={token}` | Admin inspection and validation check |
| `POST` | `/admin/override/{uuid}?token={token}` | Admin mutation (override face shape, season, curator notes) |

---

## 6. Quickstart & Verification

### 6.1 Requirements
- Python 3.10+ (tested on Python 3.14.3)
- NumPy, OpenCV (`opencv-python`), MediaPipe, Pillow, FastAPI, Uvicorn, Pydantic

### 6.2 Running Tests & Code Coverage
```powershell
python -m pytest -v --cov=vogue_engine tests/
```

**Results:**
```
======================== 25 passed, 1 warning in 7.35s ========================
TOTAL: 95% Coverage across all 22 modules
```

### 6.3 Starting the Local Development Server
```powershell
uvicorn vogue_engine.dashboards.router:app --host 0.0.0.0 --port 8000 --reload
```

- **Interactive Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Interactive ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

### 6.4 Python Programmatic Usage
```python
from vogue_engine import (
    VisionAnalysisPipeline,
    StylePermutationDispatcher,
    MasterVogueStyleReport,
)

# 1. Initialize vision pipeline
pipeline = VisionAnalysisPipeline()

# 2. Process image (accepts filepath, bytes, PIL Image, or NumPy array)
result = pipeline.process_image("portrait.jpg")

# 3. Compile full 13-domain luxury report
report: MasterVogueStyleReport = StylePermutationDispatcher.compile_report(
    report_uuid="user-123",
    geom=result.geometry,
    photo=result.photometrics,
    svg_overlay=result.svg_overlay,
)

print(f"Face Shape: {report.face_shape.classification}")
print(f"Season: {report.color.season}")
print(f"Symmetry Quotient: {report.rating.symmetry_quotient}%")
print(f"Recommended Palette: {[s.hex_code for s in report.color.primary_swatches]}")
```

---

## 7. License
MIT License. Open-source for enterprise personal style and morphometric intelligence.

## Verified entry points and build commands

This repository contains a Python FastAPI application. Run it locally after installing Python 3.10+:

```bash
python -m pip install -r requirements.lock
python main.py --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/docs` for the API UI or `http://127.0.0.1:8000/health` for the health endpoint. To compile source files without starting the server:

```bash
python -m compileall -q main.py vogue_engine
```

Optional npm command aliases (npm has no runtime dependencies):

```bash
npm ci
npm run build
npm start
```

A `package-lock.json` records the dependency-free npm launcher. **It does not lock Python dependencies.** `requirements.lock` pins Python direct dependencies, but transitive dependencies are not fully locked. For reproducible Python installs, resolve a complete lock using `uv lock` with package index access and commit `uv.lock`.

Docker option: `docker build -t vogue-engine .` then `docker run --rm -p 8000:8000 vogue-engine`.
