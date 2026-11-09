"""Aankopen boeken: facturen, kortingen, kosten en btw — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import kaart_zone

FACTUUR = [
    ("Brutobedrag handelsgoederen", "2 000,00", False),
    ("Handelskorting 10 %", "− 200,00", False),
    ("Nettobedrag handelsgoederen", "1 800,00", False),
    ("Vervoerkosten", "50,00", False),
    ("Totaal goederen en kosten", "1 850,00", True),
    ("Financiële korting 2 % bij betaling binnen 10 dagen", "(− 37,00)", False),
    ("Maatstaf van heffing btw", "1 813,00", False),
    ("Btw 21 %", "380,73", False),
    ("Terugstuurbare verpakking (zonder btw)", "40,00", False),
    ("Te betalen", "2 270,73", True),
]
N = len(FACTUUR)

PRENTEN = [
    dict(bestand="aankoopfactuur.svg", zelf=True,
         wat="Vereenvoudigde aankoopfactuur met handelskorting, vervoerkosten, financiële korting, btw en terugstuurbare verpakking.",
         vragen="klikvraag, tabel en meerkeuze over de factuur"),
]

VRAGEN = [
    klik(
        "Klik op de factuur op de regel met het bedrag waarop de btw berekend wordt.",
        "aankoopfactuur.svg",
        [kaart_zone(6, N)],
        "De maatstaf van heffing: goederen en kosten min de financiële korting, alsof die gebruikt wordt. De verpakking hoort er niet bij.",
    ),
    met_prent("aankoopfactuur.svg", tabel(
        "Bekijk de factuur. Welk bedrag boekt Winkel Zuid op elke rekening bij ontvangst?",
        [
            ("60400 Aankopen handelsgoederen", "1 850,00"),
            ("41100 Terug te vorderen btw", "380,73"),
            ("44000 Leveranciers", "2 270,73"),
        ],
        "Goederen en vervoerkosten samen op 60400. De btw is terug te vorderen. De leverancier krijgt het volle bedrag, want de financiële korting is nog niet verworven.",
        kolommen=["1 850,00", "1 813,00", "380,73", "2 270,73"],
    )),
    met_prent("aankoopfactuur.svg", mk(
        "Winkel Zuid betaalt binnen de 10 dagen. Hoeveel gaat er van de bankrekening af?",
        ["2 233,73 euro", "2 270,73 euro", "2 193,73 euro", "2 230,73 euro"],
        0,
        "De financiële korting van 37 euro mag eraf: 2 270,73 − 37 = 2 233,73 euro.",
    )),
    met_prent("aankoopfactuur.svg", sorteer(
        "Winkel Zuid betaalt de factuur binnen de 10 dagen. Staat elke rekening debet of credit?",
        ["Debet", "Credit"],
        [
            ["44000 Leveranciers, 2 270,73 euro", "Debet"],
            ["55000 Bank, 2 233,73 euro", "Credit"],
            ["Verkregen betalingskorting, 37 euro", "Credit"],
        ],
        "De schuld verdwijnt volledig (debet). De bank daalt (credit). De korting is een financiële opbrengst (credit).",
    )),
    met_prent("aankoopfactuur.svg", tabel(
        "Welke uitspraken over deze factuur kloppen?",
        [
            ("De vervoerkosten verhogen de aankoopwaarde van de goederen.", J),
            ("Op de verpakking wordt geen btw berekend.", J),
            ("De handelskorting wordt apart geboekt als opbrengst.", F),
            ("Als Winkel Zuid te laat betaalt, verandert het btw-bedrag.", F),
        ],
        "De handelskorting gaat meteen van de prijs af. De btw is berekend alsof de korting gebruikt wordt en blijft dus hetzelfde.",
    )),
    mk(
        "Brutobedrag 5 000 euro, handelskorting 8 %, financiële korting 2 % bij snelle betaling, btw 21 %. Hoeveel btw staat er op de factuur?",
        ["946,68 euro", "966,00 euro", "1 050,00 euro", "927,80 euro"],
        0,
        "Netto 5 000 − 400 = 4 600 euro. Maatstaf 4 600 − 92 = 4 508 euro. Btw 4 508 · 0,21 = 946,68 euro.",
    ),
    tabel(
        "Op welke rekeningklasse boek je elke aankoop?",
        [
            ("Een bestelwagen voor de leveringen", "Klasse 2"),
            ("Dozen sportschoenen die de winkel doorverkoopt", "Klasse 60"),
            ("De factuur van de boekhouder", "Klasse 61"),
            ("De huur van het magazijn", "Klasse 61"),
        ],
        "Wat je jaren gebruikt, is een vast actief. Wat je doorverkoopt, is handelsgoederen. Diensten en diverse goederen horen in 61.",
        kolommen=["Klasse 2", "Klasse 60", "Klasse 61"],
    ),
    sorteer(
        "Inkomende creditnota: 300 euro handelsgoederen teruggestuurd, btw 21 %. Staat elke rekening debet of credit?",
        ["Debet", "Credit"],
        [
            ["44000 Leveranciers, 363 euro", "Debet"],
            ["60400 Aankopen handelsgoederen, 300 euro", "Credit"],
            ["41100 Terug te vorderen btw, 63 euro", "Credit"],
        ],
        "De creditnota is het omgekeerde van de factuur: de schuld daalt, de aankopen en de terug te vorderen btw ook.",
    ),
    mk(
        "Een winkel ontving een factuur van 1 210 euro (1 000 euro handelsgoederen plus btw) en daarna een creditnota van 242 euro voor teruggestuurde goederen. Hoeveel is ze de leverancier nog schuldig?",
        ["968 euro", "1 210 euro", "1 000 euro", "800 euro"],
        0,
        "1 210 − 242 = 968 euro. De creditnota verlaagt de schuld met het volledige bedrag inclusief btw.",
    ),
    keuze(
        "Bij de aankoop van een bestelwagen boek je de wagen [[*debet op klasse 2|debet op 60400|credit op klasse 2]] en de btw [[*debet op 41100|credit op 45100|debet op 60400]].",
        "Een investeringsgoed is een vast actief. De btw is net als bij handelsgoederen terug te vorderen.",
    ),
    mk(
        "Een leerling boekt een aankoopfactuur zo: 60400 credit, 41100 credit, 44000 debet. Wat is er fout?",
        [
            "Alles staat aan de verkeerde kant",
            "Enkel de btw staat aan de verkeerde kant",
            "Er mag geen btw geboekt worden bij een aankoop",
            "Er is niets fout aan deze boeking",
        ],
        0,
        "Een aankoop is een kost (debet), terug te vorderen btw is een vordering (debet) en de schuld stijgt (credit). De leerling boekte een creditnota.",
    ),
    volgorde(
        "Zet de stappen om een aankoopfactuur te verwerken in de juiste volgorde.",
        [
            "De factuur controleren",
            "Het redeneerschema maken",
            "De boeking in het journaal schrijven",
            "De bedragen overbrengen naar het grootboek",
        ],
        "Eerst nakijken, dan redeneren welke rekeningen stijgen of dalen, dan journaliseren en tot slot in het grootboek zetten.",
    ),
    tabel(
        "Maak het redeneerschema bij een aankoopfactuur voor handelsgoederen op krediet. Wat gebeurt er met elke rekening?",
        [
            ("Aankopen handelsgoederen", "Kost +"),
            ("Terug te vorderen btw", "Actief +"),
            ("Leveranciers", "Passief +"),
        ],
        "Kost + en actief + staan debet, passief + staat credit.",
        kolommen=["Actief +", "Passief +", "Kost +", "Opbrengst +"],
    ),
    inv(
        "Nettobedrag 2 500 euro, financiële korting 2 %, btw 21 %. Hoeveel euro btw staat er op de factuur? Schrijf het bedrag met een komma.",
        "514,50",
        "Maatstaf 2 500 − 50 = 2 450 euro. 2 450 · 0,21 = 514,50 euro.",
    ),
    mk(
        "Factuur: handelsgoederen netto 1 000 euro, vervoerkosten 80 euro, terugstuurbare verpakking 30 euro, btw 21 % zonder financiële korting. Hoeveel staat er credit op 44000?",
        ["1 336,80 euro", "1 306,80 euro", "1 343,10 euro", "1 210,00 euro"],
        0,
        "Btw op 1 080 euro = 226,80 euro. 1 080 + 226,80 + 30 = 1 336,80 euro. Op de verpakking geen btw.",
    ),
    mk(
        "Waarom boek je terugstuurbare verpakking niet als kost?",
        [
            "Je krijgt het bedrag terug als je de verpakking terugstuurt",
            "Verpakking is gratis en heeft geen waarde",
            "Verpakking is een investeringsgoed van klasse 2",
            "Het bedrag wordt bij de btw opgeteld",
        ],
        0,
        "Het is een vordering op de leverancier: zodra de verpakking terug is, krijg je het geld terug.",
    ),
    sleep(
        "De [[handelskorting]] gaat meteen van de prijs af. De [[financiële korting]] krijg je enkel bij snelle betaling. De btw bereken je op het bedrag [[na]] beide kortingen.",
        ["voor", "verpakking"],
        "De handelskorting is zeker, de financiële korting voorwaardelijk. Voor de btw tellen ze allebei.",
    ),
    koppel(
        "Welk document hoort bij elke situatie bij de koper?",
        [
            ["De leverancier rekent geleverde goederen aan", "Aankoopfactuur"],
            ["De leverancier neemt beschadigde goederen terug", "Inkomende creditnota"],
            ["De winkel betaalt de leverancier via de bank", "Bankuittreksel"],
        ],
        ["Uitgaande creditnota"],
        "Voor de koper is een creditnota van de leverancier een inkomende creditnota.",
    ),
    mk(
        "Een winkel betaalt een factuur van 1 205,80 euro (netto 1 000 euro, financiële korting 2 %, btw op 980 euro) pas na de termijn. Wat boekt ze?",
        [
            "44000 debet en 55000 credit, elk 1 205,80 euro",
            "44000 debet 1 205,80, 55000 credit 1 185,80 en betalingskorting credit 20",
            "44000 debet 1 185,80 en 55000 credit 1 185,80",
            "44000 debet 1 205,80, 55000 credit 1 205,80 en een extra btw-regel",
        ],
        0,
        "Wie te laat betaalt, verliest de korting en betaalt het volle bedrag. De btw blijft zoals op de factuur.",
    ),
    tabel(
        "Welke rekening staat debet bij elke aankoop op krediet?",
        [
            ("Een computer voor de boekhouding", "Klasse 2"),
            ("Kantoorpapier dat meteen verbruikt wordt", "Klasse 61"),
            ("Koffiebonen die een koffiebar verkoopt per zak", "Klasse 60"),
        ],
        "Duurzaam gebruik: klasse 2. Verbruik: 61. Doorverkoop: 60.",
        kolommen=["Klasse 2", "Klasse 60", "Klasse 61"],
    ),
    mk(
        "Brutobedrag 4 000 euro, handelskorting 5 %, vervoerkosten 120 euro. Welk bedrag boek je debet op 60400?",
        ["3 920 euro", "3 800 euro", "4 120 euro", "4 000 euro"],
        0,
        "4 000 − 200 = 3 800 euro netto. Plus 120 euro vervoerkosten: 3 920 euro.",
    ),
    tabel(
        "Waar of niet waar over het grootboek?",
        [
            ("Elke rekening uit het journaal heeft een eigen grootboekrekening.", J),
            ("Na een aankoopfactuur stijgt het creditsaldo van 44000.", J),
            ("In het grootboek staan de boekingen per datum, niet per rekening.", F),
        ],
        "Het journaal volgt de datum, het grootboek groepeert per rekening.",
    ),
    mk(
        "Een creditnota vermeldt: 500 euro handelskorting achteraf op een eerdere levering, btw 21 %. Hoeveel daalt de terug te vorderen btw?",
        ["105 euro", "500 euro", "605 euro", "21 euro"],
        0,
        "500 · 0,21 = 105 euro. De korting verlaagt ook de btw die je kan terugvorderen.",
    ),
    keuze(
        "Op een factuur staat: \"netto 2 000 euro, financiële korting 3 % bij betaling binnen 8 dagen\". De btw wordt berekend op [[*1 940|2 000|2 060]] euro.",
        "2 000 − 60 = 1 940 euro: de btw gaat ervan uit dat de korting gebruikt wordt.",
    ),
    mk(
        "Een onderneming ontvangt een factuur van 605 euro voor het onderhoud van haar machines: 500 euro plus 21 % btw. Welke boeking klopt?",
        [
            "61 debet 500, 41100 debet 105, 44000 credit 605",
            "60400 debet 605, 44000 credit 605",
            "Klasse 2 debet 500, 41100 debet 105, 44000 credit 605",
            "61 debet 605, 44000 credit 605",
        ],
        0,
        "Onderhoud is een dienst (61), geen handelsgoed en geen investering. De btw is apart terug te vorderen.",
    ),
    open_(
        "Leg uit waarom de koper bij ontvangst van de factuur het volledige bedrag op 44000 Leveranciers boekt, ook al is er een financiële korting.",
        "De financiële korting is nog niet verworven: de koper krijgt ze pas als hij binnen de termijn betaalt. Daarom staat de volle schuld in de boeken. Bij een snelle betaling boekt hij de korting dan als financiële opbrengst.",
        "Een korting die nog van een voorwaarde afhangt, boek je pas als de voorwaarde vervuld is.",
    ),
    mk(
        "Een winkel stuurt verpakking van 30 euro terug en krijgt daarvoor een creditnota. Welke btw staat op die creditnota?",
        ["Geen", "6,30 euro", "21 % op de verpakking en de goederen samen", "Dezelfde btw als op de factuur"],
        0,
        "Op terugstuurbare verpakking werd geen btw aangerekend, dus ook bij het terugsturen niet.",
    ),
    casus(
        "Fietsenwinkel Trap ontvangt op 3 maart een factuur: 10 fietsen aan 400 euro, handelskorting 10 %, vervoerkosten 60 euro, financiële korting 2 % op goederen en kosten bij betaling binnen 10 dagen, btw 21 %.",
        [
            mk(
                "Welk bedrag boekt Trap debet op 60400?",
                ["3 660 euro", "3 600 euro", "4 060 euro", "3 586,80 euro"],
                0,
                "4 000 − 400 = 3 600 euro, plus 60 euro vervoer: 3 660 euro.",
            ),
            mk(
                "Hoeveel btw staat er op de factuur?",
                ["753,23 euro", "768,60 euro", "756,00 euro", "840,00 euro"],
                0,
                "Maatstaf 3 660 − 73,20 = 3 586,80 euro. 3 586,80 · 0,21 = 753,23 euro.",
            ),
            mk(
                "Trap betaalt op 10 maart. Hoeveel gaat er van de bank af?",
                ["4 340,03 euro", "4 413,23 euro", "4 326,80 euro", "4 286,03 euro"],
                0,
                "Factuur 3 660 + 753,23 = 4 413,23 euro. Min 73,20 euro korting: 4 340,03 euro.",
            ),
        ],
    ),
]
