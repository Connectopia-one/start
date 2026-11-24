"""Gesteenten — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, zonder mineralen en losse gesteentenamen, plus eigen vragen."""
from ..beyond_ak_themas import gesteenten as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, sorteer
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[8, 12, 18, 23, 26]) + [
    tabel("Magmatisch, sedimentair of metamorf?", [
        ("graniet, langzaam gestold diep in de korst", "magmatisch"),
        ("marmer, ontstaan uit kalksteen onder druk en warmte", "metamorf"),
        ("zandsteen, uit verkitte zandkorrels", "sedimentair"),
        ("steenkool, uit plantenresten in moerassen", "sedimentair"),
    ], "Uit magma, uit afzettingen, of omgevormd zonder te smelten.",
       kolommen=["magmatisch", "sedimentair", "metamorf"]),
    volgorde("Zet deze plooiingen van oud naar jong.", [
        "Caledonische plooiing", "Hercynische plooiing", "Alpiene plooiing",
    ], "De Alpiene plooiing is de jongste en duurt nog voort."),
    inv("Een stof heeft een halveringstijd van 5 730 jaar. Hoeveel procent is er na 11 460 jaar nog over?", ["25", "25%", "25 procent"],
        "Twee halveringstijden: de helft van de helft."),
    mk("Een intrusie van graniet snijdt door drie lagen kalksteen. Wat besluit je?",
       ["de graniet is jonger dan de drie lagen",
        "de graniet is ouder dan de onderste laag",
        "de graniet is even oud als de middelste laag",
        "je kan er niets over de ouderdom uit afleiden"], 0,
       "Wat door een laag snijdt, moet er later bij gekomen zijn."),
    sorteer("Hoort deze methode bij relatieve of bij absolute datering?", ["relatieve datering", "absolute datering"], [
        ["superpositie van lagen", "relatieve datering"],
        ["een halveringstijd gebruiken", "absolute datering"],
        ["een gidsfossiel vergelijken", "relatieve datering"],
        ["koolstof-14 meten", "absolute datering"],
    ], "Relatief: ouder of jonger. Absoluut: een leeftijd in jaren."),
]
