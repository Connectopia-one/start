"""Pittige hoofdstukken bij gezondheid, zorg en welzijn 🛠️ Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm, met
zelfgetekende klikprenten (huid, gewricht, hersenen, ICF-schema,
voedingsdriehoek, veiligheidstekens, koelkast, gedekte tafel, grondplan en
onderhoudsetiket). Strikt binnen de gewone hoofdstukken
(boost-dubbele-finaliteit/bron/gz_*.py). Bij waarnemen, oog en oor, beweging en
zenuwstelsel komen enkele vragen uit biologie Boost doorstroom, telkens enkel
waar de leerstof dezelfde is.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Gezondheid, zorg en welzijn"
BESTAND = "boost-df-gezondheid-zorg-en-welzijn-pittig.json"
AANTAL = 30

THEMAS = [
    ("waarnemen", "Waarnemen: van prikkel tot reactie"),
    ("oog_oor", "Het oog en het oor"),
    ("beweging", "Spieren, beenderen en gewrichten"),
    ("zenuwstelsel", "Het zenuwstelsel en de reflexen"),
    ("gezondheid", "Gezondheid in kaart: Gordon en het ICF"),
    ("ziekte_ehbo", "Ziek zijn en eerste hulp"),
    ("bevordering", "Gezondheid bevorderen: preventie, voeding en beweging"),
    ("kwaliteitsbewust", "Kwaliteitsbewust handelen"),
    ("voeding", "Voedingsstoffen en een evenwichtig dagmenu"),
    ("voedselveiligheid", "Voedselveiligheid en voedselhygiëne"),
    ("bewaren", "Voedsel bewaren"),
    ("boodschappen", "Boodschappen doen en de tafel dekken"),
    ("interieurzorg", "Interieurzorg: ruimtes, vuil en technieken"),
    ("schoonmaken", "Methodisch, veilig en duurzaam schoonmaken"),
    ("leefomgeving", "Zorg voor de woon- en leefomgeving"),
    ("linnenzorg", "Linnenzorg: sorteren, wassen en strijken"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}boost_df_gz_themas"

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
