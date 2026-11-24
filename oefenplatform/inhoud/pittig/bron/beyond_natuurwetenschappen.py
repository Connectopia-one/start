"""Pittige hoofdstukken bij Natuurwetenschappen 🌿 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op prenten. Strikt binnen de gewone
hoofdstukken (beyond/bron/nw_*.py en ww_*.py). Waar een thema samenvalt met
biologie, chemie of fysica Beyond, nemen we passende pittige vragen en
prenten van die vakken over (enkel wat binnen de gewone vragen
natuurwetenschappen valt) en vullen we aan met eigen vragen.
Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_natuurwetenschappen.py
en bouw_welzijnswetenschappen.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Natuurwetenschappen"
BESTAND = "beyond-natuurwetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("cel", "De cel: organellen, membranen en weefsels"),
    ("energie", "Fotosynthese en celademhaling"),
    ("afweer", "Bescherming en afweer tegen lichaamsvreemde stoffen"),
    ("voortplanting", "Voortplanting, zwangerschap en vruchtbaarheid"),
    ("dna", "DNA, replicatie en celdelingen"),
    ("overerving", "Overerving van genetisch materiaal"),
    ("genexpressie", "Genexpressie en DNA-technologie"),
    ("evolutie", "Ontstaan en evolutie van soorten"),
    ("biomoleculen", "Biomoleculen"),
    ("snelheid", "Snelheid van een chemische reactie"),
    ("evenwicht", "Chemisch evenwicht"),
    ("organisch", "Organische stoffen: classificatie, eigenschappen en toepassingen"),
    ("materialen", "Kunststoffen, nanomaterialen en duurzame chemie"),
    ("elektrostatica", "Elektrostatica"),
    ("elektromagnetisme", "Elektromagnetisme en inductie"),
    ("beweging", "Kracht en beweging"),
    ("trillingen", "Trillingen, golven en geluid"),
    ("spectrum", "Het elektromagnetisch spectrum"),
    ("kernfysica", "Kernfysica en radioactiviteit"),
    ("veilig", "Veilig en duurzaam werken, grootheden en eenheden"),
    ("onderzoek", "Onderzoeksvaardigheden en ontwerpen"),
    ("ww_enzymen", "Welzijnswetenschappen: Enzymen"),
    ("ww_spijsvertering", "Welzijnswetenschappen: Het spijsverteringsstelsel"),
    ("ww_uitscheiding", "Welzijnswetenschappen: Het uitscheidingsstelsel"),
    ("ww_bloed", "Welzijnswetenschappen: Het bloed"),
    ("ww_hart", "Welzijnswetenschappen: Het hart en de bloedsomloop"),
    ("ww_bloeddruk", "Welzijnswetenschappen: De bloeddruk en het lymfestelsel"),
    ("ww_ademhaling", "Welzijnswetenschappen: Het ademhalingsstelsel"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_nw_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
