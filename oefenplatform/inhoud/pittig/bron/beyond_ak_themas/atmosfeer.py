"""De opbouw van de atmosfeer — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Temperatuurprofiel ------------------------------------------------------
TP = Prent("temperatuur-atmosfeer", "Temperatuur in de atmosfeer volgens de hoogte", "grafiek van temperatuur tegen hoogte met lagen A tot D")
X, Y = assen(TP, -100, 40, 0, 100, "T (°C)", "hoogte (km)", 20, 10, links=130, rechts=700)
lagen = [(0, 12, "#e3f0f7"), (12, 50, "#eef6e6"), (50, 85, "#f7f0e3"), (85, 100, "#f3e6ee")]
for lo, hi, kl in lagen:
    TP.rect(X(-100), Y(hi), X(40) - X(-100), Y(lo) - Y(hi), kl, "none", 0)
pts = [(15, 0), (-56, 12), (-56, 20), (-2, 50), (-90, 85), (-40, 100)]
TP.pad("M" + " L ".join(f"{X(t):.0f} {Y(h):.0f}" for t, h in pts), "none", ROOD, 5)
for h in (12, 50, 85):
    TP.lijn(X(-100), Y(h), X(40), Y(h), GRIJS, 1, stippel=True)
LL = {"A": (6, "troposfeer"), "B": (31, "stratosfeer"), "C": (67, "mesosfeer"), "D": (93, "thermosfeer")}
for k, (h, _) in LL.items():
    TP.letter(790, Y(h), k)
ZTP = {k: [Prent.zone(X(-100), Y(h + 4), 760 - X(-100), 40), Prent.rond(790, Y(h), 26)] for k, (h, _) in LL.items()}
ZTP["A"] = [Prent.zone(X(-100), Y(12) + 4, 820 - X(-100), Y(0) - Y(12) - 8)]
ZTP["B"] = [Prent.zone(X(-100), Y(50) + 4, 820 - X(-100), Y(12) - Y(50) - 8)]
ZTP["C"] = [Prent.zone(X(-100), Y(85) + 4, 820 - X(-100), Y(50) - Y(85) - 8)]
ZTP["D"] = [Prent.zone(X(-100), Y(100), 820 - X(-100), Y(85) - Y(100) - 4)]
TP.tekst(700, 595, "temperatuur (°C)", 16, "end")
ZPAUZE = [Prent.zone(X(-70), Y(12) - 12, X(-40) - X(-70), 24)]

# Zonnestralen op de aardbol -------------------------------------------
ZB = Prent("zonnestralen-aardbol", "Drie even brede bundels zonlicht op 21 maart", "aardbol met drie gelijke bundels die vallen op A, B en C")
CX, CY, R = 640, 330, 230
ZB.cirkel(CX, CY, R, "#9bc1df", DONKER)
ZB.lijn(CX - R, CY, CX + R, CY, DONKER, 1, stippel=True)
ZB.tekst(CX + R + 15, CY + 5, "evenaar", 16, "start")
for k, lat in (("A", 0), ("B", 40), ("C", 65)):
    yy = CY - R * math.sin(math.radians(lat))
    xx = CX - R * math.cos(math.radians(lat))
    for d in (-15, 15):
        y0 = yy + d
        # snijpunt met de bol
        dy = y0 - CY
        if abs(dy) < R:
            xs = CX - math.sqrt(R * R - dy * dy)
            ZB.pijl(60, y0, xs, y0, "#e8c547", 3)
    ya, yb = yy - 15, yy + 15
    xa, xb = CX - math.sqrt(R * R - (ya - CY) ** 2), CX - math.sqrt(R * R - (yb - CY) ** 2)
    ZB.lijn(xa, ya, xb, yb, ROOD, 6)
    ZB.letter(xx + 75, yy, k)
ZZB = {}
for k, lat in (("A", 0), ("B", 40), ("C", 65)):
    yy = CY - R * math.sin(math.radians(lat)); xx = CX - R * math.cos(math.radians(lat))
    ZZB[k] = [Prent.rond(xx, yy, 34), Prent.rond(xx + 75, yy, 26)]

VRAGEN = [
    klik(
        "Klik op de laag waar het weer zich afspeelt.",
        TP.bestand, ZTP["A"],
        "In de troposfeer zit bijna alle waterdamp, en dus de wolken.",
    ),
    klik(
        "Klik op de laag waar de temperatuur stijgt doordat ozon ultraviolet opneemt.",
        TP.bestand, ZTP["B"],
        "In de stratosfeer zet de ozonlaag uv om in warmte.",
    ),
    klik(
        "Klik op de tropopauze.",
        TP.bestand, ZPAUZE,
        "Op ongeveer 12 km stopt de temperatuurdaling: de grens tussen troposfeer en stratosfeer.",
    ),
    met_prent(TP.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("In laag C daalt de temperatuur met de hoogte.", J),
            ("De koudste temperatuur zit bovenaan laag C.", J),
            ("In laag A stijgt de temperatuur met de hoogte.", F),
            ("Een verkeersvliegtuig vliegt in laag C.", F),
        ],
        "Een vliegtuig vliegt op 10 à 12 km, bovenaan laag A of net erboven.",
    )),
    met_prent(TP.bestand, inv(
        "Kijk naar de grafiek. Aan de grond is het 15 °C. Hoeveel graden is het ongeveer op 2 km hoogte? Neem 6,5 °C per km.",
        ["2"],
        "15 - 2 · 6,5 = 2 °C.",
    )),
    klik(
        "Klik op de plaats waar dezelfde bundel zonlicht op het kleinste oppervlak valt.",
        ZB.bestand, ZZB["A"],
        "Op de evenaar valt het licht op 21 maart bijna loodrecht in.",
    ),
    met_prent(ZB.bestand, tabel(
        "Kijk naar de bundels. Klopt dit?",
        [
            ("Bij C wordt dezelfde energie over het grootste oppervlak verspreid.", J),
            ("Bij A komt er per vierkante meter de meeste energie aan.", J),
            ("Bij C staat de zon het hoogst.", F),
            ("Het verschil komt van de invalshoek van de zonnestralen.", J),
        ],
        "Hoe schuiner de stralen, hoe minder energie per vierkante meter.",
    )),
    tabel(
        "In welke laag?",
        [
            ("bijna alle wolken", "Troposfeer"),
            ("de ozonlaag die uv tegenhoudt", "Stratosfeer"),
            ("de laag die overgaat in de ruimte", "Exosfeer"),
            ("de temperatuur daalt er met ongeveer 6,5 °C per km", "Troposfeer"),
        ],
        "Van onder naar boven: tropo-, strato-, meso-, thermo- en exosfeer.",
        kolommen=["Troposfeer", "Stratosfeer", "Exosfeer"],
    ),
    tabel(
        "Ozon: beschermend of schadelijk?",
        [
            ("ozon op 25 km hoogte", "Beschermend"),
            ("ozon bij de grond op een hete zomerdag", "Schadelijk"),
            ("ozon dat ultraviolet opslorpt", "Beschermend"),
            ("ozon dat longen en gewassen aantast", "Schadelijk"),
        ],
        "Hoog nuttig, laag schadelijk.",
        kolommen=["Beschermend", "Schadelijk"],
    ),
    volgorde(
        "Zet het ontstaan van ozon in de stratosfeer in de juiste volgorde.",
        [
            "Ultraviolet licht valt op een zuurstofmolecule",
            "De molecule splitst in twee zuurstofatomen",
            "Elk atoom hecht zich aan een andere zuurstofmolecule",
            "Er ontstaat ozon, met drie zuurstofatomen",
        ],
        "Uv splijt, de losse atomen binden opnieuw.",
    ),
    tabel(
        "Samenstelling van droge lucht: welk aandeel hoort erbij?",
        [
            ("stikstof", "ongeveer 78 %"),
            ("zuurstof", "ongeveer 21 %"),
            ("argon, koolstofdioxide en andere", "ongeveer 1 %"),
        ],
        "Stikstof is veruit het grootste deel.",
        kolommen=["ongeveer 78 %", "ongeveer 21 %", "ongeveer 1 %"],
    ),
    tabel(
        "Is dit een broeikasgas?",
        [
            ("waterdamp", J),
            ("methaan", J),
            ("argon", F),
            ("lachgas", J),
            ("stikstof", F),
        ],
        "Broeikasgassen houden langgolvige warmtestraling tegen.",
    ),
    tabel(
        "Kortgolvig of langgolvig?",
        [
            ("de straling die van de zon komt", "Kortgolvig"),
            ("de warmtestraling van de aarde", "Langgolvig"),
            ("zichtbaar licht", "Kortgolvig"),
            ("de straling die broeikasgassen tegenhouden", "Langgolvig"),
        ],
        "Een heet voorwerp zendt kortgolvig uit, een koud langgolvig.",
        kolommen=["Kortgolvig", "Langgolvig"],
    ),
    sorteer(
        "Sorteer van hoog naar laag albedo.",
        ["Hoog albedo", "Laag albedo"],
        [
            ["verse sneeuw", "Hoog albedo"],
            ["een donker naaldbos", "Laag albedo"],
            ["een witte wolk", "Hoog albedo"],
            ["de open oceaan", "Laag albedo"],
        ],
        "Lichte oppervlakken weerkaatsen veel, donkere slorpen op.",
    ),
    tabel(
        "Welk soort factor bepaalt hier de temperatuur?",
        [
            ("de breedteligging", "Rotatie en revolutie"),
            ("de hoogteligging", "Geografisch"),
            ("een warme zeestroom", "Geografisch"),
            ("de bewolking van die nacht", "Lokaal"),
            ("een zuidelijke helling", "Lokaal"),
        ],
        "Zo deelt het examen de factoren in.",
        kolommen=["Rotatie en revolutie", "Geografisch", "Lokaal"],
    ),
    casus(
        "Oostende ligt aan zee, Moskou ver landinwaarts. Beide hebben ongeveer dezelfde gemiddelde jaartemperatuur.",
        [
            tabel(
                "Klopt dit?",
                [
                    ("Moskou heeft warmere zomers.", J),
                    ("Moskou heeft koudere winters.", J),
                    ("Oostende heeft het grootste verschil tussen zomer en winter.", F),
                ],
                "Water warmt traag op en koelt traag af.",
            ),
            keuze(
                "De [[*Noord-Atlantische Drift|Labradorstroom|Canarische stroom]] maakt de winters aan onze kust nog zachter.",
                "Het verlengde van de Golfstroom brengt warm water.",
            ),
        ],
    ),
    mk(
        "Waarom koelt een heldere nacht sterker af dan een bewolkte?",
        [
            "Zonder wolken ontsnapt de warmte van de aarde vrij",
            "Op een heldere nacht waait de wind altijd uit het noorden",
            "Wolken maken zelf warmte aan zoals een kachel dat doet",
            "Zonder wolken komt er 's nachts koud licht van de maan",
        ],
        0,
        "Wolken werken als een deken voor langgolvige straling.",
    ),
    tabel(
        "Klopt dit over het hitte-eilandeffect?",
        [
            ("Steen en asfalt slaan overdag warmte op.", J),
            ("Er is in de stad weinig groen dat verkoelt.", J),
            ("Een stad is daardoor vaak warmer dan het platteland.", J),
            ("Het effect is 's nachts helemaal weg.", F),
        ],
        "Vooral 's nachts geeft de stad haar opgeslagen warmte af.",
    ),
    keuze(
        "Het warmste moment van een zonnige dag valt meestal [[*enkele uren na de middag|precies om 12 uur|kort na zonsopgang]].",
        "De bodem neemt na de middag nog een tijd meer warmte op dan hij afgeeft.",
    ),
    inv(
        "Een bergtop ligt 3000 m hoger dan het dal. In het dal is het 20 °C. Hoeveel graden is het ongeveer op de top? Neem 6,5 °C per km.",
        ["0,5", "0.5"],
        "3 · 6,5 = 19,5 graden kouder: 20 - 19,5 = 0,5 °C.",
    ),
    sleep(
        "Isothermen verbinden plaatsen met dezelfde [[temperatuur]]. Liggen ze [[dicht]] bij elkaar, dan verandert de temperatuur er [[snel]] over een korte afstand.",
        ["luchtdruk", "ver", "traag"],
        "Zoals hoogtelijnen op een wandelkaart.",
    ),
    tabel(
        "Klopt dit over de troposfeer?",
        [
            ("Ze is boven de evenaar dikker dan boven de polen.", J),
            ("Op 10 km hoogte is de luchtdruk ongeveer een kwart van die aan zee.", J),
            ("Op 10 km kan je zonder hulp gewoon ademen.", F),
        ],
        "Daarom hebben vliegtuigen een drukcabine.",
    ),
    met_prent(ZB.bestand, keuze(
        "De rode streepjes tonen het oppervlak waarop elke bundel valt. Het langste streepje ligt bij [[*C|B|A]].",
        "Daar is de energie per vierkante meter het kleinst.",
    )),
    klik(
        "Klik op de laag waar de koudste temperatuur van de grafiek bereikt wordt.",
        TP.bestand, ZTP["C"],
        "Bovenaan de mesosfeer zakt de temperatuur tot ongeveer -90 °C.",
    ),
    tabel(
        "Klopt dit over de luchtdruk en de dichtheid?",
        [
            ("Ze nemen af als je hoger komt.", J),
            ("Boven je hoofd ligt hoger minder lucht te wegen.", J),
            ("In de exosfeer botsen de moleculen voortdurend.", F),
        ],
        "In de exosfeer zitten de moleculen zo ver uiteen dat ze elkaar bijna nooit raken.",
    ),
    keuze(
        "Waarom vliegen vliegtuigen graag net boven de troposfeer? Er is daar minder [[*turbulentie|zuurstof voor de motor|zonlicht]] en minder luchtweerstand.",
        "Boven het weer is het rustiger.",
    ),
    inv(
        "Verse sneeuw weerkaatst ongeveer 90 % van het zonlicht. Hoeveel procent slorpt ze op?",
        ["10"],
        "100 - 90 = 10 %.",
    ),
    tabel(
        "Klopt dit over de stralingsbalans?",
        [
            ("De aarde ontvangt kortgolvige straling van de zon.", J),
            ("De aarde zendt langgolvige warmtestraling uit.", J),
            ("Broeikasgassen houden een deel van de warmtestraling tegen.", J),
            ("Zonder atmosfeer zou het op aarde warmer zijn.", F),
        ],
        "Zonder het natuurlijke broeikaseffect zou het veel kouder zijn.",
    ),
    open_(
        "Leg uit waarom het in een hooggebergte koud is, ook al ligt het op de evenaar.",
        "De lucht wordt van de bodem uit opgewarmd. Hoog in de bergen is de lucht dunner en houdt ze minder warmte vast. In de troposfeer daalt de temperatuur met ongeveer 6,5 °C per kilometer, dus op grote hoogte is het veel kouder dan aan de voet.",
    ),
]
