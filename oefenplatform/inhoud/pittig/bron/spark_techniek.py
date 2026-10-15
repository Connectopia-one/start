"""Pittige hoofdstukken bij techniek ✨ Spark.

Elf hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn, vooral bij techniek. Dezelfde regels als bij 🌱 Start: geen nieuwe
leerstof, de verdieping zit in de vraag. De vragen zelf staan per thema in
spark_techniek_themas/, met dezelfde namen als de themabestanden in
spark/bron/tk_*.py.
"""
import importlib

NIVEAU = "spark"
VAK = "Techniek"
BESTAND = "spark-techniek-pittig.json"

THEMAS = [
    ("tk_materialen", "Materialen en grondstoffen"),
    ("tk_energie", "Energie in een technisch systeem"),
    ("tk_stroomkring", "De elektrische stroomkring"),
    ("tk_informatie", "Informatieverwerkende systemen"),
    ("tk_krachten", "Krachten en stevigheid in een constructie"),
    ("tk_verbinden", "Verbinden, afwerken en veilig werken"),
    ("tk_meten", "Meten, eenheden en modelvoorstellingen"),
    ("tk_transport", "Transport en overbrengingen"),
    ("tk_biotechniek", "Biotechnische systemen"),
    ("tk_proces", "Het technisch proces"),
    ("tk_algoritmen", "Algoritmen en computationeel denken"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_techniek_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
