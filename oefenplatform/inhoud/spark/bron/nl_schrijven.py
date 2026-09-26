# -*- coding: utf-8 -*-
"""De vragen voor "Schrijven, spreken en gesprekken voeren" (✨ Spark, Nederlands).

Uit de vakfiche, deel Schrijven, spreken en interactie: informatie geven en
vragen, iets uitleggen, je mening geven, in gesprek gaan over maatschappelijke
thema's, iemand overtuigen, iets vertellen en creatief zijn met taal. Daarbij
de vereisten waarop je beoordeeld wordt (taakvoltooiing, woordenschat,
grammatica en zinsbouw, tekststructuur en samenhang, spelling en leestekens,
tekstopbouw en lay-out, vlotheid) en de strategieën: een schrijf- of spreekplan
maken, inspelen op je gesprekspartner en je tekst grondig nalezen.

Deel 1 gaat over de opdracht en het plan. Deel 2 gaat over nakijken,
gesprekken voeren en overtuigen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je moet uitleggen hoe je een gezelschapsspel speelt. Waarmee begin je het best?",
        opties=["Met een plan: welke stappen komen er, en in welke volgorde", "Met de moeilijkste regel", "Met een grapje", "Met de uitzonderingen op de regels, want die vergeet men het snelst"],
        antwoord=0,
        uitleg="Een schrijf- of spreekplan met kernwoorden zorgt dat je niets vergeet en in de juiste volgorde blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'taakvoltooiing' bij een schrijfopdracht?",
        opties=["Dat je doet wat gevraagd werd en je boodschap volledig overkomt", "Dat je op tijd klaar bent", "Dat je zoveel mogelijk woorden gebruikt zodat je tekst lang genoeg is", "Dat je geen fouten maakt"],
        antwoord=0,
        uitleg="Taakvoltooiing kijkt of het tekstdoel bereikt is: is de inhoud helder, correct, volledig en ter zake?",
    ),
    dict(
        type="invultekst",
        vraag="Een plan met kernwoorden dat je maakt vóór je begint te schrijven, heet een ___.",
        antwoord="schrijfplan",
        uitleg="Voor een spreekopdracht doe je hetzelfde met een spreekplan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke opdrachten vragen dat je iemand overtuigt?",
        opties=[
            "Een productadvertentie opstellen",
            "Met je ouders onderhandelen over een afspraak",
            "Een vriend warm maken voor de jeugdbeweging",
            "Een recept uitschrijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij de eerste drie wil je dat de ander iets doet of denkt. Een recept legt alleen uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een schrijfopdracht op het examen krijg je een kader dat je ondersteunt.",
        antwoord=True,
        uitleg="Je krijgt de situatie mee: voor wie je schrijft, waarom en waarover. Dat kader gebruik je ook echt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een zoekertje om je oude gitaar te verkopen. Wat hoort er zeker in?",
        opties=[
            "Wat je verkoopt, in welke staat, en hoe men je bereikt",
            "Je hele muziekgeschiedenis",
            "Een gedicht over gitaren",
            "De prijs van een nieuwe gitaar in de winkel",
        ],
        antwoord=0,
        uitleg="Informatie geven betekent: alles wat de ontvanger nodig heeft, en niets meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een goede tekststructuur?",
        opties=[
            "Een herkenbare inleiding, midden en slot",
            "Alinea's die elk één punt behandelen",
            "Signaalwoorden die de verbanden tonen",
            "Zo lang mogelijke zinnen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Structuur en samenhang worden apart beoordeeld. Lange zinnen maken een tekst net moeilijker.",
    ),
    dict(
        type="invultekst",
        vraag="Bij een spreekopdracht ben je alleen aan het woord; bij ___ ga je in gesprek met iemand.",
        antwoord="interactie",
        uitleg="Mondelinge interactie betekent: een gesprek beginnen, gaande houden en netjes beëindigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vertelt in een mail aan een vriend over je weekend. Welk doel heb je?",
        opties=["Iets vertellen", "Overtuigen", "Instructies geven", "Informatie vragen"],
        antwoord=0,
        uitleg="Vertellen is een apart doel: je deelt wat je meegemaakt hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is 'creatief zijn met taal'?",
        opties=["Spelen met rijm, ritme en lay-out om je boodschap sterker te maken", "Zoveel mogelijk moeilijke woorden gebruiken, zodat je tekst geleerd klinkt", "In een andere taal schrijven", "Zonder leestekens schrijven"],
        antwoord=0,
        uitleg="Een slogan, een gedicht of een verhaal: met eenvoudige technieken maak je je tekst opvallend.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor de mondelinge opdrachten krijg je voorbereidingstijd, maar je moet ook spontaan kunnen reageren.",
        antwoord=True,
        uitleg="Je bereidt voor wat je wil zeggen, maar een gesprek loopt nooit helemaal zoals je plande.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil informatie vragen over een product in een winkel. Welke vraag is het duidelijkst?",
        opties=["Kan u me zeggen hoelang de garantie op dit toestel loopt?", "Dat ding, is dat iets?", "Hoe zit dat allemaal?", "Ik zou graag iets weten over dat toestel daar in de rekken."],
        antwoord=0,
        uitleg="Een duidelijke vraag noemt precies wat je wil weten. Zo krijg je ook een bruikbaar antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen worden bij een schrijfopdracht beoordeeld?",
        opties=[
            "Je spelling en je leestekens",
            "Je tekstopbouw en je lay-out",
            "Of je boodschap volledig is",
            "Je handschrift",
        ],
        antwoord=[0, 1, 2],
        uitleg="Op een digitaal examen typ je, dus je handschrift telt niet mee. De rest wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Je tekst nalezen vóór je hem indient, hoort bij de opdracht.",
        antwoord=True,
        uitleg="Nalezen is een strategie: is mijn boodschap helder, gepast, correct en vlot?",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je tijdens het spreken een woord niet vindt?",
        opties=[
            "Je omschrijft het met andere woorden en gaat verder",
            "Je stopt met praten",
            "Je herhaalt tien keer hetzelfde woord",
            "Je begint helemaal opnieuw",
        ],
        antwoord=0,
        uitleg="Een omschrijving zoeken is een compensatiestrategie: je bereikt je doel langs een andere weg.",
    ),
    dict(
        type="invultekst",
        vraag="Je tekst indelen in stukken met een witregel ertussen, dat zijn je ___.",
        antwoord="alinea's",
        uitleg="Alinea's maken je tekst leesbaar. Waar nodig zet je er ook tussentitels bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gaat in gesprek over een maatschappelijk thema, bijvoorbeeld het klimaat. Wat helpt je?",
        opties=["Vooraf een paar bronnen lezen en er cijfers uit onthouden", "Alleen zeggen wat je vrienden ervan vinden, zodat je niet alleen staat", "Zo snel mogelijk praten", "Alleen luisteren"],
        antwoord=0,
        uitleg="De vakfiche vraagt uitdrukkelijk dat je bronnen gebruikt als je over zulke thema's spreekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatschappelijke thema's noemt de vakfiche als voorbeeld?",
        opties=["gezondheid", "klimaat", "sociale media", "sterrenkunde"],
        antwoord=[0, 1, 2],
        uitleg="Gezondheid, klimaat, sociale media, inspraak en mobiliteit: thema's op jouw niveau waar je zelf mee te maken hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het spreken moet je verzorgd Standaardnederlands gebruiken.",
        antwoord=True,
        uitleg="Uitspraak en intonatie worden beoordeeld: je spreekt verzorgd Standaardnederlands, geen dialect of tussentaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt de opdracht: 'Schrijf een mail aan de sportclub om je in te schrijven.' Wat is je doel?",
        opties=[
            "Informatie geven en vragen",
            "Een verhaal vertellen",
            "Iemand overtuigen",
            "Een gedicht schrijven",
        ],
        antwoord=0,
        uitleg="Je geeft je gegevens door en vraagt wat je nog moet weten: uur, prijs, uitrusting.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je hebt je tekst af. Waarop let je bij het nalezen?",
        opties=[
            "Of de boodschap helder, gepast, correct en vlot is",
            "Of de tekst precies honderd woorden telt",
            "Of je lievelingswoord erin staat",
            "Of er een foto bij staat",
        ],
        antwoord=0,
        uitleg="Dat zijn de vier vragen uit de vakfiche. Een spellingcontrole helpt, maar vervangt het nalezen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan een spellingcontrole niet voor je doen?",
        opties=[
            "Zien of je het juiste woord gebruikt hebt",
            "Een tikfout in een woord aanduiden",
            "Een ontbrekende letter opmerken",
            "Een onbekend woord markeren",
        ],
        antwoord=0,
        uitleg="'Word' in plaats van 'wordt' of 'hij ligt' in plaats van 'hij legt': dat zijn bestaande woorden, dus de controle zwijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe begin je een gesprek met iemand die je niet kent?",
        opties=[
            "Je groet, stelt jezelf voor en zegt waarvoor je komt",
            "Je begint meteen over je probleem",
            "Je wacht tot de ander iets zegt",
            "Je stuurt eerst een bericht",
        ],
        antwoord=0,
        uitleg="Een gesprek correct beginnen, gaande houden en beëindigen hoort bij mondelinge interactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe houd je een gesprek gaande?",
        opties=[
            "Je stelt vragen aan de ander",
            "Je reageert op wat de ander zegt",
            "Je toont interesse en laat de ander uitspreken",
            "Je vertelt zonder ophouden je eigen verhaal",
        ],
        antwoord=[0, 1, 2],
        uitleg="Inspelen op je gesprekspartner is een strategie. Wie alleen zendt, voert geen gesprek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gesprek beëindig je het best door gewoon weg te lopen.",
        antwoord=False,
        uitleg="Je rondt af: je bedankt, vat kort samen wat afgesproken is en groet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil je ouders overtuigen dat je later mag thuiskomen. Wat werkt het best?",
        opties=["Argumenten geven en een voorstel doen waar zij ook iets aan hebben", "Roepen dat het oneerlijk is", "Zeggen dat iedereen het mag", "Blijven herhalen wat je wil tot ze toegeven, want volhouden loont"],
        antwoord=0,
        uitleg="Onderhandelen betekent: argumenten geven, rekening houden met de ander en samen tot een afspraak komen.",
    ),
    dict(
        type="invultekst",
        vraag="Een reden die je geeft om je standpunt te verdedigen, is een ___.",
        antwoord="argument",
        uitleg="Overtuigen doe je met argumenten die aansluiten bij je standpunt, niet met herhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een korte handleiding schrijven. Welke opbouw kies je?",
        opties=["Genummerde stappen in de volgorde waarin ze uitgevoerd worden", "Een verhaal van begin tot eind", "Een betoog met argumenten, zodat de lezer overtuigd raakt om het te doen", "Een gedicht"],
        antwoord=0,
        uitleg="Bij instructies is de volgorde de structuur. Nummers of signaalwoorden houden ze uit elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen horen thuis in een formele mail aan een onbekende?",
        opties=[
            "Geachte mevrouw",
            "Met vriendelijke groeten",
            "Ik zou graag willen weten wanneer de inschrijvingen starten.",
            "Hey, alles goed?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aanhef, slotgroet en beleefde formulering horen bij een formele mail. 'Hey' bewaar je voor vrienden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een formele brief sluit je af met 'groetjes'.",
        antwoord=False,
        uitleg="'Groetjes' is informeel. In een formele brief schrijf je 'Met vriendelijke groeten' of 'Hoogachtend'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spreekopdracht duurt twee minuten. Hoe bereid je die voor?",
        opties=[
            "Met kernwoorden op een blad, niet met een volledig uitgeschreven tekst",
            "Door alles woord voor woord van buiten te leren",
            "Door niets voor te bereiden",
            "Door een tekst voor te lezen van je scherm",
        ],
        antwoord=0,
        uitleg="Met kernwoorden blijf je natuurlijk spreken en kan je oogcontact houden. Voorlezen klinkt vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'vlotheid' bij een spreekopdracht?",
        opties=["Dat je voldoende vlot spreekt, zonder telkens lang te haperen", "Dat je zo snel mogelijk praat, zodat je alles binnen de tijd kwijt kan", "Dat je geen fouten maakt", "Dat je veel gebaren maakt"],
        antwoord=0,
        uitleg="Even nadenken mag. Vlotheid gaat over de vraag of je verhaal blijft lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke strategieën helpen je als je vastzit in een schrijfopdracht?",
        opties=[
            "Een omschrijving zoeken voor het woord dat je mist",
            "Een stukje herlezen en van daaruit verder schrijven",
            "Een woordenboek of spellingcontrole gebruiken",
            "De opdracht half afwerken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Laat je niet ontmoedigen: probeer je doel langs een andere weg te bereiken. Half afwerken kost je de taakvoltooiing.",
    ),
    dict(
        type="invultekst",
        vraag="Een woord met dezelfde betekenis als een ander woord, waarmee je je tekst levendiger maakt, is een ___.",
        antwoord="synoniem",
        uitleg="Variëren in woordenschat en zinsbouw maakt een tekst levendig. Synoniemen zijn daarbij je belangrijkste hulpmiddel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een recensie van een film voor de schoolkrant. Wat hoort er zeker in?",
        opties=[
            "Je mening, met argumenten en voorbeelden uit de film",
            "Het volledige verhaal, met het einde erbij",
            "Alleen een cijfer op tien",
            "De namen van alle acteurs",
        ],
        antwoord=0,
        uitleg="Een recensie is een onderbouwde mening. Het einde verklappen doe je niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Je tekst mag langer zijn dan gevraagd, zolang alles klopt.",
        antwoord=False,
        uitleg="De opdracht bepaalt de lengte. Te lang schrijven kost tijd en leidt af van je boodschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is het duidelijkst geschreven?",
        opties=[
            "Wij vragen u het formulier vóór 15 mei terug te sturen.",
            "Het formulier dat, indien mogelijk en zo snel als het kan, teruggestuurd dient te worden, liefst voor het midden van de maand mei.",
            "Formulier terug, mei, graag.",
            "Stuur het maar eens terug als het uitkomt.",
        ],
        antwoord=0,
        uitleg="Correcte zinsbouw plus een concrete datum. De tweede zin loopt vast, de derde is geen zin, de vierde is te vaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet in een gesprek spontaan reageren op een vraag die je niet verwacht had. Wat doe je?",
        opties=["Je neemt even tijd, zegt wat je wél weet en vraagt gerust om verduidelijking", "Je zwijgt", "Je verandert van onderwerp", "Je zegt dat de vraag onduidelijk is en vraagt om een andere vraag te stellen"],
        antwoord=0,
        uitleg="Om verduidelijking vragen mag: dat hoort bij een gesprek gaande houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke technieken maken een slogan sterk?",
        opties=["Rijm", "Ritme", "Een korte, opvallende lay-out", "Veel vakjargon"],
        antwoord=[0, 1, 2],
        uitleg="Creatief taalgebruik werkt met klank en vorm. Vakjargon maakt een slogan net onbegrijpelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je je mail nog eens na vóór je hem verstuurt?",
        opties=["Omdat je hem niet meer kan terughalen en fouten je boodschap verzwakken", "Omdat dat verplicht is", "Omdat een mail met fouten door de ontvanger vaak niet geopend wordt", "Omdat je dan meer woorden hebt"],
        antwoord=0,
        uitleg="Een verzonden mail is weg. Eén keer nalezen op spelling, toon en volledigheid scheelt veel.",
    ),
]
