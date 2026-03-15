# Contributing to aml-synthetic-banks

Danke für dein Interesse! Dieses Repo lebt von Community-Beiträgen.

## Was wir brauchen

### 1. Neue Banken (Banks 02–10: Dokumente generieren)
Die `ground_truth.json` und `README.md` für alle 10 Banken existieren.
Jetzt brauchen wir die Dokument-Generatoren und die synthetischen Dokumente.

**Bearbeitungsstatus:**

| Bank | ground_truth.json | Generator | Dokumente |
|---|:---:|:---:|:---:|
| 01 Musterbank AG | ✅ | ✅ | 🔧 |
| 02 Sparkasse Nordhafen | ✅ | ❌ | ❌ |
| 03 FinTech Bank Digital | ✅ | ❌ | ❌ |
| 04 Kapitalanlagebank Premium | ✅ | ❌ | ❌ |
| 05 EuroCredit Bank | ✅ | ❌ | ❌ |
| 06 Volksbank Manufaktur | ✅ | ❌ | ❌ |
| 07 Compliance-Bank Musterhaft | ✅ | ❌ | ❌ |
| 08 Krypto-Zahlungsbank | ✅ | ❌ | ❌ |
| 09 Förderbank Westland | ✅ | ❌ | ❌ |
| 10 Handelsbank CrossBorder | ✅ | ❌ | ❌ |

### 2. Neue Regulatoriken
- `DORA` (Digital Operational Resilience Act)
- `MaRisk` §25a KWG Risikomanagement
- `AMLA` (EU Anti-Money Laundering Authority – ab 2027)

### 3. Qualitätsverbesserungen bestehender ground_truth.json
- Mehr Prüffelder pro Bank
- Detailliertere Mängelbeschreibungen
- Confidence-Mindestwerte kalibrieren

## Wie man eine neue Bank beiträgt

```bash
# 1. Fork + Clone
git clone https://github.com/YOUR_USER/aml-synthetic-banks.git
cd aml-synthetic-banks

# 2. Branch
git checkout -b feat/bank-02-sparkasse-nordhafen

# 3. Generator erstellen (Vorlage: banks/01_musterbank_ag/generate.py)
cp banks/01_musterbank_ag/generate.py banks/02_sparkasse_nordhafen/generate.py
# ... anpassen ...

# 4. Dokumente generieren
python banks/02_sparkasse_nordhafen/generate.py

# 5. Evaluierung mit finreg-agents testen (optional)
python tools/evaluate.py

# 6. PR öffnen
```

## Anforderungen an Dokumente

- **Fiktiv**: Alle Personen, Zahlen, Adressen sind erfunden
- **Realistisch**: Orientiert an echten deutschen Bankdokumenten
- **Konsistent**: Mängel müssen in mehreren Dokumenten kreuzreferenziert sein
- **ground_truth-konform**: Generierte Mängel müssen zur `ground_truth.json` passen

## Hinweis

Alle Beiträge werden unter der MIT-Lizenz veröffentlicht.
Das Repo dient ausschließlich als Testdatensatz für KI-Systeme.
Kein Bezug zu realen Instituten.
