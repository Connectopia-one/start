"""Pittige hoofdstukken bij Natuurwetenschappen 🔧 Beyond dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in examenvorm. Vooral pittige
vragen van biologie, chemie en fysica Beyond (met hun prenten), enkel wat in de
gewone hoofdstukken (beyond-dubbele-finaliteit/bron/nwd_*.py) staat, plus eigen vragen.
Kim op 24 november 2026: "werk daar dan maar aan verder".
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Natuurwetenschappen"
BESTAND = "beyond-df-natuurwetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("embryo", "Bevruchting en de ontwikkeling van embryo en foetus"),
    ("vruchtbaarheid", "Vruchtbaarheid, anticonceptie en kinderwens"),
    ("genexpressie", "Van DNA naar eiwit: genexpressie"),
    ("overerving", "Overerving van kenmerken"),
    ("evolutie", "Biologische evolutie"),
    ("selectie", "Natuurlijke selectie en het ontstaan van soorten"),
    ("labels", "Productlabels, pictogrammen en risico's van stoffen"),
    ("voeding", "Voedingsbestanddelen en etiketten"),
    ("dosis", "Dosis en concentratie van stoffen"),
    ("duurzaam", "Duurzame chemie"),
    ("magnetisme", "Elektromagnetisme"),
    ("golven", "Golven, geluid en het elektromagnetisch spectrum"),
    ("kernfysica", "Kernfysica, kernenergie en straling"),
    ("onderzoek", "Veilig werken, meten en onderzoeken"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_df_nw_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
