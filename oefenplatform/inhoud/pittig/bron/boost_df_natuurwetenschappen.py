"""Pittige hoofdstukken bij Natuurwetenschappen 🚀 Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Veel pittige
vragen van natuurwetenschappen Boost doorstroom (met hun prenten), zonder wat
deze fiche niet vraagt (indeling van het leven, atoommassa, arbeid, formules
van energievormen, specifieke en latente warmte, warmtetransport, vrije val,
veerconstante, hydrostatische druk, Pascal, gaswetten), plus eigen vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Natuurwetenschappen"
BESTAND = "boost-df-natuurwetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("feedback", "Biologische feedback en homeostase"),
    ("micro", "Micro-organismen, het microbioom en bewaring"),
    ("voortplanting", "Voortplanting en de hormonale regeling"),
    ("mengsels", "Mengsels en zuivere stoffen"),
    ("stoffen", "Chemische formules en chemische reacties"),
    ("atoom", "De bouw van het atoom en het periodiek systeem"),
    ("energie", "Energieomzettingen, vermogen en rendement"),
    ("warmte", "Warmte, faseovergangen en inwendige energie"),
    ("krachten", "Kracht als vector en bewegingstoestand"),
    ("druk", "Druk in het dagelijkse leven"),
    ("elektriciteit", "Elektriciteit, de wet van Ohm en veiligheid"),
    ("veilig", "Veilig werken, meten en levensreddend handelen"),
    ("onderzoek", "Grootheden, eenheden en wetenschappelijk onderzoek"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_nw_themas"


def _vragen(m):
    return m.VRAGEN


HOOFDSTUKKEN = [
    (titel, _vragen(importlib.import_module(f"{_PAK}.{naam}")))
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
