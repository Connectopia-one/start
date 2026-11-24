"""Vraag, aanbod en het marktevenwicht — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen grafiek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, BLAUW, ORANJE, assen

# Een markt met twee curven en vier punten -------------------------------------------
MG = Prent("markt-grafiek", "De markt voor sportdrank (per week)", "een vraag- en aanbodgrafiek: prijs in euro (0 tot 12) verticaal, hoeveelheid in flessen (0 tot 300) horizontaal; een dalende curve K en een stijgende curve L die elkaar snijden in E bij 7 euro en 125 flessen; stippellijnen bij 9 euro (punten A op K en B op L) en bij 5 euro (punten D op L en C op K)")
X, Y = assen(MG, 0, 300, 0, 12, "hoeveelheid (flessen)", "prijs (euro)", 50, 1, links=110, rechts=900)
MG.lijn(X(0), Y(12), X(300), Y(0), BLAUW, 4)          # K: Q = 300 - 25P
MG.lijn(X(0), Y(2), X(250), Y(12), ORANJE, 4)          # L: Q = 25P - 50
MG.tekst(X(20) + 10, Y(11.2), "K", 22, "start", BLAUW, True)
MG.tekst(X(250) + 12, Y(12) + 20, "L", 22, "start", ORANJE, True)
for p in (9, 5):
    MG.lijn(X(0), Y(p), X(300), Y(p), DONKER, 2, True)
PUNT = {"A": (75, 9), "B": (175, 9), "C": (175, 5), "D": (75, 5), "E": (125, 7)}
for k, (q, p) in PUNT.items():
    MG.cirkel(X(q), Y(p), 7, DONKER, DONKER, 1)
    MG.letter(X(q) + (28 if k in "BCE" else -28), Y(p) - 24, k)
ZM = {k: [Prent.rond(X(q), Y(p), 40)] for k, (q, p) in PUNT.items()}

VRAGEN = [
    klik("Klik op het marktevenwicht.", MG.bestand, ZM["E"],
         "Waar vraag en aanbod elkaar snijden, is de markt in evenwicht."),
    klik("De prijs is 9 euro. Klik op het punt dat toont hoeveel flessen de kopers willen kopen.", MG.bestand, ZM["A"],
         "K is de dalende vraagcurve. Bij 9 euro willen kopers 75 flessen."),
    klik("De prijs is 5 euro. Klik op het punt dat toont hoeveel flessen de verkopers aanbieden.", MG.bestand, ZM["D"],
         "L is de stijgende aanbodcurve. Bij 5 euro bieden verkopers maar 75 flessen aan."),
    met_prent(MG.bestand, keuze("Curve K is de [[*vraagcurve|aanbodcurve]], want ze [[*daalt|stijgt]] als de prijs stijgt.",
              "Hoe duurder, hoe minder kopers willen kopen.")),
    met_prent(MG.bestand, inv("Lees de evenwichtsprijs af, in euro.", ["7", "7 euro"], "Het snijpunt E ligt bij 7 euro.")),
    met_prent(MG.bestand, inv("Hoe groot is de evenwichtshoeveelheid, in flessen?", ["125", "125 flessen"],
              "Bij 7 euro wordt 125 flessen verhandeld.")),
    met_prent(MG.bestand, inv("Hoe groot is het overschot bij een prijs van 9 euro, in flessen?", ["100", "100 flessen"],
              "Aanbod min vraag: 175 min 75 is 100 flessen.")),
    met_prent(MG.bestand, tabel("Kijk naar de grafiek. Klopt dit?", [
        ("Bij 5 euro is er een tekort.", J),
        ("Bij 9 euro blijven er flessen onverkocht.", J),
        ("Bij 7 euro is er een overschot van 50 flessen.", F),
        ("Als de prijs vrij is, zakt ze van 9 euro naar 7 euro.", J),
    ], "Boven het evenwicht een overschot, eronder een tekort. Zonder ingrijpen schuift de prijs naar het evenwicht.")),
    casus(
        "Op de wekelijkse markt verkoopt Fatima aardbeien. De tabel geeft vraag en aanbod "
        "per prijs: bij 3 euro per bakje vragen de kopers 260 bakjes en bieden de verkopers "
        "140 aan; bij 4 euro 200 en 200; bij 5 euro 150 en 250; bij 6 euro 110 en 290.",
        [
            inv("Wat is de evenwichtsprijs, in euro?", ["4", "4 euro"], "Bij 4 euro zijn vraag en aanbod allebei 200."),
            inv("Hoe groot is het tekort bij 3 euro, in bakjes?", ["120", "120 bakjes"], "Vraag min aanbod: 260 min 140."),
            inv("Hoe groot is het overschot bij 6 euro, in bakjes?", ["180", "180 bakjes"], "Aanbod min vraag: 290 min 110."),
            mk("Fatima vraagt 5 euro en houdt elke avond bakjes over. Wat doet ze best?",
               ["Haar prijs verlagen richting 4 euro",
                "Haar prijs verhogen naar 6 euro",
                "Meer bakjes aanbieden aan dezelfde prijs",
                "Niets, want bij 5 euro is de markt in evenwicht"], 0,
               "Een overschot duwt de prijs naar beneden, tot het evenwicht."),
        ],
    ),
    tabel("Is er bij deze prijs een overschot, een tekort of evenwicht?", [
        ("vraag 120, aanbod 200", "overschot"),
        ("vraag 300, aanbod 180", "tekort"),
        ("vraag 150, aanbod 150", "evenwicht"),
        ("vraag 90, aanbod 60", "tekort"),
    ], "Aanbod groter dan vraag: overschot. Vraag groter dan aanbod: tekort.",
       kolommen=["overschot", "tekort", "evenwicht"]),
    sorteer("Ligt deze prijs boven of onder de evenwichtsprijs?", ["Boven", "Onder"], [
        ["een bakker heeft elke avond brood over", "Boven"],
        ["concerttickets zijn binnen twee minuten uitverkocht", "Onder"],
        ["een winkel stuurt al om tien uur klanten weg", "Onder"],
        ["een marktkramer houdt kratten groenten over", "Boven"],
    ], "Een overschot wijst op een te hoge prijs, een tekort op een te lage."),
    koppel("Koppel elk begrip aan zijn betekenis.", [
        ["vrager", "de koper"],
        ["aanbieder", "de verkoper"],
        ["evenwichtsprijs", "de prijs waarbij vraag en aanbod gelijk zijn"],
        ["productmarkt", "de markt van goederen en diensten"],
    ], ["de prijs die de overheid vastlegt"], "Vrager en aanbieder ontmoeten elkaar op de markt."),
    mk("Bij 6 euro vragen de kopers 100 stuks en bieden de verkopers 180 aan. Wat gebeurt er zonder ingrijpen?",
       ["De prijs zakt",
        "De prijs stijgt tot iedereen gekocht heeft",
        "De prijs blijft op 6 euro staan",
        "De verkopers bieden nog meer aan"], 0,
       "Er is een overschot van 80 stuks; verkopers laten de prijs zakken."),
    keuze("Op de verticale as van een vraag- en aanbodgrafiek staat de [[*prijs|hoeveelheid|omzet]].",
          "De hoeveelheid staat op de horizontale as."),
    tabel("Klopt dit?", [
        ("Een tekort bereken je als vraag min aanbod.", J),
        ("Bij één prijs kan er tegelijk een overschot en een tekort zijn.", F),
        ("Bij een tekort stijgt de prijs.", J),
        ("De vrager is de verkoper.", F),
    ], "Bij één prijs is het één van de twee, of evenwicht."),
    sleep("Als de prijs stijgt, [[daalt]] de gevraagde hoeveelheid en [[stijgt]] de aangeboden hoeveelheid.",
          ["blijft", "verdubbelt"], "Daarom daalt de vraagcurve en stijgt de aanbodcurve."),
    volgorde("Een prijs ligt onder het evenwicht. Zet de gevolgen in de juiste volgorde.", [
        "veel kopers willen kopen, weinig verkopers bieden aan",
        "er ontstaat een tekort",
        "kopers zijn bereid meer te betalen",
        "de prijs stijgt naar het evenwicht",
    ], "Zonder ingrijpen herstelt de markt zelf het evenwicht."),
    inv("Bij 8 euro is de vraag 90 en het aanbod 230. Hoe groot is het overschot?", ["140"], "230 min 90."),
    mk("Waarom bieden verkopers meer aan bij een hogere prijs?",
       ["Verkopen wordt dan interessanter",
        "Kopers willen dan meer kopen",
        "De overheid verplicht hen dat",
        "De productiekosten dalen altijd mee"], 0,
       "Een hogere prijs dekt beter de kosten en levert meer op."),
    klik("Klik op het punt dat toont hoeveel flessen de kopers willen bij een prijs van 5 euro.", MG.bestand, ZM["C"],
         "Op de vraagcurve K bij 5 euro: 175 flessen."),
    met_prent(MG.bestand, inv("Hoe groot is het tekort bij 5 euro, in flessen?", ["100", "100 flessen"],
              "Vraag min aanbod: 175 min 75.")),
    met_prent(MG.bestand, tabel("Welk punt hoort bij deze uitspraak?", [
        ("het aanbod bij 9 euro", "B"),
        ("de vraag bij 9 euro", "A"),
        ("vraag en aanbod zijn gelijk", "E"),
    ], "K is de vraagcurve, L de aanbodcurve.", kolommen=["A", "B", "E"])),
    mk("Bij 12 euro vragen de kopers 40 stuks en bieden de verkopers ook 40 stuks aan. Wat besluit je?",
       ["Er is geen overschot en geen tekort",
        "Er is een overschot van 40 stuks",
        "Er is een tekort van 80 stuks",
        "Dat kan je niet weten zonder grafiek"], 0,
       "Vraag en aanbod zijn gelijk: dat is het evenwicht."),
    sorteer("Beweegt de gevraagde of de aangeboden hoeveelheid mee met de prijs, of ertegen in?", ["In dezelfde richting als de prijs", "In de omgekeerde richting"], [
        ["de aangeboden hoeveelheid", "In dezelfde richting als de prijs"],
        ["de gevraagde hoeveelheid", "In de omgekeerde richting"],
        ["het aantal flessen dat producenten willen verkopen", "In dezelfde richting als de prijs"],
        ["het aantal flessen dat kopers willen", "In de omgekeerde richting"],
    ], "Aanbod stijgt mee met de prijs, vraag daalt."),
    keuze("Als vraag en aanbod gelijk zijn, blijft er [[*geen|veel]] onverkochte voorraad over.",
          "Bij de evenwichtsprijs is er geen overschot en geen tekort."),
    tabel("Welk punt uit de casus van Fatima past?", [
        ("3 euro per bakje", "tekort"),
        ("4 euro per bakje", "evenwicht"),
        ("6 euro per bakje", "overschot"),
    ], "Onder 4 euro een tekort, erboven een overschot.", kolommen=["tekort", "evenwicht", "overschot"]),
    open_("Leg uit waarom de prijs op een vrije markt naar het evenwicht beweegt, zowel vanuit een te hoge als vanuit een te lage prijs.",
          "Bij een te hoge prijs is er een overschot: verkopers houden voorraad over en laten de prijs zakken. Bij een te lage prijs is er een tekort: kopers willen meer betalen om toch iets te krijgen, en de prijs stijgt. In beide gevallen eindigt de prijs waar vraag en aanbod gelijk zijn."),
]
