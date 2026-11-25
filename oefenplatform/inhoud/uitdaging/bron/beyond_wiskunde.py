# -*- coding: utf-8 -*-
"""Uitdaging Wiskunde 🌍 Beyond doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen, van logaritmen tot matrices, integralen, kansen en vectoren in
de ruimte. Casussen, tabellen, keuzelijsten, koppelen, rekenvragen, vier
klikvragen op twee zelf getekende prenten en een open vraag. Geen nieuwe
leerstof: alles staat in de hoofdstukken van Wiskunde Beyond doorstroom.
Geen meerkeuze met meer dan één juist antwoord.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_wiskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Wiskunde"
BESTAND = "beyond-wiskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/wiskunde-beyond-uitdaging"
GRAFIEK = "grafiek-derdegraad.svg"
KLOK = "normale-verdeling-lengte.svg"
# klikvakken: zie maak_prenten_beyond_wiskunde.py
MAXIMUM = [31.7, 16.5, 10.0, 12.5]
BUIGPUNT = [45.0, 46.5, 10.0, 12.5]
GEBIED_A = [6.0, 19.6, 22.0, 58.9]
GEBIED_C = [39.0, 19.6, 11.0, 58.9]
GEBIED_F = [72.0, 19.6, 22.0, 58.9]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # De grafiek van f (prent)
    klik("Bekijk de grafiek van f. Klik op het lokaal maximum.",
         GRAFIEK, [MAXIMUM],
         "In het punt \\((-1, 2)\\) gaat de grafiek van stijgen over naar dalen: daar ligt het lokaal maximum. De afgeleide wisselt er van plus naar min."),
    klik("Klik op het buigpunt van de grafiek.",
         GRAFIEK, [BUIGPUNT],
         "In de oorsprong gaat de grafiek over van bol (holle kant naar beneden) naar hol (holle kant naar boven). Daar wisselt de tweede afgeleide van teken."),
    met_prent(GRAFIEK, tabel(
        "Het voorschrift van f is \\(f(x) = x^{3} - 3x\\). Klopt dit?",
        [
            ("\\(f'(x) < 0\\) voor \\(-1 < x < 1\\)", J),
            ("\\(f''(x) > 0\\) voor \\(x < 0\\)", F),
            ("f heeft drie reële nulwaarden.", J),
            ("f is inverteerbaar op \\(\\mathbb{R}\\).", F),
        ],
        "\\(f'(x) = 3x^{2} - 3\\) is negatief tussen \\(-1\\) en \\(1\\): daar daalt f. \\(f''(x) = 6x\\) is negatief voor \\(x < 0\\): daar is de grafiek bol. De grafiek snijdt de x-as drie keer. Een horizontale rechte zoals \\(y = 1\\) snijdt de grafiek drie keer, dus f is niet inverteerbaar op heel \\(\\mathbb{R}\\).")),
    met_prent(GRAFIEK, mk(
        "Wat is een vergelijking van de raaklijn aan de grafiek van \\(f(x) = x^{3} - 3x\\) in het punt met \\(x = 2\\)?",
        ["\\(y = 9x - 16\\)", "\\(y = 9x + 2\\)", "\\(y = 12x - 22\\)", "\\(y = 3x - 4\\)"],
        0,
        "\\(f(2) = 8 - 6 = 2\\) en \\(f'(2) = 3 \\cdot 4 - 3 = 9\\). De raaklijn is \\(y - 2 = 9(x - 2)\\), dus \\(y = 9x - 16\\).")),
    met_prent(GRAFIEK, inv(
        "Bereken de oppervlakte van het gebied tussen de grafiek van \\(f(x) = x^{3} - 3x\\) en de x-as, van \\(x = 0\\) tot \\(x = \\sqrt{3}\\). Geef een decimaal getal.",
        ["2,25", "2.25", "9/4"],
        "Op dat interval ligt de grafiek onder de x-as, dus je integreert \\(-f\\): \\(\\int_{0}^{\\sqrt{3}} (3x - x^{3})\\,dx = \\left[\\tfrac{3}{2}x^{2} - \\tfrac{1}{4}x^{4}\\right]_{0}^{\\sqrt{3}} = \\tfrac{9}{2} - \\tfrac{9}{4} = \\tfrac{9}{4}\\).")),

    # De normale verdeling (prent)
    klik("De lengte X van volwassenen is normaal verdeeld met \\(\\mu = 170\\) cm en \\(\\sigma = 8\\) cm. Klik op het gebied dat hoort bij \\(P(162 < X < 170)\\).",
         KLOK, [GEBIED_C],
         "162 ligt één standaardafwijking onder het gemiddelde. Het gebied tussen 162 en 170 is C."),
    klik("Klik op een gebied dat ongeveer 2,5 procent van de volwassenen bevat.",
         KLOK, [GEBIED_A, GEBIED_F],
         "Tussen \\(\\mu - 2\\sigma\\) en \\(\\mu + 2\\sigma\\) ligt ongeveer 95 procent. De overige 5 procent verdeelt zich gelijk over de twee staarten: A en F bevatten elk ongeveer 2,5 procent."),
    met_prent(KLOK, inv(
        "Hoeveel procent van de volwassenen is ongeveer tussen 162 en 186 cm groot? Gebruik de vuistregels 68 en 95 procent.",
        ["81,5", "81.5"],
        "Van \\(\\mu - \\sigma\\) tot \\(\\mu\\) is ongeveer 34 procent, van \\(\\mu\\) tot \\(\\mu + \\sigma\\) ook 34 procent, en van \\(\\mu + \\sigma\\) tot \\(\\mu + 2\\sigma\\) ongeveer 13,5 procent. Samen 81,5 procent.")),
    met_prent(KLOK, tabel(
        "Bereken de z-score van elke lengte.",
        [
            ("\\(186\\) cm", "\\(2\\)"),
            ("\\(166\\) cm", "\\(-0{,}5\\)"),
            ("\\(170\\) cm", "\\(0\\)"),
        ],
        "\\(z = \\dfrac{x - \\mu}{\\sigma}\\): \\((186 - 170)/8 = 2\\), \\((166 - 170)/8 = -0{,}5\\) en \\((170 - 170)/8 = 0\\).",
        kolommen=["\\(-0{,}5\\)", "\\(0\\)", "\\(2\\)"])),

    # Machten en logaritmen
    tabel(
        "Bereken.",
        [
            ("\\(\\log_{2} 32\\)", "\\(5\\)"),
            ("\\(27^{2/3}\\)", "\\(9\\)"),
            ("\\(\\ln e^{3}\\)", "\\(3\\)"),
            ("\\(\\log 0{,}01\\)", "\\(-2\\)"),
        ],
        "\\(2^{5} = 32\\). \\(27^{2/3} = (\\sqrt[3]{27})^{2} = 3^{2}\\). \\(\\ln\\) en \\(e\\) heffen elkaar op. \\(10^{-2} = 0{,}01\\).",
        kolommen=["\\(-2\\)", "\\(3\\)", "\\(5\\)", "\\(9\\)"]),
    casus(
        "Los op in \\(\\mathbb{R}\\): \\(\\ln x + \\ln(x - 1) = \\ln 6\\).",
        [
            keuze(
                "De bestaansvoorwaarde is [[*\\(x > 1\\)|\\(x > 0\\)|\\(x > 6\\)]]. Na het samennemen krijg je de vergelijking [[*\\(x^{2} - x - 6 = 0\\)|\\(2x - 1 = 6\\)|\\(x^{2} - x + 6 = 0\\)]].",
                "Beide logaritmen moeten bestaan, dus \\(x > 0\\) en \\(x > 1\\): samen \\(x > 1\\). \\(\\ln x + \\ln(x-1) = \\ln\\big(x(x-1)\\big)\\), dus \\(x^{2} - x = 6\\)."),
            inv("Welke oplossing blijft over? Geef enkel het getal.",
                "3",
                "\\(x^{2} - x - 6 = (x - 3)(x + 2) = 0\\). De oplossing \\(-2\\) voldoet niet aan de bestaansvoorwaarde, dus enkel \\(x = 3\\)."),
        ],
    ),

    # Veeltermen
    inv("Wat is de rest bij de deling van \\(x^{3} - 2x^{2} + 4\\) door \\(x - 3\\)? Geef enkel het getal.",
        "13",
        "Volgens de reststelling is de rest \\(P(3) = 27 - 18 + 4 = 13\\)."),
    keuze(
        "Voor \\(P(x) = x^{3} - 3x^{2} + 4\\) geldt \\(P(2) =\\) [[*\\(0\\)|\\(4\\)|\\(8\\)]]. Dus is \\(P(x)\\) deelbaar door [[*\\(x - 2\\)|\\(x + 2\\)|\\(x - 4\\)]].",
        "\\(P(2) = 8 - 12 + 4 = 0\\). Als \\(P(a) = 0\\), dan is \\(P(x)\\) deelbaar door \\(x - a\\)."),

    # Ongelijkheden
    mk("Wat is de oplossingsverzameling van \\(x^{2} - x - 6 \\leq 0\\)?",
       ["\\([-2, 3]\\)", "\\(]-\\infty, -2] \\cup [3, +\\infty[\\)", "\\([-3, 2]\\)", "\\(]-2, 3[\\)"],
       0,
       "De nulwaarden zijn \\(-2\\) en \\(3\\). Het is een dalparabool, dus ze is negatief tussen de nulwaarden. Omdat het teken \\(\\leq\\) is, horen de nulwaarden er ook bij."),

    # Exponentiële groei
    inv("Je zet \\(1000\\) euro op een rekening met \\(4\\) procent samengestelde intrest per jaar. Hoeveel euro staat er na \\(10\\) jaar op? Rond af op de cent.",
        ["1480,24", "1480.24", "1 480,24"],
        "De groeifactor is \\(1{,}04\\): \\(1000 \\cdot 1{,}04^{10} \\approx 1480{,}24\\) euro."),

    # Goniometrie
    mk("Wat zijn de oplossingen van \\(\\sin x = \\tfrac{1}{2}\\) in \\([0, 2\\pi[\\)?",
       ["\\(\\tfrac{\\pi}{6}\\) en \\(\\tfrac{5\\pi}{6}\\)", "\\(\\tfrac{\\pi}{3}\\) en \\(\\tfrac{2\\pi}{3}\\)", "\\(\\tfrac{\\pi}{6}\\) en \\(\\tfrac{11\\pi}{6}\\)", "\\(\\tfrac{\\pi}{3}\\) en \\(\\tfrac{5\\pi}{3}\\)"],
       0,
       "\\(\\sin \\tfrac{\\pi}{6} = \\tfrac{1}{2}\\). Supplementaire hoeken hebben dezelfde sinus, dus ook \\(\\pi - \\tfrac{\\pi}{6} = \\tfrac{5\\pi}{6}\\)."),
    tabel(
        "Bekijk \\(y = 3\\sin(2x - \\pi) + 1\\). Vul in.",
        [
            ("de amplitude", "\\(3\\)"),
            ("de periode", "\\(\\pi\\)"),
            ("de evenwichtslijn", "\\(y = 1\\)"),
        ],
        "In \\(y = a\\sin(bx - c) + d\\) is \\(|a|\\) de amplitude, \\(\\tfrac{2\\pi}{b}\\) de periode en \\(y = d\\) de evenwichtslijn. Hier: 3, \\(\\tfrac{2\\pi}{2} = \\pi\\) en \\(y = 1\\).",
        kolommen=["\\(3\\)", "\\(\\pi\\)", "\\(y = 1\\)"]),

    # Limieten en asymptoten
    tabel(
        "Bereken de limiet.",
        [
            ("\\(\\lim\\limits_{x \\to +\\infty} \\dfrac{3x^{2} + 1}{x^{2} - 4}\\)", "\\(3\\)"),
            ("\\(\\lim\\limits_{x \\to 2} \\dfrac{x^{2} - 4}{x - 2}\\)", "\\(4\\)"),
            ("\\(\\lim\\limits_{x \\to +\\infty} \\dfrac{5x}{x^{2} + 1}\\)", "\\(0\\)"),
        ],
        "Bij gelijke graad naar oneindig deel je de hoogstegraadscoëfficiënten: 3. Bij \\(\\tfrac{0}{0}\\) ontbind je: \\(\\tfrac{(x-2)(x+2)}{x-2} = x + 2 \\to 4\\). Is de graad van de noemer groter, dan is de limiet 0.",
        kolommen=["\\(0\\)", "\\(3\\)", "\\(4\\)"]),
    keuze(
        "De functie \\(f(x) = \\dfrac{2x + 1}{x - 3}\\) heeft een verticale asymptoot [[*\\(x = 3\\)|\\(x = -3\\)|\\(x = 2\\)]] en een horizontale asymptoot [[*\\(y = 2\\)|\\(y = 1\\)|\\(y = 3\\)]].",
        "De noemer is nul voor \\(x = 3\\), terwijl de teller daar niet nul is. Naar oneindig gaat f naar \\(\\tfrac{2}{1} = 2\\)."),

    # Afgeleiden
    koppel(
        "Koppel elke functie aan haar afgeleide.",
        [
            ["\\(x \\cdot e^{x}\\)", "\\((x + 1)e^{x}\\)"],
            ["\\(\\ln(x^{2} + 1)\\)", "\\(\\dfrac{2x}{x^{2} + 1}\\)"],
            ["\\(\\sin 3x\\)", "\\(3\\cos 3x\\)"],
            ["\\(\\dfrac{1}{x}\\)", "\\(-\\dfrac{1}{x^{2}}\\)"],
        ],
        ["\\(\\cos 3x\\)", "\\(x \\cdot e^{x - 1}\\)"],
        "Productregel: \\(1 \\cdot e^{x} + x \\cdot e^{x}\\). Kettingregel: \\(\\tfrac{1}{x^{2}+1} \\cdot 2x\\) en \\(\\cos 3x \\cdot 3\\). En \\((x^{-1})' = -x^{-2}\\)."),
    casus(
        "Een boer zet tegen een lange muur een rechthoekige weide af met \\(40\\) meter draad. Langs de muur komt geen draad. De twee zijden loodrecht op de muur zijn elk x meter lang.",
        [
            mk("Welke functie geeft de oppervlakte van de weide?",
               ["\\(A(x) = x(40 - 2x)\\)", "\\(A(x) = x(40 - x)\\)", "\\(A(x) = x(20 - x)\\)", "\\(A(x) = 2x(40 - x)\\)"],
               0,
               "Twee zijden van x meter gebruiken \\(2x\\) meter draad. De zijde evenwijdig met de muur is dan \\(40 - 2x\\) meter."),
            inv("Wat is de grootst mogelijke oppervlakte, in vierkante meter? Geef enkel het getal.",
                "200",
                "\\(A'(x) = 40 - 4x = 0\\) geeft \\(x = 10\\). Dan is de andere zijde 20 meter en de oppervlakte \\(10 \\cdot 20 = 200\\) vierkante meter."),
        ],
    ),

    # Rijen
    tabel(
        "Vul in.",
        [
            ("de twintigste term van de rekenkundige rij met \\(u_{1} = 5\\) en \\(d = 3\\)", "\\(62\\)"),
            ("de som van de eerste twintig termen van die rij", "\\(670\\)"),
            ("de vijfde term van de meetkundige rij met \\(u_{1} = 2\\) en \\(q = 3\\)", "\\(162\\)"),
        ],
        "\\(u_{20} = 5 + 19 \\cdot 3 = 62\\). \\(S_{20} = 20 \\cdot \\tfrac{5 + 62}{2} = 670\\). \\(u_{5} = 2 \\cdot 3^{4} = 162\\).",
        kolommen=["\\(62\\)", "\\(162\\)", "\\(670\\)"]),

    # Integralen
    mk("Wat is \\(\\int (6x^{2} - 4x + 1)\\,dx\\)?",
       ["\\(2x^{3} - 2x^{2} + x + C\\)", "\\(12x - 4 + C\\)", "\\(6x^{3} - 4x^{2} + x + C\\)", "\\(2x^{3} - 4x^{2} + C\\)"],
       0,
       "Je primitiveert term per term: \\(\\int 6x^{2}\\,dx = 2x^{3}\\), \\(\\int 4x\\,dx = 2x^{2}\\) en \\(\\int 1\\,dx = x\\)."),
    inv("Bereken \\(\\int_{0}^{\\pi} \\sin x\\,dx\\). Geef enkel het getal.",
        "2",
        "Een primitieve van \\(\\sin x\\) is \\(-\\cos x\\): \\(-\\cos \\pi + \\cos 0 = 1 + 1 = 2\\)."),

    # Complexe getallen
    mk("Hoeveel is \\((2 + 3i)(1 - i)\\)?",
       ["\\(5 + i\\)", "\\(-1 + i\\)", "\\(5 - i\\)", "\\(2 - 3i\\)"],
       0,
       "\\(2 - 2i + 3i - 3i^{2} = 2 + i + 3 = 5 + i\\), want \\(i^{2} = -1\\)."),

    # Tellen en kansen
    tabel(
        "Op hoeveel manieren kan dit?",
        [
            ("vijf lopers op een rij zetten", "\\(120\\)"),
            ("uit vijf lopers een eerste, tweede en derde plaats verdelen", "\\(60\\)"),
            ("uit vijf lopers een groepje van drie kiezen", "\\(10\\)"),
        ],
        "Een rij van vijf is een permutatie: \\(5! = 120\\). Bij de podiumplaatsen telt de volgorde (variatie): \\(5 \\cdot 4 \\cdot 3 = 60\\). Bij een groepje telt ze niet (combinatie): \\(\\binom{5}{3} = 10\\).",
        kolommen=["\\(10\\)", "\\(60\\)", "\\(120\\)"]),
    inv("Wat is de coëfficiënt van \\(x^{2}\\) in de uitwerking van \\((x + 2)^{5}\\)? Geef enkel het getal.",
        "80",
        "De term met \\(x^{2}\\) is \\(\\binom{5}{2} x^{2} \\cdot 2^{3} = 10 \\cdot 8 \\cdot x^{2} = 80x^{2}\\)."),
    casus(
        "In een klas van \\(30\\) leerlingen sporten er \\(18\\) bij een club, spelen er \\(12\\) een instrument en doen er \\(6\\) allebei. Je kiest willekeurig een leerling.",
        [
            inv("Hoe groot is de kans dat die leerling sport of een instrument speelt? Geef een decimaal getal.",
                ["0,8", "0.8", "4/5"],
                "\\(P(S \\cup M) = P(S) + P(M) - P(S \\cap M) = \\tfrac{18 + 12 - 6}{30} = \\tfrac{24}{30} = 0{,}8\\)."),
            mk("De leerling blijkt te sporten. Hoe groot is dan de kans dat hij ook een instrument speelt?",
               ["\\(\\tfrac{1}{3}\\)", "\\(\\tfrac{1}{5}\\)", "\\(\\tfrac{1}{2}\\)", "\\(\\tfrac{2}{5}\\)"],
               0,
               "\\(P(M \\mid S) = \\dfrac{P(M \\cap S)}{P(S)} = \\dfrac{6}{18} = \\tfrac{1}{3}\\)."),
        ],
    ),
    keuze(
        "Bij een hypothesetoets verwerp je \\(H_{0}\\) als de p-waarde [[*kleiner|groter]] is dan het significantieniveau. Verwerp je \\(H_{0}\\) terwijl ze eigenlijk waar is, dan maak je een [[*type I-fout|type II-fout]].",
        "Een kleine p-waarde betekent dat je resultaat erg onwaarschijnlijk is als \\(H_{0}\\) klopt. Een terechte \\(H_{0}\\) onterecht verwerpen is een type I-fout."),

    # Matrices en stelsels
    mk("A is een \\(2 \\times 3\\)-matrix en B een \\(3 \\times 4\\)-matrix. Welke dimensie heeft \\(A \\cdot B\\)?",
       ["\\(2 \\times 4\\)", "\\(3 \\times 3\\)", "\\(4 \\times 2\\)", "\\(2 \\times 3\\)"],
       0,
       "Het product bestaat omdat A drie kolommen en B drie rijen heeft. Het resultaat neemt de rijen van A en de kolommen van B over."),
    inv("Bereken de determinant van \\(\\begin{pmatrix} 1 & 2 & 0 \\\\ 0 & 1 & 3 \\\\ 2 & 0 & 1 \\end{pmatrix}\\). Geef enkel het getal.",
        "13",
        "Ontwikkel naar de eerste rij: \\(1 \\cdot (1 \\cdot 1 - 3 \\cdot 0) - 2 \\cdot (0 \\cdot 1 - 3 \\cdot 2) + 0 = 1 + 12 = 13\\)."),
    tabel(
        "Los het stelsel op: \\(x + y + z = 6\\), \\(y = 2x\\) en \\(z = 3x\\).",
        [
            ("x", "\\(1\\)"),
            ("y", "\\(2\\)"),
            ("z", "\\(3\\)"),
        ],
        "Vul y en z in de eerste vergelijking in: \\(x + 2x + 3x = 6\\), dus \\(x = 1\\), \\(y = 2\\) en \\(z = 3\\).",
        kolommen=["\\(1\\)", "\\(2\\)", "\\(3\\)"]),

    # Groepen
    tabel(
        "Is dit een groep?",
        [
            ("\\((\\mathbb{Z}, +)\\)", J),
            ("\\((\\mathbb{N}, +)\\)", F),
            ("\\((\\mathbb{Q} \\setminus \\{0\\}, \\cdot)\\)", J),
            ("\\((\\mathbb{Z}, \\cdot)\\)", F),
        ],
        "In \\((\\mathbb{N}, +)\\) heeft bijvoorbeeld 3 geen tegengestelde in \\(\\mathbb{N}\\). In \\((\\mathbb{Z}, \\cdot)\\) heeft bijvoorbeeld 2 geen invers in \\(\\mathbb{Z}\\). In de andere twee zijn alle groepseigenschappen voldaan."),

    # Ruimtemeetkunde
    keuze(
        "Voor \\(\\vec{u} = (1, 2, 2)\\) en \\(\\vec{v} = (2, -1, 0)\\) is \\(|\\vec{u}| =\\) [[*\\(3\\)|\\(5\\)|\\(9\\)]] en \\(\\vec{u} \\cdot \\vec{v} =\\) [[*\\(0\\)|\\(4\\)|\\(-2\\)]]. De twee vectoren staan dus [[*loodrecht op elkaar|evenwijdig]].",
        "\\(|\\vec{u}| = \\sqrt{1 + 4 + 4} = 3\\). Het scalair product is \\(2 - 2 + 0 = 0\\), en een scalair product nul betekent loodrecht."),
    mk("Wat is een normaalvector van het vlak \\(2x - y + 2z = 5\\)?",
       ["\\((2, -1, 2)\\)", "\\((2, 1, 2)\\)", "\\((1, 2, 0)\\)", "\\((2, -1, 5)\\)"],
       0,
       "De coëfficiënten van x, y en z in de cartesische vergelijking vormen een normaalvector."),

    # Programmeren
    inv("Een programma zet \\(\\texttt{s = 0}\\). Daarna voert het voor \\(\\texttt{i}\\) gelijk aan 1, 2, 3 en 4 telkens \\(\\texttt{s = s + i * i}\\) uit. Welke waarde heeft \\(\\texttt{s}\\) op het einde?",
        "30",
        "De lus telt de kwadraten op: \\(1 + 4 + 9 + 16 = 30\\)."),

    # Open vraag
    open_("Toon met de eerste afgeleide aan dat \\(f(x) = x^{3} - 3x\\) in \\(x = -1\\) een lokaal maximum heeft. Schrijf je redenering in stappen.",
          "\\(f'(x) = 3x^{2} - 3 = 3(x - 1)(x + 1)\\). De nulwaarden zijn \\(-1\\) en \\(1\\). Voor \\(x < -1\\) is \\(f'(x) > 0\\), dus f stijgt. Tussen \\(-1\\) en \\(1\\) is \\(f'(x) < 0\\), dus f daalt. In \\(x = -1\\) gaat f van stijgen over naar dalen: daar is een lokaal maximum, met \\(f(-1) = 2\\).",
          "Een goed antwoord berekent de afgeleide, zoekt haar nulwaarden, maakt een tekenschema en besluit uit de tekenwissel van plus naar min."),
]
