"""De reële getallen, wortels en machten — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_reele_getallen: soorten getallen, decimale vormen, procent,
wetenschappelijke notatie, wortels, machten met gehele exponenten en de
bewerkingseigenschappen. Met een zelfgetekend schema van de getallenverzamelingen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, ring_zones

VZ = "getallenverzamelingen"
R_ = (40, 60, 920, 560)
Q_ = (70, 100, 600, 500)
Z_ = (100, 150, 400, 420)
N_ = (130, 200, 190, 340)


def _schema():
    d = []
    for (x, y, b, h), naam, vul in [(R_, "ℝ", "#f3efe2"), (Q_, "ℚ", "#e6efdc"), (Z_, "ℤ", "#d6e6c7"), (N_, "ℕ", "#c3dbb0")]:
        d.append(s_vak(x, y, b, h, vul=vul, rand="#2f4a22", dikte=3, rond=18))
        d.append(s_tekst(x + 26, y + 36, naam, 30, vet=True))
    return d


GRAFIEKEN = [dict(naam=VZ, titel="De getallenverzamelingen", eigen=_schema)]
U = f"{VZ}.svg"
IRR = ring_zones(R_, Q_)
QZ = ring_zones(Q_, Z_)
ZN = ring_zones(Z_, N_)
NN = [[round(N_[0] / 10, 1), round(N_[1] / 6.4, 1), round(N_[2] / 10, 1), round(N_[3] / 6.4, 1)]]

VRAGEN = [
    klik(r"Klik in het kleinste gebied waar \(\sqrt{7}\) thuishoort.", U, IRR,
         r"\(\sqrt{7}\) is geen breuk: het hoort bij de reële getallen, buiten \(\mathbb{Q}\)."),
    klik(r"Klik in het kleinste gebied waar \(-4\) thuishoort.", U, ZN,
         r"\(-4\) is geheel, maar niet natuurlijk."),
    klik(r"Klik in het kleinste gebied waar \(0{,}125\) thuishoort.", U, QZ,
         r"\(0{,}125 = \frac{1}{8}\): een breuk, maar geen geheel getal."),
    klik(r"Klik in het kleinste gebied waar \(0{,}1010010001\ldots\) thuishoort: telkens komt er één nul bij.", U, IRR,
         "De cijfers stoppen nooit en er komt geen vast blok terug. Dus geen breuk."),
    klik(r"Klik in het kleinste gebied waar \(\sqrt{49}\) thuishoort.", U, NN,
         r"\(\sqrt{49} = 7\), een natuurlijk getal. Een wortel is dus niet altijd irrationaal."),
    sorteer("In welke kleinste verzameling hoort dit getal?", ["ℕ", "ℤ maar niet ℕ", "ℚ maar niet ℤ", "irrationaal"],
            [(r"\(\sqrt{25}\)", "ℕ"), (r"\(-\sqrt{9}\)", "ℤ maar niet ℕ"), (r"\(0{,}444\ldots\)", "ℚ maar niet ℤ"),
             (r"\(-\frac{3}{4}\)", "ℚ maar niet ℤ"), (r"\(\sqrt{12}\)", "irrationaal"), (r"\(\frac{\pi}{2}\)", "irrationaal")],
            r"Reken eerst uit wat kan: \(\sqrt{25} = 5\) en \(-\sqrt{9} = -3\). \(\sqrt{12}\) is geen volkomen kwadraat."),
    tabel("Juist of fout over de soorten getallen?",
          [(r"\(\sqrt{2} \cdot \sqrt{2}\) is rationaal.", J), (r"\(\frac{22}{7} = \pi\)", F), (r"\(-0{,}5 \in \mathbb{Z}\)", F), (r"\(\sqrt{0{,}25} \in \mathbb{Q}\)", J)],
          r"\(\sqrt{2} \cdot \sqrt{2} = 2\). \(\frac{22}{7}\) is maar een benadering van \(\pi\). \(\sqrt{0{,}25} = 0{,}5\).",
          kolommen=["Juist", "Fout"]),
    mk("Welke breuk heeft een begrensde decimale vorm?",
       [r"\(\frac{3}{8}\)", r"\(\frac{5}{12}\)", r"\(\frac{1}{30}\)", r"\(\frac{2}{3}\)"], 0,
       r"\(\frac{3}{8} = 0{,}375\). De andere geven \(0{,}41666\ldots\), \(0{,}0333\ldots\) en \(0{,}666\ldots\)."),
    inv(r"Schrijf \(0{,}000\,72\) in wetenschappelijke notatie. Vul de exponent in: \(7{,}2 \cdot 10^{?}\)", ["-4", "min 4", "min vier"],
        r"De komma schuift vier plaatsen naar rechts: \(0{,}000\,72 = 7{,}2 \cdot 10^{-4}\)."),
    mk(r"Wat is \(3{,}2 \cdot 10^{5} \cdot 2 \cdot 10^{-2}\)?",
       [r"\(6{,}4 \cdot 10^{3}\)", r"\(6{,}4 \cdot 10^{-10}\)", r"\(5{,}2 \cdot 10^{3}\)", r"\(6{,}4 \cdot 10^{7}\)"], 0,
       r"Vermenigvuldig de getallen: \(3{,}2 \cdot 2 = 6{,}4\). Tel de exponenten op: \(5 + (-2) = 3\)."),
    volgorde("Zet van klein naar groot.",
             [r"\(3 \cdot 10^{-4}\)", r"\(2{,}5 \cdot 10^{-3}\)", r"\(1{,}1 \cdot 10^{-2}\)", r"\(9 \cdot 10^{-2}\)"],
             r"Hoe negatiever de exponent, hoe kleiner het getal. Bij dezelfde exponent beslist het getal ervoor."),
    mk(r"Welke vorm is \(\sqrt{72}\) zo eenvoudig mogelijk geschreven?",
       [r"\(6\sqrt{2}\)", r"\(2\sqrt{6}\)", r"\(4\sqrt{3}\)", r"\(36\sqrt{2}\)"], 0,
       r"\(72 = 36 \cdot 2\) en \(\sqrt{36} = 6\). Zoek het grootste kwadraat dat in 72 past."),
    mk(r"Wat is \(\sqrt{18} + \sqrt{8}\)?",
       [r"\(5\sqrt{2}\)", r"\(\sqrt{26}\)", r"\(13\sqrt{2}\)", r"\(6\sqrt{2}\)"], 0,
       r"\(\sqrt{18} = 3\sqrt{2}\) en \(\sqrt{8} = 2\sqrt{2}\). Samen \(5\sqrt{2}\). Wortels optellen onder één wortel mag niet."),
    mk(r"Je maakt de noemer van \(\frac{6}{\sqrt{3}}\) wortelvrij. Wat krijg je?",
       [r"\(2\sqrt{3}\)", r"\(3\sqrt{2}\)", r"\(\frac{\sqrt{3}}{2}\)", r"\(6\sqrt{3}\)"], 0,
       r"\(\frac{6}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{6\sqrt{3}}{3} = 2\sqrt{3}\)."),
    mk(r"Wat is \(\frac{2^{-3} \cdot 2^{5}}{2^{4}}\) in decimale vorm?",
       [r"\(0{,}25\)", r"\(4\)", r"\(-4\)", r"\(\frac{1}{16}\)"], 0,
       r"Teller: \(2^{-3+5} = 2^{2}\). Delen: \(2^{2-4} = 2^{-2} = \frac{1}{4} = 0{,}25\)."),
    tabel("Juist of fout over de rekenregels van machten?",
          [(r"\((a^{2})^{3} = a^{6}\)", J), (r"\(a^{2} \cdot b^{2} = (ab)^{2}\)", J), (r"\(2^{3} + 2^{3} = 2^{6}\)", F), (r"\(5^{-1} = -5\)", F), (r"\((-1)^{100} = 1\)", J)],
          r"\(2^{3} + 2^{3} = 16 = 2^{4}\): bij een som tel je de exponenten niet op. \(5^{-1} = \frac{1}{5}\).",
          kolommen=["Juist", "Fout"]),
    inv(r"Wat is \(2^{-3}\) in decimale vorm?", ["0,125", "0.125"], r"\(2^{-3} = \frac{1}{2^{3}} = \frac{1}{8} = 0{,}125\)."),
    mk(r"Welke eigenschap gebruik je in \((4 \cdot 25) \cdot 7 = 4 \cdot (25 \cdot 7)\)?",
       ["de associativiteit", "de commutativiteit", "de distributiviteit", "de wortelregel"], 0,
       "De volgorde blijft, alleen de haakjes verschuiven. Dat is de schakeleigenschap."),
    koppel("Verbind elke handige berekening met de eigenschap die ze gebruikt.",
           [(r"\(25 \cdot 13 \cdot 4 = 25 \cdot 4 \cdot 13\)", "commutativiteit"),
            (r"\(7 \cdot 98 = 7 \cdot 100 - 7 \cdot 2\)", "distributiviteit"),
            (r"\((17 + 8) + 2 = 17 + (8 + 2)\)", "associativiteit")],
           ["wetenschappelijke notatie"],
           "Elk van de drie maakt het rekenwerk korter."),
    casus("Een vierkant tuintje heeft een oppervlakte van \\(50\\) m². Lien wil er een hekje rond zetten.", [
        mk("Hoe lang is één zijde, exact?", [r"\(5\sqrt{2}\) m", r"\(25\) m", r"\(10\sqrt{5}\) m", r"\(12{,}5\) m"], 0,
           r"\(\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}\)."),
        mk("Hoe lang is het hekje rondom, exact?", [r"\(20\sqrt{2}\) m", r"\(10\sqrt{2}\) m", r"\(200\) m", r"\(20\sqrt{50}\) m"], 0,
           r"Vier zijden: \(4 \cdot 5\sqrt{2} = 20\sqrt{2}\)."),
        inv("Hoeveel meter hekje is dat, afgerond op een centimeter? Een getal.", ["28,28", "28.28"],
            r"\(20\sqrt{2} \approx 28{,}284\), dus \(28{,}28\) m."),
        mk(r"Lien rondt eerst de zijde af op \(7\) m en rekent dan \(4 \cdot 7\). Wat loopt er mis?",
           ["ze komt meer dan een meter te kort", "er loopt niets mis, het is even juist", "ze heeft dan te veel hekje gekocht", "ze moest delen in plaats van maal"], 0,
           r"\(28\) m tegen \(28{,}28\) m. Afronden pas op het einde, anders groeit de fout mee."),
    ]),
    mk(r"Een prijs stijgt met \(20\,\%\) en daalt daarna met \(20\,\%\). Wat klopt?",
       [r"de eindprijs is \(4\,\%\) lager", "de prijs is weer even hoog", r"de eindprijs is \(4\,\%\) hoger", r"de eindprijs is \(40\,\%\) lager"], 0,
       r"\(1{,}2 \cdot 0{,}8 = 0{,}96\). De daling werkt op een groter bedrag dan de stijging."),
    sleep(r"\(\sqrt[3]{-8} =\) [[\(-2\)]], want \((-2)^{3} = -8\). Een vierkantswortel uit \(-8\) bestaat [[niet]] in \(\mathbb{R}\).",
          [r"\(2\)", "wel"], "Een kwadraat is nooit negatief, een derdemacht wel."),
    tabel("Welke decimale vorm heeft dit getal?",
          [(r"\(\frac{7}{8}\)", "begrensd"), (r"\(\frac{5}{11}\)", "onbegrensd repeterend"), (r"\(\sqrt{5}\)", "onbegrensd niet-repeterend"),
           (r"\(\frac{3}{25}\)", "begrensd"), (r"\(\frac{1}{6}\)", "onbegrensd repeterend")],
          r"\(\frac{7}{8} = 0{,}875\), \(\frac{5}{11} = 0{,}4545\ldots\), \(\frac{3}{25} = 0{,}12\), \(\frac{1}{6} = 0{,}1666\ldots\).",
          kolommen=["begrensd", "onbegrensd repeterend", "onbegrensd niet-repeterend"]),
    mk(r"Wat is \(\frac{\sqrt{75}}{\sqrt{3}}\)?", [r"\(5\)", r"\(25\)", r"\(\sqrt{72}\)", r"\(5\sqrt{3}\)"], 0,
       r"\(\frac{\sqrt{75}}{\sqrt{3}} = \sqrt{\frac{75}{3}} = \sqrt{25} = 5\)."),
    inv(r"Wat is \((-2)^{4} - 2^{4}\)? Een getal.", ["0", "nul"], r"\((-2)^{4} = 16\): een even exponent maakt het positief. \(16 - 16 = 0\)."),
    keuze(r"Bij \(-3^{2}\) werkt de macht [[*enkel op de 3|op de min en de 3 samen]], dus de uitkomst is \(-9\).",
          r"Zonder haakjes hoort het minteken niet bij het grondtal. Met haakjes: \((-3)^{2} = 9\)."),
    open_(r"Toon met een berekening dat \(\sqrt{9 + 16}\) niet gelijk is aan \(\sqrt{9} + \sqrt{16}\).",
          r"\(\sqrt{9 + 16} = \sqrt{25} = 5\), maar \(\sqrt{9} + \sqrt{16} = 3 + 4 = 7\). Een wortel van een som mag je dus niet splitsen."),
]
