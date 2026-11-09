"""De personenbelasting — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import kaart_zone

# De regels van de prent aanslagbiljet.svg: (label, bedrag, vet).
BILJET = [
    ("Belastbaar inkomen", "38 000,00", False),
    ("Belasting volgens de schijven", "13 550,00", False),
    ("Vermindering voor de belastingvrije som", "− 2 500,00", False),
    ("Belastingvermindering voor giften", "− 300,00", False),
    ("Belasting na verminderingen", "10 750,00", True),
    ("Gemeentebelasting (7 %)", "752,50", False),
    ("Totale belasting", "11 502,50", True),
    ("Ingehouden bedrijfsvoorheffing", "− 12 100,00", False),
    ("Saldo", "− 597,50", True),
]
N = len(BILJET)

PRENTEN = [
    dict(bestand="aanslagbiljet.svg", zelf=True,
         wat="Vereenvoudigd aanslagbiljet met negen regels, van belastbaar inkomen tot saldo.",
         vragen="klikvraag, tabel en meerkeuze over het aanslagbiljet"),
]

SCHIJVEN = "Schijven: tot 15 000 euro aan 25 %, van 15 000 tot 26 000 euro aan 40 %, van 26 000 tot 45 000 euro aan 45 %, daarboven 50 %."

VRAGEN = [
    mk(
        SCHIJVEN + " Hoeveel belasting volgens de schijven betaal je op een belastbaar inkomen van 38 000 euro?",
        ["13 550 euro", "17 100 euro", "15 200 euro", "9 500 euro"],
        0,
        "3 750 + 11 000 · 0,40 = 4 400 + 12 000 · 0,45 = 5 400. Samen 13 550 euro.",
    ),
    mk(
        SCHIJVEN + " Hoeveel belasting volgens de schijven betaal je op 50 000 euro?",
        ["19 200 euro", "25 000 euro", "22 500 euro", "16 700 euro"],
        0,
        "3 750 + 4 400 + 19 000 · 0,45 = 8 550 + 5 000 · 0,50 = 2 500. Samen 19 200 euro.",
    ),
    mk(
        SCHIJVEN + " De belasting volgens de schijven is 6 950 euro. Hoe hoog is het belastbaar inkomen?",
        ["23 000 euro", "17 375 euro", "27 800 euro", "21 950 euro"],
        0,
        "De eerste schijf geeft 3 750 euro. Er blijft 3 200 euro over, aan 40 %: dat is 8 000 euro in de tweede schijf. 15 000 + 8 000 = 23 000 euro.",
    ),
    tabel(
        "Wie verdient 38 000 euro, valt met zijn hoogste euro in de schijf van 45 %. Welke uitspraken kloppen?",
        [
            ("De eerste 15 000 euro wordt aan 25 % belast.", J),
            ("Het hele inkomen wordt aan 45 % belast.", F),
            ("In totaal betaalt hij minder dan 45 % van zijn inkomen.", J),
            ("Een opslag van 100 euro kost hem 45 euro extra belasting.", J),
        ],
        "Elk deel van het inkomen heeft zijn eigen tarief. Alleen wat in de hoogste schijf valt, betaalt 45 %.",
    ),
    mk(
        "De belastingvrije som is 10 000 euro, plus 1 900 euro voor één kind ten laste. Ze wordt verrekend aan 25 %. Hoeveel bedraagt de vermindering?",
        ["2 975 euro", "2 500 euro", "475 euro", "11 900 euro"],
        0,
        "10 000 + 1 900 = 11 900 euro. 11 900 · 0,25 = 2 975 euro minder belasting.",
    ),
    sorteer(
        "Tot welke soort inkomsten behoort elk bedrag?",
        ["Onroerend", "Roerend", "Beroeps", "Divers"],
        [
            ["De huur van een appartement dat je verhuurt", "Onroerend"],
            ["Dividenden van aandelen", "Roerend"],
            ["Een werkloosheidsuitkering", "Beroeps"],
            ["Het pensioen van een gepensioneerde", "Beroeps"],
            ["Interesten op een termijnrekening", "Roerend"],
            ["Een ontvangen onderhoudsuitkering", "Divers"],
        ],
        "Vervangingsinkomens zoals werkloosheid en pensioen horen bij de beroepsinkomsten. Onderhoudsuitkeringen zijn diverse inkomsten.",
    ),
    inv(
        "Op een aanslagbiljet staat aanslagjaar 2026. In welk jaar werden die inkomsten verdiend? Schrijf het jaartal.",
        "2025",
        "Het aanslagjaar volgt op het inkomstenjaar: inkomsten van 2025 horen bij aanslagjaar 2026.",
    ),
    volgorde(
        "Zet de stappen van de inning van de personenbelasting in de juiste volgorde.",
        [
            "Je verdient je loon en de werkgever houdt bedrijfsvoorheffing in",
            "Je dient je aangifte in via Tax-on-web",
            "De FOD Financiën berekent de belasting",
            "Je krijgt het aanslagbiljet",
            "Je betaalt bij of krijgt geld terug",
        ],
        "Eerst het inkomstenjaar met de voorheffing, dan in het aanslagjaar de aangifte, de berekening, het aanslagbiljet en de afrekening.",
    ),
    tabel(
        "Werkt elk voordeel op het inkomen (aftrek) of op de berekende belasting (vermindering)?",
        [
            ("Beroepskosten die van het brutoinkomen afgaan", "Aftrek"),
            ("Een gift aan een erkende instelling", "Vermindering"),
            ("Stortingen voor pensioensparen", "Vermindering"),
            ("De belastingvrije som", "Vermindering"),
        ],
        "Een aftrek verlaagt het belastbaar inkomen. Giften, pensioensparen en de belastingvrije som werken als vermindering op de belasting.",
        kolommen=["Aftrek", "Vermindering"],
    ),
    mk(
        "Mila geeft 500 euro aan een erkende instelling. Ze krijgt 45 % belastingvermindering. Wat kost die gift haar echt?",
        ["275 euro", "225 euro", "500 euro", "455 euro"],
        0,
        "De vermindering is 500 · 0,45 = 225 euro. Netto kost de gift 500 − 225 = 275 euro.",
    ),
    mk(
        "Ouders betalen 2 400 euro voor erkende kinderopvang. Ze krijgen 45 % vermindering. Hoeveel minder belasting betalen ze?",
        ["1 080 euro", "1 320 euro", "2 400 euro", "450 euro"],
        0,
        "2 400 · 0,45 = 1 080 euro minder belasting.",
    ),
    met_prent("aanslagbiljet.svg", tabel(
        "Bekijk het aanslagbiljet. Welke uitspraken kan je staven?",
        [
            ("Deze persoon krijgt geld terug.", J),
            ("De gemeentebelasting is berekend op de belasting na verminderingen.", J),
            ("De belastingvrije som verlaagt het belastbaar inkomen.", F),
            ("Via het loon werd te weinig voorheffing ingehouden.", F),
        ],
        "Het saldo is negatief: er werd 12 100 euro ingehouden, de belasting is maar 11 502,50 euro. De belastingvrije som staat als vermindering op de belasting.",
    )),
    klik(
        "Klik op het aanslagbiljet op de regel die toont hoeveel belasting de persoon tijdens het jaar al betaalde via zijn loon.",
        "aanslagbiljet.svg",
        [kaart_zone(7, N)],
        "De ingehouden bedrijfsvoorheffing: het voorschot dat de werkgever elke maand doorstortte.",
    ),
    met_prent("aanslagbiljet.svg", mk(
        "Kijk naar het aanslagbiljet. Hoe komt men aan 752,50 euro gemeentebelasting?",
        [
            "7 % van 10 750 euro",
            "7 % van 38 000 euro",
            "7 % van 13 550 euro",
            "7 % van 12 100 euro",
        ],
        0,
        "De gemeentebelasting is een percentage van de belasting na verminderingen: 10 750 · 0,07 = 752,50 euro.",
    )),
    met_prent("aanslagbiljet.svg", mk(
        "Stel dat de werkgever maar 11 000 euro bedrijfsvoorheffing had ingehouden. Wat zou het saldo dan zijn?",
        ["502,50 euro bijbetalen", "502,50 euro terugkrijgen", "1 100 euro bijbetalen", "597,50 euro terugkrijgen"],
        0,
        "11 502,50 − 11 000 = 502,50 euro. De voorheffing is dan te laag, dus je betaalt bij.",
    )),
    keuze(
        "Bij een [[*progressieve|vlakke|dalende]] belasting stijgt het tarief per schijf. Het tarief van de hoogste schijf waarin je inkomen valt, heet het [[*marginaal|gemiddeld|vast]] tarief.",
        "Het marginaal tarief geldt voor je laatste euro. Wat je gemiddeld betaalt, ligt lager.",
    ),
    mk(
        "Een werknemer krijgt 1 000 euro opslag en valt daardoor voor een deel in een hogere schijf. Een collega zegt: \"Nu verdien je netto minder dan vroeger.\" Klopt dat?",
        [
            "Nee: enkel het stuk boven de grens krijgt het hogere tarief",
            "Ja: het hele inkomen krijgt nu het hogere tarief",
            "Ja: de belastingvrije som valt weg bij een opslag",
            "Nee: opslag wordt nooit belast in de personenbelasting",
        ],
        0,
        "Bij schijven betaal je het hogere tarief alleen op het deel boven de grens. Je houdt netto dus altijd meer over.",
    ),
    tabel(
        "Waar of niet waar over het inkomstenjaar en het aanslagjaar?",
        [
            ("Loon van december 2026 hoort bij aanslagjaar 2027.", J),
            ("De aangifte van aanslagjaar 2027 dien je in 2027 in.", J),
            ("Het aanslagbiljet voor inkomsten 2026 komt nog in 2026.", F),
        ],
        "Het aanslagjaar is altijd het jaar na het inkomstenjaar, en daarin volgen aangifte en aanslagbiljet.",
    ),
    sleep(
        "Je werkgever houdt elke maand [[bedrijfsvoorheffing]] in op je loon. Dat is een [[voorschot]] op je personenbelasting. Op het [[aanslagbiljet]] wordt het verrekend met de echte belasting.",
        ["btw", "vennootschapsbelasting", "boete"],
        "De voorheffing is geen aparte belasting, maar een voorschot dat later wordt verrekend.",
    ),
    mk(
        SCHIJVEN + " Ann verdient 26 000 euro, Bert 52 000 euro. Bert verdient dubbel zoveel. Betaalt hij ook dubbel zoveel belasting volgens de schijven?",
        [
            "Nee, meer dan dubbel: 20 200 tegenover 8 150 euro",
            "Ja, precies dubbel: 16 300 tegenover 8 150 euro",
            "Nee, minder dan dubbel: 12 000 tegenover 8 150 euro",
            "Ja, want het tarief is voor iedereen 40 %",
        ],
        0,
        "Ann: 3 750 + 4 400 = 8 150 euro. Bert: 8 150 + 8 550 + 7 000 · 0,50 = 3 500, samen 20 200 euro. Dat is meer dan dubbel: zo werkt progressiviteit.",
    ),
    koppel(
        "Welk document of welke toepassing hoort bij elke stap?",
        [
            ["Je dient je aangifte online in", "Tax-on-web"],
            ["Je ziet hoeveel je moet bijbetalen of terugkrijgt", "Aanslagbiljet"],
            ["Je bewijst dat je een gift deed", "Fiscaal attest"],
            ["Je ziet hoeveel voorheffing er van je loon afging", "Loonbrief"],
        ],
        ["Factuur"],
        "Elk document heeft zijn plaats in de inning: van loonbrief tot aanslagbiljet.",
    ),
    inv(
        SCHIJVEN + " Hoeveel euro belasting volgens de schijven betaal je op 20 000 euro? Schrijf enkel het getal.",
        "5750",
        "15 000 · 0,25 = 3 750 en 5 000 · 0,40 = 2 000. Samen 5 750 euro.",
    ),
    mk(
        "Waarom betalen twee mensen met hetzelfde belastbaar inkomen soms een verschillende belasting? Duid alle juiste antwoorden aan.",
        [
            "De een heeft kinderen ten laste, de ander niet",
            "De een deed giften of pensioenspaart, de ander niet",
            "Ze wonen in gemeenten met een ander percentage gemeentebelasting",
            "De een heeft een duurdere auto",
        ],
        [0, 1, 2],
        "Kinderen verhogen de belastingvrije som, giften en pensioensparen geven verminderingen, en elke gemeente kiest haar eigen percentage.",
    ),
    tabel(
        "Geeft het een belastingvoordeel in de personenbelasting?",
        [
            ("Een gift van 100 euro aan een erkende instelling, met attest", J),
            ("Een storting op een pensioenspaarrekening", J),
            ("De kosten van erkende opvang voor een kind van drie", J),
            ("De aankoop van een nieuwe smartphone", F),
        ],
        "Giften, pensioensparen en kinderopvang staan in de aangifte. Gewone aankopen niet.",
    ),
    mk(
        "Een belastingplichtige heeft een belastbaar inkomen onder de belastingvrije som. Hoeveel personenbelasting betaalt hij?",
        [
            "Geen, want de vermindering is minstens even groot als de belasting",
            "25 % op zijn hele inkomen, de belastingvrije som telt pas vanaf 15 000 euro",
            "Het vaste minimumbedrag dat iedereen elk jaar betaalt",
            "Het dubbele van de belastingvrije som",
        ],
        0,
        "De vermindering voor de belastingvrije som valt dan even groot uit als de belasting zelf.",
    ),
    keuze(
        "Wie pensioenspaart, krijgt een [[*belastingvermindering|hogere belastingvrije som|lagere btw]] op zijn [[*stortingen|interesten|loon]], tot een maximumbedrag per jaar.",
        "Het voordeel wordt berekend op wat je stort, niet op wat het pensioensparen opbrengt.",
    ),
    open_(
        "Leg uit waarom iemand een aanslagbiljet kan krijgen met geld terug, terwijl hij het hele jaar belasting betaalde.",
        "Tijdens het jaar houdt de werkgever bedrijfsvoorheffing in als voorschot. Als die voorschotten hoger zijn dan de belasting die uiteindelijk berekend wordt, bijvoorbeeld door giften, kinderopvang of pensioensparen, krijg je het verschil terug.",
        "De voorheffing is een schatting. Het aanslagbiljet rekent de echte belasting uit.",
    ),
    casus(
        "Lotte werkt als bediende en heeft één kind van twee jaar. Haar belastbaar inkomen is 30 000 euro. Ze betaalde 1 500 euro voor erkende kinderopvang. Gebruik: schijven tot 15 000 euro aan 25 %, van 15 000 tot 26 000 euro aan 40 %, daarboven 45 %. Belastingvrije som 10 000 euro plus 1 900 euro per kind, verrekend aan 25 %. Kinderopvang: 45 % vermindering.",
        [
            mk(
                "Hoeveel belasting volgens de schijven betaalt Lotte?",
                ["9 950 euro", "13 500 euro", "8 150 euro", "11 250 euro"],
                0,
                "3 750 + 4 400 + 4 000 · 0,45 = 1 800. Samen 9 950 euro.",
            ),
            mk(
                "Hoe groot is de vermindering voor haar belastingvrije som?",
                ["2 975 euro", "2 500 euro", "3 450 euro", "475 euro"],
                0,
                "(10 000 + 1 900) · 0,25 = 2 975 euro.",
            ),
            mk(
                "Hoeveel belasting blijft over na de belastingvrije som en de kinderopvang, zonder gemeentebelasting?",
                ["6 300 euro", "6 975 euro", "7 650 euro", "5 625 euro"],
                0,
                "Kinderopvang: 1 500 · 0,45 = 675 euro. 9 950 − 2 975 − 675 = 6 300 euro.",
            ),
        ],
    ),
]
