"""De eigenheid van de filosofie — pittig (🌍 Beyond, filosofie en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus

VRAGEN = [
    sorteer(
        "Sleep elke vraag naar de wetenschap die ze onderzoekt.",
        ["Natuurwetenschappen", "Menswetenschappen", "Filosofie"],
        [
            ("Hoe snel valt een steen van een toren?", "Natuurwetenschappen"),
            ("Hoe reageren cellen op een nieuw medicijn?", "Natuurwetenschappen"),
            ("Hoeveel jongeren voelen zich eenzaam?", "Menswetenschappen"),
            ("Hoe gedragen mensen zich in een grote groep?", "Menswetenschappen"),
            ("Wat bedoelen we eigenlijk met eenzaamheid?", "Filosofie"),
            ("Mag een groep een enkeling iets opleggen?", "Filosofie"),
        ],
        "Natuurwetenschappen onderzoeken de natuur, menswetenschappen meten hoe mensen leven en zich gedragen. De filosofie onderzoekt het begrip zelf of vraagt wat zou moeten, en dat kan geen meting beslechten.",
    ),
    tabel(
        "Geldt dit voor de natuurwetenschappen, voor de menswetenschappen of voor beide?",
        [
            ("Ze werken met een methode en met gegevens.", "Beide"),
            ("Hun onderwerp weet dat het onderzocht wordt en past zich aan.", "Menswetenschappen"),
            ("Een zuiver experiment in een labo lukt er meestal goed.", "Natuurwetenschappen"),
            ("Ze laten hun uitspraken door anderen nakijken.", "Beide"),
        ],
        "Beide zijn wetenschappen met een methode en met gegevens. Het verschil zit in het onderwerp: een mens denkt mee en past zich aan, een steen niet.",
        kolommen=["Natuurwetenschappen", "Menswetenschappen", "Beide"],
    ),
    keuze(
        "Een psycholoog meet met een vragenlijst hoe gelukkig jongeren zijn. Hij werkt dan zoals de [[filosofie|*menswetenschappen|natuurwetenschappen]]. Een filosoof vraagt wat geluk eigenlijk is en werkt daarvoor met [[metingen|*argumenten|experimenten]].",
        "De psycholoog verzamelt gegevens: dat is menswetenschap. De filosoof onderzoekt het begrip zelf, met argumenten en redeneringen.",
    ),
    casus(
        "Een school wil weten of een gsm-verbod op de speelplaats goed is. Drie mensen buigen zich erover.\n"
        "Amira telt hoe vaak leerlingen op de speelplaats met elkaar praten, voor en na het verbod.\n"
        "Jonas onderzoekt met een hersenscan wat er in het brein gebeurt bij een melding op de gsm.\n"
        "Lotte vraagt of een school het vrije gebruik van een gsm wel mag verbieden, en wat vrijheid hier betekent.",
        [
            mk("Wie werkt als filosoof?", ["Jonas", "Amira", "Lotte", "Geen van de drie"], 2,
               "Lotte onderzoekt een begrip (vrijheid) en een vraag naar wat mag. Daar helpt geen meting bij."),
            mk("Welke twee werken met gegevens die ze verzamelen?", ["Amira en Lotte", "Amira en Jonas", "Jonas en Lotte", "Alle drie, ieder op zijn manier"], 1,
               "Amira telt gesprekken en Jonas meet het brein. Lotte redeneert."),
            mk("Waarom kan Amira's onderzoek alleen Lottes vraag niet beslechten?",
               ["Een telling zegt hoe het is, niet of een verbod mag of rechtvaardig is",
                "Een telling op één speelplaats is altijd te klein om iets te besluiten",
                "Amira werkt niet volgens een methode, dus haar cijfers tellen gewoon niet mee",
                "Lottes vraag gaat eigenlijk over het brein en helemaal niet over gedrag"], 0,
               "Gegevens beschrijven wat het geval is. Of iets mag, is een vraag naar wat zou moeten gelden: dat vraagt argumenten."),
        ],
    ),
    mk(
        "Welke uitspraken over de eigenheid van de filosofie kloppen?",
        [
            "Ze onderzoekt de begrippen die andere wetenschappen gewoon gebruiken.",
            "Ze heeft een eigen labo nodig om haar uitspraken na te gaan.",
            "Ze vraagt ook naar wat zou moeten, niet enkel naar wat is.",
            "Ze stopt zodra een wetenschap een antwoord gevonden heeft.",
            "Ze toetst redeneringen op hun geldigheid.",
        ],
        [0, 2, 4],
        "De filosofie onderzoekt begrippen, vraagt naar wat zou moeten en kijkt redeneringen na. Ze heeft geen labo nodig en stopt niet waar een wetenschap een antwoord geeft.",
    ),
    mk(
        "Een bioloog zegt: \"Mensen zijn ook maar dieren.\" Wanneer wordt dat een filosofische kwestie?",
        ["Wanneer je vraagt wat het woord 'maar' hier beweert over de waarde van een mens",
         "Wanneer je telt hoeveel genen een mens deelt met een chimpansee",
         "Wanneer je nagaat in welk jaar en door welke bioloog die uitspraak voor het eerst gedaan is",
         "Wanneer een andere bioloog het in een labo nameet"],
        0,
        "Hoeveel genen we delen, is biologie. Of dat iets zegt over wat een mens waard is, is een vraag naar een begrip en een veronderstelling: filosofie.",
    ),
    sleep(
        "Filosofische [[verwondering]] vertrekt niet van iets zeldzaams maar van het [[alledaagse]]. Ze is [[noodzakelijk]], want zonder verwondering komt er geen [[vraag]].",
        ["spectaculaire", "toevallig", "antwoord"],
        "Verwondering maakt het gewone weer vreemd. Ze is noodzakelijk omdat elke filosofische vraag daar begint.",
    ),
    tabel(
        "Wijst deze vraag op filosofische verwondering?",
        [
            ("Waarom is er eigenlijk iets en niet niets?", J),
            ("Hoe laat gaat de zon morgen onder?", F),
            ("Ben ik nog dezelfde persoon als toen ik vijf was?", J),
            ("Welke trein is de snelste naar Gent?", F),
        ],
        "Verwondering maakt iets vanzelfsprekends tot een vraag die geen opzoeking beslecht. Een uur of een treinverbinding zoek je gewoon op.",
        kolommen=["Ja", "Nee"],
    ),
    mk(
        "Iemand zegt: \"Ik verwonder me over de nieuwste gsm, die kan echt alles.\" Waarom is dat geen filosofische verwondering?",
        ["Het is verbazing over iets nieuws, niet het vreemd gaan vinden van iets gewoons",
         "Een gsm is een toestel, en over toestellen mag een filosoof eigenlijk helemaal niets zeggen",
         "Filosofische verwondering gaat enkel over goden en over de natuur",
         "Wie zich verbaast, heeft nooit een vraag en dus ook geen filosofie"],
        0,
        "Filosofische verwondering is je verbazen over wat zo gewoon is dat niemand er nog bij stilstaat. Verbaasd zijn over iets nieuws is iets anders.",
    ),
    casus(
        "Bron: drie verklaringen voor onweer.\n"
        "A. De oppergod is kwaad op de mensen en slingert zijn bliksem naar de aarde.\n"
        "B. Onweer ontstaat doordat warme en koude lucht tegen elkaar botsen; zo leert ons het nadenken over wat we in de natuur zelf zien.\n"
        "C. Metingen in wolken tonen dat elektrische lading zich opbouwt tot er een ontlading volgt.",
        [
            koppel("Koppel elke verklaring aan het denken waar ze bij hoort.",
                   [("Verklaring A", "mythologie"), ("Verklaring B", "natuurfilosofie"), ("Verklaring C", "wetenschap met metingen")],
                   ["filosofische verwondering"],
                   "A zoekt de oorzaak bij een god, B zoekt ze in de natuur zelf met een redenering, C steunt op metingen."),
            mk("Wat maakt verklaring B een stap vooruit tegenover A?",
               ["Ze is juist, terwijl verklaring A gewoon helemaal fout is", "Je kan erover redetwisten en ze verbeteren",
                "Ze is nauwkeurig gemeten in een labo", "Ze is korter en daarom ook beter"], 1,
               "Het beslissende is niet of ze klopt, maar dat ze een argument is dat je kan tegenspreken en verbeteren."),
            mk("Wat heeft verklaring B nog níet dat verklaring C wel heeft?",
               ["Een oorzaak in de natuur zelf", "Een redenering", "Gegevens uit metingen", "Een verhaal over goden"], 2,
               "Natuurfilosofie redeneert over de natuur; de latere wetenschap toetst met metingen."),
        ],
    ),
    volgorde(
        "Zet deze manieren om de wereld te verklaren in de volgorde waarin ze in het Westen ontstaan zijn.",
        ["Verhalen over goden en helden", "Redeneren over oorzaken in de natuur zelf", "Toetsen met metingen en experimenten"],
        "Eerst de mythologie, dan de natuurfilosofie (het begin van de westerse filosofie), en daaruit groeide later de wetenschap.",
    ),
    tabel(
        "Klopt deze uitspraak over de oorsprong van de westerse filosofie?",
        [
            ("Ze begint wanneer verklaringen met argumenten verdedigd en betwist worden.", J),
            ("Ze begint wanneer de eerste metingen in een labo gebeuren.", F),
            ("Natuurfilosofen zochten de oorzaak in de natuur zelf.", J),
            ("Een mythe kan je net als een argument tegenspreken en verbeteren.", F),
        ],
        "De westerse filosofie begint bij de stap van verhaal naar argument. Een mythe vraagt geen argument, en het labo komt pas veel later.",
        kolommen=["Juist", "Fout"],
    ),
    sorteer(
        "Is dit een filosofische vraag of niet?",
        ["Filosofisch", "Niet filosofisch"],
        [
            ("Mag je liegen om een vriend te beschermen?", "Filosofisch"),
            ("Kan een computer ooit echt begrijpen wat hij zegt?", "Filosofisch"),
            ("Wanneer weet je iets zeker?", "Filosofisch"),
            ("Hoeveel mensen wonen er in Hasselt?", "Niet filosofisch"),
            ("Welke partij won de laatste verkiezingen?", "Niet filosofisch"),
            ("Hoeveel uur slaapt een tiener gemiddeld?", "Niet filosofisch"),
        ],
        "Een filosofische vraag raakt aan begrippen of aan wat zou moeten, en geen meting of opzoeking beslecht ze. De andere drie zoek je op of meet je.",
    ),
    mk(
        "\"Niemand weet hoeveel zandkorrels er op het strand van Oostende liggen. Dus is dat een filosofische vraag.\" Wat is er mis met die redenering?",
        ["Niets: een vraag zonder bekend antwoord is altijd filosofisch",
         "Een filosofische vraag heeft altijd één vast antwoord dat iedereen moet aanvaarden",
         "Het aantal is in principe te tellen; een meting kan de vraag beslechten",
         "Over zand mag een filosoof geen vragen stellen"],
        2,
        "Dat niemand het antwoord kent, maakt een vraag niet filosofisch. Het gaat erom of een meting of opzoeking ze in principe kan beslechten.",
    ),
    keuze(
        "Een filosofische vraag kan je [[*niet|wel]] beslechten met een meting. Er bestaan [[*wel|geen]] betere en slechtere antwoorden op, want je kan de [[*argumenten|metingen|stemmen]] wegen.",
        "Geen meting beslecht een filosofische vraag, maar dat maakt elk antwoord niet even goed: argumenten kan je wegen.",
    ),
    casus(
        "In de klas zegt Mats: \"Over filosofische vragen valt niets te zeggen. Iedereen heeft gewoon zijn mening en die is even goed als die van een ander.\"\n"
        "Fien antwoordt: \"Je zegt nu zelf dat jouw mening klopt. Dan geef je toch een argument?\"",
        [
            mk("Welk misverstand over filosofische vragen heeft Mats?",
               ["Dat ze eigenlijk altijd met een meting te beslechten zijn", "Dat er geen betere en slechtere argumenten zijn",
                "Dat ze altijd over het verleden gaan", "Dat ze maar één antwoord hebben"], 1,
               "Dat er geen meting is, wil niet zeggen dat alle antwoorden even goed zijn. Argumenten kan je wegen."),
            mk("Wat toont Fien met haar antwoord?",
               ["Dat Mats zich niet verwondert", "Dat Mats zelf al een argument verdedigt en dus wel iets beweert",
                "Dat filosofie eigenlijk uit de oude mythen voortkomt", "Dat Mats een natuurwetenschapper is en geen filosoof"], 1,
               "Mats geeft zelf een stelling met een reden. Daarmee doet hij wat hij onmogelijk noemt."),
        ],
    ),
    koppel(
        "Koppel elke vraag aan het filosofische domein waar ze thuishoort.",
        [
            ("Is een mens meer dan zijn lichaam?", "wijsgerige antropologie"),
            ("Mag je een belofte breken als dat iemand helpt?", "ethiek"),
            ("Komt kennis uit de rede of uit de zintuigen?", "kennisleer"),
            ("Volgt het besluit echt uit de premissen?", "logica"),
            ("Wanneer mag een theorie wetenschappelijk heten?", "wetenschapsfilosofie"),
        ],
        ["mythologie"],
        "Wijsgerige antropologie vraagt wat de mens is, ethiek wat goed handelen is, kennisleer waar kennis vandaan komt, logica wanneer een redenering geldig is, en wetenschapsfilosofie wat wetenschap is.",
    ),
    mk(
        "Bij welk domein hoort het denken over vrijheid en determinisme?",
        ["De logica", "De wijsgerige antropologie", "De kennisleer", "De wetenschapsfilosofie"],
        1,
        "Of de mens vrij is, is een vraag over wat een mens is: wijsgerige antropologie, net als lichaam en geest en mens en dier.",
    ),
    mk(
        "Bij welk domein horen het rationalisme en het empirisme?",
        ["De ethiek", "De logica", "De wijsgerige antropologie", "De kennisleer"],
        3,
        "Rationalisme en empirisme geven twee antwoorden op de vraag waar kennis vandaan komt: kennisleer.",
    ),
    tabel(
        "Juist of fout over de filosofische domeinen?",
        [
            ("Een domein bundelt vragen over hetzelfde soort onderwerp.", J),
            ("Falsificatie hoort bij de wetenschapsfilosofie.", J),
            ("Gevolgenethiek hoort bij de logica.", F),
            ("Lichaam en geest is een vraag van de kennisleer.", F),
        ],
        "Een domein bundelt samenhangende vragen. Falsificatie is wetenschapsfilosofie; gevolgenethiek is ethiek; lichaam en geest is wijsgerige antropologie.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Bron: uit een krant. \"Een nieuwe studie toont dat 62 procent van de jongeren vindt dat dieren dezelfde rechten moeten krijgen als mensen. Een hersenonderzoek toont daarnaast dat honden pijn voelen op een manier die op de onze lijkt.\"",
        [
            mk("Welk soort onderzoek is het cijfer van 62 procent?",
               ["Natuurwetenschap", "Menswetenschap", "Filosofie", "Mythologie"], 1,
               "Een bevraging van wat mensen vinden, is menswetenschap."),
            mk("Welk soort onderzoek is het hersenonderzoek bij honden?",
               ["Natuurwetenschap", "Menswetenschap", "Filosofie", "Logica en argumentatieleer"], 0,
               "Het meet een verschijnsel in de natuur: natuurwetenschap."),
            mk("Welke vraag blijft over voor de filosofie?",
               ["Hoeveel jongeren zijn het daar precies mee eens, per leeftijd en per provincie?", "Hoe werkt het brein van een hond?",
                "Volgt uit 'een dier voelt pijn' dat het dezelfde rechten verdient?", "In welke krant stond het artikel?"], 2,
               "Of je van een feit (pijn voelen) naar een oordeel (rechten) mag gaan, beslecht geen enkele meting."),
            mk("Bij welk domein hoort die laatste vraag vooral?",
               ["De ethiek", "De kennisleer", "De logica", "De wetenschapsfilosofie"], 0,
               "Wat we dieren verschuldigd zijn, is een vraag naar goed handelen: ethiek."),
        ],
    ),
    inv(
        "Een vraag naar wat zou moeten gelden, en niet naar wat het geval is, kan je nooit beslechten met een ... (één woord)",
        ["meting", "meting.", "experiment", "opzoeking"],
        "Wat zou moeten, valt niet te meten. Daarvoor heb je argumenten nodig.",
    ),
]
