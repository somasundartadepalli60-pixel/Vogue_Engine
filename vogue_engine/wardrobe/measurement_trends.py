"""Stage 20: deterministic measurement trend summaries for local dashboards."""
from .measurements import MEASURES

def summarize_history(events):
    """Return chronological chart points and per-dimension first-to-last changes."""
    ordered = sorted(events, key=lambda event: (event['measured_on'], event['id']))
    series = {dimension: [] for dimension in MEASURES}
    for event in ordered:
        for dimension, value in event['measurements'].items():
            if dimension in series:
                series[dimension].append({'date': event['measured_on'], 'event_id': event['id'], 'cm': value})
    result = {}
    for dimension, points in series.items():
        if not points:
            continue
        result[dimension] = {
            'points': points,
            'first_cm': points[0]['cm'],
            'latest_cm': points[-1]['cm'],
            'change_cm': round(points[-1]['cm'] - points[0]['cm'], 2),
        }
    return {'events': len(ordered), 'dimensions': result}
