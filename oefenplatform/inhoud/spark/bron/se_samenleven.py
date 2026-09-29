# -*- coding: utf-8 -*-
"""De vragen voor "Ik leef samen met anderen" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik leef samen met anderen"
(12,5 % van het examen): diversiteit, respectvol en constructief samenleven,
emoties, grenzen, relaties en seksualiteit, en samenwerken.

Deel 1 hoort bij een PRENT: een schoolplein waarop tegelijk van alles gebeurt.
Het examen werkt met situaties die je moet beoordelen, en dat is precies wat
zo'n beeld kan. Kim tekende de prent op 29 september 2026.

DE PRENT IS DE BRON. Wat erop staat is hieronder opgeschreven, nageteld op het
beeld zelf en uitvergroot. Maakt iemand later een nieuwe prent, dan kloppen de
vragen van deel 1 niet meer en moeten ze herschreven worden.

Wat er op de prent staat (nageteld op 29-09-2026):
- linksvoor: een meisje alleen op een houten bank, donkere hoodie, knieën
  opgetrokken, kin op haar hand, een verdrietige blik; haar grijze rugzak en
  een grijze drinkfles liggen naast haar;
- linksachter: twee jongens die voetballen, één in een groene hoodie en één in
  een witte, met een zwart-witte bal; daarachter een overdekte fietsenstalling
  met leerlingen en fietsen;
- midden: een meisje in een roze hoodie dat alleen voorbijstapt, en een blauwe
  vuilnisbak;
- midden: een groepje van vijf jongens. Eén jongen in een donkere hoodie kijkt
  naar de grond. Een blonde jongen in een zwarte hoodie lacht en wijst met
  gestrekte arm naar hem. Twee andere jongens lachen mee. Een jongen in een
  witte hoodie met rugzak legt zijn hand op de schouder van de jongen die naar
  de grond kijkt. Een meisje met lang blond haar staat ernaast met de armen
  gekruist en lacht niet mee;
- rechts: twee jongens die pingpongen aan een blauwe betonnen tafel, één in een
  blauwe hoodie en één in een witte; rechtsachter een groepje meisjes bij het
  gebouw;
- rechtsvoor: vier leerlingen die samen op de grond zitten te eten, met een
  roze brooddoos; ze praten en lachen met elkaar;
- het schoolgebouw met grote ramen en een basketbalring rechtsboven, bomen,
  struiken met bloemen, zonnig weer.

Deel 2 gaat over de leerstof zelf: diversiteit, pesten tegenover plagen,
groepsdruk en machtsmisbruik, grenzen, toestemming, en samenwerken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Kijk naar de groep jongens in het midden van de prent. Wat gebeurt daar?",
        opties=[
            "Eén jongen wordt uitgelachen door een groepje",
            "Een groepje jongens oefent samen een dansje in",
            "Twee jongens leggen een ruzie tussen hen bij",
            "Een groepje jongens wacht tot de bel gaat",
        ],
        antwoord=0,
        uitleg="Eén jongen kijkt naar de grond terwijl er naar hem gewezen wordt en anderen lachen. De aandacht is op hem gericht, en hij lacht als enige niet mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Is wat er met die jongen gebeurt pesten of plagen?",
        opties=[
            "Pesten, want het is één tegen een groep en hij vindt het niet leuk",
            "Plagen, want iedereen op de prent is duidelijk aan het lachen",
            "Een meningsverschil, want ze zijn het gewoon oneens",
            "Geen van beide, want er wordt niemand aangeraakt",
        ],
        antwoord=0,
        uitleg="Bij plagen vinden beide kanten het grappig en zijn ze gelijkwaardig. Hier staat één iemand tegenover een groep en houdt hij zijn hoofd naar beneden. Dat is pesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je op de prent dat de jongen in het midden zich niet goed voelt?",
        opties=[
            "Hij kijkt naar de grond in plaats van naar de anderen",
            "Hij lacht niet mee terwijl de anderen dat wel doen",
            "Hij staat als enige helemaal alleen aan de andere kant",
            "Hij loopt weg van de groep",
        ],
        antwoord=[0, 1],
        uitleg="Zijn hoofd naar beneden en het feit dat hij als enige niet lacht, zijn de twee signalen. Hij loopt niet weg en staat ook niet apart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een jongen in een witte hoodie legt zijn hand op de schouder van de jongen die naar de grond kijkt. Wat is dat?",
        opties=[
            "Een gepaste reactie, want hij zoekt contact met wie het moeilijk heeft",
            "Een ongepaste reactie, want hij bemoeit zich met iets van een ander",
            "Machtsmisbruik, want hij raakt iemand aan zonder te vragen",
            "Groepsdruk, want hij duwt de jongen richting de groep",
        ],
        antwoord=0,
        uitleg="Iemand die het moeilijk heeft niet in de steek laten, is een van de gepaste reacties bij pesten. Steun geven helpt meer dan meelachen of wegkijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Naast de groep staat een meisje met lang blond haar met haar armen gekruist. Ze lacht niet mee. Wat is haar rol?",
        opties=[
            "Ze is omstaander: ze ziet het gebeuren en doet niets",
            "Ze is het slachtoffer van wat er gebeurt",
            "Ze is degene die de pesterij begint",
            "Ze staat er toevallig en ziet niets van wat er gebeurt",
        ],
        antwoord=0,
        uitleg="Ze kijkt toe zonder mee te doen en zonder in te grijpen. Dat is de rol van omstaander. Wie niets doet, laat het stilzwijgend doorgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zou het meisje met de gekruiste armen kunnen doen dat wél een gepaste reactie is?",
        opties=[
            "Zeggen dat ze het niet oké vindt",
            "Er een volwassene bij halen",
            "Achteraf naar de jongen toe gaan en vragen hoe het gaat",
            "Er een filmpje van maken en doorsturen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Iets zeggen, hulp halen en achteraf steun geven zijn alle drie gepast. Een filmpje doorsturen maakt het net erger en verspreidt het verder.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de prent zit linksvoor een meisje alleen op een bank.",
        antwoord=True,
        uitleg="Klopt. Ze zit met opgetrokken knieën en haar kin op haar hand, met haar rugzak naast zich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het meisje op de bank zit alleen en kijkt bedrukt. Wat weet je daarmee zeker?",
        opties=[
            "Alleen dat ze op dit moment alleen zit",
            "Dat ze door de anderen wordt buitengesloten",
            "Dat ze geen enkele vriend op school heeft",
            "Dat ze ruzie heeft met de groep op de speelplaats",
        ],
        antwoord=0,
        uitleg="Je ziet wat er gebeurt, niet waarom. Alleen zitten kan ook een keuze zijn, of een slechte dag. Daarom vraag je het, in plaats van het in te vullen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel leerlingen zitten er rechtsvoor samen op de grond te eten?",
        opties=["Vier", "Twee", "Drie", "Zes"],
        antwoord=0,
        uitleg="Het zijn er vier: twee jongens en twee meisjes, met een roze brooddoos tussen hen in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken van een goede samenwerking herken je in dat groepje dat samen eet?",
        opties=[
            "Ze luisteren naar elkaar",
            "Ze spreken om de beurt",
            "Ze gebruiken gepaste lichaamstaal",
            "Ze houden hun rug naar elkaar toe",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ze zijn naar elkaar toegedraaid, kijken elkaar aan en praten om de beurt. Dat zijn drie kenmerken uit de vakfiche. Hun rug naar elkaar keren doen ze net niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Er wordt op de prent gevoetbald én gepingpongd.",
        antwoord=True,
        uitleg="Klopt. Linksachter spelen twee jongens met een bal, rechts spelen er twee pingpong aan een betonnen tafel.",
    ),
    dict(
        type="invultekst",
        vraag="Rechts spelen twee jongens een balspel aan een betonnen tafel met een netje. Welk spel is dat?",
        antwoord=["pingpong", "tafeltennis"],
        uitleg="Dat is pingpong, ook tafeltennis genoemd. Je herkent het aan het netje op de tafel en de batjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de prent is iedereen met dezelfde activiteit bezig.",
        antwoord=False,
        uitleg="Er gebeuren juist heel veel dingen tegelijk: voetballen, pingpongen, eten, praten, alleen zitten en uitlachen. Zo ziet een echte speelplaats eruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk om op zo'n speelplaats goed rond te kijken?",
        opties=[
            "Omdat je pas ziet wie erbuiten valt als je verder kijkt dan je eigen groepje",
            "Omdat je zo kan tellen hoeveel leerlingen er op school zitten",
            "Omdat de leerkracht daar punten voor geeft aan het einde van het jaar",
            "Omdat je dan weet welke spelletjes het populairst zijn",
        ],
        antwoord=0,
        uitleg="Wie alleen naar de eigen vrienden kijkt, mist het meisje op de bank en de jongen met zijn hoofd naar beneden. Rondkijken is de eerste stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="De blonde jongen wijst met gestrekte arm naar de jongen die naar de grond kijkt, terwijl twee anderen meelachen. Wat doen die twee anderen?",
        opties=[
            "Ze doen mee, en daardoor gaat het pesten door",
            "Ze komen tussen en maken er een einde aan",
            "Ze hebben niets met de situatie te maken",
            "Ze halen er iemand bij die kan helpen",
        ],
        antwoord=0,
        uitleg="Meelachen lijkt onschuldig, maar het geeft de pester gelijk. Wie meelacht, is deel van wat er gebeurt.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de prent loopt er een meisje in een roze hoodie alleen voorbij.",
        antwoord=True,
        uitleg="Klopt. Ze stapt in haar eentje over de speelplaats, met haar rugzak om.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt over deze prent: op een speelplaats hoort dit erbij, daar moet je niets van zeggen. Wat klopt daar niet aan?",
        opties=[
            "Dat iets vaak gebeurt, maakt het nog niet aanvaardbaar",
            "Dat er op een speelplaats nooit iets gebeurt",
            "Dat een speelplaats altijd een veilige plek is",
            "Dat leerlingen elkaar nooit uitlachen",
        ],
        antwoord=0,
        uitleg="Gewoon worden aan iets is niet hetzelfde als het goedkeuren. Juist omdat het vaak gebeurt, is het belangrijk er wel iets van te zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke basisemoties zie je op deze prent bij verschillende leerlingen?",
        opties=[
            "Verdriet",
            "Blijdschap",
            "Angst voor een dier",
            "Walging om een geur",
        ],
        antwoord=[0, 1],
        uitleg="Het meisje op de bank en de jongen met zijn hoofd naar beneden tonen verdriet; de spelende en etende leerlingen zijn blij. Van angst of walging is niets te zien.",
    ),
    dict(
        type="waarofniet",
        vraag="De jongen die naar de grond kijkt, lacht zelf ook mee.",
        antwoord=False,
        uitleg="Hij is de enige in dat groepje die niet lacht. Dat is precies het verschil tussen plagen en pesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de beste eerste vraag die je aan het meisje op de bank kan stellen?",
        opties=[
            "Is er iets, wil je erover praten?",
            "Waarom heb jij eigenlijk geen vrienden?",
            "Zit je hier altijd zo in je eentje?",
            "Wat is er met jou nu weer aan de hand?",
        ],
        antwoord=0,
        uitleg="Een open vraag zonder oordeel geeft haar de ruimte om te antwoorden of niet. De andere drie gaan er al van uit dat er iets mis is met haar.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent diversiteit?",
        opties=[
            "Dat mensen in een samenleving van elkaar verschillen",
            "Dat mensen in een samenleving allemaal gelijk zijn",
            "Dat iedereen in een land dezelfde taal spreekt",
            "Dat mensen uit hetzelfde land moeten komen",
        ],
        antwoord=0,
        uitleg="Diversiteit is de verscheidenheid tussen mensen: in afkomst, geloof, geld, gezin, wie ze graag zien. Iedereen is anders, en dat is normaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van diversiteit noemt de vakfiche?",
        opties=[
            "Sociale diversiteit",
            "Culturele diversiteit",
            "Religieuze of levensbeschouwelijke diversiteit",
            "Seksuele diversiteit",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Alle vier staan ze in de fiche. Sociaal gaat over geld en positie, cultureel over gewoontes, religieus over geloof en overtuiging, seksueel over wie je graag ziet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is samenleven in diversiteit soms moeilijk?",
        opties=[
            "Omdat verschillen kunnen leiden tot misverstanden en vooroordelen",
            "Omdat mensen die verschillen elkaars taal nooit kunnen leren",
            "Omdat er wetten zijn die verschillen verbieden",
            "Omdat er dan niemand meer dezelfde gewoontes heeft",
        ],
        antwoord=0,
        uitleg="Wat je niet kent, begrijp je makkelijk verkeerd. Daar ontstaan misverstanden en vooroordelen uit. Dat is de moeilijke kant, niet de onmogelijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan samenleven in diversiteit ook waardevol zijn?",
        opties=[
            "Je leert manieren van doen kennen die je zelf niet had bedacht",
            "Je moet nooit meer rekening houden met iemand anders",
            "Iedereen gaat dan vanzelf net hetzelfde denken",
            "Er zijn dan minder regels nodig op school",
        ],
        antwoord=0,
        uitleg="Verschil is leerrijk. Andere gewoontes, andere gerechten, andere manieren om iets aan te pakken: je wereld wordt er groter van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen plagen en pesten?",
        opties=[
            "Plagen gaat over en weer, pesten is één kant die de andere raakt",
            "Plagen gebeurt op school, pesten gebeurt online",
            "Plagen doe je met woorden, pesten doe je met je handen",
            "Plagen doen kinderen, pesten doen volwassenen",
        ],
        antwoord=0,
        uitleg="Bij plagen zijn beide kanten gelijkwaardig en vinden ze het allebei grappig. Bij pesten is er een machtsverschil en is het steeds dezelfde die het moet ondergaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meningsverschil?",
        opties=[
            "Twee mensen denken anders over iets en zeggen dat tegen elkaar",
            "Eén persoon wordt telkens opnieuw belachelijk gemaakt",
            "Een groep sluit iemand bewust uit van een activiteit",
            "Iemand gebruikt zijn positie om een ander iets op te leggen",
        ],
        antwoord=0,
        uitleg="Een meningsverschil is gewoon van mening verschillen. Dat hoort erbij en is niet hetzelfde als pesten of uitsluiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is groepsdruk?",
        opties=[
            "De druk om iets te doen omdat de groep het doet of verwacht",
            "De druk die je voelt vlak voor een toets op school",
            "De drukte op een speelplaats tijdens de middagpauze",
            "Het gewicht van een groep mensen op een klein oppervlak",
        ],
        antwoord=0,
        uitleg="Bij groepsdruk doe je iets niet omdat je het wil, maar omdat de groep het doet of van je verwacht. Dat kan de kant van goed of van fout op gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is machtsmisbruik?",
        opties=[
            "Je positie gebruiken om iemand iets op te leggen",
            "Een beslissing nemen omdat je daar het recht toe hebt",
            "Sterker zijn dan iemand anders in een sport",
            "Een functie krijgen waar verantwoordelijkheid bij hoort",
        ],
        antwoord=0,
        uitleg="Machtsmisbruik is je sterkere positie gebruiken tegen iemand die zich moeilijk kan verweren. Macht hebben op zich is geen misbruik.",
    ),
    dict(
        type="waarofniet",
        vraag="Iemand bewust niet uitnodigen om die persoon buiten de groep te houden, is uitsluiten.",
        antwoord=True,
        uitleg="Klopt. Uitsluiten hoeft geen woorden of duwen: iemand er stelselmatig buiten laten is genoeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is racisme?",
        opties=[
            "Mensen minder behandelen om hun afkomst of huidskleur",
            "Mensen uit verschillende landen met elkaar vergelijken",
            "Interesse hebben in de gewoontes van een andere cultuur",
            "Meer dan één taal spreken in hetzelfde gesprek",
        ],
        antwoord=0,
        uitleg="Racisme is een vorm van discriminatie die op afkomst of huidskleur speelt. Belangstelling voor een andere cultuur is net het tegenovergestelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand krijgt een stage niet omdat zijn naam buitenlands klinkt. Wat is dat?",
        opties=[
            "Discriminatie",
            "Groepsdruk",
            "Een meningsverschil",
            "Een gewone sollicitatie",
        ],
        antwoord=0,
        uitleg="Hij wordt slechter behandeld om een kenmerk dat niets met de stage te maken heeft. Dat is discriminatie, en ze is bij wet verboden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reacties op pesten zijn gepast?",
        opties=[
            "Er een volwassene bij halen die kan helpen",
            "Aan de gepeste laten weten dat je achter hem staat",
            "Duidelijk zeggen dat je het niet oké vindt",
            "Terugpesten zodat de pester het ook eens voelt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hulp halen, steunen en iets zeggen werken. Terugpesten maakt er twee slachtoffers van en lost niets op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke basisemoties bestaan er?",
        opties=[
            "Blijdschap, verdriet, angst, woede",
            "Honger, dorst, slaap, kou",
            "Slim, dom, snel, traag",
            "Lawaai, stilte, licht, donker",
        ],
        antwoord=0,
        uitleg="Basisemoties zijn gevoelens die iedereen kent, zoals blijdschap, verdriet, angst, woede, verbazing en walging. De andere rijtjes zijn geen gevoelens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een mentale grens?",
        opties=[
            "De grens van wat je van binnen nog aankan",
            "De grens die je met een streep op de grond tekent",
            "De grens tussen twee landen op een kaart",
            "De grens van hoe ver je kan lopen zonder moe te worden",
        ],
        antwoord=0,
        uitleg="Een mentale grens gaat over je gevoel en je gedachten: wat je nog aankan aan opmerkingen, druk of vragen. Een lichamelijke grens gaat over je lichaam.",
    ),
    dict(
        type="waarofniet",
        vraag="Iedereen heeft dezelfde grenzen liggen.",
        antwoord=False,
        uitleg="Grenzen verschillen van persoon tot persoon, en zelfs van dag tot dag. Daarom moet je ze vragen in plaats van ze te veronderstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij respectvol omgaan met elkaars lichaam?",
        opties=[
            "Toestemming: allebei akkoord en allebei goed erbij",
            "Vrijwillig: niemand zet de ander onder druk",
            "Gelijkwaardigheid: er is geen machtsverschil",
            "Snelheid: hoe sneller het gaat, hoe beter",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt toestemming, vrijwilligheid, gelijkwaardigheid, passend bij de leeftijd, passend in de situatie en zelfrespect. Snelheid staat er niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Toestemming die onder druk gegeven wordt, telt als een echte toestemming.",
        antwoord=False,
        uitleg="Nee. Toestemming moet vrijwillig zijn. Wie ja zegt omdat hij anders iets te verliezen heeft, heeft in feite geen keuze gehad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent zelfrespect in deze context?",
        opties=[
            "Dat je ook je eigen grenzen bewaakt",
            "Dat je altijd je zin krijgt in een groep",
            "Dat je nooit aan iemand iets vraagt",
            "Dat je jezelf beter vindt dan de anderen",
        ],
        antwoord=0,
        uitleg="Zelfrespect is dat je je eigen grenzen even serieus neemt als die van een ander. Respect gaat twee kanten op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken van een goede samenwerking noemt de vakfiche?",
        opties=[
            "Afspraken nakomen",
            "Hulp vragen wanneer iets niet duidelijk is",
            "Rekening houden met de inbreng van anderen",
            "Zo snel mogelijk zelf alles beslissen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt onder meer luisteren, om de beurt spreken, meningen respecteren, afspraken nakomen, hulp vragen en rekening houden met anderen. Alles zelf beslissen hoort daar niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Duidelijk en rustig communiceren is een kenmerk van een goede samenwerking.",
        antwoord=True,
        uitleg="Klopt, dat staat zo in de vakfiche. Rustig spreken maakt het voor iedereen makkelijker om te volgen en te reageren.",
    ),
]
