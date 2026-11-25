"""Pittige hoofdstukken bij Frans 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm (ERK B1), met
zelfgetekende klikprenten. Strikt binnen de gewone hoofdstukken
(boost-doorstroom/bron/fr_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Frans"
BESTAND = "boost-do-frans-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Franse tekst analyseren"),
    ("tekstsoorten", "Tekstsoorten, tekstverbanden en verwijswoorden"),
    ("cultuur", "De Franstalige wereld: omgangsvormen en gewoontes"),
    ("schrijven", "Schrijven, schriftelijke interactie en leesbeleving"),
    ("dagelijks", "Woordvelden: mens, gezondheid en het dagelijkse leven"),
    ("wereld", "Woordvelden: school, werk, reizen en de samenleving"),
    ("naamwoorden", "Zelfstandige naamwoorden, lidwoorden en determinanten"),
    ("voornaamwoorden", "Voornaamwoorden: COD, COI, y en en"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en de trappen"),
    ("tegenwoordig", "Présent, impératif en de wederkerende werkwoorden"),
    ("verleden", "Passé composé, imparfait en plus-que-parfait"),
    ("toekomst", "Futur, conditionnel en subjonctif"),
    ("zinsbouw", "Soorten zinnen, bijzinnen en si-zinnen"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_fr_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
