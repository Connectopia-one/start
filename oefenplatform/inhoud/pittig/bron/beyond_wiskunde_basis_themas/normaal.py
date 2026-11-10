"""De normale verdeling — pittig (🌍 Beyond, wiskunde basis).

Kansen komen uit de vuistregel 68-95-99,7 of staan als uitkomst van een
rekenapp in de vraag, zodat elke vraag zonder toestel na te gaan is.
"""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

D_GRAF = venster("normaal-drie-krommen", 30, 100, 0, 0.09, 5, 0.01)
O_GRAF = venster("normaal-oppervlakte", 30, 150, 0, 0.03, 15, 0.005)


def _n(mu, sigma):
    return lambda x: math.exp(-((x - mu) / sigma) ** 2 / 2) / (sigma * math.sqrt(2 * math.pi))


A, B, C = _n(60, 5), _n(60, 10), _n(75, 5)
T = _n(90, 15)

GRAFIEKEN = [
    dict(naam=D_GRAF, titel="Drie Gausskrommen A, B en C",
         krommen=[(A, "groen", "A", (30, 100)), (B, "blauw", "B", (30, 100)), (C, "oranje", "C", (30, 100))],
         labelplek={"A": (54, A(54)), "B": (42, B(42)), "C": (81, C(81))}, ijk_x=10, ijk_y=0.02, ylabel=""),
    dict(naam=O_GRAF, titel="Testscores, normaal verdeeld",
         vlakken=[(T, 60, 120, "#7a4b8c")],
         krommen=[(T, "paars", "", (30, 150))], ijk_x=15, ijk_y=0.01, ylabel=""),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over Gausskrommen") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Klik op de top van de kromme met de grootste standaardafwijking.",
        f"{D_GRAF}.svg",
        [punt_zone(D_GRAF, 60, B(60), 30)],
        "Een grotere standaardafwijking geeft een bredere kromme. Omdat de oppervlakte altijd 1 is, ligt de top dan lager: kromme B.",
    ),
    met_prent(f"{D_GRAF}.svg", tabel(
        "Juist of fout over de krommen A, B en C?",
        [
            ("A en C hebben dezelfde standaardafwijking.", J),
            ("A en B hebben hetzelfde gemiddelde.", J),
            ("De oppervlakte onder B is groter dan die onder A.", F),
            ("Het gemiddelde van C is kleiner dan dat van A.", F),
        ],
        "A en C hebben dezelfde vorm, enkel verschoven. A en B hebben hun top boven 60. Onder elke Gausskromme is de oppervlakte 1.",
    )),
    met_prent(f"{D_GRAF}.svg", mk(
        "Kromme C heeft standaardafwijking 5. Hoeveel procent van de waarden ligt ongeveer tussen 70 en 80?",
        [r"\(95\) %", r"\(68\) %", r"\(50\) %", r"\(34\) %"],
        1,
        r"De top van C ligt bij \(75\). Van \(70\) tot \(80\) is \(\mu - \sigma\) tot \(\mu + \sigma\).",
    )),
    klik(
        r"De testscores hebben \(\mu = 90\) en \(\sigma = 15\). Klik op de horizontale as waar \(\mu + \sigma\) ligt.",
        f"{O_GRAF}.svg",
        [punt_zone(O_GRAF, 105, 0, 30)],
        r"\(90 + 15 = 105\). Daar ligt ook een buigpunt van de kromme.",
    ),
    met_prent(f"{O_GRAF}.svg", mk(
        r"De testscores hebben \(\mu = 90\) en \(\sigma = 15\). Welke kans stelt de gekleurde oppervlakte ongeveer voor?",
        [r"\(0{,}68\)", r"\(0{,}5\)", r"\(0{,}95\)", r"\(0{,}997\)"],
        2,
        r"Gekleurd is van \(60\) tot \(120\): van \(\mu - 2\sigma\) tot \(\mu + 2\sigma\).",
    )),
    mk(
        r"De lengte van volwassenen in een groep is normaal verdeeld met \(\mu = 170\) cm en \(\sigma = 8\) cm. Hoeveel procent is langer dan 186 cm?",
        [r"\(5\) %", r"\(0{,}15\) %", r"\(16\) %", r"\(2{,}5\) %"],
        3,
        r"\(186 = \mu + 2\sigma\). Buiten \(\mu \pm 2\sigma\) ligt \(5\) %, de helft daarvan aan de rechterkant.",
    ),
    inv(
        r"Een machine vult flessen met \(\mu = 1000\) ml en \(\sigma = 4\) ml (normaal verdeeld). Hoeveel procent van de flessen bevat tussen 996 en 1008 ml? Geef een kommagetal.",
        "81,5",
        r"\(996 = \mu - \sigma\) en \(1008 = \mu + 2\sigma\). De helft van \(68\) % plus de helft van \(95\) %: \(34 + 47{,}5\).",
    ),
    mk(
        r"De levensduur van batterijen is normaal verdeeld met \(\sigma = 20\) uur. De fabrikant wil dat maar \(0{,}15\) % van de batterijen het minder dan 300 uur volhoudt. Welk gemiddelde μ is daarvoor nodig?",
        [r"\(320\) uur", r"\(340\) uur", r"\(360\) uur", r"\(400\) uur"],
        2,
        r"Buiten \(\mu \pm 3\sigma\) ligt \(0{,}3\) %, aan elke kant \(0{,}15\) %. Dus \(\mu - 3 \cdot 20 = 300\).",
    ),
    tabel(
        "Juist of fout over de normale verdeling?",
        [
            (r"Een normale verdeling is symmetrisch rond \(\mu\).", J),
            (r"Een normale verdeling ligt volledig vast door \(\mu\) en \(\sigma\).", J),
            (r"De Gausskromme raakt de horizontale as in \(\mu \pm 3\sigma\).", F),
            (r"De buigpunten van de Gausskromme liggen bij \(\mu \pm 2\sigma\).", F),
        ],
        r"De kromme nadert de as, maar raakt ze nooit. De buigpunten liggen op één standaardafwijking van het gemiddelde.",
    ),
    mk(
        "Welke verdeling is waarschijnlijk niet symmetrisch?",
        [
            "De lengtes van volwassen vrouwen in België",
            "De inkomens van alle inwoners van een land",
            "Het gewicht van zakjes suiker van één machine",
            "De meetfouten van een goed afgestelde weegschaal",
        ],
        1,
        "Inkomens hebben een lange staart naar rechts: weinig mensen verdienen heel veel.",
    ),
    mk(
        r"Een rekentoestel geeft voor 20 metingen \(\bar{x} = 12{,}4\) en \(s = 1{,}8\). Wat zegt \(s\)?",
        [
            r"Dat \(1{,}8\) de kleinste meting is",
            r"Hoe sterk de metingen rond \(12{,}4\) spreiden",
            r"Dat \(1{,}8\) % van de metingen fout is",
            r"Hoeveel metingen er boven \(12{,}4\) liggen",
        ],
        1,
        "De standaardafwijking meet de spreiding rond het gemiddelde.",
    ),
    keuze(
        "Bij een normale verdeling vallen gemiddelde, mediaan en modus [[*samen|uit elkaar|weg]]. Bij een verdeling met een lange staart naar rechts ligt het gemiddelde [[*rechts|links|precies op]] van de mediaan.",
        "Symmetrie houdt de drie samen. Enkele heel grote waarden trekken het gemiddelde naar rechts, de mediaan niet.",
    ),
    sorteer(
        "Is deze grootheid ongeveer normaal verdeeld of niet?",
        ["Ongeveer normaal", "Niet normaal"],
        [
            ["De lengte van 18-jarige jongens", "Ongeveer normaal"],
            ["De wachttijd aan een kassa", "Niet normaal"],
            ["De ogen bij veel worpen met één dobbelsteen", "Niet normaal"],
            ["De schoenmaat van volwassen vrouwen", "Ongeveer normaal"],
            ["Het aantal volgers op sociale media", "Niet normaal"],
            ["Het gewicht van appels van één boom", "Ongeveer normaal"],
        ],
        "Wachttijden en volgers zijn scheef verdeeld, een dobbelsteen geeft elke uitkomst even vaak.",
    ),
    mk(
        "Een histogram is mooi klokvormig met de hoogste staaf bij 50. Wat kan je besluiten?",
        [
            "Alle waarden liggen tussen 40 en 60",
            "Het gemiddelde ligt ongeveer bij 50",
            "De standaardafwijking is 50",
            "Precies de helft van de waarden is 50",
        ],
        1,
        "Bij een symmetrische klokvorm liggen gemiddelde en top ongeveer op dezelfde plaats.",
    ),
    volgorde(
        r"X is normaal verdeeld met \(\mu = 50\) en \(\sigma = 10\). Zet deze kansen van klein naar groot.",
        [r"\(P(X > 70)\)", r"\(P(X > 60)\)", r"\(P(X < 50)\)", r"\(P(40 < X < 70)\)"],
        r"Ongeveer \(0{,}025\), \(0{,}16\), \(0{,}5\) en \(0{,}815\).",
    ),
    koppel(
        "Koppel het symbool aan zijn betekenis.",
        [
            [r"\(\mu\)", "Het gemiddelde van de populatie"],
            [r"\(\sigma\)", "De standaardafwijking van de populatie"],
            [r"\(\bar{x}\)", "Het gemiddelde van een steekproef"],
            [r"\(s\)", "De standaardafwijking van een steekproef"],
        ],
        ["De mediaan van de populatie"],
        "Griekse letters voor de populatie, Latijnse voor de steekproef.",
    ),
    sleep(
        "De grafiek van de dichtheidsfunctie van een normale verdeling heet de [[Gausskromme]]. Een kans is een [[oppervlakte]] onder die kromme, en de totale oppervlakte is [[1]].",
        ["histogram", "helling", "100"],
        "Kans = oppervlakte, en alles samen is zeker: kans 1.",
    ),
    mk(
        "Twee klassen halen gemiddeld 14 op 20. In klas A is de standaardafwijking 1, in klas B 3. Wat betekent dat?",
        [
            "Klas B heeft betere punten",
            "In klas B liggen de punten verder uit elkaar",
            "In klas A haalt iedereen 14",
            "Klas A heeft drie keer zoveel leerlingen",
        ],
        1,
        "Hetzelfde gemiddelde, maar in B zijn er meer heel hoge en heel lage punten.",
    ),
    mk(
        r"X is normaal verdeeld met \(\mu = 170\) en \(\sigma = 8\). Een rekenapp geeft \(P(X < 180) = 0{,}8944\). Hoe groot is \(P(X > 180)\)?",
        [r"\(0{,}8944\)", r"\(0{,}3944\)", r"\(0{,}1056\)", r"\(0{,}0528\)"],
        2,
        r"Complement: \(1 - 0{,}8944\).",
    ),
    inv(
        r"X is normaal verdeeld met \(\mu = 170\) en \(\sigma = 8\). Een rekenapp geeft \(P(160 < X < 180) = 0{,}7887\). Hoeveel procent ligt buiten dat interval? Rond af op één decimaal.",
        "21,1",
        r"\(1 - 0{,}7887 = 0{,}2113\), dus \(21{,}1\) %.",
    ),
    mk(
        r"X is normaal verdeeld met \(\mu = 50\) en \(\sigma = 10\), en \(P(X < 35) = 0{,}0668\). Hoe groot is \(P(X > 65)\)?",
        [r"\(0{,}9332\)", r"\(0{,}1336\)", r"\(0{,}5\)", r"\(0{,}0668\)"],
        3,
        r"\(35\) en \(65\) liggen even ver van \(50\). Door de symmetrie zijn beide staarten even groot.",
    ),
    open_(
        r"Leg uit waarom \(P(X \leq a)\) en \(P(X < a)\) gelijk zijn bij een normale verdeling.",
        r"Een kans is een oppervlakte onder de kromme. De kans op precies één waarde a is de oppervlakte boven één punt: een lijnstuk zonder breedte, dus \(0\). Of je a meetelt of niet, verandert de oppervlakte niet.",
        "Een lijnstuk heeft geen oppervlakte.",
    ),
    mk(
        r"X is normaal verdeeld met \(\mu = 20\) en \(\sigma = 2\). Onder welke waarde ligt ongeveer \(2{,}5\) % van de waarden?",
        [r"\(18\)", r"\(14\)", r"\(16\)", r"\(22\)"],
        2,
        r"\(\mu - 2\sigma = 16\). Onder die grens ligt de helft van \(5\) %.",
    ),
    mk(
        "Een histogram van wachttijden heeft een lange staart naar rechts. Mag je de vuistregel 68-95-99,7 gebruiken?",
        [
            "Ja, die geldt voor elke verdeling",
            "Ja, als de steekproef groot genoeg is",
            "Nee, die geldt enkel bij een ongeveer normale verdeling",
            "Nee, want wachttijden hebben geen gemiddelde",
        ],
        2,
        "De vuistregel steunt op de symmetrische klokvorm.",
    ),
    inv(
        r"Een steekproef bestaat uit de waarden \(4, 6, 7, 8, 10\). Hoeveel is \(\bar{x}\)?",
        "7",
        r"\(\frac{4 + 6 + 7 + 8 + 10}{5} = \frac{35}{5} = 7\).",
    ),
    mk(
        "Welke reeks heeft de grootste standaardafwijking?",
        [r"\(5, 5, 5, 5\)", r"\(4, 5, 6, 5\)", r"\(3, 5, 7, 5\)", r"\(1, 5, 9, 5\)"],
        3,
        r"Alle reeksen hebben gemiddelde \(5\). Bij \(1, 5, 9, 5\) liggen de waarden het verst van dat gemiddelde.",
    ),
    mk(
        "Je meet de lengte van heel veel leerlingen en tekent histogrammen met steeds smallere klassen. Wat zie je?",
        [
            "Het histogram wordt steeds platter",
            "Het histogram gaat steeds meer op een vloeiende klokvorm lijken",
            "Het histogram krijgt twee toppen",
            "Het gemiddelde schuift naar rechts",
        ],
        1,
        "Zo ontstaat het idee van de Gausskromme als dichtheidsfunctie.",
    ),
    casus(
        r"Het gewicht van pakken suiker is normaal verdeeld met \(\mu = 1005\) g en \(\sigma = 3\) g. Op de pakken staat 1000 g. Een rekenapp geeft \(P(X < 1000) = 0{,}0478\).",
        [
            mk(
                "Hoeveel procent van de pakken weegt minder dan op het pak staat?",
                [r"Ongeveer \(0{,}05\) %", r"Ongeveer \(4{,}8\) %", r"Ongeveer \(47{,}8\) %", r"Ongeveer \(95\) %"],
                1,
                r"\(0{,}0478 = 4{,}78\) %.",
            ),
            mk(
                "In een levering zitten 500 pakken. Hoeveel te lichte pakken verwacht je ongeveer?",
                [r"\(5\)", r"\(48\)", r"\(24\)", r"\(2\)"],
                2,
                r"\(500 \cdot 0{,}0478 \approx 24\).",
            ),
            mk(
                "De fabrikant wil minder te lichte pakken. Wat helpt?",
                [
                    "Het opschrift veranderen naar 1005 g",
                    "Het gemiddelde verhogen of nauwkeuriger vullen (kleinere σ)",
                    "De standaardafwijking vergroten",
                    "Meer pakken per levering verkopen",
                ],
                1,
                "Een hoger gemiddelde schuift de kromme weg van 1000 g, een kleinere σ maakt de linkerstaart dunner.",
            ),
        ],
    ),
]
