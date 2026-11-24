r"""Hypothesen opstellen, eenzijdig en tweezijdig toetsen — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen en een eigen prent met drie toetsen,
zoals op het digitale examen."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Drie klokcurven met gearceerde staarten ---------------------------------------------
DT = Prent("drie-toetsen", "Drie toetsen, telkens met α = 0,05", "drie klokcurven naast elkaar met de letters A, B en C; bij A is enkel de rechterstaart gekleurd, bij B beide staarten, bij C enkel de linkerstaart")
BREED, HOOG, BASIS = 260, 230, 420
MIDDENS = [180, 500, 820]


def curve(cx):
    def y(z):
        return BASIS - HOOG * math.exp(-z * z / 2)

    def x(z):
        return cx + z * BREED / 7
    return x, y


def staart(p, x, y, z1, z2):
    stap = (z2 - z1) / 40
    d = f"M{x(z1):.1f},{BASIS} " + " ".join(f"L{x(z1 + i * stap):.1f},{y(z1 + i * stap):.1f}" for i in range(41)) + f" L{x(z2):.1f},{BASIS} Z"
    p.pad(d, "#b9572f", "none", 0)


for i, cx in enumerate(MIDDENS):
    x, y = curve(cx)
    d = " ".join(f"{'M' if j == 0 else 'L'}{x(-3.5 + j * 0.05):.1f},{y(-3.5 + j * 0.05):.1f}" for j in range(141))
    DT.pad(d + f" L{x(3.5):.1f},{BASIS} L{x(-3.5):.1f},{BASIS} Z", "#dfe9d5", "none", 0)
    if i == 0:
        staart(DT, x, y, 1.645, 3.5)
    elif i == 1:
        staart(DT, x, y, 1.96, 3.5)
        staart(DT, x, y, -3.5, -1.96)
    else:
        staart(DT, x, y, -3.5, -1.645)
    DT.pad(d, "none", DONKER, 3)
    DT.lijn(x(-3.6), BASIS, x(3.6), BASIS, DONKER, 2)
    DT.lijn(cx, BASIS, cx, BASIS + 10, DONKER, 2)
    DT.tekst(cx, BASIS + 34, "μ₀", 20)
    DT.letter(cx, 520, "ABC"[i])
DT.rect(330, 575, 26, 20, "#b9572f", "none", 0, 0)
DT.tekst(366, 591, "gebied waar je H₀ verwerpt", 18, "start", "#5c6356")


def toets(c):
    cx = MIDDENS["ABC".index(c)]
    return [Prent.zone(cx - 150, 150, 300, 410)]


VRAGEN = [
    klik("Klik op de toets die hoort bij H₁: μ < 500.", DT.bestand, toets("C"),
         "Kleiner dan: enkel de linkerstaart."),
    klik("Klik op de toets die hoort bij H₁: p ≠ 0,25.", DT.bestand, toets("B"),
         "Verschilt van: beide staarten."),
    klik("Een bedrijf wil aantonen dat een nieuwe batterij langer meegaat dan 20 uur. Klik op de passende toets.", DT.bestand, toets("A"),
         "Langer dan: H₁: μ > 20, de rechterstaart."),
    met_prent(DT.bestand, keuze("Bij toets B ligt in elke staart [[*0,025|0,05|0,10]].",
              "α wordt over de twee staarten verdeeld.")),
    met_prent(DT.bestand, tabel("Welk soort toets is dit?", [
        ("A", "rechtszijdig"),
        ("B", "tweezijdig"),
        ("C", "linkszijdig"),
    ], "Kijk welke staart gekleurd is.", kolommen=["rechtszijdig", "tweezijdig", "linkszijdig"])),
    casus(
        "Een melkerij zegt dat haar flessen gemiddeld 1000 ml bevatten. Een consumentenorganisatie vermoedt dat er te weinig in zit. "
        "Ze meet 50 flessen.",
        [
            keuze("\\(H_0\\): \\(\\mu\\) [[*=|<|>]] 1000.", "De nulhypothese is altijd een gelijkheid."),
            keuze("\\(H_1\\): \\(\\mu\\) [[*<|>|≠]] 1000.", "Te weinig betekent kleiner dan."),
            keuze("Dit is een [[*linkszijdige|rechtszijdige|tweezijdige]] toets.", "Je kijkt enkel naar te kleine waarden."),
            mk("Is de voorwaarde voor de normale benadering voldaan?",
               ["ja, want n = 50 is minstens 30",
                "nee, want n moet minstens 100 zijn",
                "nee, want je kent \\(\\bar{x}\\) nog niet",
                "ja, want 1000 is groter dan 30"], 0,
               "Bij een gemiddelde is n ≥ 30 de enige voorwaarde."),
            tabel("Gaat dit over de populatie of over de steekproef?", [
                ("het gemiddelde van de 50 gemeten flessen", "steekproef"),
                ("het gemiddelde van alle flessen van de melkerij", "populatie"),
                ("het getal 1000 in de hypothesen", "populatie"),
            ], "Hypothesen gaan altijd over de populatie.", kolommen=["populatie", "steekproef"]),
        ],
    ),
    tabel("Is dit een correct paar hypothesen?", [
        ("H₀: μ = 30 en H₁: μ > 30", J),
        ("H₀: p = 0,4 en H₁: p ≠ 0,4", J),
        ("H₀: μ > 12 en H₁: μ = 12", F),
        ("H₀: \\(\\bar{x}\\) = 8 en H₁: \\(\\bar{x}\\) < 8", F),
    ], "H₀ is een gelijkheid over de populatie; H₁ is de ongelijkheid."),
    koppel("Koppel de onderzoeksvraag aan H₁. Telkens is H₀: μ = 50.", [
        ["Is het gemiddelde gestegen?", "μ > 50"],
        ["Is het gemiddelde gedaald?", "μ < 50"],
        ["Is het gemiddelde veranderd?", "μ ≠ 50"],
    ], ["\\(\\bar{x}\\) > 50"], "De richting volgt uit de vraag."),
    volgorde("Zet de eerste stappen van een hypothesetoets in de juiste volgorde.", [
        "de onderzoeksvraag lezen",
        "H₀ en H₁ in woorden en symbolen opschrijven",
        "kiezen tussen eenzijdig en tweezijdig",
        "de voorwaarden controleren",
    ], "De richting volgt uit H₁; de voorwaarden komen daarna."),
    sorteer("Hoort dit bij H₀ of bij H₁?", ["H₀", "H₁"], [
        ["bevat altijd een gelijkheidsteken", "H₀"],
        ["de bewering die je wil aantonen", "H₁"],
        ["geldt zolang de data niets anders tonen", "H₀"],
        ["bepaalt of de toets eenzijdig is", "H₁"],
    ], "H₀ is het uitgangspunt, H₁ de uitdaging."),
    mk("Een school zegt dat 75 procent van haar leerlingen fietst. Een leerling denkt dat het een ander percentage is. Welke H₁ past?",
       ["p ≠ 0,75", "p < 0,75", "p > 0,75", "μ ≠ 75"], 0,
       "Een ander percentage, zonder richting: tweezijdig, en over een proportie dus p."),
    inv("Een toets over een proportie heeft n = 60 en p = 0,15 in H₀. Hoeveel is n · p?", ["9"],
        "60 · 0,15 = 9."),
    keuze("Bij die toets is de voorwaarde n · p ≥ 10 dus [[*niet voldaan|wel voldaan]].",
          "9 is kleiner dan 10."),
    sleep("Over een gemiddelde schrijf je de hypothesen met [[\\(\\mu\\)]], over een proportie met [[\\(p\\)]].",
          ["\\(\\bar{x}\\)", "\\(\\hat{p}\\)"], "Hypothesen gaan over de populatie."),
    tabel("Mag dit?", [
        ("de richting van H₁ kiezen voor je de data bekijkt", J),
        ("overstappen naar een eenzijdige toets omdat tweezijdig niet significant was", F),
        ("met één toets twee alternatieve hypothesen tegelijk toetsen", F),
    ], "De richting staat vast voor je de data ziet."),
    mk("Een sportclub wil weten of een nieuw trainingsschema de gemiddelde looptijd van 12 minuten verkort. Welk paar past?",
       ["H₀: μ = 12 en H₁: μ < 12",
        "H₀: μ = 12 en H₁: μ > 12",
        "H₀: μ < 12 en H₁: μ = 12",
        "H₀: μ = 12 en H₁: μ ≠ 12"], 0,
       "Verkorten betekent een kleinere tijd."),
    keuze("Bij een rechtszijdige toets kijk je naar resultaten die [[*minstens zo groot|hoogstens zo groot|precies even groot]] zijn als het gevonden resultaat.",
          "De rechterstaart."),
    inv("Hoeveel staarten heeft een toets met H₁: p < 0,2? Schrijf het getal.", ["1", "één", "een"],
        "Kleiner dan: één staart, links."),
    inv("Bij een tweezijdige toets met α = 0,10: hoeveel zit er in elke staart? Schrijf als decimaal getal.", ["0,05", "0.05"],
        "0,10 / 2 = 0,05."),
    keuze("Een toets over een proportie met n = 40 en p = 0,5 in H₀: n · (1 − p) is [[*20|40|0,5]].",
          "40 · 0,5 = 20, dus voldaan."),
    mk("Waarom bevat H₀ altijd een gelijkheid?",
       ["zo ken je de verdeling waarmee je rekent",
        "omdat een ongelijkheid niet mag op het examen",
        "omdat de steekproef altijd gelijk is aan μ",
        "zo is de toets automatisch tweezijdig"], 0,
       "Met één vaste waarde voor μ of p kan je de steekproevenverdeling opstellen."),
    tabel("Eenzijdig of tweezijdig?", [
        ("Is het nieuwe medicijn sneller dan het oude?", "eenzijdig"),
        ("Verschilt de gemiddelde lengte van vorig jaar?", "tweezijdig"),
        ("Is het aandeel fouten gedaald?", "eenzijdig"),
        ("Is het slaagpercentage veranderd?", "tweezijdig"),
    ], "Een richting in de vraag geeft een eenzijdige toets.", kolommen=["eenzijdig", "tweezijdig"]),
    keuze("Onder H₀: μ = 80 met σ = 12 en n = 36 heeft \\(\\bar{x}\\) standaardafwijking [[*2|12|0,33]].",
          r"\(12 / \sqrt{36} = 2\)."),
    inv("Onder diezelfde H₀: wat is het gemiddelde van de steekproevenverdeling van het steekproefgemiddelde?", ["80"],
        "Je rekent met het getal uit H₀."),
    sleep("Een toets met H₁: μ ≠ 10 heet [[tweezijdig]]. Een toets met H₁: μ > 10 heet [[rechtszijdig]].",
          ["linkszijdig", "eenzijdig gelijk"], "Kijk naar het teken in H₁."),
    open_("Een onderzoeker toetst H₀: μ = 100 tegen H₁: μ > 105. Leg uit wat er mis is.",
          "H₀ en H₁ moeten samen alle mogelijkheden afdekken en elkaar uitsluiten. Waarden tussen 100 en 105 vallen nu onder geen van beide. H₁ moet μ > 100 zijn."),
]
