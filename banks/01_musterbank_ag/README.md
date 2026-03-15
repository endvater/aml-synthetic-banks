# Bank 01 – Musterbank AG

**Typ:** Mittelgroße Universalbank  
**Compliance-Reifegrad:** Mittel  
**Regulatorik:** GwG, KWG §25h, MaRisk  
**Gesamturteil:** Erhebliche Mängel

## Profil

Die Musterbank AG ist eine fiktive mittelgroße deutsche Universalbank mit Privat-
und Firmenkundengeschäft, ca. 520 Mitarbeitern und einem breiten Produktangebot.
Sie dient als **Baseline-Testfall** mit realistisch gemischten Compliance-Mängeln.

## Eingebaute Mängel

| Prüffeld | Ergebnis | Schweregrad | Kernmangel |
|---|---|---|---|
| S01-02 Risikoanalyse | NICHT KONFORM | Wesentlich | Risikoanalyse veraltet seit Feb 2022 (>3 Jahre) |
| S03-01 TM-Kalibrierung | NICHT KONFORM | Bedeutsam | Schwellenwert 9.000 EUR ohne Begründung |
| S03-03 Alert-Rückstau | NICHT KONFORM | Bedeutsam | 847 überfällige Alerts, Ø 19 Tage Bearbeitung |
| S08-01 Interne Revision | NICHT KONFORM | Bedeutsam | IR-Prüfung AML >2 Jahre ausständig |
| S02-01 KYC wB-Abfrage | TEILKONFORM | Gering | 18% Firmenkunden ohne aktuelle wB-Abfrage |
| S05-01 Schulungen | TEILKONFORM | Gering | 72% Abdeckung (Ziel: 95%) |

## Dokumente

```
docs/
├── 01_gwb_bestellungsurkunde.pdf
├── 02_risikoanalyse_2022.pdf        ← NICHT KONFORM: Stand Feb 2022
├── 03_kyc_handbuch.pdf              ← TEILKONFORM: 18% Firmenkunden ohne wB
├── 04_tm_konzept.pdf                ← NICHT KONFORM: 847 Alerts, 9.000 EUR
├── 05_sar_verfahren.pdf
├── 06_schulungskonzept.pdf
├── 07_aufbewahrung_iks.pdf
├── gwb_jahresbericht_2024.pdf
├── tm_alerts_2024.xlsx              ← Rückstau-Evidenz (1.247 Alerts)
├── schulungsmatrix_2024.xlsx
├── sar_statistik_2024.csv
├── interview_gwb_dr_mueller.json    ← GwB bestätigt Mängel
├── interview_compliance.json
├── tm_system.log
└── goaml.log
```

## Generierung

```bash
python banks/01_musterbank_ag/generate.py --output banks/01_musterbank_ag/docs
```

## Nutzung als Benchmark

```python
from tools.evaluate import evaluate_bank
results = evaluate_bank("01_musterbank_ag", your_aml_system)
```
