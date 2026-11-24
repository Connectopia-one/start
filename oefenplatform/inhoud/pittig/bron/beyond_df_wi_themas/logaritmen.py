"""Logaritmen — pittig (Beyond dubbele finaliteit, wiskunde).

Enkele pittige vragen wiskunde basis Beyond binnen wi_logaritmen, verder eigen vragen. Enkel het verband met machten, grondtal 10 en logaritmische schalen."""
from ..beyond_wiskunde_basis_themas import machten as M
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(M.VRAGEN, [5, 10, 13, 14, 21, 22, 24, 26]) + [
    casus(
        "De zuurtegraad van water noteer je met de pH. Voor een oplossing geldt: pH \\(= -\\log_{10} c\\), met \\(c\\) de concentratie waterstofionen. "
        "Zuiver water heeft \\(c = 10^{-7}\\), citroensap ongeveer \\(c = 10^{-2}\\).",
        [
            inv("Wat is de pH van zuiver water?", ["7", "zeven"], "\\(-\\log_{10} 10^{-7} = 7\\)."),
            inv("Wat is de pH van citroensap?", ["2", "twee"], "\\(-\\log_{10} 10^{-2} = 2\\)."),
            mk("Hoeveel keer zo groot is \\(c\\) in citroensap als in zuiver water?",
               ["\\(100\\,000\\) keer", "\\(5\\) keer", "\\(3{,}5\\) keer", "\\(1000\\) keer"], 0, "\\(10^{-2} : 10^{-7} = 10^{5}\\)."),
            keuze("Eén eenheid lager op de pH-schaal betekent een concentratie die [[*tien keer zo groot|tien keer zo klein|één eenheid groter]] is.", "Elke stap op een logaritmische schaal is een factor tien."),
        ],
    ),
    tabel("Hoeveel is deze logaritme?", [
        ("\\(\\log_{10} 10\\,000\\)", "\\(4\\)"), ("\\(\\log_{2} 16\\)", "\\(4\\)"), ("\\(\\log_{10} 0{,}001\\)", "\\(-3\\)"), ("\\(\\log_{3} \\tfrac{1}{27}\\)", "\\(-3\\)"), ("\\(\\log_{5} 625\\)", "\\(4\\)"),
    ], "Zoek telkens tot welke macht je het grondtal verheft.", kolommen=["\\(-3\\)", "\\(4\\)"]),
    koppel("Koppel elke logaritme aan de macht die hetzelfde zegt.", [
        ["\\(\\log_{2} 32 = 5\\)", "\\(2^{5} = 32\\)"], ["\\(\\log_{10} 0{,}01 = -2\\)", "\\(10^{-2} = 0{,}01\\)"],
        ["\\(\\log_{9} 3 = \\tfrac{1}{2}\\)", "\\(9^{\\tfrac{1}{2}} = 3\\)"], ["\\(\\log_{4} 1 = 0\\)", "\\(4^{0} = 1\\)"],
    ], ["\\(5^{2} = 32\\)"], "Een logaritme is een exponent."),
    inv("Hoeveel is \\(\\log_{2} \\tfrac{1}{16}\\)?", ["-4", "−4", "min 4"], "\\(2^{-4} = \\tfrac{1}{16}\\)."),
    inv("Hoeveel is \\(\\log_{8} 2\\)? Schrijf het als breuk.", ["1/3", "1 / 3", "een derde"], "\\(8^{\\tfrac{1}{3}} = 2\\)."),
    mk("Tussen welke twee gehele getallen ligt \\(\\log_{10} 4500\\)?",
       ["tussen \\(3\\) en \\(4\\)", "tussen \\(4\\) en \\(5\\)", "tussen \\(45\\) en \\(46\\)", "tussen \\(2\\) en \\(3\\)"], 0, "\\(10^{3} = 1000\\) en \\(10^{4} = 10\\,000\\)."),
    sorteer("Is de logaritme met grondtal \\(10\\) positief, nul, of bestaat ze niet?", ["positief", "nul", "bestaat niet"], [
        ["\\(\\log_{10} 25\\)", "positief"], ["\\(\\log_{10} 1\\)", "nul"], ["\\(\\log_{10} 0\\)", "bestaat niet"], ["\\(\\log_{10} (-10)\\)", "bestaat niet"], ["\\(\\log_{10} 1{,}5\\)", "positief"],
    ], "Alleen van een positief getal bestaat de logaritme."),
    mk("Een aardbeving van \\(7\\) op de schaal van Richter is hoeveel keer sterker dan een van \\(4\\), als elke stap een factor \\(10\\) is?",
       ["\\(1000\\) keer", "\\(3\\) keer", "\\(30\\) keer", "\\(1{,}75\\) keer"], 0, "Drie stappen: \\(10^{3}\\)."),
    inv("Los op: \\(5^{x} = 625\\). Hoeveel is \\(x\\)?", ["4", "vier"], "\\(\\log_{5} 625 = 4\\)."),
    inv("Los op: \\(10^{x} = 0{,}0001\\). Hoeveel is \\(x\\)?", ["-4", "−4", "min 4"], "\\(0{,}0001 = 10^{-4}\\)."),
    mk("Je lost \\(2^{x} = 100\\) op. Wat weet je al zonder rekentoestel?",
       ["\\(x\\) ligt tussen \\(6\\) en \\(7\\)", "\\(x\\) ligt tussen \\(1\\) en \\(2\\)", "\\(x = 50\\)", "\\(x\\) ligt tussen \\(9\\) en \\(10\\)"], 0, "\\(2^{6} = 64\\) en \\(2^{7} = 128\\)."),
    tabel("Klopt dit over logaritmen?", [
        ("\\(\\log_{10} 2 \\approx 0{,}30\\), dus \\(\\log_{10} 200 \\approx 2{,}30\\).", J),
        ("\\(\\log_{10} 50\\) ligt tussen \\(5\\) en \\(6\\).", F),
        ("Een getal tien keer zo groot maken verhoogt de logaritme met grondtal \\(10\\) met \\(1\\).", J),
        ("De logaritme van \\(100\\) is bij elk grondtal \\(2\\).", F),
    ], "\\(50\\) ligt tussen \\(10\\) en \\(100\\), dus de logaritme tussen \\(1\\) en \\(2\\)."),
    keuze("Een rekentoestel geeft \\(\\log_{10} x = 4{,}2\\). Dan ligt \\(x\\) tussen [[*\\(10\\,000\\) en \\(100\\,000\\)|\\(4\\) en \\(5\\)|\\(100\\) en \\(1000\\)]].", "\\(10^{4}\\) en \\(10^{5}\\)."),
    volgorde("Zet deze logaritmen van klein naar groot.", [
        "\\(\\log_{10} 0{,}01\\)", "\\(\\log_{7} 1\\)", "\\(\\log_{4} 2\\)", "\\(\\log_{2} 8\\)", "\\(\\log_{10} 100\\,000\\)",
    ], "\\(-2\\), \\(0\\), \\(\\tfrac{1}{2}\\), \\(3\\) en \\(5\\)."),
    mk("Een spaarbedrag groeit met \\(4\\) procent per jaar. Welke vergelijking los je op om te weten na hoeveel jaar het verdubbeld is?",
       ["\\(1{,}04^{t} = 2\\)", "\\(1{,}04 \\cdot t = 2\\)", "\\(t^{1{,}04} = 2\\)", "\\(0{,}04^{t} = 2\\)"], 0, "De onbekende staat in de exponent: daar heb je een logaritme voor nodig."),
    open_("Leg uit waarom \\(\\log_{10} 0\\) niet bestaat.",
          "Een logaritme zoekt de exponent waarmee \\(10\\) een getal geeft. Hoe je \\(10\\) ook verheft, je krijgt altijd een positief getal en nooit \\(0\\). Er is dus geen exponent die past.",
          "Elke macht van een positief grondtal is positief."),
    inv("Hoeveel is \\(\\log_{10} \\sqrt{10}\\)? Schrijf het als kommagetal.", ["0,5", "0.5", "1/2"], "\\(\\sqrt{10} = 10^{\\tfrac{1}{2}}\\)."),
    mk("Een geluid van \\(80\\) decibel is honderd keer zo intens als een geluid van hoeveel decibel, als \\(10\\) decibel erbij een factor \\(10\\) is?",
       ["\\(60\\) decibel", "\\(70\\) decibel", "\\(0{,}8\\) decibel", "\\(78\\) decibel"], 0, "Factor honderd is twee stappen van tien decibel."),
    sleep("In \\(2^{5} = 32\\) heet \\(2\\) het [[grondtal]] en \\(5\\) de [[exponent]]. De vraag « tot welke macht verhef ik \\(2\\) om \\(32\\) te krijgen? » beantwoord je met een [[logaritme]].",
          ["wortel", "kwadraat"], "Logaritme en macht zijn elkaars omgekeerde."),
]
