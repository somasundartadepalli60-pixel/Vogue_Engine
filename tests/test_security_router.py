"""
Integration and Security Unit Tests for Dual Dashboard Router.
Validates HMAC signature security, path isolation, token expiration,
and FastAPI endpoint execution.
"""
import pytest
import time
from starlette.testclient import TestClient

from vogue_engine.dashboards.crypto import StatelessTokenManager
from vogue_engine.dashboards.router import app
from vogue_engine.dashboards.user import REPORT_CACHE
from vogue_engine.core.vision.geometry import FaceShape, FacialGeometryMetrics
from vogue_engine.core.vision.photometrics import Season, Undertone, ContrastLevel, ColorimetricProfile
from vogue_engine.core.engine.combinatorial import StylePermutationDispatcher


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def crypto():
    return StatelessTokenManager(secret_key="TEST_SECURITY_SECRET_KEY", ttl_seconds=2)


@pytest.fixture
def seeded_report():
    uuid = "11111111-2222-3333-4444-555555555555"
    geom = FacialGeometryMetrics(
        length_to_width_ratio=1.45,
        jaw_to_zygomatic_ratio=0.76,
        forehead_to_zygomatic_ratio=0.82,
        jaw_to_forehead_ratio=0.92,
        bilateral_symmetry_score=95.0,
        mandibular_angle_degrees=105.0,
        primary_shape=FaceShape.OVAL,
        secondary_shape=FaceShape.ROUND,
        confidence=0.95,
    )
    photo = ColorimetricProfile(
        ita_angle=32.0,
        undertone=Undertone.WARM,
        contrast_level=ContrastLevel.MEDIUM,
        season=Season.AUTUMN,
        skin_lab_mean=(64.0, 12.0, 16.0),
        iris_luminance=26.0,
        hair_luminance=16.0,
        confidence=0.95,
    )
    report = StylePermutationDispatcher.compile_report(
        report_uuid=uuid,
        geom=geom,
        photo=photo,
        svg_overlay="<svg id='test'></svg>"
    )
    REPORT_CACHE[uuid] = report
    return report


class TestSecurityAndRouting:

    def test_token_lifecycle(self, crypto):
        uuid_val = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        token = crypto.generate_admin_token(uuid_val, permissions=["review", "override"])

        # 1. Valid verification
        payload = crypto.verify_admin_token(uuid_val, token)
        assert payload is not None
        assert payload["sub"] == uuid_val
        assert payload["role"] == "admin"
        assert "override" in payload["perms"]

        # 2. Tampering payload rejection
        parts = token.split(".")
        tampered_token = f"{parts[0]}TAMPERED.{parts[1]}"
        assert crypto.verify_admin_token(uuid_val, tampered_token) is None

        # 3. Path mismatch rejection (token created for uuid A, queried against uuid B)
        alien_uuid = "ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj"
        assert crypto.verify_admin_token(alien_uuid, token) is None

        # 4. Expiration rejection
        time.sleep(2.1)
        assert crypto.verify_admin_token(uuid_val, token) is None

    def test_health_endpoint(self, test_client):
        resp = test_client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "HEALTHY"
        assert data["domains_supported"] == 13

    def test_user_dashboard_html_and_json(self, test_client, seeded_report):
        uuid = seeded_report.report_uuid

        # HTML View
        html_resp = test_client.get(f"/dashboard/report/{uuid}")
        assert html_resp.status_code == 200
        assert "text/html" in html_resp.headers["content-type"]
        assert "VogueEngine" in html_resp.text
        assert "01 / Morphometric Profile" in html_resp.text

        # JSON View
        json_resp = test_client.get(f"/dashboard/report/{uuid}?format=json")
        assert json_resp.status_code == 200
        data = json_resp.json()
        assert data["report_uuid"] == uuid
        assert data["face_shape"]["classification"] == "Oval"
        assert len(data["color"]["primary_swatches"]) >= 3

    def test_user_dashboard_not_found(self, test_client):
        resp = test_client.get("/dashboard/report/00000000-0000-0000-0000-000000000000")
        assert resp.status_code == 404

    def test_admin_review_unauthorized_cases(self, test_client, seeded_report):
        uuid = seeded_report.report_uuid

        # No token
        resp_no_token = test_client.get(f"/admin/review/{uuid}")
        assert resp_no_token.status_code in [401, 422]

        # Invalid token
        resp_bad_token = test_client.get(f"/admin/review/{uuid}?token=invalid.signature")
        assert resp_bad_token.status_code == 401

    def test_admin_review_and_override_success(self, test_client, seeded_report):
        from vogue_engine.dashboards.admin import crypto_manager
        uuid = seeded_report.report_uuid
        token = crypto_manager.generate_admin_token(uuid, permissions=["review", "override"])

        # Review Inspection
        review_resp = test_client.get(f"/admin/review/{uuid}?token={token}")
        assert review_resp.status_code == 200
        assert review_resp.json()["status"] == "AUTHORIZATION_GRANTED"

        # Apply Override (Change FaceShape from Oval to Square, and Season to Winter)
        override_payload = {
            "override_face_shape": "Square",
            "override_season": "Winter",
            "curator_notes": "Audited in salon by Lead Stylist - strong bigonial definition."
        }
        post_resp = test_client.post(
            f"/admin/override/{uuid}?token={token}",
            json=override_payload
        )
        assert post_resp.status_code == 200
        data = post_resp.json()
        assert data["status"] == "MUTATION_SUCCESSFUL"
        assert data["updated_domains"]["face_shape"] == "Square"
        assert data["updated_domains"]["season"] == "Winter"

        # Verify mutation reflected in user dashboard immediately
        user_check = test_client.get(f"/dashboard/report/{uuid}?format=json")
        assert user_check.json()["face_shape"]["classification"] == "Square"
        assert user_check.json()["color"]["season"] == "Winter"
