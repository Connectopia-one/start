"""Internationale handel en samenwerkingsverbanden — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, s_lijn, GROEN, LICHT

# Een trap met vijf treden, genummerd maar zonder namen (eigen tekening).
TREDE_B, TREDE_H, X0, Y_ONDER = 170, 90, 75, 590


def trede(i):
    """Vak (x, y, b, h) van trede i (0 = laagste)."""
    return (X0 + i * TREDE_B, Y_ONDER - (i + 1) * TREDE_H, TREDE_B, (i + 1) * TREDE_H)


def _trap():
    d = [s_tekst(500, 70, "Vijf stappen van economische samenwerking", 24, vet=True),
         s_tekst(500, 102, "van minst naar meest verregaand", 20)]
    for i in range(5):
        x, y, b, h = trede(i)
        d.append(s_vak(x, y, b, h, vul=LICHT if i % 2 == 0 else "#e2ebd8", rand=GROEN, dikte=2.5))
        d.append(s_tekst(x + b / 2, y + 52, f"stap {i + 1}", 26, kleur=GROEN, vet=True))
    d.append(s_lijn(X0 - 10, Y_ONDER, X0 + 5 * TREDE_B + 10, Y_ONDER, dikte=3))
    return d


def trede_zone(i):
    x, y, b, h = trede(i)
    return pix_zone(x + 4, y + 4, b - 8, h - 8)


GRAFIEKEN = [dict(naam="handel-vijf-stappen", titel="", eigen=_trap)]
PRENTEN = [dict(bestand="handel-vijf-stappen.svg", zelf=True, wat="Trap met vijf genummerde stappen van samenwerking", vragen="klikvragen over vrijhandelszone tot monetaire unie")]
P = "handel-vijf-stappen.svg"

VRAGEN = [
    klik(
        "Op welke stap komt er voor het eerst een gemeenschappelijk buitentarief bij? Klik erop.",
        P, [trede_zone(1)],
        "Stap 2 is de douane-unie: bovenop de vrijhandelszone gebruiken alle leden hetzelfde tarief naar buiten.",
    ),
    klik(
        "Op welke stap hoort de eurozone? Klik erop.",
        P, [trede_zone(4)],
        "De eurozone heeft één munt met één centrale bank: een monetaire unie, stap 5.",
    ),
    klik(
        "Op welke stap komt er voor het eerst vrij verkeer van goederen, diensten, personen en kapitaal bij? Klik erop.",
        P, [trede_zone(2)],
        "Stap 3, de gemeenschappelijke markt, voegt de vier vrijheden toe.",
    ),
    met_prent(P, mk(
        "Op stap 1 kiest elk land zelf zijn invoerrechten tegenover landen buiten de groep. Hoe heet die stap?",
        ["Vrijhandelszone", "Douane-unie", "Economische unie", "Gemeenschappelijke markt"],
        0,
        "In een vrijhandelszone vallen de invoerrechten onderling weg, maar naar buiten kiest elk land zelf.",
    )),
    met_prent(P, mk(
        "Wat komt er op stap 4, de economische unie, bij?",
        ["De landen stemmen hun economisch beleid op elkaar af", "Eén gemeenschappelijke munt met één centrale bank voor alle leden",
         "Een gemeenschappelijk buitentarief tegenover alle landen buiten de groep", "Het wegvallen van de invoerrechten tussen de leden onderling"],
        0,
        "Stap 4 voegt het afstemmen van het economisch beleid toe. Eén munt komt pas op stap 5.",
    )),
    tabel(
        "Waar of niet waar over samenwerking tussen landen?",
        [
            ("Elke stap bevat alles van de vorige, plus iets nieuws.", J),
            ("De Europese Unie is minstens een gemeenschappelijke markt.", J),
            ("In een vrijhandelszone hebben alle landen hetzelfde tarief naar buiten.", F),
            ("Een land in een monetaire unie kan zijn munt devalueren om goedkoper te exporteren.", F),
        ],
        "Een gemeenschappelijk buitentarief hoort pas bij de douane-unie. In een monetaire unie heb je geen eigen munt meer om te devalueren.",
    ),
    mk(
        "Frankrijk koopt in een douane-unie wijn bij een lidstaat, hoewel een land buiten de unie goedkoper produceert. Hoe heet dat?",
        ["Handelsverlegging", "Handelsoverschot van de lidstaat", "Nearshoring", "Schaalvoordeel"],
        0,
        "Door het gemeenschappelijk buitentarief wordt de goedkopere wijn van buiten de unie duurder dan die van een lid.",
    ),
    sorteer(
        "Is dit een voordeel of een nadeel van een monetaire unie voor een land?",
        ["Voordeel", "Nadeel"],
        [
            ["Bedrijven hebben geen wisselkoersrisico binnen de unie", "Voordeel"],
            ["Er zijn geen wisselkosten bij handel met andere leden", "Voordeel"],
            ["Het land kan zijn munt niet meer devalueren", "Nadeel"],
        ],
        "Eén munt maakt handel gemakkelijker, maar een land verliest de mogelijkheid om met zijn munt de export goedkoper te maken.",
    ),
    tabel(
        "Wat gebeurt er als landen samenwerken en invoerrechten wegvallen?",
        [
            ("De prijs van goederen uit partnerlanden", "Daalt"),
            ("De concurrentie tussen bedrijven", "Stijgt"),
            ("De grootte van de afzetmarkt", "Stijgt"),
        ],
        "Goedkopere invoer, meer concurrentie, grotere afzetmarkten en schaalvoordelen.",
        kolommen=["Stijgt", "Daalt"],
    ),
    casus(
        "Een land heeft een bbp van 800 miljard euro. De export bedraagt 680 miljard en de import 720 miljard euro.",
        [
            inv("Hoe groot is het saldo van de handelsbalans in miljard euro? Zet een minteken als het negatief is.", "-40",
                "Export min import = 680 − 720 = −40."),
            mk("Hoe noem je dit saldo?", ["Een handelstekort", "Een handelsoverschot", "Een begrotingstekort", "Een monetaire unie"], 0,
               "Het land importeert meer dan het exporteert."),
            inv("Bereken de uitvoerquote in procent. Schrijf enkel het getal.", "85",
                "680 / 800 · 100 = 85 %."),
            inv("Bereken de invoerquote in procent. Schrijf enkel het getal.", "90",
                "720 / 800 · 100 = 90 %."),
        ],
    ),
    mk(
        "Een land heeft al jaren een groot handelstekort. Wat moet het dan doen?",
        ["Lenen bij het buitenland", "Zijn uitvoerquote verlagen", "Meer importeren", "Zijn bbp verkleinen"],
        0,
        "Wie langdurig meer koopt dan verkoopt, moet het verschil financieren met leningen uit het buitenland.",
    ),
    mk(
        "De producten van een land worden veel duurder dan die van het buitenland. Wat gebeurt er waarschijnlijk met de handelsbalans?",
        ["Het saldo daalt: er komt een handelstekort of het tekort groeit", "Het saldo stijgt: er komt een overschot",
         "Er verandert niets, want de handelsbalans telt enkel hoeveelheden", "Het land wordt lid van een douane-unie"],
        0,
        "Buitenlanders kopen minder, inwoners kopen meer in het buitenland: de export daalt en de import stijgt.",
    ),
    mk(
        "Een leerling zegt: 'Een handelsoverschot is altijd en zonder uitzondering goed.' Wat klopt?",
        ["Fout: andere landen hebben dan een tekort, en de eigen munt kan duur worden",
         "Juist: een land dat meer exporteert dan importeert, wordt altijd rijker en heeft nooit problemen",
         "Fout: een handelsoverschot betekent dat het land moet lenen bij het buitenland",
         "Juist: daarom streven alle landen tegelijk naar een groot handelsoverschot"],
        0,
        "Een overschot is niet altijd goed. En als het ene land een overschot heeft, heeft een ander land een tekort.",
    ),
    tabel(
        "Welk land heeft de meest open economie?",
        [
            ("Land A: invoerquote 20 %", "Minst open"),
            ("Land B: invoerquote 85 %", "Meest open"),
            ("Land C: invoerquote 50 %", "Ertussen"),
        ],
        "Hoe hoger de quote, hoe opener de economie.",
        kolommen=["Minst open", "Ertussen", "Meest open"],
    ),
    mk(
        "Waarom kan een uitvoerquote groter zijn dan 100 %?",
        ["De export bevat ook ingevoerde onderdelen, en die tellen niet mee in het bbp",
         "Het bbp wordt in een andere munt gemeten dan de export, en die munt is minder waard",
         "Een land kan meer goederen exporteren dan het in totaal aan het buitenland verkoopt",
         "De uitvoerquote telt de export van goederen en van diensten twee keer mee in de teller"],
        0,
        "Een land voert onderdelen in, verwerkt ze en voert ze weer uit. In het bbp telt enkel de toegevoegde waarde.",
    ),
    mk(
        "Welk land heeft meestal de hoogste uitvoerquote?",
        ["Een klein land zoals België", "Een groot land zoals de Verenigde Staten",
         "Een land met een handelstekort", "Een land dat geen lid is van een douane-unie"],
        0,
        "Grote landen hebben meestal een lagere quote dan kleine landen. België is een open economie.",
    ),
    tabel(
        "Welke vorm van productie verplaatsen is dit?",
        [
            ("Een Belgisch bedrijf verhuist zijn productie naar Vietnam voor lagere lonen", "Offshoring"),
            ("Een bedrijf brengt zijn productie van China terug naar België", "Reshoring"),
            ("Een bedrijf verhuist zijn productie van China naar Polen", "Nearshoring"),
            ("Een bedrijf laat zijn boekhouding doen door een kantoor", "Outsourcing"),
        ],
        "Uitbesteden: outsourcing. Ver weg: offshoring. Dichterbij: nearshoring. Terug: reshoring.",
        kolommen=["Outsourcing", "Offshoring", "Nearshoring", "Reshoring"],
    ),
    mk(
        "Welke reden past het best bij reshoring?",
        ["Hoge transportkosten en problemen in de toeleveringsketen", "Lagere loonkosten en soepelere milieuregels in een ver land",
         "Het gemeenschappelijk buitentarief van de douane-unie", "Een hogere invoerquote van het eigen land"],
        0,
        "Als transport duur wordt en leveringen haperen, halen bedrijven hun productie terug.",
    ),
    sleep(
        "De vier vrijheden van de Europese interne markt zijn het vrij verkeer van [[goederen]], [[diensten]], [[personen]] en [[kapitaal]].",
        ["munten", "belastingen"],
        "Die vier vrijheden maken van de EU minstens een gemeenschappelijke markt.",
    ),
    keuze(
        "Stijgt de import bij een gelijk bbp, dan [[*stijgt|daalt]] de invoerquote. Daalt de export terwijl de rest gelijk blijft, dan [[*daalt|stijgt]] het saldo van de handelsbalans.",
        "Invoerquote = import / bbp · 100. Saldo = export − import.",
    ),
    inv(
        "Een land heeft een bbp van 450 miljard en een uitvoerquote van 120 %. Hoeveel miljard bedraagt de export? Schrijf enkel het getal.",
        "540",
        "120 % van 450 = 540 miljard.",
    ),
    mk(
        "Een Belgisch bedrijf voert onderdelen in uit Duitsland, maakt er machines van en verkoopt die aan Frankrijk. Wat gebeurt er met de uitvoerquote en de invoerquote van België?",
        ["Beide stijgen", "Enkel de uitvoerquote stijgt", "Enkel de invoerquote stijgt", "Beide dalen"],
        0,
        "De onderdelen zijn import, de machines export. Daarom hebben open economieën als België hoge quotes aan beide kanten.",
    ),
    inv(
        "Het bbp van een land is 250 miljard euro en de import 175 miljard. Bereken de invoerquote in procent. Schrijf enkel het getal.",
        "70",
        "175 / 250 · 100 = 70 %.",
    ),
    tabel(
        "Handelsoverschot of handelstekort?",
        [
            ("Export 300, import 260", "Handelsoverschot"),
            ("Export 420, import 450", "Handelstekort"),
            ("Export 95, import 110", "Handelstekort"),
        ],
        "Saldo = export − import. Positief: overschot. Negatief: tekort.",
        kolommen=["Handelsoverschot", "Handelstekort"],
    ),
    mk(
        "Een bedrijf laat zijn klantendienst doen door een ander bedrijf in Gent. Hoe heet dat?",
        ["Outsourcing", "Offshoring", "Nearshoring", "Reshoring"],
        0,
        "Uitbesteden aan een ander bedrijf, in binnen- of buitenland, is outsourcing. Er wordt niets naar het buitenland verplaatst.",
    ),
    open_(
        "Een Belgisch kledingbedrijf verplaatste twintig jaar geleden zijn productie naar Azië en haalt ze nu terug naar Europa. Benoem beide verplaatsingen en geef voor elk een mogelijke reden.",
        "Eerst offshoring: productie naar een ver land, vooral voor lagere loonkosten. Nu reshoring (of nearshoring, als het naar een land dichtbij gaat): bijvoorbeeld door hoge transportkosten en problemen in de toeleveringsketen.",
    ),
    mk(
        "Een Belgische chocolatier kan dankzij de interne markt zonder invoerrechten in 27 landen verkopen. Welk voordeel van samenwerking speelt hier vooral?",
        ["Een grotere afzetmarkt en schaalvoordelen", "Handelsverlegging naar landen buiten de unie",
         "Een hoger buitentarief voor zijn eigen grondstoffen", "Het recht om de euro te devalueren"],
        0,
        "Wie voor een grotere markt produceert, kan meer maken en profiteert van schaalvoordelen.",
    ),
]
