"""Pittige hoofdstukken bij Nederlands 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, met eigen
korte teksten, gedichtjes en zelfgetekende klikprenten (communicatiemodel,
verdacht bericht, zinnen in woorden en zinsdelen, spanningsboog). Strikt
binnen de gewone hoofdstukken (boost-doorstroom/bron/nl_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Nederlands"
BESTAND = "boost-do-nederlands-pittig.json"
AANTAL = 30

THEMAS = [
    ("communicatie", "Zender, ruis en de zeven tekstsoorten"),
    ("samenhang", "Hoofdgedachte, alinea en structuuraanduiders"),
    ("argumenteren", "Argumenteren: stelling, argumentsoort en drogreden"),
    ("bronkritiek", "Bronnen wegen: objectief, gekleurd of nep"),
    ("variatie", "Standaardtaal, tussentaal en register"),
    ("woordsoorten", "De woordsoorten op een rij"),
    ("werkwoorden", "Werkwoorden, tijden en woordvorming"),
    ("zinsdelen", "Zinsdelen en samengestelde zinnen"),
    ("spelling", "Spelling, leestekens en klanken"),
    ("betekenis", "Betekenis, beeldspraak en gevoelswaarde"),
    ("verhaal", "Verhalen ontleden: verteller, tijd en ruimte"),
    ("poezie", "Poëzie, drama en literaire stromingen"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_nl_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
