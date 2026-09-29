# -*- coding: utf-8 -*-
"""De vragen voor "Eerste hulp bij ongevallen" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik reageer correct in een
noodsituatie" (7,5 % van het examen). De fiche zegt erbij dat je op het examen
de handelingen niet uitvoert maar uitlegt, en dat je bronmateriaal krijgt.

Deel 1 gaat over de vier stappen, over wanneer je 112 belt, en over de stabiele
zijligging. Deel 2 gaat over verslikking, bloeding, verstuiking en wonden.

LET OP BIJ HET AANVULLEN. Dit is het enige thema van dit vak waar een fout
antwoord iemand echt kan schaden. Elke vraag hieronder volgt de richtlijnen van
het Rode Kruis. Wie hier iets bijschrijft, controleert dat eerst bij een
betrouwbare bron, en niet uit het hoofd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste van de vier stappen in eerste hulp?",
        opties=[
            "Zorgen voor veiligheid",
            "De toestand van het slachtoffer beoordelen",
            "Gespecialiseerde hulp raadplegen",
            "Verdere eerste hulp verlenen",
        ],
        antwoord=0,
        uitleg="Eerst veiligheid: voor jezelf, voor het slachtoffer en voor de omstaanders. Een tweede slachtoffer helpt niemand vooruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de juiste volgorde van de vier stappen in eerste hulp?",
        opties=[
            "Veiligheid, toestand beoordelen, hulp raadplegen, verdere hulp verlenen",
            "Hulp raadplegen, veiligheid, verdere hulp verlenen, toestand beoordelen",
            "Toestand beoordelen, veiligheid, verdere hulp verlenen, hulp raadplegen",
            "Verdere hulp verlenen, toestand beoordelen, veiligheid, hulp raadplegen",
        ],
        antwoord=0,
        uitleg="Die volgorde staat zo in de vakfiche. Ze is logisch: eerst mag er niets meer gebeuren, dan weet je wat er aan de hand is, dan haal je hulp, dan help je zelf verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom komt 'zorg voor veiligheid' vóór alle andere stappen?",
        opties=[
            "Omdat je niemand kan helpen als jij zelf gewond raakt",
            "Omdat de hulpdiensten anders niet willen komen helpen",
            "Omdat je anders geen ambulance mag bellen",
            "Omdat het slachtoffer anders wakker wordt",
        ],
        antwoord=0,
        uitleg="Wie zelf in gevaar loopt, wordt het tweede slachtoffer. Dan zijn er twee mensen die hulp nodig hebben in plaats van één.",
    ),
    dict(
        type="invultekst",
        vraag="Welk nummer bel je in België voor een ambulance of de brandweer?",
        antwoord="112",
        uitleg="112 is het noodnummer voor een ambulance en de brandweer, in heel Europa. Voor de politie is dat 101.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vertel je zeker als je 112 belt?",
        opties=[
            "Waar het gebeurd is, zo precies mogelijk",
            "Wat er gebeurd is en hoeveel slachtoffers er zijn",
            "In welke toestand het slachtoffer is",
            "Welk merk kleren het slachtoffer draagt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De plaats, wat er gebeurd is, hoeveel slachtoffers en hoe het met hen gaat: daarmee kan de centralist de juiste hulp sturen. Kleren doen niet ter zake.",
    ),
    dict(
        type="waarofniet",
        vraag="Je legt als eerste de telefoon neer als je 112 gebeld hebt.",
        antwoord=False,
        uitleg="Je blijft aan de lijn tot de centralist zegt dat je mag ophangen. Die kan je nog vragen stellen of uitleggen wat je ondertussen moet doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe controleer je of iemand bij bewustzijn is?",
        opties=[
            "Je spreekt de persoon luid aan en schudt aan de schouders",
            "Je giet een beker koud water over het gezicht van de persoon",
            "Je tilt de persoon meteen op en draagt hem naar buiten",
            "Je wacht een kwartier af om te zien of er iets verandert",
        ],
        antwoord=0,
        uitleg="Aanspreken en zachtjes aan de schouders schudden. Reageert de persoon niet, dan is hij bewusteloos en controleer je de ademhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer leg je iemand in stabiele zijligging?",
        opties=[
            "Als de persoon bewusteloos is maar wel normaal ademt",
            "Als de persoon bewusteloos is en niet meer ademt",
            "Als de persoon bij bewustzijn is en veel pijn heeft",
            "Als de persoon een gebroken been heeft",
        ],
        antwoord=0,
        uitleg="Bewusteloos én normaal ademend: dan legt de zijligging de luchtweg vrij. Ademt de persoon niet, dan begin je meteen te reanimeren en bel je 112.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom leg je een bewusteloos slachtoffer in stabiele zijligging?",
        opties=[
            "Zodat de luchtweg vrij blijft en braaksel kan weglopen",
            "Zodat de persoon het minder koud krijgt op de grond",
            "Zodat de hulpdiensten de persoon beter kunnen zien liggen",
            "Zodat de persoon sneller weer wakker wordt",
        ],
        antwoord=0,
        uitleg="Op de rug kan de tong naar achter zakken en kan braaksel in de luchtweg komen. Op de zij loopt alles vanzelf naar buiten en blijft de luchtweg open.",
    ),
    dict(
        type="waarofniet",
        vraag="Een slachtoffer in stabiele zijligging ligt met het hoofd lichtjes achterover en de mond naar beneden gericht.",
        antwoord=True,
        uitleg="Klopt. Het hoofd lichtjes achterover houdt de luchtweg open, en de mond naar beneden laat vocht naar buiten lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je laat een slachtoffer in stabiele zijligging daarna gerust alleen achter.",
        antwoord=False,
        uitleg="Je blijft bij het slachtoffer en controleert of het blijft ademen, tot de hulpdiensten er zijn. De toestand kan snel veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand valt flauw in de klas en reageert niet als je hem aanspreekt, maar ademt wel rustig. Wat doe je?",
        opties=[
            "Je legt hem in stabiele zijligging en belt 112",
            "Je zet hem rechtop in een stoel en geeft water",
            "Je laat hem liggen zoals hij ligt en gaat verder met de les",
            "Je geeft hem tikjes in het gezicht tot hij reageert",
        ],
        antwoord=0,
        uitleg="Bewusteloos en normaal ademend: stabiele zijligging en hulp bellen. Iemand die niet reageert mag je nooit laten drinken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je bij een ongeval aankomt en er nog gevaar is, bijvoorbeeld rondslingerende stukken glas?",
        opties=[
            "Je maakt het eerst veilig of je zorgt dat je zelf veilig staat",
            "Je loopt er meteen op af want tijd is belangrijk",
            "Je wacht rustig tot de hulpdiensten er over een half uur zijn",
            "Je roept van ver of alles in orde is en gaat weer weg",
        ],
        antwoord=0,
        uitleg="Stap één blijft stap één. Pas als het veilig is, ga je erbij. Wegblijven en niets doen is geen alternatief: je belt sowieso 112.",
    ),
    dict(
        type="waarofniet",
        vraag="Als er meerdere mensen bij een ongeval staan, mag je gerust aannemen dat iemand anders al gebeld heeft.",
        antwoord=False,
        uitleg="Dat denkt iedereen tegelijk, en dan belt er niemand. Wijs iemand persoonlijk aan en vraag om te bellen, of bel zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij stap twee, de toestand van het slachtoffer beoordelen?",
        opties=[
            "Nagaan of de persoon reageert als je hem aanspreekt",
            "Nagaan of de persoon normaal ademt",
            "Kijken of er ergens zwaar bloedverlies is",
            "Vragen welk gsm-nummer de persoon heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bewustzijn, ademhaling en ernstig bloedverlies: dat zijn de drie dingen die meteen tellen. De rest kan later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klasgenoot heeft zijn arm gebroken maar is helder en praat gewoon. Welke stap sla je NIET over?",
        opties=[
            "Gespecialiseerde hulp raadplegen",
            "Het slachtoffer zelf naar huis laten fietsen",
            "De arm zelf rechttrekken",
            "Wachten tot de pijn vanzelf weggaat",
        ],
        antwoord=0,
        uitleg="Ook als iemand helder is, hoort er hulp bij. Een gebroken arm mag je nooit zelf rechttrekken en zo iemand fietst niet naar huis.",
    ),
    dict(
        type="waarofniet",
        vraag="Eerste hulp verlenen betekent dat je helpt tot de hulpdiensten er zijn.",
        antwoord=True,
        uitleg="Eerste hulp overbrugt de tijd tot de professionele hulp er is. Je houdt de toestand stabiel en voorkomt dat het erger wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand heeft een ongeval gehad en ligt op de rijweg, maar het verkeer rijdt gewoon door. Wat is hier de eerste zorg?",
        opties=[
            "De plaats veilig maken, bijvoorbeeld met een gevarendriehoek",
            "Het slachtoffer meteen van de rijweg af slepen",
            "Foto's nemen van wat er precies gebeurd is",
            "Aan alle omstaanders vragen wie hier de schuld van heeft",
        ],
        antwoord=0,
        uitleg="Zolang er verkeer aankomt, is de plaats niet veilig. Iemand verplaatsen doe je alleen als er anders onmiddellijk levensgevaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over de vier stappen klopt?",
        opties=[
            "Je doorloopt ze in die volgorde, elke keer opnieuw",
            "Je kiest er telkens twee uit die je het beste lijken",
            "Ze gelden alleen bij een ongeval met een auto",
            "Ze gelden alleen als er geen volwassene in de buurt is",
        ],
        antwoord=0,
        uitleg="De vier stappen zijn een vaste volgorde die altijd geldt, bij elk ongeval. Zo vergeet je onder stress niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij twijfel over hoe ernstig iets is, bel je beter toch 112.",
        antwoord=True,
        uitleg="Klopt. De centralist aan de lijn is opgeleid om in te schatten wat er nodig is. Twijfelen en niet bellen is het grootste risico.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn rugslagen?",
        opties=[
            "Stevige slagen met de hiel van je hand tussen de schouderbladen",
            "Zachte tikjes in de nek om iemand rustiger te laten worden",
            "Stevige slagen op de onderrug om iemand rechtop te helpen",
            "Vriendelijke klopjes op de rug om iemand aan te moedigen",
        ],
        antwoord=0,
        uitleg="Bij een ernstige verslikking geef je vijf stevige slagen met de hiel van je hand tussen de schouderbladen, om het voorwerp los te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer geef je rugslagen en buikstoten?",
        opties=[
            "Bij een ernstige verslikking, als iemand niet meer kan hoesten of spreken",
            "Bij elke verslikking, ook als iemand nog goed kan hoesten en spreken",
            "Bij een bloedneus die niet vanzelf stopt",
            "Bij iemand die flauwgevallen is maar wel ademt",
        ],
        antwoord=0,
        uitleg="Kan iemand nog hoesten, dan moedig je hem net aan om te blijven hoesten. Pas als dat niet meer lukt, ga je over tot rugslagen en buikstoten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verslikt zich en hoest luid en krachtig. Wat doe je?",
        opties=[
            "Je moedigt hem aan om te blijven hoesten",
            "Je geeft meteen vijf stevige rugslagen",
            "Je geeft hem een groot glas water te drinken",
            "Je legt hem in stabiele zijligging",
        ],
        antwoord=0,
        uitleg="Hoesten is de sterkste manier om iets uit de luchtweg te krijgen. Slaan of water geven kan het voorwerp net dieper duwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een buikstoot?",
        opties=[
            "Een stevige ruk naar binnen en naar boven onder de ribben",
            "Een duw met de vlakke hand tegen de zijkant van de buik",
            "Een stevige druk op de buik terwijl iemand ligt",
            "Een klop met de vuist op de onderbuik",
        ],
        antwoord=0,
        uitleg="Je staat achter de persoon, zet je vuist boven de navel en trekt met de andere hand stevig naar binnen en naar boven. Zo pers je lucht uit de longen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een ernstige verslikking wissel je rugslagen en buikstoten met elkaar af.",
        antwoord=True,
        uitleg="Klopt: vijf rugslagen, dan vijf buikstoten, en zo verder tot het voorwerp eruit is of tot de persoon bewusteloos raakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een wonde die hevig bloedt?",
        opties=[
            "Je drukt stevig op de wonde met een verband of een propere doek",
            "Je spoelt de wonde uitgebreid met warm water uit de kraan",
            "Je laat de wonde open liggen zodat het bloed eruit kan lopen",
            "Je wrijft over de wonde zodat het bloed stolt",
        ],
        antwoord=0,
        uitleg="Rechtstreekse druk stopt een bloeding het snelst. Je houdt die druk aan, legt het slachtoffer neer en belt 112 bij zwaar bloedverlies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke symptomen horen bij een ernstige bloeding?",
        opties=[
            "Bloed dat blijft doorstromen ondanks druk",
            "Een bleke, klamme huid",
            "Een slachtoffer dat duizelig wordt",
            "Een slachtoffer dat plots erge honger krijgt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Doorbloeden, bleek en klam zijn en duizeligheid wijzen op fors bloedverlies. Honger hoort daar niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een brandwonde?",
        opties=[
            "Tien tot twintig minuten koelen met lauw zacht stromend water",
            "Een paar seconden koelen met ijsblokjes uit de diepvries",
            "Er boter of tandpasta op smeren tegen de pijn",
            "De blaar meteen doorprikken zodat het vocht eruit kan",
        ],
        antwoord=0,
        uitleg="Lauw stromend water, lang genoeg. IJs beschadigt de huid nog meer, en boter of tandpasta houdt de warmte net vast en maakt de wonde vuil.",
    ),
    dict(
        type="waarofniet",
        vraag="Kleding die aan een brandwonde vastgekleefd zit, trek je er voorzichtig af.",
        antwoord=False,
        uitleg="Vastgekleefde kleding laat je zitten: eraf trekken scheurt de huid mee. Je koelt er gewoon overheen en laat de rest aan de hulpverleners over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een gewone huidwonde, zoals een schaafwonde?",
        opties=[
            "Spoelen met water, ontsmetten en afdekken",
            "Ontsmetten, dan pas spoelen, dan open laten",
            "Meteen afdekken zonder eerst te spoelen",
            "Er stevig op wrijven tot het niet meer bloedt",
        ],
        antwoord=0,
        uitleg="Eerst spoelen om vuil weg te krijgen, dan ontsmetten, dan afdekken met een pleister of verband zodat er geen vuil meer bij kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke symptomen horen bij een verstuiking?",
        opties=[
            "Pijn bij het bewegen van het gewricht",
            "Een zwelling rond het gewricht",
            "Een blauwe verkleuring rond het gewricht",
            "Koorts die in korte tijd snel oploopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Pijn, zwelling en een blauwe plek zijn de klassieke tekenen van een verstuiking. Koorts hoort er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij een verstuikte enkel?",
        opties=[
            "Rust geven, koelen, een drukverband aanleggen en hoog leggen",
            "Gewoon blijven doorlopen zodat het gewricht soepel blijft",
            "De enkel warm inpakken met een kruik erbij",
            "Stevig masseren om de zwelling weg te duwen",
        ],
        antwoord=0,
        uitleg="Rust, ijs, drukverband en hoogstand. Warmte en masseren maken de zwelling net groter, en doorlopen verergert de schade.",
    ),
    dict(
        type="waarofniet",
        vraag="Een koelzak leg je nooit rechtstreeks op de blote huid.",
        antwoord=True,
        uitleg="Klopt. Doe er altijd een doek tussen, anders kan je de huid bevriezen. Koelen doe je in periodes van ongeveer twintig minuten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een verstuiking en een breuk?",
        opties=[
            "Bij een verstuiking zijn de banden gerekt, bij een breuk is het bot gebroken",
            "Bij een verstuiking is het bot gebroken, bij een breuk zijn de banden gerekt",
            "Een verstuiking doet pijn en een breuk niet",
            "Een verstuiking kan alleen aan de arm en een breuk alleen aan het been",
        ],
        antwoord=0,
        uitleg="Een verstuiking is schade aan de banden rond een gewricht, een breuk is schade aan het bot zelf. Van buitenaf lijken ze soms op elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij twijfel tussen een verstuiking en een breuk laat je het gewricht met rust en laat je het nakijken.",
        antwoord=True,
        uitleg="Klopt. Je kan het verschil van buitenaf niet zeker zien, dus behandel je het voorzichtig en laat je een arts kijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand snijdt zich in de keuken en er stroomt veel bloed uit zijn hand. Wat is de eerste handeling?",
        opties=[
            "Stevig drukken op de wonde met een propere doek",
            "Eerst een pleister zoeken in de kast",
            "De hand onder heet water houden",
            "De wonde ontsmetten voor je iets anders doet",
        ],
        antwoord=0,
        uitleg="Bij hevig bloeden komt de druk eerst. Ontsmetten en verzorgen doe je pas als het bloeden onder controle is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een ernstige verslikking van een baby jonger dan één jaar geef je buikstoten.",
        antwoord=False,
        uitleg="Bij een baby geef je rugslagen en borststoten, geen buikstoten. Buikstoten kunnen bij zo'n klein lichaam inwendige schade veroorzaken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je iemand die niet reageert nooit iets te drinken geven?",
        opties=[
            "Omdat de drank in de luchtweg kan komen",
            "Omdat drinken de bloeddruk te sterk verhoogt",
            "Omdat de hulpdiensten dan niet meer mogen helpen",
            "Omdat de persoon er nog dieper door in slaap valt",
        ],
        antwoord=0,
        uitleg="Wie niet bij bewustzijn is, kan niet goed slikken. Wat je geeft, kan in de longen terechtkomen. Dat geldt ook voor water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke ongevallen uit de vakfiche moet je de symptomen kunnen herkennen?",
        opties=[
            "Bloeding",
            "Verslikking",
            "Verstuiking",
            "Griep",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt bloeding, verslikking, verstuiking en wonden, zowel huidwonden als brandwonden. Griep is een ziekte, geen ongeval.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de houding waarin je een bewusteloos maar ademend slachtoffer legt? De stabiele ...",
        antwoord="zijligging",
        uitleg="De stabiele zijligging houdt de luchtweg vrij en laat vocht naar buiten lopen in plaats van naar de longen.",
    ),
]
