"""De normale verdeling en de Gausskromme — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond (met hun prenten) binnen wi_normaal, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import normaal as N
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27]) + [
    mk("Een IQ-test heeft gemiddelde \\(100\\) en standaardafwijking \\(15\\). Welk aandeel scoort tussen \\(85\\) en \\(130\\)?",
       ["ongeveer \\(81{,}5\\) %", "ongeveer \\(68\\) %", "ongeveer \\(95\\) %", "ongeveer \\(47{,}5\\) %"], 0,
       "Van \\(85\\) tot \\(100\\) is de helft van \\(68\\) %, dus \\(34\\) %. Van \\(100\\) tot \\(130\\) is de helft van \\(95\\) %, dus \\(47{,}5\\) %. Samen \\(81{,}5\\) %."),
    tabel("Een vulmachine werkt normaal verdeeld rond \\(500\\) g. Klopt dit?", [
        ("Een kleinere standaardafwijking betekent dat de zakken nauwkeuriger gevuld zijn.", J),
        ("Ongeveer de helft van de zakken weegt minder dan \\(500\\) g.", J),
        ("Geen enkele zak kan ooit meer dan \\(520\\) g wegen.", F),
    ], "De kromme raakt de as nooit: heel uitzonderlijke waarden blijven mogelijk."),
    inv("De lengte van volwassen mannen is normaal verdeeld met gemiddelde \\(178\\) cm en standaardafwijking \\(7\\) cm. Hoeveel procent is ongeveer korter dan \\(164\\) cm?",
        ["2,5", "2,5 %", "2.5"], "\\(164\\) ligt twee standaardafwijkingen onder het gemiddelde. Buiten twee standaardafwijkingen ligt \\(5\\) %, aan elke kant de helft."),
]
