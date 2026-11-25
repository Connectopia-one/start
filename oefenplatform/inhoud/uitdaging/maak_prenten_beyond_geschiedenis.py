# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Geschiedenis 🌍 Beyond
doorstroom: een zelf geschreven (verzonnen) dagboekfragment uit 1846 en een
lijst van zes gebeurtenissen uit de 20ste eeuw.

    python3 inhoud/uitdaging/maak_prenten_beyond_geschiedenis.py

De klikvakken in uitdaging/bron/beyond_geschiedenis.py gebruiken _blad.zone.
"""
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "geschiedenis-beyond-uitdaging"
DAGBOEK = [
    "Ik sta elke dag om vijf uur op en werk tot acht uur 's avonds.",
    "Mijn dochter van negen werkt sinds de winter mee in de spinnerij.",
    "Sinds de aardappeloogst mislukte, kunnen we het brood amper betalen.",
    "De fabrieksbazen zijn allemaal hardvochtige gierigaards.",
    "Men zegt dat arbeiders in de stad zich in het geheim verenigen.",
    "Ik hoop dat de regering ooit naar mensen zoals wij zal luisteren.",
]
GEBEURTENISSEN = [
    "De val van de Berlijnse Muur",
    "De Russische Oktoberrevolutie",
    "De beurskrach van Wall Street",
    "De onafhankelijkheid van Congo",
    "De conferentie van Jalta",
    "Het Verdrag van Rome",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "dagboek-1846.svg", "Uit het dagboek van een Gentse arbeidster, 1846 (verzonnen)", DAGBOEK, grootte=22)
    blad(UIT / "gebeurtenissen-20ste-eeuw.svg", "Zes gebeurtenissen uit de 20ste eeuw", GEBEURTENISSEN, grootte=23)
