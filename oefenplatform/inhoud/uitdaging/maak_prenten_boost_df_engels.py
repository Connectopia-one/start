# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Engels 🚀 Boost dubbele
finaliteit: een verzonnen mededeling van een zwembad in zes zinnen en zes
losse zinnen waarvan er drie een fout bevatten.

    python3 inhoud/uitdaging/maak_prenten_boost_df_engels.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad, zone  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "engels-boost-df-uitdaging"

ZWEMBAD = [
    "From 6 to 19 April, Parkside Pool will be closed to the public.",
    "Because the old heating system broke down, we must replace it.",
    "During these two weeks, you can swim at the Lakeview Centre.",
    "Please bring your Parkside card, so you do not pay twice.",
    "However, the Lakeview Centre has no diving board.",
    "We are sorry for the trouble and hope to see you again soon!",
]

ZINNEN = [
    "She has lived in Leeds since three years.",
    "My brother doesn't like cold weather.",
    "Yesterday we went to the beach with our cousins.",
    "The childs were playing football in the garden.",
    "He is the most tall boy in our class.",
    "I will call you when I get home tonight.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "mededeling-zwembad.svg", "Parkside Pool – news (verzonnen)", ZWEMBAD, grootte=22)
    blad(UIT / "zes-zinnen.svg", "Zes zinnen", ZINNEN, cursief=True, grootte=23)
    print({i: zone(i, 6) for i in range(1, 7)})
