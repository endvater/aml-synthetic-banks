# Bank 08 – Krypto-Zahlungsbank AG

**Typ:** Krypto-Zahlungsdienstleister / VASP  
**Compliance-Reifegrad:** Niedrig  
**Regulatorik:** GwG, KWG, MiCA, FATF-VASP, EU 2023/1113  
**Gesamturteil:** Erhebliche Mängel

## Profil

Krypto-nativer Zahlungsdienstleister mit ca. 60 Mitarbeitern, VASP-Kundschaft,
DeFi-Protocol-Interaktionen und hoher SAR-Quote (8,3%). Travel Rule nur partiell
implementiert.

**Testfall für:** Travel Rule (EU 2023/1113), VASP-KYC, MiCA, DeFi-Risiken, Krypto-TM-Typologien.

## Eingebaute Mängel

| Prüffeld | Ergebnis | Schweregrad | Kernmangel |
|---|---|---|---|
| S10-01 Travel Rule | NICHT KONFORM | Wesentlich | Nur Transfers >1.000 EUR abgedeckt |
| S02-06 VASP-KYC | NICHT KONFORM | Wesentlich | 12 VASPs ohne FATF-Compliance-Nachweis |
| S04-02 SAR-Qualität | TEILKONFORM | Bedeutsam | SAR-Quote 8,3% mit schlechter Narrativ-Qualität |

## Status

> **TODO:** Dokumente generieren — `python banks/08_krypto_zahlungsbank/generate.py`
