"""Stelsels van twee eerstegraadsvergelijkingen — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

GRAF = venster("stelsels-drie-rechten", -2, 6, -3, 8)

GRAFIEKEN = [
    dict(naam=GRAF, titel="De rechten a, b en c",
         krommen=[(lambda x: x + 1, "groen", "a", (-2, 6)), (lambda x: -2 * x + 7, "blauw", "b", (-0.5, 5)), (lambda x: x - 2, "oranje", "c", (-1, 6))],
         labelplek={"a": (5.5, 6.5), "b": (0, 7), "c": (5.6, 3.6)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="drie rechten in een assenstelsel", vragen="klikvragen over stelsels grafisch oplossen")]

VRAGEN = [
    klik(
        "Klik op het punt dat de oplossing toont van het stelsel met de rechten a en b.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 3)],
        r"Het snijpunt van a en b is \((2, 3)\). Dat koppel klopt in beide vergelijkingen.",
    ),
    klik(
        "Klik op het punt dat de oplossing toont van het stelsel met de rechten b en c.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, 1)],
        r"b en c snijden elkaar in \((3, 1)\): \(-2 \cdot 3 + 7 = 1\) en \(3 - 2 = 1\).",
    ),
    met_prent(f"{GRAF}.svg", mk(
        "Hoeveel oplossingen heeft het stelsel met de rechten a en c?",
        ["geen, het stelsel is strijdig", "precies één", "oneindig veel", "twee"],
        0,
        "a en c hebben dezelfde richting en snijden de y-as op een andere plaats: evenwijdige rechten hebben geen snijpunt.",
    )),
    met_prent(f"{GRAF}.svg", koppel(
        "Koppel elke rechte aan haar vergelijking.",
        [["a", r"\(y = x + 1\)"], ["b", r"\(y = -2x + 7\)"], ["c", r"\(y = x - 2\)"]],
        [r"\(y = 2x + 7\)", r"\(y = -x + 1\)"],
        r"a en c stijgen even snel (richtingscoëfficiënt \(1\)) en snijden de \(y\)-as in \(1\) en \(-2\). b daalt en snijdt de \(y\)-as in \(7\).",
    )),
    mk(
        r"Los op: \(\begin{cases} 3x + 2y = 16 \\ x - 2y = 0 \end{cases}\)",
        [r"\((4, 2)\)", r"\((2, 4)\)", r"\((4, -2)\)", r"\((8, 4)\)"],
        0,
        r"Optellen laat \(y\) wegvallen: \(4x = 16\), \(x = 4\). Dan \(4 - 2y = 0\), \(y = 2\). \((2, 4)\) is het koppel in de verkeerde volgorde.",
    ),
    inv(
        r"Los op met substitutie: \(y = 3x - 4\) en \(2x + y = 11\). Wat is \(y\)?",
        ["5"],
        r"\(2x + 3x - 4 = 11\) geeft \(x = 3\), dan \(y = 9 - 4 = 5\).",
    ),
    tabel(
        "Hoeveel oplossingen heeft dit stelsel?",
        [
            (r"\(x + 2y = 4\) en \(2x + 4y = 8\)", "oneindig veel"),
            (r"\(x + 2y = 4\) en \(2x + 4y = 6\)", "geen"),
            (r"\(x + 2y = 4\) en \(x - 2y = 4\)", "één"),
            (r"\(y = 3x\) en \(y = 3x + 1\)", "geen"),
            (r"\(y = 3x\) en \(y = -3x\)", "één"),
        ],
        r"Is de tweede vergelijking een veelvoud van de eerste, dan vallen de rechten samen. Is enkel het linkerlid een veelvoud, dan zijn ze evenwijdig. Anders snijden ze in één punt.",
        kolommen=["geen", "één", "oneindig veel"],
    ),
    casus(
        r"In een bioscoop kost een ticket voor een volwassene \(12\) euro en voor een kind \(8\) euro. Een groep van \(15\) personen betaalt samen \(148\) euro.",
        [
            mk(
                r"Welk stelsel hoort bij deze situatie, met \(v\) volwassenen en \(k\) kinderen?",
                [
                    r"\(v + k = 148\) en \(12v + 8k = 15\)",
                    r"\(v + k = 15\) en \(12v + 8k = 148\)",
                    r"\(v + k = 15\) en \(8v + 12k = 148\)",
                    r"\(v - k = 15\) en \(12v + 8k = 148\)",
                ],
                1,
                "Eén vergelijking telt de personen, de andere telt het geld.",
            ),
            inv(
                "Hoeveel kinderen zijn er in de groep?",
                ["8", "8 kinderen"],
                r"\(v = 15 - k\) invullen: \(12(15 - k) + 8k = 148\), dus \(180 - 4k = 148\) en \(k = 8\). Er zijn \(7\) volwassenen.",
            ),
        ],
    ),
    volgorde(
        r"Je lost \(\begin{cases} 2x + 3y = 12 \\ 5x - 3y = 9 \end{cases}\) op met de combinatiemethode. Zet de stappen in volgorde.",
        [
            r"de vergelijkingen optellen: \(7x = 21\)",
            r"\(x = 3\) berekenen",
            r"\(x = 3\) invullen in de eerste: \(6 + 3y = 12\)",
            r"\(y = 2\) berekenen",
            r"\((3, 2)\) controleren in de tweede: \(15 - 6 = 9\)",
        ],
        r"Omdat \(3y\) en \(-3y\) tegengesteld zijn, valt \(y\) weg bij het optellen. Controleren doe je in de vergelijking die je nog niet gebruikte.",
    ),
    casus(
        r"Je lost het stelsel \(\begin{cases} 3x + 2y = 7 \\ 4x - 5y = -6 \end{cases}\) op.",
        [
            mk(
                r"Je wil \(y\) laten wegvallen. Waarmee vermenigvuldig je de vergelijkingen?",
                [
                    r"de eerste met \(5\) en de tweede met \(2\), dan optellen",
                    r"de eerste met \(4\) en de tweede met \(3\), dan optellen",
                    r"de eerste met \(2\) en de tweede met \(5\), dan aftrekken",
                    r"de eerste met \(5\) en de tweede met \(-2\), dan optellen",
                ],
                0,
                r"Dan krijg je \(10y\) en \(-10y\), en die vallen weg bij het optellen.",
            ),
            inv(
                r"Wat is \(y\)?",
                ["2"],
                r"\(15x + 10y = 35\) en \(8x - 10y = -12\) optellen: \(23x = 23\), \(x = 1\). Dan \(3 + 2y = 7\), \(y = 2\).",
            ),
        ],
    ),
    keuze(
        r"Je werkt een stelsel uit en vindt \(0 = 0\). Dan zijn de rechten [[*samenvallend|evenwijdig|snijdend]] en heeft het stelsel [[*oneindig veel oplossingen|geen oplossing|één oplossing]]. Vind je \(0 = 4\), dan is het stelsel [[*strijdig|onbepaald|bepaald]].",
        r"\(0 = 0\) klopt altijd: elk punt van de ene rechte ligt op de andere. \(0 = 4\) klopt nooit.",
    ),
    mk(
        r"Voor welke waarde van \(a\) heeft het stelsel \(y = ax + 3\) en \(y = 2x - 1\) geen oplossing?",
        [r"\(a = 3\)", r"\(a = 2\)", r"\(a = -2\)", r"\(a = -1\)"],
        1,
        r"Geen oplossing betekent evenwijdige rechten: dezelfde richtingscoëfficiënt en een ander snijpunt met de \(y\)-as. Dat is zo bij \(a = 2\), want \(3 \neq -1\).",
    ),
    casus(
        r"Een boer heeft kippen en konijnen. Samen hebben ze \(35\) koppen en \(94\) poten.",
        [
            sleep(
                r"Met \(k\) kippen en \(r\) konijnen tel je de koppen met [[\(k + r = 35\)]] en de poten met [[\(2k + 4r = 94\)]].",
                [r"\(4k + 2r = 94\)", r"\(k + r = 94\)"],
                "Elk dier heeft één kop. Een kip heeft 2 poten, een konijn 4.",
            ),
            inv(
                "Hoeveel konijnen heeft de boer?",
                ["12", "12 konijnen"],
                r"\(k = 35 - r\) invullen: \(70 - 2r + 4r = 94\), dus \(2r = 24\) en \(r = 12\). Er zijn \(23\) kippen.",
            ),
        ],
    ),
    tabel(
        "Juist of fout over stelsels?",
        [
            ("Een stelsel van twee eerstegraadsvergelijkingen kan precies twee oplossingen hebben.", F),
            ("Grafisch oplossen geeft soms maar een benadering.", J),
            ("Bij substitutie moet je altijd x eerst afzonderen.", F),
            ("Een koppel is pas een oplossing als het in beide vergelijkingen klopt.", J),
        ],
        "Twee rechten snijden in nul, één of oneindig veel punten, nooit in precies twee. Een snijpunt op een tekening lees je niet altijd exact af. Je kiest zelf welke onbekende je afzondert.",
    ),
    mk(
        r"Twee getallen hebben als som \(50\) en als verschil \(14\). Wat is het kleinste getal?",
        [r"\(36\)", r"\(18\)", r"\(32\)", r"\(22\)"],
        1,
        r"\(x + y = 50\) en \(x - y = 14\) optellen: \(2x = 64\), \(x = 32\) en \(y = 18\).",
    ),
    mk(
        r"Een gsm-abonnement A kost \(10\) euro per maand plus \(0{,}05\) euro per sms. Abonnement B kost \(15\) euro en sms'en zijn gratis. Bij hoeveel sms'en per maand kosten ze evenveel?",
        [r"\(50\)", r"\(100\)", r"\(250\)", r"\(500\)"],
        1,
        r"\(10 + 0{,}05s = 15\) geeft \(0{,}05s = 5\), dus \(s = 100\).",
    ),
    sorteer(
        r"Is het koppel een oplossing van \(\begin{cases} x + y = 6 \\ 2x - y = 3 \end{cases}\), van één van de twee vergelijkingen, of van geen enkele?",
        ["van het stelsel", "enkel van één vergelijking", "van geen enkele"],
        [
            [r"\((3, 3)\)", "van het stelsel"],
            [r"\((4, 2)\)", "enkel van één vergelijking"],
            [r"\((2, 1)\)", "enkel van één vergelijking"],
            [r"\((0, 0)\)", "van geen enkele"],
        ],
        r"\((3, 3)\): \(6\) en \(3\), allebei juist. \((4, 2)\): som \(6\), maar \(8 - 2 = 6\). \((2, 1)\): som \(3\), maar \(4 - 1 = 3\). \((0, 0)\) past nergens.",
    ),
    mk(
        r"Een snoepwinkel mengt snoep van \(8\) euro per kg met snoep van \(14\) euro per kg tot \(6\) kg mengsel van \(10\) euro per kg. Hoeveel kg goedkoop snoep gaat erin?",
        [r"\(2\) kg", r"\(3\) kg", r"\(4\) kg", r"\(5\) kg"],
        2,
        r"\(g + d = 6\) en \(8g + 14d = 60\). Met \(d = 6 - g\): \(8g + 84 - 14g = 60\), dus \(g = 4\) kg.",
    ),
    open_(
        r"Leg uit waarom het stelsel \(\begin{cases} x + y = 5 \\ 3x + 3y = 12 \end{cases}\) geen oplossing heeft, zonder het volledig uit te werken.",
        r"Deel de tweede vergelijking door \(3\): \(x + y = 4\). Dezelfde som \(x + y\) kan niet tegelijk \(5\) en \(4\) zijn. Grafisch zijn het twee evenwijdige rechten.",
    ),
    mk(
        r"Los op: \(\begin{cases} y = 2x + 1 \\ y = -x + 7 \end{cases}\)",
        [r"\((2, 5)\)", r"\((5, 2)\)", r"\((3, 4)\)", r"\((2, 3)\)"],
        0,
        r"Gelijkstellen: \(2x + 1 = -x + 7\), dus \(x = 2\) en \(y = 5\). Controle in de tweede: \(-2 + 7 = 5\).",
    ),
    inv(
        r"Een rechthoek heeft een omtrek van \(46\) cm. De lengte is \(5\) cm meer dan de breedte. Hoe groot is de oppervlakte, in cm²?",
        ["126", "126 cm²"],
        r"\(2l + 2b = 46\) en \(l = b + 5\): \(4b + 10 = 46\), \(b = 9\) en \(l = 14\). Oppervlakte \(126\) cm².",
    ),
    koppel(
        "Koppel elk stelsel aan de methode die hier het snelst werkt.",
        [
            [r"\(y = 4x\) en \(3x + y = 14\)", "substitutie"],
            [r"\(y = x + 2\) en \(y = 3x - 4\)", "gelijkstelling"],
            [r"\(2x + y = 9\) en \(5x - y = 5\)", "combinatie"],
        ],
        ["proberen"],
        "Staat één onbekende al alleen, dan substitueer je. Staat dezelfde onbekende in beide alleen, dan stel je gelijk. Hebben de termen tegengestelde coëfficiënten, dan tel je op.",
    ),
    mk(
        r"Een stelsel heeft als oplossing \((1, -2)\). Welk stelsel kan dat zijn?",
        [
            r"\(x + y = -1\) en \(2x - y = 4\)",
            r"\(x + y = 3\) en \(x - y = -1\)",
            r"\(x - y = -1\) en \(2x + y = 0\)",
            r"\(x + y = -1\) en \(2x + y = 4\)",
        ],
        0,
        r"Invullen: \(1 - 2 = -1\) en \(2 + 2 = 4\). Bij de laatste optie klopt de tweede niet: \(2 - 2 = 0\).",
    ),
    inv(
        r"Los op met gelijkstelling: \(x = 2y + 1\) en \(x = 5y - 8\). Wat is \(x\)?",
        ["7"],
        r"\(2y + 1 = 5y - 8\) geeft \(y = 3\), dan \(x = 7\).",
    ),
    mk(
        r"Het stelsel \(ax + y = 5\) en \(2x + y = 3\) heeft als oplossing een koppel met \(x = 1\). Hoeveel is \(a\)?",
        [r"\(2\)", r"\(3\)", r"\(4\)", r"\(6\)"],
        2,
        r"Uit de tweede vergelijking: \(2 + y = 3\), dus \(y = 1\). In de eerste: \(a + 1 = 5\), dus \(a = 4\).",
    ),
    inv(
        r"Drie nachten in een tweepersoonskamer en twee nachten in een eenpersoonskamer kosten samen \(410\) euro. Eén nacht in een tweepersoonskamer en vier nachten in een eenpersoonskamer kosten \(370\) euro. Hoeveel kost een nacht in een eenpersoonskamer, in euro?",
        ["70", "70 euro"],
        r"\(3t + 2e = 410\) en \(t + 4e = 370\). Met \(t = 370 - 4e\): \(1110 - 12e + 2e = 410\), dus \(e = 70\) en \(t = 90\).",
    ),
    mk(
        r"Hoeveel oplossingen heeft het stelsel \(y = 2x + 3\) en \(4x - 2y = -6\)?",
        ["geen", "precies één", "oneindig veel", "precies twee"],
        2,
        r"Deel de tweede door \(-2\): \(-2x + y = 3\), of \(y = 2x + 3\). Het is dezelfde rechte.",
    ),
]
