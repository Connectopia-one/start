"""Rechtlijnige bewegingen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, assen

# x(t)-grafiek van een wandelaar -----------------------------------------
XT = Prent("xt-wandeling", "Positie van een loper", "x(t)-grafiek: vooruit, stilstaan, sneller vooruit, terug naar het begin")
X1, Y1 = assen(XT, 0, 12, 0, 40, "t (s)", "x (m)", 1, 10)
pts = [(0, 0), (4, 20), (6, 20), (8, 40), (12, 0)]
XT.pad("M" + " L ".join(f"{X1(t):.1f} {Y1(x):.1f}" for t, x in pts), "none", BLAUW, 5)
def _zx(t1, x1, t2, x2):
    a, b = sorted((Y1(x1), Y1(x2)))
    return Prent.zone(X1(t1) + 4, a - 18, X1(t2) - X1(t1) - 8, b - a + 36)
Z_X_STIL = _zx(4, 20, 6, 20)
Z_X_SNELST = _zx(6, 20, 8, 40)
Z_X_TERUG = _zx(8, 40, 12, 0)
Z_X_EERST = _zx(0, 0, 4, 20)

# v(t)-grafiek van een auto ----------------------------------------------
VT = Prent("vt-auto", "Snelheid van een auto", "v(t)-grafiek: versnellen, constant, vertragen tot stilstand")
X2, Y2 = assen(VT, 0, 12, 0, 15, "t (s)", "v (m/s)", 1, 3)
pts = [(0, 0), (4, 12), (8, 12), (11, 0), (12, 0)]
VT.pad("M" + " L ".join(f"{X2(t):.1f} {Y2(v):.1f}" for t, v in pts), "none", ORANJE, 5)
def _zv(t1, v1, t2, v2):
    a, b = sorted((Y2(v1), Y2(v2)))
    return Prent.zone(X2(t1) + 4, a - 18, X2(t2) - X2(t1) - 8, b - a + 36)
Z_V_VERSN = _zv(0, 0, 4, 12)
Z_V_ERB = _zv(4, 12, 8, 12)
Z_V_VERTR = _zv(8, 12, 11, 0)
Z_V_STIL = _zv(11, 0, 12, 0)

VRAGEN = [
    klik(
        "Klik op het stuk waar de loper stilstaat.",
        XT.bestand, [Z_X_STIL],
        "Een vlak stuk in een x(t)-grafiek: de positie verandert niet.",
    ),
    klik(
        "Klik op het stuk waar de loper het snelst vooruitgaat.",
        XT.bestand, [Z_X_SNELST],
        "De steilste lijn hoort bij de grootste snelheid: 20 m in 2 s is 10 m/s.",
    ),
    klik(
        "Klik op het stuk waar de snelheid van de loper negatief is.",
        XT.bestand, [Z_X_TERUG],
        "De positie daalt: de loper beweegt tegengesteld aan de zin van de x-as.",
    ),
    met_prent(XT.bestand, inv(
        "Kijk naar de x(t)-grafiek. Wat is de snelheid van de loper tijdens de eerste 4 seconden, in m/s?",
        ["5"],
        "20 m in 4 s: 20 : 4 = 5 m/s.",
    )),
    met_prent(XT.bestand, inv(
        "Kijk naar de x(t)-grafiek. Hoeveel meter legt de loper in totaal af in de 12 seconden?",
        ["80"],
        "40 m vooruit en 40 m terug: de afgelegde weg is 80 m.",
    )),
    met_prent(XT.bestand, inv(
        "Kijk naar de x(t)-grafiek. Wat is de verplaatsing van de loper na 12 seconden, in meter?",
        ["0"],
        "Hij eindigt waar hij begon. De verplaatsing gaat enkel van begin naar eind.",
    )),
    klik(
        "Klik op het stuk waar de auto eenparig rechtlijnig beweegt.",
        VT.bestand, [Z_V_ERB],
        "Een vlakke lijn in een v(t)-grafiek: de snelheid blijft gelijk.",
    ),
    klik(
        "Klik op het stuk waar de versnelling negatief is.",
        VT.bestand, [Z_V_VERTR],
        "De snelheid daalt: de auto vertraagt.",
    ),
    klik(
        "Klik op het stuk waar de versnelling 3 m/s² is.",
        VT.bestand, [Z_V_VERSN],
        "Van 0 naar 12 m/s in 4 s: 12 : 4 = 3 m/s².",
    ),
    met_prent(VT.bestand, inv(
        "Kijk naar de v(t)-grafiek. Hoeveel meter legt de auto af tussen 4 s en 8 s?",
        ["48"],
        "De oppervlakte onder de grafiek is een rechthoek: 12 m/s · 4 s = 48 m.",
    )),
    met_prent(VT.bestand, inv(
        "Kijk naar de v(t)-grafiek. Hoeveel meter legt de auto af tijdens het remmen, van 8 s tot 11 s?",
        ["18"],
        "De oppervlakte is een driehoek: de helft van 12 · 3 = 18 m.",
    )),
    met_prent(VT.bestand, inv(
        "Kijk naar de v(t)-grafiek. Wat is de versnelling tijdens het remmen, in m/s²?",
        ["-4", "−4"],
        "Van 12 naar 0 m/s in 3 s: −12 : 3 = −4 m/s².",
    )),
    met_prent(VT.bestand, tabel(
        "Kijk naar de v(t)-grafiek. Klopt dit?",
        [
            ("Tussen 4 s en 8 s is de versnelling nul.", J),
            ("Na 11 s staat de auto stil.", J),
            ("Tussen 0 s en 4 s is de x(t)-grafiek een rechte lijn.", F),
            ("Tussen 8 s en 11 s rijdt de auto achteruit.", F),
        ],
        "Bij versnellen is de x(t)-grafiek een kromme. Vertragen is niet achteruitrijden: de snelheid blijft positief.",
    )),
    tabel(
        "Scalair of vectorieel?",
        [
            ("de verplaatsing", "Vectorieel"),
            ("de snelheid", "Vectorieel"),
            ("de versnelling", "Vectorieel"),
            ("de afgelegde weg", "Scalair"),
            ("het tijdsverloop", "Scalair"),
        ],
        "Een vectoriële grootheid heeft een grootte, een richting en een zin.",
        kolommen=["Scalair", "Vectorieel"],
    ),
    tabel(
        "Reken om. Klopt het?",
        [
            ("36 km/h = 10 m/s", J),
            ("72 km/h = 20 m/s", J),
            ("18 km/h = 18 m/s", F),
            ("25 m/s = 90 km/h", J),
        ],
        "Van km/h naar m/s deel je door 3,6. Omgekeerd vermenigvuldig je met 3,6.",
    ),
    inv(
        "Een trein rijdt 240 km in 3 uur. Wat is zijn gemiddelde snelheid in km/h?",
        ["80"],
        "240 : 3 = 80 km/h.",
    ),
    inv(
        "Een puntmassa start op 15 m en rijdt met 3 m/s in de zin van de x-as. Op welke positie zit ze na 5 s, in meter?",
        ["30"],
        "15 + 3 · 5 = 30 m.",
    ),
    inv(
        "Een fietser start uit stilstand en versnelt met 2 m/s². Hoe snel rijdt hij na 6 s, in m/s?",
        ["12"],
        "v = a · t = 2 · 6 = 12 m/s.",
    ),
    casus(
        "Twee auto's vertrekken op hetzelfde moment vanuit Hasselt naar dezelfde richting. Auto A rijdt 20 m/s, auto B 25 m/s. Beide bewegen eenparig rechtlijnig.",
        [
            mk(
                "Hoe zien hun x(t)-grafieken eruit?",
                [
                    "Twee rechten vanuit hetzelfde punt, B steiler",
                    "Twee vlakke lijnen, elk op een andere hoogte",
                    "Twee krommen die steeds steiler worden",
                    "Twee rechten vanuit hetzelfde punt, waarbij A steiler is",
                ],
                0,
                "Eenparig betekent rechte lijnen. De grootste snelheid geeft de steilste lijn.",
            ),
            inv(
                "Hoeveel meter ligt B na 60 s voor op A?",
                ["300"],
                "B legt 1500 m af, A 1200 m: verschil 300 m.",
            ),
            keuze(
                "Hun v(t)-grafieken zijn [[*twee vlakke lijnen|twee stijgende rechten|twee dalende rechten]].",
                "Bij een ERB blijft de snelheid gelijk.",
            ),
        ],
    ),
    koppel(
        "Koppel elke grafiek aan wat je eraan afleest.",
        [
            ("steilheid van de x(t)-grafiek", "snelheid"),
            ("steilheid van de v(t)-grafiek", "versnelling"),
            ("oppervlakte onder de v(t)-grafiek", "verplaatsing"),
        ],
        ["massa"],
        "Massa lees je niet af aan een bewegingsgrafiek.",
    ),
    sleep(
        "De vier kenmerken van een vector zijn de [[grootte]], de [[richting]], de [[zin]] en het [[aangrijpingspunt]].",
        ["temperatuur", "tijdstip"],
        "Daarom stel je een vector voor met een pijl.",
    ),
    tabel(
        "Versnelt of vertraagt het voorwerp?",
        [
            ("v is positief en a is positief", "Versnelt"),
            ("v is positief en a is negatief", "Vertraagt"),
            ("v is negatief en a is negatief", "Versnelt"),
            ("v is negatief en a is positief", "Vertraagt"),
        ],
        "Hebben v en a hetzelfde teken, dan neemt de grootte van de snelheid toe.",
        kolommen=["Versnelt", "Vertraagt"],
    ),
    klik(
        "Klik op het stuk van de v(t)-grafiek waar de auto stilstaat.",
        VT.bestand, [Z_V_STIL],
        "Een snelheid van nul: de auto staat stil.",
    ),
    klik(
        "Klik op het stuk van de x(t)-grafiek waar de loper 5 m/s loopt.",
        XT.bestand, [Z_X_EERST],
        "20 m in 4 s is 5 m/s.",
    ),
    casus(
        "Twee treinen rijden op hetzelfde spoor naar elkaar toe. Je tekent van beide de x(t)-grafiek in één assenstelsel.",
        [
            mk(
                "Hoe vind je grafisch wanneer ze elkaar kruisen?",
                [
                    "Je zoekt het snijpunt van de twee grafieken",
                    "Je zoekt waar een van de grafieken de tijdas raakt",
                    "Je meet de oppervlakte onder elke grafiek",
                    "Je vergelijkt de steilheid van beide lijnen",
                ],
                0,
                "Kruisen betekent op hetzelfde tijdstip op dezelfde positie.",
            ),
            keuze(
                "Eén grafiek stijgt en de andere daalt, want hun snelheden hebben [[*een tegengesteld teken|hetzelfde teken|geen teken]].",
                "Het teken van de snelheid zegt in welke zin de beweging gaat.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over de ogenblikkelijke en de gemiddelde snelheid?",
        [
            ("De ogenblikkelijke snelheid geldt voor één tijdstip.", J),
            ("De gemiddelde snelheid kijkt naar een heel tijdsinterval.", J),
            ("Bij een ERB zijn ze altijd verschillend.", F),
        ],
        "Bij een ERB is de snelheid op elk ogenblik dezelfde, dus gelijk aan de gemiddelde.",
    ),
    open_(
        "Leg uit waarom de afgelegde weg en de verplaatsing van een fietser die 5 km naar het werk rijdt en terug naar huis verschillen.",
        "De afgelegde weg is de hele baan: 5 km heen en 5 km terug, samen 10 km. De verplaatsing kijkt enkel naar begin en eind. Omdat de fietser terug thuis is, is zijn verplaatsing nul.",
    ),
]
