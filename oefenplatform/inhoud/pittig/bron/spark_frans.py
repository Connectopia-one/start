"""Pittige hoofdstukken bij Frans ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Dezelfde regels als bij techniek: geen nieuwe leerstof, enkel woordenschat
en grammatica uit de leerbundel (leerbundels/bron/maak_frans_spark.py) en uit
de bestaande vragen; de verdieping zit in de vraag. Frans is een taalvak, dus
invulantwoorden worden streng vergeleken: elk invulantwoord kan maar op één
manier geschreven worden, met de juiste accenten. De vragen zelf staan per
thema in spark_frans_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Frans"
BESTAND = "spark-frans-pittig.json"

THEMAS = [
    ("lezen", "Een Franse tekst lezen"),
    ("tekstsoorten", "Tekstsoorten, signaalwoorden en verwijswoorden"),
    ("schrijven", "Schrijven: berichten, uitnodigingen en mails"),
    ("foto", "Een foto of afbeelding beschrijven"),
    ("mensen", "Woordenschat: mensen, familie, gevoelens en gezondheid"),
    ("eten_wonen", "Woordenschat: eten, wonen, kleding en dagelijkse dingen"),
    ("school_sport", "Woordenschat: school, beroepen, sport en vrije tijd"),
    ("getallen_tijd", "Woordenschat: getallen, tijd, weer, reizen en landen"),
    ("lidwoorden", "Grammatica: lidwoorden, naamwoorden en voornaamwoorden"),
    ("werkwoorden", "Grammatica: werkwoorden, tijden en zinsbouw"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_frans_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
