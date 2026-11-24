"""Overerving van genetisch materiaal — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt, aangevuld met eigen vragen.
"""
from ..beyond_bio_themas import overerving as O
from .vormen import J, F, mk, inv, tabel, keuze

OVER = [O.VRAGEN[i] for i in range(28) if i not in (9, 18, 20)]

EIGEN = [
    tabel(
        "Een plant AaBb wordt gekruist met een plant aabb. Welk deel van de nakomelingen verwacht je met dit fenotype?",
        [
            ("beide dominante kenmerken", "1/4"),
            ("enkel het dominante kenmerk A", "1/4"),
            ("beide recessieve kenmerken", "1/4"),
            ("minstens één dominant kenmerk", "3/4"),
        ],
        "Een terugkruising van een dihybride geeft 1 : 1 : 1 : 1.",
        kolommen=["1/4", "1/2", "3/4"],
    ),
    keuze(
        "Een koppel heeft al drie dochters. De kans dat hun vierde kind een jongen is, is [[*50 procent|75 procent|100 procent]].",
        "Elke zwangerschap staat los van de vorige.",
    ),
    mk(
        "Een raszuivere rode bloem wordt gekruist met een raszuivere witte. Alle nakomelingen zijn roze. Wat besluit je?",
        ["De overerving is intermediair", "Rood is dominant over wit", "Wit is dominant over rood", "De ouders waren heterozygoot"],
        0,
        "De heterozygoot toont een tussenvorm.",
    ),
]

VRAGEN = OVER + EIGEN
