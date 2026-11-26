# -*- coding: utf-8 -*-
"""Humane wetenschappen: politiek, democratie en de rechtstaat.

Het eerste van zes thema's over politieke wetenschappen. Die staan enkel in de
fiche `2027_Sociale en gedragswetenschappen_3DDO` (humane wetenschappen), niet
in de fiche 3DDG (welzijnswetenschappen). Kim, 26 november 2026, na een mail
van een ouder: humane wetenschappen moet het politieke deel erbij krijgen.
De titels beginnen met "Humane wetenschappen:", zodat de wegwijzer ze kan
verbergen voor wie welzijnswetenschappen kiest (inhoud/vaknoten.ts).

De lijstjes staan letterlijk in de fiche (onderdeel "Politiek en democratie"):

    staats- en regeringsvormen: democratie, dictatuur, monarchie, oligarchie,
        republiek, theocratie
    soorten democratie: directe of rechtstreekse democratie, indirecte of
        representatieve democratie
    principes van een democratische rechtstaat: een constitutie of grondwet,
        fundamentele rechten en vrijheden, meerderheidsprincipe,
        onafhankelijke en onpartijdige rechtspraak, scheiding der machten
    de drie machten: wetgevende macht (parlementen), uitvoerende macht
        (regeringen), rechterlijke macht (hoven en rechtbanken)
    analyseren: staatsvormen toetsen aan de principes van de rechtstaat, het
        belang van de scheiding der machten, controle en evenwicht tussen de
        drie machten, onafhankelijkheid en onpartijdigheid van de rechterlijke
        macht, schendingen van de scheiding der machten

Deel 1 zijn de staats- en regeringsvormen en de soorten democratie.
Deel 2 zijn de democratische rechtstaat en de scheiding der machten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn staats- en regeringsvormen?",
        opties=[
            "de monarchie",
            "de oligarchie",
            "de theocratie",
            "de federatie van vakbonden",
            "de republiek",
            "de vrije markt",
        ],
        antwoord=[0, 1, 2, 4],
        uitleg="Monarchie, oligarchie, theocratie en republiek zijn vormen van bestuur, net als democratie en dictatuur. Een vakbondsfederatie is een organisatie en de vrije markt is een economisch begrip.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een democratie?",
        opties=[
            "een bestuursvorm waarin de macht bij het volk ligt",
            "een bestuursvorm waarin een kleine groep alle macht heeft",
            "een bestuursvorm waarin een vorst de macht erft van zijn ouders",
            "een bestuursvorm waarin geestelijken de wetten maken",
        ],
        antwoord=0,
        uitleg="Demos is volk en kratos is macht. In een democratie beslist het volk, rechtstreeks of via gekozen vertegenwoordigers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een dictatuur?",
        opties=[
            "één persoon of partij heeft alle macht, zonder vrije verkiezingen",
            "het staatshoofd wordt om de vier jaar door het volk verkozen",
            "de burgers stemmen zelf over elke nieuwe wet",
            "de macht is verdeeld over drie aparte, gelijke machten",
        ],
        antwoord=0,
        uitleg="Een dictator of één partij heeft de macht zonder dat het volk die vrij kan geven of afnemen. Tegenstemmen of oppositie wordt vaak onderdrukt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een monarchie?",
        opties=[
            "het staatshoofd is een vorst die zijn plaats meestal erft",
            "het staatshoofd is een president die verkozen wordt",
            "het land heeft geen staatshoofd en geen regering",
            "het staatshoofd is altijd de hoogste geestelijke van het land",
        ],
        antwoord=0,
        uitleg="Een koning, koningin of vorst staat aan het hoofd van de staat en erft die plaats meestal. België is een monarchie met een koning als staatshoofd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een republiek?",
        opties=[
            "het staatshoofd erft zijn plaats niet, maar wordt aangeduid of verkozen",
            "het staatshoofd is een vorst die zijn ambt van zijn ouders erft",
            "het land wordt bestuurd vanuit de regels van een godsdienst",
            "de macht ligt bij enkele rijke families die alles beslissen",
        ],
        antwoord=0,
        uitleg="In een republiek is het staatshoofd meestal een president, die voor een bepaalde tijd verkozen of aangeduid wordt. Frankrijk en Duitsland zijn republieken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een oligarchie?",
        opties=[
            "een kleine groep mensen heeft de macht in handen",
            "één vorst heeft de macht en geeft ze door aan zijn kind",
            "alle volwassen burgers beslissen samen over elke wet",
            "de macht ligt bij religieuze leiders en hun heilige teksten",
        ],
        antwoord=0,
        uitleg="Oligos betekent weinig. In een oligarchie bestuurt een kleine groep, bijvoorbeeld rijke families, legerleiders of een partijtop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een theocratie?",
        opties=[
            "het land wordt bestuurd in naam van een god, vaak door geestelijken",
            "het land wordt bestuurd door gekozen politici zonder godsdienst",
            "het land wordt bestuurd door een kleine groep rijke handelaars",
            "het land wordt bestuurd door een president en een parlement",
        ],
        antwoord=0,
        uitleg="Theos betekent god. In een theocratie komen de wetten uit een godsdienst, en religieuze leiders hebben veel of alle macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het land Eldoria beslist de raad van de hogepriesters over alle wetten. Volgens hen komen die wetten rechtstreeks uit het heilige boek. Welke staats- of regeringsvorm is dit?",
        opties=["een theocratie", "een oligarchie", "een republiek", "een directe democratie"],
        antwoord=0,
        uitleg="De macht wordt uitgeoefend in naam van een god en de wetten komen uit een godsdienst. Dat is een theocratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In Verdania kiezen de burgers om de vijf jaar een president. Die kan maar één keer herkozen worden. Welke vorm herken je zeker?",
        opties=["een republiek", "een monarchie", "een theocratie", "een oligarchie"],
        antwoord=0,
        uitleg="Het staatshoofd is een verkozen president en geen vorst. Dat is een republiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="In Morvalië hebben vijf rijke families samen de touwtjes in handen. Zij duiden de ministers aan en er zijn geen verkiezingen. Welke vorm is dit?",
        opties=["een oligarchie", "een monarchie", "een directe democratie", "een theocratie"],
        antwoord=0,
        uitleg="Een kleine groep heeft alle macht. Dat is een oligarchie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een directe en een indirecte democratie?",
        opties=[
            "in een directe democratie beslissen de burgers zelf, in een indirecte kiezen ze vertegenwoordigers",
            "in een directe democratie beslist de koning, in een indirecte beslist het parlement",
            "in een directe democratie mag iedereen stemmen, in een indirecte alleen wie belastingen betaalt",
            "in een directe democratie zijn er partijen, in een indirecte democratie zijn er geen partijen",
        ],
        antwoord=0,
        uitleg="Bij een directe of rechtstreekse democratie stemt het volk zelf over de beslissingen. Bij een indirecte of representatieve democratie kiest het volk mensen die in zijn naam beslissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klein Zwitsers kanton komen de inwoners één keer per jaar samen op het plein. Daar stemmen ze met opgestoken hand over de wetten en de begroting. Welke soort democratie is dit?",
        opties=[
            "een directe of rechtstreekse democratie",
            "een indirecte of representatieve democratie",
            "geen democratie maar een oligarchie",
            "geen democratie maar een monarchie",
        ],
        antwoord=0,
        uitleg="De inwoners beslissen zelf, zonder vertegenwoordigers tussen hen en de beslissing. Dat is directe democratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij de verkiezingen kiest Yasmina een volksvertegenwoordiger. Die stemt de volgende jaren in het parlement over nieuwe wetten. Welke soort democratie is dit?",
        opties=[
            "een indirecte of representatieve democratie",
            "een directe of rechtstreekse democratie",
            "een theocratie met verkiezingen",
            "een oligarchie met verkiezingen",
        ],
        antwoord=0,
        uitleg="Yasmina beslist niet zelf over de wetten, maar kiest iemand die dat in haar naam doet. Dat is representatieve democratie, zoals in België.",
    ),
    dict(
        type="invultekst",
        vraag="Een democratie waarin burgers vertegenwoordigers kiezen die namens hen beslissen, heet een indirecte of ... democratie.",
        antwoord=["representatieve"],
        uitleg="Representeren betekent vertegenwoordigen. De gekozen politici vertegenwoordigen de kiezers.",
    ),
    dict(
        type="invultekst",
        vraag="Een staatsvorm waarin een kleine groep alle macht heeft, heet een ...",
        antwoord=["oligarchie"],
        uitleg="Oligarchie komt van oligos, weinig, en archein, heersen: de heerschappij van enkelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land kan tegelijk een monarchie en een democratie zijn.",
        antwoord=True,
        uitleg="België heeft een koning als staatshoofd, maar het volk kiest het parlement en de koning heeft geen eigen politieke macht. Het is dus een monarchie én een democratie.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke republiek is ook een democratie.",
        antwoord=False,
        uitleg="Ook een dictatuur kan zich republiek noemen, met een president die niet vrij verkozen is. Republiek zegt iets over het staatshoofd, niet over de vrijheid van de burgers.",
    ),
    dict(
        type="waarofniet",
        vraag="In een directe democratie stemmen de burgers zelf over beslissingen, zonder vertegenwoordigers.",
        antwoord=True,
        uitleg="Dat is precies het kenmerk van een rechtstreekse democratie, zoals bij een volksraadpleging of een volksvergadering.",
    ),
    dict(
        type="waarofniet",
        vraag="In een theocratie ligt de macht bij een kleine groep rijke handelaars.",
        antwoord=False,
        uitleg="Een kleine groep rijken met de macht is een oligarchie. In een theocratie wordt geregeerd in naam van een god.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken grote landen bijna altijd een indirecte democratie?",
        opties=[
            "met miljoenen burgers is het niet haalbaar dat iedereen over elke wet stemt",
            "een indirecte democratie is de enige vorm die een grondwet kan hebben",
            "in een directe democratie mogen vrouwen en jongeren niet meestemmen",
            "een indirecte democratie heeft helemaal geen verkiezingen nodig",
        ],
        antwoord=0,
        uitleg="Over elke wet met miljoenen mensen samen beslissen is praktisch onmogelijk. Daarom kiezen burgers vertegenwoordigers, en wordt een rechtstreekse stemming zoals een referendum enkel af en toe gebruikt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een democratische rechtstaat?",
        opties=[
            "een democratie waarin ook de overheid zich aan de wet moet houden",
            "een staat waarin de rechters ook de wetten schrijven en uitvoeren",
            "een staat waarin de meerderheid alles mag beslissen, ook over minderheden",
            "een staat waarin de regering boven de wet staat als het nodig is",
        ],
        antwoord=0,
        uitleg="In een rechtstaat staat niemand boven de wet, ook de regering niet. Het volk kiest zijn bestuur, en de grondrechten van iedereen worden beschermd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn principes van een democratische rechtstaat?",
        opties=[
            "een grondwet of constitutie",
            "fundamentele rechten en vrijheden",
            "het meerderheidsprincipe",
            "één partij die alle macht krijgt",
            "de scheiding der machten",
            "rechters die de regering aanduidt en ontslaat",
        ],
        antwoord=[0, 1, 2, 4],
        uitleg="Grondwet, grondrechten, meerderheidsprincipe, scheiding der machten en onafhankelijke, onpartijdige rechtspraak zijn de principes. Eén partij met alle macht of rechters die van de regering afhangen, passen daar niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de grondwet of constitutie?",
        opties=[
            "de hoogste wet, met de grondrechten en de regels over hoe de staat werkt",
            "een lijst van alle straffen die een rechter mag opleggen",
            "het programma waarmee een partij de verkiezingen wil winnen",
            "het jaarlijkse plan van de regering met alle uitgaven",
        ],
        antwoord=0,
        uitleg="Alle andere wetten moeten met de grondwet in overeenstemming zijn. Ze legt de grondrechten vast en regelt hoe de machten werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt het meerderheidsprincipe in?",
        opties=[
            "een voorstel dat de meeste stemmen haalt, wordt aangenomen",
            "de grootste partij mag de grondrechten van anderen afschaffen",
            "de oudste parlementsleden beslissen in naam van de meerderheid",
            "een wet is pas geldig als echt iedereen ervoor stemt",
        ],
        antwoord=0,
        uitleg="In een democratie beslist de meerderheid. In een rechtstaat mag ze daarbij wel de grondrechten van de minderheid niet schenden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de scheiding der machten?",
        opties=[
            "de wetgevende, uitvoerende en rechterlijke macht liggen bij verschillende instellingen",
            "het land wordt opgedeeld in deelstaten die elk een eigen regering hebben",
            "de macht wordt elke vier jaar doorgegeven van de ene naar de andere partij",
            "de kerk en de staat mogen zich niet met elkaars zaken bemoeien",
        ],
        antwoord=0,
        uitleg="Wie wetten maakt, wie ze uitvoert en wie erover oordeelt, zijn drie verschillende instellingen. Zo kan geen enkele macht alles alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instelling hoort bij de wetgevende macht?",
        opties=["het parlement", "de regering", "het hof van beroep", "de politierechtbank"],
        antwoord=0,
        uitleg="Parlementen maken wetten. De regering voert ze uit en de hoven en rechtbanken spreken recht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instelling hoort bij de uitvoerende macht?",
        opties=["de regering", "het parlement", "de rechtbank van eerste aanleg", "het hof van beroep"],
        antwoord=0,
        uitleg="De regering met haar ministers voert de wetten uit en bestuurt het land elke dag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instellingen horen bij de rechterlijke macht?",
        opties=[
            "de hoven en rechtbanken",
            "de ministers en hun kabinetten",
            "de parlementsleden en hun partijen",
            "de burgemeesters en hun schepenen",
        ],
        antwoord=0,
        uitleg="Hoven en rechtbanken passen de wet toe op concrete zaken en spreken een oordeel uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het parlement keurt een nieuwe wet goed die het roken in auto's met kinderen verbiedt. Welke macht is hier aan het werk?",
        opties=["de wetgevende macht", "de uitvoerende macht", "de rechterlijke macht", "de vierde macht"],
        antwoord=0,
        uitleg="Een wet maken en goedkeuren is de taak van het parlement, de wetgevende macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechter beslist dat een bestuurder die met een kind in de auto rookte, een boete moet betalen. Welke macht is hier aan het werk?",
        opties=["de rechterlijke macht", "de wetgevende macht", "de uitvoerende macht", "de controlerende macht"],
        antwoord=0,
        uitleg="Een rechter past de wet toe op een concreet geval en spreekt een oordeel uit. Dat is de rechterlijke macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="De minister van Volksgezondheid laat een campagne maken en regelt de controles op het nieuwe rookverbod. Welke macht is hier aan het werk?",
        opties=["de uitvoerende macht", "de wetgevende macht", "de rechterlijke macht", "de grondwetgevende macht"],
        antwoord=0,
        uitleg="Een minister zorgt ervoor dat de wet in de praktijk wordt toegepast. Dat is de uitvoerende macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de scheiding der machten belangrijk voor een democratische samenleving?",
        opties=[
            "de machten controleren elkaar, zodat niemand zijn macht kan misbruiken",
            "zo moeten er minder verkiezingen georganiseerd worden in het land",
            "zo kan de regering sneller beslissen zonder het parlement te vragen",
            "zo hoeft het parlement zich niet meer aan de grondwet te houden",
        ],
        antwoord=0,
        uitleg="Wie alle macht heeft, kan die misbruiken. Door de macht te verdelen, houden de drie machten elkaar in evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld toont dat de machten elkaar controleren?",
        opties=[
            "het parlement stelt vragen aan een minister en kan de regering wegstemmen",
            "de minister beslist zelf welke rechter een zaak tegen hem behandelt",
            "de regering schrijft een wet en keurt die meteen zelf goed",
            "een rechter wordt ontslagen omdat de regering zijn vonnis niet goed vindt",
        ],
        antwoord=0,
        uitleg="Het parlement controleert de regering. Bij de andere voorbeelden neemt één macht net het werk of de vrijheid van een andere macht af.",
    ),
    dict(
        type="meerkeuze",
        vraag="In Kastelland ontslaat de president drie rechters van het hoogste hof, omdat ze tegen zijn nieuwe wet beslisten. Welk principe van de rechtstaat wordt hier vooral geschonden?",
        opties=[
            "de onafhankelijkheid van de rechterlijke macht",
            "het meerderheidsprincipe bij de verkiezingen",
            "het recht van burgers om een partij op te richten",
            "de indirecte of representatieve democratie",
        ],
        antwoord=0,
        uitleg="Rechters moeten kunnen oordelen zonder druk van de regering. Wie rechters ontslaat omdat hun oordeel niet bevalt, schendt de onafhankelijkheid van de rechterlijke macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een rechter onpartijdig is?",
        opties=[
            "hij kiest geen kant en behandelt beide partijen gelijk",
            "hij is lid van geen enkele partij in het parlement",
            "hij volgt altijd wat de regering in die zaak vraagt",
            "hij beslist elke zaak alleen, zonder andere rechters",
        ],
        antwoord=0,
        uitleg="Onpartijdig betekent zonder vooroordeel en zonder belang in de zaak. Onafhankelijk betekent dat hij niet onder druk staat van een andere macht.",
    ),
    dict(
        type="invultekst",
        vraag="De macht die de wetten maakt en goedkeurt, heet de ... macht.",
        antwoord=["wetgevende"],
        uitleg="De wetgevende macht ligt bij de parlementen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een democratische rechtstaat mag de meerderheid ook de grondrechten van een minderheid afschaffen.",
        antwoord=False,
        uitleg="Het meerderheidsprincipe geldt binnen de grenzen van de grondwet. De fundamentele rechten en vrijheden beschermen net ook wie in de minderheid is.",
    ),
    dict(
        type="waarofniet",
        vraag="In een rechtstaat moet ook de regering zich aan de wetten houden.",
        antwoord=True,
        uitleg="Niemand staat boven de wet. Een burger kan zelfs naar de rechter stappen tegen een beslissing van de overheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De regering is de instelling die de wetten maakt en goedkeurt.",
        antwoord=False,
        uitleg="De regering voert de wetten uit. Het parlement maakt en keurt ze goed.",
    ),
    dict(
        type="waarofniet",
        vraag="Een staat met verkiezingen, maar waar de president zelf de rechters kiest en ontslaat, voldoet niet aan alle principes van een democratische rechtstaat.",
        antwoord=True,
        uitleg="Verkiezingen alleen zijn niet genoeg. Zonder onafhankelijke rechtspraak en scheiding der machten is het geen volwaardige rechtstaat.",
    ),
]
