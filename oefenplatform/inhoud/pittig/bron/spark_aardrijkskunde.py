"""Pittige hoofdstukken bij aardrijkskunde ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij techniek: geen nieuwe leerstof, de verdieping
zit in de vraag. De leerstof staat in leerbundels/bron/maak_aardrijkskunde_spark.py;
de vragen zelf staan per thema in spark_aardrijkskunde_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Aardrijkskunde"
BESTAND = "spark-aardrijkskunde-pittig.json"

THEMAS = [
    ("ak_kaart", "Een kaart lezen"),
    ("ak_gradennet", "Waar op aarde ben je?"),
    ("ak_lagen", "De lagen van een landschap"),
    ("ak_verschillen", "Waarom landschappen verschillen"),
    ("ak_aarde", "De aarde beweegt en slijt"),
    ("ak_weer", "Het weer en zijn uitschieters"),
    ("ak_klimaat", "Het klimaat verandert"),
    ("ak_mens", "De mens verandert het landschap"),
    ("ak_kaartlagen", "Onderzoeken met kaartlagen"),
    ("ak_terrein", "Het landschap op het terrein"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_aardrijkskunde_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
