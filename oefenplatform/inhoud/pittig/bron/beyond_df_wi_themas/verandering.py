"""Gemiddelde verandering en het differentiequotiënt — pittig (Beyond dubbele finaliteit, wiskunde).

Enkele pittige vragen wiskunde basis Beyond (met hun prenten) binnen wi_verandering, verder eigen vragen. Geen afgeleiden."""
from ..beyond_wiskunde_basis_themas import afgeleiden as A
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(A.VRAGEN, [2, 3, 10, 24, 25], {"\\\\(f'(x) = 0\\\\) voor elke x": "\\\\(f(x) = 0\\\\) voor elke x"}) + [
    casus(
        "Een fietser houdt bij hoeveel kilometer ze in totaal afgelegd heeft: na \\(0\\) uur \\(0\\) km, na \\(1\\) uur \\(22\\) km, "
        "na \\(2\\) uur \\(40\\) km, na \\(3\\) uur \\(40\\) km en na \\(4\\) uur \\(64\\) km.",
        [
            inv("Wat is haar gemiddelde snelheid over de hele rit, in km/h?", ["16", "16 km/h"], "\\(64 : 4 = 16\\)."),
            inv("Wat is het differentiequotiënt van \\(0\\) tot \\(2\\) uur, in km/h?", ["20", "20 km/h"], "\\((40 - 0) : 2 = 20\\)."),
            keuze("Tussen \\(2\\) en \\(3\\) uur is het differentiequotiënt [[*\\(0\\)|\\(40\\)|\\(20\\)]]: ze nam een pauze.", "De afgelegde weg bleef gelijk."),
            mk("In welk uur reed ze het snelst?",
               ["tussen \\(3\\) en \\(4\\) uur", "tussen \\(0\\) en \\(1\\) uur", "tussen \\(1\\) en \\(2\\) uur", "tussen \\(2\\) en \\(3\\) uur"], 0, "\\(24\\) km in dat uur."),
        ],
    ),
    inv("\\(f(-2) = 9\\) en \\(f(1) = -3\\). Hoeveel is het differentiequotiënt over \\([-2, 1]\\)?", ["-4", "−4", "min 4"], "\\((-3 - 9) : (1 - (-2)) = -12 : 3\\)."),
    inv("\\(f(x) = x^{2}\\). Hoeveel is het differentiequotiënt over \\([1, 5]\\)?", ["6", "zes"], "\\((25 - 1) : 4\\)."),
    inv("\\(f(x) = x^{2}\\). Hoeveel is het differentiequotiënt over \\([-3, 3]\\)?", ["0", "nul"], "\\(f(-3) = f(3) = 9\\)."),
    mk("\\(f(x) = -2x + 7\\). Wat is het differentiequotiënt over \\([10, 50]\\)?",
       ["\\(-2\\)", "\\(7\\)", "\\(-80\\)", "\\(40\\)"], 0, "Bij een rechte is het differentiequotiënt altijd de richtingscoëfficiënt."),
    tabel("Klopt dit?", [
        ("Een differentiequotiënt zegt wat er op elk moment in het interval gebeurt.", F),
        ("Bij een rechte is het differentiequotiënt over elk interval hetzelfde.", J),
        ("Teller en noemer mag je omdraaien zonder dat het resultaat verandert.", F),
        ("Bij een kromme hangt het differentiequotiënt af van het interval.", J),
    ], "Het is een gemiddelde over het hele interval."),
    tabel("Welke eenheid hoort bij het differentiequotiënt?", [
        ("afgelegde weg in km in functie van de tijd in uur", "km/h"), ("aantal inwoners in functie van de tijd in jaar", "inwoners per jaar"),
        ("inhoud van een tank in liter in functie van de tijd in minuut", "liter per minuut"),
    ], "De eenheid van \\(y\\) per eenheid van \\(x\\).", kolommen=["km/h", "inwoners per jaar", "liter per minuut"]),
    mk("Een bergpas stijgt \\(450\\) meter over een horizontale afstand van \\(6\\) kilometer. Wat is de gemiddelde helling?",
       ["\\(7{,}5\\) procent", "\\(75\\) procent", "\\(0{,}75\\) procent", "\\(13{,}3\\) procent"], 0, "\\(450 : 6000 = 0{,}075\\)."),
    inv("Een stad telde \\(48\\,000\\) inwoners in 2015 en \\(51\\,000\\) in 2025. Hoeveel inwoners kwamen er gemiddeld per jaar bij?", ["300", "300 inwoners"], "\\(3000 : 10\\)."),
    mk("Een waterton gaat in \\(8\\) minuten van \\(120\\) naar \\(40\\) liter. Wat is het differentiequotiënt?",
       ["\\(-10\\) liter per minuut", "\\(10\\) liter per minuut", "\\(-80\\) liter per minuut", "\\(-5\\) liter per minuut"], 0, "\\((40 - 120) : 8\\)."),
    keuze("Een groter differentiequotiënt betekent een [[*steilere|hogere|lagere]] snijlijn, niet noodzakelijk een [[*hogere functiewaarde|steilere snijlijn|langer interval]].", "Het gaat over de verandering, niet over de hoogte."),
    mk("Het differentiequotiënt is \\(2\\) op de eerste helft van een interval en \\(6\\) op de tweede helft. Wat is het over het hele interval?",
       ["\\(4\\)", "\\(8\\)", "\\(12\\)", "\\(3\\)"], 0, "Twee even lange helften: het gemiddelde van \\(2\\) en \\(6\\)."),
    sorteer("Is het differentiequotiënt positief, nul of negatief?", ["positief", "nul", "negatief"], [
        ["de temperatuur gaat van \\(5\\) naar \\(12\\) graden", "positief"], ["een spaarpot gaat van \\(40\\) naar \\(40\\) euro", "nul"],
        ["een kaars gaat van \\(20\\) naar \\(14\\) cm", "negatief"], ["een plant groeit van \\(8\\) naar \\(15\\) cm", "positief"],
    ], "Kijk alleen naar begin en einde."),
    inv("Een rechte gaat door \\((2, -1)\\) en \\((6, 7)\\). Wat is haar richtingscoëfficiënt?", ["2", "twee"], "\\((7 - (-1)) : (6 - 2) = 8 : 4\\)."),
    mk("Een tank bevat \\(100\\) liter en verliest gemiddeld \\(4\\) liter per minuut. Na hoeveel minuten is hij leeg, als dat tempo blijft?",
       ["\\(25\\) minuten", "\\(400\\) minuten", "\\(96\\) minuten", "\\(4\\) minuten"], 0, "\\(100 : 4\\)."),
    open_("Leg uit waarom een gemiddelde snelheid van \\(0\\) km/h niet betekent dat je niet bewogen hebt.",
          "Een gemiddelde snelheid van nul betekent alleen dat je begin- en eindpunt op dezelfde afstand liggen. Je kan intussen heen en terug gereden zijn.",
          "Het differentiequotiënt kijkt enkel naar begin- en eindwaarde."),
    volgorde("Zet de stappen om een differentiequotiënt uit een grafiek te bepalen in volgorde.", [
        "de functiewaarden aan het begin en het einde van het interval aflezen", "het verschil van de functiewaarden berekenen", "het verschil van de \\(x\\)-waarden berekenen", "het eerste verschil delen door het tweede",
    ], "Verandering van \\(y\\) gedeeld door verandering van \\(x\\)."),
    tabel("Op welk interval is het differentiequotiënt van \\(f(x) = x^{2}\\) het grootst?", [
        ("\\([0, 1]\\)", "\\(1\\)"), ("\\([1, 3]\\)", "\\(4\\)"), ("\\([2, 4]\\)", "\\(6\\)"),
    ], "\\(\\tfrac{1 - 0}{1}\\), \\(\\tfrac{9 - 1}{2}\\) en \\(\\tfrac{16 - 4}{2}\\).", kolommen=["\\(1\\)", "\\(4\\)", "\\(6\\)"]),
    inv("Een bedrijf telde \\(800\\) klanten in maart en \\(2000\\) in september. Hoeveel klanten kwamen er gemiddeld per maand bij?", ["200", "200 klanten"], "Zes maanden: \\(1200 : 6\\)."),
    koppel("Koppel elke situatie aan haar differentiequotiënt.", [
        ["\\(150\\) km in \\(2\\) uur", "\\(75\\) km/h"], ["van \\(20\\) naar \\(5\\) graden in \\(5\\) uur", "\\(-3\\) graden per uur"],
        ["van \\(1000\\) naar \\(1200\\) euro in \\(4\\) jaar", "\\(50\\) euro per jaar"], ["van \\(12\\) naar \\(30\\) cm in \\(6\\) weken", "\\(3\\) cm per week"],
    ], ["\\(300\\) km/h"], "Verandering gedeeld door de duur."),
    keuze("Het differentiequotiënt over een interval is de richtingscoëfficiënt van de rechte door [[*het begin- en het eindpunt|de top|de oorsprong]] van dat stuk grafiek.", "Die rechte heet een snijlijn."),
    inv("Een tabel geeft bij \\(x = 3\\) de waarde \\(14\\) en bij \\(x = 11\\) de waarde \\(-2\\). Wat is het differentiequotiënt?", ["-2", "−2", "min 2"],
        "\\((-2 - 14) : (11 - 3) = -16 : 8\\)."),
]
