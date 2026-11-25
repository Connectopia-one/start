"""Pittige hoofdstukken bij Nederlands 🚀 Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Acht thema's
zijn woord voor woord dezelfde leerstof als bij doorstroom en nemen die
pittige vragen over; betekenis is aangepast (enkel ironie, overdrijving en
woordspeling). Argumenteren (zonder drogredenen), literatuur en communiceren
zijn nieuw, met eigen klikprenten (boekenplank, presentatie, sollicitatiemail).
Strikt binnen de gewone hoofdstukken (boost-dubbele-finaliteit/bron/bouw_nederlands.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Nederlands"
BESTAND = "boost-df-nederlands-pittig.json"
AANTAL = 30

THEMAS = [
    ("communicatie", "Zender, ruis en de zeven tekstsoorten"),
    ("samenhang", "Hoofdgedachte, alinea en structuuraanduiders"),
    ("argumenteren", "Feit en mening, stelling, argument en conclusie"),
    ("bronkritiek", "Bronnen wegen: objectief, gekleurd of nep"),
    ("variatie", "Standaardtaal, tussentaal en register"),
    ("woordsoorten", "De woordsoorten op een rij"),
    ("werkwoorden", "Werkwoorden, tijden en woordvorming"),
    ("zinsdelen", "Zinsdelen en samengestelde zinnen"),
    ("spelling", "Spelling, leestekens en klanken"),
    ("betekenis", "Betekenis, beeldspraak en gevoelswaarde"),
    ("literatuur", "Fictie, personages, verhaallijn, tijd en ruimte"),
    ("communiceren", "Lichaamstaal, beleefdheid en een tekst die werkt"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_nl_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
