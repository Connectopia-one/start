#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zet de wisselende woorden in het vragenbestand van 🚀 Boost dubbele finaliteit.

    python3 inhoud/boost-dubbele-finaliteit/bron/varianten_boost_df.py

Enkel Nederlands: bij dubbele finaliteit is dat het enige taalvak dat er al
staat. De lijst komt uit `varianten_nl_boost.py` bij doorstroom, want
`bouw_nederlands.py` van allebei de categorieën leest dezelfde `nl_*.py` en
de vragen zijn dus woord voor woord dezelfde.
"""
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
NIVEAU = HIER.parent
DOORSTROOM = NIVEAU.parent / "boost-doorstroom" / "bron"
sys.path.insert(0, str(DOORSTROOM))
sys.path.insert(0, str(NIVEAU.parent))

import variantenwerk  # noqa: E402  (pas na sys.path)
import varianten_nl_boost  # noqa: E402

VARIANTEN = {
    ("nederlands.json", titel): lijst for titel, lijst in varianten_nl_boost.HOOFDSTUKKEN.items()
}


def zet_varianten(bestand: str, stil: bool = False):
    """Zodat bouw_nederlands.py de varianten na een bouw terug kan zetten."""
    return variantenwerk.zet_varianten(NIVEAU, bestand, VARIANTEN, stil)


def main():
    return variantenwerk.hoofdlijn(NIVEAU, "boost-dubbele-finaliteit", VARIANTEN)


if __name__ == "__main__":
    raise SystemExit(main())
