"""Pittige hoofdstukken bij Chemie 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Veel pittige
vragen van natuurwetenschappen Boost doorstroom (met hun prenten), enkel wat
in de gewone hoofdstukken (boost-doorstroom/bron/ch_*.py) staat, plus eigen
vragen. Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Chemie"
BESTAND = "boost-do-chemie-pittig.json"
AANTAL = 30

THEMAS = [
    ("mengsels", "Mengsels, zuivere stoffen en scheidingstechnieken"),
    ("stoffen", "Enkelvoudige en samengestelde stoffen"),
    ("reacties", "Chemische reacties en energie"),
    ("atoom", "De bouw van atomen en ionen"),
    ("pse", "Het periodiek systeem der elementen"),
    ("bindingen", "Chemische bindingen en roosters"),
    ("anorganisch", "Anorganische stofklassen en naamgeving"),
    ("organisch", "Organische stoffen en de alkanen"),
    ("water", "Stoffen in water: polariteit, oplossen en pH"),
    ("reactietypes", "Neerslag-, gas-, neutralisatie- en redoxreacties"),
    ("rekenen", "Rekenen met mol, massa en concentratie"),
    ("onderzoek", "Veilig werken, meten en onderzoek"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_ch_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
