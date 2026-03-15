#!/usr/bin/env python3
"""
Bank 01 – Musterbank AG – Dokumenten-Generator

Ruft den zentralen Generator auf und schreibt die Dokumente
nach banks/01_musterbank_ag/docs/.

Verwendung:
    python banks/01_musterbank_ag/generate.py
    python banks/01_musterbank_ag/generate.py --output /tmp/musterbank
"""
import argparse
import sys
from pathlib import Path

# Zentralen Generator importieren
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools"))
from generate_bank import generate_musterbank_ag

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", default=str(Path(__file__).parent / "docs"))
    args = p.parse_args()
    generate_musterbank_ag(args.output)

if __name__ == "__main__":
    main()
