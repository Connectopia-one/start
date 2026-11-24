"""Pittige hoofdstukken bij Engels 🚀 Boost doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Eigen vragen,
enkel wat in de gewone hoofdstukken (boost-doorstroom/bron/en_*.py) staat. De
thema's in boost_en_themas/ dienen voor doorstroom én dubbele finaliteit:
VRAGEN voor doorstroom. Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-doorstroom"
VAK = "Engels"
BESTAND = "boost-do-engels-pittig.json"
AANTAL = 30

THEMAS = [
    ("lezen", "Een Engelse tekst analyseren"),
    ("tekstsoorten", "Tekstsoorten, tekstverbanden en verwijswoorden"),
    ("cultuur", "De Engelstalige wereld: gewoontes en conventies"),
    ("schrijven", "Schrijven, schriftelijke interactie en literatuurbeleving"),
    ("dagelijks", "Woordvelden: mensen, gezondheid en het dagelijkse leven"),
    ("wereld", "Woordvelden: school, werk, reizen en de samenleving"),
    ("naamwoorden", "Nouns, articles, quantifiers en numerals"),
    ("voornaamwoorden", "Pronouns: de zeven soorten"),
    ("adjectieven", "Adjectives, adverbs, comparatives en voorzetsels"),
    ("tegenwoordig", "De tegenwoordige tijden"),
    ("verleden", "De verleden en de toekomende tijden"),
    ("modalen", "Modal auxiliaries, imperative en infinitive"),
    ("zinsbouw", "Zinsdelen, soorten zinnen en bijzinnen"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_en_themas"


def _vragen(m):
    return m.VRAGEN


HOOFDSTUKKEN = [
    (titel, _vragen(importlib.import_module(f"{_PAK}.{naam}")))
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
