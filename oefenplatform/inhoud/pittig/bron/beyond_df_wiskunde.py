"""Pittige hoofdstukken bij Wiskunde 🔧 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Vooral pittige
vragen van wiskunde basis Beyond (met hun prenten), enkel wat in de gewone
hoofdstukken (beyond-dubbele-finaliteit/bron/wi_*.py) staat, plus eigen vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Wiskunde"
BESTAND = "beyond-df-wiskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("problemen", "Problemen oplossen: van situatie naar wiskunde"),
    ("machten", "Machtswortels en machten met rationale exponent"),
    ("logaritmen", "Logaritmen"),
    ("grafiek", "Een functie aflezen van haar grafiek"),
    ("verandering", "Gemiddelde verandering en het differentiequotiënt"),
    ("exponentieel", "Exponentiële functies"),
    ("groei", "Lineaire en exponentiële groeimodellen"),
    ("kansen", "Kansen en de wet van Laplace"),
    ("kansboom", "Kansbomen: product, som en complement"),
    ("steekproef", "Populatie, steekproef en representativiteit"),
    ("causaliteit", "Samenhang en causaliteit"),
    ("normaal", "De normale verdeling en de Gausskromme"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_wi_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
