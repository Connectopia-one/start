# -*- coding: utf-8 -*-
"""Atoombinding en lewisstructuren — 🌍 Beyond, chemie.

Deel 1 gaat over de binding zelf vanuit het orbitaalmodel: de sigma-binding met
haar coaxiale overlapping en radiale symmetrie, de pi-binding met haar
overlapping zijdelings, en wat dat betekent voor draaibaarheid, bindingslengte,
bindingssterkte en reactiviteit. Deel 2 gaat over de lewisstructuur: bindende en
vrije elektronenparen, de enkelvoudige, dubbele en drievoudige binding, de
formele lading, en het verschil tussen een normale atoombinding, een
donor-acceptorbinding, een ionbinding en een metaalbinding.

Een lewisstructuur tekenen kan in een vraag op het scherm niet. De vragen laten
dus tellen: hoeveel bindende paren, hoeveel vrije paren, hoeveel sigma- en
pi-bindingen, en welke formele lading daaruit volgt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat een sigma-binding volgens het orbitaalmodel?",
        opties=[
            "twee orbitalen overlappen recht tegenover elkaar, langs de bindingsas",
            "twee orbitalen overlappen zijdelings, boven en onder de bindingsas",
            "twee orbitalen wisselen hun elektronen volledig van atoom naar atoom",
            "twee orbitalen schuiven over elkaar zonder hun elektronen te delen",
        ],
        antwoord=0,
        uitleg="Die overlapping ligt op de lijn tussen de twee kernen. Daarom heet ze "
        "coaxiaal en is ze radiaal symmetrisch rond die as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een molecule vrij draaien rond een enkelvoudige binding?",
        opties=[
            "de sigma-binding blijft bij draaien even goed overlappen",
            "de sigma-binding is sterker dan elke andere soort binding",
            "de sigma-binding heeft geen elektronenpaar nodig om te bestaan",
            "de sigma-binding ligt niet op de lijn tussen de twee kernen",
        ],
        antwoord=0,
        uitleg="De overlapping is radiaal symmetrisch, dus draaien verandert niets. Bij "
        "een pi-binding zou de overlapping juist verdwijnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel pi-bindingen zitten er in een dubbele binding?",
        antwoord=["een", "één", "1"],
        uitleg="Een dubbele binding is één sigma-binding plus één pi-binding. Een "
        "drievoudige binding heeft er twee pi.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel sigma- en pi-bindingen zitten er in etheen, CH₂=CH₂?",
        opties=[
            "vijf sigma en één pi",
            "vier sigma en twee pi",
            "zes sigma en geen pi",
            "drie sigma en drie pi",
        ],
        antwoord=0,
        uitleg="Vier keer C-H en één keer C-C geeft vijf sigma-bindingen; de tweede helft "
        "van de dubbele binding is de pi.",
    ),
    dict(
        type="waarofniet",
        vraag="Een pi-binding is zwakker dan een sigma-binding tussen dezelfde atomen.",
        antwoord=True,
        uitleg="De overlapping zijdelings is kleiner dan die langs de as. Daarom breekt "
        "bij een reactie meestal eerst de pi-binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de bindingslengte van een koolstof-koolstofbinding als er een pi-binding bij komt?",
        opties=[
            "ze wordt korter, want de atomen worden dichter naar elkaar getrokken",
            "ze wordt langer, want er moet plaats zijn voor meer elektronen",
            "ze blijft gelijk, want de sigma-binding bepaalt alleen de lengte",
            "ze wordt eerst langer en daarna korter, afhankelijk van de stof",
        ],
        antwoord=0,
        uitleg="Een C-C is ongeveer 154 pm, een C=C 134 pm en een C≡C 120 pm. Meer "
        "bindingen betekent korter en sterker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een alkeen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de dubbele binding is reactiever dan een enkelvoudige",
            "de twee koolstofatomen kunnen niet vrij draaien",
            "de dubbele binding is langer dan een enkelvoudige",
            "de dubbele binding bestaat uit twee sigma-bindingen",
        ],
        antwoord=[0, 1],
        uitleg="De elektronen van de pi-binding liggen bloot boven en onder het vlak. "
        "Daardoor is ze reactief, en daardoor zit de molecule ook vast in haar vorm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een overlapping die recht op de lijn tussen twee kernen ligt?",
        antwoord=["coaxiaal", "coaxiale", "coaxiale overlapping"],
        uitleg="Co-axiaal betekent langs dezelfde as. Dat is net wat een sigma-binding "
        "haar radiale symmetrie geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel sigma- en pi-bindingen zitten er in ethyn, HC≡CH?",
        opties=[
            "drie sigma en twee pi",
            "twee sigma en drie pi",
            "vier sigma en één pi",
            "vijf sigma en geen pi",
        ],
        antwoord=0,
        uitleg="Twee keer C-H en één keer C-C geeft drie sigma; de drievoudige binding "
        "voegt er twee pi aan toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de drievoudige binding van stikstofgas zo moeilijk te breken?",
        opties=[
            "er moeten één sigma- en twee pi-bindingen samen verbroken worden",
            "er zit een vrij elektronenpaar tussen de twee stikstofatomen",
            "de twee atomen liggen ver van elkaar in de molecule",
            "stikstof heeft een heel hoge elektronegatieve waarde",
        ],
        antwoord=0,
        uitleg="Daarom is stikstofgas zo onreactief, en daarom kost het maken van "
        "kunstmest uit N₂ zoveel energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een drievoudige binding bestaat uit drie sigma-bindingen.",
        antwoord=False,
        uitleg="Ze bestaat uit één sigma en twee pi. Tussen twee atomen kan er maar één "
        "sigma-binding liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent radiale symmetrie bij een sigma-binding?",
        opties=[
            "de binding ziet er van alle kanten rond de as hetzelfde uit",
            "de binding heeft boven en onder de as dezelfde vorm",
            "de binding heeft aan beide kernen evenveel elektronen",
            "de binding heeft dezelfde lengte in elke richting",
        ],
        antwoord=0,
        uitleg="Draai je de ene helft van de molecule rond die as, dan verandert de "
        "overlapping niet. Daarom kan er vrij gedraaid worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke binding ontstaat uit de overlapping van twee p-orbitalen die naast elkaar staan?",
        opties=[
            "een pi-binding",
            "een sigma-binding",
            "een ionbinding",
            "een metaalbinding",
        ],
        antwoord=0,
        uitleg="Die twee p-orbitalen staan parallel en overlappen boven en onder het "
        "vlak van de molecule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen horen bij een pi-binding? Kruis alles aan wat juist is.",
        opties=[
            "ze verhindert het draaien rond de binding",
            "ze is reactiever dan een sigma-binding",
            "ze ligt recht op de as tussen de kernen",
            "ze is sterker dan een sigma-binding",
        ],
        antwoord=[0, 1],
        uitleg="De pi-binding ligt juist niet op de as, maar erboven en eronder. Dat "
        "maakt haar zwakker en reactiever.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel sigma-bindingen liggen er tussen twee atomen die dubbel gebonden zijn?",
        antwoord=["een", "één", "1"],
        uitleg="Altijd precies één. De tweede en eventueel de derde binding zijn "
        "pi-bindingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel sigma-bindingen zitten er in methaan, CH₄?",
        opties=[
            "vier",
            "twee",
            "vijf",
            "acht",
        ],
        antwoord=0,
        uitleg="Vier keer C-H, elk met een coaxiale overlapping. Pi-bindingen zijn er "
        "niet, want methaan is verzadigd.",
    ),
    dict(
        type="waarofniet",
        vraag="In een benzeenring liggen de pi-elektronen over de hele ring verspreid.",
        antwoord=True,
        uitleg="Die zes p-orbitalen overlappen rondom. Daardoor is benzeen stabieler dan "
        "je op basis van drie losse dubbele bindingen zou verwachten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een alkeen reactiever dan een alkaan?",
        opties=[
            "de elektronen van de pi-binding liggen open voor een aanval",
            "de sigma-bindingen van een alkeen zijn veel langer dan gewoonlijk",
            "een alkeen heeft meer waterstofatomen per koolstofatoom",
            "een alkeen heeft een hoger kookpunt dan het overeenkomstige alkaan",
        ],
        antwoord=0,
        uitleg="Daarom gaan alkenen additiereacties aan, waarbij de pi-binding opengaat "
        "en er twee nieuwe sigma-bindingen ontstaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Tussen twee atomen kunnen meerdere sigma-bindingen naast elkaar liggen.",
        antwoord=False,
        uitleg="De coaxiale plaats is maar één keer vrij. Alles wat erbij komt, moet "
        "zijdelings overlappen en is dus een pi-binding.",
    ),
    dict(
        type="invultekst",
        vraag="Welke binding breekt bij een additiereactie aan een alkeen open?",
        antwoord=["de pi-binding", "pi-binding", "pi"],
        uitleg="De sigma-binding tussen de twee koolstofatomen blijft bestaan. Daardoor "
        "valt de molecule niet uiteen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt een streepje tussen twee atomen in een lewisstructuur voor?",
        opties=[
            "een bindend elektronenpaar",
            "een vrij elektronenpaar",
            "een enkel elektron zonder partner",
            "de lading van het hele deeltje",
        ],
        antwoord=0,
        uitleg="Twee elektronen die samen de binding vormen. Een vrij paar tekent men als "
        "twee puntjes naast het atoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel vrije elektronenparen heeft het zuurstofatoom in een watermolecule?",
        opties=[
            "twee",
            "een",
            "drie",
            "vier",
        ],
        antwoord=0,
        uitleg="Zuurstof heeft zes valentie-elektronen: vier zitten in twee vrije paren, "
        "twee in de bindingen met waterstof.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel vrije elektronenparen heeft het stikstofatoom in ammoniak?",
        antwoord=["een", "één", "1"],
        uitleg="Stikstof heeft vijf valentie-elektronen: drie gaan in bindingen met "
        "waterstof, twee blijven over als vrij paar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een donor-acceptorbinding?",
        opties=[
            "één atoom levert het hele elektronenpaar van de binding",
            "elk atoom levert één elektron voor het bindende paar",
            "een atoom staat een elektron volledig af aan het andere",
            "de elektronen bewegen vrij tussen alle atomen van het rooster",
        ],
        antwoord=0,
        uitleg="Het stikstofatoom van ammoniak geeft zijn vrij paar aan een H⁺. Zo "
        "ontstaat het ammoniumion NH₄⁺.",
    ),
    dict(
        type="waarofniet",
        vraag="In het hydroxoniumion H₃O⁺ zit een donor-acceptorbinding.",
        antwoord=True,
        uitleg="Het zuurstofatoom van water geeft een vrij elektronenpaar aan een H⁺. "
        "Daarna zijn de drie bindingen niet meer van elkaar te onderscheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de formele lading van een atoom in een lewisstructuur?",
        opties=[
            "de valentie-elektronen min de vrije elektronen min het aantal bindingen",
            "de valentie-elektronen min het aantal bindingen maal twee erbij",
            "het aantal protonen min het totale aantal elektronen in de molecule",
            "het aantal bindende paren min het aantal vrije paren van het atoom",
        ],
        antwoord=0,
        uitleg="Voor het stikstofatoom in NH₄⁺: 5 − 0 − 4 geeft +1. Dat verklaart de "
        "lading van het hele ion.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ionbinding zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er worden elektronen volledig overgedragen",
            "de deeltjes trekken elkaar aan door hun lading",
            "de elektronen worden gelijk gedeeld tussen de atomen",
            "de binding komt alleen voor tussen twee niet-metalen",
        ],
        antwoord=[0, 1],
        uitleg="Natrium geeft zijn elektron aan chloor. De coulombkracht tussen Na⁺ en "
        "Cl⁻ houdt het rooster daarna samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de binding tussen positieve metaalionen en vrij bewegende elektronen?",
        antwoord=["metaalbinding", "de metaalbinding", "metaalbindingen"],
        uitleg="Die vrije elektronen verklaren waarom een metaal stroom geleidt en "
        "waarom je het kunt pletten zonder dat het breekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bindende elektronenparen heeft het koolstofatoom in koolstofdioxide?",
        opties=[
            "vier, verdeeld over twee dubbele bindingen",
            "twee, verdeeld over twee enkelvoudige bindingen",
            "drie, verdeeld over een dubbele en een enkele",
            "zes, verdeeld over twee drievoudige bindingen",
        ],
        antwoord=0,
        uitleg="O=C=O: elke dubbele binding is twee paren. Zo komt koolstof aan zijn "
        "octet van acht elektronen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de octetregel over een lewisstructuur?",
        opties=[
            "elk atoom streeft naar acht elektronen in zijn buitenste niveau",
            "elk atoom streeft naar acht bindingen met andere atomen",
            "elk atoom heeft acht vrije elektronenparen nodig om stabiel te zijn",
            "elk atoom deelt acht elektronen met elk van zijn buuratomen",
        ],
        antwoord=0,
        uitleg="Bindende en vrije paren tellen allebei mee. Waterstof is de uitzondering: "
        "die is al tevreden met twee.",
    ),
    dict(
        type="waarofniet",
        vraag="In een lewisstructuur tellen de vrije elektronenparen niet mee voor het octet.",
        antwoord=False,
        uitleg="Ze tellen wel mee. Bij water heeft zuurstof twee bindende en twee vrije "
        "paren, en dat zijn samen acht elektronen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bindingen heeft een koolstofatoom in een neutrale organische molecule altijd?",
        opties=[
            "vier",
            "twee",
            "drie",
            "zes",
        ],
        antwoord=0,
        uitleg="Koolstof heeft vier valentie-elektronen en heeft er vier nodig voor zijn "
        "octet. Vandaar vier bindingen, enkelvoudig of niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het ammoniumion NH₄⁺ zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het heeft vier bindende elektronenparen",
            "het stikstofatoom heeft formele lading +1",
            "het heeft nog één vrij elektronenpaar over",
            "het stikstofatoom heeft formele lading −1",
        ],
        antwoord=[0, 1],
        uitleg="Het vrije paar van de stikstof is in de vierde binding gaan zitten. "
        "Daardoor blijft er geen vrij paar meer over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel elektronen zitten er in één elektronenpaar?",
        antwoord=["twee", "2"],
        uitleg="Een paar is altijd twee elektronen, of het nu bindend of vrij is. Daarom "
        "tekent men het als een streepje of twee puntjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een polyatomisch ion heeft een lading van 2−. Wat betekent dat voor de lewisstructuur?",
        opties=[
            "er zitten twee elektronen meer in dan de neutrale atomen samen hebben",
            "er zitten twee protonen minder in dan de neutrale atomen samen hebben",
            "er zitten twee bindende elektronenparen minder in de structuur",
            "er zitten twee vrije elektronenparen meer bij elk zuurstofatoom",
        ],
        antwoord=0,
        uitleg="Bij het sulfaation SO₄²⁻ reken je dus twee extra elektronen mee bij het "
        "verdelen over de bindingen en de vrije paren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt een metaal elektrische stroom?",
        opties=[
            "de valentie-elektronen bewegen vrij door het hele rooster",
            "de metaalionen zelf verplaatsen zich door het rooster",
            "de atomen geven hun elektronen aan elkaar door in een rij",
            "de bindingen tussen de atomen zijn polair en geleidend",
        ],
        antwoord=0,
        uitleg="Die elektronenzee is wat een metaalbinding anders maakt dan een "
        "atoombinding of een ionbinding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel vrije elektronenparen heeft elk chlooratoom in Cl₂?",
        opties=[
            "drie",
            "een",
            "twee",
            "vier",
        ],
        antwoord=0,
        uitleg="Chloor heeft zeven valentie-elektronen: één gaat in de binding, de zes "
        "andere vormen drie vrije paren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een normale atoombinding ontstaat doordat elk atoom één elektron voor het bindende paar levert.",
        antwoord=True,
        uitleg="Bij een donor-acceptorbinding komt het hele paar van één atoom. Het "
        "resultaat ziet er daarna hetzelfde uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De formele lading van een atoom is hetzelfde als zijn oxidatiegetal.",
        antwoord=False,
        uitleg="Bij de formele lading verdeel je de bindende elektronen eerlijk over de "
        "twee atomen; bij het oxidatiegetal geef je ze helemaal aan het meest "
        "elektronegatieve atoom.",
    ),
    dict(
        type="invultekst",
        vraag="Welk atoom is tevreden met twee elektronen in plaats van acht?",
        antwoord=["waterstof", "H", "het waterstofatoom"],
        uitleg="Waterstof heeft maar één hoofdniveau, en dat is vol met twee elektronen. "
        "Dat is de configuratie van helium.",
    ),
]
