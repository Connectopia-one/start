# -*- coding: utf-8 -*-
"""Uitdaging Kunstbeschouwing en filosofie 🚀 Boost doorstroom (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Twee kerkgevels en zes vragen om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Kunstbeschouwing en filosofie Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_kunst_filosofie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Kunstbeschouwing en filosofie"
BESTAND = "boost-kunst-filosofie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/kunst-filosofie-boost-uitdaging"
GEVELS = "twee-kerkgevels.svg"
VRAGEN6 = "zes-vragen.svg"

# klikvakken uit maak_prenten_boost_kunst_filosofie.py
GEVEL = {"A": [7.0, 26.0, 36.0, 70.0], "B": [57.0, 11.0, 36.0, 85.0]}
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Kerkgevels (prent)
    klik("Bekijk de twee kerkgevels. Klik op de gevel in gotische stijl.",
         GEVELS, [GEVEL["B"]],
         "Gevel B is hoog en slank, met spitsbogen en grote vensters. Dat zijn kenmerken van de gotiek."),
    klik("Klik op de gevel in romaanse stijl.",
         GEVELS, [GEVEL["A"]],
         "Gevel A is laag en zwaar, met kleine vensters en rondbogen: typisch romaans."),
    met_prent(GEVELS, keuze(
        "Gevel A heeft [[*rondbogen|spitsbogen]] en kleine vensters, omdat de [[*dikke muren|dunne glaswanden]] het gewicht moeten dragen. De stijl van gevel B kwam [[*na|voor]] die van gevel A.",
        "Een romaanse kerk heeft dikke muren en kleine vensters. De gotiek volgde op de romaanse stijl en kon met spitsbogen en steunberen hoger bouwen.")),
    met_prent(GEVELS, mk(
        "Waarom kon de bouwmeester van gevel B hoger bouwen en grotere vensters maken?",
        ["Spitsbogen leiden het gewicht steiler naar beneden.", "Hij gebruikte enkel licht hout in plaats van zware steen.", "De kerk was in het echt veel kleiner dan ze op de prent lijkt.", "Grote vensters maken een muur vanzelf veel sterker en steviger."],
        0,
        "De spitsboog duwt minder zijwaarts dan een rondboog. Samen met steunberen kon de gotiek zo hoger bouwen met meer glas.")),

    # Zes vragen (prent)
    klik("Lees de zes vragen. Klik op de filosofische vraag over de mens.",
         VRAGEN6, [Z[3]],
         "'Wat maakt een mens tot een mens?' is fundamenteel, open en universeel, en je kan ze niet met een meting beslechten. Ze hoort bij de antropologie."),
    klik("Klik op de vraag die bij de ethiek hoort.",
         VRAGEN6, [Z[5]],
         "'Is het ooit goed om te liegen?' gaat over goed handelen. Dat is het domein van de ethiek."),
    met_prent(VRAGEN6, tabel(
        "Welk soort vraag is dit?",
        [
            ("Vraag 1: Hoeveel inwoners telt België vandaag?", "Weetvraag"),
            ("Vraag 2: Vind jij voetbal leuker dan tennis?", "Meningsvraag"),
            ("Vraag 4: In welk jaar schilderde Rubens zijn bekendste werk?", "Weetvraag"),
            ("Vraag 6: Welke pizza bestel jij het liefst?", "Meningsvraag"),
        ],
        "Een weetvraag heeft één juist antwoord dat je kan opzoeken. Een meningsvraag vraagt naar wat iemand persoonlijk vindt.",
        kolommen=["Weetvraag", "Meningsvraag", "Filosofische vraag"])),

    # Cultuur en kunstcriteria
    keuze(
        "Koken hoort bij cultuur in de [[*brede|enge]] betekenis. Een uiting die mensen maakten maar geen kunst is, heet een [[*cultuuruiting|kunstuiting]].",
        "In de brede betekenis is cultuur alles wat mensen maken. Elke kunstuiting is een cultuuruiting, maar niet omgekeerd."),
    sleep(
        "Een urinoir in een museum is vooral kunst door zijn [[originaliteit]]. Een duur schilderij scoort hoog op [[economische waarde]].",
        ["vakmanschap", "esthetische waarde"],
        "Bij een urinoir telt het nieuwe idee, niet het handwerk of de schoonheid. De prijs hoort bij de economische waarde."),

    # Kunstvormen
    tabel(
        "Bij welke kunstvorm hoort dit?",
        [
            ("Een roman", "Literatuur"),
            ("Een bronzen ruiterbeeld op een plein", "Beeldende kunsten"),
            ("Een balletvoorstelling", "Podiumkunsten"),
            ("Een stoel van een ontwerper", "Architectuur en design"),
        ],
        "De vijf kunstvormen zijn architectuur en design, audiovisuele kunsten, beeldende kunsten, literatuur en podiumkunsten.",
        kolommen=["Literatuur", "Beeldende kunsten", "Podiumkunsten", "Architectuur en design"]),

    # Kunstgeschiedenis
    volgorde(
        "Zet deze periodes en stromingen in de juiste volgorde, van oud naar recent.",
        ["prehistorie", "Egyptische kunst", "Griekse kunst", "romaanse kunst", "gotiek", "renaissance"],
        "Van de grotschilderingen via Egypte en de klassieke oudheid naar de middeleeuwen (romaans, dan gotiek) en de renaissance."),
    volgorde(
        "Zet deze stromingen in de juiste volgorde, van oud naar recent.",
        ["barok", "realisme", "impressionisme", "popart"],
        "De barok volgt op de renaissance. Realisme en impressionisme horen bij de moderne tijd, popart bij de hedendaagse tijd."),
    koppel(
        "Koppel de stroming aan haar kenmerk.",
        [
            ["renaissance", "rust, symmetrie en perspectief"],
            ["barok", "beweging, contrast en sterke emotie"],
            ["impressionisme", "de indruk van één ogenblik"],
            ["popart", "beelden uit reclame en strips"],
        ],
        ["piramides als koningsgraf"],
        "Piramides horen bij de Egyptische kunst, niet bij een van deze stromingen."),
    tabel(
        "Klopt dit over de Egyptische kunst?",
        [
            ("Een mens wordt vaak met het hoofd en de benen van opzij getoond.", J),
            ("De piramides waren koningsgraven.", J),
            ("Egyptische kunst is jonger dan de renaissance.", F),
        ],
        "Egyptische kunst volgt vaste regels en is duizenden jaren ouder dan de renaissance."),

    # Functies, inhoud en context
    tabel(
        "Welke functie heeft deze kunstuiting vooral?",
        [
            ("Een standbeeld dat de macht van een koning toont", "Politiek"),
            ("Een strip die een avontuur vertelt", "Narratief"),
            ("Een behangpatroon met bloemetjes", "Decoratief"),
            ("Een spotprent die onrecht aanklaagt", "Maatschappijkritisch"),
        ],
        "Een kunstuiting kan zeven functies hebben: decoratief, economisch, filosofisch, maatschappijkritisch, narratief, ontspannend en politiek.",
        kolommen=["Politiek", "Narratief", "Decoratief", "Maatschappijkritisch"]),
    keuze(
        "Bij de context vraag je onder meer [[*wanneer en waar|hoe duur en hoe groot]] een werk gemaakt werd. Een Afrikaans masker in een Europees museum heeft zijn [[*oorspronkelijke context|vormgeving]] verloren.",
        "De context is de tijd, de plaats en de persoonlijke situatie van de maker. Uit zijn omgeving gehaald, verandert de betekenis van een werk."),

    # Vormgeving
    keuze(
        "Rood, geel en blauw zijn de [[*primaire|secundaire]] kleuren. Een gebouw in één kleur heet [[*monochroom|symmetrisch]]. Bij [[*skeletbouw|een gotische gevel]] draagt een geraamte het gebouw in plaats van de muren.",
        "Door primaire kleuren te mengen krijg je de secundaire. Skeletbouw maakt glazen wanden mogelijk."),
    sorteer(
        "Is dit een middel van vormgeving of een element van de inhoud?",
        ["Middel van vormgeving", "Inhoud"],
        [
            ["kleurgebruik", "Middel van vormgeving"],
            ["het onderwerp", "Inhoud"],
            ["compositie", "Middel van vormgeving"],
            ["de functie", "Inhoud"],
            ["licht en schaduw", "Middel van vormgeving"],
        ],
        "Middelen van vormgeving gaan over hoe het werk gemaakt is. Onderwerp en functie gaan over wat het toont en waarvoor het dient."),

    # Filosofie: kennis en oorsprong
    sorteer(
        "Welk soort kennis is dit?",
        ["Dagdagelijkse kennis", "Wetenschappelijke kennis"],
        [
            ["Mijn oma zegt dat kamillethee helpt tegen buikpijn.", "Dagdagelijkse kennis"],
            ["Een studie met 2 000 deelnemers meet het effect van slaap op leren.", "Wetenschappelijke kennis"],
            ["Iedereen weet dat je niet moet zwemmen na het eten.", "Dagdagelijkse kennis"],
            ["Een bioloog toetst met een proef hoe snel bacteriën groeien.", "Wetenschappelijke kennis"],
        ],
        "Wetenschappelijke kennis komt uit methodisch onderzoek. Dagdagelijkse kennis neem je over zonder ze te controleren."),
    koppel(
        "Koppel de natuurfilosoof aan zijn idee.",
        [
            ["Thales", "water is de oerstof"],
            ["Heraclitus", "alles stroomt"],
            ["Parmenides", "verandering is schijn"],
            ["Pythagoras", "alles is getal"],
        ],
        ["de ziel is de vorm van het lichaam"],
        "Dat de ziel de vorm van het lichaam is, zei Aristoteles, die na de natuurfilosofen leefde."),
    keuze(
        "Een mythe verklaart de wereld met [[*goden|de natuur zelf]]. De eerste filosofen zochten een verklaring [[*in de natuur|bij de goden]].",
        "De stap van mythe naar filosofie is de stap van bovennatuurlijke verhalen naar redeneringen over de natuur."),

    # Filosofische vraag en domeinen
    tabel(
        "Welk kenmerk van een filosofische vraag wordt hier beschreven?",
        [
            ("Ze geldt voor iedereen, overal.", "Universeel"),
            ("Er is geen definitief eindantwoord.", "Open"),
            ("Ze gaat over de grond van de dingen.", "Fundamenteel"),
        ],
        "Een filosofische vraag is fundamenteel, meerduidig, niet-empirisch op te lossen, open en universeel.",
        kolommen=["Universeel", "Open", "Fundamenteel"]),
    tabel(
        "Bij welk filosofisch domein hoort deze vraag?",
        [
            ("Wat maakt een kunstwerk mooi?", "Esthetica"),
            ("Bestaat er een leven na de dood?", "Metafysica"),
            ("Mag je een dier opofferen voor een medicijn?", "Ethiek"),
            ("Kunnen we iets met zekerheid weten?", "Kennisleer"),
        ],
        "Esthetica gaat over schoonheid, metafysica over wat er bestaat voorbij het waarneembare, ethiek over goed handelen en kennisleer over waarheid en kennis.",
        kolommen=["Esthetica", "Metafysica", "Ethiek", "Kennisleer"]),

    # Vaardigheden
    volgorde(
        "Zet de drie stappen van de AUB-methode in de juiste volgorde.",
        ["argument", "uitleg", "bijvoorbeeld"],
        "Eerst noem je je argument, dan leg je het uit en tot slot maak je het concreet met een voorbeeld."),
    keuze(
        "Iemand zegt: 'Dat is gewoon zo.' Er ontbreekt een [[*argument met uitleg|weetvraag]]. Bij stap 3 van het stappenplan voor een filosofische tekst [[*reflecteer je|lees je globaal]].",
        "Een standpunt zonder argument overtuigt niet. Het stappenplan is: globaal lezen, grondig lezen, reflecteren."),

    # Lichaam en geest, mens en dier
    koppel(
        "Koppel de filosoof aan zijn visie op lichaam en geest.",
        [
            ["Plato", "de ziel is onsterfelijk en zit gevangen in het lichaam"],
            ["Aristoteles", "de ziel is de vorm van het lichaam"],
            ["Descartes", "ik denk, dus ik ben: de geest staat los van het lichaam"],
        ],
        ["alles stroomt"],
        "'Alles stroomt' is van Heraclitus, een natuurfilosoof. Het hoort niet bij het debat over lichaam en geest."),
    tabel(
        "Past deze uitspraak bij het monisme of bij het dualisme?",
        [
            ("Zonder lichaam kan er geen geest bestaan.", "Monisme"),
            ("Mijn ziel leeft verder na de dood.", "Dualisme"),
            ("Denken is niets anders dan hersenactiviteit.", "Monisme"),
        ],
        "Het monisme ziet lichaam en geest als één. Het dualisme ziet twee aparte delen die los van elkaar kunnen bestaan.",
        kolommen=["Monisme", "Dualisme"]),
    mk("Iemand zegt: 'Een dier voelt niets, het is een soort machine.' Bij wie sluit die persoon aan?",
       ["Descartes", "Peter Singer", "Darwin", "Pythagoras"],
       0,
       "Descartes zag dieren als machines zonder geest. Singer en Darwin verkleinen net de kloof tussen mens en dier."),

    # Ethiek
    sorteer(
        "Plichtethiek of gevolgenethiek?",
        ["Plichtethiek", "Gevolgenethiek"],
        [
            ["Liegen blijft fout, ook als het iemand beschermt.", "Plichtethiek"],
            ["Een daad is goed als ze het meeste geluk oplevert.", "Gevolgenethiek"],
            ["Je mag een mens nooit louter als middel gebruiken.", "Plichtethiek"],
            ["We moeten dierenleed meetellen omdat dieren ook lijden.", "Gevolgenethiek"],
        ],
        "De plichtethiek (Kant) kijkt naar de regel zelf. De gevolgenethiek of het utilisme (Mill, Singer) kijkt naar het resultaat."),
    koppel(
        "Koppel de filosoof aan de ethische stroming.",
        [
            ["Immanuel Kant", "plichtethiek"],
            ["John Stuart Mill", "gevolgenethiek"],
        ],
        ["natuurfilosofie"],
        "Kant is de bekendste plichtethicus. Mill verdedigde het utilisme, een vorm van gevolgenethiek."),
    keuze(
        "Eerlijkheid is een [[*waarde|norm]]. 'Je mag niet spieken' is een [[*norm|waarde]]. Een keuze waarbij elke optie iets waardevols schendt, is een [[*dilemma|weetvraag]].",
        "Een waarde is een doel dat je belangrijk vindt, een norm is de concrete regel die eruit volgt."),
    mk("Iemand zegt: 'Wat goed is, verschilt van cultuur tot cultuur.' Welke visie verdedigt die persoon?",
       ["het moreel relativisme", "de plichtethiek van Kant", "het dualisme van Descartes", "de natuurfilosofie van Thales"],
       0,
       "Het moreel relativisme zegt dat goed en kwaad relatief zijn. Een bezwaar is dat je dan geen enkele daad nog echt kan veroordelen."),
    keuze(
        "Verantwoordelijkheid veronderstelt [[*vrijheid|gehoorzaamheid]]. Een wet die roken in cafés verbiedt, laat [[*gezondheid en vrijheid|kunst en schoonheid]] botsen.",
        "Je kan maar verantwoordelijk zijn als je echt kon kiezen. Bij een rookverbod botst de gezondheid van anderen met de vrijheid van de roker."),
    tabel(
        "Hoort dit argument over dierenproeven bij de plichtethiek of de gevolgenethiek?",
        [
            ("Dierenproeven redden later veel mensenlevens.", "Gevolgenethiek"),
            ("Een dier mag je nooit gebruiken als louter middel.", "Plichtethiek"),
            ("Het leed van de dieren weegt zwaarder dan de winst.", "Gevolgenethiek"),
        ],
        "Wie gevolgen afweegt, redeneert als gevolgenethicus. Wie een onvoorwaardelijke regel inroept, redeneert als plichtethicus.",
        kolommen=["Plichtethiek", "Gevolgenethiek"]),
    mk("Wat is paternalisme in het debat over risicogedrag bij jongeren?",
       ["Anderen beslissen voor je eigen bestwil.", "Jongeren beslissen alles volledig zelf, altijd.", "Ouders mogen hun kinderen nooit iets verbieden.", "De overheid houdt zich overal helemaal buiten."],
       0,
       "Bij paternalisme beperkt iemand je keuze om je te beschermen, zoals een leeftijdsgrens voor alcohol."),

    mk("Waarom ontstond de westerse filosofie juist in Griekse havensteden zoals Milete?",
       ["Daar kwamen mensen en ideeën uit veel culturen samen.", "Daar waren de goden het sterkst aanwezig in de tempels.", "Daar woonden de rijkste koningen van de toenmalige wereld.", "Daar verboden de priesters alle oude mythes en verhalen."],
       0,
       "In een havenstad ontmoetten handelaars elkaar met verschillende verhalen. Dat zette mensen aan het denken over wat echt waar is."),
    mk("Filosofie heet soms 'de moeder van de wetenschappen'. Wat bedoelt men daarmee?",
       ["Veel wetenschappen groeiden uit de filosofie.", "Filosofen deden als eersten proeven in een labo.", "Filosofie geeft op elke vraag één vast antwoord.", "Wetenschappers moeten eerst filosofie studeren."],
       0,
       "Vragen over de natuur, de mens en de samenleving begonnen in de filosofie. Later werden het aparte wetenschappen."),
    tabel(
        "Welke kunst hoort bij welke samenleving of periode?",
        [
            ("Patronen en kalligrafie in plaats van mensfiguren", "Arabische kunst"),
            ("Tempels met zuilen en beelden van ideale lichamen", "Griekse kunst"),
            ("Dieren geschilderd op de wand van een grot", "Prehistorische kunst"),
        ],
        "Arabische kunst werkt vaak met patronen en kalligrafie. De Griekse kunst zocht de ideale schoonheid. Grotschilderingen horen bij de prehistorie.",
        kolommen=["Arabische kunst", "Griekse kunst", "Prehistorische kunst"]),
    keuze(
        "Gelijke kansen voor iedereen, los van geslacht, heet [[*gendergelijkheid|genderidentiteit]]. Wie zelf over zijn lichaam beslist, beroept zich op de waarde [[*autonomie|gehoorzaamheid]].",
        "Gendergelijkheid gaat over gelijke kansen. Autonomie betekent zelfbeschikking."),
    # Schrijfopdracht
    open_("Moet de overheid energiedrankjes verbieden voor jongeren onder 16? Geef je standpunt en bouw één argument op met de AUB-methode.",
          "Ik vind dat de overheid energiedrankjes mag verbieden onder 16 jaar. Argument: de drankjes schaden de gezondheid van jongeren. Uitleg: ze bevatten veel cafeïne en suiker, en een jong lichaam reageert daar sterker op met hartkloppingen en slaapproblemen. Bijvoorbeeld: een leerling die 's avonds twee blikjes drinkt, slaapt slecht en kan zich de volgende dag niet concentreren in de klas.",
          "Een goed antwoord geeft een duidelijk standpunt en een volledig AUB-argument: een argument, een uitleg en een concreet voorbeeld."),
]
