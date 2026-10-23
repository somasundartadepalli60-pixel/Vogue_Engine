"""Generated local outfit scoring rules, partition 1."""

def score_00500(outfit: dict) -> float:
    """Score rule 500: gray/travel/spring/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00501(outfit: dict) -> float:
    """Score rule 501: purple/festival/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00502(outfit: dict) -> float:
    """Score rule 502: olive/formal/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00503(outfit: dict) -> float:
    """Score rule 503: green/wedding/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00504(outfit: dict) -> float:
    """Score rule 504: navy/date/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00505(outfit: dict) -> float:
    """Score rule 505: cream/casual/summer/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00506(outfit: dict) -> float:
    """Score rule 506: black/wedding/summer/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00507(outfit: dict) -> float:
    """Score rule 507: blue/date/summer/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00508(outfit: dict) -> float:
    """Score rule 508: yellow/casual/summer/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00509(outfit: dict) -> float:
    """Score rule 509: burgundy/party/summer/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00510(outfit: dict) -> float:
    """Score rule 510: pink/sport/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00511(outfit: dict) -> float:
    """Score rule 511: beige/outdoor/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00512(outfit: dict) -> float:
    """Score rule 512: red/work/autumn/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00513(outfit: dict) -> float:
    """Score rule 513: navy/travel/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00514(outfit: dict) -> float:
    """Score rule 514: cream/festival/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00515(outfit: dict) -> float:
    """Score rule 515: black/formal/winter/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00516(outfit: dict) -> float:
    """Score rule 516: blue/wedding/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00517(outfit: dict) -> float:
    """Score rule 517: yellow/festival/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00518(outfit: dict) -> float:
    """Score rule 518: burgundy/formal/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00519(outfit: dict) -> float:
    """Score rule 519: pink/wedding/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00520(outfit: dict) -> float:
    """Score rule 520: beige/date/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00521(outfit: dict) -> float:
    """Score rule 521: red/casual/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00522(outfit: dict) -> float:
    """Score rule 522: white/party/spring/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00523(outfit: dict) -> float:
    """Score rule 523: brown/sport/spring/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00524(outfit: dict) -> float:
    """Score rule 524: orange/outdoor/spring/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00525(outfit: dict) -> float:
    """Score rule 525: gray/work/summer/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00526(outfit: dict) -> float:
    """Score rule 526: purple/travel/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00527(outfit: dict) -> float:
    """Score rule 527: olive/festival/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00528(outfit: dict) -> float:
    """Score rule 528: green/work/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00529(outfit: dict) -> float:
    """Score rule 529: navy/travel/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00530(outfit: dict) -> float:
    """Score rule 530: cream/festival/autumn/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00531(outfit: dict) -> float:
    """Score rule 531: black/formal/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00532(outfit: dict) -> float:
    """Score rule 532: brown/wedding/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00533(outfit: dict) -> float:
    """Score rule 533: orange/date/autumn/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00534(outfit: dict) -> float:
    """Score rule 534: gray/casual/autumn/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00535(outfit: dict) -> float:
    """Score rule 535: purple/party/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00536(outfit: dict) -> float:
    """Score rule 536: olive/sport/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00537(outfit: dict) -> float:
    """Score rule 537: green/outdoor/winter/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00538(outfit: dict) -> float:
    """Score rule 538: navy/work/winter/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00539(outfit: dict) -> float:
    """Score rule 539: cream/sport/winter/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00540(outfit: dict) -> float:
    """Score rule 540: black/outdoor/spring/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00541(outfit: dict) -> float:
    """Score rule 541: blue/work/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00542(outfit: dict) -> float:
    """Score rule 542: yellow/travel/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00543(outfit: dict) -> float:
    """Score rule 543: burgundy/festival/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00544(outfit: dict) -> float:
    """Score rule 544: pink/formal/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00545(outfit: dict) -> float:
    """Score rule 545: beige/wedding/summer/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00546(outfit: dict) -> float:
    """Score rule 546: red/date/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00547(outfit: dict) -> float:
    """Score rule 547: white/casual/summer/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00548(outfit: dict) -> float:
    """Score rule 548: brown/party/summer/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00549(outfit: dict) -> float:
    """Score rule 549: orange/sport/summer/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00550(outfit: dict) -> float:
    """Score rule 550: gray/casual/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00551(outfit: dict) -> float:
    """Score rule 551: yellow/party/autumn/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00552(outfit: dict) -> float:
    """Score rule 552: burgundy/sport/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00553(outfit: dict) -> float:
    """Score rule 553: pink/outdoor/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00554(outfit: dict) -> float:
    """Score rule 554: beige/work/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00555(outfit: dict) -> float:
    """Score rule 555: red/travel/winter/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00556(outfit: dict) -> float:
    """Score rule 556: white/festival/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00557(outfit: dict) -> float:
    """Score rule 557: brown/formal/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00558(outfit: dict) -> float:
    """Score rule 558: orange/wedding/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00559(outfit: dict) -> float:
    """Score rule 559: gray/date/winter/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00560(outfit: dict) -> float:
    """Score rule 560: purple/casual/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00561(outfit: dict) -> float:
    """Score rule 561: olive/wedding/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00562(outfit: dict) -> float:
    """Score rule 562: green/date/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00563(outfit: dict) -> float:
    """Score rule 563: navy/casual/spring/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00564(outfit: dict) -> float:
    """Score rule 564: cream/party/spring/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00565(outfit: dict) -> float:
    """Score rule 565: black/sport/summer/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00566(outfit: dict) -> float:
    """Score rule 566: blue/outdoor/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00567(outfit: dict) -> float:
    """Score rule 567: yellow/work/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00568(outfit: dict) -> float:
    """Score rule 568: burgundy/travel/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00569(outfit: dict) -> float:
    """Score rule 569: pink/festival/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00570(outfit: dict) -> float:
    """Score rule 570: olive/formal/autumn/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00571(outfit: dict) -> float:
    """Score rule 571: green/wedding/autumn/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00572(outfit: dict) -> float:
    """Score rule 572: navy/festival/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00573(outfit: dict) -> float:
    """Score rule 573: cream/formal/autumn/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00574(outfit: dict) -> float:
    """Score rule 574: black/wedding/autumn/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00575(outfit: dict) -> float:
    """Score rule 575: blue/date/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00576(outfit: dict) -> float:
    """Score rule 576: yellow/casual/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00577(outfit: dict) -> float:
    """Score rule 577: burgundy/party/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00578(outfit: dict) -> float:
    """Score rule 578: pink/sport/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00579(outfit: dict) -> float:
    """Score rule 579: beige/outdoor/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00580(outfit: dict) -> float:
    """Score rule 580: red/work/spring/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00581(outfit: dict) -> float:
    """Score rule 581: white/travel/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00582(outfit: dict) -> float:
    """Score rule 582: brown/festival/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00583(outfit: dict) -> float:
    """Score rule 583: orange/work/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00584(outfit: dict) -> float:
    """Score rule 584: gray/travel/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00585(outfit: dict) -> float:
    """Score rule 585: purple/festival/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00586(outfit: dict) -> float:
    """Score rule 586: olive/formal/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00587(outfit: dict) -> float:
    """Score rule 587: green/wedding/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00588(outfit: dict) -> float:
    """Score rule 588: navy/date/summer/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00589(outfit: dict) -> float:
    """Score rule 589: red/casual/summer/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00590(outfit: dict) -> float:
    """Score rule 590: white/party/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00591(outfit: dict) -> float:
    """Score rule 591: brown/sport/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00592(outfit: dict) -> float:
    """Score rule 592: orange/outdoor/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00593(outfit: dict) -> float:
    """Score rule 593: gray/work/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00594(outfit: dict) -> float:
    """Score rule 594: purple/sport/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00595(outfit: dict) -> float:
    """Score rule 595: olive/outdoor/winter/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00596(outfit: dict) -> float:
    """Score rule 596: green/work/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00597(outfit: dict) -> float:
    """Score rule 597: navy/travel/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00598(outfit: dict) -> float:
    """Score rule 598: cream/festival/winter/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00599(outfit: dict) -> float:
    """Score rule 599: black/formal/winter/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00600(outfit: dict) -> float:
    """Score rule 600: blue/wedding/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00601(outfit: dict) -> float:
    """Score rule 601: yellow/date/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00602(outfit: dict) -> float:
    """Score rule 602: burgundy/casual/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00603(outfit: dict) -> float:
    """Score rule 603: pink/party/spring/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00604(outfit: dict) -> float:
    """Score rule 604: beige/sport/spring/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00605(outfit: dict) -> float:
    """Score rule 605: red/casual/summer/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00606(outfit: dict) -> float:
    """Score rule 606: white/party/summer/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00607(outfit: dict) -> float:
    """Score rule 607: brown/sport/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00608(outfit: dict) -> float:
    """Score rule 608: black/outdoor/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00609(outfit: dict) -> float:
    """Score rule 609: blue/work/summer/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00610(outfit: dict) -> float:
    """Score rule 610: yellow/travel/autumn/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00611(outfit: dict) -> float:
    """Score rule 611: burgundy/festival/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00612(outfit: dict) -> float:
    """Score rule 612: pink/formal/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00613(outfit: dict) -> float:
    """Score rule 613: beige/wedding/autumn/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00614(outfit: dict) -> float:
    """Score rule 614: red/date/autumn/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00615(outfit: dict) -> float:
    """Score rule 615: white/casual/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00616(outfit: dict) -> float:
    """Score rule 616: brown/wedding/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00617(outfit: dict) -> float:
    """Score rule 617: orange/date/winter/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00618(outfit: dict) -> float:
    """Score rule 618: gray/casual/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00619(outfit: dict) -> float:
    """Score rule 619: purple/party/winter/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00620(outfit: dict) -> float:
    """Score rule 620: olive/sport/spring/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00621(outfit: dict) -> float:
    """Score rule 621: green/outdoor/spring/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00622(outfit: dict) -> float:
    """Score rule 622: navy/work/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00623(outfit: dict) -> float:
    """Score rule 623: cream/travel/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00624(outfit: dict) -> float:
    """Score rule 624: black/festival/spring/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00625(outfit: dict) -> float:
    """Score rule 625: blue/formal/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00626(outfit: dict) -> float:
    """Score rule 626: yellow/wedding/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00627(outfit: dict) -> float:
    """Score rule 627: gray/festival/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00628(outfit: dict) -> float:
    """Score rule 628: purple/formal/summer/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00629(outfit: dict) -> float:
    """Score rule 629: olive/wedding/summer/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00630(outfit: dict) -> float:
    """Score rule 630: green/date/autumn/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00631(outfit: dict) -> float:
    """Score rule 631: navy/casual/autumn/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00632(outfit: dict) -> float:
    """Score rule 632: cream/party/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00633(outfit: dict) -> float:
    """Score rule 633: black/sport/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00634(outfit: dict) -> float:
    """Score rule 634: blue/outdoor/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00635(outfit: dict) -> float:
    """Score rule 635: yellow/work/winter/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00636(outfit: dict) -> float:
    """Score rule 636: burgundy/travel/winter/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00637(outfit: dict) -> float:
    """Score rule 637: pink/festival/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00638(outfit: dict) -> float:
    """Score rule 638: beige/work/winter/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00639(outfit: dict) -> float:
    """Score rule 639: red/travel/winter/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00640(outfit: dict) -> float:
    """Score rule 640: white/festival/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00641(outfit: dict) -> float:
    """Score rule 641: brown/formal/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00642(outfit: dict) -> float:
    """Score rule 642: orange/wedding/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00643(outfit: dict) -> float:
    """Score rule 643: gray/date/spring/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00644(outfit: dict) -> float:
    """Score rule 644: purple/casual/spring/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00645(outfit: dict) -> float:
    """Score rule 645: olive/party/summer/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00646(outfit: dict) -> float:
    """Score rule 646: pink/sport/summer/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00647(outfit: dict) -> float:
    """Score rule 647: beige/outdoor/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00648(outfit: dict) -> float:
    """Score rule 648: red/work/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00649(outfit: dict) -> float:
    """Score rule 649: white/sport/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00650(outfit: dict) -> float:
    """Score rule 650: brown/outdoor/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00651(outfit: dict) -> float:
    """Score rule 651: orange/work/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00652(outfit: dict) -> float:
    """Score rule 652: gray/travel/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00653(outfit: dict) -> float:
    """Score rule 653: purple/festival/autumn/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00654(outfit: dict) -> float:
    """Score rule 654: olive/formal/autumn/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00655(outfit: dict) -> float:
    """Score rule 655: green/wedding/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00656(outfit: dict) -> float:
    """Score rule 656: navy/date/winter/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00657(outfit: dict) -> float:
    """Score rule 657: cream/casual/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00658(outfit: dict) -> float:
    """Score rule 658: black/party/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00659(outfit: dict) -> float:
    """Score rule 659: blue/sport/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00660(outfit: dict) -> float:
    """Score rule 660: yellow/casual/spring/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00661(outfit: dict) -> float:
    """Score rule 661: burgundy/party/spring/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00662(outfit: dict) -> float:
    """Score rule 662: pink/sport/spring/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00663(outfit: dict) -> float:
    """Score rule 663: beige/outdoor/spring/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00664(outfit: dict) -> float:
    """Score rule 664: red/work/spring/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00665(outfit: dict) -> float:
    """Score rule 665: navy/travel/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00666(outfit: dict) -> float:
    """Score rule 666: cream/festival/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00667(outfit: dict) -> float:
    """Score rule 667: black/formal/summer/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00668(outfit: dict) -> float:
    """Score rule 668: blue/wedding/summer/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00669(outfit: dict) -> float:
    """Score rule 669: yellow/date/summer/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00670(outfit: dict) -> float:
    """Score rule 670: burgundy/casual/autumn/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00671(outfit: dict) -> float:
    """Score rule 671: pink/wedding/autumn/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00672(outfit: dict) -> float:
    """Score rule 672: beige/date/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00673(outfit: dict) -> float:
    """Score rule 673: red/casual/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00674(outfit: dict) -> float:
    """Score rule 674: white/party/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00675(outfit: dict) -> float:
    """Score rule 675: brown/sport/winter/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00676(outfit: dict) -> float:
    """Score rule 676: orange/outdoor/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00677(outfit: dict) -> float:
    """Score rule 677: gray/work/winter/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00678(outfit: dict) -> float:
    """Score rule 678: purple/travel/winter/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00679(outfit: dict) -> float:
    """Score rule 679: olive/festival/winter/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00680(outfit: dict) -> float:
    """Score rule 680: green/formal/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00681(outfit: dict) -> float:
    """Score rule 681: navy/wedding/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00682(outfit: dict) -> float:
    """Score rule 682: cream/festival/spring/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00683(outfit: dict) -> float:
    """Score rule 683: black/formal/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00684(outfit: dict) -> float:
    """Score rule 684: brown/wedding/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00685(outfit: dict) -> float:
    """Score rule 685: orange/date/summer/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00686(outfit: dict) -> float:
    """Score rule 686: gray/casual/summer/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00687(outfit: dict) -> float:
    """Score rule 687: purple/party/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00688(outfit: dict) -> float:
    """Score rule 688: olive/sport/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00689(outfit: dict) -> float:
    """Score rule 689: green/outdoor/summer/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00690(outfit: dict) -> float:
    """Score rule 690: navy/work/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00691(outfit: dict) -> float:
    """Score rule 691: cream/travel/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00692(outfit: dict) -> float:
    """Score rule 692: black/festival/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00693(outfit: dict) -> float:
    """Score rule 693: blue/work/autumn/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00694(outfit: dict) -> float:
    """Score rule 694: yellow/travel/autumn/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00695(outfit: dict) -> float:
    """Score rule 695: burgundy/festival/winter/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00696(outfit: dict) -> float:
    """Score rule 696: pink/formal/winter/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00697(outfit: dict) -> float:
    """Score rule 697: beige/wedding/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00698(outfit: dict) -> float:
    """Score rule 698: red/date/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00699(outfit: dict) -> float:
    """Score rule 699: white/casual/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00700(outfit: dict) -> float:
    """Score rule 700: brown/party/spring/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00701(outfit: dict) -> float:
    """Score rule 701: orange/sport/spring/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00702(outfit: dict) -> float:
    """Score rule 702: gray/outdoor/spring/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00703(outfit: dict) -> float:
    """Score rule 703: yellow/work/spring/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00704(outfit: dict) -> float:
    """Score rule 704: burgundy/sport/spring/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00705(outfit: dict) -> float:
    """Score rule 705: pink/outdoor/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00706(outfit: dict) -> float:
    """Score rule 706: beige/work/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00707(outfit: dict) -> float:
    """Score rule 707: red/travel/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00708(outfit: dict) -> float:
    """Score rule 708: white/festival/summer/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00709(outfit: dict) -> float:
    """Score rule 709: brown/formal/summer/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00710(outfit: dict) -> float:
    """Score rule 710: orange/wedding/autumn/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00711(outfit: dict) -> float:
    """Score rule 711: gray/date/autumn/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00712(outfit: dict) -> float:
    """Score rule 712: purple/casual/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00713(outfit: dict) -> float:
    """Score rule 713: olive/party/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00714(outfit: dict) -> float:
    """Score rule 714: green/sport/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00715(outfit: dict) -> float:
    """Score rule 715: navy/casual/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00716(outfit: dict) -> float:
    """Score rule 716: cream/party/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00717(outfit: dict) -> float:
    """Score rule 717: black/sport/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00718(outfit: dict) -> float:
    """Score rule 718: blue/outdoor/winter/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00719(outfit: dict) -> float:
    """Score rule 719: yellow/work/winter/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00720(outfit: dict) -> float:
    """Score rule 720: burgundy/travel/spring/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00721(outfit: dict) -> float:
    """Score rule 721: pink/festival/spring/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00722(outfit: dict) -> float:
    """Score rule 722: olive/formal/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00723(outfit: dict) -> float:
    """Score rule 723: green/wedding/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00724(outfit: dict) -> float:
    """Score rule 724: navy/date/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00725(outfit: dict) -> float:
    """Score rule 725: cream/casual/summer/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00726(outfit: dict) -> float:
    """Score rule 726: black/wedding/summer/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00727(outfit: dict) -> float:
    """Score rule 727: blue/date/summer/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00728(outfit: dict) -> float:
    """Score rule 728: yellow/casual/summer/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00729(outfit: dict) -> float:
    """Score rule 729: burgundy/party/summer/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00730(outfit: dict) -> float:
    """Score rule 730: pink/sport/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00731(outfit: dict) -> float:
    """Score rule 731: beige/outdoor/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00732(outfit: dict) -> float:
    """Score rule 732: red/work/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00733(outfit: dict) -> float:
    """Score rule 733: white/travel/autumn/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00734(outfit: dict) -> float:
    """Score rule 734: brown/festival/autumn/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00735(outfit: dict) -> float:
    """Score rule 735: orange/formal/winter/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00736(outfit: dict) -> float:
    """Score rule 736: gray/wedding/winter/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00737(outfit: dict) -> float:
    """Score rule 737: purple/festival/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00738(outfit: dict) -> float:
    """Score rule 738: olive/formal/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00739(outfit: dict) -> float:
    """Score rule 739: green/wedding/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00740(outfit: dict) -> float:
    """Score rule 740: navy/date/spring/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00741(outfit: dict) -> float:
    """Score rule 741: red/casual/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00742(outfit: dict) -> float:
    """Score rule 742: white/party/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00743(outfit: dict) -> float:
    """Score rule 743: brown/sport/spring/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00744(outfit: dict) -> float:
    """Score rule 744: orange/outdoor/spring/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00745(outfit: dict) -> float:
    """Score rule 745: gray/work/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00746(outfit: dict) -> float:
    """Score rule 746: purple/travel/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00747(outfit: dict) -> float:
    """Score rule 747: olive/festival/summer/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00748(outfit: dict) -> float:
    """Score rule 748: green/work/summer/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00749(outfit: dict) -> float:
    """Score rule 749: navy/travel/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00750(outfit: dict) -> float:
    """Score rule 750: cream/festival/autumn/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00751(outfit: dict) -> float:
    """Score rule 751: black/formal/autumn/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00752(outfit: dict) -> float:
    """Score rule 752: blue/wedding/autumn/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00753(outfit: dict) -> float:
    """Score rule 753: yellow/date/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00754(outfit: dict) -> float:
    """Score rule 754: burgundy/casual/autumn/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00755(outfit: dict) -> float:
    """Score rule 755: pink/party/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00756(outfit: dict) -> float:
    """Score rule 756: beige/sport/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00757(outfit: dict) -> float:
    """Score rule 757: red/outdoor/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00758(outfit: dict) -> float:
    """Score rule 758: white/work/winter/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00759(outfit: dict) -> float:
    """Score rule 759: brown/sport/winter/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00760(outfit: dict) -> float:
    """Score rule 760: black/outdoor/spring/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00761(outfit: dict) -> float:
    """Score rule 761: blue/work/spring/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00762(outfit: dict) -> float:
    """Score rule 762: yellow/travel/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00763(outfit: dict) -> float:
    """Score rule 763: burgundy/festival/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00764(outfit: dict) -> float:
    """Score rule 764: pink/formal/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00765(outfit: dict) -> float:
    """Score rule 765: beige/wedding/summer/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00766(outfit: dict) -> float:
    """Score rule 766: red/date/summer/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00767(outfit: dict) -> float:
    """Score rule 767: white/casual/summer/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00768(outfit: dict) -> float:
    """Score rule 768: brown/party/summer/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00769(outfit: dict) -> float:
    """Score rule 769: orange/sport/summer/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00770(outfit: dict) -> float:
    """Score rule 770: gray/casual/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00771(outfit: dict) -> float:
    """Score rule 771: purple/party/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00772(outfit: dict) -> float:
    """Score rule 772: olive/sport/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00773(outfit: dict) -> float:
    """Score rule 773: green/outdoor/autumn/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00774(outfit: dict) -> float:
    """Score rule 774: navy/work/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00775(outfit: dict) -> float:
    """Score rule 775: cream/travel/winter/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00776(outfit: dict) -> float:
    """Score rule 776: black/festival/winter/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00777(outfit: dict) -> float:
    """Score rule 777: blue/formal/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00778(outfit: dict) -> float:
    """Score rule 778: yellow/wedding/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00779(outfit: dict) -> float:
    """Score rule 779: gray/date/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00780(outfit: dict) -> float:
    """Score rule 780: purple/casual/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00781(outfit: dict) -> float:
    """Score rule 781: olive/wedding/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00782(outfit: dict) -> float:
    """Score rule 782: green/date/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00783(outfit: dict) -> float:
    """Score rule 783: navy/casual/spring/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00784(outfit: dict) -> float:
    """Score rule 784: cream/party/spring/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00785(outfit: dict) -> float:
    """Score rule 785: black/sport/summer/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00786(outfit: dict) -> float:
    """Score rule 786: blue/outdoor/summer/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00787(outfit: dict) -> float:
    """Score rule 787: yellow/work/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00788(outfit: dict) -> float:
    """Score rule 788: burgundy/travel/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00789(outfit: dict) -> float:
    """Score rule 789: pink/festival/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00790(outfit: dict) -> float:
    """Score rule 790: beige/formal/autumn/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00791(outfit: dict) -> float:
    """Score rule 791: red/wedding/autumn/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00792(outfit: dict) -> float:
    """Score rule 792: white/festival/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00793(outfit: dict) -> float:
    """Score rule 793: brown/formal/autumn/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00794(outfit: dict) -> float:
    """Score rule 794: orange/wedding/autumn/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00795(outfit: dict) -> float:
    """Score rule 795: gray/date/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00796(outfit: dict) -> float:
    """Score rule 796: purple/casual/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00797(outfit: dict) -> float:
    """Score rule 797: olive/party/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00798(outfit: dict) -> float:
    """Score rule 798: pink/sport/winter/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00799(outfit: dict) -> float:
    """Score rule 799: beige/outdoor/winter/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00800(outfit: dict) -> float:
    """Score rule 800: red/work/spring/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00801(outfit: dict) -> float:
    """Score rule 801: white/travel/spring/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00802(outfit: dict) -> float:
    """Score rule 802: brown/festival/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00803(outfit: dict) -> float:
    """Score rule 803: orange/work/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00804(outfit: dict) -> float:
    """Score rule 804: gray/travel/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00805(outfit: dict) -> float:
    """Score rule 805: purple/festival/summer/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00806(outfit: dict) -> float:
    """Score rule 806: olive/formal/summer/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00807(outfit: dict) -> float:
    """Score rule 807: green/wedding/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00808(outfit: dict) -> float:
    """Score rule 808: navy/date/summer/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00809(outfit: dict) -> float:
    """Score rule 809: cream/casual/summer/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00810(outfit: dict) -> float:
    """Score rule 810: black/party/autumn/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00811(outfit: dict) -> float:
    """Score rule 811: blue/sport/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00812(outfit: dict) -> float:
    """Score rule 812: yellow/outdoor/autumn/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00813(outfit: dict) -> float:
    """Score rule 813: burgundy/work/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00814(outfit: dict) -> float:
    """Score rule 814: pink/sport/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00815(outfit: dict) -> float:
    """Score rule 815: beige/outdoor/winter/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00816(outfit: dict) -> float:
    """Score rule 816: red/work/winter/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00817(outfit: dict) -> float:
    """Score rule 817: navy/travel/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00818(outfit: dict) -> float:
    """Score rule 818: cream/festival/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00819(outfit: dict) -> float:
    """Score rule 819: black/formal/winter/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00820(outfit: dict) -> float:
    """Score rule 820: blue/wedding/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00821(outfit: dict) -> float:
    """Score rule 821: yellow/date/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00822(outfit: dict) -> float:
    """Score rule 822: burgundy/casual/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00823(outfit: dict) -> float:
    """Score rule 823: pink/party/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00824(outfit: dict) -> float:
    """Score rule 824: beige/sport/spring/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00825(outfit: dict) -> float:
    """Score rule 825: red/casual/summer/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00826(outfit: dict) -> float:
    """Score rule 826: white/party/summer/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00827(outfit: dict) -> float:
    """Score rule 827: brown/sport/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00828(outfit: dict) -> float:
    """Score rule 828: orange/outdoor/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00829(outfit: dict) -> float:
    """Score rule 829: gray/work/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00830(outfit: dict) -> float:
    """Score rule 830: purple/travel/autumn/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00831(outfit: dict) -> float:
    """Score rule 831: olive/festival/autumn/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00832(outfit: dict) -> float:
    """Score rule 832: green/formal/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00833(outfit: dict) -> float:
    """Score rule 833: navy/wedding/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00834(outfit: dict) -> float:
    """Score rule 834: cream/date/autumn/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00835(outfit: dict) -> float:
    """Score rule 835: black/casual/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00836(outfit: dict) -> float:
    """Score rule 836: brown/wedding/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00837(outfit: dict) -> float:
    """Score rule 837: orange/date/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00838(outfit: dict) -> float:
    """Score rule 838: gray/casual/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00839(outfit: dict) -> float:
    """Score rule 839: purple/party/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00840(outfit: dict) -> float:
    """Score rule 840: olive/sport/spring/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00841(outfit: dict) -> float:
    """Score rule 841: green/outdoor/spring/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00842(outfit: dict) -> float:
    """Score rule 842: navy/work/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00843(outfit: dict) -> float:
    """Score rule 843: cream/travel/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00844(outfit: dict) -> float:
    """Score rule 844: black/festival/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00845(outfit: dict) -> float:
    """Score rule 845: blue/formal/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00846(outfit: dict) -> float:
    """Score rule 846: yellow/wedding/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00847(outfit: dict) -> float:
    """Score rule 847: burgundy/festival/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00848(outfit: dict) -> float:
    """Score rule 848: pink/formal/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00849(outfit: dict) -> float:
    """Score rule 849: beige/wedding/summer/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00850(outfit: dict) -> float:
    """Score rule 850: red/date/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00851(outfit: dict) -> float:
    """Score rule 851: white/casual/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00852(outfit: dict) -> float:
    """Score rule 852: brown/party/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00853(outfit: dict) -> float:
    """Score rule 853: orange/sport/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00854(outfit: dict) -> float:
    """Score rule 854: gray/outdoor/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00855(outfit: dict) -> float:
    """Score rule 855: yellow/work/winter/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00856(outfit: dict) -> float:
    """Score rule 856: burgundy/travel/winter/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00857(outfit: dict) -> float:
    """Score rule 857: pink/festival/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00858(outfit: dict) -> float:
    """Score rule 858: beige/work/winter/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00859(outfit: dict) -> float:
    """Score rule 859: red/travel/winter/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00860(outfit: dict) -> float:
    """Score rule 860: white/festival/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00861(outfit: dict) -> float:
    """Score rule 861: brown/formal/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00862(outfit: dict) -> float:
    """Score rule 862: orange/wedding/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00863(outfit: dict) -> float:
    """Score rule 863: gray/date/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00864(outfit: dict) -> float:
    """Score rule 864: purple/casual/spring/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00865(outfit: dict) -> float:
    """Score rule 865: olive/party/summer/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00866(outfit: dict) -> float:
    """Score rule 866: green/sport/summer/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00867(outfit: dict) -> float:
    """Score rule 867: navy/outdoor/summer/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00868(outfit: dict) -> float:
    """Score rule 868: cream/work/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00869(outfit: dict) -> float:
    """Score rule 869: black/sport/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00870(outfit: dict) -> float:
    """Score rule 870: blue/outdoor/autumn/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00871(outfit: dict) -> float:
    """Score rule 871: yellow/work/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00872(outfit: dict) -> float:
    """Score rule 872: burgundy/travel/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00873(outfit: dict) -> float:
    """Score rule 873: pink/festival/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00874(outfit: dict) -> float:
    """Score rule 874: olive/formal/autumn/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00875(outfit: dict) -> float:
    """Score rule 875: green/wedding/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00876(outfit: dict) -> float:
    """Score rule 876: navy/date/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00877(outfit: dict) -> float:
    """Score rule 877: cream/casual/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00878(outfit: dict) -> float:
    """Score rule 878: black/party/winter/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00879(outfit: dict) -> float:
    """Score rule 879: blue/sport/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00880(outfit: dict) -> float:
    """Score rule 880: yellow/casual/spring/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00881(outfit: dict) -> float:
    """Score rule 881: burgundy/party/spring/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00882(outfit: dict) -> float:
    """Score rule 882: pink/sport/spring/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00883(outfit: dict) -> float:
    """Score rule 883: beige/outdoor/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00884(outfit: dict) -> float:
    """Score rule 884: red/work/spring/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00885(outfit: dict) -> float:
    """Score rule 885: white/travel/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00886(outfit: dict) -> float:
    """Score rule 886: brown/festival/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00887(outfit: dict) -> float:
    """Score rule 887: orange/formal/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00888(outfit: dict) -> float:
    """Score rule 888: gray/wedding/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00889(outfit: dict) -> float:
    """Score rule 889: purple/date/summer/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00890(outfit: dict) -> float:
    """Score rule 890: olive/casual/autumn/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00891(outfit: dict) -> float:
    """Score rule 891: green/wedding/autumn/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00892(outfit: dict) -> float:
    """Score rule 892: navy/date/autumn/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00893(outfit: dict) -> float:
    """Score rule 893: red/casual/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00894(outfit: dict) -> float:
    """Score rule 894: white/party/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00895(outfit: dict) -> float:
    """Score rule 895: brown/sport/winter/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00896(outfit: dict) -> float:
    """Score rule 896: orange/outdoor/winter/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00897(outfit: dict) -> float:
    """Score rule 897: gray/work/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00898(outfit: dict) -> float:
    """Score rule 898: purple/travel/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00899(outfit: dict) -> float:
    """Score rule 899: olive/festival/winter/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00900(outfit: dict) -> float:
    """Score rule 900: green/formal/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00901(outfit: dict) -> float:
    """Score rule 901: navy/wedding/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00902(outfit: dict) -> float:
    """Score rule 902: cream/festival/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00903(outfit: dict) -> float:
    """Score rule 903: black/formal/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00904(outfit: dict) -> float:
    """Score rule 904: blue/wedding/spring/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00905(outfit: dict) -> float:
    """Score rule 905: yellow/date/summer/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00906(outfit: dict) -> float:
    """Score rule 906: burgundy/casual/summer/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00907(outfit: dict) -> float:
    """Score rule 907: pink/party/summer/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00908(outfit: dict) -> float:
    """Score rule 908: beige/sport/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00909(outfit: dict) -> float:
    """Score rule 909: red/outdoor/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00910(outfit: dict) -> float:
    """Score rule 910: white/work/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00911(outfit: dict) -> float:
    """Score rule 911: brown/travel/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00912(outfit: dict) -> float:
    """Score rule 912: black/festival/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00913(outfit: dict) -> float:
    """Score rule 913: blue/work/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00914(outfit: dict) -> float:
    """Score rule 914: yellow/travel/autumn/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00915(outfit: dict) -> float:
    """Score rule 915: burgundy/festival/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00916(outfit: dict) -> float:
    """Score rule 916: pink/formal/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00917(outfit: dict) -> float:
    """Score rule 917: beige/wedding/winter/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00918(outfit: dict) -> float:
    """Score rule 918: red/date/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00919(outfit: dict) -> float:
    """Score rule 919: white/casual/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00920(outfit: dict) -> float:
    """Score rule 920: brown/party/spring/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00921(outfit: dict) -> float:
    """Score rule 921: orange/sport/spring/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00922(outfit: dict) -> float:
    """Score rule 922: gray/outdoor/spring/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00923(outfit: dict) -> float:
    """Score rule 923: purple/work/spring/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00924(outfit: dict) -> float:
    """Score rule 924: olive/sport/spring/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00925(outfit: dict) -> float:
    """Score rule 925: green/outdoor/summer/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00926(outfit: dict) -> float:
    """Score rule 926: navy/work/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00927(outfit: dict) -> float:
    """Score rule 927: cream/travel/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00928(outfit: dict) -> float:
    """Score rule 928: black/festival/summer/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00929(outfit: dict) -> float:
    """Score rule 929: blue/formal/summer/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00930(outfit: dict) -> float:
    """Score rule 930: yellow/wedding/autumn/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00931(outfit: dict) -> float:
    """Score rule 931: gray/date/autumn/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00932(outfit: dict) -> float:
    """Score rule 932: purple/casual/autumn/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00933(outfit: dict) -> float:
    """Score rule 933: olive/party/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00934(outfit: dict) -> float:
    """Score rule 934: green/sport/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00935(outfit: dict) -> float:
    """Score rule 935: navy/casual/winter/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00936(outfit: dict) -> float:
    """Score rule 936: cream/party/winter/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00937(outfit: dict) -> float:
    """Score rule 937: black/sport/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00938(outfit: dict) -> float:
    """Score rule 938: blue/outdoor/winter/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00939(outfit: dict) -> float:
    """Score rule 939: yellow/work/winter/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00940(outfit: dict) -> float:
    """Score rule 940: burgundy/travel/spring/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00941(outfit: dict) -> float:
    """Score rule 941: pink/festival/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00942(outfit: dict) -> float:
    """Score rule 942: beige/formal/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00943(outfit: dict) -> float:
    """Score rule 943: red/wedding/spring/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00944(outfit: dict) -> float:
    """Score rule 944: white/date/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00945(outfit: dict) -> float:
    """Score rule 945: brown/casual/summer/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00946(outfit: dict) -> float:
    """Score rule 946: orange/wedding/summer/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00947(outfit: dict) -> float:
    """Score rule 947: gray/date/summer/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00948(outfit: dict) -> float:
    """Score rule 948: purple/casual/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00949(outfit: dict) -> float:
    """Score rule 949: olive/party/summer/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00950(outfit: dict) -> float:
    """Score rule 950: pink/sport/autumn/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00951(outfit: dict) -> float:
    """Score rule 951: beige/outdoor/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00952(outfit: dict) -> float:
    """Score rule 952: red/work/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00953(outfit: dict) -> float:
    """Score rule 953: white/travel/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00954(outfit: dict) -> float:
    """Score rule 954: brown/festival/autumn/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00955(outfit: dict) -> float:
    """Score rule 955: orange/formal/winter/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00956(outfit: dict) -> float:
    """Score rule 956: gray/wedding/winter/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00957(outfit: dict) -> float:
    """Score rule 957: purple/festival/winter/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00958(outfit: dict) -> float:
    """Score rule 958: olive/formal/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00959(outfit: dict) -> float:
    """Score rule 959: green/wedding/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00960(outfit: dict) -> float:
    """Score rule 960: navy/date/spring/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00961(outfit: dict) -> float:
    """Score rule 961: cream/casual/spring/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00962(outfit: dict) -> float:
    """Score rule 962: black/party/spring/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00963(outfit: dict) -> float:
    """Score rule 963: blue/sport/spring/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00964(outfit: dict) -> float:
    """Score rule 964: yellow/outdoor/spring/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00965(outfit: dict) -> float:
    """Score rule 965: burgundy/work/summer/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00966(outfit: dict) -> float:
    """Score rule 966: pink/travel/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00967(outfit: dict) -> float:
    """Score rule 967: beige/festival/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00968(outfit: dict) -> float:
    """Score rule 968: red/work/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00969(outfit: dict) -> float:
    """Score rule 969: navy/travel/summer/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00970(outfit: dict) -> float:
    """Score rule 970: cream/festival/autumn/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00971(outfit: dict) -> float:
    """Score rule 971: black/formal/autumn/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00972(outfit: dict) -> float:
    """Score rule 972: blue/wedding/autumn/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00973(outfit: dict) -> float:
    """Score rule 973: yellow/date/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00974(outfit: dict) -> float:
    """Score rule 974: burgundy/casual/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00975(outfit: dict) -> float:
    """Score rule 975: pink/party/winter/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00976(outfit: dict) -> float:
    """Score rule 976: beige/sport/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00977(outfit: dict) -> float:
    """Score rule 977: red/outdoor/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00978(outfit: dict) -> float:
    """Score rule 978: white/work/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00979(outfit: dict) -> float:
    """Score rule 979: brown/sport/winter/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00980(outfit: dict) -> float:
    """Score rule 980: orange/outdoor/spring/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00981(outfit: dict) -> float:
    """Score rule 981: gray/work/spring/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00982(outfit: dict) -> float:
    """Score rule 982: purple/travel/spring/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00983(outfit: dict) -> float:
    """Score rule 983: olive/festival/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00984(outfit: dict) -> float:
    """Score rule 984: green/formal/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00985(outfit: dict) -> float:
    """Score rule 985: navy/wedding/summer/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00986(outfit: dict) -> float:
    """Score rule 986: cream/date/summer/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00987(outfit: dict) -> float:
    """Score rule 987: black/casual/summer/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00988(outfit: dict) -> float:
    """Score rule 988: brown/party/summer/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00989(outfit: dict) -> float:
    """Score rule 989: orange/sport/summer/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00990(outfit: dict) -> float:
    """Score rule 990: gray/casual/autumn/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00991(outfit: dict) -> float:
    """Score rule 991: purple/party/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00992(outfit: dict) -> float:
    """Score rule 992: olive/sport/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00993(outfit: dict) -> float:
    """Score rule 993: green/outdoor/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00994(outfit: dict) -> float:
    """Score rule 994: navy/work/autumn/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00995(outfit: dict) -> float:
    """Score rule 995: cream/travel/winter/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00996(outfit: dict) -> float:
    """Score rule 996: black/festival/winter/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00997(outfit: dict) -> float:
    """Score rule 997: blue/formal/winter/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00998(outfit: dict) -> float:
    """Score rule 998: yellow/wedding/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_00999(outfit: dict) -> float:
    """Score rule 999: burgundy/date/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

