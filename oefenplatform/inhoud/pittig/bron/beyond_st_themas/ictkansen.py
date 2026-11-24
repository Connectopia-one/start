r"""Kansen berekenen met ICT — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en een eigen schermafdruk van een kansrekenmachine,
zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Schermafdruk van een kansrekenmachine ------------------------------------------------------
KM = Prent("kansrekenmachine", "Kansrekenmachine", "een venster met bovenaan een keuzelijst 'Verdeling: normaal', daaronder twee velden μ = 65 en σ = 10, drie keuzerondjes P(X < a), P(a < X < b) en P(X > a) waarvan het derde aangeduid, een veld a = 80, een knop Bereken en een resultaatvak met 0,0668")
GR = "#5c6356"
KM.rect(150, 70, 700, 540, "#ffffff", DONKER, 14, 3)
KM.rect(150, 70, 700, 50, "#2f4a22", DONKER, 14, 0)
KM.rect(150, 100, 700, 20, "#2f4a22", "none", 0, 0)
KM.tekst(180, 103, "Kansrekenmachine", 22, "start", "#ffffff", True)
KM.tekst(190, 165, "Verdeling", 20, "start", GR)
KM.rect(330, 140, 260, 40, "#f4f4f0", DONKER, 6, 2)
KM.tekst(345, 167, "normaal", 20, "start")
KM.tekst(570, 167, "▾", 20)
KM.tekst(190, 235, "μ", 24, "start", DONKER, True)
KM.rect(230, 210, 150, 40, "#ffffff", DONKER, 6, 2)
KM.tekst(245, 237, "65", 20, "start")
KM.tekst(450, 235, "σ", 24, "start", DONKER, True)
KM.rect(490, 210, 150, 40, "#ffffff", DONKER, 6, 2)
KM.tekst(505, 237, "10", 20, "start")
KM.tekst(190, 300, "Soort kans", 20, "start", GR)
OPT = [("P(X < a)", 330), ("P(a < X < b)", 470), ("P(X > a)", 650)]
for i, (t, x) in enumerate(OPT):
    KM.cirkel(x, 330, 11, "#ffffff", DONKER, 2)
    if i == 2:
        KM.cirkel(x, 330, 6, DONKER, DONKER, 1)
    KM.tekst(x + 20, 337, t, 20, "start")
KM.tekst(190, 405, "a", 24, "start", DONKER, True)
KM.rect(230, 380, 150, 40, "#ffffff", DONKER, 6, 2)
KM.tekst(245, 407, "80", 20, "start")
KM.tekst(450, 405, "b", 24, "start", GR, True)
KM.rect(490, 380, 150, 40, "#ecebe6", GR, 6, 2)
KM.rect(330, 460, 200, 50, "#5f7f4a", DONKER, 10, 2)
KM.tekst(430, 493, "Bereken", 22, "middle", "#ffffff", True)
KM.tekst(190, 568, "Resultaat", 20, "start", GR)
KM.rect(330, 540, 200, 44, "#f4f4f0", DONKER, 6, 2)
KM.tekst(345, 569, "0,0668", 22, "start", DONKER, True)

Z_SIGMA = [Prent.zone(440, 200, 210, 60)]
Z_MU = [Prent.zone(180, 200, 210, 60)]
Z_LINKS = [Prent.zone(310, 310, 120, 40)]
Z_TUSSEN = [Prent.zone(450, 310, 170, 40)]
Z_VERDELING = [Prent.zone(320, 135, 280, 50)]

VRAGEN = [
    klik("Klik op het veld waar je de standaardafwijking invult.", KM.bestand, Z_SIGMA,
         "σ is de standaardafwijking, μ het gemiddelde."),
    klik("Je wil met dezelfde verdeling P(X ≤ 50) berekenen. Klik op de soort kans die je dan kiest.", KM.bestand, Z_LINKS,
         "Kleiner dan een grens: P(X < a). Bij een continue verdeling maakt ≤ of < niet uit."),
    klik("Je wil P(55 < X < 75) berekenen. Klik op de soort kans die je dan kiest.", KM.bestand, Z_TUSSEN,
         "Tussen twee grenzen: P(a < X < b)."),
    klik("Je wil een binomiale kans berekenen. Klik op wat je eerst moet aanpassen.", KM.bestand, Z_VERDELING,
         "Kies eerst de verdeling; dan vraagt het venster n en p."),
    met_prent(KM.bestand, keuze("Het venster berekent nu de kans dat een waarde van N(65; 10) [[*groter is dan 80|kleiner is dan 80|precies 80 is]].",
              "De derde keuze, met a = 80.")),
    met_prent(KM.bestand, keuze("Het resultaat 0,0668 hoort bij z = [[*1,5|−1,5|15]].",
              "(80 − 65) / 10 = 1,5.")),
    met_prent(KM.bestand, inv("Met dezelfde μ en σ: hoeveel is P(X < 50)? Rond af op vier decimalen.", ["0,0668", "0.0668"],
              "50 ligt even ver onder 65 als 80 erboven; door de symmetrie is de kans gelijk.")),
    met_prent(KM.bestand, inv("Met dezelfde μ en σ: hoeveel is P(55 < X < 75)? Rond af op drie decimalen.", ["0,683", "0.683"],
              "Van μ − σ tot μ + σ.")),
    inv(r"\(X \sim B(15; 0{,}4)\). Bereken \(P(X = 6)\) op drie decimalen.", ["0,207", "0.207"],
        "Binomiale verdeling, n = 15, p = 0,4, kans op precies 6."),
    inv(r"\(X \sim B(15; 0{,}4)\). Bereken \(P(X \leq 3)\) op drie decimalen.", ["0,091", "0.091"],
        "Cumulatief tot en met 3."),
    inv(r"\(X \sim B(15; 0{,}4)\). Bereken \(P(X \geq 10)\) op drie decimalen.", ["0,034", "0.034"],
        r"\(1 - P(X \leq 9)\)."),
    inv(r"Je gooit 8 keer met een munt. Bereken de kans op precies 4 keer kop op vier decimalen.", ["0,2734", "0.2734"],
        r"\(X \sim B(8; 0{,}5)\), \(P(X = 4) = 70/256\)."),
    inv(r"Je gooit 10 keer met een dobbelsteen. Bereken de kans op minstens twee zessen op drie decimalen.", ["0,515", "0.515"],
        r"\(1 - P(X \leq 1)\) bij \(B(10; 1/6)\)."),
    casus(
        "Een fabriek levert bouten. 20 procent heeft een kleine kras. Een klant controleert 25 bouten. X is het aantal bouten met een kras.",
        [
            keuze("In de rekenapp kies je [[*binomiaal|normaal]] met n = [[*25|20]] en p = [[*0,2|25]].",
                  "Een vast aantal onafhankelijke controles met telkens dezelfde kans."),
            inv("Hoe groot is de kans op precies 5 bouten met een kras? Rond af op drie decimalen.", ["0,196", "0.196"], "P(X = 5)."),
            inv("Hoe groot is de kans op hoogstens 5 bouten met een kras? Rond af op drie decimalen.", ["0,617", "0.617"], "Cumulatief: P(X ≤ 5)."),
            mk("Hoe bereken je P(X > 5) uit die cumulatieve kans?",
               ["1 − P(X ≤ 5)", "1 − P(X ≤ 4)", "P(X ≤ 5) − P(X = 5)", "P(X ≤ 5) + P(X = 5)"], 0,
               "Meer dan 5 is het complement van hoogstens 5."),
        ],
    ),
    inv(r"Een vulmachine werkt volgens \(N(250; 6)\) ml. Bereken \(P(X < 240)\) op drie decimalen.", ["0,048", "0.048"],
        "Normaal, μ = 250, σ = 6, links van 240."),
    inv(r"Bij diezelfde machine: bereken \(P(245 < X < 260)\) op drie decimalen.", ["0,750", "0.750", "0,75", "0.75"],
        "Tussen twee grenzen."),
    inv("Bij een linkszijdige toets vind je z = −1,8. Bereken de p-waarde op vier decimalen.", ["0,0359", "0.0359"],
        "De oppervlakte links van −1,8 onder de standaardnormale curve."),
    inv("Bij een tweezijdige toets vind je z = 2,4. Bereken de p-waarde op vier decimalen.", ["0,0164", "0.0164"],
        "Twee keer de staart rechts van 2,4."),
    tabel("Welke soort kans kies je in de rekenapp?", [
        ("hoogstens 12", "P(X < a)"),
        ("meer dan 30", "P(X > a)"),
        ("tussen 18 en 22", "P(a < X < b)"),
    ], "Lees de woorden in de opgave nauwkeurig.", kolommen=["P(X < a)", "P(X > a)", "P(a < X < b)"]),
    sorteer("Welke verdeling kies je in de rekenapp?", ["binomiaal", "normaal"], [
        ["het aantal juiste gokantwoorden op 20 vragen", "binomiaal"],
        ["de lengte van volwassen vrouwen", "normaal"],
        ["het aantal defecte lampen in een doos van 50", "binomiaal"],
        ["de reactietijd bij een rijtest", "normaal"],
    ], "Tellen van successen: binomiaal. Een continue meetwaarde rond een gemiddelde: normaal."),
    volgorde("Zet de stappen om P(X ≥ 8) bij een binomiale verdeling met ICT te berekenen in de juiste volgorde.", [
        "binomiale verdeling kiezen",
        "n en p invullen",
        "P(X ≤ 7) laten berekenen",
        "het resultaat van 1 aftrekken",
    ], "Minstens 8 is het complement van hoogstens 7."),
    mk("Een leerling krijgt bij een rechtszijdige toets een p-waarde van 0,9641. Wat is het meest waarschijnlijk?",
       ["hij las de linkerstaart af in plaats van de rechter",
        "het resultaat is heel sterk significant bij elke keuze van α",
        "hij vulde σ in waar μ moest staan in het venster",
        "de toets had eigenlijk tweezijdig moeten zijn"], 0,
       "1 − 0,9641 = 0,0359 is de echte rechterstaart."),
    keuze("Bij een discrete verdeling is P(X < 5) gelijk aan [[*P(X ≤ 4)|P(X ≤ 5)|1 − P(X ≤ 5)]].",
          "Kleiner dan 5 is hoogstens 4 bij gehele getallen."),
    inv(r"Een test slaagt in 90 procent van de gevallen. Je doet 12 tests. Bereken de kans dat er minstens 11 slagen, op drie decimalen.", ["0,659", "0.659"],
        r"\(1 - P(X \leq 10)\) bij \(B(12; 0{,}9)\)."),
    inv(r"Bij \(Z \sim N(0; 1)\): bereken \(P(Z > -1)\) op vier decimalen.", ["0,8413", "0.8413"],
        "Rechts van −1 ligt alles behalve de linkerstaart van 0,1587."),
    keuze(r"Bij \(X \sim B(20; 0{,}5)\) is \(P(6 \leq X \leq 14)\) gelijk aan \(P(X \leq 14)\) min [[*\(P(X \leq 5)\)|\(P(X \leq 6)\)|\(P(X = 6)\)]].",
          "6 moet erbij blijven, dus trek je enkel tot en met 5 af."),
    open_("Een leerling berekent bij X ~ B(30; 0,5) de kans P(X ≥ 20) als 1 − P(X ≤ 20). Leg uit wat er mis is.",
          "Het complement van 'minstens 20' is 'hoogstens 19'. Hij moet dus 1 − P(X ≤ 19) berekenen. Door 20 mee af te trekken, telt hij de kans op precies 20 niet mee."),
]
