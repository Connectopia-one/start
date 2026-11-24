"""Pittige hoofdstukken bij Fysica 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Veel pittige
vragen van natuurwetenschappen Boost doorstroom (met hun prenten), enkel wat
in de gewone hoofdstukken (boost-doorstroom/bron/fy_*.py) staat, plus eigen
vragen. Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Fysica"
BESTAND = "boost-do-fysica-pittig.json"
AANTAL = 30

THEMAS = [
    ("grootheden", "Grootheden, eenheden en nauwkeurig meten"),
    ("erb", "Eenparig rechtlijnige beweging"),
    ("evrb", "Versnelde beweging, vrije val en verticale worp"),
    ("krachten", "Krachten, krachtenbalans en zwaartekracht"),
    ("evenwicht", "Archimedeskracht, moment en evenwicht"),
    ("druk", "Druk bij vaste stoffen en in vloeistoffen"),
    ("gassen", "Gassen, temperatuur en de gaswetten"),
    ("energie", "Arbeid, energie, vermogen en rendement"),
    ("warmte", "Warmte, faseovergangen en de warmtebalans"),
    ("elektriciteit", "Elektrische stroom, spanning en weerstand"),
    ("optica", "Licht: weerkaatsing, breking en lenzen"),
    ("onderzoek", "Veilig werken, meten en onderzoek"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_fy_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
