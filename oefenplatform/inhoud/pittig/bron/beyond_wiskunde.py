"""Pittige hoofdstukken bij wiskunde 🌍 Beyond doorstroom (wiskunde gevorderd).

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Geen extra leerstof: alles staat in de leerbundels en de
gewone hoofdstukken van wiskunde Beyond doorstroom (beyond/bron/bouw_wiskunde.py).
Kim op 24 november 2026: overal pittige hoofdstukken, vak per vak.

De thematitels zijn dezelfde als bij de gewone hoofdstukken, zodat elk pittig
hoofdstuk naast zijn gewone delen komt te staan. Alle grafieken en schetsen
tekent Claude zelf: maak_prenten_wiskunde_beyond.py.
"""
import importlib
import importlib.util

NIVEAU = "beyond-doorstroom"
VAK = "Wiskunde"
BESTAND = "beyond-wiskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("machten", "Machtswortels, machten en logaritmen"),
    ("veeltermen", "Veeltermen, deelbaarheid en Horner"),
    ("vergelijkingen", "Vergelijkingen en ongelijkheden oplossen"),
    ("aflezen", "Een functie aflezen van haar grafiek"),
    ("tweedegraad", "Tweedegraadsfuncties en transformaties"),
    ("exponentieel", "Exponentiële en logaritmische functies"),
    ("goniometrie", "Goniometrische functies en goniometrie"),
    ("limieten", "Limieten, continuïteit en asymptoten"),
    ("afgeleiden", "Afgeleiden en het verloop van een functie"),
    ("rijen", "Rijen en hun limiet"),
    ("primitieven", "Primitieven en de onbepaalde integraal"),
    ("integraal", "De bepaalde integraal en haar toepassingen"),
    ("complex", "Complexe getallen"),
    ("tellen", "Telproblemen en het binomium"),
    ("kans", "Kansrekenen en kansverdelingen"),
    ("normaal", "Statistiek: normale verdeling en hypothesetoets"),
    ("matrices", "Matrices en hun bewerkingen"),
    ("stelsels", "Stelsels oplossen en matrixmodellen"),
    ("groepen", "Algebraïsche structuren en groepen"),
    ("vectoren", "Punten, vectoren en afstanden in de ruimte"),
    ("ruimte", "Rechten en vlakken in de ruimte"),
    ("programmeren", "Programmeren: algoritmen en structuren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_wiskunde_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if importlib.util.find_spec(f"{_PAK}.{naam}")
]
