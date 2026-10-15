"""Pittige hoofdstukken bij Engels ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij techniek: geen nieuwe leerstof, alleen
woordenschat en grammatica uit de leerbundel; de verdieping zit in de vraag.
Engels is een taalvak: invulantwoorden worden streng vergeleken (zie
lib/taalvak.ts), dus elk invulantwoord kan maar op één manier geschreven
worden. De vragen zelf staan per thema in spark_engels_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Engels"
BESTAND = "spark-engels-pittig.json"

THEMAS = [
    ("lezen", "Een Engelse tekst lezen"),
    ("tekstsoorten", "Tekstsoorten, signaalwoorden en verwijswoorden"),
    ("schrijven", "Schrijven: berichten, uitnodigingen en mails"),
    ("landen", "Engelstalige landen en literaire teksten"),
    ("ws_mensen", "Woordenschat: mensen, familie, gevoelens en gezondheid"),
    ("ws_eten", "Woordenschat: eten, wonen, kleding en dagelijkse dingen"),
    ("ws_school", "Woordenschat: school, beroepen, sport en vrije tijd"),
    ("ws_tijd", "Woordenschat: getallen, tijd, weer, reizen en landen"),
    ("gr_naamwoorden", "Grammatica: naamwoorden, lidwoorden en voornaamwoorden"),
    ("gr_werkwoorden", "Grammatica: werkwoorden, tijden en zinsbouw"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_engels_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
