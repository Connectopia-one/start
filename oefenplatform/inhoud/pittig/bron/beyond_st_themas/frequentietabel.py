r"""Frequentietabellen, ook gegroepeerd — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en een eigen frequentietabel met één fout, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Frequentietabel van toetsscores (40 leerlingen), met één foute cel --------------------------
FT = Prent("frequentietabel-scores", "Scores op tien van 40 leerlingen", "een frequentietabel met vier kolommen (score, absolute frequentie, relatieve frequentie, cumulatieve frequentie) en vijf rijen voor de scores 5 tot 9; absolute frequenties 4, 6, 10, 12, 8; relatieve 10 %, 15 %, 25 %, 30 %, 20 %; cumulatieve 4, 10, 20, 30, 40")
KOP = ["score", "absolute freq.", "relatieve freq.", "cumulatieve freq."]
RIJEN = [("5", "4", "10 %", "4"), ("6", "6", "15 %", "10"), ("7", "10", "25 %", "20"),
         ("8", "12", "30 %", "30"), ("9", "8", "20 %", "40")]
X0, Y0, KB, RH = 120, 110, 190, 70
FT.rect(X0, Y0, 4 * KB, RH, "#dfe9d5", DONKER, 0, 2)
for j, k in enumerate(KOP):
    FT.tekst(X0 + j * KB + KB / 2, Y0 + 43, k, 19, "middle", DONKER, True)
for i, r in enumerate(RIJEN):
    y = Y0 + (i + 1) * RH
    FT.rect(X0, y, 4 * KB, RH, "#ffffff", DONKER, 0, 2)
    for j, w in enumerate(r):
        FT.tekst(X0 + j * KB + KB / 2, y + 44, w, 22)
for j in range(1, 4):
    FT.lijn(X0 + j * KB, Y0, X0 + j * KB, Y0 + 6 * RH, DONKER, 2)
FT.rect(X0, Y0 + 6 * RH, 4 * KB, RH, "#f4f4f0", DONKER, 0, 2)
FT.tekst(X0 + KB / 2, Y0 + 6 * RH + 44, "totaal", 20, "middle", DONKER, True)
FT.tekst(X0 + KB + KB / 2, Y0 + 6 * RH + 44, "40", 22)
FT.tekst(X0 + 2 * KB + KB / 2, Y0 + 6 * RH + 44, "100 %", 22)
for j in range(1, 3):
    FT.lijn(X0 + j * KB, Y0 + 6 * RH, X0 + j * KB, Y0 + 7 * RH, DONKER, 2)


def cel(rij, kol):
    return [Prent.zone(X0 + kol * KB, Y0 + rij * RH, KB, RH)]


VRAGEN = [
    klik("In deze tabel staat één foute cel. Klik erop.", FT.bestand, cel(4, 3),
         "Tot en met 8: 4 + 6 + 10 + 12 = 32, niet 30."),
    klik("Klik op de cel die zegt hoeveel leerlingen hoogstens 7 haalden.", FT.bestand, cel(3, 3),
         "De cumulatieve frequentie bij score 7: 20 leerlingen."),
    klik("Klik op de cel die toont welk deel van de klas precies 6 haalde.", FT.bestand, cel(2, 2),
         "De relatieve frequentie bij score 6."),
    met_prent(FT.bestand, inv("Hoeveel leerlingen haalden minstens 8?", ["20"],
              "12 + 8 = 20.")),
    met_prent(FT.bestand, inv("Hoeveel procent haalde hoogstens 6?", ["25", "25%", "25 procent"],
              "10 % + 15 % = 25 %.")),
    met_prent(FT.bestand, keuze("De modus van deze scores is [[*8|7|12]].",
              "De score met de grootste absolute frequentie.")),
    met_prent(FT.bestand, keuze("De mediaan van de 40 scores is [[*7,5|7|8]].",
              "De 20ste score is een 7 en de 21ste een 8 (de cumulatieve frequentie bij 7 is 20).")),
    tabel("Vul de ontbrekende waarde in. Dataset van 50 gegevens.", [
        ("absolute frequentie 15: relatieve frequentie in procent", "30"),
        ("relatieve frequentie 8 procent: absolute frequentie", "4"),
        ("absolute frequentie 20: relatieve frequentie in procent", "40"),
    ], "Relatief = absoluut / totaal.", kolommen=["30", "4", "40"]),
    casus(
        "Een sportclub noteert de leeftijd van 60 leden in klassen: [10, 20[ heeft 9 leden, [20, 30[ heeft 18, "
        "[30, 40[ heeft 15, [40, 50[ heeft 12 en [50, 60[ de rest.",
        [
            inv("Hoeveel leden zitten in de klasse [50, 60[?", ["6"], "60 − 9 − 18 − 15 − 12 = 6."),
            inv("Wat is het klassenmidden van [30, 40[?", ["35"], "(30 + 40) / 2."),
            inv("Hoeveel procent van de leden is jonger dan 30?", ["45", "45%", "45 procent"],
                "(9 + 18) / 60 = 0,45."),
            keuze("De klassenbreedte is [[*10|5|60]].", "Elke klasse is 10 jaar breed."),
            mk("Kan je uit deze tabel afleiden hoeveel leden precies 25 jaar zijn?",
               ["nee, binnen een klasse ken je de waarden niet",
                "ja, dat is 18 gedeeld door 10, dus ongeveer 2",
                "ja, want 25 is het klassenmidden van [20, 30[",
                "ja, dat is de cumulatieve frequentie van [20, 30["], 0,
               "Groeperen kost informatie: de afzonderlijke waarden zijn weg."),
        ],
    ),
    inv("Een gegroepeerde tabel: [0, 10[ met frequentie 5, [10, 20[ met 10 en [20, 30[ met 5. Bereken het gemiddelde met de klassenmiddens.", ["15"],
        "(5 · 5 + 15 · 10 + 25 · 5) / 20 = 300 / 20 = 15."),
    tabel("Zijn deze klassen goed gekozen voor een continue variabele?", [
        ("[0, 5[, [5, 10[, [10, 15[", J),
        ("0–5, 5–10, 10–15 (grenzen in beide klassen)", F),
        ("0–4, 5–9, 10–14 (gaten tussen de klassen)", F),
    ], "Elke waarde moet in precies één klasse vallen, zonder overlap en zonder gaten."),
    sorteer("Groepeer je deze variabele in klassen?", ["groeperen", "niet groeperen"], [
        ["het gewicht van 800 pasgeboren baby's", "groeperen"],
        ["het aantal huisdieren per gezin", "niet groeperen"],
        ["het inkomen van 5000 werknemers", "groeperen"],
        ["de lievelingskleur van leerlingen", "niet groeperen"],
    ], "Groeperen helpt bij veel verschillende numerieke waarden."),
    keuze("De laatste cumulatieve frequentie is altijd gelijk aan [[*het totale aantal gegevens|de grootste absolute frequentie|100]].",
          "Tot en met de laatste waarde tel je alles."),
    inv("Cumulatieve frequenties: 7, 19, 34, 42, 50. Wat is de absolute frequentie van de derde waarde?", ["15"],
        "34 − 19 = 15."),
    inv("Bij diezelfde cumulatieve frequenties: hoeveel procent van de gegevens zit in de eerste twee waarden?", ["38", "38%", "38 procent"],
        "19 / 50 = 0,38."),
    koppel("Koppel elke kolom aan wat ze toont.", [
        ["absolute frequentie", "hoe vaak een waarde voorkomt"],
        ["relatieve frequentie", "welk deel van het geheel een waarde vormt"],
        ["cumulatieve frequentie", "hoeveel gegevens tot en met een waarde"],
    ], ["het gemiddelde van de klassengrenzen"], "Drie kolommen in een frequentietabel."),
    mk("School A heeft 30 leerlingen met een fiets van 120, school B 45 van 300. Waar fietst het grootste deel?",
       ["school A", "school B", "evenveel", "dat kan je niet zeggen"], 0,
       "A: 25 procent, B: 15 procent. Vergelijk relatieve frequenties."),
    volgorde("Zet de stappen om een gegroepeerde frequentietabel op te stellen in de juiste volgorde.", [
        "kleinste en grootste waarde opzoeken",
        "het aantal klassen en de klassenbreedte kiezen",
        "elke waarde in haar klasse tellen",
        "relatieve en cumulatieve frequenties berekenen",
    ], "Eerst het bereik, dan de klassen, dan tellen."),
    sleep("Het [[klassenmidden]] van [60, 80[ is 70. De [[klassenbreedte]] is 20.",
          ["modus", "frequentie"], "Twee begrippen bij gegroepeerde tabellen."),
    tabel("Klopt dit over frequentietabellen?", [
        ("relatieve frequenties zijn samen 100 procent", J),
        ("een absolute frequentie kan 2,5 zijn", F),
        ("een lege klasse mag in een gegroepeerde tabel staan", J),
    ], "Absolute frequenties zijn aantallen; een lege klasse is ook informatie."),
    inv("Een waarde heeft relatieve frequentie 0,15 in een dataset van 240 gegevens. Wat is haar absolute frequentie?", ["36"],
        "0,15 · 240 = 36."),
    met_prent(FT.bestand, inv("Wat moet de foute cel zijn?", ["32"],
              "4 + 6 + 10 + 12 = 32.")),
    met_prent(FT.bestand, inv("Bereken het gemiddelde van de 40 scores. Schrijf als decimaal getal.", ["7,3", "7.3"],
              "(5 · 4 + 6 · 6 + 7 · 10 + 8 · 12 + 9 · 8) / 40 = 292 / 40 = 7,3.")),
    keuze("Met 3 klassen ziet een histogram er [[*grover|fijner]] uit dan met 12 klassen voor dezelfde gegevens.",
          "Het aantal klassen bepaalt hoeveel detail je ziet."),
    inv("Een klasse loopt van 145 tot 160. Wat is het klassenmidden? Schrijf als decimaal getal.", ["152,5", "152.5"],
        "(145 + 160) / 2 = 152,5."),
    open_("Een leerling maakt een tabel met relatieve frequenties 22 %, 31 %, 18 % en 26 %. Wat besluit je en wat moet hij doen?",
          "Samen geeft dat 97 procent in plaats van 100 procent. Er zit dus een fout in: hij moet zijn telling of zijn delingen nakijken, of nagaan of er een waarde ontbreekt."),
]
