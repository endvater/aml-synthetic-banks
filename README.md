# aml-synthetic-banks

**Open-Source Benchmark: 10 synthetische Finanzinstitute für AML/GwG-KI-Systeme**

Ein realistischer, maschinenlesbarer Testdatensatz für die Evaluierung von
AML-AI-Systemen – ähnlich wie SQuAD für NLP oder MLPerf für Hardware.

> ⚠️ Alle Banken, Personen und Dokumente sind vollständig **fiktiv**.
> Kein Bezug zu realen Instituten. Nicht für reale Prüfungen geeignet.

---

## Die 10 Banken

| # | Bank | Typ | Compliance-Reifegrad | Gesamturteil |
|---|---|---|:---:|---|
| 01 | [Musterbank AG](banks/01_musterbank_ag/) | Mittelgroße Universalbank | Mittel | Erhebliche Mängel |
| 02 | [Sparkasse Nordhafen](banks/02_sparkasse_nordhafen/) | Kleine Regionalbank | **Niedrig** | Erhebliche Mängel |
| 03 | [FinTech Bank Digital GmbH](banks/03_fintech_bank_digital/) | Neobank | Mittel | Mängel |
| 04 | [Kapitalanlagebank Premium AG](banks/04_kapitalanlagebank_premium/) | Private Banking | **Niedrig-Mittel** | Erhebliche Mängel |
| 05 | [EuroCredit Bank S.A.](banks/05_eurocredit_bank/) | Ausländische Tochter | Mittel | Mängel |
| 06 | [Volksbank Manufaktur eG](banks/06_volksbank_manufaktur/) | Genossenschaftsbank | Mittel | Mängel |
| 07 | [**Compliance-Bank Musterhaft AG**](banks/07_compliance_bank_musterhaft/) ✅ | Universalbank | **Hoch** | **Keine Mängel** |
| 08 | [Krypto-Zahlungsbank AG](banks/08_krypto_zahlungsbank/) | VASP | **Niedrig** | Erhebliche Mängel |
| 09 | [Förderbank Westland AöR](banks/09_foerderbank_westland/) | Öffentlich-rechtlich | Hoch | Geringfügige Mängel |
| 10 | [Handelsbank CrossBorder GmbH](banks/10_handelsbank_crossborder/) | Trade Finance | Mittel | Erhebliche Mängel |

**Bank 07** ist der Positiv-Benchmark (False-Positive-Test).

---

## Struktur

```
aml-synthetic-banks/
├── banks/
│   ├── 01_musterbank_ag/
│   │   ├── docs/               # Synthetische PDFs, Excel, Logs, Interviews
│   │   ├── ground_truth.json   # Erwartete Bewertungen je Prüffeld
│   │   ├── generate.py         # Dokumenten-Generator
│   │   └── README.md
│   └── 02_sparkasse_nordhafen/
│       ├── ground_truth.json
│       └── README.md
├── schemas/
│   ├── ground_truth_schema.json    # JSON Schema für ground_truth.json
│   └── document_metadata_schema.json
├── tools/
│   ├── generate_bank.py        # Zentraler Dokumenten-Generator
│   └── evaluate.py             # Benchmark-Runner
├── CONTRIBUTING.md
├── requirements.txt
└── README.md
```

---

## Schnellstart

### Musterbank AG (Bank 01) Dokumente generieren

```bash
pip install -r requirements.txt
python banks/01_musterbank_ag/generate.py
ls banks/01_musterbank_ag/docs/
```

### Eigenes System evaluieren

```python
from tools.evaluate import load_ground_truth, evaluate_predictions, print_report

# 1. Ground Truth laden
gt = load_ground_truth("01_musterbank_ag")

# 2. Dein System auf die Dokumente loslassen
# predictions = your_aml_system.run("banks/01_musterbank_ag/docs")
# Format: {"S01-01": "konform", "S01-02": "nicht_konform", ...}

# 3. Evaluieren
results = evaluate_predictions(gt, predictions)
print_report(results)
```

### Ausgabe-Beispiel

```
============================================================
BENCHMARK REPORT: Musterbank AG (01_musterbank_ag)
============================================================
  Precision:          87.5%
  Recall:             70.0%
  F1-Score:           77.8%
  False Positive Rate: 5.9%
  Exact Match Rate:   69.2%

  Per-Field Ergebnisse:
    S01-01        ✅  konform         = konform
    S01-02        ✅  nicht_konform   = nicht_konform
    S03-01        🔴 FP!  konform    ≠ nicht_konform
    S03-03        ✅  nicht_konform   = nicht_konform
    ...
```

---

## ground_truth.json Format

```json
{
  "bank_id": "01_musterbank_ag",
  "bank_name": "Musterbank AG",
  "compliance_maturity": "mittel",
  "gesamturteil": "erhebliche_maengel",
  "prueffelder": [
    {
      "id": "S01-02",
      "titel": "Aktualität der Risikoanalyse",
      "ergebnis": "nicht_konform",
      "schweregrad": "wesentlich",
      "maengel": ["Risikoanalyse datiert auf Feb 2022 - keine Aktualisierung seit >3 Jahren"],
      "rechtsgrundlagen": ["§ 5 Abs. 2 GwG"],
      "relevante_dokumente": ["02_risikoanalyse_2022.pdf"],
      "erwartete_confidence_min": 0.55
    }
  ]
}
```

Vollständiges Schema: [schemas/ground_truth_schema.json](schemas/ground_truth_schema.json)

---

## Abgedeckte Regulatoriken

| Regulatorik | Banken | Prüffelder |
|---|---|---|
| GwG (alle §§) | alle | S01-S08 |
| KWG §25h TM | 01, 02, 03, 04, 06, 09, 10 | S03 |
| KWG §25b Outsourcing | 03, 05 | S09 |
| MiCA / FATF-VASP | 08 | S10 |
| EU 2023/1113 Travel Rule | 05, 08 | S02, S10 |
| AWG/AWV Sanktionen | 10 | S11 |
| TBML Trade Finance | 06, 10 | S03, S11 |
| GwG-Ausnahmen §3 Abs. 2 | 09 | S02 |

---

## Für wen ist dieses Repo?

- **RegTech-Entwickler**: Teste dein AML-AI-System auf standardisierten Daten
- **Compliance-Teams**: Demo-Material ohne echte Kundendaten
- **Forschung**: Reproduzierbare Benchmarks für Paper und Evaluierungen
- **Ausbildung**: Realistische GwG-Prüfungsszenarien für Schulungen

---

## Beitragen

Alle Dokument-Generatoren (Banks 02–10) brauchen noch Implementierungen!
→ [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Lizenz

MIT License – frei nutzbar, modifizierbar und redistribuierbar.

---

## Verwandte Projekte

- [endvater/finreg-agents](https://github.com/endvater/finreg-agents) – Das AML-AI-Framework, das diesen Benchmark nutzt
- [FinCrime Watchdog](https://watchdog.endvater.de) – Blog-Begleitung zum Projekt

---

*Entstanden aus dem [FinRegAgents v2 Härtetest-Artikel](https://watchdog.endvater.de/2026/03/08/finregagents-v2-wie-ein-ki-agent-heute-eine-gwg-sonderpruefung-der-musterbank-ag-durchgefuehrt-hat-und-was-dabei-alles-schiefgelaufen-ist/) vom 08. März 2026.*
