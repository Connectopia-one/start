r"""Betrouwbaarheidsintervallen — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en een eigen prent met tien intervallen, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Tien 95%-intervallen uit tien steekproeven ------------------------------------------------
TI = Prent("tien-intervallen", "Tien 95%-betrouwbaarheidsintervallen voor hetzelfde populatiegemiddelde μ = 40", "tien horizontale intervallen onder elkaar, genummerd 1 tot 10, met een verticale stippellijn bij μ = 40; interval 7 ligt volledig rechts van 40, alle andere snijden de lijn")
L, R = 200, 900


def X(v):
    return L + (R - L) * (v - 30) / 20


INT = [(36.5, 43.1), (38.2, 44.8), (35.0, 41.6), (37.9, 44.5), (34.6, 41.2),
       (36.8, 43.4), (40.9, 47.5), (37.2, 43.8), (33.9, 40.5), (38.6, 45.2)]
TOP, STAP = 100, 44
for g in range(30, 51, 5):
    TI.lijn(X(g), TOP + 10 * STAP - 10, X(g), TOP + 10 * STAP, DONKER, 2)
    TI.tekst(X(g), TOP + 10 * STAP + 26, str(g), 18)
TI.lijn(L, TOP + 10 * STAP - 5, R, TOP + 10 * STAP - 5, DONKER, 2)
TI.lijn(X(40), TOP - 20, X(40), TOP + 10 * STAP - 5, "#b9572f", 3, True)
TI.tekst(X(40), TOP - 28, "μ = 40", 18, "middle", "#b9572f", True)
for i, (a, b) in enumerate(INT):
    y = TOP + i * STAP + 10
    TI.tekst(L - 40, y + 6, f"steekproef {i + 1}", 17, "end", "#5c6356")
    TI.lijn(X(a), y, X(b), y, DONKER, 4)
    TI.lijn(X(a), y - 9, X(a), y + 9, DONKER, 3)
    TI.lijn(X(b), y - 9, X(b), y + 9, DONKER, 3)
    TI.cirkel((X(a) + X(b)) / 2, y, 6, DONKER, DONKER, 1)


def rij(i):
    return [Prent.zone(40, TOP + (i - 1) * STAP - 10, R - 40, STAP)]


VRAGEN = [
    klik("Klik op het interval dat de populatiewaarde mist.", TI.bestand, rij(7),
         "Steekproef 7 loopt van ongeveer 41 tot 47,5 en bevat 40 niet."),
    klik("Klik op het interval met het grootste steekproefgemiddelde.", TI.bestand, rij(7),
         "Het midden van een interval is het steekproefgemiddelde; bij steekproef 7 ligt dat het verst rechts."),
    klik("Klik op het interval met het kleinste steekproefgemiddelde.", TI.bestand, rij(9),
         "Het middenpunt van steekproef 9 ligt het verst links."),
    met_prent(TI.bestand, inv("Hoeveel van deze tien intervallen bevatten μ?", ["9", "negen"],
              "Alleen steekproef 7 mist.")),
    met_prent(TI.bestand, keuze("Alle intervallen zijn even breed, omdat ze dezelfde [[*steekproefgrootte en hetzelfde niveau|steekproefgemiddelden|ondergrens]] hebben.",
              "De breedte hangt af van n, σ en het niveau, niet van het gemiddelde.")),
    met_prent(TI.bestand, keuze("Neem je 200 zulke intervallen, dan verwacht je dat er ongeveer [[*10|5|20]] μ missen.",
              "5 procent van 200 is 10.")),
    met_prent(TI.bestand, inv("Interval 3 loopt van 35,0 tot 41,6. Hoe groot is de foutenmarge? Schrijf als decimaal getal.", ["3,3", "3.3"],
              "(41,6 − 35,0) / 2 = 3,3.")),
    casus(
        "Een peiling bij 1000 kiezers geeft partij Groenvelden 23 procent, met een 95%-betrouwbaarheidsinterval van 20,4 tot 25,6 procent.",
        [
            inv("Hoe groot is de foutenmarge in procent? Schrijf als decimaal getal.", ["2,6", "2.6"],
                "(25,6 − 20,4) / 2 = 2,6."),
            keuze("Het midden van het interval is [[*23|25,6|20,4]] procent.", "Het steekproefresultaat."),
            tabel("Is deze uitspraak verdedigbaar?", [
                ("de partij haalt waarschijnlijk tussen 20 en 26 procent", J),
                ("de partij haalt zeker 23 procent", F),
                ("een score van 27 procent is weinig aannemelijk", J),
            ], "Het interval geeft aannemelijke waarden, geen zekerheid."),
            mk("Een week later geeft een peiling bij 4000 kiezers ook 23 procent. Wat verwacht je van de marge?",
               ["ongeveer de helft, 1,3 procent", "ongeveer een kwart, 0,65 procent", "vier keer zo groot", "precies dezelfde"], 0,
               r"Vier keer zo veel kiezers: de marge deelt door \(\sqrt{4} = 2\)."),
        ],
    ),
    sorteer("Wordt het interval breder of smaller?", ["breder", "smaller"], [
        ["het niveau gaat van 95 naar 99 procent", "breder"],
        ["de steekproef wordt groter", "smaller"],
        ["de spreiding in de populatie is groter", "breder"],
        ["het niveau gaat van 95 naar 90 procent", "smaller"],
    ], "Zekerder of meer spreiding maakt breder; meer gegevens maken smaller."),
    tabel("Wat is de foutenmarge van dit interval?", [
        ("van 12 tot 18", "3"),
        ("van 0,40 tot 0,46", "0,03"),
        ("van 95 tot 105", "5"),
    ], "De helft van de breedte.", kolommen=["3", "0,03", "5"]),
    inv("Een interval heeft als midden 64 en een foutenmarge van 2,5. Wat is de bovengrens? Schrijf als decimaal getal.", ["66,5", "66.5"],
        "64 + 2,5 = 66,5."),
    keuze("Wil je de foutenmarge drie keer kleiner maken, dan moet de steekproef [[*9|3|6]] keer zo groot worden.",
          r"De marge gaat met \(1/\sqrt{n}\)."),
    mk("H₀: μ = 50. Het 95%-interval voor μ loopt van 51,2 tot 56,8. Wat besluit je tweezijdig op niveau 5 procent?",
       ["H₀ verwerpen, want 50 ligt buiten het interval",
        "H₀ niet verwerpen, want het interval is breed",
        "H₀ verwerpen, want 56,8 is groter dan 50",
        "geen besluit, een interval zegt niets over een toets"], 0,
       "Ligt de waarde uit H₀ buiten het interval, dan verwerp je H₀."),
    koppel("Koppel elk begrip aan de omschrijving.", [
        ["foutenmarge", "de helft van de breedte van het interval"],
        ["betrouwbaarheidsniveau", "het percentage intervallen dat de populatiewaarde vangt"],
        ["puntschatting", "het steekproefresultaat in het midden"],
    ], ["de spreiding van de populatie"], "Drie begrippen rond een interval."),
    tabel("Klopt dit voor een 95%-betrouwbaarheidsinterval voor een gemiddelde?", [
        ("het gaat over μ, niet over de individuele waarden", J),
        ("95 procent van de metingen ligt in het interval", F),
        ("een nieuwe steekproef geeft meestal een ander interval", J),
    ], "Het interval schat één getal van de populatie."),
    sleep("Een groter betrouwbaarheidsniveau maakt je schatting [[zekerder]] maar ook [[minder nauwkeurig]].",
          ["onzekerder", "nauwkeuriger"], "Een breder net vangt vaker, maar zegt minder precies waar het getal ligt."),
    inv("Twee intervallen: A van 10 tot 14 en B van 15 tot 19. Hoeveel eenheden zit er tussen de bovengrens van A en de ondergrens van B?", ["1"],
        "15 − 14 = 1: ze overlappen niet."),
    keuze("Omdat die intervallen niet overlappen, is er [[*een aanwijzing|geen enkele aanwijzing]] dat de twee populatiegemiddelden verschillen.",
          "Geen overlap wijst op een echt verschil."),
    inv("Een 95%-interval voor een proportie loopt van 0,32 tot 0,40. Wat is de puntschatting? Schrijf als decimaal getal.", ["0,36", "0.36"],
        "Het midden: (0,32 + 0,40) / 2."),
    keuze("Een onderzoeker verlaagt het niveau van 95 naar 90 procent zonder de steekproef te veranderen. Het interval wordt [[*smaller|breder|even breed]].",
          "Minder zekerheid vraagt een smaller net."),
    tabel("Ligt de waarde uit H₀ binnen het interval van 2,1 tot 2,9?", [
        ("H₀: μ = 2,5", J),
        ("H₀: μ = 3", F),
        ("H₀: μ = 2", F),
    ], "Binnen het interval: H₀ niet verwerpen. Erbuiten: wel verwerpen."),
    mk("Waarom zegt een smal interval niets over of de steekproef representatief was?",
       ["de breedte hangt van n af, niet van hoe je koos",
        "omdat een smal interval altijd fout berekend is",
        "omdat representatief enkel bij proporties bestaat",
        "omdat het niveau dan automatisch 99 procent is"], 0,
       "Een grote maar scheve steekproef geeft een smal interval rond een verkeerde waarde."),
    inv("Een interval loopt van 70 tot 82. Hoe breed is het?", ["12"], "82 − 70 = 12."),
    keuze("De foutenmarge van dat interval is dan [[*6|12|76]].", "De helft van 12."),
    met_prent(TI.bestand, keuze("Steekproef 7 is [[*geen rekenfout|een rekenfout]]: bij 95 procent mag af en toe een interval μ missen.",
              "Gemiddeld één op de twintig intervallen mist μ.")),
    volgorde("Zet de stappen om uit een interval de schatting en de marge te halen in de juiste volgorde.", [
        "de onder- en bovengrens aflezen",
        "de breedte berekenen als bovengrens min ondergrens",
        "de marge berekenen als de helft van de breedte",
        "de schatting berekenen als ondergrens plus marge",
    ], "Zo vind je het midden en de afstand tot de grenzen."),
    open_("Een krant meldt: 'Uit onze peiling blijkt dat 51 procent voor het plan is (marge 4 procent). Een meerderheid is dus voor.' Wat is er mis?",
          "Het interval loopt van 47 tot 55 procent. Ook waarden onder 50 procent zijn aannemelijk, dus mag je niet besluiten dat een meerderheid voor is."),
]
