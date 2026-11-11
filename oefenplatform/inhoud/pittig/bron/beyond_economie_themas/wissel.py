"""De wisselmarkt en de betalingsbalans — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("wissel-markt-euro", 0, 20, 0, 2, 2, 0.2)
PUNTEN = {"E": (10, 1.2), "F": (12, 1.32), "G": (12, 1.08)}

GRAFIEKEN = [
    dict(naam=G, titel="Wisselmarkt van de euro (koers in dollar per euro)",
         krommen=[(lambda q: 1.8 - 0.06 * q, "groen", "V1", (0, 20)), (lambda q: 2.04 - 0.06 * q, "paars", "V2", (3.5, 20)),
                  (lambda q: 0.6 + 0.06 * q, "blauw", "A1", (0, 20)), (lambda q: 0.36 + 0.06 * q, "oranje", "A2", (0, 20))],
         labelplek={"V1": (18.5, 0.69), "V2": (19, 0.9), "A1": (18, 1.68), "A2": (19.2, 1.512)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="hoeveelheid euro", ylabel="koers in dollar", ijk_x=2, ijk_y=0.2),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat="Vraag (V1, V2) en aanbod (A1, A2) van euro op de wisselmarkt", vragen="klikvragen over appreciatie en depreciatie")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "De markt staat in punt E. De ECB verhoogt de rente, en verder verandert er niets. Klik op het nieuwe evenwicht.",
        P, [punt_zone(G, *PUNTEN["F"])],
        "Een hogere rente maakt beleggen in euro aantrekkelijker: de vraag naar euro stijgt (V1 naar V2) en de euro apprecieert.",
    ),
    klik(
        "De markt staat in punt E. Het inkomen in de eurozone stijgt, zodat Europeanen meer importeren uit de VS. Klik op het nieuwe evenwicht.",
        P, [punt_zone(G, *PUNTEN["G"])],
        "Wie Amerikaanse producten koopt, ruilt euro's in voor dollars: het aanbod van euro stijgt (A1 naar A2) en de euro deprecieert.",
    ),
    met_prent(P, mk(
        "Van E naar F: wat gebeurt er met de euro?",
        ["Hij apprecieert van 1,20 naar 1,32 dollar", "Hij deprecieert van 1,20 naar 1,32 dollar",
         "Hij apprecieert van 1,20 naar 1,08 dollar", "Hij deprecieert van 1,32 naar 1,20 dollar"],
        0,
        "Je krijgt meer dollar voor een euro: de euro wordt duurder, hij apprecieert.",
    )),
    met_prent(P, tabel(
        "Gaat de markt van E naar F (vraag naar euro stijgt) of van E naar G (aanbod van euro stijgt)?",
        [
            ("Consumenten wereldwijd verkiezen Europese producten", "Naar F"),
            ("Europese beleggers kopen massaal Amerikaanse aandelen", "Naar G"),
            ("Het inkomen in de VS stijgt, Amerikanen kopen meer Europese producten", "Naar F"),
            ("Belgische bedrijven kopen meer Amerikaanse machines", "Naar G"),
        ],
        "Wie euro's nodig heeft, vraagt euro's. Wie euro's omwisselt in dollar, biedt euro's aan.",
        kolommen=["Naar F", "Naar G"],
    )),
    tabel(
        "Vraagt deze persoon euro's of biedt hij euro's aan?",
        [
            ("Een Japanse toerist die in Brugge op hotel gaat", "Vraagt euro's"),
            ("Een Belgische toerist die naar Japan reist", "Biedt euro's aan"),
            ("Een Amerikaans bedrijf dat Belgische chocolade koopt", "Vraagt euro's"),
            ("Een Belgisch bedrijf dat Amerikaanse software koopt", "Biedt euro's aan"),
        ],
        "De Japanse toerist heeft euro's nodig. De Belgische toerist ruilt euro's om in yen.",
        kolommen=["Vraagt euro's", "Biedt euro's aan"],
    ),
    mk(
        "Waarom is de wisselmarkt een markt met volkomen concurrentie?",
        ["Er zijn veel kopers en verkopers van een homogeen product", "De ECB bepaalt elke dag opnieuw de koers voor iedereen",
         "Er is in elk land maar één verkoper van de eigen munt", "Enkel commerciële banken mogen er munten kopen en verkopen"],
        0,
        "Exporteurs, importeurs, beleggers, speculanten, toeristen en centrale banken verhandelen er dezelfde munten.",
    ),
    casus(
        "De koers EUR/USD is 1,25: voor 1 euro krijg je 1,25 dollar.",
        [
            inv("Een Belgisch product kost 120 euro. Hoeveel dollar betaalt een Amerikaan ervoor? Schrijf enkel het getal.", "150",
                "120 · 1,25 = 150 dollar."),
            inv("Een Belgische importeur krijgt een factuur van 2 000 dollar. Hoeveel euro betaalt hij? Schrijf enkel het getal.", "1600",
                "2 000 / 1,25 = 1 600 euro."),
            mk("De koers stijgt naar 1,40. Wat gebeurt er met de prijs van dat Belgische product voor Amerikanen?",
               ["Het wordt duurder: 168 dollar", "Het wordt goedkoper: 134 dollar", "Het blijft 150 dollar", "Het wordt duurder: 140 dollar"], 0,
               "120 · 1,40 = 168 dollar. Een apprecierende euro maakt Europese producten duurder voor Amerikanen."),
        ],
    ),
    tabel(
        "De euro apprecieert. Wat gebeurt er?",
        [
            ("Europese producten voor Amerikanen", "Duurder"),
            ("Amerikaanse producten voor Europeanen", "Goedkoper"),
            ("De Europese export naar de VS", "Daalt"),
            ("De Europese import uit de VS", "Stijgt"),
        ],
        "Bij appreciatie wordt de euro duurder: de export daalt en de import stijgt.",
        kolommen=["Duurder", "Goedkoper", "Stijgt", "Daalt"],
    ),
    tabel(
        "Apprecieert of deprecieert de euro?",
        [
            ("De inflatie in de eurozone ligt hoger dan in de VS", "Deprecieert"),
            ("De rente in de eurozone daalt", "Deprecieert"),
            ("Speculanten verwachten dat de euro zal stijgen en kopen nu euro's", "Apprecieert"),
            ("Buitenlandse beleggers kopen meer Europese aandelen", "Apprecieert"),
        ],
        "Hogere inflatie en een lagere rente maken de euro minder aantrekkelijk. Meer vraag naar euro doet hem appreciëren.",
        kolommen=["Apprecieert", "Deprecieert"],
    ),
    mk(
        "Een Belgische exporteur wordt binnen drie maanden in dollar betaald. Intussen stijgt de dollar tegenover de euro. Wat betekent dat voor hem?",
        ["Hij wint: hij krijgt meer euro's voor zijn dollars", "Hij verliest: hij krijgt minder euro's voor zijn dollars",
         "Er verandert niets: de factuur ligt vast", "Hij moet de factuur opnieuw opstellen in euro"],
        0,
        "Dat is het wisselkoersrisico, maar hier valt het in zijn voordeel uit.",
    ),
    keuze(
        "Een vlottende wisselkoers wordt bepaald door [[*vraag en aanbod|de regering]]. Een vaste wisselkoers geeft bedrijven [[*minder|meer]] wisselkoersrisico.",
        "Bij een vaste koers weet een exporteur vooraf hoeveel hij zal ontvangen.",
    ),
    tabel(
        "Op welke post van de betalingsbalans komt deze transactie?",
        [
            ("Een Belgisch bedrijf verkoopt machines aan Duitsland", "Goederen"),
            ("Een Nederlandse toerist betaalt een hotel in Brugge", "Diensten"),
            ("Een Belg krijgt dividend van een buitenlands bedrijf", "Primaire inkomens"),
            ("Een werknemer stuurt geld naar zijn familie in Marokko", "Secundaire inkomens"),
            ("Een Belgisch bedrijf bouwt een fabriek in Polen", "Financiële rekening"),
        ],
        "Goederen, diensten, primaire en secundaire inkomens staan op de lopende rekening. Beleggingen en investeringen op de financiële rekening.",
        kolommen=["Goederen", "Diensten", "Primaire inkomens", "Secundaire inkomens", "Financiële rekening"],
    ),
    mk(
        "Uit welke drie deelrekeningen bestaat de betalingsbalans?",
        ["Lopende rekening, kapitaalrekening en financiële rekening", "Handelsbalans, begroting van de overheid en staatsschuld",
         "Spaarrekening, zichtrekening en termijnrekening van de centrale bank", "Goederen, diensten, primaire inkomens en secundaire inkomens"],
        0,
        "Goederen, diensten en inkomens zijn posten van de lopende rekening.",
    ),
    mk(
        "Welke post van de lopende rekening is de handelsbalans?",
        ["Goederen", "Diensten", "Primaire inkomens", "Secundaire inkomens"],
        0,
        "De handelsbalans is de export en de import van goederen.",
    ),
    volgorde(
        "Een land met een vlottende wisselkoers heeft een groot tekort op de lopende rekening. Zet de gevolgen in de juiste volgorde.",
        ["Het land koopt meer in het buitenland dan het verkoopt", "Er wordt meer eigen munt aangeboden dan gevraagd",
         "De munt deprecieert", "De export wordt goedkoper en het tekort verkleint"],
        "Een depreciatie kan het tekort zelf helpen verkleinen.",
    ),
    koppel(
        "Koppel elke internationale instelling aan haar taak.",
        [
            ["IMF", "Landen met betalingsbalansproblemen helpen"],
            ["Wereldbank", "Armoede bestrijden met ontwikkelingsleningen"],
            ["OESO", "Onderzoek en beleidsadvies voor haar lidstaten"],
        ],
        ["De wisselkoersen van alle munten vastleggen"],
        "Geen van die instellingen legt de wisselkoersen vast. Ook de Wereldbank doet dat niet.",
    ),
    tabel(
        "Waar of niet waar over wisselkoersen?",
        [
            ("Gaat de koers EUR/USD van 1,10 naar 1,20, dan apprecieert de euro.", J),
            ("Een depreciërende euro maakt Amerikaanse producten goedkoper voor Europeanen.", F),
            ("Een hogere inflatie in de eurozone doet de euro appreciëren.", F),
            ("Ook centrale banken zijn actief op de wisselmarkt.", J),
        ],
        "Bij depreciatie worden Amerikaanse producten duurder voor Europeanen. Hogere inflatie doet de euro depreciëren.",
    ),
    inv(
        "1 euro = 1,10 dollar. Een Belgische importeur betaalt een factuur van 8 800 dollar. Hoeveel euro kost dat? Schrijf enkel het getal.",
        "8000",
        "8 800 / 1,10 = 8 000 euro.",
    ),
    sleep(
        "Gaat de koers van de euro omhoog, dan [[apprecieert]] de euro. Gaat hij omlaag, dan [[deprecieert]] hij.",
        ["devalueert", "inflateert"],
        "Appreciatie: de euro wordt duurder. Depreciatie: goedkoper.",
    ),
    open_(
        "Leg uit waarom een renteverhoging door de ECB de euro kan doen appreciëren, en wat dat betekent voor Belgische exporteurs.",
        "Een hogere rente maakt beleggen in euro aantrekkelijker. Buitenlandse beleggers vragen meer euro's, dus de koers stijgt: de euro apprecieert. Belgische producten worden dan duurder voor buitenlanders, waardoor de export kan dalen.",
    ),
    mk(
        "Een Belgische importeur moet over zes maanden 50 000 dollar betalen. Welk risico loopt hij?",
        ["De dollar stijgt, waardoor de factuur hem meer euro kost", "De dollar daalt, waardoor de factuur hem meer euro kost",
         "De Belgische rente stijgt, waardoor zijn spaargeld minder waard wordt", "Er is geen risico, want het bedrag in dollar ligt vast"],
        0,
        "Wisselkoersrisico: stijgt de dollar, dan moet hij meer euro's omwisselen om 50 000 dollar te betalen.",
    ),
    inv(
        "1 euro = 1,15 dollar. Een Belgisch product kost 200 euro. Hoeveel dollar betaalt een Amerikaan ervoor? Schrijf enkel het getal.",
        "230",
        "200 · 1,15 = 230 dollar.",
    ),
    mk(
        "De euro deprecieert tegenover de dollar. Wie in België is daar blij mee?",
        ["Een bedrijf dat veel naar de VS exporteert", "Een Belg die op reis gaat naar New York",
         "Een bedrijf dat veel Amerikaanse grondstoffen invoert", "Een Belgische student die in de VS studeert"],
        0,
        "Bij een depreciërende euro worden Europese producten goedkoper voor Amerikanen: de export stijgt.",
    ),
    sorteer(
        "Staat deze transactie op de lopende rekening of op de financiële rekening?",
        ["Lopende rekening", "Financiële rekening"],
        [
            ["Een Belg koopt Amerikaanse aandelen", "Financiële rekening"],
            ["België voert auto's uit naar Frankrijk", "Lopende rekening"],
            ["Een Duitse familie boekt een vakantie aan de Belgische kust", "Lopende rekening"],
            ["Een Japans bedrijf bouwt een fabriek in Limburg", "Financiële rekening"],
        ],
        "Goederen, diensten en inkomens: lopende rekening. Beleggingen en investeringen: financiële rekening.",
    ),
    mk(
        "Een Belgisch bedrijf koopt een Amerikaans bedrijf over. Waar komt die transactie op de betalingsbalans?",
        ["Op de financiële rekening", "Bij de goederen op de lopende rekening",
         "Bij de diensten op de lopende rekening", "Bij de secundaire inkomens op de lopende rekening"],
        0,
        "Een investering in het buitenland staat op de financiële rekening.",
    ),
    keuze(
        "Bij een koers van 1,10 dollar per euro krijg je voor 100 euro [[*110|91]] dollar, en kost 110 dollar je [[*100|121]] euro.",
        "Van euro naar dollar vermenigvuldig je met de koers, van dollar naar euro deel je erdoor.",
    ),
    mk(
        "Een land heeft ernstige betalingsbalansproblemen. Welke instelling kan helpen?",
        ["Het IMF", "De Wereldbank", "De OESO", "De Europese Commissie"],
        0,
        "Het Internationaal Monetair Fonds helpt landen met betalingsbalansproblemen.",
    ),
    tabel(
        "Wie is actief op de wisselmarkt?",
        [
            ("Exporteurs en importeurs", J),
            ("Beleggers en speculanten", J),
            ("Toeristen", J),
            ("Enkel de Europese Centrale Bank", F),
        ],
        "Veel soorten kopers en verkopers, ook centrale banken, maar niet enkel zij.",
    ),
]
