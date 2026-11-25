"""Pittige hoofdstukken bij ontwikkeling en pedagogisch handelen 🚀 Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, met
zelfgetekende klikprenten. Strikt binnen de gewone hoofdstukken
(boost-dubbele-finaliteit/bron/op_*.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Ontwikkeling en pedagogisch handelen"
BESTAND = "boost-df-ontwikkeling-en-pedagogisch-handelen-pittig.json"
AANTAL = 30

THEMAS = [
    ("welbevinden", "Welzijn en welbevinden"),
    ("determinanten", "Wat bepaalt onze gezondheid"),
    ("basisbegrippen", "Ontwikkeling: de basisbegrippen"),
    ("fysiek", "De fysieke en motorische ontwikkeling"),
    ("piaget", "Het denken volgens Piaget"),
    ("kohlberg_erikson", "Kohlberg en Erikson"),
    ("socio_emotioneel", "De socio-emotionele ontwikkeling"),
    ("volwassenen", "De volwassene en de oudere"),
    ("observeren", "Waarnemen en observeren"),
    ("rapporteren", "Rapporteren en respectvol omgaan"),
    ("behoeften", "Gedrag en behoeften"),
    ("communicatie", "Communiceren en actief luisteren"),
    ("feedback", "Feedback en verbindend communiceren"),
    ("vrije_tijd", "Vrije tijd, spel en expressie"),
    ("spel", "Spelvormen en speelgoed"),
    ("activiteiten_volwassenen", "Activiteiten voor volwassenen"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_op_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
