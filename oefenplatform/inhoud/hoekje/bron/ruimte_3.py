# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — De ruimte, deel 3: vragen van Kim, aangevuld."""

VAK = "De ruimte"
BESTAND = "de-ruimte.json"
TITEL = "Verder dan de planeten"
VOLGORDE = 3

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Soms zien we een ver sterrenstelsel dubbel of uitgerekt, alsof er een lens voor hangt. Hoe heet dat?",
        "opties": [
            "Een zwaartekrachtlens",
            "Het dopplereffect",
            "De gebeurtenishorizon",
            "De parallax van het stelsel",
        ],
        "antwoord": 0,
        "uitleg": "Zware massa buigt de ruimte, en licht dat erlangs scheert volgt die bocht. Staat er toevallig een sterrenstelsel precies tussen ons en iets verder weg, dan werkt dat als een vergrootglas. Einstein voorspelde het; vandaag gebruiken sterrenkundigen het om nog verder te kijken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waar worden zware elementen zoals goud en platina gesmeed?",
        "opties": [
            "Bij een supernova of een botsing van twee neutronensterren",
            "In de rustige kern van een gewone ster zoals onze zon",
            "Bij het langzaam afkoelen en verdampen van een witte dwerg",
            "In de koude gasnevels waaruit nieuwe sterren ontstaan",
        ],
        "antwoord": 0,
        "uitleg": "Tot ijzer levert kernfusie energie op; daarna kost het energie, dus een gewone ster stopt daar. Alleen bij de waanzinnige druk van een supernova of een botsing van neutronensterren gaat het verder. Het goud in een ring is dus ouder dan de aarde zelf.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe denken wetenschappers dat onze maan ontstaan is?",
        "opties": [
            "Uit het puin van een botsing met een jonge planeet ter grootte van Mars",
            "De aarde ving een rondzwervende planetoïde in met haar zwaartekracht",
            "De jonge aarde draaide zo snel dat er een stuk van afgeslingerd werd",
            "De maan en de aarde ontstonden apart, uit dezelfde stofwolk",
        ],
        "antwoord": 0,
        "uitleg": "Die botser heeft zelfs een naam gekregen: Theia. Het weggeslagen puin klonterde in een baan om de aarde samen. Het bewijs zit in de maanstenen: hun samenstelling lijkt griezelig veel op de buitenlagen van de aarde, en dat past niet bij een ingevangen brok van elders.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een lichtdeeltje dat in de kern van de zon ontstaat, doet er tienduizenden jaren over om naar buiten te raken. Hoe kan dat?",
        "opties": [
            "Het wordt onderweg voortdurend opgeslorpt en weer uitgezonden, elke keer in een andere richting",
            "De zon is zo onvoorstelbaar groot dat zelfs licht er met zijn eigen snelheid eeuwen over doet",
            "De magnetische velden rond de zon houden het licht een tijdlang gevangen",
            "Het licht moet wachten tot er een zonnevlam is om te kunnen ontsnappen",
        ],
        "antwoord": 0,
        "uitleg": "Het gaat wel degelijk met de lichtsnelheid, maar het legt geen rechte weg af. In dat loodzware gas botst het ontelbare keren en verandert het telkens van richting: een dronkemanswandeling. Eenmaal aan de oppervlakte is het in acht minuten bij ons.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is een supernova van het type Ia zo nuttig om afstanden te meten?",
        "opties": [
            "Zulke ontploffingen zijn altijd ongeveer even fel, dus verraadt hun helderheid hun afstand",
            "Zulke ontploffingen zijn altijd even lang zichtbaar, dus verraadt hun duur de afstand",
            "Zulke ontploffingen geven altijd dezelfde kleur, en die verkleurt met de afstand",
            "Zulke ontploffingen komen zo vaak voor dat je gewoon kunt middelen",
        ],
        "antwoord": 0,
        "uitleg": "Het is een witte dwerg die massa wegzuigt van een buurster en bij een vaste grenswaarde ontploft. Altijd bij dezelfde massa, dus altijd even fel: een standaardkaars. Zie je er een die flauw lijkt, dan weet je hoe ver hij staat. Zo ontdekte men dat het heelal steeds sneller uitdijt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat ligt er aan de allerbuitenste rand van ons zonnestelsel, ver voorbij de Kuipergordel?",
        "opties": [
            "De Oortwolk, een reusachtige bol van ijzige kometen rondom alles",
            "De asteroïdengordel met brokken steen tussen Mars en Jupiter",
            "Een vlakke ring van stof die alleen in het baanvlak ligt",
            "De rand van het heelal, waar de ruimte zelf ophoudt",
        ],
        "antwoord": 0,
        "uitleg": "Niemand heeft die wolk ooit gezien; we leiden hem af uit de banen van langeperiodekometen die er vandaan lijken te komen. Hij ligt duizenden keren verder dan Neptunus, en licht doet er ruim een jaar over om er te raken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een magnetar?",
        "opties": [
            "Een neutronenster met een onvoorstelbaar sterk magnetisch veld",
            "Een planeet die volledig uit magnetisch ijzererts bestaat",
            "Een zwart gat dat sterren naar zich toe trekt met magnetisme",
            "Een ster met twee magnetische polen die om elkaar draaien",
        ],
        "antwoord": 0,
        "uitleg": "Het zijn de sterkste magneten die we kennen: duizend miljard keer sterker dan een koelkastmagneet. Op duizend kilometer afstand zou zo'n veld de atomen in je lichaam vervormen. Gelukkig staat de dichtstbijzijnde duizenden lichtjaren ver.",
    },
    {
        "type": "waarofniet",
        "vraag": "De zon heeft geen vast oppervlak waar je op zou kunnen staan.",
        "antwoord": True,
        "uitleg": "Ze bestaat helemaal uit gloeiend gas en plasma. Wat wij haar oppervlak noemen, is gewoon de laag waar het gas doorzichtig genoeg wordt om licht te laten ontsnappen. Er is geen grens, alleen gas dat naar buiten toe steeds ijler wordt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Zonnevlekken zien er donker uit. Wat zijn het?",
        "opties": [
            "Plekken die koeler zijn dan hun omgeving, door sterke magnetische velden",
            "Echte gaten in het oppervlak, waardoor je de donkere binnenkant van de zon ziet",
            "Schaduwen van planeten die voor de zon langs schuiven",
            "Wolken van roet die op het oppervlak van de zon drijven",
        ],
        "antwoord": 0,
        "uitleg": "Ze zijn nog altijd zo'n 3500 graden heet, maar tegen de 5500 graden ernaast lijken ze zwart. Zou je er eentje los aan de hemel hangen, dan zou hij feller schijnen dan de volle maan. Het aantal zonnevlekken gaat op en neer in een ritme van ongeveer elf jaar.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is Mars rood?",
        "opties": [
            "Het stof op de bodem bestaat grotendeels uit geroest ijzer",
            "De dampkring van Mars bestaat uit gassen die zelf rood van kleur zijn",
            "De planeet is zo heet dat hij gloeit als een kachel",
            "Het rode licht van de zon weerkaatst er het sterkst",
        ],
        "antwoord": 0,
        "uitleg": "Mars is letterlijk verroest: ijzer in het stof heeft zich met zuurstof verbonden tot ijzeroxide, hetzelfde spul dat een oude fiets bruinrood maakt. Stofstormen verspreiden het over de hele planeet, soms wekenlang.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op Venus is het aan de oppervlakte ruim 460 graden, heter dan op Mercurius, dat veel dichter bij de zon staat. Hoe komt dat?",
        "opties": [
            "Haar dikke dampkring van koolstofdioxide houdt de warmte gevangen",
            "Venus staat zo dicht bij ons dat ze ook onze warmte opvangt",
            "Venus draait zo traag om haar as dat dezelfde kant eindeloos ligt op te warmen",
            "In de kern van Venus woedt nog altijd een kernreactie",
        ],
        "antwoord": 0,
        "uitleg": "Het zonlicht raakt binnen, de warmte raakt er niet meer uit: een broeikaseffect dat volledig op hol geslagen is. De druk aan de oppervlakte is bovendien als negenhonderd meter diep onder water. Sondes die er landden, hielden het hoogstens twee uur uit.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Grote Rode Vlek op Jupiter is een vulkaan die al eeuwen uitbarst.",
        "antwoord": False,
        "uitleg": "Het is een storm, geen vulkaan: Jupiter heeft niet eens een vaste bodem om een vulkaan op te zetten. Die storm wordt al sinds de zeventiende eeuw waargenomen en er past nog altijd een hele aarde in, al krimpt hij de laatste decennia zichtbaar.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waar zoeken wetenschappers in ons zonnestelsel het liefst naar leven, buiten Mars?",
        "opties": [
            "Onder het ijs van manen als Europa en Enceladus, waar vloeibaar water zit",
            "In de wolkenlagen boven de zuidpool van de reuzenplaneet Jupiter",
            "Op de eeuwig donkere bodem van kraters op Mercurius, waar het koel blijft",
            "In de ringen van Saturnus, tussen de ijsbrokken",
        ],
        "antwoord": 0,
        "uitleg": "Enceladus spuit zelfs pluimen water de ruimte in, dwars door scheuren in zijn ijskorst: een sonde kan er dwars doorheen vliegen en proeven. De warmte komt niet van de zon maar van het kneden door de zwaartekracht van de reuzenplaneet.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op Titan, een maan van Saturnus, liggen meren en stromen er rivieren. Waaruit bestaat die vloeistof?",
        "opties": [
            "Uit methaan en ethaan, want daar is water steenhard bevroren",
            "Uit gewoon water, precies zoals de rivieren en meren bij ons op aarde",
            "Uit vloeibaar ijzer, dat door de kou naar boven komt",
            "Uit vloeibare zuurstof, die uit de dampkring neerslaat",
        ],
        "antwoord": 0,
        "uitleg": "Bij min 180 graden is water zo hard als rots, maar methaan blijft vloeibaar. Titan heeft dus een echte kringloop met wolken, regen en rivieren, alleen met een andere vloeistof. Het is de enige maan in ons zonnestelsel met een dikke dampkring.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Uranus draait zowat liggend rond de zon, met zijn as bijna in zijn baanvlak. Wat is daarvan het gevolg?",
        "opties": [
            "Elke pool krijgt om beurten ruim twintig jaar zon en daarna twintig jaar nacht",
            "De planeet heeft helemaal geen seizoenen, want de zon staat altijd gelijk",
            "Een dag op Uranus duurt precies even lang als een jaar",
            "De zon komt er elke dag in een andere richting op",
        ],
        "antwoord": 0,
        "uitleg": "Uranus doet 84 jaar over één rondje, en ligt daarbij op zijn kant. Waarschijnlijk heeft een enorme botsing hem ooit omvergekegeld. Zijn manen en ringen draaien netjes mee in dat gekantelde vlak.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom zien we de Melkweg als een lichte band dwars over de hemel?",
        "opties": [
            "Omdat wij er middenin zitten en we dus door de platte schijf heen kijken",
            "Omdat de sterren zich aan de hemel vanzelf in een lange rij scharen",
            "Omdat het stof hoog in onze eigen dampkring het sterlicht tot een band bundelt",
            "Omdat we naar de rand van het heelal kijken, die rond ons ligt",
        ],
        "antwoord": 0,
        "uitleg": "Ons sterrenstelsel is een platte schijf, en de zon zit ergens in die schijf. Kijk je in het vlak ervan, dan kijk je door duizenden lichtjaren sterren heen. Kijk je er loodrecht op, dan zie je er veel minder. Galileo was de eerste die met een kijker zag dat die band gewoon uit sterren bestaat.",
    },
    {
        "type": "waarofniet",
        "vraag": "In het midden van de Melkweg zit een zwart gat van miljoenen zonsmassa's.",
        "antwoord": True,
        "uitleg": "Het heet Sagittarius A*. We weten het doordat sterren er in razendsnelle, strakke ellipsen omheen zwiepen rond iets wat we niet zien. In 2022 verscheen het eerste beeld ervan. Gevaarlijk is het niet: het staat 26 000 lichtjaar ver en zuigt niets naar zich toe dat er niet al naartoe viel.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Sterren fonkelen 's nachts, planeten bijna niet. Waarom niet?",
        "opties": [
            "Een planeet is voor ons een klein schijfje, een ster maar één punt",
            "Een planeet staat zo dicht bij ons dat haar licht veel te sterk is om te flikkeren",
            "Planeten maken hun eigen licht, en dat flikkert niet",
            "Planeten staan lager aan de hemel, waar de lucht rustiger is",
        ],
        "antwoord": 0,
        "uitleg": "Het fonkelen ontstaat in onze eigen dampkring: wervelende luchtlagen buigen het licht alle kanten op. Bij een puntbron zie je dat meteen; bij een schijfje middelt het uit, want niet alle punten flikkeren tegelijk dezelfde kant op. Vandaar de vuistregel: wat rustig staat te schijnen, is meestal een planeet.",
    },
    {
        "type": "invultekst",
        "vraag": "De ruimtetelescoop James Webb staat in een rustig punt op anderhalf miljoen kilometer van ons, in de schaduw van de aarde. Hoe noemen we zo'n evenwichtspunt? Een ... -punt.",
        "antwoord": "lagrange",
        "uitleg": "In zo'n lagrangepunt heffen de zwaartekracht van de zon en die van de aarde elkaar net zo op dat een telescoop er met weinig brandstof kan blijven hangen. Webb staat in L2 en houdt zon, aarde en maan altijd achter zijn zonneschild, zodat hij in het donker en de kou kan werken.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op de maan heb je dezelfde snelheid nodig als op aarde om weg te raken.",
        "antwoord": False,
        "uitleg": "Op aarde is de ontsnappingssnelheid ongeveer 11,2 kilometer per seconde, zo'n 40 000 kilometer per uur. Op de maan is dat maar 2,4, en daarom volstond daar een klein opstijgtrapje in plaats van een reusachtige raket. Bij een zwart gat ligt die snelheid boven de lichtsnelheid, en dus raakt niets er nog weg.",
    },
]
