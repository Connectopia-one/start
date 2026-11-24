"""Pittige hoofdstukken bij Economie 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (boost-doorstroom/bron/ec_*.py en bw_*.py)
staat, met zelfgetekende grafieken om op te klikken (maak_prenten_ec_boost_do.py).
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Economie"
BESTAND = "boost-do-economie-pittig.json"
AANTAL = 30

THEMAS = [
    ("kringloop", "De economische kringloop"),
    ("bbp", "Productie, toegevoegde waarde en het bbp"),
    ("groei", "Economische groei, welvaart en welzijn"),
    ("behoeften", "Behoeften, schaarste en soorten goederen"),
    ("nut", "Nut, preferentie en de indifferentiecurve"),
    ("budget", "De budgetlijn en de optimale goederencombinatie"),
    ("productie", "Productiefactoren, productiefunctie en meeropbrengsten"),
    ("kosten", "De kosten- en de opbrengstencurven"),
    ("optimaal", "De optimale productiegrootte en winstmaximalisatie"),
    ("markt", "De markt met volkomen concurrentie en de overheid"),
    ("arbeid", "De arbeidsmarkt en de collectieve afspraken"),
    ("handel", "Internationale handel en handelsbelemmeringen"),
    ("vormen_ond", "Ondernemingsvormen en aansprakelijkheid"),
    ("balans", "De balans en de resultatenrekening"),
    ("boekhouden", "Dubbel boekhouden: redeneerschema, journaal en grootboek"),
    ("facturen", "Facturen, kortingen en btw"),
    ("strategie", "Bedrijfsstrategie: missie, visie, SWOT en stakeholders"),
    ("marketing", "Marktonderzoek, doelgroep en de marketingmix"),
    ("product", "Producten, merken, prijsstrategie en distributie"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_ec_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
