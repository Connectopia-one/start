"""Marktvormen en het monopolie — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

G = venster("monopolie-mo-mk", 0, 90, 0, 100, 10, 10)
PUNTEN = {"A": (30, 60), "B": (30, 30), "C": (60, 30), "D": (45, 45)}

GRAFIEKEN = [
    dict(naam=G, titel="Monopolist: prijsafzetcurve P = 90 − Q, MO = 90 − 2Q, MK = 30",
         krommen=[(lambda q: 90 - q, "groen", "P", (0, 82)), (lambda q: 90 - 2 * q, "oranje", "MO", (0, 45)),
                  (lambda q: 30, "blauw", "MK", (0, 88))],
         labelplek={"P": (80, 10), "MO": (41, 8), "MK": (84, 30)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="hoeveelheid", ylabel="prijs, kosten", ijk_x=10, ijk_y=10),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over het evenwicht van een monopolist")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "Klik op het punt dat de prijs en de hoeveelheid toont die de monopolist kiest om zijn winst zo groot mogelijk te maken.",
        P, [punt_zone(G, *PUNTEN["A"])],
        "Hij kiest de hoeveelheid waar MO = MK (Q = 30) en leest de prijs af op de prijsafzetcurve: punt A, prijs 60. Punt B geeft wel de hoeveelheid, maar niet de prijs.",
    ),
    klik(
        "Klik op het punt waar de markt zou uitkomen bij volkomen concurrentie met dezelfde kosten.",
        P, [punt_zone(G, *PUNTEN["C"])],
        "Bij volkomen concurrentie is de prijs gelijk aan MK: 90 − Q = 30, dus Q = 60 en P = 30. Dat is punt C.",
    ),
    klik(
        "Klik op het punt waar de totale opbrengst van de monopolist het grootst is.",
        P, [punt_zone(G, *PUNTEN["D"])],
        "De totale opbrengst is het grootst waar MO = 0, dus bij Q = 45. De prijs is dan 45: punt D.",
    ),
    klik(
        "Klik in het gebied dat het welvaartsverlies van het monopolie voorstelt.",
        P, [vak_zone(G, 31, 42, 31, 42)],
        "Het welvaartsverlies is de driehoek tussen A, B en C: de ruilen tussen Q = 30 en Q = 60 die niet meer doorgaan.",
    ),
    met_prent(P, inv(
        "Bereken het welvaartsverlies van dit monopolie. Schrijf enkel het getal.",
        "450",
        "½ · (60 − 30) · (60 − 30) = 450.",
    )),
    met_prent(P, inv(
        "De gemiddelde kosten bij de gekozen hoeveelheid zijn 40. Bereken de winst van de monopolist. Schrijf enkel het getal.",
        "600",
        "Winst = (P − GK) · Q = (60 − 40) · 30 = 600.",
    )),
    casus(
        "Een farmabedrijf heeft een patent op een geneesmiddel. De prijsafzetcurve is P = 200 − 4Q en de marginale kosten zijn 40.",
        [
            mk("Wat is de vergelijking van de marginale opbrengst?",
               ["MO = 200 − 8Q", "MO = 200 − 4Q", "MO = 200 − 2Q", "MO = 100 − 4Q"], 0,
               "Bij P = a − bQ is MO = a − 2bQ: twee keer zo steil."),
            inv("Bereken de hoeveelheid die het bedrijf zal maken. Schrijf enkel het getal.", "20",
                "200 − 8Q = 40, dus 8Q = 160 en Q = 20."),
            inv("Welke prijs vraagt het bedrijf? Schrijf enkel het getal.", "120",
                "Op de prijsafzetcurve: P = 200 − 4 · 20 = 120."),
            inv("Bij welke hoeveelheid is de totale opbrengst het grootst? Schrijf enkel het getal.", "25",
                "TO is het grootst waar MO = 0: 200 − 8Q = 0, dus Q = 25."),
        ],
    ),
    tabel(
        "Welke marktvorm past bij de beschrijving?",
        [
            ("Duizenden graanboeren; niemand kan de prijs beïnvloeden", "Atomische markt"),
            ("Honderden restaurants, elk met een eigen keuken en sfeer", "Monopolistische concurrentie"),
            ("Drie grote telecombedrijven", "Oligopolie"),
            ("Eén spoorbedrijf mag als enige het net uitbaten", "Monopolie"),
        ],
        "Hoe minder aanbieders en hoe moeilijker toetreden, hoe meer invloed op de prijs.",
        kolommen=["Atomische markt", "Monopolistische concurrentie", "Oligopolie", "Monopolie"],
    ),
    volgorde(
        "Zet deze marktvormen van weinig naar veel invloed van een aanbieder op de prijs.",
        ["Atomische markt", "Monopolistische concurrentie", "Oligopolie", "Monopolie"],
        "Prijsnemer, een beetje invloed, veel invloed, prijszetter.",
    ),
    mk(
        "Van welke twee dingen hangt de marktvorm vooral af?",
        ["Het aantal marktpartijen en de toetredingsmogelijkheden", "De prijs van het product en het inkomen van de kopers op die markt",
         "De grootte van het land en het aantal inwoners", "De kwaliteit van het product en de reclame-uitgaven"],
        0,
        "Hoeveel aanbieders er zijn en hoe gemakkelijk een nieuwe aanbieder kan beginnen.",
    ),
    mk(
        "Een markt is heel transparant. Wat betekent dat?",
        ["Kopers en verkopers hebben een goed overzicht van prijzen en kwaliteit",
         "De overheid publiceert de winst van elk bedrijf op een website",
         "Iedereen mag zonder vergunning een bedrijf beginnen op die markt",
         "Alle aanbieders verkopen exact hetzelfde product aan dezelfde prijs"],
        0,
        "Transparant: je ziet goed wat er te koop is, aan welke prijs en welke kwaliteit.",
    ),
    tabel(
        "Een bedrijf heeft TCK = 300. Bij 25 stuks zijn de TVK 700. Bereken.",
        [
            ("TK", "1 000"),
            ("GK", "40"),
            ("GCK", "12"),
            ("GVK", "28"),
        ],
        "TK = 300 + 700 = 1 000. GK = 1 000 / 25 = 40. GCK = 300 / 25 = 12. GVK = 700 / 25 = 28.",
        kolommen=["1 000", "40", "12", "28"],
    ),
    inv(
        "Het maken van 30 stuks kost 900 euro, het maken van 31 stuks kost 935 euro. Hoe groot zijn de marginale kosten van het 31ste stuk? Schrijf enkel het getal.",
        "35",
        "935 − 900 = 35 euro.",
    ),
    keuze(
        "De MK-curve snijdt de GK-curve in haar [[*laagste|hoogste]] punt, en de GCK [[*dalen|stijgen]] als de productie stijgt.",
        "De vaste kosten worden over meer stuks verdeeld, en MK trekt GK omlaag zolang ze eronder ligt.",
    ),
    mk(
        "Waarom ligt de MO-curve van een monopolist onder zijn prijsafzetcurve?",
        ["Om een stuk meer te verkopen, moet hij de prijs verlagen voor alle stuks die hij verkoopt",
         "Omdat zijn marginale kosten altijd hoger zijn dan de prijs die hij aan de klant vraagt",
         "Omdat de overheid een deel van elke extra verkoop als belasting van hem afneemt",
         "Omdat hij bij elk extra stuk ook extra vaste kosten moet betalen aan zijn leveranciers"],
        0,
        "De prijsafzetcurve daalt. Een extra stuk brengt de nieuwe prijs op, maar de vorige stuks brengen nu ook minder op.",
    ),
    tabel(
        "Waar of niet waar over het monopolie?",
        [
            ("Bij een monopolist is de gemiddelde opbrengst gelijk aan de prijs.", J),
            ("Bij een monopolist is de marginale opbrengst gelijk aan de prijs.", F),
            ("Een monopolist maakt de meeste winst waar zijn totale opbrengst het grootst is.", F),
            ("Bij volkomen concurrentie is de marginale opbrengst gelijk aan de marktprijs.", J),
        ],
        "GO = TO / Q = P. MO ligt onder de prijs. De beste winst ligt waar MO = MK, niet waar TO maximaal is.",
    ),
    mk(
        "Een monopolist heeft berekend dat MO = MK bij Q = 50. Hoe bepaalt hij zijn prijs?",
        ["Hij leest de prijs af op de prijsafzetcurve, recht boven Q = 50",
         "Hij neemt de waarde van de marginale opbrengst bij Q = 50 als prijs",
         "Hij neemt de waarde van de marginale kosten bij Q = 50 als prijs",
         "Hij kiest de hoogste prijs waarbij er op de markt net nog iets gevraagd wordt"],
        0,
        "De prijs lees je af boven het snijpunt van MO en MK, op de prijsafzetcurve: zoveel willen de kopers voor 50 stuks betalen.",
    ),
    tabel(
        "Vergelijk het monopolie met volkomen concurrentie (zelfde vraag, zelfde kosten). Is het groter of kleiner bij het monopolie?",
        [
            ("De prijs", "Groter bij monopolie"),
            ("De verhandelde hoeveelheid", "Kleiner bij monopolie"),
            ("Het consumentensurplus", "Kleiner bij monopolie"),
            ("Het welvaartsverlies", "Groter bij monopolie"),
        ],
        "Een monopolist vraagt een hogere prijs voor een kleinere hoeveelheid. Er verdwijnt welvaart die niemand krijgt.",
        kolommen=["Groter bij monopolie", "Kleiner bij monopolie"],
    ),
    mk(
        "Een markt van volkomen concurrentie wordt overgenomen door één bedrijf, dat een monopolist wordt. Wat gebeurt er met het surplus van de kopers?",
        ["Het daalt: een deel gaat naar de monopolist en een deel verdwijnt als welvaartsverlies",
         "Het daalt, maar alles wat de consumenten verliezen gaat naar de monopolist, er gaat niets verloren",
         "Het stijgt, omdat de monopolist een deel van zijn producentensurplus aan de consumenten geeft",
         "Het blijft gelijk, omdat de vraagcurve van de consumenten niet verandert"],
        0,
        "Een deel van het consumentensurplus wordt producentensurplus, een ander deel krijgt niemand.",
    ),
    sorteer(
        "Kan dit een monopolie doen ontstaan?",
        ["Ja", "Nee"],
        [
            ["Een farmabedrijf krijgt een patent op een nieuw geneesmiddel", "Ja"],
            ["Eén bedrijf krijgt als enige de toelating om het spoornet uit te baten", "Ja"],
            ["Er zijn heel veel kleine bakkers in een stad die elk brood bakken", "Nee"],
            ["Iedereen kan zonder kosten en zonder vergunning een webwinkel starten", "Nee"],
        ],
        "Een monopolie ontstaat waar nieuwe aanbieders moeilijk kunnen toetreden.",
    ),
    koppel(
        "Koppel elke afkorting aan haar betekenis.",
        [
            ["GCK", "Gemiddelde constante kosten"],
            ["TVK", "Totale variabele kosten"],
            ["MK", "Extra kosten van één stuk meer"],
            ["GO", "Totale opbrengst gedeeld door de hoeveelheid"],
        ],
        ["Totale opbrengst min totale kosten"],
        "Totale opbrengst min totale kosten is de winst; die hoort bij geen van deze afkortingen.",
    ),
    open_(
        "Leg uit waarom economen een monopolie ongunstig vinden voor de welvaart, ook al gaat de winst van de monopolist naar iemand.",
        "De monopolist vraagt een hogere prijs voor een kleinere hoeveelheid dan bij volkomen concurrentie. Een deel van het consumentensurplus gaat naar hem, maar een ander deel verdwijnt: ruilen die voor koper en verkoper voordelig waren, gaan niet meer door. Dat welvaartsverlies krijgt niemand.",
    ),
    mk(
        "Hoe ziet de prijsafzetcurve van een monopolist eruit?",
        ["Dalend: het is de vraagcurve van de hele markt", "Horizontaal: hij kan zoveel verkopen als hij wil aan de marktprijs",
         "Stijgend: het is het stijgende deel van zijn MK-curve", "Verticaal: hij verkoopt altijd dezelfde hoeveelheid"],
        0,
        "Wil hij meer verkopen, dan moet hij de prijs verlagen. Een horizontale curve hoort bij een producent bij volkomen concurrentie.",
    ),
    inv(
        "De prijsafzetcurve van een monopolist is P = 60 − 3Q. Bij welke hoeveelheid is zijn totale opbrengst het grootst? Schrijf enkel het getal.",
        "10",
        "MO = 60 − 6Q = 0, dus Q = 10.",
    ),
    mk(
        "Een monopolist heeft prijsafzetcurve P = 80 − 2Q. Wat is zijn totale opbrengst als functie van Q?",
        ["TO = 80Q − 2Q²", "TO = 80 − 4Q", "TO = 80 − 2Q", "TO = 80Q − 4Q²"],
        0,
        "TO = P · Q = (80 − 2Q) · Q = 80Q − 2Q².",
    ),
    tabel(
        "Een bedrijf maakt meer stuks. Wat gebeurt er op korte termijn met deze kosten?",
        [
            ("TCK", "Blijft gelijk"),
            ("TVK", "Stijgt"),
            ("GCK", "Daalt"),
        ],
        "De constante kosten veranderen niet; verdeeld over meer stuks worden ze per stuk kleiner.",
        kolommen=["Stijgt", "Daalt", "Blijft gelijk"],
    ),
    keuze(
        "Een monopolist is een [[*prijszetter|prijsnemer]], een producent op een atomische markt is een [[*prijsnemer|prijszetter]].",
        "De monopolist kiest zelf de prijs; een kleine producent bij volkomen concurrentie moet de marktprijs aanvaarden.",
    ),
]
