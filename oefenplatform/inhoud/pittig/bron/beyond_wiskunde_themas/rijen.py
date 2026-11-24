"""Rijen en hun limiet — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone

GRAF = venster("rijen-alternerend-bey", 0, 9, -1, 6)
TERMEN = [(n, 2 + 3 * (-0.5) ** (n - 1)) for n in range(1, 9)]

GRAFIEKEN = [
    dict(naam=GRAF, titel="De eerste acht termen van de rij u", reeksen=[(TERMEN, "paars", "u")], stippel=[("h", 2)], xlabel="n", ylabel="uₙ"),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="alternerende rij 2 + 3·(−1/2)^(n−1) met stippellijn y = 2", vragen="klikvragen over convergentie en termen")]

VRAGEN = [
    klik(
        "Klik op de kleinste term van de rij die je ziet.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 0.5)],
        r"\(u_{2} = 2 + 3 \cdot \left(-\tfrac{1}{2}\right) = 0{,}5\).",
    ),
    klik(
        "Klik op de eerste term die op minder dan 0,1 van de limiet ligt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 6, TERMEN[5][1])],
        r"De limiet is 2. \(u_{5} \approx 2{,}19\) ligt nog op \(0{,}19\), \(u_{6} \approx 1{,}91\) op \(0{,}09\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de rij. Juist of fout?",
        [("De rij is alternerend rond 2.", J), ("De rij convergeert naar 2.", J), ("De rij is stijgend.", F), ("Alle termen zijn positief.", J), (r"De rij is meetkundig.", F)],
        r"\(u_{n} - 2\) is meetkundig met reden \(-\tfrac{1}{2}\), maar \(u_{n}\) zelf niet: \(\tfrac{u_{2}}{u_{1}} = 0{,}1\) en \(\tfrac{u_{3}}{u_{2}} = 5{,}5\).",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{GRAF}.svg", mk(
        "Kijk naar de rij. Welk voorschrift past?",
        [r"\(u_{n} = 2 + 3\left(-\tfrac{1}{2}\right)^{n - 1}\)", r"\(u_{n} = 5\left(-\tfrac{1}{2}\right)^{n - 1}\)", r"\(u_{n} = 2 - 3\left(\tfrac{1}{2}\right)^{n}\)", r"\(u_{n} = 5 - \tfrac{n}{2}\)"],
        0,
        r"\(u_{1} = 5\), \(u_{2} = 0{,}5\) en de schommeling rond 2 halveert telkens.",
    )),
    tabel(
        "Rekenkundig, meetkundig of geen van beide?",
        [("5, 2, −1, −4, …", "rekenkundig"), ("48, −24, 12, −6, …", "meetkundig"), ("1, 4, 9, 16, …", "geen van beide"), ("7, 7, 7, 7, …", "allebei"), ("3, 3,3, 3,63, 3,993, …", "meetkundig")],
        r"Een constante rij is rekenkundig met \(d = 0\) en meetkundig met \(q = 1\). De laatste heeft \(q = 1{,}1\).",
        kolommen=["rekenkundig", "meetkundig", "allebei", "geen van beide"],
    ),
    mk(
        r"In een rekenkundige rij is \(u_{4} = 17\) en \(u_{10} = 41\). Wat is \(u_{1}\)?",
        [r"\(5\)", r"\(4\)", r"\(13\)", r"\(1\)"],
        0,
        r"\(6d = 24\), \(d = 4\). \(u_{1} = 17 - 3 \cdot 4 = 5\).",
    ),
    inv(
        r"Hoeveel is \(3 + 7 + 11 + \ldots + 79\)?",
        ["820"],
        r"\(d = 4\), \(79 = 3 + (n - 1)4\) geeft \(n = 20\). \(S = 20 \cdot \tfrac{3 + 79}{2} = 820\).",
    ),
    mk(
        r"In een meetkundige rij is \(u_{2} = 6\) en \(u_{5} = 162\). Wat is \(q\)?",
        [r"\(3\)", r"\(27\)", r"\(52\)", r"\(\sqrt{27}\)"],
        0,
        r"\(q^{3} = \tfrac{162}{6} = 27\), dus \(q = 3\).",
    ),
    inv(
        r"Bereken \(2 + 6 + 18 + \ldots\) tot en met de achtste term.",
        ["6560"],
        r"\(S_{8} = 2 \cdot \dfrac{3^{8} - 1}{3 - 1} = 3^{8} - 1 = 6560\).",
    ),
    sorteer(
        "Convergent of divergent?",
        ["Convergent", "Divergent"],
        [(r"\(u_{n} = \tfrac{3n - 1}{n + 2}\)", "Convergent"), (r"\(u_{n} = (-1)^{n}\)", "Divergent"), (r"\(u_{n} = 0{,}9^{n}\)", "Convergent"), (r"\(u_{n} = 1{,}1^{n}\)", "Divergent"), (r"\(u_{n} = \tfrac{(-1)^{n}}{n}\)", "Convergent"), (r"\(u_{n} = 2n - 5\)", "Divergent")],
        r"\(\tfrac{(-1)^{n}}{n}\) springt, maar de sprongen worden kleiner: limiet 0.",
    ),
    casus(
        "Een bal valt van 10 m hoog en stuitert telkens tot 60 % van de vorige hoogte.",
        [
            inv("Hoe hoog stuitert hij na de derde bots, in meter?", ["2,16", "2.16"], r"\(10 \cdot 0{,}6^{3} = 2{,}16\)."),
            mk("Hoeveel meter legt hij in totaal naar beneden af, als hij oneindig lang stuitert?", ["25 m", "16,7 m", "50 m", "oneindig veel"], 0,
               r"\(10 + 6 + 3{,}6 + \ldots = \dfrac{10}{1 - 0{,}6} = 25\)."),
            mk("En de totale afstand, op en neer samen?", ["40 m", "50 m", "25 m", "35 m"], 0,
               r"Naar boven: \(6 + 3{,}6 + \ldots = 15\). Totaal \(25 + 15 = 40\)."),
        ],
    ),
    tabel(
        "Bereken de limiet van de rij.",
        [(r"\(\lim\dfrac{5n^{2} - 1}{2n^{2} + n}\)", r"\(\tfrac{5}{2}\)"), (r"\(\lim\left(\tfrac{2}{3}\right)^{n}\)", r"\(0\)"), (r"\(\lim\dfrac{n}{n^{2} + 1}\)", r"\(0\)"), (r"\(\lim\dfrac{3^{n}}{3^{n} + 1}\)", r"\(1\)")],
        "Deel door de snelst groeiende term.",
        kolommen=[r"\(\tfrac{5}{2}\)", r"\(0\)", r"\(1\)"],
    ),
    inv(
        r"Schrijf \(0{,}\overline{36} = 0{,}363636\ldots\) als vereenvoudigde breuk.",
        ["4/11"],
        r"\(\tfrac{36}{100} + \tfrac{36}{100^{2}} + \ldots = \dfrac{0{,}36}{1 - 0{,}01} = \dfrac{36}{99} = \dfrac{4}{11}\).",
    ),
    keuze(
        r"Een oneindige meetkundige reeks heeft een eindige som als [[*\(|q| < 1\)|\(q > 0\)|\(q < 1\)]]. De som is dan [[*\(\dfrac{u_{1}}{1 - q}\)|\(\dfrac{u_{1}}{q - 1}\)|\(u_{1} \cdot q\)]].",
        r"Met \(q = -2\) is \(q < 1\), maar de termen worden steeds groter.",
    ),
    mk(
        r"Een rij is recursief gegeven: \(u_{1} = 2\) en \(u_{n + 1} = 3u_{n} - 1\). Wat is \(u_{4}\)?",
        [r"\(41\)", r"\(14\)", r"\(53\)", r"\(122\)"],
        0,
        r"\(u_{2} = 5\), \(u_{3} = 14\), \(u_{4} = 41\).",
    ),
    koppel(
        "Verbind de rij met haar limiet.",
        [(r"\(\dfrac{4n + 3}{2n - 1}\)", r"\(2\)"), (r"\(\left(-\tfrac{1}{3}\right)^{n}\)", r"\(0\)"), (r"\(\sqrt{n}\)", r"\(+\infty\)"), (r"\(1 + \tfrac{1}{2} + \tfrac{1}{4} + \ldots + \tfrac{1}{2^{n}}\)", r"\(2\)")],
        [r"\(-\infty\)"],
        "Twee rijen kunnen dezelfde limiet hebben.",
    ),
    mk(
        "Een werknemer krijgt 2000 euro per maand en elk jaar 2 % opslag. Hoeveel verdient hij in totaal over de eerste 10 jaar, afgerond?",
        ["262 793 euro", "240 000 euro", "244 800 euro", "292 559 euro"],
        0,
        r"Jaarloon 24 000, meetkundig met \(q = 1{,}02\): \(24\,000 \cdot \dfrac{1{,}02^{10} - 1}{0{,}02} \approx 262\,793\).",
    ),
    tabel(
        "Over rijen: juist of fout?",
        [("Elke stijgende rij is divergent.", F), ("Een rekenkundige rij met d ≠ 0 divergeert.", J), ("Als de som van een reeks bestaat, gaan de termen naar 0.", J), ("Als de termen naar 0 gaan, bestaat de som van de reeks altijd.", F)],
        r"\(1 - \tfrac{1}{n}\) stijgt en convergeert. De harmonische reeks \(1 + \tfrac{1}{2} + \tfrac{1}{3} + \ldots\) heeft termen die naar 0 gaan, maar geen eindige som.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"Bij een rekenkundige rij liggen de punten \((n, u_{n})\) op een [[rechte]]. Bij een meetkundige rij met \(q > 1\) groeien ze [[exponentieel]].",
        ["parabool", "lineair"],
        "Vast verschil: lineair. Vaste factor: exponentieel.",
    ),
    inv(
        r"Vanaf welke \(n\) is \(0{,}8^{n} < 0{,}01\)?",
        ["21"],
        r"\(n > \dfrac{\ln 0{,}01}{\ln 0{,}8} \approx 20{,}6\).",
    ),
    volgorde(
        "Zet de termen van klein naar groot.",
        [r"\(\lim\left(1 - \tfrac{1}{n}\right)\)", r"\(\sum_{k=0}^{\infty}\left(\tfrac{1}{3}\right)^{k}\)", r"\(\sum_{k=0}^{\infty}\left(\tfrac{1}{2}\right)^{k}\)", r"\(\lim\dfrac{3n}{n + 1}\)"],
        r"\(1\), \(\tfrac{3}{2}\), \(2\), \(3\).",
    ),
    mk(
        r"Wat is \(\lim\limits_{n \to +\infty}\left(\sqrt{n + 1} - \sqrt{n}\right)\)?",
        [r"\(0\)", r"\(1\)", r"\(+\infty\)", r"bestaat niet"],
        0,
        r"\(\dfrac{1}{\sqrt{n + 1} + \sqrt{n}} \to 0\).",
    ),
    inv(
        r"De som van een oneindige meetkundige reeks is 12 en \(u_{1} = 4\). Hoeveel is \(q\)? Typ als breuk.",
        ["2/3"],
        r"\(\tfrac{4}{1 - q} = 12\) geeft \(1 - q = \tfrac{1}{3}\).",
    ),
    tabel(
        r"Over de rij \(u_{n} = \tfrac{n}{n + 1}\). Juist of fout?",
        [("De rij is stijgend.", J), ("Alle termen liggen tussen 0 en 1.", J), ("De limiet is 1.", J), ("Er is een term gelijk aan 1.", F)],
        r"\(\tfrac{n}{n + 1} = 1 - \tfrac{1}{n + 1}\): stijgend naar 1, zonder het te bereiken.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Hoeveel termen van de rij \(5, 9, 13, \ldots\) moet je optellen om een som van 230 te krijgen?",
        ["10", "12", "56", "9"],
        0,
        r"\(S_{n} = \tfrac{n}{2}(10 + 4(n - 1)) = 2n^{2} + 3n = 230\) geeft \(n = 10\).",
    ),
    inv(
        r"De termen \(x\), \(x + 6\), \(x + 18\) vormen een meetkundige rij. Hoeveel is \(x\)?",
        ["6"],
        r"\((x + 6)^{2} = x(x + 18)\) geeft \(x^{2} + 12x + 36 = x^{2} + 18x\), dus \(x = 6\). De rij is \(6, 12, 24\).",
    ),
    tabel(
        r"Welke uitspraak past bij de rij \(u_{n} = 3 \cdot 2^{n}\)?",
        [("meetkundig met q = 2", J), (r"\(u_{1} = 6\)", J), ("convergent", F), (r"\(\tfrac{u_{n + 1}}{u_{n}} = 2\) voor elke n", J)],
        "Een meetkundige rij met q > 1 en positieve termen gaat naar +∞.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"Het getal \(0{,}999\ldots\) is [[*gelijk aan|iets kleiner dan]] 1, want \(\tfrac{0{,}9}{1 - 0{,}1} =\) [[*1|0,9|0,99]].",
        "Een oneindige meetkundige reeks met q = 0,1.",
    ),
]
