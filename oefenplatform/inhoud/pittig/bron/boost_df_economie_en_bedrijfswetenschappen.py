"""Pittige hoofdstukken bij Economie en bedrijfswetenschappen 🛠️ Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (boost-dubbele-finaliteit/bron/eb_*.py)
staat. Zelfgetekende prenten (maak_prenten_eb_boost_df.py): organogram,
informatiestroom, vacature, arbeidsovereenkomst, loonbrief, affiche,
documentenstroom en vrachtbrief. De grafieken van nut, productie, kosten en
opbrengsten zijn dezelfde als bij economie Boost doorstroom.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Economie en bedrijfswetenschappen"
BESTAND = "boost-df-economie-en-bedrijfswetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("behoeften", "Behoeften, schaarste en soorten goederen"),
    ("nut", "Nut, voorkeuren en de vraag van de consument"),
    ("productiefactoren", "De productiefactoren en de productie"),
    ("kosten", "De kosten van de producent"),
    ("opbrengsten", "Opbrengsten, optimale productiegrootte en aanbod"),
    ("ondernemingsvormen", "Soorten ondernemingen en hun verplichtingen"),
    ("organisatie", "De organisatiestructuur van een onderneming"),
    ("afdelingen", "De afdelingen en hun samenwerking"),
    ("hr", "Werving, selectie en de werkplek"),
    ("arbeidsovereenkomst", "Aanwerving en de arbeidsovereenkomst"),
    ("schorsing", "Schorsing en einde van de arbeidsovereenkomst"),
    ("loon", "De loonfiche en de loonberekening"),
    ("marketing", "De marketingmix"),
    ("verkoopgesprek", "Soorten klanten en het verkoopgesprek"),
    ("documenten", "Commerciële documenten en de documentenstroom"),
    ("logistiek", "Transport, expeditie en logistiek"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_eb_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
