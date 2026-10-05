#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zet de wisselende woorden in het vragenbestand van 🚀 Boost dubbele finaliteit.

    python3 inhoud/boost-dubbele-finaliteit/bron/varianten_boost_df.py

Nederlands en Engels. De lijsten komen uit `varianten_nl_boost.py` en
`varianten_en_boost.py` bij doorstroom, want `bouw_nederlands.py` en
`bouw_engels.py` van allebei de categorieën lezen dezelfde thema's.

Bij Nederlands zijn alle hoofdstukken met varianten woord voor woord hetzelfde
gebleven. Bij Engels niet: de pronouns, de tijden en de zinsbouw zijn hier
aangepast aan het A2-niveau, en die hoofdstukken hebben ook een andere titel
gekregen. Daarom staan hieronder alleen de drie thema's die onveranderd zijn
gebleven; een variant op een vraag die hier niet meer staat, zou het script
toch doen stoppen.
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
import varianten_en_boost  # noqa: E402

# De Engelse thema's die bij dubbele finaliteit onveranderd bleven, met
# dezelfde hoofdstuktitel als bij doorstroom.
ENGELS_ONVERANDERD = (
    "Nouns, articles, quantifiers en numerals",
    "Adjectives, adverbs, comparatives en voorzetsels",
    "De tegenwoordige tijden",
)

VARIANTEN = {
    ("nederlands.json", titel): lijst for titel, lijst in varianten_nl_boost.HOOFDSTUKKEN.items()
}
VARIANTEN.update(
    {
        ("engels.json", titel): lijst
        for titel, lijst in varianten_en_boost.HOOFDSTUKKEN.items()
        if titel.rsplit(" — ", 1)[0] in ENGELS_ONVERANDERD
    }
)


def zet_varianten(bestand: str, stil: bool = False):
    """Zodat bouw_nederlands.py de varianten na een bouw terug kan zetten."""
    return variantenwerk.zet_varianten(NIVEAU, bestand, VARIANTEN, stil)


def main():
    return variantenwerk.hoofdlijn(NIVEAU, "boost-dubbele-finaliteit", VARIANTEN)


if __name__ == "__main__":
    raise SystemExit(main())
