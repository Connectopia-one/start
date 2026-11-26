"""Pittige hoofdstukken bij kunstbeschouwing en filosofie 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie. Kim op 26 november 2026 (vraag van een ouder): het
vak kwam erbij naast filosofie en recht.

De filosofiethema's die beide vakken delen, gebruiken dezelfde pittige vragen
als filosofie en recht (beyond_filorecht_themas): een leerling volgt maar één
van de twee vakken. De kunstthema's, de zijnsleer en de politieke filosofie
zijn nieuw (beyond_kf_themas), strikt binnen beyond/bron/kfb_*.py. De
prenten tekent Claude zelf: maak_prenten_kf_beyond.py.

De thematitels zijn dezelfde als in beyond/bron/bouw_kunstbeschouwing_en_filosofie.py.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Kunstbeschouwing en filosofie"
BESTAND = "beyond-kunstbeschouwing-en-filosofie-pittig.json"
AANTAL = 30

THEMAS = [
    ("kf", "kunstvormen", "Kunst, cultuur en de kunstvormen"),
    ("kf", "inhoud", "Inhoud, functies en context van een kunstuiting"),
    ("kf", "oudheid", "Kunst van de prehistorie, Egypte en de klassieke oudheid"),
    ("kf", "middeleeuwen", "Middeleeuwen, renaissance en barok"),
    ("kf", "modern", "Van romantiek tot popart: moderne en hedendaagse kunst"),
    ("kf", "elementen", "Niet-westerse invloeden en kunsthistorische elementen"),
    ("kf", "analyse", "Kunstanalyse en kunstreflectie"),
    ("fr", "eigenheid", "De eigenheid van de filosofie"),
    ("fr", "lichaamgeest", "Lichaam en geest: monisme en dualisme"),
    ("fr", "mensdier", "Cultuur en natuur: mens, dier en machine"),
    ("fr", "vrijheid1", "Vrijheid en determinisme van de oudheid tot de 19de eeuw"),
    ("fr", "vrijheid2", "Vrijheid en determinisme in de 20ste eeuw"),
    ("fr", "ethiek", "Ethiek: basisbegrippen en vier benaderingen"),
    ("fr", "gevolgplicht", "Gevolgenethiek en plichtethiek"),
    ("fr", "deugdzorg", "Deugdethiek en zorgethiek"),
    ("fr", "geluk", "Ethiek en geluk"),
    ("kf", "zijnsleer", "Zijnsleer: schijn en werkelijkheid, worden en zijn"),
    ("fr", "kennis", "Bronnen van kennis, rationalisme en empirisme"),
    ("fr", "falsificatie", "Van natuurfilosofie naar wetenschap: falsificatie en demarcatie"),
    ("fr", "argumentatie", "Argumentatieleer: redeneervormen en drogredenen"),
    ("kf", "polfil1", "Politieke filosofie: individu, gemeenschap en legitimiteit"),
    ("kf", "polfil2", "Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid"),
]

PAKKET = {"kf": "beyond_kf_themas", "fr": "beyond_filorecht_themas"}
_VOOR = __package__ + "." if __package__ else ""


def _laad(soort, naam):
    try:
        return importlib.import_module(f"{_VOOR}{PAKKET[soort]}.{naam}").VRAGEN
    except ModuleNotFoundError:
        return None


HOOFDSTUKKEN = [
    (titel, vragen)
    for soort, naam, titel in THEMAS
    if (vragen := _laad(soort, naam)) is not None
]
