r"""Grafische voorstellingen kiezen en lezen — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen, zes eigen mini-grafieken en een
misleidende grafiek, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

GROEN = "#5f7f4a"
ZG = Prent("zes-grafieken", "Zes grafische voorstellingen", "zes kleine grafieken in twee rijen met de letters A tot F: A een histogram met aansluitende staven, B een spreidingsdiagram, C een boxplot, D losse staven met namen eronder, E een dotplot met stapeltjes stippen, F een lijndiagram met jaartallen")
VAKKEN = {"A": (80, 105), "B": (390, 105), "C": (700, 105), "D": (80, 385), "E": (390, 385), "F": (700, 385)}
BR, HO = 250, 200
for c, (x0, y0) in VAKKEN.items():
    ZG.rect(x0, y0, BR, HO, "#ffffff", DONKER, 8, 2)
    ZG.letter(x0 + 20, y0 - 18, c)
    ZG.lijn(x0 + 25, y0 + HO - 30, x0 + BR - 15, y0 + HO - 30, DONKER, 2)
    ZG.lijn(x0 + 25, y0 + HO - 30, x0 + 25, y0 + 20, DONKER, 2)

# A histogram
x0, y0 = VAKKEN["A"]
for i, h in enumerate([30, 70, 120, 140, 90, 40]):
    ZG.rect(x0 + 30 + i * 33, y0 + HO - 30 - h, 33, h, "#c4d5b5", DONKER, 0, 2)
# B spreidingsdiagram
x0, y0 = VAKKEN["B"]
for i, (a, b) in enumerate([(10, 20), (30, 35), (45, 30), (60, 60), (80, 55), (95, 90), (120, 85), (140, 110), (160, 120), (180, 140), (200, 135)]):
    ZG.cirkel(x0 + 30 + a, y0 + HO - 40 - b * 0.9, 5, GROEN, DONKER, 1)
# C boxplot
x0, y0 = VAKKEN["C"]
yc = y0 + 85
ZG.lijn(x0 + 45, yc, x0 + 85, yc, DONKER, 2)
ZG.rect(x0 + 85, yc - 30, 80, 60, "#c4d5b5", DONKER, 0, 2)
ZG.lijn(x0 + 120, yc - 30, x0 + 120, yc + 30, DONKER, 3)
ZG.lijn(x0 + 165, yc, x0 + 220, yc, DONKER, 2)
ZG.lijn(x0 + 45, yc - 15, x0 + 45, yc + 15, DONKER, 2)
ZG.lijn(x0 + 220, yc - 15, x0 + 220, yc + 15, DONKER, 2)
# D staafdiagram
x0, y0 = VAKKEN["D"]
for i, (h, t) in enumerate([(110, "Lat"), (70, "Wet"), (130, "Eco"), (50, "Kun")]):
    ZG.rect(x0 + 40 + i * 50, y0 + HO - 30 - h, 32, h, "#c4d5b5", DONKER, 0, 2)
    ZG.tekst(x0 + 56 + i * 50, y0 + HO - 10, t, 14, "middle", "#5c6356")
# E dotplot
x0, y0 = VAKKEN["E"]
for i, n in enumerate([1, 3, 5, 4, 2, 1]):
    for k in range(n):
        ZG.cirkel(x0 + 50 + i * 33, y0 + HO - 45 - k * 22, 8, GROEN, DONKER, 1)
# F lijndiagram
x0, y0 = VAKKEN["F"]
pts = [(0, 60), (1, 75), (2, 70), (3, 100), (4, 120), (5, 115)]
d = " ".join(f"{'M' if i == 0 else 'L'}{x0 + 45 + a * 36},{y0 + HO - 40 - b}" for i, (a, b) in enumerate(pts))
ZG.pad(d, "none", GROEN, 3)
for a, b in pts:
    ZG.cirkel(x0 + 45 + a * 36, y0 + HO - 40 - b, 4, GROEN, DONKER, 1)
for a, t in [(0, "2020"), (5, "2025")]:
    ZG.tekst(x0 + 45 + a * 36, y0 + HO - 10, t, 14, "middle", "#5c6356")


def vak(c):
    x0, y0 = VAKKEN[c]
    return [Prent.zone(x0 - 10, y0 - 40, BR + 20, HO + 50)]


# Misleidende staafgrafiek -----------------------------------------------------------------
MS = Prent("misleidende-staven", "Leerlingen die met de fiets komen", "een staafdiagram met drie staven voor de scholen Noord (82), Midden (85) en Zuid (88); de verticale as begint bij 80 en loopt tot 90, waardoor Zuid vier keer zo hoog lijkt als Noord")
L, B, T = 200, 520, 100


def Ym(v):
    return B - (B - T) * (v - 80) / 10


MS.lijn(L, B, 850, B, DONKER, 3)
MS.lijn(L, B, L, T - 10, DONKER, 3)
for v in range(80, 91, 2):
    MS.lijn(L - 8, Ym(v), L, Ym(v), DONKER, 2)
    MS.tekst(L - 14, Ym(v) + 6, str(v), 18, "end")
MS.tekst(L, T - 25, "aantal leerlingen", 18, "start", "#5c6356")
for i, (t, v) in enumerate([("Noord", 82), ("Midden", 85), ("Zuid", 88)]):
    x = L + 90 + i * 210
    MS.rect(x, Ym(v), 120, B - Ym(v), "#c4d5b5", DONKER, 0, 2)
    MS.tekst(x + 60, B + 32, t, 20)
Z_AS = [Prent.zone(L - 80, T - 40, 110, B - T + 60)]

VRAGEN = [
    klik("Klik op de grafiek die het best past om een verloop in de tijd te tonen.", ZG.bestand, vak("F"),
         "Een lijndiagram met de tijd op de horizontale as."),
    klik("Klik op de grafiek die de vijf kengetallen van een dataset toont.", ZG.bestand, vak("C"),
         "Een boxplot: minimum, Q1, mediaan, Q3 en maximum."),
    klik("Klik op de grafiek die bij een niet-numerieke variabele zoals studierichting hoort.", ZG.bestand, vak("D"),
         "Een staafdiagram met losse staven per categorie."),
    klik("Klik op de grafiek waarin je elke afzonderlijke waarde van een kleine dataset ziet.", ZG.bestand, vak("E"),
         "Een dotplot: één stip per gegeven."),
    klik("Klik op de grafiek die een continue variabele in klassen toont.", ZG.bestand, vak("A"),
         "Een histogram: de staven sluiten op elkaar aan."),
    met_prent(ZG.bestand, tabel("Welke grafiek kies je?", [
        ("het verband tussen slaapuren en toetsscore", "B"),
        ("het aantal leerlingen per hobby", "D"),
        ("de lengte van 2000 rekruten", "A"),
    ], "Twee numerieke variabelen: spreidingsdiagram; categorieën: staafdiagram; veel continue waarden: histogram.",
       kolommen=["A", "B", "D"])),
    met_prent(ZG.bestand, inv("Hoeveel gegevens telt de dataset in dotplot E?", ["16"],
              "1 + 3 + 5 + 4 + 2 + 1 = 16.")),
    met_prent(ZG.bestand, keuze("Het histogram A is ongeveer [[*symmetrisch met één top|scheef naar rechts|tweetoppig]].",
              "De staven stijgen en dalen ongeveer even snel rond één top.")),
    klik("Klik op wat deze grafiek misleidend maakt.", MS.bestand, Z_AS,
         "De verticale as begint bij 80 in plaats van 0."),
    met_prent(MS.bestand, inv("Hoeveel procent meer fietsers heeft Zuid dan Noord? Rond af op een geheel getal.", ["7", "7%", "7 procent"],
              "(88 − 82) / 82 ≈ 0,073."),),
    met_prent(MS.bestand, keuze("Op het eerste gezicht lijkt de staaf van Zuid ongeveer [[*vier|twee|anderhalve]] keer zo hoog als die van Noord.",
              "Vanaf 80 gemeten: 8 tegenover 2.")),
    met_prent(MS.bestand, mk("Hoe maak je deze grafiek eerlijk?",
              ["de verticale as bij 0 laten beginnen",
               "de staven driedimensionaal tekenen",
               "de schooltjes in een andere volgorde zetten",
               "een lijndiagram maken van de drie scholen"], 0,
              "Bij een staafdiagram hoort de as bij 0 te beginnen.")),
    sorteer("Welke grafiek past het best?", ["lijndiagram", "staafdiagram", "boxplot"], [
        ["de temperatuur per uur op één dag", "lijndiagram"],
        ["het aantal leden per jeugdbeweging", "staafdiagram"],
        ["de spreiding van loontjes in drie bedrijven vergelijken", "boxplot"],
        ["het aantal inwoners van een stad per jaar sinds 1990", "lijndiagram"],
    ], "Tijd: lijndiagram. Categorieën: staafdiagram. Spreiding vergelijken: boxplots naast elkaar."),
    tabel("Klopt dit over grafische voorstellingen?", [
        ("bij een histogram staan de staven tegen elkaar", J),
        ("een boxplot toont hoeveel gegevens er in elke klasse vallen", F),
        ("een 3D-staafdiagram leest moeilijker dan een vlak", J),
        ("uit een histogram lees je het exacte gemiddelde af", F),
    ], "Een histogram toont klassen, geen afzonderlijke waarden; een boxplot toont posities."),
    casus(
        "Een gemeente toont in een folder het aantal bezoekers van de bibliotheek: 2021: 12 000, 2022: 12 400, 2023: 12 900, 2025: 15 800. "
        "Ze tekent een lijndiagram met vier punten op gelijke afstand.",
        [
            keuze("Het jaar [[*2024|2021|2026]] ontbreekt.", "Na 2023 springt de reeks naar 2025."),
            mk("Waarom is de grafiek misleidend?",
               ["de laatste stijging lijkt over één jaar te gaan",
                "een lijndiagram mag nooit voor bezoekers gebruikt worden",
                "de getallen zijn te groot om in een grafiek te zetten",
                "er staan te weinig kleuren in de lijnen van de grafiek"], 0,
               "Gelijke afstanden suggereren gelijke tijdsstappen."),
            inv("Hoeveel bezoekers kwamen er gemiddeld per jaar bij tussen 2023 en 2025?", ["1450"],
                "(15 800 − 12 900) / 2 = 1450."),
        ],
    ),
    koppel("Koppel de grafiek aan wat je er goed in ziet.", [
        ["histogram", "de vorm van de verdeling"],
        ["boxplot", "mediaan, kwartielen en uitschieters"],
        ["spreidingsdiagram", "samenhang tussen twee variabelen"],
    ], ["het verloop van één categorie"], "Elke grafiek heeft haar sterkte."),
    sleep("Een grafiek heeft altijd een [[titel]] en bij elke as een naam met [[eenheid]].",
          ["legende", "kleur"], "Zonder dat kan een lezer niets met de grafiek."),
    met_prent(ZG.bestand, keuze("Uit boxplot C kan je [[*niet|wel]] aflezen hoeveel gegevens er in de dataset zitten.",
              "Een boxplot toont posities, geen aantallen.")),
    met_prent(ZG.bestand, keuze("De modus van de gegevens in dotplot E ligt bij de [[*derde|eerste|zesde]] stapel van links.",
              "De hoogste stapel: vijf stippen.")),
    met_prent(ZG.bestand, keuze("Spreidingsdiagram B toont een [[*positieve|negatieve]] samenhang.",
              "De punten stijgen van links naar rechts.")),
    met_prent(ZG.bestand, tabel("Staan de staven tegen elkaar?", [
        ("grafiek A", J),
        ("grafiek D", F),
        ("een histogram van gewichten in klassen", J),
    ], "Histogram: aansluitend. Staafdiagram: los.")),
    mk("Welke voorstelling kies je om te tonen dat één afdeling veel meer uitschieters heeft dan drie andere?",
       ["vier boxplots naast elkaar",
        "één lijndiagram met vier lijnen",
        "een staafdiagram met het gemiddelde per afdeling",
        "één histogram van alle afdelingen samen"], 0,
       "Een boxplot toont uitschieters apart als punten."),
    inv("Een histogram heeft klassen van 10 breed en de staaf van [40, 50[ is 24 hoog. Hoeveel gegevens liggen er tussen 40 en 50?", ["24"],
        "Bij gelijke klassenbreedtes is de hoogte de frequentie."),
    tabel("Is deze grafiek eerlijk?", [
        ("staafdiagram met as vanaf 0, met titel en eenheid", J),
        ("lijndiagram met jaartallen 2019, 2020, 2024 op gelijke afstand", F),
        ("twee histogrammen naast elkaar met een andere verticale schaal", F),
    ], "Gelijke stappen, gelijke schalen, as vanaf 0 bij staven."),
    keuze("Een histogram met een lange staart naar rechts heet [[*scheef naar rechts|scheef naar links|symmetrisch]].",
          "De staart wijst naar de kant van de scheefheid."),
    volgorde("Zet de stappen om een goede grafiek te maken in de juiste volgorde.", [
        "nagaan welk soort variabele je hebt",
        "de passende voorstelling kiezen",
        "de grafiek met ICT maken",
        "titel, asnamen en eenheden controleren",
    ], "Het soort variabele bepaalt de grafiek."),
    inv("Een dotplot toont boven de waarden 2, 3 en 4 respectievelijk 3, 6 en 1 stippen. Hoeveel is het gemiddelde? Schrijf als decimaal getal.", ["2,8", "2.8"],
        "(2 · 3 + 3 · 6 + 4 · 1) / 10 = 28 / 10."),
    open_("Een leerling maakt een histogram van de lengte van jongens en meisjes samen en ziet twee toppen. Wat besluit je en wat zou je aanraden?",
          "Er zitten waarschijnlijk twee groepen in de data met een ander gemiddelde. Het is beter om voor jongens en meisjes een apart histogram of twee boxplots naast elkaar te maken."),
]
