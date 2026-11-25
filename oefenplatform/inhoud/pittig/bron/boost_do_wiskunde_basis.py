"""Pittige hoofdstukken bij wiskunde basis 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Strikt binnen de gewone hoofdstukken van wiskunde basis
Boost doorstroom (boost-doorstroom/bron/bouw_wiskunde_basis.py, wb_*.py),
zonder extra leerstof. Kim op 24 november 2026: "werk daar dan maar aan verder".

De thematitels zijn dezelfde als bij de gewone hoofdstukken, zodat elk pittig
hoofdstuk naast zijn gewone delen komt te staan. Alle grafieken en schetsen
tekent Claude zelf: maak_prenten_wiskunde_basis_boost_do.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Wiskunde basis"
BESTAND = "boost-do-wiskunde-basis-pittig.json"
AANTAL = 30

THEMAS = [
    ("reele_getallen", "De reële getallen, wortels en machten"),
    ("ordenen", "Getallen ordenen, afronden en intervallen"),
    ("logica", "Logica: bewerkingen en waarheidstabellen"),
    ("bewijzen", "Redeneren, bewijzen en tegenvoorbeelden"),
    ("ruimte", "Ruimtefiguren, vlakke voorstellingen en vectoren"),
    ("gelijkvormig", "Schaalverandering en gelijkvormige figuren"),
    ("pythagoras", "Pythagoras en de goniometrische verhoudingen"),
    ("formules", "Formules omvormen"),
    ("vergelijkingen", "Eerstegraadsvergelijkingen en -ongelijkheden"),
    ("stelsels", "Stelsels van twee vergelijkingen"),
    ("tweedegraad", "Tweedegraadsvergelijkingen"),
    ("functies", "Het functiebegrip en de eerstegraadsfunctie"),
    ("parabool", "De tweedegraadsfunctie en haar parabool"),
    ("telproblemen", "Telproblemen en problemen oplossen"),
    ("statistiek", "Gegevens weergeven en samenvatten"),
    ("verbanden", "Verbanden tussen twee grootheden"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_wb_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
