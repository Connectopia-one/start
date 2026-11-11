# -*- coding: utf-8 -*-
"""De leerbundels voor bedrijfswetenschappen en recht op 🌍 Beyond doorstroom-niveau.

Gebaseerd op de vakfiche bedrijfswetenschappen en recht 3de graad
doorstroom (2027_bedrijfswetenschappenenrecht_3DO), richting
bedrijfswetenschappen. Dezelfde twintig thema's als de vragen in
`../../beyond/bedrijfswetenschappen-en-recht.json` (gebouwd door
`../../beyond/bron/bouw_bedrijfswetenschappen.py`).

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/bedrijfswetenschappen-en-recht.json`
doet daar het voorwerk voor.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Bedrijfswetenschappen en recht"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[slug + "-beyond-doorstroom"] = b


def boeking(regels, uitleg=None):
    """Een journaalpost als tabel: (rekeningnummer, naam, debet, credit)."""
    rijen = [[nr, ("&nbsp;&nbsp;&nbsp;&nbsp;aan " + naam) if c and not d else naam,
              d or "", c or ""] for nr, naam, d, c in regels]
    t = tabel(["rekening", "naam", "debet", "credit"], rijen)
    return t + (f"<p style='margin-top:6px'>{uitleg}</p>" if uitleg else "")


# ───────────────────────── 1. Ondernemingsvormen vergelijken
zet("ondernemingsvormen-vergelijken",
    titel="Ondernemingsvormen vergelijken",
    onder="Eenmanszaak, maatschap, bv, nv en cv naast elkaar: oprichting, aansprakelijkheid, aandelen, belasting en boekhouding.",
    secties=[
        dict(kop="Met of zonder rechtspersoonlijkheid", blokken=[
            ("p", "Bij een <strong>eenmanszaak</strong> vallen de onderneming en de ondernemer samen: er is <strong>geen eigen rechtspersoonlijkheid</strong>. "
                  "Ook een <strong>maatschap</strong> is geen rechtspersoon. Een maatschap is een overeenkomst tussen minstens twee personen, vaak vrije beroepen die samenwerken, bijvoorbeeld artsen. "
                  "Zonder rechtspersoonlijkheid ben je <strong>onbeperkt</strong> aansprakelijk: ook met je privévermogen (je huis, je spaargeld)."),
            ("p", "Een <strong>bv</strong>, <strong>nv</strong> en <strong>cv</strong> zijn vennootschappen <strong>met rechtspersoonlijkheid</strong>. Ze bieden <strong>beperkte aansprakelijkheid</strong>: "
                  "een aandeelhouder kan hoogstens zijn inbreng verliezen; zijn privévermogen blijft beschermd tegen de schuldeisers van de vennootschap."),
        ]),
        dict(kop="De vormen naast elkaar", blokken=[
            ("kader", tabel(["", "eenmanszaak", "maatschap", "bv", "nv", "cv"],
                            [["oprichters", "één", "minstens twee", "minstens één", "minstens één", "minstens drie"],
                             ["oprichting", "inschrijving in de Kruispuntbank van Ondernemingen, geen akte", "onderhandse akte mag", "authentieke akte bij de notaris", "authentieke akte bij de notaris", "authentieke akte bij de notaris"],
                             ["minimumkapitaal", "geen", "geen", "geen (wel toereikend aanvangsvermogen en financieel plan)", "61 500 euro", "geen"],
                             ["aansprakelijkheid", "onbeperkt", "onbeperkt", "beperkt", "beperkt", "beperkt"],
                             ["aandelen", "–", "–", "standaard beperkt overdraagbaar; statuten kunnen dat vrijer maken", "in principe vrij overdraagbaar", "beperkt overdraagbaar (standaard enkel naar andere aandeelhouders)"],
                             ["belasting op de winst", "personenbelasting (progressief)", "personenbelasting van de vennoten", "vennootschapsbelasting", "vennootschapsbelasting", "vennootschapsbelasting"],
                             ["boekhouding", "bij kleine omzet een vereenvoudigde of enkelvoudige boekhouding", "", "dubbele boekhouding", "dubbele boekhouding", "dubbele boekhouding"],
                             ["jaarrekening", "moet geen jaarrekening neerleggen", "", "bij de Nationale Bank", "bij de Nationale Bank", "bij de Nationale Bank"]])),
        ]),
        dict(kop="Wat je moet onthouden per vorm", blokken=[
            ("kader", "<ul><li><strong>bv:</strong> sinds het Wetboek van vennootschappen en verenigingen <strong>geen minimumkapitaal</strong> meer (vroeger 18 550 euro). In de plaats: een <strong>toereikend aanvangsvermogen en een financieel plan</strong>. "
                      "Gaat de bv binnen drie jaar failliet met een duidelijk ontoereikend aanvangsvermogen, dan kunnen de oprichters aansprakelijk gesteld worden: <strong>oprichtersaansprakelijkheid</strong>. "
                      "Zonder andere regeling in de statuten moeten de andere aandeelhouders akkoord gaan als je aandelen aan buitenstaanders wil overdragen.</li>"
                      "<li><strong>nv:</strong> de enige met een minimumkapitaal (61 500 euro). Eén oprichter volstaat. De aandelen zijn vrij overdraagbaar: dat is nodig voor een <strong>beursnotering</strong>, dus past de nv bij een grote onderneming die naar de beurs wil.</li>"
                      "<li><strong>cv (coöperatieve vennootschap):</strong> een samenwerking met een coöperatief doel: minstens drie oprichters, geen minimumkapitaal, beperkte aansprakelijkheid. De aandelen zijn beperkt overdraagbaar, zodat de samenwerking tussen de leden behouden blijft.</li>"
                      "<li><strong>maatschap:</strong> eenvoudig op te richten en fiscaal transparant: elke vennoot geeft zijn deel van de winst aan in zijn personenbelasting. Geen minimumkapitaal.</li></ul>"),
            ("p", "Een vennootschap betaalt zelf <strong>vennootschapsbelasting</strong> (venb). De winst van een eenmanszaak is inkomen van de ondernemer: "
                  "<strong>progressieve personenbelasting</strong>, dus hoe hoger de winst, hoe hoger het tarief op de hoogste schijf. De balanscentrale van de Nationale Bank maakt de jaarrekeningen openbaar."),
            ("p", "<strong>Nadeel</strong> van een vennootschap tegenover een eenmanszaak: meer administratie en kosten bij de oprichting (notaris, dubbele boekhouding, jaarrekening)."),
        ]),
        dict(kop="Kiezen", blokken=[
            ("kader", tabel(["situatie", "beste vorm", "waarom"],
                            [["iemand start alleen en wil haar privévermogen beschermen", "bv", "kan met één oprichter, beperkte aansprakelijkheid (een cv vraagt drie oprichters)"],
                             ["een vriendengroep met een coöperatief doel, zonder groot startkapitaal", "cv", "samenwerking, geen minimumkapitaal, beperkte aansprakelijkheid"],
                             ["een grote onderneming die naar de beurs wil", "nv", "vrij overdraagbare aandelen"],
                             ["artsen die samenwerken", "maatschap", "eenvoudig en fiscaal transparant"]])),
        ]),
    ],
    onthoud=[
        "Geen rechtspersoonlijkheid (eenmanszaak, maatschap): onbeperkt aansprakelijk, personenbelasting.",
        "bv, nv, cv: rechtspersoon, beperkte aansprakelijkheid, vennootschapsbelasting, dubbele boekhouding, jaarrekening bij de Nationale Bank.",
        "Enkel de nv heeft een minimumkapitaal: 61 500 euro. De bv heeft een toereikend aanvangsvermogen en een financieel plan.",
        "Oprichters: bv en nv minstens één, cv minstens drie, maatschap minstens twee.",
        "Aandelen: nv vrij, bv standaard beperkt, cv het meest beperkt.",
    ])


# ───────────────────────── 2. De personenbelasting
zet("de-personenbelasting",
    titel="De personenbelasting",
    onder="Wie betaalt ze, op welke inkomsten, hoe verloopt de aangifte en hoe reken je met schijven.",
    secties=[
        dict(kop="Wat en wie", blokken=[
            ("p", "De <strong>personenbelasting</strong> is de belasting op het inkomen van de <strong>inwoners van België</strong>. Er zijn vier soorten inkomsten:"),
            ("kader", tabel(["soort inkomsten", "voorbeelden"],
                            [["onroerende inkomsten", "inkomsten uit gebouwen en gronden, zoals de huur van een woning die je verhuurt"],
                             ["roerende inkomsten", "inkomsten uit beleggingen: dividenden en interesten"],
                             ["beroepsinkomsten", "het loon van een werknemer, winsten en baten van zelfstandigen (ook de winst van een eenmanszaak)"],
                             ["diverse inkomsten", "een restgroep, zoals een occasionele winst"]])),
        ]),
        dict(kop="Van inkomen tot aanslagbiljet", blokken=[
            ("fig", svg.stappen(["inkomen verdienen", "aangifte", "aanslagbiljet", "betalen of|terugkrijgen"]), "De volgorde."),
            ("kader", "<ul><li>Het <strong>inkomstenjaar</strong> is het jaar waarin je het inkomen verdient. Het <strong>aanslagjaar</strong> is het jaar erna: dan doe je aangifte en volgt de berekening. Loon uit 2026 hoort bij aanslagjaar 2027. Ze zijn dus nooit hetzelfde jaar.</li>"
                      "<li>Wie een aangifteformulier krijgt, is verplicht om aangifte te doen, meestal in het aanslagjaar, rond de zomer (het formulier en Tax-on-web openen in het voorjaar). Wie te laat aangifte doet, kan een boete krijgen.</li>"
                      "<li>Online dien je je aangifte in met <strong>Tax-on-web</strong> van de FOD Financiën (via MyMinfin).</li>"
                      "<li>Bij een <strong>voorstel van vereenvoudigde aangifte</strong> vult de FOD Financiën alles vooraf in. Klopt alles en ben je akkoord, dan hoef je niets te doen.</li>"
                      "<li>Het <strong>aanslagbiljet</strong> toont de berekening: het belastbaar inkomen, de belasting, de voorheffingen en het saldo: of je moet bijbetalen of terugkrijgt.</li></ul>"),
            ("p", "De winst van een eenmanszaak valt onder de progressieve personenbelasting. De <strong>bedrijfsvoorheffing</strong> is een voorschot op de belasting, ingehouden op je loon. De werkgever stort ze elke maand door aan de overheid. "
                  "Op het aanslagbiljet worden de ingehouden bedrijfsvoorheffingen afgetrokken van de berekende belasting. Was de voorheffing hoger dan de verschuldigde belasting, dan krijg je het verschil terug. "
                  "Een positief saldo te betalen betekent dat je nog belasting moet bijbetalen. Daarbovenop komt de <strong>gemeentebelasting</strong>: een percentage van de personenbelasting dat elke gemeente zelf kiest."),
        ]),
        dict(kop="Rekenen met schijven", blokken=[
            ("p", "Je betaalt niet op het brutoloon: eerst gaan onder meer de sociale bijdragen en de beroepskosten eraf. Dan blijft het <strong>belastbaar inkomen</strong> over. "
                  "De personenbelasting is <strong>progressief</strong>: het inkomen wordt in <strong>schijven</strong> verdeeld met stijgende tarieven. "
                  "Het hoogste tarief geldt enkel voor het deel van je inkomen dat in de hoogste schijf valt, niet op je volledige inkomen."),
            ("kader", tabel(["schijf", "tarief", "op 30 000 euro"],
                            [["0 tot 15 000 euro", "25 %", "15 000 · 0,25 = 3 750"],
                             ["15 000 tot 26 000 euro", "40 %", "11 000 · 0,40 = 4 400"],
                             ["boven 26 000 euro", "45 %", "4 000 · 0,45 = 1 800"],
                             ["<strong>samen</strong>", "", "<strong>9 950 euro</strong>"]])),
            ("p", "Met enkel 25 % en 40 % (grens 15 000 euro) geeft 20 000 euro: 3 750 + 5 000 · 0,40 = <strong>5 750 euro</strong>. 12 000 euro valt volledig in de eerste schijf: 12 000 · 0,25 = 3 000 euro."),
            ("p", "De <strong>belastingvrije som</strong> is het deel van je inkomen zonder belasting. Iedereen heeft een basisbedrag; het wordt <strong>hoger</strong> per kind ten laste. "
                  "Een hogere belastingvrije som betekent minder belasting. Rekenvoorbeeld: belastingvrije som 10 000 euro, verrekend aan 25 %, geeft 2 500 euro. 9 950 − 2 500 = <strong>7 450 euro</strong>."),
            ("p", "Stijgt je belastbaar inkomen van 40 000 naar 41 000 euro bij een hoogste tarief van 45 %, dan valt die extra 1 000 euro volledig in de hoogste schijf: 450 euro extra belasting. "
                  "Om de belasting te berekenen heb je het belastbaar inkomen, de belastingschijven en de belastingvrije som nodig."),
        ]),
        dict(kop="Aftrek en vermindering", blokken=[
            ("p", "Een <strong>belastingaftrek</strong> verlaagt het <strong>inkomen</strong>, een <strong>belastingvermindering</strong> verlaagt de berekende <strong>belasting</strong>. Voorbeelden van voordelen:"),
            ("kader", "<ul><li><strong>Giften</strong> aan een erkende instelling, vanaf een minimumbedrag per jaar. Ze tellen enkel met een <strong>fiscaal attest</strong>; de instelling bezorgt dat ook rechtstreeks aan de FOD Financiën.</li>"
                      "<li><strong>Pensioensparen</strong>: belastingvermindering op de stortingen, tot een maximumbedrag per jaar.</li>"
                      "<li>De kosten van <strong>kinderopvang</strong> voor erkende opvang van jonge kinderen.</li></ul>"),
        ]),
    ],
    onthoud=[
        "Vier soorten: onroerende, roerende, beroeps- en diverse inkomsten.",
        "Inkomstenjaar: je verdient. Aanslagjaar (het jaar erna): aangifte en berekening.",
        "Progressief: elke schijf zijn eigen tarief; het hoogste tarief enkel op het deel in de hoogste schijf.",
        "Bedrijfsvoorheffing = voorschot; verrekend op het aanslagbiljet.",
        "Aftrek verlaagt het inkomen, vermindering verlaagt de belasting.",
    ])


# ───────────────────────── 3. De vennootschapsbelasting en de voorafbetalingen
zet("de-vennootschapsbelasting-en-de-voorafbetalingen",
    titel="De vennootschapsbelasting en de voorafbetalingen",
    onder="Hoe een vennootschap belast wordt, het verschil met een eenmanszaak, en hoe voorafbetalingen een vermeerdering vermijden.",
    secties=[
        dict(kop="Grondslag en tarief", blokken=[
            ("p", "Een vennootschap betaalt vennootschapsbelasting op haar <strong>belastbare winst</strong> van het boekjaar, niet op de omzet: omzet is de verkoop, winst is wat er overblijft na de kosten. "
                  "Het tarief is <strong>vast</strong> (niet progressief), met een <strong>verlaagd tarief</strong> op een eerste schijf voor kleine vennootschappen die aan bepaalde voorwaarden voldoen."),
            ("kader", tabel(["voorbeeld", "berekening", "belasting"],
                            [["winst 80 000 euro, tarief 25 %", "80 000 · 0,25", "20 000 euro"],
                             ["winst 60 000 euro, tarief 20 %", "60 000 · 0,20", "12 000 euro"],
                             ["kleine vennootschap, winst 150 000 euro: 20 % op de eerste 100 000 euro, 25 % op de rest", "20 000 + 50 000 · 0,25 = 20 000 + 12 500", "32 500 euro"],
                             ["idem, winst 200 000 euro", "20 000 + 100 000 · 0,25", "45 000 euro"]])),
        ]),
        dict(kop="Boekjaar en aanslagjaar", blokken=[
            ("p", "Het <strong>boekjaar</strong> is de periode van twaalf maanden waarover de boekhouding loopt. Het kan samenvallen met het kalenderjaar, maar dat hoeft niet. "
                  "Zowel de vennootschapsbelasting als de personenbelasting gebruiken het begrip <strong>aanslagjaar</strong>: bij de personenbelasting volgt het op het inkomstenjaar, bij de vennootschapsbelasting hangt het af van de datum waarop het boekjaar afsluit."),
            ("kader", tabel(["boekjaar", "afsluiting", "aanslagjaar"],
                            [["1 januari tot 31 december 2026", "op 31 december: het volgende jaar", "2027"],
                             ["1 juli 2025 tot 30 juni 2026", "niet op 31 december: het jaar van de afsluiting", "2026"],
                             ["1 april 2026 tot 31 maart 2027", "niet op 31 december: het jaar van de afsluiting", "2027"]])),
        ]),
        dict(kop="Eenmanszaak of vennootschap", blokken=[
            ("kader", tabel(["", "eenmanszaak", "vennootschap"],
                            [["belasting", "personenbelasting, geen eigen aangifte vennootschapsbelasting", "vennootschapsbelasting"],
                             ["grondslag", "zijn totale belastbare inkomen: de winst telt samen met zijn andere inkomsten", "de belastbare winst"],
                             ["tarief", "progressief: bij stijgende winst stijgt het gemiddelde tarief, want een groter deel valt in de hogere schijven (tot 50 %)", "vast tarief"],
                             ["voorafbetalingen", "kan ook voorafbetalen; voordeel heet een bonificatie", "voorafbetalingen verlagen de vermeerdering"]])),
            ("p", "Bij een <strong>hoge winst</strong> (bijvoorbeeld 120 000 euro) kan een vennootschap voordeliger zijn: het vaste tarief ligt lager dan de hoogste schijven van de personenbelasting. "
                  "Vergelijk je beide, kijk dan naar de grondslag van de belasting, de progressiviteit en de voorafbetalingen."),
        ]),
        dict(kop="Voorafbetalingen", blokken=[
            ("p", "<strong>Voorafbetalingen</strong> (VA) zijn voorschotten op de belasting tijdens het jaar zelf, geen extra belasting: ze worden verrekend met de belasting die je verschuldigd bent. "
                  "Bij een boekjaar gelijk aan het kalenderjaar zijn er <strong>vier</strong> vervaldagen: <strong>10 april, 10 juli, 10 oktober en 20 december</strong>."),
            ("p", "Wie te weinig voorafbetaalt, krijgt een <strong>belastingvermeerdering</strong>. Wie niets voorafbetaalt, betaalt de volledige belasting pas na de aanslag, plus die vermeerdering. "
                  "Elke voorafbetaling geeft een voordeel: een percentage dat daalt naarmate ze later in het jaar valt. Een vroege voorafbetaling telt dus zwaarder: de eerste verlaagt de vermeerdering het meest. "
                  "Meer en vroeger voorafbetalen verlaagt de vermeerdering."),
            ("kader", tabel(["geval", "vermeerdering", "voordeel VA", "over"],
                            [["belasting 20 000 euro, geen VA, 9 %", "20 000 · 0,09 = 1 800", "0", "1 800 euro"],
                             ["belasting 20 000 euro, VA1 15 000 euro aan 12 %", "1 800", "15 000 · 0,12 = 1 800", "0 euro"],
                             ["belasting 40 000 euro, VA1 10 000 aan 12 %, VA2 10 000 aan 10 %", "40 000 · 0,09 = 3 600", "1 200 + 1 000 = 2 200", "1 400 euro"]])),
            ("p", "In de vennootschapsbelasting daalt de vermeerdering hoogstens tot <strong>nul</strong>: je krijgt er geen geld bij. In de personenbelasting kan een zelfstandige wel een <strong>bonificatie</strong> krijgen: een voordeel, geen boete. "
                  "Een startende kleine vennootschap krijgt de eerste drie boekjaren geen vermeerdering, om starters te helpen."),
        ]),
    ],
    onthoud=[
        "Vennootschapsbelasting: vast tarief op de belastbare winst; verlaagd tarief enkel voor kleine vennootschappen.",
        "Personenbelasting: progressief op het totale belastbare inkomen.",
        "Aanslagjaar: afsluiting op 31 december geeft het jaar erna, anders het jaar van de afsluiting.",
        "Vier voorafbetalingen: 10 april, 10 juli, 10 oktober, 20 december. Vroeger = meer voordeel.",
        "Vermeerdering − voordeel van de VA, hoogstens tot nul.",
    ])


# ───────────────────────── 4. Aankopen boeken
zet("aankopen-boeken-facturen-kortingen-kosten-en-btw",
    titel="Aankopen boeken: facturen, kortingen, kosten en btw",
    onder="Een aankoopfactuur ontleden en boeken met het MAR: handelskorting, financiële korting, bijkomende kosten, verpakking, btw en creditnota's.",
    secties=[
        dict(kop="De basisregels van de dubbele boekhouding", blokken=[
            ("kader", tabel(["soort rekening", "stijging (+)", "daling (−)"],
                            [["actief (A)", "debet", "credit"],
                             ["passief (P)", "credit", "debet"],
                             ["kost (K)", "debet", ""],
                             ["opbrengst (O)", "credit", ""]])),
            ("p", "In een correcte boeking is het <strong>totaal debet altijd gelijk aan het totaal credit</strong>: dat is het principe van de dubbele boekhouding. "
                  "Een rekeningnummer uit het MAR (minimumindelingsschema) bestaat op het examen uit <strong>vijf</strong> cijfers, bijvoorbeeld 60400 Aankopen handelsgoederen."),
            ("p", "Het <strong>journaal</strong> zet alle boekingen in één lijst, in de volgorde van de datum. Het <strong>grootboek</strong> ordent de boekingen per rekening: "
                  "elke rekening heeft een debet- en een creditkant, zoals een T-rekening."),
            ("p", "In een <strong>redeneerschema</strong> redeneer je per rekening voor je boekt: rekeningnummer, soort rekening (A, P, K of O), plus of min, debet of credit. "
                  "De soort wordt op het examen niet beoordeeld; enkel nummer, bedrag en D of C tellen."),
            ("kader", tabel(["rekening", "soort", "+ of −", "D of C"],
                            [["60400 Aankopen handelsgoederen", "K", "+", "D"],
                             ["41100 Terug te vorderen btw", "A (vordering op de staat)", "+", "D"],
                             ["44000 Leveranciers", "P (schuld, klasse 4: op ten hoogste een jaar)", "+", "C"]])),
        ]),
        dict(kop="Welke rekening, en kortingen en kosten op de factuur", blokken=[
            ("kader", tabel(["aankoop", "rekening"],
                            [["handelsgoederen (om door te verkopen)", "60400 Aankopen handelsgoederen: een kost, klasse 6"],
                             ["energie (elektriciteit), huur van het magazijn, telefoon, kantoorpapier", "klasse 61, diensten en diverse goederen"],
                             ["een computer, een machine, een bestelwagen: gebruik je meerdere jaren", "een rekening van klasse 2, vaste activa"],
                             ["de btw op elke aankoopfactuur, ook bij een investering", "41100 Terug te vorderen btw (niet 45100 Te betalen btw)"],
                             ["de schuld", "44000 Leveranciers"]])),

            ("kader", "<ul><li><strong>Handelskorting</strong>: zie je op de factuur en verlaagt meteen het aankoopbedrag. Je boekt het nettobedrag op 60400, niet apart op een opbrengstrekening.</li>"
                      "<li><strong>Bijkomende kosten</strong> op de factuur (vervoerskosten, verzekering tijdens het vervoer) horen bij de aankoopwaarde en verhogen het bedrag op 60400.</li>"
                      "<li><strong>Financiële korting</strong> (korting voor contante betaling): hangt af van wanneer je betaalt. De btw wordt berekend alsof de korting gebruikt wordt, maar je boekt de factuur aan het volle bedrag: de korting is nog niet verworven. Pas bij de betaling blijkt of je ze gebruikt.</li>"
                      "<li><strong>Terugstuurbare verpakking</strong>: zonder btw (je krijgt het bedrag terug als je ze terugstuurt). Ze komt op een aparte regel, als vordering op de leverancier.</li></ul>"),
            ("kader", tabel(["factuur", "berekening"],
                            [["handelsgoederen 2 000 euro, handelskorting 10 %", "2 000 · 0,90 = 1 800 euro"],
                             ["handelsgoederen 5 000 euro, handelskorting 10 %, vervoer 100 euro", "4 500 + 100 = 4 600 euro op 60400"],
                             ["netto 1 000 euro, financiële korting 2 %, btw 21 %", "btw op 1 000 − 20 = 980 euro: 980 · 0,21 = 205,80 euro; 44000: 1 000 + 205,80 = 1 205,80 euro"]])),
        ]),
        dict(kop="Voorbeeld: aankoopfactuur", blokken=[
            ("p", "Handelsgoederen 3 000 euro, handelskorting 5 %, btw 21 %, geen financiële korting. Netto: 3 000 · 0,95 = 2 850 euro. Btw: 2 850 · 0,21 = 598,50 euro."),
            ("kader", boeking([("60400", "Aankopen handelsgoederen", "2 850,00", None),
                               ("41100", "Terug te vorderen btw", "598,50", None),
                               ("44000", "Leveranciers", None, "3 448,50")])),
            ("p", "Bij een gewone aankoopfactuur staan 60400 en 41100 dus <strong>debet</strong> en 44000 Leveranciers <strong>credit</strong>. "
                  "Bij een factuur voor huur boek je debet een rekening van klasse 61 en 41100; de schuld komt credit op 44000."),
        ]),
        dict(kop="Inkomende creditnota", blokken=[
            ("p", "Stuur je handelsgoederen terug, dan krijg je een <strong>creditnota</strong>. Die <strong>verlaagt</strong> de schuld: 44000 staat debet; de aankoop en de terug te vorderen btw dalen en staan credit. "
                  "Voorbeeld: 200 euro handelsgoederen terug, btw 21 %:"),
            ("kader", boeking([("44000", "Leveranciers", "242,00", None),
                               ("60400", "Aankopen handelsgoederen", None, "200,00"),
                               ("41100", "Terug te vorderen btw", None, "42,00")])),
        ]),
    ],
    onthoud=[
        "Actief en kost +: debet. Passief en opbrengst +: credit. Totaal debet = totaal credit.",
        "60400 handelsgoederen, klasse 61 diensten, klasse 2 investeringen, 41100 btw, 44000 leveranciers.",
        "Handelskorting en bijkomende kosten zitten in het bedrag op 60400.",
        "Financiële korting: btw op het bedrag na korting, maar de factuur aan het volle bedrag boeken.",
        "Creditnota: omgekeerde boeking, 44000 debet.",
    ])


# ───────────────────────── 5. Verkopen, betalingen en geldbewegingen boeken
zet("verkopen-betalingen-en-geldbewegingen-boeken",
    titel="Verkopen, betalingen en geldbewegingen boeken",
    onder="Verkoopfacturen, uitgaande creditnota's, dagontvangsten, betalingen via bank en kas, en interne overboekingen.",
    secties=[
        dict(kop="De verkoopfactuur", blokken=[
            ("kader", tabel(["rekening", "wat", "kant"],
                            [["40000 Handelsdebiteuren", "de klant moet nog betalen: je vordering stijgt", "debet"],
                             ["70000 Verkopen handelsgoederen", "een opbrengst (klasse 7)", "credit"],
                             ["45100 Te betalen btw", "btw die je moet doorstorten aan de staat: een schuld, geen opbrengst", "credit"]])),
            ("p", "De <strong>handelskorting</strong> verlaagt meteen het bedrag op 70000: je boekt niet eerst bruto en dan de korting apart. "
                  "Doorgerekende <strong>vervoerskosten</strong> horen bij de maatstaf van heffing: ook daarop komt btw, aan het tarief van de goederen. "
                  "<strong>Terugstuurbare verpakking</strong> staat op een aparte regel, zonder btw: de klant krijgt het bedrag terug als hij ze terugbrengt."),
            ("p", "Voorbeeld: 4 000 euro handelsgoederen, handelskorting 5 %, btw 21 %. Netto 4 000 · 0,95 = 3 800 euro; btw 3 800 · 0,21 = 798 euro."),
            ("kader", boeking([("40000", "Handelsdebiteuren", "4 598,00", None),
                               ("70000", "Verkopen handelsgoederen", None, "3 800,00"),
                               ("45100", "Te betalen btw", None, "798,00")])),
            ("p", "<strong>Met financiële korting:</strong> netto 2 000 euro, 2 % korting mogelijk. De btw wordt berekend alsof de korting gebruikt wordt: op 2 000 − 40 = 1 960 euro, dus 411,60 euro. "
                  "Op 40000 komt het volle bedrag: 2 000 + 411,60 = 2 411,60 euro."),
        ]),
        dict(kop="Uitgaande creditnota", blokken=[
            ("p", "Stuurt een klant goederen terug, dan maakt de verkoper een <strong>uitgaande creditnota</strong> (voor de klant is het een inkomende). De verkoop en de te betalen btw dalen (debet), de vordering op de klant daalt (credit). "
                  "Voorbeeld: 300 euro goederen, btw 21 %:"),
            ("kader", boeking([("70000", "Verkopen handelsgoederen", "300,00", None),
                               ("45100", "Te betalen btw", "63,00", None),
                               ("40000", "Handelsdebiteuren", None, "363,00")])),
        ]),
        dict(kop="Dagontvangsten", blokken=[
            ("p", "<strong>Dagontvangsten</strong> zijn kleinhandelsverkopen zonder factuur: een bakker verkoopt brood aan de toog en noteert het totaal van de dag. Niet elke klant krijgt een factuur. "
                  "De btw zit in het bedrag: deel door 1,21. 1 210 / 1,21 = 1 000 euro verkoop en 210 euro btw; 2 420 / 1,21 = 2 000 euro, btw 420 euro. In contanten staat <strong>57000 Kassen</strong> debet."),
        ]),
        dict(kop="Betalingen via bank en kas", blokken=[
            ("kader", tabel(["verrichting", "debet", "credit"],
                            [["een klant betaalt via de bank", "55000 Kredietinstellingen", "40000 Handelsdebiteuren"],
                             ["een klant betaalt contant aan de kassa (121 euro)", "57000 Kassen", "40000 Handelsdebiteuren"],
                             ["je betaalt een leverancier via de bank", "44000 Leveranciers (de schuld daalt)", "55000 Kredietinstellingen"],
                             ["een postzegel betaald uit de kas", "kostenrekening", "57000 Kassen"]])),
            ("p", "Een contante betaling uit of in de kas boek je met een <strong>kasstuk</strong>: elk kasdocument toont een ontvangst of een uitgave in contanten."),
            ("p", "<strong>Financiële korting bij de betaling.</strong> Een klant betaalt een factuur van 1 205,80 euro binnen de termijn met 2 % op 1 000 euro: 1 205,80 − 20 = 1 185,80 euro. "
                  "40000 staat credit voor het volle bedrag (de volledige vordering verdwijnt), 55000 debet voor het betaalde bedrag. De toegekende financiële korting is voor de verkoper een <strong>kost</strong> (hij ontvangt minder geld dan de vordering): die 20 euro staat debet. "
                  "Betaalt de klant na de kortingstermijn, dan verliest hij de korting en betaalt hij het volle bedrag."),
        ]),
        dict(kop="Interne overboekingen", blokken=[
            ("p", "<strong>58000 Interne overboekingen</strong> is een tussenrekening voor geld tussen bank en kas. Kas en bank boeken elk in hun eigen dagboek; via 58000 boek je dezelfde verrichting niet twee keer. "
                  "Je haalt 500 euro van de bank voor de kas:"),
            ("kader", tabel(["boeking", "debet", "credit"],
                            [["bankuittreksel", "58000 Interne overboekingen 500", "55000 Kredietinstellingen 500 (de bank daalt)"],
                             ["kasstuk", "57000 Kassen 500", "58000 Interne overboekingen 500"]])),
            ("p", "Na beide boekingen is het saldo van 58000 nul: het geld is enkel van plaats veranderd. Het totaal van de liquide middelen verandert niet. "
                  "Breng je geld van de kas naar de bank, dan gebruik je 57000 Kassen, 58000 en 55000 Kredietinstellingen."),
        ]),
    ],
    onthoud=[
        "Verkoopfactuur: 40000 debet; 70000 en 45100 credit.",
        "Btw op een verkoop is een schuld aan de staat, geen opbrengst.",
        "Uitgaande creditnota: 70000 en 45100 debet, 40000 credit.",
        "Dagontvangsten: bedrag / 1,21 = verkoop zonder btw; 57000 Kassen debet.",
        "Bank ↔ kas altijd via 58000; daarna is 58000 nul.",
    ])


# ───────────────────────── 6. Investeringen, leningen, lonen en btw boeken
zet("investeringen-leningen-lonen-en-btw-boeken",
    titel="Investeringen, leningen, lonen en btw boeken",
    onder="Een investering op krediet, een lening en haar aflossing, de loonsynthese en de btw-verrekening.",
    secties=[
        dict(kop="Investeringen en leningen", blokken=[
            ("p", "Een machine wordt gekocht en betaald met een lening van de bank: dat zijn <strong>twee</strong> verrichtingen en dus twee boekingen, de factuur en de lening. "
                  "Bij een investering op krediet staat de rekening van het vast actief <strong>debet</strong> (een actief dat stijgt), met 41100 voor de btw en 44000 credit."),
            ("p", "Een lening van 50 000 euro over vijf jaar (een <strong>investeringskrediet</strong>) is <strong>vreemd vermogen</strong>: geld dat je moet terugbetalen. "
                  "Je boekt ze in rekeninggroep <strong>17 Schulden op meer dan een jaar</strong>. Als de bank het bedrag stort, staat 55000 Kredietinstellingen debet. Een lening ontvangen verhoogt de omzet niet: het is geen verkoop."),
            ("kader", tabel(["moment", "boeking"],
                            [["de bank stort de lening", "55000 Kredietinstellingen debet, 17 Schulden op meer dan een jaar credit"],
                             ["einde van het jaar", "het deel dat binnen het jaar vervalt, verhuist naar groep 42 (schulden op meer dan een jaar die binnen het jaar vervallen): bij 100 000 euro in vijf gelijke delen is dat 20 000 euro"],
                             ["aflossing: 10 000 kapitaal en 1 500 interest", "42 debet 10 000 (de schuld daalt), 65 Financiële kosten debet 1 500, 55000 credit 11 500"]])),
            ("p", "Het kapitaal terugbetalen is <strong>geen kost</strong>: bank en schuld dalen allebei, het eigen vermogen blijft gelijk. Enkel de <strong>interest</strong> is een kost: een financiële kost, groep 65."),
        ]),
        dict(kop="Lonen", blokken=[
            ("kader", tabel(["begrip", "uitleg"],
                            [["brutoloon", "een kost voor de werkgever: groep 62 Bezoldigingen en sociale lasten (niet 60400)"],
                             ["RSZ werknemer", "ingehouden op het brutoloon, bv. 13,07 %: 3 000 · 0,1307 = 392,10 euro"],
                             ["bedrijfsvoorheffing", "ingehouden op het loon; een schuld van de werkgever aan de fiscus, die hij doorstort"],
                             ["nettoloon", "brutoloon − RSZ werknemer − bedrijfsvoorheffing: wat de werknemer echt op zijn rekening krijgt"],
                             ["werkgeversbijdrage RSZ", "betaalt de werkgever <strong>bovenop</strong> het brutoloon: een extra kost, niet afgehouden van het loon. 25 % op 4 000 euro: totale loonkost 5 000 euro"],
                             ["verplicht voorschot", "voor <strong>arbeiders</strong>: een deel van het loon halverwege de maand, later afgetrokken van het nettoloon. Bedienden worden maandelijks betaald"]])),
            ("kader", "<ul><li>Bruto 2 500, RSZ 326,75, voorheffing 400: netto 2 500 − 326,75 − 400 = <strong>1 773,25 euro</strong>.</li>"
                      "<li>Bruto 2 000, RSZ 261,40, voorheffing 300, voorschot 600: netto 1 438,60, nog uit te betalen <strong>838,60 euro</strong>.</li></ul>"),
            ("p", "De <strong>loonsynthese</strong> is het overzicht van alle lonen van de maand: brutolonen, inhoudingen, werkgeversbijdragen en netto. Veel kleine werkgevers laten ze maken door een <strong>sociaal secretariaat</strong>."),
            ("kader", tabel(["debet: kosten van de werkgever", "credit: schulden"],
                            [["brutolonen (groep 62)", "ingehouden bedrijfsvoorheffing (aan de fiscus)"],
                             ["werkgeversbijdragen RSZ (groep 62)", "RSZ-bijdragen van werknemer en werkgever (groep 45), samen doorgestort aan de RSZ"],
                             ["", "nettoloon: schuld aan het personeel"]])),
            ("p", "Ingehouden voorheffing en voorschot zijn geen extra kosten. Bij de uitbetaling van de nettolonen via de bank daalt de schuld aan het personeel (debet) en staat 55000 Kredietinstellingen credit. "
                  "De factuur van het sociaal secretariaat is een dienst: klasse 61, met de btw op 41100 Terug te vorderen btw. Bij de betaling ervan staat 44000 debet en 55000 credit."),
        ]),
        dict(kop="Btw-verrekening en -vereffening", blokken=[
            ("p", "Bij de <strong>btw-verrekening</strong> boek je de te betalen en de terug te vorderen btw tegen elkaar weg (wegboeken): 45100 Te betalen btw staat debet, 41100 Terug te vorderen btw credit. "
                  "Het saldo toont of je de staat moet betalen of geld terugkrijgt."),
            ("kader", tabel(["45100 te betalen", "41100 terug te vorderen", "gevolg"],
                            [["8 000 euro", "5 000 euro", "de onderneming stort 3 000 euro"],
                             ["4 000 euro", "6 000 euro", "de staat moet 2 000 euro terugbetalen: er is meer btw betaald bij aankopen dan aangerekend bij verkopen"]])),
            ("p", "Bij de <strong>btw-vereffening</strong> betaalt de onderneming het saldo aan de staat met een overschrijving naar de FOD Financiën: 45100 debet, 55000 credit."),
        ]),
    ],
    onthoud=[
        "Lening: groep 17; deel dat binnen het jaar vervalt naar groep 42. Interest = kost (groep 65), aflossing niet.",
        "Nettoloon = bruto − RSZ werknemer − bedrijfsvoorheffing.",
        "Loonsynthese: brutoloon en werkgeversbijdragen debet (kosten), inhoudingen en netto credit (schulden).",
        "Verplicht voorschot: enkel arbeiders.",
        "Btw-verrekening: 45100 debet, 41100 credit; het saldo betaal je of krijg je terug.",
    ])


# ───────────────────────── 7. Eindejaarsverrichtingen en de saldibalans
zet("eindejaarsverrichtingen-en-de-saldibalans",
    titel="Eindejaarsverrichtingen en de saldibalans",
    onder="Afschrijvingen, voorraadwijziging, voorzieningen, overlopende rekeningen, de belasting en de bestemming van het resultaat, tot aan de jaarrekening.",
    secties=[
        dict(kop="Van proefbalans tot jaarrekening", blokken=[
            ("fig", svg.stappen(["proefbalans", "inventaris-|verrichtingen", "definitieve|saldibalans", "jaarrekening"]), "De volgorde aan het einde van het boekjaar."),
            ("p", "De <strong>proefbalans</strong> is een overzicht van alle rekeningen met totalen en saldi: je controleert of totaal debet en totaal credit gelijk zijn. "
                  "Dan volgen de eindejaarsboekingen (inventarisverrichtingen). Pas daarna maak je de <strong>definitieve saldibalans</strong>, die per rekening het saldo toont. "
                  "Daaruit haal je de <strong>jaarrekening</strong>: de <strong>balans</strong> (activa en passiva), de <strong>resultatenrekening</strong> (de kostenrekeningen en de opbrengstrekeningen) en een toelichting."),
        ]),
        dict(kop="Afschrijvingen", blokken=[
            ("p", "Een <strong>afschrijving</strong> spreidt de kost van een investering over de jaren dat je ze gebruikt. Ze is een <strong>kost zonder uitgave</strong>: er gaat geen geld van de bank. Daarom telt ze mee in de cashflow. "
                  "<strong>Lineair</strong> afschrijven (de lineaire afschrijving) betekent elk jaar hetzelfde bedrag, ook in het laatste jaar."),
            ("kader", "<p style='text-align:center'><strong>jaarlijkse afschrijving = (aanschafwaarde − restwaarde) / gebruiksduur</strong></p>"
                      "<p style='text-align:center'><strong>boekwaarde</strong> (nettoboekwaarde) = aanschafwaarde − geboekte afschrijvingen</p>"),
            ("kader", tabel(["investering", "afschrijving per jaar"],
                            [["machine 50 000 euro, 5 jaar, geen restwaarde", "50 000 / 5 = 10 000 euro"],
                             ["bestelwagen 36 000 euro, restwaarde 6 000 euro, 5 jaar", "(36 000 − 6 000) / 5 = 6 000 euro"],
                             ["computer 3 000 euro, 3 jaar", "1 000 euro; boekwaarde na 2 jaar: 3 000 − 2 · 1 000 = 1 000 euro"]])),
            ("p", "Een afschrijving verlaagt de boekwaarde. Na de volledige gebruiksduur is de boekwaarde gelijk aan de restwaarde."),
        ]),
        dict(kop="Voorraadwijziging", blokken=[
            ("kader", "<p style='text-align:center'><strong>voorraadwijziging = eindvoorraad − beginvoorraad</strong><br><strong>kostprijs van de verkochte goederen = aankopen + beginvoorraad − eindvoorraad</strong></p>"),
            ("kader", tabel(["aankopen", "beginvoorraad", "eindvoorraad", "voorraadwijziging", "kostprijs verkochte goederen"],
                            [["50 000", "8 000", "10 000", "toename van 2 000", "48 000"],
                             ["40 000", "12 000", "9 000", "afname van 3 000", "43 000"]])),
            ("p", "Stijgt de voorraad, dan verlaagt de voorraadwijziging de kosten van het jaar: een deel van de aankopen is nog niet verkocht. "
                  "Een <strong>daling</strong> van de voorraad <strong>verlaagt</strong> de winst: er werd meer verkocht dan aangekocht, dus de kost van de verkochte goederen stijgt."),
        ]),
        dict(kop="Voorzieningen en schulden", blokken=[
            ("p", "Een <strong>voorziening voor risico's en kosten</strong> is een bedrag opzij voor een <strong>waarschijnlijk</strong> verlies, bijvoorbeeld voor een lopend geschil of een grote herstelling. "
                  "Het bedrag is nog niet zeker. Het aanleggen is een <strong>kost</strong>, geboekt in het jaar waarin het risico ontstaat."),
            ("p", "Het deel van een lening dat binnen het jaar vervalt, gaat van groep 17 naar groep 42. Zo toont de balans wat er op korte termijn betaald moet worden."),
        ]),
        dict(kop="Overlopende rekeningen", blokken=[
            ("p", "Overlopende rekeningen zorgen ervoor dat kosten en opbrengsten in het juiste boekjaar komen: het principe van de <strong>periodetoerekening</strong>."),
            ("kader", tabel(["rekening", "betekenis", "voorbeeld", "balans"],
                            [["over te dragen kosten", "al betaald, hoort bij het volgende jaar", "verzekering voor 12 maanden betaald op 1 oktober: januari tot september (9 maanden) hoort bij volgend jaar", "actief (een soort vordering)"],
                             ["toe te rekenen kosten", "kost van dit jaar, nog te betalen", "elektriciteit van december, gefactureerd in januari", "passief (schuld)"],
                             ["over te dragen opbrengsten", "al ontvangen, hoort bij het volgende jaar", "een klant betaalt in december al de huur voor januari", "passief"],
                             ["verkregen opbrengsten", "opbrengst van dit jaar, later ontvangen", "interest op een spaarrekening van dit jaar, volgend jaar gestort", "actief"]])),
        ]),
        dict(kop="Belasting en bestemming van het resultaat", blokken=[
            ("p", "De geraamde <strong>belasting op het resultaat</strong> boek je als kost in groep 67. Winst voor belasting 100 000 euro aan 25 %: 25 000 euro. "
                  "De voorafbetalingen stonden op een vordering op de fiscus (een voorschot dat later verrekend wordt): bij 18 000 euro voorafbetalingen moet er nog 7 000 euro betaald worden."),
            ("p", "De <strong>bestemming van het resultaat</strong>: beslissen wat er met de winst gebeurt. De winst kan naar <strong>reserves</strong>, naar <strong>dividenden</strong> of naar <strong>overgedragen winst</strong> (naar het volgende jaar). "
                  "Dividenden zijn een verdeling van de winst, <strong>geen kost</strong>. Na de bestemming is de winst van het jaar helemaal verdeeld: elke euro krijgt een bestemming."),
        ]),
    ],
    onthoud=[
        "Lineaire afschrijving = (aanschafwaarde − restwaarde) / gebruiksduur; een kost zonder uitgave.",
        "Kostprijs verkochte goederen = aankopen + beginvoorraad − eindvoorraad.",
        "Voorziening: waarschijnlijk verlies, bedrag nog onzeker, een kost.",
        "Over te dragen kosten en verkregen opbrengsten: actief. Toe te rekenen kosten en over te dragen opbrengsten: passief.",
        "Proefbalans → eindejaarsboekingen → definitieve saldibalans → jaarrekening (balans, resultatenrekening, toelichting).",
    ])


# ───────────────────────── 8. De balans voor financiële analyse
def balansfiguur(breedte=470):
    """De herschikte balans: links de activa, rechts de passiva, met het nettobedrijfskapitaal."""
    h, L, B = 230, 45, 145
    R = L + B + 20
    d = []
    def blok(x, y0, y1, tekst, kleur, sub=""):
        d.append(f'<rect x="{x}" y="{y0}" width="{B}" height="{y1 - y0}" fill="{kleur}" fill-opacity=".16" stroke="{kleur}" stroke-width="1.4"/>')
        d.append(svg._tekst(x + B / 2, (y0 + y1) / 2 + (0 if sub else 4), tekst, 11, svg.INK, "middle", True))
        if sub:
            d.append(svg._tekst(x + B / 2, (y0 + y1) / 2 + 14, sub, 9.5, svg.DIM))
    T, M, E = 20, 140, 220
    blok(L, T, M, "langdurende activa", svg.FOREST, "langer dan een jaar")
    blok(L, M, E, "courante activa", svg.AMBER, "binnen het jaar")
    blok(R, T, 85, "eigen vermogen", svg.FOREST)
    blok(R, 85, 120, "vreemd vermogen LT", svg.FOREST)
    blok(R, 120, E, "vreemd vermogen KT", svg.AMBER, "binnen het jaar")
    d.append(svg._tekst(L + B / 2, 12, "ACTIVA", 10, svg.DIM, "middle", True))
    d.append(svg._tekst(R + B / 2, 12, "PASSIVA", 10, svg.DIM, "middle", True))
    # permanent vermogen
    x = R + B + 8
    d.append(f'<path d="M{x},{T} h6 v{120 - T} h-6" fill="none" stroke="{svg.INK}" stroke-width="1.2"/>')
    d.append(svg._tekst(x + 10, (T + 120) / 2 - 2, "permanent", 10, svg.INK, "start", True))
    d.append(svg._tekst(x + 10, (T + 120) / 2 + 11, "vermogen", 10, svg.INK, "start", True))
    # nettobedrijfskapitaal
    d.append(f'<rect x="{L}" y="{120}" width="{R + B - L}" height="{M - 120}" fill="{svg.FOREST}" fill-opacity=".10" stroke="{svg.FOREST}" stroke-dasharray="4 3"/>')
    d.append(svg._tekst(L - 6, 133, "NBK", 10, svg.FOREST, "end", True))
    return svg._svg(breedte, h, "".join(d))


zet("de-balans-voor-financiele-analyse",
    titel="De balans voor financiële analyse",
    onder="De balans herschikken naar lange en korte termijn, het nettobedrijfskapitaal, en verticale en horizontale analyse.",
    secties=[
        dict(kop="De herschikte balans", blokken=[
            ("p", "Voor een financiële analyse herschik je de balans om <strong>lange en korte termijn</strong> duidelijk te scheiden. Zo kan je liquiditeit en solvabiliteit beoordelen. "
                  "Op de balans is het totaal van de activa altijd gelijk aan het totaal van de passiva: elke bezitting is gefinancierd met eigen of vreemd vermogen."),
            ("fig", balansfiguur(), "Het nettobedrijfskapitaal (NBK) is het stuk courante activa dat met permanent vermogen gefinancierd is."),
        ]),
        dict(kop="Wat hoort waar?", blokken=[
            ("kader", tabel(["post", "wat hoort erbij"],
                            [["langdurende activa", "bezittingen die langer dan een jaar blijven: terreinen en gebouwen, machines, vorderingen op meer dan een jaar"],
                             ["courante activa", "voorraden (binnen het jaar verkocht of gebruikt), vorderingen op ten hoogste een jaar (op klanten), geldbeleggingen, liquide middelen (het geld op de bankrekening, direct beschikbaar)"],
                             ["eigen vermogen", "het kapitaal, de reserves (winst die in de onderneming blijft), de overgedragen winst (van de eigenaars)"],
                             ["vreemd vermogen op lange termijn", "een hypothecaire lening over 20 jaar, een obligatielening op tien jaar (behalve het deel dat binnen het jaar vervalt)"],
                             ["vreemd vermogen op korte termijn", "schulden aan leveranciers, te betalen btw: binnen het jaar te betalen"]])),
            ("p", "<strong>Permanent vermogen</strong> = eigen vermogen + vreemd vermogen op lange termijn: het blijft langer dan een jaar ter beschikking. 150 000 + 100 000 = 250 000 euro. "
                  "Vuistregel: financier langdurende activa met permanent vermogen, want wat lang in het bedrijf blijft, financier je met vermogen dat lang blijft."),
        ]),
        dict(kop="Het nettobedrijfskapitaal", blokken=[
            ("kader", "<p style='text-align:center'><strong>NBK = permanent vermogen − langdurende activa = courante activa − vreemd vermogen op korte termijn</strong></p>"),
            ("p", "Langs de bovenkant of de onderkant van de balans krijg je altijd hetzelfde. 300 000 − 250 000 = 50 000 euro; of 180 000 − 120 000 = 60 000 euro. "
                  "Een <strong>positief</strong> NBK betekent dat een deel van de courante activa met permanent vermogen gefinancierd is: gezond. "
                  "Een <strong>negatief</strong> NBK betekent dat langdurende activa deels met kortlopende schulden gefinancierd zijn: meestal een risico."),
        ]),
        dict(kop="Verticale en horizontale analyse", blokken=[
            ("kader", tabel(["", "verticale analyse", "horizontale analyse"],
                            [["wat", "elke post als % van het balanstotaal, binnen één balans van één jaar", "de evolutie van een post over de jaren"],
                             ["formule", "post / balanstotaal · 100", "(nieuw − oud) / oud · 100"],
                             ["voorbeeld", "eigen vermogen 200 000 op 500 000: 40 %; liquide middelen 30 000 op 600 000: 5 %", "voorraad 40 000 → 50 000: +25 %; omzet 1 000 000 → 900 000: −10 %; 80 000 → 60 000: −25 %"],
                             ["sterk punt", "alle activaposten samen = 100 %; je kan bedrijven van verschillende grootte beter vergelijken", "je ziet trends"]])),
            ("p", "Stijgt in de verticale analyse het aandeel van de schulden op korte termijn, dan steunt de onderneming meer op kortlopende schulden. Dat kan druk zetten op de liquiditeit."),
        ]),
        dict(kop="Waar vind je de cijfers?", blokken=[
            ("p", "De jaarrekeningen van Belgische vennootschappen vind je gratis in de <strong>balanscentrale van de Nationale Bank</strong>. Uit een gepubliceerde jaarrekening kan je zelf kerncijfers berekenen; op het examen krijg je een jaarrekening en een formularium. "
                  "Een beperking: een balans is een <strong>momentopname</strong>, meestal op 31 december."),
        ]),
    ],
    onthoud=[
        "Langdurend = langer dan een jaar; courant = binnen het jaar.",
        "Permanent vermogen = eigen vermogen + vreemd vermogen op lange termijn.",
        "NBK = permanent vermogen − langdurende activa = courante activa − VV korte termijn. Positief is gezond.",
        "Verticaal: % van het balanstotaal. Horizontaal: evolutie over de jaren.",
    ])


# ───────────────────────── 9. Kerncijfers: liquiditeit
zet("kerncijfers-liquiditeit",
    titel="Kerncijfers: liquiditeit",
    onder="Kan de onderneming haar schulden op korte termijn betalen? Current ratio, quick ratio, klanten- en leverancierskrediet, omlooptijd van de voorraad.",
    secties=[
        dict(kop="Liquiditeit in ruime en enge zin", blokken=[
            ("p", "De <strong>liquiditeit</strong> meet of een onderneming haar schulden op <strong>korte termijn</strong> kan betalen. Quick ratio en klantenkrediet horen bij de liquiditeit; solvabiliteit en rendabiliteit zijn andere groepen kerncijfers."),
            ("kader", tabel(["kerncijfer", "formule", "voorbeeld"],
                            [["current ratio (liquiditeit in ruime zin)", "courante activa / vreemd vermogen op korte termijn", "300 000 / 200 000 = 1,5; 240 000 / 160 000 = 1,5"],
                             ["quick ratio (liquiditeit in enge zin, acid test)", "(vorderingen op ten hoogste een jaar + geldbeleggingen + liquide middelen) / vreemd vermogen op korte termijn, dus <strong>zonder de voorraden</strong>",
                              "(300 000 − 100 000) / 250 000 = 0,8; (80 000 + 20 000 + 25 000) / 100 000 = 1,25"]])),
            ("kader", "<ul><li>Groter dan 1 is gunstig: meer courante activa dan kortlopende schulden. Een current ratio van 0,7 betekent dat de kortlopende schulden groter zijn dan de courante activa.</li>"
                      "<li>De quick ratio laat de voorraden weg, want die moeten eerst nog verkocht worden. Ze is dus altijd kleiner dan of gelijk aan de current ratio. Bij 0,8 dekken de snelle middelen maar 80 % van de kortlopende schulden.</li>"
                      "<li>Een heel hoge current ratio (bv. 4) heeft ook een gevaar: er zit te veel geld vast in voorraad of kas, en middelen die stilliggen brengen weinig op.</li>"
                      "<li>De current ratio en het nettobedrijfskapitaal gebruiken dezelfde balansposten: de current ratio is een verhouding, het NBK een verschil. Een negatief NBK gaat samen met een current ratio kleiner dan 1.</li>"
                      "<li>Een lening op lange termijn om voorraad te kopen <strong>verbetert</strong> de current ratio: de courante activa stijgen, de kortlopende schulden niet.</li></ul>"),
        ]),
        dict(kop="Termijnen in dagen", blokken=[
            ("kader", tabel(["kerncijfer", "formule", "voorbeeld"],
                            [["klantenkrediet: hoeveel dagen klanten gemiddeld nodig hebben om te betalen", "handelsvorderingen / (omzet · 1,21) · 365", "60 500 / (500 000 · 1,21) · 365 = 36,5 dagen"],
                             ["leverancierskrediet: hoeveel dagen de onderneming wacht om haar leveranciers te betalen", "handelsschulden / (aankopen · 1,21) · 365", "48 400 / 484 000 · 365 = 36,5 dagen; 24 200 / 242 000 · 365 ≈ 37 dagen"],
                             ["omlooptijd van de voorraad: hoeveel dagen goederen gemiddeld in voorraad blijven", "gemiddelde voorraad / kostprijs verkochte goederen · 365", "50 000 / 365 000 · 365 = 50 dagen"]])),
            ("p", "Bij klanten- en leverancierskrediet tel je de <strong>btw</strong> bij de omzet of de aankopen, omdat de vorderingen en schulden inclusief btw zijn: zo vergelijk je bedragen van dezelfde soort."),
            ("kader", "<ul><li>Hoe korter het klantenkrediet, hoe sneller het geld binnenkomt. Stijgt het, dan betalen klanten trager en verslechtert de liquiditeit. Een winkel die enkel contant verkoopt, heeft ongeveer 0 dagen klantenkrediet.</li>"
                      "<li>Klantenkrediet 60 dagen bij een betalingstermijn van 30 dagen: klanten betalen gemiddeld te laat. Maatregelen: herinneringen sturen, korting geven bij snelle betaling, of <strong>factoring</strong> (de factor betaalt de vordering meteen, zodat het klantenkrediet in feite korter wordt).</li>"
                      "<li>Een langer leverancierskrediet is gunstig zolang de relatie goed blijft. Veel langer dan de afgesproken termijn kan de relatie met leveranciers schaden.</li>"
                      "<li>Hoe hoger de omlooptijd van de voorraad, hoe langer het geld vastzit: slecht voor de liquiditeit.</li></ul>"),
        ]),
        dict(kop="Netto te financieren periode", blokken=[
            ("kader", "<p style='text-align:center'><strong>netto te financieren periode = omlooptijd voorraad + klantenkrediet − leverancierskrediet</strong></p>"),
            ("p", "Het is de periode die de onderneming zelf moet financieren. 40 + 30 − 45 = 25 dagen; 60 + 45 − 30 = 75 dagen. Korter is gunstiger: de onderneming moet minder lang zelf de kosten voorschieten. "
                  "Verkort het klantenkrediet van 50 naar 35 dagen, dan daalt de netto te financieren periode met 15 dagen."),
            ("p", "De liquiditeit verbeteren: klanten sneller laten betalen en minder voorraad aanhouden. Let op: een onderneming met winst kan toch een liquiditeitsprobleem hebben, want winst is niet hetzelfde als geld op de bank."),
            ("weetje", "Vergelijk kerncijfers best met bedrijven uit dezelfde sector, omdat normen per sector verschillen. Een supermarkt heeft bijvoorbeeld een heel kort klantenkrediet."),
        ]),
    ],
    onthoud=[
        "Current ratio = CA / VVKT; quick ratio = (CA − voorraden) / VVKT. Groter dan 1 is gunstig.",
        "Klantenkrediet = vorderingen / (omzet · 1,21) · 365; leverancierskrediet = schulden / (aankopen · 1,21) · 365.",
        "Omlooptijd voorraad = gemiddelde voorraad / kostprijs verkochte goederen · 365.",
        "Netto te financieren periode = voorraad + klanten − leveranciers. Korter is beter.",
    ])


# ───────────────────────── 10. Kerncijfers: solvabiliteit en rendabiliteit
zet("kerncijfers-solvabiliteit-en-rendabiliteit",
    titel="Kerncijfers: solvabiliteit en rendabiliteit",
    onder="Kan de onderneming haar schulden op lange termijn dragen, en hoeveel brengt het vermogen op? Met de financiële hefboom.",
    secties=[
        dict(kop="Solvabiliteit en schuldgraad", blokken=[
            ("p", "De <strong>solvabiliteit</strong> meet of een onderneming op <strong>lange termijn</strong> haar schulden kan dragen: haar financiële onafhankelijkheid. De solvabiliteit en de schuldgraad horen bij de solvabiliteitskerncijfers; "
                  "je berekent ze allebei met gegevens van de balans."),
            ("kader", tabel(["kerncijfer", "formule", "voorbeeld"],
                            [["solvabiliteit", "eigen vermogen / totaal vermogen · 100", "400 000 / 1 000 000 = 40 %; 500 000 / 800 000 = 62,5 %"],
                             ["schuldgraad", "vreemd vermogen / totaal vermogen · 100", "700 000 / 1 000 000 = 70 %; 450 000 / 900 000 = 50 %"]])),
            ("kader", "<ul><li>Solvabiliteit en schuldgraad zijn samen <strong>100 %</strong> (spiegelbeeld): solvabiliteit 25 % geeft schuldgraad 75 %. Zonder vreemd vermogen is de solvabiliteit 100 %.</li>"
                      "<li>Hoe meer schulden, hoe <strong>afhankelijker</strong> van de schuldeisers. Een schuldgraad van 90 % is geen teken van een sterke onderneming.</li>"
                      "<li>Een lage solvabiliteit maakt het moeilijker om een nieuwe lening te krijgen: de bank ziet meer risico. Vraagt de bank minstens 30 % en is het 250 000 / 1 000 000 = 25 %, dan is de solvabiliteit te laag.</li>"
                      "<li><strong>Verbeteren</strong>: winst in de onderneming houden als reserve, of een kapitaalsverhoging doen: beide verhogen het eigen vermogen. Verlies verlaagt het eigen vermogen, dus de solvabiliteit daalt.</li>"
                      "<li>Een onderneming kan winstgevend zijn en toch een lage solvabiliteit hebben, als ze veel winst maakt met veel geleend geld.</li></ul>"),
        ]),
        dict(kop="Rendabiliteit", blokken=[
            ("p", "Rendabiliteit gaat over <strong>winst</strong>, liquiditeit over het betalen van schulden op korte termijn: ze betekenen niet hetzelfde."),
            ("kader", tabel(["kerncijfer", "formule", "voorbeeld"],
                            [["rendabiliteit van het eigen vermogen (REV): het rendement voor de aandeelhouders", "nettowinst na belasting / eigen vermogen · 100", "30 000 / 200 000 = 15 %; 50 000 / 400 000 = 12,5 %"],
                             ["rendabiliteit van het totaal vermogen (RTV): hoe goed de onderneming al haar middelen inzet", "(winst na belasting + interestkosten) / totaal vermogen · 100", "(40 000 + 20 000) / 600 000 = 10 %"]])),
            ("p", "Bij de REV neem je de nettowinst na belasting: wat echt voor de eigenaars is. In de teller van de RTV neem je het resultaat <strong>vóór interestkosten</strong>, want het totaal vermogen komt van eigenaars én schuldeisers: beiden krijgen een vergoeding, winst en interest. "
                  "Een belegger vergelijkt de REV met de rente op een spaarrekening om te zien of het risico van beleggen loont: een aandeel is riskanter, dus de REV moet hoger liggen."),
        ]),
        dict(kop="De financiële hefboom", blokken=[
            ("p", "De <strong>financiële hefboom</strong> is het effect van lenen op het rendement van de eigenaars. Om te weten of een lening het rendement verhoogt, vergelijk je de <strong>RTV met de interestvoet</strong>."),
            ("kader", tabel(["situatie", "hefboom", "als de onderneming meer leent"],
                            [["RTV hoger dan de interestvoet (8 % tegen 5 %): het vermogen brengt meer op dan de interest", "positief", "de REV stijgt"],
                             ["RTV gelijk aan de interestvoet", "neutraal", "lenen verandert niets"],
                             ["RTV lager dan de interestvoet (4 % tegen 6 %)", "negatief", "de REV daalt: het geleende geld kost meer dan het opbrengt"]])),
            ("p", "De <strong>hefboomfactor</strong> = REV / RTV. 18 / 12 = 1,5: groter dan 1, dus een positieve hefboom. Meer lenen verhoogt dus <strong>niet altijd</strong> de REV."),
        ]),
    ],
    onthoud=[
        "Solvabiliteit = EV / TV; schuldgraad = VV / TV; samen 100 %.",
        "REV = nettowinst na belasting / EV.",
        "RTV = (winst na belasting + interest) / TV.",
        "Hefboom positief als RTV > interestvoet; hefboomfactor = REV / RTV.",
    ])


# ───────────────────────── 11. Financieringsvormen
zet("financieringsvormen",
    titel="Financieringsvormen",
    onder="Eigen of vreemd vermogen, lange of korte termijn: welke financiering past bij welke nood?",
    secties=[
        dict(kop="Eigen vermogen", blokken=[
            ("kader", tabel(["vorm", "uitleg"],
                            [["zelffinanciering (autofinanciering)", "winst niet uitkeren maar in de onderneming laten: het eigen vermogen stijgt via de reserves. Ook afschrijvingen zorgen voor middelen die in de onderneming blijven"],
                             ["kapitaalsverhoging", "de eigenaars of nieuwe aandeelhouders brengen geld in"]])),
            ("p", "<strong>Voordeel</strong>: geen interest (wel verwachten de aandeelhouders een vergoeding, bijvoorbeeld dividend) en de schuldgraad daalt. "
                  "<strong>Nadelen van een kapitaalsverhoging</strong>: als nieuwe aandeelhouders instappen, wordt de zeggenschap van de oude verdeeld, en de winst wordt over meer aandelen verdeeld."),
        ]),
        dict(kop="Vreemd vermogen op lange termijn", blokken=[
            ("kader", tabel(["vorm", "uitleg"],
                            [["investeringskrediet", "een lening op lange termijn voor bijvoorbeeld machines, afgelost over de levensduur van de investering"],
                             ["hypothecaire lening", "om onroerende goederen te financieren, meestal over vijftien tot twintig jaar. De <strong>waarborg</strong> is het gebouw of de grond: kan de onderneming niet betalen, dan kan de bank het goed laten verkopen"],
                             ["obligatielening", "een lening bij het publiek via schuldbewijzen: beleggers kopen obligaties en krijgen jaarlijks interest. Zo haal je veel geld op zonder zeggenschap af te staan: obligatiehouders zijn schuldeisers, geen eigenaars"]])),
            ("p", "<strong>Voordeel</strong> van vreemd vermogen: de interest is fiscaal aftrekbaar als kost (verlaagt de belastbare winst). <strong>Nadeel</strong>: je moet interest betalen en terugbetalen, ook als het slecht gaat. "
                  "Hoe meer vreemd vermogen, hoe hoger de schuldgraad."),
        ]),
        dict(kop="Vreemd vermogen op korte termijn", blokken=[
            ("kader", tabel(["vorm", "uitleg"],
                            [["kaskrediet", "je mag tijdelijk onder nul gaan op je zichtrekening: <strong>flexibel</strong>"],
                             ["straight loan", "een korte lening: vast bedrag, vaste periode. Je krijgt het volledige bedrag in één keer en betaalt terug op de vervaldag: <strong>niet flexibel</strong>"],
                             ["leverancierskrediet", "je mag de leverancier later betalen en gebruikt het geld intussen zelf. Niet altijd gratis: wie de korting voor snelle betaling misloopt, betaalt in feite een prijs voor het krediet"],
                             ["factoring", "je verkoopt je vorderingen op klanten aan een gespecialiseerde firma, de factor. Die betaalt meteen het grootste deel en int ze zelf. Je krijgt sneller geld, maar betaalt een vergoeding"]])),
        ]),
        dict(kop="Leasing en de crowd", blokken=[
            ("kader", tabel(["vorm", "uitleg"],
                            [["financiële leasing", "een huurcontract met aankoopoptie op het einde: de leasingnemer draagt de risico's en kan op het einde eigenaar worden, meestal voor een klein bedrag"],
                             ["operationele leasing", "de leasinggever blijft eigenaar en zorgt vaak voor onderhoud, zoals bij bedrijfswagens"],
                             ["crowdfunding", "veel mensen geven elk een klein bedrag; vaak krijgen de gevers een product of tegenprestatie (een gift of voorverkoop). Past bij een start-up met een origineel product en weinig eigen geld, die via een platform meteen interesse kan testen"],
                             ["crowdlending", "veel particulieren lenen geld aan een onderneming en krijgen interest: een lening, geen gift"]])),
            ("p", "Voordeel van leasing: je betaalt niet meteen het volle bedrag, maar een periodieke vergoeding, en houdt geld vrij voor andere zaken."),
        ]),
        dict(kop="Kiezen: de gouden balansregel", blokken=[
            ("p", "<strong>Langdurende activa financier je best met vermogen op lange termijn</strong>; een tijdelijke nood financier je op korte termijn."),
            ("kader", tabel(["nood", "past het best"],
                            [["een bakkerij wil een nieuwe oven van 40 000 euro (gaat jaren mee)", "een investeringskrediet"],
                             ["een winkel heeft in december tijdelijk extra voorraad nodig", "een kaskrediet of straight loan"],
                             ["een gebouw", "een hypothecaire lening, geen straight loan"]])),
        ]),
    ],
    onthoud=[
        "Eigen vermogen: zelffinanciering en kapitaalsverhoging (geen interest, wel zeggenschap delen).",
        "Lange termijn: investeringskrediet, hypothecaire lening, obligatielening.",
        "Korte termijn: kaskrediet (flexibel), straight loan (vast), leverancierskrediet, factoring.",
        "Crowdfunding: gift of voorverkoop. Crowdlending: lening met interest.",
        "Gouden balansregel: lang met lang, kort met kort.",
    ])


# ───────────────────────── 12. Investeringsprojecten beoordelen
zet("investeringsprojecten-beoordelen",
    titel="Investeringsprojecten beoordelen",
    onder="Soorten investeringen, de cashflow, en drie methodes om een project te beoordelen: terugverdientijd, ROI en netto contante waarde.",
    secties=[
        dict(kop="Soorten investeringen", blokken=[
            ("kader", tabel(["soort", "voorbeeld"],
                            [["vervangingsinvestering", "een versleten machine vervangen door een gelijkaardige: de capaciteit blijft gelijk"],
                             ["uitbreidingsinvestering", "een tweede productielijn om meer te maken: de capaciteit stijgt"],
                             ["rationalisatie-investering", "een robot die het werk goedkoper maakt: kosten besparen"],
                             ["materieel / immaterieel", "een machine kan je vastnemen; een softwarelicentie niet, maar ze heeft waarde voor meerdere jaren: immaterieel"],
                             ["financiële investering", "aandelen van een ander bedrijf kopen: een belegging, geen machine of gebouw"],
                             ["desinvestering", "een investering verkopen of afstoten, bv. een oude machine verkopen"]])),
        ]),
        dict(kop="De cashflow", blokken=[
            ("kader", "<p style='text-align:center'><strong>cashflow = nettowinst + afschrijvingen</strong></p>"),
            ("p", "Afschrijvingen verlagen de winst, maar er gaat geen geld uit: een kost zonder uitgave. Daarom tel je ze terug bij de winst op. De cashflow is dus <strong>niet</strong> gelijk aan de nettowinst. "
                  "12 000 + 8 000 = 20 000 euro. Investering 40 000 euro over 4 jaar zonder restwaarde: afschrijving 10 000 euro; met nettowinst 5 000 euro is de cashflow 15 000 euro. "
                  "Met restwaarde: (20 000 − 4 000) / 4 = 4 000 euro afschrijving per jaar."),
            ("p", "In een <strong>cashflowtabel</strong> staan de cashflow per jaar en de <strong>gecumuleerde cashflow</strong> (de som tot en met dat jaar). Die toont wanneer de investering terugverdiend is."),
            ("kader", tabel(["jaar", "cashflow", "gecumuleerde cashflow", "investering 100 000"],
                            [["1", "40 000", "40 000", "nog 60 000"],
                             ["2", "35 000", "75 000", "nog 25 000"],
                             ["3", "25 000", "100 000", "terugverdiend na 3 jaar"],
                             ["4", "20 000", "120 000", ""]])),
        ]),
        dict(kop="Terugverdientijd en ROI", blokken=[
            ("p", "De <strong>terugverdientijd</strong> is de tijd tot de cashflows de investering terugbetalen. Gelijke cashflows: investering / cashflow, bv. 60 000 / 20 000 = 3 jaar."),
            ("kader", "<ul><li>Investering 50 000, cashflows 20 000 per jaar: na 2 jaar 40 000 terug; de resterende 10 000 is de helft van jaar 3: <strong>2,5 jaar</strong>.</li>"
                      "<li>Investering 80 000, cashflows 30 000: na 2 jaar 60 000; 20 000 / 30 000 = 2/3 jaar = 8 maanden: <strong>2 jaar en 8 maanden</strong>.</li></ul>"),
            ("p", "Hoe korter, hoe sneller het geld terug is en hoe minder lang het vastzit: een goede maatstaf voor het <strong>risico</strong>. "
                  "<strong>Nadeel</strong>: ze houdt geen rekening met de cashflows na de terugverdientijd. Twee projecten met dezelfde terugverdientijd zijn dus niet altijd even goed."),
            ("p", "De <strong>return on investment (ROI)</strong> meet de gemiddelde winst in procent van de investering: gemiddelde jaarlijkse nettowinst / investering · 100. "
                  "15 000 / 100 000 = 15 %. Totale winst 20 000 over 5 jaar op 50 000: 4 000 / 50 000 = 8 %. Een hogere ROI is gunstiger; vergelijk ze met de rente op een lening of een andere belegging."),
        ]),
        dict(kop="De netto contante waarde", blokken=[
            ("p", "Een euro vandaag is meer waard dan een euro binnen vijf jaar, want je kan hem beleggen: de <strong>tijdswaarde van geld</strong>. Daarom <strong>verdisconteer</strong> je toekomstige cashflows naar vandaag."),
            ("kader", "<p style='text-align:center'><strong>contante waarde = cashflow / (1 + r)<sup>n</sup></strong> &nbsp;&nbsp; <strong>NCW = som van de contante waarden − investering</strong></p>"),
            ("kader", "<ul><li>11 000 euro over één jaar aan 10 %: 11 000 / 1,10 = 10 000 euro.</li>"
                      "<li>12 100 euro over twee jaar aan 10 %: 12 100 / 1,10² = 12 100 / 1,21 = 10 000 euro.</li>"
                      "<li>Investering 30 000, contante waarde van de cashflows 32 500: NCW = 2 500 euro.</li></ul>"),
            ("p", "Een project is aanvaardbaar als de <strong>NCW positief</strong> is: dan brengt het meer op dan de gevraagde rente. Project A (+2 000) kies je boven project B (−1 000). "
                  "Een negatieve NCW betekent niet altijd verlies in de boekhouding: het project kan winst maken, maar minder dan de vereiste rente. "
                  "Voor de NCW heb je de cashflows per jaar, de rentevoet en het investeringsbedrag nodig. De rentevoet is vaak de rente op een lening of het rendement van een andere belegging. "
                  "Bij een <strong>hogere</strong> rentevoet zijn toekomstige cashflows minder waard: de NCW <strong>daalt</strong>. De NCW houdt als enige van de drie methodes rekening met de tijdswaarde van geld en is daarom nauwkeuriger."),
        ]),
    ],
    onthoud=[
        "Vervanging, uitbreiding, rationalisatie; materieel, immaterieel, financieel.",
        "Cashflow = nettowinst + afschrijvingen.",
        "Terugverdientijd: hoe snel terug (risico), maar negeert latere cashflows.",
        "ROI = gemiddelde nettowinst / investering.",
        "NCW = contante waarde van de cashflows − investering; positief = aanvaardbaar.",
    ])


# ───────────────────────── 13. SWOT, stakeholders en het ondernemingsplan
def kwadrant(vakken, rijkop=("", ""), kolkop=("", ""), breedte=470, hoogte=230, aslabels=None):
    """Vier vakken in een raster van 2 op 2 (SWOT, BCG-matrix).

    vakken: vier (titel, onderschrift, kleur) in leesvolgorde
    rijkop / kolkop: korte labels links van de rijen en boven de kolommen
    aslabels: (x-as, y-as) met een pijl, voor de BCG-matrix
    """
    L, T = 80, 26
    w, h = (breedte - L - 20) / 2, (hoogte - T - (26 if aslabels else 8)) / 2
    d = []
    for i, (titel, sub, k) in enumerate(vakken):
        x, y = L + (i % 2) * w, T + (i // 2) * h
        d.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w - 4:.1f}" height="{h - 4:.1f}" rx="8" fill="{k}" fill-opacity=".14" stroke="{k}" stroke-width="1.4"/>')
        d.append(svg._tekst(x + w / 2 - 2, y + h / 2 - 4, titel, 12.5, svg.INK, "middle", True))
        if sub:
            d.append(svg._tekst(x + w / 2 - 2, y + h / 2 + 13, sub, 9.5, svg.DIM))
    for j, t in enumerate(rijkop):
        d.append(svg._tekst(L - 8, T + j * h + h / 2 + 3, t, 10, svg.DIM, "end", True))
    for j, t in enumerate(kolkop):
        d.append(svg._tekst(L + j * w + w / 2, T - 9, t, 10, svg.DIM, "middle", True))
    if aslabels:
        y0 = T + 2 * h + 6
        d.append(f'<line x1="{L + 2 * w - 4:.1f}" y1="{y0}" x2="{L:.1f}" y2="{y0}" stroke="{svg.DIM}" stroke-width="1.2"/>')
        d.append(f'<path d="M{L},{y0} l7,-4 v8 z" fill="{svg.DIM}"/>')
        d.append(svg._tekst(L + w, y0 + 14, aslabels[0], 10, svg.DIM))
    return svg._svg(breedte, hoogte, "".join(d))


zet("swot-stakeholders-en-het-ondernemingsplan",
    titel="SWOT, stakeholders en het ondernemingsplan",
    onder="De positie van een onderneming onderzoeken, de belangen van stakeholders kennen, en een idee uitwerken in een ondernemingsplan.",
    secties=[
        dict(kop="De SWOT-analyse", blokken=[
            ("fig", kwadrant([("S: sterktes", "strengths", svg.FOREST), ("W: zwaktes", "weaknesses", svg.AMBER),
                              ("O: kansen", "opportunities", svg.FOREST), ("T: bedreigingen", "threats", svg.AMBER)],
                             rijkop=("intern", "extern"), kolkop=("positief", "negatief")),
             "Sterktes en zwaktes gaan over de onderneming zelf, kansen en bedreigingen komen uit de omgeving."),
            ("p", "Kansen en bedreigingen kan de onderneming niet zelf bepalen: ze komen uit de omgeving en ze kan er enkel op reageren. "
                  "Het <strong>doel</strong> van een SWOT-analyse is strategische keuzes onderbouwen: je combineert sterktes met kansen en zoekt oplossingen voor zwaktes en bedreigingen. "
                  "Ook een vzw of een school kan een SWOT-analyse maken."),
            ("kader", tabel(["voorbeeld", "in de SWOT"],
                            [["een bakkerij heeft zeer ervaren bakkers", "sterkte"],
                             ["een verouderde website; te weinig parkeerplaatsen", "zwakte (intern)"],
                             ["een nieuwe subsidie voor duurzame investeringen; e-bikes worden steeds populairder", "kans"],
                             ["een nieuwe concurrent opent een winkel in dezelfde straat", "bedreiging"],
                             ["een kledingwinkel verkoopt goed online en steeds meer mensen kopen online", "een sterkte en een kans"]])),
        ]),
        dict(kop="Stakeholders", blokken=[
            ("p", "Een <strong>stakeholder</strong> is iemand met een belang bij de onderneming. <strong>Intern</strong>: werknemers en de eigenaars. <strong>Extern</strong>: klanten, leveranciers, buren, de overheid, de bank."),
            ("p", "Stakeholders kunnen <strong>tegenstrijdige belangen</strong> hebben: aandeelhouders willen veel winst of meer dividend, werknemers hogere lonen, buurtbewoners minder geluidsoverlast van een fabriek. "
                  "Een bank is een schuldeiser en verwacht vooral dat leningen en interest terugbetaald worden."),
        ]),
        dict(kop="Missie, visie en strategie", blokken=[
            ("kader", tabel(["begrip", "betekenis", "voorbeeld"],
                            [["missie", "waarom de onderneming bestaat en wat ze doet; blijft lang hetzelfde", "'Wij bakken elke dag vers brood met lokale granen.'"],
                             ["visie", "waar ze in de toekomst wil staan: een toekomstbeeld, niet hoe ze er vandaag voor staat", "'Wij willen in 2030 de meest duurzame bakkerij van Limburg zijn.'"],
                             ["strategie", "het plan om van de missie naar de visie te gaan", "doelen en acties, die wel elk jaar kunnen veranderen"]])),
            ("p", "De bedrijfsstrategie hangt af van de doelgroep, de concurrentie, de producten, de middelen en de omgeving. Een strategie houdt dus rekening met de omgeving. "
                  "<strong>Actuele ontwikkelingen</strong> beïnvloeden de strategie: een strengere wet op verpakkingen voor een producent van plastic flessen, of sterk stijgende energieprijzen, waarop een bedrijf kan beslissen te investeren in zonnepanelen."),
        ]),
        dict(kop="Het ondernemingsplan", blokken=[
            ("p", "In een <strong>ondernemingsplan</strong> (businessplan) beschrijft een starter zijn idee, de markt, de organisatie en de financiën. Zo toetst hij zijn idee en overtuigt hij financiers: banken vragen het vaak voor ze een lening geven."),
            ("kader", "<ul><li>voorstelling van de ondernemer, het product en de markt;</li>"
                      "<li>een <strong>marketingplan</strong>;</li>"
                      "<li>een <strong>financieel plan</strong>: de verwachte omzet, kosten en financiering, met een openingsbalans, een resultatenbegroting en een liquiditeitsbegroting. Bij de oprichting van een bv is het verplicht.</li></ul>"),
            ("p", "Een <strong>marktonderzoek</strong> helpt om de vraag in te schatten en de omzet beter te voorspellen: wie de klanten zijn, wat de concurrenten doen, prijzen en trends. "
                  "Het bestaat uit <strong>deskresearch</strong> (bestaande gegevens opzoeken) en <strong>fieldresearch</strong> (zelf nieuwe verzamelen), bijvoorbeeld een enquête bij mogelijke klanten over wat ze willen en wat ze willen betalen."),
        ]),
    ],
    onthoud=[
        "SWOT: sterktes en zwaktes intern, kansen en bedreigingen extern.",
        "Stakeholders: intern (werknemers, eigenaars) en extern (klanten, buren, overheid, bank); belangen kunnen botsen.",
        "Missie = waarom we bestaan; visie = toekomstbeeld; strategie = de weg ertussen.",
        "Ondernemingsplan met marketingplan en financieel plan; marktonderzoek: desk- en fieldresearch.",
    ])


# ───────────────────────── 14. Het Business Model Canvas en de BCG-matrix
def bmc(breedte=470):
    """Het Business Model Canvas: negen vakken op één blad."""
    W, H, top = breedte - 4, 250, 180
    c = (W) / 5
    d = []
    def vak(x, y, w, h, t1, t2="", kleur=svg.FOREST):
        d.append(f'<rect x="{x + 2:.1f}" y="{y + 2:.1f}" width="{w - 4:.1f}" height="{h - 4:.1f}" rx="6" fill="{kleur}" fill-opacity=".12" stroke="{kleur}" stroke-width="1.2"/>')
        d.append(svg._tekst(x + w / 2, y + h / 2 - 2, t1, 10, svg.INK, "middle", True))
        if t2:
            d.append(svg._tekst(x + w / 2, y + h / 2 + 11, t2, 10, svg.INK, "middle", True))
    vak(0, 0, c, top, "strategische", "partners")
    vak(c, 0, c, top / 2, "kern-", "activiteiten")
    vak(c, top / 2, c, top / 2, "kern-", "middelen")
    vak(2 * c, 0, c, top, "waarde-", "proposities", svg.AMBER)
    vak(3 * c, 0, c, top / 2, "klant-", "relaties")
    vak(3 * c, top / 2, c, top / 2, "kanalen")
    vak(4 * c, 0, c, top, "klant-", "segmenten")
    vak(0, top, W / 2, H - top, "kostenstructuur", "", svg.DIM)
    vak(W / 2, top, W / 2, H - top, "inkomstenstromen", "", svg.DIM)
    return svg._svg(breedte, H, "".join(d))


zet("het-business-model-canvas-en-de-bcg-matrix",
    titel="Het Business Model Canvas en de BCG-matrix",
    onder="Een bedrijfsmodel op één blad uittekenen, en een portfolio van producten beoordelen met de BCG-matrix.",
    secties=[
        dict(kop="Het Business Model Canvas", blokken=[
            ("p", "Het <strong>Business Model Canvas</strong> (BMC) past op <strong>één blad</strong> en geeft een snel overzicht van het bedrijfsmodel, geen lang document. Je kan er ook een nieuw bedrijfsidee snel mee uittekenen. Het heeft <strong>negen</strong> bouwstenen."),
            ("fig", bmc(), "Links de kant van de onderneming, rechts de klantkant, in het midden de waardepropositie. Onderaan het geld."),
        ]),
        dict(kop="De negen bouwstenen", blokken=[
            ("kader", tabel(["bouwsteen", "vraag", "voorbeeld"],
                            [["waardeproposities (value propositions)", "welke waarde creëer je voor de klant: welk probleem los je op, welke behoefte vervul je?", "vers brood elke dag"],
                             ["klantsegmenten (customer segments)", "voor wie creëer je waarde: de groepen klanten", "particulieren en bedrijven, elk met een eigen waardepropositie"],
                             ["kanalen (channels)", "hoe bereik je de klant, hoe komt het product bij hem?", "een webshop of een winkel (een webshop is een kanaal, geen kernmiddel)"],
                             ["klantrelaties", "hoe houd je contact met de klanten?", "persoonlijke hulp (een persoonlijke coach in een fitnesscentrum), zelfbediening, een community"],
                             ["kernactiviteiten (key activities)", "wat doe je vooral?", "brood bakken en verkopen"],
                             ["kernmiddelen (key resources)", "wat heb je nodig?", "een oven, een winkelpand, ervaren bakkers"],
                             ["strategische partners (key partners)", "wie helpt je de waardepropositie waar te maken?", "de molen die het meel levert; een batterijproducent voor een fietsfabrikant"],
                             ["inkomstenstromen (revenue streams)", "hoe verdien je geld?", "een maandelijks abonnement bij een streamingdienst"],
                             ["kostenstructuur (cost structure)", "wat zijn de belangrijkste kosten?", "de huur van servers en de lonen van programmeurs"]])),
            ("p", "Kernmiddelen zijn wat je <strong>hebt</strong>, kernactiviteiten wat je <strong>doet</strong>. Klantsegmenten, kanalen en klantrelaties staan aan de klantkant; activiteiten, middelen en partners aan de kant van de onderneming. "
                  "Inkomstenstromen en kostenstructuur gaan over geld en bepalen samen of het model winstgevend is."),
        ]),
        dict(kop="De BCG-matrix", blokken=[
            ("p", "Met de <strong>BCG-matrix</strong> beoordeelt een onderneming haar <strong>portfolio</strong> van producten: welke leveren geld op en welke kosten geld? Ze zet de <strong>marktgroei</strong> uit tegen het <strong>relatief marktaandeel</strong> "
                  "(je marktaandeel tegenover dat van de grootste concurrent; boven 1 ben je de marktleider)."),
            ("fig", kwadrant([("star", "investeren", svg.FOREST), ("question mark", "kiezen: investeren of stoppen", svg.AMBER),
                              ("cash cow", "melken", svg.FOREST), ("dog", "afstoten of uitfaseren", svg.DIM)],
                             rijkop=("hoge groei", "lage groei"), kolkop=("hoog marktaandeel", "laag marktaandeel")),
             "De vier vakken van de BCG-matrix met de strategie die er meestal bij past."),
            ("kader", tabel(["vak", "kenmerken", "voorbeeld"],
                            [["star", "hoog marktaandeel, sterk groeiende markt; groeit mee en vraagt nog veel investeringen, levert dus niet altijd meer op dan hij kost. Stopt de markt met groeien, dan wordt hij meestal een cash cow", ""],
                             ["cash cow (melkkoe)", "hoog marktaandeel, markt groeit nauwelijks; brengt veel geld op en vraagt weinig investeringen. Dat geld gaat naar stars en question marks", "gsm-hoesjes: 40 % van een markt die 2 % groeit"],
                             ["question mark", "laag marktaandeel in een groeiende markt; onzeker of het een star wordt. Met investeringen kan het een star worden, anders een dog", "sportdrankje: 3 % van een markt die 20 % groeit"],
                             ["dog (poor dog)", "laag marktaandeel, weinig marktgroei; levert weinig op en heeft weinig toekomst", ""]])),
            ("p", "Om een product te plaatsen heb je de groei van de markt en het marktaandeel tegenover de concurrent nodig, bijvoorbeeld uit een marktrapport of krantenartikel. "
                  "Een gezonde portfolio heeft een mix van cash cows, stars en question marks: de cash cows betalen de investeringen in de groeiers."),
        ]),
    ],
    onthoud=[
        "BMC: negen bouwstenen op één blad; de waardepropositie in het midden.",
        "Kernmiddelen = wat je hebt; kernactiviteiten = wat je doet; kanalen = hoe je de klant bereikt.",
        "BCG: marktgroei tegen relatief marktaandeel.",
        "Star (investeren), cash cow (melken), question mark (kiezen), dog (afstoten).",
    ])


# ───────────────────────── 15. Marketingstrategie en de marketingmix
zet("marketingstrategie-en-de-marketingmix",
    titel="Marketingstrategie en de marketingmix",
    onder="De 4 P's en de 4 C's, soorten markten en goederen, merken, de productlevenscyclus, prijs, distributie, online marketing en de customer journey.",
    secties=[
        dict(kop="Marketingmix en doelgroep", blokken=[
            ("p", "Een <strong>doelgroep</strong> is de groep klanten die je wil bereiken. Een duidelijke doelgroep helpt om de marketingmix goed af te stemmen. "
                  "Een <strong>buyer persona</strong> is een uitgewerkt profiel van een typische klant, met naam, leeftijd, interesses en noden: zo communiceer je gerichter."),
            ("kader", tabel(["4 P's (de onderneming)", "4 C's (vanuit de klant)", "vraag"],
                            [["product", "customer (value)", "welke waarde krijgt de klant?"],
                             ["prijs", "cost", "alle kosten voor de klant, niet enkel de prijs: ook tijd, verplaatsing en moeite"],
                             ["plaats", "convenience", "hoe gemakkelijk kan de klant het product krijgen?"],
                             ["promotie", "communication", "hoe praat je met de klant?"]])),
            ("kader", tabel(["vorm", "betekenis", "voorbeeld"],
                            [["B2B", "business to business", "kantoormeubelen verkopen aan bedrijven"],
                             ["B2C", "business to consumer", "een supermarkt"],
                             ["C2C", "consumer to consumer", "je oude fiets via een tweedehandssite aan een particulier verkopen"],
                             ["C2B", "consumer to business", "een foto aanbieden aan een fotobank"]])),
            ("p", "<strong>E-commerce</strong> is kopen en verkopen via het internet: webshops en online platformen."),
        ]),
        dict(kop="Product", blokken=[
            ("kader", tabel(["soort goed", "kenmerk", "voorbeeld"],
                            [["convenience goed (gemaksgoed)", "vaak en zonder vergelijken gekocht", "een pak melk"],
                             ["shopping goed", "je vergelijkt prijzen en merken", "een wasmachine"],
                             ["unsought goed (ongezocht)", "koop je niet uit jezelf", "een uitvaartverzekering"],
                             ["industrieel goed", "door bedrijven gekocht om verder te produceren", "grondstoffen, machines"]])),
            ("p", "De <strong>breedte</strong> van een assortiment is het aantal productgroepen, de <strong>diepte</strong> het aantal varianten binnen een productgroep. "
                  "Een <strong>A-merk</strong> is een bekend fabrikantenmerk, meestal duurder. Een <strong>winkelmerk</strong> is een merk van de winkelketen zelf, als standaard-, budget- en biolijn. "
                  "<strong>Multibrands</strong>: verschillende merken voor dezelfde productgroep, om verschillende doelgroepen aan te spreken. "
                  "<strong>Lijnextensie</strong>: een nieuwe variant in dezelfde productgroep onder dezelfde naam (een nieuwe smaak chips). <strong>Merkextensie</strong>: het merk stapt in een nieuwe productgroep (een chocolademerk dat ijsjes uitbrengt)."),
            ("fig", svg.stappen(["ontwikkeling", "introductie", "groei", "volwassenheid", "neergang"]), "De productlevenscyclus: ontwikkeling, introductiefase, groeifase, volwassenheidsfase en neergangsfase."),
            ("p", "In de <strong>introductiefase</strong> is de omzet laag en zijn de reclamekosten hoog: het product moet nog bekend raken. In de <strong>groeifase</strong> stijgt de omzet het snelst. In de <strong>neergangsfase</strong> daalt de omzet."),
        ]),
        dict(kop="Prijs en plaats", blokken=[
            ("kader", tabel(["prijsstrategie", "uitleg"],
                            [["penetratieprijs", "laag starten om snel marktaandeel te winnen"],
                             ["afroomprijsstrategie (afromen)", "een nieuw product eerst duur voor wie het meteen wil; daarna zakt de prijs voor een breder publiek"]])),
            ("kader", tabel(["distributie", "uitleg", "voorbeeld"],
                            [["intensief", "zo veel mogelijk verkooppunten", "frisdrank in elke supermarkt, tankstation en automaat"],
                             ["selectief", "een beperkt aantal geschikte verkooppunten", "elektronica bij gespecialiseerde winkels"],
                             ["exclusief", "heel weinig verkooppunten, versterkt het luxebeeld", "luxehorloges in enkele winkels per land"]])),
            ("p", "<strong>Pushstrategie</strong>: het product via de tussenhandel naar de klant duwen, bijvoorbeeld met extra korting voor winkels die het opnemen. "
                  "<strong>Pullstrategie</strong>: de producent richt zijn reclame rechtstreeks op de consument, die dan zelf in de winkel naar het product vraagt."),
        ]),
        dict(kop="Promotie online en de customer journey", blokken=[
            ("p", "<strong>SEO</strong> (search engine optimization): hoger komen in de gewone zoekresultaten door goede inhoud en techniek, onbetaald. "
                  "<strong>SEA</strong> (search engine advertising): betaalde advertenties in een zoekmachine, je betaalt per klik. Ze betekenen dus niet hetzelfde."),
            ("fig", svg.stappen(["bewustwording", "overweging", "aankoop", "service", "loyaliteit"]), "De customer journey (klantreis)."),
            ("p", "De <strong>customer journey</strong> is de reeks fasen die een klant doorloopt, van het eerste contact tot terugkomen. Wie reviews leest en prijzen vergelijkt, zit in de fase <strong>overweging</strong>. "
                  "Een <strong>touchpoint</strong> is elk contactmoment tussen klant en merk: een advertentie, een website, de kassa, de klantendienst. "
                  "In de fase service (hulp na de aankoop) zijn de klantendienst en een handleiding touchpoints. Een klantenkaart met spaarpunten speelt in op <strong>loyaliteit</strong>."),
        ]),
    ],
    onthoud=[
        "4 P's: product, prijs, plaats, promotie; 4 C's vanuit de klant: customer, cost, convenience, communication.",
        "Convenience, shopping, unsought en industriële goederen.",
        "Lijnextensie: nieuwe variant; merkextensie: nieuwe productgroep.",
        "Penetratieprijs laag, afromen hoog; distributie intensief, selectief, exclusief.",
        "SEO onbetaald, SEA betaald. Customer journey: bewustwording, overweging, aankoop, service, loyaliteit.",
    ])


# ───────────────────────── 16. De arbeidsovereenkomst
zet("de-arbeidsovereenkomst-begin-schorsing-en-einde",
    titel="De arbeidsovereenkomst: begin, schorsing en einde",
    onder="Wanneer is er een arbeidsovereenkomst, welke soorten bestaan er, wanneer wordt ze geschorst en hoe eindigt ze?",
    secties=[
        dict(kop="Het begin", blokken=[
            ("p", "Drie elementen maken van een afspraak een arbeidsovereenkomst: <strong>arbeid, loon en gezag</strong>. De werknemer werkt tegen loon onder het gezag van de werkgever."),
            ("p", "<strong>Geldigheidsvereisten</strong>: toestemming van beide partijen, bekwaamheid van de partijen, een geoorloofd voorwerp en een geoorloofde oorzaak. "
                  "Een overeenkomst om illegaal werk te doen is dus nietig, ook als beide partijen akkoord gaan. "
                  "Uit een arbeidsovereenkomst lees je de partijen, de duur van de overeenkomst en de aard en omvang van het werk af."),
            ("kader", tabel(["indeling", "soorten"],
                            [["aard van het werk", "arbeider (handarbeid) of bediende (hoofdarbeid); sinds het eenheidsstatuut zijn veel verschillen verdwenen, maar het onderscheid bestaat nog"],
                             ["duur", "onbepaalde tijd, bepaalde tijd (eindigt automatisch op de einddatum, zonder opzegging), duidelijk omschreven werk (eindigt als het werk klaar is, bv. een huis bouwen), vervangingsovereenkomst"],
                             ["deeltijds", "moet schriftelijk, met de werkroosters erbij"],
                             ["studentenovereenkomst", "schriftelijk, uiterlijk bij de start van het werk; verminderde sociale bijdragen tot een maximum aantal uren per jaar"],
                             ["flexi-job", "bijverdienen in bepaalde sectoren tegen een gunstig fiscaal regime, voor wie al 4/5 werkt elders of gepensioneerden"]])),
        ]),
        dict(kop="De schorsing", blokken=[
            ("p", "Bij een <strong>schorsing</strong> vallen werk en loon tijdelijk stil, maar de overeenkomst blijft bestaan."),
            ("kader", tabel(["in hoofde van de werknemer", "uitleg"],
                            [["ziekte", "de werkgever betaalt de eerste periode het loon, daarna het ziekenfonds; de werknemer bezorgt een doktersattest"],
                             ["jaarlijkse vakantie", "geen einde van de overeenkomst; de werknemer krijgt vakantiegeld"],
                             ["klein verlet", "afwezigheid met loon bij een familiefeit (huwelijk, overlijden)"],
                             ["verlof om dwingende redenen", "in principe onbetaald, tenzij een cao of afspraak iets anders bepaalt"],
                             ["bevallingsverlof, geboorteverlof", "geboorteverlof voor de vader: deels door de werkgever, de rest door het ziekenfonds"],
                             ["zorgverlof", "ernstige zorg aan een familielid of gezinslid"],
                             ["tijdskrediet, loopbaanonderbreking", "tijdelijk minder of niet werken, met een uitkering van de RVA"],
                             ["politiek mandaat, lekenrechter", "bv. schepen worden, of zetelen in de arbeidsrechtbank"],
                             ["voorlopige hechtenis", "de overeenkomst wordt geschorst"],
                             ["staking", "de werknemers leggen het werk neer: geen loon, vakbondsleden kunnen een stakingsvergoeding krijgen"]])),
            ("kader", tabel(["in hoofde van de werkgever", "uitleg"],
                            [["economische werkloosheid", "gebrek aan werk wegens economische redenen, bv. minder bestellingen"],
                             ["werkloosheid wegens slecht weer", "een bouwvakker bij zware vorst; uitkering via de RVA"],
                             ["technische stoornis, overmacht", "een fabriek valt stil door een brand. Overmacht kan ook bij de werknemer"],
                             ["verloren arbeidsuren met gewaarborgd dagloon", "loon voor een dag waarop het werk buiten zijn schuld stilvalt, bv. een machine valt stil"],
                             ["uitsluiting of lock-out", "de werkgever sluit de werknemers uit (niet hetzelfde als een staking)"]])),
        ]),
        dict(kop="Het einde", blokken=[
            ("kader", "<ul><li><strong>Opzegging met een opzegtermijn</strong>: de periode tussen de opzegging en het einde. De duur hangt af van de anciënniteit; je leest ze af in een tabel (bv. 1 tot 2 jaar: 7 weken bij ontslag door de werkgever, dus ook bij 18 maanden). Stopt de werknemer zelf, dan is de termijn korter (een aparte kolom).</li>"
                      "<li><strong>Verbrekingsvergoeding</strong>: de werkgever betaalt het loon voor de opzegtermijn zonder dat er gewerkt wordt.</li>"
                      "<li><strong>Ontslag om dringende reden</strong> (bv. diefstal): de overeenkomst eindigt meteen, zonder opzegtermijn.</li>"
                      "<li><strong>Beëindiging in onderling akkoord</strong>: geen opzegtermijn nodig.</li>"
                      "<li>Het <strong>einde van de termijn</strong> of van het werk, en het <strong>overlijden</strong> van de werknemer.</li></ul>"),
        ]),
    ],
    onthoud=[
        "Arbeidsovereenkomst = arbeid + loon + gezag.",
        "Schorsing: werk en loon vallen stil, de overeenkomst blijft (ziekte, vakantie, verlof, staking, economische werkloosheid ...).",
        "Opzegtermijn volgens anciënniteit; korter als de werknemer zelf stopt.",
        "Dringende reden: meteen weg, zonder opzegtermijn.",
    ])


# ───────────────────────── 17. Logistiek en supply chain management
from maak_wiskunde_basis_beyond import plot as _plot  # noqa: E402  (zelfde grafiekhulp)

zet("logistiek-en-supply-chain-management",
    titel="Logistiek en supply chain management",
    onder="De keten van leverancier tot klant, magazijnen, inkoop, productievormen, voorraadbeheer en de LPI.",
    secties=[
        dict(kop="De keten", blokken=[
            ("p", "<strong>Logistiek management</strong> gaat over de goederenstroom in de eigen onderneming. <strong>Supply chain management</strong> kijkt breder: de hele keten van leverancier tot klant afstemmen, ook buiten de eigen onderneming. "
                  "Een <strong>logistieke flow</strong> bestaat uit goederen, informatie en geld: goederen gaan naar de klant, informatie en geld gaan beide richtingen uit."),
            ("kader", tabel(["model", "uitleg"],
                            [["pushmodel (supply management)", "produceren op basis van een voorspelling; de goederen worden in de markt geduwd. Meestal meer voorraad"],
                             ["pullmodel", "de productie start pas na een vraag van de klant; de klant trekt de goederen door de keten"]])),
            ("p", "Het <strong>klantorderontkoppelingspunt (KOOP)</strong> is het punt vanaf waar op bestelling gewerkt wordt: ervoor op voorraad, erna op bestelling. "
                  "Een meubelmaker die een kast pas maakt als de klant bestelt, met hout uit voorraad: KOOP bij de grondstoffen. Een supermarkt met blikken soep uit voorraad: KOOP bij de klant."),
        ]),
        dict(kop="Magazijnen", blokken=[
            ("kader", tabel(["magazijn", "uitleg"],
                            [["bevoorradingsmagazijn (productiemagazijn)", "materialen voor de productie, dicht bij de productie"],
                             ["distributiecentrum", "verdeelt naar winkels, bv. het centrale magazijn van een supermarktketen"],
                             ["crossdockmagazijn (transitmagazijn)", "goederen worden meteen overgeladen, zonder lange opslag"],
                             ["groupagecentrum", "bundelt kleine zendingen van verschillende bedrijven tot één grote lading: goedkoper vervoer"],
                             ["public warehouse", "verhuurt opslagruimte aan verschillende bedrijven"]])),
        ]),
        dict(kop="Inkoop en productie", blokken=[
            ("p", "Inkoopstrategieën: <strong>strategisch</strong> (keuzes op lange termijn, zoals met welke leveranciers je samenwerkt), tactisch, <strong>operationeel</strong> (de dagelijkse bestellingen) en ondersteunend."),
            ("fig", svg.stappen(["specifiëren", "aanvraag", "leverancier|kiezen", "onder-|handelen", "bestellen", "controleren"]), "Het inkoopproces: na het onderhandelen plaats je een aankooporder; eerst controleer je de goederen, als laatste de factuur en de betaling."),
            ("kader", tabel(["productievorm", "uitleg", "voorbeeld"],
                            [["divergente productie", "uit één grondstof veel producten", "melk tot boter, kaas en room"],
                             ["convergente productie", "uit veel onderdelen één product", "een auto"],
                             ["parallelle productie", "verschillende producten op aparte lijnen naast elkaar, onafhankelijk", ""],
                             ["serieproductie", "een reeks gelijke producten na elkaar", "500 identieke stoelen"],
                             ["mass customisation", "een product op maat aan de prijs van massaproductie", "sneakers die je online zelf samenstelt"]])),
            ("p", "<strong>Outsourcing</strong>: een taak uitbesteden aan een ander bedrijf (boekhouding, transport). Voordelen: je focust op je kernactiviteit en gebruikt de kennis van een specialist. Nadeel: minder controle."),
        ]),
        dict(kop="Voorraadbeheer", blokken=[
            ("kader", tabel(["begrip", "uitleg"],
                            [["technische voorraad", "wat fysiek in het magazijn ligt; je kan het tellen"],
                             ["gereserveerde voorraad", "ligt er nog, maar is al beloofd aan klanten: niet meer vrij te verkopen"],
                             ["beschikbare voorraad", "technische voorraad + besteld − gereserveerd: 500 + 200 − 150 = 550 stuks"],
                             ["minimumvoorraad (veiligheidsvoorraad)", "de buffer die er altijd moet zijn"],
                             ["maximumvoorraad", "de grootste voorraad die je aanhoudt; hoger kost te veel of past niet"]])),
            ("p", "<strong>Voorraadkosten</strong>: de huur van het magazijn, de interest op het geld dat in de voorraad zit, verzekering, bederf en veroudering. "
                  "Grote bestellingen geven een grotere gemiddelde voorraad, dus <strong>hogere bewaarkosten</strong>, maar de <strong>bestelkosten dalen</strong>. Het laagste punt van de totale kosten geeft de beste bestelgrootte."),
            ("fig", _plot([(lambda q: 40 / q if q > 0 else None, "a", "bestelkosten"), (lambda q: 0.4 * q, "g", "bewaarkosten"),
                           (lambda q: 40 / q + 0.4 * q if q > 0 else None, "v", "totaal")], 0, 20, 0, 16, breedte=340, hoogte=210,
                          punten=[(10, 8, "")], stap_x=2, stap_y=2, xlabel="q", ylabel="kosten", toon_een=False),
             "Horizontaal de bestelgrootte q. Bestelkosten dalen, bewaarkosten stijgen; het punt op de totale kosten is de beste bestelgrootte."),
            ("p", "<strong>Just In Time</strong> (JIT): goederen precies op tijd geleverd, zodat er bijna geen voorraad nodig is. Lagere voorraadkosten, maar betrouwbare leveranciers nodig: "
                  "een onderneming wordt net <strong>gevoeliger</strong> voor problemen bij leveranciers, want er is weinig buffer."),
            ("weetje", "De <strong>Logistics Performance Index (LPI)</strong> van de Wereldbank (lpi.worldbank.org) meet hoe goed de logistiek van een land werkt. Een hogere score is beter: goede infrastructuur en een vlotte douane maken een land aantrekkelijker voor logistieke bedrijven."),
        ]),
    ],
    onthoud=[
        "Supply chain = de hele keten; logistiek = de eigen onderneming. Flow: goederen, informatie, geld.",
        "Push: op voorspelling. Pull: op vraag van de klant. KOOP: vanaf daar op bestelling.",
        "Beschikbare voorraad = technisch + besteld − gereserveerd.",
        "Grotere bestelling: lagere bestelkosten, hogere bewaarkosten.",
        "JIT: weinig voorraad, maar gevoelig voor leveringsproblemen.",
    ])


# ───────────────────────── 18. Human-resources-management
zet("human-resources-management",
    titel="Human-resources-management",
    onder="Het beleid rond de medewerkers: instroom, doorstroom en uitstroom, belonen en motiveren, en hr-KPI's.",
    secties=[
        dict(kop="Wat is hrm?", blokken=[
            ("p", "<strong>Human-resources-management</strong> (hrm) is het beleid rond de medewerkers, van aanwerven en opleiden tot belonen en afscheid nemen: de hele loopbaan, niet enkel de aanwerving. "
                  "Het is belangrijk voor het totale bedrijfsbeleid: de juiste mensen maken de strategie waar. "
                  "Taken van de hr-afdeling: personeel aanwerven, opleidingen organiseren, loonbeleid, evaluaties en welzijn op het werk."),
            ("fig", svg.stappen(["instroom", "doorstroom", "uitstroom"]), "De drie fasen."),
            ("kader", tabel(["fase", "instrumenten"],
                            [["instroom", "werving (mensen aantrekken om te solliciteren), selectie (de beste kandidaat kiezen; eerst werven, dan selecteren), onthaalbeleid (nieuwe medewerkers goed laten starten, zodat ze niet snel vertrekken)"],
                             ["doorstroom", "groeien binnen de onderneming: opleiding en loopbaanplanning, functioneringsgesprek (hoe loopt het werk, hoe kan de werknemer groeien)"],
                             ["uitstroom", "het vertrek: pensioen, ontslag, outplacement (begeleiding van een ontslagen werknemer naar een nieuwe job), exitgesprek (waarom vertrekken mensen?)"]])),
        ]),
        dict(kop="Werving en selectie", blokken=[
            ("p", "Bij <strong>interne werving</strong> werf je iemand uit het eigen bedrijf aan: die kent het bedrijf al. Een <strong>uitzendkantoor</strong> kan helpen bij de werving door kandidaten te zoeken en voor te stellen."),
            ("kader", tabel(["selectietool", "uitleg"],
                            [["interview", "een gesprek, bv. met de leidinggevende en iemand van hr: de meest gebruikte tool"],
                             ["proef of test", "test de kennis of vaardigheden"],
                             ["assessment", "praktijkopdrachten, zoals een rollenspel of een postbakoefening"],
                             ["referentie", "informatie vragen aan een vorige werkgever, altijd met toestemming van de kandidaat"]])),
        ]),
        dict(kop="Belonen en motiveren", blokken=[
            ("kader", tabel(["financiële beloning", "niet-financiële motivatie"],
                            [["loonsverhoging, bonus op basis van prestaties, winstdeelname, premies en commissies", "erkenning en waardering van de leidinggevende, verantwoordelijkheid, uitdaging"],
                             ["extralegale voordelen: maaltijdcheques, ecocheques", "thuiswerken mogelijk maken"]])),
            ("p", "In een <strong>cafetariaplan</strong> kies je zelf voordelen uit een pakket, bijvoorbeeld een fiets, extra vakantie of een smartphone in plaats van een deel van de bonus: een beloning op maat motiveert meer. "
                  "Werknemers die zich gewaardeerd voelen, blijven meestal langer: dat verlaagt het personeelsverloop."),
            ("p", "<strong>Duurzaam hr-beleid</strong>: medewerkers lang gezond en gemotiveerd laten werken, met werkbaar werk, levenslang leren en aandacht voor welzijn."),
        ]),
        dict(kop="Hr-KPI's", blokken=[
            ("p", "Een <strong>hr-KPI</strong> (key performance indicator) is een cijfer dat het hr-beleid meet, zodat je het kan bijsturen: cijfers tonen of maatregelen werken. "
                  "Voorbeelden: personeelsverloop, ziekteverzuim, opleidingsuren per werknemer, tevredenheid."),
            ("kader", tabel(["KPI", "formule", "voorbeeld"],
                            [["personeelsverloop", "vertrokken werknemers / gemiddeld aantal werknemers · 100", "20 / 200 = 10 %"],
                             ["ziekteverzuim", "zieke werknemers op een gemiddelde dag / aantal werknemers · 100", "3 / 50 = 6 %"]])),
            ("p", "Een hoog ziekteverzuim is geen positief signaal: het kan wijzen op slechte werkomstandigheden of te veel werkdruk. "
                  "Vertrekken veel jonge werknemers na een jaar, dan kan een beter onthaal en loopbaanplan helpen: ze voelen zich sneller thuis en zien groeikansen."),
        ]),
    ],
    onthoud=[
        "Instroom (werving, selectie, onthaal), doorstroom (opleiding, loopbaan, functioneringsgesprek), uitstroom (outplacement, exitgesprek).",
        "Selectietools: interview, test, assessment, referentie.",
        "Financieel (bonus, loonsverhoging, cheques) en niet-financieel (erkenning, verantwoordelijkheid, thuiswerk); cafetariaplan.",
        "Personeelsverloop = vertrokken / gemiddeld aantal · 100.",
    ])


# ───────────────────────── 19. Kostprijsberekening en break-even
zet("kostprijsberekening-en-break-even",
    titel="Kostprijsberekening en break-even",
    onder="Soorten kosten, de kostprijs en de verkoopprijs berekenen, indirecte kosten verdelen en het break-evenpunt vinden.",
    secties=[
        dict(kop="Soorten kosten", blokken=[
            ("kader", tabel(["kost", "uitleg", "voorbeeld"],
                            [["vast", "verandert niet als je meer of minder produceert; per stuk daalt hij als je meer maakt", "de huur van de fabriek"],
                             ["variabel", "totaal stijgt met de productie, per stuk blijft hij meestal gelijk", "de grondstoffen"],
                             ["direct", "toe te wijzen aan één product", "het hout voor één tafel; de lonen van een arbeider die enkel aan dat product werkt"],
                             ["indirect", "te verdelen over meerdere producten", "de verlichting van de fabriek"]])),
            ("p", "De <strong>kostendrager</strong> is het product waaraan je kosten toerekent. Een <strong>kostenplaats</strong> is een afdeling waar kosten gemaakt worden, bv. zagen of verpakken. "
                  "Een <strong>verdeelsleutel</strong> bepaalt hoe je indirecte kosten verdeelt, bv. volgens de oppervlakte (of het volume, voor verwarming) of het aantal machine-uren."),
        ]),
        dict(kop="Indirecte kosten verdelen", blokken=[
            ("p", "<strong>Eenvoudige opslagmethode</strong>: directe kosten + een percentage voor de indirecte kosten. 200 + 30 % = 260 euro; 500 · 1,40 = 700 euro. "
                  "Minder nauwkeurig, want ze verdeelt de indirecte kosten met één percentage. Een <strong>kostenverdeelstaat</strong> verdeelt de <strong>indirecte</strong> kosten per afdeling met een passende verdeelsleutel; directe kosten wijs je meteen aan het product toe."),
            ("p", "Voorbeeld: 12 000 euro indirecte kosten volgens oppervlakte. Afdeling A 300 m², B 100 m²: A krijgt 3/4, dus 9 000 euro, en B 3 000 euro."),
        ]),
        dict(kop="Van kostprijs tot verkoopprijs", blokken=[
            ("kader", tabel(["stap", "samenstelling", "voorbeeld"],
                            [["fabricagekostprijs", "directe grondstoffen + directe lonen in de productie + deel van de indirecte productiekosten", "80 euro"],
                             ["verkoopkostprijs", "fabricagekostprijs + verkoop- en administratiekosten (dus altijd ≥ fabricagekostprijs)", "80 + 20 = 100 euro"],
                             ["verkoopprijs zonder btw", "verkoopkostprijs + winstopslag", "100 · 1,25 = 125 euro; 80 · 1,20 = 96 euro"]])),
            ("p", "Een handelaar rekent vaak een opslag op de <strong>inkoopprijs</strong>: een jas van 40 euro met 60 % geeft 64 euro. Dezelfde opslag op de verkoopkostprijs geeft een ander bedrag, want die is hoger dan de inkoopprijs."),
        ]),
        dict(kop="Break-even", blokken=[
            ("p", "De <strong>dekkingsbijdrage per stuk</strong> = verkoopprijs − variabele kosten per stuk: elk stuk draagt dat bedrag bij om de vaste kosten te dekken."),
            ("kader", "<p style='text-align:center'><strong>break-evenafzet = vaste kosten / dekkingsbijdrage per stuk</strong> (in stuks)<br>"
                      "<strong>break-evenomzet = break-evenafzet · verkoopprijs</strong> (in euro)</p>"),
            ("fig", _plot([(lambda q: 50 * q, "v", "opbrengsten"), (lambda q: 20000 + 30 * q, "a", "totale kosten"), (lambda q: 20000, "g", "vaste kosten")],
                          0, 2000, 0, 100000, breedte=360, hoogte=220, punten=[(1000, 50000, "break-even")], stap_x=250, stap_y=12500,
                          xlabel="q", ylabel="euro", toon_een=False),
             "Vaste kosten 20 000 euro, prijs 50 euro, variabele kosten 30 euro: break-even bij 1 000 stuks en 50 000 euro. Horizontaal het aantal stuks q. Links verlies, rechts winst."),
            ("kader", tabel(["gegeven", "break-even"],
                            [["vaste kosten 20 000, prijs 50, variabel 30", "20 000 / 20 = 1 000 stuks; omzet 50 000 euro"],
                             ["vaste kosten 36 000, prijs 20, variabel 8", "36 000 / 12 = 3 000 stuks"],
                             ["vaste kosten 10 000, dekkingsbijdrage 25", "400 stuks"],
                             ["vaste kosten 60 000, dekkingsbijdrage 40 % van de prijs", "omzet 60 000 / 0,40 = 150 000 euro"]])),
            ("p", "Bij de break-evenafzet is er geen winst en geen verlies: opbrengsten en kosten zijn even groot. In de grafiek snijdt de lijn van de totale opbrengsten daar de lijn van de totale kosten; de lijn van de vaste kosten is horizontaal. "
                  "Boven de break-evenafzet levert elk extra stuk winst op ter grootte van de dekkingsbijdrage: 1 500 stuks bij break-even 1 000 en dekkingsbijdrage 20 euro geeft 500 · 20 = 10 000 euro winst."),
            ("p", "Stijgen de <strong>vaste kosten</strong>, dan stijgt de break-evenafzet. Stijgt de <strong>verkoopprijs</strong>, dan stijgt de dekkingsbijdrage en daalt de break-evenafzet. "
                  "Hoge vaste kosten met lage variabele kosten geven een grote dekkingsbijdrage per stuk, maar er moeten ook veel vaste kosten gedekt worden. "
                  "Let op: de break-evenafzet is in stuks, de break-evenomzet in euro."),
        ]),
    ],
    onthoud=[
        "Vast: per stuk dalend. Variabel: per stuk gelijk. Direct: aan één product. Indirect: verdelen met een verdeelsleutel.",
        "Fabricagekostprijs + verkoop- en administratiekosten = verkoopkostprijs; + winstopslag = verkoopprijs.",
        "Dekkingsbijdrage = prijs − variabele kosten per stuk.",
        "Break-evenafzet = vaste kosten / dekkingsbijdrage; break-evenomzet = afzet · prijs.",
    ])


# ───────────────────────── 20. Relationele databanken
def relatiefiguur(breedte=470):
    """Twee tabellen in een één-op-veel-relatie: Klanten (1) en Bestellingen (∞)."""
    d = []
    def tab(x, titel, velden, sleutel):
        d.append(f'<rect x="{x}" y="10" width="150" height="{26 + 18 * len(velden)}" rx="6" fill="#ffffff" stroke="{svg.FOREST}" stroke-width="1.4"/>')
        d.append(f'<rect x="{x}" y="10" width="150" height="24" rx="6" fill="{svg.FOREST}" fill-opacity=".16"/>')
        d.append(svg._tekst(x + 75, 27, titel, 11, svg.INK, "middle", True))
        for i, v in enumerate(velden):
            d.append(svg._tekst(x + 10, 52 + 18 * i, ("🔑 " if v == sleutel else "") + v, 10, svg.INK, "start", v == sleutel))
    tab(30, "Klanten", ["Klantnummer", "Naam", "Gemeente"], "Klantnummer")
    tab(290, "Bestellingen", ["Bestelnummer", "Klantnummer", "Datum", "Bedrag"], "Bestelnummer")
    d.append(f'<path d="M180,48 C235,48 235,66 290,66" fill="none" stroke="{svg.AMBER}" stroke-width="2"/>')
    d.append(svg._tekst(188, 42, "1", 12, svg.AMBER, "start", True))
    d.append(svg._tekst(276, 60, "∞", 14, svg.AMBER, "end", True))
    return svg._svg(breedte, 112, "".join(d))


zet("relationele-databanken",
    titel="Relationele databanken",
    onder="Tabellen, sleutels en relaties, veldeigenschappen en gegevenstypes, en query's in Access.",
    secties=[
        dict(kop="Tabellen en sleutels", blokken=[
            ("p", "Een <strong>relationele databank</strong> bestaat uit tabellen die via relaties verbonden zijn: je koppelt ze met sleutels. Een Access-databank bevat tabellen, query's, formulieren (om gegevens gemakkelijk in te voeren en te bekijken) en rapporten (om overzichtelijk af te drukken, niet om in te voeren)."),
            ("p", "Een <strong>record</strong> is één rij, een <strong>veld</strong> een kolom (bv. Postcode). De <strong>primaire sleutel</strong> is een veld dat elk record uniek maakt, bv. een klantnummer: twee records mogen nooit dezelfde waarde hebben. Ze is vaak een getal of AutoNummering, niet altijd tekst."),
            ("fig", relatiefiguur(), "Een één-op-veel-relatie: een klant plaatst veel bestellingen, een bestelling hoort bij één klant."),
            ("kader", tabel(["begrip", "uitleg"],
                            [["één-op-veel-relatie", "de primaire tabel (Klanten) staat aan de 'één'-kant; haar primaire sleutel komt als veld terug in de gerelateerde tabel (Bestellingen)"],
                             ["één-op-één-relatie", "bij elk record hoort hoogstens één record in de andere tabel, bv. een werknemer en zijn badge"],
                             ["referentiële integriteit", "de koppeling blijft kloppen: geen bestelling voor een onbestaande klant, en een klant met bestellingen blijft staan"],
                             ["redundantie", "dezelfde gegevens op meerdere plaatsen; vermijden door gegevens over meerdere tabellen te splitsen (een klantadres maar één keer)"],
                             ["gegevensintegriteit", "de gegevens zijn juist, volledig en consistent; validatieregels, vereiste velden en referentiële integriteit helpen"]])),
        ]),
        dict(kop="Gegevenstypes en veldeigenschappen", blokken=[
            ("kader", tabel(["gegeven", "gegevenstype"],
                            [["geboortedatum", "Datum/tijd (Access kan ermee rekenen en sorteren)"],
                             ["prijs in euro", "Valuta (rekent nauwkeurig met bedragen)"],
                             ["telefoonnummer", "Korte tekst (je rekent er niet mee en een voorloopnul zou verdwijnen)"],
                             ["'Betaald' ja of nee", "Ja/nee"],
                             ["volgnummer", "AutoNummering"]])),
            ("kader", tabel(["veldeigenschap", "wat ze doet"],
                            [["vereist", "het veld mag niet leeg blijven"],
                             ["validatieregel", "controleert of een waarde mag, bv. Aantal > 0; de validatietekst verschijnt bij een fout"],
                             ["invoermasker", "legt vast hoe je moet invoeren, bv. een postcode met vier cijfers"],
                             ["standaardwaarde", "wordt automatisch ingevuld, bv. Land = België"],
                             ["bijschrift", "de tekst die als kolomnaam getoond wordt"],
                             ["veldlengte (veldgrootte)", "het maximum aantal tekens, bv. 4 voor een Belgische postcode"]])),
        ]),
        dict(kop="Query's en filters", blokken=[
            ("kader", tabel(["query", "wat ze doet"],
                            [["selectiequery", "selecteert en sorteert zonder iets te wijzigen; met een criterium (bv. 'Hasselt' in het veld Gemeente) beperk je de records"],
                             ["totaalquery", "groepeert en rekent: som, gemiddelde, aantal, maximum, minimum. Bv. het aantal bestellingen per klant, of per categorie de totale omzet (één rij per groep)"],
                             ["bijwerkquery (actie)", "wijzigt bestaande gegevens, bv. alle prijzen + 5 %"],
                             ["tabelmaakquery (actie)", "maakt van een selectie een nieuwe tabel, bv. enkel de klanten uit Limburg"],
                             ["toevoegquery (actie)", "voegt records toe aan een bestaande tabel"],
                             ["verwijderquery (actie)", "verwijdert records die aan een voorwaarde voldoen, bv. bestellingen van vóór 2020; dat is definitief"]])),
            ("p", "Een <strong>filter</strong> toont enkel de records die aan de voorwaarde voldoen; de andere blijven bewaard. Met een <strong>selectiefilter</strong> klik je een waarde aan en zie je alle records met dezelfde waarde, bv. dezelfde postcode."),
        ]),
    ],
    onthoud=[
        "Record = rij, veld = kolom; de primaire sleutel is uniek.",
        "Eén-op-veel: de sleutel van de primaire tabel komt terug in de gerelateerde tabel.",
        "Referentiële integriteit: geen bestelling zonder bestaande klant. Splitsen tegen redundantie.",
        "Selectiequery wijzigt niets; actiequery's: bijwerk, tabelmaak, toevoeg, verwijder.",
        "Formulier om in te voeren, rapport om af te drukken.",
    ])
