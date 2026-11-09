"""Investeringsprojecten beoordelen — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone

CF_KOPPEN = ["Jaar 0", "Jaar 1", "Jaar 2", "Jaar 3", "Jaar 4"]
CF_RIJEN = ["Investering", "Nettowinst", "Afschrijving", "Cashflow", "Gecumuleerde cashflow"]
CF = [
    ["− 80 000", "", "", "", ""],
    ["", "5 000", "10 000", "15 000", "10 000"],
    ["", "20 000", "20 000", "20 000", "20 000"],
    ["", "25 000", "30 000", "35 000", "30 000"],
    ["− 80 000", "− 55 000", "− 25 000", "10 000", "40 000"],
]

PRENTEN = [
    dict(bestand="cashflowtabel.svg", zelf=True,
         wat="Cashflowtabel over vier jaar met investering, nettowinst, afschrijving, cashflow en gecumuleerde cashflow.",
         vragen="klikvraag en rekenvragen over terugverdientijd, ROI en NCW"),
]

VRAGEN = [
    klik(
        "Klik in de cashflowtabel op het vak dat toont in welk jaar de machine terugverdiend is.",
        "cashflowtabel.svg",
        [raster_zone(4, 3, 5, 5)],
        "In jaar 3 wordt de gecumuleerde cashflow voor het eerst positief: daar is de investering terugverdiend.",
    ),
    met_prent("cashflowtabel.svg", mk(
        "Bereken de terugverdientijd van de machine, als de cashflow gelijk gespreid is over het jaar.",
        ["Ongeveer 2,7 jaar", "Ongeveer 3,3 jaar", "Precies 3 jaar", "Ongeveer 2,3 jaar"],
        0,
        "Na 2 jaar is er nog 25 000 euro terug te verdienen. Jaar 3 brengt 35 000 euro: 25/35 = 0,71. Samen ongeveer 2,7 jaar.",
    )),
    met_prent("cashflowtabel.svg", mk(
        "Bereken de ROI van de machine als gemiddelde nettowinst per jaar gedeeld door de investering.",
        ["12,5 %", "50 %", "35,9 %", "10 %"],
        0,
        "Gemiddelde nettowinst (5 000 + 10 000 + 15 000 + 10 000) / 4 = 10 000 euro. 10 000 / 80 000 = 12,5 %.",
    )),
    met_prent("cashflowtabel.svg", mk(
        "De contante waarden van de cashflows aan 10 % zijn 22 727, 24 793, 26 296 en 20 490 euro. Wat is de NCW, en is het project aanvaardbaar?",
        [
            "Ongeveer 14 307 euro: aanvaardbaar",
            "Ongeveer 40 000 euro: aanvaardbaar",
            "Ongeveer − 14 307 euro: niet aanvaardbaar",
            "Ongeveer 94 307 euro: aanvaardbaar",
        ],
        0,
        "Som van de contante waarden 94 307 euro, min de investering van 80 000 euro: ongeveer 14 307 euro. Een positieve NCW betekent dat het project meer opbrengt dan 10 %.",
    )),
    met_prent("cashflowtabel.svg", tabel(
        "Welke uitspraken over de cashflowtabel kloppen?",
        [
            ("De cashflow is de nettowinst plus de afschrijving.", J),
            ("De afschrijving wordt opgeteld, omdat ze een kost is waarvoor geen geld buitengaat.", J),
            ("Zonder rente bekeken brengt de machine over vier jaar 40 000 euro meer op dan ze kost.", J),
            ("De gecumuleerde cashflow van jaar 4 is de NCW.", F),
        ],
        "De gecumuleerde cashflow houdt geen rekening met de tijdswaarde van geld. Voor de NCW verdisconteer je eerst.",
    )),
    met_prent("cashflowtabel.svg", mk(
        "Stel dat de nettowinst in jaar 3 maar 5 000 euro is in plaats van 15 000 euro. Wat wordt de terugverdientijd?",
        ["Precies 3 jaar", "Ongeveer 2,7 jaar", "Ongeveer 3,5 jaar", "Precies 2 jaar"],
        0,
        "De cashflow van jaar 3 wordt 25 000 euro. Na 2 jaar is er nog 25 000 euro terug te verdienen: dat lukt precies op het einde van jaar 3.",
    )),
    tabel(
        "Is de investering materieel, immaterieel of financieel?",
        [
            ("Een nieuw magazijn", "Materieel"),
            ("Een licentie op boekhoudsoftware", "Immaterieel"),
            ("Aandelen in een leverancier", "Financieel"),
            ("Een octrooi op een uitvinding", "Immaterieel"),
        ],
        "Materieel kan je aanraken, immaterieel is een recht of kennis, financieel is een deelname in een andere onderneming.",
        kolommen=["Materieel", "Immaterieel", "Financieel"],
    ),
    mk(
        "Nettowinst 18 000 euro, afschrijvingen 12 000 euro. Hoeveel is de cashflow?",
        ["30 000 euro", "6 000 euro", "18 000 euro", "12 000 euro"],
        0,
        "Cashflow = nettowinst + afschrijvingen = 30 000 euro.",
    ),
    mk(
        "Een project heeft een jaarlijkse cashflow van 24 000 euro en een terugverdientijd van precies 4 jaar. Hoe groot was de investering?",
        ["96 000 euro", "6 000 euro", "28 000 euro", "120 000 euro"],
        0,
        "Bij een gelijke cashflow: investering = cashflow · terugverdientijd = 24 000 · 4 = 96 000 euro.",
    ),
    mk(
        "Project A: investering 50 000 euro, cashflow 25 000 euro per jaar gedurende 2 jaar. Project B: investering 50 000 euro, cashflow 20 000 euro per jaar gedurende 5 jaar. Welk project kies je met enkel de terugverdientijd, en wat zie je dan over het hoofd?",
        [
            "A, maar B brengt na de terugverdientijd nog veel meer op",
            "B, maar A heeft een kortere terugverdientijd",
            "A, en er wordt niets over het hoofd gezien",
            "B, omdat de cashflow per jaar kleiner is",
        ],
        0,
        "A is na 2 jaar terugverdiend, B na 2,5 jaar. Maar A brengt daarna niets meer op, B nog jaren. De terugverdientijd negeert alles daarna.",
    ),
    mk(
        "Een cashflow van 12 100 euro komt binnen over 2 jaar. De rente is 10 %. Hoeveel is die cashflow vandaag waard?",
        ["10 000 euro", "11 000 euro", "9 680 euro", "14 641 euro"],
        0,
        "12 100 / 1,10² = 12 100 / 1,21 = 10 000 euro.",
    ),
    tabel(
        "Welke soort investering is het?",
        [
            ("Een bakker koopt een tweede oven om meer brood te bakken", "Uitbreiding"),
            ("Een versleten heftruck wordt vervangen door een gelijkaardige", "Vervanging"),
            ("Een magazijn koopt een robot die het werk goedkoper maakt", "Rationalisatie"),
            ("Een fabriek koopt een extra productielijn voor een nieuwe markt", "Uitbreiding"),
        ],
        "Uitbreiding verhoogt de capaciteit, vervanging houdt ze gelijk, rationalisatie verlaagt de kosten.",
        kolommen=["Vervanging", "Uitbreiding", "Rationalisatie"],
    ),
    keuze(
        "Een project is volgens de NCW aanvaardbaar als de NCW [[*positief|negatief|kleiner dan de investering]] is. Bij een hogere rentevoet wordt de NCW [[*kleiner|groter|negatief]].",
        "Een hogere rente maakt toekomstige euro's vandaag minder waard.",
    ),
    tabel(
        "Waar of niet waar over de beoordelingsmethoden?",
        [
            ("De terugverdientijd houdt geen rekening met cashflows na het terugverdienen.", J),
            ("De NCW houdt rekening met de tijdswaarde van geld.", J),
            ("Een project met de kortste terugverdientijd heeft altijd de hoogste NCW.", F),
            ("Bij een hogere ROI is het project rendabeler, als de rest gelijk is.", J),
        ],
        "Elke methode bekijkt een ander aspect. Daarom gebruik je ze samen.",
    ),
    sorteer(
        "Hoort het bij de berekening van de cashflow, of niet?",
        ["Telt mee", "Telt niet mee"],
        [
            ["De nettowinst van het jaar", "Telt mee"],
            ["De afschrijving van het jaar", "Telt mee"],
            ["De btw op de aankoop van de machine", "Telt niet mee"],
            ["Het dividend dat de aandeelhouders vragen", "Telt niet mee"],
        ],
        "Cashflow = nettowinst + afschrijvingen. Btw is terug te vorderen en dividend is een verdeling van de winst.",
    ),
    inv(
        "Investering 75 000 euro, jaarlijkse cashflow 30 000 euro. Hoeveel jaar is de terugverdientijd? Schrijf het getal met een komma.",
        "2,5",
        "75 000 / 30 000 = 2,5 jaar.",
    ),
    mk(
        "Twee projecten hebben elk een NCW van 5 000 euro. Project A vraagt 20 000 euro investering, project B 200 000 euro. Welke vergelijking helpt om te kiezen?",
        [
            "De ROI of het rendement per geïnvesteerde euro",
            "Enkel de NCW, want die is gelijk",
            "Enkel de investering: kies altijd de grootste",
            "De afschrijving van het eerste jaar",
        ],
        0,
        "Met dezelfde NCW levert A veel meer op per geïnvesteerde euro.",
    ),
    koppel(
        "Welke vraag beantwoordt elke methode?",
        [
            ["Hoe snel heb ik mijn geld terug?", "Terugverdientijd"],
            ["Hoeveel winst levert elke geïnvesteerde euro gemiddeld op?", "ROI"],
            ["Hoeveel meer is het project vandaag waard dan het kost?", "NCW"],
        ],
        ["Current ratio"],
        "Drie methoden, drie invalshoeken op hetzelfde project.",
    ),
    volgorde(
        "Zet de stappen om de NCW te berekenen in de juiste volgorde.",
        [
            "De cashflow van elk jaar berekenen",
            "Elke cashflow verdisconteren naar vandaag",
            "De contante waarden optellen",
            "De investering ervan aftrekken",
        ],
        "Eerst de cashflows, dan terugrekenen naar vandaag, optellen en de investering eraf.",
    ),
    mk(
        "Een machine van 40 000 euro geeft 5 jaar lang 10 000 euro cashflow. Zonder rente lijkt ze 10 000 euro op te brengen. Bij 10 % rente is de NCW ongeveer − 2 092 euro. Wat besluit je?",
        [
            "Het project brengt minder op dan 10 % en is niet aanvaardbaar",
            "Het project is aanvaardbaar, want het brengt 10 000 euro op",
            "De berekening is fout, want een NCW kan niet negatief zijn",
            "Het project is aanvaardbaar, want de terugverdientijd is korter dan 5 jaar",
        ],
        0,
        "Een negatieve NCW betekent dat het geld elders aan 10 % meer zou opbrengen.",
    ),
    sleep(
        "De [[netto contante waarde]] rekent alle toekomstige cashflows terug naar vandaag met een [[rentevoet]]. Daarna trek je de [[investering]] af.",
        ["terugverdientijd", "afschrijving"],
        "Een euro vandaag is meer waard dan een euro later, omdat je hem kan beleggen.",
    ),
    mk(
        "Waarom tel je de afschrijving op bij de nettowinst om de cashflow te vinden?",
        [
            "Ze verlaagde de winst, maar er ging geen geld voor buiten",
            "Afschrijvingen zijn een opbrengst",
            "De fiscus betaalt de afschrijving terug",
            "Zo wordt de winst mooier voor de aandeelhouders",
        ],
        0,
        "De machine werd al betaald bij de aankoop. De afschrijving spreidt die kost op papier, zonder nieuwe uitgave.",
    ),
    tabel(
        "Wat gebeurt er met de NCW?",
        [
            ("De rentevoet stijgt van 6 % naar 9 %", "Daalt"),
            ("De cashflows van elk jaar worden hoger", "Stijgt"),
            ("De investering wordt duurder", "Daalt"),
            ("Dezelfde cashflows komen een jaar vroeger binnen", "Stijgt"),
        ],
        "Hogere en vroegere cashflows maken de NCW groter, een hogere rente en een duurdere investering kleiner.",
        kolommen=["Stijgt", "Daalt"],
    ),
    inv(
        "Investering 120 000 euro, gemiddelde jaarlijkse nettowinst 18 000 euro. Hoeveel procent is de ROI, berekend op de investering? Schrijf enkel het getal.",
        "15",
        "18 000 / 120 000 · 100 = 15 %.",
    ),
    mk(
        "Investering 100 000 euro. Cashflows: jaar 1 30 000, jaar 2 30 000, jaar 3 50 000, jaar 4 20 000 euro. Wat is de terugverdientijd?",
        ["2,8 jaar", "3,2 jaar", "3 jaar", "2,5 jaar"],
        0,
        "Na 2 jaar is 60 000 euro terug. Er blijft 40 000 euro, en jaar 3 brengt 50 000 euro: 40/50 = 0,8. Samen 2,8 jaar.",
    ),
    open_(
        "Leg uit waarom een onderneming een project met een positieve gecumuleerde cashflow toch kan afwijzen.",
        "De gecumuleerde cashflow telt euro's van verschillende jaren gewoon op. Een euro later is minder waard dan een euro vandaag, omdat je het geld intussen kan beleggen. Als de NCW bij de gevraagde rentevoet negatief is, brengt het project minder op dan een andere belegging.",
        "De tijdswaarde van geld maakt het verschil.",
    ),
    mk(
        "Een onderneming kiest tussen een machine die 6 jaar meegaat en een die 3 jaar meegaat, met dezelfde jaarlijkse cashflow. Wat is een zwakte van de terugverdientijd bij deze keuze?",
        [
            "Ze kan dezelfde terugverdientijd geven, terwijl de eerste machine veel langer opbrengt",
            "Ze houdt te veel rekening met de rentevoet",
            "Ze kan enkel berekend worden voor machines van 5 jaar",
            "Ze geeft altijd de voorkeur aan de duurste machine",
        ],
        0,
        "De terugverdientijd kijkt niet verder dan het moment van terugverdienen.",
    ),
    casus(
        "Drukkerij Blad overweegt een printer van 60 000 euro die 3 jaar meegaat zonder restwaarde. Verwachte nettowinst per jaar: 8 000, 12 000 en 10 000 euro. De rentevoet is 8 %.",
        [
            mk(
                "Wat zijn de cashflows van jaar 1, 2 en 3?",
                [
                    "28 000, 32 000 en 30 000 euro",
                    "8 000, 12 000 en 10 000 euro",
                    "20 000, 20 000 en 20 000 euro",
                    "− 12 000, − 8 000 en − 10 000 euro",
                ],
                0,
                "Afschrijving 60 000 / 3 = 20 000 euro per jaar, opgeteld bij de nettowinst.",
            ),
            mk(
                "Na hoeveel jaar heeft Blad de printer terugverdiend?",
                ["2 jaar", "2,5 jaar", "3 jaar", "1,9 jaar"],
                0,
                "Na jaar 1: − 32 000. Na jaar 2: 0. Precies na 2 jaar is de printer terugverdiend.",
            ),
            mk(
                "De contante waarden aan 8 % zijn ongeveer 25 926, 27 435 en 23 815 euro. Wat is de NCW?",
                ["Ongeveer 17 176 euro", "Ongeveer 30 000 euro", "Ongeveer 77 176 euro", "Ongeveer − 17 176 euro"],
                0,
                "25 926 + 27 435 + 23 815 = 77 176 euro. Min 60 000 euro: ongeveer 17 176 euro.",
            ),
        ],
    ),
]
