"""De vennootschapsbelasting en de voorafbetalingen — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import va_zone

PRENTEN = [
    dict(bestand="voorafbetalingen.svg", zelf=True,
         wat="Tijdlijn van een boekjaar met de vier vervaldagen van de voorafbetalingen.",
         vragen="klikvraag en meerkeuze over de voorafbetalingen"),
]

KLEIN = "Gegeven: 20 % op de eerste 100 000 euro winst, 25 % op de rest."
VA = "Gegeven: vermeerdering 9 % van de belasting. Voordeel per voorafbetaling: VA1 12 %, VA2 10 %, VA3 8 %, VA4 6 %."

VRAGEN = [
    mk(
        "Een kleine vennootschap heeft een belastbare winst van 180 000 euro. " + KLEIN + " Hoeveel vennootschapsbelasting betaalt ze?",
        ["40 000 euro", "45 000 euro", "36 000 euro", "38 000 euro"],
        0,
        "100 000 · 0,20 = 20 000 en 80 000 · 0,25 = 20 000. Samen 40 000 euro.",
    ),
    mk(
        "Een kleine vennootschap betaalt 32 500 euro vennootschapsbelasting. " + KLEIN + " Hoeveel belastbare winst had ze?",
        ["150 000 euro", "130 000 euro", "162 500 euro", "125 000 euro"],
        0,
        "De eerste 100 000 euro geeft 20 000 euro. De rest, 12 500 euro, komt van 12 500 / 0,25 = 50 000 euro winst. Samen 150 000 euro.",
    ),
    mk(
        "Een ondernemer maakt 80 000 euro winst. Als eenmanszaak: schijven tot 15 000 euro aan 25 %, tot 26 000 aan 40 %, tot 45 000 aan 45 %, daarboven 50 % (zonder belastingvrije som). Als kleine bv: 20 %. Hoeveel belasting spaart de bv uit?",
        ["18 200 euro", "24 000 euro", "16 000 euro", "34 200 euro"],
        0,
        "Eenmanszaak: 3 750 + 4 400 + 8 550 + 35 000 · 0,50 = 17 500, samen 34 200 euro. Bv: 80 000 · 0,20 = 16 000 euro. Verschil 18 200 euro.",
    ),
    tabel(
        "Geldt het voor de eenmanszaak of voor de vennootschap?",
        [
            ("De winst valt samen met de andere inkomens van de ondernemer", "Eenmanszaak"),
            ("Het tarief stijgt in schijven tot 50 %", "Eenmanszaak"),
            ("Een vast tarief, met een verlaagd tarief voor kleine ondernemingen", "Vennootschap"),
            ("Voorafbetalingen kunnen een bonificatie opleveren", "Eenmanszaak"),
        ],
        "De eenmanszaak zit in de personenbelasting: progressief, samen met andere inkomens, en met bonificatie. De vennootschap betaalt een vlak tarief.",
        kolommen=["Eenmanszaak", "Vennootschap"],
    ),
    mk(
        "De vennootschapsbelasting is 50 000 euro. " + VA + " De vennootschap stortte VA1 20 000 euro en VA3 10 000 euro. Hoeveel vermeerdering blijft over?",
        ["1 300 euro", "4 500 euro", "3 200 euro", "2 100 euro"],
        0,
        "Vermeerdering 50 000 · 0,09 = 4 500 euro. Voordeel: 20 000 · 0,12 = 2 400 en 10 000 · 0,08 = 800. 4 500 − 3 200 = 1 300 euro.",
    ),
    mk(
        "De vennootschapsbelasting wordt 30 000 euro. " + VA + " Hoeveel moet de vennootschap minstens storten bij VA1 om helemaal geen vermeerdering te krijgen?",
        ["22 500 euro", "30 000 euro", "2 700 euro", "27 000 euro"],
        0,
        "De vermeerdering is 30 000 · 0,09 = 2 700 euro. Met 12 % voordeel heb je 2 700 / 0,12 = 22 500 euro nodig.",
    ),
    mk(
        VA + " Een vennootschap twijfelt: 10 000 euro storten bij VA2 of bij VA4. Hoeveel meer vermeerdering valt weg als ze VA2 kiest?",
        ["400 euro", "1 000 euro", "600 euro", "40 euro"],
        0,
        "VA2: 10 000 · 0,10 = 1 000 euro. VA4: 10 000 · 0,06 = 600 euro. Verschil 400 euro.",
    ),
    tabel(
        "Waar of niet waar over het boekjaar en het aanslagjaar van een vennootschap?",
        [
            ("Het boekjaar hoeft niet samen te vallen met het kalenderjaar.", J),
            ("Een boekjaar van 1 januari tot 31 december 2026 hoort bij aanslagjaar 2027.", J),
            ("De voorafbetalingen gebeuren pas in het aanslagjaar.", F),
        ],
        "Voorafbetalingen doe je tijdens het boekjaar zelf. Het aanslagjaar volgt daarna.",
    ),
    volgorde(
        "Zet de stappen van de vennootschapsbelasting in de juiste volgorde.",
        [
            "Tijdens het boekjaar voorafbetalingen storten",
            "Het boekjaar afsluiten",
            "De aangifte indienen",
            "Het aanslagbiljet ontvangen",
            "Het saldo betalen of terugkrijgen",
        ],
        "De voorafbetalingen vallen tijdens het boekjaar, de rest volgt na de afsluiting.",
    ),
    klik(
        "Klik op de voorafbetaling die bij hetzelfde bedrag de grootste vermeerdering wegneemt.",
        "voorafbetalingen.svg",
        [va_zone(0)],
        "VA1, op 10 april. Hoe vroeger je betaalt, hoe langer de staat het geld al heeft, en hoe groter het voordeel.",
    ),
    met_prent("voorafbetalingen.svg", mk(
        VA + " Een vennootschap met een boekjaar gelijk aan het kalenderjaar stort 10 000 euro op 15 november. Hoeveel vermeerdering valt daardoor weg?",
        ["600 euro", "800 euro", "1 000 euro", "1 200 euro"],
        0,
        "Na 10 oktober en vóór 20 december telt een storting als VA4: 10 000 · 0,06 = 600 euro.",
    )),
    met_prent("voorafbetalingen.svg", tabel(
        "Een vennootschap met een boekjaar gelijk aan het kalenderjaar stort op deze dagen. Als welke voorafbetaling telt elke storting?",
        [
            ("2 maart", "VA1"),
            ("25 mei", "VA2"),
            ("1 september", "VA3"),
            ("15 december", "VA4"),
        ],
        "Een storting telt voor de eerstvolgende vervaldag: tot 10 april VA1, tot 10 juli VA2, tot 10 oktober VA3 en tot 20 december VA4.",
        kolommen=["VA1", "VA2", "VA3", "VA4"],
    )),
    keuze(
        "Wie te weinig voorafbetalingen doet, krijgt een [[*vermeerdering|bonificatie|aftrek]]. Een zelfstandige met een eenmanszaak die genoeg vooraf betaalt, kan bovendien een [[*bonificatie|vermeerdering|boete]] krijgen.",
        "In de vennootschapsbelasting daalt de vermeerdering hoogstens tot nul. Een bonificatie bestaat enkel in de personenbelasting.",
    ),
    sleep(
        "Een vennootschap betaalt belasting op haar [[belastbare winst]]. Kleine vennootschappen krijgen een [[verlaagd tarief]] op de eerste 100 000 euro. De belasting wordt verrekend met de [[voorafbetalingen]].",
        ["omzet", "personenbelasting", "brutoloon"],
        "Niet de omzet, maar de winst na kosten is de grondslag.",
    ),
    tabel(
        "Krijgt de vennootschap een vermeerdering als ze niets vooraf betaalt?",
        [
            ("Een kleine bv in haar tweede boekjaar", F),
            ("Een grote nv die al tien jaar bestaat", J),
            ("Een kleine cv in haar vijfde boekjaar", J),
        ],
        "Kleine vennootschappen zijn de eerste drie boekjaren vrijgesteld van de vermeerdering. Daarna niet meer.",
    ),
    inv(
        "Een grote vennootschap heeft een belastbare winst van 64 000 euro. Het tarief is 25 %. Hoeveel euro vennootschapsbelasting betaalt ze? Schrijf enkel het getal.",
        "16000",
        "64 000 · 0,25 = 16 000 euro.",
    ),
    mk(
        "Een vennootschap deed 40 000 euro voorafbetalingen. De belasting blijkt maar 30 000 euro te zijn. Wat gebeurt er?",
        [
            "Ze krijgt het verschil van 10 000 euro terug",
            "Ze verliest de 10 000 euro te veel, als boete",
            "Ze moet de 10 000 euro als schuld boeken",
            "De 10 000 euro gaat automatisch naar de personenbelasting van de zaakvoerder",
        ],
        0,
        "Voorafbetalingen zijn voorschotten. Wat te veel betaald is, krijgt de vennootschap terug na de berekening.",
    ),
    tabel(
        "Waar of niet waar over de bonificatie?",
        [
            ("Een bonificatie is een voordeel en geen boete.", J),
            ("Een vennootschap kan een bonificatie krijgen bovenop het wegvallen van de vermeerdering.", F),
            ("Een zelfstandige in de personenbelasting kan een bonificatie krijgen.", J),
        ],
        "De bonificatie hoort bij de personenbelasting van zelfstandigen. Bij een vennootschap valt hoogstens de vermeerdering weg.",
    ),
    koppel(
        "Welke vervaldag hoort bij elke voorafbetaling, voor een boekjaar gelijk aan het kalenderjaar?",
        [
            ["VA1", "10 april"],
            ["VA2", "10 juli"],
            ["VA3", "10 oktober"],
            ["VA4", "20 december"],
        ],
        ["31 januari"],
        "De vier vervaldagen liggen telkens in het boekjaar zelf.",
    ),
    mk(
        "Waarom telt een voorafbetaling in april zwaarder dan een in december?",
        [
            "De staat heeft het geld dan langer ter beschikking",
            "In december zijn de banken gesloten voor belastingen",
            "Een betaling in december telt pas mee voor het volgende aanslagjaar",
            "In april is de belasting nog niet gekend, dus het is een gok",
        ],
        0,
        "Wie vroeger betaalt, geeft de staat langer het geld. Daarom is het voordeel van VA1 het grootst.",
    ),
    sorteer(
        "Hoort het bij de personenbelasting of bij de vennootschapsbelasting?",
        ["Personenbelasting", "Vennootschapsbelasting"],
        [
            ["Belastingvrije som", "Personenbelasting"],
            ["Verlaagd tarief van 20 % voor kleine ondernemingen", "Vennootschapsbelasting"],
            ["Bonificatie voor voorafbetalingen", "Personenbelasting"],
            ["Boekjaar dat niet gelijk loopt met het kalenderjaar", "Vennootschapsbelasting"],
            ["Progressieve schijven", "Personenbelasting"],
        ],
        "Een belastingvrije som en schijven bestaan enkel voor natuurlijke personen. Een eigen boekjaar en het verlaagd tarief horen bij de vennootschap.",
    ),
    mk(
        "De vennootschapsbelasting is 40 000 euro. " + VA + " De vennootschap stortte VA2 15 000 euro en VA4 20 000 euro. Hoeveel vermeerdering blijft over?",
        ["900 euro", "3 600 euro", "2 700 euro", "0 euro"],
        0,
        "Vermeerdering 3 600 euro. Voordeel 15 000 · 0,10 = 1 500 en 20 000 · 0,06 = 1 200. 3 600 − 2 700 = 900 euro.",
    ),
    mk(
        "De vennootschapsbelasting is 40 000 euro. " + VA + " Welke voorafbetaling vermijdt de vermeerdering helemaal?",
        [
            "30 000 euro bij VA1",
            "40 000 euro bij VA4",
            "20 000 euro bij VA2 en 10 000 euro bij VA3",
            "40 000 euro bij VA3",
        ],
        0,
        "De vermeerdering is 3 600 euro. VA1: 30 000 · 0,12 = 3 600. De andere geven 2 400, 2 800 en 3 200 euro.",
    ),
    inv(
        "Een grote vennootschap doet geen voorafbetalingen. Haar belasting is 35 000 euro en de vermeerdering is 9 %. Hoeveel euro vermeerdering betaalt ze? Schrijf enkel het getal.",
        "3150",
        "35 000 · 0,09 = 3 150 euro.",
    ),
    tabel(
        "Hoort het bij het boekjaar of bij het aanslagjaar?",
        [
            ("De periode waarin de vennootschap haar winst maakt", "Boekjaar"),
            ("Het jaar waarin de belasting wordt berekend en gevestigd", "Aanslagjaar"),
            ("De periode waarin de voorafbetalingen vallen", "Boekjaar"),
        ],
        "Winst en voorafbetalingen horen bij het boekjaar. De berekening volgt in het aanslagjaar.",
        kolommen=["Boekjaar", "Aanslagjaar"],
    ),
    mk(
        "Waarop wordt de vennootschapsbelasting berekend?",
        [
            "Op de belastbare winst",
            "Op de volledige omzet van het jaar",
            "Op het kapitaal dat de aandeelhouders inbrachten",
            "Op de lonen die de vennootschap uitbetaalde",
        ],
        0,
        "Grondslag is de winst die overblijft na de aftrekbare kosten, niet de omzet.",
    ),
    open_(
        "Vergelijk de belasting op de winst van een eenmanszaak en van een vennootschap op twee punten.",
        "De winst van een eenmanszaak valt in de personenbelasting en wordt progressief belast tot 50 %, samen met de andere inkomens. Een vennootschap betaalt vennootschapsbelasting aan een vast tarief van 25 %, of 20 % op de eerste 100 000 euro voor kleine vennootschappen. Bij voorafbetalingen kan een zelfstandige een bonificatie krijgen, een vennootschap hoogstens het wegvallen van de vermeerdering.",
        "Grondslag, progressiviteit en voorafbetalingen zijn de drie vergelijkingspunten.",
    ),
    casus(
        "Bakkerij Vers bv is een kleine vennootschap in haar zesde boekjaar, gelijk aan het kalenderjaar. De belastbare winst is 120 000 euro. Ze stortte 10 000 euro op 5 april en 5 000 euro op 1 juli. " + KLEIN + " " + VA,
        [
            mk(
                "Hoeveel vennootschapsbelasting betaalt Bakkerij Vers, zonder vermeerdering?",
                ["25 000 euro", "30 000 euro", "24 000 euro", "20 000 euro"],
                0,
                "100 000 · 0,20 = 20 000 en 20 000 · 0,25 = 5 000. Samen 25 000 euro.",
            ),
            mk(
                "Hoeveel vermeerdering blijft er over na de voorafbetalingen?",
                ["550 euro", "2 250 euro", "1 050 euro", "0 euro"],
                0,
                "Vermeerdering 25 000 · 0,09 = 2 250 euro. Voordeel 10 000 · 0,12 = 1 200 (VA1) en 5 000 · 0,10 = 500 (VA2). 2 250 − 1 700 = 550 euro.",
            ),
            mk(
                "Hoeveel moet Bakkerij Vers na het aanslagbiljet nog betalen?",
                ["10 550 euro", "25 550 euro", "10 000 euro", "9 450 euro"],
                0,
                "Belasting plus vermeerdering: 25 000 + 550 = 25 550 euro. Daarvan is 15 000 euro al vooraf betaald. Er blijft 10 550 euro.",
            ),
        ],
    ),
]
