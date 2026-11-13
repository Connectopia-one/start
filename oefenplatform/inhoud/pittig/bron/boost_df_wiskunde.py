"""Pittige hoofdstukken bij wiskunde 🚀 Boost dubbele finaliteit.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Geen extra leerstof: alles staat in de leerbundels en de
gewone hoofdstukken van wiskunde Boost dubbele finaliteit
(boost-dubbele-finaliteit/bron/bouw_wiskunde.py). Kim op 13 november 2026: na
de telling van wat het meest geoefend wordt, eerst dit vak.

De thematitels zijn dezelfde als bij de gewone hoofdstukken, zodat elk pittig
hoofdstuk naast zijn gewone delen komt te staan. Alle grafieken en schetsen
tekent Claude zelf: maak_prenten_wiskunde_boost_df.py.
"""
import importlib

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Wiskunde"
BESTAND = "boost-df-wiskunde-pittig.json"
AANTAL = 30

THEMAS = [
    ("problemen", "Een opgave aanpakken: van context naar wiskunde"),
    ("reele", "Reële getallen, wortels en machten"),
    ("ordenen", "Ordenen, afronden en intervallen"),
    ("ruimte", "Rechten, vlakken en gelijkvormigheid"),
    ("pythagoras", "Pythagoras en de rechthoekige driehoek"),
    ("goniometrie", "De rechthoekige driehoek oplossen en toepassen"),
    ("formules", "Formules omvormen en eerstegraadsvergelijkingen"),
    ("stelsels", "Stelsels van twee eerstegraadsvergelijkingen"),
    ("functies", "Functies en de rechte"),
    ("grafisch", "Tekenverloop, verloopschema en grafisch oplossen"),
    ("tellen", "Telproblemen met boom- en venndiagram"),
    ("statistiek", "Statistiek: voorstellingen, centrum en spreiding"),
    ("misleiding", "Misleiding met cijfers en grafieken"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__ + '.' if __package__ else ''}boost_df_wiskunde_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
