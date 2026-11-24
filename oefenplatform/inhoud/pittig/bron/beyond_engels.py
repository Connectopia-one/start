"""Pittige hoofdstukken bij Engels 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie (lezen bij een tekst, woordenschat, grammatica,
schrijven). Strikt binnen de gewone hoofdstukken (beyond/bron/en3_*.py).
Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_engels.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Engels"
BESTAND = "beyond-engels-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Engelse tekst analyseren"),
    ("tekstsoorten", "Tekstsoorten en de bedoeling van een tekst"),
    ("dagelijks", "Woordvelden: wonen, eten en vrije tijd"),
    ("gezondheid", "Woordvelden: gezondheid, natuur en duurzaamheid"),
    ("school", "Woordvelden: school, werk, geld en verkeer"),
    ("cultuur", "Woordvelden: kunst, literatuur, politiek en reizen"),
    ("wetenschap", "Woordvelden: wetenschap, techniek en taal"),
    ("naamwoorden", "Naamwoorden, lidwoorden en hoeveelheden"),
    ("voornaamwoorden", "Voornaamwoorden en betrekkelijke bijzinnen"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels"),
    ("tegenwoordig", "De tegenwoordige tijden en de present perfect"),
    ("verleden", "De verleden tijden"),
    ("modalen", "De toekomst, de modale hulpwerkwoorden en de gerund"),
    ("zinsbouw", "Zinsbouw, indirecte rede en de passieve vorm"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_en_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
