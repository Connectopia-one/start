"""Pittige hoofdstukken bij Chemie ⚗️ Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie, met klikvragen op zelfgetekende prenten
(maak_prenten_chem_beyond.py). Strikt binnen de gewone hoofdstukken
(beyond/bron/ch3_*.py). Kim op 24 november 2026: "ik wil gewoon alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_chemie.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Chemie"
BESTAND = "beyond-chemie-pittig.json"
AANTAL = 30

THEMAS = [
    ("anorganisch", "Anorganische stoffen: stofklassen en naamgeving"),
    ("organisch", "Organische stoffen: stofklassen en naamgeving"),
    ("isomerie", "Isomerie en chiraliteit"),
    ("atoom", "Atoombouw, orbitalen en het periodiek systeem"),
    ("binding", "Atoombinding en lewisstructuren"),
    ("eigenschappen", "Ruimtelijke structuur, polariteit en intermoleculaire krachten"),
    ("rekenen", "Chemisch rekenen: mol, molaire massa en concentratie"),
    ("stoichiometrie", "Stoichiometrie, overmaat en de algemene gaswet"),
    ("snelheid", "Reactiesnelheid, botsingsmodel en energiediagram"),
    ("evenwicht", "Chemisch evenwicht en de wet van Le Chatelier"),
    ("zuren", "Zuren en basen en het doorgeven van protonen"),
    ("ph", "pH, pOH en rekenen met zuren en basen"),
    ("buffers", "Buffers en zuurbasetitraties"),
    ("redox", "Oxidatiegetallen en redoxreacties"),
    ("cellen", "Galvanische cellen en elektrolyse"),
    ("corrosie", "Toepassingen van redox: batterijen, galvaniseren en corrosie"),
    ("reactietypes", "Organische reacties: substitutie en het radicalaire mechanisme"),
    ("additie", "Organische reacties: additie, eliminatie en condensatie"),
    ("kunststoffen", "Kunststoffen: polymeren en hun eigenschappen"),
    ("nano", "Nanomaterialen"),
    ("duurzaam", "Duurzame chemie en de circulaire economie"),
    ("veilig", "Veilig werken, meetinstrumenten en beduidende cijfers"),
    ("onderzoek", "Wetenschappelijk onderzoek, ontwerpen en STEM"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_chem_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
