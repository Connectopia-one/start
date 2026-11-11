"""Het inkomensevenwicht, de multiplicator en het AV-AA-schema — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G1 = venster("evenwicht-45-graden", 0, 400, 0, 400, 50, 50)
G2 = venster("evenwicht-av-aa", 0, 16, 0, 12, 2, 2)
P1 = {"E": (200, 200), "F": (300, 300)}
P2 = {"E": (8, 6), "F": (10, 7), "G": (6, 7)}

GRAFIEKEN = [
    dict(naam=G1, titel="Inkomensevenwicht: C = 40 + 0,5Y, I stijgt van 60 naar 110",
         krommen=[(lambda y: y, "oranje", "45°", (0, 400)), (lambda y: 100 + 0.5 * y, "groen", "C + I", (0, 400)),
                  (lambda y: 150 + 0.5 * y, "blauw", "C + I′", (0, 400))],
         labelplek={"45°": (100, 100), "C + I": (40, 120), "C + I′": (40, 170)},
         punten=[(x, y, k) for k, (x, y) in P1.items()],
         xlabel="inkomen Y", ylabel="bestedingen", ijk_x=50, ijk_y=50),
    dict(naam=G2, titel="AV-AA-schema (korte termijn)",
         krommen=[(lambda y: 10 - 0.5 * y, "groen", "AV", (0, 16)), (lambda y: 12 - 0.5 * y, "paars", "AV′", (0, 16)),
                  (lambda y: 2 + 0.5 * y, "blauw", "AA", (0, 16)), (lambda y: 4 + 0.5 * y, "oranje", "AA′", (0, 15))],
         labelplek={"AV": (15, 2.5), "AV′": (15.5, 4.25), "AA": (15, 9.5), "AA′": (13, 10.5)},
         punten=[(x, y, k) for k, (x, y) in P2.items()],
         xlabel="reëel bbp", ylabel="prijspeil", ijk_x=2, ijk_y=2),
]

PRENTEN = [
    dict(bestand=f"{G1}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen en rekenvragen over het inkomensevenwicht en de multiplicator"),
    dict(bestand=f"{G2}.svg", zelf=True, wat="AV-AA-schema met AV, AV′, AA en AA′", vragen="klikvragen over vraag- en aanbodschokken"),
]
PA, PB = f"{G1}.svg", f"{G2}.svg"

VRAGEN = [
    klik(
        "Klik op het inkomensevenwicht nadat de investeringen gestegen zijn naar 110.",
        PA, [punt_zone(G1, *P1["F"])],
        "Het evenwicht ligt waar de nieuwe bestedingslijn C + I′ de 45°-lijn snijdt: Y = 300.",
    ),
    met_prent(PA, inv(
        "Bereken het evenwichtsinkomen bij I = 60. Schrijf enkel het getal.",
        "200",
        "Y = 40 + 0,5Y + 60, dus 0,5Y = 100 en Y = 200.",
    )),
    met_prent(PA, inv(
        "Hoe groot is de multiplicator in dit model? Schrijf enkel het getal.",
        "2",
        "1 / (1 − 0,5) = 1 / 0,5 = 2.",
    )),
    met_prent(PA, mk(
        "De investeringen stijgen met 50. Met hoeveel stijgt het evenwichtsinkomen?",
        ["Met 100", "Met 50", "Met 25", "Met 200"],
        0,
        "Multiplicator 2 · 50 = 100: van 200 naar 300.",
    )),
    met_prent(PA, mk(
        "Wat toont de 45°-lijn?",
        ["De punten waar de bestedingen gelijk zijn aan het inkomen Y", "De consumptie van de gezinnen bij elk mogelijk inkomen",
         "De investeringen van de bedrijven, die altijd even groot blijven", "Het potentieel bbp dat de economie normaal kan produceren"],
        0,
        "Het evenwicht ligt waar de bestedingslijn de 45°-lijn snijdt.",
    )),
    klik(
        "De markt staat in E. De gezinnen en bedrijven gaan veel meer besteden. Klik op het nieuwe evenwicht op korte termijn.",
        PB, [punt_zone(G2, *P2["F"])],
        "Een positieve vraagschok: AV schuift naar rechts (AV′). Prijspeil en reëel bbp stijgen: punt F.",
    ),
    klik(
        "De markt staat in E. De olieprijs stijgt fors. Klik op het nieuwe evenwicht op korte termijn.",
        PB, [punt_zone(G2, *P2["G"])],
        "Een negatieve aanbodschok: AA schuift naar links (AA′). Hogere prijzen en minder productie: punt G.",
    ),
    met_prent(PB, mk(
        "Van E naar G: hoe noem je die combinatie van gevolgen?",
        ["Stagflatie: hogere prijzen en minder productie", "Deflatie: dalende prijzen en tegelijk meer productie",
         "Een positieve vraagschok", "Een bestedingsevenwicht"],
        0,
        "Het prijspeil stijgt van 6 naar 7 en het reëel bbp daalt van 8 naar 6.",
    )),
    met_prent(PB, mk(
        "Het potentieel bbp is 8. Op lange termijn is de AA-curve verticaal bij 8. Wat gebeurt er op lange termijn na de vraagschok van E naar F?",
        ["Het bbp keert terug naar 8 en het prijspeil blijft hoger", "Het bbp blijft 10 en het prijspeil daalt weer naar 6",
         "Het bbp en het prijspeil keren allebei terug naar E", "Het bbp stijgt verder en het prijspeil daalt"],
        0,
        "Met een verticale AA op lange termijn keert het bbp terug naar het potentieel; het prijspeil blijft hoger.",
    )),
    tabel(
        "Welke curve verschuift, en in welke richting?",
        [
            ("Het consumentenvertrouwen stort in", "AV naar links"),
            ("Een technologische doorbraak", "AA naar rechts"),
            ("De overheid investeert veel meer in wegen en scholen", "AV naar rechts"),
            ("De olieprijs stijgt fors", "AA naar links"),
        ],
        "Bestedingen verschuiven AV, productiekosten en techniek verschuiven AA.",
        kolommen=["AV naar rechts", "AV naar links", "AA naar rechts", "AA naar links"],
    ),
    tabel(
        "Bereken de multiplicator bij deze marginale consumptiequote.",
        [
            ("0,6", "2,5"),
            ("0,8", "5"),
            ("0,9", "10"),
        ],
        "Multiplicator = 1 / (1 − marginale consumptiequote).",
        kolommen=["2,5", "5", "10"],
    ),
    casus(
        "In een gesloten economie zonder overheid geldt C = 30 + 0,6Y en I = 50.",
        [
            inv("Bereken het evenwichtsinkomen. Schrijf enkel het getal.", "200",
                "Y = 30 + 0,6Y + 50, dus 0,4Y = 80 en Y = 200."),
            mk("Hoe groot is de marginale spaarquote?", ["0,4", "0,6", "30", "2,5"], 0,
               "1 − 0,6 = 0,4: van elke extra euro wordt 40 cent gespaard."),
            inv("De investeringen dalen met 10. Met hoeveel daalt het evenwichtsinkomen? Schrijf enkel het getal.", "25",
                "Multiplicator 1 / 0,4 = 2,5. 2,5 · 10 = 25."),
        ],
    ),
    mk(
        "Waarom levert een extra uitgave meer inkomen op dan de uitgave zelf?",
        ["De uitgave wordt inkomen voor anderen, die verder besteden", "De overheid verdubbelt elke extra uitgave",
         "De prijzen stijgen, waardoor het inkomen groter lijkt", "Banken scheppen bij elke uitgave nieuw geld voor de klanten"],
        0,
        "Bij elke ronde wordt een deel opnieuw besteed: het multiplicatoreffect.",
    ),
    tabel(
        "Wordt de multiplicator groter of kleiner?",
        [
            ("De marginale spaarquote stijgt", "Kleiner"),
            ("Er komen belastingen bij", "Kleiner"),
            ("De marginale consumptiequote stijgt", "Groter"),
        ],
        "Spaarlek en belastinglek maken de multiplicator kleiner.",
        kolommen=["Groter", "Kleiner"],
    ),
    mk(
        "Wat blijft er constant in het vereenvoudigd model van het inkomensevenwicht?",
        ["De prijzen, de geldhoeveelheid en de rente", "Het inkomen, de consumptie en de investeringen",
         "De werkloosheid en de export", "Het bbp en de bevolking"],
        0,
        "Daarom wordt het evenwichtsinkomen enkel door de effectieve vraag bepaald.",
    ),
    mk(
        "Een gezin zou graag een nieuwe keuken kopen, maar heeft er het geld niet voor. Telt die wens mee in de effectieve vraag?",
        ["Nee: enkel bestedingen waarvoor ook koopkracht is, tellen mee", "Ja: elke wens om iets te kopen, ook zonder geld, is effectieve vraag",
         "Ja, maar enkel als het gezin later toch nog een lening krijgt bij de bank", "Nee, want een keuken is altijd een investering van een bedrijf, geen consumptie"],
        0,
        "Effectieve vraag zijn de bestedingen waarvoor ook koopkracht is.",
    ),
    tabel(
        "Budgettair of monetair beleid?",
        [
            ("De belastingen verlagen", "Budgettair"),
            ("De rente verlagen", "Monetair"),
            ("Meer investeren in scholen", "Budgettair"),
            ("De rente verhogen", "Monetair"),
        ],
        "Budgettair: uitgaven en belastingen van de overheden. Monetair: de rente, voor België door de ECB.",
        kolommen=["Budgettair", "Monetair"],
    ),
    mk(
        "De Vlaamse regering wil de rente in de eurozone verlagen om de economie te steunen. Kan dat?",
        ["Nee, dat kan enkel de Europese Centrale Bank", "Ja, elke regering bepaalt haar eigen rente",
         "Ja, als de federale regering ermee akkoord gaat", "Nee, de rente wordt bepaald door het IMF"],
        0,
        "Monetair beleid is voor de eurozone in handen van de ECB.",
    ),
    keuze(
        "Een renteverhoging is een [[*restrictief|expansief]] monetair beleid en doet de AV-curve naar [[*links|rechts]] schuiven.",
        "Een hogere rente remt de bestedingen af.",
    ),
    koppel(
        "Koppel elke curve aan haar verloop.",
        [
            ["AV", "Dalend"],
            ["AA op korte termijn", "Stijgend"],
            ["AA op lange termijn", "Verticaal bij het potentieel bbp"],
        ],
        ["Horizontaal bij de evenwichtsprijs"],
        "Op lange termijn is de productie niet hoger dan het potentieel bbp, wat het prijspeil ook is.",
    ),
    open_(
        "De overheid verhoogt haar uitgaven met 10 miljard. Leg uit waarom het inkomen met meer dan 10 miljard stijgt, en waarom het effect kleiner is als mensen veel sparen.",
        "De 10 miljard wordt inkomen voor bedrijven en werknemers, die een deel ervan opnieuw besteden. Dat wordt weer inkomen voor anderen, enzovoort: het multiplicatoreffect. Bij elke ronde lekt er een deel weg naar sparen (en belastingen). Hoe meer mensen sparen, hoe kleiner de multiplicator.",
    ),
    inv(
        "De marginale consumptiequote is 0,75 en de overheid verhoogt haar uitgaven met 12 miljard. Met hoeveel miljard stijgt het inkomen in het eenvoudige model? Schrijf enkel het getal.",
        "48",
        "Multiplicator 1 / 0,25 = 4. 4 · 12 = 48 miljard.",
    ),
    mk(
        "Hoe heet de multiplicator als het gaat om extra investeringen?",
        ["De investeringsmultiplicator", "De marginale spaarquote", "De positieve outputkloof", "Het belastinglek van de overheid"],
        0,
        "Het verschijnsel zelf heet het multiplicatoreffect.",
    ),
    sorteer(
        "Is dit een lek in het multiplicatorproces?",
        ["Wel een lek", "Geen lek"],
        [
            ["Het deel van het extra inkomen dat gespaard wordt", "Wel een lek"],
            ["Het deel van het extra inkomen voor belastingen", "Wel een lek"],
            ["Het deel van het extra inkomen dat opnieuw besteed wordt", "Geen lek"],
        ],
        "Wat opnieuw besteed wordt, houdt het proces net gaande.",
    ),
    mk(
        "Je tekent een AV-AA-schema. Wat zet je op de assen?",
        ["Het algemeen prijspeil en het reëel bbp", "De rente en de hoeveelheid krediet in de economie",
         "Het inkomen Y en de bestedingen", "De koers en de hoeveelheid euro"],
        0,
        "In tegenstelling tot het vereenvoudigd model mogen de prijzen hier wel veranderen.",
    ),
    keuze(
        "Het macro-economisch evenwicht op korte termijn ligt op het snijpunt van [[*AV|de 45°-lijn]] en [[*AA op korte termijn|AA op lange termijn]].",
        "Op korte termijn is AA stijgend.",
    ),
    volgorde(
        "De overheid verlaagt de belastingen. Zet de gevolgen in de juiste volgorde.",
        ["Gezinnen houden meer over", "Gezinnen besteden meer", "De AV-curve schuift naar rechts", "Prijspeil en reëel bbp stijgen op korte termijn"],
        "Een expansief budgettair beleid verschuift AV naar rechts.",
    ),
    tabel(
        "Waar of niet waar over het inkomensevenwicht?",
        [
            ("Stijgen de autonome investeringen, dan schuift de bestedingslijn omhoog.", J),
            ("Met belastingen erbij is de multiplicator groter dan zonder.", F),
            ("Een daling van de investeringen doet het inkomen met meer dan die daling dalen.", J),
            ("Bij een marginale consumptiequote van 0,9 is de multiplicator 0,9.", F),
        ],
        "Belastingen zijn een lek: de multiplicator wordt kleiner. Bij 0,9 is de multiplicator 1 / 0,1 = 10.",
    ),
]
