"""Pittige hoofdstukken bij Statistiek 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het digitale
examen van de Examencommissie (invul-, sleep-, dropdown- en meerkeuzevragen,
met eigen grafieken en tabellen; alleen combinaties, notaties zoals in de bijlage). Strikt binnen de gewone
hoofdstukken (beyond/bron/st_*.py). Kim op 24 november 2026: "ik wil gewoon
alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_statistiek.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Statistiek"
BESTAND = "beyond-statistiek-pittig.json"
AANTAL = 30

THEMAS = [
    ("problemen", "Problemen oplossen en ICT gebruiken"),
    ("telregels", "De telregels: product, som en complement"),
    ("combinaties", "Faculteit en combinaties"),
    ("binomiaal", "Kansvariabelen en de binomiale verdeling"),
    ("verwachting", "Verwachtingswaarde, variantie en standaardafwijking"),
    ("normaal", "De normale verdeling en standaardiseren"),
    ("steekproeven", "Populatie, steekproef en de steekproevenverdeling"),
    ("hypothese", "Hypothesen opstellen: H0, H1 en de richting"),
    ("pwaarde", "De p-waarde, het significantieniveau en de twee fouten"),
    ("betrouwbaarheid", "Betrouwbaarheidsinterval en foutenmarge"),
    ("spreidingsdiagram", "Spreidingsdiagrammen, trendlijn en correlatie"),
    ("ictkansen", "Kansen berekenen met de kansrekenmachine"),
    ("frequentietabel", "Frequentietabellen en gegevens groeperen"),
    ("grafieken", "De juiste grafische voorstelling kiezen"),
    ("kengetallen", "Centrummaten: gemiddelde, mediaan en modus"),
    ("spreiding", "Spreidingsmaten en de boxplot"),
    ("ictdata", "Een dataset doorrekenen met het rekenblad"),
    ("onderzoek", "Een statistisch onderzoek met de rekenapps"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_st_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
