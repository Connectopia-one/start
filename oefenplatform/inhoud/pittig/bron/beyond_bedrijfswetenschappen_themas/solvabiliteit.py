"""Kerncijfers: solvabiliteit en rendabiliteit — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone, balans_zone

HEFBOOM_KOPPEN = ["A", "B", "C"]
HEFBOOM_RIJEN = ["Eigen vermogen", "Vreemd vermogen aan 5\u00a0%", "Resultaat vóór interest", "Interest", "Winst", "Rendabiliteit eigen vermogen"]
HEFBOOM = [
    ["1 000 000", "500 000", "200 000"],
    ["0", "500 000", "800 000"],
    ["100 000", "100 000", "100 000"],
    ["0", "25 000", "40 000"],
    ["100 000", "75 000", "60 000"],
    ["10 %", "15 %", "30 %"],
]

PRENTEN = [
    dict(bestand="hefboom.svg", zelf=True,
         wat="Tabel met drie financieringen (A, B, C) van 1 000 000 euro en het rendement voor de eigenaars.",
         vragen="klikvraag en vragen over de financiële hefboom"),
    dict(bestand="balans-velo.svg", zelf=True,
         wat="Dezelfde balans van Velo nv als bij het hoofdstuk over de balans.",
         vragen="solvabiliteit en schuldgraad"),
]

VRAGEN = [
    klik(
        "Klik in de tabel op het vak waar de financiële hefboom de eigenaars het meest oplevert.",
        "hefboom.svg",
        [raster_zone(5, 2, 6, 3)],
        "Bij C is de rendabiliteit van het eigen vermogen 30 %. Het geleende geld brengt 10 % op en kost maar 5 %.",
    ),
    met_prent("hefboom.svg", tabel(
        "Welke uitspraken over de drie financieringen kloppen?",
        [
            ("De rendabiliteit van het totaal vermogen is bij A, B en C 10 %.", J),
            ("De hefboom is positief, omdat het vermogen meer opbrengt dan de interest.", J),
            ("Bij C is de solvabiliteit het hoogst.", F),
            ("Hoe meer er geleend wordt, hoe kleiner de winst in euro.", J),
        ],
        "Het resultaat vóór interest is telkens 100 000 euro op 1 000 000 euro. Bij C is de solvabiliteit maar 20 %. De winst in euro daalt, maar het rendement per euro eigen vermogen stijgt.",
    )),
    met_prent("hefboom.svg", mk(
        "Stel dat het resultaat vóór interest daalt naar 30 000 euro. Hoeveel is de rendabiliteit van het eigen vermogen bij C dan?",
        ["− 5 %", "3 %", "15 %", "− 10 %"],
        0,
        "Winst: 30 000 − 40 000 = − 10 000 euro. − 10 000 / 200 000 · 100 = − 5 %. Het vermogen brengt maar 3 % op en kost 5 %: de hefboom werkt nu tegen.",
    )),
    met_prent("hefboom.svg", mk(
        "Bij welk resultaat vóór interest is de rendabiliteit van het eigen vermogen bij A, B en C precies gelijk?",
        ["50 000 euro", "100 000 euro", "25 000 euro", "0 euro"],
        0,
        "Bij 50 000 euro is de rendabiliteit van het totaal vermogen 5 %, gelijk aan de interestvoet: de hefboom is neutraal en overal is het rendement 5 %.",
    )),
    met_prent("balans-velo.svg", tabel(
        "Bereken de solvabiliteit en de schuldgraad van Velo nv.",
        [
            ("Solvabiliteit", "45 %"),
            ("Schuldgraad", "55 %"),
            ("Aandeel vreemd vermogen op korte termijn in het totaal", "30 %"),
        ],
        "Eigen vermogen 450 000 / 1 000 000 = 45 %. Vreemd vermogen 550 000 / 1 000 000 = 55 %. Korte termijn 300 000 / 1 000 000 = 30 %.",
        kolommen=["30 %", "45 %", "55 %", "70 %"],
    )),
    klik(
        "Klik op de balans van Velo nv op de post die je in de teller zet bij de solvabiliteit.",
        "balans-velo.svg",
        [balans_zone("ev")],
        "Solvabiliteit = eigen vermogen / totaal vermogen.",
    ),
    mk(
        "Winst na belasting 54 000 euro, interestkosten 18 000 euro, eigen vermogen 360 000 euro, totaal vermogen 900 000 euro. Wat zijn de rendabiliteit van het eigen en van het totaal vermogen?",
        [
            "Eigen 15 %, totaal 8 %",
            "Eigen 8 %, totaal 15 %",
            "Eigen 20 %, totaal 6 %",
            "Eigen 15 %, totaal 6 %",
        ],
        0,
        "54 000 / 360 000 = 15 %. (54 000 + 18 000) / 900 000 = 8 %.",
    ),
    mk(
        "Rendabiliteit van het eigen vermogen 12 %, eigen vermogen 250 000 euro. Hoeveel winst na belasting maakte de onderneming?",
        ["30 000 euro", "20 833 euro", "3 000 euro", "120 000 euro"],
        0,
        "250 000 · 0,12 = 30 000 euro.",
    ),
    mk(
        "Een onderneming heeft een solvabiliteit van 35 % en een totaal vermogen van 2 000 000 euro. Hoeveel vreemd vermogen heeft ze?",
        ["1 300 000 euro", "700 000 euro", "350 000 euro", "1 650 000 euro"],
        0,
        "Eigen vermogen 2 000 000 · 0,35 = 700 000 euro. Vreemd vermogen 2 000 000 − 700 000 = 1 300 000 euro.",
    ),
    tabel(
        "Wat gebeurt er met de solvabiliteit bij elke verrichting?",
        [
            ("Een kapitaalverhoging met inbreng van geld", "Stijgt"),
            ("Een nieuwe banklening voor een machine", "Daalt"),
            ("Winst die in de reserves blijft", "Stijgt"),
            ("Een uitbetaling van dividend", "Daalt"),
        ],
        "Meer eigen vermogen doet de solvabiliteit stijgen. Meer schulden of minder eigen vermogen doen haar dalen.",
        kolommen=["Stijgt", "Daalt", "Blijft gelijk"],
    ),
    mk(
        "Rendabiliteit van het totaal vermogen 7 %, interestvoet 4 %. De onderneming leent extra. Wat gebeurt er met de rendabiliteit van het eigen vermogen en met de solvabiliteit?",
        [
            "Het rendement stijgt, de solvabiliteit daalt",
            "Het rendement daalt, de solvabiliteit stijgt",
            "Allebei stijgen",
            "Allebei dalen",
        ],
        0,
        "Positieve hefboom: meer lenen verhoogt het rendement voor de eigenaars, maar het risico stijgt omdat het eigen vermogen een kleiner deel wordt.",
    ),
    keuze(
        "De financiële hefboom is [[*positief|negatief|neutraal]] als de rendabiliteit van het totaal vermogen hoger is dan de [[*interestvoet|solvabiliteit|current ratio]].",
        "Dan brengt elke geleende euro meer op dan hij kost.",
    ),
    sorteer(
        "Is het een kerncijfer over solvabiliteit of over rendabiliteit?",
        ["Solvabiliteit", "Rendabiliteit"],
        [
            ["Eigen vermogen / totaal vermogen", "Solvabiliteit"],
            ["Vreemd vermogen / totaal vermogen", "Solvabiliteit"],
            ["Winst na belasting / eigen vermogen", "Rendabiliteit"],
            ["(Winst na belasting + interest) / totaal vermogen", "Rendabiliteit"],
        ],
        "Solvabiliteit gaat over hoe het vermogen is samengesteld, rendabiliteit over wat het opbrengt.",
    ),
    inv(
        "Vreemd vermogen 640 000 euro, totaal vermogen 800 000 euro. Hoeveel procent is de solvabiliteit? Schrijf enkel het getal.",
        "20",
        "Eigen vermogen 800 000 − 640 000 = 160 000 euro. 160 000 / 800 000 · 100 = 20 %.",
    ),
    mk(
        "Een bank geeft enkel een lening als de solvabiliteit na de lening minstens 30 % is. Eigen vermogen 300 000 euro, totaal vermogen 800 000 euro. Hoeveel kan de onderneming maximaal lenen?",
        ["200 000 euro", "500 000 euro", "240 000 euro", "100 000 euro"],
        0,
        "300 000 euro moet minstens 30 % van het nieuwe totaal zijn: het totaal mag hoogstens 1 000 000 euro worden. 1 000 000 − 800 000 = 200 000 euro.",
    ),
    sleep(
        "De [[solvabiliteit]] meet of een onderneming op lange termijn al haar schulden kan betalen. De [[schuldgraad]] is daar het spiegelbeeld van. Samen zijn ze [[100 %]].",
        ["liquiditeit", "50 %"],
        "Eigen vermogen en vreemd vermogen vormen samen het totaal vermogen.",
    ),
    tabel(
        "Waar of niet waar over solvabiliteit, rendabiliteit en hefboom?",
        [
            ("Een onderneming met een hoge rendabiliteit kan toch een lage solvabiliteit hebben.", J),
            ("Een negatieve hefboom betekent dat lenen het rendement voor de eigenaars verlaagt.", J),
            ("De rendabiliteit van het eigen vermogen gebruikt de winst vóór interest.", F),
            ("Een hoge schuldgraad maakt een onderneming kwetsbaarder als de winst daalt.", J),
        ],
        "Kerncijfers meten verschillende dingen. De rendabiliteit van het eigen vermogen gebruikt de winst na interest en belasting.",
    ),
    koppel(
        "Wie heeft vooral belangstelling voor welk kerncijfer?",
        [
            ["Een aandeelhouder die wil weten wat zijn inbreng opbrengt", "Rendabiliteit eigen vermogen"],
            ["Een bank die een lening op tien jaar overweegt", "Solvabiliteit"],
            ["Een leverancier die wil weten of hij volgende maand betaald wordt", "Current ratio"],
        ],
        ["Omlooptijd voorraad"],
        "Elke stakeholder kijkt naar het cijfer dat bij zijn risico of belang past.",
    ),
    mk(
        "Onderneming X heeft een solvabiliteit van 60 %, onderneming Y van 15 %. Beide hebben een rendabiliteit van het totaal vermogen van 9 % en lenen aan 4 %. Welke heeft de hoogste rendabiliteit van het eigen vermogen?",
        [
            "Y, omdat ze meer leent bij een positieve hefboom",
            "X, omdat ze meer eigen vermogen heeft",
            "Ze zijn gelijk, omdat de rendabiliteit van het totaal vermogen gelijk is",
            "X, omdat ze minder interest betaalt",
        ],
        0,
        "Met een positieve hefboom levert elke geleende euro de eigenaars extra op. Y leent het meest.",
    ),
    mk(
        "Totaal vermogen 500 000 euro, waarvan 200 000 euro eigen vermogen. Resultaat vóór interest 40 000 euro, interestvoet 6 %, belasting buiten beschouwing. Hoeveel is de rendabiliteit van het eigen vermogen?",
        ["11 %", "8 %", "20 %", "14 %"],
        0,
        "Interest 300 000 · 0,06 = 18 000 euro. Winst 40 000 − 18 000 = 22 000 euro. 22 000 / 200 000 = 11 %.",
    ),
    volgorde(
        "Rangschik deze ondernemingen van meest naar minst solvabel.",
        [
            "Eigen vermogen 600 000 op een totaal van 1 000 000",
            "Eigen vermogen 300 000 op een totaal van 750 000",
            "Eigen vermogen 100 000 op een totaal van 400 000",
            "Eigen vermogen 50 000 op een totaal van 500 000",
        ],
        "60 %, 40 %, 25 % en 10 %.",
    ),
    mk(
        "Waarom is een heel lage solvabiliteit gevaarlijk, ook als de onderneming nu winst maakt?",
        [
            "Bij tegenvallende resultaten blijven de interest en de aflossingen wel verschuldigd",
            "Een lage solvabiliteit betekent dat de onderneming nog geen vaste klanten heeft opgebouwd",
            "De fiscus belast ondernemingen met een lage solvabiliteit hoger",
            "Een lage solvabiliteit maakt de voorraad duurder",
        ],
        0,
        "Schuldeisers moeten altijd betaald worden. Met weinig eigen vermogen is er weinig buffer om verliezen op te vangen.",
    ),
    inv(
        "Winst na belasting 45 000 euro, interestkosten 15 000 euro, totaal vermogen 750 000 euro. Hoeveel procent is de rendabiliteit van het totaal vermogen? Schrijf enkel het getal.",
        "8",
        "(45 000 + 15 000) / 750 000 · 100 = 8 %.",
    ),
    mk(
        "Twee gelijke vennootschappen maken elk jaar winst. De ene keert alles uit als dividend, de andere houdt alles in de reserves. Wat zie je na een paar jaar?",
        [
            "De tweede heeft een hogere solvabiliteit",
            "De eerste heeft een hogere solvabiliteit",
            "Hun solvabiliteit blijft gelijk, want dividend is een kost",
            "De tweede heeft meer vreemd vermogen",
        ],
        0,
        "Gereserveerde winst verhoogt het eigen vermogen. Uitgekeerde winst verlaat de vennootschap.",
    ),
    inv(
        "Eigen vermogen 210 000 euro, totaal vermogen 700 000 euro. Hoeveel procent is de schuldgraad? Schrijf enkel het getal.",
        "70",
        "Vreemd vermogen 490 000 euro. 490 000 / 700 000 · 100 = 70 %. Of: 100 % − 30 % solvabiliteit.",
    ),
    tabel(
        "De hefboom is positief. Wat gebeurt er met de rendabiliteit van het eigen vermogen?",
        [
            ("De onderneming leent extra en investeert het geld even rendabel", "Stijgt"),
            ("De onderneming betaalt een lening terug met nieuw kapitaal van de aandeelhouders", "Daalt"),
            ("De interestvoet stijgt, maar blijft onder de rendabiliteit van het totaal vermogen", "Daalt"),
            ("Het resultaat vóór interest stijgt", "Stijgt"),
        ],
        "Bij een positieve hefboom helpt meer vreemd vermogen de eigenaars. Duurdere leningen en minder lenen verkleinen dat voordeel.",
        kolommen=["Stijgt", "Daalt"],
    ),
    open_(
        "Leg met een voorbeeld uit hoe de financiële hefboom werkt.",
        "Een onderneming haalt 10 % rendement op haar totaal vermogen en leent aan 5 %. Met elke geleende euro verdient ze 10 cent en betaalt ze 5 cent interest: de 5 cent verschil gaat naar de eigenaars. Hoe meer ze leent, hoe hoger het rendement op het eigen vermogen. Als het rendement onder de 5 % zakt, werkt het omgekeerd.",
        "De hefboom versterkt het rendement in beide richtingen.",
    ),
    casus(
        "Sportzaak Fit nv heeft een totaal vermogen van 1 200 000 euro, waarvan 480 000 euro eigen vermogen. De interestkosten zijn 36 000 euro en de winst na belasting 60 000 euro.",
        [
            mk(
                "Hoeveel is de solvabiliteit van Fit nv?",
                ["40 %", "60 %", "48 %", "25 %"],
                0,
                "480 000 / 1 200 000 · 100 = 40 %.",
            ),
            mk(
                "Hoeveel is de rendabiliteit van het eigen vermogen?",
                ["12,5 %", "5 %", "20 %", "8 %"],
                0,
                "60 000 / 480 000 · 100 = 12,5 %.",
            ),
            mk(
                "Hoeveel is de rendabiliteit van het totaal vermogen, en is de hefboom positief als de interestvoet 5 % is?",
                [
                    "8 %, de hefboom is positief",
                    "8 %, de hefboom is negatief",
                    "5 %, de hefboom is neutraal",
                    "3 %, de hefboom is negatief",
                ],
                0,
                "(60 000 + 36 000) / 1 200 000 = 8 %. Dat is meer dan 5 %: positieve hefboom.",
            ),
        ],
    ),
]
