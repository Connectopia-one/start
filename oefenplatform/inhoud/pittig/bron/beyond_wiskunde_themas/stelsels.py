"""Stelsels oplossen en matrixmodellen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_lijn, GROEN, LICHT

GRAAF = "stelsels-graaf-bey"
_K = {"A": (230, 170), "B": (230, 470), "C": (520, 320), "D": (820, 320)}
_R = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D")]


def _graaf():
    d = [s_lijn(*_K[a], *_K[b], dikte=4) for a, b in _R]
    for n, (x, y) in _K.items():
        d.append(f'<circle cx="{x}" cy="{y}" r="44" fill="{LICHT}" stroke="{GROEN}" stroke-width="4"/>')
        d.append(s_tekst(x, y + 13, n, 36, vet=True))
    return d


def _zone(n):
    x, y = _K[n]
    return pix_zone(x - 55, y - 55, 110, 110)


GRAFIEKEN = [dict(naam=GRAAF, titel="Een graaf met vier knopen", eigen=_graaf)]
PRENTEN = [dict(bestand=f"{GRAAF}.svg", zelf=True, wat="graaf met knopen A, B, C, D en vier verbindingen", vragen="klikvragen over de verbindingsmatrix")]

VRAGEN = [
    klik(
        "Klik op de knoop waarvan de rij in de verbindingsmatrix de meeste enen heeft.",
        f"{GRAAF}.svg",
        [_zone("C")],
        "C is verbonden met A, B en D: drie enen.",
    ),
    klik(
        r"Klik op de knoop waarvoor de rij in de verbindingsmatrix \(\begin{pmatrix} 0 & 0 & 1 & 0 \end{pmatrix}\) is, met de knopen in de volgorde A, B, C, D.",
        f"{GRAAF}.svg",
        [_zone("D")],
        "Enkel een verbinding met C: dat is D.",
    ),
    met_prent(f"{GRAAF}.svg", tabel(
        r"\(V\) is de verbindingsmatrix van deze graaf, met de knopen in de volgorde A, B, C, D. Juist of fout?",
        [(r"\(V\) is symmetrisch.", J), (r"Op de hoofddiagonaal van \(V\) staan enen.", F), (r"Het element op plaats \((1, 4)\) van \(V^{2}\) is 1.", J), (r"Er is een rechtstreekse verbinding van A naar D.", F)],
        r"Van A naar D is er één weg van lengte 2: via C. Een knoop is niet met zichzelf verbonden.",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{GRAAF}.svg", inv(
        r"Hoeveel wegen van lengte 2 lopen er van A terug naar A? Dat is het element \((1, 1)\) van \(V^{2}\).",
        ["2", "twee"],
        "A–B–A en A–C–A.",
    )),
    inv(
        r"Los op: \(\begin{cases} x + y + z = 6 \\ y + z = 5 \\ z = 3 \end{cases}\). Schrijf de oplossing als \((x, y, z)\).",
        ["(1,2,3)", "(1, 2, 3)"],
        r"Van onder naar boven: \(z = 3\), \(y = 2\), \(x = 1\).",
    ),
    sorteer(
        "Is het stelsel bepaald, onbepaald of strijdig?",
        ["Bepaald", "Onbepaald", "Strijdig"],
        [(r"\(x + y = 5\) en \(x - y = 1\)", "Bepaald"), (r"\(x + 2y = 3\) en \(2x + 4y = 6\)", "Onbepaald"), (r"\(x + 2y = 3\) en \(2x + 4y = 7\)", "Strijdig"),
         (r"\(\text{rang}(A) = 2\), \(\text{rang}(A \mid B) = 3\)", "Strijdig"), (r"\(\text{rang}(A) = \text{rang}(A \mid B) = 3\) bij 3 onbekenden", "Bepaald"), (r"\(\text{rang}(A) = \text{rang}(A \mid B) = 2\) bij 4 onbekenden", "Onbepaald")],
        "Vergelijk rang(A), rang(A | B) en het aantal onbekenden.",
    ),
    mk(
        r"De rijcanonieke vorm is \(\left(\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)\). Wat is de oplossing met \(z = t\)?",
        [r"\(x = 3 - 2t,\ y = 1 + t,\ z = t\)", r"\(x = 3 + 2t,\ y = 1 - t,\ z = t\)", r"\(x = 3,\ y = 1,\ z = 0\)", "er is geen oplossing"],
        0,
        r"\(x + 2z = 3\) en \(y - z = 1\): breng de termen met \(z\) naar rechts.",
    ),
    mk(
        r"Voor welke \(k\) heeft \(\begin{cases} x + ky = 2 \\ 2x + 4y = 4 \end{cases}\) oneindig veel oplossingen?",
        [r"\(k = 2\)", r"\(k = 4\)", r"\(k = -2\)", r"voor geen enkele \(k\)"],
        0,
        r"Voor \(k = 2\) is de tweede vergelijking het dubbel van de eerste.",
    ),
    tabel(
        r"Het stelsel \(\begin{cases} x + ky = 2 \\ 2x + 4y = 4 \end{cases}\): juist of fout?",
        [(r"Voor \(k = 3\) is het stelsel bepaald.", J), (r"Er is een \(k\) waarvoor het stelsel strijdig is.", F), (r"Voor elke \(k\) is \((2, 0)\) een oplossing.", J)],
        r"\((2, 0)\) voldoet altijd, dus het stelsel is nooit strijdig.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        r"Klanten wisselen elk jaar tussen merk P en merk Q volgens \(T = \begin{pmatrix} 0{,}8 & 0{,}3 \\ 0{,}2 & 0{,}7 \end{pmatrix}\). De eerste kolom hoort bij wie nu P heeft. Nu hebben 100 klanten P en 100 klanten Q.",
        [
            mk("Hoeveel procent van de P-klanten stapt na een jaar over naar Q?", ["20 %", "80 %", "30 %", "70 %"], 0, "Dat staat onderaan in de eerste kolom."),
            inv("Hoeveel klanten heeft P na één jaar?", ["110", "honderdtien"], r"\(0{,}8 \cdot 100 + 0{,}3 \cdot 100\)."),
            inv("Bij het evenwicht blijft het totaal 200. Hoeveel klanten heeft P dan?", ["120", "honderdtwintig"], r"Evenwicht: \(0{,}2p = 0{,}3q\), met \(p + q = 200\)."),
        ],
    ),
    tabel(
        "Is het een Markov-matrix?",
        [(r"\(\begin{pmatrix} 0{,}5 & 0{,}1 \\ 0{,}5 & 0{,}9 \end{pmatrix}\)", J), (r"\(\begin{pmatrix} 0{,}6 & 0{,}4 \\ 0{,}6 & 0{,}4 \end{pmatrix}\)", F), (r"\(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\)", J), (r"\(\begin{pmatrix} 0{,}7 & 0{,}5 \\ 0{,}2 & 0{,}5 \end{pmatrix}\)", F)],
        "Elke kolom moet optellen tot 1, en geen enkel getal mag negatief zijn.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Een populatie heeft jongen en volwassen dieren. Lesliematrix \(L = \begin{pmatrix} 0 & 2 \\ 0{,}5 & 0 \end{pmatrix}\), nu 10 jongen en 10 volwassen. Hoe ziet de populatie er na één stap uit?",
        ["20 jongen en 5 volwassen", "5 jongen en 20 volwassen", "10 jongen en 10 volwassen", "20 jongen en 10 volwassen"],
        0,
        "Elke volwassene krijgt 2 jongen; de helft van de jongen wordt volwassen.",
    ),
    koppel(
        "Verbind het matrixmodel met wat het beschrijft.",
        [("Lesliematrix", "een populatie per leeftijdsgroep"), ("Markov-matrix", "kansen om van toestand te wisselen"), ("verbindingsmatrix", "welke knopen rechtstreeks verbonden zijn"), ("migratiematrix", "verhuizen tussen streken")],
        ["de oplossing van een stelsel"],
        "Elke toepassing gebruikt een andere soort vierkante matrix.",
    ),
    volgorde(
        "Zet de stappen om een stelsel op te lossen met Gauss-Jordan in volgorde.",
        [r"schrijf de uitgebreide matrix \((A \mid B)\)", "maak met rijoperaties nullen onder de spilelementen", "maak ook nullen boven de spilelementen en zet de spillen op 1", "lees de oplossing af of stel vast dat het stelsel strijdig is"],
        "Het doel is de rijcanonieke vorm.",
    ),
    mk(
        r"Je lost \(AX = B\) op met \(A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\), \(A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\) en \(B = \begin{pmatrix} 4 \\ 11 \end{pmatrix}\). Wat is \(X\)?",
        [r"\(\begin{pmatrix} 1 \\ 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 2 \\ 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 23 \\ 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 \\ -2 \end{pmatrix}\)"],
        0,
        r"\(X = A^{-1}B\): \(12 - 11 = 1\) en \(-20 + 22 = 2\).",
    ),
    inv(
        "Twee T-shirts en drie petten kosten samen 46 euro. Eén T-shirt en één pet kosten samen 18 euro. Hoeveel euro kost een pet?",
        ["10", "tien"],
        r"\(2t + 3p = 46\) en \(2t + 2p = 36\) aftrekken geeft \(p = 10\).",
    ),
    keuze(
        r"Een stelsel met 3 onbekenden en \(\text{rang}(A) = \text{rang}(A \mid B) = 1\) heeft [[*2|1|0]] vrijheidsgraden. Het is [[*onbepaald|bepaald|strijdig]].",
        "Vrijheidsgraden = aantal onbekenden min de rang.",
    ),
    tabel(
        "Over het aantal oplossingen van stelsels: juist of fout?",
        [(r"Een stelsel met 2 vergelijkingen en 3 onbekenden kan strijdig zijn.", J), (r"Een stelsel waarvan alle rechterleden 0 zijn, heeft altijd minstens één oplossing.", J), (r"Als \(\det A \neq 0\), heeft \(AX = B\) precies één oplossing.", J), (r"Een stelsel met 3 vergelijkingen en 2 onbekenden is altijd strijdig.", F)],
        r"Een homogeen stelsel heeft altijd de nuloplossing. Drie rechten door één punt geven drie vergelijkingen met één oplossing.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"De evenwichtstoestand \(X\) voldoet aan [[\(TX = X\)]]. Je vindt de toestand na \(k\) stappen met [[\(T^{k}X_{0}\)]].",
        [r"\(TX = 0\)", r"\(kTX_{0}\)"],
        "Bij evenwicht verandert de toestand niet meer.",
    ),
    mk(
        r"Met \(T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\) en \(X_{0} = \begin{pmatrix} 30 \\ 70 \end{pmatrix}\): wat gebeurt er?",
        ["de toestand springt bij elke stap heen en weer", "het model komt na één stap in evenwicht", "na enkele stappen zit alles in de eerste groep", "de totale groep wordt elke stap kleiner"],
        0,
        r"\(X_{1} = (70, 30)\), \(X_{2} = (30, 70)\): er komt geen evenwicht.",
    ),
    inv(
        r"Een stelsel met 5 onbekenden heeft \(\text{rang}(A) = \text{rang}(A \mid B) = 3\). Hoeveel vrijheidsgraden heeft het?",
        ["2", "twee"],
        r"\(5 - 3\).",
    ),
    mk(
        r"Welke rij in de rijcanonieke vorm toont dat het stelsel strijdig is?",
        [r"\(\left(\begin{array}{ccc|c} 0 & 0 & 0 & 2 \end{array}\right)\)", r"\(\left(\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right)\)", r"\(\left(\begin{array}{ccc|c} 0 & 0 & 1 & 0 \end{array}\right)\)", r"\(\left(\begin{array}{ccc|c} 1 & 0 & 0 & 2 \end{array}\right)\)"],
        0,
        r"Die rij zegt \(0 = 2\).",
    ),
    tabel(
        r"Een migratiemodel heeft \(T = \begin{pmatrix} 0{,}9 & 0{,}2 \\ 0{,}1 & 0{,}8 \end{pmatrix}\) voor stad en platteland, met de stad in de eerste kolom. Juist of fout?",
        [("10 % van de stedelingen verhuist per jaar naar het platteland.", J), ("80 % van de plattelandsbewoners blijft wonen waar ze wonen.", J), ("Het totale aantal inwoners verandert door dit model.", F)],
        "Elke kolom telt op tot 1: niemand verdwijnt of komt erbij.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Drie bestellingen bevatten dezelfde drie artikelen a, b en c. Bestelling 1: twee keer a, één keer b en één keer c, samen 9 euro. Bestelling 2: a, twee keer b en c, samen 8 euro. Bestelling 3: a, b en twee keer c, samen 7 euro.",
        [
            inv("Tel de drie vergelijkingen op. Hoeveel kosten a, b en c samen, in euro?", ["6", "zes"], r"\(4a + 4b + 4c = 24\)."),
            inv("Hoeveel euro kost artikel a?", ["3", "drie"], r"Bestelling 1 min de som: \(a = 9 - 6\)."),
        ],
    ),
    mk(
        "Wanneer is de verbindingsmatrix van een graaf niet symmetrisch?",
        ["als sommige verbindingen maar in één richting lopen", "als de graaf meer dan vier knopen en lussen heeft", "als er een knoop is zonder enige verbinding met de rest", "als twee knopen langs twee wegen verbonden zijn"],
        0,
        "Bij eenrichtingsverkeer kan je wel van A naar B, maar niet terug.",
    ),
    inv(
        r"Met \(T = \begin{pmatrix} 0{,}5 & 0{,}5 \\ 0{,}5 & 0{,}5 \end{pmatrix}\) en \(X_{0} = \begin{pmatrix} 80 \\ 20 \end{pmatrix}\): hoeveel zitten er na één stap in de eerste groep?",
        ["50", "vijftig"],
        r"\(0{,}5 \cdot 80 + 0{,}5 \cdot 20\).",
    ),
    mk(
        "Welke bewerking geeft mogelijk een stelsel dat niet gelijkwaardig is?",
        ["beide leden van een vergelijking kwadrateren", "twee vergelijkingen van plaats met elkaar wisselen", "een vergelijking met 5 vermenigvuldigen", "een vergelijking bij een andere optellen"],
        0,
        "Kwadrateren kan oplossingen toevoegen; de andere drie zijn elementaire rijoperaties.",
    ),
]
