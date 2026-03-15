# Bank 03 – FinTech Bank Digital GmbH

**Typ:** Neobank / Digitalbank  
**Compliance-Reifegrad:** Mittel  
**Regulatorik:** GwG, KWG, ZAG, PSD2  
**Gesamturteil:** Mängel

## Profil

Volldigitale Neobank mit API-only-Ansatz, ca. 80 Mitarbeitern und KI-basiertem
Transaction Monitoring (SaaS-Dienstleister). Technisch fortgeschritten, aber
lückenhafte Compliance-Dokumentation beim TM-Modell und ungeklärte
Auslagerungsverträge.

**Testfall für:** Digitale Geschäftsmodelle, KI-basiertes TM, Outsourcing-Compliance, eID-Verfahren.

## Eingebaute Mängel

| Prüffeld | Ergebnis | Schweregrad | Kernmangel |
|---|---|---|---|
| S09-01 Outsourcing TM | NICHT KONFORM | Bedeutsam | Kein § 6 Abs. 7 GwG-Auslagerungsvertrag |
| S03-01 KI-TM Dokumentation | TEILKONFORM | Bedeutsam | Kein XAI-Nachweis, kein Backtesting |
| S04-01 goAML-Integration | TEILKONFORM | Gering | Testumgebung fehlt |

## Status

> **TODO:** Dokumente generieren — `python banks/03_fintech_bank_digital/generate.py`
