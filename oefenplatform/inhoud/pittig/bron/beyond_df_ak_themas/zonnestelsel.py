"""Zonnestelsel — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, zonder de lagen van de zon, plus eigen vragen."""
from ..beyond_ak_themas import zonnestelsel as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, sorteer
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[1, 2, 3, 4, 21, 22, 26]) + [
    volgorde("Zet deze planeten in volgorde, van dicht bij de zon naar ver.", [
        "Venus", "Mars", "Saturnus", "Neptunus",
    ], "Mercurius, Venus, Aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus."),
    tabel("Klopt dit over Venus en Mars?", [
        ("Venus is warmer dan Mercurius door haar dikke atmosfeer", J),
        ("Mars houdt door zijn kleine zwaartekracht weinig atmosfeer vast", J),
        ("Venus heeft vloeibare oceanen zoals de aarde", F),
    ], "Een dikke atmosfeer houdt warmte vast; een kleine planeet houdt zijn gassen slecht vast."),
    inv("Een planeet doet 12 aardse jaren over één omloop. Hoeveel keer draait de aarde rond de zon terwijl die planeet er 3 omlopen maakt?", ["36"],
        "3 · 12 = 36."),
    mk("Waarom zie je op de maan veel meer inslagkraters dan op de aarde?",
       ["de maan heeft geen atmosfeer en geen erosie",
        "de maan trekt meer meteorieten aan dan de aarde",
        "op aarde vallen nooit grote meteorieten",
        "de maan staat dichter bij de planetoïdengordel"], 0,
       "Zonder lucht verbranden brokken niet, en zonder wind en water blijven kraters bewaard."),
    sorteer("Waar komt dit object vandaan?", ["planetoïdengordel", "voorbij Neptunus"], [
        ["Ceres", "planetoïdengordel"],
        ["Pluto", "voorbij Neptunus"],
        ["Eris", "voorbij Neptunus"],
        ["een rotsbrok tussen Mars en Jupiter", "planetoïdengordel"],
    ], "Ceres ligt in de gordel; Pluto en Eris in de Kuipergordel."),
    keuze("Jupiter beschermt de aarde een beetje, omdat zijn [[*zwaartekracht|magneetveld|atmosfeer]] veel kometen en planetoïden afbuigt.",
          "Zijn grote massa trekt brokken weg uit de binnenste banen."),
    tabel("Is dit een gevolg van een grote inslag op aarde?", [
        ("een inslagkrater", J),
        ("het uitsterven van veel soorten, zoals de dinosauriërs", J),
        ("de seizoenen", F),
    ], "De seizoenen komen door de scheve aardas."),
]
