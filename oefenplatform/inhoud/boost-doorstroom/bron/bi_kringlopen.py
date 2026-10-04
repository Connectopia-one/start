# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Kringlopen, voedselrelaties en de mens.

Tweede helft van de kop "materie- en energiestromen" van de vakfiche
biologie 2de graad doorstroomfinaliteit.

Deel 1 gaat over de kringlopen van water, koolstof en stikstof, en over wat
de mens daarin verandert. Deel 2 gaat over het ecosysteem als geheel:
abiotische en biotische factoren, draagkracht, populaties, successie en de
voetafdruk van de mens.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat koolstof een kringloop doorloopt?",
        opties=[
            "dezelfde koolstofatomen worden telkens hergebruikt",
            "er komt voortdurend nieuwe koolstof in de wereld bij",
            "koolstof verdwijnt na gebruik definitief uit het ecosysteem",
            "koolstof komt enkel in levende wezens voor",
        ],
        antwoord=0,
        uitleg="Materie verdwijnt niet. Een koolstofatoom zit vandaag in de lucht, morgen in een blad en volgend jaar in een dier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke processen brengen koolstof in de koolstofkringloop? Kruis alles aan wat juist is.",
        opties=[
            "de fotosynthese haalt koolstofdioxide uit de lucht",
            "de celademhaling geeft koolstofdioxide af",
            "het verbranden van steenkool en aardolie geeft koolstofdioxide af",
            "de verdamping van water uit de oceaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opname door planten, afgifte door ademhaling en afgifte door verbranden zijn de grote stromen. Verdamping hoort bij de waterkringloop.",
    ),
    dict(
        type="invultekst",
        vraag="Welk proces haalt koolstofdioxide uit de lucht en zet de koolstof in organische stof om?",
        antwoord=["fotosynthese", "de fotosynthese"],
        uitleg="Alleen de fotosynthese brengt koolstof uit de lucht het leven in. Alle organische stof in een ecosysteem begint daar.",
    ),
    dict(
        type="waarofniet",
        vraag="Steenkool en aardolie zijn ontstaan uit resten van organismen van lang geleden.",
        antwoord=True,
        uitleg="Die koolstof zat miljoenen jaren opgesloten in de bodem. Door ze te verbranden brengen we haar in korte tijd terug in de lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt het koolstofdioxidegehalte van de lucht?",
        opties=[
            "we verbranden fossiele brandstoffen te snel",
            "planten zijn gestopt met fotosynthese",
            "de oceanen geven al hun koolstof in één keer af",
            "de celademhaling van dieren is sterker geworden",
        ],
        antwoord=0,
        uitleg="De kringloop was in evenwicht tot we fossiele voorraden gingen openen. We voegen koolstof toe aan een kring die ze niet zo snel kwijtraakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bos geeft tijdens zijn groei netto koolstof aan de lucht af.",
        antwoord=False,
        uitleg="Een groeiend bos legt koolstof juist vast: het hout dat erbij komt, is opgeslagen koolstof. Pas bij kappen en verbranden komt die weer vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij de waterkringloop? Kruis alles aan wat juist is.",
        opties=[
            "verdamping uit zeeën, meren en planten",
            "condensatie tot wolken",
            "neerslag als regen of sneeuw",
            "verbranding van water",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verdampen, condenseren en neerslaan zijn de drie stappen. Water verbrandt niet; het is zelf al een eindproduct van verbranding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verdampen van water via de bladeren van planten?",
        antwoord=["transpiratie", "de transpiratie", "verdamping"],
        uitleg="In een bos gaat een groot deel van de neerslag langs de bladeren terug de lucht in. Daarom is een bos belangrijk in de waterkringloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er bij een hevige regen sneller water op een verharde straat dan op een weide?",
        opties=[
            "het water kan niet in de bodem dringen en loopt meteen oppervlakkig weg",
            "er valt op een straat meer regen dan op een weide",
            "verharding laat het water sneller verdampen",
            "een weide houdt helemaal geen water tegen",
        ],
        antwoord=0,
        uitleg="Een bodem met planten neemt water op en geeft het traag door. Beton doet dat niet, en dan komt alles tegelijk in de riool of de beek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kunnen planten het stikstofgas uit de lucht niet rechtstreeks gebruiken?",
        opties=[
            "de binding in het stikstofgasmolecule is te sterk",
            "stikstofgas komt niet in de bodem terecht",
            "planten hebben geen stikstof nodig",
            "stikstofgas lost niet op in water",
        ],
        antwoord=0,
        uitleg="Planten nemen stikstof op als nitraat of ammonium uit de bodem. Het gas uit de lucht moet eerst door bacteriën of door de industrie omgezet worden.",
    ),
    dict(
        type="invultekst",
        vraag="Welke organismen kunnen stikstofgas uit de lucht voor planten bruikbaar maken?",
        antwoord=["bacteriën", "stikstofbindende bacteriën", "bacterien"],
        uitleg="Die bacteriën leven vrij in de bodem of in knolletjes op de wortels van vlinderbloemigen. Zij binden het stikstofgas tot bruikbare stoffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Klaver en bonen kunnen met hulp van bacteriën in hun wortelknolletjes stikstof uit de lucht gebruiken.",
        antwoord=True,
        uitleg="Daarom verrijken die gewassen de bodem. Boeren zaaien ze als groenbedekker tussen twee andere gewassen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is te veel stikstof in de natuur een probleem?",
        opties=[
            "snelgroeiende soorten verdringen de rest",
            "planten kunnen geen stikstof uit de bodem verdragen",
            "stikstof verwarmt de bodem van een natuurgebied te sterk",
            "de reducenten verdwijnen uit een bodem met veel stikstof",
        ],
        antwoord=0,
        uitleg="Brandnetel en gras varen er wel bij, maar heide en veel bloemen niet. Daarom gaat de biodiversiteit achteruit bij overmatige bemesting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is eutrofiëring van een vijver?",
        opties=[
            "overbemesting laat de algen woekeren en de zuurstof instorten",
            "de vijver droogt uit door de hoge temperatuur",
            "de vijver verliest al zijn mineralen door de regen",
            "de vijver wordt zuurder door de neerslag",
        ],
        antwoord=0,
        uitleg="Een algenlaag houdt het licht weg, de waterplanten sterven, de reducenten gebruiken de zuurstof op en dan sterven de vissen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij eutrofiëring sterven vissen door een gebrek aan zuurstofgas in het water.",
        antwoord=True,
        uitleg="De reducenten die de afgestorven algen verwerken, verbruiken daarbij heel veel zuurstof. Voor de vissen blijft er dan te weinig over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen nemen planten als mineraal uit de bodem op? Kruis alles aan wat juist is.",
        opties=[
            "nitraat",
            "fosfaat",
            "kalium",
            "glucose",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat zijn de drie hoofdmineralen in mest. Glucose maakt de plant zelf; die neemt ze niet uit de bodem op.",
    ),
    dict(
        type="waarofniet",
        vraag="De kringloop van fosfor verloopt sneller dan die van koolstof, omdat fosfaat ook een gasvorm heeft.",
        antwoord=False,
        uitleg="Fosfor heeft geen gasvorm. Het zit in gesteente en bodem en komt traag vrij, dus verloopt die kringloop juist veel langzamer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe grijpt de mens in de koolstofkringloop in? Kruis alles aan wat juist is.",
        opties=[
            "door fossiele brandstoffen te verbranden",
            "door bossen te kappen",
            "door veengebieden te draineren",
            "door water te laten verdampen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verbranden, kappen en veen laten oxideren brengen elk koolstof in de lucht. Verdamping van water hoort bij een andere kringloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boer ploegt een stuk oud grasland om tot akker. Wat gebeurt er met de koolstof in de bodem?",
        opties=[
            "een deel oxideert en komt als koolstofdioxide vrij",
            "ze blijft onveranderd in de bodem zitten",
            "ze wordt door het ploegen vastgelegd in de ondergrond",
            "ze verandert in stikstof",
        ],
        antwoord=0,
        uitleg="Ploegen brengt lucht bij de organische stof, en de reducenten gaan dan sneller aan de slag. Een deel van de bodemkoolstof gaat zo de lucht in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een gesloten kringloop op een boerderij gunstig, waarbij mest van het eigen vee op de eigen akkers gaat?",
        opties=[
            "de mineralen blijven op het bedrijf zelf",
            "de gewassen groeien dan zonder enige mineralen",
            "er komen dan helemaal geen reducenten bij te pas",
            "de bodem houdt dan geen water meer vast",
        ],
        antwoord=0,
        uitleg="Wat het vee eet, komt via de mest weer op het land. Dat is dezelfde kringloop als in de natuur, maar met de boer erin.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een ecosysteem?",
        opties=[
            "alle organismen samen met hun omgeving",
            "alle dieren die in een gebied leven",
            "het geheel van alle planten op aarde",
            "een gebied dat door de mens beheerd wordt",
        ],
        antwoord=0,
        uitleg="Een ecosysteem omvat het leven én de bodem, het water, het licht en het klimaat. Juist de wisselwerking tussen die twee maakt het een systeem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren zijn abiotisch? Kruis alles aan wat juist is.",
        opties=[
            "de temperatuur",
            "de zuurtegraad van de bodem",
            "de lichtsterkte",
            "het aantal roofdieren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Abiotisch betekent niet-levend. Roofdieren zijn levend en dus een biotische factor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je alle individuen van één soort die in hetzelfde gebied leven?",
        antwoord=["populatie", "een populatie", "de populatie"],
        uitleg="Een populatie is één soort op één plaats. Alle populaties samen vormen de levensgemeenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de draagkracht van een gebied?",
        opties=[
            "het aantal individuen dat een gebied blijvend kan onderhouden",
            "het gewicht dat de bodem van een gebied kan dragen",
            "het aantal soorten dat ooit in het gebied geleefd heeft",
            "de hoeveelheid energie die de zon er levert",
        ],
        antwoord=0,
        uitleg="Voedsel, water en schuilplaatsen stellen een bovengrens. Boven de draagkracht daalt de populatie weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een populatie die boven de draagkracht van haar gebied uitgroeit, daalt daarna weer.",
        antwoord=True,
        uitleg="Het voedsel raakt op en ziekten slaan toe. Daardoor schommelt een populatie rond de draagkracht heen en weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren bepalen of een populatie groeit of krimpt? Kruis alles aan wat juist is.",
        opties=[
            "het aantal geboorten",
            "het aantal sterfgevallen",
            "het aantal dieren dat het gebied binnenkomt of verlaat",
            "het aantal soorten in de buurt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Geboorte, sterfte en verhuizing samen bepalen de verandering. Het aantal andere soorten speelt daarin geen rechtstreekse rol.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geleidelijk veranderen van een levensgemeenschap, zoals een kale bodem die bos wordt?",
        antwoord=["successie", "de successie"],
        uitleg="Eerst komen pioniers op de kale bodem, dan grassen, dan struiken en ten slotte bomen. Elke stap maakt de volgende mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kunnen pioniersplanten op een kale bodem groeien waar bomen dat niet kunnen?",
        opties=[
            "ze verdragen weinig voeding en veel licht",
            "ze hebben helemaal geen licht nodig om te groeien",
            "ze groeien sneller dan elke andere plant ter wereld",
            "ze hebben geen wortels en dus geen bodem nodig",
        ],
        antwoord=0,
        uitleg="Pioniers zijn taai en bescheiden. Hun afgestorven resten vormen de eerste humus, en pas daarna krijgen veeleisender soorten een kans.",
    ),
    dict(
        type="waarofniet",
        vraag="Een jong ecosysteem is meestal stabieler dan een ecosysteem in een late fase van de successie.",
        antwoord=False,
        uitleg="Het is omgekeerd. In een late fase zijn er meer soorten en meer verbindingen, dus kan een andere soort de rol overnemen van wie wegvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de ecologische niche van een soort?",
        opties=[
            "het geheel van omstandigheden en rollen waarin die soort kan leven",
            "de plaats waar het nest van die soort ligt",
            "het aantal individuen van die soort in een gebied",
            "de soort die er het dichtst bij verwant is",
        ],
        antwoord=0,
        uitleg="De niche is meer dan een adres: het gaat ook over wat de soort eet, wanneer ze actief is en wat ze verdraagt.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee soorten met precies dezelfde niche kunnen in hetzelfde gebied blijvend naast elkaar bestaan.",
        antwoord=False,
        uitleg="Volledige overlap betekent volledige competitie. Een van beide verdwijnt of verschuift haar niche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een indicatorsoort?",
        opties=[
            "een soort waarvan de aanwezigheid iets zegt over de toestand van het milieu",
            "de soort met het grootste aantal individuen in een gebied",
            "de soort die het langst in een gebied leeft",
            "de soort die bovenaan de voedselketen staat",
        ],
        antwoord=0,
        uitleg="Korstmossen verdragen weinig luchtvervuiling en kokerjuffers weinig watervervuiling. Vind je ze, dan is de toestand goed.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de maat voor het beslag dat iemands manier van leven op de aarde legt?",
        antwoord=["ecologische voetafdruk", "voetafdruk", "de ecologische voetafdruk"],
        uitleg="De voetafdruk rekent voeding, wonen, verplaatsen en spullen om naar oppervlakte. Zo wordt zichtbaar of een levenswijze houdbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke keuzes verkleinen de ecologische voetafdruk? Kruis alles aan wat juist is.",
        opties=[
            "minder vlees eten",
            "minder met het vliegtuig reizen",
            "spullen langer gebruiken en herstellen",
            "elk jaar een nieuw toestel kopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voeding, verplaatsing en spullen zijn de grootste posten. Vaak vernieuwen vergroot de afdruk juist.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plantaardig dieet heeft gemiddeld een kleinere voetafdruk dan een dieet met veel vlees.",
        antwoord=True,
        uitleg="Vlees komt een trofisch niveau hoger, dus ging er al veel energie verloren. Daarvoor is meer land en water nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het beperken van de klimaatverandering ook een zaak van biodiversiteit?",
        opties=[
            "soorten kunnen niet altijd meeverhuizen",
            "warmte doodt alle organismen even snel",
            "biodiversiteit hangt enkel van de bodem af",
            "een warmer klimaat geeft overal meer soorten",
        ],
        antwoord=0,
        uitleg="Een soort op een bergtop of in een versnipperd landschap kan niet opschuiven. Daardoor verliest ze haar leefgebied helemaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente wil een beek weer laten kronkelen in plaats van recht door een buis. Welk voordeel heeft dat?",
        opties=[
            "de beek houdt meer water vast en meer leven",
            "het water stroomt sneller naar de rivier toe",
            "er komen minder soorten in en rond de beek",
            "de beek heeft dan geen zuurstof meer nodig",
        ],
        antwoord=0,
        uitleg="Bochten, ondiepe oevers en overstroombare weides geven leven een plaats en houden water op bij hevige regen. Een rechte buis doet het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een natuurbeheerder die een heide wil behouden, moet er soms bomen weghalen.",
        antwoord=True,
        uitleg="Zonder ingrijpen zet de successie door en wordt de heide bos. Beheer houdt het systeem dus met opzet in een vroegere fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker wil weten of een beek vervuild is. Wat is de verstandigste aanpak?",
        opties=[
            "de waterdiertjes bepalen en vergelijken",
            "de kleur van het water van de oever af beoordelen",
            "het aantal vissen in de beek schatten",
            "de temperatuur van het water één keer meten",
        ],
        antwoord=0,
        uitleg="Indicatorsoorten vertellen over de toestand van de maanden ervoor, niet enkel over het ogenblik van de meting. Daarom is dat betrouwbaarder.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gebied verdwijnen de bijen. Welk gevolg verwacht je in de jaren erna?",
        opties=[
            "planten die insecten nodig hebben, nemen af",
            "alle planten in het gebied verdwijnen onmiddellijk",
            "er verandert niets, want planten kunnen zich zelf bestuiven",
            "de bomen gaan over op bestuiving door zoogdieren",
        ],
        antwoord=0,
        uitleg="Niet alle planten hangen van insecten af, maar heel veel wel. Zonder bestuivers dalen hun zaadzetting en daarna hun aantal.",
    ),
]
