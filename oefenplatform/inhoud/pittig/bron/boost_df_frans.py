"""Pittige hoofdstukken bij Frans 🛠️ Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, op het niveau van
de vakfiche (ERK A2). Strikt binnen de gewone hoofdstukken
(boost-dubbele-finaliteit/bron/frdf_*.py). Een deel van de vragen komt uit Frans
Beyond dubbele finaliteit, telkens enkel waar de leerstof dezelfde is; de rest
zijn eigen teksten en vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Frans"
BESTAND = "boost-df-frans-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Franse tekst begrijpen"),
    ("tekstsoorten", "Tekstsoorten, tekstverbanden en leesstrategieën"),
    ("cultuur", "De Franstalige wereld: omgangsvormen en gewoontes"),
    ("schrijven", "Schrijven, schriftelijke interactie en leesbeleving"),
    ("spreken", "Spreken, gesprekken, klank en spelling"),
    ("mens", "Woordvelden: mens, familie, gevoelens en gezondheid"),
    ("dagelijks", "Woordvelden: eten, kleding, wonen en winkelen"),
    ("school", "Woordvelden: school, werk en de professionele wereld"),
    ("onderweg", "Woordvelden: tijd, weer, reizen en vervoer"),
    ("naamwoorden", "Zelfstandige naamwoorden, lidwoorden en determinanten"),
    ("voornaamwoorden", "Voornaamwoorden: sujet, COD, COI en de wederkerende"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en de trappen"),
    ("tegenwoordig", "Présent, impératif en de wederkerende werkwoorden"),
    ("verleden", "Passé composé, imparfait en passé récent"),
    ("toekomst", "Futur proche, futur simple en de conditionnel de politesse"),
    ("zinsbouw", "Zinsbouw, zinsdelen, voegwoorden en de overeenkomst"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_fr_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
