"""Pittige hoofdstukken bij geschiedenis 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, meteen in de vormen van het
examen van de Examencommissie, zoals bij geschiedenis 🌍 Beyond. Kim op 11
november 2026: elk lege vakje aanvullen, vanaf ✨ Spark in examenvorm; Boost
geschiedenis als proefvak. Geen extra leerstof: alles staat in de leerbundels
van geschiedenis Boost (leerbundels/bron/maak_geschiedenis_boost.py).

De vragen staan per thema in boost_geschiedenis_themas/. Prenten die Claude
zelf tekent: maak_prenten_geschiedenis_boost.py.
"""
import importlib

NIVEAU = "boost-doorstroom"
VAK = "Geschiedenis"
BESTAND = "boost-geschiedenis-pittig.json"
AANTAL = 30

THEMAS = [
    ("referentiekader", "Het historisch referentiekader"),
    ("rome_franken", "Van Rome naar de Franken"),
    ("standen_stad", "Standen, domein en stad"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.boost_geschiedenis_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
