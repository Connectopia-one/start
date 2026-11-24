"""Pittige hoofdstukken bij Aardrijkskunde 🔧 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. De vakfiche van
de dubbele finaliteit dekt grotendeels dezelfde leerstof als die van de
doorstroom. Daarom nemen de thema's de pittige vragen van Aardrijkskunde Beyond
doorstroom over (beyond_ak_themas, met hun prenten), behalve de vragen over
leerstof die niet in de gewone hoofdstukken van de dubbele finaliteit staat
(beyond-dubbele-finaliteit/bron/ak2_*.py), en vullen ze aan met eigen vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".

De thematitels zijn dezelfde als in beyond-dubbele-finaliteit/bron/bouw_aardrijkskunde.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Aardrijkskunde"
BESTAND = "beyond-df-aardrijkskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("situeren", "Situeren op aarde en de aardse sferen"),
    ("heelal", "Het heelal en de plaats van de aarde"),
    ("zonnestelsel", "Het zonnestelsel en zijn kleine lichamen"),
    ("bewegingen", "De bewegingen van de aarde"),
    ("atmosfeer", "De atmosfeer en de temperatuur op aarde"),
    ("wind", "Luchtdruk, wind en de grote circulatie"),
    ("neerslag", "Water in de lucht en de neerslag"),
    ("klimaat", "Klimaten, biomen en zeestromen"),
    ("geosfeer", "De bouw van de aarde en de platentektoniek"),
    ("vulkanen", "Vulkanen en aardbevingen"),
    ("gesteenten", "Gesteenten en de geologische tijd"),
    ("verwering", "Verwering en massatransport"),
    ("erosie", "Erosie door water, ijs en wind"),
    ("klimaatnu", "De huidige klimaatverandering"),
    ("ruimte", "Verstedelijking en het ruimtelijk beleid"),
    ("landschap", "Het landschap lezen en duurzaam ruimtegebruik"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_ak_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
