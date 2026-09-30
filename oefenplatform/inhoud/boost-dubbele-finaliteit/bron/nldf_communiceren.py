# -*- coding: utf-8 -*-
"""De vragen voor "Lichaamstaal, beleefdheid en een tekst die werkt".

Nieuw geschreven voor dubbele finaliteit. Bij doorstroom bestaat dit thema niet
zo: daar zit het spreken in een aparte fiche waarvan het doen zelf (een
spreekopdracht opnemen, een gesprek voeren) 40 % van het examen uitmaakt, en
dat oefen je niet achter een scherm.

Hier is het anders. Spreken en gesprekken samen wegen 24 %, en de DF-fiche zet
er leerstof bij die je wél kan kennen en oefenen: non-verbale communicatie
(lichaamstaal, mimiek, oogcontact, houding, afstand en bewegingen; intonatie,
articulatie, tempo en volume; kleding en uiterlijk; emoji's), de
beleefdheidsconventies, de criteria waaraan je tekst of je mondelinge opdracht
minimaal moet voldoen, en de strategieën die je helpen om te begrijpen en om
begrepen te worden.

Deel 1 gaat over wat je zegt zonder woorden en over beleefdheid; deel 2 over de
eisen aan een tekst en over de strategieën, notities inbegrepen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij non-verbale communicatie?",
        opties=[
            "lichaamstaal en mimiek",
            "oogcontact, houding en afstand",
            "intonatie, tempo en volume",
            "de spelling van je woorden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Spelling is verbaal, en zelfs enkel schriftelijk. Alles wat je overbrengt náást de woorden, is non-verbaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je typt op een forum een hele zin in hoofdletters. Hoe komt dat over?",
        opties=[
            "als schreeuwerig en storend",
            "als extra beleefd tegenover de lezer",
            "als een teken dat je twijfelt",
            "als een grapje dat iedereen begrijpt",
        ],
        antwoord=0,
        uitleg="Hoofdletters zijn online een vorm van non-verbaal gedrag geworden. Ze lezen als roepen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je tijdens een presentatie alles afleest, verlies je de connectie met je luisteraar.",
        antwoord=True,
        uitleg="Je kijkt dan naar je blad in plaats van naar de mensen. Daarom oefen je met kernwoorden in plaats van met een volledige tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is mimiek?",
        opties=[
            "wat je gezicht laat zien terwijl je spreekt",
            "de snelheid waarmee je woorden uitspreekt",
            "de afstand die je tot je gesprekspartner houdt",
            "de kleren die je kiest voor een gesprek",
        ],
        antwoord=0,
        uitleg="Mimiek is de uitdrukking op je gezicht. Tempo, afstand en kleding zijn andere vormen van non-verbaal gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is articulatie?",
        opties=[
            "hoe duidelijk je de klanken van je woorden vormt",
            "hoe luid je spreekt in een grote ruimte",
            "hoe je je zinnen laat stijgen en dalen",
            "hoe snel je door je tekst heen gaat",
        ],
        antwoord=0,
        uitleg="Articulatie gaat over duidelijkheid, intonatie over stijgen en dalen, volume over luidheid en tempo over snelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Emoji's zijn een vorm van non-verbale communicatie.",
        antwoord=True,
        uitleg="Ze doen schriftelijk wat je gezicht doet als je spreekt: ze geven de toon aan bij de woorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een formele mail om te solliciteren voor een vakantiejob. Wat doe je?",
        opties=[
            "de ontvanger aanspreken met u en beleefd afsluiten",
            "een paar smileys zetten om vriendelijk over te komen",
            "afsluiten met groetjes, dat leest wat losser",
            "in jongerentaal schrijven om jezelf te tonen",
        ],
        antwoord=0,
        uitleg="Een formele mail sluit je niet af met groetjes en smileys horen er niet in. Die keuzes zeggen iets over jou.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de manier waarop je je stem laat stijgen en dalen?",
        antwoord=["intonatie", "de intonatie"],
        uitleg="Met intonatie hoor je of een zin een vraag is, of iemand twijfelt, of iemand iets ironisch bedoelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer spreek je iemand aan met u?",
        opties=[
            "bij een volwassene met wie je geen nauwe band hebt",
            "bij iedereen die ouder is dan zestien jaar",
            "enkel bij mensen die jou eerst met u aanspreken",
            "enkel als je iets van die persoon nodig hebt",
        ],
        antwoord=0,
        uitleg="Het gaat niet om leeftijd alleen maar om afstand. Je oom van veertig blijf je gewoon tutoyeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een smiley is in elke soort bericht even gepast.",
        antwoord=False,
        uitleg="In een WhatsAppbericht aan vrienden ondersteunt een smiley je boodschap; in een formele mail is hij ongepast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de beleefdheidsconventies in een gesprek?",
        opties=[
            "je gesprekspartner laten uitspreken",
            "een gepast register en een gepaste toon kiezen",
            "interesse tonen in wat de ander zegt",
            "zo veel mogelijk zelf aan het woord blijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wie het gesprek volpraat, respecteert de conventies niet, hoe vriendelijk hij ook klinkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom let je op de lichaamstaal van je gesprekspartner?",
        opties=[
            "om in te schatten hoe je boodschap aankomt en daarop te reageren",
            "om te kunnen zeggen of hij de waarheid spreekt",
            "om te weten hoe lang het gesprek nog zal duren",
            "om te bepalen of hij ouder of jonger is dan jij",
        ],
        antwoord=0,
        uitleg="Fronsen, wegkijken of knikken vertelt je of je verder moet uitleggen. Of iemand liegt, lees je er niet aan af.",
    ),
    dict(
        type="waarofniet",
        vraag="Kleding en uiterlijk horen niet bij communicatie, want je zegt er niets mee.",
        antwoord=False,
        uitleg="De fiche rekent ze uitdrukkelijk bij de non-verbale communicatie. Wie op een sollicitatie komt, kiest niet toevallig wat hij aantrekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gesprek correct voeren betekent dat je het kan:",
        opties=[
            "beginnen",
            "gaande houden",
            "beëindigen",
            "winnen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een gesprek is geen wedstrijd. Beginnen, gaande houden en beëindigen zijn drie aparte vaardigheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bus is te laat en je belt je leerkracht op om te zeggen dat je tien minuten later bent. Wie is hier de ontvanger?",
        opties=[
            "je leerkracht",
            "de busmaatschappij",
            "jijzelf",
            "je beste vriendin",
        ],
        antwoord=0,
        uitleg="De zender ben jij, het kanaal is de telefoon, de boodschap is je vertraging en de ontvanger is wie je opbelt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je alles wat je overbrengt zonder woorden?",
        antwoord=["non-verbale communicatie", "nonverbale communicatie"],
        uitleg="Lichaamstaal, mimiek, oogcontact, intonatie, kleding en emoji's horen er allemaal bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie voldoende oogcontact maakt, komt doorgaans betrouwbaarder over bij zijn gesprekspartner.",
        antwoord=True,
        uitleg="Daarom staat het ook bij de criteria voor spreken en gesprekken: gepaste, niet-storende lichaamstaal en voldoende oogcontact.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spreekt heel snel omdat je zenuwachtig bent. Welk criterium komt daardoor in het gedrang?",
        opties=[
            "je vlotheid en je verstaanbaarheid",
            "je taakvoltooiing",
            "je spelling",
            "je lay-out",
        ],
        antwoord=0,
        uitleg="Spelling en lay-out gelden enkel voor wat je schrijft. Bij spreken tellen vlotheid, uitspraak en intonatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom pas je je taalgebruik aan je ontvanger aan?",
        opties=[
            "omdat dezelfde boodschap anders aankomt bij een vriend dan bij een directeur",
            "omdat je bij een directeur altijd minder mag vertellen",
            "omdat je anders geen structuuraanduiders mag gebruiken",
            "omdat een vriend geen formele taal zou verstaan",
        ],
        antwoord=0,
        uitleg="Je verandert niet wát je zegt maar hóé je het zegt: de toon, het register, de aanspreking.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens een gesprek mag je je gesprekspartner onderbreken zodra je iets weet wat hij niet weet.",
        antwoord=False,
        uitleg="Wachten tot iemand uitgesproken is, hoort bij de beleefdheidsconventies. Wat je weet, kan een zin later nog.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent taakvoltooiing als criterium voor je tekst?",
        opties=[
            "je tekstdoel is bereikt en je boodschap komt volledig over",
            "je hebt je tekst binnen de voorziene tijd afgewerkt",
            "je hebt het gevraagde aantal woorden precies gehaald",
            "je hebt je tekst helemaal zonder fouten geschreven",
        ],
        antwoord=0,
        uitleg="Een tekst zonder spelfouten die zijn doel mist, voldoet niet. Taakvoltooiing gaat over of het werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke criteria gelden enkel voor schrijven en schriftelijke interactie?",
        opties=[
            "spelling en leestekengebruik",
            "tekstopbouw en lay-out",
            "titels en alinea-indeling",
            "uitspraak en intonatie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uitspraak en intonatie horen bij spreken en gesprekken. De rest kan je enkel op papier of op een scherm beoordelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het criterium woordenschat volstaat het dat je de meest gewone woorden correct gebruikt.",
        antwoord=False,
        uitleg="Er wordt ook minder frequente woordenschat verwacht, en figuurlijke taal: een uitdrukking, een vergelijking, een metafoor of een spreekwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met variatie in zinsbouw?",
        opties=[
            "je bouwt niet elke zin op dezelfde manier op",
            "je gebruikt in elke alinea een ander onderwerp",
            "je wisselt voortdurend van werkwoordstijd",
            "je zet elke zin in een andere alinea",
        ],
        antwoord=0,
        uitleg="Vijf zinnen na elkaar die met hetzelfde woord beginnen, lezen vlak. Variatie houdt de lezer bij de les.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke strategieën helpen je om een moeilijke tekst te begrijpen?",
        opties=[
            "jezelf eerst vragen stellen over wat je al weet",
            "letten op de titel, de tussentitels en de beelden",
            "onbekende woorden afleiden uit de context",
            "elk woord dat je niet kent meteen opzoeken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles opzoeken kost te veel tijd op een examen. Zoek enkel op wat je echt nodig hebt om de tekst te begrijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je neemt notities bij een luistertekst. Waaraan moeten ze voldoen?",
        opties=[
            "ze sluiten aan bij de inhoud en zijn achteraf nog bruikbaar",
            "ze zijn in volledige zinnen en netjes geschreven",
            "ze bevatten elk woord dat je gehoord hebt",
            "ze zijn korter dan tien regels",
        ],
        antwoord=0,
        uitleg="Afkortingen, symbolen en telegramstijl mogen. Het enige dat telt, is dat je er straks nog iets mee kan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mindmap of een schema kan dienen als notitie bij een tekst.",
        antwoord=True,
        uitleg="Een schema, een tabel of een mindmap laten verbanden sneller zien dan losse zinnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de indeling inleiding, midden en slot van een tekst?",
        antwoord=["de IMS-structuur", "IMS-structuur", "IMS"],
        uitleg="Elke goed gestructureerde tekst heeft een inleiding, een midden en een slot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel deelonderwerpen horen er in één alinea?",
        opties=[
            "één",
            "twee",
            "drie",
            "zo veel als er passen",
        ],
        antwoord=0,
        uitleg="Per alinea vind je één deelonderwerp terug. Begint er iets nieuws, dan begin je een nieuwe alinea.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je een spreek- of schrijfplan met kernwoorden?",
        opties=[
            "om de volgorde vast te leggen zonder al je zinnen uit te schrijven",
            "om precies te weten hoeveel woorden je gaat gebruiken",
            "om de spelling van moeilijke woorden vooraf na te kijken",
            "om te vermijden dat je nog naar je publiek moet kijken",
        ],
        antwoord=0,
        uitleg="Met kernwoorden hou je je lijn vast en blijf je toch vrij in je formulering. Een uitgeschreven tekst lees je af.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag op het examen Nederlands een online woordenboek en een spellingcontrole gebruiken.",
        antwoord=True,
        uitleg="Ze staan als link in je examen. Oefen er thuis mee, want tijdens het examen heb je geen tijd om alles op te zoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zit vast en weet niet hoe je iets moet formuleren. Wat is een goede strategie?",
        opties=[
            "een omschrijving zoeken of een stukje herlezen",
            "de zin overslaan en hopen dat niemand het merkt",
            "een woord uit een andere taal laten staan",
            "je hele tekst opnieuw beginnen vanaf het begin",
        ],
        antwoord=0,
        uitleg="Je doel bereiken op een andere manier is geoorloofd. Vastlopen en stoppen is het enige wat niet helpt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij creatief zijn met taal?",
        opties=[
            "rijm en ritme",
            "spanningsopbouw",
            "spelen met tijd en ruimte",
            "zo veel mogelijk moeilijke woorden gebruiken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Moeilijke woorden stapelen is geen creativiteit maar mist vaak zijn doel. Humor en stijlfiguren horen er wel bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je verwijswoorden en signaalwoorden samen?",
        antwoord=["structuuraanduiders", "de structuuraanduiders"],
        uitleg="Zij, hem, deze en hun verwijzen; maar, dus, want en hoewel geven een signaal over de gedachtegang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een korte handleiding voor een beamer. Wat is je tekstdoel?",
        opties=[
            "iemand iets uitleggen",
            "iemand overtuigen",
            "je mening geven",
            "iets vertellen",
        ],
        antwoord=0,
        uitleg="Een handleiding, een recept en een stappenplan hebben hetzelfde doel: de lezer iets laten doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst met een gepaste lay-out heeft altijd tussentitels nodig.",
        antwoord=False,
        uitleg="Indien nodig gebruik je titels of tussentitels. In een korte mail zouden ze net vreemd staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke opdrachten vragen dat je in interactie gaat?",
        opties=[
            "schriftelijk reageren op wat iemand anders schreef",
            "een gesprek voeren met iemand over een thema",
            "reageren op een discussie op een forum",
            "een verhaal voorlezen voor een klas",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij een spreekopdracht ben je alleen aan het woord. Interactie betekent dat er iemand terugspreekt of terugschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je voor je je tekst indient?",
        opties=[
            "grondig nalezen of de communicatie helder, gepast, correct en vlot is",
            "tellen hoeveel signaalwoorden je gebruikt hebt",
            "de laatste alinea nog eens herhalen als slot",
            "je tekst korter maken tot hij op één bladzijde past",
        ],
        antwoord=0,
        uitleg="Die vier woorden zijn precies waarop je tekst beoordeeld wordt. Lees hem na alsof je de ontvanger bent.",
    ),
    dict(
        type="waarofniet",
        vraag="Je krijgt voor de mondelinge opdrachten voorbereidingstijd, maar je moet ook spontaan kunnen reageren.",
        antwoord=True,
        uitleg="Je krijgt vijftien minuten voorbereiding voor twee opdrachten; wat je gesprekspartner zegt, staat niet op je blad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk criterium gaat over inleiding, midden, slot en duidelijke tekstverbanden?",
        opties=[
            "tekststructuur en samenhang",
            "taakvoltooiing",
            "register en beleefdheidsconventies",
            "grammatica en zinsbouw",
        ],
        antwoord=0,
        uitleg="Signaalwoorden maken die samenhang zichtbaar: ten eerste, daarom, tot slot.",
    ),
]
