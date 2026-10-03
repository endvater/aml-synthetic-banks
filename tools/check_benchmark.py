"""Validate all synthetic banks and exercise the evaluator with known labels."""
import json
from pathlib import Path
from jsonschema import Draft7Validator
from evaluate import evaluate_predictions

ROOT = Path(__file__).resolve().parents[1]
validator = Draft7Validator(json.loads((ROOT / "schemas/ground_truth_schema.json").read_text()))
banks = sorted((ROOT / "banks").glob("*/ground_truth.json"))
assert len(banks) == 10, "Expected ten benchmark banks"
for path in banks:
    truth = json.loads(path.read_text())
    validator.validate(truth)
    assert truth["bank_id"] == path.parent.name
    ids = [field["id"] for field in truth["prueffelder"]]
    assert ids and len(ids) == len(set(ids)), f"Duplicate or absent fields: {path}"
    predictions = {field["id"]: field["ergebnis"] for field in truth["prueffelder"]}
    result = evaluate_predictions(truth, predictions)
    assert result["exact_match_rate"] == 1.0
    assert result["false_positive_rate"] == 0.0
    assert not result["missing_predictions"]

# Catch metric regressions with one false positive and one false negative.
truth = {"bank_id": "test", "bank_name": "test", "prueffelder": [
    {"id": "A", "ergebnis": "konform"},
    {"id": "B", "ergebnis": "nicht_konform"},
]}
result = evaluate_predictions(truth, {"A": "nicht_konform", "B": "konform"})
assert result["confusion_matrix"] == {"tp": 0, "fp": 1, "fn": 1, "tn": 0}
assert result["false_positive_rate"] == 1.0
assert result["exact_match_rate"] == 0.0
print("10 Ground-Truth-Dateien und Evaluator-Gegenprobe validiert")
