"""Pittige hoofdstukken bij Biologie 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Veel pittige
vragen van natuurwetenschappen Boost doorstroom (met hun prenten), enkel wat
in de gewone hoofdstukken (boost-doorstroom/bron/bi_*.py) staat, plus eigen
vragen en een eigen prent van het oor (maak_prenten_bi_boost_do.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Biologie"
BESTAND = "boost-do-biologie-pittig.json"
AANTAL = 30

THEMAS = [
    ("planten", "Homeostase en waterhuishouding bij planten"),
    ("zenuwstelsel", "Van prikkel tot reactie en het zenuwstelsel"),
    ("oog", "Het oog"),
    ("oor", "Het oor en het evenwicht"),
    ("spieren", "De spieren en de klieren"),
    ("voortplanting", "Voortplanting en de menstruatiecyclus"),
    ("micro", "Biodiversiteit en micro-organismen"),
    ("gedrag", "Gedrag en interactie"),
    ("stromen", "Materie- en energiestromen in een ecosysteem"),
    ("kringlopen", "Kringlopen, voedselrelaties en de mens"),
    ("ehbo", "Levensreddend handelen"),
    ("onderzoek", "Wetenschappelijk onderzoek en STEM"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_bi_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
