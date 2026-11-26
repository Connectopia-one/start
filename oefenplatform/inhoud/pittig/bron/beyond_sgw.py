"""Pittige hoofdstukken bij Sociale en gedragswetenschappen 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het digitale
examen van de Examencommissie (invul-, sleep-, dropdown- en meerkeuzevragen,
met eigen schema's en tabellen). Strikt binnen de gewone
hoofdstukken (beyond/bron/sg_*.py). Kim op 24 november 2026: "ik wil gewoon
alles online hebben", vak per vak.

De thematitels zijn dezelfde als in beyond/bron/bouw_sgw.py.
"""
import importlib
from importlib.util import find_spec

NIVEAU = "beyond-doorstroom"
VAK = "Sociale en gedragswetenschappen"
BESTAND = "beyond-sociale-en-gedragswetenschappen-pittig.json"
AANTAL = 30

THEMAS = [
    ("ontwikkeling", "Ontwikkelingspsychologie: de begrippen en de drie basisvragen"),
    ("biologisch", "Ontwikkeling: de biologische en de psychodynamische benadering"),
    ("leren", "Ontwikkeling: de behavioristische en de cognitieve benadering"),
    ("systemisch", "Ontwikkeling: de humanistische en de systemische benadering"),
    ("sociaalgedrag", "Prosociaal gedrag, antisociaal gedrag en sociale cognitie"),
    ("groepen", "Cognitieve dissonantie en processen in een groep"),
    ("beinvloeding", "Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid"),
    ("persoonlijkheid", "Persoonlijkheid: wat ze is en hoe een brein reageert"),
    ("persbenadering", "Persoonlijkheid: van Freud over Bandura naar Rogers"),
    ("trekken", "Persoonlijkheid: trekken, de big five en HEXACO"),
    ("opvoeding", "Opvoeden: milieus, dimensies, stijlen en middelen"),
    ("pedmodellen", "Pedagogische modellen en opvoeden in bijzondere contexten"),
    ("communicatie", "Communicatieve vaardigheden: kaders en gesprekstechnieken"),
    # Enkel humane wetenschappen (Kim, 26 november 2026); dezelfde titels als
    # in beyond/bron/bouw_sgw.py.
    ("hw_democratie", "Humane wetenschappen: politiek, democratie en de rechtstaat"),
    ("hw_belgie", "Humane wetenschappen: de Belgische staat en zijn bestuursniveaus"),
    ("hw_partijen", "Humane wetenschappen: ideologieën, partijen en verkiezingen"),
    ("hw_participatie", "Humane wetenschappen: participatie, kiesstelsel en kiesrecht"),
    ("hw_recht", "Humane wetenschappen: het recht in de samenleving"),
    ("hw_globalisering", "Humane wetenschappen: globalisering, de VN en de Europese Unie"),
    ("socialisatie", "Socialisatie: posities, rollen en vier visies"),
    ("stratificatie", "Sociale stratificatie en de verklaringsmodellen"),
    ("mobiliteit", "Sociale mobiliteit, meritocratie en het matheüseffect"),
    ("media", "Mediatisering en de functies van de massamedia"),
    ("beeldvorming", "Mediatheorieën, beeldvorming en persvrijheid"),
    ("vraagstukken", "Maatschappelijke vraagstukken en de redeneeractiviteiten"),
    ("onderzoek", "De onderzoekscyclus van oriënteren tot rapporteren"),
]

_PAK = f"{__package__ + '.' if __package__ else ''}beyond_sgw_themas"
HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{_PAK}.{naam}").VRAGEN)
    for naam, titel in THEMAS
    if find_spec(f"{_PAK}.{naam}")
]
