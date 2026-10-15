"""Pittige hoofdstukken bij wiskunde ✨ Spark.

Negen hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij 🌱 Start: geen nieuwe leerstof, de verdieping zit
in de vraag. Bij wiskunde nooit meerdere juiste antwoorden, en elke vraag met
een uitgerekend getal als antwoord heeft een veld reken dat bouw_pittig.py
narekent. De vragen zelf staan per thema in spark_wiskunde_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Wiskunde"
BESTAND = "spark-wiskunde-pittig.json"

THEMAS = [
    ("negatieve_getallen", "Negatieve getallen en procenten"),
    ("getallenleer", "Getallenleer"),
    ("probleemoplossend_denken", "Probleemoplossend denken"),
    ("redeneringen", "Wiskundige redeneringen en uitspraken"),
    ("meetkunde", "Meetkunde"),
    ("metend_rekenen", "Metend rekenen"),
    ("relaties_en_verandering", "Relaties en verandering"),
    ("data_en_onzekerheid", "Data en onzekerheid"),
    ("verzamelingen", "Verzamelingen"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_wiskunde_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
