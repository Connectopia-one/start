"""Formules omvormen en eerstegraadsvergelijkingen — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("formules-abonnementen-do", 0, 200, 0, 50, 20, 5)


def _a(x):
    return 20 + 0.1 * x


def _b(x):
    return 8 + 0.2 * x


GRAFIEKEN = [
    dict(naam=GRAF, titel="Maandprijs van twee belabonnementen", krommen=[(_a, "groen", "A", (0, 200)), (_b, "blauw", "B", (0, 200))],
         labelplek={"A": (185, 41), "B": (170, 46.5)}, xlabel="minuten", ylabel="euro"),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="twee rechten: kosten van abonnement A en B", vragen="klikvragen over vergelijkingen en ongelijkheden grafisch oplossen")]

VRAGEN = [
    klik(
        "Klik op het punt waar beide abonnementen evenveel kosten.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 120, 32)],
        r"\(20 + 0{,}1x = 8 + 0{,}2x\) geeft \(12 = 0{,}1x\), dus \(x = 120\) minuten, voor \(32\) euro.",
    ),
    klik(
        "Klik in het gebied van de minuten waarvoor abonnement A goedkoper is.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, 125, 200)],
        "Rechts van het snijpunt ligt de rechte van A onder die van B: vanaf meer dan 120 minuten is A goedkoper.",
    ),
    klik(
        "Klik op het punt dat toont hoeveel abonnement B kost als je niet belt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0, 8)],
        "Bij 0 minuten betaal je enkel het vaste bedrag van B: 8 euro. Dat is het snijpunt met de verticale as.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek. Juist of fout?",
        [("Bij 60 minuten is B goedkoper.", J),
         ("Elke extra minuut kost bij A meer dan bij B.", F),
         ("Bij 200 minuten betaal je bij B 48 euro.", J),
         ("De rechte van B is steiler dan die van A.", J),
         ("De twee rechten zijn evenwijdig.", F)],
        "B kost 0,20 euro per minuut, A maar 0,10. Daarom is B steiler en snijden de rechten elkaar.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Welke omvorming is juist?",
        [(r"\(v = \tfrac{s}{t}\) wordt \(t = \tfrac{s}{v}\)", J),
         (r"\(P = U \cdot I\) wordt \(I = U \cdot P\)", F),
         (r"\(y = 3x - 6\) wordt \(x = \tfrac{y + 6}{3}\)", J),
         (r"\(A = \tfrac{b \cdot h}{2}\) wordt \(h = \tfrac{2A}{b}\)", J),
         (r"\(C = 2\pi r\) wordt \(r = 2\pi C\)", F),
         (r"\(E = mc^{2}\) wordt \(c = \sqrt{\tfrac{E}{m}}\)", J)],
        r"Controleer met getallen. Bij \(P = U \cdot I\) deel je door \(U\): \(I = \tfrac{P}{U}\). Bij \(C = 2\pi r\) deel je door \(2\pi\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Druk \(a\) uit in \(v = v_{0} + a \cdot t\).",
        [r"\(a = \dfrac{v - v_{0}}{t}\)", r"\(a = \dfrac{v}{t} - v_{0}\)", r"\(a = (v - v_{0}) \cdot t\)", r"\(a = \dfrac{v + v_{0}}{t}\)"],
        0,
        r"Eerst \(v_{0}\) naar de andere kant: \(v - v_{0} = a \cdot t\). Dan delen door \(t\).",
    ),
    mk(
        r"De temperatuur in Fahrenheit is \(F = 1{,}8 \cdot C + 32\). Hoeveel graden Celsius is \(77\) °F?",
        ["25 °C", "43 °C", "60,6 °C", "13 °C"],
        0,
        r"\(C = \dfrac{F - 32}{1{,}8} = \dfrac{45}{1{,}8} = 25\).",
    ),
    casus(
        r"De energie die een waterkoker gebruikt, is \(E = P \cdot t\). Het vermogen \(P\) is \(2000\) W en \(E\) is in joule als \(t\) in seconden staat.",
        [
            mk("Hoe druk je de tijd uit?", [r"\(t = E \cdot P\)", r"\(t = \tfrac{E}{P}\)", r"\(t = \tfrac{P}{E}\)", r"\(t = E - P\)"], 1, r"Deel beide leden door \(P\)."),
            inv("Hoelang duurt het om 300 000 J te leveren, in seconden?", ["150", "150 s"], r"\(\tfrac{300\,000}{2000} = 150\) s, twee en een halve minuut."),
            mk("Wat gebeurt er met de tijd als het vermogen halveert en E gelijk blijft?", ["ze halveert", "ze verdubbelt", "ze blijft gelijk", "ze wordt vier keer zo groot"], 1,
               r"\(t\) en \(P\) zijn omgekeerd evenredig."),
        ],
    ),
    keuze(
        r"In \(p = \tfrac{F}{A}\) is de druk [[*recht evenredig|omgekeerd evenredig]] met de kracht en [[*omgekeerd evenredig|recht evenredig]] met de oppervlakte.",
        "Meer kracht geeft meer druk. Een grotere oppervlakte verdeelt de kracht, dus minder druk: daarom zak je met ski's niet weg in de sneeuw.",
    ),
    mk(
        r"In \(E_{p} = m \cdot g \cdot h\) wordt de hoogte drie keer zo groot en de massa gehalveerd. Wat gebeurt er met \(E_{p}\)?",
        ["ze wordt 1,5 keer zo groot", "ze wordt 6 keer zo groot", "ze blijft gelijk", "ze wordt 3 keer zo klein"],
        0,
        r"\(3 \cdot \tfrac{1}{2} = 1{,}5\).",
    ),
    inv(
        r"Los op: \(\dfrac{2x - 1}{3} = \dfrac{x + 4}{2}\).",
        ["14", "x = 14", "x=14"],
        r"Vermenigvuldig beide leden met \(6\): \(4x - 2 = 3x + 12\), dus \(x = 14\).",
    ),
    mk(
        r"Los op: \(5 - 2(x - 3) = 3x - 4\).",
        [r"\(x = 3\)", r"\(x = 1\)", r"\(x = 2{,}2\)", r"\(x = 15\)"],
        0,
        r"\(5 - 2x + 6 = 3x - 4\) geeft \(15 = 5x\), dus \(x = 3\). Let op het minteken voor de haakjes.",
    ),
    sorteer(
        "Hoeveel oplossingen heeft de vergelijking?",
        ["Eén oplossing", "Geen oplossing", "Elke x is oplossing"],
        [(r"\(2(x + 3) = 2x + 6\)", "Elke x is oplossing"),
         (r"\(3x - 1 = 3x + 4\)", "Geen oplossing"),
         (r"\(4x = 0\)", "Eén oplossing"),
         (r"\(x + x = 2x + 1\)", "Geen oplossing"),
         (r"\(5 - x = x - 5\)", "Eén oplossing"),
         (r"\(\tfrac{6x}{3} = 2x\)", "Elke x is oplossing")],
        r"Vereenvoudig tot de vorm \(ax = b\). Valt \(x\) weg, dan krijg je ofwel een ware uitspraak (elke \(x\)) of een valse (geen).",
    ),
    tabel(
        r"Wat is de oplossingenverzameling?",
        [(r"\(2x - 3 < 7\)", r"\(\left]-\infty, 5\right[\)"),
         (r"\(-4x \leq 8\)", r"\(\left[-2, +\infty\right[\)"),
         (r"\(3 - x > 1\)", r"\(\left]-\infty, 2\right[\)"),
         (r"\(\tfrac{x}{-2} \geq 1\)", r"\(\left]-\infty, -2\right]\)")],
        "Deel je door een negatief getal, dan draait het teken om.",
        kolommen=[r"\(\left]-\infty, 5\right[\)", r"\(\left[-2, +\infty\right[\)", r"\(\left]-\infty, 2\right[\)", r"\(\left]-\infty, -2\right]\)"],
    ),
    mk(
        r"Welk geheel getal is de kleinste oplossing van \(7 - 3x < 1\)?",
        ["2", "3", "1", "−2"],
        1,
        r"\(-3x < -6\) geeft \(x > 2\). Het kleinste gehele getal groter dan \(2\) is \(3\).",
    ),
    casus(
        "Een fietsverhuur vraagt 12 euro vast en 3 euro per uur. Een tweede zaak vraagt geen vast bedrag maar 5 euro per uur.",
        [
            mk("Welke vergelijking zoekt het aantal uren waarbij beide even duur zijn?", [r"\(12 + 3x = 5x\)", r"\(12x + 3 = 5x\)", r"\(12 + 5x = 3x\)", r"\(15x = 5x\)"], 0, "Vast bedrag plus prijs per uur keer het aantal uren."),
            inv("Na hoeveel uur zijn ze even duur?", ["6", "6 uur"], r"\(12 = 2x\), dus \(x = 6\)."),
            mk("Je huurt 4 uur. Welke zaak kies je?", ["de eerste", "de tweede", "allebei even duur", "dat kun je niet weten"], 1,
               r"Eerste: \(12 + 12 = 24\) euro. Tweede: \(20\) euro. Onder de zes uur is de tweede goedkoper."),
        ],
    ),
    volgorde(
        r"Zet de stappen in de goede volgorde om \(\tfrac{x}{4} - 1 = \tfrac{x}{6}\) op te lossen.",
        [r"beide leden maal \(12\): \(3x - 12 = 2x\)", r"\(2x\) aftrekken: \(x - 12 = 0\)", r"\(12\) optellen: \(x = 12\)", r"controleren: \(3 - 1 = 2\)"],
        "Eerst de noemers wegwerken met het kleinste gemeenschappelijk veelvoud, dan de onbekenden aan één kant, en altijd controleren.",
    ),
    tabel(
        "Juist of fout over het omvormen?",
        [("Je mag beide leden van een vergelijking met hetzelfde getal vermenigvuldigen, behalve met 0.", J),
         ("Als je beide leden kwadrateert, kan er een valse oplossing bijkomen.", J),
         ("Bij een ongelijkheid mag je beide leden met een negatief getal vermenigvuldigen zonder iets te veranderen.", F),
         (r"Uit \(x \cdot (x - 2) = 3 \cdot (x - 2)\) volgt altijd \(x = 3\).", F)],
        r"Wie door \(x - 2\) deelt, verliest de oplossing \(x = 2\). Kwadrateren maakt van \(x = -3\) en \(x = 3\) hetzelfde.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"In \(I = \tfrac{U}{R}\) is \(I\) de [[stroomsterkte]]. Wordt \(R\) twee keer zo groot bij dezelfde \(U\), dan wordt \(I\) [[twee keer zo klein]].",
        ["spanning", "twee keer zo groot", "vier keer zo klein"],
        "R staat in de noemer: groter R, kleinere stroom.",
    ),
    mk(
        r"De omtrek van een rechthoek is \(P = 2(l + b)\). Hoe druk je \(b\) uit?",
        [r"\(b = \tfrac{P}{2} - l\)", r"\(b = \tfrac{P - l}{2}\)", r"\(b = 2P - l\)", r"\(b = \tfrac{P}{2l}\)"],
        0,
        r"Deel eerst door \(2\): \(\tfrac{P}{2} = l + b\). Trek dan \(l\) af.",
    ),
    inv(
        "Drie opeenvolgende gehele getallen hebben als som 87. Wat is het grootste?",
        ["30"],
        r"\(x + (x + 1) + (x + 2) = 87\) geeft \(3x = 84\), \(x = 28\). Het grootste is \(30\).",
    ),
    koppel(
        "Verbind de zin met de vergelijking.",
        [("het dubbel van een getal verminderd met 5 is 11", r"\(2x - 5 = 11\)"),
         ("een getal vermeerderd met 5, en dat gedeeld door 2, is 11", r"\(\tfrac{x + 5}{2} = 11\)"),
         ("de helft van een getal plus 5 is 11", r"\(\tfrac{x}{2} + 5 = 11\)"),
         ("een getal plus de helft ervan is 11", r"\(x + \tfrac{x}{2} = 11\)")],
        [r"\(2(x - 5) = 11\)"],
        "Lees goed waar 'de helft' of 'het dubbel' op slaat.",
    ),
    mk(
        "Een vader is nu 40 en zijn zoon 12. Over hoeveel jaar is de vader dubbel zo oud als de zoon?",
        ["over 14 jaar", "over 16 jaar", "over 8 jaar", "over 28 jaar"],
        1,
        r"\(40 + x = 2(12 + x)\) geeft \(40 + x = 24 + 2x\), dus \(x = 16\). Dan is hij 56 en de zoon 28.",
    ),
    mk(
        r"Een getal \(x\) voldoet aan \(-2 \leq 3x + 4 < 10\). Welk interval hoort daarbij?",
        [r"\(\left[-2, 2\right[\)", r"\(\left]-2, 2\right]\)", r"\(\left[-2, 10\right[\)", r"\(\left[2, 6\right[\)"],
        0,
        r"Trek overal \(4\) af: \(-6 \leq 3x < 6\). Deel door \(3\): \(-2 \leq x < 2\).",
    ),
    tabel(
        r"Is \(x = -2\) een oplossing?",
        [(r"\(3x + 7 = 1\)", J), (r"\(x^{2} = -4\)", F), (r"\(-x > 1\)", J), (r"\(2 - x = 0\)", F)],
        r"Vul \(-2\) in: \(-6 + 7 = 1\) klopt, \((-2)^{2} = 4\), \(-(-2) = 2 > 1\), \(2 + 2 = 4\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"De gemiddelde snelheid is \(v = \tfrac{s}{t}\). Een trein rijdt 270 km aan 90 km/u. Hoeveel uur rijdt hij?",
        ["3", "3 uur", "3 u"],
        r"\(t = \tfrac{s}{v} = \tfrac{270}{90} = 3\) uur.",
    ),
]
