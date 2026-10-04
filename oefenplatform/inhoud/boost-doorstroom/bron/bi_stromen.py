# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Materie- en energiestromen in een ecosysteem.

Hoort bij de kop "materie- en energiestromen" van de vakfiche biologie
2de graad doorstroomfinaliteit. Dat onderdeel weegt 15 % van het examen en
is daarom over twee thema's gespreid: dit thema en de kringlopen.

Deel 1 gaat over de cel als plaats waar stoffen en energie omgezet worden:
fotosynthese, celademhaling en gisting, en het verband tussen die drie.
Deel 2 gaat over het ecosysteem: producenten, consumenten en reducenten,
voedselketens en voedselwebben, en de energiepiramide.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een autotroof en een heterotroof organisme?",
        opties=[
            "een autotroof maakt zijn eigen organische stoffen, een heterotroof moet ze opnemen",
            "een autotroof leeft in water en een heterotroof op het land",
            "een autotroof bestaat uit één cel en een heterotroof uit meer cellen",
            "een autotroof heeft geen energie nodig en een heterotroof wel",
        ],
        antwoord=0,
        uitleg="Autotroof betekent zelfvoedend. Groene planten bouwen hun eigen glucose; dieren en schimmels moeten die uit hun voedsel halen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke energiebron gebruikt een groene plant om haar eigen voedsel te maken?",
        antwoord=["zonlicht", "licht", "het zonlicht"],
        uitleg="Bij de fotosynthese vangt het chlorofyl lichtenergie op. Die energie komt in de glucose terecht als chemische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn de grondstoffen van de fotosynthese?",
        opties=[
            "koolstofdioxide en water",
            "glucose en zuurstofgas",
            "stikstofgas en water",
            "glucose en koolstofdioxide",
        ],
        antwoord=0,
        uitleg="De plant haalt koolstofdioxide uit de lucht en water uit de bodem. Met lichtenergie bouwt ze daar glucose van, en zuurstofgas blijft over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de fotosynthese komt zuurstofgas vrij.",
        antwoord=True,
        uitleg="Het zuurstofgas komt van het gesplitste water. Zo goed als alle zuurstof in onze lucht is door fotosynthese gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat levert de celademhaling op?",
        opties=[
            "energie voor de cel, plus koolstofdioxide en water",
            "glucose en zuurstofgas",
            "lichtenergie en water",
            "glucose en koolstofdioxide",
        ],
        antwoord=0,
        uitleg="Bij de celademhaling wordt glucose met zuurstofgas afgebroken. De energie die daarbij vrijkomt, gebruikt de cel voor haar werk.",
    ),
    dict(
        type="invultekst",
        vraag="In welk celorganel gebeurt de celademhaling?",
        antwoord=["mitochondrion", "mitochondriën", "het mitochondrion"],
        uitleg="Het mitochondrion is de energiecentrale van de cel. Cellen die veel werken, zoals spiercellen, hebben er veel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over fotosynthese en celademhaling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de producten van het ene zijn de grondstoffen van het andere",
            "fotosynthese slaat energie op en celademhaling maakt ze vrij",
            "een plantencel doet beide",
            "een dierlijke cel doet beide",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een plant doet fotosynthese én ademt, want ook zij heeft energie nodig. Een dierlijke cel doet enkel celademhaling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant doet enkel fotosynthese en geen celademhaling.",
        antwoord=False,
        uitleg="Ook een plant moet energie vrijmaken voor haar groei en haar transport. Bij daglicht maakt ze alleen meer glucose dan ze opstookt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft een plant bij daglicht netto zuurstofgas af en in het donker netto koolstofdioxide?",
        opties=[
            "bij licht overheerst de fotosynthese, in het donker valt ze weg",
            "een plant ademt enkel in het donker en nooit bij daglicht",
            "een plant doet fotosynthese ook in het donker, maar dan trager",
            "de huidmondjes staan in het donker helemaal dicht",
        ],
        antwoord=0,
        uitleg="De celademhaling loopt dag en nacht. Bij licht wordt ze overstemd door de fotosynthese, en in het donker blijft ze alleen over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de afbraak van glucose zonder zuurstofgas?",
        antwoord=["gisting", "de gisting", "fermentatie"],
        uitleg="Bij gisting wordt glucose maar gedeeltelijk afgebroken. Er komt dus veel minder energie vrij dan bij de celademhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat levert alcoholgisting door gist op?",
        opties=[
            "ethanol en koolstofdioxide",
            "melkzuur en water",
            "glucose en zuurstofgas",
            "water en koolstofdioxide",
        ],
        antwoord=0,
        uitleg="Daarom gebruikt men gist voor bier en wijn, en ook voor brood: het gas blaast het deeg op en de alcohol verdampt in de oven.",
    ),
    dict(
        type="waarofniet",
        vraag="Gisting levert per molecule glucose veel minder energie op dan de celademhaling.",
        antwoord=True,
        uitleg="Bij gisting blijft er nog energie in de ethanol of het melkzuur zitten. Pas met zuurstofgas wordt de glucose helemaal afgebroken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom krijg je bij een zware sprint een branderig gevoel in je benen?",
        opties=[
            "de spieren schakelen bij zuurstofgebrek over op melkzuurgisting",
            "de spieren stoppen met de celademhaling en gaan fotosynthetiseren",
            "de mitochondriën verlaten de spiercellen",
            "de spieren nemen water op uit het bloed",
        ],
        antwoord=0,
        uitleg="Bij een sprint komt er niet snel genoeg zuurstof binnen. De spier breekt glucose dan onvolledig af, en het melkzuur dat overblijft, voelt branderig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van alle chemische omzettingen in een organisme?",
        antwoord=["stofwisseling", "metabolisme", "de stofwisseling"],
        uitleg="De stofwisseling omvat zowel het opbouwen van stoffen als het afbreken ervan. Beide gebeuren voortdurend in elke cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen in ons voedsel leveren energie? Kruis alles aan wat juist is.",
        opties=[
            "koolhydraten",
            "vetten",
            "proteïnen",
            "mineralen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Koolhydraten, vetten en proteïnen kan het lichaam afbreken voor energie. Mineralen en vitaminen zijn nodig, maar leveren geen energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Koolhydraten leveren per gram meer energie dan vetten.",
        antwoord=False,
        uitleg="Vetten leveren per gram meer. Daarom slaat het lichaam zijn reserve vooral als vet op: dat weegt voor dezelfde energie minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een enzym in een cel?",
        opties=[
            "het versnelt een bepaalde omzetting zonder er zelf bij op te gaan",
            "het levert de energie voor een omzetting",
            "het vervoert stoffen door de celmembraan",
            "het slaat de erfelijke informatie op",
        ],
        antwoord=0,
        uitleg="Een enzym is een biokatalysator. Het past op één bepaalde stof, zodat de reactie bij lichaamstemperatuur snel genoeg verloopt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een enzym werkt het best binnen een nauw gebied van temperatuur en zuurtegraad.",
        antwoord=True,
        uitleg="Buiten dat gebied verliest het zijn vorm en past het niet meer op zijn stof. Daarom is koorts gevaarlijk en werkt maagenzym enkel in zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker zet een waterplant in een buisje in het licht en meet de gasbelletjes. Wat meet zij?",
        opties=[
            "het zuurstofgas dat bij de fotosynthese vrijkomt",
            "het koolstofdioxide dat bij de celademhaling vrijkomt",
            "de waterdamp die uit het blad verdampt",
            "het stikstofgas dat de plant uit de bodem haalt",
        ],
        antwoord=0,
        uitleg="Bij licht overheerst de fotosynthese, en het gas dat dan vrijkomt is zuurstofgas. Zet je de lamp verder weg, dan komen er minder belletjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde onderzoeker verdubbelt de lichtsterkte en ziet het aantal belletjes niet verder stijgen. Wat besluit je?",
        opties=[
            "een andere factor, zoals het koolstofdioxide, is nu de beperkende factor",
            "de plant doet geen fotosynthese meer",
            "licht speelt geen rol bij de fotosynthese",
            "de plant is door het licht beschadigd geraakt",
        ],
        antwoord=0,
        uitleg="Het proces loopt maar zo snel als zijn krapste grondstof toelaat. Boven een bepaalde lichtsterkte wordt niet het licht maar iets anders de rem.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie rollen onderscheidt men in een ecosysteem?",
        opties=[
            "producenten, consumenten en reducenten",
            "planten, dieren en stenen",
            "jagers, prooien en vluchters",
            "autotrofen, parasieten en gastheren",
        ],
        antwoord=0,
        uitleg="Producenten maken organische stof, consumenten eten die, reducenten breken alles weer af. Zo loopt de materie rond.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de organismen die dood organisch materiaal afbreken?",
        antwoord=["reducenten", "reducent", "de reducenten"],
        uitleg="Bacteriën, schimmels en bodemdieren zijn de reducenten. Zij maken de mineralen vrij die planten opnieuw opnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voedselketen?",
        opties=[
            "een rij organismen waarin elk het volgende tot voedsel dient",
            "alle organismen die in één gebied leven",
            "de rij van alle stoffen in een plant",
            "de weg van een stof door één organisme",
        ],
        antwoord=0,
        uitleg="Een voedselketen begint bij een producent en gaat met pijlen naar wie wie eet. De pijl wijst in de richting waarin de energie gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="In een voedselketen wijst de pijl van het gegeten organisme naar wie het eet.",
        antwoord=True,
        uitleg="De pijl volgt de stroom van stof en energie. Gras, pijl, koe, pijl, mens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft een voedselweb de werkelijkheid beter weer dan een voedselketen?",
        opties=[
            "de meeste dieren eten meer dan één soort",
            "een voedselweb heeft geen producenten nodig",
            "een voedselweb laat de reducenten weg",
            "een voedselweb geldt enkel in het water",
        ],
        antwoord=0,
        uitleg="Een keten is één draad uit het web. Omdat soorten meerdere verbindingen hebben, is een web een eerlijker beeld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de plaats van een organisme in een voedselketen, zoals producent of eerste consument?",
        antwoord=["trofisch niveau", "voedselniveau", "trofische niveau"],
        uitleg="Elk niveau staat één stap verder van de zon. Hoe hoger het niveau, hoe minder energie er nog over is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een energiepiramide naar boven toe smaller?",
        opties=[
            "bij elke stap gaat het meeste verloren als warmte",
            "er zijn naar boven toe minder soorten in de wereld",
            "de dieren bovenaan zijn groter en nemen minder plaats in",
            "de energie wordt bij elke stap in materie omgezet",
        ],
        antwoord=0,
        uitleg="Een koe gebruikt het grootste deel van haar gras zelf en geeft warmte af. Van elke stap blijft maar ongeveer een tiende over voor het volgende niveau.",
    ),
    dict(
        type="waarofniet",
        vraag="Ongeveer een tiende van de energie van een niveau komt in het volgende niveau terecht.",
        antwoord=True,
        uitleg="De rest wordt verbruikt of verdwijnt als warmte. Daarom zijn er maar vier of vijf niveaus mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn er in een ecosysteem zelden meer dan vier of vijf trofische niveaus?",
        opties=[
            "na elke stap blijft er te weinig energie over",
            "er zijn niet genoeg soorten om meer niveaus te vullen",
            "de reducenten eten alle energie van bovenaf op",
            "roofdieren willen niet op elkaar jagen",
        ],
        antwoord=0,
        uitleg="Wie op een roofdier zou jagen, vindt daar bijna geen energie meer. Daarom loopt een keten na vier of vijf stappen dood.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de materiestroom en de energiestroom in een ecosysteem?",
        opties=[
            "materie gaat rond in kringlopen, energie stroomt er maar één keer door",
            "energie gaat rond in kringlopen, materie stroomt er maar één keer door",
            "beide gaan in kringlopen rond",
            "beide stromen maar één keer door het ecosysteem",
        ],
        antwoord=0,
        uitleg="Koolstof en stikstof worden eindeloos hergebruikt. De zonne-energie verlaat het ecosysteem uiteindelijk als warmte en komt niet terug.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ecosysteem heeft geen energie van buiten nodig, want ook de energie gaat er in een kringloop rond.",
        antwoord=False,
        uitleg="Enkel de materie gaat rond. De energie loopt één kant uit en gaat als warmte verloren, dus is er voortdurend zonlicht nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organismen zijn producenten? Kruis alles aan wat juist is.",
        opties=[
            "gras in een weide",
            "algen in een vijver",
            "een eik in een bos",
            "een schimmel op een dode stam",
        ],
        antwoord=[0, 1, 2],
        uitleg="Producenten maken zelf organische stof met licht. Een schimmel kan dat niet en leeft van dood materiaal, dus is hij een reducent.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een consument die zich met plantaardig materiaal voedt?",
        antwoord=["herbivoor", "een herbivoor", "plantenteter"],
        uitleg="Een herbivoor staat op het eerste consumentenniveau. Een carnivoor eet dieren en een omnivoor eet van beide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een bepaald stuk land meer mensen voeden met graan dan met vlees?",
        opties=[
            "van graan naar vlees gaat veel energie verloren",
            "graan bevat per kilogram meer energie dan vlees",
            "vee heeft geen water nodig en graan wel",
            "graan groeit op elke bodem en gras niet",
        ],
        antwoord=0,
        uitleg="Eet je het graan zelf, dan sla je een trofisch niveau over. Ga je langs het vee, dan blijft er maar een tiende van de energie over.",
    ),
    dict(
        type="waarofniet",
        vraag="Sommige giftige stoffen hopen zich op naar de top van een voedselketen toe.",
        antwoord=True,
        uitleg="Een stof die het lichaam niet afbreekt, blijft bij elke stap achter in het vet. Daarom zit er het meest van in de roofdieren bovenaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is biomassa?",
        opties=[
            "de totale massa levend materiaal in een gebied of op een niveau",
            "de hoeveelheid energie die de zon per dag levert",
            "de massa van de bodem in een gebied",
            "het aantal soorten dat in een gebied voorkomt",
        ],
        antwoord=0,
        uitleg="Met biomassa vergelijkt men niveaus en gebieden. Meestal neemt ze naar de top van de piramide toe sterk af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol spelen de reducenten in de stromen van een ecosysteem? Kruis alles aan wat juist is.",
        opties=[
            "ze breken dood organisch materiaal af",
            "ze maken mineralen vrij voor de producenten",
            "ze maken de materiekringloop rond",
            "ze brengen nieuwe energie het ecosysteem in",
        ],
        antwoord=[0, 1, 2],
        uitleg="Reducenten sluiten de kringloop van de materie. Nieuwe energie komt enkel van de zon, via de producenten.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder reducenten zou een ecosysteem blijven werken zolang de zon schijnt.",
        antwoord=False,
        uitleg="De mineralen zouden in dood materiaal opgesloten blijven en de producenten kregen niets meer. Dan stopt alles, hoeveel licht er ook valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een vijver verdwijnen alle waterplanten door vervuiling. Welk gevolg verwacht je?",
        opties=[
            "de producenten vallen weg, en de consumenten erbij",
            "de consumenten gaan zelf fotosynthese doen",
            "de reducenten nemen de rol van producent over",
            "er verandert niets zolang de zon blijft schijnen",
        ],
        antwoord=0,
        uitleg="De producenten zijn de ingang van alle energie. Vallen ze weg, dan stort het hele web dat erop rust in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een landbouwer vergelijkt twee percelen: één met alleen maïs, één met een mengsel van gewassen. Wat verwacht je over het bodemleven?",
        opties=[
            "het mengsel geeft meer verschillende plantenresten, dus een rijker bodemleven",
            "het bodemleven is in beide percelen precies gelijk",
            "alleen maïs geeft het rijkste bodemleven",
            "bodemleven hangt enkel van de temperatuur af",
        ],
        antwoord=0,
        uitleg="Verschillende plantenresten voeden verschillende reducenten. Eén gewas voedt telkens dezelfde kleine groep.",
    ),
]
