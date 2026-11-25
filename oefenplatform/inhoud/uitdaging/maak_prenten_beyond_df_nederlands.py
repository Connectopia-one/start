# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Nederlands 🌍 Beyond dubbele
finaliteit: een lezersbrief en een verhaalfragment, allebei zelf geschreven.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_nederlands.py

De klikvakken in uitdaging/bron/beyond_df_nederlands.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "nederlands-beyond-df-uitdaging"
BRIEF = [
    "Onze gemeente wil het zwembad sluiten om geld te besparen.",
    "Het zwembad kost de gemeente elk jaar 400 000 euro.",
    "Toch is dat een slechte beslissing, want kinderen leren er zwemmen.",
    "Bovendien gebruiken drie scholen het zwembad elke week.",
    "De schepen die dit voorstelt, kan zelf niet eens zwemmen.",
    "Daarom vraag ik de gemeenteraad om het zwembad open te houden.",
]
VERHAAL = [
    "De bel ging. Noor bleef nog even zitten.",
    "Ze voelde haar hart bonzen toen ze aan het examen dacht.",
    "'Kom je?' riep Amir vanuit de gang.",
    "Buiten stormde het, de bomen bogen bijna dubbel.",
    "Twee jaar eerder had ze dezelfde zenuwen gehad.",
    "Ze haalde diep adem en stond op.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "lezersbrief-zwembad.svg", "Lezersbrief: red ons zwembad!", BRIEF, grootte=22)
    blad(UIT / "verhaal-noor.svg", "Uit een verhaal", VERHAAL, grootte=23)
