# -*- coding: utf-8 -*-
"""De normale verdeling en standaardiseren.

De vakfiche noemt de normale verdeling op drie plaatsen: bij de
hypothesetoetsen, bij de betrouwbaarheidsintervallen en bij het werken met
grote datasets ("Je beoordeelt op basis van een grafische voorstelling of
het model van de normale verdeling geschikt is voor de gegeven data").
Zonder dit thema hangen die drie in de lucht, daarom staat het hier apart.

De bijlage geeft de notaties: X ~ N(mu, sigma) voor een normale verdeling,
Z ~ N(0,1) voor de standaardnormale verdeling, en standaardiseren als
Z = (X − mu) / sigma.

De vuistregel van achtenzestig, vijfennegentig en negenennegentig komma zeven
procent staat níét in het formularium van deze fiche. Ze staat wel in elk
handboek en ze is nodig om te beoordelen of de normale verdeling past, dus ze
staat hier als vuistregel en nooit als een formule die je moet kennen.

Deel 1 is de vorm van de normale verdeling en haar eigenschappen.
Deel 2 is standaardiseren en kansen aflezen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de grafiek van een normale verdeling eruit?",
        opties=[
            "een symmetrische klokvorm met één top",
            "een rechte lijn die stijgt van nul naar één",
            "een trap die bij elke waarde een stap omhoog doet",
            "een kromme die naar links scheef hangt",
        ],
        antwoord=0,
        uitleg="Daarom spreekt men ook van een klokcurve of een gausscurve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de notatie X ~ N(mu, sigma)?",
        opties=[
            "X is normaal verdeeld met gemiddelde mu en standaardafwijking sigma",
            "X ligt tussen mu en sigma",
            "X is het gemiddelde van mu metingen",
            "X is normaal verdeeld met variantie mu en gemiddelde sigma",
        ],
        antwoord=0,
        uitleg="Zo staat ze in de bijlage Begrippen en notaties: eerst het gemiddelde, dan de standaardafwijking.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een normale verdeling vallen het gemiddelde, de mediaan en de modus samen.",
        antwoord=True,
        uitleg="Door de symmetrie liggen ze alle drie onder de top. Bij scheve data gebeurt dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Is de normale verdeling discreet of continu?",
        opties=["continu", "discreet", "allebei", "geen van de twee"],
        antwoord=0,
        uitleg="Ze beschrijft meetwaarden zoals lengte of gewicht, die elke waarde in een interval kunnen aannemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de oppervlakte onder de hele curve van een normale verdeling?",
        opties=["één", "nul", "mu", "sigma"],
        antwoord=0,
        uitleg="Die oppervlakte is de totale kans, en die is altijd één. Een kans is bij een continue verdeling een oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de curve als sigma groter wordt en mu gelijk blijft?",
        opties=[
            "de curve wordt breder en platter",
            "de curve wordt smaller en hoger",
            "de curve schuift naar rechts",
            "de curve wordt scheef naar één kant",
        ],
        antwoord=0,
        uitleg="Meer spreiding betekent meer oppervlakte in de staarten, dus de top moet lager liggen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is P(X < mu) bij een normale verdeling? Geef het getal als decimaal.",
        antwoord=["0,5", "0.5"],
        uitleg="Door de symmetrie ligt precies de helft van de oppervlakte links van het gemiddelde.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een normale verdeling schuift de curve naar rechts als mu groter wordt.",
        antwoord=True,
        uitleg="mu bepaalt waar de top ligt, sigma bepaalt hoe breed de curve is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel procent van de waarden ligt volgens de vuistregel tussen mu min sigma en mu plus sigma?",
        opties=[
            "ongeveer achtenzestig procent",
            "ongeveer vijftig procent",
            "ongeveer vijfennegentig procent",
            "ongeveer vijfentwintig procent",
        ],
        antwoord=0,
        uitleg="Twee standaardafwijkingen geven ongeveer vijfennegentig procent, drie ongeveer negenennegentig komma zeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke data zijn het meest geschikt voor een model met een normale verdeling?",
        opties=[
            "de lengte van duizend volwassen mannen",
            "het aantal kinderen per gezin in een wijk",
            "het inkomen van alle inwoners van een land",
            "het aantal dagen regen per maand",
        ],
        antwoord=0,
        uitleg="Lengte is continu en ligt symmetrisch rond een gemiddelde. Inkomen hangt scheef naar rechts.",
    ),
    dict(
        type="waarofniet",
        vraag="Een histogram met een lange staart naar rechts past goed bij een normale verdeling.",
        antwoord=False,
        uitleg="Dan zijn de data scheef en is het model niet geschikt. Een normale verdeling is symmetrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet beoordelen of de normale verdeling past bij een dataset. Wat doe je volgens de fiche?",
        opties=[
            "je maakt met ICT een grafische voorstelling en bekijkt de vorm",
            "je berekent het gemiddelde en kijkt of het een geheel getal is",
            "je neemt een tweede steekproef en vergelijkt de twee gemiddelden",
            "je deelt de standaardafwijking door het gemiddelde",
        ],
        antwoord=0,
        uitleg="De fiche vraagt letterlijk: je beoordeelt op basis van een grafische voorstelling. Een histogram is daar het geschiktst voor.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk ander woord wordt de klokcurve van de normale verdeling ook aangeduid? Eén woord.",
        antwoord=["gausscurve", "gauss", "klokcurve"],
        uitleg="Naar de wiskundige Gauss. In het Nederlands spreekt men ook van een klokcurve.",
    ),
    dict(
        type="waarofniet",
        vraag="De curve van een normale verdeling raakt de horizontale as aan de uiteinden.",
        antwoord=False,
        uitleg="Ze komt er steeds dichter bij maar raakt ze nooit. Daarom is elke waarde in principe mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een normale verdeling met mu gelijk aan honderd en sigma gelijk aan vijftien, tussen welke waarden ligt ongeveer vijfennegentig procent?",
        opties=["zeventig en honderddertig", "vijfentachtig en honderdvijftien", "vijfenvijftig en honderdvijfenveertig", "negentig en honderdtien"],
        antwoord=0,
        uitleg="Twee sigma aan elke kant: honderd min dertig en honderd plus dertig. Dat is de vuistregel voor vijfennegentig procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is P(X = 180) bij een normale verdeling gelijk aan nul?",
        opties=[
            "omdat één exacte waarde geen oppervlakte onder de curve heeft",
            "omdat honderdtachtig te ver van het gemiddelde ligt",
            "omdat de normale verdeling enkel hele getallen toelaat",
            "omdat een kans bij een continue verdeling nooit berekend kan worden",
        ],
        antwoord=0,
        uitleg="Bij een continue verdeling werk je altijd met een interval, bijvoorbeeld tussen 179,5 en 180,5 centimeter.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee normale verdelingen met hetzelfde gemiddelde maar een andere standaardafwijking hebben dezelfde top.",
        antwoord=False,
        uitleg="De top ligt wel boven hetzelfde gemiddelde, maar ze is niet even hoog. De bredere curve is platter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een histogram van de examenscores heeft twee duidelijke toppen. Wat besluit je?",
        opties=[
            "de normale verdeling is geen geschikt model voor deze data",
            "de normale verdeling past, want twee toppen betekent twee gemiddelden",
            "je moet het gemiddelde van de twee toppen nemen als mu",
            "er is een rekenfout in het histogram gemaakt",
        ],
        antwoord=0,
        uitleg="Een normale verdeling heeft juist één top. Twee toppen wijzen vaak op twee groepen in de data.",
    ),
    dict(
        type="invultekst",
        vraag="Welke letter gebruikt de bijlage voor een standaardnormaal verdeelde kansvariabele? Eén letter.",
        antwoord=["z", "Z"],
        uitleg="Z ~ N(0,1): gemiddelde nul en standaardafwijking één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt dat het aantal zessen bij tien worpen normaal verdeeld is. Wat klopt daar niet?",
        opties=[
            "dat aantal is discreet, dus het is binomiaal en niet normaal verdeeld",
            "tien worpen is te weinig om van een verdeling te spreken",
            "een dobbelsteen is niet eerlijk genoeg voor een normale verdeling",
            "dat klopt wel, elk aantal successen is normaal verdeeld",
        ],
        antwoord=0,
        uitleg="Een aantal tel je, dus het is discreet. De normale verdeling hoort bij continue grootheden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de standaardnormale verdeling?",
        opties=[
            "de normale verdeling met gemiddelde nul en standaardafwijking één",
            "de normale verdeling met gemiddelde één en standaardafwijking nul",
            "de normale verdeling die bij elke dataset past",
            "de normale verdeling met de kleinste mogelijke spreiding",
        ],
        antwoord=0,
        uitleg="De bijlage noteert ze als Z ~ N(0,1).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de gestandaardiseerde waarde Z?",
        opties=[
            "X min mu, gedeeld door sigma",
            "X min sigma, gedeeld door mu",
            "X plus mu, gedeeld door sigma",
            "mu min X, maal sigma",
        ],
        antwoord=0,
        uitleg="Zo staat ze in de bijlage: Z = (X − mu) / sigma. Dat getal volgt dan N(0,1).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een z-waarde van plus twee?",
        opties=[
            "de waarde ligt twee standaardafwijkingen boven het gemiddelde",
            "de waarde is twee keer zo groot als het gemiddelde",
            "de kans op die waarde is twee procent",
            "de waarde ligt twee eenheden boven het gemiddelde",
        ],
        antwoord=0,
        uitleg="Een z-waarde drukt een afstand uit in standaardafwijkingen, niet in de eenheid van de meting.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve z-waarde betekent dat de waarde onder het gemiddelde ligt.",
        antwoord=True,
        uitleg="Het teken van X min mu bepaalt het teken van z.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij mu gelijk aan zeventig en sigma gelijk aan vijf, welke z-waarde hoort bij X gelijk aan tachtig?",
        opties=["twee", "tien", "vijf", "nul komma vijf"],
        antwoord=0,
        uitleg="Tachtig min zeventig is tien, gedeeld door vijf is twee.",
    ),
    dict(
        type="invultekst",
        vraag="Bij mu gelijk aan vijftig en sigma gelijk aan vier, welke z-waarde hoort bij X gelijk aan tweeënveertig? Geef het getal in cijfers, met een teken.",
        antwoord=["-2", "−2"],
        uitleg="Tweeënveertig min vijftig is min acht, gedeeld door vier is min twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom standaardiseert men een normale verdeling?",
        opties=[
            "om waarden uit verschillende verdelingen met elkaar te kunnen vergelijken",
            "om de verdeling symmetrisch te maken",
            "om de standaardafwijking kleiner te maken",
            "om van een continue verdeling een discrete te maken",
        ],
        antwoord=0,
        uitleg="Een score van zeventig op een toets zegt niets zonder mu en sigma. De z-waarde maakt twee toetsen vergelijkbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een z-waarde van nul betekent dat de kans op die waarde nul is.",
        antwoord=False,
        uitleg="z gelijk aan nul betekent juist dat de waarde gelijk is aan het gemiddelde, daar waar de curve haar top heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Ann haalt zeventig op een toets met mu zestig en sigma vijf. Bo haalt tachtig op een toets met mu zeventig en sigma tien. Wie deed relatief beter?",
        opties=[
            "Ann, want haar z-waarde is twee en die van Bo is één",
            "Bo, want tachtig is hoger dan zeventig",
            "ze deden allebei even goed, want ze zitten tien boven het gemiddelde",
            "dat kan je niet vergelijken zonder het aantal leerlingen te kennen",
        ],
        antwoord=0,
        uitleg="Ann staat twee standaardafwijkingen boven het gemiddelde, Bo maar één. Daarvoor dient standaardiseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je op het examen een kans bij een normale verdeling?",
        opties=[
            "met een rekenapp, waarbij je mu, sigma en de grenzen invult",
            "door de formule van de klokcurve met de hand te integreren",
            "door de vuistregel toe te passen, dat is de enige manier",
            "door het aantal waarden onder de grens te tellen",
        ],
        antwoord=0,
        uitleg="De fiche vraagt het gebruik van de rekenapps. Je toont wel je werkwijze en je redenering.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een normale verdeling is P(X > mu plus sigma) gelijk aan P(X < mu min sigma).",
        antwoord=True,
        uitleg="De curve is symmetrisch rond mu, dus de twee staarten hebben dezelfde oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="De lengte van Belgische mannen volgt N(178; 7). Welke kans is het grootst?",
        opties=[
            "de kans op een lengte tussen 171 en 185",
            "de kans op een lengte boven 192",
            "de kans op een lengte onder 164",
            "de kans op een lengte boven 199",
        ],
        antwoord=0,
        uitleg="Dat is het interval van één sigma aan elke kant, dus ongeveer achtenzestig procent. De andere zijn staarten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een z-waarde van drie komma vijf wijst meestal op wat?",
        opties=[
            "een uitzonderlijke waarde, mogelijk een uitschieter",
            "een heel gewone waarde dicht bij het gemiddelde",
            "een rekenfout, want z kan niet groter zijn dan drie",
            "een verdeling die niet normaal is",
        ],
        antwoord=0,
        uitleg="Buiten drie sigma ligt minder dan nul komma drie procent van de waarden. Zo'n waarde verdient aandacht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is P(Z < 0) bij de standaardnormale verdeling? Geef het getal als decimaal.",
        antwoord=["0,5", "0.5"],
        uitleg="Nul is het gemiddelde van Z, dus de helft van de oppervlakte ligt links.",
    ),
    dict(
        type="waarofniet",
        vraag="Na standaardiseren is de vorm van de verdeling veranderd van klokvormig naar symmetrisch rechthoekig.",
        antwoord=False,
        uitleg="De vorm blijft dezelfde klok. Enkel de schaal op de as verandert: mu wordt nul en sigma wordt één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabrikant wil dat slechts twee komma vijf procent van de pakken onder het gewicht valt. Welke z-waarde hoort bij die grens?",
        opties=[
            "ongeveer min 1,96",
            "ongeveer plus 1,96",
            "ongeveer min 2,5",
            "ongeveer min 0,025",
        ],
        antwoord=0,
        uitleg="Twee komma vijf procent in de linkerstaart hoort bij z gelijk aan min 1,96. Datzelfde getal komt terug bij het betrouwbaarheidsinterval van vijfennegentig procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij N(500; 20) ligt een pak van 540 gram hoe ver van het gemiddelde?",
        opties=[
            "twee standaardafwijkingen boven het gemiddelde",
            "veertig standaardafwijkingen boven het gemiddelde",
            "een halve standaardafwijking boven het gemiddelde",
            "twintig standaardafwijkingen boven het gemiddelde",
        ],
        antwoord=0,
        uitleg="540 min 500 is 40, gedeeld door 20 is 2.",
    ),
    dict(
        type="waarofniet",
        vraag="Om twee verdelingen met een verschillende eenheid te vergelijken, moet je eerst standaardiseren.",
        antwoord=True,
        uitleg="Een z-waarde heeft geen eenheid. Daardoor kan je een lengte met een gewicht vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij N(mu, sigma) berekent een leerling z als sigma min X gedeeld door mu. Wat is er mis?",
        opties=[
            "de drie getallen staan op de verkeerde plaats in de formule",
            "er ontbreekt enkel een minteken voor het resultaat",
            "de formule klopt, maar het resultaat moet gekwadrateerd worden",
            "sigma en mu mogen inderdaad verwisseld worden",
        ],
        antwoord=0,
        uitleg="Het is Z = (X − mu) / sigma: eerst het verschil met het gemiddelde, dan delen door de standaardafwijking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men de normale verdeling zo vaak bij grote datasets?",
        opties=[
            "omdat veel gemeten grootheden van nature rond een gemiddelde liggen",
            "omdat elke dataset bij genoeg metingen normaal verdeeld wordt",
            "omdat ze de enige verdeling is die een rekenapp aankan",
            "omdat ze geen standaardafwijking nodig heeft",
        ],
        antwoord=0,
        uitleg="Lengte, gewicht en meetfouten liggen vaak symmetrisch rond een gemiddelde. Maar je moet altijd nagaan of het past.",
    ),
]
