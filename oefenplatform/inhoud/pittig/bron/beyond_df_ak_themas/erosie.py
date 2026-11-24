"""Erosie — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom plus twee eigen vragen."""
from ..beyond_ak_themas import erosie as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[9, 10]) + [
    tabel("Bovenloop, middenloop of benedenloop?", [
        ("steil verval, V-dal en grote rolstenen", "bovenloop"),
        ("brede meanders en een alluviale vlakte met fijn slib", "benedenloop"),
        ("het verval neemt af en de rivier begint te kronkelen", "middenloop"),
    ], "Van bron naar monding daalt het verval en worden de korrels kleiner.",
       kolommen=["bovenloop", "middenloop", "benedenloop"]),
    keuze("Een rivier stroomt 0,1 m/s. Volgens het Hjülströmdiagram blijven klei en slib dan [[*zweven|bezinken]], terwijl grind [[*blijft liggen|in suspensie gaat]].",
          "Kleine korrels zweven bij lage snelheid nog; grote korrels hebben veel meer snelheid nodig."),
]
