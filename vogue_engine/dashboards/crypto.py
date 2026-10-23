"""
Cryptographic Stateless Token Manager.
Uses HMAC-SHA256 for zero-database verification of administrative privileges.
Ensures runtime state isolation and URL path parameter integrity.
"""
import hmac
import hashlib
import json
import base64
import time
from typing import Optional, Dict, Any, List

from vogue_engine.configs.security_config import SecurityTokens


class StatelessTokenManager:
    """
    Zero-database cryptographic token signer and validator using HMAC-SHA256.
    Ensures path-level runtime isolation between public reports and admin mutations.
    """

    def __init__(
        self,
        secret_key: Optional[str] = None,
        ttl_seconds: Optional[int] = None,
    ):
        key = secret_key or SecurityTokens.DEFAULT_SECRET_KEY
        self._secret = key.encode("utf-8")
        self._ttl = ttl_seconds if ttl_seconds is not None else SecurityTokens.DEFAULT_TOKEN_TTL_SECONDS

    def generate_admin_token(
        self,
        report_uuid: str,
        permissions: Optional[List[str]] = None,
    ) -> str:
        """
        Encodes claims and signs a stateless token for `/admin/review/{uuid}?token={token}`.
        """
        now = int(time.time())
        payload = {
            "sub": report_uuid,
            "role": "admin",
            "perms": permissions or ["review", "override"],
            "iat": now,
            "exp": now + self._ttl,
        }
        raw_bytes = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        encoded_payload = base64.urlsafe_b64encode(raw_bytes).decode("utf-8").rstrip("=")

        signature = hmac.new(
            self._secret,
            encoded_payload.encode("utf-8"),
            hashlib.sha256
        ).digest()
        encoded_sig = base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")

        return f"{encoded_payload}.{encoded_sig}"

    def verify_admin_token(self, report_uuid: str, token: str) -> Optional[Dict[str, Any]]:
        """
        Validates token authenticity, signature integrity, and target subject binding.
        Returns payload dict if valid, or None if invalid/expired/tampered.
        """
        if not token or "." not in token:
            return None

        try:
            parts = token.split(".")
            if len(parts) != 2:
                return None

            payload_b64, sig_b64 = parts[0], parts[1]

            # Recompute expected signature
            expected_sig = hmac.new(
                self._secret,
                payload_b64.encode("utf-8"),
                hashlib.sha256
            ).digest()
            expected_sig_b64 = base64.urlsafe_b64encode(expected_sig).decode("utf-8").rstrip("=")

            if not hmac.compare_digest(sig_b64, expected_sig_b64):
                return None  # Signature tampering detected

            # Decode JSON payload
            padding = "=" * (-len(payload_b64) % 4)
            payload_bytes = base64.urlsafe_b64decode(payload_b64 + padding)
            payload = json.loads(payload_bytes.decode("utf-8"))

            now = time.time()
            # Check expiration immediately (RFC 7519: current time must be strictly before exp)
            if payload.get("exp", 0) <= now:
                return None

            # Check issued-at is not in the future
            if payload.get("iat", 0) - SecurityTokens.MAX_CLOCK_SKEW_SECONDS > now:
                return None

            # Validate subject binding (token must match target path UUID)
            if payload.get("sub") != report_uuid:
                return None

            # Validate role
            if payload.get("role") != "admin":
                return None

            return payload
        except Exception:
            return None
