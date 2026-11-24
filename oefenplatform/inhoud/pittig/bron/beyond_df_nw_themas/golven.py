"""Golven, geluid en straling — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen natuurwetenschappen en fysica Beyond over golven, geluid en het spectrum binnen nwd_golven, plus eigen vragen."""
from ..beyond_nw_themas import trillingen as T, spectrum as SP
from ..beyond_fys_themas import golven as G
from ..beyond_fys_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(T.VRAGEN, [1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 20, 21, 22, 24]) + kies(SP.VRAGEN, [2, 11, 17, 22, 23]) + kies(G.VRAGEN, [26]) + [
    tabel("Klopt dit over geluidsniveaus?", [
        ("De gehoordrempel ligt bij \\(0\\) dB.", J),
        ("Vanaf ongeveer \\(120\\) dB doet geluid pijn.", J),
        ("Twee keer zoveel geluidsintensiteit geeft twee keer zoveel decibel.", F),
        ("Beschadigde haarcellen groeien altijd weer aan.", F),
    ], "Dubbele intensiteit is maar \\(3\\) dB meer; haarcellen herstellen niet."),
    mk("Een sonar op een schip hoort de echo van de zeebodem na \\(0{,}4\\) s. Geluid gaat \\(1500\\) m/s in water. Hoe diep is de zee?",
       ["\\(300\\) m", "\\(600\\) m", "\\(150\\) m", "\\(3750\\) m"], 0,
       "Heen en terug duurt \\(0{,}4\\) s, dus enkel heen \\(0{,}2\\) s: \\(1500 \\cdot 0{,}2 = 300\\) m."),
    keuze("Een loodschort beschermt bij een röntgenfoto, omdat lood röntgenstraling [[*tegenhoudt|weerkaatst als een spiegel|omzet in geluid]].", "Röntgenstraling is ioniserend; lood absorbeert ze."),
]
