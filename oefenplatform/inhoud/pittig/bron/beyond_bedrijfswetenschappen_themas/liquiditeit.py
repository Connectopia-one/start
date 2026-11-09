"""Kerncijfers: liquiditeit — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import cyclus_zone

PRENTEN = [
    dict(bestand="bedrijfscyclus.svg", zelf=True,
         wat="Bedrijfscyclus in dagen met omlooptijd voorraad, klantenkrediet, leverancierskrediet en een balk met een vraagteken.",
         vragen="klikvraag en rekenvragen over de netto te financieren periode"),
    dict(bestand="balans-velo.svg", zelf=True,
         wat="Dezelfde balans van Velo nv als bij het hoofdstuk over de balans.",
         vragen="current ratio en quick ratio"),
]

VRAGEN = [
    klik(
        "Klik op de bedrijfscyclus op de balk die de netto te financieren periode toont: de dagen waarin de groothandel de leverancier al betaald heeft, maar zelf nog geen geld van de klant kreeg.",
        "bedrijfscyclus.svg",
        [cyclus_zone("ntfp")],
        "Van dag 40 (leverancier betaald) tot dag 80 (klant betaalt): die periode moet de onderneming zelf financieren.",
    ),
    met_prent("bedrijfscyclus.svg", mk(
        "Hoeveel dagen is de netto te financieren periode van deze groothandel?",
        ["40 dagen", "80 dagen", "120 dagen", "20 dagen"],
        0,
        "Omlooptijd voorraad + klantenkrediet − leverancierskrediet = 50 + 30 − 40 = 40 dagen.",
    )),
    met_prent("bedrijfscyclus.svg", mk(
        "De groothandel spreekt af dat ze haar leverancier pas na 55 dagen betaalt. Hoeveel dagen is de netto te financieren periode dan?",
        ["25 dagen", "55 dagen", "40 dagen", "15 dagen"],
        0,
        "50 + 30 − 55 = 25 dagen. Een langer leverancierskrediet verkort de periode die je zelf moet financieren.",
    )),
    met_prent("bedrijfscyclus.svg", tabel(
        "Welke uitspraken over deze bedrijfscyclus kloppen?",
        [
            ("De goederen liggen gemiddeld 50 dagen in het magazijn voor ze verkocht worden.", J),
            ("De klant betaalt gemiddeld 30 dagen na de verkoop.", J),
            ("De leverancier wordt betaald nadat de klant betaald heeft.", F),
            ("Als de klanten sneller betalen, wordt de netto te financieren periode korter.", J),
        ],
        "De leverancier wordt op dag 40 betaald, de klant betaalt pas op dag 80.",
    )),
    met_prent("balans-velo.svg", tabel(
        "Bereken de liquiditeit van Velo nv. Welke waarde hoort bij elk kerncijfer?",
        [
            ("Current ratio", "1,33"),
            ("Quick ratio", "0,83"),
            ("Liquide middelen / vreemd vermogen op korte termijn", "0,23"),
        ],
        "Current ratio: 400 000 / 300 000 = 1,33. Quick ratio zonder voorraad: (180 000 + 70 000) / 300 000 = 0,83. Enkel de liquide middelen: 70 000 / 300 000 = 0,23.",
        kolommen=["0,23", "0,83", "1,33", "2,00"],
    )),
    mk(
        "Omzet 730 000 euro zonder btw, btw 21 %, gemiddelde handelsvorderingen 121 000 euro. Hoeveel dagen is het klantenkrediet?",
        ["50 dagen", "60 dagen", "41 dagen", "30 dagen"],
        0,
        "121 000 / (730 000 · 1,21) · 365 = 121 000 / 883 300 · 365 = 50 dagen.",
    ),
    mk(
        "Aankopen 584 000 euro zonder btw, btw 21 %, gemiddelde handelsschulden 58 080 euro. Hoeveel dagen is het leverancierskrediet?",
        ["30 dagen", "36 dagen", "25 dagen", "45 dagen"],
        0,
        "58 080 / (584 000 · 1,21) · 365 = 58 080 / 706 640 · 365 = 30 dagen.",
    ),
    mk(
        "Beginvoorraad 40 000 euro, eindvoorraad 50 000 euro, kostprijs van de verkochte goederen 657 000 euro. Hoeveel dagen is de omlooptijd van de voorraad?",
        ["25 dagen", "28 dagen", "22 dagen", "50 dagen"],
        0,
        "Gemiddelde voorraad (40 000 + 50 000) / 2 = 45 000 euro. 45 000 / 657 000 · 365 = 25 dagen.",
    ),
    mk(
        "Het klantenkrediet is 45 dagen en de omzet inclusief btw is 1 460 000 euro. Hoe groot zijn de gemiddelde handelsvorderingen?",
        ["180 000 euro", "120 000 euro", "148 760 euro", "32 444 euro"],
        0,
        "Vorderingen = omzet incl. btw · dagen / 365 = 1 460 000 · 45 / 365 = 180 000 euro.",
    ),
    tabel(
        "Een onderneming heeft een current ratio groter dan 1. Wat gebeurt er met de current ratio bij elke verrichting?",
        [
            ("Een leverancier betalen met geld van de bank", "Stijgt"),
            ("Voorraad kopen op krediet", "Daalt"),
            ("Een lening op lange termijn ontvangen op de bank", "Stijgt"),
            ("Een klant betaalt zijn factuur via de bank", "Blijft gelijk"),
        ],
        "Bij een ratio boven 1 doet een even grote daling van teller en noemer de ratio stijgen, en een even grote stijging haar dalen. Een inning wisselt enkel courante activa om.",
        kolommen=["Stijgt", "Daalt", "Blijft gelijk"],
    ),
    sorteer(
        "Verbetert of verslechtert de maatregel de liquiditeit?",
        ["Verbetert", "Verslechtert"],
        [
            ["Klanten sneller laten betalen", "Verbetert"],
            ["Minder voorraad aanhouden", "Verbetert"],
            ["Leveranciers sneller betalen dan nodig", "Verslechtert"],
            ["Een machine kopen met een lening op korte termijn", "Verslechtert"],
            ["Klantenfacturen verkopen via factoring", "Verbetert"],
        ],
        "Alles wat geld sneller binnenbrengt of later laat buitengaan, helpt de liquiditeit.",
    ),
    keuze(
        "De quick ratio laat de [[*voorraden|vorderingen|liquide middelen]] weg, omdat die eerst nog [[*verkocht|geïnd|afgeschreven]] moeten worden voor er geld binnenkomt.",
        "De quick ratio is strenger: enkel wat snel geld is, telt mee.",
    ),
    inv(
        "Courante activa 450 000 euro, vreemd vermogen op korte termijn 300 000 euro. Hoeveel is de current ratio? Schrijf het getal met een komma.",
        "1,5",
        "450 000 / 300 000 = 1,5.",
    ),
    mk(
        "Een onderneming heeft een current ratio van 1,6 en een quick ratio van 0,6. Wat besluit je?",
        [
            "Een groot deel van de courante activa zit vast in voorraad",
            "De onderneming heeft veel geld op de bank",
            "De klanten betalen heel snel",
            "De onderneming heeft geen schulden op korte termijn",
        ],
        0,
        "Het verschil tussen beide ratio's is de voorraad. Zonder die voorraad te verkopen, kan ze haar kortlopende schulden niet betalen.",
    ),
    koppel(
        "Welke berekening hoort bij elk kerncijfer?",
        [
            ["Courante activa / vreemd vermogen op korte termijn", "Current ratio"],
            ["(Vorderingen + geldbeleggingen + liquide middelen) / vreemd vermogen op korte termijn", "Quick ratio"],
            ["Gemiddelde voorraad / kostprijs verkochte goederen · 365", "Omlooptijd voorraad"],
            ["Gemiddelde handelsvorderingen / omzet incl. btw · 365", "Klantenkrediet"],
        ],
        ["Solvabiliteit"],
        "Het formularium krijg je op het examen, maar je moet weten welk kerncijfer wat meet.",
    ),
    sleep(
        "De netto te financieren periode is de omlooptijd van de voorraad [[plus]] het klantenkrediet [[min]] het leverancierskrediet.",
        ["maal", "gedeeld door"],
        "De leverancier financiert een deel van de cyclus. De rest moet de onderneming zelf dragen.",
    ),
    mk(
        "Een supermarkt heeft een negatieve netto te financieren periode. Hoe kan dat?",
        [
            "Klanten betalen meteen, en de leveranciers pas later",
            "De supermarkt betaalt haar leveranciers vooraf",
            "De voorraad ligt maanden in de rekken",
            "De klanten krijgen lang krediet",
        ],
        0,
        "Kort voorraad, bijna geen klantenkrediet en een lang leverancierskrediet: de leveranciers financieren de supermarkt.",
    ),
    mk(
        "Een onderneming wil haar netto te financieren periode met 10 dagen verkorten. Welke maatregel helpt?",
        [
            "Met de leveranciers 10 dagen langer betalingsuitstel afspreken",
            "De klanten 10 dagen langer laten betalen",
            "10 dagen meer voorraad aanhouden",
            "De leveranciers 10 dagen sneller betalen",
        ],
        0,
        "Het leverancierskrediet wordt afgetrokken: hoe langer, hoe korter de periode die je zelf financiert.",
    ),
    volgorde(
        "Zet de stappen om het klantenkrediet te berekenen in de juiste volgorde.",
        [
            "De gemiddelde handelsvorderingen berekenen",
            "De omzet verhogen met de btw",
            "De vorderingen delen door de omzet inclusief btw",
            "Het resultaat vermenigvuldigen met 365",
        ],
        "Vorderingen staan inclusief btw in de boeken, dus vergelijk je ze met de omzet inclusief btw.",
    ),
    mk(
        "Waarom gebruik je bij de omlooptijd van de voorraad de kostprijs van de verkochte goederen en niet de omzet?",
        [
            "De voorraad staat in de boeken aan aankoopprijs, niet aan verkoopprijs",
            "De omzet bevat btw die je niet mag gebruiken",
            "De kostprijs is altijd kleiner, zodat het cijfer mooier lijkt",
            "De omzet staat niet in de jaarrekening",
        ],
        0,
        "Teller en noemer moeten op dezelfde manier gewaardeerd zijn: allebei aan aankoopprijs.",
    ),
    tabel(
        "Waar of niet waar over de current ratio, de quick ratio en het nettobedrijfskapitaal?",
        [
            ("Een current ratio van 1,2 gaat samen met een positief nettobedrijfskapitaal.", J),
            ("Een negatief nettobedrijfskapitaal kan samengaan met een current ratio van 1,4.", F),
            ("De quick ratio is nooit groter dan de current ratio.", J),
        ],
        "Current ratio boven 1 betekent courante activa groter dan kortlopende schulden: dat is precies een positief nettobedrijfskapitaal.",
    ),
    inv(
        "Omlooptijd voorraad 35 dagen, klantenkrediet 40 dagen, leverancierskrediet 50 dagen. Hoeveel dagen is de netto te financieren periode? Schrijf enkel het getal.",
        "25",
        "35 + 40 − 50 = 25 dagen.",
    ),
    mk(
        "Vorderingen 90 000 euro, liquide middelen 30 000 euro, voorraad 80 000 euro, vreemd vermogen op korte termijn 150 000 euro. Wat zijn de current ratio en de quick ratio?",
        [
            "Current 1,33 en quick 0,8",
            "Current 0,8 en quick 1,33",
            "Current 1,33 en quick 0,53",
            "Current 2,0 en quick 0,8",
        ],
        0,
        "Courante activa 200 000 euro: 200 000 / 150 000 = 1,33. Zonder voorraad: 120 000 / 150 000 = 0,8.",
    ),
    mk(
        "De omzet stijgt sterk, maar de gemiddelde handelsvorderingen blijven gelijk. Wat gebeurt er met het klantenkrediet?",
        [
            "Het wordt korter",
            "Het wordt langer",
            "Het blijft gelijk",
            "Het wordt negatief",
        ],
        0,
        "De noemer wordt groter terwijl de teller gelijk blijft: de klanten betalen dus sneller.",
    ),
    met_prent("bedrijfscyclus.svg", mk(
        "De groothandel verkoopt haar goederen 10 dagen sneller. De klanten en de leverancier betalen even snel als nu. Hoeveel dagen is de netto te financieren periode dan?",
        ["30 dagen", "40 dagen", "50 dagen", "20 dagen"],
        0,
        "Omlooptijd voorraad 40 dagen: 40 + 30 − 40 = 30 dagen.",
    )),
    inv(
        "Aankopen 365 000 euro zonder btw, btw 21 %, gemiddelde handelsschulden 54 450 euro. Hoeveel dagen is het leverancierskrediet? Schrijf enkel het getal.",
        "45",
        "54 450 / (365 000 · 1,21) · 365 = 54 450 / 441 650 · 365 = 45 dagen.",
    ),
    open_(
        "Leg uit hoe een onderneming die winst maakt, toch in betalingsproblemen kan komen.",
        "Winst zegt niet wanneer het geld binnenkomt. Als de klanten traag betalen, de voorraad lang blijft liggen of de leveranciers snel betaald moeten worden, kan er te weinig geld in kas zijn om de schulden op tijd te betalen, ook al is de onderneming rendabel.",
        "Rendabiliteit en liquiditeit meten iets anders: winst tegenover geld op het juiste moment.",
    ),
    casus(
        "Groothandel Pak heeft een omzet van 1 095 000 euro zonder btw en aankopen van 730 000 euro zonder btw (btw 21 %). De kostprijs van de verkochte goederen is 730 000 euro. Gemiddeld: voorraad 60 000 euro, handelsvorderingen 145 200 euro, handelsschulden 84 700 euro.",
        [
            mk(
                "Hoeveel dagen is de omlooptijd van de voorraad?",
                ["30 dagen", "20 dagen", "36 dagen", "60 dagen"],
                0,
                "60 000 / 730 000 · 365 = 30 dagen.",
            ),
            mk(
                "Hoeveel dagen is het klantenkrediet?",
                ["40 dagen", "48 dagen", "33 dagen", "73 dagen"],
                0,
                "145 200 / (1 095 000 · 1,21) · 365 = 145 200 / 1 324 950 · 365 = 40 dagen.",
            ),
            mk(
                "Het leverancierskrediet is 35 dagen. Hoeveel dagen moet Pak zelf financieren?",
                ["35 dagen", "105 dagen", "45 dagen", "5 dagen"],
                0,
                "30 + 40 − 35 = 35 dagen.",
            ),
        ],
    ),
]
