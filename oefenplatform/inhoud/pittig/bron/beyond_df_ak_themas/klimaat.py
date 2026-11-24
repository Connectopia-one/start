"""Klimaat — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, zonder de thermohaliene circulatie, plus eigen vragen."""
from ..beyond_ak_themas import weer as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[14, 15, 16]) + [
    tabel("Welk klimaat past bij dit klimatogram?", [
        ("het hele jaar rond 27 °C en elke maand meer dan 150 mm", "tropisch regenwoud"),
        ("hete, droge zomers en zachte, natte winters", "mediterraan"),
        ("bijna geen neerslag en grote verschillen tussen dag en nacht", "woestijn"),
    ], "Lees temperatuur en neerslag samen.", kolommen=["tropisch regenwoud", "mediterraan", "woestijn"]),
    keuze("In een klimatogram van Buenos Aires liggen de warmste maanden [[*aan de randen, in december en januari|in het midden, in juli]].",
          "Op het zuidelijk halfrond is het zomer als het bij ons winter is."),
    mk("In de toendra valt genoeg neerslag voor mossen en grassen. Wat houdt er de bomen tegen?",
       ["de altijd bevroren ondergrond",
        "er valt te veel neerslag voor boomwortels",
        "de zon schijnt er het hele jaar niet",
        "de grond bestaat er overal uit kaal gesteente"], 0,
       "Wortels kunnen niet diep in de altijd bevroren ondergrond."),
]
