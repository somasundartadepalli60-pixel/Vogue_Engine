"""Lazy dispatch for the generated rule library. No network or secrets required."""
from importlib import import_module

def evaluate(rule_id: int, outfit: dict) -> float:
    """Return a deterministic compatibility score for one rule (0..100)."""
    if not 0 <= rule_id < 50000:
        raise ValueError("rule_id must be in range 0..49999")
    module = import_module(f"vogue_engine.generated_style_rules.rules_{rule_id // 500:03d}")
    return getattr(module, f"score_{rule_id:05d}")(outfit)

def evaluate_many(rule_ids, outfit):
    return {rule_id: evaluate(rule_id, outfit) for rule_id in rule_ids}
