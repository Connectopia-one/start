# -*- coding: utf-8 -*-
"""De vragen voor "Democratie en dictatuur" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik leef in een democratische
rechtsstaat" (15 % van het examen), eerste helft: de principes van de
democratische rechtsstaat, het verschil met een autoritair regime, en je eigen
verantwoordelijkheid daarin.

Deel 1 gaat over de zeven principes en over de scheiding van de machten.
Deel 2 gaat over democratie tegenover dictatuur, en over inspraak, rechten en
plichten. De tweede helft van dit onderdeel, de bestuursniveaus van België,
staat in [[se_belgie]].

De fiche vraagt uitdrukkelijk dat je kan *beoordelen* of een principe
gerespecteerd wordt in een gegeven situatie. Daarom staan er hier zoveel
vragen die met een situatie beginnen in plaats van met een definitie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent democratie, letterlijk?",
        opties=[
            "Het volk regeert",
            "De koning regeert over het volk",
            "De rijkste mensen regeren mee",
            "De oudste inwoners nemen de beslissingen",
        ],
        antwoord=0,
        uitleg="Democratie komt uit het Grieks: demos is volk en kratos is macht. In een democratie ligt de macht dus bij de bevolking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de principes van een democratische rechtsstaat?",
        opties=[
            "Stemrecht en vrije verkiezingen",
            "Scheiding van de machten",
            "Vrije meningsuiting en persvrijheid",
            "Eén partij die alle zetels krijgt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt stemrecht, vrije verkiezingen, scheiding van de machten, individuele vrijheid, een grondwet, vrije meningsuiting en persvrijheid, en gelijkheid voor de wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een grondwet?",
        opties=[
            "De hoogste wet, waar alle andere wetten zich aan moeten houden",
            "De wet die bepaalt wie welke grond in het land in bezit heeft",
            "De eerste wet die een nieuwe regering laat stemmen",
            "Een wet die om de vijf jaar volledig vervangen wordt",
        ],
        antwoord=0,
        uitleg="De grondwet staat boven alle andere wetten. Ze legt de basisregels van het land vast en beschermt de rechten van iedereen die er woont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie machten onderscheidt men in een rechtsstaat?",
        opties=[
            "De wetgevende, de uitvoerende en de rechterlijke macht",
            "De koninklijke, de kerkelijke en de militaire macht",
            "De federale, de regionale en de lokale macht",
            "De politieke, de economische en de sociale macht",
        ],
        antwoord=0,
        uitleg="De wetgevende macht maakt de wetten, de uitvoerende macht voert ze uit, en de rechterlijke macht spreekt recht als er een conflict is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de wetgevende macht?",
        opties=[
            "Ze maakt en stemt de wetten",
            "Ze voert de wetten in de praktijk uit",
            "Ze spreekt recht in een conflict",
            "Ze houdt toezicht op de politie",
        ],
        antwoord=0,
        uitleg="De wetgevende macht is het parlement. Daar worden wetten voorgesteld, besproken en gestemd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de uitvoerende macht?",
        opties=[
            "Ze zorgt ervoor dat de wetten in de praktijk gebracht worden",
            "Ze brengt nieuwe wetsvoorstellen in het parlement ter stemming",
            "Ze beslist welke straf iemand krijgt na een proces",
            "Ze schrijft de grondwet van het land",
        ],
        antwoord=0,
        uitleg="De uitvoerende macht is de regering. Zij voert uit wat het parlement beslist heeft en stuurt de administratie aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie oefent de rechterlijke macht uit?",
        opties=[
            "De rechters in de rechtbanken en de hoven",
            "De ministers van de regering",
            "De volksvertegenwoordigers in het parlement",
            "De burgemeester van elke gemeente",
        ],
        antwoord=0,
        uitleg="De rechterlijke macht ligt bij de rechters. Zij passen de wet toe op een concreet geval en oordelen onafhankelijk van de regering.",
    ),
    dict(
        type="waarofniet",
        vraag="Het is de bedoeling dat dezelfde persoon alle drie de machten tegelijk in handen heeft.",
        antwoord=False,
        uitleg="Juist niet. Ze zijn gescheiden zodat ze elkaar kunnen controleren. Alle macht bij één persoon is precies wat een dictatuur kenmerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn de drie machten van elkaar gescheiden?",
        opties=[
            "Zodat ze elkaar kunnen controleren en niemand alle macht krijgt",
            "Zodat het werk over meer mensen verdeeld raakt en sneller gaat",
            "Zodat elke provincie zijn eigen macht kan uitoefenen",
            "Zodat de koning er niet meer bij betrokken hoeft te zijn",
        ],
        antwoord=0,
        uitleg="Een macht die zichzelf controleert, controleert niets. Door ze te scheiden houden ze elkaar in evenwicht. Dat heet de scheiding der machten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent vrije verkiezingen?",
        opties=[
            "Iedereen stemt zonder dwang en in het geheim",
            "Je hoeft niet te gaan stemmen als je geen zin hebt",
            "De verkiezingen kosten de kiezer geen geld",
            "Er is maar één partij waar je op kan stemmen",
        ],
        antwoord=0,
        uitleg="Vrij wil zeggen: niemand dwingt je voor wie je kiest, en niemand kan zien wat je stemt. Daarom bestaat het stemhokje.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor het federale parlement moet je in België gaan stemmen, ook al kies je zelf op wie.",
        antwoord=True,
        uitleg="Klopt, dat is de stemplicht. Ze geldt voor de federale, de Vlaamse en de Europese verkiezingen; voor de gemeenteraad in Vlaanderen niet meer sinds 2024. Wat je op je stembiljet zet, blijft altijd aan jou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent gelijkheid voor de wet?",
        opties=[
            "Dezelfde wet geldt voor iedereen, ook voor wie macht of geld heeft",
            "Iedereen krijgt van de staat elk jaar precies evenveel geld uitbetaald",
            "Iedereen moet dezelfde job en hetzelfde loon krijgen",
            "Iedereen moet dezelfde mening hebben over de wet",
        ],
        antwoord=0,
        uitleg="Gelijkheid voor de wet betekent dat niemand boven de wet staat. Een minister die te snel rijdt, krijgt dezelfde boete als iedereen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is persvrijheid?",
        opties=[
            "Journalisten mogen berichten zonder dat de overheid dat verbiedt",
            "Kranten en nieuwssites zijn voor iedereen gratis te lezen",
            "Iedereen mag zelf een krant beginnen zonder ervoor te betalen",
            "De overheid schrijft zelf mee aan het nieuws van de dag",
        ],
        antwoord=0,
        uitleg="Persvrijheid is dat de media vrij kunnen berichten, ook over de regering. Dat is net hoe de bevolking kan controleren wat er gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een journalist schrijft een kritisch artikel over een minister en wordt daarvoor opgepakt. Welk principe wordt hier geschonden?",
        opties=[
            "De persvrijheid",
            "Het stemrecht van de bevolking",
            "De aanwezigheid van een grondwet",
            "De scheiding tussen gemeente en provincie",
        ],
        antwoord=0,
        uitleg="Kritiek op de macht is precies wat persvrijheid beschermt. Wie daarvoor opgepakt wordt, leeft niet meer in een vrije pers.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land mag maar één partij deelnemen aan de verkiezingen. Welke principes worden hier geschonden?",
        opties=[
            "De vrije verkiezingen",
            "Het stemrecht wordt zinloos gemaakt",
            "De individuele vrijheid om te kiezen",
            "De gelijkheid voor de wet in strafzaken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Als er maar één keuze is, zijn de verkiezingen niet vrij, betekent je stem niets meer en heb je geen keuzevrijheid. Met strafrecht heeft dit niets te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Je individuele vrijheid loopt tot waar de vrijheid van iemand anders begint.",
        antwoord=True,
        uitleg="Klopt. Vrijheid is geen vrijgeleide: de wet zet de grenzen, en die wet geldt voor iedereen gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechter spreekt een vriend van de eerste minister vrij, enkel omdat hij een vriend van de eerste minister is. Wat loopt hier mis?",
        opties=[
            "De gelijkheid voor de wet",
            "De persvrijheid in het land",
            "Het recht om te gaan stemmen",
            "De vrijheid van meningsuiting",
        ],
        antwoord=0,
        uitleg="Wie je kent zou geen rol mogen spelen. Dat er met twee maten gemeten wordt, breekt de gelijkheid voor de wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een regering beslist dat rechters voortaan door haar benoemd en ontslagen worden. Welk principe komt in gevaar?",
        opties=[
            "De scheiding van de machten",
            "Het stemrecht van de bevolking",
            "De persvrijheid van journalisten",
            "De vrijheid van vereniging",
        ],
        antwoord=0,
        uitleg="Rechters die door de regering ontslagen kunnen worden, durven die regering niet meer tegen te spreken. Dan is de rechterlijke macht niet meer onafhankelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Vrije meningsuiting betekent dat je alles mag zeggen, ook oproepen tot geweld tegen een groep.",
        antwoord=False,
        uitleg="Vrije meningsuiting heeft grenzen: aanzetten tot haat of geweld is strafbaar. Je mag kritiek geven, je mag niet oproepen om iemand iets aan te doen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de hoogste wet van een land, waar alle andere wetten zich aan moeten houden?",
        antwoord=["de grondwet", "grondwet"],
        uitleg="De grondwet legt de basisregels vast en beschermt de rechten van iedereen. Geen enkele gewone wet mag ertegen ingaan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een autoritair regime?",
        opties=[
            "Een bestuur waarin één persoon of groep alle macht heeft",
            "Een bestuur waarin de bevolking om de vijf jaar kiest",
            "Een bestuur waarin de rechters alles beslissen",
            "Een bestuur waarin elke gemeente apart beslist",
        ],
        antwoord=0,
        uitleg="Bij een autoritair regime ligt de macht bij één persoon of één groep, en is er geen echte controle van buitenaf. Een dictatuur is daar een voorbeeld van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je in een dictatuur dat je in een democratie niet ziet?",
        opties=[
            "Verkiezingen waarvan de uitslag op voorhand vastligt",
            "Journalisten die opgepakt worden om wat ze schrijven",
            "Rechters die doen wat de leider hun opdraagt",
            "Een parlement dat over nieuwe wetten stemt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Schijnverkiezingen, opgepakte journalisten en rechters zonder eigen oordeel zijn kenmerken van een dictatuur. Een parlement dat stemt hoort bij een democratie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een dictatuur worden er soms verkiezingen gehouden.",
        antwoord=True,
        uitleg="Klopt, maar dan zijn ze niet vrij: er is maar één partij, of de uitslag ligt op voorhand vast. De vorm is er, de inhoud niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land verdwijnt de grondwet, worden rechters door de leider benoemd en mag er maar één krant verschijnen. Wat is dat land geworden?",
        opties=[
            "Een autoritair regime",
            "Een democratische rechtsstaat",
            "Een land met scheiding van de machten",
            "Een land met volledige persvrijheid",
        ],
        antwoord=0,
        uitleg="Drie principes tegelijk verdwenen: de grondwet, de onafhankelijke rechters en de vrije pers. Dan is er van een rechtsstaat niets meer over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het om inspraak te hebben?",
        opties=[
            "Je mening telt mee in een beslissing die ook over jou gaat",
            "Je beslist helemaal in je eentje wat er verder gaat gebeuren",
            "Je mag toekijken terwijl anderen beslissen",
            "Je moet altijd akkoord gaan met de meerderheid",
        ],
        antwoord=0,
        uitleg="Inspraak is dat je gehoord wordt en dat je mening meeweegt. Het is niet hetzelfde als altijd je zin krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke van deze situaties heb je inspraak?",
        opties=[
            "De leerlingenraad vraagt wat er op de speelplaats moet komen",
            "Je gezin bespreekt samen waar jullie op vakantie gaan",
            "Je sportclub laat de leden stemmen over nieuwe trainingsuren",
            "De bus rijdt volgens een uurrooster dat al jaren vastligt",
        ],
        antwoord=[0, 1, 2],
        uitleg="In de eerste drie wordt je mening gevraagd voor er beslist wordt. Bij het busuurrooster gebeurt dat niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Inspraak betekent dat jouw voorstel altijd wordt uitgevoerd.",
        antwoord=False,
        uitleg="Je wordt gehoord, maar er zijn ook andere meningen. Inspraak gaat over meepraten, niet over altijd gelijk krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn rechten die je in België hebt?",
        opties=[
            "Het recht op onderwijs",
            "Het recht om je mening te uiten",
            "Het recht op een eerlijk proces",
            "Het recht om nooit belastingen te betalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onderwijs, meningsuiting en een eerlijk proces zijn rechten. Belastingen betalen is net een plicht, en daarmee wordt onder meer dat onderwijs betaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een plicht in België?",
        opties=[
            "Naar school gaan tot je achttien bent",
            "Lid worden van een jeugdbeweging",
            "Elke zondag gaan sporten",
            "Een krant kopen bij elke verkiezing",
        ],
        antwoord=0,
        uitleg="De leerplicht loopt tot achttien jaar. De andere drie zijn vrije keuzes, geen verplichtingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Rechten en plichten horen bij elkaar: waar de een stopt, begint vaak de ander.",
        antwoord=True,
        uitleg="Klopt. Jij hebt het recht om je mening te zeggen, en tegelijk de plicht om anderen die van hen te laten zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk dat mensen gaan stemmen?",
        opties=[
            "Omdat de samenstelling van het parlement er rechtstreeks van afhangt",
            "Omdat je anders je identiteitskaart op het gemeentehuis moet inleveren",
            "Omdat je stem bepaalt wie er rechter wordt",
            "Omdat je dan een lagere belasting betaalt",
        ],
        antwoord=0,
        uitleg="Wie in het parlement zit, beslist mee over de wetten. Wie niet stemt, laat die keuze aan anderen over.",
    ),
    dict(
        type="waarofniet",
        vraag="In België worden rechters verkozen door de bevolking.",
        antwoord=False,
        uitleg="Rechters worden benoemd, niet verkozen, juist om hen onafhankelijk te houden van de politiek en van de waan van de dag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school laat de leerlingen stemmen over het thema van het schoolfeest, maar de directie kiest achteraf zelf iets anders zonder uitleg. Wat klopt hier niet?",
        opties=[
            "De inspraak was maar schijn, want de uitslag telde niet mee",
            "De leerlingen hadden helemaal geen recht om daarover te stemmen",
            "De directie mag zelf nooit iets beslissen",
            "Een schoolfeest hoort niet bij inspraak",
        ],
        antwoord=0,
        uitleg="Als je mening gevraagd wordt en er daarna niets mee gebeurt, was het geen echte inspraak. Uitleg geven bij een andere keuze hoort er wel bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is vrije meningsuiting belangrijk voor een democratie?",
        opties=[
            "Omdat je alleen kan kiezen als je vrij kan horen en zeggen wat er speelt",
            "Omdat de regering dan precies weet welke mensen het niet met haar eens zijn",
            "Omdat er dan minder wetten nodig zijn in een land",
            "Omdat de verkiezingen er sneller door verlopen",
        ],
        antwoord=0,
        uitleg="Een keuze maken kan pas als je de argumenten kent. Wie niets mag zeggen en niets mag horen, kan niet echt kiezen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechtsstaat betekent dat ook de overheid zelf zich aan de wet moet houden.",
        antwoord=True,
        uitleg="Klopt, dat is net het punt. In een rechtsstaat staat niemand boven de wet, ook de regering en het parlement niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je als jongere doen om mee te wegen op beslissingen, ook al mag je nog niet stemmen?",
        opties=[
            "Je kandidaat stellen voor de leerlingenraad",
            "Meedoen aan een jeugdraad in je gemeente",
            "Je mening geven op een inspraakmoment",
            "Wachten tot je achttien bent en tot dan niets doen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Leerlingenraad, jeugdraad en inspraakmomenten staan wel open voor jongeren. Alleen wachten is de enige manier waarop je zeker niets verandert.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we een bestuur waarin één persoon of groep alle macht heeft en er geen vrije verkiezingen zijn?",
        antwoord=["een dictatuur", "dictatuur"],
        uitleg="Een dictatuur is een vorm van autoritair regime. De macht ligt bij één persoon of groep en wordt niet gecontroleerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land mogen mensen wel stemmen, maar de regering laat vooraf bepalen wie zich kandidaat mag stellen. Wat is er aan de hand?",
        opties=[
            "De verkiezingen zijn niet echt vrij",
            "Er is geen grondwet meer in dat land",
            "De rechterlijke macht is er afgeschaft",
            "De bevolking heeft er geen stemplicht",
        ],
        antwoord=0,
        uitleg="Kiezen uit een lijst die de macht zelf heeft samengesteld, is geen vrije keuze. De vorm van de verkiezing zegt dus niet alles.",
    ),
    dict(
        type="waarofniet",
        vraag="Betogen mag in een democratie, zolang je geen kritiek geeft op de regering.",
        antwoord=False,
        uitleg="Kritiek op de regering is net waar het betogingsrecht voor bestaat. Vreedzaam betogen tegen een beslissing mag altijd; alleen geweld mag niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grootste verschil tussen een democratie en een autoritair regime?",
        opties=[
            "In een democratie wordt de macht gecontroleerd en kan ze wisselen",
            "In een democratie zijn er meer inwoners dan in een dictatuur",
            "In een democratie bestaan er geen wetten die je moet volgen",
            "In een democratie is er geen leger en in een dictatuur wel",
        ],
        antwoord=0,
        uitleg="Het draait om controle en wissel: verkiezingen, gescheiden machten en een vrije pers zorgen ervoor dat niemand de macht voorgoed houdt.",
    ),
]
