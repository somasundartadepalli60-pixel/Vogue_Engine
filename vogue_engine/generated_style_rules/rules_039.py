"""Generated local outfit scoring rules, partition 39."""

def score_19500(outfit: dict) -> float:
    """Score rule 19500: gray/work/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19501(outfit: dict) -> float:
    """Score rule 19501: purple/travel/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19502(outfit: dict) -> float:
    """Score rule 19502: olive/festival/spring/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19503(outfit: dict) -> float:
    """Score rule 19503: green/work/spring/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19504(outfit: dict) -> float:
    """Score rule 19504: navy/travel/spring/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19505(outfit: dict) -> float:
    """Score rule 19505: cream/festival/summer/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19506(outfit: dict) -> float:
    """Score rule 19506: black/formal/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19507(outfit: dict) -> float:
    """Score rule 19507: blue/wedding/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19508(outfit: dict) -> float:
    """Score rule 19508: yellow/date/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19509(outfit: dict) -> float:
    """Score rule 19509: burgundy/casual/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19510(outfit: dict) -> float:
    """Score rule 19510: pink/party/autumn/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19511(outfit: dict) -> float:
    """Score rule 19511: beige/sport/autumn/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19512(outfit: dict) -> float:
    """Score rule 19512: red/outdoor/autumn/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19513(outfit: dict) -> float:
    """Score rule 19513: navy/work/autumn/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19514(outfit: dict) -> float:
    """Score rule 19514: cream/sport/autumn/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19515(outfit: dict) -> float:
    """Score rule 19515: black/outdoor/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19516(outfit: dict) -> float:
    """Score rule 19516: blue/work/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19517(outfit: dict) -> float:
    """Score rule 19517: yellow/travel/winter/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19518(outfit: dict) -> float:
    """Score rule 19518: burgundy/festival/winter/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19519(outfit: dict) -> float:
    """Score rule 19519: pink/formal/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19520(outfit: dict) -> float:
    """Score rule 19520: beige/wedding/spring/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19521(outfit: dict) -> float:
    """Score rule 19521: red/date/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19522(outfit: dict) -> float:
    """Score rule 19522: white/casual/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19523(outfit: dict) -> float:
    """Score rule 19523: brown/party/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19524(outfit: dict) -> float:
    """Score rule 19524: orange/sport/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19525(outfit: dict) -> float:
    """Score rule 19525: gray/casual/summer/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19526(outfit: dict) -> float:
    """Score rule 19526: purple/party/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19527(outfit: dict) -> float:
    """Score rule 19527: olive/sport/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19528(outfit: dict) -> float:
    """Score rule 19528: green/outdoor/summer/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19529(outfit: dict) -> float:
    """Score rule 19529: navy/work/summer/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19530(outfit: dict) -> float:
    """Score rule 19530: cream/travel/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19531(outfit: dict) -> float:
    """Score rule 19531: black/festival/autumn/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19532(outfit: dict) -> float:
    """Score rule 19532: brown/formal/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19533(outfit: dict) -> float:
    """Score rule 19533: orange/wedding/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19534(outfit: dict) -> float:
    """Score rule 19534: gray/date/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19535(outfit: dict) -> float:
    """Score rule 19535: purple/casual/winter/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19536(outfit: dict) -> float:
    """Score rule 19536: olive/wedding/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19537(outfit: dict) -> float:
    """Score rule 19537: green/date/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19538(outfit: dict) -> float:
    """Score rule 19538: navy/casual/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19539(outfit: dict) -> float:
    """Score rule 19539: cream/party/winter/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19540(outfit: dict) -> float:
    """Score rule 19540: black/sport/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19541(outfit: dict) -> float:
    """Score rule 19541: blue/outdoor/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19542(outfit: dict) -> float:
    """Score rule 19542: yellow/work/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19543(outfit: dict) -> float:
    """Score rule 19543: burgundy/travel/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19544(outfit: dict) -> float:
    """Score rule 19544: pink/festival/spring/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19545(outfit: dict) -> float:
    """Score rule 19545: beige/formal/summer/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19546(outfit: dict) -> float:
    """Score rule 19546: red/wedding/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19547(outfit: dict) -> float:
    """Score rule 19547: white/festival/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19548(outfit: dict) -> float:
    """Score rule 19548: brown/formal/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19549(outfit: dict) -> float:
    """Score rule 19549: orange/wedding/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19550(outfit: dict) -> float:
    """Score rule 19550: gray/date/autumn/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19551(outfit: dict) -> float:
    """Score rule 19551: yellow/casual/autumn/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19552(outfit: dict) -> float:
    """Score rule 19552: burgundy/party/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19553(outfit: dict) -> float:
    """Score rule 19553: pink/sport/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19554(outfit: dict) -> float:
    """Score rule 19554: beige/outdoor/autumn/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19555(outfit: dict) -> float:
    """Score rule 19555: red/work/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19556(outfit: dict) -> float:
    """Score rule 19556: white/travel/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19557(outfit: dict) -> float:
    """Score rule 19557: brown/festival/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19558(outfit: dict) -> float:
    """Score rule 19558: orange/work/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19559(outfit: dict) -> float:
    """Score rule 19559: gray/travel/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19560(outfit: dict) -> float:
    """Score rule 19560: purple/festival/spring/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19561(outfit: dict) -> float:
    """Score rule 19561: olive/formal/spring/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19562(outfit: dict) -> float:
    """Score rule 19562: green/wedding/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19563(outfit: dict) -> float:
    """Score rule 19563: navy/date/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19564(outfit: dict) -> float:
    """Score rule 19564: cream/casual/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19565(outfit: dict) -> float:
    """Score rule 19565: black/party/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19566(outfit: dict) -> float:
    """Score rule 19566: blue/sport/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19567(outfit: dict) -> float:
    """Score rule 19567: yellow/outdoor/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19568(outfit: dict) -> float:
    """Score rule 19568: burgundy/work/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19569(outfit: dict) -> float:
    """Score rule 19569: pink/sport/summer/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19570(outfit: dict) -> float:
    """Score rule 19570: olive/outdoor/autumn/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19571(outfit: dict) -> float:
    """Score rule 19571: green/work/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19572(outfit: dict) -> float:
    """Score rule 19572: navy/travel/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19573(outfit: dict) -> float:
    """Score rule 19573: cream/festival/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19574(outfit: dict) -> float:
    """Score rule 19574: black/formal/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19575(outfit: dict) -> float:
    """Score rule 19575: blue/wedding/winter/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19576(outfit: dict) -> float:
    """Score rule 19576: yellow/date/winter/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19577(outfit: dict) -> float:
    """Score rule 19577: burgundy/casual/winter/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19578(outfit: dict) -> float:
    """Score rule 19578: pink/party/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19579(outfit: dict) -> float:
    """Score rule 19579: beige/sport/winter/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19580(outfit: dict) -> float:
    """Score rule 19580: red/casual/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19581(outfit: dict) -> float:
    """Score rule 19581: white/party/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19582(outfit: dict) -> float:
    """Score rule 19582: brown/sport/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19583(outfit: dict) -> float:
    """Score rule 19583: orange/outdoor/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19584(outfit: dict) -> float:
    """Score rule 19584: gray/work/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19585(outfit: dict) -> float:
    """Score rule 19585: purple/travel/summer/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19586(outfit: dict) -> float:
    """Score rule 19586: olive/festival/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19587(outfit: dict) -> float:
    """Score rule 19587: green/formal/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19588(outfit: dict) -> float:
    """Score rule 19588: navy/wedding/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19589(outfit: dict) -> float:
    """Score rule 19589: red/date/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19590(outfit: dict) -> float:
    """Score rule 19590: white/casual/autumn/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19591(outfit: dict) -> float:
    """Score rule 19591: brown/wedding/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19592(outfit: dict) -> float:
    """Score rule 19592: orange/date/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19593(outfit: dict) -> float:
    """Score rule 19593: gray/casual/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19594(outfit: dict) -> float:
    """Score rule 19594: purple/party/autumn/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19595(outfit: dict) -> float:
    """Score rule 19595: olive/sport/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19596(outfit: dict) -> float:
    """Score rule 19596: green/outdoor/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19597(outfit: dict) -> float:
    """Score rule 19597: navy/work/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19598(outfit: dict) -> float:
    """Score rule 19598: cream/travel/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19599(outfit: dict) -> float:
    """Score rule 19599: black/festival/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19600(outfit: dict) -> float:
    """Score rule 19600: blue/formal/spring/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19601(outfit: dict) -> float:
    """Score rule 19601: yellow/wedding/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19602(outfit: dict) -> float:
    """Score rule 19602: burgundy/festival/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19603(outfit: dict) -> float:
    """Score rule 19603: pink/formal/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19604(outfit: dict) -> float:
    """Score rule 19604: beige/wedding/spring/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19605(outfit: dict) -> float:
    """Score rule 19605: red/date/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19606(outfit: dict) -> float:
    """Score rule 19606: white/casual/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19607(outfit: dict) -> float:
    """Score rule 19607: brown/party/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19608(outfit: dict) -> float:
    """Score rule 19608: black/sport/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19609(outfit: dict) -> float:
    """Score rule 19609: blue/outdoor/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19610(outfit: dict) -> float:
    """Score rule 19610: yellow/work/autumn/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19611(outfit: dict) -> float:
    """Score rule 19611: burgundy/travel/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19612(outfit: dict) -> float:
    """Score rule 19612: pink/festival/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19613(outfit: dict) -> float:
    """Score rule 19613: beige/work/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19614(outfit: dict) -> float:
    """Score rule 19614: red/travel/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19615(outfit: dict) -> float:
    """Score rule 19615: white/festival/winter/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19616(outfit: dict) -> float:
    """Score rule 19616: brown/formal/winter/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19617(outfit: dict) -> float:
    """Score rule 19617: orange/wedding/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19618(outfit: dict) -> float:
    """Score rule 19618: gray/date/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19619(outfit: dict) -> float:
    """Score rule 19619: purple/casual/winter/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19620(outfit: dict) -> float:
    """Score rule 19620: olive/party/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19621(outfit: dict) -> float:
    """Score rule 19621: green/sport/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19622(outfit: dict) -> float:
    """Score rule 19622: navy/outdoor/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19623(outfit: dict) -> float:
    """Score rule 19623: cream/work/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19624(outfit: dict) -> float:
    """Score rule 19624: black/sport/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19625(outfit: dict) -> float:
    """Score rule 19625: blue/outdoor/summer/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19626(outfit: dict) -> float:
    """Score rule 19626: yellow/work/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19627(outfit: dict) -> float:
    """Score rule 19627: gray/travel/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19628(outfit: dict) -> float:
    """Score rule 19628: purple/festival/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19629(outfit: dict) -> float:
    """Score rule 19629: olive/formal/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19630(outfit: dict) -> float:
    """Score rule 19630: green/wedding/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19631(outfit: dict) -> float:
    """Score rule 19631: navy/date/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19632(outfit: dict) -> float:
    """Score rule 19632: cream/casual/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19633(outfit: dict) -> float:
    """Score rule 19633: black/party/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19634(outfit: dict) -> float:
    """Score rule 19634: blue/sport/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19635(outfit: dict) -> float:
    """Score rule 19635: yellow/casual/winter/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19636(outfit: dict) -> float:
    """Score rule 19636: burgundy/party/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19637(outfit: dict) -> float:
    """Score rule 19637: pink/sport/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19638(outfit: dict) -> float:
    """Score rule 19638: beige/outdoor/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19639(outfit: dict) -> float:
    """Score rule 19639: red/work/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19640(outfit: dict) -> float:
    """Score rule 19640: white/travel/spring/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19641(outfit: dict) -> float:
    """Score rule 19641: brown/festival/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19642(outfit: dict) -> float:
    """Score rule 19642: orange/formal/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19643(outfit: dict) -> float:
    """Score rule 19643: gray/wedding/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19644(outfit: dict) -> float:
    """Score rule 19644: purple/date/spring/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19645(outfit: dict) -> float:
    """Score rule 19645: olive/casual/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19646(outfit: dict) -> float:
    """Score rule 19646: pink/wedding/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19647(outfit: dict) -> float:
    """Score rule 19647: beige/date/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19648(outfit: dict) -> float:
    """Score rule 19648: red/casual/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19649(outfit: dict) -> float:
    """Score rule 19649: white/party/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19650(outfit: dict) -> float:
    """Score rule 19650: brown/sport/autumn/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19651(outfit: dict) -> float:
    """Score rule 19651: orange/outdoor/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19652(outfit: dict) -> float:
    """Score rule 19652: gray/work/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19653(outfit: dict) -> float:
    """Score rule 19653: purple/travel/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19654(outfit: dict) -> float:
    """Score rule 19654: olive/festival/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19655(outfit: dict) -> float:
    """Score rule 19655: green/formal/winter/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19656(outfit: dict) -> float:
    """Score rule 19656: navy/wedding/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19657(outfit: dict) -> float:
    """Score rule 19657: cream/festival/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19658(outfit: dict) -> float:
    """Score rule 19658: black/formal/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19659(outfit: dict) -> float:
    """Score rule 19659: blue/wedding/winter/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19660(outfit: dict) -> float:
    """Score rule 19660: yellow/date/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19661(outfit: dict) -> float:
    """Score rule 19661: burgundy/casual/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19662(outfit: dict) -> float:
    """Score rule 19662: pink/party/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19663(outfit: dict) -> float:
    """Score rule 19663: beige/sport/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19664(outfit: dict) -> float:
    """Score rule 19664: red/outdoor/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19665(outfit: dict) -> float:
    """Score rule 19665: navy/work/summer/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19666(outfit: dict) -> float:
    """Score rule 19666: cream/travel/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19667(outfit: dict) -> float:
    """Score rule 19667: black/festival/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19668(outfit: dict) -> float:
    """Score rule 19668: blue/work/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19669(outfit: dict) -> float:
    """Score rule 19669: yellow/travel/summer/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19670(outfit: dict) -> float:
    """Score rule 19670: burgundy/festival/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19671(outfit: dict) -> float:
    """Score rule 19671: pink/formal/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19672(outfit: dict) -> float:
    """Score rule 19672: beige/wedding/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19673(outfit: dict) -> float:
    """Score rule 19673: red/date/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19674(outfit: dict) -> float:
    """Score rule 19674: white/casual/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19675(outfit: dict) -> float:
    """Score rule 19675: brown/party/winter/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19676(outfit: dict) -> float:
    """Score rule 19676: orange/sport/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19677(outfit: dict) -> float:
    """Score rule 19677: gray/outdoor/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19678(outfit: dict) -> float:
    """Score rule 19678: purple/work/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19679(outfit: dict) -> float:
    """Score rule 19679: olive/sport/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19680(outfit: dict) -> float:
    """Score rule 19680: green/outdoor/spring/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19681(outfit: dict) -> float:
    """Score rule 19681: navy/work/spring/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19682(outfit: dict) -> float:
    """Score rule 19682: cream/travel/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19683(outfit: dict) -> float:
    """Score rule 19683: black/festival/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19684(outfit: dict) -> float:
    """Score rule 19684: brown/formal/spring/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19685(outfit: dict) -> float:
    """Score rule 19685: orange/wedding/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19686(outfit: dict) -> float:
    """Score rule 19686: gray/date/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19687(outfit: dict) -> float:
    """Score rule 19687: purple/casual/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19688(outfit: dict) -> float:
    """Score rule 19688: olive/party/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19689(outfit: dict) -> float:
    """Score rule 19689: green/sport/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19690(outfit: dict) -> float:
    """Score rule 19690: navy/casual/autumn/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19691(outfit: dict) -> float:
    """Score rule 19691: cream/party/autumn/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19692(outfit: dict) -> float:
    """Score rule 19692: black/sport/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19693(outfit: dict) -> float:
    """Score rule 19693: blue/outdoor/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19694(outfit: dict) -> float:
    """Score rule 19694: yellow/work/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19695(outfit: dict) -> float:
    """Score rule 19695: burgundy/travel/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19696(outfit: dict) -> float:
    """Score rule 19696: pink/festival/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19697(outfit: dict) -> float:
    """Score rule 19697: beige/formal/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19698(outfit: dict) -> float:
    """Score rule 19698: red/wedding/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19699(outfit: dict) -> float:
    """Score rule 19699: white/date/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19700(outfit: dict) -> float:
    """Score rule 19700: brown/casual/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19701(outfit: dict) -> float:
    """Score rule 19701: orange/wedding/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19702(outfit: dict) -> float:
    """Score rule 19702: gray/date/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19703(outfit: dict) -> float:
    """Score rule 19703: yellow/casual/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19704(outfit: dict) -> float:
    """Score rule 19704: burgundy/party/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19705(outfit: dict) -> float:
    """Score rule 19705: pink/sport/summer/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19706(outfit: dict) -> float:
    """Score rule 19706: beige/outdoor/summer/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19707(outfit: dict) -> float:
    """Score rule 19707: red/work/summer/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19708(outfit: dict) -> float:
    """Score rule 19708: white/travel/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19709(outfit: dict) -> float:
    """Score rule 19709: brown/festival/summer/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19710(outfit: dict) -> float:
    """Score rule 19710: orange/formal/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19711(outfit: dict) -> float:
    """Score rule 19711: gray/wedding/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19712(outfit: dict) -> float:
    """Score rule 19712: purple/festival/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19713(outfit: dict) -> float:
    """Score rule 19713: olive/formal/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19714(outfit: dict) -> float:
    """Score rule 19714: green/wedding/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19715(outfit: dict) -> float:
    """Score rule 19715: navy/date/winter/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19716(outfit: dict) -> float:
    """Score rule 19716: cream/casual/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19717(outfit: dict) -> float:
    """Score rule 19717: black/party/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19718(outfit: dict) -> float:
    """Score rule 19718: blue/sport/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19719(outfit: dict) -> float:
    """Score rule 19719: yellow/outdoor/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19720(outfit: dict) -> float:
    """Score rule 19720: burgundy/work/spring/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19721(outfit: dict) -> float:
    """Score rule 19721: pink/travel/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19722(outfit: dict) -> float:
    """Score rule 19722: olive/festival/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19723(outfit: dict) -> float:
    """Score rule 19723: green/work/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19724(outfit: dict) -> float:
    """Score rule 19724: navy/travel/spring/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19725(outfit: dict) -> float:
    """Score rule 19725: cream/festival/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19726(outfit: dict) -> float:
    """Score rule 19726: black/formal/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19727(outfit: dict) -> float:
    """Score rule 19727: blue/wedding/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19728(outfit: dict) -> float:
    """Score rule 19728: yellow/date/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19729(outfit: dict) -> float:
    """Score rule 19729: burgundy/casual/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19730(outfit: dict) -> float:
    """Score rule 19730: pink/party/autumn/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19731(outfit: dict) -> float:
    """Score rule 19731: beige/sport/autumn/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19732(outfit: dict) -> float:
    """Score rule 19732: red/outdoor/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19733(outfit: dict) -> float:
    """Score rule 19733: white/work/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19734(outfit: dict) -> float:
    """Score rule 19734: brown/sport/autumn/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19735(outfit: dict) -> float:
    """Score rule 19735: orange/outdoor/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19736(outfit: dict) -> float:
    """Score rule 19736: gray/work/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19737(outfit: dict) -> float:
    """Score rule 19737: purple/travel/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19738(outfit: dict) -> float:
    """Score rule 19738: olive/festival/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19739(outfit: dict) -> float:
    """Score rule 19739: green/formal/winter/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19740(outfit: dict) -> float:
    """Score rule 19740: navy/wedding/spring/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19741(outfit: dict) -> float:
    """Score rule 19741: red/date/spring/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19742(outfit: dict) -> float:
    """Score rule 19742: white/casual/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19743(outfit: dict) -> float:
    """Score rule 19743: brown/party/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19744(outfit: dict) -> float:
    """Score rule 19744: orange/sport/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19745(outfit: dict) -> float:
    """Score rule 19745: gray/casual/summer/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19746(outfit: dict) -> float:
    """Score rule 19746: purple/party/summer/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19747(outfit: dict) -> float:
    """Score rule 19747: olive/sport/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19748(outfit: dict) -> float:
    """Score rule 19748: green/outdoor/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19749(outfit: dict) -> float:
    """Score rule 19749: navy/work/summer/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19750(outfit: dict) -> float:
    """Score rule 19750: cream/travel/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19751(outfit: dict) -> float:
    """Score rule 19751: black/festival/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19752(outfit: dict) -> float:
    """Score rule 19752: blue/formal/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19753(outfit: dict) -> float:
    """Score rule 19753: yellow/wedding/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19754(outfit: dict) -> float:
    """Score rule 19754: burgundy/date/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19755(outfit: dict) -> float:
    """Score rule 19755: pink/casual/winter/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19756(outfit: dict) -> float:
    """Score rule 19756: beige/wedding/winter/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19757(outfit: dict) -> float:
    """Score rule 19757: red/date/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19758(outfit: dict) -> float:
    """Score rule 19758: white/casual/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19759(outfit: dict) -> float:
    """Score rule 19759: brown/party/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19760(outfit: dict) -> float:
    """Score rule 19760: black/sport/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19761(outfit: dict) -> float:
    """Score rule 19761: blue/outdoor/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19762(outfit: dict) -> float:
    """Score rule 19762: yellow/work/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19763(outfit: dict) -> float:
    """Score rule 19763: burgundy/travel/spring/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19764(outfit: dict) -> float:
    """Score rule 19764: pink/festival/spring/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19765(outfit: dict) -> float:
    """Score rule 19765: beige/formal/summer/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19766(outfit: dict) -> float:
    """Score rule 19766: red/wedding/summer/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19767(outfit: dict) -> float:
    """Score rule 19767: white/festival/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19768(outfit: dict) -> float:
    """Score rule 19768: brown/formal/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19769(outfit: dict) -> float:
    """Score rule 19769: orange/wedding/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19770(outfit: dict) -> float:
    """Score rule 19770: gray/date/autumn/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19771(outfit: dict) -> float:
    """Score rule 19771: purple/casual/autumn/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19772(outfit: dict) -> float:
    """Score rule 19772: olive/party/autumn/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19773(outfit: dict) -> float:
    """Score rule 19773: green/sport/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19774(outfit: dict) -> float:
    """Score rule 19774: navy/outdoor/autumn/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19775(outfit: dict) -> float:
    """Score rule 19775: cream/work/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19776(outfit: dict) -> float:
    """Score rule 19776: black/travel/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19777(outfit: dict) -> float:
    """Score rule 19777: blue/festival/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19778(outfit: dict) -> float:
    """Score rule 19778: yellow/work/winter/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19779(outfit: dict) -> float:
    """Score rule 19779: gray/travel/winter/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19780(outfit: dict) -> float:
    """Score rule 19780: purple/festival/spring/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19781(outfit: dict) -> float:
    """Score rule 19781: olive/formal/spring/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19782(outfit: dict) -> float:
    """Score rule 19782: green/wedding/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19783(outfit: dict) -> float:
    """Score rule 19783: navy/date/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19784(outfit: dict) -> float:
    """Score rule 19784: cream/casual/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19785(outfit: dict) -> float:
    """Score rule 19785: black/party/summer/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19786(outfit: dict) -> float:
    """Score rule 19786: blue/sport/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19787(outfit: dict) -> float:
    """Score rule 19787: yellow/outdoor/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19788(outfit: dict) -> float:
    """Score rule 19788: burgundy/work/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19789(outfit: dict) -> float:
    """Score rule 19789: pink/sport/summer/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19790(outfit: dict) -> float:
    """Score rule 19790: beige/outdoor/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19791(outfit: dict) -> float:
    """Score rule 19791: red/work/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19792(outfit: dict) -> float:
    """Score rule 19792: white/travel/autumn/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19793(outfit: dict) -> float:
    """Score rule 19793: brown/festival/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19794(outfit: dict) -> float:
    """Score rule 19794: orange/formal/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19795(outfit: dict) -> float:
    """Score rule 19795: gray/wedding/winter/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19796(outfit: dict) -> float:
    """Score rule 19796: purple/date/winter/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19797(outfit: dict) -> float:
    """Score rule 19797: olive/casual/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19798(outfit: dict) -> float:
    """Score rule 19798: pink/party/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19799(outfit: dict) -> float:
    """Score rule 19799: beige/sport/winter/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19800(outfit: dict) -> float:
    """Score rule 19800: red/casual/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19801(outfit: dict) -> float:
    """Score rule 19801: white/party/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19802(outfit: dict) -> float:
    """Score rule 19802: brown/sport/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19803(outfit: dict) -> float:
    """Score rule 19803: orange/outdoor/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19804(outfit: dict) -> float:
    """Score rule 19804: gray/work/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19805(outfit: dict) -> float:
    """Score rule 19805: purple/travel/summer/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19806(outfit: dict) -> float:
    """Score rule 19806: olive/festival/summer/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19807(outfit: dict) -> float:
    """Score rule 19807: green/formal/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19808(outfit: dict) -> float:
    """Score rule 19808: navy/wedding/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19809(outfit: dict) -> float:
    """Score rule 19809: cream/date/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19810(outfit: dict) -> float:
    """Score rule 19810: black/casual/autumn/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19811(outfit: dict) -> float:
    """Score rule 19811: blue/wedding/autumn/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19812(outfit: dict) -> float:
    """Score rule 19812: yellow/date/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19813(outfit: dict) -> float:
    """Score rule 19813: burgundy/casual/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19814(outfit: dict) -> float:
    """Score rule 19814: pink/party/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19815(outfit: dict) -> float:
    """Score rule 19815: beige/sport/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19816(outfit: dict) -> float:
    """Score rule 19816: red/outdoor/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19817(outfit: dict) -> float:
    """Score rule 19817: navy/work/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19818(outfit: dict) -> float:
    """Score rule 19818: cream/travel/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19819(outfit: dict) -> float:
    """Score rule 19819: black/festival/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19820(outfit: dict) -> float:
    """Score rule 19820: blue/formal/spring/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19821(outfit: dict) -> float:
    """Score rule 19821: yellow/wedding/spring/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19822(outfit: dict) -> float:
    """Score rule 19822: burgundy/festival/spring/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19823(outfit: dict) -> float:
    """Score rule 19823: pink/formal/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19824(outfit: dict) -> float:
    """Score rule 19824: beige/wedding/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19825(outfit: dict) -> float:
    """Score rule 19825: red/date/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19826(outfit: dict) -> float:
    """Score rule 19826: white/casual/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19827(outfit: dict) -> float:
    """Score rule 19827: brown/party/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19828(outfit: dict) -> float:
    """Score rule 19828: orange/sport/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19829(outfit: dict) -> float:
    """Score rule 19829: gray/outdoor/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19830(outfit: dict) -> float:
    """Score rule 19830: purple/work/autumn/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19831(outfit: dict) -> float:
    """Score rule 19831: olive/travel/autumn/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19832(outfit: dict) -> float:
    """Score rule 19832: green/festival/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19833(outfit: dict) -> float:
    """Score rule 19833: navy/work/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19834(outfit: dict) -> float:
    """Score rule 19834: cream/travel/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19835(outfit: dict) -> float:
    """Score rule 19835: black/festival/winter/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19836(outfit: dict) -> float:
    """Score rule 19836: brown/formal/winter/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19837(outfit: dict) -> float:
    """Score rule 19837: orange/wedding/winter/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19838(outfit: dict) -> float:
    """Score rule 19838: gray/date/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19839(outfit: dict) -> float:
    """Score rule 19839: purple/casual/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19840(outfit: dict) -> float:
    """Score rule 19840: olive/party/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19841(outfit: dict) -> float:
    """Score rule 19841: green/sport/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19842(outfit: dict) -> float:
    """Score rule 19842: navy/outdoor/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19843(outfit: dict) -> float:
    """Score rule 19843: cream/work/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19844(outfit: dict) -> float:
    """Score rule 19844: black/sport/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19845(outfit: dict) -> float:
    """Score rule 19845: blue/outdoor/summer/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19846(outfit: dict) -> float:
    """Score rule 19846: yellow/work/summer/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19847(outfit: dict) -> float:
    """Score rule 19847: burgundy/travel/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19848(outfit: dict) -> float:
    """Score rule 19848: pink/festival/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19849(outfit: dict) -> float:
    """Score rule 19849: beige/formal/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19850(outfit: dict) -> float:
    """Score rule 19850: red/wedding/autumn/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19851(outfit: dict) -> float:
    """Score rule 19851: white/date/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19852(outfit: dict) -> float:
    """Score rule 19852: brown/casual/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19853(outfit: dict) -> float:
    """Score rule 19853: orange/party/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19854(outfit: dict) -> float:
    """Score rule 19854: gray/sport/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19855(outfit: dict) -> float:
    """Score rule 19855: yellow/casual/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19856(outfit: dict) -> float:
    """Score rule 19856: burgundy/party/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19857(outfit: dict) -> float:
    """Score rule 19857: pink/sport/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19858(outfit: dict) -> float:
    """Score rule 19858: beige/outdoor/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19859(outfit: dict) -> float:
    """Score rule 19859: red/work/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19860(outfit: dict) -> float:
    """Score rule 19860: white/travel/spring/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19861(outfit: dict) -> float:
    """Score rule 19861: brown/festival/spring/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19862(outfit: dict) -> float:
    """Score rule 19862: orange/formal/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19863(outfit: dict) -> float:
    """Score rule 19863: gray/wedding/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19864(outfit: dict) -> float:
    """Score rule 19864: purple/date/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19865(outfit: dict) -> float:
    """Score rule 19865: olive/casual/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19866(outfit: dict) -> float:
    """Score rule 19866: green/wedding/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19867(outfit: dict) -> float:
    """Score rule 19867: navy/date/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19868(outfit: dict) -> float:
    """Score rule 19868: cream/casual/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19869(outfit: dict) -> float:
    """Score rule 19869: black/party/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19870(outfit: dict) -> float:
    """Score rule 19870: blue/sport/autumn/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19871(outfit: dict) -> float:
    """Score rule 19871: yellow/outdoor/autumn/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19872(outfit: dict) -> float:
    """Score rule 19872: burgundy/work/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19873(outfit: dict) -> float:
    """Score rule 19873: pink/travel/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19874(outfit: dict) -> float:
    """Score rule 19874: olive/festival/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19875(outfit: dict) -> float:
    """Score rule 19875: green/formal/winter/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19876(outfit: dict) -> float:
    """Score rule 19876: navy/wedding/winter/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19877(outfit: dict) -> float:
    """Score rule 19877: cream/festival/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19878(outfit: dict) -> float:
    """Score rule 19878: black/formal/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19879(outfit: dict) -> float:
    """Score rule 19879: blue/wedding/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19880(outfit: dict) -> float:
    """Score rule 19880: yellow/date/spring/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19881(outfit: dict) -> float:
    """Score rule 19881: burgundy/casual/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19882(outfit: dict) -> float:
    """Score rule 19882: pink/party/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19883(outfit: dict) -> float:
    """Score rule 19883: beige/sport/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19884(outfit: dict) -> float:
    """Score rule 19884: red/outdoor/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19885(outfit: dict) -> float:
    """Score rule 19885: white/work/summer/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19886(outfit: dict) -> float:
    """Score rule 19886: brown/travel/summer/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19887(outfit: dict) -> float:
    """Score rule 19887: orange/festival/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19888(outfit: dict) -> float:
    """Score rule 19888: gray/work/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19889(outfit: dict) -> float:
    """Score rule 19889: purple/travel/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19890(outfit: dict) -> float:
    """Score rule 19890: olive/festival/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19891(outfit: dict) -> float:
    """Score rule 19891: green/formal/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19892(outfit: dict) -> float:
    """Score rule 19892: navy/wedding/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19893(outfit: dict) -> float:
    """Score rule 19893: red/date/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19894(outfit: dict) -> float:
    """Score rule 19894: white/casual/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19895(outfit: dict) -> float:
    """Score rule 19895: brown/party/winter/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19896(outfit: dict) -> float:
    """Score rule 19896: orange/sport/winter/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19897(outfit: dict) -> float:
    """Score rule 19897: gray/outdoor/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19898(outfit: dict) -> float:
    """Score rule 19898: purple/work/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19899(outfit: dict) -> float:
    """Score rule 19899: olive/sport/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19900(outfit: dict) -> float:
    """Score rule 19900: green/outdoor/spring/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19901(outfit: dict) -> float:
    """Score rule 19901: navy/work/spring/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19902(outfit: dict) -> float:
    """Score rule 19902: cream/travel/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19903(outfit: dict) -> float:
    """Score rule 19903: black/festival/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19904(outfit: dict) -> float:
    """Score rule 19904: blue/formal/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19905(outfit: dict) -> float:
    """Score rule 19905: yellow/wedding/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19906(outfit: dict) -> float:
    """Score rule 19906: burgundy/date/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19907(outfit: dict) -> float:
    """Score rule 19907: pink/casual/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19908(outfit: dict) -> float:
    """Score rule 19908: beige/party/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19909(outfit: dict) -> float:
    """Score rule 19909: red/sport/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19910(outfit: dict) -> float:
    """Score rule 19910: white/casual/autumn/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19911(outfit: dict) -> float:
    """Score rule 19911: brown/party/autumn/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19912(outfit: dict) -> float:
    """Score rule 19912: black/sport/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19913(outfit: dict) -> float:
    """Score rule 19913: blue/outdoor/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19914(outfit: dict) -> float:
    """Score rule 19914: yellow/work/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19915(outfit: dict) -> float:
    """Score rule 19915: burgundy/travel/winter/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19916(outfit: dict) -> float:
    """Score rule 19916: pink/festival/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19917(outfit: dict) -> float:
    """Score rule 19917: beige/formal/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19918(outfit: dict) -> float:
    """Score rule 19918: red/wedding/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19919(outfit: dict) -> float:
    """Score rule 19919: white/date/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19920(outfit: dict) -> float:
    """Score rule 19920: brown/casual/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19921(outfit: dict) -> float:
    """Score rule 19921: orange/wedding/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19922(outfit: dict) -> float:
    """Score rule 19922: gray/date/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19923(outfit: dict) -> float:
    """Score rule 19923: purple/casual/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19924(outfit: dict) -> float:
    """Score rule 19924: olive/party/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19925(outfit: dict) -> float:
    """Score rule 19925: green/sport/summer/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19926(outfit: dict) -> float:
    """Score rule 19926: navy/outdoor/summer/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19927(outfit: dict) -> float:
    """Score rule 19927: cream/work/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19928(outfit: dict) -> float:
    """Score rule 19928: black/travel/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19929(outfit: dict) -> float:
    """Score rule 19929: blue/festival/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19930(outfit: dict) -> float:
    """Score rule 19930: yellow/formal/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19931(outfit: dict) -> float:
    """Score rule 19931: gray/wedding/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19932(outfit: dict) -> float:
    """Score rule 19932: purple/festival/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19933(outfit: dict) -> float:
    """Score rule 19933: olive/formal/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19934(outfit: dict) -> float:
    """Score rule 19934: green/wedding/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19935(outfit: dict) -> float:
    """Score rule 19935: navy/date/winter/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19936(outfit: dict) -> float:
    """Score rule 19936: cream/casual/winter/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19937(outfit: dict) -> float:
    """Score rule 19937: black/party/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19938(outfit: dict) -> float:
    """Score rule 19938: blue/sport/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19939(outfit: dict) -> float:
    """Score rule 19939: yellow/outdoor/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19940(outfit: dict) -> float:
    """Score rule 19940: burgundy/work/spring/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19941(outfit: dict) -> float:
    """Score rule 19941: pink/travel/spring/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19942(outfit: dict) -> float:
    """Score rule 19942: beige/festival/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19943(outfit: dict) -> float:
    """Score rule 19943: red/work/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19944(outfit: dict) -> float:
    """Score rule 19944: white/travel/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19945(outfit: dict) -> float:
    """Score rule 19945: brown/festival/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19946(outfit: dict) -> float:
    """Score rule 19946: orange/formal/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19947(outfit: dict) -> float:
    """Score rule 19947: gray/wedding/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19948(outfit: dict) -> float:
    """Score rule 19948: purple/date/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19949(outfit: dict) -> float:
    """Score rule 19949: olive/casual/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19950(outfit: dict) -> float:
    """Score rule 19950: pink/party/autumn/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19951(outfit: dict) -> float:
    """Score rule 19951: beige/sport/autumn/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19952(outfit: dict) -> float:
    """Score rule 19952: red/outdoor/autumn/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19953(outfit: dict) -> float:
    """Score rule 19953: white/work/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19954(outfit: dict) -> float:
    """Score rule 19954: brown/sport/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19955(outfit: dict) -> float:
    """Score rule 19955: orange/outdoor/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19956(outfit: dict) -> float:
    """Score rule 19956: gray/work/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19957(outfit: dict) -> float:
    """Score rule 19957: purple/travel/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19958(outfit: dict) -> float:
    """Score rule 19958: olive/festival/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19959(outfit: dict) -> float:
    """Score rule 19959: green/formal/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19960(outfit: dict) -> float:
    """Score rule 19960: navy/wedding/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19961(outfit: dict) -> float:
    """Score rule 19961: cream/date/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19962(outfit: dict) -> float:
    """Score rule 19962: black/casual/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19963(outfit: dict) -> float:
    """Score rule 19963: blue/party/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19964(outfit: dict) -> float:
    """Score rule 19964: yellow/sport/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19965(outfit: dict) -> float:
    """Score rule 19965: burgundy/casual/summer/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19966(outfit: dict) -> float:
    """Score rule 19966: pink/party/summer/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19967(outfit: dict) -> float:
    """Score rule 19967: beige/sport/summer/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19968(outfit: dict) -> float:
    """Score rule 19968: red/outdoor/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19969(outfit: dict) -> float:
    """Score rule 19969: navy/work/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19970(outfit: dict) -> float:
    """Score rule 19970: cream/travel/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19971(outfit: dict) -> float:
    """Score rule 19971: black/festival/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19972(outfit: dict) -> float:
    """Score rule 19972: blue/formal/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19973(outfit: dict) -> float:
    """Score rule 19973: yellow/wedding/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19974(outfit: dict) -> float:
    """Score rule 19974: burgundy/date/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19975(outfit: dict) -> float:
    """Score rule 19975: pink/casual/winter/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19976(outfit: dict) -> float:
    """Score rule 19976: beige/wedding/winter/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19977(outfit: dict) -> float:
    """Score rule 19977: red/date/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19978(outfit: dict) -> float:
    """Score rule 19978: white/casual/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19979(outfit: dict) -> float:
    """Score rule 19979: brown/party/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19980(outfit: dict) -> float:
    """Score rule 19980: orange/sport/spring/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19981(outfit: dict) -> float:
    """Score rule 19981: gray/outdoor/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19982(outfit: dict) -> float:
    """Score rule 19982: purple/work/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19983(outfit: dict) -> float:
    """Score rule 19983: olive/travel/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19984(outfit: dict) -> float:
    """Score rule 19984: green/festival/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19985(outfit: dict) -> float:
    """Score rule 19985: navy/formal/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19986(outfit: dict) -> float:
    """Score rule 19986: cream/wedding/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19987(outfit: dict) -> float:
    """Score rule 19987: black/festival/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19988(outfit: dict) -> float:
    """Score rule 19988: brown/formal/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19989(outfit: dict) -> float:
    """Score rule 19989: orange/wedding/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19990(outfit: dict) -> float:
    """Score rule 19990: gray/date/autumn/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19991(outfit: dict) -> float:
    """Score rule 19991: purple/casual/autumn/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19992(outfit: dict) -> float:
    """Score rule 19992: olive/party/autumn/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19993(outfit: dict) -> float:
    """Score rule 19993: green/sport/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19994(outfit: dict) -> float:
    """Score rule 19994: navy/outdoor/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19995(outfit: dict) -> float:
    """Score rule 19995: cream/work/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19996(outfit: dict) -> float:
    """Score rule 19996: black/travel/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19997(outfit: dict) -> float:
    """Score rule 19997: blue/festival/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19998(outfit: dict) -> float:
    """Score rule 19998: yellow/work/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_19999(outfit: dict) -> float:
    """Score rule 19999: burgundy/travel/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

