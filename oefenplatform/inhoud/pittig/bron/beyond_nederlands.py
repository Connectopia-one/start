"""Pittige hoofdstukken bij Nederlands 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen
van de Examencommissie (lezen en luisteren bij een tekst, literatuur,
taalbeschouwing). Strikt binnen de gewone hoofdstukken (beyond/bron/nl_*.py).
Kim op 24 november 2026: na geschiedenis dubbele finaliteit dit vak, omdat er
het meest op geoefend wordt.

De thematitels zijn dezelfde als in beyond/bron/bouw_nederlands.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Nederlands"
BESTAND = "beyond-nederlands-pittig.json"
AANTAL = 30

THEMAS = [
    ("tekstsoorten", "Tekstsoorten en teksttypes"),
    ("hoofdgedachte", "Onderwerp, hoofdgedachte en samenvatten"),
    ("bronnen", "Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing"),
    ("communicatie", "Het communicatiemodel en ruis"),
    ("tekstopbouw", "Tekstopbouw, alineaverbanden en structuuraanduiders"),
    ("argumentatie", "Argumentatie en drogredenen"),
    ("genres", "Literaire begrippen en genres"),
    ("verhaal", "Verhaalkenmerken en vertelperspectief"),
    ("poezie", "Poëzie: dichtvormen, strofen en rijm"),
    ("drama", "Dramatiek en theatertekens"),
    ("stijlfiguren", "Stijlfiguren en beeldspraak"),
    ("stromingen", "Literaire stromingen van de middeleeuwen tot nu"),
    ("varieteiten", "Taalvariëteiten, registers en beleefdheid"),
    ("identiteit", "Taal en identiteit: stereotypering, inclusie en non-verbale communicatie"),
    ("spelling", "Klanken, spelling, diakritische tekens en interpunctie"),
    ("woordsoorten", "Woordsoorten"),
    ("morfologie", "Morfologie: samenstellingen, afleidingen en werkwoordstijden"),
    ("zinsbouw", "Zinsontleding en zinsbouw"),
    ("semantiek", "Semantiek: betekenisrelaties, gevoelswaarde en herkomst"),
    ("schrijven", "Schrijven en schriftelijke interactie"),
    ("spreken", "Spreken en gesprekken voeren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_nederlands_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
