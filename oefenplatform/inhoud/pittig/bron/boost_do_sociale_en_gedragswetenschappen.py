"""Pittige hoofdstukken bij sociale en gedragswetenschappen 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, met
zelfgetekende klikprenten. Strikt binnen de gewone hoofdstukken
(boost-doorstroom/bron/sg_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Sociale en gedragswetenschappen"
BESTAND = "boost-do-sociale-en-gedragswetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("ontwikkeling", "Ontwikkeling: groeien, rijpen en leren"),
    ("fysiek", "De fysieke ontwikkeling"),
    ("piaget", "De cognitieve ontwikkeling volgens Piaget"),
    ("kohlberg", "De morele ontwikkeling volgens Kohlberg"),
    ("hechting", "De sociale ontwikkeling en de gehechtheid"),
    ("erikson", "De psychosociale ontwikkeling volgens Erikson"),
    ("persoonlijkheid", "Persoonlijkheid, karakter en temperament"),
    ("zelfconcept", "Het zelfconcept: zelfbeeld en zelfwaardering"),
    ("emoties", "Emoties: componenten en functies"),
    ("motivatie", "Motivatie en attributies"),
    ("cultuur", "Cultuur en cultuuruitingen"),
    ("socialisatie", "Socialisatie, enculturatie en acculturatie"),
    ("instituties", "Sociale instituties"),
    ("groepen", "Sociale groepen en de typologie van Merton"),
    ("rollen", "Sociale positie, sociale rol en rollenconflicten"),
    ("status", "Sociale status en kansen in de samenleving"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_do_sg_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
