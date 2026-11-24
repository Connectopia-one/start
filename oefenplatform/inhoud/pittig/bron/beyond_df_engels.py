"""Pittige hoofdstukken bij Engels 🔧 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, op het niveau
van de vakfiche (ERK A2+). Strikt binnen de gewone hoofdstukken
(beyond-dubbele-finaliteit/bron/en2_*.py): geen past perfect, geen passieve vorm
en geen indirecte rede, want die staan niet in deze vakfiche.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Engels"
BESTAND = "beyond-df-engels-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Engelse tekst lezen"),
    ("tekstsoorten", "Tekstsoorten en de bedoeling van een tekst"),
    ("cultuur", "De Engelstalige wereld: gewoontes en reizen"),
    ("schrijven", "Schrijven, spreken en je beleving bij een tekst"),
    ("dagelijks", "Woordvelden: dagelijks leven, eten en wonen"),
    ("gezondheid", "Woordvelden: gezondheid, natuur en duurzaamheid"),
    ("school", "Woordvelden: school, werk, geld en verkeer"),
    ("kunst", "Woordvelden: kunst, geschiedenis en de samenleving"),
    ("wetenschap", "Woordvelden: wetenschap, techniek en taal"),
    ("naamwoorden", "Naamwoorden, lidwoorden en hoeveelheden"),
    ("voornaamwoorden", "Voornaamwoorden en betrekkelijke bijzinnen"),
    ("adjectieven", "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels"),
    ("tegenwoordig", "De tegenwoordige tijden en de present perfect"),
    ("verleden", "De verleden tijden"),
    ("toekomst", "De toekomende tijd en de modale hulpwerkwoorden"),
    ("zinsbouw", "Zinsbouw, zinsdelen en de voorwaardelijke bijzin"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_en_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
