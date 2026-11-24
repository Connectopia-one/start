"""Pythagoras en de rechthoekige driehoek — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_lijn, s_tekst, pix_zone, DONKER, GROEN

DRIE = "pythagoras-driehoek-do"
A, B, C = (800, 520), (240, 170), (240, 520)


def _driehoek():
    d = [f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#eef5e6" stroke="{GROEN}" stroke-width="4"/>',
         f'<polyline points="{C[0]},{C[1]-34} {C[0]+34},{C[1]-34} {C[0]+34},{C[1]}" fill="none" stroke="{DONKER}" stroke-width="2"/>',
         f'<path d="M {A[0]-70},{A[1]} A 70 70 0 0 1 {A[0]-59.4},{A[1]-37.1}" fill="none" stroke="#7a4b8c" stroke-width="3"/>',
         s_tekst(A[0] - 100, A[1] - 14, "α", 26, kleur="#7a4b8c", vet=True),
         f'<path d="M {B[0]},{B[1]+70} A 70 70 0 0 0 {B[0]+59.4},{B[1]+37.1}" fill="none" stroke="#7a4b8c" stroke-width="3"/>',
         s_tekst(B[0] + 24, B[1] + 112, "β", 26, kleur="#7a4b8c", vet=True),
         s_tekst(A[0] + 24, A[1] + 10, "A", 28, vet=True),
         s_tekst(B[0] - 4, B[1] - 16, "B", 28, vet=True),
         s_tekst(C[0] - 28, C[1] + 10, "C", 28, vet=True)]
    return d


def _midzone(p, q):
    x, y = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    return pix_zone(x - 45, y - 45, 90, 90)


GRAFIEKEN = [dict(naam=DRIE, titel="Rechthoekige driehoek ABC met rechte hoek in C", eigen=_driehoek)]
PRENTEN = [dict(bestand=f"{DRIE}.svg", zelf=True, wat="rechthoekige driehoek ABC met hoeken α in A en β in B", vragen="klikvragen over schuine, overstaande en aanliggende zijde")]

VRAGEN = [
    klik(
        "Klik op de zijde die overstaand is ten opzichte van hoek α.",
        f"{DRIE}.svg",
        [_midzone(B, C)],
        "De overstaande zijde ligt tegenover de hoek en raakt hem niet: dat is BC.",
    ),
    klik(
        "Klik op de zijde die aanliggend is ten opzichte van hoek β.",
        f"{DRIE}.svg",
        [_midzone(B, C)],
        "BC raakt hoek β en is geen schuine zijde. Dezelfde zijde is dus overstaand voor α en aanliggend voor β.",
    ),
    klik(
        "Klik op de zijde die je in de noemer zet bij \\(\\sin\\beta\\).",
        f"{DRIE}.svg",
        [_midzone(A, B)],
        "Bij sinus en cosinus staat altijd de schuine zijde in de noemer: AB.",
    ),
    met_prent(f"{DRIE}.svg", tabel(
        "Kijk naar de driehoek. Welke breuk hoort erbij?",
        [(r"\(\sin\alpha\)", r"\(\tfrac{|BC|}{|AB|}\)"), (r"\(\cos\alpha\)", r"\(\tfrac{|AC|}{|AB|}\)"), (r"\(\tan\alpha\)", r"\(\tfrac{|BC|}{|AC|}\)"), (r"\(\tan\beta\)", r"\(\tfrac{|AC|}{|BC|}\)")],
        "Sinus: overstaande op schuine. Cosinus: aanliggende op schuine. Tangens: overstaande op aanliggende.",
        kolommen=[r"\(\tfrac{|BC|}{|AB|}\)", r"\(\tfrac{|AC|}{|AB|}\)", r"\(\tfrac{|BC|}{|AC|}\)", r"\(\tfrac{|AC|}{|BC|}\)"],
    )),
    met_prent(f"{DRIE}.svg", tabel(
        "Kijk naar de driehoek. Juist of fout?",
        [(r"\(\sin\alpha = \cos\beta\)", J), (r"\(|AB|^{2} = |AC|^{2} + |BC|^{2}\)", J), (r"\(\alpha + \beta = 180^\circ\)", F), (r"\(\tan\alpha \cdot \tan\beta = 1\)", J), (r"\(|BC| > |AB|\)", F)],
        r"α en β zijn complementair (samen \(90^\circ\)). Daardoor is \(\sin\alpha = \cos\beta\) en zijn de tangensen elkaars omgekeerde. De schuine zijde is de langste.",
        kolommen=["Juist", "Fout"],
    )),
    sorteer(
        "Zijn dit de zijden van een rechthoekige driehoek?",
        ["Rechthoekig", "Niet rechthoekig"],
        [(r"\(8\), \(15\), \(17\)", "Rechthoekig"), (r"\(7\), \(24\), \(25\)", "Rechthoekig"), (r"\(6\), \(7\), \(9\)", "Niet rechthoekig"),
         (r"\(1\), \(1\), \(\sqrt{2}\)", "Rechthoekig"), (r"\(2\), \(3\), \(4\)", "Niet rechthoekig"), (r"\(10\), \(24\), \(25\)", "Niet rechthoekig")],
        r"Controleer of de som van de kwadraten van de twee kleinste zijden gelijk is aan het kwadraat van de grootste. \(100 + 576 = 676 \neq 625\).",
    ),
    mk(
        "Een rechthoekig scherm is 48 cm breed en 36 cm hoog. Hoe lang is de diagonaal?",
        ["84 cm", "60 cm", "42 cm", "72 cm"],
        1,
        r"\(\sqrt{48^{2} + 36^{2}} = \sqrt{2304 + 1296} = \sqrt{3600} = 60\) cm.",
    ),
    inv(
        r"Bereken de afstand tussen \(P(-3, -1)\) en \(Q(3, 7)\).",
        ["10"],
        r"\(\sqrt{(3 - (-3))^{2} + (7 - (-1))^{2}} = \sqrt{36 + 64} = 10\).",
    ),
    mk(
        r"De afstand tussen \(A(1, 2)\) en \(B(x, 2)\) is \(5\). Welke waarden kan \(x\) hebben?",
        [r"enkel \(6\)", r"\(6\) of \(-4\)", r"\(5\) of \(-5\)", r"\(4\) of \(-6\)"],
        1,
        r"Beide punten liggen op dezelfde hoogte, dus \(|x - 1| = 5\): \(x = 6\) of \(x = -4\).",
    ),
    casus(
        "Een balk is 6 cm lang, 8 cm breed en 24 cm hoog.",
        [
            inv("Hoe lang is de diagonaal van het grondvlak, in cm?", ["10", "10 cm"], r"\(\sqrt{36 + 64} = 10\) cm."),
            inv("Hoe lang is de ruimtediagonaal, in cm?", ["26", "26 cm"], r"\(\sqrt{10^{2} + 24^{2}} = \sqrt{676} = 26\) cm."),
            mk("Past een stok van 25 cm schuin in de doos, met het deksel dicht?",
               ["ja, langs de ruimtediagonaal", "nee, want de hoogte is maar 24 cm", "nee, want het grondvlak is maar 10 cm", "dat kun je niet weten"], 0,
               "De ruimtediagonaal is 26 cm, de langste rechte lijn in de balk. Een stok van 25 cm past dus."),
        ],
    ),
    mk(
        "Een ladder van 6,5 m staat tegen een muur en reikt tot 6 m hoog. Hoe ver staat de voet van de muur?",
        ["0,5 m", "2,5 m", "8,8 m", "1,5 m"],
        1,
        r"\(\sqrt{6{,}5^{2} - 6^{2}} = \sqrt{42{,}25 - 36} = \sqrt{6{,}25} = 2{,}5\) m.",
    ),
    tabel(
        "Juist of fout over goniometrische getallen?",
        [
            (r"\(\sin 60^\circ = \cos 30^\circ\)", J),
            (r"\(\sin 45^\circ = \cos 45^\circ\)", J),
            (r"\(\tan 30^\circ > 1\)", F),
            (r"\(\sin 90^\circ = 0\)", F),
            (r"\(\cos 60^\circ = 0{,}5\)", J),
            (r"Als de hoek groter wordt, wordt de cosinus van een scherpe hoek groter.", F),
        ],
        r"Complementaire hoeken wisselen sinus en cosinus. \(\tan\alpha > 1\) pas vanaf \(45^\circ\). \(\sin 90^\circ = 1\). De cosinus daalt van \(1\) naar \(0\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"\(\cos\alpha = \tfrac{5}{13}\) en \(\alpha\) is scherp. Hoeveel is \(\tan\alpha\)?",
        [r"\(\tfrac{12}{13}\)", r"\(\tfrac{5}{12}\)", r"\(\tfrac{12}{5}\)", r"\(\tfrac{13}{12}\)"],
        2,
        r"Aanliggende \(5\), schuine \(13\), dus overstaande \(\sqrt{169 - 25} = 12\). \(\tan\alpha = \tfrac{12}{5}\).",
    ),
    inv(
        r"\(\sin\alpha = 0{,}28\) en \(\alpha\) is scherp. Bereken \(\cos\alpha\).",
        ["0,96", "0.96"],
        r"\(\cos^{2}\alpha = 1 - 0{,}0784 = 0{,}9216\), dus \(\cos\alpha = 0{,}96\).",
    ),
    casus(
        "Je staat 30 m van een toren. Je ogen zijn 1,6 m boven de grond. Je kijkt onder een hoek van 40° naar de top.",
        [
            mk("Welk goniometrisch getal gebruik je?", ["de sinus", "de cosinus", "de tangens", "de grondformule"], 2,
               "Je kent de aanliggende zijde (30 m) en zoekt de overstaande: tangens."),
            mk("Hoe hoog is de toren, afgerond op een decimeter?", ["25,2 m", "26,8 m", "21,0 m", "40,8 m"], 1,
               r"\(30 \cdot \tan 40^\circ \approx 25{,}2\) m boven je ogen, plus \(1{,}6\) m geeft \(26{,}8\) m."),
        ],
    ),
    mk(
        "Een weg stijgt over 400 m afstand langs de weg 28 m. Welke hoek maakt de weg met het horizontale vlak?",
        [r"ongeveer \(4^\circ\)", r"ongeveer \(7^\circ\)", r"ongeveer \(86^\circ\)", r"ongeveer \(14^\circ\)"],
        0,
        r"400 m is de schuine zijde en 28 m de overstaande. \(\sin\alpha = 0{,}07\) geeft \(\alpha \approx 4^\circ\).",
    ),
    koppel(
        "Wat ken je, en welk getal gebruik je om de gevraagde zijde te vinden?",
        [("hoek en schuine zijde, je zoekt de overstaande", "sinus"),
         ("hoek en aanliggende, je zoekt de schuine zijde", "cosinus"),
         ("hoek en aanliggende, je zoekt de overstaande", "tangens"),
         ("twee rechthoekszijden, je zoekt de schuine zijde", "Pythagoras")],
        ["sinusregel"],
        "Kies de verhouding waarin de gekende en de gezochte zijde allebei voorkomen.",
    ),
    keuze(
        "In een rechthoekige driehoek ligt de schuine zijde altijd [[*tegenover de rechte hoek|naast de kleinste hoek|onderaan]]. Ze is altijd de [[*langste|kortste]] zijde.",
        "De grootste hoek ligt tegenover de grootste zijde, en de rechte hoek is de grootste.",
    ),
    mk(
        "Een vierkant heeft een diagonaal van 10 cm. Hoe groot is de oppervlakte?",
        [r"\(100\) cm\(^{2}\)", r"\(50\) cm\(^{2}\)", r"\(25\) cm\(^{2}\)", r"\(70{,}7\) cm\(^{2}\)"],
        1,
        r"\(z^{2} + z^{2} = 100\), dus \(z^{2} = 50\). De oppervlakte is \(z^{2} = 50\) cm\(^{2}\).",
    ),
    inv(
        "Een gelijkzijdige driehoek heeft zijde 2. Hoe hoog is hij? Typ bijvoorbeeld 2√3.",
        ["√3", "wortel 3", "1√3"],
        r"De hoogte deelt de basis in twee stukken van \(1\). \(\sqrt{2^{2} - 1^{2}} = \sqrt{3}\).",
    ),
    volgorde(
        "Zet deze goniometrische getallen van klein naar groot.",
        [r"\(\sin 10^\circ\)", r"\(\cos 70^\circ\)", r"\(\sin 50^\circ\)", r"\(\cos 20^\circ\)", r"\(\tan 60^\circ\)"],
        r"\(\cos 70^\circ = \sin 20^\circ\) en \(\cos 20^\circ = \sin 70^\circ\). Een sinus stijgt met de hoek. \(\tan 60^\circ = \sqrt{3} \approx 1{,}73\) is groter dan \(1\).",
    ),
    sleep(
        r"Op de goniometrische cirkel met straal [[1]] is de x-coördinaat van een punt de [[cosinus]] en de y-coördinaat de [[sinus]] van de hoek. Daarom geldt \(\sin^{2}\alpha + \cos^{2}\alpha =\) [[1]].",
        ["tangens", "0", "2"],
        "Het punt ligt op afstand 1 van de oorsprong: Pythagoras geeft meteen de grondformule.",
    ),
    tabel(
        r"Twee hoeken: zijn ze complementair, supplementair of geen van beide?",
        [(r"\(35^\circ\) en \(55^\circ\)", "complementair"), (r"\(35^\circ\) en \(145^\circ\)", "supplementair"), (r"\(45^\circ\) en \(45^\circ\)", "complementair"), (r"\(60^\circ\) en \(60^\circ\)", "geen van beide"), (r"\(90^\circ\) en \(90^\circ\)", "supplementair")],
        r"Complementair: samen \(90^\circ\). Supplementair: samen \(180^\circ\).",
        kolommen=["complementair", "supplementair", "geen van beide"],
    ),
    mk(
        "Een vlieger hangt aan een touw van 50 m dat een hoek van 60° met de grond maakt. Hoe hoog hangt de vlieger boven je hand?",
        ["25 m", r"ongeveer \(43{,}3\) m", r"ongeveer \(86{,}6\) m", r"ongeveer \(28{,}9\) m"],
        1,
        r"\(50 \cdot \sin 60^\circ = 50 \cdot \tfrac{\sqrt{3}}{2} \approx 43{,}3\) m.",
    ),
    mk(
        r"Welk punt ligt even ver van de oorsprong als \(P(3, 4)\)?",
        [r"\((4, 4)\)", r"\((0, -5)\)", r"\((1, 6)\)", r"\((2, 3)\)"],
        1,
        r"\(|OP| = \sqrt{9 + 16} = 5\). Het punt \((0, -5)\) ligt ook op afstand \(5\).",
    ),
    tabel(
        r"Een rechthoekige driehoek heeft rechthoekszijden \(a\) en \(b\) en schuine zijde \(c\). Juist of fout?",
        [(r"\(c < a + b\)", J), (r"\(c^{2} = (a + b)^{2}\)", F), (r"\(c = a + b\) als \(a = b\)", F), (r"\(a = \sqrt{c^{2} - b^{2}}\)", J)],
        r"\((a + b)^{2} = a^{2} + 2ab + b^{2}\), dat is meer dan \(c^{2}\). Een omweg langs twee zijden is altijd langer dan de rechte weg.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"In driehoek ABC is de hoek in C recht, \(|AB| = 20\) en \(\alpha = 30^\circ\) in A. Hoe lang is \(|BC|\)?",
        ["10"],
        r"BC is overstaand voor α. \(|BC| = 20 \cdot \sin 30^\circ = 10\).",
    ),
]
