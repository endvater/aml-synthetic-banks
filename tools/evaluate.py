#!/usr/bin/env python3
"""
aml-synthetic-banks – Benchmark-Runner

Evaluiert ein AML-AI-System gegen alle (oder ausgewählte) synthetische Banken
und gibt Precision, Recall, F1 und False-Positive-Rate pro Prüffeld aus.

Verwendung:
    from tools.evaluate import load_ground_truth, evaluate_predictions

    ground_truth = load_ground_truth("01_musterbank_ag")
    # predictions = {prueffeld_id: "konform" | "teilkonform" | "nicht_konform" | "nicht_prüfbar"}
    results = evaluate_predictions(ground_truth, predictions)
    print_report(results)
"""

import json
import sys
from pathlib import Path
from typing import Any

BANKS_DIR = Path(__file__).parent.parent / "banks"
VALID_RESULTS = {"konform", "teilkonform", "nicht_konform", "nicht_prüfbar"}
NON_COMPLIANT = {"teilkonform", "nicht_konform"}


def load_ground_truth(bank_id: str) -> dict:
    """Lädt ground_truth.json für eine Bank."""
    path = BANKS_DIR / bank_id / "ground_truth.json"
    if not path.exists():
        raise FileNotFoundError(f"ground_truth.json nicht gefunden: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def evaluate_predictions(
    ground_truth: dict,
    predictions: dict[str, str],
) -> dict[str, Any]:
    """
    Vergleicht Vorhersagen mit Ground Truth.

    Args:
        ground_truth: Geladene ground_truth.json
        predictions: Dict {prueffeld_id: ergebnis}

    Returns:
        Dict mit Metriken: precision, recall, f1, false_positive_rate,
        per_field_results, confusion_matrix
    """
    gt_fields = {f["id"]: f for f in ground_truth["prueffelder"]}

    tp = fp = fn = tn = 0
    per_field = {}

    for field_id, gt_field in gt_fields.items():
        gt_result = gt_field["ergebnis"]
        pred_result = predictions.get(field_id)

        if pred_result is None:
            per_field[field_id] = {"status": "missing", "expected": gt_result}
            continue

        # Binäre Klassifikation: non-compliant (teilkonform/nicht_konform) vs compliant
        gt_nc = gt_result in NON_COMPLIANT
        pred_nc = pred_result in NON_COMPLIANT

        if gt_nc and pred_nc:
            tp += 1
            status = "true_positive"
        elif not gt_nc and pred_nc:
            fp += 1
            status = "false_positive"
        elif gt_nc and not pred_nc:
            fn += 1
            status = "false_negative"
        else:
            tn += 1
            status = "true_negative"

        per_field[field_id] = {
            "status": status,
            "expected": gt_result,
            "predicted": pred_result,
            "exact_match": gt_result == pred_result,
            "schweregrad": gt_field.get("schweregrad", "n/a"),
        }

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    exact_matches = sum(1 for v in per_field.values() if v.get("exact_match", False))
    total_evaluated = sum(1 for v in per_field.values() if "predicted" in v)

    return {
        "bank_id": ground_truth["bank_id"],
        "bank_name": ground_truth["bank_name"],
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "false_positive_rate": round(fpr, 4),
        "exact_match_rate": round(exact_matches / total_evaluated, 4) if total_evaluated > 0 else 0.0,
        "confusion_matrix": {"tp": tp, "fp": fp, "fn": fn, "tn": tn},
        "per_field": per_field,
        "missing_predictions": [k for k, v in per_field.items() if v.get("status") == "missing"],
    }


def false_positive_rate(results: dict) -> float:
    """Gibt die False-Positive-Rate aus einem evaluate_predictions-Ergebnis zurück."""
    return results["false_positive_rate"]


def print_report(results: dict) -> None:
    """Gibt einen formatierten Benchmark-Report auf stdout aus."""
    b = results["bank_id"]
    n = results["bank_name"]
    print(f"\n{'='*60}")
    print(f"BENCHMARK REPORT: {n} ({b})")
    print(f"{'='*60}")
    print(f"  Precision:          {results['precision']:.1%}")
    print(f"  Recall:             {results['recall']:.1%}")
    print(f"  F1-Score:           {results['f1']:.1%}")
    print(f"  False Positive Rate:{results['false_positive_rate']:.1%}")
    print(f"  Exact Match Rate:   {results['exact_match_rate']:.1%}")
    cm = results["confusion_matrix"]
    print(f"  Confusion Matrix:   TP={cm['tp']} FP={cm['fp']} FN={cm['fn']} TN={cm['tn']}")

    if results["missing_predictions"]:
        print(f"\n  FEHLENDE Vorhersagen: {results['missing_predictions']}")

    print(f"\n  Per-Field Ergebnisse:")
    for fid, r in results["per_field"].items():
        if r["status"] == "missing":
            print(f"    {fid:12s}  [MISSING]  erwartet: {r['expected']}")
        else:
            icon = {"true_positive": "✅", "true_negative": "✅",
                    "false_positive": "🔴 FP!", "false_negative": "🟡 FN!"}.get(r["status"], "?")
            match = "=" if r["exact_match"] else "≠"
            print(f"    {fid:12s}  {icon}  {r['predicted']:15s} {match} {r['expected']}")


def evaluate_all_banks(system_fn) -> list[dict]:
    """
    Evaluiert ein System gegen alle verfügbaren Banken.

    Args:
        system_fn: Callable(bank_id: str, docs_path: Path) -> dict[str, str]
                   Gibt Vorhersagen zurück: {prueffeld_id: ergebnis}

    Returns:
        Liste von evaluate_predictions-Ergebnissen
    """
    results = []
    for bank_dir in sorted(BANKS_DIR.iterdir()):
        if not bank_dir.is_dir() or not (bank_dir / "ground_truth.json").exists():
            continue
        bank_id = bank_dir.name
        print(f"\nEvaluiere: {bank_id} ...", flush=True)
        try:
            gt = load_ground_truth(bank_id)
            docs_path = bank_dir / "docs"
            predictions = system_fn(bank_id, docs_path)
            r = evaluate_predictions(gt, predictions)
            results.append(r)
            print_report(r)
        except Exception as e:
            print(f"  FEHLER: {e}", file=sys.stderr)
    return results


if __name__ == "__main__":
    # Demo: Zeige alle verfügbaren Banken
    print("Verfügbare Banken:")
    for bank_dir in sorted(BANKS_DIR.iterdir()):
        if bank_dir.is_dir() and (bank_dir / "ground_truth.json").exists():
            gt = load_ground_truth(bank_dir.name)
            n_fields = len(gt["prueffelder"])
            print(f"  {bank_dir.name:40s}  {gt['compliance_maturity']:12s}  {n_fields} Felder")
