"""Pittige hoofdstukken bij Latijn 🚀 Boost doorstroom.

Eén hoofdstuk per groep teksten, telkens dertig vragen, in examenvorm. Eigen
vragen, enkel over de teksten, woorden en grammatica die in de gewone
hoofdstukken (boost-doorstroom/bron/latijn/) staan. Kim op
26 november 2026: "werk het dan maar helemaal uit".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Latijn"
BESTAND = "boost-do-latijn-pittig.json"
AANTAL = 30

THEMAS = [
    ("caesar", "Caesar: De bello Gallico"),
    ("ovidius_a", "Ovidius: Pyramus en Thisbe"),
    ("ovidius_b", "Ovidius: goden, kunstenaars en uitvinders"),
    ("natuur", "Natuurfenomenen: Plinius, Gellius, Ammianus, de zondvloed en Galilei"),
    ("geloof", "Geloof en bijgeloof: Plinius en Trajanus, Petronius, Erasmus en de Malleus"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_lat_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
