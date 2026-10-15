"""Pittige hoofdstukken bij samenleving en economie ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij techniek: geen nieuwe leerstof buiten de
leerbundel (leerbundels/bron/maak_samenleving.py) en de veertig bestaande
vragen van het thema; de verdieping zit in de vraag. De vragen zelf staan per
thema in spark_samenleving_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Samenleving en economie"
BESTAND = "spark-samenleving-en-economie-pittig.json"

THEMAS = [
    ("identiteit", "Ik ben wie ik ben"),
    ("samenleven", "Ik leef samen met anderen"),
    ("eerste_hulp", "Eerste hulp bij ongevallen"),
    ("democratie", "Democratie en dictatuur"),
    ("belgie", "Hoe België bestuurd wordt"),
    ("kringloop", "De economische kringloop"),
    ("overheid", "De overheid in de economie"),
    ("financien", "Ik beheer mijn financiën"),
    ("digitaal", "Digitaal communiceren en bestanden beheren"),
    ("kantoor_online", "Word, Excel, PowerPoint en veilig online"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_samenleving_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
