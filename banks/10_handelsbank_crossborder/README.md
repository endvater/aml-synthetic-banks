# Bank 10 – Handelsbank CrossBorder GmbH

**Typ:** Handelsfinanzierungsbank / Trade Finance  
**Compliance-Reifegrad:** Mittel  
**Regulatorik:** GwG, KWG, AWG/AWV, EU-Sanktionsrecht  
**Gesamturteil:** Erhebliche Mängel

## Profil

Spezialisierte Handelsfinanzierungsbank mit ~180 Mitarbeitern, Fokus auf
Dokumentenakkreditive, Bankgarantien und Trade Finance für MENA- und
APAC-Märkte. Hohes TBML-Risiko, Sanktions-Screening-Lücken, Korrespondenzbanken
in Hochrisikoländern.

**Testfall für:** TBML-Typologien, Sanktions-Screening, AWG/AWV, Dual-Use-Güter, Korrespondenzbanken-Due-Diligence.

## Eingebaute Mängel

| Prüffeld | Ergebnis | Schweregrad | Kernmangel |
|---|---|---|---|
| S11-01 Sanctions Screening | NICHT KONFORM | Wesentlich | Sanctions-Liste veraltet, kein Waren-Screening |
| S03-05 TBML-TM | NICHT KONFORM | Wesentlich | Keine Preis-Plausibilisierung, kein Geo-Risiko |
| S02-08 Korrespondenzbanken | TEILKONFORM | Bedeutsam | EDD für 3 Hochrisiko-Korrespondenzbanken fehlt |
| S01-02 TBML-Risikoanalyse | TEILKONFORM | Bedeutsam | Länderrisiko-Matrix MENA veraltet |

## Status

> **TODO:** Dokumente generieren — `python banks/10_handelsbank_crossborder/generate.py`
