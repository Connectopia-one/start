"""Pittige hoofdstukken bij Frans 🔧 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, op het niveau
van de vakfiche (ERK A2+). Strikt binnen de gewone hoofdstukken
(beyond-dubbele-finaliteit/bron/fr2_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Frans"
BESTAND = "beyond-df-frans-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Franse tekst lezen"),
    ("tekstsoorten", "Tekstsoorten en de bedoeling van een tekst"),
    ("cultuur", "De Franstalige wereld: gewoontes en reizen"),
    ("schrijven", "Schrijven en spreken in het Frans"),
    ("dagelijks", "Woordvelden: dagelijks leven, eten en wonen"),
    ("gezondheid", "Woordvelden: gezondheid, natuur en milieu"),
    ("school", "Woordvelden: school, werk, geld en verkeer"),
    ("kunst", "Woordvelden: kunst, geschiedenis en de samenleving"),
    ("wetenschap", "Woordvelden: wetenschap, techniek en taal"),
    ("determinanten", "Lidwoorden, aanwijzers, bezitters en getallen"),
    ("voornaamwoorden", "Voornaamwoorden en betrekkelijke bijzinnen"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels"),
    ("presens", "De tegenwoordige tijd en de gebiedende wijs"),
    ("verleden", "De verleden tijden"),
    ("toekomst", "De toekomende tijd en de conditionnel"),
    ("zinsbouw", "Zinsbouw, zinsdelen en congruentie"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_fr_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
