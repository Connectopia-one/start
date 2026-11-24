"""Tekstopbouw, alineaverbanden en vaste tekststructuren — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_tekstopbouw van dubbele finaliteit passen, zonder de vragen over begrippen die daar niet in staan."""
from ..beyond_nederlands_themas import tekstopbouw as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20])
VRAGEN += [
    tabel("Welke vaste tekststructuur past bij deze tussentitels?", [
        ("Wat is het probleem? / Waar komt het vandaan? / Wat kunnen we eraan doen?", "probleemstructuur"),
        ("Vroeger / Hoe het veranderde / Vandaag", "ontwikkelingsstructuur"),
        ("De maatregel / Waarom hij nodig is / Wat hij oplevert", "maatregelstructuur"),
        ("Model A / Model B / Welk is beter?", "vergelijkingsstructuur"),
    ], "De tussentitels verraden vaak de structuur.", kolommen=["probleemstructuur", "ontwikkelingsstructuur", "maatregelstructuur", "vergelijkingsstructuur"]),
    mk("Een tekst begint met een opvallend cijfer: \"Elke dag gooien we in België een miljoen broden weg.\" Wat is de functie van die inleiding?",
       ["de aandacht van de lezer trekken", "het slot van de tekst samenvatten", "een tegenargument weerleggen", "de bronnen van de tekst vermelden"], 0,
       "Een verrassend feit maakt de lezer nieuwsgierig."),
    keuze("Het slot van een informatieve tekst bevat vaak een [[*samenvatting|nieuw argument|inhoudstafel]] of een blik vooruit.", "Het slot rondt af en brengt geen nieuwe hoofdzaken."),
    tabel("Hoort dit bij de inleiding, de kern of het slot?", [
        ("het onderwerp aankondigen", "inleiding"), ("de hoofdpunten uitwerken met voorbeelden", "kern"), ("een conclusie trekken", "slot"),
    ], "Inleiding, kern en slot hebben elk hun taak.", kolommen=["inleiding", "kern", "slot"]),
]
