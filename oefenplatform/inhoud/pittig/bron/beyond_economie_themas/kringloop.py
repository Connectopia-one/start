"""De economische kringloop en de macro-economische identiteiten — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, s_lijn, GROEN, LICHT

# De uitgebreide kringloop als eigen prent: vijf actoren in vakken.
ACTOREN = {
    "Gezinnen": (130, 320),
    "Bedrijven": (870, 320),
    "Overheid": (500, 110),
    "Financiële instellingen": (500, 530),
    "Buitenland": (870, 560),
}


def _rand(naam, naar):
    """Het punt op de rand van het vak van naam, in de richting van naar."""
    x, y = ACTOREN[naam]
    tx, ty = naar
    breed = (250 if len(naam) > 12 else 190) / 2
    dx, dy = tx - x, ty - y
    f = min(breed / abs(dx) if dx else 1e9, 30 / abs(dy) if dy else 1e9)
    return x + dx * f, y + dy * f


def _kringloop():
    d = [f'<defs><marker id="pk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         f'<path d="M0,0 L10,5 L0,10 z" fill="{GROEN}"/></marker></defs>']
    pijlen = [
        ("Gezinnen", "Bedrijven", "consumptie C", -14),
        ("Bedrijven", "Gezinnen", "lonen, winsten", 14),
        ("Gezinnen", "Overheid", "belastingen T", 0),
        ("Overheid", "Bedrijven", "overheidsbestedingen G", 0),
        ("Gezinnen", "Financiële instellingen", "sparen S", 0),
        ("Financiële instellingen", "Bedrijven", "investeringen I", 0),
        ("Bedrijven", "Buitenland", "", 0),
    ]
    for van, naar, label, schuif in pijlen:
        (x1, y1) = _rand(van, ACTOREN[naar])
        (x2, y2) = _rand(naar, ACTOREN[van])
        y1, y2 = y1 + schuif, y2 + schuif
        d.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GROEN}" stroke-width="3"'
                 + ('' if not label else ' marker-end="url(#pk)"') + '/>')
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + (-16 if schuif < 0 else 22 if schuif > 0 else 0)
            w = len(label) * 9.5 + 16
            d.append(s_vak(mx - w / 2, my - 15, w, 26, vul="#fffdf7", rand="#fffdf7", dikte=0))
            d.append(s_tekst(mx, my + 5, label, 17))
    for naam, (x, y) in ACTOREN.items():
        breed = 250 if len(naam) > 12 else 190
        d.append(s_vak(x - breed / 2, y - 30, breed, 60, vul=LICHT, rand=GROEN, rond=14))
        d.append(s_tekst(x, y + 7, naam, 20, vet=True))
    return d


GRAFIEKEN = [dict(naam="kringloop-vijf-actoren", titel="De uitgebreide economische kringloop (geldstromen)", eigen=_kringloop)]

PRENTEN = [dict(bestand="kringloop-vijf-actoren.svg", zelf=True, wat=GRAFIEKEN[0]["titel"],
                vragen="klikvragen op een actor en vragen over de geldstromen")]

P = "kringloop-vijf-actoren.svg"


def _zone(naam):
    x, y = ACTOREN[naam]
    breed = 250 if len(naam) > 12 else 190
    return pix_zone(x - breed / 2, y - 30, breed, 60)


VRAGEN = [
    klik(
        "Klik op de actor waar het sparen van de gezinnen terechtkomt en waar bedrijven geld lenen om te investeren.",
        P, [_zone("Financiële instellingen")],
        "De financiële instellingen verzamelen het spaargeld en lenen het uit aan bedrijven die investeren.",
    ),
    klik(
        "In deze tekening ontbreekt de geldstroom voor de Belgische export. Klik op de actor die voor die export betaalt.",
        P, [_zone("Buitenland")],
        "Bij export gaan goederen naar het buitenland en komt er geld uit het buitenland naar België.",
    ),
    met_prent(P, mk(
        "De pijl 'belastingen T' loopt van de gezinnen naar de overheid. Welke stroom loopt in de omgekeerde richting, van de overheid naar de gezinnen?",
        ["Uitkeringen en lonen van ambtenaren", "Consumptie van gezinnen bij de overheid", "Investeringen van de overheid in bedrijven", "Betalingen voor de import"],
        0,
        "De overheid betaalt uitkeringen en de lonen van ambtenaren aan de gezinnen.",
    )),
    met_prent(P, tabel(
        "Is de stroom een reële stroom of een geldstroom?",
        [
            ("Een leerkracht geeft les op een school van de overheid", "Reële stroom"),
            ("De overheid stort het loon van die leerkracht", "Geldstroom"),
            ("Een Belgische fabriek levert machines aan Duitsland", "Reële stroom"),
            ("Een gezin betaalt de bakker", "Geldstroom"),
        ],
        "Arbeid, goederen en diensten zijn reële stromen. De betaling ervoor loopt als geldstroom in de omgekeerde richting.",
        kolommen=["Reële stroom", "Geldstroom"],
    )),
    inv(
        "Een land heeft Y = 2 000, T = 500 en S = 300. Hoe groot is de consumptie C? Schrijf enkel het getal.",
        "1200",
        "Y = T + C + S, dus C = 2 000 − 500 − 300 = 1 200.",
    ),
    inv(
        "C = 900, I = 250, G = 400, X = 600 en M = 650. Hoe groot is het nationaal inkomen Y? Schrijf enkel het getal.",
        "1500",
        "Y = C + I + G + (X − M) = 900 + 250 + 400 + (600 − 650) = 1 500.",
    ),
    mk(
        "Y = 1 800, C = 1 100, I = 300 en G = 450. Wat weet je over de netto-export?",
        ["Ze is −50: het land importeert meer dan het exporteert", "Ze is +50: het land exporteert meer dan het importeert",
         "Ze is 0: export en import zijn even groot", "Ze is 1 850: de som van alle bestedingen"],
        0,
        "X − M = Y − C − I − G = 1 800 − 1 100 − 300 − 450 = −50.",
    ),
    tabel(
        "In een land is S = 200, I = 260, T = 380 en G = 350. Bereken de saldi.",
        [("Spaarsaldo S − I", "−60"), ("Begrotingssaldo T − G", "+30"), ("Handelsbalanssaldo X − M", "−30")],
        "S − I = −60 en T − G = +30. Samen zijn ze gelijk aan X − M: −60 + 30 = −30.",
        kolommen=["−60", "−30", "+30", "+60"],
    ),
    mk(
        "Het spaarsaldo is +40 en het handelsbalanssaldo is +10. Wat is het begrotingssaldo?",
        ["−30: een begrotingstekort", "+30: een begrotingsoverschot", "+50: een begrotingsoverschot", "−50: een begrotingstekort"],
        0,
        "(S − I) + (T − G) = X − M, dus T − G = 10 − 40 = −30.",
    ),
    mk(
        "De overheid heeft een groot begrotingstekort, maar het land heeft toch een handelsoverschot. Wat moet dan waar zijn?",
        ["De particulieren sparen veel meer dan ze investeren", "De particulieren investeren meer dan ze sparen",
         "De overheid ontvangt meer dan ze uitgeeft", "De import is groter dan de export"],
        0,
        "Een negatief T − G en een positief X − M kan alleen als S − I sterk positief is.",
    ),
    sorteer(
        "Is dit in de kringloop sparen of investeren?",
        ["Sparen (S)", "Investeren (I)"],
        [
            ["Een gezin koopt aandelen van een bedrijf", "Sparen (S)"],
            ["Een bakker koopt een nieuwe oven", "Investeren (I)"],
            ["Een gezin zet geld op een spaarrekening", "Sparen (S)"],
            ["Een fabriek bouwt een nieuwe hal", "Investeren (I)"],
            ["Een bedrijf legt een grotere voorraad aan", "Investeren (I)"],
        ],
        "Investeren is in de kringloop een aankoop van kapitaalgoederen door bedrijven. Aandelen kopen is voor een gezin sparen.",
    ),
    koppel(
        "Op welke markt gebeurt het?",
        [
            ["Een student solliciteert voor een vakantiejob", "Arbeidsmarkt"],
            ["Een gezin koopt een nieuwe wasmachine", "Productmarkt"],
            ["Een bedrijf leent geld voor een nieuwe fabriek", "Kapitaalmarkt"],
        ],
        ["Wisselmarkt", "Grondmarkt"],
        "Arbeid wordt verhandeld op de arbeidsmarkt, goederen op de productmarkt en geld voor lange termijn op de kapitaalmarkt.",
    ),
    keuze(
        "Op de arbeidsmarkt [[*bieden|vragen]] de gezinnen arbeid aan en [[*vragen|bieden]] de bedrijven en de overheid arbeid.",
        "De gezinnen leveren arbeid, de werkgevers vragen ze.",
    ),
    sleep(
        "Bij elke actor is wat [[binnenkomt]] gelijk aan wat [[buitengaat]]. Daarom kan je met de kringloop een [[ontbrekend]] cijfer berekenen.",
        ["groeit", "verdwijnt", "geschat"],
        "Dat is de kern van de macro-economische identiteiten.",
    ),
    mk(
        "Een gezin verdient 60 000 euro, betaalt 18 000 euro belastingen en spaart 7 000 euro. Een vriend zegt: 'Dan consumeert het gezin 42 000 euro.' Klopt dat?",
        ["Nee, het gezin consumeert 35 000 euro", "Ja, want 60 000 − 18 000 = 42 000", "Nee, het gezin consumeert 53 000 euro", "Ja, sparen telt niet mee"],
        0,
        "De vriend vergeet het sparen: 60 000 − 18 000 − 7 000 = 35 000 euro.",
    ),
    tabel(
        "Waar of niet waar over de kringloop?",
        [
            ("De geldstroom loopt in dezelfde richting als de goederenstroom.", F),
            ("Een reële stroom kan bestaan uit arbeid.", J),
            ("In de kringloop is het kopen van aandelen door een gezin een investering.", F),
            ("Mantelzorg zit niet in het klassieke kringloopmodel.", J),
        ],
        "De geldstroom loopt tegengesteld. Aandelen kopen is sparen. Onbetaald werk telt het model niet mee.",
    ),
    mk(
        "Welke tekortkoming van het klassieke kringloopmodel toont dit voorbeeld: een fabriek produceert meer en de cijfers stijgen, maar de rivier ernaast raakt vervuild?",
        ["Het model telt enkel wat met geld betaald wordt en ziet vervuiling niet",
         "Het model telt de overheid niet mee als actor", "Het model vergeet de export naar het buitenland", "Het model telt de vervuiling dubbel als productie"],
        0,
        "Vervuiling, afval en de grenzen van grondstoffen zitten niet in de klassieke kringloop.",
    ),
    mk(
        "Het begrotingssaldo is 0. Wat volgt uit S − I = X − M?",
        ["Wat de particulieren meer sparen dan investeren, vloeit als handelsoverschot naar het buitenland",
         "Het land heeft dan altijd een handelstekort met het buitenland", "De particulieren sparen niets en investeren alles", "Export en import zijn dan altijd precies even groot"],
        0,
        "Met T − G = 0 blijft over: S − I = X − M.",
    ),
    inv(
        "Y = 1 200, T = 300, C = 750. Hoe groot is S? Schrijf enkel het getal.",
        "150",
        "S = Y − T − C = 1 200 − 300 − 750 = 150.",
    ),
    mk(
        "Welke formule klopt bij de financiële instellingen?",
        ["S + T = I + G + X − M", "S + I = T + G + X − M", "Y = C + S + G", "S − T = I − G"],
        0,
        "Bij de financiële instellingen komt alles samen: S + T = I + G + X − M.",
    ),
    volgorde(
        "Je kent Y, T en C van een land en wil het spaarsaldo berekenen. Zet de stappen in de juiste volgorde.",
        ["S berekenen als Y − T − C", "De investeringen I opzoeken", "S − I uitrekenen", "Het teken lezen: positief betekent dat de particulieren meer sparen dan ze investeren"],
        "Eerst het sparen vinden, dan de investeringen ervan aftrekken en het resultaat duiden.",
    ),
    mk(
        "In een land stijgen de investeringen (I) sterk, terwijl S, T, G en de export gelijk blijven. Wat gebeurt er volgens S + T = I + G + X − M met de import?",
        ["De import stijgt even sterk", "De import daalt even sterk", "De import blijft gelijk", "De import halveert"],
        0,
        "Blijft de linkerkant gelijk en stijgt I, dan moet M evenveel stijgen.",
    ),
    tabel(
        "Welk saldo is het?",
        [
            ("De particulieren sparen meer dan ze investeren", "S − I"),
            ("De overheid ontvangt minder dan ze uitgeeft", "T − G"),
            ("Het land exporteert meer dan het importeert", "X − M"),
        ],
        "Spaarsaldo, begrotingssaldo en handelsbalanssaldo.",
        kolommen=["S − I", "T − G", "X − M"],
    ),
    mk(
        "Waarom staan belastingen (T) in Y = T + C + S aan de kant van de gezinnen?",
        ["Het inkomen van de gezinnen gaat naar belastingen, consumptie en sparen",
         "De gezinnen ontvangen de belastingen van de overheid als inkomen", "Belastingen zijn in de kringloop een vorm van investeren",
         "Belastingen gaan rechtstreeks naar het buitenland"],
        0,
        "Het inkomen Y verdeelt zich over wat gezinnen afdragen, uitgeven en opzijzetten.",
    ),
    casus(
        "Een eenvoudig land: Y = 1 000, C = 600, I = 150, G = 250, T = 200, X = 300.",
        [
            inv("Hoe groot is de import M? Schrijf enkel het getal.", "300",
                "M = C + I + G + X − Y = 600 + 150 + 250 + 300 − 1 000 = 300."),
            inv("Hoe groot is het sparen S? Schrijf enkel het getal.", "200",
                "S = Y − T − C = 1 000 − 200 − 600 = 200."),
            mk("Welke saldi heeft dit land?",
               ["S − I = +50, T − G = −50, X − M = 0", "S − I = −50, T − G = +50, X − M = 0",
                "S − I = +50, T − G = +50, X − M = +100", "S − I = 0, T − G = 0, X − M = 0"],
               0,
               "S − I = 200 − 150 = 50, T − G = 200 − 250 = −50, X − M = 300 − 300 = 0. Samen klopt het: 50 − 50 = 0."),
        ],
    ),
    mk(
        "Een leerling zegt: 'Een reële stroom is het geld dat echt betaald wordt.' Wat is er fout?",
        ["Een reële stroom is net geen geld: het zijn goederen, diensten en productiefactoren",
         "Een reële stroom gaat enkel van België naar het buitenland", "Een reële stroom bestaat alleen tussen gezinnen en de overheid",
         "Er is niets fout aan: zo staat het in de kringloop"],
        0,
        "Het woord reëel verwijst naar goederen, diensten en arbeid, niet naar geld.",
    ),
    sorteer(
        "Komt het geld bij de Belgische gezinnen binnen of gaat het buiten?",
        ["Binnen", "Buiten"],
        [
            ["Loon van een bedrijf", "Binnen"],
            ["Personenbelasting", "Buiten"],
            ["Een werkloosheidsuitkering", "Binnen"],
            ["Boodschappen in de supermarkt", "Buiten"],
        ],
        "Lonen en uitkeringen komen binnen, belastingen en consumptie gaan buiten.",
    ),
    open_(
        "Leg uit waarom S + T = I + G + X − M altijd moet kloppen in een kringloop.",
        "Wat de gezinnen niet consumeren (sparen en belastingen) lekt weg uit de kringloop. Omdat alles wat geproduceerd wordt ook gekocht wordt, moet dat terugkomen als investeringen, overheidsbestedingen en netto-export.",
    ),
]
