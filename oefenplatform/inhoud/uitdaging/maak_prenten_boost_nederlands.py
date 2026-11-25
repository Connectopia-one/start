# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Nederlands 🚀 Boost doorstroom:
een lezersbrief en een kort verhaalfragment, allebei zelf geschreven
(Heidebeek is verzonnen).

    python3 inhoud/uitdaging/maak_prenten_boost_nederlands.py

De klikvakken in uitdaging/bron/boost_nederlands.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "nederlands-boost-uitdaging"
BRIEF = [
    "De gemeente Heidebeek wil de schoolstraat afsluiten voor auto's.",
    "Volgens de politie gebeurden daar vorig jaar zes ongevallen.",
    "Ik vind dat een uitstekend plan.",
    "Wie tegen is, wil blijkbaar dat er kinderen omvergereden worden.",
    "Bovendien gaan kinderen die te voet komen, frisser aan de les beginnen.",
    "Daarom moet de gemeente de straat al vanaf januari afsluiten.",
]
VERHAAL = [
    "Het regende al drie dagen in Heidebeek.",
    "Jonas stond aan het raam en dacht terug aan die zomer bij zijn opa.",
    "Toen scheen de zon elke dag en lachte het hele dorp.",
    "Nu leek het huis van de buren wel een grijze, natte spons.",
    "Plots ging de bel.",
    "Voor de deur stond iemand die hij al tien jaar niet meer had gezien.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "lezersbrief-schoolstraat.svg", "Lezersbrief: maak er een schoolstraat van!", BRIEF, grootte=22)
    blad(UIT / "verhaal-jonas.svg", "Uit een verhaal", VERHAAL, grootte=22)
