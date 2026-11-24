"""Pittige hoofdstukken bij Aardrijkskunde 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (boost-doorstroom/bron/ak_*.py) staat. De
thema's in boost_ak_themas/ dienen voor doorstroom én dubbele finaliteit:
VRAGEN voor doorstroom, VRAGEN_DF voor dubbele finaliteit (zonder HDI,
transitiemodel, hiërarchie van steden, inbreiding, outsourcing, reconversie,
bodemerosie, albedo, ...). Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Aardrijkskunde"
BESTAND = "boost-do-aardrijkskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("situeren", "Waar ligt het, en hoe weet je dat?"),
    ("wonen", "Waar wonen de mensen?"),
    ("bevolking", "Hoe een bevolking verandert"),
    ("stad", "Stad en platteland"),
    ("grondstoffen", "Grondstoffen, energie en industrie"),
    ("landbouw", "Landbouw, handel en toerisme"),
    ("mondialisering", "Mondialisering"),
    ("duurzaam", "Duurzaam omgaan met de ruimte"),
    ("broeikas", "Het versterkte broeikaseffect"),
    ("onderzoek", "Een geografisch onderzoek voeren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_ak_themas"


def _vragen(m):
    return getattr(m, "VRAGEN", m.VRAGEN)


HOOFDSTUKKEN = [
    (titel, _vragen(importlib.import_module(f"{_PAK}.{naam}")))
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
