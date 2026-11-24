"""Het rekenblad Excel — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen schermafdruk
van een rekenblad, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een klein rekenblad -------------------------------------------------------------------
XL = Prent("excel-rekenblad", "Een rekenblad met schoolmateriaal", "een rekenblad met kolommen A tot D en rijen 1 tot 6; rij 1 Product, Prijs, Aantal, Totaal; Pen 2 10 20; Schrift 3 4 12; Map 5 2 10; Lat 1 6 6; in A6 Som en in D6 48; cel D3 is geselecteerd en de formulebalk toont =B3*C3")
X0, Y0, BK, HR = 160, 150, 180, 62
XL.rect(100, 60, 800, 44, "#f4f4f2", GRIJS, 4, 1)
XL.tekst(120, 89, "fx", 18, "start", DONKER, True)
XL.tekst(170, 89, "=B3*C3", 20, "start")
for j, kol in enumerate("ABCD"):
    XL.rect(X0 + j * BK, Y0 - 36, BK, 36, "#ecebe6", GRIJS, 0, 1)
    XL.tekst(X0 + j * BK + BK / 2, Y0 - 11, kol, 18)
DATA = [["Product", "Prijs", "Aantal", "Totaal"], ["Pen", "2", "10", "20"], ["Schrift", "3", "4", "12"],
        ["Map", "5", "2", "10"], ["Lat", "1", "6", "6"], ["Som", "", "", "48"]]
for i, rij in enumerate(DATA):
    y = Y0 + i * HR
    XL.rect(110, y, 50, HR, "#ecebe6", GRIJS, 0, 1)
    XL.tekst(135, y + 38, str(i + 1), 18)
    for j, w in enumerate(rij):
        sel = (i == 2 and j == 3)
        XL.rect(X0 + j * BK, y, BK, HR, "#ffffff", DONKER if sel else GRIJS, 0, 4 if sel else 1)
        if w:
            vet = i == 0 or (i == 5 and j in (0, 3))
            if j == 0 or i == 0:
                XL.tekst(X0 + j * BK + 12, y + 38, w, 20, "start", DONKER, vet)
            else:
                XL.tekst(X0 + j * BK + BK - 14, y + 38, w, 20, "end", DONKER, vet)


def cel(adres):
    j, i = "ABCD".index(adres[0]), int(adres[1:]) - 1
    return [Prent.zone(X0 + j * BK, Y0 + i * HR, BK, HR)]


VRAGEN = [
    klik("Klik op de cel met het resultaat van =MAX(D2:D5).", XL.bestand, cel("D2"),
         "De grootste waarde in D2 tot en met D5 is 20, in D2."),
    klik("Klik op de cel met het resultaat van =MIN(B2:B5).", XL.bestand, cel("B5"),
         "De kleinste prijs is 1, in B5."),
    klik("Klik op de cel waarvan je de formule in de formulebalk ziet.", XL.bestand, cel("D3"),
         "De geselecteerde cel is D3; de formulebalk toont haar formule."),
    klik("Klik op de cel waarin een formule met SOM staat.", XL.bestand, cel("D6"),
         "In D6 staat de som van D2:D5, namelijk 48."),
    met_prent(XL.bestand, inv("Wat geeft =GEMIDDELDE(C2:C5)? Schrijf het getal.", ["5,5", "5.5"],
              "(10 + 4 + 2 + 6) gedeeld door 4 is 5,5.")),
    met_prent(XL.bestand, inv("Welke formule staat er in D6? Schrijf ze zoals Excel.", ["=SOM(D2:D5)", "=som(D2:D5)", "=SOM(d2:d5)"],
              "De som van het bereik D2 tot en met D5.")),
    met_prent(XL.bestand, inv("Je sleept de formule uit D3 met de vulgreep naar D4. Welke formule staat er dan in D4?",
              ["=B4*C4", "=b4*c4"], "Relatieve verwijzingen schuiven één rij mee.")),
    met_prent(XL.bestand, keuze("=ALS(D4>15;\"veel\";\"weinig\") geeft [[*weinig|veel]].",
              "D4 is 10, en 10 is niet groter dan 15.")),
    met_prent(XL.bestand, tabel("Kijk naar het rekenblad. Klopt dit?", [
        ("A1:D6 is een bereik.", J),
        ("C3 bevat het getal 4.", J),
        ("De formule in D3 begint met een isgelijkteken.", J),
        ("B5 is de cel in kolom 5, rij B.", F),
    ], "Eerst de kolomletter, dan het rijnummer.")),
    casus(
        "In een rekenblad staat in B1 het btw-percentage 21 %. In A3 tot A10 staan prijzen "
        "zonder btw. In B3 typt Mo =A3*B1 en sleept die formule naar B10. Vanaf B4 klopt er "
        "niets meer.",
        [
            mk("Waarom loopt het mis vanaf B4?",
               ["B1 schuift mee naar B2, B3 enzovoort",
                "Een formule mag geen procent bevatten",
                "De vulgreep werkt enkel horizontaal",
                "A3 is een absolute verwijzing"], 0,
               "Een relatieve verwijzing schuift mee bij het doortrekken."),
            inv("Hoe schrijft hij de formule in B3 zodat het doortrekken wel klopt?", ["=A3*$B$1", "=a3*$b$1", "=A3*B$1", "=A3*$B1"],
                "Met $B$1 blijft de verwijzing naar het btw-percentage vast staan."),
            keuze("$B$1 is een [[*absolute|relatieve]] verwijzing.", "Het dollarteken zet kolom en rij vast."),
        ],
    ),
    koppel("Koppel elke functie aan wat ze doet.", [
        ["SOM", "telt alle getallen in een bereik op"],
        ["GEMIDDELDE", "telt op en deelt door het aantal"],
        ["MAX", "geeft het grootste getal"],
        ["ALS", "geeft een ander resultaat naargelang een voorwaarde"],
        ["VERT.ZOEKEN", "zoekt in de eerste kolom en geeft iets uit dezelfde rij"],
    ], ["zet de opmaak van een cel vast"], "Functies uit het leerdoel."),
    tabel("Welke grafiek past het best?", [
        ("het aandeel van elke afdeling in de totale omzet", "cirkeldiagram"),
        ("de temperatuur elke dag van de maand", "lijngrafiek"),
        ("de verkoop van vier producten naast elkaar", "kolomgrafiek"),
    ], "Delen van een geheel, evolutie in de tijd, vergelijking.",
       kolommen=["kolomgrafiek", "lijngrafiek", "cirkeldiagram"]),
    tabel("Welke getalnotatie toont dit?", [
        ("€ 12,50", "valuta"),
        ("25%", "percentage"),
        ("24/11/2026", "datum"),
    ], "Getalnotaties veranderen het uitzicht, niet de waarde.", kolommen=["valuta", "percentage", "datum"]),
    keuze("Je typt 0,4 in een cel met percentagenotatie. Je ziet [[*40%|0,4%|4%]].",
          "De percentagenotatie toont het getal maal honderd."),
    sorteer("Verandert dit de waarde in de cel of enkel het uitzicht?", ["Enkel het uitzicht", "De waarde"], [
        ["voorwaardelijke opmaak", "Enkel het uitzicht"],
        ["een nieuwe formule typen", "De waarde"],
        ["valutanotatie", "Enkel het uitzicht"],
        ["een ander getal intypen", "De waarde"],
    ], "Opmaak verandert nooit de inhoud."),
    tabel("Klopt dit over de structuur van een rekenblad?", [
        ("Een werkmap is het bestand, een werkblad een tabblad erin.", J),
        ("Een bereik noteer je met een dubbelpunt, zoals A1:A10.", J),
        ("Een celadres begint met het rijnummer.", F),
    ], "Eerst de kolomletter, dan het rijnummer, zoals B7."),
    inv("In B2 staat =SOM(A1:A3). Je sleept die formule naar C2. Welke formule staat er in C2?",
        ["=SOM(B1:B3)", "=som(B1:B3)"], "Bij horizontaal doortrekken schuiven de kolomletters mee."),
    mk("Welke formule berekent de prijs met 21 procent btw als de prijs zonder btw in A2 staat?",
       ["=A2*1,21",
        "=A2+0,21",
        "=A2*21/100",
        "A2*1,21 zonder teken"], 0,
       "Een formule begint met =; 21 procent erbij is maal 1,21."),
    sleep("Elke formule begint met een [[isgelijkteken]]. Om een verwijzing vast te zetten gebruik je het [[dollarteken]].",
          ["haakje", "puntkomma"], "Zonder = blijft het tekst."),
    klik("Klik op de cel met het resultaat van =C2*B4.", XL.bestand, cel("D2"),
         "C2 is 10 en B4 is 2, samen 20. Dat staat in D2."),
    met_prent(XL.bestand, inv("Wat geeft =MAX(C2:C5)-MIN(C2:C5)? Schrijf het getal.", ["8"],
              "Het grootste aantal is 10, het kleinste 2: 10 min 2 is 8.")),
    met_prent(XL.bestand, keuze("=ALS(B3>=3;\"duur\";\"goedkoop\") geeft [[*duur|goedkoop]].",
              "B3 is 3, en 3 is groter dan of gelijk aan 3.")),
    met_prent(XL.bestand, mk("Welk bereik selecteer je om enkel de aantallen van alle producten op te tellen?",
              ["C2:C5", "C1:C6", "A2:D5", "B2:C5"], 0,
              "De aantallen staan in kolom C, van rij 2 tot en met rij 5.")),
    volgorde("Zet de stappen om een cirkeldiagram van de totalen te maken in de juiste volgorde.", [
        "de cellen met de productnamen en de totalen selecteren",
        "naar het tabblad Invoegen gaan",
        "het cirkeldiagram kiezen",
        "een titel en labels aan de grafiek geven",
    ], "Eerst de gegevens selecteren, dan de grafiek invoegen en afwerken."),
    tabel("Relatief of absoluut? Kies voor elke verwijzing.", [
        ("A1", "relatief"),
        ("$A$1", "absoluut"),
        ("D7", "relatief"),
        ("$C$2", "absoluut"),
    ], "Met dollartekens voor kolom en rij staat de verwijzing vast.", kolommen=["relatief", "absoluut"]),
    mk("Een leerkracht wil bij elke punt boven 10 automatisch geslaagd zien en anders niet geslaagd. Welke functie gebruikt ze?",
       ["ALS", "SOM", "VERT.ZOEKEN", "GEMIDDELDE"], 0,
       "ALS geeft een ander resultaat naargelang de voorwaarde klopt."),
    keuze("Je wil in een lange prijslijst de prijs van een productcode opzoeken. Je gebruikt [[*VERT.ZOEKEN|ALS|MAX]].",
          "VERT.ZOEKEN zoekt de code in de eerste kolom en geeft de prijs uit dezelfde rij."),
    open_("Leg uit wat de vulgreep doet met een formule met relatieve verwijzingen, en wanneer je een absolute verwijzing nodig hebt.",
          "De vulgreep trekt een formule door naar andere cellen; relatieve verwijzingen schuiven dan mee. Moet de formule altijd naar dezelfde cel kijken, zoals een btw-percentage in één cel, dan zet je die verwijzing vast met dollartekens, bijvoorbeeld $B$1."),
]
