"""Situeren — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, zonder nadir, plus één eigen vraag."""
from ..beyond_ak_themas import situeren as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[23]) + [
    tabel("Welke hulpbron gebruik je het best?", [
        ("de leeftijdsopbouw van een gemeente bekijken", "leeftijdshistogram"),
        ("temperatuur en neerslag per maand van een stad vergelijken", "klimatogram"),
        ("een onbekend gesteente benoemen aan zijn kenmerken", "determineertabel"),
    ], "Elke hulpbron toont iets anders.", kolommen=["leeftijdshistogram", "klimatogram", "determineertabel"]),
]
