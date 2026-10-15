"""Pittige hoofdstukken bij Nederlands ✨ Spark.

Tien hoofdstukken, één per thema, telkens twintig vragen. Bij ✨ Spark is elk
thema in een deel 1 en een deel 2 gesplitst; het pittige hoofdstuk hoort bij
het hele thema en komt in het oefenplatform meteen achter deel 2 te staan.

Dit kwam er op 15 oktober 2026 na een melding dat de Spark-vragen te makkelijk
zijn. Geen nieuwe leerstof: alles staat in de leerbundel of in de veertig
vragen van het thema. De verdieping zit in de vraag: een regel toepassen in
een zin die het kind nog niet zag, twee regels tegelijk, de fout aanwijzen,
of van het gevolg terug naar de oorzaak. De aparte hoofdstukken voor
begrijpend lezen en spellingvarianten krijgen hier geen pittig deel.

Nederlands is een taalvak, dus een ingetypt antwoord wordt streng vergeleken
(zie lib/taalvak.ts). Elke invulvraag heeft daarom één ondubbelzinnig antwoord.
De vragen zelf staan per thema in spark_nederlands_themas/.
"""
import importlib

NIVEAU = "spark"
VAK = "Nederlands"
BESTAND = "spark-nederlands-pittig.json"

THEMAS = [
    ("onderwerp_hoofdgedachte", "Onderwerp, hoofdgedachte en hoofdpunten"),
    ("tekstsoorten_communicatie", "Tekstsoorten en het communicatiemodel"),
    ("feiten_meningen", "Feiten, meningen en betrouwbaarheid"),
    ("tekststructuur", "Tekststructuur en signaalwoorden"),
    ("schrijven_spreken", "Schrijven, spreken en gesprekken voeren"),
    ("register_taalvariatie", "Register, taalvariatie en non-verbale communicatie"),
    ("literatuur_beeldspraak", "Literatuur en beeldspraak"),
    ("spelling_werkwoorden", "Spelling, leestekens en werkwoordsvormen"),
    ("woordsoorten", "Woordsoorten en woordvorming"),
    ("zinsdelen", "Zinsdelen, zinssoorten en congruentie"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__}.spark_nederlands_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
