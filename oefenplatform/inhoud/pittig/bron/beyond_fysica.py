"""Pittige hoofdstukken bij Fysica 🔭 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op zelfgetekende prenten
(maak_prenten_fys_beyond.py). Strikt binnen de gewone hoofdstukken
(beyond/bron/fy3_*.py). Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_fysica.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Fysica"
BESTAND = "beyond-fysica-pittig.json"
AANTAL = 30

THEMAS = [
    ("lading", "Elektrische lading, geleiders en influentie"),
    ("veld", "De wet van Coulomb en het elektrisch veld"),
    ("potentiaal", "Elektrische energie, potentiaal en spanning"),
    ("stroom", "Elektrodynamica: stroom, weerstand en schakelingen"),
    ("magneet", "Magneten en het magnetisch veld"),
    ("magkracht", "De magnetische kracht op een stroom en op een lading"),
    ("inductie", "Elektromagnetische inductie"),
    ("statica", "Statica: krachten, moment en evenwicht"),
    ("newton", "De wetten van Newton"),
    ("beweging", "Rechtlijnige beweging: ERB en EVRB"),
    ("worp", "De horizontale worp"),
    ("gravitatie", "De gravitatiekracht en de cirkelbeweging"),
    ("arbeid", "Arbeid, energie en vermogen"),
    ("gaswetten", "De gaswetten en de algemene gaswet"),
    ("warmte", "Warmteleer: temperatuur, warmte en faseovergangen"),
    ("trillingen", "Harmonische trillingen"),
    ("golven", "Golven en hun eigenschappen"),
    ("licht", "Licht, geluid en het elektromagnetisch spectrum"),
    ("kwantum", "Kwantumfysica: het foto-elektrisch effect en dualiteit"),
    ("kern", "De atoomkern, radioactief verval en halveringstijd"),
    ("straling", "Kernenergie, straling en haar effecten"),
    ("meten", "Veilig werken, meetinstrumenten en meetonzekerheid"),
    ("onderzoek", "Wetenschappelijk onderzoek, ontwerpen en STEM"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_fys_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
