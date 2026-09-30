#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zet de wisselende woorden in de vragenbestanden van 🚀 Boost doorstroom.

    python3 inhoud/boost-doorstroom/bron/varianten_boost_doorstroom.py

De lijsten zelf staan per vak in `varianten_nl_boost.py` en
`varianten_en_boost.py`. Die van Nederlands worden ook door
`boost-dubbele-finaliteit/bron/varianten_boost_df.py` gebruikt: daar staan
precies dezelfde vragen in.

Het gereedschap staat in `inhoud/variantenwerk.py`, de uitleg voor Kim in
`inhoud/varianten/README.md`.
"""
import pathlib
import sys

HIER = pathlib.Path(__file__).parent
NIVEAU = HIER.parent
sys.path.insert(0, str(HIER))
sys.path.insert(0, str(NIVEAU.parent))

import variantenwerk  # noqa: E402  (pas na sys.path)
import varianten_en_boost  # noqa: E402
import varianten_nl_boost  # noqa: E402

VARIANTEN = {}
VARIANTEN.update(
    {("nederlands.json", titel): lijst for titel, lijst in varianten_nl_boost.HOOFDSTUKKEN.items()}
)
VARIANTEN.update(
    {("engels.json", titel): lijst for titel, lijst in varianten_en_boost.HOOFDSTUKKEN.items()}
)


def zet_varianten(bestand: str, stil: bool = False):
    """Zodat de bouwscripts de varianten na een bouw terug kunnen zetten."""
    return variantenwerk.zet_varianten(NIVEAU, bestand, VARIANTEN, stil)


def main():
    return variantenwerk.hoofdlijn(NIVEAU, "boost-doorstroom", VARIANTEN)


if __name__ == "__main__":
    raise SystemExit(main())
