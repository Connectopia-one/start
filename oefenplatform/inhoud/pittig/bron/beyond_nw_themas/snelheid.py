"""Snelheid van een chemische reactie — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen chemie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt (geen reactieorde), aangevuld met eigen vragen.
"""
from ..beyond_chem_themas import snelheid as S
from .vormen import J, F, mk, inv, tabel, keuze, casus

OVER = [S.VRAGEN[i] for i in range(28) if i not in (11, 12, 13, 24, 25)]

EIGEN = [
    casus(
        "Lena laat telkens 1 g magnesium reageren met 50 mL zoutzuur en meet hoeveel waterstofgas er per minuut ontstaat. "
        "Proef A: een lintje magnesium in zoutzuur van 20 °C. Proef B: magnesiumpoeder in zoutzuur van 20 °C. Proef C: een lintje magnesium in zoutzuur van 40 °C. Het zuur is telkens ruim voldoende.",
        [
            tabel(
                "Gaat de reactie sneller dan in proef A?",
                [
                    ("proef B", J),
                    ("proef C", J),
                    ("proef A met 100 mL van hetzelfde zuur in plaats van 50 mL", F),
                ],
                "Poeder geeft een hogere verdelingsgraad, warmte meer effectieve botsingen. Meer volume van dezelfde concentratie verandert de snelheid niet.",
            ),
            mk(
                "Ontstaat er op het einde van de drie proeven evenveel waterstofgas?",
                ["Ja, er is telkens evenveel magnesium", "Nee, proef B geeft het meeste gas want poeder", "Nee, proef C geeft het meeste gas want warmer", "Nee, proef A geeft het meeste gas want trager"],
                0,
                "De snelheid verschilt, de hoeveelheid product niet.",
            ),
        ],
    ),
    tabel(
        "Is deze botsing elastisch of effectief?",
        [
            ("De deeltjes stuiteren weg zonder te veranderen.", "elastisch"),
            ("Er ontstaat een nieuw deeltje.", "effectief"),
            ("De deeltjes botsen met te weinig energie.", "elastisch"),
            ("De deeltjes botsen met genoeg energie en in de juiste stand.", "effectief"),
        ],
        "Alleen effectieve botsingen leiden tot een reactie.",
        kolommen=["elastisch", "effectief"],
    ),
    keuze(
        "Als je een gasmengsel in een kleiner vat perst, wordt de reactie [[*sneller|trager]].",
        "De concentratie stijgt, dus er zijn meer botsingen per seconde.",
    ),
    mk(
        "Waarom verloopt de reactie van waterstof met chloor pas als je er licht op schijnt?",
        ["Het licht levert de activeringsenergie", "Het licht verlaagt de reactie-energie", "Het licht maakt de gassen geconcentreerder", "Het licht werkt als katalysator die opgebruikt wordt"],
        0,
        "Licht geeft de energie om de reactie te doen starten.",
    ),
    tabel(
        "Verandert een katalysator dit?",
        [
            ("de activeringsenergie", J),
            ("de reactie-energie", F),
            ("het deel van de deeltjes met genoeg energie om te reageren", J),
            ("de hoeveelheid product op het einde", F),
        ],
        "Een katalysator maakt de weg korter, niet het begin- of eindpunt.",
    ),
    inv(
        "In 20 s daalt de concentratie van een reagens van 1,0 mol/L naar 0,6 mol/L. Wat is de gemiddelde reactiesnelheid in mol/(L·s)?",
        ["0,02", "0.02"],
        "(1,0 − 0,6) : 20 = 0,02 mol/(L·s).",
    ),
]

VRAGEN = OVER + EIGEN
