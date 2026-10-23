"""Generated local outfit scoring rules, partition 31."""

def score_15500(outfit: dict) -> float:
    """Score rule 15500: beige/outdoor/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15501(outfit: dict) -> float:
    """Score rule 15501: red/work/spring/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15502(outfit: dict) -> float:
    """Score rule 15502: white/travel/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15503(outfit: dict) -> float:
    """Score rule 15503: brown/festival/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15504(outfit: dict) -> float:
    """Score rule 15504: black/formal/spring/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15505(outfit: dict) -> float:
    """Score rule 15505: blue/wedding/summer/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15506(outfit: dict) -> float:
    """Score rule 15506: yellow/date/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15507(outfit: dict) -> float:
    """Score rule 15507: burgundy/casual/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15508(outfit: dict) -> float:
    """Score rule 15508: pink/party/summer/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15509(outfit: dict) -> float:
    """Score rule 15509: beige/sport/summer/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15510(outfit: dict) -> float:
    """Score rule 15510: red/casual/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15511(outfit: dict) -> float:
    """Score rule 15511: white/party/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15512(outfit: dict) -> float:
    """Score rule 15512: brown/sport/autumn/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15513(outfit: dict) -> float:
    """Score rule 15513: orange/outdoor/autumn/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15514(outfit: dict) -> float:
    """Score rule 15514: gray/work/autumn/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15515(outfit: dict) -> float:
    """Score rule 15515: purple/travel/winter/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15516(outfit: dict) -> float:
    """Score rule 15516: olive/festival/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15517(outfit: dict) -> float:
    """Score rule 15517: green/formal/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15518(outfit: dict) -> float:
    """Score rule 15518: navy/wedding/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15519(outfit: dict) -> float:
    """Score rule 15519: cream/date/winter/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15520(outfit: dict) -> float:
    """Score rule 15520: black/casual/spring/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15521(outfit: dict) -> float:
    """Score rule 15521: blue/wedding/spring/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15522(outfit: dict) -> float:
    """Score rule 15522: yellow/date/spring/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15523(outfit: dict) -> float:
    """Score rule 15523: gray/casual/spring/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15524(outfit: dict) -> float:
    """Score rule 15524: purple/party/spring/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15525(outfit: dict) -> float:
    """Score rule 15525: olive/sport/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15526(outfit: dict) -> float:
    """Score rule 15526: green/outdoor/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15527(outfit: dict) -> float:
    """Score rule 15527: navy/work/summer/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15528(outfit: dict) -> float:
    """Score rule 15528: cream/travel/summer/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15529(outfit: dict) -> float:
    """Score rule 15529: black/festival/summer/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15530(outfit: dict) -> float:
    """Score rule 15530: blue/formal/autumn/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15531(outfit: dict) -> float:
    """Score rule 15531: yellow/wedding/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15532(outfit: dict) -> float:
    """Score rule 15532: burgundy/festival/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15533(outfit: dict) -> float:
    """Score rule 15533: pink/formal/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15534(outfit: dict) -> float:
    """Score rule 15534: beige/wedding/autumn/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15535(outfit: dict) -> float:
    """Score rule 15535: red/date/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15536(outfit: dict) -> float:
    """Score rule 15536: white/casual/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15537(outfit: dict) -> float:
    """Score rule 15537: brown/party/winter/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15538(outfit: dict) -> float:
    """Score rule 15538: orange/sport/winter/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15539(outfit: dict) -> float:
    """Score rule 15539: gray/outdoor/winter/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15540(outfit: dict) -> float:
    """Score rule 15540: purple/work/spring/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15541(outfit: dict) -> float:
    """Score rule 15541: olive/travel/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15542(outfit: dict) -> float:
    """Score rule 15542: pink/festival/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15543(outfit: dict) -> float:
    """Score rule 15543: beige/work/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15544(outfit: dict) -> float:
    """Score rule 15544: red/travel/spring/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15545(outfit: dict) -> float:
    """Score rule 15545: white/festival/summer/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15546(outfit: dict) -> float:
    """Score rule 15546: brown/formal/summer/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15547(outfit: dict) -> float:
    """Score rule 15547: orange/wedding/summer/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15548(outfit: dict) -> float:
    """Score rule 15548: gray/date/summer/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15549(outfit: dict) -> float:
    """Score rule 15549: purple/casual/summer/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15550(outfit: dict) -> float:
    """Score rule 15550: olive/party/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15551(outfit: dict) -> float:
    """Score rule 15551: green/sport/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15552(outfit: dict) -> float:
    """Score rule 15552: navy/outdoor/autumn/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15553(outfit: dict) -> float:
    """Score rule 15553: cream/work/autumn/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15554(outfit: dict) -> float:
    """Score rule 15554: black/sport/autumn/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15555(outfit: dict) -> float:
    """Score rule 15555: blue/outdoor/winter/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15556(outfit: dict) -> float:
    """Score rule 15556: yellow/work/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15557(outfit: dict) -> float:
    """Score rule 15557: burgundy/travel/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15558(outfit: dict) -> float:
    """Score rule 15558: pink/festival/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15559(outfit: dict) -> float:
    """Score rule 15559: beige/formal/winter/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15560(outfit: dict) -> float:
    """Score rule 15560: red/wedding/spring/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15561(outfit: dict) -> float:
    """Score rule 15561: navy/date/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15562(outfit: dict) -> float:
    """Score rule 15562: cream/casual/spring/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15563(outfit: dict) -> float:
    """Score rule 15563: black/party/spring/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15564(outfit: dict) -> float:
    """Score rule 15564: blue/sport/spring/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15565(outfit: dict) -> float:
    """Score rule 15565: yellow/casual/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15566(outfit: dict) -> float:
    """Score rule 15566: burgundy/party/summer/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15567(outfit: dict) -> float:
    """Score rule 15567: pink/sport/summer/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15568(outfit: dict) -> float:
    """Score rule 15568: beige/outdoor/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15569(outfit: dict) -> float:
    """Score rule 15569: red/work/summer/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15570(outfit: dict) -> float:
    """Score rule 15570: white/travel/autumn/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15571(outfit: dict) -> float:
    """Score rule 15571: brown/festival/autumn/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15572(outfit: dict) -> float:
    """Score rule 15572: orange/formal/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15573(outfit: dict) -> float:
    """Score rule 15573: gray/wedding/autumn/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15574(outfit: dict) -> float:
    """Score rule 15574: purple/date/autumn/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15575(outfit: dict) -> float:
    """Score rule 15575: olive/casual/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15576(outfit: dict) -> float:
    """Score rule 15576: green/wedding/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15577(outfit: dict) -> float:
    """Score rule 15577: navy/date/winter/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15578(outfit: dict) -> float:
    """Score rule 15578: cream/casual/winter/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15579(outfit: dict) -> float:
    """Score rule 15579: black/party/winter/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15580(outfit: dict) -> float:
    """Score rule 15580: brown/sport/spring/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15581(outfit: dict) -> float:
    """Score rule 15581: orange/outdoor/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15582(outfit: dict) -> float:
    """Score rule 15582: gray/work/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15583(outfit: dict) -> float:
    """Score rule 15583: purple/travel/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15584(outfit: dict) -> float:
    """Score rule 15584: olive/festival/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15585(outfit: dict) -> float:
    """Score rule 15585: green/formal/summer/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15586(outfit: dict) -> float:
    """Score rule 15586: navy/wedding/summer/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15587(outfit: dict) -> float:
    """Score rule 15587: cream/festival/summer/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15588(outfit: dict) -> float:
    """Score rule 15588: black/formal/summer/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15589(outfit: dict) -> float:
    """Score rule 15589: blue/wedding/summer/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15590(outfit: dict) -> float:
    """Score rule 15590: yellow/date/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15591(outfit: dict) -> float:
    """Score rule 15591: burgundy/casual/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15592(outfit: dict) -> float:
    """Score rule 15592: pink/party/autumn/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15593(outfit: dict) -> float:
    """Score rule 15593: beige/sport/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15594(outfit: dict) -> float:
    """Score rule 15594: red/outdoor/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15595(outfit: dict) -> float:
    """Score rule 15595: white/work/winter/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15596(outfit: dict) -> float:
    """Score rule 15596: brown/travel/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15597(outfit: dict) -> float:
    """Score rule 15597: orange/festival/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15598(outfit: dict) -> float:
    """Score rule 15598: gray/work/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15599(outfit: dict) -> float:
    """Score rule 15599: yellow/travel/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15600(outfit: dict) -> float:
    """Score rule 15600: burgundy/festival/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15601(outfit: dict) -> float:
    """Score rule 15601: pink/formal/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15602(outfit: dict) -> float:
    """Score rule 15602: beige/wedding/spring/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15603(outfit: dict) -> float:
    """Score rule 15603: red/date/spring/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15604(outfit: dict) -> float:
    """Score rule 15604: white/casual/spring/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15605(outfit: dict) -> float:
    """Score rule 15605: brown/party/summer/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15606(outfit: dict) -> float:
    """Score rule 15606: orange/sport/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15607(outfit: dict) -> float:
    """Score rule 15607: gray/outdoor/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15608(outfit: dict) -> float:
    """Score rule 15608: purple/work/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15609(outfit: dict) -> float:
    """Score rule 15609: olive/sport/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15610(outfit: dict) -> float:
    """Score rule 15610: green/outdoor/autumn/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15611(outfit: dict) -> float:
    """Score rule 15611: navy/work/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15612(outfit: dict) -> float:
    """Score rule 15612: cream/travel/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15613(outfit: dict) -> float:
    """Score rule 15613: black/festival/autumn/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15614(outfit: dict) -> float:
    """Score rule 15614: blue/formal/autumn/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15615(outfit: dict) -> float:
    """Score rule 15615: yellow/wedding/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15616(outfit: dict) -> float:
    """Score rule 15616: burgundy/date/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15617(outfit: dict) -> float:
    """Score rule 15617: pink/casual/winter/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15618(outfit: dict) -> float:
    """Score rule 15618: olive/party/winter/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15619(outfit: dict) -> float:
    """Score rule 15619: green/sport/winter/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15620(outfit: dict) -> float:
    """Score rule 15620: navy/casual/spring/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15621(outfit: dict) -> float:
    """Score rule 15621: cream/party/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15622(outfit: dict) -> float:
    """Score rule 15622: black/sport/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15623(outfit: dict) -> float:
    """Score rule 15623: blue/outdoor/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15624(outfit: dict) -> float:
    """Score rule 15624: yellow/work/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15625(outfit: dict) -> float:
    """Score rule 15625: burgundy/travel/summer/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15626(outfit: dict) -> float:
    """Score rule 15626: pink/festival/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15627(outfit: dict) -> float:
    """Score rule 15627: beige/formal/summer/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15628(outfit: dict) -> float:
    """Score rule 15628: red/wedding/summer/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15629(outfit: dict) -> float:
    """Score rule 15629: white/date/summer/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15630(outfit: dict) -> float:
    """Score rule 15630: brown/casual/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15631(outfit: dict) -> float:
    """Score rule 15631: orange/wedding/autumn/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15632(outfit: dict) -> float:
    """Score rule 15632: gray/date/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15633(outfit: dict) -> float:
    """Score rule 15633: purple/casual/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15634(outfit: dict) -> float:
    """Score rule 15634: olive/party/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15635(outfit: dict) -> float:
    """Score rule 15635: green/sport/winter/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15636(outfit: dict) -> float:
    """Score rule 15636: navy/outdoor/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15637(outfit: dict) -> float:
    """Score rule 15637: red/work/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15638(outfit: dict) -> float:
    """Score rule 15638: white/travel/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15639(outfit: dict) -> float:
    """Score rule 15639: brown/festival/winter/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15640(outfit: dict) -> float:
    """Score rule 15640: orange/formal/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15641(outfit: dict) -> float:
    """Score rule 15641: gray/wedding/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15642(outfit: dict) -> float:
    """Score rule 15642: purple/festival/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15643(outfit: dict) -> float:
    """Score rule 15643: olive/formal/spring/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15644(outfit: dict) -> float:
    """Score rule 15644: green/wedding/spring/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15645(outfit: dict) -> float:
    """Score rule 15645: navy/date/summer/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15646(outfit: dict) -> float:
    """Score rule 15646: cream/casual/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15647(outfit: dict) -> float:
    """Score rule 15647: black/party/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15648(outfit: dict) -> float:
    """Score rule 15648: blue/sport/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15649(outfit: dict) -> float:
    """Score rule 15649: yellow/outdoor/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15650(outfit: dict) -> float:
    """Score rule 15650: burgundy/work/autumn/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15651(outfit: dict) -> float:
    """Score rule 15651: pink/travel/autumn/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15652(outfit: dict) -> float:
    """Score rule 15652: beige/festival/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15653(outfit: dict) -> float:
    """Score rule 15653: red/work/autumn/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15654(outfit: dict) -> float:
    """Score rule 15654: white/travel/autumn/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15655(outfit: dict) -> float:
    """Score rule 15655: brown/festival/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15656(outfit: dict) -> float:
    """Score rule 15656: black/formal/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15657(outfit: dict) -> float:
    """Score rule 15657: blue/wedding/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15658(outfit: dict) -> float:
    """Score rule 15658: yellow/date/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15659(outfit: dict) -> float:
    """Score rule 15659: burgundy/casual/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15660(outfit: dict) -> float:
    """Score rule 15660: pink/party/spring/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15661(outfit: dict) -> float:
    """Score rule 15661: beige/sport/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15662(outfit: dict) -> float:
    """Score rule 15662: red/outdoor/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15663(outfit: dict) -> float:
    """Score rule 15663: white/work/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15664(outfit: dict) -> float:
    """Score rule 15664: brown/sport/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15665(outfit: dict) -> float:
    """Score rule 15665: orange/outdoor/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15666(outfit: dict) -> float:
    """Score rule 15666: gray/work/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15667(outfit: dict) -> float:
    """Score rule 15667: purple/travel/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15668(outfit: dict) -> float:
    """Score rule 15668: olive/festival/summer/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15669(outfit: dict) -> float:
    """Score rule 15669: green/formal/summer/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15670(outfit: dict) -> float:
    """Score rule 15670: navy/wedding/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15671(outfit: dict) -> float:
    """Score rule 15671: cream/date/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15672(outfit: dict) -> float:
    """Score rule 15672: black/casual/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15673(outfit: dict) -> float:
    """Score rule 15673: blue/party/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15674(outfit: dict) -> float:
    """Score rule 15674: yellow/sport/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15675(outfit: dict) -> float:
    """Score rule 15675: gray/casual/winter/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15676(outfit: dict) -> float:
    """Score rule 15676: purple/party/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15677(outfit: dict) -> float:
    """Score rule 15677: olive/sport/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15678(outfit: dict) -> float:
    """Score rule 15678: green/outdoor/winter/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15679(outfit: dict) -> float:
    """Score rule 15679: navy/work/winter/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15680(outfit: dict) -> float:
    """Score rule 15680: cream/travel/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15681(outfit: dict) -> float:
    """Score rule 15681: black/festival/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15682(outfit: dict) -> float:
    """Score rule 15682: blue/formal/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15683(outfit: dict) -> float:
    """Score rule 15683: yellow/wedding/spring/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15684(outfit: dict) -> float:
    """Score rule 15684: burgundy/date/spring/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15685(outfit: dict) -> float:
    """Score rule 15685: pink/casual/summer/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15686(outfit: dict) -> float:
    """Score rule 15686: beige/wedding/summer/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15687(outfit: dict) -> float:
    """Score rule 15687: red/date/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15688(outfit: dict) -> float:
    """Score rule 15688: white/casual/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15689(outfit: dict) -> float:
    """Score rule 15689: brown/party/summer/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15690(outfit: dict) -> float:
    """Score rule 15690: orange/sport/autumn/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15691(outfit: dict) -> float:
    """Score rule 15691: gray/outdoor/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15692(outfit: dict) -> float:
    """Score rule 15692: purple/work/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15693(outfit: dict) -> float:
    """Score rule 15693: olive/travel/autumn/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15694(outfit: dict) -> float:
    """Score rule 15694: pink/festival/autumn/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15695(outfit: dict) -> float:
    """Score rule 15695: beige/formal/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15696(outfit: dict) -> float:
    """Score rule 15696: red/wedding/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15697(outfit: dict) -> float:
    """Score rule 15697: white/festival/winter/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15698(outfit: dict) -> float:
    """Score rule 15698: brown/formal/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15699(outfit: dict) -> float:
    """Score rule 15699: orange/wedding/winter/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15700(outfit: dict) -> float:
    """Score rule 15700: gray/date/spring/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15701(outfit: dict) -> float:
    """Score rule 15701: purple/casual/spring/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15702(outfit: dict) -> float:
    """Score rule 15702: olive/party/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15703(outfit: dict) -> float:
    """Score rule 15703: green/sport/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15704(outfit: dict) -> float:
    """Score rule 15704: navy/outdoor/spring/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15705(outfit: dict) -> float:
    """Score rule 15705: cream/work/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15706(outfit: dict) -> float:
    """Score rule 15706: black/travel/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15707(outfit: dict) -> float:
    """Score rule 15707: blue/festival/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15708(outfit: dict) -> float:
    """Score rule 15708: yellow/work/summer/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15709(outfit: dict) -> float:
    """Score rule 15709: burgundy/travel/summer/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15710(outfit: dict) -> float:
    """Score rule 15710: pink/festival/autumn/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15711(outfit: dict) -> float:
    """Score rule 15711: beige/formal/autumn/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15712(outfit: dict) -> float:
    """Score rule 15712: red/wedding/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15713(outfit: dict) -> float:
    """Score rule 15713: navy/date/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15714(outfit: dict) -> float:
    """Score rule 15714: cream/casual/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15715(outfit: dict) -> float:
    """Score rule 15715: black/party/winter/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15716(outfit: dict) -> float:
    """Score rule 15716: blue/sport/winter/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15717(outfit: dict) -> float:
    """Score rule 15717: yellow/outdoor/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15718(outfit: dict) -> float:
    """Score rule 15718: burgundy/work/winter/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15719(outfit: dict) -> float:
    """Score rule 15719: pink/sport/winter/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15720(outfit: dict) -> float:
    """Score rule 15720: beige/outdoor/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15721(outfit: dict) -> float:
    """Score rule 15721: red/work/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15722(outfit: dict) -> float:
    """Score rule 15722: white/travel/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15723(outfit: dict) -> float:
    """Score rule 15723: brown/festival/spring/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15724(outfit: dict) -> float:
    """Score rule 15724: orange/formal/spring/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15725(outfit: dict) -> float:
    """Score rule 15725: gray/wedding/summer/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15726(outfit: dict) -> float:
    """Score rule 15726: purple/date/summer/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15727(outfit: dict) -> float:
    """Score rule 15727: olive/casual/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15728(outfit: dict) -> float:
    """Score rule 15728: green/party/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15729(outfit: dict) -> float:
    """Score rule 15729: navy/sport/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15730(outfit: dict) -> float:
    """Score rule 15730: cream/casual/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15731(outfit: dict) -> float:
    """Score rule 15731: black/party/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15732(outfit: dict) -> float:
    """Score rule 15732: brown/sport/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15733(outfit: dict) -> float:
    """Score rule 15733: orange/outdoor/autumn/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15734(outfit: dict) -> float:
    """Score rule 15734: gray/work/autumn/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15735(outfit: dict) -> float:
    """Score rule 15735: purple/travel/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15736(outfit: dict) -> float:
    """Score rule 15736: olive/festival/winter/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15737(outfit: dict) -> float:
    """Score rule 15737: green/formal/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15738(outfit: dict) -> float:
    """Score rule 15738: navy/wedding/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15739(outfit: dict) -> float:
    """Score rule 15739: cream/date/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15740(outfit: dict) -> float:
    """Score rule 15740: black/casual/spring/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15741(outfit: dict) -> float:
    """Score rule 15741: blue/wedding/spring/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15742(outfit: dict) -> float:
    """Score rule 15742: yellow/date/spring/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15743(outfit: dict) -> float:
    """Score rule 15743: burgundy/casual/spring/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15744(outfit: dict) -> float:
    """Score rule 15744: pink/party/spring/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15745(outfit: dict) -> float:
    """Score rule 15745: beige/sport/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15746(outfit: dict) -> float:
    """Score rule 15746: red/outdoor/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15747(outfit: dict) -> float:
    """Score rule 15747: white/work/summer/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15748(outfit: dict) -> float:
    """Score rule 15748: brown/travel/summer/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15749(outfit: dict) -> float:
    """Score rule 15749: orange/festival/summer/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15750(outfit: dict) -> float:
    """Score rule 15750: gray/formal/autumn/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15751(outfit: dict) -> float:
    """Score rule 15751: yellow/wedding/autumn/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15752(outfit: dict) -> float:
    """Score rule 15752: burgundy/festival/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15753(outfit: dict) -> float:
    """Score rule 15753: pink/formal/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15754(outfit: dict) -> float:
    """Score rule 15754: beige/wedding/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15755(outfit: dict) -> float:
    """Score rule 15755: red/date/winter/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15756(outfit: dict) -> float:
    """Score rule 15756: white/casual/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15757(outfit: dict) -> float:
    """Score rule 15757: brown/party/winter/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15758(outfit: dict) -> float:
    """Score rule 15758: orange/sport/winter/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15759(outfit: dict) -> float:
    """Score rule 15759: gray/outdoor/winter/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15760(outfit: dict) -> float:
    """Score rule 15760: purple/work/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15761(outfit: dict) -> float:
    """Score rule 15761: olive/travel/spring/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15762(outfit: dict) -> float:
    """Score rule 15762: green/festival/spring/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15763(outfit: dict) -> float:
    """Score rule 15763: navy/work/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15764(outfit: dict) -> float:
    """Score rule 15764: cream/travel/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15765(outfit: dict) -> float:
    """Score rule 15765: black/festival/summer/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15766(outfit: dict) -> float:
    """Score rule 15766: blue/formal/summer/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15767(outfit: dict) -> float:
    """Score rule 15767: yellow/wedding/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15768(outfit: dict) -> float:
    """Score rule 15768: burgundy/date/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15769(outfit: dict) -> float:
    """Score rule 15769: pink/casual/summer/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15770(outfit: dict) -> float:
    """Score rule 15770: olive/party/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15771(outfit: dict) -> float:
    """Score rule 15771: green/sport/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15772(outfit: dict) -> float:
    """Score rule 15772: navy/outdoor/autumn/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15773(outfit: dict) -> float:
    """Score rule 15773: cream/work/autumn/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15774(outfit: dict) -> float:
    """Score rule 15774: black/sport/autumn/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15775(outfit: dict) -> float:
    """Score rule 15775: blue/outdoor/winter/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15776(outfit: dict) -> float:
    """Score rule 15776: yellow/work/winter/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15777(outfit: dict) -> float:
    """Score rule 15777: burgundy/travel/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15778(outfit: dict) -> float:
    """Score rule 15778: pink/festival/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15779(outfit: dict) -> float:
    """Score rule 15779: beige/formal/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15780(outfit: dict) -> float:
    """Score rule 15780: red/wedding/spring/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15781(outfit: dict) -> float:
    """Score rule 15781: white/date/spring/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15782(outfit: dict) -> float:
    """Score rule 15782: brown/casual/spring/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15783(outfit: dict) -> float:
    """Score rule 15783: orange/party/spring/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15784(outfit: dict) -> float:
    """Score rule 15784: gray/sport/spring/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15785(outfit: dict) -> float:
    """Score rule 15785: purple/casual/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15786(outfit: dict) -> float:
    """Score rule 15786: olive/party/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15787(outfit: dict) -> float:
    """Score rule 15787: green/sport/summer/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15788(outfit: dict) -> float:
    """Score rule 15788: navy/outdoor/summer/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15789(outfit: dict) -> float:
    """Score rule 15789: red/work/summer/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15790(outfit: dict) -> float:
    """Score rule 15790: white/travel/autumn/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15791(outfit: dict) -> float:
    """Score rule 15791: brown/festival/autumn/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15792(outfit: dict) -> float:
    """Score rule 15792: orange/formal/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15793(outfit: dict) -> float:
    """Score rule 15793: gray/wedding/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15794(outfit: dict) -> float:
    """Score rule 15794: purple/date/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15795(outfit: dict) -> float:
    """Score rule 15795: olive/casual/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15796(outfit: dict) -> float:
    """Score rule 15796: green/wedding/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15797(outfit: dict) -> float:
    """Score rule 15797: navy/date/winter/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15798(outfit: dict) -> float:
    """Score rule 15798: cream/casual/winter/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15799(outfit: dict) -> float:
    """Score rule 15799: black/party/winter/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15800(outfit: dict) -> float:
    """Score rule 15800: blue/sport/spring/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15801(outfit: dict) -> float:
    """Score rule 15801: yellow/outdoor/spring/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15802(outfit: dict) -> float:
    """Score rule 15802: burgundy/work/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15803(outfit: dict) -> float:
    """Score rule 15803: pink/travel/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15804(outfit: dict) -> float:
    """Score rule 15804: beige/festival/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15805(outfit: dict) -> float:
    """Score rule 15805: red/formal/summer/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15806(outfit: dict) -> float:
    """Score rule 15806: white/wedding/summer/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15807(outfit: dict) -> float:
    """Score rule 15807: brown/festival/summer/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15808(outfit: dict) -> float:
    """Score rule 15808: black/formal/summer/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15809(outfit: dict) -> float:
    """Score rule 15809: blue/wedding/summer/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15810(outfit: dict) -> float:
    """Score rule 15810: yellow/date/autumn/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15811(outfit: dict) -> float:
    """Score rule 15811: burgundy/casual/autumn/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15812(outfit: dict) -> float:
    """Score rule 15812: pink/party/autumn/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15813(outfit: dict) -> float:
    """Score rule 15813: beige/sport/autumn/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15814(outfit: dict) -> float:
    """Score rule 15814: red/outdoor/autumn/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15815(outfit: dict) -> float:
    """Score rule 15815: white/work/winter/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15816(outfit: dict) -> float:
    """Score rule 15816: brown/travel/winter/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15817(outfit: dict) -> float:
    """Score rule 15817: orange/festival/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15818(outfit: dict) -> float:
    """Score rule 15818: gray/work/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15819(outfit: dict) -> float:
    """Score rule 15819: purple/travel/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15820(outfit: dict) -> float:
    """Score rule 15820: olive/festival/spring/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15821(outfit: dict) -> float:
    """Score rule 15821: green/formal/spring/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15822(outfit: dict) -> float:
    """Score rule 15822: navy/wedding/spring/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15823(outfit: dict) -> float:
    """Score rule 15823: cream/date/spring/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15824(outfit: dict) -> float:
    """Score rule 15824: black/casual/spring/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15825(outfit: dict) -> float:
    """Score rule 15825: blue/party/summer/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15826(outfit: dict) -> float:
    """Score rule 15826: yellow/sport/summer/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15827(outfit: dict) -> float:
    """Score rule 15827: gray/outdoor/summer/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15828(outfit: dict) -> float:
    """Score rule 15828: purple/work/summer/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15829(outfit: dict) -> float:
    """Score rule 15829: olive/sport/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15830(outfit: dict) -> float:
    """Score rule 15830: green/outdoor/autumn/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15831(outfit: dict) -> float:
    """Score rule 15831: navy/work/autumn/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15832(outfit: dict) -> float:
    """Score rule 15832: cream/travel/autumn/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15833(outfit: dict) -> float:
    """Score rule 15833: black/festival/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15834(outfit: dict) -> float:
    """Score rule 15834: blue/formal/autumn/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15835(outfit: dict) -> float:
    """Score rule 15835: yellow/wedding/winter/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15836(outfit: dict) -> float:
    """Score rule 15836: burgundy/date/winter/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15837(outfit: dict) -> float:
    """Score rule 15837: pink/casual/winter/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15838(outfit: dict) -> float:
    """Score rule 15838: beige/party/winter/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15839(outfit: dict) -> float:
    """Score rule 15839: red/sport/winter/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15840(outfit: dict) -> float:
    """Score rule 15840: white/casual/spring/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15841(outfit: dict) -> float:
    """Score rule 15841: brown/party/spring/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15842(outfit: dict) -> float:
    """Score rule 15842: orange/sport/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15843(outfit: dict) -> float:
    """Score rule 15843: gray/outdoor/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15844(outfit: dict) -> float:
    """Score rule 15844: purple/work/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15845(outfit: dict) -> float:
    """Score rule 15845: olive/travel/summer/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15846(outfit: dict) -> float:
    """Score rule 15846: pink/festival/summer/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15847(outfit: dict) -> float:
    """Score rule 15847: beige/formal/summer/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15848(outfit: dict) -> float:
    """Score rule 15848: red/wedding/summer/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15849(outfit: dict) -> float:
    """Score rule 15849: white/date/summer/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15850(outfit: dict) -> float:
    """Score rule 15850: brown/casual/autumn/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15851(outfit: dict) -> float:
    """Score rule 15851: orange/wedding/autumn/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15852(outfit: dict) -> float:
    """Score rule 15852: gray/date/autumn/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15853(outfit: dict) -> float:
    """Score rule 15853: purple/casual/autumn/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15854(outfit: dict) -> float:
    """Score rule 15854: olive/party/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15855(outfit: dict) -> float:
    """Score rule 15855: green/sport/winter/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15856(outfit: dict) -> float:
    """Score rule 15856: navy/outdoor/winter/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15857(outfit: dict) -> float:
    """Score rule 15857: cream/work/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15858(outfit: dict) -> float:
    """Score rule 15858: black/travel/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15859(outfit: dict) -> float:
    """Score rule 15859: blue/festival/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15860(outfit: dict) -> float:
    """Score rule 15860: yellow/formal/spring/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15861(outfit: dict) -> float:
    """Score rule 15861: burgundy/wedding/spring/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15862(outfit: dict) -> float:
    """Score rule 15862: pink/festival/spring/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15863(outfit: dict) -> float:
    """Score rule 15863: beige/formal/spring/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15864(outfit: dict) -> float:
    """Score rule 15864: red/wedding/spring/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15865(outfit: dict) -> float:
    """Score rule 15865: navy/date/summer/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15866(outfit: dict) -> float:
    """Score rule 15866: cream/casual/summer/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15867(outfit: dict) -> float:
    """Score rule 15867: black/party/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15868(outfit: dict) -> float:
    """Score rule 15868: blue/sport/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15869(outfit: dict) -> float:
    """Score rule 15869: yellow/outdoor/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15870(outfit: dict) -> float:
    """Score rule 15870: burgundy/work/autumn/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15871(outfit: dict) -> float:
    """Score rule 15871: pink/travel/autumn/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15872(outfit: dict) -> float:
    """Score rule 15872: beige/festival/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15873(outfit: dict) -> float:
    """Score rule 15873: red/work/autumn/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15874(outfit: dict) -> float:
    """Score rule 15874: white/travel/autumn/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15875(outfit: dict) -> float:
    """Score rule 15875: brown/festival/winter/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15876(outfit: dict) -> float:
    """Score rule 15876: orange/formal/winter/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15877(outfit: dict) -> float:
    """Score rule 15877: gray/wedding/winter/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15878(outfit: dict) -> float:
    """Score rule 15878: purple/date/winter/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15879(outfit: dict) -> float:
    """Score rule 15879: olive/casual/winter/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15880(outfit: dict) -> float:
    """Score rule 15880: green/party/spring/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15881(outfit: dict) -> float:
    """Score rule 15881: navy/sport/spring/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15882(outfit: dict) -> float:
    """Score rule 15882: cream/outdoor/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15883(outfit: dict) -> float:
    """Score rule 15883: black/work/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15884(outfit: dict) -> float:
    """Score rule 15884: brown/sport/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15885(outfit: dict) -> float:
    """Score rule 15885: orange/outdoor/summer/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15886(outfit: dict) -> float:
    """Score rule 15886: gray/work/summer/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15887(outfit: dict) -> float:
    """Score rule 15887: purple/travel/summer/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15888(outfit: dict) -> float:
    """Score rule 15888: olive/festival/summer/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15889(outfit: dict) -> float:
    """Score rule 15889: green/formal/summer/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15890(outfit: dict) -> float:
    """Score rule 15890: navy/wedding/autumn/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15891(outfit: dict) -> float:
    """Score rule 15891: cream/date/autumn/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15892(outfit: dict) -> float:
    """Score rule 15892: black/casual/autumn/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15893(outfit: dict) -> float:
    """Score rule 15893: blue/party/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15894(outfit: dict) -> float:
    """Score rule 15894: yellow/sport/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15895(outfit: dict) -> float:
    """Score rule 15895: burgundy/casual/winter/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15896(outfit: dict) -> float:
    """Score rule 15896: pink/party/winter/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15897(outfit: dict) -> float:
    """Score rule 15897: beige/sport/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15898(outfit: dict) -> float:
    """Score rule 15898: red/outdoor/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15899(outfit: dict) -> float:
    """Score rule 15899: white/work/winter/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15900(outfit: dict) -> float:
    """Score rule 15900: brown/travel/spring/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15901(outfit: dict) -> float:
    """Score rule 15901: orange/festival/spring/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15902(outfit: dict) -> float:
    """Score rule 15902: gray/formal/spring/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15903(outfit: dict) -> float:
    """Score rule 15903: yellow/wedding/spring/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15904(outfit: dict) -> float:
    """Score rule 15904: burgundy/date/spring/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15905(outfit: dict) -> float:
    """Score rule 15905: pink/casual/summer/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15906(outfit: dict) -> float:
    """Score rule 15906: beige/wedding/summer/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15907(outfit: dict) -> float:
    """Score rule 15907: red/date/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15908(outfit: dict) -> float:
    """Score rule 15908: white/casual/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15909(outfit: dict) -> float:
    """Score rule 15909: brown/party/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15910(outfit: dict) -> float:
    """Score rule 15910: orange/sport/autumn/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15911(outfit: dict) -> float:
    """Score rule 15911: gray/outdoor/autumn/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15912(outfit: dict) -> float:
    """Score rule 15912: purple/work/autumn/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15913(outfit: dict) -> float:
    """Score rule 15913: olive/travel/autumn/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15914(outfit: dict) -> float:
    """Score rule 15914: green/festival/autumn/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15915(outfit: dict) -> float:
    """Score rule 15915: navy/formal/winter/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15916(outfit: dict) -> float:
    """Score rule 15916: cream/wedding/winter/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15917(outfit: dict) -> float:
    """Score rule 15917: black/festival/winter/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15918(outfit: dict) -> float:
    """Score rule 15918: blue/formal/winter/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15919(outfit: dict) -> float:
    """Score rule 15919: yellow/wedding/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15920(outfit: dict) -> float:
    """Score rule 15920: burgundy/date/spring/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15921(outfit: dict) -> float:
    """Score rule 15921: pink/casual/spring/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15922(outfit: dict) -> float:
    """Score rule 15922: olive/party/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15923(outfit: dict) -> float:
    """Score rule 15923: green/sport/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15924(outfit: dict) -> float:
    """Score rule 15924: navy/outdoor/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15925(outfit: dict) -> float:
    """Score rule 15925: cream/work/summer/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15926(outfit: dict) -> float:
    """Score rule 15926: black/travel/summer/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15927(outfit: dict) -> float:
    """Score rule 15927: blue/festival/summer/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15928(outfit: dict) -> float:
    """Score rule 15928: yellow/work/summer/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15929(outfit: dict) -> float:
    """Score rule 15929: burgundy/travel/summer/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15930(outfit: dict) -> float:
    """Score rule 15930: pink/festival/autumn/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15931(outfit: dict) -> float:
    """Score rule 15931: beige/formal/autumn/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15932(outfit: dict) -> float:
    """Score rule 15932: red/wedding/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15933(outfit: dict) -> float:
    """Score rule 15933: white/date/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15934(outfit: dict) -> float:
    """Score rule 15934: brown/casual/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15935(outfit: dict) -> float:
    """Score rule 15935: orange/party/winter/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15936(outfit: dict) -> float:
    """Score rule 15936: gray/sport/winter/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15937(outfit: dict) -> float:
    """Score rule 15937: purple/outdoor/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15938(outfit: dict) -> float:
    """Score rule 15938: olive/work/winter/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15939(outfit: dict) -> float:
    """Score rule 15939: green/sport/winter/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15940(outfit: dict) -> float:
    """Score rule 15940: navy/outdoor/spring/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15941(outfit: dict) -> float:
    """Score rule 15941: red/work/spring/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15942(outfit: dict) -> float:
    """Score rule 15942: white/travel/spring/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15943(outfit: dict) -> float:
    """Score rule 15943: brown/festival/spring/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15944(outfit: dict) -> float:
    """Score rule 15944: orange/formal/spring/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15945(outfit: dict) -> float:
    """Score rule 15945: gray/wedding/summer/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15946(outfit: dict) -> float:
    """Score rule 15946: purple/date/summer/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15947(outfit: dict) -> float:
    """Score rule 15947: olive/casual/summer/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15948(outfit: dict) -> float:
    """Score rule 15948: green/party/summer/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15949(outfit: dict) -> float:
    """Score rule 15949: navy/sport/summer/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15950(outfit: dict) -> float:
    """Score rule 15950: cream/casual/autumn/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15951(outfit: dict) -> float:
    """Score rule 15951: black/party/autumn/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15952(outfit: dict) -> float:
    """Score rule 15952: blue/sport/autumn/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15953(outfit: dict) -> float:
    """Score rule 15953: yellow/outdoor/autumn/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15954(outfit: dict) -> float:
    """Score rule 15954: burgundy/work/autumn/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15955(outfit: dict) -> float:
    """Score rule 15955: pink/travel/winter/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15956(outfit: dict) -> float:
    """Score rule 15956: beige/festival/winter/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15957(outfit: dict) -> float:
    """Score rule 15957: red/formal/winter/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15958(outfit: dict) -> float:
    """Score rule 15958: white/wedding/winter/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15959(outfit: dict) -> float:
    """Score rule 15959: brown/date/winter/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15960(outfit: dict) -> float:
    """Score rule 15960: black/casual/spring/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15961(outfit: dict) -> float:
    """Score rule 15961: blue/wedding/spring/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15962(outfit: dict) -> float:
    """Score rule 15962: yellow/date/spring/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15963(outfit: dict) -> float:
    """Score rule 15963: burgundy/casual/spring/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15964(outfit: dict) -> float:
    """Score rule 15964: pink/party/spring/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15965(outfit: dict) -> float:
    """Score rule 15965: beige/sport/summer/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15966(outfit: dict) -> float:
    """Score rule 15966: red/outdoor/summer/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15967(outfit: dict) -> float:
    """Score rule 15967: white/work/summer/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15968(outfit: dict) -> float:
    """Score rule 15968: brown/travel/summer/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15969(outfit: dict) -> float:
    """Score rule 15969: orange/festival/summer/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15970(outfit: dict) -> float:
    """Score rule 15970: gray/formal/autumn/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15971(outfit: dict) -> float:
    """Score rule 15971: purple/wedding/autumn/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15972(outfit: dict) -> float:
    """Score rule 15972: olive/festival/autumn/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15973(outfit: dict) -> float:
    """Score rule 15973: green/formal/autumn/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15974(outfit: dict) -> float:
    """Score rule 15974: navy/wedding/autumn/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15975(outfit: dict) -> float:
    """Score rule 15975: cream/date/winter/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15976(outfit: dict) -> float:
    """Score rule 15976: black/casual/winter/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15977(outfit: dict) -> float:
    """Score rule 15977: blue/party/winter/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15978(outfit: dict) -> float:
    """Score rule 15978: yellow/sport/winter/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15979(outfit: dict) -> float:
    """Score rule 15979: gray/outdoor/winter/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15980(outfit: dict) -> float:
    """Score rule 15980: purple/work/spring/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15981(outfit: dict) -> float:
    """Score rule 15981: olive/travel/spring/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15982(outfit: dict) -> float:
    """Score rule 15982: green/festival/spring/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15983(outfit: dict) -> float:
    """Score rule 15983: navy/work/spring/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15984(outfit: dict) -> float:
    """Score rule 15984: cream/travel/spring/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15985(outfit: dict) -> float:
    """Score rule 15985: black/festival/summer/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15986(outfit: dict) -> float:
    """Score rule 15986: blue/formal/summer/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15987(outfit: dict) -> float:
    """Score rule 15987: yellow/wedding/summer/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15988(outfit: dict) -> float:
    """Score rule 15988: burgundy/date/summer/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15989(outfit: dict) -> float:
    """Score rule 15989: pink/casual/summer/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15990(outfit: dict) -> float:
    """Score rule 15990: beige/party/autumn/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15991(outfit: dict) -> float:
    """Score rule 15991: red/sport/autumn/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15992(outfit: dict) -> float:
    """Score rule 15992: white/outdoor/autumn/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15993(outfit: dict) -> float:
    """Score rule 15993: brown/work/autumn/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15994(outfit: dict) -> float:
    """Score rule 15994: orange/sport/autumn/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15995(outfit: dict) -> float:
    """Score rule 15995: gray/outdoor/winter/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15996(outfit: dict) -> float:
    """Score rule 15996: purple/work/winter/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15997(outfit: dict) -> float:
    """Score rule 15997: olive/travel/winter/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15998(outfit: dict) -> float:
    """Score rule 15998: pink/festival/winter/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_15999(outfit: dict) -> float:
    """Score rule 15999: beige/formal/winter/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

