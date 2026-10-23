"""
Canonical MediaPipe FaceMesh 468/478 Landmark Indices.
Standardized anatomical and photometric sampling landmarks.
"""

class FaceMeshLandmarks:
    """Canonical MediaPipe 468-point index mappings for facial morphometrics."""
    # Sagittal Midline Vertical Axis
    TRICHION = 10           # Forehead hairline top midpoint
    GLABELLA = 151          # Between eyebrows / forehead bottom
    SELLION = 168           # Nasal root / bridge midpoint
    NOSE_TIP = 1            # Pronasale (tip of nose)
    SUBNASALE = 2           # Base of columella / subnasal point
    LABRALE_SUPERIUS = 0    # Upper lip vermilion border top
    STOMION = 14            # Labial fissure / mouth center
    LABRALE_INFERIUS = 17   # Lower lip vermilion border bottom
    SUBLABIALE = 18         # Sulcus inferior between lip and chin
    MENTON = 152            # Chin bottom midpoint (gnathion / menton)

    # Lateral Facial Boundary (Bizygomatic - Cheekbone Width)
    ZYGOMATIC_LEFT = 454    # Left facial outer boundary / zygomatic prominence
    ZYGOMATIC_RIGHT = 234   # Right facial outer boundary / zygomatic prominence

    # Mandibular & Jaw Angles (Bigonial Width)
    GONION_LEFT = 365       # Left jaw angle
    GONION_RIGHT = 136      # Right jaw angle
    JAW_LINE_LEFT_MID = 397 # Mid-jaw point left
    JAW_LINE_RIGHT_MID = 172# Mid-jaw point right
    JAW_CHIN_LEFT = 378     # Lateral mental tuberosity left
    JAW_CHIN_RIGHT = 149    # Lateral mental tuberosity right

    # Frontotemporal Width (Forehead / Temple Width)
    TEMPLE_LEFT = 284       # Left temple boundary
    TEMPLE_RIGHT = 54       # Right temple boundary
    FOREHEAD_LEFT_CREST = 332
    FOREHEAD_RIGHT_CREST = 103

    # Ocular Anchors (Pupillary & Palpebral Fissures)
    LEFT_EYE_OUTER = 263
    LEFT_EYE_INNER = 362
    RIGHT_EYE_INNER = 133
    RIGHT_EYE_OUTER = 33
    LEFT_EYE_TOP = 386
    LEFT_EYE_BOTTOM = 374
    RIGHT_EYE_TOP = 159
    RIGHT_EYE_BOTTOM = 145

    # Iris Centers (when 478-landmark model is active)
    LEFT_IRIS_CENTER = 468
    RIGHT_IRIS_CENTER = 473

    # Cheeks / Photometric Sampling Polygons (Avoids vascular flush & rosacea)
    CHEEK_SAMPLE_RIGHT = [117, 118, 100, 126, 142]
    CHEEK_SAMPLE_LEFT = [346, 347, 329, 355, 371]
    FOREHEAD_SAMPLE = [67, 109, 10, 338, 297]
    CHIN_SAMPLE = [175, 199, 152, 428, 396]
