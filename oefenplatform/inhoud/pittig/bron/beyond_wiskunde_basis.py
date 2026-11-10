"""Pittige hoofdstukken bij wiskunde basis 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Strikt uit de vakfiches 2027_wiskunde_3DO_Basis, _WEL en
_BED, zonder extra leerstof. Kim op 9 november 2026: elk vak meteen volledig,
met gewone en pittige hoofdstukken.

De thematitels zijn dezelfde als in beyond/bron/bouw_wiskunde_basis.py. Zo komt
elk pittig hoofdstuk naast zijn gewone delen te staan, en laat de keuze "Ik leer
voor" (lib/leerrichting.ts) ook de pittige hoofdstukken weg die een richting
niet nodig heeft: dat werkt op het begin van de titel. Alle grafieken tekent
Claude zelf: maak_prenten_wiskunde_basis_beyond.py.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Wiskunde basis"
BESTAND = "beyond-wiskunde-basis-pittig.json"
AANTAL = 30

BED = "Bedrijfswetenschappen: "
THEMAS = [
    ("machten", "Machtswortels, machten en logaritmen"),
    ("grafisch", "Grafisch onderzoek van een functie"),
    ("tweedegraad", "Tweedegraadsfuncties"),
    ("tweedegraadsvgl", "Tweedegraadsvergelijkingen algebraïsch oplossen"),
    ("exponentieel", "Exponentiële functies en groeimodellen"),
    ("sinus", "De sinusfunctie en de goniometrische cirkel"),
    ("vergelijkingen", "Vergelijkingen grafisch oplossen"),
    ("afgeleiden", "Afgeleiden: helling en raaklijn"),
    ("rijen", "Rekenkundige en meetkundige rijen"),
    ("kansen", "Kansrekenen met kansbomen en kruistabellen"),
    ("steekproeven", "Steekproeven, samenhang en causaliteit"),
    ("normaal", "De normale verdeling"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__ + '.' if __package__ else ''}beyond_wiskunde_basis_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
