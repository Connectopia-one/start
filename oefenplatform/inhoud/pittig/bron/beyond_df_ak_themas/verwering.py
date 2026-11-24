"""Verwering — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom plus één eigen vraag."""
from ..beyond_ak_themas import verwering as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[17]) + [
    tabel("Welke soort verwering is dit?", [
        ("water bevriest in een spleet en wrikt de rots open", "fysisch"),
        ("zuur regenwater lost kalksteen op", "chemisch"),
        ("een boomwortel duwt een rots uit elkaar", "biologisch"),
    ], "Mechanisch, door een reactie, of door levende wezens.",
       kolommen=["fysisch", "chemisch", "biologisch"]),
]
