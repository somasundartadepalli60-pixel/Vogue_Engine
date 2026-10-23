"""Generated local outfit scoring rules, partition 9."""

def score_04500(outfit: dict) -> float:
    """Score rule 4500: brown/outdoor/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04501(outfit: dict) -> float:
    """Score rule 4501: orange/work/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04502(outfit: dict) -> float:
    """Score rule 4502: gray/travel/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04503(outfit: dict) -> float:
    """Score rule 4503: yellow/festival/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04504(outfit: dict) -> float:
    """Score rule 4504: burgundy/formal/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04505(outfit: dict) -> float:
    """Score rule 4505: pink/wedding/summer/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04506(outfit: dict) -> float:
    """Score rule 4506: beige/date/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04507(outfit: dict) -> float:
    """Score rule 4507: red/casual/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04508(outfit: dict) -> float:
    """Score rule 4508: white/party/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04509(outfit: dict) -> float:
    """Score rule 4509: brown/sport/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04510(outfit: dict) -> float:
    """Score rule 4510: orange/casual/autumn/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04511(outfit: dict) -> float:
    """Score rule 4511: gray/party/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04512(outfit: dict) -> float:
    """Score rule 4512: purple/sport/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04513(outfit: dict) -> float:
    """Score rule 4513: olive/outdoor/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04514(outfit: dict) -> float:
    """Score rule 4514: green/work/autumn/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04515(outfit: dict) -> float:
    """Score rule 4515: navy/travel/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04516(outfit: dict) -> float:
    """Score rule 4516: cream/festival/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04517(outfit: dict) -> float:
    """Score rule 4517: black/formal/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04518(outfit: dict) -> float:
    """Score rule 4518: blue/wedding/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04519(outfit: dict) -> float:
    """Score rule 4519: yellow/date/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04520(outfit: dict) -> float:
    """Score rule 4520: burgundy/casual/spring/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04521(outfit: dict) -> float:
    """Score rule 4521: pink/wedding/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04522(outfit: dict) -> float:
    """Score rule 4522: olive/date/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04523(outfit: dict) -> float:
    """Score rule 4523: green/casual/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04524(outfit: dict) -> float:
    """Score rule 4524: navy/party/spring/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04525(outfit: dict) -> float:
    """Score rule 4525: cream/sport/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04526(outfit: dict) -> float:
    """Score rule 4526: black/outdoor/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04527(outfit: dict) -> float:
    """Score rule 4527: blue/work/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04528(outfit: dict) -> float:
    """Score rule 4528: yellow/travel/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04529(outfit: dict) -> float:
    """Score rule 4529: burgundy/festival/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04530(outfit: dict) -> float:
    """Score rule 4530: pink/formal/autumn/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04531(outfit: dict) -> float:
    """Score rule 4531: beige/wedding/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04532(outfit: dict) -> float:
    """Score rule 4532: red/festival/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04533(outfit: dict) -> float:
    """Score rule 4533: white/formal/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04534(outfit: dict) -> float:
    """Score rule 4534: brown/wedding/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04535(outfit: dict) -> float:
    """Score rule 4535: orange/date/winter/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04536(outfit: dict) -> float:
    """Score rule 4536: gray/casual/winter/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04537(outfit: dict) -> float:
    """Score rule 4537: purple/party/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04538(outfit: dict) -> float:
    """Score rule 4538: olive/sport/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04539(outfit: dict) -> float:
    """Score rule 4539: green/outdoor/winter/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04540(outfit: dict) -> float:
    """Score rule 4540: navy/work/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04541(outfit: dict) -> float:
    """Score rule 4541: red/travel/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04542(outfit: dict) -> float:
    """Score rule 4542: white/festival/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04543(outfit: dict) -> float:
    """Score rule 4543: brown/work/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04544(outfit: dict) -> float:
    """Score rule 4544: orange/travel/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04545(outfit: dict) -> float:
    """Score rule 4545: gray/festival/summer/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04546(outfit: dict) -> float:
    """Score rule 4546: purple/formal/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04547(outfit: dict) -> float:
    """Score rule 4547: olive/wedding/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04548(outfit: dict) -> float:
    """Score rule 4548: green/date/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04549(outfit: dict) -> float:
    """Score rule 4549: navy/casual/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04550(outfit: dict) -> float:
    """Score rule 4550: cream/party/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04551(outfit: dict) -> float:
    """Score rule 4551: black/sport/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04552(outfit: dict) -> float:
    """Score rule 4552: blue/outdoor/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04553(outfit: dict) -> float:
    """Score rule 4553: yellow/work/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04554(outfit: dict) -> float:
    """Score rule 4554: burgundy/sport/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04555(outfit: dict) -> float:
    """Score rule 4555: pink/outdoor/winter/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04556(outfit: dict) -> float:
    """Score rule 4556: beige/work/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04557(outfit: dict) -> float:
    """Score rule 4557: red/travel/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04558(outfit: dict) -> float:
    """Score rule 4558: white/festival/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04559(outfit: dict) -> float:
    """Score rule 4559: brown/formal/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04560(outfit: dict) -> float:
    """Score rule 4560: black/wedding/spring/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04561(outfit: dict) -> float:
    """Score rule 4561: blue/date/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04562(outfit: dict) -> float:
    """Score rule 4562: yellow/casual/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04563(outfit: dict) -> float:
    """Score rule 4563: burgundy/party/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04564(outfit: dict) -> float:
    """Score rule 4564: pink/sport/spring/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04565(outfit: dict) -> float:
    """Score rule 4565: beige/casual/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04566(outfit: dict) -> float:
    """Score rule 4566: red/party/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04567(outfit: dict) -> float:
    """Score rule 4567: white/sport/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04568(outfit: dict) -> float:
    """Score rule 4568: brown/outdoor/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04569(outfit: dict) -> float:
    """Score rule 4569: orange/work/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04570(outfit: dict) -> float:
    """Score rule 4570: gray/travel/autumn/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04571(outfit: dict) -> float:
    """Score rule 4571: purple/festival/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04572(outfit: dict) -> float:
    """Score rule 4572: olive/formal/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04573(outfit: dict) -> float:
    """Score rule 4573: green/wedding/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04574(outfit: dict) -> float:
    """Score rule 4574: navy/date/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04575(outfit: dict) -> float:
    """Score rule 4575: cream/casual/winter/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04576(outfit: dict) -> float:
    """Score rule 4576: black/wedding/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04577(outfit: dict) -> float:
    """Score rule 4577: blue/date/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04578(outfit: dict) -> float:
    """Score rule 4578: yellow/casual/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04579(outfit: dict) -> float:
    """Score rule 4579: gray/party/winter/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04580(outfit: dict) -> float:
    """Score rule 4580: purple/sport/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04581(outfit: dict) -> float:
    """Score rule 4581: olive/outdoor/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04582(outfit: dict) -> float:
    """Score rule 4582: green/work/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04583(outfit: dict) -> float:
    """Score rule 4583: navy/travel/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04584(outfit: dict) -> float:
    """Score rule 4584: cream/festival/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04585(outfit: dict) -> float:
    """Score rule 4585: black/formal/summer/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04586(outfit: dict) -> float:
    """Score rule 4586: blue/wedding/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04587(outfit: dict) -> float:
    """Score rule 4587: yellow/festival/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04588(outfit: dict) -> float:
    """Score rule 4588: burgundy/formal/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04589(outfit: dict) -> float:
    """Score rule 4589: pink/wedding/summer/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04590(outfit: dict) -> float:
    """Score rule 4590: beige/date/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04591(outfit: dict) -> float:
    """Score rule 4591: red/casual/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04592(outfit: dict) -> float:
    """Score rule 4592: white/party/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04593(outfit: dict) -> float:
    """Score rule 4593: brown/sport/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04594(outfit: dict) -> float:
    """Score rule 4594: orange/outdoor/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04595(outfit: dict) -> float:
    """Score rule 4595: gray/work/winter/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04596(outfit: dict) -> float:
    """Score rule 4596: purple/travel/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04597(outfit: dict) -> float:
    """Score rule 4597: olive/festival/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04598(outfit: dict) -> float:
    """Score rule 4598: pink/work/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04599(outfit: dict) -> float:
    """Score rule 4599: beige/travel/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04600(outfit: dict) -> float:
    """Score rule 4600: red/festival/spring/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04601(outfit: dict) -> float:
    """Score rule 4601: white/formal/spring/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04602(outfit: dict) -> float:
    """Score rule 4602: brown/wedding/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04603(outfit: dict) -> float:
    """Score rule 4603: orange/date/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04604(outfit: dict) -> float:
    """Score rule 4604: gray/casual/spring/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04605(outfit: dict) -> float:
    """Score rule 4605: purple/party/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04606(outfit: dict) -> float:
    """Score rule 4606: olive/sport/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04607(outfit: dict) -> float:
    """Score rule 4607: green/outdoor/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04608(outfit: dict) -> float:
    """Score rule 4608: navy/work/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04609(outfit: dict) -> float:
    """Score rule 4609: cream/sport/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04610(outfit: dict) -> float:
    """Score rule 4610: black/outdoor/autumn/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04611(outfit: dict) -> float:
    """Score rule 4611: blue/work/autumn/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04612(outfit: dict) -> float:
    """Score rule 4612: yellow/travel/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04613(outfit: dict) -> float:
    """Score rule 4613: burgundy/festival/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04614(outfit: dict) -> float:
    """Score rule 4614: pink/formal/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04615(outfit: dict) -> float:
    """Score rule 4615: beige/wedding/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04616(outfit: dict) -> float:
    """Score rule 4616: red/date/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04617(outfit: dict) -> float:
    """Score rule 4617: navy/casual/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04618(outfit: dict) -> float:
    """Score rule 4618: cream/party/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04619(outfit: dict) -> float:
    """Score rule 4619: black/sport/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04620(outfit: dict) -> float:
    """Score rule 4620: blue/casual/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04621(outfit: dict) -> float:
    """Score rule 4621: yellow/party/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04622(outfit: dict) -> float:
    """Score rule 4622: burgundy/sport/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04623(outfit: dict) -> float:
    """Score rule 4623: pink/outdoor/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04624(outfit: dict) -> float:
    """Score rule 4624: beige/work/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04625(outfit: dict) -> float:
    """Score rule 4625: red/travel/summer/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04626(outfit: dict) -> float:
    """Score rule 4626: white/festival/summer/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04627(outfit: dict) -> float:
    """Score rule 4627: brown/formal/summer/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04628(outfit: dict) -> float:
    """Score rule 4628: orange/wedding/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04629(outfit: dict) -> float:
    """Score rule 4629: gray/date/summer/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04630(outfit: dict) -> float:
    """Score rule 4630: purple/casual/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04631(outfit: dict) -> float:
    """Score rule 4631: olive/wedding/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04632(outfit: dict) -> float:
    """Score rule 4632: green/date/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04633(outfit: dict) -> float:
    """Score rule 4633: navy/casual/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04634(outfit: dict) -> float:
    """Score rule 4634: cream/party/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04635(outfit: dict) -> float:
    """Score rule 4635: black/sport/winter/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04636(outfit: dict) -> float:
    """Score rule 4636: brown/outdoor/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04637(outfit: dict) -> float:
    """Score rule 4637: orange/work/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04638(outfit: dict) -> float:
    """Score rule 4638: gray/travel/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04639(outfit: dict) -> float:
    """Score rule 4639: purple/festival/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04640(outfit: dict) -> float:
    """Score rule 4640: olive/formal/spring/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04641(outfit: dict) -> float:
    """Score rule 4641: green/wedding/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04642(outfit: dict) -> float:
    """Score rule 4642: navy/festival/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04643(outfit: dict) -> float:
    """Score rule 4643: cream/formal/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04644(outfit: dict) -> float:
    """Score rule 4644: black/wedding/spring/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04645(outfit: dict) -> float:
    """Score rule 4645: blue/date/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04646(outfit: dict) -> float:
    """Score rule 4646: yellow/casual/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04647(outfit: dict) -> float:
    """Score rule 4647: burgundy/party/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04648(outfit: dict) -> float:
    """Score rule 4648: pink/sport/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04649(outfit: dict) -> float:
    """Score rule 4649: beige/outdoor/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04650(outfit: dict) -> float:
    """Score rule 4650: red/work/autumn/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04651(outfit: dict) -> float:
    """Score rule 4651: white/travel/autumn/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04652(outfit: dict) -> float:
    """Score rule 4652: brown/festival/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04653(outfit: dict) -> float:
    """Score rule 4653: orange/work/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04654(outfit: dict) -> float:
    """Score rule 4654: gray/travel/autumn/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04655(outfit: dict) -> float:
    """Score rule 4655: yellow/festival/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04656(outfit: dict) -> float:
    """Score rule 4656: burgundy/formal/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04657(outfit: dict) -> float:
    """Score rule 4657: pink/wedding/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04658(outfit: dict) -> float:
    """Score rule 4658: beige/date/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04659(outfit: dict) -> float:
    """Score rule 4659: red/casual/winter/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04660(outfit: dict) -> float:
    """Score rule 4660: white/party/spring/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04661(outfit: dict) -> float:
    """Score rule 4661: brown/sport/spring/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04662(outfit: dict) -> float:
    """Score rule 4662: orange/outdoor/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04663(outfit: dict) -> float:
    """Score rule 4663: gray/work/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04664(outfit: dict) -> float:
    """Score rule 4664: purple/sport/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04665(outfit: dict) -> float:
    """Score rule 4665: olive/outdoor/summer/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04666(outfit: dict) -> float:
    """Score rule 4666: green/work/summer/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04667(outfit: dict) -> float:
    """Score rule 4667: navy/travel/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04668(outfit: dict) -> float:
    """Score rule 4668: cream/festival/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04669(outfit: dict) -> float:
    """Score rule 4669: black/formal/summer/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04670(outfit: dict) -> float:
    """Score rule 4670: blue/wedding/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04671(outfit: dict) -> float:
    """Score rule 4671: yellow/date/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04672(outfit: dict) -> float:
    """Score rule 4672: burgundy/casual/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04673(outfit: dict) -> float:
    """Score rule 4673: pink/party/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04674(outfit: dict) -> float:
    """Score rule 4674: olive/sport/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04675(outfit: dict) -> float:
    """Score rule 4675: green/casual/winter/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04676(outfit: dict) -> float:
    """Score rule 4676: navy/party/winter/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04677(outfit: dict) -> float:
    """Score rule 4677: cream/sport/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04678(outfit: dict) -> float:
    """Score rule 4678: black/outdoor/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04679(outfit: dict) -> float:
    """Score rule 4679: blue/work/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04680(outfit: dict) -> float:
    """Score rule 4680: yellow/travel/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04681(outfit: dict) -> float:
    """Score rule 4681: burgundy/festival/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04682(outfit: dict) -> float:
    """Score rule 4682: pink/formal/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04683(outfit: dict) -> float:
    """Score rule 4683: beige/wedding/spring/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04684(outfit: dict) -> float:
    """Score rule 4684: red/date/spring/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04685(outfit: dict) -> float:
    """Score rule 4685: white/casual/summer/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04686(outfit: dict) -> float:
    """Score rule 4686: brown/wedding/summer/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04687(outfit: dict) -> float:
    """Score rule 4687: orange/date/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04688(outfit: dict) -> float:
    """Score rule 4688: gray/casual/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04689(outfit: dict) -> float:
    """Score rule 4689: purple/party/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04690(outfit: dict) -> float:
    """Score rule 4690: olive/sport/autumn/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04691(outfit: dict) -> float:
    """Score rule 4691: green/outdoor/autumn/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04692(outfit: dict) -> float:
    """Score rule 4692: navy/work/autumn/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04693(outfit: dict) -> float:
    """Score rule 4693: red/travel/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04694(outfit: dict) -> float:
    """Score rule 4694: white/festival/autumn/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04695(outfit: dict) -> float:
    """Score rule 4695: brown/formal/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04696(outfit: dict) -> float:
    """Score rule 4696: orange/wedding/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04697(outfit: dict) -> float:
    """Score rule 4697: gray/festival/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04698(outfit: dict) -> float:
    """Score rule 4698: purple/formal/winter/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04699(outfit: dict) -> float:
    """Score rule 4699: olive/wedding/winter/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04700(outfit: dict) -> float:
    """Score rule 4700: green/date/spring/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04701(outfit: dict) -> float:
    """Score rule 4701: navy/casual/spring/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04702(outfit: dict) -> float:
    """Score rule 4702: cream/party/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04703(outfit: dict) -> float:
    """Score rule 4703: black/sport/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04704(outfit: dict) -> float:
    """Score rule 4704: blue/outdoor/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04705(outfit: dict) -> float:
    """Score rule 4705: yellow/work/summer/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04706(outfit: dict) -> float:
    """Score rule 4706: burgundy/travel/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04707(outfit: dict) -> float:
    """Score rule 4707: pink/festival/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04708(outfit: dict) -> float:
    """Score rule 4708: beige/work/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04709(outfit: dict) -> float:
    """Score rule 4709: red/travel/summer/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04710(outfit: dict) -> float:
    """Score rule 4710: white/festival/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04711(outfit: dict) -> float:
    """Score rule 4711: brown/formal/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04712(outfit: dict) -> float:
    """Score rule 4712: black/wedding/autumn/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04713(outfit: dict) -> float:
    """Score rule 4713: blue/date/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04714(outfit: dict) -> float:
    """Score rule 4714: yellow/casual/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04715(outfit: dict) -> float:
    """Score rule 4715: burgundy/party/winter/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04716(outfit: dict) -> float:
    """Score rule 4716: pink/sport/winter/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04717(outfit: dict) -> float:
    """Score rule 4717: beige/outdoor/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04718(outfit: dict) -> float:
    """Score rule 4718: red/work/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04719(outfit: dict) -> float:
    """Score rule 4719: white/sport/winter/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04720(outfit: dict) -> float:
    """Score rule 4720: brown/outdoor/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04721(outfit: dict) -> float:
    """Score rule 4721: orange/work/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04722(outfit: dict) -> float:
    """Score rule 4722: gray/travel/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04723(outfit: dict) -> float:
    """Score rule 4723: purple/festival/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04724(outfit: dict) -> float:
    """Score rule 4724: olive/formal/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04725(outfit: dict) -> float:
    """Score rule 4725: green/wedding/summer/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04726(outfit: dict) -> float:
    """Score rule 4726: navy/date/summer/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04727(outfit: dict) -> float:
    """Score rule 4727: cream/casual/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04728(outfit: dict) -> float:
    """Score rule 4728: black/party/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04729(outfit: dict) -> float:
    """Score rule 4729: blue/sport/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04730(outfit: dict) -> float:
    """Score rule 4730: yellow/casual/autumn/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04731(outfit: dict) -> float:
    """Score rule 4731: gray/party/autumn/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04732(outfit: dict) -> float:
    """Score rule 4732: purple/sport/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04733(outfit: dict) -> float:
    """Score rule 4733: olive/outdoor/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04734(outfit: dict) -> float:
    """Score rule 4734: green/work/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04735(outfit: dict) -> float:
    """Score rule 4735: navy/travel/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04736(outfit: dict) -> float:
    """Score rule 4736: cream/festival/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04737(outfit: dict) -> float:
    """Score rule 4737: black/formal/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04738(outfit: dict) -> float:
    """Score rule 4738: blue/wedding/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04739(outfit: dict) -> float:
    """Score rule 4739: yellow/date/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04740(outfit: dict) -> float:
    """Score rule 4740: burgundy/casual/spring/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04741(outfit: dict) -> float:
    """Score rule 4741: pink/wedding/spring/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04742(outfit: dict) -> float:
    """Score rule 4742: beige/date/spring/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04743(outfit: dict) -> float:
    """Score rule 4743: red/casual/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04744(outfit: dict) -> float:
    """Score rule 4744: white/party/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04745(outfit: dict) -> float:
    """Score rule 4745: brown/sport/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04746(outfit: dict) -> float:
    """Score rule 4746: orange/outdoor/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04747(outfit: dict) -> float:
    """Score rule 4747: gray/work/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04748(outfit: dict) -> float:
    """Score rule 4748: purple/travel/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04749(outfit: dict) -> float:
    """Score rule 4749: olive/festival/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04750(outfit: dict) -> float:
    """Score rule 4750: pink/formal/autumn/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04751(outfit: dict) -> float:
    """Score rule 4751: beige/wedding/autumn/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04752(outfit: dict) -> float:
    """Score rule 4752: red/festival/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04753(outfit: dict) -> float:
    """Score rule 4753: white/formal/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04754(outfit: dict) -> float:
    """Score rule 4754: brown/wedding/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04755(outfit: dict) -> float:
    """Score rule 4755: orange/date/winter/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04756(outfit: dict) -> float:
    """Score rule 4756: gray/casual/winter/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04757(outfit: dict) -> float:
    """Score rule 4757: purple/party/winter/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04758(outfit: dict) -> float:
    """Score rule 4758: olive/sport/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04759(outfit: dict) -> float:
    """Score rule 4759: green/outdoor/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04760(outfit: dict) -> float:
    """Score rule 4760: navy/work/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04761(outfit: dict) -> float:
    """Score rule 4761: cream/travel/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04762(outfit: dict) -> float:
    """Score rule 4762: black/festival/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04763(outfit: dict) -> float:
    """Score rule 4763: blue/work/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04764(outfit: dict) -> float:
    """Score rule 4764: yellow/travel/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04765(outfit: dict) -> float:
    """Score rule 4765: burgundy/festival/summer/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04766(outfit: dict) -> float:
    """Score rule 4766: pink/formal/summer/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04767(outfit: dict) -> float:
    """Score rule 4767: beige/wedding/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04768(outfit: dict) -> float:
    """Score rule 4768: red/date/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04769(outfit: dict) -> float:
    """Score rule 4769: navy/casual/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04770(outfit: dict) -> float:
    """Score rule 4770: cream/party/autumn/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04771(outfit: dict) -> float:
    """Score rule 4771: black/sport/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04772(outfit: dict) -> float:
    """Score rule 4772: blue/outdoor/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04773(outfit: dict) -> float:
    """Score rule 4773: yellow/work/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04774(outfit: dict) -> float:
    """Score rule 4774: burgundy/sport/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04775(outfit: dict) -> float:
    """Score rule 4775: pink/outdoor/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04776(outfit: dict) -> float:
    """Score rule 4776: beige/work/winter/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04777(outfit: dict) -> float:
    """Score rule 4777: red/travel/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04778(outfit: dict) -> float:
    """Score rule 4778: white/festival/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04779(outfit: dict) -> float:
    """Score rule 4779: brown/formal/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04780(outfit: dict) -> float:
    """Score rule 4780: orange/wedding/spring/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04781(outfit: dict) -> float:
    """Score rule 4781: gray/date/spring/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04782(outfit: dict) -> float:
    """Score rule 4782: purple/casual/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04783(outfit: dict) -> float:
    """Score rule 4783: olive/party/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04784(outfit: dict) -> float:
    """Score rule 4784: green/sport/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04785(outfit: dict) -> float:
    """Score rule 4785: navy/casual/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04786(outfit: dict) -> float:
    """Score rule 4786: cream/party/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04787(outfit: dict) -> float:
    """Score rule 4787: black/sport/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04788(outfit: dict) -> float:
    """Score rule 4788: brown/outdoor/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04789(outfit: dict) -> float:
    """Score rule 4789: orange/work/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04790(outfit: dict) -> float:
    """Score rule 4790: gray/travel/autumn/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04791(outfit: dict) -> float:
    """Score rule 4791: purple/festival/autumn/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04792(outfit: dict) -> float:
    """Score rule 4792: olive/formal/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04793(outfit: dict) -> float:
    """Score rule 4793: green/wedding/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04794(outfit: dict) -> float:
    """Score rule 4794: navy/date/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04795(outfit: dict) -> float:
    """Score rule 4795: cream/casual/winter/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04796(outfit: dict) -> float:
    """Score rule 4796: black/wedding/winter/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04797(outfit: dict) -> float:
    """Score rule 4797: blue/date/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04798(outfit: dict) -> float:
    """Score rule 4798: yellow/casual/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04799(outfit: dict) -> float:
    """Score rule 4799: burgundy/party/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04800(outfit: dict) -> float:
    """Score rule 4800: pink/sport/spring/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04801(outfit: dict) -> float:
    """Score rule 4801: beige/outdoor/spring/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04802(outfit: dict) -> float:
    """Score rule 4802: red/work/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04803(outfit: dict) -> float:
    """Score rule 4803: white/travel/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04804(outfit: dict) -> float:
    """Score rule 4804: brown/festival/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04805(outfit: dict) -> float:
    """Score rule 4805: orange/formal/summer/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04806(outfit: dict) -> float:
    """Score rule 4806: gray/wedding/summer/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04807(outfit: dict) -> float:
    """Score rule 4807: yellow/festival/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04808(outfit: dict) -> float:
    """Score rule 4808: burgundy/formal/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04809(outfit: dict) -> float:
    """Score rule 4809: pink/wedding/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04810(outfit: dict) -> float:
    """Score rule 4810: beige/date/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04811(outfit: dict) -> float:
    """Score rule 4811: red/casual/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04812(outfit: dict) -> float:
    """Score rule 4812: white/party/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04813(outfit: dict) -> float:
    """Score rule 4813: brown/sport/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04814(outfit: dict) -> float:
    """Score rule 4814: orange/outdoor/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04815(outfit: dict) -> float:
    """Score rule 4815: gray/work/winter/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04816(outfit: dict) -> float:
    """Score rule 4816: purple/travel/winter/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04817(outfit: dict) -> float:
    """Score rule 4817: olive/festival/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04818(outfit: dict) -> float:
    """Score rule 4818: green/work/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04819(outfit: dict) -> float:
    """Score rule 4819: navy/travel/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04820(outfit: dict) -> float:
    """Score rule 4820: cream/festival/spring/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04821(outfit: dict) -> float:
    """Score rule 4821: black/formal/spring/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04822(outfit: dict) -> float:
    """Score rule 4822: blue/wedding/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04823(outfit: dict) -> float:
    """Score rule 4823: yellow/date/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04824(outfit: dict) -> float:
    """Score rule 4824: burgundy/casual/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04825(outfit: dict) -> float:
    """Score rule 4825: pink/party/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04826(outfit: dict) -> float:
    """Score rule 4826: olive/sport/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04827(outfit: dict) -> float:
    """Score rule 4827: green/outdoor/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04828(outfit: dict) -> float:
    """Score rule 4828: navy/work/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04829(outfit: dict) -> float:
    """Score rule 4829: cream/sport/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04830(outfit: dict) -> float:
    """Score rule 4830: black/outdoor/autumn/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04831(outfit: dict) -> float:
    """Score rule 4831: blue/work/autumn/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04832(outfit: dict) -> float:
    """Score rule 4832: yellow/travel/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04833(outfit: dict) -> float:
    """Score rule 4833: burgundy/festival/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04834(outfit: dict) -> float:
    """Score rule 4834: pink/formal/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04835(outfit: dict) -> float:
    """Score rule 4835: beige/wedding/winter/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04836(outfit: dict) -> float:
    """Score rule 4836: red/date/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04837(outfit: dict) -> float:
    """Score rule 4837: white/casual/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04838(outfit: dict) -> float:
    """Score rule 4838: brown/party/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04839(outfit: dict) -> float:
    """Score rule 4839: orange/sport/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04840(outfit: dict) -> float:
    """Score rule 4840: gray/casual/spring/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04841(outfit: dict) -> float:
    """Score rule 4841: purple/party/spring/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04842(outfit: dict) -> float:
    """Score rule 4842: olive/sport/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04843(outfit: dict) -> float:
    """Score rule 4843: green/outdoor/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04844(outfit: dict) -> float:
    """Score rule 4844: navy/work/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04845(outfit: dict) -> float:
    """Score rule 4845: red/travel/summer/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04846(outfit: dict) -> float:
    """Score rule 4846: white/festival/summer/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04847(outfit: dict) -> float:
    """Score rule 4847: brown/formal/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04848(outfit: dict) -> float:
    """Score rule 4848: orange/wedding/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04849(outfit: dict) -> float:
    """Score rule 4849: gray/date/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04850(outfit: dict) -> float:
    """Score rule 4850: purple/casual/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04851(outfit: dict) -> float:
    """Score rule 4851: olive/wedding/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04852(outfit: dict) -> float:
    """Score rule 4852: green/date/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04853(outfit: dict) -> float:
    """Score rule 4853: navy/casual/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04854(outfit: dict) -> float:
    """Score rule 4854: cream/party/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04855(outfit: dict) -> float:
    """Score rule 4855: black/sport/winter/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04856(outfit: dict) -> float:
    """Score rule 4856: blue/outdoor/winter/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04857(outfit: dict) -> float:
    """Score rule 4857: yellow/work/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04858(outfit: dict) -> float:
    """Score rule 4858: burgundy/travel/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04859(outfit: dict) -> float:
    """Score rule 4859: pink/festival/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04860(outfit: dict) -> float:
    """Score rule 4860: beige/formal/spring/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04861(outfit: dict) -> float:
    """Score rule 4861: red/wedding/spring/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04862(outfit: dict) -> float:
    """Score rule 4862: white/festival/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04863(outfit: dict) -> float:
    """Score rule 4863: brown/formal/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04864(outfit: dict) -> float:
    """Score rule 4864: black/wedding/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04865(outfit: dict) -> float:
    """Score rule 4865: blue/date/summer/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04866(outfit: dict) -> float:
    """Score rule 4866: yellow/casual/summer/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04867(outfit: dict) -> float:
    """Score rule 4867: burgundy/party/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04868(outfit: dict) -> float:
    """Score rule 4868: pink/sport/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04869(outfit: dict) -> float:
    """Score rule 4869: beige/outdoor/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04870(outfit: dict) -> float:
    """Score rule 4870: red/work/autumn/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04871(outfit: dict) -> float:
    """Score rule 4871: white/travel/autumn/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04872(outfit: dict) -> float:
    """Score rule 4872: brown/festival/autumn/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04873(outfit: dict) -> float:
    """Score rule 4873: orange/work/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04874(outfit: dict) -> float:
    """Score rule 4874: gray/travel/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04875(outfit: dict) -> float:
    """Score rule 4875: purple/festival/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04876(outfit: dict) -> float:
    """Score rule 4876: olive/formal/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04877(outfit: dict) -> float:
    """Score rule 4877: green/wedding/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04878(outfit: dict) -> float:
    """Score rule 4878: navy/date/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04879(outfit: dict) -> float:
    """Score rule 4879: cream/casual/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04880(outfit: dict) -> float:
    """Score rule 4880: black/party/spring/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04881(outfit: dict) -> float:
    """Score rule 4881: blue/sport/spring/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04882(outfit: dict) -> float:
    """Score rule 4882: yellow/outdoor/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04883(outfit: dict) -> float:
    """Score rule 4883: gray/work/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04884(outfit: dict) -> float:
    """Score rule 4884: purple/sport/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04885(outfit: dict) -> float:
    """Score rule 4885: olive/outdoor/summer/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04886(outfit: dict) -> float:
    """Score rule 4886: green/work/summer/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04887(outfit: dict) -> float:
    """Score rule 4887: navy/travel/summer/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04888(outfit: dict) -> float:
    """Score rule 4888: cream/festival/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04889(outfit: dict) -> float:
    """Score rule 4889: black/formal/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04890(outfit: dict) -> float:
    """Score rule 4890: blue/wedding/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04891(outfit: dict) -> float:
    """Score rule 4891: yellow/date/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04892(outfit: dict) -> float:
    """Score rule 4892: burgundy/casual/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04893(outfit: dict) -> float:
    """Score rule 4893: pink/party/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04894(outfit: dict) -> float:
    """Score rule 4894: beige/sport/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04895(outfit: dict) -> float:
    """Score rule 4895: red/casual/winter/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04896(outfit: dict) -> float:
    """Score rule 4896: white/party/winter/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04897(outfit: dict) -> float:
    """Score rule 4897: brown/sport/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04898(outfit: dict) -> float:
    """Score rule 4898: orange/outdoor/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04899(outfit: dict) -> float:
    """Score rule 4899: gray/work/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04900(outfit: dict) -> float:
    """Score rule 4900: purple/travel/spring/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04901(outfit: dict) -> float:
    """Score rule 4901: olive/festival/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04902(outfit: dict) -> float:
    """Score rule 4902: pink/formal/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04903(outfit: dict) -> float:
    """Score rule 4903: beige/wedding/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04904(outfit: dict) -> float:
    """Score rule 4904: red/date/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04905(outfit: dict) -> float:
    """Score rule 4905: white/casual/summer/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04906(outfit: dict) -> float:
    """Score rule 4906: brown/wedding/summer/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04907(outfit: dict) -> float:
    """Score rule 4907: orange/date/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04908(outfit: dict) -> float:
    """Score rule 4908: gray/casual/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04909(outfit: dict) -> float:
    """Score rule 4909: purple/party/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04910(outfit: dict) -> float:
    """Score rule 4910: olive/sport/autumn/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04911(outfit: dict) -> float:
    """Score rule 4911: green/outdoor/autumn/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04912(outfit: dict) -> float:
    """Score rule 4912: navy/work/autumn/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04913(outfit: dict) -> float:
    """Score rule 4913: cream/travel/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04914(outfit: dict) -> float:
    """Score rule 4914: black/festival/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04915(outfit: dict) -> float:
    """Score rule 4915: blue/formal/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04916(outfit: dict) -> float:
    """Score rule 4916: yellow/wedding/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04917(outfit: dict) -> float:
    """Score rule 4917: burgundy/festival/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04918(outfit: dict) -> float:
    """Score rule 4918: pink/formal/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04919(outfit: dict) -> float:
    """Score rule 4919: beige/wedding/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04920(outfit: dict) -> float:
    """Score rule 4920: red/date/spring/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04921(outfit: dict) -> float:
    """Score rule 4921: navy/casual/spring/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04922(outfit: dict) -> float:
    """Score rule 4922: cream/party/spring/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04923(outfit: dict) -> float:
    """Score rule 4923: black/sport/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04924(outfit: dict) -> float:
    """Score rule 4924: blue/outdoor/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04925(outfit: dict) -> float:
    """Score rule 4925: yellow/work/summer/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04926(outfit: dict) -> float:
    """Score rule 4926: burgundy/travel/summer/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04927(outfit: dict) -> float:
    """Score rule 4927: pink/festival/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04928(outfit: dict) -> float:
    """Score rule 4928: beige/work/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04929(outfit: dict) -> float:
    """Score rule 4929: red/travel/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04930(outfit: dict) -> float:
    """Score rule 4930: white/festival/autumn/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04931(outfit: dict) -> float:
    """Score rule 4931: brown/formal/autumn/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04932(outfit: dict) -> float:
    """Score rule 4932: orange/wedding/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04933(outfit: dict) -> float:
    """Score rule 4933: gray/date/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04934(outfit: dict) -> float:
    """Score rule 4934: purple/casual/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04935(outfit: dict) -> float:
    """Score rule 4935: olive/party/winter/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04936(outfit: dict) -> float:
    """Score rule 4936: green/sport/winter/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04937(outfit: dict) -> float:
    """Score rule 4937: navy/outdoor/winter/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04938(outfit: dict) -> float:
    """Score rule 4938: cream/work/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04939(outfit: dict) -> float:
    """Score rule 4939: black/sport/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04940(outfit: dict) -> float:
    """Score rule 4940: brown/outdoor/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04941(outfit: dict) -> float:
    """Score rule 4941: orange/work/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04942(outfit: dict) -> float:
    """Score rule 4942: gray/travel/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04943(outfit: dict) -> float:
    """Score rule 4943: purple/festival/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04944(outfit: dict) -> float:
    """Score rule 4944: olive/formal/spring/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04945(outfit: dict) -> float:
    """Score rule 4945: green/wedding/summer/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04946(outfit: dict) -> float:
    """Score rule 4946: navy/date/summer/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04947(outfit: dict) -> float:
    """Score rule 4947: cream/casual/summer/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04948(outfit: dict) -> float:
    """Score rule 4948: black/party/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04949(outfit: dict) -> float:
    """Score rule 4949: blue/sport/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04950(outfit: dict) -> float:
    """Score rule 4950: yellow/casual/autumn/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04951(outfit: dict) -> float:
    """Score rule 4951: burgundy/party/autumn/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04952(outfit: dict) -> float:
    """Score rule 4952: pink/sport/autumn/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04953(outfit: dict) -> float:
    """Score rule 4953: beige/outdoor/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04954(outfit: dict) -> float:
    """Score rule 4954: red/work/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04955(outfit: dict) -> float:
    """Score rule 4955: white/travel/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04956(outfit: dict) -> float:
    """Score rule 4956: brown/festival/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04957(outfit: dict) -> float:
    """Score rule 4957: orange/formal/winter/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04958(outfit: dict) -> float:
    """Score rule 4958: gray/wedding/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04959(outfit: dict) -> float:
    """Score rule 4959: yellow/date/winter/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04960(outfit: dict) -> float:
    """Score rule 4960: burgundy/casual/spring/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04961(outfit: dict) -> float:
    """Score rule 4961: pink/wedding/spring/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04962(outfit: dict) -> float:
    """Score rule 4962: beige/date/spring/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04963(outfit: dict) -> float:
    """Score rule 4963: red/casual/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04964(outfit: dict) -> float:
    """Score rule 4964: white/party/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04965(outfit: dict) -> float:
    """Score rule 4965: brown/sport/summer/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04966(outfit: dict) -> float:
    """Score rule 4966: orange/outdoor/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04967(outfit: dict) -> float:
    """Score rule 4967: gray/work/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04968(outfit: dict) -> float:
    """Score rule 4968: purple/travel/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04969(outfit: dict) -> float:
    """Score rule 4969: olive/festival/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04970(outfit: dict) -> float:
    """Score rule 4970: green/formal/autumn/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04971(outfit: dict) -> float:
    """Score rule 4971: navy/wedding/autumn/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04972(outfit: dict) -> float:
    """Score rule 4972: cream/festival/autumn/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04973(outfit: dict) -> float:
    """Score rule 4973: black/formal/autumn/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04974(outfit: dict) -> float:
    """Score rule 4974: blue/wedding/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04975(outfit: dict) -> float:
    """Score rule 4975: yellow/date/winter/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04976(outfit: dict) -> float:
    """Score rule 4976: burgundy/casual/winter/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04977(outfit: dict) -> float:
    """Score rule 4977: pink/party/winter/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04978(outfit: dict) -> float:
    """Score rule 4978: olive/sport/winter/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04979(outfit: dict) -> float:
    """Score rule 4979: green/outdoor/winter/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04980(outfit: dict) -> float:
    """Score rule 4980: navy/work/spring/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04981(outfit: dict) -> float:
    """Score rule 4981: cream/travel/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04982(outfit: dict) -> float:
    """Score rule 4982: black/festival/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04983(outfit: dict) -> float:
    """Score rule 4983: blue/work/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04984(outfit: dict) -> float:
    """Score rule 4984: yellow/travel/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04985(outfit: dict) -> float:
    """Score rule 4985: burgundy/festival/summer/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04986(outfit: dict) -> float:
    """Score rule 4986: pink/formal/summer/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04987(outfit: dict) -> float:
    """Score rule 4987: beige/wedding/summer/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04988(outfit: dict) -> float:
    """Score rule 4988: red/date/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04989(outfit: dict) -> float:
    """Score rule 4989: white/casual/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04990(outfit: dict) -> float:
    """Score rule 4990: brown/party/autumn/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04991(outfit: dict) -> float:
    """Score rule 4991: orange/sport/autumn/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04992(outfit: dict) -> float:
    """Score rule 4992: gray/outdoor/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04993(outfit: dict) -> float:
    """Score rule 4993: purple/work/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04994(outfit: dict) -> float:
    """Score rule 4994: olive/sport/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04995(outfit: dict) -> float:
    """Score rule 4995: green/outdoor/winter/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04996(outfit: dict) -> float:
    """Score rule 4996: navy/work/winter/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04997(outfit: dict) -> float:
    """Score rule 4997: red/travel/winter/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04998(outfit: dict) -> float:
    """Score rule 4998: white/festival/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_04999(outfit: dict) -> float:
    """Score rule 4999: brown/formal/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

