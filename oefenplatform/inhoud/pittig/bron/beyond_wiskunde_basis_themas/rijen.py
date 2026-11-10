"""Rekenkundige en meetkundige rijen — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

R_GRAF = venster("rijen-drie-rijen", 0, 8.6, 0, 36, 1, 2)


def _u(n):
    return 3 * n + 8


def _v(n):
    return 2 * 1.5 ** (n - 1)


def _w(n):
    return 32 * 0.5 ** (n - 1)


N = range(1, 9)
GRAFIEKEN = [
    dict(naam=R_GRAF, titel="De eerste acht termen van de rijen u, v en w",
         reeksen=[
             ([(n, _u(n)) for n in N], "groen", "u"),
             ([(n, _v(n)) for n in N if _v(n) <= 36], "oranje", "v"),
             ([(n, _w(n)) for n in N], "blauw", "w"),
         ],
         labelplek={"v": (7, _v(7)), "w": (1, 32)},
         xlabel="n", ylabel="", ijk_x=1, ijk_y=4),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over rijen") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Klik op de eerste term van de rij v die groter is dan 20.",
        f"{R_GRAF}.svg",
        [punt_zone(R_GRAF, 7, _v(7), 26)],
        r"\(v_6 \approx 15{,}2\) en \(v_7 \approx 22{,}8\). De zevende term is de eerste boven 20.",
    ),
    klik(
        "Klik op de zesde term van de rij u.",
        f"{R_GRAF}.svg",
        [punt_zone(R_GRAF, 6, _u(6), 26)],
        r"Tel op de horizontale as tot \(n = 6\): \(u_6 = 26\).",
    ),
    met_prent(f"{R_GRAF}.svg", mk(
        "Welke rij heeft een toenemende stijging?",
        ["u", "w", "v", "Geen van de drie"],
        2,
        "De sprongen tussen de punten van v worden telkens groter. Bij u zijn ze altijd even groot, w daalt.",
    )),
    met_prent(f"{R_GRAF}.svg", tabel(
        "Lees af en vul aan.",
        [
            ("De reden q van v", "1,5"),
            ("De reden q van w", "0,5"),
            ("De eerste term van w", "32"),
        ],
        r"v: \(2, 3, 4{,}5, \dots\), telkens maal \(1{,}5\). w: \(32, 16, 8, \dots\), telkens gedeeld door 2.",
        kolommen=["32", "1,5", "0,5", "2"],
    )),
    met_prent(f"{R_GRAF}.svg", mk(
        "Welk expliciet voorschrift heeft de rij u?",
        [r"\(u_n = 11 + 3n\)", r"\(u_n = 8n + 3\)", r"\(u_n = 11 \cdot 3^{n-1}\)", r"\(u_n = 3n + 8\)"],
        3,
        r"\(u_1 = 11\) en het verschil is 3: \(u_n = 11 + (n - 1) \cdot 3 = 3n + 8\).",
    )),
    mk(
        r"Een rij heeft \(u_1 = 4\) en \(u_{n+1} = u_n - 3\). Wat is \(u_5\)?",
        [r"\(-11\)", r"\(-8\)", r"\(-5\)", r"\(16\)"],
        1,
        r"\(4, 1, -2, -5, -8\).",
    ),
    inv(
        r"Een meetkundige rij heeft \(v_1 = 3\) en reden \(q = 2\). Wat is \(v_6\)?",
        "96",
        r"\(v_6 = 3 \cdot 2^5 = 96\).",
    ),
    mk(
        "Welk voorschrift hoort bij een rekenkundige rij?",
        [r"\(u_n = 7 \cdot 4^n\)", r"\(u_n = n^2 + 1\)", r"\(u_n = 7 - 4n\)", r"\(u_n = \dfrac{4}{n}\)"],
        2,
        r"Een rekenkundige rij heeft een voorschrift van de eerste graad in n: elke stap komt er hetzelfde getal bij (hier \(-4\)).",
    ),
    tabel(
        "Juist of fout over rijen?",
        [
            (r"Een rekenkundige rij met verschil \(v > 0\) is stijgend.", J),
            ("Bij een rekenkundige rij liggen de punten van de grafiek op een parabool.", F),
            (r"De rij \(10, 7, 4, 1, \dots\) is rekenkundig.", J),
            (r"Een meetkundige rij met reden \(q = 1{,}1\) en positieve termen is dalend.", F),
        ],
        r"Een constant verschil geeft punten op een rechte. Vermenigvuldigen met \(1{,}1\) maakt positieve termen groter.",
    ),
    keuze(
        "Een rekenkundige rij hoort bij [[*lineaire|exponentiële|kwadratische]] groei. Een meetkundige rij met positieve reden hoort bij [[*exponentiële|lineaire|kwadratische]] groei.",
        "Telkens hetzelfde erbij: lineair. Telkens met hetzelfde getal vermenigvuldigen: exponentieel.",
    ),
    mk(
        r"Wat is de som van de eerste 10 termen van \(7, 11, 15, \dots\)?",
        [r"\(430\)", r"\(215\)", r"\(500\)", r"\(250\)"],
        3,
        r"\(u_{10} = 7 + 9 \cdot 4 = 43\). \(s_{10} = \frac{10}{2}(7 + 43) = 250\).",
    ),
    inv(
        r"Wat is de som van de eerste 8 termen van \(3, 6, 12, \dots\)?",
        "765",
        r"\(s_8 = 3 \cdot \frac{2^8 - 1}{2 - 1} = 3 \cdot 255 = 765\).",
    ),
    mk(
        "Je zet 2000 euro op een rekening met 3 % enkelvoudige intrest per jaar. Hoeveel staat er na 5 jaar?",
        [r"\(2318{,}55\) euro", r"\(2300\) euro", r"\(2030\) euro", r"\(2600\) euro"],
        1,
        r"Enkelvoudig: elk jaar \(3\) % van \(2000\), dus \(60\) euro. \(2000 + 5 \cdot 60 = 2300\).",
    ),
    mk(
        "Welk voorschrift geeft het kapitaal na n jaar bij 1000 euro aan 2 % samengestelde intrest per jaar?",
        [r"\(K_n = 1000 + 20n\)", r"\(K_n = 1000 \cdot 0{,}02^n\)", r"\(K_n = 1000 \cdot 1{,}02^n\)", r"\(K_n = 1000 \cdot 2^n\)"],
        2,
        r"Elk jaar komt er \(2\) % bij: het kapitaal wordt maal \(1{,}02\). Dat is een meetkundige rij met reden \(1{,}02\).",
    ),
    sorteer(
        "Rekenkundig of meetkundig?",
        ["Rekenkundig", "Meetkundig"],
        [
            [r"\(5, 10, 20, 40, \dots\)", "Meetkundig"],
            [r"\(5, 10, 15, 20, \dots\)", "Rekenkundig"],
            [r"\(u_{n+1} = u_n + 0{,}5\)", "Rekenkundig"],
            [r"\(u_{n+1} = 0{,}5 \cdot u_n\)", "Meetkundig"],
            ["Een plant groeit elke week 2 cm", "Rekenkundig"],
            ["Een bedrag groeit elk jaar met 4 %", "Meetkundig"],
        ],
        "Er telkens hetzelfde bij doen: rekenkundig. Telkens met hetzelfde getal vermenigvuldigen: meetkundig.",
    ),
    volgorde(
        "Zet deze termen van groot naar klein.",
        [
            r"\(v_5\) van \(v_n = 3 \cdot 2^{n-1}\)",
            r"de vierde term van \(6, 13, 20, \dots\)",
            r"\(u_{10}\) van \(u_n = 50 - 4n\)",
            r"\(w_3\) van de meetkundige rij met \(w_1 = 100\) en \(q = 0{,}1\)",
        ],
        r"\(v_5 = 48\), de vierde term is \(27\), \(u_{10} = 10\) en \(w_3 = 1\).",
    ),
    koppel(
        "Koppel de rij aan haar recursief voorschrift.",
        [
            [r"\(2, 6, 18, 54, \dots\)", r"\(u_1 = 2,\ u_{n+1} = 3u_n\)"],
            [r"\(2, 5, 8, 11, \dots\)", r"\(u_1 = 2,\ u_{n+1} = u_n + 3\)"],
            [r"\(2, -6, 18, -54, \dots\)", r"\(u_1 = 2,\ u_{n+1} = -3u_n\)"],
            [r"\(2, -1, -4, -7, \dots\)", r"\(u_1 = 2,\ u_{n+1} = u_n - 3\)"],
        ],
        [r"\(u_1 = 3,\ u_{n+1} = 2u_n\)"],
        "Kijk of je van de ene term naar de volgende optelt of vermenigvuldigt, en met welk teken.",
    ),
    sleep(
        "Bij een rekenkundige rij is het [[verschil]] van twee opeenvolgende termen constant, bij een meetkundige rij het [[quotiënt]]. De grafische voorstelling bestaat uit losse [[punten]], want n is een natuurlijk getal.",
        ["product", "som", "lijnstukken"],
        "Constant verschil of constant quotiënt, en de rangnummers zijn 1, 2, 3, …",
    ),
    mk(
        r"Van een rekenkundige rij is \(u_3 = 11\) en \(u_7 = 23\). Wat is het verschil?",
        [r"\(12\)", r"\(4\)", r"\(2\)", r"\(3\)"],
        3,
        r"Van \(u_3\) naar \(u_7\) zijn 4 stappen: \(\frac{23 - 11}{4} = 3\).",
    ),
    mk(
        r"Een meetkundige rij met positieve termen heeft \(v_2 = 12\) en \(v_4 = 48\). Wat is \(v_1\)?",
        [r"\(3\)", r"\(6\)", r"\(24\)", r"\(4\)"],
        1,
        r"\(q^2 = \frac{48}{12} = 4\), dus \(q = 2\) en \(v_1 = \frac{12}{2} = 6\).",
    ),
    tabel(
        "Juist of fout over stijgen en dalen?",
        [
            (r"De rij \(u_n = 2^n\) heeft een toenemende stijging.", J),
            (r"De rij \(u_n = 5n - 1\) heeft een toenemende stijging.", F),
            (r"De rij \(u_n = 100 \cdot 0{,}8^n\) heeft een afnemende daling.", J),
            (r"De rij \(u_n = -3n + 4\) is stijgend.", F),
        ],
        r"Een rekenkundige rij stijgt of daalt gelijkmatig. \(100 \cdot 0{,}8^n\): \(80, 64, 51{,}2, \dots\), de sprongen worden kleiner.",
    ),
    open_(
        "Leg uit waarom samengestelde intrest op lange termijn meer oplevert dan enkelvoudige intrest aan hetzelfde percentage.",
        "Bij enkelvoudige intrest krijg je elk jaar intrest op het beginkapitaal: er komt telkens hetzelfde bedrag bij (rekenkundige rij). Bij samengestelde intrest krijg je ook intrest op de intrest van vorige jaren: het kapitaal wordt telkens met dezelfde factor vermenigvuldigd (meetkundige rij). Exponentiële groei haalt lineaire groei altijd in.",
        "Intrest op intrest.",
    ),
    mk(
        r"Hoeveel termen van de rij \(4, 7, 10, \dots\) zijn kleiner dan \(100\)?",
        [r"\(33\)", r"\(31\)", r"\(32\)", r"\(96\)"],
        2,
        r"\(u_n = 3n + 1 < 100\) geeft \(n < 33\). \(u_{32} = 97\), \(u_{33} = 100\) is niet kleiner.",
    ),
    inv(
        "Een bal valt van 2 m en botst telkens terug tot 60 % van de vorige hoogte. Hoe hoog (in m) komt hij na de derde bots? Rond af op drie decimalen.",
        "0,432",
        r"\(2 \cdot 0{,}6^3 = 2 \cdot 0{,}216 = 0{,}432\) m.",
    ),
    mk(
        r"De punten van een meetkundige rij liggen op de grafiek van \(f(x) = b \cdot a^x\). Hoe hangt de reden q samen met a?",
        [r"\(q = b\)", r"\(q = a - 1\)", r"\(q = \dfrac{1}{a}\)", r"\(q = a\)"],
        3,
        r"Van n naar \(n + 1\) wordt \(b \cdot a^n\) maal a. De groeifactor is de reden.",
    ),
    mk(
        "Een bedrijf verkoopt in het eerste jaar 5000 stuks en daarna elk jaar 200 stuks meer. Hoeveel stuks verkoopt het in totaal in de eerste 10 jaar?",
        [r"\(68\,000\)", r"\(50\,000\)", r"\(59\,000\)", r"\(118\,000\)"],
        2,
        r"Jaar 10: \(5000 + 9 \cdot 200 = 6800\). \(s_{10} = \frac{10}{2}(5000 + 6800) = 59\,000\).",
    ),
    mk(
        r"Wat weet je over een meetkundige rij met reden \(q = -2\) en \(u_1 = 1\)?",
        ["Ze is stijgend", "Ze is dalend", "Ze is constant", "Ze is niet stijgend en niet dalend"],
        3,
        r"\(1, -2, 4, -8, \dots\): de termen wisselen van teken, dus de rij gaat op en neer.",
    ),
    casus(
        "Iemand zet 1500 euro op een rekening met 2,5 % samengestelde intrest per jaar en stort daarna niets meer bij.",
        [
            mk(
                "Welk voorschrift geeft het kapitaal na n jaar?",
                [r"\(K_n = 1500 \cdot 0{,}025^n\)", r"\(K_n = 1500 + 37{,}5n\)", r"\(K_n = 1500 \cdot 1{,}025^n\)", r"\(K_n = 1500 \cdot 1{,}25^n\)"],
                2,
                r"\(2{,}5\) % erbij betekent maal \(1{,}025\).",
            ),
            inv(
                "Hoeveel staat er na 4 jaar op de rekening? Rond af op de cent.",
                "1655,72",
                r"\(1500 \cdot 1{,}025^4 \approx 1500 \cdot 1{,}103813 \approx 1655{,}72\) euro.",
            ),
            mk(
                "Na hoeveel volle jaren staat er voor het eerst meer dan 2000 euro?",
                [r"\(11\)", r"\(14\)", r"\(12\)", r"\(20\)"],
                2,
                r"Na 11 jaar: \(1500 \cdot 1{,}025^{11} \approx 1968\). Na 12 jaar: \(\approx 2017\).",
            ),
        ],
    ),
]
