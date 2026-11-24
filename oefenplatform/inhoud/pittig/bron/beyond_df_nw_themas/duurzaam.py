"""Duurzaamheid, circulaire economie en kunststoffen — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen chemie Beyond (ladder van Lansink, economieën, waterstof, kunststoffen) binnen nwd_duurzaam, plus eigen vragen."""
from ..beyond_chem_themas import duurzaam as D, kunststoffen as K
from ..beyond_chem_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 19, 20, 21, 23, 25, 26, 27]) + kies(K.VRAGEN, [0, 1, 2, 3, 12, 13, 24]) + [
    koppel("Koppel elk voorbeeld aan wat er met het materiaal gebeurt.", [
        ["een oude ladder wordt een boekenrek", "upcycling"], ["een petfles wordt een bloempot", "downcycling"],
        ["een glazen fles wordt opnieuw gevuld", "hergebruik"], ["een drinkbus in plaats van wegwerpflesjes", "preventie"],
    ], ["storten"], "Bij upcycling stijgt de waarde, bij downcycling daalt de kwaliteit."),
    tabel("Is deze energievorm hernieuwbaar?", [
        ("zonne-energie", J), ("steenkool", F), ("windenergie", J), ("aardgas", F),
    ], "Zon en wind raken niet op; steenkool en aardgas zijn fossiel."),
]
