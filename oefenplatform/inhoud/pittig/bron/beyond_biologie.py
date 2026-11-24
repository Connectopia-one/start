"""Pittige hoofdstukken bij Biologie 🧬 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op zelfgetekende prenten
(maak_prenten_bio_beyond.py). Strikt binnen de gewone hoofdstukken
(beyond/bron/bi3_*.py). Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_biologie.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Biologie"
BESTAND = "beyond-biologie-pittig.json"
AANTAL = 30

THEMAS = [
    ("cel", "De cel, de organellen en de biologische membranen"),
    ("weefsels", "Celdifferentiatie, weefsels en celtypes"),
    ("enzymen", "Enzymen, transport door membranen en osmose"),
    ("energie", "Fotosynthese, celademhaling en gisting"),
    ("afweer", "Niet-specifieke en specifieke afweer"),
    ("immunisatie", "Immunisatie, bloedgroepen en falende afweer"),
    ("gametogenese", "Gametogenese en de hormonale regeling"),
    ("bevruchting", "Bevruchting, embryo en foetus"),
    ("vruchtbaarheid", "Vruchtbaarheid regelen en behandelen"),
    ("dna", "DNA, RNA en de replicatie"),
    ("celdeling", "De celcyclus, mitose en meiose"),
    ("overerving", "Overerving en de wetten van Mendel"),
    ("genexpressie", "Genexpressie: transcriptie en translatie"),
    ("genregulatie", "Genregulatie, epigenetica en nature of nurture"),
    ("mutaties", "Mutaties, mutagenen en kanker"),
    ("dnatechnologie", "DNA-technologie en gentechnologie"),
    ("evolutie", "Argumenten voor evolutie en de evolutietheorieën"),
    ("selectie", "Selectie, soortvorming en de menswording"),
    ("biomoleculen", "Biomoleculen: sachariden, lipiden en proteïnen"),
    ("veilig", "Veilig en duurzaam werken in het labo"),
    ("onderzoek", "Wetenschappelijk onderzoek, ontwerpen en STEM"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_bio_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
