# Bank 07 – Compliance-Bank Musterhaft AG ✅

**Typ:** Mittelgroße Universalbank  
**Compliance-Reifegrad:** Hoch  
**Regulatorik:** GwG, KWG, MaRisk, DORA  
**Gesamturteil:** Keine Mängel

## ⚠️ POSITIV-BENCHMARK

Diese Bank ist **absichtlich vollständig compliant**. Alle Prüffelder sollen
`KONFORM` ergeben. Dieser Testfall dient ausschließlich zur Messung der
**False-Positive-Rate** eines AML-AI-Systems.

Ein gutes System sollte hier **0 Mängel** finden.
Jeder gemeldete Mangel ist ein False Positive.

## Verwendung

```python
from tools.evaluate import evaluate_bank, false_positive_rate

results = evaluate_bank("07_compliance_bank_musterhaft", your_system)
fp_rate = false_positive_rate(results)
print(f"False Positive Rate: {fp_rate:.1%}")  # Ziel: < 5%
```

## Status

> **TODO:** Dokumente generieren — `python banks/07_compliance_bank_musterhaft/generate.py`
