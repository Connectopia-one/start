"""Formules omvormen en eerstegraadsvergelijkingen — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

GRAF = venster("formules-twee-rechten", -2, 7, -3, 8)


def _f(x):
    return 2 * x - 1


def _g(x):
    return -x + 5


GRAFIEKEN = [
    dict(naam=GRAF, titel="De rechten f en g", krommen=[(_f, "groen", "f", (-1, 4.5)), (_g, "blauw", "g", (-2, 7))],
         labelplek={"f": (4, 7), "g": (6.5, -1.5)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="twee rechten in een assenstelsel", vragen="klikvragen over vergelijkingen grafisch oplossen")]

VRAGEN = [
    klik(
        r"Klik op het punt dat de oplossing van \(f(x) = g(x)\) toont.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 3)],
        r"Waar beide rechten even hoog liggen, zijn de functiewaarden gelijk: in het snijpunt \((2, 3)\). De oplossing is \(x = 2\).",
    ),
    klik(
        r"Klik op het punt dat de oplossing van \(f(x) = 0\) toont.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0.5, 0)],
        r"\(f(x) = 0\) waar de rechte f de \(x\)-as snijdt: \(2x - 1 = 0\) geeft \(x = \tfrac{1}{2}\).",
    ),
    met_prent(f"{GRAF}.svg", mk(
        r"Voor welke \(x\) geldt \(f(x) > g(x)\)?",
        [r"\(x < 2\)", r"\(x > 2\)", r"\(x > 3\)", r"\(x < 5\)"],
        1,
        r"Rechts van het snijpunt ligt de stijgende rechte f boven de dalende rechte g.",
    )),
    met_prent(f"{GRAF}.svg", inv(
        r"Los op: \(g(x) = -1\). Wat is \(x\)?",
        ["6"],
        r"\(-x + 5 = -1\) geeft \(x = 6\). Op de grafiek: g gaat door \((6, -1)\).",
    )),
    mk(
        r"De formule voor de omtrek van een rechthoek is \(O = 2(l + b)\). Hoe druk je \(b\) uit?",
        [r"\(b = \dfrac{O}{2} - l\)", r"\(b = \dfrac{O - l}{2}\)", r"\(b = 2O - l\)", r"\(b = \dfrac{O}{2l}\)"],
        0,
        r"Eerst beide leden delen door \(2\): \(\tfrac{O}{2} = l + b\). Dan \(l\) aftrekken. Controle met \(l = 5\), \(b = 3\): \(O = 16\) en \(8 - 5 = 3\).",
    ),
    mk(
        r"Een temperatuur in °C zet je om naar °F met \(F = 1{,}8C + 32\). Hoe druk je \(C\) uit?",
        [r"\(C = \dfrac{F}{1{,}8} - 32\)", r"\(C = 1{,}8(F - 32)\)", r"\(C = \dfrac{F - 32}{1{,}8}\)", r"\(C = \dfrac{F + 32}{1{,}8}\)"],
        2,
        r"Eerst \(32\) aftrekken, dan delen door \(1{,}8\). Controle: \(212\) °F geeft \(\tfrac{180}{1{,}8} = 100\) °C.",
    ),
    inv(
        r"Hoeveel °C is \(77\) °F, met \(F = 1{,}8C + 32\)?",
        ["25", "25 °C", "25°C"],
        r"\(77 - 32 = 45\) en \(45 : 1{,}8 = 25\).",
    ),
    volgorde(
        r"Los op: \(\dfrac{x - 3}{4} = \dfrac{x}{2} + 1\). Zet de stappen in volgorde.",
        [
            r"beide leden maal \(4\): \(x - 3 = 2x + 4\)",
            r"\(x\)-termen naar één kant: \(-3 - 4 = 2x - x\)",
            r"uitrekenen: \(x = -7\)",
            r"controleren: \(\tfrac{-10}{4} = -2{,}5\) en \(\tfrac{-7}{2} + 1 = -2{,}5\)",
        ],
        "Eerst de noemers wegwerken met het kleinste gemeenschappelijke veelvoud, dan de onbekende afzonderen, dan controleren.",
    ),
    mk(
        r"Los op: \(3(x - 2) - 2(x + 1) = 5\).",
        [r"\(x = 13\)", r"\(x = 9\)", r"\(x = 3\)", r"\(x = 5\)"],
        0,
        r"\(3x - 6 - 2x - 2 = 5\), dus \(x - 8 = 5\) en \(x = 13\). Let op: \(-2 \cdot 1 = -2\), niet \(+2\).",
    ),
    tabel(
        "Hoeveel oplossingen heeft deze vergelijking?",
        [
            (r"\(2(x + 3) = 2x + 6\)", "oneindig veel"),
            (r"\(2(x + 3) = 2x + 5\)", "geen"),
            (r"\(2(x + 3) = x + 6\)", "één"),
            (r"\(5x - 5 = 5(x - 1)\)", "oneindig veel"),
            (r"\(4x = 4x - 1\)", "geen"),
        ],
        r"Valt \(x\) weg en blijft er iets waars over (zoals \(6 = 6\)), dan klopt elke \(x\). Blijft er iets vals over (\(6 = 5\)), dan is er geen oplossing.",
        kolommen=["geen", "één", "oneindig veel"],
    ),
    mk(
        r"Wat is de oplossingenverzameling van \(5 - 2x \geq 11\)?",
        [r"\(\left[-3, +\infty\right[\)", r"\(\left]-\infty, -3\right]\)", r"\(\left]-\infty, 3\right]\)", r"\(\left[3, +\infty\right[\)"],
        1,
        r"\(-2x \geq 6\). Delen door \(-2\) draait het teken om: \(x \leq -3\).",
    ),
    sorteer(
        r"Hoort dit getal bij de oplossingen van \(4 - x < 2x + 1\)?",
        ["Oplossing", "Geen oplossing"],
        [
            [r"\(0\)", "Geen oplossing"],
            [r"\(1\)", "Geen oplossing"],
            [r"\(1{,}5\)", "Oplossing"],
            [r"\(10\)", "Oplossing"],
            [r"\(-2\)", "Geen oplossing"],
        ],
        r"\(3 < 3x\), dus \(x > 1\). Bij \(x = 1\) staat er \(3 < 3\): dat klopt niet.",
    ),
    casus(
        r"Een fitnesscentrum heeft twee formules. Formule A: \(30\) euro per maand inschrijving, plus \(2\) euro per bezoek. Formule B: geen inschrijving, \(5\) euro per bezoek.",
        [
            mk(
                "Bij hoeveel bezoeken per maand kosten beide formules evenveel?",
                [r"\(6\)", r"\(10\)", r"\(15\)", r"\(30\)"],
                1,
                r"\(30 + 2b = 5b\) geeft \(30 = 3b\), dus \(b = 10\).",
            ),
            keuze(
                "Wie 14 keer per maand gaat, kiest best formule [[*A|B]]. Die kost dan [[*58|70|42]] euro.",
                r"A: \(30 + 2 \cdot 14 = 58\) euro. B: \(5 \cdot 14 = 70\) euro.",
            ),
        ],
    ),
    koppel(
        "Koppel elke formule aan de omvorming naar de gevraagde letter.",
        [
            [r"\(v = \dfrac{s}{t}\), naar \(t\)", r"\(t = \dfrac{s}{v}\)"],
            [r"\(p = \dfrac{F}{A}\), naar \(F\)", r"\(F = p \cdot A\)"],
            [r"\(A = \dfrac{b \cdot h}{2}\), naar \(h\)", r"\(h = \dfrac{2A}{b}\)"],
            [r"\(y = ax + b\), naar \(x\)", r"\(x = \dfrac{y - b}{a}\)"],
        ],
        [r"\(t = s \cdot v\)", r"\(h = \dfrac{A}{2b}\)"],
        "Controleer elke omvorming met een eenvoudig getallenvoorbeeld: zo valt een omgekeerde breuk meteen op.",
    ),
    mk(
        r"De kinetische energie is \(E_{k} = \tfrac{1}{2}mv^{2}\). Hoe druk je \(v\) uit (met \(v > 0\))?",
        [r"\(v = \sqrt{\dfrac{2E_{k}}{m}}\)", r"\(v = \dfrac{2E_{k}}{m}\)", r"\(v = \sqrt{2E_{k}m}\)", r"\(v = \dfrac{\sqrt{E_{k}}}{2m}\)"],
        0,
        r"Beide leden maal \(2\), delen door \(m\), dan de vierkantswortel: \(v^{2} = \tfrac{2E_{k}}{m}\).",
    ),
    inv(
        r"Bij \(U = R \cdot I\) is \(U = 230\) V en \(R = 46\) ohm. Hoeveel ampère is \(I\)?",
        ["5", "5 A", "5 ampère"],
        r"\(I = \tfrac{U}{R} = \tfrac{230}{46} = 5\) A.",
    ),
    tabel(
        "Juist of fout over het omvormen van gelijkheden en ongelijkheden?",
        [
            ("Je mag bij beide leden van een vergelijking hetzelfde getal optellen.", J),
            ("Als je beide leden van een ongelijkheid met een negatief getal vermenigvuldigt, draait het teken om.", J),
            ("Je mag beide leden van een vergelijking delen door x, ook als x nul kan zijn.", F),
            ("Als je beide leden van een ongelijkheid kwadrateert, blijft ze altijd kloppen.", F),
        ],
        r"Delen door een letter die nul kan zijn, kan een oplossing doen verdwijnen. Kwadrateren: \(-3 < 2\), maar \(9 > 4\).",
    ),
    inv(
        r"Een taxi rekent \(3{,}50\) euro opstap en \(2{,}10\) euro per km. Je hebt \(25\) euro. Hoeveel volle kilometer kan je hoogstens rijden?",
        ["10", "10 km"],
        r"\(3{,}50 + 2{,}10k \leq 25\) geeft \(k \leq 10{,}2\ldots\). Hoogstens \(10\) volle kilometer.",
    ),
    mk(
        r"Een vader is nu \(3\) keer zo oud als zijn dochter. Over \(12\) jaar is hij \(2\) keer zo oud. Hoe oud is de dochter nu?",
        [r"\(6\)", r"\(12\)", r"\(18\)", r"\(24\)"],
        1,
        r"Dochter \(x\), vader \(3x\). Over \(12\) jaar: \(3x + 12 = 2(x + 12)\), dus \(x = 12\). De vader is \(36\), later \(48\) en \(24\).",
    ),
    keuze(
        r"Je lost \(-4x < 12\) op. Je deelt door [[*\(-4\)|\(4\)|\(12\)]] en het teken [[*draait om|blijft staan]]. De oplossing is [[*\(x > -3\)|\(x < -3\)|\(x > 3\)]].",
        r"Delen door een negatief getal draait het ongelijkheidsteken om. Controle: \(x = 0\) geeft \(0 < 12\), en \(0 > -3\) klopt.",
    ),
    mk(
        r"De som van drie opeenvolgende gehele getallen is \(87\). Wat is het grootste getal?",
        [r"\(28\)", r"\(29\)", r"\(30\)", r"\(31\)"],
        2,
        r"\(x + (x + 1) + (x + 2) = 87\) geeft \(3x + 3 = 87\), \(x = 28\). De getallen zijn \(28, 29, 30\).",
    ),
    sleep(
        r"Bij \(f(x) = 0\) zoek je de [[nulwaarde]] van \(f\): daar snijdt de grafiek de [[\(x\)-as]]. Bij \(f(x) = g(x)\) zoek je de \(x\)-coördinaat van het [[snijpunt]] van beide grafieken.",
        [r"\(y\)-as", "top"],
        "Een vergelijking grafisch oplossen betekent: kijken waar de grafieken elkaar of de as raken of snijden.",
    ),
    mk(
        r"Een kaars is \(24\) cm lang en brandt \(1{,}5\) cm per uur. Na hoeveel uur is ze nog \(9\) cm?",
        [r"\(6\) uur", r"\(10\) uur", r"\(13{,}5\) uur", r"\(16\) uur"],
        1,
        r"\(24 - 1{,}5t = 9\) geeft \(1{,}5t = 15\), dus \(t = 10\) uur.",
    ),
    open_(
        r"Een leerling lost \(-2x > 8\) op en schrijft \(x > -4\). Controleer met een getal of dat klopt en leg uit wat er fout liep.",
        r"Neem \(x = 0\): dat voldoet aan \(x > -4\), maar \(-2 \cdot 0 = 0\) is niet groter dan \(8\). De leerling vergat dat het teken omdraait als je deelt door een negatief getal. Juist is \(x < -4\).",
    ),
    mk(
        r"Los op: \(\dfrac{2x + 1}{3} = \dfrac{x - 1}{2}\).",
        [r"\(x = -5\)", r"\(x = 5\)", r"\(x = -1\)", r"\(x = \tfrac{1}{7}\)"],
        0,
        r"Beide leden maal \(6\): \(4x + 2 = 3x - 3\), dus \(x = -5\). Controle: \(\tfrac{-9}{3} = -3\) en \(\tfrac{-6}{2} = -3\).",
    ),
    inv(
        r"De massadichtheid van ijzer is \(7{,}9\) g/cm³. Hoeveel cm³ is een blok ijzer van \(395\) g?",
        ["50", "50 cm³"],
        r"\(\rho = \tfrac{m}{V}\) omvormen geeft \(V = \tfrac{m}{\rho} = \tfrac{395}{7{,}9} = 50\) cm³.",
    ),
    mk(
        r"Een fietser vertrekt om 10 u aan \(18\) km/u. Een tweede fietser vertrekt om 11 u langs dezelfde weg aan \(24\) km/u. Hoe laat haalt de tweede de eerste in?",
        [r"om 13 u", r"om 14 u", r"om 15 u", r"om 12 u"],
        1,
        r"Met \(t\) uren na 11 u: \(18(t + 1) = 24t\) geeft \(18 = 6t\), \(t = 3\). Dat is om 14 u.",
    ),
    inv(
        r"Los op: \(0{,}5x + 3 = 2x - 1{,}5\). Wat is \(x\)?",
        ["3"],
        r"\(3 + 1{,}5 = 2x - 0{,}5x\), dus \(4{,}5 = 1{,}5x\) en \(x = 3\).",
    ),
    keuze(
        r"Bij \(E_{k} = \tfrac{1}{2}mv^{2}\): als de massa verdubbelt, wordt de energie [[*\(2\)|\(4\)|\(\tfrac{1}{2}\)]] keer zo groot. Als de snelheid verdrievoudigt, wordt de energie [[*\(9\)|\(3\)|\(6\)]] keer zo groot.",
        r"De energie is recht evenredig met \(m\), maar met het kwadraat van \(v\): \(3^{2} = 9\).",
    ),
]
