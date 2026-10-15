"""Pittige hoofdstukken bij geschiedenis ✨ Spark.

Zes hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij de andere vakken: geen nieuwe leerstof, de
verdieping zit in de vraag. De vragen zelf staan per thema in
spark_geschiedenis_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Geschiedenis"
BESTAND = "spark-geschiedenis-pittig.json"

THEMAS = [
    ("referentiekader", "Het historisch referentiekader"),
    ("prehistorie", "De prehistorie"),
    ("mesopotamie_egypte", "Mesopotamië en Egypte"),
    ("griekenland", "Het oude Griekenland"),
    ("romeinse_rijk", "Het Romeinse Rijk"),
    ("bronnen_kunst", "Bronnen, kunst en beeldvorming"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_geschiedenis_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
