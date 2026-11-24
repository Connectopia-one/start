"""Ordenen, afronden, intervallen en wetenschappelijke notatie — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import getallenas

AS = "ordenen-as-do"
_AS, _ZONES = getallenas(-3, 3, 0.5, [("P", -2.5), ("Q", -0.6), ("R", 0.45), ("S", 1.75), ("T", 2.25)], ijk=[-3, -2, -1, 0, 1, 2, 3])

GRAFIEKEN = [dict(naam=AS, titel="Vijf punten op de getallenas", eigen=lambda: _AS)]
PRENTEN = [dict(bestand=f"{AS}.svg", zelf=True, wat="getallenas van -3 tot 3 met vijf punten", vragen="klikvragen over ordenen en intervallen")]

VRAGEN = [
    klik(
        r"Klik op het punt dat in het interval \(\left]-1, 0\right[\) ligt.",
        f"{AS}.svg",
        [_ZONES["Q"]],
        r"Q ligt op \(-0{,}6\): groter dan \(-1\) en kleiner dan \(0\).",
    ),
    klik(
        r"Klik op het punt dat in \(\left[\tfrac{3}{2}, 2\right]\) ligt.",
        f"{AS}.svg",
        [_ZONES["S"]],
        r"\(\tfrac{3}{2} = 1{,}5\). S ligt op \(1{,}75\), tussen \(1{,}5\) en \(2\). T ligt al voorbij \(2\).",
    ),
    klik(
        r"Klik op het punt dat het dichtst bij \(\tfrac{1}{2}\) ligt.",
        f"{AS}.svg",
        [_ZONES["R"]],
        r"R ligt op \(0{,}45\), op \(0{,}05\) van \(\tfrac{1}{2}\).",
    ),
    met_prent(f"{AS}.svg", volgorde(
        "Zet de punten van klein naar groot.",
        ["P", "Q", "R", "S", "T"],
        "Op een getallenas ligt het kleinste getal het meest links.",
    )),
    met_prent(f"{AS}.svg", tabel(
        r"Ligt het punt in het interval \(\left]-\infty, 0{,}45\right]\)?",
        [("P", J), ("Q", J), ("R", J), ("S", F), ("T", F)],
        r"Het haakje bij \(0{,}45\) is gesloten, dus R hoort erbij. S en T liggen rechts van \(0{,}45\).",
        kolommen=["Juist", "Fout"],
    )),
    volgorde(
        "Zet van klein naar groot.",
        [r"\(-\tfrac{7}{4}\)", r"\(-1{,}7\)", r"\(-\sqrt{2}\)", r"\(\tfrac{2}{3}\)", r"\(0{,}67\)"],
        r"\(-1{,}75 < -1{,}7 < -1{,}41 < 0{,}666\ldots < 0{,}67\). Bij negatieve getallen is het getal met het grootste cijfer het kleinst.",
    ),
    tabel(
        "Juist of fout?",
        [
            (r"\(-0{,}3 < -0{,}29\)", J),
            (r"\(\tfrac{5}{8} > 0{,}63\)", F),
            (r"\(\sqrt{3} > 1{,}7\)", J),
            (r"\(-2{,}5 \geq -2{,}05\)", F),
            (r"\(33\% < \tfrac{1}{3}\)", J),
        ],
        r"\(\tfrac{5}{8} = 0{,}625\). \(-2{,}5\) ligt links van \(-2{,}05\). \(\tfrac{1}{3} = 33{,}33\ldots\%\).",
        kolommen=["Juist", "Fout"],
    ),
    koppel(
        "Verbind elke beschrijving met het interval.",
        [
            (r"\(x\) is minstens \(-2\) en kleiner dan \(5\)", r"\(\left[-2, 5\right[\)"),
            (r"\(x\) is groter dan \(-2\) en hoogstens \(5\)", r"\(\left]-2, 5\right]\)"),
            (r"\(x\) ligt strikt tussen \(-2\) en \(5\)", r"\(\left]-2, 5\right[\)"),
            (r"\(x\) is minstens \(5\)", r"\(\left[5, +\infty\right[\)"),
        ],
        [r"\(\left[-2, +\infty\right]\)"],
        r"'Minstens' en 'hoogstens' horen bij een gesloten haakje. Bij oneindig staat het haakje altijd open, dus \(\left[-2, +\infty\right]\) kan niet.",
    ),
    mk(
        r"Welk geheel getal hoort niet bij \(\left]-3, 2\right]\)?",
        [r"\(-2\)", r"\(-3\)", r"\(0\)", r"\(2\)"],
        1,
        r"Het haakje bij \(-3\) is open, dus \(-3\) hoort er niet bij. \(2\) wel, want daar staat een gesloten haakje.",
    ),
    inv(
        r"Hoeveel gehele getallen liggen in het interval \(\left[-4, 3\right[\)?",
        ["7", "zeven"],
        r"\(-4, -3, -2, -1, 0, 1, 2\): zeven getallen. \(3\) hoort er niet bij.",
    ),
    tabel(
        "Rond af op twee cijfers na de komma. Welke uitkomst klopt?",
        [
            (r"\(4{,}995\)", r"\(5{,}00\)"),
            (r"\(0{,}0749\)", r"\(0{,}07\)"),
            (r"\(12{,}345\)", r"\(12{,}35\)"),
            (r"\(7{,}0049\)", r"\(7{,}00\)"),
        ],
        r"Kijk enkel naar het derde cijfer na de komma. Bij \(4{,}995\) rond je naar boven en schuift alles door naar \(5{,}00\).",
        kolommen=[r"\(5{,}00\)", r"\(0{,}07\)", r"\(12{,}35\)", r"\(7{,}00\)"],
    ),
    mk(
        r"Een lengte wordt gemeten als \(3{,}6\) m, afgerond op een decimeter. Welke echte lengte is mogelijk?",
        [r"\(3{,}54\) m", r"\(3{,}66\) m", r"\(3{,}57\) m", r"\(3{,}65\) m"],
        2,
        r"De echte lengte ligt in \(\left[3{,}55\,;\,3{,}65\right[\). \(3{,}57\) past, \(3{,}65\) zou al \(3{,}7\) geven.",
    ),
    casus(
        r"Een leerling berekent de oppervlakte van een cirkel met straal \(2{,}35\) cm. Hij rondt eerst de straal af op \(2{,}4\) cm en rekent dan \(\pi \cdot 2{,}4^{2}\).",
        [
            mk("Hoeveel krijgt hij, afgerond op twee cijfers na de komma?",
               [r"\(17{,}35\) cm\(^{2}\)", r"\(18{,}10\) cm\(^{2}\)", r"\(15{,}08\) cm\(^{2}\)", r"\(7{,}54\) cm\(^{2}\)"], 1,
               r"\(\pi \cdot 5{,}76 \approx 18{,}10\) cm\(^{2}\)."),
            mk("Wat is de uitkomst als hij pas op het einde afrondt?",
               [r"\(17{,}35\) cm\(^{2}\)", r"\(18{,}10\) cm\(^{2}\)", r"\(17{,}97\) cm\(^{2}\)", r"\(14{,}77\) cm\(^{2}\)"], 0,
               r"\(\pi \cdot 2{,}35^{2} = \pi \cdot 5{,}5225 \approx 17{,}35\) cm\(^{2}\)."),
            mk("Wat leer je daaruit?",
               ["Afronden maakt nooit uit",
                "Wie te vroeg afrondt, krijgt een fout die tijdens de berekening groter wordt",
                "Je moet altijd naar boven afronden",
                "Je mag π vervangen door 3"], 1,
               r"Het verschil is bijna \(0{,}8\) cm\(^{2}\). Rond pas af op het einde."),
        ],
    ),
    sorteer(
        "Is dit een correcte wetenschappelijke notatie?",
        ["Correct", "Niet correct"],
        [
            (r"\(3{,}2 \cdot 10^{7}\)", "Correct"),
            (r"\(32 \cdot 10^{6}\)", "Niet correct"),
            (r"\(0{,}32 \cdot 10^{8}\)", "Niet correct"),
            (r"\(9{,}99 \cdot 10^{-3}\)", "Correct"),
            (r"\(1 \cdot 10^{0}\)", "Correct"),
        ],
        r"Voor de komma staat precies één cijfer van \(1\) tot \(9\). \(32\) en \(0{,}32\) voldoen daar niet aan, ook al stellen ze hetzelfde getal voor.",
    ),
    mk(
        r"Hoeveel is \((3 \cdot 10^{4}) \cdot (5 \cdot 10^{-7})\) in wetenschappelijke notatie?",
        [r"\(15 \cdot 10^{-3}\)", r"\(1{,}5 \cdot 10^{-2}\)", r"\(1{,}5 \cdot 10^{-3}\)", r"\(8 \cdot 10^{-3}\)"],
        1,
        r"\(3 \cdot 5 = 15\) en \(10^{4} \cdot 10^{-7} = 10^{-3}\). \(15 \cdot 10^{-3} = 1{,}5 \cdot 10^{-2}\).",
    ),
    mk(
        r"Hoeveel is \(\dfrac{8 \cdot 10^{9}}{2 \cdot 10^{3}}\)?",
        [r"\(4 \cdot 10^{3}\)", r"\(4 \cdot 10^{6}\)", r"\(6 \cdot 10^{6}\)", r"\(4 \cdot 10^{12}\)"],
        1,
        r"\(8 : 2 = 4\) en \(10^{9 - 3} = 10^{6}\).",
    ),
    inv(
        r"Een bacterie is \(0{,}000\,002\) m lang. Schrijf dat in wetenschappelijke notatie. Typ bijvoorbeeld 3 x 10^-4.",
        ["2 x 10^-6", "2x10^-6", "2 · 10^-6", "2*10^-6", "2 x 10^(-6)"],
        r"De komma schuift zes plaatsen naar rechts: \(2 \cdot 10^{-6}\) m.",
    ),
    volgorde(
        "Zet deze getallen in wetenschappelijke notatie van klein naar groot.",
        [r"\(9 \cdot 10^{-5}\)", r"\(1{,}2 \cdot 10^{-4}\)", r"\(3 \cdot 10^{-4}\)", r"\(2 \cdot 10^{2}\)", r"\(7{,}5 \cdot 10^{2}\)"],
        r"Vergelijk eerst de exponenten: hoe kleiner, hoe kleiner het getal. Bij dezelfde exponent beslist het getal ervoor.",
    ),
    tabel(
        "Juist of fout over intervallen?",
        [
            (r"\(\left[2, 2\right]\) bevat precies één getal.", J),
            (r"\(\left]2, 2\right[\) bevat het getal \(2\).", F),
            (r"\(\left]0, 1\right[\) bevat oneindig veel getallen.", J),
            (r"\(\left]-\infty, 0\right]\) bevat alle negatieve getallen en \(0\).", J),
            (r"\(\left]1, 3\right]\) is een gesloten interval.", F),
        ],
        r"\(\left]2, 2\right[\) is leeg. \(\left]1, 3\right]\) is halfopen: aan één kant open, aan de andere gesloten.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"Bij 'alle getallen kleiner dan \(4\)' hoort het interval [[*\(\left]-\infty, 4\right[\)|\(\left]-\infty, 4\right]\)]]. Het haakje bij oneindig staat altijd [[*open|gesloten]].",
        "Kleiner dan, niet gelijk aan: het haakje bij 4 is open. Oneindig is geen getal, dus daar staat het haakje altijd open.",
    ),
    mk(
        "Een stad heeft 287 456 inwoners. Hoeveel is dat afgerond op duizendtallen?",
        ["287 000", "288 000", "290 000", "287 500"],
        0,
        "Het honderdtal is een 4, dus je rondt naar beneden af.",
    ),
    inv(
        r"Schat \(\dfrac{612}{29}\) door af te ronden op tientallen. Welke schatting krijg je?",
        ["20", "ongeveer 20"],
        r"\(600 : 30 = 20\). De exacte uitkomst is ongeveer \(21{,}1\).",
    ),
    sleep(
        r"Het interval \(\left]-1, 4\right]\) is [[halfopen]]: \(-1\) hoort er [[niet]] bij en \(4\) hoort er [[wel]] bij.",
        ["gesloten", "altijd"],
        "Een rond haakje dat van het getal wegwijst, sluit het getal uit.",
    ),
    mk(
        r"De massa van een stofdeeltje is \(4{,}2 \cdot 10^{-9}\) kg. Hoeveel gram is dat?",
        [r"\(4{,}2 \cdot 10^{-12}\) g", r"\(4{,}2 \cdot 10^{-6}\) g", r"\(4{,}2 \cdot 10^{-3}\) g", r"\(4{,}2 \cdot 10^{-9}\) g"],
        1,
        r"\(1\) kg is \(10^{3}\) g. \(4{,}2 \cdot 10^{-9} \cdot 10^{3} = 4{,}2 \cdot 10^{-6}\) g.",
    ),
    inv(
        r"Welk is het grootste geheel getal in \(\left]-5, \sqrt{10}\right[\)?",
        ["3", "drie"],
        r"\(\sqrt{10} \approx 3{,}16\). Het grootste gehele getal kleiner dan dat is \(3\).",
    ),
    mk(
        r"Welk getal ligt tussen \(\tfrac{3}{7}\) en \(\tfrac{1}{2}\)?",
        [r"\(0{,}41\)", r"\(0{,}45\)", r"\(0{,}52\)", r"\(0{,}42\)"],
        1,
        r"\(\tfrac{3}{7} \approx 0{,}429\) en \(\tfrac{1}{2} = 0{,}5\). Enkel \(0{,}45\) ligt daartussen.",
    ),
    tabel(
        r"Een getal \(x\) is afgerond op een geheel getal gelijk aan \(8\). Kan \(x\) gelijk zijn aan dit getal?",
        [(r"\(7{,}5\)", J), (r"\(8{,}49\)", J), (r"\(8{,}5\)", F), (r"\(7{,}49\)", F)],
        r"Alle getallen in \(\left[7{,}5\,;\,8{,}5\right[\) worden \(8\). \(8{,}5\) rond je af naar \(9\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"De afstand aarde-zon is ongeveer \(1{,}5 \cdot 10^{8}\) km. Licht legt \(3 \cdot 10^{5}\) km per seconde af. Hoelang doet het licht erover?",
        [r"\(5 \cdot 10^{2}\) s", r"\(4{,}5 \cdot 10^{13}\) s", r"\(2 \cdot 10^{-3}\) s", r"\(5 \cdot 10^{3}\) s"],
        0,
        r"\(\dfrac{1{,}5 \cdot 10^{8}}{3 \cdot 10^{5}} = 0{,}5 \cdot 10^{3} = 5 \cdot 10^{2}\) s, iets meer dan acht minuten.",
    ),
]
