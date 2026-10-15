"""Pittige hoofdstukken bij natuurwetenschappen ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij techniek: geen nieuwe leerstof, de verdieping zit
in de vraag (twee stappen, omgekeerd redeneren, misvattingen, nieuwe situaties).
De leerstof komt uit leerbundels/bron/maak_natuurwetenschappen_spark.py en de
veertig bestaande vragen per thema. De vragen zelf staan per thema in
spark_natuurwetenschappen_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Natuurwetenschappen"
BESTAND = "spark-natuurwetenschappen-pittig.json"

THEMAS = [
    ("cellen", "Cellen, weefsels en organen"),
    ("fotosynthese", "Fotosynthese en de plant"),
    ("lichaam", "Het menselijk lichaam"),
    ("voortplanting", "Voortplanting"),
    ("ecologie", "Ecologie en biodiversiteit"),
    ("materie", "Materie, stoffen en mengsels"),
    ("massadichtheid", "Massadichtheid"),
    ("energie", "Energie, kracht en snelheid"),
    ("meten", "Veilig werken, meten en eenheden"),
    ("onderzoek", "Wetenschappelijk onderzoek"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_natuurwetenschappen_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
