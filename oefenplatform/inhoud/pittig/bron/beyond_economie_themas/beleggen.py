"""De financiële markt en beleggen — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("beleggen-markt-financiele-middelen", 0, 20, 0, 10, 2, 1)
PUNTEN = {"E": (8, 5), "F": (10, 4), "G": (10, 6), "H": (12, 3)}

GRAFIEKEN = [
    dict(naam=G, titel="Markt van financiële middelen",
         krommen=[(lambda q: 9 - 0.5 * q, "groen", "V1", (0, 16.5)), (lambda q: 11 - 0.5 * q, "paars", "V2", (0, 20)),
                  (lambda q: 1 + 0.5 * q, "blauw", "A1", (0, 18)), (lambda q: -1 + 0.5 * q, "oranje", "A2", (2, 20))],
         labelplek={"V1": (15.5, 1.25), "V2": (19, 1.5), "A1": (16.5, 9.25), "A2": (19, 8.5)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="hoeveelheid krediet", ylabel="rente (%)", ijk_x=2, ijk_y=1),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat="Vraag (V1, V2) en aanbod (A1, A2) van financiële middelen, met de rente op de verticale as", vragen="klikvragen over sparen, lenen en de rente")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "De markt staat in punt E. Gezinnen gaan veel meer sparen, en verder verandert er niets. Klik op het nieuwe evenwicht.",
        P, [punt_zone(G, *PUNTEN["F"])],
        "Spaarders bieden financiële middelen aan. Meer sparen verschuift het aanbod van A1 naar A2: de rente daalt naar 4 %.",
    ),
    klik(
        "De markt staat in punt E. De overheid leent veel meer om een tekort te financieren. Klik op het nieuwe evenwicht.",
        P, [punt_zone(G, *PUNTEN["G"])],
        "Ontleners vragen financiële middelen. Meer lenen verschuift de vraag van V1 naar V2: de rente stijgt naar 6 %.",
    ),
    met_prent(P, mk(
        "Wie vormt op deze markt de aanbodcurve A1?",
        ["Spaarders, zoals gezinnen die sparen en pensioenfondsen", "Ontleners, zoals gezinnen die met een lening een huis kopen",
         "Bedrijven die met geleend geld willen investeren in nieuwe machines", "De overheid die een tekort op haar begroting moet financieren"],
        0,
        "Spaarders bieden geld aan; gezinnen met een woonkrediet, investerende bedrijven en de overheid vragen het.",
    )),
    met_prent(P, keuze(
        "Op deze markt is de prijs de [[*rente|wisselkoers]]. Van E naar H is een beweging [[*op|van]] de vraagcurve V1.",
        "H ligt op dezelfde curve V1 als E: enkel de rente veranderde.",
    )),
    tabel(
        "Gaat dit over de geldmarkt of de kapitaalmarkt?",
        [
            ("Een lening van drie maanden tussen twee banken", "Geldmarkt"),
            ("Aandelen kopen op de beurs", "Kapitaalmarkt"),
            ("Een obligatie met een looptijd van tien jaar", "Kapitaalmarkt"),
            ("Een kaskrediet dat een bedrijf binnen het jaar terugbetaalt", "Geldmarkt"),
        ],
        "Geldmarkt: korte termijn, tot een jaar. Kapitaalmarkt: lange termijn, zoals aandelen en obligaties.",
        kolommen=["Geldmarkt", "Kapitaalmarkt"],
    ),
    tabel(
        "Primaire of secundaire markt?",
        [
            ("Een bedrijf gaat naar de beurs en geeft nieuwe aandelen uit", "Primaire markt"),
            ("Je verkoopt je aandelen via de beurs aan een andere belegger", "Secundaire markt"),
            ("De overheid geeft nieuwe staatsobligaties uit", "Primaire markt"),
        ],
        "Primair: nieuwe effecten. Secundair: bestaande effecten die beleggers onder elkaar verhandelen.",
        kolommen=["Primaire markt", "Secundaire markt"],
    ),
    tabel(
        "Hoort dit bij een obligatie of bij een aandeel?",
        [
            ("Een deel van de eigendom van een bedrijf", "Aandeel"),
            ("Een lening met rente aan een bedrijf of overheid", "Obligatie"),
            ("Stemrecht op de algemene vergadering", "Aandeel"),
            ("Een looptijd en een coupon", "Obligatie"),
            ("Eventueel een dividend", "Aandeel"),
        ],
        "Een obligatie is een lening, een aandeel is eigendom.",
        kolommen=["Obligatie", "Aandeel"],
    ),
    mk(
        "Je hebt een obligatie met een vaste rente van 2 %. De marktrente stijgt naar 4 %. Wat gebeurt er met de koers van je obligatie?",
        ["Ze daalt, want nieuwe obligaties geven meer rente", "Ze stijgt, want rente is goed voor beleggers",
         "Ze blijft gelijk, want de rente van je obligatie ligt vast", "Ze stijgt, want je krijgt nu 4 % rente"],
        0,
        "Niemand wil nog de volle prijs betalen voor een oude obligatie die minder geeft dan een nieuwe.",
    ),
    tabel(
        "Waar of niet waar over beleggen in obligaties en aandelen?",
        [
            ("Een obligatie is zonder risico.", F),
            ("Een bedrijf is niet verplicht om elk jaar dividend uit te keren.", J),
            ("Het rendement van een obligatie hangt ook af van de kredietwaardigheid van de uitgever.", J),
            ("De koers van een aandeel schommelt meestal minder dan die van een obligatie.", F),
        ],
        "Ook een obligatie heeft risico (rente en kredietwaardigheid). Aandelen schommelen sterker.",
    ),
    mk(
        "Waar hangt het rendement van een aandeel vooral van af?",
        ["De verwachte winst van het bedrijf", "De coupon die op het aandeel staat",
         "De looptijd van het aandeel", "Het aantal stemmen van de aandeelhouder"],
        0,
        "Een aandeel brengt dividend en koersstijging op, en die hangen af van de verwachte winst.",
    ),
    mk(
        "Een gepensioneerde wil absoluut zeker zijn dat ze haar inleg terugkrijgt. Welk product past het best?",
        ["Een Tak21-verzekering", "Een Tak23-verzekering", "Een aandelenfonds", "Een ETF op een beursindex"],
        0,
        "Tak21 heeft een gewaarborgd kapitaal en een gewaarborgde rente. Bij Tak23 kan je minder terugkrijgen.",
    ),
    koppel(
        "Koppel elk product aan zijn omschrijving.",
        [
            ["ETF", "Indexfonds dat je op elk moment op de beurs verhandelt"],
            ["Bevek", "Fonds met veranderlijk kapitaal"],
            ["Gemengd fonds", "Belegt in aandelen én obligaties"],
            ["Tak23-verzekering", "Rendement via beleggingsfondsen, zonder kapitaalgarantie"],
        ],
        ["Gewaarborgd kapitaal met gewaarborgde rente"],
        "Gewaarborgd kapitaal en gewaarborgde rente horen bij Tak21.",
    ),
    volgorde(
        "Zet deze beleggingen van meestal minst naar meest risicovol.",
        ["Een Tak21-verzekering", "Een obligatiefonds", "Een gemengd fonds", "Een aandelenfonds"],
        "Tak21 is gewaarborgd. Obligaties schommelen minder dan aandelen, een gemengd fonds zit ertussen.",
    ),
    mk(
        "Sam belegt zijn spaargeld niet in één bedrijf, maar in aandelen van twintig bedrijven en wat obligaties. Waarom?",
        ["Om het risico te beperken", "Om minder belastingen te betalen", "Om zeker elk jaar dividend te krijgen", "Omdat de wet dat verplicht"],
        0,
        "Gaat één belegging slecht, dan weegt dat minder zwaar door.",
    ),
    tabel(
        "Is dit een professionele belegger?",
        [
            ("Een pensioenfonds", "Wel"),
            ("Een verzekeraar", "Wel"),
            ("Een leerkracht die zelf aandelen koopt", "Niet"),
        ],
        "Pensioenfondsen en verzekeraars beleggen beroepsmatig; een particulier niet.",
        kolommen=["Wel", "Niet"],
    ),
    mk(
        "Wat doen banken op de markt van financiële middelen?",
        ["Ze verzamelen spaargeld en lenen het uit", "Ze bepalen de koers van alle aandelen",
         "Ze drukken bankbiljetten voor hun klanten", "Ze geven enkel leningen aan de overheid"],
        0,
        "Banken staan tussen spaarders en kredietnemers.",
    ),
    tabel(
        "Bij welke letter van ESG hoort dit?",
        [
            ("Weinig uitstoot", "E"),
            ("Kinderarbeid bij leveranciers weren", "S"),
            ("Een onafhankelijke raad van bestuur", "G"),
            ("Een eerlijke beloning van de top van het bedrijf", "G"),
        ],
        "E = Environment (milieu), S = Social, G = Governance (bestuur).",
        kolommen=["E", "S", "G"],
    ),
    mk(
        "Een fonds noemt zich 'groen', maar belegt grotendeels in olie- en gasbedrijven. Hoe noem je dat?",
        ["Greenwashing", "Spreiding", "Een Tak21-belegging", "Een primaire markt"],
        0,
        "Groen lijken zonder het te zijn, heet greenwashing.",
    ),
    mk(
        "Wat verlaagt de ESG-score van een fonds?",
        ["Beleggingen in bedrijven met een corruptieschandaal", "Beleggingen in bedrijven met weinig uitstoot",
         "Een goed bestuur bij de bedrijven waarin het belegt", "Een laag rendement van het fonds"],
        0,
        "Hoge uitstoot en corruptieschandalen verlagen de score. Het rendement zit niet in de ESG-score.",
    ),
    sleep(
        "De beurs hoort bij de [[kapitaalmarkt]] en is een [[secundaire]] markt.",
        ["geldmarkt", "primaire"],
        "Op de beurs verhandelen beleggers bestaande aandelen en obligaties voor de lange termijn.",
    ),
    casus(
        "Lotte heeft 10 000 euro. Ze twijfelt tussen een obligatie van een stabiel bedrijf met een vaste coupon van 3 % en aandelen van een jong technologiebedrijf.",
        [
            mk("Welke belegging is het meest risicovol?", ["De aandelen", "De obligatie", "Allebei even risicovol", "Geen van beide"], 0,
               "Aandelenkoersen schommelen sterker dan obligaties."),
            inv("Hoeveel euro rente levert de obligatie haar per jaar op?", "300",
                "3 % van 10 000 = 300 euro."),
            mk("Lotte koopt de obligatie. Het bedrijf raakt in financiële problemen. Wat is het risico?",
               ["Ze krijgt haar geld misschien niet volledig terug", "Ze moet extra geld bijstorten",
                "Ze wordt automatisch aandeelhouder met stemrecht in het bedrijf", "Er is geen risico, want de coupon ligt vast"], 0,
               "Het rendement van een obligatie hangt ook af van de kredietwaardigheid van de uitgever."),
        ],
    ),
    open_(
        "Leg uit waarom de rente stijgt als de overheid veel meer leent, en wat dat betekent voor een gezin dat een huis wil kopen.",
        "De overheid vraagt meer financiële middelen, dus de vraagcurve verschuift naar rechts en de rente (de prijs op die markt) stijgt. Een gezin dat een woonkrediet nodig heeft, moet dan meer rente betalen.",
    ),
    mk(
        "Een bedrijf geeft nieuwe obligaties uit om een fabriek te bouwen. Wat doet het eigenlijk?",
        ["Het leent geld voor lange termijn op de primaire markt", "Het verkoopt een deel van zijn eigendom op de secundaire markt",
         "Het leent geld voor drie maanden op de geldmarkt", "Het keert een dividend uit aan zijn aandeelhouders"],
        0,
        "Een obligatie is een lening. Nieuwe effecten worden op de primaire markt uitgegeven, en lange termijn hoort bij de kapitaalmarkt.",
    ),
    tabel(
        "Wat gebeurt er met de rente?",
        [
            ("Gezinnen sparen minder", "Stijgt"),
            ("Bedrijven willen veel minder investeren", "Daalt"),
            ("Pensioenfondsen krijgen veel meer geld om te beleggen", "Daalt"),
        ],
        "Minder aanbod of meer vraag doet de rente stijgen; meer aanbod of minder vraag doet ze dalen.",
        kolommen=["Stijgt", "Daalt"],
    ),
    mk(
        "De marktrente daalt sterk. Wat gebeurt er met de koers van een bestaande obligatie met een vaste rente?",
        ["Ze stijgt, want nieuwe obligaties geven minder", "Ze daalt, want rente wordt minder belangrijk",
         "Ze blijft gelijk, want de coupon verandert niet", "Ze daalt, want de uitgever betaalt minder rente"],
        0,
        "Een oude obligatie die meer geeft dan een nieuwe, wordt gegeerd: beleggers willen er meer voor betalen.",
    ),
    keuze(
        "Een bevek heeft een [[*veranderlijk|vast]] kapitaal, een bevak een [[*vast|veranderlijk]] kapitaal.",
        "De k van bevek staat voor veranderlijk kapitaal, de a van bevak voor vast kapitaal.",
    ),
    inv(
        "Een aandeel kost 50 euro. Na een jaar is het 54 euro waard en kreeg je 1 euro dividend. Hoeveel procent rendement haalde je in totaal? Schrijf enkel het getal.",
        "10",
        "Koersstijging 4 + dividend 1 = 5 euro op 50 euro: 10 %.",
    ),
    mk(
        "Wat betekent duurzaam beleggen?",
        ["Je kijkt niet enkel naar het hoogste rendement, maar ook naar milieu, sociale kant en bestuur",
         "Je belegt enkel in obligaties met een looptijd van meer dan tien jaar, zodat je geld lang vastligt",
         "Je verkoopt je aandelen nooit meer, wat er ook gebeurt met de koers of met het bedrijf",
         "Je belegt enkel in Belgische bedrijven, omdat die strengere regels volgen dan buitenlandse"],
        0,
        "De ESG-score zegt hoe duurzaam de bedrijven zijn waarin een fonds belegt.",
    ),
]
