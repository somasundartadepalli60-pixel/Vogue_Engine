"""
Colorimetric, CIELAB, sRGB, and Photometric conversion constants.
"""

class ColorSpaceConstants:
    """Standardized constants for dermatological photometrics and color science."""
    # Standard Observer Illuminant D65 (Daylight) Reference Tristimulus Values
    REF_X_D65 = 95.047
    REF_Y_D65 = 100.000
    REF_Z_D65 = 108.883

    # Individual Typology Angle (ITA) Classification Thresholds
    # ITA° = [ArcTan((L* - 50) / b*)] * (180 / π)
    ITA_VERY_LIGHT_THRESHOLD = 55.0
    ITA_LIGHT_THRESHOLD = 41.0
    ITA_INTERMEDIATE_THRESHOLD = 28.0
    ITA_TAN_THRESHOLD = 10.0
    ITA_DARK_THRESHOLD = -30.0

    # Undertone b*/a* ratio thresholds
    UNDERTONE_WARM_RATIO_MIN = 1.25
    UNDERTONE_COOL_RATIO_MAX = 0.75

    # Contrast Level RMS Thresholds
    CONTRAST_HIGH_MIN = 45.0
    CONTRAST_MEDIUM_MIN = 28.0
