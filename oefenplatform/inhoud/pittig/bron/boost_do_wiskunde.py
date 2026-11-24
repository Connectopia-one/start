"""Pittige hoofdstukken bij wiskunde 🚀 Boost doorstroom (wiskunde gevorderd).

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Geen extra leerstof: alles staat in de leerbundels en de
gewone hoofdstukken van wiskunde Boost doorstroom
(boost-doorstroom/bron/bouw_wiskunde.py, wi_*.py). Kim op 24 november 2026:
eerste vak van de pittige vragen voor heel Boost en Beyond.

De thematitels zijn dezelfde als bij de gewone hoofdstukken, zodat elk pittig
hoofdstuk naast zijn gewone delen komt te staan. Alle grafieken en schetsen
tekent Claude zelf: maak_prenten_wiskunde_boost_do.py.
"""
import importlib

NIVEAU = "boost-doorstroom"
VAK = "Wiskunde"
BESTAND = "boost-do-wiskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("problemen", "Een opgave aanpakken: van context naar wiskunde"),
    ("logica", "Logica: symbolen, waarheidstabellen en poorten"),
    ("reele", "Reële getallen, wortels en machten"),
    ("ordenen", "Ordenen, afronden, intervallen en wetenschappelijke notatie"),
    ("ruimte", "Rechten, vlakken en gelijkvormigheid"),
    ("pythagoras", "Pythagoras en de rechthoekige driehoek"),
    ("driehoek", "Sinusregel, cosinusregel en vectoren"),
    ("formules", "Formules omvormen en eerstegraadsvergelijkingen"),
    ("tweedegraad", "Stelsels en tweedegraadsvergelijkingen"),
    ("functies", "Functies en de rechte"),
    ("parabool", "De parabool, transformaties en functiekenmerken"),
    ("tellen", "Telproblemen met boom- en venndiagram"),
    ("statistiek", "Statistiek: voorstellingen, centrum en spreiding"),
    ("misleiding", "Misleiding met cijfers, en verbanden in een puntenwolk"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__ + '.' if __package__ else ''}boost_do_wiskunde_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
