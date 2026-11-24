"""Pittige hoofdstukken bij Toegepaste economie 🛠️ Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Enkel wat in de
gewone hoofdstukken (boost-dubbele-finaliteit/bron/bouw_toegepaste_economie.py)
staat. Boekhoudvragen deels gedeeld met economie Boost doorstroom, ICT-vragen
deels gedeeld met Samenleving en economie Beyond. Zelfgetekende prenten
(maak_prenten_te_boost_df.py): verkoopfactuur, btw-aangifte, bladzijde met
objecten, kolomgrafiek, multifunctioneel toestel, mappenvenster,
databanktabel, bankuittreksel en proef- en saldibalans.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Toegepaste economie"
BESTAND = "boost-df-toegepaste-economie-pittig.json"
AANTAL = 30

THEMAS = [
    ("boekhouding", "Waarom boekhouden en hoe het werkt"),
    ("balans", "De balans en de resultatenrekening"),
    ("mar", "Het MAR en het redeneerschema"),
    ("aankoop", "Aankopen: documenten, kortingen en btw"),
    ("verkoop", "Verkopen en de verkoopfactuur"),
    ("btw", "De btw en de btw-aangifte"),
    ("registreren", "Aankopen, verkopen en bankverrichtingen boeken"),
    ("eindejaar", "Van proefbalans tot eindbalans"),
    ("tekstverwerking", "Tekstverwerking: klavier, opmaak en stijlen"),
    ("objecten", "Illustraties, schema's en tabellen"),
    ("rekenblad", "Het rekenblad: cellen, bereiken en opmaak"),
    ("functies", "Formules en functies in een rekenblad"),
    ("grafieken", "Grafieken maken en lezen"),
    ("afdrukken", "Afdrukken, kopiëren en scannen"),
    ("bewaren", "Bestanden beheren en bewaren"),
    ("presenteren", "Presenteren en gegevens in een databank"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_te_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
