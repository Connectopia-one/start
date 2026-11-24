"""Trillingen, golven en geluid — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen fysica Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt, aangevuld met eigen vragen over geluid.
"""
from ..beyond_fys_themas import trillingen as T, golven as G, licht as L
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, casus

OVER = (
    [T.VRAGEN[i] for i in (2, 3, 4, 19, 22, 23, 24)]
    + [G.VRAGEN[i] for i in (3, 4, 10, 19, 20, 22)]
    + [L.VRAGEN[i] for i in (5, 6, 7, 9, 10, 24, 26)]
)

EIGEN = [
    casus(
        "Jonas staat op een festival op 5 m van een luidspreker. Hij meet 104 dB.",
        [
            mk(
                "Hij stapt achteruit tot 10 m van de luidspreker. Hoeveel dB meet hij ongeveer?",
                ["98 dB", "52 dB", "101 dB", "110 dB"],
                0,
                "Twee keer zo ver staan geeft ongeveer 6 dB minder.",
            ),
            mk(
                "Een tweede, even luide luidspreker gaat naast de eerste spelen. Hoeveel dB meet hij dan op 5 m?",
                ["107 dB", "208 dB", "104 dB", "110 dB"],
                0,
                "Twee keer zoveel geluidsintensiteit geeft ongeveer 3 dB meer.",
            ),
            tabel(
                "Is dit een goede maatregel voor zijn gehoor?",
                [
                    ("oordopjes dragen", J),
                    ("af en toe een pauze nemen op een rustige plek", J),
                    ("dicht bij de luidspreker gaan staan zodat het korter duurt", F),
                ],
                "Minder luid en minder lang beschermen allebei.",
            ),
            keuze(
                "Blijvende gehoorschade ontstaat in [[*het binnenoor|het trommelvlies|de oorschelp]], waar de haarcellen beschadigd raken.",
                "Beschadigde haarcellen groeien niet terug.",
            ),
        ],
    ),
    sorteer(
        "Kan een mens dit geluid horen?",
        ["Hoorbaar", "Niet hoorbaar"],
        [
            ("een toon van 440 Hz", "Hoorbaar"),
            ("een fluitje van een hondentrainer op 30 000 Hz", "Niet hoorbaar"),
            ("een trilling van 10 Hz bij een aardbeving", "Niet hoorbaar"),
            ("een vogel die zingt op 4000 Hz", "Hoorbaar"),
        ],
        "Een mens hoort ongeveer van 20 tot 20 000 Hz.",
    ),
    tabel(
        "Mechanische of elektromagnetische golf?",
        [
            ("geluid", "mechanisch"),
            ("licht van de zon", "elektromagnetisch"),
            ("een golf op het water", "mechanisch"),
            ("wifi-signaal", "elektromagnetisch"),
        ],
        "Een mechanische golf heeft een middenstof nodig.",
        kolommen=["mechanisch", "elektromagnetisch"],
    ),
    inv(
        "Een trilling heeft een periode van 0,02 s. Wat is de frequentie, in Hz?",
        ["50"],
        "f = 1 / T = 1 / 0,02 = 50 Hz.",
    ),
    mk(
        "Een echografie gebruikt ultrasoon geluid. Waarom geen röntgenstraling?",
        ["Ultrasoon geluid is niet ioniserend", "Ultrasoon geluid gaat sneller door het lichaam", "Röntgenstraling kan je niet weerkaatsen", "Röntgenstraling is te zacht om iets te zien"],
        0,
        "Daarom is een echografie veilig voor een ongeboren kind.",
    ),
    koppel(
        "Koppel de eigenschap van het geluid aan de eigenschap van de golf.",
        [
            ("toonhoogte", "frequentie"),
            ("luidheid", "amplitude"),
            ("klankkleur", "vorm van de trilling"),
        ],
        ["golfsnelheid"],
        "Wat je hoort, hangt af van wat je op de oscilloscoop ziet.",
    ),
    volgorde(
        "Zet deze middenstoffen van trage naar snelle voortplanting van geluid.",
        ["koude lucht", "warme lucht", "water", "staal"],
        "Hoe dichter en stijver de stof, hoe sneller het geluid.",
    ),
]

VRAGEN = OVER + EIGEN
