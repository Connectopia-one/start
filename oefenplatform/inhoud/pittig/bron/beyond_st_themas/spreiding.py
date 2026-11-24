r"""Spreidingsmaten en boxplots — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en twee eigen boxplots, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Twee boxplots op één schaal --------------------------------------------------------------
BP = Prent("twee-boxplots", "Punten op 20 in klas A en klas B", "twee horizontale boxplots op een as van 0 tot 20; klas A: minimum 4, Q1 8, mediaan 12, Q3 15, maximum 19; klas B: minimum 7, Q1 10, mediaan 11, Q3 12, bovenste snorhaar tot 14 en een los punt bij 19")
L, R = 170, 900


def X(v):
    return L + (R - L) * v / 20


AS = 540
BP.lijn(L, AS, R, AS, DONKER, 3)
for v in range(0, 21, 2):
    BP.lijn(X(v), AS, X(v), AS + 10, DONKER, 2)
    BP.tekst(X(v), AS + 34, str(v), 18)
BP.tekst((L + R) / 2, 615, "punt op 20", 18, "middle", "#5c6356")


def boxplot(y, mn, q1, me, q3, mx, label, uit=None):
    BP.tekst(L - 30, y + 7, label, 22, "end", DONKER, True)
    BP.lijn(X(mn), y, X(q1), y, DONKER, 3)
    BP.lijn(X(q3), y, X(mx), y, DONKER, 3)
    BP.lijn(X(mn), y - 20, X(mn), y + 20, DONKER, 3)
    BP.lijn(X(mx), y - 20, X(mx), y + 20, DONKER, 3)
    BP.rect(X(q1), y - 45, X(q3) - X(q1), 90, "#c4d5b5", DONKER, 0, 3)
    BP.lijn(X(me), y - 45, X(me), y + 45, DONKER, 4)
    if uit is not None:
        BP.cirkel(X(uit), y, 9, "#ffffff", DONKER, 3)


YA, YB = 180, 390
boxplot(YA, 4, 8, 12, 15, 19, "klas A")
boxplot(YB, 7, 10, 11, 12, 14, "klas B", 19)

Z_A = [Prent.zone(L - 140, YA - 70, R - L + 160, 140)]
Z_B = [Prent.zone(L - 140, YB - 70, X(16) - L + 140, 140)]
Z_UIT = [Prent.zone(X(19) - 30, YB - 30, 60, 60)]
Z_MED_B = [Prent.zone(X(11) - 12, YB - 55, 24, 110)]
Z_Q1_A = [Prent.zone(X(8) - 12, YA - 55, 24, 110)]

VRAGEN = [
    klik("Klik op de uitschieter.", BP.bestand, Z_UIT,
         "Het losse punt bij 19 in klas B."),
    klik("Klik op de mediaan van klas B.", BP.bestand, Z_MED_B,
         "De dikke streep in de doos, bij 11."),
    klik("Klik op het eerste kwartiel van klas A.", BP.bestand, Z_Q1_A,
         "De linkerkant van de doos, bij 8."),
    klik("Klik op de boxplot van de klas waar de middelste helft van de punten het verst uit elkaar ligt.", BP.bestand, Z_A,
         "De doos van A is breder: interkwartielafstand 7 tegenover 2."),
    met_prent(BP.bestand, inv("Wat is de interkwartielafstand van klas A?", ["7"], "15 − 8 = 7.")),
    met_prent(BP.bestand, inv("Wat is de variatiebreedte van klas B, met de uitschieter erbij?", ["12"], "19 − 7 = 12.")),
    met_prent(BP.bestand, inv("Boven welke waarde is een punt in klas B een uitschieter?", ["15"],
              "Q3 + 1,5 · IKA = 12 + 1,5 · 2 = 15.")),
    met_prent(BP.bestand, keuze("Ongeveer [[*25|50|75]] procent van klas A haalde minder dan 8.",
              "Onder Q1 ligt een kwart.")),
    met_prent(BP.bestand, keuze("Ongeveer [[*50|25|75]] procent van klas B haalde tussen 10 en 12.",
              "Tussen Q1 en Q3 ligt de middelste helft.")),
    met_prent(BP.bestand, tabel("Klopt dit voor deze twee boxplots?", [
        ("de mediaan van A is hoger dan die van B", J),
        ("klas B telt meer leerlingen dan klas A", F),
        ("de punten van B liggen meer op een hoop dan die van A", J),
    ], "Een boxplot toont posities, geen aantallen.")),
    met_prent(BP.bestand, keuze("Uit de boxplot van A blijkt dat de verdeling [[*een beetje scheef naar links|perfect symmetrisch|sterk scheef naar rechts]] is.",
              "De mediaan (12) ligt rechts van het midden van de doos (11,5): het linkerdeel van de doos is langer.")),
    inv("Bereken de variatiebreedte van 14, 3, 22, 9, 17, 6.", ["19"], "22 − 3 = 19."),
    casus(
        "Gegeven de gerangschikte dataset: 2, 4, 5, 7, 8, 10, 11, 13, 20.",
        [
            inv("Wat is de mediaan?", ["8"], "De vijfde van negen waarden."),
            inv("Wat is Q1? Schrijf als decimaal getal.", ["4,5", "4.5"],
                "Onderste helft zonder mediaan: 2, 4, 5, 7. Gemiddelde van 4 en 5."),
            inv("Wat is Q3? Schrijf als decimaal getal.", ["12"],
                "Bovenste helft: 10, 11, 13, 20. Gemiddelde van 11 en 13."),
            inv("Wat is de interkwartielafstand? Schrijf als decimaal getal.", ["7,5", "7.5"], "12 − 4,5 = 7,5."),
            keuze("Is 20 een uitschieter volgens de vuistregel? [[*nee, de grens is 23,25|ja, want 20 is veel groter dan 13|ja, de grens is 19,5]]",
                  "12 + 1,5 · 7,5 = 23,25."),
        ],
    ),
    tabel("Hoe gevoelig is deze spreidingsmaat voor één extreme waarde?", [
        ("variatiebreedte", "heel gevoelig"),
        ("interkwartielafstand", "weinig gevoelig"),
        ("standaardafwijking", "gevoelig"),
    ], "De variatiebreedte gebruikt enkel de uitersten; de IKA enkel het midden; s alle waarden.",
       kolommen=["heel gevoelig", "gevoelig", "weinig gevoelig"]),
    mk("Dataset P: 10, 10, 10, 10. Dataset Q: 4, 8, 12, 16. Wat klopt?",
       ["P heeft standaardafwijking 0, Q niet",
        "beide hebben dezelfde standaardafwijking",
        "Q heeft standaardafwijking 0, P niet",
        "beide hebben standaardafwijking 10"], 0,
       "Zonder enige spreiding is s = 0; beide hebben wel gemiddelde 10."),
    keuze("Als je bij elke waarde 5 optelt, blijft de standaardafwijking [[*gelijk|5 groter|5 keer zo groot]].",
          "Alles schuift op; de afstanden tot het gemiddelde veranderen niet."),
    keuze("Als je elke waarde verdubbelt, wordt de standaardafwijking [[*2 keer zo groot|4 keer zo groot|niet anders]].",
          "Alle afstanden tot het gemiddelde verdubbelen."),
    sorteer("Hoort dit bij een centrummaat of een spreidingsmaat?", ["centrummaat", "spreidingsmaat"], [
        ["mediaan", "centrummaat"],
        ["interkwartielafstand", "spreidingsmaat"],
        ["modus", "centrummaat"],
        ["standaardafwijking", "spreidingsmaat"],
    ], "Centrum: waar liggen de gegevens? Spreiding: hoe ver uit elkaar?"),
    volgorde("Zet de vijf getallen van een boxplot van klein naar groot.", [
        "minimum", "eerste kwartiel", "mediaan", "derde kwartiel", "maximum",
    ], "Zo lees je een boxplot van links naar rechts."),
    sleep("De doos van een boxplot loopt van [[Q1]] tot [[Q3]]. De lengte van de doos is de [[interkwartielafstand]].",
          ["minimum", "variatiebreedte"], "De middelste helft van de gegevens."),
    inv("Q1 = 24 en Q3 = 36. Onder welke waarde is een punt een uitschieter?", ["6"],
        "24 − 1,5 · 12 = 6."),
    inv("Een dataset heeft gemiddelde 70 en standaardafwijking 4. Hoeveel standaardafwijkingen ligt 82 boven het gemiddelde?", ["3", "drie"],
        "(82 − 70) / 4 = 3."),
    mk("Welke spreidingsmaat kies je best voor de huurprijzen in een stad met enkele peperdure penthouses?",
       ["de interkwartielafstand",
        "de variatiebreedte van alle huurprijzen samen",
        "de standaardafwijking van alle huurprijzen",
        "het verschil tussen gemiddelde en modus"], 0,
       "De IKA kijkt enkel naar de middelste helft en negeert de extreme waarden."),
    met_prent(BP.bestand, keuze("Zonder de uitschieter is de variatiebreedte van klas B [[*7|12|2]].",
              "14 − 7 = 7.")),
    tabel("Kan dit een standaardafwijking zijn?", [
        ("0", J),
        ("−2,5", F),
        ("13,7", J),
    ], "Een standaardafwijking is nooit negatief."),
    open_("Twee klassen hebben allebei gemiddelde 13 op 20. In klas A is s = 1,5 en in klas B is s = 5. Wat zegt dat over de klassen?",
          "In klas A liggen de punten dicht bij 13: de klas is vrij gelijk. In klas B zijn de verschillen groot, met zowel heel lage als heel hoge punten. Hetzelfde gemiddelde verbergt een heel ander beeld."),
]
