r"""Datasets verwerken met ICT — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en een eigen rekenblad, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Rekenblad met een dataset en vijf berekende kengetallen zonder naam ------------------------
RB = Prent("rekenblad-kengetallen", "Rekenblad met een dataset en vijf berekende kengetallen", "een rekenblad: in kolom A de waarden 6, 9, 9, 10, 12, 14, 15, 18, 23 (rijen 2 tot 10); in kolom D vijf berekende getallen zonder naam: D2 = 12,89, D3 = 5,25, D4 = 12, D5 = 9, D6 = 16,5")
X0, Y0, KB, RH = 140, 80, 150, 46
KOL = ["", "A", "B", "C", "D", "E"]
BREED = [60, KB, KB, KB, KB, KB]
xs = [X0]
for b in BREED[:-1]:
    xs.append(xs[-1] + b)
for j, k in enumerate(KOL):
    RB.rect(xs[j], Y0, BREED[j], RH, "#ecebe6", "#9aa39a", 0, 1)
    RB.tekst(xs[j] + BREED[j] / 2, Y0 + 31, k, 18, "middle", "#5c6356", True)
DATA = {1: "waarde", 2: "6", 3: "9", 4: "9", 5: "10", 6: "12", 7: "14", 8: "15", 9: "18", 10: "23"}
UIT = {2: "12,89", 3: "5,25", 4: "12", 5: "9", 6: "16,5"}
for r in range(1, 11):
    y = Y0 + r * RH
    RB.rect(xs[0], y, BREED[0], RH, "#ecebe6", "#9aa39a", 0, 1)
    RB.tekst(xs[0] + 30, y + 31, str(r), 18, "middle", "#5c6356", True)
    for j in range(1, 6):
        RB.rect(xs[j], y, BREED[j], RH, "#ffffff", "#c9cdc4", 0, 1)
    if r in DATA:
        RB.tekst(xs[1] + KB - 14, y + 31, DATA[r], 20, "end", DONKER, r == 1)
    if r in UIT:
        RB.tekst(xs[4] + KB - 14, y + 31, UIT[r], 20, "end")


def cel_d(r):
    return [Prent.zone(xs[4], Y0 + r * RH, KB, RH)]


VRAGEN = [
    klik("Klik op de cel met de mediaan van de dataset.", RB.bestand, cel_d(4),
         "Negen waarden: de vijfde is 12."),
    klik("Klik op de cel met het gemiddelde.", RB.bestand, cel_d(2),
         "116 / 9 ≈ 12,89."),
    klik("Klik op de cel met het derde kwartiel.", RB.bestand, cel_d(6),
         "Bovenste helft zonder mediaan: 14, 15, 18, 23. (15 + 18) / 2 = 16,5."),
    klik("Klik op de cel met de steekproefstandaardafwijking s.", RB.bestand, cel_d(3),
         "De enige spreidingsmaat tussen de vijf getallen."),
    met_prent(RB.bestand, inv("Hoeveel is de interkwartielafstand van deze dataset? Schrijf als decimaal getal.", ["7,5", "7.5"],
              "16,5 − 9 = 7,5.")),
    met_prent(RB.bestand, inv("Hoeveel is de variatiebreedte?", ["17"], "23 − 6 = 17.")),
    met_prent(RB.bestand, keuze("Het gemiddelde ligt [[*iets boven|iets onder|precies op]] de mediaan, door de grote waarde 23.",
              "12,89 tegenover 12.")),
    met_prent(RB.bestand, keuze("Is 23 een uitschieter volgens de vuistregel? [[*nee, de grens is 27,75|ja, de grens is 20|ja, want 23 is de grootste]]",
              "16,5 + 1,5 · 7,5 = 27,75.")),
    inv("Bereken met ICT de steekproefstandaardafwijking s van 2, 5, 7, 8, 8, 11, 12, 15. Rond af op twee decimalen.", ["4,11", "4.11"],
        "Met de steekproefversie (delen door n − 1)."),
    inv("Bereken de mediaan van 2, 5, 7, 8, 8, 11, 12, 15.", ["8"], "Het gemiddelde van de 4de en 5de waarde: 8 en 8."),
    inv("Bereken het gemiddelde van 2, 5, 7, 8, 8, 11, 12, 15. Schrijf als decimaal getal.", ["8,5", "8.5"], "68 / 8 = 8,5."),
    casus(
        "Een leerling meet de batterij van haar gsm. Ze zet in een rekenblad het aantal uren gebruik (x) en het percentage dat nog over is (y): "
        "x: 2, 4, 5, 7, 9, 10 en y: 30, 27, 25, 20, 17, 14.",
        [
            inv("Bereken r op twee decimalen.", ["-1,00", "-1.00", "-1", "-1,0"],
                "Het rekenblad geeft ongeveer −0,996."),
            inv("Bereken de richtingscoëfficiënt van de trendlijn op twee decimalen.", ["-2,01", "-2.01"],
                "y ≈ −2,01x + 34,57."),
            keuze("Volgens het formularium is dit een [[*sterke negatieve|matige negatieve|sterke positieve]] samenhang.",
                  "|r| is groter dan 0,7 en r is negatief."),
            inv("Welk percentage voorspelt de trendlijn y = −2,01x + 34,57 na 6 uur gebruik? Rond af op één decimaal.", ["22,5", "22.5"],
                "−2,01 · 6 + 34,57 = 22,51."),
        ],
    ),
    inv("x: 1 tot en met 8. y: 3, 6, 5, 9, 10, 12, 13, 17. Bereken r op twee decimalen.", ["0,98", "0.98"],
        "Het rekenblad geeft ongeveer 0,977."),
    inv("Bij diezelfde acht paren: hoeveel is de richtingscoëfficiënt van de trendlijn op twee decimalen?", ["1,85", "1.85"],
        "y ≈ 1,85x + 1,07."),
    tabel("Verandert dit als je de kolommen x en y van plaats wisselt?", [
        ("de correlatiecoëfficiënt r", "blijft gelijk"),
        ("de vergelijking van de trendlijn", "verandert"),
        ("het aantal punten in het spreidingsdiagram", "blijft gelijk"),
    ], "r is symmetrisch, de trendlijn voorspelt y uit x.", kolommen=["blijft gelijk", "verandert"]),
    keuze("Bij de standaardafwijking van een steekproef kies je in het rekenblad de versie die deelt door [[*n − 1|n|n + 1]].",
          "De steekproefversie s."),
    sorteer("Gebruik je hiervoor de steekproefversie of de populatieversie van de standaardafwijking?", ["steekproef (s)", "populatie (σ)"], [
        ["de lengte van 50 willekeurige leerlingen van een school van 900", "steekproef (s)"],
        ["de punten van alle 22 leerlingen van jouw klas, enkel over die klas", "populatie (σ)"],
        ["de wachttijd van 120 bezoekers van een pretpark", "steekproef (s)"],
        ["de leeftijd van alle 11 spelers van een ploeg, enkel over die ploeg", "populatie (σ)"],
    ], "Beschrijf je de hele groep zelf, dan is het een populatie."),
    volgorde("Zet de stappen om een trendlijn met het rekenblad te bepalen in de juiste volgorde.", [
        "x en y in twee kolommen zetten",
        "beide kolommen selecteren",
        "een spreidingsdiagram invoegen",
        "de trendlijn met vergelijking laten tonen",
    ], "Eerst de punten, dan de lijn."),
    mk("Het rekenblad geeft bij een dataset van 9 getallen s = 5,25 en σ = 4,95. Hoe kan dat?",
       ["s deelt door n − 1, σ door n",
        "het rekenblad heeft zich vergist",
        "σ gebruikt enkel de middelste helft van de data",
        "s rondt de waarden eerst af op een geheel getal"], 0,
       "Door n − 1 delen geeft een iets grotere waarde."),
    koppel("Koppel de berekening aan wat je in het rekenblad selecteert.", [
        ["gemiddelde van één variabele", "één kolom"],
        ["correlatiecoëfficiënt", "twee kolommen"],
        ["kansverdeling B(n; p)", "geen kolom, enkel n en p"],
    ], ["drie kolommen"], "Wat je nodig hebt, hangt af van de berekening."),
    keuze("Een rekenblad geeft r = 1,08. Dat is [[*onmogelijk, je las iets anders af|een heel sterk verband|een zwak verband]].",
          "r ligt altijd tussen −1 en 1."),
    met_prent(RB.bestand, keuze("Om het gemiddelde te berekenen, selecteer je in het rekenblad de cellen [[*A2 tot A10|A1 tot A10|D2 tot D6]].",
              "Enkel de waarden, niet de kop in A1.")),
    met_prent(RB.bestand, inv("Hoeveel is de som van de waarden in kolom A?", ["116"],
              "6 + 9 + 9 + 10 + 12 + 14 + 15 + 18 + 23 = 116.")),
    met_prent(RB.bestand, keuze("Komt er een tiende waarde 40 bij, dan [[*stijgt|daalt|blijft]] de mediaan van 12 naar 13.",
              "Tien waarden: (12 + 14) / 2 = 13.")),
    tabel("Mag je dit afronden tijdens het rekenen?", [
        ("een tussenresultaat dat je nog verder gebruikt", F),
        ("het eindantwoord, op het gevraagde aantal decimalen", J),
        ("een breuk als 1/3 in een volgende stap", F),
    ], "Rond pas op het einde af, zo vermijd je afrondingsfouten."),
    inv("Een trendlijn is y = 1,85x + 1,07. Welke y voorspelt ze bij x = 6? Rond af op twee decimalen.", ["12,17", "12.17"],
        "1,85 · 6 + 1,07 = 12,17."),
    open_("Een leerling geeft als antwoord enkel '4,11' bij de vraag naar de standaardafwijking van een dataset. Wat ontbreekt er voor een volledig antwoord op het examen?",
          "Hij moet ook noteren welke berekening hij met welk hulpmiddel deed: welke gegevens hij invoerde, dat hij de steekproefstandaardafwijking s koos, en het antwoord met de juiste eenheid."),
]
