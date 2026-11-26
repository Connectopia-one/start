"""Pittige hoofdstukken bij Duits 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (boost-doorstroom/bron/de_*.py) staat en
enkel schriftelijk: lezen, schrijven, woordenschat en grammatica. Kim op
26 november 2026: "werk het dan maar helemaal uit".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Duits"
BESTAND = "boost-do-duits-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Duitse tekst lezen"),
    ("tekstsoorten", "Tekstsoorten, signaalwoorden en verwijswoorden"),
    ("schrijven", "Schrijven en schriftelijke interactie"),
    ("ich", "Woordvelden: ik, mijn familie, mijn lichaam en kleding"),
    ("alltag", "Woordvelden: thuis, eten, winkelen en media"),
    ("welt", "Woordvelden: school, werk, vrije tijd, reizen en weer"),
    ("naamwoorden", "Lidwoorden, meervoud en naamvallen"),
    ("voornaamwoorden", "Voornaamwoorden: persoonlijk, bezittelijk, aanwijzend en vragend"),
    ("praesens", "Präsens en Imperativ"),
    ("perfekt", "Perfekt en Futur"),
    ("zinsbouw", "Zinsbouw: soorten zinnen, Satzklammer en voegwoorden"),
    ("voorzetsels", "Voorzetsels, telwoorden, bijwoorden en uitspraak"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_de_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
