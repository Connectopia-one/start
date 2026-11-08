"""Pittige hoofdstukken bij geschiedenis 🌍 Beyond.

Eén hoofdstuk per thema, telkens dertig vragen, meteen in de vormen van het
examen van de Examencommissie: tabellen, keuzelijsten, koppelen, slepen,
volgorde, klikken op een prent, open vragen en casussen met bronnen.

Kim op 6 november 2026: per pittig hoofdstuk 30 vragen in plaats van 20, alles
strikt uit de vakfiche (2027_geschiedenis_3DDO), zonder extra leerstof. Op 8
november koos ze geschiedenis Beyond als proefvak, na reviews dat Beyond te
veel pure theorie is en te weinig zoals op het examen.

De vragen staan per thema in beyond_geschiedenis_themas/. Elk themabestand
heeft ook een lijst PRENTEN; maak_prentenlijst.py zet die samen voor Kim.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Geschiedenis"
BESTAND = "beyond-geschiedenis-pittig.json"
AANTAL = 30

THEMAS = [
    ("referentiekader", "Het historisch referentiekader"),
    ("restauratie_belgie", "Restauratie, revolutie en het ontstaan van België"),
    ("industrialisatie", "Industrialisatie en de sociale kwestie"),
    ("imperialisme", "Modern imperialisme, Congo en China"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.beyond_geschiedenis_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
