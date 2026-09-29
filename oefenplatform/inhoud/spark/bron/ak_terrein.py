# -*- coding: utf-8 -*-
"""De vragen voor "Het landschap op het terrein" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "geografisch onderzoek", onderdeel
"het landschap onderzoeken met gepaste onderzoekstechnieken" (17,5 % van het
examen, samen met [[ak_geopunt]]).

Deel 1 gaat over het terreinwerk zelf: je onderzoeksgebied lokaliseren met een
GPS en met een kaart, jezelf oriënteren ten opzichte van landschapselementen,
en het reliëf beschrijven met de helling, de hoogteverschillen en de
horizonlijn.
Deel 2 gaat over wat je daarna beschrijft: de vegetatie, de bebouwing en het
landgebruik, en over het bodemonderzoek waarbij je de losse gesteenten in de
ondergrond determineert.

De determineerkenmerken van de vier losse gesteenten zijn de klassieke
veldproeven en worden hier consequent zo gebruikt: grind heeft korrels die je
duidelijk ziet, zand knerpt tussen je tanden en rolt niet, leem voelt zacht en
melig aan, en klei is plakkerig, glimt als je erover wrijft en rolt tot een dun
draadje. Wie hier iets bijschrijft, houdt zich aan die vier.

De vragen blijven bij wat je op het terrein kán vaststellen. Alles wat je enkel
uit een kaartlaag of uit een boek weet, hoort in [[ak_geopunt]] of bij de andere
thema's thuis.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je gaat met de klas een stuk landschap onderzoeken. Wat doe je als eerste ter plaatse?",
        opties=[
            "Vaststellen waar je precies staat",
            "Meteen beginnen met de bodem uit te graven",
            "De namen van de planten opzoeken",
            "Een foto van het hele gebied nemen",
        ],
        antwoord=0,
        uitleg="Zonder te weten waar je staat, kan je je waarnemingen nergens aan koppelen. Eerst lokaliseren, dan oriënteren, en pas daarna beschrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hulpmiddelen gebruik je om je onderzoeksgebied te lokaliseren? Er zijn er meerdere juist.",
        opties=[
            "Een satellietnavigatiesysteem",
            "Een kaart van het gebied",
            "De coördinaten van het punt",
            "Een thermometer om de temperatuur te meten",
            "Een regenmeter om de neerslag te meten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Lokaliseren is bepalen wáár je bent. Daarvoor dienen GPS, kaart en coördinaten. Een thermometer en een regenmeter meten het weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Lokaliseren en oriënteren zijn twee verschillende dingen.",
        antwoord=True,
        uitleg="Lokaliseren is bepalen waar je staat. Oriënteren is bepalen welke kant je uit kijkt. Je hebt allebei nodig voor je iets kan opschrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil je kaart in de juiste richting leggen. Hoe doe je dat?",
        opties=[
            "Je draait de kaart tot de noordpijl naar het noorden wijst",
            "Je legt de kaart met de titel naar je toe",
            "Je legt de kaart plat op de grond met de legende boven",
            "Je houdt de kaart recht voor je met de schaal bovenaan",
        ],
        antwoord=0,
        uitleg="Wijst de noordpijl van de kaart in dezelfde richting als de naald van je kompas, dan ligt wat je voor je ziet ook voor je op de kaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een landschapselement waaraan je je kan oriënteren? Er zijn er meerdere juist.",
        opties=[
            "Een kerktoren",
            "Een watertoren",
            "Een lange bomenrij",
            "Een wolk aan de hemel",
            "Een auto die voorbijrijdt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een herkenningspunt moet blijven staan. Een toren of een bomenrij staat er morgen nog; een wolk en een auto zijn binnen een minuut weg.",
    ),
    dict(
        type="invultekst",
        vraag="Bepalen welke kant je uit kijkt, noemt men jezelf ___.",
        antwoord="oriënteren",
        uitleg="Oriënteren kan met een kompas, met de stand van de zon of met herkenningspunten in het landschap zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke richting staat de zon rond de middag bij ons?",
        opties=[
            "In het zuiden",
            "In het noorden",
            "In het oosten",
            "In het westen",
        ],
        antwoord=0,
        uitleg="Bij ons komt de zon ruwweg in het oosten op, staat ze rond de middag in het zuiden en gaat ze in het westen onder. Zo kan je je ook zonder kompas oriënteren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kompas werkt betrouwbaar vlak naast een ijzeren hek of een auto.",
        antwoord=False,
        uitleg="IJzer en magneten trekken de naald scheef. Ga enkele meters verderop staan voor je de richting afleest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijf je als je het reliëf van je onderzoeksgebied beschrijft? Er zijn er meerdere juist.",
        opties=[
            "De helling van het terrein",
            "De hoogteverschillen die je ziet",
            "Waar de horizonlijn ligt",
            "Welke bomen er groeien",
            "Hoeveel huizen er staan",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt drie dingen bij het reliëf: de helling, de hoogteverschillen en de horizonlijn. Bomen horen bij de vegetatie en huizen bij de bebouwing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je staat onderaan een helling. Wat merk je aan de horizonlijn?",
        opties=[
            "Ze ligt dichtbij, want de helling neemt je zicht weg",
            "Ze ligt verder weg dan op een vlakte",
            "Ze ligt precies even ver weg als op elke andere plaats",
            "Ze is helemaal niet te zien in een dal",
        ],
        antwoord=0,
        uitleg="Wat je ziet, wordt begrensd door het terrein zelf. Onderaan een helling is de horizon de helling; bovenop kijk je juist heel ver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je op het terrein vaststellen dat een helling steil is?",
        opties=[
            "Je merkt dat je zwaarder moet stappen om te klimmen",
            "Je ziet dat er veel meer bomen op groeien dan beneden",
            "Je voelt dat de wind er harder waait",
            "Je hoort dat het er stiller is dan beneden",
        ],
        antwoord=0,
        uitleg="Steilte voel je in je benen, en je ziet het aan het terrein: kortere afstand, groter hoogteverschil. Op de kaart zie je het aan de hoogtelijnen dicht bijeen.",
    ),
    dict(
        type="invultekst",
        vraag="Het verschil in hoogte tussen het laagste en het hoogste punt van je gebied heet het ___.",
        antwoord="hoogteverschil",
        uitleg="Op het terrein schat je dat, met een hoogtekaart of een GPS meet je het. Zeg er altijd bij tussen welke twee punten je gemeten hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een satellietnavigatiesysteem werkt overal even goed, ook in een gebouw of onder dicht bladerdek.",
        antwoord=False,
        uitleg="Het toestel heeft zicht op de satellieten nodig. Onder een dak, in een diep dal of onder dicht bos wordt de plaatsbepaling onnauwkeurig of valt ze weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je op het terrein ook het tijdstip van je waarnemingen?",
        opties=[
            "Omdat het landschap er per seizoen en per uur anders bij ligt",
            "Omdat je anders de coördinaten van het punt niet kan berekenen",
            "Omdat het kompas per uur anders uitslaat",
            "Omdat het hoogteverschil met de dag verandert",
        ],
        antwoord=0,
        uitleg="Een akker in maart ziet er anders uit dan in augustus, en een veld in de ochtendmist anders dan in de middagzon. Wie later vergelijkt, moet dat weten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat neem je mee voor een terreinonderzoek? Er zijn er meerdere juist.",
        opties=[
            "Een kompas",
            "Een kaart van het gebied",
            "Een schepje om de bodem te bekijken",
            "Een barometer voor de luchtdruk",
            "Een globe van de wereld",
        ],
        antwoord=[0, 1, 2],
        uitleg="Op het terrein heb je nodig wat je ter plaatse gebruikt: kompas, kaart, schrijfgerei en iets om de bodem mee te bekijken. Een globe hoort in de klas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je beschrijft het landschap ten opzichte van een kerktoren. Wat noteer je het best?",
        opties=[
            "In welke richting en hoe ver hij ligt",
            "Hoe oud de kerk ongeveer is",
            "Hoeveel mensen er naar de mis gaan",
            "Welke kleur de dakpannen hebben",
        ],
        antwoord=0,
        uitleg="Voor het situeren tellen richting en afstand. De ouderdom en de kleur zijn misschien interessant, maar helpen niet om je positie vast te leggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een landschap volledig beschrijven zonder ooit ter plaatse te gaan.",
        antwoord=False,
        uitleg="Kaarten en foto's brengen je ver, maar niet alles staat erop. Geluid, geur, de staat van een gracht of een pas gekapte haag zie je enkel ter plaatse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je op het terrein een schets in plaats van alleen een foto?",
        opties=[
            "Omdat je op een schets zelf kiest wat belangrijk is",
            "Omdat een foto op het terrein niet mag",
            "Omdat een schets nauwkeuriger is dan een foto van hetzelfde",
            "Omdat je op een foto de kleuren niet ziet",
        ],
        antwoord=0,
        uitleg="Op een foto staat alles even hard. Op een schets teken je de horizonlijn, de helling en de elementen die er voor jouw vraag toe doen, en laat je de rest weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een transect of doorsnede van een landschap?",
        opties=[
            "Een tekening van het terrein zoals je het van opzij zou zien",
            "Een foto van het hele gebied genomen vanuit een vliegtuig",
            "Een lijst van alle planten die je er gevonden hebt",
            "Een kaart waarop de gemeentegrenzen staan",
        ],
        antwoord=0,
        uitleg="Een doorsnede toont het reliëf van opzij, met de hoogtes langs een lijn door het gebied. Zo zie je in één beeld waar het klimt en waar het daalt.",
    ),
    dict(
        type="invultekst",
        vraag="Het gebied waarin je je waarnemingen doet, bak je vooraf af; dat is je onderzoeks___.",
        antwoord="onderzoeksgebied",
        uitleg="Zonder afbakening blijf je bezig. Eén perceel, één beekvallei of één straat is voor een terreinonderzoek vaak al groot genoeg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je staat in je onderzoeksgebied en je beschrijft wat er groeit, wat er gebouwd staat en waar de grond voor dient. Wat beschrijf je dan?",
        opties=[
            "De vegetatie, de bebouwing en het landgebruik",
            "Het reliëf, de bodem en de ondergrond",
            "Het klimaat, het weer en de wind",
            "De coördinaten, de richting en de afstand",
        ],
        antwoord=0,
        uitleg="Dat zijn de drie dingen die de fiche na het reliëf noemt. Samen met het reliëf en de bodem heb je dan het hele landschap beschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat noteer je als je de vegetatie beschrijft? Er zijn er meerdere juist.",
        opties=[
            "Of er bomen, struiken of gras staan",
            "Of het loofbomen of naaldbomen zijn",
            "Hoe dicht de begroeiing staat",
            "Wie de eigenaar van het perceel is",
            "Wanneer de bomen geplant werden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij de vegetatie beschrijf je wat er groeit en hoe dicht. De eigenaar en het plantjaar zie je op het terrein niet, en die horen bij andere bronnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet in het midden van een weide een rij knotwilgen langs een gracht. Wat is dat?",
        opties=[
            "Een landschapselement dat door de mens is aangeplant",
            "Natuurlijke vegetatie die daar vanzelf gegroeid is",
            "Een stuk bos dat is blijven staan bij het kappen",
            "Een grens tussen twee klimaatzones",
        ],
        antwoord=0,
        uitleg="Knotwilgen worden geplant en regelmatig geknot voor het hout. Ze staan er dus door toedoen van de mens, ook al zien ze er natuurlijk uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Aan de bebouwing kan je zien hoe de grond in een gebied gebruikt wordt.",
        antwoord=True,
        uitleg="Loodsen en silo's wijzen op een landbouwbedrijf, rijhuizen op een dorpskern, hallen met parkings op een bedrijventerrein. De gebouwen verraden de functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van landgebruik kan je op het terrein vaststellen? Er zijn er meerdere juist.",
        opties=[
            "Landbouw",
            "Wonen",
            "Recreatie",
            "De bodemtextuur",
            "De hoogteligging",
        ],
        antwoord=[0, 1, 2],
        uitleg="Landgebruik is wat de mens met de grond doet: landbouw, wonen, industrie, verkeer, recreatie. Bodem en hoogte zijn natuurlijke lagen.",
    ),
    dict(
        type="invultekst",
        vraag="Om de bodem te bekijken, graaf je een klein ___ zodat je de lagen onder elkaar ziet.",
        antwoord="kuiltje",
        uitleg="Je hoeft geen put te graven. Een kuiltje van een spade diep toont al de donkere bovenlaag en de lichtere laag eronder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderzoek je bij een bodemonderzoek op het terrein? Er zijn er meerdere juist.",
        opties=[
            "De textuur van de bodem",
            "De kleur van de lagen",
            "Hoe vochtig de bodem is",
            "Hoeveel het perceel waard is",
            "Wie het perceel bewerkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je kijkt naar textuur, kleur, vochtigheid en de lagen onder elkaar. Wat het kost en wie het bewerkt, is geen aardrijkskundige waarneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wrijft wat vochtige grond tussen je vingers en het knerpt duidelijk. Welk los gesteente is dit?",
        opties=[
            "Zand",
            "Klei",
            "Leem",
            "Veen",
        ],
        antwoord=0,
        uitleg="Zandkorrels zijn hoekig en hard genoeg om te knerpen tussen je vingers en tussen je tanden. Klei en leem voelen juist glad of zacht aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rolt vochtige grond tot een dun draadje en het blijft heel. Waarop wijst dat?",
        opties=[
            "Op klei",
            "Op zand",
            "Op grind",
            "Op een mengeling van zand en grind",
        ],
        antwoord=0,
        uitleg="Alleen klei is plakkerig genoeg om tot een dun draadje of een ringetje te rollen. Zand valt meteen uit elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Leem voelt zacht en melig aan, bijna als bloem.",
        antwoord=True,
        uitleg="De korrels van leem liggen tussen die van zand en klei in. Daardoor knerpt het niet en plakt het ook niet echt; het voelt poederig aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je grind onmiddellijk?",
        opties=[
            "Aan de korrels die je met het blote oog ziet liggen",
            "Aan de zachte, meelachtige manier waarop het aanvoelt",
            "Aan het glimmen wanneer je erover wrijft",
            "Aan de sterke geur bij het uitgraven",
        ],
        antwoord=0,
        uitleg="Grind bestaat uit steentjes van meer dan twee millimeter. Die zie je gewoon liggen, terwijl je bij zand, leem en klei moet voelen.",
    ),
    dict(
        type="invultekst",
        vraag="Een tabel waarmee je stap voor stap bepaalt met welk gesteente je te maken hebt, heet een ___.",
        antwoord="determineertabel",
        uitleg="Zo'n tabel stelt telkens een vraag met twee antwoorden. Elk antwoord brengt je naar de volgende vraag, tot er maar één mogelijkheid overblijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de kleur van een bodemlaag nuttige informatie?",
        opties=[
            "Omdat ze iets zegt over het vocht en de humus",
            "Omdat ze de hoogte van het terrein verraadt",
            "Omdat ze aangeeft hoe oud de bodem is in jaren",
            "Omdat ze vertelt wie de grond bewerkt heeft",
        ],
        antwoord=0,
        uitleg="Een donkere bovenlaag wijst op humus, roestbruine vlekken op water dat afwisselend stijgt en daalt, en een grijze laag op grond die lang nat blijft.",
    ),
    dict(
        type="waarofniet",
        vraag="De bovenste bodemlaag is meestal donkerder dan de laag eronder.",
        antwoord=True,
        uitleg="In de bovenlaag zitten de resten van planten en dieren, en die humus maakt de grond donker. Daaronder zit de ondergrond, die lichter van kleur is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt in een weide een natte, grijzige bodem met riet errond. Wat besluit je?",
        opties=[
            "Het grondwater staat hier hoog",
            "De bodem bestaat hier uit grind",
            "Hier heeft ooit een gebouw gestaan",
            "Deze grond is pas geploegd",
        ],
        antwoord=0,
        uitleg="Riet groeit op natte grond, en een grijze kleur wijst op bodem die lang verzadigd is. Samen zeggen die twee dat het water hier dicht bij het oppervlak staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je je waarnemingen op het terrein achteraf met een kaart?",
        opties=[
            "Om na te gaan of wat je zag overeenkomt met wat de kaart toont",
            "Om te weten hoe laat je die dag begonnen bent met kijken",
            "Om de coördinaten van het gebied achteraf te kunnen berekenen",
            "Om de kaart daarna te kunnen bijkleuren",
        ],
        antwoord=0,
        uitleg="Het terrein en de kaart vullen elkaar aan. Verschilt wat je ziet van wat de kaart zegt, dan is de kaart verouderd of heb je iets ontdekt dat er nog niet op staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een terreinonderzoek doet, mag zonder meer overal een put graven.",
        antwoord=False,
        uitleg="Bijna alle grond is van iemand. Vraag toestemming, graaf een klein kuiltje en leg het daarna weer dicht zoals je het gevonden hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een verslag van een terreinonderzoek? Er zijn er meerdere juist.",
        opties=[
            "Waar en wanneer je gekeken hebt",
            "Wat je waargenomen hebt",
            "Welk besluit je eruit trekt",
            "Hoeveel het onderzoek gekost heeft",
            "Wie er allemaal meegegaan is en waarom",
        ],
        antwoord=[0, 1, 2],
        uitleg="Plaats, tijd, waarneming en besluit maken een verslag bruikbaar voor iemand anders. De rest is voor dit onderzoek niet van belang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de eigen leefomgeving een goed onderzoeksgebied om mee te beginnen?",
        opties=[
            "Omdat je er vaak komt en de veranderingen zelf ziet",
            "Omdat er daar meer landschapslagen zijn dan elders",
            "Omdat er nooit toestemming nodig is in je eigen buurt",
            "Omdat de kaarten er nauwkeuriger van zijn",
        ],
        antwoord=0,
        uitleg="Je kent de plek, je kan er makkelijk terugkeren, en je hebt er zelf zien veranderen. Dat maakt het vergelijken met oude kaarten veel sprekender.",
    ),
    dict(
        type="invultekst",
        vraag="De manieren om ter plaatse in het landschap te werken, noemt men samen ___.",
        antwoord="terreintechnieken",
        uitleg="Lokaliseren, oriënteren, het reliëf beschrijven, de vegetatie en de bebouwing noteren en de bodem onderzoeken: dat zijn samen de terreintechnieken.",
    ),
]
