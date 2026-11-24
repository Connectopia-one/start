"""Bewegingen — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom plus één eigen vraag."""
from ..beyond_ak_themas import bewegingen as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[25]) + [
    inv("Het is 14 uur conventionele tijd in Brussel in de winter. Hoe laat is het dan in een stad in de uurgordel die 3 gordels oostelijker ligt? Geef het uur als getal.", ["17"],
        "Per uurgordel naar het oosten gaat de klok één uur vooruit: 14 + 3 = 17."),
]
