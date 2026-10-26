# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — De ruimte, deel 5: Gemini-reeks 4 van Kim, aangevuld.

Kim liet op 26 oktober 2026 een vierde reeks uit haar Gemini-gesprek nakijken.
Zeven van de tien ruimtevragen stonden inhoudelijk al in deel 1 tot 4 (het
Lagrange-punt, de Roche-limiet, spaghettificatie, de hitte op Venus, wat er na
een supernova overblijft, zwaartekrachtgolven en roodverschuiving). De drie
nieuwe (Carrington, Andromeda, de Kuipergordel) staan hier, met zeventien
eigen vragen erbij.
"""

VAK = "De ruimte"
BESTAND = "de-ruimte.json"
TITEL = "Zonnestormen, kometen en verre manen"
VOLGORDE = 5

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": r"In september \(1859\) vielen overal telegraaflijnen uit en zag men poollicht tot in de tropen. Wat was er gebeurd?",
        "opties": [
            "Een reusachtige uitbarsting op de zon had de aarde getroffen",
            "Een grote komeet was rakelings langs de aarde gevlogen",
            "Een vulkaan in Indonesië had as tot in de ruimte geblazen",
            "Alle planeten stonden die week netjes op één lange rij",
        ],
        "antwoord": 0,
        "uitleg": r"De Engelse sterrenkundige Richard Carrington zag die dag een felle flits op de zon. Minder dan een dag later sloeg een wolk geladen deeltjes tegen het magneetveld van de aarde. Telegrafisten kregen schokken en sommige toestellen bleven seinen zonder batterij. Gebeurt dat vandaag, dan liggen satellieten, gps en stroomnetten in het vuur. Daarom houden ruimteweerkundigen de zon dag en nacht in het oog.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Bijna alle sterrenstelsels bewegen van ons weg, maar het Andromedastelsel komt op ons af. Waarom?",
        "opties": [
            "Op die korte afstand wint hun onderlinge zwaartekracht het van de uitdijing",
            "Een zwaar zwart gat achter Andromeda duwt het stelsel onze richting uit",
            "Andromeda draait zo snel rond zijn as dat het zichzelf naar ons slingert",
            "Het lijkt maar zo: we zien Andromeda in een spiegeling van ons eigen stelsel",
        ],
        "antwoord": 0,
        "uitleg": r"De uitdijing van het heelal speelt pas over enorme afstanden. Andromeda staat op \(2{,}5\) miljoen lichtjaar, voor sterrenstelsels is dat de buren. Op die afstand trekken de Melkweg en Andromeda elkaar aan, met zo'n \(110\) km per seconde. Over ongeveer vier à vijf miljard jaar smelten ze samen tot één groot stelsel.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Pluto zwerft rond in een brede schijf van ijzige brokken net voorbij Neptunus. Hoe heet die schijf?",
        "opties": [
            "De Kuipergordel",
            "De Oortwolk",
            "De asteroïdengordel",
            "De Van Allengordel",
        ],
        "antwoord": 0,
        "uitleg": r"Ze heet naar de Nederlands-Amerikaanse sterrenkundige Gerard Kuiper. Er zitten Pluto en nog andere dwergplaneten in, en van daar komen veel kometen die om de paar jaar terugkeren. De Oortwolk ligt nog duizend keer verder. De Van Allengordels zijn iets heel anders: twee ringen geladen deeltjes rond de aarde zelf. In \(2019\) vloog de sonde New Horizons langs Arrokoth, een sneeuwman van twee aan elkaar gekleefde bollen in de Kuipergordel.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe weten sterrenkundigen waaruit een ster bestaat, terwijl er nooit iemand geweest is?",
        "opties": [
            "Elk element laat eigen donkere lijntjes na in de kleurenband van het sterlicht",
            "Ruimtesondes vliegen langs de ster en brengen een staal gas mee terug",
            "Meteorieten die op aarde vallen, komen van die sterren en verraden het",
            "Uit de temperatuur van de ster volgt vanzelf welke stoffen erin moeten zitten",
        ],
        "antwoord": 0,
        "uitleg": "Stuur sterlicht door een prisma en je krijgt een regenboog vol fijne zwarte streepjes. Elk element slorpt licht van precies zijn eigen kleuren op, en laat zo een soort streepjescode achter. Waterstof, natrium of ijzer: je leest het af zonder er ooit te komen. Een sonde zou er trouwens duizenden jaren over doen om zelfs maar de dichtstbijzijnde ster te bereiken.",
    },
    {
        "type": "waarofniet",
        "vraag": "Helium werd eerst in het licht van de zon ontdekt, en pas bijna dertig jaar later op aarde.",
        "antwoord": True,
        "uitleg": r"In \(1868\) zagen sterrenkundigen bij een zonsverduistering een geel lijntje in het zonlicht dat bij geen enkel bekend element paste. Ze noemden het nieuwe element naar Helios, de Griekse zonnegod. Pas in \(1895\) vond de Schotse scheikundige William Ramsay het ook op aarde, in een gesteente.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een dag op Mars heet een sol. Hoe lang duurt die?",
        "opties": [
            "Ongeveer veertig minuten langer dan een dag op aarde",
            "Ongeveer twee keer zo lang als een dag op aarde",
            "Ongeveer half zo lang als een dag op aarde",
            "Precies even lang, tot op de seconde",
        ],
        "antwoord": 0,
        "uitleg": r"Een sol duurt \(24\) uur en \(39\) minuten. Wie bij de NASA een marsrobot bestuurt, leeft daarom soms op marstijd: elke dag begint het werk veertig minuten later dan de dag ervoor. Na een paar weken ontbijt je midden in de nacht. Een jaar op Mars duurt dan weer bijna twee aardse jaren.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Olympus Mons op Mars is met zowat \(22\) km de hoogste vulkaan van het zonnestelsel. Hoe kon hij zo hoog worden?",
        "opties": [
            "De korst schuift er niet, dus bleef hij miljoenen jaren op één plek aangroeien",
            "Op Mars waait het nooit, dus blies er nooit een korrel stof van de berg weg",
            "Mars is vanbinnen veel heter dan de aarde, dus spuwt hij tien keer meer lava",
            "Een inslag van een planetoïde duwde de grond daar als een bult omhoog",
        ],
        "antwoord": 0,
        "uitleg": "Op aarde schuiven de platen van de korst langzaam over een hete plek in de mantel. Daardoor krijg je een rij vulkanen naast elkaar, zoals de eilanden van Hawaï, in plaats van één reus. Op Mars ligt de korst stil en stapelde de lava zich op dezelfde plaats op. De zwakkere zwaartekracht helpt ook: een berg zakt er minder snel onder zijn eigen gewicht in. En het waait op Mars wel degelijk, met stofstormen die soms de hele planeet bedekken.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een jaar op Mercurius duurt langer dan een jaar op aarde.",
        "antwoord": False,
        "uitleg": r"Mercurius staat het dichtst bij de zon en raast in maar \(88\) dagen rond, nog geen drie maanden. Hoe dichter bij de zon, hoe korter de baan en hoe sneller een planeet moet gaan om niet in de zon te vallen. Neptunus, helemaal buitenaan, doet er \(165\) jaar over.",
    },
    {
        "type": "waarofniet",
        "vraag": "Saturnus is gemiddeld lichter dan water: in een reusachtig bad zou hij blijven drijven.",
        "antwoord": True,
        "uitleg": r"Saturnus is enorm groot, maar bestaat bijna helemaal uit waterstof en helium. Een liter Saturnus weegt gemiddeld zo'n \(0{,}7\) kilo, een liter water \(1\) kilo. Een bad om hem in te leggen bestaat natuurlijk niet, en zijn kern van steen en ijs zou wel zinken als je hem ooit kon losmaken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op de foto's van de maanlandingen zie je geen enkele ster aan de zwarte hemel. Hoe komt dat?",
        "opties": [
            "De camera stond afgesteld op de felle grond, en dan vallen zwakke sterren weg",
            "Op de maan zijn sterren onzichtbaar, want er is geen lucht om hun licht te dragen",
            "Het was op de maan net nacht, en dan zie je daar nooit sterren aan de hemel",
            "De sterren zijn er achteraf uitgehaald om de foto's rustiger te laten ogen",
        ],
        "antwoord": 0,
        "uitleg": "De astronauten werkten in vol zonlicht op een felle grijze bodem, in witte pakken. Om dat niet als één witte vlek te fotograferen, stond de camera op een heel korte belichting. Het zwakke licht van sterren komt dan gewoon niet op de foto. Probeer het zelf 's avonds met je gsm onder een felle straatlamp: ook dan blijft de hemel zwart. Licht heeft trouwens helemaal geen lucht nodig om te reizen.",
    },
    {
        "type": "invultekst",
        "vraag": r"In \(1957\) draaide een hondje als eerste dier rond de aarde, aan boord van de Spoetnik \(2\). Hoe heette ze?",
        "antwoord": "Laika",
        "uitleg": r"Laika was een zwerfhond uit Moskou, gekozen omdat zwerfhonden kou en honger gewoon waren. Ze overleefde de reis spijtig genoeg niet: een terugkeer was nooit gepland, en de capsule werd binnen enkele uren te warm. Pas in \(1960\) kwamen Belka en Strelka levend terug. Laika's verhaal zette veel mensen aan het denken over hoe we met proefdieren omgaan.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Waarom moest de ruimtetelescoop Hubble in \(1993\) een soort bril krijgen?",
        "opties": [
            "Zijn grote spiegel was een fractie van een haardikte verkeerd geslepen",
            "Een wolk ruimtestof had zijn lens na drie jaar dof en kras gemaakt",
            "Hij was te dicht bij de aarde gelanceerd en zag daardoor alles wazig",
            "Een zonnestorm had zijn camera's verbrand en ze kleurenblind gemaakt",
        ],
        "antwoord": 0,
        "uitleg": r"De spiegel van \(2{,}4\) meter was aan de rand \(2\) duizendste millimeter te plat, een vijftigste van de dikte van een haar. Genoeg om alle beelden wazig te maken. Astronauten vlogen erheen en bouwden er correctielenzen in, net zoals een bril de fout van een oog opvangt. Daarna maakte Hubble de scherpste foto's die de mensheid ooit van het heelal had gezien.",
    },
    {
        "type": "waarofniet",
        "vraag": "De sterren van een sterrenbeeld, zoals de Grote Beer, staan allemaal ongeveer even ver van ons.",
        "antwoord": False,
        "uitleg": "Een sterrenbeeld is een tekening die wij van op aarde maken, zoals wolken die op een draak lijken. De sterren ervan staan soms honderden lichtjaren achter elkaar en hebben niets met elkaar te maken. Vanaf een andere ster bekeken zou de Grote Beer er helemaal anders uitzien, of gewoon niet bestaan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een komeet heeft een lange staart. Naar welke kant wijst die?",
        "opties": [
            "Altijd van de zon weg, ook als de komeet al terug naar buiten vliegt",
            "Altijd achter de komeet aan, zoals de rook achter een stoomtrein",
            "Altijd naar de aarde toe, omdat onze zwaartekracht er stevig aan trekt",
            "Altijd naar de dichtstbijzijnde planeet, door het magneetveld ervan",
        ],
        "antwoord": 0,
        "uitleg": "Een komeet is een vuile sneeuwbal. Komt hij dicht bij de zon, dan verdampt er ijs en komt er stof los. Het licht en de zonnewind blazen dat weg, altijd recht van de zon af. Vliegt de komeet weer naar buiten, dan gaat zijn staart dus vóór hem uit. Vaak zijn er zelfs twee staarten: een rechte blauwe van gas en een gebogen witte van stof.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke maan is de grootste van het hele zonnestelsel?",
        "opties": [
            "Ganymedes, een maan van Jupiter",
            "Titan, een maan van Saturnus",
            "Europa, een maan van Jupiter",
            "Onze eigen maan, rond de aarde",
        ],
        "antwoord": 0,
        "uitleg": r"Ganymedes is met ruim \(5200\) km doorsnede groter dan de planeet Mercurius. Titan is maar een klein beetje kleiner en ook groter dan Mercurius. Onze maan staat op de vijfde plaats. Ganymedes is ook de enige maan met een eigen magneetveld, en onder zijn ijskorst zit vermoedelijk een zoute oceaan met meer water dan alle zeeën op aarde samen.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In \(2021\) vloog het helikoptertje Ingenuity als eerste toestel op een andere planeet. Waarom was vliegen op Mars zo moeilijk?",
        "opties": [
            "De lucht is er honderd keer dunner, dus de wieken vinden weinig houvast",
            "De zwaartekracht is er drie keer sterker dan bij ons op de aarde",
            "Het waait er altijd zo hard dat alles meteen omver wordt geblazen",
            "Het is er zo koud dat een motor meteen bevriest als hij stilvalt",
        ],
        "antwoord": 0,
        "uitleg": r"Op de grond van Mars is de lucht zo dun als bij ons op meer dan dertig kilometer hoogte. Ingenuity woog maar \(1{,}8\) kilo en draaide zijn wieken rond met \(2400\) toeren per minuut, vijf keer sneller dan een gewone helikopter. Het was gepland voor vijf vluchten van een paar minuten; het werden er tweeënzeventig.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een astronaut wordt in de ruimte een paar centimeter langer.",
        "antwoord": True,
        "uitleg": "Op aarde drukt de zwaartekracht de kussentjes tussen je wervels de hele dag een beetje plat; 's ochtends ben je daarom al iets langer dan 's avonds. In gewichtloosheid veren die kussentjes helemaal open, en een astronaut wint tot een paar centimeter. Terug op aarde krimpt hij weer, en hebben veel astronauten een tijdje rugpijn.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op de maan is het overdag ruim honderd graden en 's nachts ver onder nul. Waarom is dat verschil zo groot?",
        "opties": [
            "Er is geen dampkring die de warmte verdeelt en 's nachts vasthoudt",
            "De maan staat overdag een stuk dichter bij de zon dan 's nachts",
            "De maangrond is van metaal en geeft zijn warmte razendsnel af",
            "Er waait 's nachts een ijzige wind over het hele maanoppervlak",
        ],
        "antwoord": 0,
        "uitleg": r"Op aarde werkt de lucht als een deken: overdag verspreidt ze de warmte, 's nachts houdt ze die vast. Op de maan is er geen deken. Een maandag duurt bovendien twee weken, dus de grond bakt veertien dagen in de zon, tot zo'n \(120\) graden. Daarna volgen veertien dagen nacht, tot onder \(-170\) graden. Ruimtepakken moeten dus allebei aankunnen.",
    },
    {
        "type": "invultekst",
        "vraag": r"In \(1961\) vloog de eerste mens in de ruimte, een Rus. Wat was zijn achternaam?",
        "antwoord": ["Gagarin", "Gagarine", "Gagarien"],
        "uitleg": r"Joeri Gagarin draaide op \(12\) april \(1961\) in \(108\) minuten één rondje rond de aarde, in de capsule Vostok \(1\). Hij was \(27\) jaar en werd op slag wereldberoemd. Zijn eerste woord bij de start was 'Pojechali!', wat zoveel betekent als: daar gaan we!",
    },
    {
        "type": "invultekst",
        "vraag": r"Het ruimtestation ISS draait in ongeveer \(90\) minuten één keer rond de aarde. Hoeveel keer per etmaal van \(24\) uur ziet de bemanning de zon opkomen?",
        "antwoord": "16",
        "uitleg": r"Een etmaal telt \(24 \cdot 60 = 1440\) minuten, en \(1440 : 90 = 16\). Elke omloop brengt één zonsopgang en één zonsondergang, dus de bemanning ziet er zestien van elk, elke dag. Daarom leeft het ISS op een vaste klok, de Britse tijd, en hangen er verduisteringsgordijnen bij de slaapplaatsen.",
    },
]
