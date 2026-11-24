"""De arbeidsmarkt en de collectieve afspraken — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_arbeid, met een zelfgetekende arbeidsmarkt met minimumloon om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, PAARS, DONKER

# Vraag naar arbeid Qv = 900 − 30W, aanbod Qa = 300 + 20W: evenwicht W = 12, Q = 540. Minimumloon 15.
AM = Prent("arbeidsmarkt-minimumloon", "Arbeidsmarkt voor magazijniers", "vraag naar en aanbod van arbeid met een minimumloon van 15 euro per uur en punten A tot D")
OX, OY = 140, 570
def P(q, w): return OX + q * 0.95, OY - w * 23
AM.lijn(OX, OY, OX + 760, OY, DONKER, 3); AM.lijn(OX, OY, OX, 50, DONKER, 3)
for q in range(100, 800, 100):
    AM.lijn(P(q, 0)[0], OY, P(q, 0)[0], OY + 8, DONKER, 2); AM.tekst(P(q, 0)[0], OY + 28, str(q), 16)
for w in range(2, 22, 2):
    AM.lijn(OX - 8, P(0, w)[1], OX, P(0, w)[1], DONKER, 2); AM.tekst(OX - 14, P(0, w)[1] + 5, str(w), 15, "end")
AM.tekst(OX + 760, OY + 56, "aantal werknemers", 18, "end"); AM.tekst(OX - 10, 42, "loon W (euro per uur)", 18, "start")
AM.lijn(*P(900 - 30 * 20, 20), *P(900 - 30 * 4, 4), BLAUW, 4)
AM.lijn(*P(300 + 20 * 3, 3), *P(300 + 20 * 20, 20), ORANJE, 4)
AM.tekst(P(300, 20)[0] - 10, P(300, 20)[1] + 4, "vraag naar arbeid", 17, "end", BLAUW, True)
AM.tekst(P(700, 20)[0] + 10, P(700, 20)[1] + 22, "aanbod van arbeid", 17, "start", ORANJE, True)
AM.lijn(OX, P(0, 15)[1], OX + 740, P(0, 15)[1], PAARS, 2, True)
AM.tekst(OX + 10, P(0, 15)[1] - 8, "minimumloon 15 euro", 16, "start", PAARS, True)
AM.lijn(P(450, 15)[0], P(450, 15)[1] - 6, P(600, 15)[0], P(600, 15)[1] - 6, PAARS, 6)
PT = {"A": (540, 12), "B": (450, 15), "C": (600, 15), "D": (525, 15)}
OFF = {"A": (34, 8), "B": (-30, -28), "C": (30, -28), "D": (0, -42)}
for t, (q, w) in PT.items():
    x, y = P(q, w)
    if t != "D":
        AM.cirkel(x, y, 7, DONKER, DONKER, 1)
    AM.letter(x + OFF[t][0], y + OFF[t][1], t)
U = "arbeidsmarkt-minimumloon.svg"
Z = {t: Prent.rond(P(q, w)[0] + OFF[t][0], P(q, w)[1] + OFF[t][1], 32) for t, (q, w) in PT.items()}

VRAGEN = [
    klik("Klik op het evenwicht op deze arbeidsmarkt zonder minimumloon.", U, [Z["A"]],
         "In A snijden vraag en aanbod: 12 euro per uur, 540 werknemers."),
    klik("Klik op het punt dat toont hoeveel werknemers de bedrijven willen aanwerven bij het minimumloon.", U, [Z["B"]],
         "Bij 15 euro vragen de bedrijven 900 − 450 = 450 werknemers."),
    klik("Klik op de letter die het stuk tussen B en C aanduidt: de mensen die willen werken maar geen baan vinden.", U, [Z["D"]],
         "Tussen B (450) en C (600) zitten 150 mensen zonder werk: werkloosheid."),
    casus("Lees de gegevens van de grafiek.\n\nVraag naar arbeid: Qv = 900 − 30W\nAanbod van arbeid: Qa = 300 + 20W\nW is het loon in euro per uur.", [
        inv("Bereken het evenwichtsloon. Schrijf enkel het getal.", ["12"],
            "900 − 30W = 300 + 20W → 600 = 50W → W = 12."),
        inv("Hoeveel mensen bieden zich aan bij een minimumloon van 15 euro? Schrijf enkel het getal.", ["600"],
            "300 + 20 × 15 = 600."),
        inv("Hoe groot is de werkloosheid bij dat minimumloon? Schrijf enkel het getal.", ["150"],
            "Aanbod 600 − vraag 450 = 150."),
        keuze("Een minimumloon van 10 euro zou op deze markt [[*niets veranderen|werkloosheid veroorzaken|een tekort aan werk veroorzaken]].",
              "Het ligt onder het evenwichtsloon van 12 euro: niet bindend."),
    ]),
    tabel("Wie is vrager en wie is aanbieder?",
          [("op de arbeidsmarkt: de bedrijven", "vrager"), ("op de arbeidsmarkt: de gezinnen", "aanbieder"), ("op de goederenmarkt: de gezinnen", "vrager"), ("op de goederenmarkt: de bedrijven", "aanbieder")],
          "Op de arbeidsmarkt draaien de rollen om.",
          kolommen=["vrager", "aanbieder"]),
    tabel("Wat verschuift er?",
          [("De verkoop van fietsen stijgt sterk.", "vraag naar fietsmakers stijgt"), ("Veel fietsmakers gaan met pensioen.", "aanbod van fietsmakers daalt"), ("Er komen veel geschoolde fietsmakers uit het buitenland.", "aanbod van fietsmakers stijgt")],
          "De vraag naar arbeid is afgeleid van de vraag naar producten.",
          kolommen=["vraag naar fietsmakers stijgt", "aanbod van fietsmakers daalt", "aanbod van fietsmakers stijgt"]),
    keuze("Niemand wil arbeid om de arbeid zelf. De vraag naar arbeid is een [[*afgeleide vraag|vrije vraag|collectieve vraag]].",
          "Ze volgt uit de vraag naar de producten."),
    keuze("Voor een knelpuntberoep is de vraag naar arbeid [[*groter|kleiner]] dan het aanbod.",
          "Bedrijven vinden moeilijk mensen; het loon wordt opgedreven."),
    mk("Waarom verdient een ervaren ICT-specialist meestal meer dan een vakkenvuller?",
       ["Vraag en aanbod verschillen per beroep.", "De overheid legt alle lonen per beroep vast.", "Vakkenvullers werken minder uren per week.", "ICT-bedrijven betalen geen sociale bijdragen."], 0,
       "Een schaars beroep met veel vraag levert een hoger loon op."),
    koppel("Welk begrip over collectieve afspraken hoort bij welke omschrijving?",
           [("cao", "akkoord over loon en arbeidsvoorwaarden in een sector"), ("ipa", "akkoord over alle sectoren heen"), ("sociale partners", "vakbonden en werkgeversorganisaties"), ("indexering", "lonen stijgen mee met de prijzen")],
           ["minimumprijs"], "De collectieve afspraken in België."),
    tabel("Klopt dit over collectieve afspraken?",
          [("Een cao geldt enkel voor vakbondsleden.", F), ("Een ipa wordt per bedrijf afzonderlijk gesloten.", F), ("Een cao kan de arbeidsduur regelen.", J), ("De vakbonden onderhandelen met de werkgeversorganisaties.", J)],
          "Een cao geldt voor alle werknemers van het paritair comité; het ipa is nationaal."),
    keuze("Een sector spreekt in een cao 2 % loonsverhoging af. De loonkosten van de bedrijven [[*stijgen|dalen|blijven gelijk]].",
          "Arbeid wordt duurder."),
    keuze("De prijs op de arbeidsmarkt is het [[*loon|pacht|intrest]].",
          "Elke productiefactor heeft zijn eigen prijs."),
    sorteer("Verschuift dit de vraag naar of het aanbod van arbeid?", ["vraag", "aanbod"],
            [("vergrijzing", "aanbod"), ("meer bestellingen bij de bedrijven", "vraag"), ("immigratie van mensen op arbeidsleeftijd", "aanbod"), ("een daling van de verkoop", "vraag"), ("meer vrouwen die buitenshuis gaan werken", "aanbod"), ("robots die routinetaken overnemen", "vraag")],
            "Bevolking verschuift het aanbod; de verkoop en technologie verschuiven de vraag."),
    tabel("Is dit een argument tegen een hoog minimumloon?",
          [("Bedrijven werven minder laaggeschoolden aan.", J), ("Werkenden kunnen beter rondkomen.", F), ("Sommige jobs worden vervangen door machines.", J)],
          "Het is een afweging tussen bescherming en mogelijke werkloosheid."),
    mk("Waarom gebeurt de loonvorming in België niet volledig via de markt?",
       ["Eén werknemer staat zwak tegenover de werkgever.", "Er is in België helemaal geen vraag naar arbeid.", "Lonen mogen in België nooit of te nooit veranderen.", "De gezinnen bepalen in hun eentje alle lonen."], 0,
       "Daarom onderhandelen vakbonden collectief."),
    inv("Vraag naar arbeid: Qv = 1 200 − 40W, aanbod: Qa = 200 + 60W. Bereken het evenwichtsloon. Schrijf enkel het getal.", ["10"],
        "1 200 − 40W = 200 + 60W → 1 000 = 100W → W = 10."),
    inv("Zelfde functies. Hoeveel mensen werken er in evenwicht? Schrijf enkel het getal.", ["800"],
        "1 200 − 400 = 800 en 200 + 600 = 800."),
    keuze("Een technologische doorbraak verhoogt de productiviteit. De lonen kunnen dan stijgen [[*zonder dat de kosten per stuk stijgen|terwijl de productie daalt|omdat er minder gewerkt wordt]].",
          "Elke werknemer maakt meer."),
    sleep("Ligt het loon boven het evenwicht, dan is het aanbod van arbeid [[groter]] dan de vraag. Dat overschot heet [[werkloosheid]].",
          ["kleiner", "inflatie"], "Een te hoog loon op de arbeidsmarkt."),
    keuze("De arbeidsmarkt bestaat uit vele [[*deelmarkten per beroep en streek|gelijke markten met één loon]].",
          "Elke deelmarkt heeft een eigen evenwicht."),
    keuze("Een minimumloon onder het evenwichtsloon is [[*niet bindend|bindend]]: de markt betaalt al meer.",
          "Dan verandert er niets."),
    inv("Hoe noem je een beroep waarvoor bedrijven moeilijk mensen vinden? Schrijf één woord.", ["knelpuntberoep", "knelpuntberoepen"],
        "Bij een knelpuntberoep is de vraag groter dan het aanbod."),
    keuze("Bij een hoger loon bieden [[*meer|minder]] mensen hun arbeid aan.",
          "Werken wordt aantrekkelijker; de aanbodcurve stijgt."),
    tabel("Stijgt of daalt het evenwichtsloon in deze sector?",
          [("De vraag naar arbeid stijgt, het aanbod blijft.", "stijgt"), ("Het aanbod van arbeid stijgt, de vraag blijft.", "daalt"), ("Veel werknemers gaan met pensioen.", "stijgt")],
          "Meer vraag of minder aanbod duwt het loon omhoog.",
          kolommen=["stijgt", "daalt"]),
    keuze("Een bedrijf werft iemand aan zolang die werknemer [[*meer opbrengt dan hij kost|minder kost dan het minimumloon|jonger is dan dertig]].",
          "Dezelfde marginale redenering als bij de productie."),
    open_("Leg uit waarom het minimumloon een keuze is tussen twee doelen.",
          "Het beschermt werkenden zodat ze kunnen rondkomen, maar als het boven het evenwicht ligt, kan het tot minder aanwervingen en dus werkloosheid leiden.",
          "Bescherming tegenover mogelijke werkloosheid."),
]
