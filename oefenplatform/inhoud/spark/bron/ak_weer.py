# -*- coding: utf-8 -*-
"""De vragen voor "Het weer en zijn uitschieters" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "veranderingen in het landschap",
onderdeel "verandering door weer" (deel van de 40 %, samen met
[[ak_aardkorst]], [[ak_klimaat]] en [[ak_mens]]).

Deel 1 gaat over de weerelementen en hun eenheden: temperatuur in graden
Celsius, luchtdruk in hectopascal, windsnelheid in kilometer per uur, de
windrichting, en neerslag in millimeter. Ook de toestellen waarmee je ze meet
en het verschil tussen weer en klimaat.
Deel 2 gaat over extreem weer: hevige regenval, storm, orkaan en tornado, en
wat die met een landschap doen.

De eenheden en de getallen komen uit de fiche en uit de weerkunde: 1 millimeter
neerslag is 1 liter per vierkante meter, de gemiddelde luchtdruk op zeeniveau
is ongeveer 1013 hectopascal, de schaal van Beaufort loopt van 0 tot 12, en een
orkaan ontstaat boven zeewater van minstens ongeveer 26 graden. Wie hier een
getal bijschrijft, rekent het na en zet het ook in
`leerbundels/bron/controleer.py`.

Eén valkuil die in de vragen uitdrukkelijk aan bod komt: een windrichting wordt
genoemd naar waar de wind vandáán komt, niet waar hij naartoe waait.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Het is vandaag 9 graden, het waait stevig en het regent. Wat beschrijf je daarmee?",
        opties=[
            "Het weer van vandaag",
            "Het klimaat van de streek",
            "Het seizoen waarin we zitten",
            "De ligging van het gebied",
        ],
        antwoord=0,
        uitleg="Het weer is de toestand van de lucht op dit moment en op deze plaats. Pas als je dat over dertig jaar uitmiddelt, spreek je over het klimaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn weerelementen volgens de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "De temperatuur",
            "De luchtdruk",
            "De neerslag",
            "De hoogteligging",
            "De bodemsoort",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt vijf weerelementen: temperatuur, luchtdruk, windsnelheid, windrichting en neerslag. Hoogteligging en bodem horen bij het landschap, niet bij het weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke eenheid wordt de luchtdruk uitgedrukt?",
        opties=[
            "In hectopascal",
            "In graden Celsius",
            "In millimeter",
            "In kilometer per uur",
        ],
        antwoord=0,
        uitleg="Luchtdruk meet je in hectopascal, afgekort hPa. Op zeeniveau is de gemiddelde druk ongeveer 1013 hectopascal.",
    ),
    dict(
        type="invultekst",
        vraag="Neerslag wordt gemeten in ___.",
        antwoord="millimeter",
        uitleg="Eén millimeter neerslag betekent dat er op elke vierkante meter één liter water gevallen is. Zo kan je buien van verschillende plaatsen vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Er is 12 millimeter regen gevallen. Hoeveel liter kwam er op één vierkante meter terecht?",
        opties=[
            "12 liter",
            "1,2 liter",
            "120 liter",
            "Dat hangt af van hoe lang het regende",
        ],
        antwoord=0,
        uitleg="Eén millimeter komt overeen met één liter per vierkante meter. Twaalf millimeter is dus twaalf liter, of twaalf volle flessen op die ene meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je de windsnelheid?",
        opties=[
            "Met een anemometer",
            "Met een barometer",
            "Met een thermometer",
            "Met een regenmeter",
        ],
        antwoord=0,
        uitleg="Een anemometer heeft meestal drie kommetjes die ronddraaien. Hoe sneller ze draaien, hoe harder het waait.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk toestel hoort bij welke meting? Welke uitspraken kloppen? Er zijn er meerdere juist.",
        opties=[
            "Een thermometer meet de temperatuur",
            "Een barometer meet de luchtdruk",
            "Een regenmeter meet de neerslag",
            "Een windvaan meet de windsnelheid",
            "Een kompas meet de luchtvochtigheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een windvaan wijst de richting aan waaruit de wind komt, niet de snelheid; daarvoor dient de anemometer. En een kompas wijst het noorden aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een westenwind is een wind die uit het westen komt.",
        antwoord=True,
        uitleg="Een windrichting wordt altijd genoemd naar waar de wind vandaan komt. Een noordenwind komt dus uit het noorden en voert bij ons koude lucht aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="De barometer daalt sterk. Wat mag je verwachten?",
        opties=[
            "Wolken, wind en kans op regen",
            "Strakblauwe hemel en windstilte",
            "Vrieskou met heldere nachten",
            "Mist die de hele dag blijft hangen",
        ],
        antwoord=0,
        uitleg="Dalende druk wijst op een naderende depressie. In een lagedrukgebied stijgt lucht op, koelt af en vormt wolken, en dat geeft wind en neerslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een hogedrukgebied?",
        opties=[
            "Rustig en meestal droog weer",
            "Hevige buien en veel wind",
            "Sneeuw in elk seizoen van het jaar",
            "Snel wisselende temperaturen per uur",
        ],
        antwoord=0,
        uitleg="In een hogedrukgebied daalt de lucht en lossen wolken op. Dat geeft in de zomer zonnige dagen en in de winter vaak vrieskou of mist.",
    ),
    dict(
        type="waarofniet",
        vraag="De temperatuur wordt in België gemeten in graden Fahrenheit.",
        antwoord=False,
        uitleg="Bij ons en in het grootste deel van de wereld gebruikt men graden Celsius. Fahrenheit is vooral in de Verenigde Staten in gebruik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat een thermometer van een weerstation in een wit kastje met spleetjes?",
        opties=[
            "Om de zon weg te houden maar de lucht door te laten",
            "Om te vermijden dat de regen het meettoestel stukmaakt",
            "Om hem tegen diefstal te beschermen",
            "Om de meting van elders leesbaar te houden",
        ],
        antwoord=0,
        uitleg="In de volle zon meet een thermometer de warmte van de zon, niet die van de lucht. Het witte kastje weert de straling en laat de lucht toch vrij passeren.",
    ),
    dict(
        type="invultekst",
        vraag="De schaal waarmee de windkracht in stappen van 0 tot 12 wordt aangegeven, is de schaal van ___.",
        antwoord="Beaufort",
        uitleg="Bij 0 Beaufort staat de rook recht omhoog, bij 12 spreken we van orkaankracht. De schaal beschrijft wat je aan bomen, water en daken ziet gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een klimatogram?",
        opties=[
            "Een grafiek met de temperatuur en de neerslag per maand",
            "Een kaart met alle klimaatzones van de wereld erop getekend",
            "Een tabel met het weer van de voorbije week",
            "Een schema met de windrichtingen op een plaats",
        ],
        antwoord=0,
        uitleg="Op een klimatogram staan twaalf maanden naast elkaar: de neerslag als staafjes en de temperatuur als een lijn. Zo zie je in één blik wat voor klimaat een plaats heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een klimatogram lopen de staafjes in juli en augustus heel hoog, en in januari zijn ze bijna leeg. Wat weet je?",
        opties=[
            "Daar valt de meeste neerslag in de zomer",
            "Daar is het in de zomer het warmst",
            "Daar waait het in de zomer het hardst",
            "Daar duurt de zomer langer dan de winter",
        ],
        antwoord=0,
        uitleg="De staafjes op een klimatogram zijn altijd de neerslag. De temperatuur lees je van de lijn af, niet van de staafjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit één klimatogram kan je aflezen of het op het noordelijk of het zuidelijk halfrond ligt.",
        antwoord=True,
        uitleg="Op het noordelijk halfrond ligt de warmste maand rond juli, op het zuidelijk halfrond rond januari. Staat de temperatuurlijn in het midden laag, dan ligt de plaats in het zuiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van neerslag bestaan er? Er zijn er meerdere juist.",
        opties=[
            "Regen",
            "Sneeuw",
            "Hagel",
            "Wind",
            "Mist die blijft hangen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Neerslag is water dat uit de lucht naar beneden valt: regen, motregen, sneeuw, hagel, ijzel. Wind is luchtbeweging en mist is een wolk op de grond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het op een bergtop meestal kouder dan in het dal eronder?",
        opties=[
            "Omdat de lucht hoger dunner is en minder warmte vasthoudt",
            "Omdat de zon daar minder lang boven de horizon staat",
            "Omdat er hoger altijd meer wind uit het noorden waait",
            "Omdat sneeuw op de top de lucht eromheen afkoelt",
        ],
        antwoord=0,
        uitleg="Hoe hoger je komt, hoe ijler de lucht. Ze kan minder warmte vasthouden, en daarom daalt de temperatuur ongeveer met elke honderd meter stijging.",
    ),
    dict(
        type="waarofniet",
        vraag="Het weer van morgen kan tot op het uur nauwkeurig voorspeld worden.",
        antwoord=False,
        uitleg="Een voorspelling voor morgen klopt meestal goed, maar niet tot op het uur en niet tot op de gemeente. Hoe verder vooruit, hoe onzekerder ze wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Een gebied met lage luchtdruk, dat wolken en regen aanvoert, heet een ___.",
        antwoord="depressie",
        uitleg="Depressies komen bij ons meestal van over de Atlantische Oceaan binnen. In de herfst en de winter volgen ze elkaar soms dagenlang op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Na een nacht met heel veel regen staat een straat blank en is een stuk van een akker weggespoeld. Wat gebeurde er?",
        opties=[
            "Extreem weer heeft het landschap veranderd",
            "Het klimaat van de streek is veranderd",
            "De bodem is er van soort veranderd",
            "Het reliëf is er plots gaan stijgen",
        ],
        antwoord=0,
        uitleg="Eén hevige bui is extreem weer, geen klimaatverandering. Zulke buien kunnen op enkele uren tijd wel echte sporen in het landschap achterlaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als er in korte tijd heel veel regen valt op een droge, harde bodem?",
        opties=[
            "Het water stroomt over de grond weg",
            "Het water zakt bijzonder snel in de grond",
            "Het water blijft er dagenlang rustig staan",
            "Het water verdampt meteen door de warmte",
        ],
        antwoord=0,
        uitleg="Een uitgedroogde bodem neemt water traag op. Valt er dan veel in één keer, dan loopt het eroverheen in plaats van erin, en dat geeft modderstromen.",
    ),
    dict(
        type="waarofniet",
        vraag="Verharde oppervlakken zoals wegen en parkings vergroten de kans op wateroverlast.",
        antwoord=True,
        uitleg="Op beton en asfalt kan geen druppel wegzakken. Al dat water moet naar de riool of de beek, en die kunnen het bij een hevige bui niet slikken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke sporen laat een overstroming in een landschap na? Er zijn er meerdere juist.",
        opties=[
            "Een laag slib op de velden",
            "Weggespoelde wegen en bruggen",
            "Uitgesleten geulen in de akkers",
            "Een blijvend hoger reliëf in de streek",
            "Een andere bodemsoort in de hele vallei",
        ],
        antwoord=[0, 1, 2],
        uitleg="Water laat slib achter, sleept wegen mee en snijdt geulen uit. Het reliëf van een hele streek verandert er niet blijvend door, en de bodemsoort ook niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vanaf welke windkracht op de schaal van Beaufort spreekt men van storm?",
        opties=[
            "Vanaf 9",
            "Vanaf 4",
            "Vanaf 6",
            "Vanaf 12",
        ],
        antwoord=0,
        uitleg="Vanaf 9 Beaufort spreekt men van storm, vanaf 10 van zware storm en bij 12 van orkaankracht. Bij 6 is het gewoon krachtige wind.",
    ),
    dict(
        type="invultekst",
        vraag="Een tropische wervelstorm boven warm zeewater heet een ___.",
        antwoord="orkaan",
        uitleg="In de Atlantische Oceaan heet zo'n storm een orkaan. In het westen van de Stille Oceaan noemt men hem een tyfoon, en rond de Indische Oceaan een cycloon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstaan orkanen enkel boven warm zeewater?",
        opties=[
            "Omdat warm water veel damp en energie levert",
            "Omdat warm water lichter is dan koud water",
            "Omdat er boven warm water nooit wind staat",
            "Omdat warm water de lucht droger maakt",
        ],
        antwoord=0,
        uitleg="Een orkaan draait op verdamping. Boven zeewater van ongeveer 26 graden of warmer stijgt er genoeg vochtige lucht op om zo'n storm op gang te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het oog van een orkaan?",
        opties=[
            "Het rustige midden van de storm",
            "De plaats waar de storm het hevigst is",
            "Het punt waar de storm de kust raakt",
            "De wolk die het hoogst boven de storm uitsteekt",
        ],
        antwoord=0,
        uitleg="In het oog is het windstil en breekt soms de zon door. Rond dat oog ligt juist de oogwand, met de zwaarste wind van de hele storm.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tornado bestrijkt een veel breder gebied dan een orkaan.",
        antwoord=False,
        uitleg="Net omgekeerd: een orkaan is honderden kilometers breed, een tornado vaak maar enkele honderden meters. In dat smalle spoor kan de wind wel heftiger zijn dan in een orkaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit ontstaat een tornado meestal?",
        opties=[
            "Uit een zware onweersbui",
            "Uit een gewone regenbui in de lente",
            "Uit een hogedrukgebied boven het land",
            "Uit mist die boven een meer blijft hangen",
        ],
        antwoord=0,
        uitleg="Een tornado hangt als een slurf onder een zwaar onweer. In België komen ze zelden voor, maar ze bestaan wel degelijk, meestal in de zomer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een zware storm met een bos? Er zijn er meerdere juist.",
        opties=[
            "Bomen breken doormidden",
            "Bomen waaien met wortel en al om",
            "Er vallen open plekken in het bos",
            "De bodem verandert er van bodemsoort door",
            "Het bos verandert er blijvend van boomsoort door",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een zware storm kan hele percelen platleggen. Waar het bos openvalt, komt er licht op de bodem en begint een nieuwe generatie bomen te groeien. De bodemsoort verandert daar niet door.",
    ),
    dict(
        type="invultekst",
        vraag="Water dat bij storm tegen de kust wordt opgestuwd en daar over de dijk dreigt te slaan, noemt men een ___.",
        antwoord="stormvloed",
        uitleg="Bij een stormvloed duwt de wind het zeewater tegen de kust op, bovenop het gewone hoogwater. Daarom liggen er langs onze kust dijken en stormmuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een stormvloed aan onze kust gevaarlijker als hij samenvalt met springtij?",
        opties=[
            "Omdat het water dan toch al hoger staat",
            "Omdat de wind dan altijd sterker waait",
            "Omdat de zee dan warmer is dan gewoonlijk",
            "Omdat de stranden dan breder zijn dan anders",
        ],
        antwoord=0,
        uitleg="Bij springtij is het verschil tussen eb en vloed het grootst. Komt daar nog een storm bij die het water opstuwt, dan stapelen de twee zich op.",
    ),
    dict(
        type="waarofniet",
        vraag="Extreem weer komt in België niet voor.",
        antwoord=False,
        uitleg="Ook bij ons zijn er zware stormen, hagelbuien die oogsten vernielen, en overstromingen na hevige regen. Orkanen en tornado's blijven zeldzaam, maar de rest niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen helpen tegen wateroverlast na hevige regen? Er zijn er meerdere juist.",
        opties=[
            "Een overstromingsgebied naast de rivier aanleggen",
            "Regenwater laten insijpelen in plaats van het af te voeren",
            "Beken meer ruimte geven om te kronkelen",
            "Elke beek in een rechte betonnen goot leggen",
            "Nog meer oppervlakte verharden rond de stad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Water moet plaats en tijd krijgen. Gebieden die mogen onderlopen, bodems die water opnemen en beken die mogen kronkelen, remmen de piek af. Beton doet juist het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom loopt een dorp onder aan de voet van een helling en niet bovenop?",
        opties=[
            "Omdat het water van de helling naar beneden stroomt",
            "Omdat de bodem beneden altijd uit klei bestaat",
            "Omdat er beneden meer regen valt dan boven",
            "Omdat er beneden minder riolering is aangelegd",
        ],
        antwoord=0,
        uitleg="Water volgt de zwaartekracht. Alles wat op de helling valt en niet wegzakt, komt onderaan samen, en juist daar liggen vaak de oudste huizen van een dorp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen weer en extreem weer?",
        opties=[
            "Extreem weer wijkt sterk af van het gewone",
            "Extreem weer komt enkel in de tropen voor",
            "Extreem weer duurt altijd meerdere weken",
            "Extreem weer wordt nooit op voorhand gemeld",
        ],
        antwoord=0,
        uitleg="Extreem weer is weer dat ver buiten het gewone valt: veel meer regen, veel meer wind of veel meer hitte dan normaal voor die plaats en dat seizoen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hagelbui kan in enkele minuten een hele oogst vernielen.",
        antwoord=True,
        uitleg="Hagelstenen slaan bladeren, vruchten en jonge planten kapot. Daarom spannen fruittelers netten boven hun boomgaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een weerbericht kondigt code oranje aan. Wat betekent dat?",
        opties=[
            "Er wordt gevaarlijk weer verwacht",
            "Het weer blijft de hele dag onveranderd",
            "Er mag niemand nog naar buiten",
            "Het weerbericht is nog niet zeker",
        ],
        antwoord=0,
        uitleg="De kleurcodes waarschuwen voor gevaar. Geel betekent opletten, oranje betekent gevaarlijk weer, en rood betekent dat er zware schade verwacht wordt.",
    ),
    dict(
        type="invultekst",
        vraag="De smalle, draaiende luchtslurf onder een onweerswolk heet een ___.",
        antwoord="tornado",
        uitleg="Je herkent hem aan de trechter die uit de wolk naar de grond zakt. Raakt hij de grond niet, dan spreekt men van een slurf of een trechterwolk.",
    ),
]
