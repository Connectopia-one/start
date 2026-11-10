"""Tweedegraadsvergelijkingen algebraïsch oplossen — pittig (🌍 Beyond, wiskunde basis; niet voor welzijnswetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

PRENTEN = []

VRAGEN = [
    mk(
        r"Los op: \(3x^{2} = 12x\).",
        [r"\(V = \{0, 4\}\)", r"\(V = \{4\}\)", r"\(V = \{-4, 4\}\)", r"\(V = \{0, -4\}\)"],
        0,
        r"\(3x^{2} - 12x = 0 \Rightarrow 3x(x - 4) = 0\). Wie door \(x\) deelt, verliest de oplossing \(0\).",
    ),
    mk(
        r"Los op: \(2x^{2} - 50 = 0\).",
        [r"\(V = \{-5, 5\}\)", r"\(V = \{5\}\)", r"\(V = \{-25, 25\}\)", r"\(V = \emptyset\)"],
        0,
        r"\(x^{2} = 25\), dus \(x = 5\) of \(x = -5\).",
    ),
    mk(
        r"Los op: \(4x^{2} + 36 = 0\).",
        [r"\(V = \emptyset\)", r"\(V = \{-3, 3\}\)", r"\(V = \{3\}\)", r"\(V = \{-9\}\)"],
        0,
        r"\(x^{2} = -9\) heeft geen reële oplossing: een kwadraat is nooit negatief.",
    ),
    tabel(
        "Hoeveel reële oplossingen heeft de vergelijking?",
        [
            (r"\(x^{2} - 6x + 9 = 0\)", "Eén"),
            (r"\(2x^{2} + x - 3 = 0\)", "Twee"),
            (r"\(x^{2} + 2x + 5 = 0\)", "Geen"),
            (r"\(-x^{2} + 4x - 1 = 0\)", "Twee"),
        ],
        r"\(D = b^{2} - 4ac\): \(0\), \(25\), \(-16\) en \(12\). Positief: twee, nul: één, negatief: geen.",
        kolommen=["Geen", "Eén", "Twee"],
    ),
    inv(
        r"Bereken de discriminant van \(3x^{2} - 5x - 2 = 0\).",
        "49",
        r"\(D = (-5)^{2} - 4 \cdot 3 \cdot (-2) = 25 + 24 = 49\).",
    ),
    mk(
        r"Los op: \(3x^{2} - 5x - 2 = 0\).",
        [r"\(V = \left\{-\frac{1}{3}, 2\right\}\)", r"\(V = \left\{\frac{1}{3}, -2\right\}\)", r"\(V = \{-1, 6\}\)", r"\(V = \left\{-2, \frac{1}{3}\right\}\)"],
        0,
        r"Met \(x = \frac{-b \pm \sqrt{D}}{2a}\) vind je \(x = 2\) of \(x = -\frac{1}{3}\). Controle: \(3 \cdot 4 - 10 - 2 = 0\).",
    ),
    mk(
        r"Voor welke \(k\) heeft \(x^{2} + 6x + k = 0\) precies één oplossing?",
        [r"\(k = 9\)", r"\(k = 36\)", r"\(k = 3\)", r"\(k = -9\)"],
        0,
        r"\(D = 36 - 4k = 0\) geeft \(k = 9\). Dan is \(x^{2} + 6x + 9 = (x + 3)^{2}\).",
    ),
    mk(
        r"Een leerling lost \((x - 2)(x + 5) = 8\) op met: \(x - 2 = 8\) of \(x + 5 = 8\). Wat klopt?",
        [
            r"Fout: zo'n product mag je enkel splitsen als het rechterlid \(0\) is.",
            r"Juist: elke factor moet gelijk zijn aan \(8\).",
            r"Juist, maar enkel omdat \(8\) positief is.",
            r"Fout: je moet eerst door \(x\) delen.",
        ],
        0,
        r"Een product is \(0\) als een factor \(0\) is. Voor \(8\) geldt dat niet: werk eerst uit en breng alles naar één lid.",
    ),
    inv(
        r"Los op: \((x - 2)(x + 5) = 8\). Geef de positieve oplossing.",
        "3",
        r"\(x^{2} + 3x - 10 = 8 \Rightarrow x^{2} + 3x - 18 = 0 \Rightarrow (x + 6)(x - 3) = 0\).",
    ),
    koppel(
        "Koppel de vergelijking aan haar ontbinding in factoren.",
        [
            [r"\(x^{2} - 7x + 12 = 0\)", r"\((x - 3)(x - 4) = 0\)"],
            [r"\(x^{2} + x - 12 = 0\)", r"\((x + 4)(x - 3) = 0\)"],
            [r"\(x^{2} - 16 = 0\)", r"\((x - 4)(x + 4) = 0\)"],
            [r"\(x^{2} - 4x = 0\)", r"\(x(x - 4) = 0\)"],
        ],
        [r"\((x + 3)(x + 4) = 0\)"],
        "Zoek twee getallen met als product c en als som b.",
    ),
    sorteer(
        "Volledige of onvolledige vierkantsvergelijking?",
        ["Volledig", "Onvolledig"],
        [
            [r"\(5x^{2} - 20 = 0\)", "Onvolledig"],
            [r"\(x^{2} + 3x - 1 = 0\)", "Volledig"],
            [r"\(-2x^{2} + 7x = 0\)", "Onvolledig"],
            [r"\(4x^{2} - 4x + 1 = 0\)", "Volledig"],
        ],
        r"Bij een onvolledige vergelijking is \(b = 0\) of \(c = 0\). Die los je op zonder discriminant.",
    ),
    mk(
        r"Waar snijden \(y = x^{2} - 2x\) en \(y = x + 4\) elkaar?",
        [r"In \((4, 8)\) en \((-1, 3)\)", r"In \((4, 0)\) en \((-1, 0)\)", r"In \((-4, 0)\) en \((1, 5)\)", r"Ze snijden elkaar niet."],
        0,
        r"\(x^{2} - 2x = x + 4 \Rightarrow x^{2} - 3x - 4 = 0 \Rightarrow x = 4\) of \(x = -1\). De \(y\)-waarden vind je met \(y = x + 4\).",
    ),
    tabel(
        r"Juist of fout over \(ax^{2} + bx + c = 0\) (met \(a \neq 0\))?",
        [
            (r"Als \(a\) en \(c\) een tegengesteld teken hebben, zijn er zeker twee oplossingen.", J),
            (r"Als \(c = 0\), is \(0\) altijd een oplossing.", J),
            (r"Als \(b = 0\), is er altijd een oplossing.", F),
            (r"Als \(D < 0\), snijdt de parabool \(y = ax^{2} + bx + c\) de \(x\)-as niet.", J),
        ],
        r"Bij tegengestelde tekens is \(-4ac > 0\), dus \(D > 0\). Bij \(b = 0\) kan \(x^{2} = -\frac{c}{a}\) negatief zijn.",
    ),
    mk(
        r"Een vergelijking heeft als oplossingen \(2\) en \(-7\). Welke vergelijking kan het zijn?",
        [r"\(x^{2} + 5x - 14 = 0\)", r"\(x^{2} - 5x - 14 = 0\)", r"\(x^{2} + 5x + 14 = 0\)", r"\(x^{2} - 9x + 14 = 0\)"],
        0,
        r"\((x - 2)(x + 7) = x^{2} + 5x - 14\).",
    ),
    volgorde(
        r"Zet de stappen om \(2x^{2} = 3 - 5x\) op te lossen in de juiste volgorde.",
        [
            r"Alles naar één lid: \(2x^{2} + 5x - 3 = 0\)",
            r"\(a\), \(b\) en \(c\) aflezen: \(2\), \(5\) en \(-3\)",
            r"\(D = 25 + 24 = 49\) berekenen",
            r"\(x = \frac{-5 \pm 7}{4}\): \(x = \frac{1}{2}\) of \(x = -3\)",
        ],
        "Eerst de standaardvorm, dan de coëfficiënten, de discriminant en de formule.",
    ),
    keuze(
        "Als de discriminant nul is, heeft de vergelijking [[*één|twee|geen]] oplossing, en de parabool [[*raakt|snijdt|mist]] de x-as in haar top.",
        "Eén oplossing hoort bij een top op de x-as.",
    ),
    mk(
        r"De nulwaarden van \(f(x) = x^{2} - 4x + c\) liggen \(6\) uit elkaar. Hoeveel is \(c\)?",
        [r"\(-5\)", r"\(5\)", r"\(-12\)", r"\(4\)"],
        0,
        r"De symmetrieas is \(x = 2\), dus de nulwaarden zijn \(2 - 3 = -1\) en \(2 + 3 = 5\). \((x + 1)(x - 5) = x^{2} - 4x - 5\).",
    ),
    inv(
        r"Een getal vermeerderd met zijn kwadraat geeft \(42\). Wat is het positieve getal?",
        "6",
        r"\(x^{2} + x - 42 = 0 \Rightarrow (x + 7)(x - 6) = 0\). Ook \(-7\) voldoet, maar dat is negatief.",
    ),
    mk(
        r"Een rechthoek is \(3\) cm langer dan breed en heeft een oppervlakte van \(40\) cm². Hoe breed is hij?",
        [r"\(5\) cm", r"\(8\) cm", r"\(6{,}3\) cm", r"\(10\) cm"],
        0,
        r"\(x(x + 3) = 40 \Rightarrow x^{2} + 3x - 40 = 0 \Rightarrow (x + 8)(x - 5) = 0\). Een breedte is positief: \(5\) cm.",
    ),
    tabel(
        r"Welke \(x\) is een oplossing van \(x^{2} - x - 6 = 0\)?",
        [
            (r"\(x = 3\)", J),
            (r"\(x = -2\)", J),
            (r"\(x = 2\)", F),
            (r"\(x = -3\)", F),
        ],
        r"Invullen: \(9 - 3 - 6 = 0\) en \(4 + 2 - 6 = 0\). Bij \(2\) en \(-3\) krijg je \(-4\) en \(6\).",
        kolommen=["Oplossing", "Geen oplossing"],
    ),
    mk(
        r"Een bal wordt opgegooid: \(h(t) = -5t^{2} + 20t + 25\) (meter, seconden). Na hoeveel seconden raakt hij de grond?",
        [r"\(5\) s", r"\(2\) s", r"\(25\) s", r"\(1\) s"],
        0,
        r"\(-5t^{2} + 20t + 25 = 0 \Rightarrow t^{2} - 4t - 5 = 0 \Rightarrow t = 5\) of \(t = -1\). Een negatieve tijd past niet bij de situatie.",
    ),
    mk(
        r"Wanneer is dezelfde bal (\(h(t) = -5t^{2} + 20t + 25\)) op \(40\) m hoogte?",
        [r"Na \(1\) s en na \(3\) s", r"Enkel na \(2\) s", r"Na \(3\) s en na \(5\) s", r"Nooit"],
        0,
        r"\(-5t^{2} + 20t + 25 = 40 \Rightarrow t^{2} - 4t + 3 = 0 \Rightarrow t = 1\) of \(t = 3\): eens op weg naar boven, eens op weg naar beneden.",
    ),
    sleep(
        "De getallen die een vergelijking waar maken, zijn de [[oplossingen]]. Samen vormen ze de [[oplossingenverzameling]] V.",
        ["nulpunten", "coëfficiënten"],
        "Bij ax² + bx + c = 0 zijn de oplossingen dezelfde als de nulwaarden van f(x) = ax² + bx + c.",
    ),
    mk(
        r"Hoeveel snijpunten hebben \(y = x^{2} + 1\) en \(y = 2x\)?",
        [r"Eén: ze raken elkaar in \((1, 2)\)", r"Twee", r"Geen", r"Oneindig veel"],
        0,
        r"\(x^{2} - 2x + 1 = 0\) heeft \(D = 0\): één oplossing \(x = 1\).",
    ),
    tabel(
        r"Welke aanpak is het snelst?",
        [
            (r"\(x^{2} = 49\)", "Vierkantswortel nemen"),
            (r"\(x^{2} + 8x = 0\)", "x buiten haakjes"),
            (r"\(3x^{2} - 7x + 1 = 0\)", "Discriminant"),
        ],
        "Bij een onvolledige vergelijking heb je de discriminant niet nodig.",
        kolommen=["Vierkantswortel nemen", "x buiten haakjes", "Discriminant"],
    ),
    mk(
        r"Los op: \((x - 4)^{2} = 9\).",
        [r"\(V = \{1, 7\}\)", r"\(V = \{7\}\)", r"\(V = \{-5, 13\}\)", r"\(V = \{4 - \sqrt{3}, 4 + \sqrt{3}\}\)"],
        0,
        r"\(x - 4 = 3\) of \(x - 4 = -3\), dus \(x = 7\) of \(x = 1\). Vergeet de negatieve wortel niet.",
    ),
    open_(
        r"Leg uit waarom je bij \(x^{2} = 5x\) niet zomaar door \(x\) mag delen.",
        r"Delen door \(x\) mag enkel als \(x \neq 0\). Zo verlies je de oplossing \(x = 0\). Beter: \(x^{2} - 5x = 0 \Rightarrow x(x - 5) = 0\), dus \(V = \{0, 5\}\).",
        "Een factor gelijk aan nul is ook een oplossing.",
    ),
    casus(
        r"Een fotokader heeft een buitenmaat van \(30\) cm op \(20\) cm. De lijst is overal even breed (\(x\) cm). De foto erin heeft een oppervlakte van \(336\) cm².",
        [
            mk(
                "Welke vergelijking past?",
                [r"\((30 - 2x)(20 - 2x) = 336\)", r"\((30 - x)(20 - x) = 336\)", r"\(30 \cdot 20 - 2x = 336\)", r"\((30 + 2x)(20 + 2x) = 336\)"],
                0,
                r"Aan beide kanten gaat er \(x\) af, dus per zijde \(2x\).",
            ),
            mk(
                "Welke oplossingen heeft die vergelijking?",
                [r"\(x = 2\) en \(x = 23\)", r"\(x = 3\) en \(x = 22\)", r"\(x = 4\) en \(x = 21\)", r"\(x = -2\) en \(x = 23\)"],
                0,
                r"\(4x^{2} - 100x + 600 = 336 \Rightarrow x^{2} - 25x + 66 = 0 \Rightarrow (x - 2)(x - 23) = 0\).",
            ),
            mk(
                "Hoe breed is de lijst?",
                [r"\(2\) cm", r"\(23\) cm", r"\(12{,}5\) cm", r"\(4\) cm"],
                0,
                r"Een lijst van \(23\) cm past niet rond een kader van \(20\) cm breed. Enkel \(2\) cm kan.",
            ),
        ],
    ),
]
