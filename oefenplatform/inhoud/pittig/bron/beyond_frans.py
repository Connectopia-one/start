"""Pittige hoofdstukken bij Frans 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie (lezen bij een tekst, woordenschat, grammatica,
schrijven). Strikt binnen de gewone hoofdstukken (beyond/bron/fr_*.py).
Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_frans.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Frans"
BESTAND = "beyond-frans-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Franse tekst analyseren"),
    ("tekstsoorten", "Tekstsoorten en de bedoeling van een tekst"),
    ("cultuur", "De Franstalige wereld: omgangsvormen en gewoontes"),
    ("literatuur", "Literaire teksten en literatuurbeleving"),
    ("schrijven", "Schrijven en schriftelijke interactie"),
    ("dagelijks", "Woordvelden: de mens, gezondheid, eten en wonen"),
    ("samenleving", "Woordvelden: school, werk, reizen en de samenleving"),
    ("naamwoorden", "Naamwoorden, lidwoorden en determinanten"),
    ("voornaamwoorden", "Voornaamwoorden: COD, COI, y en en"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en de trappen"),
    ("verleden", "De verleden tijden en de accord van het deelwoord"),
    ("wijzen", "Futur, conditionnel, subjonctif en de gérondif"),
    ("zinsbouw", "Zinsbouw, indirecte rede en de passieve zin"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_fr_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
