# Generated scoring library

This release adds 50,000 distinct deterministic outfit scoring functions spread across 100 lazily loaded Python modules. Each function evaluates color, occasion, season, fit, and temperature compatibility with rule-specific parameters. No API keys or environment files are needed.

Example:

```python
from vogue_engine.generated_style_rules.engine import evaluate
print(evaluate(0, {"color":"black", "occasion":"casual", "season":"summer", "fit":"regular", "temperature_c":22}))
```

**Important:** The large LOC count comes predominantly from automatically generated, repetitive scoring functions. These are executable but are not 50,000 independently designed features. The library is lazy-loaded to avoid loading all functions into memory at once.
