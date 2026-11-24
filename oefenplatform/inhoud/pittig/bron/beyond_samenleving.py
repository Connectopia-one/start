"""Pittige hoofdstukken bij Samenleving en economie 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het digitale
examen van de Examencommissie (invul-, sleep-, dropdown- en meerkeuzevragen,
met schermafdrukken bij de Office-thema's). Strikt binnen de gewone
hoofdstukken (beyond/bron/se_*.py). Kim op 24 november 2026: "ik wil gewoon
alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_samenleving.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Samenleving en economie"
BESTAND = "beyond-samenleving-en-economie-pittig.json"
AANTAL = 30

THEMAS = [
    ("identiteit", "Identiteit: de lagen, de factoren en het wereldbeeld"),
    ("diversiteit", "Samenleven in diversiteit"),
    ("omgang", "Respectvol samenleven: communicatie, grenzen en samenwerken"),
    ("eerstehulp", "Ongevallen herkennen en eerste hulp geven"),
    ("reanimatie", "Een hartstilstand, reanimatie en de AED"),
    ("overheid", "De inkomsten en de uitgaven van de overheid"),
    ("sociaal", "Sociale zekerheid, uitkeringen en herverdeling"),
    ("markt", "Vraag, aanbod en het marktevenwicht"),
    ("ingrijpen", "Verschuivingen op de markt en de overheid die ingrijpt"),
    ("contract", "De arbeidsovereenkomst en het arbeidsreglement"),
    ("loon", "Van brutoloon naar nettoloon"),
    ("werkvloer", "Welzijn op het werk en waar je met vragen terechtkan"),
    ("aankoop", "De totale aankoopkost en het consumentenkrediet"),
    ("budget", "Het persoonlijk budget en je administratie"),
    ("sparen", "Sparen, beleggen en de invloed van inflatie"),
    ("verzekering", "Verzekeringen, een schadegeval en de polis"),
    ("word", "Tekstverwerking met Word"),
    ("excel", "Het rekenblad Excel"),
    ("powerpoint", "Presenteren met PowerPoint"),
    ("digiregels", "Veilig en correct online: recht, phishing en netiquette"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_se_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
