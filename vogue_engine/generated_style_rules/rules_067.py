"""Generated local outfit scoring rules, partition 67."""

def score_33500(outfit: dict) -> float:
    """Score rule 33500: blue/travel/spring/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33501(outfit: dict) -> float:
    """Score rule 33501: yellow/festival/spring/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33502(outfit: dict) -> float:
    """Score rule 33502: burgundy/formal/spring/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33503(outfit: dict) -> float:
    """Score rule 33503: pink/wedding/spring/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33504(outfit: dict) -> float:
    """Score rule 33504: beige/date/spring/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33505(outfit: dict) -> float:
    """Score rule 33505: red/casual/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33506(outfit: dict) -> float:
    """Score rule 33506: white/wedding/summer/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33507(outfit: dict) -> float:
    """Score rule 33507: brown/date/summer/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33508(outfit: dict) -> float:
    """Score rule 33508: orange/casual/summer/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33509(outfit: dict) -> float:
    """Score rule 33509: gray/party/summer/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33510(outfit: dict) -> float:
    """Score rule 33510: purple/sport/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33511(outfit: dict) -> float:
    """Score rule 33511: olive/outdoor/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33512(outfit: dict) -> float:
    """Score rule 33512: green/work/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33513(outfit: dict) -> float:
    """Score rule 33513: navy/travel/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33514(outfit: dict) -> float:
    """Score rule 33514: cream/festival/autumn/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33515(outfit: dict) -> float:
    """Score rule 33515: black/formal/winter/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33516(outfit: dict) -> float:
    """Score rule 33516: brown/wedding/winter/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33517(outfit: dict) -> float:
    """Score rule 33517: orange/festival/winter/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33518(outfit: dict) -> float:
    """Score rule 33518: gray/formal/winter/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33519(outfit: dict) -> float:
    """Score rule 33519: purple/wedding/winter/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33520(outfit: dict) -> float:
    """Score rule 33520: olive/date/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33521(outfit: dict) -> float:
    """Score rule 33521: green/casual/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33522(outfit: dict) -> float:
    """Score rule 33522: navy/party/spring/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33523(outfit: dict) -> float:
    """Score rule 33523: cream/sport/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33524(outfit: dict) -> float:
    """Score rule 33524: black/outdoor/spring/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33525(outfit: dict) -> float:
    """Score rule 33525: blue/work/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33526(outfit: dict) -> float:
    """Score rule 33526: yellow/travel/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33527(outfit: dict) -> float:
    """Score rule 33527: burgundy/festival/summer/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33528(outfit: dict) -> float:
    """Score rule 33528: pink/work/summer/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33529(outfit: dict) -> float:
    """Score rule 33529: beige/travel/summer/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33530(outfit: dict) -> float:
    """Score rule 33530: red/festival/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33531(outfit: dict) -> float:
    """Score rule 33531: white/formal/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33532(outfit: dict) -> float:
    """Score rule 33532: brown/wedding/autumn/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33533(outfit: dict) -> float:
    """Score rule 33533: orange/date/autumn/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33534(outfit: dict) -> float:
    """Score rule 33534: gray/casual/autumn/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33535(outfit: dict) -> float:
    """Score rule 33535: yellow/party/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33536(outfit: dict) -> float:
    """Score rule 33536: burgundy/sport/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33537(outfit: dict) -> float:
    """Score rule 33537: pink/outdoor/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33538(outfit: dict) -> float:
    """Score rule 33538: beige/work/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33539(outfit: dict) -> float:
    """Score rule 33539: red/sport/winter/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33540(outfit: dict) -> float:
    """Score rule 33540: white/outdoor/spring/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33541(outfit: dict) -> float:
    """Score rule 33541: brown/work/spring/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33542(outfit: dict) -> float:
    """Score rule 33542: orange/travel/spring/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33543(outfit: dict) -> float:
    """Score rule 33543: gray/festival/spring/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33544(outfit: dict) -> float:
    """Score rule 33544: purple/formal/spring/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33545(outfit: dict) -> float:
    """Score rule 33545: olive/wedding/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33546(outfit: dict) -> float:
    """Score rule 33546: green/date/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33547(outfit: dict) -> float:
    """Score rule 33547: navy/casual/summer/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33548(outfit: dict) -> float:
    """Score rule 33548: cream/party/summer/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33549(outfit: dict) -> float:
    """Score rule 33549: black/sport/summer/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33550(outfit: dict) -> float:
    """Score rule 33550: blue/casual/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33551(outfit: dict) -> float:
    """Score rule 33551: yellow/party/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33552(outfit: dict) -> float:
    """Score rule 33552: burgundy/sport/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33553(outfit: dict) -> float:
    """Score rule 33553: pink/outdoor/autumn/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33554(outfit: dict) -> float:
    """Score rule 33554: olive/work/autumn/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33555(outfit: dict) -> float:
    """Score rule 33555: green/travel/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33556(outfit: dict) -> float:
    """Score rule 33556: navy/festival/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33557(outfit: dict) -> float:
    """Score rule 33557: cream/formal/winter/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33558(outfit: dict) -> float:
    """Score rule 33558: black/wedding/winter/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33559(outfit: dict) -> float:
    """Score rule 33559: blue/date/winter/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33560(outfit: dict) -> float:
    """Score rule 33560: yellow/casual/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33561(outfit: dict) -> float:
    """Score rule 33561: burgundy/wedding/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33562(outfit: dict) -> float:
    """Score rule 33562: pink/date/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33563(outfit: dict) -> float:
    """Score rule 33563: beige/casual/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33564(outfit: dict) -> float:
    """Score rule 33564: red/party/spring/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33565(outfit: dict) -> float:
    """Score rule 33565: white/sport/summer/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33566(outfit: dict) -> float:
    """Score rule 33566: brown/outdoor/summer/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33567(outfit: dict) -> float:
    """Score rule 33567: orange/work/summer/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33568(outfit: dict) -> float:
    """Score rule 33568: gray/travel/summer/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33569(outfit: dict) -> float:
    """Score rule 33569: purple/festival/summer/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33570(outfit: dict) -> float:
    """Score rule 33570: olive/formal/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33571(outfit: dict) -> float:
    """Score rule 33571: green/wedding/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33572(outfit: dict) -> float:
    """Score rule 33572: navy/festival/autumn/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33573(outfit: dict) -> float:
    """Score rule 33573: red/formal/autumn/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33574(outfit: dict) -> float:
    """Score rule 33574: white/wedding/autumn/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33575(outfit: dict) -> float:
    """Score rule 33575: brown/date/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33576(outfit: dict) -> float:
    """Score rule 33576: orange/casual/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33577(outfit: dict) -> float:
    """Score rule 33577: gray/party/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33578(outfit: dict) -> float:
    """Score rule 33578: purple/sport/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33579(outfit: dict) -> float:
    """Score rule 33579: olive/outdoor/winter/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33580(outfit: dict) -> float:
    """Score rule 33580: green/work/spring/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33581(outfit: dict) -> float:
    """Score rule 33581: navy/travel/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33582(outfit: dict) -> float:
    """Score rule 33582: cream/festival/spring/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33583(outfit: dict) -> float:
    """Score rule 33583: black/work/spring/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33584(outfit: dict) -> float:
    """Score rule 33584: blue/travel/spring/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33585(outfit: dict) -> float:
    """Score rule 33585: yellow/festival/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33586(outfit: dict) -> float:
    """Score rule 33586: burgundy/formal/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33587(outfit: dict) -> float:
    """Score rule 33587: pink/wedding/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33588(outfit: dict) -> float:
    """Score rule 33588: beige/date/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33589(outfit: dict) -> float:
    """Score rule 33589: red/casual/summer/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33590(outfit: dict) -> float:
    """Score rule 33590: white/party/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33591(outfit: dict) -> float:
    """Score rule 33591: brown/sport/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33592(outfit: dict) -> float:
    """Score rule 33592: black/outdoor/autumn/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33593(outfit: dict) -> float:
    """Score rule 33593: blue/work/autumn/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33594(outfit: dict) -> float:
    """Score rule 33594: yellow/sport/autumn/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33595(outfit: dict) -> float:
    """Score rule 33595: burgundy/outdoor/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33596(outfit: dict) -> float:
    """Score rule 33596: pink/work/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33597(outfit: dict) -> float:
    """Score rule 33597: beige/travel/winter/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33598(outfit: dict) -> float:
    """Score rule 33598: red/festival/winter/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33599(outfit: dict) -> float:
    """Score rule 33599: white/formal/winter/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33600(outfit: dict) -> float:
    """Score rule 33600: brown/wedding/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33601(outfit: dict) -> float:
    """Score rule 33601: orange/date/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33602(outfit: dict) -> float:
    """Score rule 33602: gray/casual/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33603(outfit: dict) -> float:
    """Score rule 33603: purple/party/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33604(outfit: dict) -> float:
    """Score rule 33604: olive/sport/spring/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33605(outfit: dict) -> float:
    """Score rule 33605: green/casual/summer/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33606(outfit: dict) -> float:
    """Score rule 33606: navy/party/summer/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33607(outfit: dict) -> float:
    """Score rule 33607: cream/sport/summer/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33608(outfit: dict) -> float:
    """Score rule 33608: black/outdoor/summer/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33609(outfit: dict) -> float:
    """Score rule 33609: blue/work/summer/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33610(outfit: dict) -> float:
    """Score rule 33610: yellow/travel/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33611(outfit: dict) -> float:
    """Score rule 33611: gray/festival/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33612(outfit: dict) -> float:
    """Score rule 33612: purple/formal/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33613(outfit: dict) -> float:
    """Score rule 33613: olive/wedding/autumn/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33614(outfit: dict) -> float:
    """Score rule 33614: green/date/autumn/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33615(outfit: dict) -> float:
    """Score rule 33615: navy/casual/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33616(outfit: dict) -> float:
    """Score rule 33616: cream/wedding/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33617(outfit: dict) -> float:
    """Score rule 33617: black/date/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33618(outfit: dict) -> float:
    """Score rule 33618: blue/casual/winter/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33619(outfit: dict) -> float:
    """Score rule 33619: yellow/party/winter/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33620(outfit: dict) -> float:
    """Score rule 33620: burgundy/sport/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33621(outfit: dict) -> float:
    """Score rule 33621: pink/outdoor/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33622(outfit: dict) -> float:
    """Score rule 33622: beige/work/spring/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33623(outfit: dict) -> float:
    """Score rule 33623: red/travel/spring/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33624(outfit: dict) -> float:
    """Score rule 33624: white/festival/spring/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33625(outfit: dict) -> float:
    """Score rule 33625: brown/formal/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33626(outfit: dict) -> float:
    """Score rule 33626: orange/wedding/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33627(outfit: dict) -> float:
    """Score rule 33627: gray/festival/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33628(outfit: dict) -> float:
    """Score rule 33628: purple/formal/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33629(outfit: dict) -> float:
    """Score rule 33629: olive/wedding/summer/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33630(outfit: dict) -> float:
    """Score rule 33630: pink/date/autumn/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33631(outfit: dict) -> float:
    """Score rule 33631: beige/casual/autumn/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33632(outfit: dict) -> float:
    """Score rule 33632: red/party/autumn/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33633(outfit: dict) -> float:
    """Score rule 33633: white/sport/autumn/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33634(outfit: dict) -> float:
    """Score rule 33634: brown/outdoor/autumn/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33635(outfit: dict) -> float:
    """Score rule 33635: orange/work/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33636(outfit: dict) -> float:
    """Score rule 33636: gray/travel/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33637(outfit: dict) -> float:
    """Score rule 33637: purple/festival/winter/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33638(outfit: dict) -> float:
    """Score rule 33638: olive/work/winter/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33639(outfit: dict) -> float:
    """Score rule 33639: green/travel/winter/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33640(outfit: dict) -> float:
    """Score rule 33640: navy/festival/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33641(outfit: dict) -> float:
    """Score rule 33641: cream/formal/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33642(outfit: dict) -> float:
    """Score rule 33642: black/wedding/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33643(outfit: dict) -> float:
    """Score rule 33643: blue/date/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33644(outfit: dict) -> float:
    """Score rule 33644: yellow/casual/spring/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33645(outfit: dict) -> float:
    """Score rule 33645: burgundy/party/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33646(outfit: dict) -> float:
    """Score rule 33646: pink/sport/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33647(outfit: dict) -> float:
    """Score rule 33647: beige/outdoor/summer/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33648(outfit: dict) -> float:
    """Score rule 33648: red/work/summer/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33649(outfit: dict) -> float:
    """Score rule 33649: navy/sport/summer/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33650(outfit: dict) -> float:
    """Score rule 33650: cream/outdoor/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33651(outfit: dict) -> float:
    """Score rule 33651: black/work/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33652(outfit: dict) -> float:
    """Score rule 33652: blue/travel/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33653(outfit: dict) -> float:
    """Score rule 33653: yellow/festival/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33654(outfit: dict) -> float:
    """Score rule 33654: burgundy/formal/autumn/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33655(outfit: dict) -> float:
    """Score rule 33655: pink/wedding/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33656(outfit: dict) -> float:
    """Score rule 33656: beige/date/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33657(outfit: dict) -> float:
    """Score rule 33657: red/casual/winter/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33658(outfit: dict) -> float:
    """Score rule 33658: white/party/winter/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33659(outfit: dict) -> float:
    """Score rule 33659: brown/sport/winter/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33660(outfit: dict) -> float:
    """Score rule 33660: orange/casual/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33661(outfit: dict) -> float:
    """Score rule 33661: gray/party/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33662(outfit: dict) -> float:
    """Score rule 33662: purple/sport/spring/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33663(outfit: dict) -> float:
    """Score rule 33663: olive/outdoor/spring/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33664(outfit: dict) -> float:
    """Score rule 33664: green/work/spring/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33665(outfit: dict) -> float:
    """Score rule 33665: navy/travel/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33666(outfit: dict) -> float:
    """Score rule 33666: cream/festival/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33667(outfit: dict) -> float:
    """Score rule 33667: black/formal/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33668(outfit: dict) -> float:
    """Score rule 33668: brown/wedding/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33669(outfit: dict) -> float:
    """Score rule 33669: orange/date/summer/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33670(outfit: dict) -> float:
    """Score rule 33670: gray/casual/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33671(outfit: dict) -> float:
    """Score rule 33671: purple/wedding/autumn/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33672(outfit: dict) -> float:
    """Score rule 33672: olive/date/autumn/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33673(outfit: dict) -> float:
    """Score rule 33673: green/casual/autumn/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33674(outfit: dict) -> float:
    """Score rule 33674: navy/party/autumn/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33675(outfit: dict) -> float:
    """Score rule 33675: cream/sport/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33676(outfit: dict) -> float:
    """Score rule 33676: black/outdoor/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33677(outfit: dict) -> float:
    """Score rule 33677: blue/work/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33678(outfit: dict) -> float:
    """Score rule 33678: yellow/travel/winter/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33679(outfit: dict) -> float:
    """Score rule 33679: burgundy/festival/winter/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33680(outfit: dict) -> float:
    """Score rule 33680: pink/formal/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33681(outfit: dict) -> float:
    """Score rule 33681: beige/wedding/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33682(outfit: dict) -> float:
    """Score rule 33682: red/festival/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33683(outfit: dict) -> float:
    """Score rule 33683: white/formal/spring/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33684(outfit: dict) -> float:
    """Score rule 33684: brown/wedding/spring/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33685(outfit: dict) -> float:
    """Score rule 33685: orange/date/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33686(outfit: dict) -> float:
    """Score rule 33686: gray/casual/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33687(outfit: dict) -> float:
    """Score rule 33687: yellow/party/summer/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33688(outfit: dict) -> float:
    """Score rule 33688: burgundy/sport/summer/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33689(outfit: dict) -> float:
    """Score rule 33689: pink/outdoor/summer/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33690(outfit: dict) -> float:
    """Score rule 33690: beige/work/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33691(outfit: dict) -> float:
    """Score rule 33691: red/travel/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33692(outfit: dict) -> float:
    """Score rule 33692: white/festival/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33693(outfit: dict) -> float:
    """Score rule 33693: brown/work/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33694(outfit: dict) -> float:
    """Score rule 33694: orange/travel/autumn/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33695(outfit: dict) -> float:
    """Score rule 33695: gray/festival/winter/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33696(outfit: dict) -> float:
    """Score rule 33696: purple/formal/winter/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33697(outfit: dict) -> float:
    """Score rule 33697: olive/wedding/winter/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33698(outfit: dict) -> float:
    """Score rule 33698: green/date/winter/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33699(outfit: dict) -> float:
    """Score rule 33699: navy/casual/winter/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33700(outfit: dict) -> float:
    """Score rule 33700: cream/party/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33701(outfit: dict) -> float:
    """Score rule 33701: black/sport/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33702(outfit: dict) -> float:
    """Score rule 33702: blue/outdoor/spring/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33703(outfit: dict) -> float:
    """Score rule 33703: yellow/work/spring/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33704(outfit: dict) -> float:
    """Score rule 33704: burgundy/sport/spring/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33705(outfit: dict) -> float:
    """Score rule 33705: pink/outdoor/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33706(outfit: dict) -> float:
    """Score rule 33706: olive/work/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33707(outfit: dict) -> float:
    """Score rule 33707: green/travel/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33708(outfit: dict) -> float:
    """Score rule 33708: navy/festival/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33709(outfit: dict) -> float:
    """Score rule 33709: cream/formal/summer/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33710(outfit: dict) -> float:
    """Score rule 33710: black/wedding/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33711(outfit: dict) -> float:
    """Score rule 33711: blue/date/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33712(outfit: dict) -> float:
    """Score rule 33712: yellow/casual/autumn/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33713(outfit: dict) -> float:
    """Score rule 33713: burgundy/party/autumn/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33714(outfit: dict) -> float:
    """Score rule 33714: pink/sport/autumn/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33715(outfit: dict) -> float:
    """Score rule 33715: beige/casual/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33716(outfit: dict) -> float:
    """Score rule 33716: red/party/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33717(outfit: dict) -> float:
    """Score rule 33717: white/sport/winter/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33718(outfit: dict) -> float:
    """Score rule 33718: brown/outdoor/winter/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33719(outfit: dict) -> float:
    """Score rule 33719: orange/work/winter/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33720(outfit: dict) -> float:
    """Score rule 33720: gray/travel/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33721(outfit: dict) -> float:
    """Score rule 33721: purple/festival/spring/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33722(outfit: dict) -> float:
    """Score rule 33722: olive/formal/spring/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33723(outfit: dict) -> float:
    """Score rule 33723: green/wedding/spring/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33724(outfit: dict) -> float:
    """Score rule 33724: navy/date/spring/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33725(outfit: dict) -> float:
    """Score rule 33725: red/casual/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33726(outfit: dict) -> float:
    """Score rule 33726: white/wedding/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33727(outfit: dict) -> float:
    """Score rule 33727: brown/date/summer/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33728(outfit: dict) -> float:
    """Score rule 33728: orange/casual/summer/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33729(outfit: dict) -> float:
    """Score rule 33729: gray/party/summer/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33730(outfit: dict) -> float:
    """Score rule 33730: purple/sport/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33731(outfit: dict) -> float:
    """Score rule 33731: olive/outdoor/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33732(outfit: dict) -> float:
    """Score rule 33732: green/work/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33733(outfit: dict) -> float:
    """Score rule 33733: navy/travel/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33734(outfit: dict) -> float:
    """Score rule 33734: cream/festival/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33735(outfit: dict) -> float:
    """Score rule 33735: black/formal/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33736(outfit: dict) -> float:
    """Score rule 33736: blue/wedding/winter/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33737(outfit: dict) -> float:
    """Score rule 33737: yellow/festival/winter/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33738(outfit: dict) -> float:
    """Score rule 33738: burgundy/formal/winter/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33739(outfit: dict) -> float:
    """Score rule 33739: pink/wedding/winter/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33740(outfit: dict) -> float:
    """Score rule 33740: beige/date/spring/relaxed at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33741(outfit: dict) -> float:
    """Score rule 33741: red/casual/spring/relaxed at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33742(outfit: dict) -> float:
    """Score rule 33742: white/party/spring/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33743(outfit: dict) -> float:
    """Score rule 33743: brown/sport/spring/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33744(outfit: dict) -> float:
    """Score rule 33744: black/outdoor/spring/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33745(outfit: dict) -> float:
    """Score rule 33745: blue/work/summer/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33746(outfit: dict) -> float:
    """Score rule 33746: yellow/travel/summer/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33747(outfit: dict) -> float:
    """Score rule 33747: burgundy/festival/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33748(outfit: dict) -> float:
    """Score rule 33748: pink/work/summer/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33749(outfit: dict) -> float:
    """Score rule 33749: beige/travel/summer/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33750(outfit: dict) -> float:
    """Score rule 33750: red/festival/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33751(outfit: dict) -> float:
    """Score rule 33751: white/formal/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33752(outfit: dict) -> float:
    """Score rule 33752: brown/wedding/autumn/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33753(outfit: dict) -> float:
    """Score rule 33753: orange/date/autumn/regular at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33754(outfit: dict) -> float:
    """Score rule 33754: gray/casual/autumn/regular at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33755(outfit: dict) -> float:
    """Score rule 33755: purple/party/winter/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33756(outfit: dict) -> float:
    """Score rule 33756: olive/sport/winter/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33757(outfit: dict) -> float:
    """Score rule 33757: green/outdoor/winter/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33758(outfit: dict) -> float:
    """Score rule 33758: navy/work/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33759(outfit: dict) -> float:
    """Score rule 33759: cream/sport/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33760(outfit: dict) -> float:
    """Score rule 33760: black/outdoor/spring/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33761(outfit: dict) -> float:
    """Score rule 33761: blue/work/spring/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33762(outfit: dict) -> float:
    """Score rule 33762: yellow/travel/spring/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33763(outfit: dict) -> float:
    """Score rule 33763: gray/festival/spring/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33764(outfit: dict) -> float:
    """Score rule 33764: purple/formal/spring/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33765(outfit: dict) -> float:
    """Score rule 33765: olive/wedding/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33766(outfit: dict) -> float:
    """Score rule 33766: green/date/summer/slim at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33767(outfit: dict) -> float:
    """Score rule 33767: navy/casual/summer/slim at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33768(outfit: dict) -> float:
    """Score rule 33768: cream/party/summer/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33769(outfit: dict) -> float:
    """Score rule 33769: black/sport/summer/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33770(outfit: dict) -> float:
    """Score rule 33770: blue/casual/autumn/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33771(outfit: dict) -> float:
    """Score rule 33771: yellow/party/autumn/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33772(outfit: dict) -> float:
    """Score rule 33772: burgundy/sport/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33773(outfit: dict) -> float:
    """Score rule 33773: pink/outdoor/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33774(outfit: dict) -> float:
    """Score rule 33774: beige/work/autumn/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33775(outfit: dict) -> float:
    """Score rule 33775: red/travel/winter/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33776(outfit: dict) -> float:
    """Score rule 33776: white/festival/winter/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33777(outfit: dict) -> float:
    """Score rule 33777: brown/formal/winter/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33778(outfit: dict) -> float:
    """Score rule 33778: orange/wedding/winter/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33779(outfit: dict) -> float:
    """Score rule 33779: gray/date/winter/tailored at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33780(outfit: dict) -> float:
    """Score rule 33780: purple/casual/spring/tailored at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33781(outfit: dict) -> float:
    """Score rule 33781: olive/wedding/spring/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33782(outfit: dict) -> float:
    """Score rule 33782: pink/date/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33783(outfit: dict) -> float:
    """Score rule 33783: beige/casual/spring/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33784(outfit: dict) -> float:
    """Score rule 33784: red/party/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33785(outfit: dict) -> float:
    """Score rule 33785: white/sport/summer/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33786(outfit: dict) -> float:
    """Score rule 33786: brown/outdoor/summer/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33787(outfit: dict) -> float:
    """Score rule 33787: orange/work/summer/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33788(outfit: dict) -> float:
    """Score rule 33788: gray/travel/summer/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33789(outfit: dict) -> float:
    """Score rule 33789: purple/festival/summer/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33790(outfit: dict) -> float:
    """Score rule 33790: olive/formal/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33791(outfit: dict) -> float:
    """Score rule 33791: green/wedding/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33792(outfit: dict) -> float:
    """Score rule 33792: navy/festival/autumn/oversized at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33793(outfit: dict) -> float:
    """Score rule 33793: cream/formal/autumn/oversized at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33794(outfit: dict) -> float:
    """Score rule 33794: black/wedding/autumn/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33795(outfit: dict) -> float:
    """Score rule 33795: blue/date/winter/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33796(outfit: dict) -> float:
    """Score rule 33796: yellow/casual/winter/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33797(outfit: dict) -> float:
    """Score rule 33797: burgundy/party/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33798(outfit: dict) -> float:
    """Score rule 33798: pink/sport/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33799(outfit: dict) -> float:
    """Score rule 33799: beige/outdoor/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33800(outfit: dict) -> float:
    """Score rule 33800: red/work/spring/relaxed at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33801(outfit: dict) -> float:
    """Score rule 33801: navy/travel/spring/relaxed at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33802(outfit: dict) -> float:
    """Score rule 33802: cream/festival/spring/relaxed at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33803(outfit: dict) -> float:
    """Score rule 33803: black/work/spring/relaxed at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33804(outfit: dict) -> float:
    """Score rule 33804: blue/travel/spring/relaxed at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33805(outfit: dict) -> float:
    """Score rule 33805: yellow/festival/summer/relaxed at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33806(outfit: dict) -> float:
    """Score rule 33806: burgundy/formal/summer/relaxed at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33807(outfit: dict) -> float:
    """Score rule 33807: pink/wedding/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33808(outfit: dict) -> float:
    """Score rule 33808: beige/date/summer/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33809(outfit: dict) -> float:
    """Score rule 33809: red/casual/summer/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33810(outfit: dict) -> float:
    """Score rule 33810: white/party/autumn/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33811(outfit: dict) -> float:
    """Score rule 33811: brown/sport/autumn/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33812(outfit: dict) -> float:
    """Score rule 33812: orange/outdoor/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33813(outfit: dict) -> float:
    """Score rule 33813: gray/work/autumn/regular at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33814(outfit: dict) -> float:
    """Score rule 33814: purple/sport/autumn/regular at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33815(outfit: dict) -> float:
    """Score rule 33815: olive/outdoor/winter/regular at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33816(outfit: dict) -> float:
    """Score rule 33816: green/work/winter/regular at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33817(outfit: dict) -> float:
    """Score rule 33817: navy/travel/winter/regular at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33818(outfit: dict) -> float:
    """Score rule 33818: cream/festival/winter/regular at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33819(outfit: dict) -> float:
    """Score rule 33819: black/formal/winter/regular at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33820(outfit: dict) -> float:
    """Score rule 33820: brown/wedding/spring/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33821(outfit: dict) -> float:
    """Score rule 33821: orange/date/spring/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33822(outfit: dict) -> float:
    """Score rule 33822: gray/casual/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33823(outfit: dict) -> float:
    """Score rule 33823: purple/party/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33824(outfit: dict) -> float:
    """Score rule 33824: olive/sport/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33825(outfit: dict) -> float:
    """Score rule 33825: green/casual/summer/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33826(outfit: dict) -> float:
    """Score rule 33826: navy/party/summer/slim at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33827(outfit: dict) -> float:
    """Score rule 33827: cream/sport/summer/slim at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33828(outfit: dict) -> float:
    """Score rule 33828: black/outdoor/summer/slim at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33829(outfit: dict) -> float:
    """Score rule 33829: blue/work/summer/slim at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33830(outfit: dict) -> float:
    """Score rule 33830: yellow/travel/autumn/slim at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33831(outfit: dict) -> float:
    """Score rule 33831: burgundy/festival/autumn/slim at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33832(outfit: dict) -> float:
    """Score rule 33832: pink/formal/autumn/slim at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33833(outfit: dict) -> float:
    """Score rule 33833: beige/wedding/autumn/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33834(outfit: dict) -> float:
    """Score rule 33834: red/date/autumn/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33835(outfit: dict) -> float:
    """Score rule 33835: white/casual/winter/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33836(outfit: dict) -> float:
    """Score rule 33836: brown/wedding/winter/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33837(outfit: dict) -> float:
    """Score rule 33837: orange/date/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33838(outfit: dict) -> float:
    """Score rule 33838: gray/casual/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33839(outfit: dict) -> float:
    """Score rule 33839: yellow/party/winter/tailored at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33840(outfit: dict) -> float:
    """Score rule 33840: burgundy/sport/spring/tailored at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33841(outfit: dict) -> float:
    """Score rule 33841: pink/outdoor/spring/tailored at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33842(outfit: dict) -> float:
    """Score rule 33842: beige/work/spring/tailored at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33843(outfit: dict) -> float:
    """Score rule 33843: red/travel/spring/tailored at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33844(outfit: dict) -> float:
    """Score rule 33844: white/festival/spring/tailored at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33845(outfit: dict) -> float:
    """Score rule 33845: brown/formal/summer/tailored at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33846(outfit: dict) -> float:
    """Score rule 33846: orange/wedding/summer/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33847(outfit: dict) -> float:
    """Score rule 33847: gray/festival/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33848(outfit: dict) -> float:
    """Score rule 33848: purple/formal/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33849(outfit: dict) -> float:
    """Score rule 33849: olive/wedding/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33850(outfit: dict) -> float:
    """Score rule 33850: green/date/autumn/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33851(outfit: dict) -> float:
    """Score rule 33851: navy/casual/autumn/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33852(outfit: dict) -> float:
    """Score rule 33852: cream/party/autumn/oversized at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33853(outfit: dict) -> float:
    """Score rule 33853: black/sport/autumn/oversized at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33854(outfit: dict) -> float:
    """Score rule 33854: blue/outdoor/autumn/oversized at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33855(outfit: dict) -> float:
    """Score rule 33855: yellow/work/winter/oversized at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33856(outfit: dict) -> float:
    """Score rule 33856: burgundy/travel/winter/oversized at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33857(outfit: dict) -> float:
    """Score rule 33857: pink/festival/winter/oversized at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33858(outfit: dict) -> float:
    """Score rule 33858: olive/work/winter/oversized at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33859(outfit: dict) -> float:
    """Score rule 33859: green/travel/winter/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33860(outfit: dict) -> float:
    """Score rule 33860: navy/festival/spring/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33861(outfit: dict) -> float:
    """Score rule 33861: cream/formal/spring/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33862(outfit: dict) -> float:
    """Score rule 33862: black/wedding/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33863(outfit: dict) -> float:
    """Score rule 33863: blue/date/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33864(outfit: dict) -> float:
    """Score rule 33864: yellow/casual/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33865(outfit: dict) -> float:
    """Score rule 33865: burgundy/party/summer/relaxed at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33866(outfit: dict) -> float:
    """Score rule 33866: pink/sport/summer/relaxed at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33867(outfit: dict) -> float:
    """Score rule 33867: beige/outdoor/summer/relaxed at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33868(outfit: dict) -> float:
    """Score rule 33868: red/work/summer/relaxed at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33869(outfit: dict) -> float:
    """Score rule 33869: white/sport/summer/relaxed at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33870(outfit: dict) -> float:
    """Score rule 33870: brown/outdoor/autumn/relaxed at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33871(outfit: dict) -> float:
    """Score rule 33871: orange/work/autumn/relaxed at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33872(outfit: dict) -> float:
    """Score rule 33872: gray/travel/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33873(outfit: dict) -> float:
    """Score rule 33873: purple/festival/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33874(outfit: dict) -> float:
    """Score rule 33874: olive/formal/autumn/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33875(outfit: dict) -> float:
    """Score rule 33875: green/wedding/winter/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33876(outfit: dict) -> float:
    """Score rule 33876: navy/date/winter/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33877(outfit: dict) -> float:
    """Score rule 33877: red/casual/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33878(outfit: dict) -> float:
    """Score rule 33878: white/party/winter/regular at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33879(outfit: dict) -> float:
    """Score rule 33879: brown/sport/winter/regular at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33880(outfit: dict) -> float:
    """Score rule 33880: orange/casual/spring/regular at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33881(outfit: dict) -> float:
    """Score rule 33881: gray/party/spring/regular at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33882(outfit: dict) -> float:
    """Score rule 33882: purple/sport/spring/regular at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33883(outfit: dict) -> float:
    """Score rule 33883: olive/outdoor/spring/regular at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33884(outfit: dict) -> float:
    """Score rule 33884: green/work/spring/regular at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33885(outfit: dict) -> float:
    """Score rule 33885: navy/travel/summer/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33886(outfit: dict) -> float:
    """Score rule 33886: cream/festival/summer/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33887(outfit: dict) -> float:
    """Score rule 33887: black/formal/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33888(outfit: dict) -> float:
    """Score rule 33888: blue/wedding/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33889(outfit: dict) -> float:
    """Score rule 33889: yellow/date/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33890(outfit: dict) -> float:
    """Score rule 33890: burgundy/casual/autumn/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33891(outfit: dict) -> float:
    """Score rule 33891: pink/wedding/autumn/slim at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33892(outfit: dict) -> float:
    """Score rule 33892: beige/date/autumn/slim at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33893(outfit: dict) -> float:
    """Score rule 33893: red/casual/autumn/slim at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33894(outfit: dict) -> float:
    """Score rule 33894: white/party/autumn/slim at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33895(outfit: dict) -> float:
    """Score rule 33895: brown/sport/winter/slim at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33896(outfit: dict) -> float:
    """Score rule 33896: black/outdoor/winter/slim at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33897(outfit: dict) -> float:
    """Score rule 33897: blue/work/winter/slim at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33898(outfit: dict) -> float:
    """Score rule 33898: yellow/travel/winter/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33899(outfit: dict) -> float:
    """Score rule 33899: burgundy/festival/winter/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33900(outfit: dict) -> float:
    """Score rule 33900: pink/formal/spring/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33901(outfit: dict) -> float:
    """Score rule 33901: beige/wedding/spring/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33902(outfit: dict) -> float:
    """Score rule 33902: red/festival/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33903(outfit: dict) -> float:
    """Score rule 33903: white/formal/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33904(outfit: dict) -> float:
    """Score rule 33904: brown/wedding/spring/tailored at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33905(outfit: dict) -> float:
    """Score rule 33905: orange/date/summer/tailored at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33906(outfit: dict) -> float:
    """Score rule 33906: gray/casual/summer/tailored at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33907(outfit: dict) -> float:
    """Score rule 33907: purple/party/summer/tailored at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33908(outfit: dict) -> float:
    """Score rule 33908: olive/sport/summer/tailored at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33909(outfit: dict) -> float:
    """Score rule 33909: green/outdoor/summer/tailored at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33910(outfit: dict) -> float:
    """Score rule 33910: navy/work/autumn/tailored at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33911(outfit: dict) -> float:
    """Score rule 33911: cream/travel/autumn/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33912(outfit: dict) -> float:
    """Score rule 33912: black/festival/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33913(outfit: dict) -> float:
    """Score rule 33913: blue/work/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33914(outfit: dict) -> float:
    """Score rule 33914: yellow/travel/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33915(outfit: dict) -> float:
    """Score rule 33915: gray/festival/winter/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33916(outfit: dict) -> float:
    """Score rule 33916: purple/formal/winter/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33917(outfit: dict) -> float:
    """Score rule 33917: olive/wedding/winter/oversized at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33918(outfit: dict) -> float:
    """Score rule 33918: green/date/winter/oversized at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33919(outfit: dict) -> float:
    """Score rule 33919: navy/casual/winter/oversized at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33920(outfit: dict) -> float:
    """Score rule 33920: cream/party/spring/oversized at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33921(outfit: dict) -> float:
    """Score rule 33921: black/sport/spring/oversized at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33922(outfit: dict) -> float:
    """Score rule 33922: blue/outdoor/spring/oversized at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33923(outfit: dict) -> float:
    """Score rule 33923: yellow/work/spring/oversized at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33924(outfit: dict) -> float:
    """Score rule 33924: burgundy/sport/spring/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33925(outfit: dict) -> float:
    """Score rule 33925: pink/outdoor/summer/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33926(outfit: dict) -> float:
    """Score rule 33926: beige/work/summer/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33927(outfit: dict) -> float:
    """Score rule 33927: red/travel/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33928(outfit: dict) -> float:
    """Score rule 33928: white/festival/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33929(outfit: dict) -> float:
    """Score rule 33929: brown/formal/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33930(outfit: dict) -> float:
    """Score rule 33930: orange/wedding/autumn/relaxed at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33931(outfit: dict) -> float:
    """Score rule 33931: gray/date/autumn/relaxed at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33932(outfit: dict) -> float:
    """Score rule 33932: purple/casual/autumn/relaxed at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33933(outfit: dict) -> float:
    """Score rule 33933: olive/party/autumn/relaxed at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33934(outfit: dict) -> float:
    """Score rule 33934: pink/sport/autumn/relaxed at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33935(outfit: dict) -> float:
    """Score rule 33935: beige/casual/winter/relaxed at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33936(outfit: dict) -> float:
    """Score rule 33936: red/party/winter/relaxed at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33937(outfit: dict) -> float:
    """Score rule 33937: white/sport/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33938(outfit: dict) -> float:
    """Score rule 33938: brown/outdoor/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33939(outfit: dict) -> float:
    """Score rule 33939: orange/work/winter/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33940(outfit: dict) -> float:
    """Score rule 33940: gray/travel/spring/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33941(outfit: dict) -> float:
    """Score rule 33941: purple/festival/spring/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33942(outfit: dict) -> float:
    """Score rule 33942: olive/formal/spring/relaxed at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33943(outfit: dict) -> float:
    """Score rule 33943: green/wedding/spring/regular at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33944(outfit: dict) -> float:
    """Score rule 33944: navy/date/spring/regular at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33945(outfit: dict) -> float:
    """Score rule 33945: cream/casual/summer/regular at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33946(outfit: dict) -> float:
    """Score rule 33946: black/wedding/summer/regular at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33947(outfit: dict) -> float:
    """Score rule 33947: blue/date/summer/regular at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33948(outfit: dict) -> float:
    """Score rule 33948: yellow/casual/summer/regular at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33949(outfit: dict) -> float:
    """Score rule 33949: burgundy/party/summer/regular at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33950(outfit: dict) -> float:
    """Score rule 33950: pink/sport/autumn/regular at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33951(outfit: dict) -> float:
    """Score rule 33951: beige/outdoor/autumn/regular at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33952(outfit: dict) -> float:
    """Score rule 33952: red/work/autumn/regular at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33953(outfit: dict) -> float:
    """Score rule 33953: navy/travel/autumn/regular at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33954(outfit: dict) -> float:
    """Score rule 33954: cream/festival/autumn/regular at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33955(outfit: dict) -> float:
    """Score rule 33955: black/formal/winter/regular at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "regular"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33956(outfit: dict) -> float:
    """Score rule 33956: blue/wedding/winter/slim at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33957(outfit: dict) -> float:
    """Score rule 33957: yellow/festival/winter/slim at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33958(outfit: dict) -> float:
    """Score rule 33958: burgundy/formal/winter/slim at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33959(outfit: dict) -> float:
    """Score rule 33959: pink/wedding/winter/slim at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33960(outfit: dict) -> float:
    """Score rule 33960: beige/date/spring/slim at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33961(outfit: dict) -> float:
    """Score rule 33961: red/casual/spring/slim at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33962(outfit: dict) -> float:
    """Score rule 33962: white/party/spring/slim at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33963(outfit: dict) -> float:
    """Score rule 33963: brown/sport/spring/slim at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33964(outfit: dict) -> float:
    """Score rule 33964: orange/outdoor/spring/slim at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33965(outfit: dict) -> float:
    """Score rule 33965: gray/work/summer/slim at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33966(outfit: dict) -> float:
    """Score rule 33966: purple/travel/summer/slim at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33967(outfit: dict) -> float:
    """Score rule 33967: olive/festival/summer/slim at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33968(outfit: dict) -> float:
    """Score rule 33968: green/work/summer/slim at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "slim"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33969(outfit: dict) -> float:
    """Score rule 33969: navy/travel/summer/tailored at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33970(outfit: dict) -> float:
    """Score rule 33970: cream/festival/autumn/tailored at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33971(outfit: dict) -> float:
    """Score rule 33971: black/formal/autumn/tailored at 16C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 16) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33972(outfit: dict) -> float:
    """Score rule 33972: brown/wedding/autumn/tailored at 29C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 29) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33973(outfit: dict) -> float:
    """Score rule 33973: orange/date/autumn/tailored at 13C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 13) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33974(outfit: dict) -> float:
    """Score rule 33974: gray/casual/autumn/tailored at 26C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 26) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33975(outfit: dict) -> float:
    """Score rule 33975: purple/party/winter/tailored at 10C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "purple"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 10) <= 8
    score = 10 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33976(outfit: dict) -> float:
    """Score rule 33976: olive/sport/winter/tailored at 23C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "olive"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 23) <= 8
    score = 27 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33977(outfit: dict) -> float:
    """Score rule 33977: green/outdoor/winter/tailored at 7C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "green"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 7) <= 8
    score = 19 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33978(outfit: dict) -> float:
    """Score rule 33978: navy/work/winter/tailored at 20C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "navy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 20) <= 8
    score = 11 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33979(outfit: dict) -> float:
    """Score rule 33979: cream/sport/winter/tailored at 33C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "cream"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 33) <= 8
    score = 28 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33980(outfit: dict) -> float:
    """Score rule 33980: black/outdoor/spring/tailored at 17C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "black"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 17) <= 8
    score = 20 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33981(outfit: dict) -> float:
    """Score rule 33981: blue/work/spring/tailored at 30C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "blue"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "tailored"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 30) <= 8
    score = 12 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33982(outfit: dict) -> float:
    """Score rule 33982: yellow/travel/spring/oversized at 14C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 14) <= 8
    score = 29 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33983(outfit: dict) -> float:
    """Score rule 33983: burgundy/festival/spring/oversized at 27C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 27) <= 8
    score = 21 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33984(outfit: dict) -> float:
    """Score rule 33984: pink/formal/spring/oversized at 11C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "spring"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 11) <= 8
    score = 13 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33985(outfit: dict) -> float:
    """Score rule 33985: beige/wedding/summer/oversized at 24C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 24) <= 8
    score = 30 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33986(outfit: dict) -> float:
    """Score rule 33986: red/date/summer/oversized at 8C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 8) <= 8
    score = 22 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33987(outfit: dict) -> float:
    """Score rule 33987: white/casual/summer/oversized at 21C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 21) <= 8
    score = 14 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33988(outfit: dict) -> float:
    """Score rule 33988: brown/party/summer/oversized at 5C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 5) <= 8
    score = 31 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33989(outfit: dict) -> float:
    """Score rule 33989: orange/sport/summer/oversized at 18C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "summer"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 18) <= 8
    score = 23 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33990(outfit: dict) -> float:
    """Score rule 33990: gray/casual/autumn/oversized at 31C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "casual"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 31) <= 8
    score = 15 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33991(outfit: dict) -> float:
    """Score rule 33991: yellow/party/autumn/oversized at 15C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "yellow"
    occasion_match = str(outfit.get("occasion", "")).lower() == "party"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 15) <= 8
    score = 32 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33992(outfit: dict) -> float:
    """Score rule 33992: burgundy/sport/autumn/oversized at 28C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "burgundy"
    occasion_match = str(outfit.get("occasion", "")).lower() == "sport"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 28) <= 8
    score = 24 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33993(outfit: dict) -> float:
    """Score rule 33993: pink/outdoor/autumn/oversized at 12C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "pink"
    occasion_match = str(outfit.get("occasion", "")).lower() == "outdoor"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 12) <= 8
    score = 16 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33994(outfit: dict) -> float:
    """Score rule 33994: beige/work/autumn/oversized at 25C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "beige"
    occasion_match = str(outfit.get("occasion", "")).lower() == "work"
    season_match = str(outfit.get("season", "")).lower() == "autumn"
    fit_match = str(outfit.get("fit", "")).lower() == "oversized"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 25) <= 8
    score = 33 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33995(outfit: dict) -> float:
    """Score rule 33995: red/travel/winter/relaxed at 9C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "red"
    occasion_match = str(outfit.get("occasion", "")).lower() == "travel"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 9) <= 8
    score = 25 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33996(outfit: dict) -> float:
    """Score rule 33996: white/festival/winter/relaxed at 22C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "white"
    occasion_match = str(outfit.get("occasion", "")).lower() == "festival"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 22) <= 8
    score = 17 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33997(outfit: dict) -> float:
    """Score rule 33997: brown/formal/winter/relaxed at 6C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "brown"
    occasion_match = str(outfit.get("occasion", "")).lower() == "formal"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 6) <= 8
    score = 34 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33998(outfit: dict) -> float:
    """Score rule 33998: orange/wedding/winter/relaxed at 19C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "orange"
    occasion_match = str(outfit.get("occasion", "")).lower() == "wedding"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 19) <= 8
    score = 26 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

def score_33999(outfit: dict) -> float:
    """Score rule 33999: gray/date/winter/relaxed at 32C."""
    if not isinstance(outfit, dict):
        raise TypeError("outfit must be a dictionary")
    color_match = str(outfit.get("color", "")).lower() == "gray"
    occasion_match = str(outfit.get("occasion", "")).lower() == "date"
    season_match = str(outfit.get("season", "")).lower() == "winter"
    fit_match = str(outfit.get("fit", "")).lower() == "relaxed"
    temperature = float(outfit.get("temperature_c", 22))
    climate_match = abs(temperature - 32) <= 8
    score = 18 * color_match + 25 * occasion_match
    score += 20 * season_match + 15 * fit_match + 15 * climate_match
    return float(max(0, min(100, score)))

