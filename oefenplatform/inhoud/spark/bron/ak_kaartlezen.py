# -*- coding: utf-8 -*-
"""De vragen voor "Een kaart lezen" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "lokaliseren, oriënteren en
situeren" (22,5 % van het examen, samen met [[ak_gradennet]]).

Deel 1 gaat over wat er op een kaart staat en hoe je het afleest: de titel, de
legende, de schaal, de noordpijl en de windstreken, en de hoogtelijnen. Ook het
verschil tussen een kaart, een plan, een luchtfoto en een satellietbeeld.
Deel 2 gaat over rekenen met de schaal, afstanden meten met de lijn- en de
breukschaal, en wat hoogtelijnen over het reliëf vertellen.

Twee dingen om in de gaten te houden als hier iets bijkomt. De getallen bij de
schaal zijn nagerekend en staan ook in `leerbundels/bron/controleer.py`; zet een
nieuwe rekenvraag daar mee bij. En de vragen moeten te maken zijn zonder dat er
een kaart bij ligt, want in het oefenplatform ligt er geen. Wie een vraag wil
schrijven waarbij je écht op een kaart moet aanwijzen, hoort die in de
oefenbundel thuis, niet hier.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je krijgt een kaart in handen en je wil eerst weten waarover ze gaat. Waar kijk je dan?",
        opties=[
            "Naar de titel",
            "Naar de schaal die eronder staat afgedrukt",
            "Naar de kleuren die het meest voorkomen",
            "Naar het aantal plaatsnamen dat erop staat",
        ],
        antwoord=0,
        uitleg="De titel zegt waarover de kaart gaat en welk gebied ze toont. Daarmee weet je meteen of je de juiste kaart voor je hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de legende van een kaart?",
        opties=[
            "Ze legt uit wat de tekens en de kleuren betekenen",
            "Ze vertelt het verhaal van de streek op de kaart",
            "Ze geeft de namen van alle dorpen in het gebied",
            "Ze toont hoeveel mensen er in het gebied wonen",
        ],
        antwoord=0,
        uitleg="Een kaart werkt met tekens en kleuren. De legende is het lijstje dat zegt wat elk teken en elke kleur voorstelt. Zonder legende kan je een kaart niet lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze dingen horen op een goede kaart te staan? Er zijn er meerdere juist.",
        opties=[
            "Een legende",
            "Een schaal",
            "Een noordpijl",
            "Het aantal inwoners van het gebied dat afgebeeld wordt",
            "De datum waarop jij het gebied bezocht hebt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een kaart hoort een titel, een legende, een schaal en een noordpijl te dragen. Het inwonertal en jouw bezoek horen daar niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een luchtfoto zie je het gebied zoals het er echt uitziet, op een kaart zie je tekens die iets voorstellen.",
        antwoord=True,
        uitleg="Dat is het verschil. Een luchtfoto is een opname van de werkelijkheid. Een kaart is getekend: daarop staat een bos als een groen vlak en een weg als een lijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een plan?",
        opties=[
            "Een kaart van een klein gebied, met veel details",
            "Een kaart waarop enkel de wegen aangeduid staan",
            "Een kaart die toont hoe een gebied er vroeger uitzag",
            "Een kaart waarop de hoogte met kleuren aangeduid is",
        ],
        antwoord=0,
        uitleg="Een plan toont een klein gebied, bijvoorbeeld een stadscentrum of een gebouw, en juist daardoor passen er veel details op.",
    ),
    dict(
        type="invultekst",
        vraag="Het pijltje dat op een kaart aanwijst waar het noorden ligt, noem je de ___.",
        antwoord="noordpijl",
        uitleg="De noordpijl zegt hoe de kaart georiënteerd is. Zonder die pijl weet je niet welke kant het noorden op is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier windstreken noemen we de hoofdwindstreken?",
        opties=[
            "Noord, oost, zuid en west",
            "Noord, noordoost, oost en zuidoost",
            "Links, rechts, boven en onder",
            "Noord, zuid, opwaarts en neerwaarts",
        ],
        antwoord=0,
        uitleg="De vier hoofdwindstreken zijn noord, oost, zuid en west. Daartussen liggen de tussenwindstreken zoals noordoost en zuidwest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je staat met je gezicht naar het noorden gedraaid. Wat ligt er dan achter je?",
        opties=[
            "Het zuiden",
            "Het oosten",
            "Het westen",
            "Dat hangt af van waar je op aarde staat",
        ],
        antwoord=0,
        uitleg="Noord en zuid liggen tegenover elkaar, net als oost en west. Kijk je naar het noorden, dan ligt het zuiden in je rug, het oosten rechts en het westen links.",
    ),
    dict(
        type="waarofniet",
        vraag="Op elke kaart ligt het noorden bovenaan.",
        antwoord=False,
        uitleg="Meestal wel, maar niet altijd. Daarom staat er een noordpijl op: die zegt hoe je de kaart moet houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bronnen tonen een gebied van bovenaf gezien? Er zijn er meerdere juist.",
        opties=[
            "Een kaart",
            "Een luchtfoto",
            "Een satellietbeeld",
            "Een foto die je op straat van een huis neemt",
            "Een tekst waarin de streek beschreven wordt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een kaart, een luchtfoto en een satellietbeeld kijken alle drie van boven naar beneden. Een gewone foto op straat kijkt er van opzij naar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hoogtelijn op een kaart?",
        opties=[
            "Een lijn door alle punten die even hoog liggen",
            "Een lijn die de kortste weg naar de top toont",
            "Een lijn die de grens van een gemeente aanduidt",
            "Een lijn die aangeeft waar het water naartoe loopt",
        ],
        antwoord=0,
        uitleg="Een hoogtelijn verbindt alle punten van dezelfde hoogte. Zo zie je op een platte kaart toch hoe hoog en hoe steil het gebied is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een kaart liggen de hoogtelijnen op een bepaalde plaats heel dicht bij elkaar. Wat betekent dat?",
        opties=[
            "Daar is de helling steil",
            "Daar liggen de dorpen dicht bij elkaar",
            "Daar is het gebied vlak en gemakkelijk begaanbaar",
            "Daar houdt de gemeente op en begint de volgende",
        ],
        antwoord=0,
        uitleg="Liggen de lijnen dicht bij elkaar, dan stijgt het terrein over een korte afstand veel: dat is een steile helling. Liggen ze ver uit elkaar, dan loopt het zacht.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee hoogtelijnen op dezelfde kaart kunnen elkaar nooit kruisen.",
        antwoord=True,
        uitleg="Dat kan niet. Op het snijpunt zou het terrein dan twee verschillende hoogtes tegelijk moeten hebben, en dat bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vanaf welk punt wordt de hoogte op een kaart geteld?",
        opties=[
            "Vanaf de zeespiegel",
            "Vanaf het laagste punt van het land",
            "Vanaf de bodem van de dichtste rivier",
            "Vanaf de plek waar de kaart getekend werd",
        ],
        antwoord=0,
        uitleg="Alle hoogtes op een kaart worden geteld vanaf de zeespiegel. Daarom schrijft men er soms bij: meter boven de zeespiegel.",
    ),
    dict(
        type="invultekst",
        vraag="Het hoogst gelegen punt van een gebied heet het ___ van dat gebied.",
        antwoord="hoogtepunt",
        uitleg="Op een kaart staat bij zo'n hoogtepunt vaak een stipje met het aantal meter erbij. Het hoogtepunt van België is het Signaal van Botrange.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dingen kan je afleiden van een kaart met hoogtelijnen? Er zijn er meerdere juist.",
        opties=[
            "Het hoogteverschil tussen twee punten",
            "Hoe steil een helling is",
            "Hoe hoog een plaats boven de zeespiegel ligt",
            "Hoe warm het er gemiddeld is in de zomer",
            "Hoeveel mensen er in het gebied wonen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hoogtelijnen gaan enkel over het reliëf: de hoogteligging, het hoogteverschil en de steilte. Over temperatuur of bevolking zeggen ze niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een luchtfoto heeft altijd een legende.",
        antwoord=False,
        uitleg="Een luchtfoto toont de werkelijkheid, dus er zijn geen tekens die uitgelegd moeten worden. Een legende hoort bij een getekende kaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een kompas?",
        opties=[
            "Om te weten welke kant het noorden op ligt",
            "Om de afstand tussen twee plaatsen te meten",
            "Om te weten hoe hoog je boven de zeespiegel staat",
            "Om te zien hoeveel graden het buiten precies is",
        ],
        antwoord=0,
        uitleg="De naald van een kompas wijst naar het noorden. Daarmee draai je jezelf en je kaart in de juiste richting: dat heet je oriënteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een windroos staat de letter O bij een van de richtingen. Welke richting is dat?",
        opties=[
            "Het oosten",
            "Het onderste punt van de kaart",
            "De richting waar de zon ondergaat",
            "De richting waar het altijd het koudst is",
        ],
        antwoord=0,
        uitleg="O staat voor oost, de kant waar de zon opkomt. De zon gaat onder in het westen, bij de W.",
    ),
    dict(
        type="invultekst",
        vraag="De windstreek die tussen het zuiden en het westen in ligt, heet het ___.",
        antwoord="zuidwesten",
        uitleg="Tussen twee hoofdwindstreken ligt telkens een tussenwindstreek: noordoost, zuidoost, zuidwest en noordwest.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de schaal van een kaart?",
        opties=[
            "Hoeveel keer het gebied verkleind is",
            "Hoe oud de gegevens op de kaart zijn",
            "Hoe groot het blad papier is waarop ze staat",
            "Hoeveel kilometer je moet stappen om er te raken",
        ],
        antwoord=0,
        uitleg="Een gebied past nooit op ware grootte op papier. De schaal zegt hoeveel keer alles verkleind werd, en daarmee kan je echte afstanden terugrekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een kaart staat de schaal 1 : 25 000. Wat betekent dat?",
        opties=[
            "Eén centimeter op de kaart is 25 000 centimeter in het echt",
            "Eén centimeter op de kaart is 25 000 meter in het echt",
            "Er passen 25 000 van die kaarten op het echte gebied",
            "De kaart werd 25 000 keer gedrukt voor de scholen",
        ],
        antwoord=0,
        uitleg="Een breukschaal rekent met dezelfde eenheid links en rechts. 1 : 25 000 wil zeggen dat één centimeter op papier overeenkomt met 25 000 centimeter in werkelijkheid.",
    ),
    dict(
        type="invultekst",
        vraag="Eén centimeter op een kaart met schaal 1 : 25 000 komt in werkelijkheid overeen met ___ meter.",
        antwoord="250",
        uitleg="25 000 centimeter is 250 meter, want honderd centimeter maakt één meter. Reken dus 25 000 gedeeld door 100.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een kaart met schaal 1 : 50 000 meet je tussen twee dorpen 3 centimeter. Hoe ver liggen ze in het echt uit elkaar?",
        opties=[
            "1,5 kilometer",
            "150 meter",
            "15 kilometer",
            "50 kilometer",
        ],
        antwoord=0,
        uitleg="Eén centimeter is hier 50 000 centimeter, dus 500 meter. Drie centimeter is dan 1500 meter, of 1,5 kilometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze schalen verkleinen het gebied sterker dan 1 : 50 000? Er zijn er meerdere juist.",
        opties=[
            "1 : 100 000",
            "1 : 250 000",
            "1 : 25 000",
            "1 : 10 000",
        ],
        antwoord=[0, 1],
        uitleg="Hoe groter het getal achter de dubbele punt, hoe sterker verkleind. 100 000 en 250 000 zijn groter dan 50 000, dus die verkleinen meer. Bij 25 000 en 10 000 is dat net minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke van deze kaarten zie je de meeste details van een dorp?",
        opties=[
            "Op een kaart met schaal 1 : 10 000",
            "Op een kaart met schaal 1 : 50 000",
            "Op een kaart met schaal 1 : 100 000",
            "Op een kaart met schaal 1 : 250 000",
        ],
        antwoord=0,
        uitleg="Hoe kleiner het getal achter de dubbele punt, hoe minder verkleind en hoe meer detail. Op 1 : 10 000 zie je zelfs losse gebouwen staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een lijnschaal?",
        opties=[
            "Een balkje met de echte afstand erbij geschreven",
            "Een lijn die de kaart in twee gelijke helften deelt",
            "Een lijn die je van de ene naar de andere stad trekt",
            "Een lijstje van alle afstanden tussen de grote steden",
        ],
        antwoord=0,
        uitleg="Bij een lijnschaal staat een balkje op de kaart waarop aangeduid is hoeveel meter of kilometer die lengte voorstelt. Je legt je meetlat ernaast en je leest af.",
    ),
    dict(
        type="waarofniet",
        vraag="Met een breukschaal kan je geen afstanden berekenen, daarvoor heb je altijd een lijnschaal nodig.",
        antwoord=False,
        uitleg="Ook met een breukschaal gaat dat prima. Je meet de afstand op de kaart en je vermenigvuldigt met het getal achter de dubbele punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heb je nodig om een afstand op een kaart uit te rekenen? Er zijn er meerdere juist.",
        opties=[
            "Een meetlat",
            "De schaal van de kaart",
            "Een kompas",
            "De legende van de kaart",
            "De titel van de kaart",
        ],
        antwoord=[0, 1],
        uitleg="Meten doe je met een meetlat, omrekenen doe je met de schaal. Het kompas dient om je te oriënteren, de legende om tekens te begrijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet 4 centimeter op een kaart met schaal 1 : 25 000. Hoeveel kilometer is dat in het echt?",
        opties=[
            "1 kilometer",
            "4 kilometer",
            "10 kilometer",
            "100 kilometer",
        ],
        antwoord=0,
        uitleg="Eén centimeter is hier 250 meter. Vier centimeter is dus 1000 meter, en dat is precies één kilometer.",
    ),
    dict(
        type="invultekst",
        vraag="Op een kaart met schaal 1 : 100 000 komt één centimeter overeen met ___ kilometer.",
        antwoord="1",
        uitleg="100 000 centimeter is 1000 meter, en dat is één kilometer. Daarom is 1 : 100 000 zo'n handige schaal om mee te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten hoe lang een bochtige weg is. Hoe meet je die het best op de kaart?",
        opties=[
            "Je volgt de bochten met een touwtje en meet dat daarna",
            "Je trekt een rechte lijn van het begin naar het einde",
            "Je meet de afstand tussen de twee dichtste dorpen",
            "Je telt hoeveel bochten er zijn en vermenigvuldigt dat",
        ],
        antwoord=0,
        uitleg="Een rechte lijn geeft de afstand in vogelvlucht, niet de weglengte. Leg een touwtje of een strookje papier in de bochten en meet dat pas daarna.",
    ),
    dict(
        type="waarofniet",
        vraag="De afstand in vogelvlucht is korter dan de afstand langs de weg.",
        antwoord=True,
        uitleg="In vogelvlucht ga je in rechte lijn. Een weg moet om heuvels, huizen en rivieren heen, en is dus altijd langer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gaat van de hoogtelijn van 100 meter naar die van 160 meter. Hoeveel stijg je?",
        opties=[
            "60 meter",
            "6 meter",
            "160 meter",
            "260 meter",
        ],
        antwoord=0,
        uitleg="Het hoogteverschil is het verschil tussen de twee hoogtes: 160 min 100 is 60 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een heuvel liggen de hoogtelijnen aan de ene kant ver uit elkaar en aan de andere kant dicht bijeen. Wat weet je daardoor?",
        opties=[
            "De kant met de lijnen dicht bijeen is de steilste",
            "De kant met de lijnen dicht bijeen is de laagste",
            "De kant met de lijnen ver uit elkaar is het hoogst",
            "De heuvel is aan beide kanten precies even steil",
        ],
        antwoord=0,
        uitleg="Dicht bijeen betekent veel hoogte over weinig afstand, dus steil. Een heuvel kan aan de ene kant zacht oplopen en aan de andere kant abrupt afbreken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reliëfvormen noemt de vakfiche? Er zijn er meerdere juist.",
        opties=[
            "De vlakte",
            "Het plateau",
            "De heuvel",
            "De rivier",
            "Het bos",
        ],
        antwoord=[0, 1, 2],
        uitleg="De reliëfvormen zijn de vlakte, het plateau, de heuvel of het heuvelland, en de berg of het gebergte. Een rivier en een bos horen bij andere lagen van het landschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plateau is een hooggelegen gebied met een sterk golvend oppervlak.",
        antwoord=False,
        uitleg="Een plateau ligt wel hoog, maar het is juist vlak bovenop. Het golvende zit in het heuvelland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een heuvel en een berg?",
        opties=[
            "Een berg is veel hoger en meestal steiler",
            "Een berg ligt altijd aan de kust en een heuvel niet",
            "Een berg is van steen en een heuvel van aarde gemaakt",
            "Een berg heeft een naam en een heuvel heeft er geen",
        ],
        antwoord=0,
        uitleg="Het onderscheid zit in de hoogte en de steilte. Meerdere bergen samen vormen een gebergte, meerdere heuvels een heuvelland.",
    ),
    dict(
        type="invultekst",
        vraag="De denkbeeldige lijn in de verte waar de lucht en de aarde elkaar lijken te raken, heet de ___.",
        antwoord="horizonlijn",
        uitleg="De horizonlijn hoort bij de reliëfelementen. Sta je op een vlakte, dan ligt ze laag en ver weg; sta je in een dal, dan wordt ze door de hellingen weggenomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hoogteverschil tussen twee punten is het verschil tussen hun hoogte boven de zeespiegel.",
        antwoord=True,
        uitleg="Ligt het ene punt op 340 meter en het andere op 120 meter, dan is het hoogteverschil 220 meter. Je trekt gewoon af.",
    ),
]
