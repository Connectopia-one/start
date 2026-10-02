# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Bevruchting en de ontwikkeling van embryo en foetus.

Biologie, de kop "Voortplanting bij de mens" met haar onderkop "Ontwikkeling
van embryo en foetus" uit de vakfiche natuurwetenschappen 3DU. Deel 1 gaat over
de hormonen van de menstruele cyclus, de bouw van de eicel en de zaadcel, de
bevruchting en de innesteling. Deel 2 gaat over de embryonale en de foetale
fase, de placenta en de navelstreng, de geboorte, en wat het gedrag van de
moeder en haar omgeving met de vrucht doen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk hormoon zorgt ervoor dat een follikel in de eierstok rijpt?",
        opties=[
            "follikelstimulerend hormoon FSH",
            "luteïniserend hormoon LH",
            "progesteron uit het geel lichaam",
            "testosteron uit de teelballen",
        ],
        antwoord=0,
        uitleg="FSH komt uit de hypofyse en zet in de eerste helft van de cyclus een follikel aan het rijpen. De naam zegt het zelf: follikel stimulerend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hormonen maakt de hypofyse zelf? Er zijn er twee.",
        opties=[
            "follikelstimulerend hormoon FSH",
            "luteïniserend hormoon LH",
            "oestrogeen, dat de baarmoeder opbouwt",
            "progesteron, dat de baarmoeder op peil houdt",
        ],
        antwoord=[0, 1],
        uitleg="De hypofyse ligt onder de hersenen en stuurt de eierstok aan met FSH en LH. Oestrogeen en progesteron komen uit de eierstok zelf, uit de follikel en het geel lichaam.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de plotse, sterke stijging van LH die de eisprong uitlokt?",
        antwoord=["LH-piek", "de LH-piek", "LH piek"],
        uitleg="Halverwege de cyclus schiet de hoeveelheid LH in het bloed omhoog. Die LH-piek doet de rijpe follikel openbarsten, en dat is de eisprong of ovulatie.",
    ),
    dict(
        type="waarofniet",
        vraag="De eisprong gebeurt ongeveer veertien dagen vóór de volgende menstruatie.",
        antwoord=True,
        uitleg="De tweede helft van de cyclus duurt bij bijna iedereen veertien dagen. De eerste helft is wél wisselend, dus je rekent de eisprong terug vanaf de volgende menstruatie en niet vooruit vanaf de vorige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de follikel nadat de eicel eruit vertrokken is?",
        opties=[
            "hij wordt het geel lichaam",
            "hij verlaat mee de eierstok",
            "hij groeit uit tot een nieuwe eicel",
            "hij zakt mee naar de baarmoeder",
        ],
        antwoord=0,
        uitleg="De lege follikel blijft in de eierstok achter en wordt het geel lichaam. Dat is een tijdelijke hormoonklier die progesteron maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon maakt het geel lichaam vooral?",
        opties=[
            "progesteron",
            "testosteron",
            "follikelstimulerend hormoon",
            "luteïniserend hormoon",
        ],
        antwoord=0,
        uitleg="Het geel lichaam maakt progesteron. Dat houdt het baarmoederslijmvlies dik, zodat een bevruchte eicel zich kan innestelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als er geen bevruchting is, valt het geel lichaam weg en begint de menstruatie.",
        antwoord=True,
        uitleg="Zonder bevruchting verdwijnt het geel lichaam na een dag of twaalf. Het progesteron zakt, het slijmvlies kan niet in stand blijven en wordt afgestoten: de menstruatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoelang blijft een eicel na de eisprong bevruchtbaar?",
        opties=[
            "ongeveer een halve tot een hele dag",
            "ongeveer een volle week",
            "ongeveer veertien dagen",
            "ongeveer één uur",
        ],
        antwoord=0,
        uitleg="Een eicel leeft maar twaalf tot vierentwintig uur. Zaadcellen houden het in het vrouwelijk lichaam wel enkele dagen uit, en daarom liggen de vruchtbare dagen vóór de eisprong.",
    ),
    dict(
        type="invultekst",
        vraag="Welke klier bij de man maakt het geslachtshormoon testosteron?",
        antwoord=["teelbal", "de teelbal", "teelballen", "testikel", "de teelballen"],
        uitleg="De teelbal of testikel maakt zowel de zaadcellen als het hormoon testosteron. Dat hormoon zorgt ook voor de secundaire geslachtskenmerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het middenstuk of de hals van een zaadcel?",
        opties=[
            "het levert de energie om te zwemmen",
            "het bevat het erfelijk materiaal",
            "het boort zich door de eicelvliezen",
            "het bevat het reservevoedsel",
        ],
        antwoord=0,
        uitleg="In het middenstuk zitten de mitochondriën. Die leveren de energie waarmee de flagel de cel vooruit zweept.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen horen bij een zaadcel? Er zijn er drie.",
        opties=[
            "een flagel of staart",
            "een kop met een enzym",
            "mitochondriën in het middenstuk",
            "een dikke laag reservevoedsel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een zaadcel is gebouwd om te bewegen: kop, middenstuk en staart. Reservevoedsel neemt hij niet mee, dat zit juist in de eicel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zaadcel is veel groter dan een eicel.",
        antwoord=False,
        uitleg="Het is net omgekeerd. De eicel is de grootste cel van het menselijk lichaam, de zaadcel een van de kleinste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het enzym in de kop van de zaadcel?",
        opties=[
            "om de vliezen rond de eicel open te maken",
            "om de eicel van energie te voorzien",
            "om de staart sneller te laten slaan",
            "om de kern van de eicel te verdubbelen",
        ],
        antwoord=0,
        uitleg="Rond de eicel ligt een eiwitlaag. Het enzym breekt daar een weg in, zodat de kop van de zaadcel bij het celmembraan van de eicel kan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de cel die ontstaat als de kernen van de eicel en de zaadcel versmelten?",
        antwoord=["zygote", "de zygote", "zygoot"],
        uitleg="De versmelting van de twee kernen maakt één cel met het volledige erfelijk materiaal: de zygote. Daaruit groeit het hele kind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in het vrouwelijk voortplantingsstelsel gebeurt de bevruchting meestal?",
        opties=[
            "in de eileider",
            "in de baarmoeder",
            "in de eierstok",
            "in de schede",
        ],
        antwoord=0,
        uitleg="De eicel wordt na de eisprong opgevangen door de eileider, en daar komt de zaadcel hem tegemoet. De bevruchte eicel reist daarna verder naar de baarmoeder.",
    ),
    dict(
        type="waarofniet",
        vraag="De zaadcellen leggen hun weg naar de eicel af door de baarmoeder heen.",
        antwoord=True,
        uitleg="Na de zaadlozing zwemmen ze vanuit de schede door de baarmoederhals en de baarmoeder tot in de eileider. Van de miljoenen zaadcellen geraken er maar enkele honderden tot daar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er meteen nadat één zaadcel binnen is?",
        opties=[
            "het bevruchtingsmembraan sluit de eicel af",
            "de eicel begint zich meteen te delen",
            "de eicel maakt een tweede celkern aan",
            "de eicel verdubbelt haar reservevoedsel",
        ],
        antwoord=0,
        uitleg="Rond de eicel vormt zich meteen een bevruchtingsmembraan. Dat houdt alle andere zaadcellen buiten, want twee zaadcellen zouden te veel erfelijk materiaal binnenbrengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft een eicel wél en een zaadcel niet? Er zijn er twee.",
        opties=[
            "reservevoedsel in het cytoplasma",
            "een laag eiwit rondom de cel",
            "een staart om mee te zwemmen",
            "een kop met een enzym erin",
        ],
        antwoord=[0, 1],
        uitleg="De eicel moet de eerste dagen op eigen voorraad verder, dus draagt ze voedsel mee, met een eiwitlaag eromheen. De staart en het enzym zijn juist de uitrusting van de zaadcel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het vastzetten van de kiemblaas in het baarmoederslijmvlies?",
        antwoord=["innesteling", "de innesteling", "innestelen"],
        uitleg="Een dag of zes na de bevruchting nestelt de kiemblaas zich in het dikke slijmvlies. Pas dan is er echt sprake van een zwangerschap.",
    ),
    dict(
        type="waarofniet",
        vraag="De bevruchte eicel nestelt zich al in terwijl ze nog in de eileider zit.",
        antwoord=False,
        uitleg="Ze deelt zich onderweg wel al, maar de innesteling gebeurt pas in de baarmoeder. Nestelt ze zich toch in de eileider in, dan heet dat een buitenbaarmoederlijke zwangerschap.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de embryonale fase?",
        opties=[
            "de organen worden aangelegd",
            "de vrucht wordt vooral veel zwaarder",
            "de longen oefenen de ademhaling",
            "de vrucht draait zich met het hoofd omlaag",
        ],
        antwoord=0,
        uitleg="In de eerste acht weken worden alle organen aangelegd, de organogenese. Daarna groeit en rijpt wat er al is, en dat is de foetale fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lang duurt de embryonale fase ongeveer?",
        opties=[
            "de eerste acht weken",
            "de eerste twee weken",
            "de eerste zes maanden",
            "de hele zwangerschap",
        ],
        antwoord=0,
        uitleg="Na ongeveer acht weken zijn alle organen aangelegd en spreken we van een foetus. De zwangerschap zelf duurt ongeveer veertig weken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het aanleggen van de organen in de eerste weken?",
        antwoord=["organogenese", "de organogenese"],
        uitleg="Organogenese betekent letterlijk het ontstaan van de organen. Juist omdat alles dan aangelegd wordt, is de vrucht in die weken het gevoeligst voor schadelijke stoffen.",
    ),
    dict(
        type="waarofniet",
        vraag="De vrucht is pas levensvatbaar vanaf ongeveer vierentwintig weken.",
        antwoord=True,
        uitleg="Rond vierentwintig weken zijn de longen ver genoeg om met veel hulp te kunnen werken. Volgroeid is een baby pas rond zevenendertig tot veertig weken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de placenta?",
        opties=[
            "uit een deel van de moeder en een deel van de vrucht",
            "uit weefsel van de moeder alleen",
            "uit weefsel van de vrucht alleen",
            "uit samengeperst vruchtwater",
        ],
        antwoord=0,
        uitleg="De placenta of moederkoek heeft een moederlijk en een foetaal deel. Daar liggen het bloed van de moeder en dat van het kind vlak bij elkaar, gescheiden door de placentabarrière.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bloed van de moeder en het bloed van de vrucht lopen in de placenta door elkaar.",
        antwoord=False,
        uitleg="Ze komen heel dicht bij elkaar, maar blijven gescheiden door de placentabarrière. De uitwisseling gebeurt dóór die wand heen, van stof tot stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gaat er via de placenta van de moeder naar de vrucht? Er zijn er twee.",
        opties=[
            "zuurstof uit het bloed van de moeder",
            "voedingsstoffen zoals glucose",
            "koolstofdioxide uit de vrucht",
            "afvalstoffen uit de vrucht",
        ],
        antwoord=[0, 1],
        uitleg="De placenta werkt in twee richtingen. Zuurstof en voeding gaan naar de vrucht, koolstofdioxide en afvalstoffen gaan de andere kant op, naar het bloed van de moeder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit er in de navelstreng?",
        opties=[
            "twee slagaders en één ader",
            "één slagader en één ader",
            "alleen zenuwen en spierweefsel",
            "alleen vruchtwater en vetweefsel",
        ],
        antwoord=0,
        uitleg="Twee navelstrengslagaders brengen het zuurstofarme bloed van de vrucht naar de placenta, en één navelstrengader brengt het zuurstofrijke bloed terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vloeistof waarin de vrucht drijft en die haar beschermt tegen stoten?",
        antwoord=["vruchtwater", "het vruchtwater"],
        uitleg="Het vruchtwater vangt schokken op, houdt de temperatuur gelijk en laat de vrucht vrij bewegen, waardoor de spieren zich kunnen ontwikkelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fase van de bevalling komt eerst?",
        opties=[
            "de ontsluiting",
            "de uitdrijving",
            "de nageboorte",
            "het doorknippen van de navelstreng",
        ],
        antwoord=0,
        uitleg="Eerst gaat de baarmoederhals open, dat is de ontsluiting. Daarna wordt de baby geboren, de uitdrijving, en ten slotte komt de placenta naar buiten, de nageboorte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de laatste fase van de bevalling, waarin de placenta naar buiten komt?",
        antwoord=["nageboorte", "de nageboorte"],
        uitleg="Na de geboorte van het kind laat de placenta los van de baarmoederwand en komt ze mee naar buiten. Daarom heet dat de nageboorte.",
    ),
    dict(
        type="waarofniet",
        vraag="Weeën zijn samentrekkingen van de spierwand van de baarmoeder.",
        antwoord=True,
        uitleg="De baarmoeder is een holle spier. Haar samentrekkingen openen eerst de baarmoederhals en duwen daarna de baby naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom raadt men alcohol af tijdens de zwangerschap?",
        opties=[
            "alcohol gaat door de placenta naar de vrucht",
            "alcohol maakt het vruchtwater te zuur",
            "alcohol verhindert de innesteling",
            "alcohol verkort de navelstreng",
        ],
        antwoord=0,
        uitleg="Alcohol raakt vlot door de placentabarrière, en de lever van de vrucht kan hem nog niet afbreken. Hij stoort vooral de aanleg van de hersenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen noem je teratogeen?",
        opties=[
            "stoffen die de ontwikkeling van de vrucht verstoren",
            "stoffen die de moeder sneller doen vermoeien",
            "stoffen die de bevalling op gang brengen",
            "stoffen die de melkproductie stimuleren",
        ],
        antwoord=0,
        uitleg="Teratogene stoffen veroorzaken afwijkingen bij de vrucht. Zware metalen zoals kwik, cadmium en lood horen daarbij, net als sommige geneesmiddelen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vitamine wordt vóór en in het begin van de zwangerschap aangeraden om afwijkingen aan de ruggengraat te voorkomen?",
        antwoord=["foliumzuur", "vitamine B11", "vitamine B9"],
        uitleg="Foliumzuur helpt bij het sluiten van de neurale buis, waaruit het ruggenmerg groeit. Dat gebeurt heel vroeg, dus begin je er het best al vóór de zwangerschap mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ziekteverwekkers zijn gevaarlijk voor een ongeboren kind? Er zijn er drie.",
        opties=[
            "het rubellavirus of rodehond",
            "de toxoplasmose-parasiet",
            "het zikavirus",
            "het virus van een gewone wratje",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rodehond, toxoplasmose en zika raken door de placenta en kunnen de aanleg van hersenen, ogen en oren verstoren. Een gewone wrat op de huid blijft waar hij zit.",
    ),
    dict(
        type="waarofniet",
        vraag="Rauwe melkproducten en onvoldoende verhit vlees worden tijdens de zwangerschap afgeraden.",
        antwoord=True,
        uitleg="Daarin kunnen listeria en de toxoplasmose-parasiet zitten. Goed verhitten doodt ze, en daarom geldt de raad vooral voor rauwe en onvoldoende verhitte producten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is passief roken ook een probleem?",
        opties=[
            "de schadelijke stoffen komen ook zo in het bloed van de moeder",
            "de rook verwarmt het vruchtwater te sterk",
            "de rook maakt de navelstreng korter",
            "de rook vertraagt de weeën tijdens de bevalling",
        ],
        antwoord=0,
        uitleg="Wie meerookt, ademt dezelfde stoffen in. Koolstofmonoxide neemt in het bloed de plaats van zuurstof in, en dan krijgt de vrucht minder zuurstof binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe ouder de moeder, hoe kleiner de kans op een chromosoomafwijking bij de vrucht.",
        antwoord=False,
        uitleg="Het is omgekeerd: met de leeftijd stijgt die kans. Daarom wordt vanaf een bepaalde leeftijd extra onderzoek aangeboden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aanpassing in haar levensstijl helpt een zwangere vrouw het meest?",
        opties=[
            "stoppen met roken en met alcohol",
            "elke dag twee keer zo veel eten",
            "alle beweging zo veel mogelijk laten",
            "zo weinig mogelijk buitenkomen",
        ],
        antwoord=0,
        uitleg="Roken en alcohol zijn de twee vermijdbare factoren met het grootste effect. Eten voor twee hoeft niet, en matig bewegen is juist goed.",
    ),
]
