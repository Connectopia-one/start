"""Productiefactoren, productiefunctie en meeropbrengsten — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_productie, met een zelfgetekende TP-curve om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, ROOD, DONKER

# TP bij 0..8 werknemers; MP: 12, 18, 24, 16, 10, 4, 0, -6
TPW = [0, 12, 30, 54, 70, 80, 84, 84, 78]
TC = Prent("tp-curve", "Totale productie van een werkplaats", "totale productie TP bij 0 tot 8 werknemers, met punten A tot E")
OX, OY = 140, 560
def P(n, tp): return OX + n * 85, OY - tp * 5.6
TC.lijn(OX, OY, OX + 740, OY, DONKER, 3); TC.lijn(OX, OY, OX, 60, DONKER, 3)
for n in range(1, 9):
    TC.lijn(P(n, 0)[0], OY, P(n, 0)[0], OY + 8, DONKER, 2); TC.tekst(P(n, 0)[0], OY + 28, str(n), 16)
for v in range(10, 90, 10):
    TC.lijn(OX - 8, P(0, v)[1], OX, P(0, v)[1], DONKER, 2); TC.tekst(OX - 14, P(0, v)[1] + 5, str(v), 15, "end")
    TC.lijn(OX, P(0, v)[1], OX + 740, P(0, v)[1], "#ebe7dc", 1)
TC.tekst(OX + 740, OY + 56, "aantal werknemers", 18, "end"); TC.tekst(OX - 10, 50, "TP (stuks per dag)", 18, "start")
TC.pad("M " + " L ".join(f"{P(n, t)[0]},{P(n, t)[1]:.1f}" for n, t in enumerate(TPW)), "none", BLAUW, 4)
LET = {"A": 2, "B": 3, "C": 5, "D": 7, "E": 8}
for t, n in LET.items():
    x, y = P(n, TPW[n]); TC.cirkel(x, y, 7, DONKER, DONKER, 1); TC.letter(x, y - 36, t)
U = "tp-curve.svg"
Z = {t: Prent.zone(P(n, TPW[n])[0] - 34, P(n, TPW[n])[1] - 60, 68, 80) for t, n in LET.items()}

VRAGEN = [
    klik("De grafiek toont de totale productie bij een vaste werkplaats. Klik op het punt waar de toenemende meeropbrengsten eindigen.", U, [Z["B"]],
         "MP is 12, 18, 24, dan 16: de derde werknemer heeft de grootste MP. Daarna nemen de meeropbrengsten af."),
    klik("Klik op het punt waar de laatste werknemer niets meer toevoegt aan de totale productie.", U, [Z["D"]],
         "Bij 6 en 7 werknemers is TP 84. De zevende voegt niets toe: MP = 0."),
    klik("Klik op het punt waar een extra werknemer de totale productie doet dalen.", U, [Z["E"]],
         "Van 7 naar 8 werknemers daalt TP van 84 naar 78: MP = −6."),
    casus("Lees de tabel van een fietsherstelplaats.\n\nwerknemers: 1 · 2 · 3 · 4 · 5 · 6\nTP (fietsen per dag): 8 · 20 · 36 · 46 · 52 · 54", [
        tabel("Hoe groot is MP van deze werknemer?",
              [("de 2de", "12"), ("de 3de", "16"), ("de 4de", "10"), ("de 6de", "2")],
              "MP = TP min de vorige TP.",
              kolommen=["2", "10", "12", "16"]),
        inv("Hoe groot is de gemiddelde productie bij 4 werknemers? Schrijf het getal met een komma als het nodig is.", ["11,5", "11.5"],
            "46 / 4 = 11,5 fietsen per werknemer."),
        keuze("Vanaf de [[*4de|2de|6de]] werknemer nemen de meeropbrengsten af.",
              "MP: 8, 12, 16, 10, 6, 2. De top ligt bij de derde."),
        keuze("Bij de 6de werknemer is TP [[*nog altijd stijgend|al dalend|gelijk gebleven]].",
              "MP is 2: positief, dus TP stijgt nog, alleen trager."),
    ]),
    koppel("Welke vergoeding hoort bij welke productiefactor?",
           [("arbeid", "loon"), ("kapitaal", "intrest"), ("natuur", "pacht"), ("ondernemerschap", "winst")],
           ["subsidie"], "Vier factoren, vier vergoedingen."),
    sorteer("Bij welke productiefactor hoort dit?", ["arbeid", "kapitaal", "natuur", "ondernemerschap"],
            [("de vrachtwagens van een transportfirma", "kapitaal"), ("het werk van een boekhouder", "arbeid"), ("een stuk landbouwgrond", "natuur"), ("beslissen wat er geproduceerd wordt", "ondernemerschap"), ("het bedrijfsgebouw", "kapitaal"), ("het water uit een bron", "natuur")],
            "Kapitaal is door mensen gemaakt; natuur komt uit de natuur."),
    tabel("Klopt dit over productiefactoren?",
          [("Geld is zelf een productiefactor.", F), ("Op lange termijn kan een bedrijf alle factoren aanpassen.", J), ("Machines horen bij natuur.", F), ("De ondernemer draagt het risico.", J)],
          "Met geld koop je productiefactoren; machines zijn kapitaal."),
    keuze("Een frituur kan snel een extra student aannemen, maar niet snel een tweede frietketel plaatsen. Op korte termijn is de frietketel de [[*vaste|variabele]] factor.",
          "Kapitaal ligt hier vast, arbeid is variabel."),
    mk("Een kleine werkplaats neemt een tweede en een derde werknemer aan, en de productie per extra werknemer stijgt. Wat is de oorzaak?",
       ["door taakverdeling en specialisatie", "omdat de machines goedkoper worden", "omdat de lonen dan lager liggen", "omdat de vraag naar het product stijgt"], 0,
       "Samen kan ieder zich op één taak toeleggen."),
    mk("In dezelfde werkplaats levert de achtste werknemer minder op dan de zevende. Wat is de oorzaak?",
       ["meer werkers op dezelfde vaste factor", "de werknemers worden ouder en trager", "de prijs van het product begint te dalen", "de ondernemer neemt minder risico"], 0,
       "Met te veel mensen op één machine sta je elkaar in de weg."),
    tabel("Stijgt, daalt of blijft TP gelijk bij een extra werknemer?",
          [("MP = 15", "stijgt"), ("MP = 0", "blijft gelijk"), ("MP = −3", "daalt"), ("MP = 1", "stijgt")],
          "Het teken van MP beslist.",
          kolommen=["stijgt", "blijft gelijk", "daalt"]),
    inv("TP bij 4 werknemers is 100 stuks, bij 5 werknemers 118 stuks. Hoe groot is MP van de vijfde? Schrijf enkel het getal.", ["18"],
        "118 − 100 = 18."),
    inv("Een atelier maakt met 8 werknemers 200 stuks. Hoe groot is de gemiddelde productie? Schrijf enkel het getal.", ["25"],
        "200 / 8 = 25 stuks per werknemer."),
    inv("MP van de eerste vier werknemers is 10, 14, 11 en 7. Hoe groot is TP bij vier werknemers? Schrijf enkel het getal.", ["42"],
        "TP is de som van de MP-waarden: 10 + 14 + 11 + 7 = 42."),
    keuze("De wet van de toe- en afnemende meeropbrengsten geldt op [[*korte termijn|lange termijn|elke termijn]].",
          "Ze veronderstelt dat minstens één factor vastligt."),
    keuze("Een bedrijf verdubbelt op lange termijn al zijn factoren en de productie stijgt met meer dan het dubbele. Dat heet [[*schaalvoordelen|afnemende meeropbrengsten|een vaste factor]].",
          "Groter worden maakt het per stuk efficiënter."),
    keuze("Een boer huurt een weide en betaalt daarvoor [[*pacht|intrest|loon]].",
          "Pacht vergoedt de factor natuur."),
    tabel("Kapitaalgoed of intermediair goed voor een meubelmaker?",
          [("een zaagmachine", "kapitaalgoed"), ("eikenhouten planken", "intermediair goed"), ("schroeven en lijm", "intermediair goed"), ("een werkbank", "kapitaalgoed")],
          "Een kapitaalgoed blijft; een intermediair goed gaat op in het product.",
          kolommen=["kapitaalgoed", "intermediair goed"]),
    sleep("De productiefunctie toont het verband tussen de ingezette [[productiefactoren]] en de [[productie]]. Op korte termijn ligt minstens één factor [[vast]].",
          ["winst", "variabel"], "Wat is een productiefunctie?"),
    keuze("Dalende meeropbrengsten doen de kosten per stuk [[*stijgen|dalen]].",
          "Elke extra werknemer kost evenveel, maar levert minder extra op."),
    klik("Klik op het punt waar de gemiddelde productie het hoogst is.", U, [Z["B"]],
         "GP = TP gedeeld door het aantal werknemers. A: 30 / 2 = 15. B: 54 / 3 = 18. C: 80 / 5 = 16. D: 84 / 7 = 12. E: 78 / 8 = 9,75."),
    keuze("Een extra werknemer die de anderen in de weg loopt, heeft een [[*negatieve|positieve]] marginale productie.",
          "Dan daalt TP."),
    inv("TP bij 1 tot 4 werknemers: 15, 35, 50, 58. Bij welke werknemer is MP het grootst? Schrijf het rangnummer.", ["2", "de 2de", "tweede"],
        "MP: 15, 20, 15, 8. De tweede werknemer voegt het meest toe."),
    tabel("Korte of lange termijn?",
          [("een extra ploeg werknemers inzetten", "korte termijn"), ("een tweede fabriek bouwen", "lange termijn"), ("overuren laten presteren", "korte termijn"), ("een nieuwe productielijn plaatsen", "lange termijn")],
          "Op korte termijn ligt het kapitaal vast.",
          kolommen=["korte termijn", "lange termijn"]),
    keuze("Een bedrijf plaatst zonnepanelen voor eigen stroom. Daarbij spelen de factoren [[*natuur en kapitaal|arbeid en winst|natuur en loon]] mee.",
          "De zon is natuur, de panelen zijn kapitaal."),
    keuze("Zolang MP positief is, [[*blijft TP stijgen|daalt TP|blijft TP gelijk]].",
          "Elke werknemer voegt nog iets toe."),
    open_("Twee bakkerijen hebben dezelfde ovens en evenveel personeel, maar de ene bakt meer. Geef een mogelijke reden.",
          "De ene bakkerij is beter georganiseerd of haar bakkers hebben meer vakkennis of zijn meer gemotiveerd.",
          "Organisatie en vakkennis bepalen mee hoeveel productie je haalt."),
]
