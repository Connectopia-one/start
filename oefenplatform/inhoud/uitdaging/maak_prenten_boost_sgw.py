# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Sociale en gedragswetenschappen
🚀 Boost doorstroom: zes situaties uit de ontwikkeling en zes groepen.

    python3 inhoud/uitdaging/maak_prenten_boost_sgw.py

De klikvakken in uitdaging/bron/boost_sgw.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "sgw-boost-uitdaging"
SITUATIES = [
    "Een baby van vier maanden zoekt niet naar het speeltje onder de doek.",
    "Een kleuter zegt dat de maan hem volgt omdat ze hem lief vindt.",
    "Een kind van negen legt tien stokjes van klein naar groot.",
    "Een jongen van tien steelt geen snoep, omdat hij bang is voor straf.",
    "Een meisje van vijftien probeert elke maand een andere stijl en groep uit.",
    "Een vrouw van zeventig kijkt tevreden terug op haar leven.",
]
GROEPEN = [
    "Het gezin van Sara",
    "Alle supporters van dezelfde voetbalploeg",
    "Alle linkshandigen in België",
    "De mensen die samen op dezelfde bus wachten",
    "Een vakbond met statuten en duizenden leden",
    "Vijf vriendinnen die elke vrijdag afspreken",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "zes-situaties.svg", "Zes situaties uit een mensenleven", SITUATIES, grootte=21)
    blad(UIT / "zes-groepen.svg", "Zes verzamelingen mensen", GROEPEN, grootte=22)
