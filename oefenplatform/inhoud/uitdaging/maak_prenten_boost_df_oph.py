# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Ontwikkeling en pedagogisch
handelen 🚀 Boost dubbele finaliteit: zes verzonnen observatienotities uit
een kinderopvang en zes verzonnen uitspraken van kinderen en jongeren.

    python3 inhoud/uitdaging/maak_prenten_boost_df_oph.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "oph-boost-df-uitdaging"

NOTITIES = [
    "Lotte (4) stapelt zes blokken op elkaar en roept: 'Een toren!'",
    "Mehdi is altijd lui als we moeten opruimen.",
    "Sara huilt drie minuten als mama vertrekt, daarna speelt ze verder.",
    "Kinderen uit grote gezinnen delen nooit graag hun speelgoed.",
    "Tom zit in de hoek en kijkt tien minuten naar twee spelende kinderen.",
    "Ik denk dat Nina boos is, want ze is vast moe van gisteren.",
]

UITSPRAKEN = [
    "'De zon is moe, ze gaat slapen achter de berg.'",
    "'Ik pik geen snoep, want dan krijg ik straf van papa.'",
    "'Het is evenveel water, je hebt het alleen in een breder glas gegoten.'",
    "'Wat zou er gebeuren als er op aarde geen zwaartekracht was?'",
    "'Ik hou me aan de afspraken, want zo hoort het in onze klas.'",
    "'Als ik mijn ogen dichtdoe, kan niemand mij zien.'",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "zes-notities.svg", "Zes observatienotities (verzonnen)", NOTITIES, grootte=21)
    blad(UIT / "zes-uitspraken.svg", "Zes uitspraken (verzonnen)", UITSPRAKEN, cursief=True, grootte=21)
