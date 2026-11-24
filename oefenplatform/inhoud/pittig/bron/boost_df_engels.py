"""Pittige hoofdstukken bij Engels 🚀 Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (en_*.py en endf_*.py) staat. VRAGEN_DF
waar het thema er een heeft: zonder modale hulpwerkwoorden, past perfect,
going to, betrekkelijke voornaamwoorden en conditionals (niveau A2). Plus de
twee eigen thema's spreken en klank. Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Engels"
BESTAND = "boost-df-engels-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Engelse tekst analyseren"),
    ("tekstsoorten", "Tekstsoorten, tekstverbanden en verwijswoorden"),
    ("schrijven", "Schrijven, schriftelijke interactie en literatuurbeleving"),
    ("spreken", "Spreken, gesprekken en hoe je beoordeeld wordt"),
    ("cultuur", "De Engelstalige wereld: gewoontes en conventies"),
    ("dagelijks", "Woordvelden: mensen, gezondheid en het dagelijkse leven"),
    ("wereld", "Woordvelden: school, werk, reizen en de samenleving"),
    ("naamwoorden", "Nouns, articles, quantifiers en numerals"),
    ("voornaamwoorden", "Pronouns: de vijf soorten en de onbepaalde woorden"),
    ("adjectieven", "Adjectives, adverbs, comparatives en voorzetsels"),
    ("tegenwoordig", "De tegenwoordige tijden"),
    ("verleden", "Past simple, past continuous en de toekomst met will"),
    ("zinsbouw", "Zinsdelen, soorten zinnen en samengestelde zinnen"),
    ("klank", "Klank, klemtoon, intonatie en spelling"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_en_themas"


def _vragen(m):
    return getattr(m, "VRAGEN_DF", m.VRAGEN)


HOOFDSTUKKEN = [
    (titel, _vragen(importlib.import_module(f"{_PAK}.{naam}")))
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
