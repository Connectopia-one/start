# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Het oor en het evenwicht.

Hoort bij "waarnemen en verwerken van prikkels" van de vakfiche biologie
2de graad doorstroomfinaliteit. Dit onderdeel staat niet in de fiche
natuurwetenschappen en is dus volledig nieuw.

Deel 1 volgt het geluid door het uitwendige, het midden- en het inwendige
oor tot in het orgaan van Corti, en behandelt de afwijkingen die de fiche
opsomt. Deel 2 gaat over het evenwichtsorgaan: de positiezin, de rotatiezin
en de traagheid van de vloeistof.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie delen onderscheidt men bij het oor?",
        opties=[
            "het uitwendige oor, het middenoor en het inwendige oor",
            "het voorste oor, het bovenste oor en het achterste oor",
            "de oorschelp, de gehoorgang en het trommelvel",
            "het hoorgedeelte, het spraakgedeelte en het evenwichtsgedeelte",
        ],
        antwoord=0,
        uitleg="Het geluid gaat achtereenvolgens door die drie delen. Elk deel geeft het op zijn eigen manier door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen horen bij het uitwendige oor? Kruis alles aan wat juist is.",
        opties=[
            "de oorschelp",
            "de gehoorgang",
            "het trommelvel",
            "de gehoorbeentjes",
        ],
        antwoord=[0, 1, 2],
        uitleg="Oorschelp, gehoorgang en trommelvel vormen het uitwendige oor. De gehoorbeentjes liggen er net achter, in het middenoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van de oorschelp?",
        opties=[
            "het geluid opvangen en naar de gehoorgang leiden",
            "het geluid omzetten in zenuwimpulsen",
            "de druk aan beide kanten van het trommelvel gelijk houden",
            "het geluid versterken met drie kleine beentjes",
        ],
        antwoord=0,
        uitleg="De oorschelp werkt als een trechter. Haar vorm helpt ook om te horen uit welke richting een geluid komt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het dunne vel aan het einde van de gehoorgang dat door het geluid in beweging komt?",
        antwoord=["trommelvel", "het trommelvel", "trommelvlies"],
        uitleg="Het trommelvel trilt mee op de geluidsgolven, net als het vel van een trommel. Die trilling geeft het door aan de gehoorbeentjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heten de drie gehoorbeentjes in het middenoor?",
        opties=[
            "hamer, aambeeld en stijgbeugel",
            "hamer, beitel en zaag",
            "stijgbeugel, spaakbeen en ellebeen",
            "aambeeld, slakkenhuis en sleutelbeen",
        ],
        antwoord=0,
        uitleg="De namen komen van hun vorm. Ze vormen een kettinkje van het trommelvel naar het inwendige oor.",
    ),
    dict(
        type="waarofniet",
        vraag="De gehoorbeentjes versterken de trilling van het trommelvel.",
        antwoord=True,
        uitleg="Ze werken als een hefboomsysteem en brengen de trilling van een groot vel naar een klein venstertje. Daardoor wordt de druk veel groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de buis van Eustachius?",
        opties=[
            "ze verbindt het middenoor met de neus-keelholte om de druk gelijk te houden",
            "ze brengt de trillingen van het trommelvel naar het slakkenhuis",
            "ze voert het oorsmeer uit de gehoorgang naar buiten",
            "ze vangt de rotatie van het hoofd op",
        ],
        antwoord=0,
        uitleg="Zonder die buis zou het trommelvel bij elke drukverandering bollen. Daarom helpt slikken of gapen als je oren in een vliegtuig dichtzitten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het spiraalvormige deel van het inwendige oor waarin het gehoor zit?",
        antwoord=["slakkenhuis", "het slakkenhuis", "cochlea"],
        uitleg="Het slakkenhuis of de cochlea is een met vloeistof gevulde buis die opgerold ligt als een slakkenschelp. Daarin ligt het orgaan van Corti.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar liggen de haarcellen die het geluid in zenuwimpulsen omzetten?",
        opties=[
            "in het orgaan van Corti in het slakkenhuis",
            "op het trommelvel, net achter de gehoorgang",
            "op de steel van de hamer in het middenoor",
            "in de buis van Eustachius naar de neus-keelholte",
        ],
        antwoord=0,
        uitleg="Het orgaan van Corti ligt op het basilaire membraan in het slakkenhuis. De haarcellen erin buigen mee met de vloeistofgolf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de weg van het geluid in de juiste orde.",
        opties=[
            "oorschelp, gehoorgang, trommelvel, gehoorbeentjes, slakkenhuis, gehoorzenuw",
            "gehoorgang, trommelvel, slakkenhuis, gehoorbeentjes, oorschelp, gehoorzenuw",
            "trommelvel, oorschelp, gehoorbeentjes, gehoorzenuw, slakkenhuis, gehoorgang",
            "oorschelp, gehoorbeentjes, gehoorgang, slakkenhuis, trommelvel, gehoorzenuw",
        ],
        antwoord=0,
        uitleg="Lucht trilt, dan een vel, dan beentjes, dan vloeistof, dan een haarcel, dan een zenuw. Bij elke stap verandert het geluid van vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="In het slakkenhuis reist het geluid verder door de lucht, net als in de gehoorgang.",
        antwoord=False,
        uitleg="Het slakkenhuis is met vloeistof gevuld. De stijgbeugel duwt op een venstertje en zet die vloeistof in beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoor je een hoge toon op een andere plaats in het slakkenhuis dan een lage toon?",
        opties=[
            "het membraan is niet overal even stijf, dus komt elke toonhoogte elders in trilling",
            "hoge tonen gaan sneller door de vloeistof dan lage tonen",
            "hoge tonen worden door de hamer en lage tonen door het aambeeld doorgegeven",
            "het slakkenhuis draait voor een hoge toon in de andere richting",
        ],
        antwoord=0,
        uitleg="Bij het begin is het membraan smal en stijf, verderop breed en slap. Daardoor heeft elke plaats haar eigen toonhoogte.",
    ),
    dict(
        type="invultekst",
        vraag="Welke zenuw brengt de geluidsimpulsen naar de hersenen?",
        antwoord=["gehoorzenuw", "de gehoorzenuw"],
        uitleg="De gehoorzenuw vertrekt bij de haarcellen en loopt naar de hersenschors, waar je het geluid pas als klank herkent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan geleidingsslechthorendheid veroorzaken? Kruis alles aan wat juist is.",
        opties=[
            "een prop oorsmeer in de gehoorgang",
            "een gaatje in het trommelvel",
            "vocht in het middenoor na een ontsteking",
            "beschadigde haarcellen in het slakkenhuis",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij geleidingsslechthorendheid raakt het geluid niet goed tot in het inwendige oor. Beschadigde haarcellen geven een andere soort slechthorendheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Haarcellen die door hard geluid beschadigd zijn, groeien bij de mens niet meer terug.",
        antwoord=True,
        uitleg="Daarom is gehoorschade blijvend. Oordopjes op een festival of in een werkplaats zijn dus geen overdreven voorzichtigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort iemand met ouderdomsslechthorendheid vooral de hoge tonen minder?",
        opties=[
            "de haarcellen voor hoge tonen staan vooraan in het slakkenhuis en krijgen alle geluid te verwerken",
            "hoge tonen komen met de jaren niet meer door het trommelvel heen naar het middenoor",
            "de gehoorbeentjes groeien met de jaren aan elkaar vast en geven de trilling niet meer door",
            "de gehoorzenuw geeft hoge tonen enkel bij kinderen door en verliest dat vermogen later",
        ],
        antwoord=0,
        uitleg="Alle geluid gaat eerst langs het begin van het slakkenhuis, waar de hoge tonen gevoeld worden. Die cellen slijten dus het snelst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoortoestel herstelt beschadigde haarcellen.",
        antwoord=False,
        uitleg="Een hoortoestel versterkt enkel het geluid, zodat de cellen die nog werken meer te verwerken krijgen. Herstellen doet het niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beschermt het oor zich tegen aanhoudend hard geluid?",
        opties=[
            "kleine spiertjes in het middenoor spannen de keten van beentjes zodat die minder doorgeeft",
            "het trommelvel wordt dikker zolang het lawaai duurt en laat dan minder trilling door",
            "de gehoorgang sluit zich volledig af zolang het geluid boven een bepaalde grens blijft",
            "het slakkenhuis loopt tijdelijk leeg, zodat de golf de haarcellen niet meer bereikt",
        ],
        antwoord=0,
        uitleg="Die reflex dempt de overdracht, maar werkt pas na een fractie van een seconde en niet sterk genoeg. Bij een knal of urenlang lawaai helpt hij dus weinig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is oorsuizen of tinnitus?",
        opties=[
            "een geluid horen dat er van buiten niet is, vaak na gehoorschade",
            "een oorontsteking met vocht achter het trommelvel",
            "het gevoel dat de kamer blijft draaien na een rondje",
            "het dichtzitten van de oren bij het landen van een vliegtuig",
        ],
        antwoord=0,
        uitleg="Bij tinnitus geven beschadigde haarcellen of de zenuwbaan signalen door zonder prikkel. Je hoort dan een piep of gesuis.",
    ),
    dict(
        type="waarofniet",
        vraag="Horen gebeurt pas echt in de hersenen en niet al in het slakkenhuis.",
        antwoord=True,
        uitleg="Het slakkenhuis levert impulsen; de hersenschors maakt daar spraak, muziek of lawaai van. Daarom kan je een stem uit een rumoerige zaal pikken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welk orgaan ligt naast het slakkenhuis in het inwendige oor?",
        opties=[
            "het evenwichtsorgaan",
            "de buis van Eustachius",
            "de gele vlek",
            "de eilandjes van Langerhans",
        ],
        antwoord=0,
        uitleg="Gehoor en evenwicht zitten in hetzelfde benige doosje in de schedel. Daarom kan één aandoening beide tegelijk raken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee zintuiglijke taken heeft het evenwichtsorgaan?",
        opties=[
            "de positiezin en de rotatiezin",
            "de tastzin en de pijnzin",
            "de kleurzin en de diepte",
            "de reukzin en de smaakzin",
        ],
        antwoord=0,
        uitleg="De positiezin zegt hoe je hoofd staat, de rotatiezin of en hoe het draait. Samen weet je waar je bent in de ruimte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel halfcirkelvormige kanaaltjes heeft het evenwichtsorgaan per oor?",
        antwoord=["drie", "3"],
        uitleg="De drie kanaaltjes staan loodrecht op elkaar, zoals drie zijden van een hoek. Zo wordt elke draairichting opgevangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan de drie kanaaltjes loodrecht op elkaar?",
        opties=[
            "zo kan elke draairichting van het hoofd opgevangen worden",
            "zo passen ze het best in de kleine ruimte van de schedel",
            "zo kan de vloeistof van het ene naar het andere stromen",
            "zo blijven de haarcellen in alle drie even koud",
        ],
        antwoord=0,
        uitleg="Draaien gebeurt in drie richtingen: knikken, kantelen en rondkijken. Met drie kanalen in drie vlakken wordt elke draai gemeten.",
    ),
    dict(
        type="waarofniet",
        vraag="In de kanaaltjes van het evenwichtsorgaan zit vloeistof.",
        antwoord=True,
        uitleg="Die vloeistof blijft door haar traagheid even achter als het hoofd begint te draaien. Net die achterstand wordt gevoeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe merkt het oor dat je hoofd begint te draaien?",
        opties=[
            "de vloeistof blijft door haar traagheid achter en buigt de haarcellen om",
            "de haarcellen voelen de luchtdruk in het middenoor stijgen",
            "de gehoorbeentjes kantelen mee met het hoofd",
            "het trommelvel bolt naar binnen bij elke draai",
        ],
        antwoord=0,
        uitleg="Het bot draait mee met je hoofd, maar de vloeistof komt pas later op gang. Dat verschil duwt de haartjes om en levert een signaal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eigenschap van de vloeistof waardoor ze bij een draai even achterblijft?",
        antwoord=["traagheid", "de traagheid", "inertie"],
        uitleg="Traagheid is de neiging van materie om haar beweging te houden. Daardoor loopt de vloeistof achter op het kanaal dat haar omsluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je draait een hele tijd rond en stopt plots. Waarom blijf je dan duizelig?",
        opties=[
            "de vloeistof draait nog door en meldt dus een draai die er niet meer is",
            "de haarcellen zijn door het draaien blijvend beschadigd",
            "het trommelvel heeft tijd nodig om terug te komen",
            "de gehoorzenuw raakt bij draaien tijdelijk los van het slakkenhuis",
        ],
        antwoord=0,
        uitleg="Het kanaal staat stil, de vloeistof niet. Je ogen zeggen stil en je oor zegt draaien, en dat botsende bericht voelt als duizeligheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de positiezin van het evenwichtsorgaan?",
        opties=[
            "de stand van je hoofd ten opzichte van de zwaartekracht",
            "de toonhoogte van het geluid dat binnenkomt",
            "de afstand tot het voorwerp waar je naar kijkt",
            "de temperatuur van de vloeistof in het slakkenhuis",
        ],
        antwoord=0,
        uitleg="In de zakjes van het evenwichtsorgaan liggen gewichtjes op de haarcellen. Kantelt je hoofd, dan glijden die mee en weet je hoe je staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Het evenwichtsorgaan werkt ook als je je ogen dichthoudt.",
        antwoord=True,
        uitleg="Daarom weet je met gesloten ogen nog welke kant boven is. Op één been staan wordt dan wel moeilijker, want de ogen hielpen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke informatie gebruiken je hersenen om je evenwicht te bewaren? Kruis alles aan wat juist is.",
        opties=[
            "de signalen van het evenwichtsorgaan",
            "wat je ogen zien",
            "de rek in spieren en gewrichten",
            "de toonhoogte van het geluid om je heen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Oor, ogen en lichaamsgevoel leveren elk een stuk, en de kleine hersenen leggen die samen. Geluid speelt daarbij geen rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom word je soms wagenziek als je in een rijdende auto leest?",
        opties=[
            "je oor meldt beweging terwijl je ogen een stilstaand blad zien",
            "het trommelvel komt in de auto onder te hoge druk te staan",
            "je oren horen de motor te luid en dat verstoort het evenwicht",
            "de vloeistof in het slakkenhuis loopt bij rijden naar één kant",
        ],
        antwoord=0,
        uitleg="Je hersenen krijgen twee tegenstrijdige berichten. Dat conflict geeft misselijkheid, en naar buiten kijken helpt omdat de berichten dan weer kloppen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ontsteking in het inwendige oor kan zowel het gehoor als het evenwicht aantasten.",
        antwoord=True,
        uitleg="Gehoor en evenwicht liggen vlak bij elkaar en delen hun zenuw naar de hersenen. Daarom gaat zo'n ontsteking vaak met duizeligheid en slechter horen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol spelen de kleine hersenen bij het evenwicht?",
        opties=[
            "ze leggen de signalen van oor, ogen en spieren samen en stemmen de beweging erop af",
            "ze maken de vloeistof aan die in de kanaaltjes zit",
            "ze vangen zelf de draaiing van het hoofd op",
            "ze regelen de luchtdruk in het middenoor",
        ],
        antwoord=0,
        uitleg="De kleine hersenen zijn de regelkamer van het evenwicht. Daarom valt iemand met schade aan dat deel moeilijk recht te houden.",
    ),
    dict(
        type="invultekst",
        vraag="Welk zintuig naast het oor helpt je het meest om recht te blijven staan?",
        antwoord=["ogen", "de ogen", "zicht"],
        uitleg="Je ogen geven een vast punt in de kamer. Doe ze dicht terwijl je op één been staat, en je merkt hoeveel ze meehelpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een danser draait snel rond en blijft toch recht. Hoe lukt dat?",
        opties=[
            "door oefening leren de hersenen de signalen van het oor anders te wegen",
            "het evenwichtsorgaan van een danser heeft meer dan drie kanaaltjes",
            "de vloeistof in de kanaaltjes wordt door oefening dikker",
            "een danser gebruikt het evenwichtsorgaan helemaal niet meer",
        ],
        antwoord=0,
        uitleg="Het orgaan zelf blijft hetzelfde; de verwerking verandert. Dansers prikken bovendien met hun blik telkens een vast punt aan.",
    ),
    dict(
        type="waarofniet",
        vraag="De positiezin zit in het slakkenhuis en de rotatiezin in het evenwichtsorgaan.",
        antwoord=False,
        uitleg="Beide zitten in het evenwichtsorgaan: de positiezin in de zakjes met gewichtjes, de rotatiezin in de drie kanaaltjes. Het slakkenhuis dient voor het gehoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de haarcellen in het slakkenhuis en die in het evenwichtsorgaan gemeen? Kruis alles aan wat juist is.",
        opties=[
            "ze vangen beweging van vloeistof op",
            "ze zetten die beweging om in zenuwimpulsen",
            "ze liggen beide in het inwendige oor",
            "ze reageren beide op de toonhoogte van geluid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het is in beide gevallen hetzelfde principe: een haartje dat omgebogen wordt, wekt een impuls op. Enkel de haarcellen in het slakkenhuis gaan over toonhoogte.",
    ),
    dict(
        type="waarofniet",
        vraag="Het evenwichtsorgaan stuurt zijn signalen rechtstreeks naar de spieren zonder langs het centrale zenuwstelsel te gaan.",
        antwoord=False,
        uitleg="De signalen gaan eerst naar de hersenstam en de kleine hersenen. Pas daar wordt beslist welke spier moet bijsturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand stapt in het donker over een oneffen pad en struikelt sneller dan bij daglicht. Waarom?",
        opties=[
            "een van de drie bronnen van evenwichtsinformatie valt weg, dus wordt bijsturen moeilijker",
            "het evenwichtsorgaan werkt in het donker helemaal niet",
            "de haarcellen hebben licht nodig om een impuls op te wekken",
            "de vloeistof in de kanaaltjes wordt in het donker stijver",
        ],
        antwoord=0,
        uitleg="Zonder zicht blijven enkel het oor en het lichaamsgevoel over. Dat volstaat op een vlakke vloer, maar niet op een pad vol kuilen.",
    ),
]
