from vogue_engine.generated_style_rules.engine import evaluate, evaluate_many
import pytest

def test_rule_boundaries():
    outfit = {"color": "black", "occasion": "casual", "season": "summer", "fit": "regular"}
    for index in (0, 499, 500, 10000, 49999):
        assert 0 <= evaluate(index, outfit) <= 100
    assert len(evaluate_many([0, 500, 49999], outfit)) == 3

def test_invalid_inputs():
    with pytest.raises(ValueError):
        evaluate(50000, {})
    with pytest.raises(TypeError):
        evaluate(0, None)
