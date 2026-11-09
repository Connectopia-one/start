"""Pittige hoofdstukken bij bedrijfswetenschappen en recht 🌍 Beyond.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Strikt uit de vakfiche 2027_bedrijfswetenschappenenrecht_3DO,
zonder extra leerstof. Kim op 9 november 2026: "ik zou dat inderdaad eerst
volledig maken dat we elk vak direct goed dien" — bij elk nieuw vak horen de
pittige hoofdstukken er meteen bij.

De thematitels zijn dezelfde als in beyond/bron/bouw_bedrijfswetenschappen.py,
zodat elk pittig hoofdstuk naast zijn gewone delen komt te staan. Alle prenten
tekent Claude zelf: maak_prenten_bedrijfswetenschappen_beyond.py.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Bedrijfswetenschappen en recht"
BESTAND = "beyond-bedrijfswetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("vormen_vergelijken", "Ondernemingsvormen vergelijken"),
    ("personenbelasting", "De personenbelasting"),
    ("venb", "De vennootschapsbelasting en de voorafbetalingen"),
    ("aankopen", "Aankopen boeken: facturen, kortingen, kosten en btw"),
    ("verkopen", "Verkopen, betalingen en geldbewegingen boeken"),
    ("lonen", "Investeringen, leningen, lonen en btw boeken"),
    ("inventaris", "Eindejaarsverrichtingen en de saldibalans"),
    ("balans", "De balans voor financiële analyse"),
    ("liquiditeit", "Kerncijfers: liquiditeit"),
    ("solvabiliteit", "Kerncijfers: solvabiliteit en rendabiliteit"),
    ("financiering", "Financieringsvormen"),
    ("investeringen", "Investeringsprojecten beoordelen"),
    ("strategie", "SWOT, stakeholders en het ondernemingsplan"),
    ("bmc", "Het Business Model Canvas en de BCG-matrix"),
    ("marketing", "Marketingstrategie en de marketingmix"),
    ("arbeid", "De arbeidsovereenkomst: begin, schorsing en einde"),
    ("logistiek", "Logistiek en supply chain management"),
    ("hrm", "Human-resources-management"),
    ("kostprijs", "Kostprijsberekening en break-even"),
    ("databank", "Relationele databanken"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.beyond_bedrijfswetenschappen_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
