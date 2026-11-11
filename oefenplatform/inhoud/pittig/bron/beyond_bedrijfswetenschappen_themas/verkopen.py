"""Verkopen, betalingen en geldbewegingen boeken — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import kaart_zone

KASBLAD = [
    ("Beginsaldo kas", "300,00", False),
    ("Dagontvangsten (btw 21 % inbegrepen)", "3 630,00", False),
    ("Aankoop postzegels", "− 30,00", False),
    ("Storting op de bankrekening", "− 3 000,00", False),
    ("Eindsaldo kas", "900,00", True),
]
N = len(KASBLAD)

PRENTEN = [
    dict(bestand="kasblad.svg", zelf=True,
         wat="Kasblad van een kledingwinkel met beginsaldo, dagontvangsten, een kleine uitgave, een storting en het eindsaldo.",
         vragen="klikvraag, tabel en meerkeuze over het kasblad"),
]

VRAGEN = [
    klik(
        "Klik op het kasblad op de regel die je boekt via de tussenrekening 58000 Interne overboekingen.",
        "kasblad.svg",
        [kaart_zone(3, N)],
        "Geld van de kas naar de bank is een interne geldbeweging: het blijft van de onderneming, het verandert enkel van plaats.",
    ),
    met_prent("kasblad.svg", tabel(
        "Bekijk het kasblad. Welk bedrag boekt de winkel voor de dagontvangsten op elke rekening?",
        [
            ("57000 Kassen (debet)", "3 630"),
            ("70000 Verkopen handelsgoederen (credit)", "3 000"),
            ("45100 Te betalen btw (credit)", "630"),
        ],
        "De kas ontvangt het volle bedrag. 3 630 / 1,21 = 3 000 euro verkopen, en 630 euro btw is een schuld aan de staat.",
        kolommen=["3 630", "3 000", "630", "762,30"],
    )),
    met_prent("kasblad.svg", sorteer(
        "De storting van de kas naar de bank gebeurt in twee boekingen. Welke rekening staat debet en welke credit?",
        ["Debet", "Credit"],
        [
            ["Boeking 1: 58000 Interne overboekingen", "Debet"],
            ["Boeking 1: 57000 Kassen", "Credit"],
            ["Boeking 2: 55000 Kredietinstellingen", "Debet"],
            ["Boeking 2: 58000 Interne overboekingen", "Credit"],
        ],
        "Eerst verlaat het geld de kas, dan komt het op de bank. Na de twee boekingen staat 58000 weer op nul.",
    )),
    met_prent("kasblad.svg", mk(
        "Een leerling zegt: \"De storting van 3 000 euro is een kost voor de winkel.\" Wat is de beste reactie?",
        [
            "Nee, het geld verhuist enkel van de kas naar de bank",
            "Ja, alles wat uit de kas gaat, is een kost",
            "Ja, maar je mag ze pas boeken op het einde van het jaar",
            "Nee, het is een opbrengst, want de bank stijgt",
        ],
        0,
        "Een interne geldbeweging verandert het vermogen niet: kas daalt en bank stijgt met hetzelfde bedrag.",
    )),
    mk(
        "Verkoopfactuur: brutobedrag 6 000 euro, handelskorting 5 %, doorgerekende vervoerkosten 100 euro, btw 21 %, geen financiële korting. Hoeveel staat er debet op 40000 Handelsdebiteuren?",
        ["7 018 euro", "6 897 euro", "7 381 euro", "5 800 euro"],
        0,
        "6 000 − 300 = 5 700 euro. Plus 100 euro kosten: 5 800 euro. Btw 1 218 euro. Samen 7 018 euro.",
    ),
    tabel(
        "Welke rekening en welke kant hoort bij elk bedrag van die verkoopfactuur?",
        [
            ("40000 Handelsdebiteuren, 7 018 euro", "Debet"),
            ("70000 Verkopen handelsgoederen, 5 700 euro", "Credit"),
            ("Doorgerekende kosten, 100 euro", "Credit"),
            ("45100 Te betalen btw, 1 218 euro", "Credit"),
        ],
        "De vordering op de klant staat debet. Verkopen, doorgerekende kosten en de btw-schuld staan credit.",
        kolommen=["Debet", "Credit"],
    ),
    mk(
        "Een klant betaalt een factuur van 2 411,60 euro (netto 2 000 euro, financiële korting 2 %, btw op 1 960 euro) binnen de termijn. Hoeveel ontvangt de verkoper op de bank?",
        ["2 371,60 euro", "2 411,60 euro", "2 363,37 euro", "2 420,00 euro"],
        0,
        "De klant mag 40 euro korting aftrekken: 2 411,60 − 40 = 2 371,60 euro.",
    ),
    sorteer(
        "De klant betaalt die factuur met financiële korting. Debet of credit bij de verkoper?",
        ["Debet", "Credit"],
        [
            ["55000 Kredietinstellingen, 2 371,60 euro", "Debet"],
            ["Toegestane betalingskorting, 40 euro", "Debet"],
            ["40000 Handelsdebiteuren, 2 411,60 euro", "Credit"],
        ],
        "De vordering verdwijnt volledig (credit). De bank stijgt en de korting is een financiële kost (debet).",
    ),
    tabel(
        "Waar of niet waar over een uitgaande creditnota?",
        [
            ("Ze verlaagt de vordering op de klant.", J),
            ("Ze verlaagt de te betalen btw.", J),
            ("De verkoper boekt 40000 debet.", F),
            ("Voor de klant is het een inkomende creditnota.", J),
        ],
        "De creditnota is het omgekeerde van de verkoopfactuur: 70000 en 45100 debet, 40000 credit.",
    ),
    mk(
        "Een winkel stuurde een factuur van 3 630 euro (3 000 euro plus btw). De klant stuurt goederen van 500 euro terug. Hoeveel staat er nog open op 40000?",
        ["3 025 euro", "3 130 euro", "3 500 euro", "2 500 euro"],
        0,
        "De creditnota is 500 + 105 = 605 euro. 3 630 − 605 = 3 025 euro.",
    ),
    keuze(
        "Dagontvangsten van een winkel boek je [[*met de kassa-opbrengst van de dag, btw inbegrepen|met een factuur per klant|enkel aan het einde van het jaar]], en de btw zit er [[*al in|nog niet in|nooit in]].",
        "In de detailhandel krijgt niet elke klant een factuur. De kassa geeft het totaal per dag, btw inbegrepen.",
    ),
    inv(
        "Dagontvangsten 4 840 euro, btw 21 % inbegrepen. Hoeveel euro verkopen zonder btw boek je op 70000? Schrijf enkel het getal.",
        "4000",
        "4 840 / 1,21 = 4 000 euro. De rest, 840 euro, is btw.",
    ),
    tabel(
        "Is het een interne geldbeweging?",
        [
            ("Geld van de bank afhalen voor de kassa", J),
            ("Een overschrijving van de zichtrekening naar de spaarrekening van de onderneming", J),
            ("Een leverancier betalen via de bank", F),
            ("Een klant betaalt cash", F),
        ],
        "Intern: het geld blijft van de onderneming. Bij een leverancier of een klant gaat het geld naar of komt het van iemand anders.",
    ),
    mk(
        "Waarom gebruik je 58000 Interne overboekingen bij een storting van kas naar bank, in plaats van rechtstreeks 55000 debet en 57000 credit?",
        [
            "Kas en bank worden apart geboekt, vaak op een ander moment en van een ander stuk",
            "Omdat er btw op een storting zit die apart moet staan in de boekhouding van de onderneming",
            "Omdat 58000 een kostenrekening is",
            "Omdat de bank anders twee keer zou stijgen",
        ],
        0,
        "Het kasblad en het bankuittreksel worden elk apart verwerkt. De tussenrekening voorkomt dat je de beweging twee keer of niet boekt.",
    ),
    koppel(
        "Welk stuk is de basis van elke boeking?",
        [
            ["Een klant betaalt een factuur via overschrijving", "Bankuittreksel"],
            ["De winkel verkoopt contant aan particulieren", "Kasticket of kasblad"],
            ["De winkel neemt goederen terug van een klant", "Uitgaande creditnota"],
            ["De winkel levert op krediet aan een bedrijf", "Verkoopfactuur"],
        ],
        ["Inkomende creditnota"],
        "Elke boeking steunt op een stuk dat bewijst wat er gebeurde.",
    ),
    mk(
        "Een klant betaalt een factuur te laat en trekt toch 2 % financiële korting af. De verkoper aanvaardt dat niet. Wat staat er nog open op 40000?",
        [
            "Het bedrag van de korting",
            "Niets, de klant heeft betaald",
            "Het volle factuurbedrag",
            "De btw op de korting",
        ],
        0,
        "Na de termijn heeft de klant geen recht meer op de korting. Het verschil blijft een vordering.",
    ),
    sleep(
        "Bij een verkoop op krediet stijgt de vordering op [[40000]] Handelsdebiteuren. De opbrengst komt op [[70000]] Verkopen handelsgoederen, en de btw op [[45100]] Te betalen btw.",
        ["41100", "44000"],
        "41100 is de terug te vorderen btw bij aankopen en 44000 de schuld aan leveranciers.",
    ),
    mk(
        "Verkoopfactuur: netto 1 500 euro, terugstuurbare verpakking 50 euro, btw 21 %. Hoeveel staat er credit op 45100?",
        ["315 euro", "325,50 euro", "1 815 euro", "10,50 euro"],
        0,
        "Op de verpakking komt geen btw: 1 500 · 0,21 = 315 euro.",
    ),
    tabel(
        "Op welke rekening boek je elk bedrag van de verkoper?",
        [
            ("De btw op een verkoopfactuur", "45100"),
            ("Het totaal van een verkoopfactuur op krediet", "40000"),
            ("De verkoop van handelsgoederen", "70000"),
            ("Contant geld uit de kassa", "57000"),
        ],
        "Bij verkopen: 40000 vordering, 70000 opbrengst, 45100 btw-schuld, 57000 cash.",
        kolommen=["40000", "45100", "57000", "70000"],
    ),
    mk(
        "Wat is het verschil tussen de financiële korting bij de koper en bij de verkoper?",
        [
            "Voor de koper is ze een opbrengst, voor de verkoper een kost",
            "Voor allebei is ze een kost",
            "Voor de koper is ze een kost, voor de verkoper een opbrengst",
            "Ze wordt bij geen van beiden geboekt, enkel op de factuur",
        ],
        0,
        "De koper betaalt minder: verkregen betalingskorting. De verkoper ontvangt minder: toegestane betalingskorting.",
    ),
    volgorde(
        "Zet de verrichtingen bij een verkoop op krediet in de juiste volgorde, vanuit de verkoper.",
        [
            "De verkoopfactuur opmaken en boeken",
            "Een uitgaande creditnota boeken voor teruggenomen goederen",
            "Het bankuittreksel met de betaling van de klant boeken",
            "Vaststellen dat 40000 voor deze klant op nul staat",
        ],
        "Factuur, eventuele creditnota, betaling: daarna is de vordering volledig weg.",
    ),
    mk(
        "Welke verrichtingen komen op het kasblad van de winkel? Duid alle juiste antwoorden aan.",
        [
            "Een contante verkoop aan een particulier",
            "Postzegels die cash betaald worden",
            "Een leverancier betalen via overschrijving",
            "Een verkoop op krediet aan een bedrijf",
        ],
        [0, 1],
        "Op het kasblad staat enkel wat met contant geld gebeurt. Overschrijvingen staan op het bankuittreksel, een verkoop op krediet op de factuur.",
    ),
    sorteer(
        "De winkel maakt een uitgaande creditnota voor teruggenomen goederen. Debet of credit?",
        ["Debet", "Credit"],
        [
            ["70000 Verkopen handelsgoederen", "Debet"],
            ["45100 Te betalen btw", "Debet"],
            ["40000 Handelsdebiteuren", "Credit"],
        ],
        "Het omgekeerde van de verkoopfactuur: de opbrengst en de btw-schuld dalen, de vordering op de klant ook.",
    ),
    tabel(
        "Een klant betaalt een factuur van 1 000 euro deels cash en deels via de bank. Welke uitspraken kloppen?",
        [
            ("57000 en 55000 staan allebei debet.", J),
            ("40000 staat credit voor 1 000 euro.", J),
            ("Er komt opnieuw btw bij.", F),
        ],
        "Twee geldrekeningen stijgen samen met het totaal van de vordering. De btw werd al bij de factuur geboekt.",
    ),
    inv(
        "Een klant betaalt binnen de termijn een factuur van 6 050 euro, met 100 euro financiële korting. Hoeveel euro ontvangt de verkoper? Schrijf enkel het getal.",
        "5950",
        "6 050 − 100 = 5 950 euro.",
    ),
    mk(
        "Doorgerekende vervoerkosten op een verkoopfactuur: hoe boekt de verkoper ze?",
        [
            "Als opbrengst, met btw erop",
            "Als kost, zonder btw",
            "Als vordering zonder btw, zoals verpakking",
            "Niet, want de klant betaalt de transporteur zelf",
        ],
        0,
        "De verkoper rekent de kosten aan de klant aan: dat is een opbrengst, en er komt btw op.",
    ),
    open_(
        "Leg uit waarom het saldo van 58000 Interne overboekingen na een volledige storting van kas naar bank nul is.",
        "Bij de eerste boeking staat 58000 debet voor het bedrag dat uit de kas gaat. Bij de tweede boeking staat het credit voor hetzelfde bedrag dat op de bank komt. Debet en credit heffen elkaar op.",
        "Een tussenrekening blijft enkel open zolang een van de twee boekingen ontbreekt.",
    ),
    casus(
        "Schoenwinkel Stap verkoopt op 2 mei op krediet aan een sportclub: 50 paar aan 80 euro, handelskorting 10 %, financiële korting 2 % bij betaling binnen 8 dagen, btw 21 %. Op 9 mei betaalt de club via de bank.",
        [
            mk(
                "Hoeveel btw rekent Stap aan op de factuur aan de sportclub?",
                ["740,88 euro", "756,00 euro", "840,00 euro", "725,76 euro"],
                0,
                "4 000 − 400 = 3 600 euro. Maatstaf 3 600 − 72 = 3 528 euro. 3 528 · 0,21 = 740,88 euro.",
            ),
            mk(
                "Welk bedrag boekt Stap debet op 40000 op 2 mei?",
                ["4 340,88 euro", "4 268,88 euro", "4 356,00 euro", "4 340,00 euro"],
                0,
                "3 600 + 740,88 = 4 340,88 euro: de korting is nog niet toegekend.",
            ),
            mk(
                "Wat ontvangt Stap op 9 mei op de bank?",
                ["4 268,88 euro", "4 340,88 euro", "4 196,88 euro", "4 254,48 euro"],
                0,
                "De club betaalt binnen 8 dagen: 4 340,88 − 72 = 4 268,88 euro.",
            ),
        ],
    ),
]
