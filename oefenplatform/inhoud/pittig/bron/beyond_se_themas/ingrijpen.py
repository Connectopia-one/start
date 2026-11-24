"""Verschuivingen op de markt en de overheid die ingrijpt — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen grafiek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, BLAUW, ORANJE, assen

# Verschuivende curven ---------------------------------------------------------------
VS = Prent("markt-verschuivingen", "De markt voor fietsen (per maand)", "een grafiek met twee vraagcurven V1 en V2 (V2 rechts van V1) en drie aanbodcurven A1 (midden), A2 (links) en A3 (rechts); het oorspronkelijke evenwicht E ligt op V1 en A1; de punten R, S, T en U zijn andere snijpunten")
X, Y = assen(VS, 0, 400, 0, 12, "hoeveelheid (fietsen)", "prijs (honderd euro)", 50, 1, links=110, rechts=880)
VS.lijn(X(0), Y(12), X(300), Y(0), BLAUW, 4)           # V1
VS.lijn(X(100), Y(12), X(400), Y(0), BLAUW, 3)         # V2
VS.lijn(X(0), Y(2), X(250), Y(12), ORANJE, 4)          # A1
VS.lijn(X(0), Y(6), X(150), Y(12), ORANJE, 3)          # A2
VS.lijn(X(50), Y(0), X(350), Y(12), ORANJE, 3)         # A3
for t, x, y, kl in (("V1", 8, 11.6, BLAUW), ("V2", 108, 11.6, BLAUW), ("A1", 255, 11.6, ORANJE), ("A2", 155, 11.6, ORANJE), ("A3", 355, 11.6, ORANJE)):
    VS.tekst(X(x), Y(y), t, 18, "start", kl, True)
PV = {"E": (125, 7), "R": (175, 9), "S": (75, 9), "T": (125, 11), "U": (175, 5)}
for k, (q, p) in PV.items():
    VS.cirkel(X(q), Y(p), 7, DONKER, DONKER, 1)
    VS.letter(X(q) + 28, Y(p) + 26, k)
ZV = {k: [Prent.rond(X(q) + 12, Y(p) + 12, 38)] for k, (q, p) in PV.items()}

VRAGEN = [
    klik("De markt staat in E. De lonen van de kopers stijgen. Klik op het nieuwe evenwicht.", VS.bestand, ZV["R"],
         "Meer inkomen: de vraagcurve schuift naar rechts (V2). Nieuw evenwicht op V2 en A1: hogere prijs, meer fietsen."),
    klik("De markt staat in E. Staal wordt veel duurder. Klik op het nieuwe evenwicht.", VS.bestand, ZV["S"],
         "Duurdere grondstoffen: het aanbod schuift naar links (A2). Hogere prijs, minder fietsen."),
    klik("De markt staat in E. De overheid geeft fietsfabrikanten een subsidie. Klik op het nieuwe evenwicht.", VS.bestand, ZV["U"],
         "Een subsidie maakt produceren goedkoper: het aanbod schuift naar rechts (A3). Lagere prijs, meer fietsen."),
    klik("De markt staat in E. De lonen stijgen én staal wordt duurder. Klik op het nieuwe evenwicht.", VS.bestand, ZV["T"],
         "Vraag naar rechts en aanbod naar links: de prijs stijgt sterk, de hoeveelheid blijft hier gelijk."),
    met_prent(VS.bestand, tabel("Van E naar dit punt: wat gebeurt er met de prijs?", [
        ("R", "stijgt"), ("S", "stijgt"), ("U", "daalt"),
    ], "R en S liggen hoger dan E, U lager.", kolommen=["stijgt", "daalt"])),
    met_prent(VS.bestand, inv("Van E naar U: met hoeveel fietsen stijgt de verhandelde hoeveelheid?", ["50", "50 fietsen"],
              "Van 125 naar 175 fietsen.")),
    tabel("Verschuift de vraagcurve, de aanbodcurve, of beweeg je op de curve?", [
        ("De prijs van het product zelf daalt.", "beweging op de curve"),
        ("Een nieuwe machine maakt produceren goedkoper.", "aanbodcurve"),
        ("Het product komt in de mode door een influencer.", "vraagcurve"),
        ("Er komen veel nieuwe kopers bij in de stad.", "vraagcurve"),
    ], "Enkel een verandering van de eigen prijs geeft een beweging op de curve.",
       kolommen=["vraagcurve", "aanbodcurve", "beweging op de curve"]),
    sorteer("Verschuift de curve naar links of naar rechts?", ["Naar links", "Naar rechts"], [
        ["vraag: het inkomen van de kopers daalt", "Naar links"],
        ["aanbod: een betere techniek", "Naar rechts"],
        ["aanbod: een slechte oogst", "Naar links"],
        ["vraag: er komen kopers bij", "Naar rechts"],
    ], "Links is minder bij elke prijs, rechts is meer."),
    casus(
        "Na een zomer met veel regen is de oogst van tomaten mislukt. Tegelijk raden "
        "dokters aan meer groenten te eten, waardoor meer mensen tomaten willen.",
        [
            keuze("Door de slechte oogst verschuift de [[*aanbodcurve|vraagcurve]] naar [[*links|rechts]].",
                  "Er komt bij elke prijs minder op de markt."),
            keuze("Door het advies van de dokters verschuift de [[*vraagcurve|aanbodcurve]] naar [[*rechts|links]].",
                  "Er willen bij elke prijs meer mensen kopen."),
            mk("Wat gebeurt er zeker met de prijs van tomaten?",
               ["Ze stijgt",
                "Ze daalt",
                "Ze blijft gelijk",
                "Dat kan je niet weten"], 0,
               "Minder aanbod en meer vraag duwen de prijs allebei omhoog."),
        ],
    ),
    tabel("Welke maatregel van de overheid is dit?", [
        ("een extra belasting op tabak", "btw en accijnzen"),
        ("een premie voor een warmtepomp", "premies en subsidies"),
        ("een hoogste toegelaten huurprijs", "minimum- en maximumprijzen"),
        ("een bodemprijs voor melk voor boeren", "minimum- en maximumprijzen"),
    ], "Drie soorten overheidsmaatregelen.",
       kolommen=["btw en accijnzen", "premies en subsidies", "minimum- en maximumprijzen"]),
    tabel("Wat geeft deze vaste prijs?", [
        ("een minimumprijs boven het evenwicht", "overschot"),
        ("een maximumprijs onder het evenwicht", "tekort"),
        ("een maximumprijs boven het evenwicht", "geen effect"),
        ("een minimumprijs onder het evenwicht", "geen effect"),
    ], "Een vaste prijs werkt enkel als ze de markt belet het evenwicht te bereiken.",
       kolommen=["overschot", "tekort", "geen effect"]),
    casus(
        "Op de markt van studentenkamers is de evenwichtshuur 500 euro per maand. Bij 500 euro "
        "worden 800 kamers verhuurd. De stad legt een maximumhuur van 400 euro op. Bij 400 euro "
        "willen 1000 studenten een kamer, maar bieden de eigenaars maar 650 kamers aan.",
        [
            inv("Hoe groot is het tekort aan kamers?", ["350", "350 kamers"], "1000 min 650."),
            mk("Waarom voert de stad deze maximumprijs in?",
               ["Om kamers betaalbaar te houden",
                "Om meer eigenaars aan te trekken",
                "Om een overschot aan kamers weg te werken",
                "Om de eigenaars een hoger inkomen te geven"], 0,
               "Een maximumprijs beschermt de kopers, hier de studenten."),
            keuze("Door de maximumhuur worden er [[*minder|meer]] kamers verhuurd dan zonder ingrijpen.",
                  "Eigenaars bieden er nog maar 650 aan in plaats van 800."),
        ],
    ),
    mk("Waarom legt de overheid accijnzen op alcohol?",
       ["Om het gebruik bewust te ontmoedigen",
        "Om alcohol voor iedereen betaalbaar te houden",
        "Om een tekort aan alcohol weg te werken",
        "Om de producenten een minimuminkomen te geven"], 0,
       "Een accijns maakt het product duurder, zodat er minder van gekocht wordt."),
    keuze("Een belasting op een product doet de aanbodcurve naar [[*links|rechts]] schuiven en de prijs [[*stijgen|dalen]].",
          "Verkopen wordt duurder voor de aanbieder."),
    mk("De overheid geeft een premie aan wie zonnepanelen koopt. Wat verwacht je op die markt?",
       ["Meer vraag: een hogere prijs en meer panelen",
        "Minder vraag: een lagere prijs en minder panelen",
        "Meer aanbod: een lagere prijs en meer panelen",
        "Geen verandering, want de prijs blijft gelijk"], 0,
       "Een premie voor kopers verschuift de vraag naar rechts."),
    sleep("Een vaste prijs boven het evenwicht heet een [[minimumprijs]] en geeft een [[overschot]].",
          ["maximumprijs", "tekort"], "Een maximumprijs onder het evenwicht geeft een tekort."),
    tabel("Klopt dit over verschuivingen en prijzen?", [
        ("Een prijsdaling van het product zelf verschuift de vraagcurve.", F),
        ("Meer kopers verschuiven de vraagcurve naar rechts.", J),
        ("Als de vraag naar rechts schuift, daalt de evenwichtsprijs.", F),
        ("Een subsidie aan producenten verlaagt de prijs voor de koper.", J),
    ], "Bij meer vraag en hetzelfde aanbod stijgt de prijs."),
    volgorde("Een minimumprijs ligt boven het evenwicht. Zet de gevolgen in de juiste volgorde.", [
        "de prijs mag niet zakken tot het evenwicht",
        "verkopers bieden veel aan, kopers kopen minder",
        "er ontstaat een overschot",
    ], "Daarom koopt de overheid soms zelf het overschot op."),
    met_prent(VS.bestand, tabel("Welke gebeurtenis brengt de markt van E naar dit punt?", [
        ("R", "meer vraag"), ("S", "minder aanbod"), ("U", "meer aanbod"),
    ], "R ligt op V2 en A1, S op V1 en A2, U op V1 en A3.", kolommen=["meer vraag", "minder aanbod", "meer aanbod"])),
    met_prent(VS.bestand, keuze("Van E naar S stijgt de prijs en [[*daalt|stijgt]] de verhandelde hoeveelheid.",
              "S ligt hoger en meer naar links dan E.")),
    mk("Een vergelijkbaar product wordt veel goedkoper. Wat gebeurt er met de vraagcurve van ons product?",
       ["Ze schuift naar links",
        "Ze schuift naar rechts",
        "Je beweegt langs dezelfde curve",
        "De aanbodcurve schuift naar links"], 0,
       "Kopers stappen over naar het goedkopere alternatief."),
    koppel("Koppel elke maatregel aan zijn gevolg op de markt.", [
        ["accijns", "aanbod naar links, hogere prijs"],
        ["subsidie aan producenten", "aanbod naar rechts, lagere prijs"],
        ["maximumprijs onder het evenwicht", "tekort"],
        ["minimumprijs boven het evenwicht", "overschot"],
    ], ["vraag naar links, hogere prijs"], "Drie soorten overheidsmaatregelen met elk hun gevolg."),
    inv("De evenwichtsprijs van melk is 30 cent per liter. De overheid legt een minimumprijs van 40 cent op. Bij 40 cent bieden boeren 900 000 liter aan en kopen de klanten 600 000 liter. Hoe groot is het overschot, in liter?",
        ["300000", "300 000", "300.000"], "900 000 min 600 000."),
    sorteer("Beschermt deze maatregel vooral de kopers of vooral de producenten?", ["Kopers", "Producenten"], [
        ["een maximumprijs voor energie", "Kopers"],
        ["een bodemprijs voor graan", "Producenten"],
        ["een maximumhuur", "Kopers"],
        ["een minimumprijs voor melk", "Producenten"],
    ], "Een maximumprijs houdt iets betaalbaar, een minimumprijs garandeert een inkomen."),
    tabel("Is dit een maatregel van de overheid volgens het leerdoel?", [
        ("btw en accijnzen heffen", J),
        ("premies en subsidies geven", J),
        ("minimum- en maximumprijzen invoeren", J),
        ("de productie van alle bedrijven overnemen", F),
    ], "Drie soorten maatregelen."),
    open_("Leg uit waarom een maximumprijs voor huur goed bedoeld is, maar toch een probleem kan geven.",
          "De maximumprijs houdt huren betaalbaar voor wie al een woning vindt. Maar omdat ze onder het evenwicht ligt, willen meer mensen huren dan er woningen aangeboden worden: er ontstaat een tekort, en sommigen vinden niets."),
]
