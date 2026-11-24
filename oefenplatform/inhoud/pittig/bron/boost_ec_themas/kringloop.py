"""De economische kringloop — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_kringloop, met een zelfgetekend kringloopschema om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, DONKER

KR = Prent("kringloop-schema", "Kringloopschema", "gezinnen links, bedrijven rechts, overheid onderaan; zes pijlen met een letter")
KR.rect(60, 230, 220, 110, "#e8f0dd", DONKER, 14)
KR.tekst(170, 293, "GEZINNEN", 26, vet=True)
KR.rect(720, 230, 220, 110, "#f6e7d4", DONKER, 14)
KR.tekst(830, 293, "BEDRIJVEN", 26, vet=True)
KR.rect(390, 500, 220, 100, "#e3ebf3", DONKER, 14)
KR.tekst(500, 558, "OVERHEID", 26, vet=True)
# boven: twee pijlen tussen gezinnen en bedrijven
KR.pijl(280, 120, 720, 120, BLAUW)            # A: gezin -> bedrijf (bovenste)
KR.pijl(720, 190, 280, 190, ORANJE)           # B: bedrijf -> gezin
KR.pijl(280, 380, 720, 380, ORANJE)           # C: gezin -> bedrijf (onder)
KR.pijl(720, 440, 280, 440, BLAUW)            # D: bedrijf -> gezin (onder)
KR.pijl(170, 340, 390, 540, GROEN)            # E: gezin -> overheid
KR.pijl(610, 560, 830, 340, GROEN)            # F: overheid -> bedrijf
KR.lijn(150, 120, 280, 120, BLAUW, 3); KR.lijn(150, 120, 150, 230, BLAUW, 3)
KR.lijn(720, 120, 850, 120, BLAUW, 3)
KR.lijn(720, 190, 790, 190, ORANJE, 3); KR.lijn(790, 190, 790, 230, ORANJE, 3)
KR.lijn(210, 190, 280, 190, ORANJE, 3); KR.lijn(210, 190, 210, 230, ORANJE, 3)
KR.lijn(850, 120, 850, 230, BLAUW, 3)
KR.tekst(20, 560, "blauw = geld", 17, "start", BLAUW, True)
KR.tekst(20, 585, "oranje = goederen, diensten,", 17, "start", ORANJE, True)
KR.tekst(20, 605, "productiefactoren", 17, "start", ORANJE, True)
KR.tekst(20, 630, "groen = met de overheid", 17, "start", GROEN, True)
POS = {"A": (500, 95), "B": (500, 165), "C": (500, 355), "D": (500, 470), "E": (255, 470), "F": (745, 470)}
for t, (x, y) in POS.items():
    KR.letter(x, y, t)
U = "kringloop-schema.svg"
Z = {t: Prent.rond(x, y, 36) for t, (x, y) in POS.items()}

VRAGEN = [
    klik("In het schema zijn de blauwe pijlen geld. Klik op de letter bij de geldstroom die de gezinnen betalen voor wat ze bij de bedrijven kopen.", U, [Z["A"]],
         "Pijl A loopt van de gezinnen naar de bedrijven en is blauw: de betaling voor goederen en diensten."),
    klik("Klik op de letter bij de pijl die de productiefactoren voorstelt, zoals arbeid.", U, [Z["C"]],
         "Pijl C is oranje en loopt van de gezinnen naar de bedrijven: de gezinnen leveren arbeid en kapitaal."),
    klik("Klik op de letter bij de pijl met de lonen, de intrest en de huur.", U, [Z["D"]],
         "Pijl D is blauw en loopt van de bedrijven naar de gezinnen: de vergoedingen voor de productiefactoren."),
    klik("Klik op de letter bij de pijl die bijvoorbeeld de personenbelasting kan voorstellen.", U, [Z["E"]],
         "Pijl E loopt van de gezinnen naar de overheid."),
    klik("De overheid koopt computers voor scholen. Klik op de letter bij de pijl met die betaling.", U, [Z["F"]],
         "Pijl F loopt van de overheid naar de bedrijven."),
    koppel("Welke vergoeding hoort bij welke productiefactor?",
           [("arbeid", "loon"), ("kapitaal", "intrest"), ("natuur", "pacht of huur"), ("ondernemerschap", "winst")],
           ["subsidie"], "Elke productiefactor krijgt zijn eigen vergoeding."),
    sorteer("Hoort dit bij de reële stroom of bij de geldstroom?", ["reële stroom", "geldstroom"],
            [("een brood dat een gezin koopt", "reële stroom"), ("het loon van een verpleegkundige", "geldstroom"), ("de arbeid van een bouwvakker", "reële stroom"), ("de btw op een fiets", "geldstroom"), ("een knipbeurt bij de kapper", "reële stroom"), ("een kinderbijslag", "geldstroom")],
            "De reële stroom is wat er echt geleverd wordt; de geldstroom is de betaling."),
    casus("Lees de situatie.\n\nNora werkt als boekhouder bij een fietsenfabriek en verdient 2 800 euro bruto per maand. Ze betaalt 750 euro belastingen en sociale bijdragen. Van wat overblijft, zet ze 250 euro op haar spaarrekening. Met de rest koopt ze onder meer een nieuwe fiets bij een Duitse webwinkel.", [
        inv("Hoeveel euro besteedt Nora per maand? Schrijf enkel het getal.", ["1800", "1 800", "1.800"],
            "2 800 − 750 = 2 050 beschikbaar inkomen; 2 050 − 250 = 1 800 euro."),
        tabel("Is dit een lek of een injectie voor de Belgische kringloop?",
              [("de belastingen van Nora", "lek"), ("het spaargeld van Nora", "lek"), ("de fiets uit Duitsland", "lek"), ("de fietsen die haar fabriek naar Nederland uitvoert", "injectie")],
              "Sparen, belastingen en invoer zijn lekken; uitvoer is een injectie.",
              kolommen=["lek", "injectie"]),
        keuze("Nora levert aan haar werkgever de productiefactor [[*arbeid|kapitaal|natuur]].",
              "Ze werkt: arbeid, vergoed met loon."),
    ]),
    tabel("Welke actoren staan hier tegenover elkaar?",
          [("Een slager koopt vlees bij een groothandel.", "twee bedrijven"), ("Een student krijgt een studiebeurs.", "overheid en gezin"), ("Een gezin koopt een auto bij de garage.", "gezin en bedrijf"), ("Een bedrijf betaalt vennootschapsbelasting.", "bedrijf en overheid")],
          "Kijk wie levert en wie betaalt.",
          kolommen=["twee bedrijven", "gezin en bedrijf", "overheid en gezin", "bedrijf en overheid"]),
    mk("Een bedrijf koopt een nieuwe vrachtwagen om mee te leveren. Hoe heet die uitgave?",
       ["een investering", "een consumptie van het gezin", "een belasting aan de overheid", "een uitkering aan de werknemers"], 0,
       "Een kapitaalgoed kopen om mee te produceren is investeren."),
    tabel("Klopt dit over de kringloop?",
          [("De goederenstroom en de geldstroom lopen in tegengestelde richting.", J), ("Een eenmanszaak zonder personeel hoort bij de gezinnen.", F), ("Een uitkering is een geldstroom zonder tegenprestatie.", J), ("Invoer brengt geld in de binnenlandse kringloop.", F)],
          "Een eenmanszaak produceert om te verkopen: bedrijf. Invoer is een lek."),
    sorteer("Lek of injectie?", ["lek", "injectie"],
            [("sparen", "lek"), ("investeringen", "injectie"), ("belastingen", "lek"), ("overheidsuitgaven", "injectie"), ("invoer", "lek"), ("uitvoer", "injectie")],
            "Lekken halen bestedingen uit de kringloop, injecties brengen ze erin."),
    keuze("Als de gezinnen minder uitgeven, dalen de [[*omzet en de lonen bij de bedrijven|belastingen die de gezinnen betalen aan de banken|uitgaven van het buitenland]].",
          "Het kettingeffect: de uitgave van de ene is het inkomen van de andere."),
    inv("Een gezin heeft een beschikbaar inkomen van 3 200 euro en besteedt 2 900 euro. Hoeveel spaart het? Schrijf enkel het getal.", ["300"],
        "Wat niet besteed wordt, is sparen: 3 200 − 2 900 = 300."),
    volgorde("Een gezin koopt brood. Zet de geldstroom van de kringloop in een logische volgorde.",
             ["het gezin betaalt de bakker", "de bakker betaalt zijn bakkersgast een loon", "de bakkersgast betaalt belastingen", "de overheid betaalt een leraar"],
             "Het geld gaat telkens van eigenaar: de uitgave van de ene is het inkomen van de andere."),
    mk("Waarom laat het eenvoudige kringloopschema het buitenland weg?",
       ["Om het model overzichtelijk te houden.", "Omdat België geen handel drijft met het buitenland.", "Omdat het buitenland geen geldstromen veroorzaakt.", "Omdat de overheid de handel met het buitenland verbiedt."], 0,
       "Een model laat bewust details weg."),
    sleep("Een Belgisch bedrijf voert chocolade uit naar Japan. De chocolade gaat naar [[Japan]] en het geld komt naar [[België]]. Voor België is dat een [[injectie]].",
          ["lek", "Duitsland"], "Bij uitvoer verlaten de goederen het land en komt de betaling binnen."),
    tabel("Is dit een geldstroom van de overheid naar de gezinnen?",
          [("het loon van een ambtenaar", J), ("een werkloosheidsuitkering", J), ("de btw op een tv", F), ("het pensioen van een gepensioneerde leraar", J)],
          "De btw gaat de andere kant op: naar de overheid."),
    keuze("Het geld dat banken uitlenen aan bedrijven die investeren, komt vooral van [[*het spaargeld van de gezinnen|de belastingen van de overheid|de invoer uit het buitenland]].",
          "Via de banken keert spaargeld als investering terug in de kringloop."),
    inv("Hoe noem je de productiefactor waarvoor een ondernemer winst krijgt? Schrijf één woord.", ["ondernemerschap", "ondernemen", "organisatie"],
        "Ondernemerschap: de ondernemer neemt het risico en krijgt de winst."),
    mk("Een gemeente betaalt een aannemer om een fietspad aan te leggen. Wat klopt?",
       ["Het geld gaat van de gemeente naar de aannemer.", "Het fietspad gaat van de gemeente naar de aannemer.", "Het geld gaat van de aannemer naar de gemeente.", "Er lopen hier enkel geldstromen tussen gezinnen."], 0,
       "De overheid is de koper; de aannemer levert het werk."),
    sorteer("Wat doet deze actor in de kringloop?", ["gezinnen", "bedrijven", "overheid"],
            [("levert arbeid", "gezinnen"), ("int belastingen", "overheid"), ("produceert om te verkopen", "bedrijven"), ("betaalt uitkeringen", "overheid"), ("koopt consumptiegoederen", "gezinnen"), ("verkoopt goederen aan de gezinnen", "bedrijven")],
            "Elke actor heeft zijn eigen rol."),
    keuze("Een kapper knipt je haar. Die knipbeurt hoort bij de [[*reële stroom|geldstroom|lekken]].",
          "Een dienst wordt echt geleverd: reële stroom."),
    klik("Klik op de letter bij de pijl met de goederen en diensten die de gezinnen krijgen.", U, [Z["B"]],
         "Pijl B is oranje en loopt van de bedrijven naar de gezinnen."),
    keuze("Economie bestudeert vooral hoe mensen [[*keuzes maken met schaarse middelen|zoveel mogelijk geld verdienen|de natuur beschermen]].",
          "Produceren, verdelen en verbruiken: altijd kiezen, want middelen zijn schaars."),
    tabel("Hoort deze actor in het eenvoudige binnenlandse schema?",
          [("de gezinnen", J), ("de overheid", J), ("het buitenland", F), ("de bedrijven", J)],
          "Het eenvoudige schema blijft binnen de grenzen; het buitenland komt er pas bij met in- en uitvoer."),
    inv("Een bedrijf heeft 40 000 euro omzet van gezinnen, betaalt 25 000 euro lonen en 5 000 euro belastingen. Hoeveel euro blijft er nog over voor andere kosten en winst? Schrijf enkel het getal.", ["10000", "10 000", "10.000"],
        "40 000 − 25 000 − 5 000 = 10 000 euro."),
    open_("Leg in één of twee zinnen uit waarom sparen een lek is, maar het geld niet voor altijd uit de kringloop verdwijnt.",
          "Gespaard geld wordt niet besteed bij de bedrijven, maar de bank leent het uit aan bedrijven die investeren, zodat het als injectie terugkomt.",
          "Sparen is een lek; via de bank kan het terugkeren als investering."),
]
