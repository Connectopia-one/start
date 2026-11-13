"""Pittige hoofdstukken bij filosofie en recht 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie (digitaal: invul-, sleep-, dropdown- en
meerkeuzevragen, vaak bij een bron). Strikt binnen de gewone hoofdstukken
(beyond/bron/fr_*.py): geen filosoof, stelling of boek dat daar niet staat.
Kim op 13 november 2026: na wiskunde Boost dubbele finaliteit dit vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_filorecht.py, zodat elk
pittig hoofdstuk naast zijn gewone delen komt te staan. De prenten tekent
Claude zelf: maak_prenten_filorecht_beyond.py.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Filosofie en recht"
BESTAND = "beyond-filosofie-en-recht-pittig.json"
AANTAL = 30

THEMAS = [
    ("eigenheid", "De eigenheid van de filosofie"),
    ("kennis", "Bronnen van kennis, rationalisme en empirisme"),
    ("falsificatie", "Van natuurfilosofie naar wetenschap: falsificatie en demarcatie"),
    ("lichaamgeest", "Lichaam en geest: monisme en dualisme"),
    ("mensdier", "Cultuur en natuur: mens, dier en machine"),
    ("vrijheid1", "Vrijheid en determinisme van de oudheid tot de 19de eeuw"),
    ("vrijheid2", "Vrijheid en determinisme in de 20ste eeuw"),
    ("ethiek", "Ethiek: basisbegrippen en vier benaderingen"),
    ("gevolgplicht", "Gevolgenethiek en plichtethiek"),
    ("deugdzorg", "Deugdethiek en zorgethiek"),
    ("geluk", "Ethiek en geluk"),
    ("argumentatie", "Argumentatieleer: redeneervormen en drogredenen"),
    ("rechtsstaat", "De democratische rechtsstaat en haar principes"),
    ("machten", "De scheiding der machten en de rechterlijke macht"),
    ("justitie", "De functies van justitie, de rechtspraak en de deontologie"),
    ("actueel", "Actuele thema's binnen recht"),
    ("buitengerechtelijk", "Buitengerechtelijke procedures en juridische bijstand"),
    ("piramide", "De gerechtelijke piramide: rechtbanken en hoven"),
    ("procedures", "Burgerlijk recht en strafrecht: het verloop van een procedure"),
    ("actoren", "Juridische termen en actoren"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__ + '.' if __package__ else ''}beyond_filorecht_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
