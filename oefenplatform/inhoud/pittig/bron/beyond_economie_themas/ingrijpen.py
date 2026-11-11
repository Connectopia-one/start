"""Prijsregulering, quota, belastingen en subsidies — pittig (🌍 Beyond, economie).

Vaste markt in dit hoofdstuk: Qv = 90 − P en Qa = 2P − 30, evenwicht P = 40 en Q = 50.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

GM = venster("ingrijpen-maximumprijs", 0, 90, 0, 100, 10, 10)
GB = venster("ingrijpen-belasting", 0, 90, 0, 100, 10, 10)
MAX = {"E": (50, 40), "K": (30, 30), "L": (60, 30)}
BEL = {"E": (50, 40), "R": (40, 50), "S": (40, 35)}

V = lambda q: 90 - q          # noqa: E731  vraag: P = 90 − Q
A = lambda q: 15 + q / 2      # noqa: E731  aanbod: P = 15 + Q/2
AT = lambda q: 30 + q / 2     # noqa: E731  aanbod met belasting 15

GRAFIEKEN = [
    dict(naam=GM, titel="Markt van huurwoningen: maximumprijs van 30",
         krommen=[(V, "groen", "V", (0, 82)), (A, "blauw", "A", (0, 90))],
         stippel=[("h", 30)],
         labelplek={"V": (80, 10), "A": (86, 58)},
         punten=[(x, y, k) for k, (x, y) in MAX.items()],
         xlabel="hoeveelheid", ylabel="prijs", ijk_x=10, ijk_y=10),
    dict(naam=GB, titel="Belasting van 15 euro per stuk bij de producent",
         krommen=[(V, "groen", "V", (0, 82)), (A, "blauw", "A", (0, 90)), (AT, "oranje", "A+t", (0, 90))],
         labelplek={"V": (80, 10), "A": (86, 58), "A+t": (78, 69)},
         punten=[(x, y, k) for k, (x, y) in BEL.items()],
         xlabel="hoeveelheid", ylabel="prijs", ijk_x=10, ijk_y=10),
]

PRENTEN = [
    dict(bestand=f"{GM}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over tekort en welvaartsverlies"),
    dict(bestand=f"{GB}.svg", zelf=True, wat=GRAFIEKEN[1]["titel"], vragen="klikvragen over wie de belasting draagt"),
]
PM, PB = f"{GM}.svg", f"{GB}.svg"

VRAGEN = [
    klik(
        "Bij de maximumprijs van 30: klik op het punt dat toont hoeveel er werkelijk verhandeld wordt.",
        PM, [punt_zone(GM, *MAX["K"])],
        "Bij 30 bieden de verhuurders maar 30 woningen aan. Meer kan er niet verhandeld worden: punt K.",
    ),
    klik(
        "Klik in het gebied dat het welvaartsverlies door de maximumprijs voorstelt.",
        PM, [vak_zone(GM, 32, 42, 38, 46)],
        "Het welvaartsverlies is de driehoek tussen vraag en aanbod, van Q = 30 tot Q = 50: de ruilen die niet meer doorgaan.",
    ),
    met_prent(PM, inv(
        "Hoe groot is het tekort bij de maximumprijs van 30? Schrijf enkel het getal.",
        "30",
        "Qv = 90 − 30 = 60 en Qa = 2 · 30 − 30 = 30. Tekort = 60 − 30 = 30.",
    )),
    met_prent(PM, inv(
        "Bereken het welvaartsverlies door de maximumprijs van 30. Bij Q = 30 willen kopers 60 betalen. Schrijf enkel het getal.",
        "300",
        "½ · (50 − 30) · (60 − 30) = 300.",
    )),
    met_prent(PM, mk(
        "De overheid verandert de maximumprijs in 45. Wat gebeurt er?",
        ["Niets: een maximumprijs boven de evenwichtsprijs van 40 heeft geen effect",
         "Het tekort wordt groter, want de maximumprijs ligt nu hoger dan voorheen",
         "Er ontstaat een overschot van 15, want de prijs ligt boven het evenwicht",
         "De prijs wordt 45, want verhuurders vragen altijd de hoogst toegelaten prijs"],
        0,
        "Een maximumprijs werkt enkel als ze onder de evenwichtsprijs ligt. De markt blijft bij 40 en 50.",
    )),
    klik(
        "Klik op het punt met de prijs die de kopers betalen na de belasting.",
        PB, [punt_zone(GB, *BEL["R"])],
        "Het nieuwe evenwicht ligt waar de vraag de verschoven aanbodcurve A+t snijdt: Q = 40 en P = 50.",
    ),
    klik(
        "Klik in het gebied dat het welvaartsverlies door de belasting voorstelt.",
        PB, [vak_zone(GB, 41, 46, 39, 44)],
        "Het welvaartsverlies is de driehoek tussen vraag en oorspronkelijk aanbod, van Q = 40 tot Q = 50.",
    ),
    casus(
        "Vraag Qv = 90 − P, aanbod zonder belasting Qa = 2P − 30. De overheid heft 15 euro per stuk bij de producent.",
        [
            inv("Hoeveel houdt de producent per stuk over na de belasting? Schrijf enkel het getal.", "35",
                "De koper betaalt 50, de producent houdt 50 − 15 = 35 over."),
            inv("Hoeveel ontvangt de overheid? Schrijf enkel het getal.", "600",
                "15 · 40 = 600."),
            inv("Hoe groot is het welvaartsverlies? Schrijf enkel het getal.", "75",
                "½ · (50 − 40) · 15 = 75."),
            mk("Wie draagt het grootste deel van de belasting?",
               ["De kopers: zij betalen 10 meer, de producent ontvangt 5 minder",
                "De producenten: zij ontvangen 10 minder, de kopers betalen 5 meer",
                "De overheid: zij draagt alles",
                "Kopers en producenten elk de helft"], 0,
               "Van 40 naar 50 voor de koper (+10), van 40 naar 35 voor de producent (−5)."),
        ],
    ),
    mk(
        "Waarom zijn de belastingontvangsten van de overheid geen welvaartsverlies?",
        ["Ze gaan niet verloren, ze gaan naar de overheid", "Ze worden altijd volledig terugbetaald aan de producenten",
         "Ze zijn kleiner dan het consumentensurplus", "Ze worden enkel door de kopers betaald"],
        0,
        "Wat de kopers en verkopers aan belasting verliezen, krijgt de overheid. Enkel de driehoek krijgt niemand.",
    ),
    tabel(
        "Een minimumprijs van 50 op deze markt (Qv = 90 − P, Qa = 2P − 30). Bereken.",
        [
            ("Gevraagde hoeveelheid", "40"),
            ("Aangeboden hoeveelheid", "70"),
            ("Overschot", "30"),
        ],
        "Qv = 90 − 50 = 40. Qa = 100 − 30 = 70. Overschot = 70 − 40 = 30.",
        kolommen=["30", "40", "70"],
    ),
    mk(
        "Een minimumprijs boven de evenwichtsprijs geeft een overschot. Wat doet de overheid daar vaak mee?",
        ["Ze koopt het overschot op en slaat het op of verwerkt het",
         "Ze verplicht de consumenten om het overschot te kopen",
         "Ze verlaagt de minimumprijs elke week tot het overschot weg is",
         "Ze laat de producenten het overschot gratis weggeven"],
        0,
        "Het overschot wordt vaak door de overheid opgekocht.",
    ),
    mk(
        "Een minimumprijs voor melk ligt boven de evenwichtsprijs. Wat gebeurt er met de totale welvaart?",
        ["Ze stijgt niet: er wordt minder verhandeld dan in het evenwicht",
         "Ze stijgt, want de melkboeren verdienen meer per liter",
         "Ze blijft gelijk, want wat de kopers verliezen, winnen de boeren",
         "Ze stijgt, want er wordt meer melk geproduceerd"],
        0,
        "Er wordt minder verhandeld, dus er gaan voordelige ruilen verloren.",
    ),
    tabel(
        "Wat is het gevolg van deze maatregel (elk apart, ten opzichte van het evenwicht)?",
        [
            ("Maximumprijs onder de evenwichtsprijs", "Tekort"),
            ("Minimumprijs boven de evenwichtsprijs", "Overschot"),
            ("Maximumprijs boven de evenwichtsprijs", "Geen effect"),
            ("Minimumprijs onder de evenwichtsprijs", "Geen effect"),
        ],
        "Een maximumprijs werkt enkel onder, een minimumprijs enkel boven de evenwichtsprijs.",
        kolommen=["Tekort", "Overschot", "Geen effect"],
    ),
    sorteer(
        "Is dit een gevolg van een maximumprijs (onder het evenwicht) of van een minimumprijs (boven het evenwicht)?",
        ["Maximumprijs", "Minimumprijs"],
        [
            ["Wachtrijen", "Maximumprijs"],
            ["Een zwarte markt", "Maximumprijs"],
            ["De overheid koopt producten op", "Minimumprijs"],
            ["Lange wachtlijsten voor huurwoningen", "Maximumprijs"],
            ["Landbouwers worden beschermd", "Minimumprijs"],
        ],
        "Een maximumprijs geeft een tekort, een minimumprijs een overschot.",
    ),
    casus(
        "Op dezelfde markt (Qv = 90 − P, Qa = 2P − 30) legt de overheid een productiequotum van 30 op.",
        [
            inv("Welke prijs willen de kopers betalen voor 30 stuks? Schrijf enkel het getal.", "60",
                "Qv = 30 als P = 90 − 30 = 60."),
            inv("Welke prijs zouden de producenten volgens hun aanbodcurve vragen voor 30 stuks? Schrijf enkel het getal.", "30",
                "Qa = 30 als 2P − 30 = 30, dus P = 30."),
            mk("Wie wint er bij dit quotum?",
               ["De producenten met een quotum: ze krijgen een hogere prijs", "De kopers: ze betalen minder, want er wordt minder geproduceerd",
                "Niemand: de prijs blijft gewoon 40 euro", "De overheid: ze int een belasting op elk verkocht stuk"], 0,
               "De prijs stijgt van 40 naar 60. De producenten met een quotum winnen."),
        ],
    ),
    tabel(
        "Een subsidie van 15 euro per stuk aan de producent op deze markt. Bereken.",
        [
            ("Nieuwe prijs voor de koper", "30"),
            ("Nieuwe hoeveelheid", "60"),
            ("Kost voor de overheid", "900"),
        ],
        "Nieuw aanbod Qa = 2(P + 15) − 30 = 2P. 90 − P = 2P geeft P = 30 en Q = 60. Kost: 15 · 60 = 900.",
        kolommen=["30", "60", "900"],
    ),
    tabel(
        "Waar of niet waar over belastingen en subsidies?",
        [
            ("Een belasting per stuk bij de producent verschuift de aanbodcurve naar rechts.", F),
            ("Is de vraag heel inelastisch, dan dragen de consumenten het grootste deel van de belasting.", J),
            ("Een subsidie geeft op een competitieve markt zonder externe effecten geen welvaartsverlies.", F),
            ("Hoe elastischer vraag en aanbod, hoe groter het welvaartsverlies van een belasting.", J),
        ],
        "Een belasting verschuift het aanbod naar boven (links). Ook een subsidie geeft een welvaartsverlies: er wordt meer gemaakt dan wat kopers waard vinden.",
    ),
    koppel(
        "Koppel elke maatregel aan wat hij doet.",
        [
            ["Productiequotum", "Een maximale hoeveelheid die mag worden geproduceerd"],
            ["Accijns op tabak", "Een indirecte belasting op een goed"],
            ["Subsidie per stuk", "Aanbodcurve naar rechts, lagere prijs"],
            ["Maximumhuurprijs", "Een prijs die niet overschreden mag worden"],
        ],
        ["Een belasting op het inkomen van de verhuurders"],
        "Accijnzen en btw zijn indirecte belastingen: ze liggen op goederen.",
    ),
    keuze(
        "Is de vraag heel [[*elastisch|inelastisch]], dan draagt vooral de producent een belasting per stuk. Een maximumhuurprijs ver onder de marktprijs geeft op lange termijn [[*minder|meer]] huurwoningen.",
        "Kopers die gemakkelijk afhaken, laten de producent de belasting dragen.",
    ),
    mk(
        "Waarom geeft een maximumhuurprijs ver onder de marktprijs op lange termijn lange wachtlijsten?",
        ["Verhuurders bieden minder woningen aan, terwijl meer mensen willen huren",
         "Huurders willen minder huren omdat de woningen goedkoper worden en ze liever kopen",
         "De overheid koopt alle woningen op die door de lage prijs niet verhuurd raken",
         "Er ontstaat een groot overschot aan huurwoningen dat niemand wil huren"],
        0,
        "Aan een te lage prijs is het aanbod klein en de vraag groot: een tekort.",
    ),
    open_(
        "Een gemeente overweegt een maximumprijs voor broden, ver onder de evenwichtsprijs, zodat iedereen goedkoop brood kan kopen. Leg uit waarom dat minder goed uitpakt dan het lijkt.",
        "Aan die lage prijs bieden bakkers minder brood aan, terwijl kopers er meer willen. Er ontstaat een tekort, met wachtrijen en misschien een zwarte markt. Er wordt minder verhandeld dan in het evenwicht, dus er is een welvaartsverlies. Wie geen brood vindt, heeft niets aan de lage prijs.",
    ),
    mk(
        "Welke belasting is een indirecte belasting?",
        ["De btw op een nieuwe fiets", "De personenbelasting op je loon", "De vennootschapsbelasting op de winst van een bedrijf", "De onroerende voorheffing op je huis"],
        0,
        "Indirecte belastingen liggen op goederen, zoals de btw en accijnzen.",
    ),
    inv(
        "Een belasting van 15 per stuk verlaagt de verhandelde hoeveelheid van 50 naar 40. Hoeveel procent minder wordt er verhandeld? Schrijf enkel het getal.",
        "20",
        "−10 / 50 = −20 %.",
    ),
    keuze(
        "Een productiequotum onder de evenwichtshoeveelheid doet de prijs [[*stijgen|dalen]], er wordt [[*minder|meer]] verhandeld en er is [[*wel|geen]] welvaartsverlies.",
        "Minder aanbod aan een hogere prijs: voordelige ruilen gaan verloren.",
    ),
    volgorde(
        "Een maximumprijs onder de evenwichtsprijs: zet de gevolgen in de juiste volgorde.",
        ["De prijs mag niet hoger dan het maximum", "Producenten bieden minder aan, kopers vragen meer",
         "Er ontstaat een tekort", "Er komen wachtrijen en een zwarte markt"],
        "Lagere prijs, minder aanbod en meer vraag, dus een tekort, met wachtrijen en zwarte handel als gevolg.",
    ),
]
