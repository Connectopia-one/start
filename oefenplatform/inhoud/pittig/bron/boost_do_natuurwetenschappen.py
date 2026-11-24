"""Pittige hoofdstukken bij Natuurwetenschappen 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op zelfgetekende prenten
(maak_prenten_nw_boost_do.py). Strikt binnen de gewone hoofdstukken
(boost-doorstroom/bron/nw_*.py). Kim op 24 november 2026: na Nederlands
Beyond doorstroom dit vak, omdat er het meest op geoefend wordt.

De thematitels zijn dezelfde als in boost-doorstroom/bron/bouw_natuurwetenschappen.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Natuurwetenschappen"
BESTAND = "boost-do-natuurwetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("planten", "Water en homeostase bij planten"),
    ("prikkel", "Van prikkel tot reactie, en het oog"),
    ("zenuwstelsel", "Het zenuwstelsel"),
    ("spieren", "Spieren, klieren en hormonen"),
    ("voortplanting", "Voortplanting en de hormonale regeling"),
    ("micro", "Biodiversiteit en micro-organismen"),
    ("ecosysteem", "Gedrag, interactie en ecosystemen"),
    ("mengsels", "Mengsels en zuivere stoffen"),
    ("stoffen", "Enkelvoudige en samengestelde stoffen, en chemische reacties"),
    ("atoom", "De bouw van het atoom en het periodiek systeem"),
    ("binding", "Chemische bindingen en roosters"),
    ("namen", "Stoffen classificeren en benoemen"),
    ("water", "Stoffen in water, reacties en berekeningen"),
    ("beweging", "Rechtlijnige bewegingen"),
    ("krachten", "Vrije val, verticale worp en krachten"),
    ("druk", "Druk en de gaswetten"),
    ("energie", "Arbeid, energie, vermogen en rendement"),
    ("warmte", "Warmte en faseovergangen"),
    ("elektriciteit", "Elektriciteit en de wet van Ohm"),
    ("veilig", "Veilig werken, meten en levensreddend handelen"),
    ("onderzoek", "Grootheden, eenheden en wetenschappelijk onderzoek"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_nw_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
