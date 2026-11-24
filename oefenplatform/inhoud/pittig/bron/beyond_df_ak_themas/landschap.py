"""Landschap en duurzaam ruimtegebruik — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom over het landschap lezen en duurzaam ruimtegebruik, plus eigen vragen."""
from ..beyond_ak_themas import landschap as _B, duurzaam as _D
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[8, 11, 15, 17, 20, 23, 25, 26]) + kies(_D.VRAGEN, enkel=[8, 14, 18, 22, 23, 24]) + [
    tabel("Welke bron gebruik je best?", [
        ("hoe hoog en hoe steil een helling is", "digitaal hoogtemodel"),
        ("of de grond zand, leem of klei is", "bodemkaart"),
        ("welke lagen er onder de grond zitten", "geologische doorsnede"),
    ], "Elke bron toont een ander deel van het landschap.",
       kolommen=["digitaal hoogtemodel", "bodemkaart", "geologische doorsnede"]),
    keuze("Een windpark helpt het doel [[*duurzame energie|leven op het land]], maar kan schade doen aan het doel [[*leven op het land|duurzame energie]] als het in een natuurgebied komt.",
          "Een maatregel kan goed zijn voor het ene doel en slecht voor het andere."),
]
