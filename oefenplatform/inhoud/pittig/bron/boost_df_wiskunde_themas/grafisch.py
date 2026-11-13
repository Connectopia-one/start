"""Tekenverloop, verloopschema en grafisch oplossen — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

# f(x) = (x + 2)(x - 1)(x - 4) / 4: nulwaarden -2, 1, 4; max ≈ 2,6 in x ≈ -0,73; min ≈ -2,6 in x ≈ 2,73
GRAF = venster("grafisch-f-derdegraad", -3, 5, -6, 6)
# kosten en opbrengst van een fietsenmaker
WINST = venster("grafisch-kosten-opbrengst", 0, 16, 0, 900, 2, 100)


def _f(x):
    return (x + 2) * (x - 1) * (x - 4) / 4


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f", krommen=[(_f, "groen", "", (-2.7, 4.7))]),
    dict(naam=WINST, titel="Kosten K en opbrengst O (in euro) bij x verkochte fietsen",
         krommen=[(lambda x: 300 + 20 * x, "oranje", "K", (0, 16)), (lambda x: 50 * x, "blauw", "O", (0, 16))],
         xlabel="x", ylabel="euro", labelplek={"K": (15, 600), "O": (15.4, 770)}),
]
PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over tekenverloop en grafisch oplossen") for g in GRAFIEKEN]

VRAGEN = [
    klik(
        "Klik op een stuk van de grafiek waar f stijgt en negatief is.",
        f"{GRAF}.svg",
        [vak_zone(GRAF, -2.7, -2, -6, 0), vak_zone(GRAF, 2.73, 4, -2.7, 0)],
        r"Stijgend én onder de \(x\)-as: links van \(-2\), en tussen het minimum (rond \(x \approx 2{,}7\)) en de nulwaarde \(4\).",
    ),
    klik(
        "Klik op de nulwaarde van f die tussen de twee toppen ligt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 0)],
        r"De nulwaarden zijn \(-2\), \(1\) en \(4\). Tussen de top links (rond \(x \approx -0{,}7\)) en de top rechts (rond \(x \approx 2{,}7\)) ligt \(1\).",
    ),
    met_prent(f"{GRAF}.svg", mk(
        r"Wat is de oplossingenverzameling van \(f(x) > 0\), binnen het getekende stuk?",
        [
            r"\(\left]-2, 1\right[ \cup \left]4, 4{,}7\right]\)",
            r"\(\left[-2, 1\right] \cup \left[4, 4{,}7\right]\)",
            r"\(\left]-2{,}7; -2\right[ \cup \left]1, 4\right[\)",
            r"\(\left]-0{,}7;\ 2{,}7\right[\)",
        ],
        0,
        r"Boven de \(x\)-as: tussen \(-2\) en \(1\), en rechts van \(4\). De nulwaarden zelf horen er niet bij, want daar is \(f(x) = 0\).",
    )),
    met_prent(f"{GRAF}.svg", tabel(
        "Vul het tekenverloop van f aan: welk teken heeft f(x)?",
        [
            (r"voor \(x = -2{,}5\)", "−"),
            (r"voor \(x = -2\)", "0"),
            (r"voor \(x = 0\)", "+"),
            (r"voor \(x = 3\)", "−"),
            (r"voor \(x = 4{,}5\)", "+"),
        ],
        r"Links van \(-2\) ligt de grafiek onder de as, tussen \(-2\) en \(1\) erboven, tussen \(1\) en \(4\) eronder, rechts van \(4\) erboven. In een nulwaarde staat een \(0\).",
        kolommen=["+", "0", "−"],
    )),
    met_prent(f"{GRAF}.svg", sorteer(
        "Stijgt of daalt f op dit interval?",
        ["stijgt", "daalt"],
        [
            [r"\(\left[-2{,}5;\ -1\right]\)", "stijgt"],
            [r"\(\left[0, 2\right]\)", "daalt"],
            [r"\(\left[3, 4{,}5\right]\)", "stijgt"],
            [r"\(\left[1, 2{,}5\right]\)", "daalt"],
        ],
        r"Het verloopschema: stijgen tot het maximum rond \(-0{,}7\), dalen tot het minimum rond \(2{,}7\), daarna weer stijgen. Stijgen of dalen staat los van boven of onder de as.",
    )),
    met_prent(f"{GRAF}.svg", inv(
        r"Hoeveel oplossingen heeft \(f(x) = 2\) binnen het getekende stuk?",
        ["3", "drie"],
        r"De horizontale lijn \(y = 2\) snijdt de grafiek drie keer: één keer links van de top, één keer bij \(x = 0\) (want \(f(0) = 2\)) en één keer rechts, voorbij \(4\).",
    )),
    klik(
        "Klik op het break-evenpunt: daar zijn kosten en opbrengst gelijk.",
        f"{WINST}.svg",
        [punt_zone(WINST, 10, 500)],
        r"\(300 + 20x = 50x\) geeft \(x = 10\): bij \(10\) fietsen zijn kosten en opbrengst allebei \(500\) euro.",
    ),
    met_prent(f"{WINST}.svg", mk(
        "Hoeveel winst maakt de fietsenmaker bij 14 fietsen?",
        [r"\(120\) euro", r"\(700\) euro", r"\(580\) euro", r"\(420\) euro"],
        0,
        r"Opbrengst \(50 \cdot 14 = 700\) euro, kosten \(300 + 20 \cdot 14 = 580\) euro. Winst \(700 - 580 = 120\) euro.",
    )),
    met_prent(f"{WINST}.svg", keuze(
        "Links van het snijpunt ligt de grafiek van [[*K|O]] boven die van [[*O|K]]: daar maakt de fietsenmaker [[*verlies|winst]].",
        "Waar de kosten hoger zijn dan de opbrengst, is er verlies. Rechts van het snijpunt ligt O boven K.",
    )),
    mk(
        r"Wat is de oplossing van \(-2x + 6 \leq 0\)?",
        [r"\(x \leq 3\)", r"\(x \geq 3\)", r"\(x \geq -3\)", r"\(x \leq -3\)"],
        1,
        r"De rechte daalt en heeft nulwaarde \(3\). Rechts daarvan is ze negatief. Algebraïsch: \(-2x \leq -6\), delen door \(-2\) draait het teken: \(x \geq 3\).",
    ),
    tabel(
        r"Juist of fout over \(f(x) = -\tfrac{1}{2}x + 2\)?",
        [
            ("Het tekenverloop is: + voor x < 4, 0 in x = 4, − voor x > 4.", J),
            ("De functie stijgt, want ze is positief voor kleine x.", F),
            ("Het verloopschema is één pijl naar beneden over heel ℝ.", J),
            (r"\(f(0) = 4\)", F),
        ],
        r"Negatieve richtingscoëfficiënt: dalend overal. Nulwaarde \(-\tfrac{1}{2}x + 2 = 0\) geeft \(x = 4\). \(f(0) = 2\), het snijpunt met de \(y\)-as.",
    ),
    koppel(
        "Koppel elke vraag aan wat je op de grafiek zoekt.",
        [
            [r"\(f(x) = 0\)", r"waar de grafiek van \(f\) de \(x\)-as snijdt"],
            [r"\(f(x) < 0\)", r"waar de grafiek van \(f\) onder de \(x\)-as ligt"],
            [r"\(f(x) = g(x)\)", "waar de twee grafieken elkaar snijden"],
            [r"\(f(x) > g(x)\)", r"waar de grafiek van \(f\) boven die van \(g\) ligt"],
        ],
        [r"waar de grafiek van \(f\) de \(y\)-as snijdt"],
        r"Het snijpunt met de \(y\)-as is \(f(0)\); dat beantwoordt geen van deze vragen.",
    ),
    mk(
        r"De grafieken van \(f\) en \(g\) snijden elkaar enkel in \(x = -1\) en \(x = 3\). Tussen die waarden ligt \(f\) onder \(g\). Wat is de oplossing van \(f(x) \geq g(x)\)?",
        [
            r"\(\left]-\infty, -1\right] \cup \left[3, +\infty\right[\)",
            r"\(\left[-1, 3\right]\)",
            r"\(\left]-1, 3\right[\)",
            r"\(\left]-\infty, -1\right[ \cup \left]3, +\infty\right[\)",
        ],
        0,
        r"Buiten de snijpunten ligt \(f\) boven \(g\). Met \(\geq\) horen de snijpunten zelf erbij: gesloten haakjes bij \(-1\) en \(3\).",
    ),
    casus(
        r"Een verhuurfirma A vraagt \(40\) euro per dag voor een bestelwagen plus \(0{,}25\) euro per km. Firma B vraagt \(25\) euro per dag plus \(0{,}40\) euro per km. Je huurt voor één dag.",
        [
            inv(
                "Bij hoeveel km kosten beide firma's evenveel?",
                ["100", "100 km"],
                r"\(40 + 0{,}25k = 25 + 0{,}40k\) geeft \(15 = 0{,}15k\), dus \(k = 100\).",
            ),
            mk(
                "Voor welke afstanden is firma A goedkoper?",
                [r"voor minder dan \(100\) km", r"voor meer dan \(100\) km", r"voor meer dan \(160\) km", "voor elke afstand"],
                1,
                r"A heeft een hoger vast bedrag maar een lagere prijs per km: na het snijpunt groeit A trager. Bij \(200\) km: A \(90\) euro, B \(105\) euro.",
            ),
        ],
    ),
    volgorde(
        r"Je lost \(3x - 2 < x + 4\) grafisch op. Zet de stappen in volgorde.",
        [
            r"de rechten \(y = 3x - 2\) en \(y = x + 4\) tekenen",
            r"het snijpunt aflezen: \(x = 3\)",
            r"kijken aan welke kant de eerste rechte lager ligt",
            r"de oplossing noteren: \(\left]-\infty, 3\right[\)",
            r"controleren met een getal, bv. \(x = 0\): \(-2 < 4\)",
        ],
        "Eerst tekenen, dan het snijpunt, dan de kant kiezen, dan noteren en controleren.",
    ),
    sleep(
        "Een tekenverloop toont waar een functie [[positief]] of [[negatief]] is. Een verloopschema toont waar ze [[stijgt]] of daalt.",
        ["constant", "groot"],
        "Positief of negatief gaat over boven of onder de x-as liggen. Stijgen of dalen gaat over de richting.",
    ),
    tabel(
        "Juist of fout over functies en hun grafiek?",
        [
            ("Een functie die stijgt, kan negatieve functiewaarden hebben.", J),
            ("In een maximum gaat een functie over van stijgen naar dalen.", J),
            ("Een functie met een nulwaarde verandert daar altijd van teken.", F),
            ("Een eerstegraadsfunctie heeft altijd een maximum.", F),
        ],
        r"Een grafiek kan de \(x\)-as raken zonder erdoor te gaan, zoals \(y = x^{2}\) in \(0\). Een rechte die niet horizontaal is, stijgt of daalt overal: geen maximum.",
    ),
    mk(
        r"Een zwembad loopt leeg. Het waterpeil is \(h(t) = 180 - 12t\) cm na \(t\) uur. Wanneer staat er minder dan \(60\) cm water in?",
        [r"na \(10\) uur", r"vanaf meer dan \(10\) uur", r"na \(5\) uur", r"vanaf meer dan \(15\) uur"],
        1,
        r"\(180 - 12t < 60\) geeft \(120 < 12t\), dus \(t > 10\) uur.",
    ),
    inv(
        r"Een gsm-abonnement kost \(12\) euro per maand plus \(0{,}08\) euro per minuut bellen boven de bundel. Je wil hoogstens \(20\) euro betalen. Hoeveel minuten kan je hoogstens extra bellen?",
        ["100", "100 minuten"],
        r"\(12 + 0{,}08m \leq 20\) geeft \(m \leq 100\).",
    ),
    mk(
        r"Waar snijden \(f(x) = 2x - 3\) en \(g(x) = -x + 9\) elkaar?",
        [r"\((4, 5)\)", r"\((2, 1)\)", r"\((3, 6)\)", r"\((6, 3)\)"],
        0,
        r"\(2x - 3 = -x + 9\) geeft \(3x = 12\), \(x = 4\) en \(y = 5\). Controle: \(-4 + 9 = 5\).",
    ),
    open_(
        r"Een leerling zegt: 'Rechts van haar maximum is een functie negatief.' Leg uit waarom dat niet klopt, met een voorbeeld.",
        r"Rechts van een maximum daalt de functie, maar ze kan nog lang boven de \(x\)-as liggen. Bij f in deze oefeningen ligt het maximum rond \(x = -0{,}7\) en is f nog positief tot \(x = 1\). Dalen gaat over de richting, negatief over de ligging.",
    ),
    mk(
        r"Een functie heeft dit tekenverloop: \(-\) voor \(x < -1\), \(0\) in \(-1\), \(+\) tussen \(-1\) en \(5\), \(0\) in \(5\), \(-\) voor \(x > 5\). Wat is de oplossing van \(f(x) \leq 0\)?",
        [
            r"\(\left]-\infty, -1\right] \cup \left[5, +\infty\right[\)",
            r"\(\left[-1, 5\right]\)",
            r"\(\left]-\infty, -1\right[ \cup \left]5, +\infty\right[\)",
            r"\(\left]-1, 5\right[\)",
        ],
        0,
        r"Negatief of nul: links van \(-1\), rechts van \(5\), en de nulwaarden zelf horen erbij.",
    ),
    tabel(
        r"De opbrengst van een schoolfuif is \(O(n) = 8n\) en de kosten zijn \(K(n) = 600 + 2n\), met \(n\) bezoekers. Juist of fout?",
        [
            (r"Bij \(120\) bezoekers is er winst.", J),
            (r"Het break-evenpunt ligt bij \(75\) bezoekers.", F),
            (r"Elke extra bezoeker brengt \(6\) euro winst op.", J),
            (r"Bij \(50\) bezoekers is het verlies \(300\) euro.", J),
        ],
        r"\(8n = 600 + 2n\) geeft \(n = 100\): dat is het break-evenpunt. Bij \(120\): \(960 - 840 = 120\) euro winst. Elke bezoeker: \(8 - 2 = 6\) euro. Bij \(50\): \(400 - 700 = -300\).",
    ),
    klik(
        "Klik op het punt dat de vaste kosten van de fietsenmaker toont.",
        f"{WINST}.svg",
        [punt_zone(WINST, 0, 300)],
        r"De vaste kosten betaal je ook als je niets verkoopt: \(K(0) = 300\) euro, het snijpunt van K met de verticale as.",
    ),
    met_prent(f"{GRAF}.svg", mk(
        r"Hoeveel oplossingen heeft \(f(x) = 3\) binnen het getekende stuk?",
        [r"\(0\)", r"\(1\)", r"\(2\)", r"\(3\)"],
        1,
        r"Het maximum links is maar ongeveer \(2{,}6\), dus de lijn \(y = 3\) raakt daar niets. Enkel rechts, voorbij \(x = 4\), komt de grafiek op hoogte \(3\).",
    )),
    mk(
        r"Hoe ziet het verloopschema van \(f(x) = 3\) eruit?",
        [
            "één pijl omhoog over heel ℝ",
            "een horizontale pijl over heel ℝ: de functie is constant",
            "een pijl omhoog tot 3 en daarna naar beneden",
            "een 0 in x = 3",
        ],
        1,
        "Een constante functie stijgt niet en daalt niet. Haar tekenverloop is overal +, want 3 is positief.",
    ),
    inv(
        r"Voor welke \(x\) wordt \(f(x) = 4x - 10\) positief? Geef de grens: f is positief voor \(x\) groter dan ...",
        ["2,5", "2.5", "5/2"],
        r"\(4x - 10 > 0\) geeft \(x > 2{,}5\). De rechte stijgt, dus rechts van de nulwaarde is ze positief.",
    ),
    keuze(
        r"Voor \(f(x) = 2x + 4\) is het teken [[*\(-\)|\(+\)]] voor \(x < -2\) en [[*\(+\)|\(-\)]] voor \(x > -2\), en het verloopschema is [[*stijgend|dalend|constant]].",
        r"Nulwaarde \(-2\), richtingscoëfficiënt \(2 > 0\): links negatief, rechts positief, en overal stijgend.",
    ),
    sorteer(
        r"Is \(f(x) = -3x + 6\) bij deze \(x\) positief, nul of negatief?",
        ["positief", "nul", "negatief"],
        [
            [r"\(x = -1\)", "positief"],
            [r"\(x = 2\)", "nul"],
            [r"\(x = 5\)", "negatief"],
            [r"\(x = 0\)", "positief"],
            [r"\(x = 2{,}5\)", "negatief"],
        ],
        r"Nulwaarde \(2\). De rechte daalt: links van \(2\) positief, rechts ervan negatief. \(f(2{,}5) = -1{,}5\).",
    ),
]
