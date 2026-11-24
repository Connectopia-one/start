"""Machtswortels en machten met rationale exponent — pittig (Beyond dubbele finaliteit, wiskunde).

Enkele pittige vragen wiskunde basis Beyond binnen wi_machten, verder eigen vragen."""
from ..beyond_wiskunde_basis_themas import machten as M
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(M.VRAGEN, [0, 1, 3, 4, 15, 17, 18, 25]) + [
    casus(
        "Een kubusvormige waterton heeft een inhoud van \\(216\\) liter, dus \\(216\\) kubieke decimeter. "
        "Een tweede, grotere ton heeft een inhoud van \\(512\\) kubieke decimeter.",
        [
            inv("Hoe lang is een ribbe van de eerste ton, in dm?", ["6", "6 dm", "zes"], "\\(\\sqrt[3]{216} = 6\\)."),
            inv("Hoe lang is een ribbe van de tweede ton, in dm?", ["8", "8 dm", "acht"], "\\(\\sqrt[3]{512} = 8\\)."),
            mk("Hoe schrijf je de ribbe van een kubus met inhoud \\(V\\) als macht?",
               ["\\(V^{\\tfrac{1}{3}}\\)", "\\(V^{3}\\)", "\\(V^{-\\tfrac{1}{3}}\\)", "\\(3^{V}\\)"], 0, "Een derdemachtswortel is een macht met exponent een derde."),
        ],
    ),
    tabel("Hoeveel is dit?", [
        ("\\(32^{\\tfrac{2}{5}}\\)", "\\(4\\)"), ("\\(8^{\\tfrac{2}{3}}\\)", "\\(4\\)"), ("\\(9^{\\tfrac{3}{2}}\\)", "\\(27\\)"), ("\\(64^{\\tfrac{1}{3}}\\)", "\\(4\\)"), ("\\(81^{\\tfrac{3}{4}}\\)", "\\(27\\)"),
    ], "Eerst de wortel, dan de macht: dat houdt de getallen klein.", kolommen=["\\(4\\)", "\\(27\\)"]),
    inv("Hoeveel is \\(4^{-\\tfrac{1}{2}}\\)? Schrijf het als decimaal getal.", ["0,5", "0.5", "1/2"], "\\(4^{\\tfrac{1}{2}} = 2\\), en de negatieve exponent keert om."),
    mk("Welke uitdrukking is gelijk aan \\(a^{\\tfrac{3}{4}} \\cdot a^{\\tfrac{1}{4}}\\)?",
       ["\\(a\\)", "\\(a^{\\tfrac{3}{16}}\\)", "\\(a^{\\tfrac{1}{2}}\\)", "\\(a^{3}\\)"], 0, "Drie vierde plus een vierde is één."),
    mk("Welke uitdrukking is gelijk aan \\(\\left(a^{\\tfrac{2}{3}}\\right)^{6}\\)?",
       ["\\(a^{4}\\)", "\\(a^{\\tfrac{20}{3}}\\)", "\\(a^{9}\\)", "\\(a^{\\tfrac{1}{9}}\\)"], 0, "Macht van een macht: \\(\\tfrac{2}{3} \\cdot 6 = 4\\)."),
    tabel("Klopt dit?", [
        ("\\(5^{0} = 1\\)", J), ("\\(\\left(2 + 3\\right)^{2} = 2^{2} + 3^{2}\\)", F),
        ("\\(\\left(2 \\cdot 3\\right)^{2} = 2^{2} \\cdot 3^{2}\\)", J), ("\\(2^{3} \\cdot 3^{2} = 6^{5}\\)", F),
    ], "Een macht van een product mag je verdelen, een macht van een som niet; verschillende grondtallen mag je niet samennemen."),
    inv("Tussen welke twee gehele getallen ligt \\(\\sqrt[3]{50}\\)? Geef het kleinste.", ["3", "drie"], "\\(3^{3} = 27\\) en \\(4^{3} = 64\\)."),
    volgorde("Zet van klein naar groot.", [
        "\\(2^{-2}\\)", "\\(16^{\\tfrac{1}{4}}\\)", "\\(\\sqrt{9}\\)", "\\(8^{\\tfrac{2}{3}}\\)", "\\(2^{3}\\)",
    ], "\\(0{,}25\\), \\(2\\), \\(3\\), \\(4\\) en \\(8\\)."),
    keuze("\\(\\sqrt[4]{-16}\\) [[*bestaat niet|is gelijk aan \\(-2\\)|is gelijk aan \\(2\\)]] binnen de reële getallen, maar \\(\\sqrt[3]{-8}\\) [[*is gelijk aan \\(-2\\)|bestaat niet|is gelijk aan \\(2\\)]].", "Een even wortel uit een negatief getal bestaat niet; een oneven wel."),
    mk("Een leerling rekent \\(\\sqrt{7}\\) eerst af op \\(2{,}6\\) en rekent daarna \\(\\left(\\sqrt{7}\\right)^{2}\\) uit als \\(2{,}6^{2} = 6{,}76\\). Wat is er mis?",
       ["Hij rondde te vroeg af; het juiste antwoord is precies \\(7\\).", "Niets, \\(6{,}76\\) is het juiste antwoord, want hij rekende correct.", "Hij moest \\(\\sqrt{7}\\) eerst afronden op \\(3\\), dat is eenvoudiger.", "Een wortel mag je nooit in het kwadraat brengen."], 0,
       "Rond pas af op het einde."),
    inv("Hoe schrijf je \\(\\sqrt[4]{x^{3}}\\) als macht van \\(x\\)? Geef enkel de exponent als breuk.", ["3/4", "3 / 4"], "De macht onder de wortel komt in de teller, de wortelexponent in de noemer."),
    koppel("Koppel elke wortel aan de macht die hetzelfde betekent.", [
        ["\\(\\sqrt{a}\\)", "\\(a^{\\tfrac{1}{2}}\\)"], ["\\(\\sqrt[3]{a}\\)", "\\(a^{\\tfrac{1}{3}}\\)"],
        ["\\(\\sqrt[3]{a^{2}}\\)", "\\(a^{\\tfrac{2}{3}}\\)"], ["\\(\\sqrt{a^{3}}\\)", "\\(a^{\\tfrac{3}{2}}\\)"],
    ], ["\\(a^{3}\\)"], "Teller: de macht. Noemer: de wortel."),
    mk("Een vierkant tuinhuis heeft een vloer van \\(20\\) vierkante meter. Hoe lang is een zijde, afgerond op een centimeter?",
       ["\\(4{,}47\\) m", "\\(5{,}00\\) m", "\\(10{,}00\\) m", "\\(4{,}00\\) m"], 0, "\\(\\sqrt{20} \\approx 4{,}472\\)."),
    inv("Hoeveel is \\(\\dfrac{2^{5} \\cdot 2^{-2}}{2^{2}}\\)?", ["2", "twee"], "\\(2^{5 - 2 - 2} = 2^{1}\\)."),
    sorteer("Is het resultaat een geheel getal of niet?", ["geheel getal", "geen geheel getal"], [
        ["\\(27^{\\tfrac{1}{3}}\\)", "geheel getal"], ["\\(2^{-1}\\)", "geen geheel getal"], ["\\(\\sqrt{12}\\)", "geen geheel getal"],
        ["\\(100^{\\tfrac{3}{2}}\\)", "geheel getal"], ["\\(10^{-2}\\)", "geen geheel getal"],
    ], "\\(100^{\\tfrac{3}{2}} = 10^{3} = 1000\\)."),
    open_("Leg uit waarom \\(25^{\\tfrac{3}{2}}\\) gelijk is aan \\(125\\).",
          "De exponent drie halve betekent eerst de vierkantswortel en dan de derde macht. \\(\\sqrt{25} = 5\\) en \\(5^{3} = 125\\).",
          "Noemer is de wortel, teller is de macht."),
    keuze("\\(a^{\\tfrac{1}{2}} : a^{\\tfrac{1}{3}} = a^{[[*\\tfrac{1}{6}|\\tfrac{3}{2}|\\tfrac{5}{6}]]}\\)", "Een half min een derde is een zesde."),
    inv("Een bacteriecultuur verdubbelt elk uur. Met welke factor groeit ze in een half uur? Rond af op twee cijfers na de komma.", ["1,41", "1.41"], "\\(2^{\\tfrac{1}{2}} = \\sqrt{2} \\approx 1{,}41\\)."),
    mk("Welke uitdrukking is gelijk aan \\(\\dfrac{1}{\\sqrt[3]{x}}\\) (met \\(x > 0\\))?",
       ["\\(x^{-\\tfrac{1}{3}}\\)", "\\(x^{-3}\\)", "\\(x^{\\tfrac{1}{3}}\\)", "\\(-x^{\\tfrac{1}{3}}\\)"], 0, "Omkeren geeft een negatieve exponent."),
    tabel("Is het resultaat groter of kleiner dan \\(1\\)?", [
        ("\\(3^{-2}\\)", "kleiner"), ("\\(0{,}5^{-1}\\)", "groter"), ("\\(16^{\\tfrac{1}{4}}\\)", "groter"), ("\\(\\left(\\tfrac{1}{4}\\right)^{\\tfrac{1}{2}}\\)", "kleiner"),
    ], "\\(\\tfrac{1}{9}\\), \\(2\\), \\(2\\) en \\(\\tfrac{1}{2}\\).", kolommen=["kleiner", "groter"]),
]
