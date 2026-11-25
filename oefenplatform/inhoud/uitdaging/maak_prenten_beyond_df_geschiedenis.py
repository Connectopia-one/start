# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Geschiedenis 🌍 Beyond dubbele
finaliteit: een zelf geschreven (verzonnen) brief van een soldaat aan de
IJzer in 1916 en een lijst van zes gebeurtenissen uit de Belgische geschiedenis.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_geschiedenis.py

De klikvakken in uitdaging/bron/beyond_df_geschiedenis.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "geschiedenis-beyond-df-uitdaging"
BRIEF = [
    "Lieve moeder, ik schrijf je vanuit de loopgraaf bij Diksmuide.",
    "Het water staat tot aan onze knieën sinds de sluizen open zijn.",
    "Gisteren vielen er weer obussen vlak bij onze post.",
    "De officieren spreken enkel Frans tegen ons.",
    "De Duitsers zijn allemaal laffe barbaren.",
    "Ik hoop dat de oorlog voor Kerstmis voorbij is.",
]
BELGIE = [
    "Algemeen enkelvoudig stemrecht voor mannen",
    "De Belgische Revolutie",
    "De onafhankelijkheid van Congo",
    "België wordt een federale staat",
    "De Duitse inval in België in de Eerste Wereldoorlog",
    "De Koningskwestie",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "brief-ijzer-1916.svg", "Brief van een soldaat aan de IJzer, 1916 (verzonnen)", BRIEF, grootte=22)
    blad(UIT / "gebeurtenissen-belgie.svg", "Zes gebeurtenissen uit de Belgische geschiedenis", BELGIE, grootte=23)
