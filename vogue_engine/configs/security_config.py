"""
Cryptographic Security Configuration.
Defines parameters for zero-database HMAC-SHA256 signature verification,
token expiration, and path isolation.
"""
import os

class SecurityTokens:
    # Ephemeral key: no embedded shared secret and no API key or .env required.
    # Admin links issued before a server restart become invalid.
    DEFAULT_SECRET_KEY = os.urandom(32).hex()
    DEFAULT_TOKEN_TTL_SECONDS = int(os.environ.get("VOGUE_TOKEN_TTL", "86400")) # 24 Hours
    HASH_ALGORITHM = "sha256"
    MAX_CLOCK_SKEW_SECONDS = 60
    
    # Path separation
    USER_DASHBOARD_PREFIX = "/dashboard/report/"
    ADMIN_OVERRIDE_PREFIX = "/admin/review/"
