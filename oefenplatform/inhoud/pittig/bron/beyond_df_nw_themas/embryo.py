"""Bevruchting en de ontwikkeling van embryo en foetus — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen biologie Beyond (zelfde prenten), enkel wat in de gewone hoofdstukken nwd_embryo staat, plus eigen vragen."""
from ..beyond_bio_themas import gametogenese as G, bevruchting as B
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"luteale fase": "tweede helft van de cyclus", "blastocyst": "kiemblaas",
      "Bij de klievingsdelingen wordt het geheel niet groter.": "Bij de delingen onderweg wordt het geheel niet groter.",
      "Een stoornis tijdens de organogenese laat blijvende sporen.": "Een stoornis terwijl de organen aangelegd worden, laat blijvende sporen."}

VRAGEN = kies(G.VRAGEN, [0, 1, 2, 3, 5, 18, 21], _V) + kies(B.VRAGEN, [0, 1, 2, 9, 10, 11, 12, 14, 16, 17, 18, 19, 22, 24, 25], _V) + [
    volgorde("Zet de fasen van de bevalling in de juiste volgorde.", [
        "de ontsluiting", "de uitdrijving van de baby", "de nageboorte",
    ], "Eerst gaat de baarmoederhals open, dan wordt de baby geboren, daarna komt de placenta."),
    mk("Een vrouw heeft een cyclus van 32 dagen. Rond welke dag valt de eisprong ongeveer?",
       ["dag 18", "dag 14", "dag 16", "dag 32 − 18"], 0,
       "Ongeveer veertien dagen vóór de volgende menstruatie: 32 − 14 = 18."),
    mk("Waarom is de eicel zo veel groter dan een zaadcel?",
       ["ze draagt voedsel voor de eerste delingen", "ze moet zelf snel naar de zaadcel toe zwemmen",
        "ze bevat veel meer chromosomen dan de zaadcel", "ze moet de placenta al meteen helemaal vormen"], 0,
       "Het grote cytoplasma voedt de eerste delingen."),
    tabel("Wat gaat er via de placenta van de moeder naar het kind?", [
        ("zuurstof", J), ("glucose", J), ("koolstofdioxide van het kind", F), ("antistoffen", J),
    ], "Koolstofdioxide en afvalstoffen gaan net de andere kant op, van het kind naar de moeder."),
    sorteer("Embryonale of foetale fase?", ["embryonale fase", "foetale fase"], [
        ["de organen worden aangelegd", "embryonale fase"], ["vooral groeien en rijpen", "foetale fase"],
        ["de eerste acht weken", "embryonale fase"], ["levensvatbaar vanaf ongeveer 24 weken", "foetale fase"],
    ], "In de embryonale fase worden de organen aangelegd, daarna groeit de foetus vooral."),
    open_("Leg uit waarom foliumzuur al vóór de zwangerschap aangeraden wordt en niet pas als de vrouw weet dat ze zwanger is.",
          "De ruggengraat en het zenuwstelsel worden in de eerste weken aangelegd, vaak nog voor de vrouw weet dat ze zwanger is. Dan moet er al genoeg foliumzuur zijn.",
          "De organen worden in de eerste acht weken aangelegd."),
]
