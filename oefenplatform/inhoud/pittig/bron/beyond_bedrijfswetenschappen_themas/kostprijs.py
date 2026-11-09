"""Kostprijsberekening en break-even — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import be_zone, be_zones

PRENTEN = [
    dict(bestand="breakeven.svg", zelf=True,
         wat="Break-evengrafiek van Plaat bv: vaste kosten (A), totale kosten (B) en omzet (C) volgens de afzet.",
         vragen="klikvragen en rekenvragen over het break-evenpunt"),
]

VRAGEN = [
    klik(
        "Klik op het break-evenpunt van Plaat bv.",
        "breakeven.svg",
        [be_zone("punt")],
        "Het break-evenpunt ligt waar de omzet (C) de totale kosten (B) snijdt: bij 1 000 stuks en 50 000 euro.",
    ),
    klik(
        "Klik op een plaats in de grafiek waar Plaat bv winst maakt.",
        "breakeven.svg",
        be_zones("winst"),
        "Rechts van het break-evenpunt ligt de omzet (C) boven de totale kosten (B): daar is er winst.",
    ),
    klik(
        "Klik op een plaats in de grafiek waar Plaat bv verlies maakt.",
        "breakeven.svg",
        be_zones("verlies"),
        "Links van het break-evenpunt ligt de omzet (C) onder de totale kosten (B): daar is er verlies.",
    ),
    met_prent("breakeven.svg", tabel(
        "Wat stelt elke lijn voor?",
        [
            ("Lijn A: horizontaal op 20 000 euro", "Vaste kosten"),
            ("Lijn B: start op 20 000 euro en stijgt", "Totale kosten"),
            ("Lijn C: start in nul en stijgt het steilst", "Omzet"),
        ],
        "De vaste kosten veranderen niet met de afzet. De totale kosten = vaste + variabele kosten. De omzet start bij nul verkochte stuks.",
        kolommen=["Vaste kosten", "Totale kosten", "Omzet"],
    )),
    met_prent("breakeven.svg", mk(
        "Hoeveel bedragen de variabele kosten per stuk van Plaat bv?",
        ["30 euro", "50 euro", "20 euro", "10 euro"],
        0,
        "Bij 2 000 stuks zijn de totale kosten 80 000 euro. Daarvan is 20 000 vast: 60 000 / 2 000 = 30 euro per stuk.",
    )),
    met_prent("breakeven.svg", mk(
        "Wat is de verkoopprijs per stuk van Plaat bv?",
        ["50 euro", "30 euro", "100 euro", "20 euro"],
        0,
        "Bij 2 000 stuks is de omzet 100 000 euro: 100 000 / 2 000 = 50 euro.",
    )),
    met_prent("breakeven.svg", mk(
        "Hoeveel winst maakt Plaat bv bij een afzet van 1 500 stuks?",
        ["10 000 euro", "75 000 euro", "30 000 euro", "5 000 euro"],
        0,
        "Omzet 1 500 × 50 = 75 000. Kosten 20 000 + 1 500 × 30 = 65 000. Winst 10 000 euro, of 500 stuks boven break-even × 20 euro dekkingsbijdrage.",
    )),
    met_prent("breakeven.svg", mk(
        "De vaste kosten van Plaat bv stijgen tot 30 000 euro. Prijs en variabele kosten blijven gelijk. Wat wordt de break-evenafzet?",
        ["1 500 stuks", "1 000 stuks", "600 stuks", "1 200 stuks"],
        0,
        "30 000 / (50 − 30) = 30 000 / 20 = 1 500 stuks.",
    )),
    tabel(
        "Is de kost vast of variabel voor een fabriek van stoelen?",
        [
            ("Het hout voor de stoelen", "Variabel"),
            ("De huur van de fabriekshal", "Vast"),
            ("De verzekering van het gebouw", "Vast"),
            ("De verpakking van elke stoel", "Variabel"),
        ],
        "Variabele kosten stijgen met elke extra stoel, vaste kosten blijven gelijk.",
        kolommen=["Vast", "Variabel"],
    ),
    tabel(
        "Is de kost direct of indirect voor de kostendrager \"stoel model Luna\"?",
        [
            ("Het hout dat in een stoel Luna gaat", "Direct"),
            ("Het loon van de arbeider die enkel stoelen Luna maakt", "Direct"),
            ("De verwarming van de fabriek waar verschillende modellen gemaakt worden", "Indirect"),
            ("Het loon van de boekhouder", "Indirect"),
        ],
        "Een directe kost kan je rechtstreeks aan één product toewijzen. Een indirecte kost wordt gedeeld en moet verdeeld worden.",
        kolommen=["Direct", "Indirect"],
    ),
    koppel(
        "Koppel het begrip aan de juiste omschrijving.",
        [
            ["Kostendrager", "Het product waaraan je de kosten toewijst"],
            ["Kostenplaats", "De afdeling waar kosten ontstaan"],
            ["Verdeelsleutel", "De maatstaf om indirecte kosten te verdelen"],
        ],
        ["De winst na belastingen"],
        "Wat krijgt de kosten, waar ontstaan ze en hoe verdeel je ze?",
    ),
    tabel(
        "Welke verdeelsleutel past het best?",
        [
            ("Huur van het gebouw", "Oppervlakte"),
            ("Elektriciteit van de machines", "Machine-uren"),
            ("Kosten van de personeelsdienst", "Aantal werknemers"),
        ],
        "De sleutel moet zo goed mogelijk weerspiegelen hoeveel elke afdeling van de kost gebruikt.",
        kolommen=["Oppervlakte", "Machine-uren", "Aantal werknemers"],
    ),
    mk(
        "De huur van 18 000 euro wordt verdeeld volgens oppervlakte. Productie gebruikt 450 m², aankoop 90 m² en verkoop 60 m². Hoeveel huur krijgt productie?",
        ["13 500 euro", "6 000 euro", "4 500 euro", "2 700 euro"],
        0,
        "Totaal 600 m². Productie: 450 / 600 × 18 000 = 13 500 euro.",
    ),
    mk(
        "De directe kosten van een kast zijn 300 euro. Het bedrijf rekent 35 % opslag voor indirecte kosten. Wat is de kostprijs volgens de eenvoudige opslagmethode?",
        ["405 euro", "335 euro", "105 euro", "465 euro"],
        0,
        "300 × 1,35 = 405 euro.",
    ),
    volgorde(
        "Zet de opbouw van de verkoopprijs in de juiste volgorde, van de eerste naar de laatste stap.",
        [
            "Directe kosten",
            "Fabricagekostprijs",
            "Verkoopkostprijs",
            "Verkoopprijs zonder btw",
        ],
        "Elke stap telt er een laag kosten of winst bij.",
    ),
    tabel(
        "Een tafel heeft een fabricagekostprijs van 240 euro. De verkoop- en administratiekosten zijn 60 euro per tafel. De winstopslag is 20 % op de verkoopkostprijs. Vul aan.",
        [
            ("Verkoopkostprijs", "300 euro"),
            ("Winstopslag", "60 euro"),
            ("Verkoopprijs zonder btw", "360 euro"),
        ],
        "240 + 60 = 300. 20 % van 300 = 60. 300 + 60 = 360.",
        kolommen=["60 euro", "300 euro", "360 euro"],
    ),
    mk(
        "Een handelaar koopt een lamp aan 80 euro en rekent 45 % op de inkoopprijs. Wat is de verkoopprijs zonder btw?",
        ["116 euro", "125 euro", "36 euro", "145 euro"],
        0,
        "80 × 1,45 = 116 euro.",
    ),
    mk(
        "Vaste kosten 48 000 euro, verkoopprijs 75 euro, variabele kosten 45 euro per stuk. Wat is de break-evenomzet?",
        ["120 000 euro", "1 600 euro", "80 000 euro", "48 000 euro"],
        0,
        "Break-evenafzet = 48 000 / (75 − 45) = 1 600 stuks. Omzet = 1 600 × 75 = 120 000 euro.",
    ),
    keuze(
        "Als de verkoopprijs stijgt en de rest gelijk blijft, wordt de dekkingsbijdrage [[*groter|kleiner|nul]] en de break-evenafzet [[*kleiner|groter|gelijk]].",
        "Elk stuk dekt dan meer van de vaste kosten, dus je hebt er minder nodig.",
    ),
    tabel(
        "Waar of niet waar over kosten en break-even?",
        [
            ("De vaste kosten per stuk dalen als je meer produceert.", J),
            ("De variabele kosten per stuk stijgen meestal als je meer produceert.", F),
            ("Als de vaste kosten stijgen, stijgt ook de break-evenafzet.", J),
            ("De break-evenomzet wordt uitgedrukt in stuks.", F),
        ],
        "Vaste kosten worden over meer stuks gespreid. De break-evenomzet is een bedrag in euro.",
    ),
    inv(
        "Hoe noemt men het aantal stuks waarbij een onderneming geen winst en geen verlies maakt?",
        "break-evenafzet",
        "De omzet dekt dan net alle vaste en variabele kosten.",
    ),
    mk(
        "Een meubelmaker rekent voor al zijn producten hetzelfde opslagpercentage voor indirecte kosten. Wat is daar het nadeel van?",
        [
            "Ze rekent één percentage voor alle indirecte kosten, ongeacht welke afdeling ze veroorzaakt",
            "Ze vergeet de directe kosten mee te tellen",
            "Ze is enkel toegelaten voor handelsbedrijven",
            "Ze rekent de winst twee keer mee",
        ],
        0,
        "Niet elk product gebruikt evenveel van de gedeelde kosten. Eén percentage voor alles is dan te ruw.",
    ),
    mk(
        "Vaste kosten 30 000 euro. De dekkingsbijdrage is 25 % van de verkoopprijs. Hoeveel is de break-evenomzet?",
        ["120 000 euro", "7 500 euro", "37 500 euro", "40 000 euro"],
        0,
        "Elke euro omzet dekt 0,25 euro vaste kosten. 30 000 / 0,25 = 120 000 euro.",
    ),
    mk(
        "Verkoopkostprijs 150 euro. De verkoopprijs zonder btw is 180 euro. Hoeveel procent winstopslag op de verkoopkostprijs is dat?",
        ["20 %", "30 %", "16,7 %", "25 %"],
        0,
        "Winst 180 − 150 = 30 euro. 30 / 150 = 0,20 = 20 %.",
    ),
    mk(
        "Een fabriek produceert 2 000 stuks. De vaste kosten zijn 40 000 euro. Hoeveel vaste kosten draagt elk stuk, en wat gebeurt er bij 4 000 stuks?",
        ["20 euro per stuk, bij 4 000 stuks 10 euro", "20 euro per stuk, bij 4 000 stuks 40 euro", "40 euro per stuk, bij 4 000 stuks ook 40 euro", "10 euro per stuk, bij 4 000 stuks 20 euro"],
        0,
        "40 000 / 2 000 = 20 euro. 40 000 / 4 000 = 10 euro: de vaste kosten worden over meer stuks gespreid.",
    ),
    mk(
        "De afdeling productie krijgt 30 000 euro gedeelde kosten toegewezen. Ze maakt 6 000 stoelen. Welk bedrag komt er per stoel bij de directe kosten?",
        ["5 euro", "30 euro", "6 euro", "50 euro"],
        0,
        "30 000 / 6 000 = 5 euro per stoel. Zo kom je tot de fabricagekostprijs.",
    ),
    open_(
        "Een bakker met hoge vaste kosten en lage variabele kosten twijfelt of hij zijn prijzen moet verlagen om meer brood te verkopen. Leg uit waar hij op moet letten, met het begrip dekkingsbijdrage.",
        "Een lagere prijs verkleint de dekkingsbijdrage per brood, waardoor de break-evenafzet stijgt. De prijsverlaging loont enkel als hij daardoor genoeg extra broden verkoopt om de kleinere dekkingsbijdrage per stuk te compenseren.",
        "Kijk altijd naar wat elk stuk bijdraagt tot het dekken van de vaste kosten.",
    ),
    casus(
        "Kaarsenmakerij Vlam heeft vaste kosten van 24 000 euro per jaar. Een kaars kost 4 euro aan variabele kosten en wordt verkocht aan 10 euro zonder btw.",
        [
            mk(
                "Hoeveel is de dekkingsbijdrage per kaars?",
                ["6 euro", "10 euro", "4 euro", "14 euro"],
                0,
                "10 − 4 = 6 euro.",
            ),
            mk(
                "Hoeveel kaarsen moet Vlam verkopen om break-even te draaien?",
                ["4 000", "2 400", "6 000", "1 714"],
                0,
                "24 000 / 6 = 4 000 kaarsen.",
            ),
            mk(
                "Vlam verkoopt 5 500 kaarsen. Hoeveel winst maakt ze?",
                ["9 000 euro", "55 000 euro", "33 000 euro", "31 000 euro"],
                0,
                "1 500 kaarsen boven break-even × 6 euro = 9 000 euro.",
            ),
        ],
    ),
]
