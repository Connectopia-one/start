"""Pittige hoofdstukken bij kunstbeschouwing en filosofie 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, met
zelfgetekende klikprenten. Strikt binnen de gewone hoofdstukken
(boost-doorstroom/bron/kb_*.py en fi_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Kunstbeschouwing en filosofie"
BESTAND = "boost-do-kunstbeschouwing-en-filosofie-pittig.json"
AANTAL = 30

THEMAS = [
    ("cultuur", "Kunst als deel van een cultuur"),
    ("kunstvormen", "De kunstvormen"),
    ("periodes", "Kunst van de prehistorie tot de middeleeuwen"),
    ("stromingen", "Kunststromingen van de renaissance tot vandaag"),
    ("inhoud", "Samenlevingen, inhoud en context van een kunstuiting"),
    ("vormgeving", "Richtvragen en de middelen van vormgeving"),
    ("eigenheid", "De eigenheid van de filosofie"),
    ("oorsprong", "De oorsprong van de westerse filosofie"),
    ("vragen", "Soorten vragen en de filosofische vraag"),
    ("domeinen", "De filosofische domeinen"),
    ("vaardigheden", "De filosofische vaardigheden"),
    ("lichaam_geest", "Lichaam en geest"),
    ("mens_dier", "Mens en dier"),
    ("ethische_stromingen", "De ethische stromingen en hun filosofen"),
    ("moraal", "Begrippen uit de moraalfilosofie"),
    ("vraagstukken", "Ethische vraagstukken analyseren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_kf_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
