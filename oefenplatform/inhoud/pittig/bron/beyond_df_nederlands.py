"""Pittige hoofdstukken bij Nederlands Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Pittige vragen
van Nederlands Beyond doorstroom die binnen de gewone hoofdstukken
(beyond-dubbele-finaliteit/bron/nl_*.py) passen, plus eigen vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Nederlands"
BESTAND = "beyond-df-nederlands-pittig.json"
AANTAL = 30

THEMAS = [
    ("hoofdgedachte", "Onderwerp, hoofdgedachte en hoofdpunten"),
    ("tekstsoorten", "Tekstsoorten en teksttypes"),
    ("bronnen", "Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing"),
    ("communicatie", "Het communicatiemodel en ruis"),
    ("tekstopbouw", "Tekstopbouw, alineaverbanden en vaste tekststructuren"),
    ("structuur", "Structuuraanduiders: verwijswoorden en signaalwoorden"),
    ("argumentatie", "Argumentatie, feiten en meningen, en drogredenen"),
    ("strategie", "Lees- en luisterstrategieën en notities nemen"),
    ("multimedia", "Multimediale elementen en non-verbale communicatie"),
    ("verhaal", "Verhaallijn, personages en vertelperspectief"),
    ("spanning", "Tijd, ruimte, thema en spanningsopbouw"),
    ("genres", "Genres, fictie en non-fictie, en je eigen leeservaring"),
    ("varieteiten", "Taalvariëteiten, registers en beleefdheid"),
    ("identiteit", "Taal en identiteit: stereotypering, inclusie en exclusie"),
    ("spelling", "Klanken, spelling, diakritische tekens en interpunctie"),
    ("woordsoorten", "Woordsoorten"),
    ("morfologie", "Morfologie: samenstellingen, afleidingen en werkwoordstijden"),
    ("zinsbouw", "Zinsontleding en zinsbouw"),
    ("semantiek", "Semantiek: betekenisrelaties, gevoelswaarde en humor"),
    ("schrijven", "Schrijven en schriftelijke interactie"),
    ("spreken", "Spreken en gesprekken voeren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_nl_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
