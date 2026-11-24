"""Warmte en faseovergangen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, assen

# Opwarmcurve van ijs tot stoom ------------------------------------------
OC = Prent("ijs-tot-stoom", "Je verwarmt ijs van -20 °C tot stoom van 120 °C", "temperatuur tegen toegevoerde warmte met stukken A tot E")
X, Y = assen(OC, 0, 10, -40, 140, "toegevoerde warmte", "T (°C)", 1, 20)
PUNTEN = [(0, -20), (0.6, 0), (2.4, 0), (3.8, 100), (8.8, 100), (9.5, 120)]
OC.pad("M" + " L ".join(f"{X(a):.0f} {Y(b):.0f}" for a, b in PUNTEN), "none", ROOD, 5)
OC.lijn(X(0), Y(0), X(10), Y(0), GRIJS, 1, stippel=True)
OC.lijn(X(0), Y(100), X(10), Y(100), GRIJS, 1, stippel=True)
LET = {"A": (0.3, -10, 0, 40), "B": (1.5, 0, 0, -40), "C": (3.1, 50, -40, -10), "D": (6.3, 100, 0, -40), "E": (9.15, 110, -38, -12)}
ZOC = {}
for k, (a, b, dx, dy) in LET.items():
    OC.letter(X(a) + dx, Y(b) + dy, k)
    ZOC[k] = [Prent.rond(X(a) + dx, Y(b) + dy, 26)]
ZOC["A"].append(Prent.zone(X(0), Y(0) - 5, X(0.6) - X(0), Y(-20) - Y(0) + 10))
ZOC["B"].append(Prent.zone(X(0.6) + 5, Y(0) - 18, X(2.4) - X(0.6) - 10, 36))
ZOC["C"].append(Prent.zone(X(2.4) + 5, Y(100) + 10, X(3.8) - X(2.4) - 10, Y(0) - Y(100) - 20))
ZOC["D"].append(Prent.zone(X(3.8) + 5, Y(100) - 18, X(8.8) - X(3.8) - 10, 36))
ZOC["E"].append(Prent.zone(X(8.8) + 5, Y(120) - 5, X(9.5) - X(8.8), Y(100) - Y(120) - 5))

# Pot op het vuur --------------------------------------------------------
PO = Prent("pot-op-vuur", "Drie manieren waarop warmte zich verplaatst", "kookpot op een vuur met pijlen A, B en C")
PO.rect(300, 260, 300, 220, "#bfc5cc", DONKER, 10)
PO.rect(310, 300, 280, 170, "#cfe5f5", "none", 6)
PO.rect(600, 300, 230, 24, "#7a5a3a", DONKER, 8)
for x in (340, 400, 460, 520, 570):
    PO.pad(f"M{x} 560 Q {x - 25} 520 {x} 490 Q {x + 25} 520 {x} 560 Z", "#f4a259", ROOD, 2)
PO.rect(280, 560, 340, 20, "#555555", DONKER, 4)
PO.pad("M380 440 C 340 400 340 340 380 320", "none", BLAUW, 4)
PO.pijl(380, 330, 385, 318, BLAUW, 4)
PO.pad("M520 320 C 560 340 560 400 520 440", "none", BLAUW, 4)
PO.pijl(522, 430, 515, 445, BLAUW, 4)
PO.pijl(620, 312, 800, 312, ROOD, 4)
PO.pijl(230, 380, 110, 380, ORANJE, 5)
PO.pijl(230, 330, 120, 280, ORANJE, 5)
PO.pijl(230, 430, 120, 480, ORANJE, 5)
PO.letter(450, 380, "A")
PO.letter(710, 270, "B")
PO.letter(170, 220, "C")
ZPO = {"A": [Prent.zone(320, 300, 260, 170)], "B": [Prent.zone(600, 260, 240, 70)], "C": [Prent.zone(100, 190, 140, 300)]}

VRAGEN = [
    klik(
        "Klik op het stuk waar het ijs smelt.",
        OC.bestand, ZOC["B"],
        "Het eerste vlakke stuk ligt op 0 °C: daar smelt het ijs.",
    ),
    klik(
        "Klik op het stuk waar vloeibaar water opwarmt.",
        OC.bestand, ZOC["C"],
        "Tussen 0 en 100 °C stijgt de temperatuur van het vloeibare water.",
    ),
    met_prent(OC.bestand, tabel(
        "Kijk naar de opwarmcurve van water. Klopt dit?",
        [
            ("In stuk D is er latente warmte nodig.", J),
            ("Stuk D is langer dan stuk B, dus verdampen vraagt meer warmte dan smelten.", J),
            ("In stuk B stijgt de temperatuur traag.", F),
            ("In stuk E is alles stoom.", J),
        ],
        "Op de vlakke stukken gaat alle warmte naar de faseovergang.",
    )),
    met_prent(OC.bestand, keuze(
        "In stuk A is het water [[*vast|vloeibaar|gasvormig]] en neemt het merkbare warmte op.",
        "Onder 0 °C is water ijs.",
    )),
    klik(
        "Klik op de plaats waar warmte zich vooral door convectie verplaatst.",
        PO.bestand, ZPO["A"],
        "Het warme water stijgt, het koudere zakt: de stof zelf neemt de warmte mee.",
    ),
    klik(
        "Klik op de pijl die geleiding toont.",
        PO.bestand, ZPO["B"],
        "Langs de steel geven de deeltjes hun beweging door aan hun buren.",
    ),
    met_prent(PO.bestand, keuze(
        "Je hand naast de hete pot voelt warmte zonder iets aan te raken. Dat is [[*straling|geleiding|convectie]], pijl C.",
        "Straling heeft geen stof nodig.",
    )),
    tabel(
        "Geleiding, convectie of straling?",
        [
            ("een lepel in hete soep wordt warm", "Geleiding"),
            ("warme lucht van een radiator vult de kamer", "Convectie"),
            ("je gezicht wordt warm in de zon", "Straling"),
            ("een strijkijzer op een hemd", "Geleiding"),
            ("water in een pot draait rond tijdens het koken", "Convectie"),
        ],
        "Contact: geleiding. Stromende stof: convectie. Zonder stof: straling.",
        kolommen=["Geleiding", "Convectie", "Straling"],
    ),
    tabel(
        "Warmte of temperatuur?",
        [
            ("meet je in joule", "Warmte"),
            ("meet je met een thermometer", "Temperatuur"),
            ("is energie die overgaat", "Warmte"),
            ("hangt samen met hoe snel de deeltjes bewegen", "Temperatuur"),
        ],
        "Temperatuur zegt hoe warm iets is, warmte is de energie die overgaat.",
        kolommen=["Warmte", "Temperatuur"],
    ),
    inv(
        "Hoeveel joule heb je nodig om 0,5 kg water 20 °C op te warmen? Neem 4180 J per kg per °C.",
        ["41800", "41 800"],
        "Q = c · m · ΔT = 4180 · 0,5 · 20 = 41 800 J.",
    ),
    inv(
        "Een blok van 2 kg neemt 9000 J op en warmt 5 °C op. Wat is de specifieke warmtecapaciteit, in J per kg per °C?",
        ["900"],
        "c = Q : (m · ΔT) = 9000 : 10 = 900.",
    ),
    casus(
        "Op een zomerdag ligt Noor op het strand. Om twaalf uur is het zand gloeiend heet, maar het zeewater is nog fris. 's Avonds is het zand al afgekoeld, terwijl de zee lauw blijft.",
        [
            mk(
                "Hoe verklaar je dat?",
                [
                    "Water heeft een veel grotere specifieke warmtecapaciteit dan zand",
                    "Het zand krijgt overdag veel meer zonlicht dan het water dat ernaast ligt",
                    "Zeewater geleidt de warmte veel beter dan zand en houdt ze daardoor vast",
                    "Het zout in het zeewater maakt de zee 's avonds warmer dan de lucht erboven",
                ],
                0,
                "Water moet veel energie opnemen en afgeven voor één graad verschil.",
            ),
            keuze(
                "Het zand heeft een [[*kleine|grote|even grote]] specifieke warmtecapaciteit en warmt dus snel op en af.",
                "Een kleine warmtecapaciteit geeft snelle temperatuurwissels.",
            ),
        ],
    ),
    inv(
        "Je mengt 1 kg water van 90 °C met 2 kg water van 30 °C. Wat wordt de eindtemperatuur, in °C? Er gaat geen warmte verloren.",
        ["50"],
        "Afgegeven = opgenomen: 1 · (90 - T) = 2 · (T - 30). Dat geeft 90 - T = 2T - 60, dus T = 50 °C.",
    ),
    tabel(
        "Neemt de stof warmte op of geeft ze warmte af?",
        [
            ("smelten", "Neemt op"),
            ("condenseren", "Geeft af"),
            ("verdampen", "Neemt op"),
            ("stollen", "Geeft af"),
            ("sublimeren", "Neemt op"),
            ("desublimeren", "Geeft af"),
        ],
        "Naar een toestand met zwakkere cohesiekrachten: warmte opnemen.",
        kolommen=["Neemt op", "Geeft af"],
    ),
    koppel(
        "Koppel elk voorbeeld aan de faseovergang.",
        [
            ("rijm op het gras op een koude ochtend", "desublimeren"),
            ("droogijs dat rookt op tafel", "sublimeren"),
            ("een beslagen badkamerspiegel", "condenseren"),
            ("een plas die opdroogt in de zon", "verdampen"),
        ],
        ["stollen"],
        "Vast naar gas zonder vloeistof: sublimeren. Gas naar vast: desublimeren.",
    ),
    inv(
        "Hoeveel joule heb je nodig om 2 kg ijs van 0 °C te smelten? De specifieke smeltwarmte is 334 000 J per kg.",
        ["668000", "668 000"],
        "Q = l · m = 334 000 · 2 = 668 000 J.",
    ),
    tabel(
        "Merkbare of latente warmte?",
        [
            ("soep warmt op van 20 °C naar 60 °C", "Merkbare"),
            ("een ijsblokje smelt bij 0 °C", "Latente"),
            ("water kookt weg bij 100 °C", "Latente"),
            ("een ijzeren staaf koelt af van 300 °C naar 50 °C", "Merkbare"),
        ],
        "Merkbaar: de temperatuur verandert. Latent: de fase verandert.",
        kolommen=["Merkbare", "Latente"],
    ),
    tabel(
        "Klopt dit over een fruitboer die bij nachtvorst water op zijn bloesems sproeit?",
        [
            ("Het water geeft warmte af terwijl het stolt.", J),
            ("Zolang er water stolt, blijft de bloesem rond 0 °C.", J),
            ("Het ijs maakt de bloesem kouder dan de lucht.", F),
            ("Stollen vraagt warmte uit de bloesem.", F),
        ],
        "Bij stollen komt latente warmte vrij.",
    ),
    sleep(
        "Als ijs smelt, breken de [[cohesiekrachten]] tussen de deeltjes gedeeltelijk. De deeltjes kunnen dan langs elkaar [[schuiven]]. De temperatuur blijft tijdens het smelten [[gelijk]].",
        ["stijgen", "versnellen"],
        "De warmte gaat naar het losbreken, niet naar sneller bewegen.",
    ),
    mk(
        "Je zit na het zwemmen in een natte handdoek in de wind. Waarom heb je het zo koud?",
        [
            "Het water verdampt en haalt daarbij warmte uit je huid",
            "Het water houdt de warmte van de zon tegen zodat je opwarmt",
            "De wind blaast koude naar binnen door de natte handdoek",
            "Het water op je huid condenseert en neemt zo warmte van je op",
        ],
        0,
        "Verdampen vraagt veel warmte. De wind voert de damp weg, zodat er sneller nieuw water verdampt.",
    ),
    tabel(
        "Klopt dit over een calorimeter?",
        [
            ("Hij is goed geïsoleerd.", J),
            ("Je meet er warmte mee die een stof opneemt of afgeeft.", J),
            ("Hij laat bewust veel warmte naar buiten.", F),
            ("Je gebruikt hem om een warmtebalans op te stellen.", J),
        ],
        "Hoe minder warmte ontsnapt, hoe beter de meting.",
    ),
    volgorde(
        "Zet in de juiste volgorde: een warmtebalans oplossen.",
        [
            "Bepaal welk deel warmte afgeeft en welk deel opneemt",
            "Schrijf voor elk deel de warmte met c · m · ΔT",
            "Stel afgegeven warmte gelijk aan opgenomen warmte",
            "Los de vergelijking op naar de eindtemperatuur",
        ],
        "Behoud van energie: wat het ene deel verliest, wint het andere.",
    ),
    inv(
        "Een glas met 0,2 kg water van 25 °C koelt af tot 5 °C. Hoeveel joule geeft het water af? Neem 4180 J per kg per °C.",
        ["16720", "16 720"],
        "Q = 4180 · 0,2 · 20 = 16 720 J.",
    ),
    tabel(
        "Een tapijt en een tegelvloer liggen in dezelfde kamer. Klopt dit?",
        [
            ("Een tapijt en een tegelvloer in dezelfde kamer hebben dezelfde temperatuur.", J),
            ("Een tegel voelt kouder omdat hij warmte sneller wegleidt.", J),
            ("Een tapijt is een goede warmtegeleider.", F),
            ("Je huid voelt hoe snel ze warmte verliest.", J),
        ],
        "Je voelt het warmteverlies, niet de temperatuur zelf.",
    ),
    met_prent(OC.bestand, tabel(
        "Kijk naar de curve. In welk stuk is het water in deze toestand?",
        [
            ("enkel ijs", "A"),
            ("ijs en water samen", "B"),
            ("enkel vloeibaar water", "C"),
            ("water en stoom samen", "D"),
        ],
        "Op een vlak stuk zijn twee fasen tegelijk aanwezig.",
        kolommen=["A", "B", "C", "D", "E"],
    )),
    met_prent(PO.bestand, tabel(
        "Kijk naar de pot. Klopt dit?",
        [
            ("Een houten handvat helpt tegen pijl B.", J),
            ("Pijl C kan ook door een luchtledige ruimte gaan.", J),
            ("Bij A blijft het water op zijn plaats en geven de deeltjes enkel een duwtje door.", F),
            ("Zonder deksel gaat er ook warmte weg met de damp.", J),
        ],
        "Hout is een isolator. Bij convectie stroomt de stof zelf.",
    )),
    keuze(
        "Twee voorwerpen raken elkaar tot ze dezelfde temperatuur hebben. Dat heet [[*thermisch evenwicht|latente warmte|warmtecapaciteit]].",
        "Dan stopt de netto warmtestroom.",
    ),
    inv(
        "Hoeveel joule komt er vrij als 0,1 kg water van 0 °C helemaal bevriest? De specifieke smeltwarmte is 334 000 J per kg.",
        ["33400", "33 400"],
        "Stollen geeft evenveel warmte af als smelten vraagt: 334 000 · 0,1 = 33 400 J.",
    ),
    open_(
        "Leg uit waarom een brandwonde door stoom van 100 °C erger is dan een door water van 100 °C.",
        "Stoom condenseert op je huid. Daarbij geeft hij de grote verdampingswarmte af, als latente warmte. Daarna geeft het water nog merkbare warmte af terwijl het afkoelt. Zo krijgt je huid veel meer energie dan van water dat enkel afkoelt.",
    ),
]
