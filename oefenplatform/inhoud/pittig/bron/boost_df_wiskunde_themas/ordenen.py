"""Ordenen, afronden en intervallen — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import getallenas

AS = "ordenen-getallenas"
_AS, _Z = getallenas(-3, 3, 0.5, [("P", -2.5), ("Q", -1), ("R", 0.25), ("S", 2), ("T", 2.75)], ijk=[-3, -2, -1, 0, 1, 2, 3])

GRAFIEKEN = [dict(naam=AS, titel="Vijf punten op de getallenas", eigen=lambda: _AS)]
PRENTEN = [dict(bestand=f"{AS}.svg", zelf=True, wat="getallenas met vijf punten", vragen="klikvragen over intervallen")]

VRAGEN = [
    klik(
        r"Klik op een punt dat in het interval \(\left]-1, 2\right]\) ligt.",
        f"{AS}.svg",
        [_Z["R"], _Z["S"]],
        r"R ligt op \(0{,}25\) en S op \(2\): de rechtergrens hoort erbij. Q ligt op \(-1\), en die grens hoort er net niet bij.",
    ),
    klik(
        r"Klik op het punt dat in \(\left]-\infty, -2\right[\) ligt.",
        f"{AS}.svg",
        [_Z["P"]],
        r"Enkel P, op \(-2{,}5\), ligt links van \(-2\).",
    ),
    met_prent(f"{AS}.svg", tabel(
        "Ligt het punt in het interval?",
        [
            (r"Q in \(\left[-1, 0\right]\)", J),
            (r"S in \(\left[0, 2\right[\)", F),
            (r"T in \(\left]2, +\infty\right[\)", J),
            (r"R in \(\left]-3, 0\right]\)", F),
        ],
        r"Q ligt op \(-1\), een gesloten grens. S ligt op \(2\), en daar staat het haakje naar buiten. T ligt op \(2{,}75\). R ligt op \(0{,}25\), net rechts van \(0\).",
    )),
    koppel(
        "Koppel elke beschrijving aan het juiste interval.",
        [
            [r"\(x\) is minstens \(-2\) en kleiner dan \(5\)", r"\(\left[-2, 5\right[\)"],
            [r"\(x\) is groter dan \(-2\) en hoogstens \(5\)", r"\(\left]-2, 5\right]\)"],
            [r"\(x\) ligt van \(-2\) tot en met \(5\)", r"\(\left[-2, 5\right]\)"],
            [r"\(x\) is hoogstens \(5\)", r"\(\left]-\infty, 5\right]\)"],
        ],
        [r"\(\left[5, +\infty\right[\)", r"\(\left]-2, 5\right[\)"],
        "Minstens en hoogstens betekenen dat de grens meetelt: een haakje naar binnen. Groter dan en kleiner dan sluiten de grens uit.",
    ),
    mk(
        r"Welke getallen behoren tot zowel \(\left[-1, 4\right[\) als \(\left]2, 6\right]\)?",
        [r"\(\left]2, 4\right[\)", r"\(\left[-1, 6\right]\)", r"\(\left[2, 4\right]\)", r"\(\left]-1, 6\right[\)"],
        0,
        r"Getallen die in allebei liggen: groter dan \(2\) en kleiner dan \(4\). Beide grenzen vallen weg, want \(2\) hoort niet bij het tweede en \(4\) niet bij het eerste interval.",
    ),
    inv(
        r"Hoeveel gehele getallen liggen in het interval \(\left]-3, 4\right]\)?",
        ["7", "zeven"],
        r"\(-2, -1, 0, 1, 2, 3, 4\): de \(-3\) hoort er niet bij, de \(4\) wel.",
    ),
    volgorde(
        "Zet deze getallen van klein naar groot.",
        [r"\(-\tfrac{3}{4}\)", r"\(-0{,}7\)", r"\(-65\%\)", r"\(0{,}07\)", r"\(\tfrac{1}{8}\)"],
        r"\(-0{,}75 < -0{,}7 < -0{,}65 < 0{,}07 < 0{,}125\). Bij negatieve getallen is het getal met de grootste absolute waarde het kleinst.",
    ),
    mk(
        r"Welk getal ligt tussen \(\tfrac{2}{3}\) en \(\tfrac{3}{4}\)?",
        [r"\(\tfrac{5}{7}\)", r"\(0{,}76\)", r"\(\tfrac{5}{8}\)", r"\(0{,}66\)"],
        0,
        r"\(\tfrac{2}{3} \approx 0{,}667\) en \(\tfrac{3}{4} = 0{,}75\). \(\tfrac{5}{7} \approx 0{,}714\) ligt ertussen; \(\tfrac{5}{8} = 0{,}625\) is te klein.",
    ),
    tabel(
        "Juist of fout over afronden?",
        [
            (r"\(2{,}695\) afgerond op twee decimalen is \(2{,}70\).", J),
            (r"\(14{,}49\) afgerond op een geheel getal is \(15\), want je rondt eerst \(14{,}49\) af op \(14{,}5\).", F),
            (r"\(0{,}0396\) afgerond op drie decimalen is \(0{,}040\).", J),
            (r"\(1999{,}6\) afgerond op een geheel getal is \(2000\).", J),
        ],
        r"Je kijkt enkel naar het eerste cijfer dat wegvalt. Bij \(14{,}49\) is dat een \(4\): \(14\). Stapsgewijs afronden geeft een fout resultaat.",
    ),
    casus(
        r"Een weegschaal toont gewichten afgerond op \(0{,}1\) kg. Ze toont \(3{,}4\) kg.",
        [
            mk(
                "In welk interval ligt het echte gewicht?",
                [r"\(\left[3{,}35;\ 3{,}45\right[\)", r"\(\left[3{,}3;\ 3{,}5\right]\)", r"\(\left[3{,}4;\ 3{,}5\right[\)", r"\(\left]3{,}35;\ 3{,}45\right]\)"],
                0,
                r"Alles van \(3{,}35\) tot net onder \(3{,}45\) wordt \(3{,}4\). \(3{,}45\) zelf wordt al \(3{,}5\).",
            ),
            inv(
                "Je legt drie zulke pakken op de weegschaal, die elk 3,4 kg tonen. Hoeveel kg kan het samen hoogstens wegen, net niet meegerekend? Typ een kommagetal.",
                ["10,35", "10.35"],
                r"Elk pak weegt minder dan \(3{,}45\) kg, samen dus minder dan \(10{,}35\) kg.",
            ),
        ],
    ),
    koppel(
        "Koppel elk getal aan zijn wetenschappelijke notatie.",
        [
            [r"\(45\,000\)", r"\(4{,}5 \cdot 10^{4}\)"],
            [r"\(0{,}00045\)", r"\(4{,}5 \cdot 10^{-4}\)"],
            [r"\(450\)", r"\(4{,}5 \cdot 10^{2}\)"],
            [r"\(0{,}045\)", r"\(4{,}5 \cdot 10^{-2}\)"],
        ],
        [r"\(45 \cdot 10^{3}\)", r"\(4{,}5 \cdot 10^{-3}\)"],
        r"Voor de komma staat één cijfer van \(1\) tot \(9\). \(45 \cdot 10^{3}\) heeft de goede waarde, maar is geen wetenschappelijke notatie.",
    ),
    mk(
        r"Hoeveel is \(\left(3 \cdot 10^{5}\right) \cdot \left(4 \cdot 10^{-2}\right)\) in wetenschappelijke notatie?",
        [r"\(12 \cdot 10^{3}\)", r"\(1{,}2 \cdot 10^{4}\)", r"\(1{,}2 \cdot 10^{3}\)", r"\(7 \cdot 10^{3}\)"],
        1,
        r"\(3 \cdot 4 = 12\) en \(10^{5} \cdot 10^{-2} = 10^{3}\). \(12 \cdot 10^{3}\) heeft twee cijfers voor de komma, dus \(1{,}2 \cdot 10^{4}\).",
    ),
    inv(
        r"Een bacterie is \(2 \cdot 10^{-6}\) m lang. Hoeveel bacteriën passen er achter elkaar op \(1\) cm? Typ het als gewoon getal.",
        ["5000", "5 000"],
        r"\(1\) cm \(= 10^{-2}\) m. \(\dfrac{10^{-2}}{2 \cdot 10^{-6}} = 0{,}5 \cdot 10^{4} = 5000\).",
    ),
    sorteer(
        "Is dit een geldige wetenschappelijke notatie?",
        ["Ja", "Nee"],
        [
            [r"\(7{,}02 \cdot 10^{-8}\)", "Ja"],
            [r"\(0{,}5 \cdot 10^{3}\)", "Nee"],
            [r"\(10 \cdot 10^{4}\)", "Nee"],
            [r"\(1 \cdot 10^{0}\)", "Ja"],
            [r"\(9{,}99 \cdot 10^{12}\)", "Ja"],
        ],
        r"Het getal voor de macht moet minstens \(1\) en kleiner dan \(10\) zijn. \(0{,}5\) is te klein, \(10\) is te groot.",
    ),
    mk(
        r"Welke schatting ligt het dichtst bij \(\dfrac{612 \cdot 0{,}49}{2{,}97}\)?",
        [r"\(10\)", r"\(100\)", r"\(1000\)", r"\(50\)"],
        1,
        r"Ongeveer \(\dfrac{600 \cdot 0{,}5}{3} = \dfrac{300}{3} = 100\).",
    ),
    keuze(
        r"\(-5\) is [[*kleiner dan|groter dan]] \(-2\), want \(-5\) ligt op de getallenas [[*links van|rechts van]] \(-2\). Van twee negatieve getallen is het getal met de grootste absolute waarde het [[*kleinst|grootst]].",
        r"Op de getallenas ligt een kleiner getal links. \(|-5| = 5 > 2\), maar \(-5 < -2\).",
    ),
    tabel(
        "Juist of fout over intervallen?",
        [
            (r"\(\left]3, 3\right[\) bevat geen enkel getal.", J),
            (r"\(\left[-\infty, 2\right]\) is een correcte notatie.", F),
            (r"Tussen \(0{,}1\) en \(0{,}11\) liggen oneindig veel reële getallen.", J),
            (r"\(\left]1, 2\right[\) bevat het kleinste getal groter dan \(1\).", F),
        ],
        r"Bij oneindig staat het haakje altijd naar buiten. Er is geen kleinste getal groter dan \(1\): tussen \(1\) en elk getal erboven ligt er nog een.",
    ),
    mk(
        r"Welke ongelijkheid hoort bij het interval \(\left[-4, 1\right[\)?",
        [r"\(-4 < x \leq 1\)", r"\(-4 \leq x < 1\)", r"\(-4 \leq x \leq 1\)", r"\(x \geq -4\) of \(x < 1\)"],
        1,
        r"Het haakje naar binnen bij \(-4\) betekent \(\leq\), het haakje naar buiten bij \(1\) betekent \(<\). En het is 'en', niet 'of'.",
    ),
    inv(
        r"De afstand aarde-maan is ongeveer \(384\,400\) km. Schrijf in wetenschappelijke notatie, afgerond op twee decimalen. Typ bijvoorbeeld 2,51·10^7.",
        ["3,84·10^5", "3,84*10^5", "3,84 · 10^5", "3,84x10^5", "3,84 x 10^5", "3,84.10^5", "3.84·10^5"],
        r"\(384\,400 = 3{,}844 \cdot 10^{5} \approx 3{,}84 \cdot 10^{5}\) km.",
    ),
    mk(
        r"Waarom rond je pas op het einde af? Je berekent \(3 \cdot 1{,}26 \cdot 4\).",
        [
            r"tussendoor afronden op één decimaal geeft \(3 \cdot 1{,}3 \cdot 4 = 15{,}6\) in plaats van \(15{,}12\)",
            "de volgorde van vermenigvuldigen verandert de uitkomst",
            "anders mag je geen rekentoestel gebruiken",
            "op het einde afronden geeft altijd een geheel getal",
        ],
        0,
        r"Een kleine afronding wordt mee vermenigvuldigd: \(0{,}04 \cdot 12 = 0{,}48\) verschil.",
    ),
    mk(
        r"Hoeveel procent is \(\tfrac{5}{16}\)?",
        [r"\(31{,}25\%\)", r"\(3{,}2\%\)", r"\(51{,}6\%\)", r"\(32\%\)"],
        0,
        r"\(5 : 16 = 0{,}3125\), dus \(31{,}25\) honderdsten.",
    ),
    sleep(
        r"Het interval \(\left[2, 7\right]\) noem je [[gesloten]], het interval \(\left]2, 7\right[\) noem je [[open]] en \(\left[2, 7\right[\) noem je [[halfopen]].",
        ["oneindig", "leeg"],
        "Gesloten: beide grenzen horen erbij. Open: geen enkele. Halfopen: één van de twee.",
    ),
    inv(
        r"Rond \(\sqrt{50}\) af op twee decimalen.",
        ["7,07", "7.07"],
        r"\(\sqrt{50} = 7{,}0710\ldots\): de derde decimaal is \(1\), dus naar beneden.",
    ),
    mk(
        r"Een atoom heeft een diameter van \(1{,}2 \cdot 10^{-10}\) m en een kern van \(2{,}4 \cdot 10^{-15}\) m. Hoeveel keer is het atoom groter dan de kern?",
        [r"\(5 \cdot 10^{4}\)", r"\(2 \cdot 10^{-5}\)", r"\(0{,}5 \cdot 10^{-5}\)", r"\(2 \cdot 10^{5}\)"],
        0,
        r"\(\dfrac{1{,}2}{2{,}4} = 0{,}5\) en \(\dfrac{10^{-10}}{10^{-15}} = 10^{5}\): \(0{,}5 \cdot 10^{5} = 5 \cdot 10^{4}\).",
    ),
    casus(
        r"De ideale temperatuur in een koelkast ligt tussen \(2\) en \(5\) graden, grenzen inbegrepen. Een thermometer meet om het uur.",
        [
            mk(
                "Welk interval hoort bij de ideale temperatuur?",
                [r"\(\left]2, 5\right[\)", r"\(\left[2, 5\right]\)", r"\(\left[2, 5\right[\)", r"\(\left]2, 5\right]\)"],
                1,
                "Grenzen inbegrepen: aan beide kanten een haakje naar binnen.",
            ),
            sorteer(
                "Zit de meting in het ideale interval?",
                ["Ja", "Nee"],
                [
                    [r"\(2\) °C", "Ja"],
                    [r"\(5{,}1\) °C", "Nee"],
                    [r"\(1{,}9\) °C", "Nee"],
                    [r"\(4{,}99\) °C", "Ja"],
                ],
                r"\(2\) en \(4{,}99\) liggen van \(2\) tot en met \(5\). \(5{,}1\) en \(1{,}9\) vallen erbuiten.",
            ),
        ],
    ),
    open_(
        r"Leg uit waarom \(\left]4, 1\right]\) geen correcte intervalnotatie is, en schrijf hoe het wel moet als je de getallen groter dan \(1\) en hoogstens \(4\) bedoelt.",
        r"In een interval staat de kleinste grens altijd links. Hier staat \(4\) links van \(1\). Bedoel je de getallen groter dan \(1\) en hoogstens \(4\), dan schrijf je \(\left]1, 4\right]\).",
    ),
    inv(
        r"Hoeveel is \(6 \cdot 10^{-3}\) gedeeld door \(3 \cdot 10^{2}\)? Typ het als gewoon kommagetal.",
        ["0,00002", "0.00002"],
        r"\(\dfrac{6}{3} = 2\) en \(\dfrac{10^{-3}}{10^{2}} = 10^{-5}\): \(2 \cdot 10^{-5} = 0{,}00002\).",
    ),
    mk(
        r"Een getal wordt afgerond op een tiental en geeft \(370\). Welk getal kan het niet geweest zijn?",
        [r"\(365\)", r"\(374{,}9\)", r"\(375\)", r"\(368{,}2\)"],
        2,
        r"Alles van \(365\) tot net onder \(375\) wordt \(370\). \(375\) zelf wordt al \(380\).",
    ),
]
