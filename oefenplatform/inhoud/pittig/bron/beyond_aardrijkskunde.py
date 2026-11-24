"""Pittige hoofdstukken bij Aardrijkskunde 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op zelfgetekende prenten
(maak_prenten_ak_beyond.py). Strikt binnen de gewone hoofdstukken
(beyond/bron/ak_*.py). Kim op 24 november 2026: na Natuurwetenschappen Boost
doorstroom dit vak, omdat er veel op geoefend wordt.

De thematitels zijn dezelfde als in beyond/bron/bouw_aardrijkskunde.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Aardrijkskunde"
BESTAND = "beyond-aardrijkskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("situeren", "Situeren, kaarten en observatie"),
    ("heelal", "Het heelal: ontstaan en afstanden"),
    ("zonnestelsel", "De zon en het zonnestelsel"),
    ("bewegingen", "De bewegingen van de aarde"),
    ("maan", "De maan, getijden en verduisteringen"),
    ("atmosfeer", "De opbouw van de atmosfeer"),
    ("wind", "Luchtdruk en winden"),
    ("neerslag", "Neerslag en de kringloop van het water"),
    ("weer", "Klimaatgebieden, biomen en zeestromen"),
    ("weerkaart", "Het weer in Europa"),
    ("geosfeer", "De opbouw van de geosfeer"),
    ("platentektoniek", "Platentektoniek en reliëfvorming"),
    ("vulkanen", "Aardbevingen en vulkanisme"),
    ("gesteenten", "Gesteenten, mineralen en datering"),
    ("verwering", "Verwering, karst en massatransport"),
    ("erosie", "Erosie door water, ijs en wind"),
    ("klimaatgeologisch", "Klimaat doorheen de geologische tijd"),
    ("klimaatnu", "De huidige klimaatverandering"),
    ("ruimte", "Verstedelijking en ruimtegebruik"),
    ("duurzaam", "Duurzaam ruimtegebruik"),
    ("landschap", "Het landschap lezen"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_ak_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
