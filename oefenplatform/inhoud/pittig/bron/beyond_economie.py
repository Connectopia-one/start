"""Pittige hoofdstukken bij economie 🌍 Beyond doorstroom.

Eén hoofdstuk per thema, telkens dertig vragen, in de vormen van het examen van
de Examencommissie. Strikt uit de vakfiche 2027_algemene_economie_3DDO_3DDG en
de leerbundels die daarop steunen, zonder extra leerstof. Kim op 9 november
2026: elk vak meteen volledig, met gewone en pittige hoofdstukken; op
11 november 2026 gaf ze het startsein voor economie.

De thematitels zijn dezelfde als in beyond/bron/bouw_economie.py, zodat elk
pittig hoofdstuk naast zijn gewone delen komt te staan. Alle grafieken tekent
Claude zelf: maak_prenten_economie_beyond.py.
"""
import importlib

NIVEAU = "beyond-doorstroom"
VAK = "Economie"
BESTAND = "beyond-economie-pittig.json"
AANTAL = 30

THEMAS = [
    ("kringloop", "De economische kringloop en de macro-economische identiteiten"),
    ("duurzaam", "Alternatieve economische modellen, MVO en de SDG's"),
    ("bbp", "Het bbp, economische groei en welvaartsindicatoren"),
    ("vraag", "De vraagcurve en de prijselasticiteit van de vraag"),
    ("aanbod", "Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod"),
    ("surplus", "Consumenten- en producentensurplus en het welvaartsoptimum"),
    ("monopolie", "Marktvormen en het monopolie"),
    ("oligopolie", "Monopolistische concurrentie, oligopolie en speltheorie"),
    ("ingrijpen", "Prijsregulering, quota, belastingen en subsidies"),
    ("marktfalen", "Marktmacht, marktfalen, externe effecten en publieke goederen"),
    ("arbeid", "De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren"),
    ("geld", "Geld, monetaire aggregaten en geldschepping"),
    ("beleggen", "De financiële markt en beleggen"),
    ("ongelijkheid", "Inkomensongelijkheid, armoede en herverdeling"),
    ("handel", "Internationale handel en samenwerkingsverbanden"),
    ("wissel", "De wisselmarkt en de betalingsbalans"),
    ("conjunctuur", "De conjunctuur, conjunctuurindicatoren en de begroting"),
    ("evenwicht", "Het inkomensevenwicht, de multiplicator en het AV-AA-schema"),
    ("inflatie", "Inflatie, deflatie en prijsstabiliteit"),
    ("onderzoek", "Economisch onderzoek: onderzoeksvraag, methode en besluit"),
]

HOOFDSTUKKEN = [
    (titel, importlib.import_module(f"{__package__ + '.' if __package__ else ''}beyond_economie_themas.{naam}").VRAGEN)
    for naam, titel in THEMAS
]
