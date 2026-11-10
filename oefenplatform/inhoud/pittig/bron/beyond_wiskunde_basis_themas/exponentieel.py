"""Exponentiële functies en groeimodellen — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

# A: y = 2^x, B: y = 3·(1/2)^x − 1 (asymptoot y = −1)
E_GRAF = venster("exponentieel-ab", -4, 5, -3, 9)
# Afkoeling: T(t) = 20 + 70·0,9^t (°C, minuten)
K_GRAF = venster("exponentieel-afkoeling", 0, 40, 0, 100, 5, 10)


def _a(x):
    return 2 ** x


def _b(x):
    return 3 * 0.5 ** x - 1


def _k(t):
    return 20 + 70 * 0.9 ** t


GRAFIEKEN = [
    dict(naam=E_GRAF, titel="Twee exponentiële functies", krommen=[(_a, "groen", "A", (-4, 3.17)), (_b, "blauw", "B", (-1.7, 5))],
         stippel=[("h", -1)], labelplek={"A": (3.0, 8.0), "B": (4.6, -0.9)}),
    dict(naam=K_GRAF, titel="Temperatuur T (°C) van een kop thee, t minuten na het inschenken",
         krommen=[(_k, "oranje", "", (0, 40))], stippel=[("h", 20)], xlabel="t", ylabel="T", ijk_x=5, ijk_y=10),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen en vragen over exponentiële functies") for g in GRAFIEKEN]

VRAGEN = [
    klik(
        "Klik op het punt dat op de grafiek van elke functie y = aˣ ligt, en dus ook op A.",
        f"{E_GRAF}.svg",
        [punt_zone(E_GRAF, 0, 1, 20)],
        r"\(a^{0} = 1\) voor elk grondtal: elke grafiek \(y = a^{x}\) gaat door \((0, 1)\).",
    ),
    klik(
        "Klik op het snijpunt van grafiek B met de y-as.",
        f"{E_GRAF}.svg",
        [punt_zone(E_GRAF, 0, 2, 20)],
        r"\(3 \cdot \left(\frac{1}{2}\right)^{0} - 1 = 3 - 1 = 2\). Het snijpunt is \((0, 2)\).",
    ),
    met_prent(f"{E_GRAF}.svg", tabel(
        "Juist of fout over de grafieken A en B?",
        [
            ("A stijgt over heel haar domein.", J),
            ("B heeft als horizontale asymptoot y = −1.", J),
            ("Het bereik van B is ]0, +∞[.", F),
            ("A en B snijden elkaar in precies één punt.", J),
        ],
        r"Door de verticale verschuiving met \(-1\) zakt ook de asymptoot naar \(y = -1\). Het bereik van B is \(]-1, +\infty[\).",
    )),
    met_prent(f"{E_GRAF}.svg", mk(
        "Welk voorschrift hoort bij B?",
        [r"\(y = 3 \cdot \left(\frac{1}{2}\right)^{x} - 1\)", r"\(y = 3 \cdot 2^{x} - 1\)", r"\(y = \left(\frac{1}{2}\right)^{x} + 2\)", r"\(y = -3 \cdot \left(\frac{1}{2}\right)^{x} - 1\)"],
        0,
        r"B daalt, dus het grondtal ligt tussen \(0\) en \(1\). De asymptoot \(y = -1\) geeft \(c = -1\), en in \(x = 0\) is \(b + c = 2\), dus \(b = 3\).",
    )),
    klik(
        "Klik op de plaats waar de thee het snelst afkoelt.",
        f"{K_GRAF}.svg",
        [punt_zone(K_GRAF, 0, 90, 40)],
        "Meteen na het inschenken is de grafiek het steilst. Hoe dichter bij de kamertemperatuur, hoe trager de thee afkoelt.",
    ),
    met_prent(f"{K_GRAF}.svg", mk(
        "Welk kenmerk van de grafiek is de kamertemperatuur?",
        ["De horizontale asymptoot", "De nulwaarde", "Het snijpunt met de y-as", "De verticale asymptoot"],
        0,
        "De thee nadert 20 °C, maar haalt die waarde nooit helemaal: dat is de horizontale asymptoot T = 20.",
    )),
    met_prent(f"{K_GRAF}.svg", mk(
        r"Het voorschrift is \(T(t) = 20 + 70 \cdot 0{,}9^{t}\). Met hoeveel procent daalt het verschil met de kamertemperatuur per minuut?",
        [r"\(10\,\%\)", r"\(90\,\%\)", r"\(0{,}9\,\%\)", r"\(70\,\%\)"],
        0,
        r"De groeifactor is \(0{,}9\): elke minuut blijft \(90\,\%\) van het verschil over, er gaat dus \(10\,\%\) af.",
    )),
    tabel(
        "Lineair of exponentieel groeimodel?",
        [
            ("Een spaarrekening met 2 % samengestelde intrest per jaar", "Exponentieel"),
            ("Een kaars die elk uur 1,5 cm korter wordt", "Lineair"),
            ("Een bacteriekweek die elke 20 minuten verdubbelt", "Exponentieel"),
            ("Een abonnement van 15 euro per maand plus 30 euro instap", "Lineair"),
        ],
        "Lineair: elke tijdseenheid komt er hetzelfde bedrag bij. Exponentieel: elke tijdseenheid wordt er met dezelfde factor vermenigvuldigd.",
        kolommen=["Lineair", "Exponentieel"],
    ),
    mk(
        "Een bedrag groeit met 5 % per jaar. Wat is de groeifactor per maand, afgerond op vier decimalen?",
        [r"\(1{,}0041\)", r"\(1{,}0042\)", r"\(1{,}05\)", r"\(0{,}4167\)"],
        0,
        r"\(1{,}05^{\frac{1}{12}} \approx 1{,}0041\). Gewoon \(5\,\% / 12\) nemen geeft \(1{,}0042\): dat is niet hetzelfde.",
    ),
    inv(
        "Een stad telt 40 000 inwoners en groeit met 2 % per jaar. Hoeveel inwoners zijn er na 3 jaar? Rond af op een geheel getal.",
        "42448",
        r"\(40\,000 \cdot 1{,}02^{3} = 40\,000 \cdot 1{,}061208 = 42\,448{,}32\).",
    ),
    mk(
        "Een radioactieve stof heeft een halveringstijd van 8 dagen. Hoeveel procent is er na 24 dagen nog over?",
        [r"\(12{,}5\,\%\)", r"\(25\,\%\)", r"\(33\,\%\)", r"\(0\,\%\)"],
        0,
        r"\(24\) dagen is \(3\) halveringstijden: \(\left(\frac{1}{2}\right)^{3} = \frac{1}{8} = 12{,}5\,\%\).",
    ),
    mk(
        "Een hoeveelheid verdubbelt elke 5 jaar. Wat is de groeifactor per jaar?",
        [r"\(2^{\frac{1}{5}} \approx 1{,}149\)", r"\(1{,}2\)", r"\(\frac{2}{5} = 0{,}4\)", r"\(2^{5} = 32\)"],
        0,
        r"Na \(5\) jaar is de factor \(a^{5} = 2\), dus \(a = 2^{\frac{1}{5}} \approx 1{,}149\): ongeveer \(14{,}9\,\%\) per jaar.",
    ),
    mk(
        "Een kapitaal groeit met 3 % per jaar. Na hoeveel jaar is het verdubbeld?",
        [r"Ongeveer \(23{,}4\) jaar", r"Ongeveer \(33{,}3\) jaar", r"Ongeveer \(6{,}7\) jaar", r"Precies \(30\) jaar"],
        0,
        r"\(1{,}03^{t} = 2 \Rightarrow t = \frac{\log 2}{\log 1{,}03} \approx 23{,}4\).",
    ),
    koppel(
        "Koppel de transformatie van y = 2ˣ aan het voorschrift.",
        [
            ["3 eenheden naar boven", r"\(y = 2^{x} + 3\)"],
            ["Spiegelen rond de x-as", r"\(y = -2^{x}\)"],
            ["Verticaal uitrekken met factor 3", r"\(y = 3 \cdot 2^{x}\)"],
        ],
        [r"\(y = 2^{x + 3}\)", r"\(y = 2^{3x}\)"],
        "Bij b · aˣ + c is b de verticale uitrekking (negatief: ook spiegelen) en c de verticale verschuiving.",
    ),
    tabel(
        r"Wat zijn de kenmerken van \(f(x) = -2 \cdot 3^{x} + 5\)?",
        [
            ("Horizontale asymptoot", "y = 5"),
            ("Bereik", "]−∞, 5["),
            ("Stijgen of dalen", "Dalend"),
        ],
        r"\(3^{x}\) stijgt, maar de factor \(-2\) spiegelt de grafiek: ze daalt. Ze blijft onder de asymptoot \(y = 5\).",
        kolommen=["y = 5", "]−∞, 5[", "Dalend"],
    ),
    sorteer(
        "Stijgende of dalende functie?",
        ["Stijgend", "Dalend"],
        [
            [r"\(y = 0{,}8^{x}\)", "Dalend"],
            [r"\(y = 5 \cdot 1{,}1^{x}\)", "Stijgend"],
            [r"\(y = -1{,}5^{x}\)", "Dalend"],
            [r"\(y = -0{,}5^{x} + 2\)", "Stijgend"],
        ],
        "Een grondtal groter dan 1 stijgt, tussen 0 en 1 daalt. Een minteken ervoor keert dat om.",
    ),
    mk(
        r"Een exponentiële functie \(y = b \cdot a^{x}\) gaat door \((0, 5)\) en \((2, 45)\). Wat is \(a\)?",
        [r"\(3\)", r"\(9\)", r"\(20\)", r"\(\sqrt{45}\)"],
        0,
        r"\((0, 5)\) geeft \(b = 5\). Dan \(5a^{2} = 45 \Rightarrow a^{2} = 9 \Rightarrow a = 3\) (een grondtal is positief).",
    ),
    keuze(
        "Bij een groeipercentage van −15 % per jaar is de groeifactor [[*0,85|1,15|−0,15]]. Na twee jaar is er nog [[*72,25 %|70 %|85 %]] over.",
        "0,85 · 0,85 = 0,7225: je trekt niet gewoon twee keer 15 % af.",
    ),
    inv(
        "Een auto kost nieuw 25 000 euro en verliest elk jaar 20 % van zijn waarde. Hoeveel euro is hij na 2 jaar waard?",
        "16000",
        r"\(25\,000 \cdot 0{,}8^{2} = 25\,000 \cdot 0{,}64 = 16\,000\) euro.",
    ),
    mk(
        r"Wat gebeurt er met \(y = 4 \cdot 0{,}6^{x}\) als \(x \to +\infty\)?",
        [r"\(y\) nadert \(0\)", r"\(y\) nadert \(4\)", r"\(y\) wordt oneindig groot", r"\(y\) nadert \(0{,}6\)"],
        0,
        r"Machten van \(0{,}6\) worden steeds kleiner: de \(x\)-as is de horizontale asymptoot.",
    ),
    tabel(
        "Juist of fout over exponentiële groei?",
        [
            ("Bij exponentiële groei is de toename per jaar elk jaar even groot.", F),
            ("Een exponentiële groei met groeifactor groter dan 1 wordt uiteindelijk groter dan elke lineaire groei.", J),
            ("Een groeifactor van 1 betekent dat de hoeveelheid gelijk blijft.", J),
        ],
        "Exponentiële groei vermenigvuldigt telkens met dezelfde factor, dus de toename wordt steeds groter.",
    ),
    volgorde(
        "Je berekent na hoeveel tijd een hoeveelheid van 500 g, die 12 % per uur afneemt, onder 100 g zakt. Zet de stappen in de juiste volgorde.",
        [
            r"Groeifactor bepalen: \(0{,}88\)",
            r"Vergelijking opstellen: \(500 \cdot 0{,}88^{t} = 100\)",
            r"Delen door \(500\): \(0{,}88^{t} = 0{,}2\)",
            r"Logaritme nemen: \(t = \frac{\log 0{,}2}{\log 0{,}88} \approx 12{,}6\) uur",
        ],
        "Eerst de factor, dan de vergelijking, dan de exponent vrijmaken met een logaritme.",
    ),
    sleep(
        "In het model N(t) = N₀ · aᵗ is N₀ de [[beginwaarde]] en a de [[groeifactor]] per tijdseenheid.",
        ["asymptoot", "periode"],
        "Bij t = 0 is aᵗ = 1, dus N(0) = N₀.",
    ),
    mk(
        "Een medicijn wordt elke 6 uur voor de helft afgebroken. Welk voorschrift geeft de hoeveelheid na t uur, bij een dosis van 400 mg?",
        [r"\(400 \cdot 0{,}5^{\frac{t}{6}}\)", r"\(400 \cdot 0{,}5^{6t}\)", r"\(400 - 6t\)", r"\(400 \cdot 6^{-t}\)"],
        0,
        r"Na \(t\) uur zijn er \(\frac{t}{6}\) halveringstijden voorbij.",
    ),
    mk(
        r"Welk punt ligt zeker op de grafiek van \(y = a^{x}\) (met \(a > 0\), \(a \neq 1\))?",
        [r"\((1, a)\)", r"\((a, 1)\)", r"\((0, a)\)", r"\((1, 0)\)"],
        0,
        r"\(a^{1} = a\), dus \((1, a)\) ligt altijd op de grafiek.",
    ),
    inv(
        r"Een kapitaal van \(2000\) euro staat \(5\) jaar op een rekening met \(3\,\%\) samengestelde intrest per jaar. Hoeveel euro is het dan? Rond af op de cent.",
        "2318,55",
        r"\(2000 \cdot 1{,}03^{5} = 2000 \cdot 1{,}159274\ldots \approx 2318{,}55\) euro.",
    ),
    open_(
        "Een bank belooft 4 % intrest per jaar. Een andere bank belooft 0,33 % per maand. Welke is beter? Leg uit.",
        r"Per jaar geeft de tweede bank \(1{,}0033^{12} \approx 1{,}0403\), dus ongeveer \(4{,}03\,\%\). Dat is iets meer dan \(4\,\%\), dus de tweede bank is (net) beter.",
        "Zet beide om naar dezelfde tijdseenheid.",
    ),
    casus(
        "Een algenplaag bedekt op dag 0 een oppervlakte van 3 m² van een vijver van 300 m². Elke dag wordt de bedekte oppervlakte 1,5 keer zo groot.",
        [
            mk(
                "Welk voorschrift geeft de bedekte oppervlakte A na t dagen?",
                [r"\(A(t) = 3 \cdot 1{,}5^{t}\)", r"\(A(t) = 3 + 1{,}5t\)", r"\(A(t) = 1{,}5 \cdot 3^{t}\)", r"\(A(t) = 300 \cdot 1{,}5^{t}\)"],
                0,
                "Beginwaarde 3, groeifactor 1,5 per dag.",
            ),
            mk(
                "Na hoeveel dagen is de vijver voor het eerst helemaal bedekt?",
                [r"Na \(12\) dagen", r"Na \(11\) dagen", r"Na \(100\) dagen", r"Na \(198\) dagen"],
                0,
                r"\(1{,}5^{t} = 100 \Rightarrow t = \frac{\log 100}{\log 1{,}5} \approx 11{,}4\). Na \(11\) dagen is het nog niet helemaal, na \(12\) dagen wel.",
            ),
            mk(
                "Hoeveel procent groeit de bedekte oppervlakte per dag?",
                [r"\(50\,\%\)", r"\(150\,\%\)", r"\(1{,}5\,\%\)", r"\(15\,\%\)"],
                0,
                r"Groeifactor \(1{,}5 = 1 + 0{,}5\): een groei van \(50\,\%\).",
            ),
        ],
    ),
]
