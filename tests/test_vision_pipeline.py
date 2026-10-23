"""
Comprehensive Integration Tests for Vision Analysis Pipeline and Endpoint.
Tests end-to-end image ingestion, format normalization, SVG overlays,
and the `/api/v1/analyze` upload endpoint.
"""
import io
import pytest
import numpy as np
import cv2
from PIL import Image
from starlette.testclient import TestClient

from vogue_engine.core.vision.pipeline import VisionAnalysisPipeline, VisionAnalysisResult
from vogue_engine.core.vision.morphometrics import MorphometricVisualizer
from vogue_engine.core.vision.geometry import FaceShape
from vogue_engine.dashboards.router import app
from vogue_engine.dashboards.user import REPORT_CACHE


class TestVisionPipeline:

    @pytest.fixture
    def test_client(self):
        return TestClient(app)

    @pytest.fixture
    def sample_image_bytes(self, synthetic_face_image):
        success, encoded = cv2.imencode(".png", synthetic_face_image)
        assert success
        return encoded.tobytes()

    def test_svg_overlay_generation(self, synthetic_canonical_mesh):
        """Validates luxury wireframe SVG overlay construction."""
        svg = MorphometricVisualizer.generate_svg_overlay(
            synthetic_canonical_mesh, FaceShape.OVAL
        )
        assert svg.startswith("<svg")
        assert svg.endswith("</svg>")
        assert "vogue-morphometric-overlay" in svg
        assert "OVAL PROFILE" in svg
        assert "stroke='#D4AF37'" in svg

    def test_normalize_image_inputs(self, synthetic_face_image, sample_image_bytes):
        """Tests image normalization across heterogeneous formats."""
        pipeline = VisionAnalysisPipeline()

        # 1. BGR numpy array
        res_bgr = pipeline._normalize_image_input(synthetic_face_image)
        assert res_bgr.shape == synthetic_face_image.shape

        # 2. Grayscale numpy array
        gray = cv2.cvtColor(synthetic_face_image, cv2.COLOR_BGR2GRAY)
        res_gray = pipeline._normalize_image_input(gray)
        assert res_gray.ndim == 3 and res_gray.shape[2] == 3

        # 3. BGRA (4-channel) numpy array
        bgra = cv2.cvtColor(synthetic_face_image, cv2.COLOR_BGR2BGRA)
        res_bgra = pipeline._normalize_image_input(bgra)
        assert res_bgra.shape[2] == 3

        # 4. PIL Image
        pil_img = Image.fromarray(cv2.cvtColor(synthetic_face_image, cv2.COLOR_BGR2RGB))
        res_pil = pipeline._normalize_image_input(pil_img)
        assert res_pil.ndim == 3 and res_pil.shape[2] == 3

        # 5. Byte buffer
        res_bytes = pipeline._normalize_image_input(sample_image_bytes)
        assert res_bytes.shape == synthetic_face_image.shape

        # 6. Invalid input types
        with pytest.raises(TypeError):
            pipeline._normalize_image_input(12345)

        with pytest.raises(FileNotFoundError):
            pipeline._normalize_image_input("non_existent_file_path_123456.png")

        with pytest.raises(ValueError):
            pipeline._normalize_image_input(b"corrupt_invalid_image_bytes")

    def test_process_image_end_to_end(self, synthetic_face_image):
        """Verifies full execution of vision pipeline from image to feature extraction."""
        pipeline = VisionAnalysisPipeline()
        result = pipeline.process_image(synthetic_face_image)

        assert isinstance(result, VisionAnalysisResult)
        assert result.geometry is not None
        assert result.photometrics is not None
        assert isinstance(result.svg_overlay, str)
        assert len(result.svg_overlay) > 50
        assert result.landmarks.shape == (468, 3)

    def test_analyze_endpoint_success(self, test_client, sample_image_bytes):
        """Tests POST /api/v1/analyze with image file upload and admin token generation."""
        files = {
            "file": ("portrait.png", io.BytesIO(sample_image_bytes), "image/png")
        }
        resp = test_client.post("/api/v1/analyze", files=files)
        assert resp.status_code == 200

        data = resp.json()
        assert "report_uuid" in data
        assert "user_dashboard_url" in data
        assert "admin_override_url" in data
        assert "admin_token" in data
        assert "classification" in data

        report_uuid = data["report_uuid"]
        assert report_uuid in REPORT_CACHE

        # Retrieve user report directly
        report_resp = test_client.get(f"/dashboard/report/{report_uuid}?format=json")
        assert report_resp.status_code == 200
        report_data = report_resp.json()
        assert report_data["report_uuid"] == report_uuid
        assert "color" in report_data
        assert "face_shape" in report_data

    def test_analyze_endpoint_empty_file(self, test_client):
        """Tests POST /api/v1/analyze rejection of empty file upload."""
        files = {
            "file": ("empty.png", io.BytesIO(b""), "image/png")
        }
        resp = test_client.post("/api/v1/analyze", files=files)
        assert resp.status_code == 400
