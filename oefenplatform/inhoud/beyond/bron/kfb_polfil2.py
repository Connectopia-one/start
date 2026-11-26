# -*- coding: utf-8 -*-
"""Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid.

Thema filosofie dat enkel in kunstbeschouwing en filosofie (fiche 3DDO)
staat:

    rechtvaardigheid bij Aristoteles, in algemene en in specifieke zin
    de sociale contracttheorie bij Hobbes, Locke en Rousseau
    rechtvaardigheid bij John Rawls: grondbeginselen en social justice
    gelijkheid volgens liberalisme en communitarisme: individuele en
    culturele politieke gelijkheid
    politieke vrijheid: John Stuart Mill (liberty principle), Isaiah Berlin
    (positieve en negatieve vrijheid, betekenis en gevolgen), Hannah Arendt
    de kritiek van Joan Tronto op het organiseren van zorg in de maatschappij
    (uit het deel zorgethiek, dat filosofie en recht niet heeft)

Deel 1: rechtvaardigheid en gelijkheid. Deel 2: politieke vrijheid en de
kritiek van Tronto.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Aristoteles met rechtvaardigheid in algemene zin?",
        opties=[
            "de wetten volgen en zo bijdragen aan het goede leven van allen",
            "iedereen precies hetzelfde bedrag geven, wat hij ook doet of laat",
            "altijd het eigen voordeel zoeken, zolang niemand het merkt",
            "de sterkste in de stad laten beslissen wat eerlijk is en wat niet",
        ],
        antwoord=0,
        uitleg="In algemene zin is rechtvaardigheid de volledige deugd tegenover anderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is verdelende rechtvaardigheid bij Aristoteles?",
        opties=[
            "goederen en eer verdelen naar verdienste, in verhouding",
            "iedereen exact hetzelfde geven, los van wat hij deed",
            "een schade herstellen, ongeacht wie de dader is",
            "de macht verdelen over drie gescheiden machten",
        ],
        antwoord=0,
        uitleg="Wie meer bijdraagt, krijgt meer. Gelijken worden gelijk, ongelijken ongelijk behandeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is herstellende of corrigerende rechtvaardigheid bij Aristoteles?",
        opties=[
            "een onrecht of schade rechtzetten, los van wie de partijen zijn",
            "eer en goederen verdelen naar de verdienste van elke burger",
            "de wetten van de stad zo goed mogelijk volgen",
            "de rijksten meer belasting laten betalen",
        ],
        antwoord=0,
        uitleg="Wie schade aanricht, moet die herstellen. Het maakt niet uit of de dader rijk of arm is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van de sociale contracttheorie?",
        opties=[
            "de staat ontstaat uit een afspraak om de natuurtoestand te verlaten",
            "de staat is door God gegeven aan één koninklijke familie",
            "de staat is er altijd geweest en heeft geen begin of oorsprong",
            "de staat ontstaat uit een oorlog die de sterkste groep altijd wint",
        ],
        antwoord=0,
        uitleg="Hobbes, Locke en Rousseau denken elk op hun manier na over dat contract.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke koppeling van denker en sociaal contract klopt?",
        opties=[
            "Hobbes: veiligheid; Locke: natuurrechten beschermen; Rousseau: de algemene wil",
            "Hobbes: de algemene wil; Locke: veiligheid; Rousseau: natuurrechten beschermen",
            "Hobbes: natuurrechten beschermen; Locke: de algemene wil; Rousseau: veiligheid",
            "Hobbes: de algemene wil; Locke: natuurrechten beschermen; Rousseau: veiligheid",
        ],
        antwoord=0,
        uitleg="Hobbes zoekt vrede, Locke bescherming van leven, vrijheid en eigendom, Rousseau een volk dat zichzelf bestuurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de sluier van onwetendheid bij John Rawls?",
        opties=[
            "je kiest de regels zonder je eigen plaats te kennen",
            "je kiest de regels pas als je weet hoe rijk je bent",
            "een doek die rechters dragen om de beklaagde niet te zien",
            "het verbod om over politiek te praten in de klas of op het werk",
        ],
        antwoord=0,
        uitleg="Wie niet weet of hij rijk of arm, gezond of ziek zal zijn, kiest eerlijke regels voor iedereen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grondbeginselen van rechtvaardigheid formuleert Rawls?",
        opties=[
            "iedereen heeft gelijke basisvrijheden",
            "ongelijkheid mag enkel als ze ook de minst bevoordeelden helpt",
            "wie het hardst werkt, krijgt altijd alles",
            "de gemeenschap beslist wie vrijheid krijgt",
        ],
        antwoord=[0, 1],
        uitleg="Het eerste is het vrijheidsbeginsel, het tweede het verschilbeginsel, samen met eerlijke gelijke kansen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met social justice bij Rawls?",
        opties=[
            "de instellingen verdelen rechten, kansen en middelen eerlijk",
            "elke burger moet zelf zijn eigen rechtbank oprichten in zijn buurt",
            "het geld van de staat gaat enkel naar wie het meeste werkt",
            "rechtvaardigheid hangt enkel af van wat één persoon goed vindt",
        ],
        antwoord=0,
        uitleg="Het gaat om de basisstructuur van de samenleving: belastingen, onderwijs, gezondheidszorg, ...",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is individuele politieke gelijkheid, zoals het liberalisme ze ziet?",
        opties=[
            "elke burger heeft dezelfde rechten, welke afkomst ook",
            "elke cultuur krijgt eigen rechten en eigen regels",
            "elke burger krijgt precies evenveel geld van de staat",
            "elke burger moet dezelfde godsdienst volgen als de meerderheid",
        ],
        antwoord=0,
        uitleg="Eén persoon, één stem: de staat kijkt naar het individu, niet naar de groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is culturele politieke gelijkheid, zoals het communitarisme ze ziet?",
        opties=[
            "ook culturele groepen verdienen erkenning en bescherming",
            "alle culturen moeten opgaan in één en dezelfde cultuur",
            "enkel de cultuur van de meerderheid telt in de politiek",
            "cultuur speelt geen enkele rol in de politiek of de wetten",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld onderwijs in de eigen taal of erkenning van een minderheid. Charles Taylor schreef over de politiek van erkenning.",
    ),
    dict(
        type="invultekst",
        vraag="Het gedachte-experiment van Rawls, waarbij je je eigen plaats in de samenleving niet kent, heet de sluier van ...",
        antwoord=["onwetendheid"],
        uitleg="Zo kies je regels die eerlijk zijn voor wie er het slechtst aan toe is.",
    ),
    dict(
        type="invultekst",
        vraag="Het beginsel van Rawls dat ongelijkheid enkel toelaat als ze de minst bevoordeelden helpt, heet het ...",
        antwoord=["verschilbeginsel", "differentiebeginsel"],
        uitleg="Ongelijkheid is dus niet altijd onrechtvaardig, maar moet iedereen ten goede komen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij verdelende rechtvaardigheid krijgt volgens Aristoteles iedereen exact hetzelfde.",
        antwoord=False,
        uitleg="Aristoteles verdeelt naar verdienste, in verhouding. Gelijk is niet hetzelfde als identiek.",
    ),
    dict(
        type="waarofniet",
        vraag="Hobbes, Locke en Rousseau verklaren alle drie het ontstaan van de staat met een sociaal contract.",
        antwoord=True,
        uitleg="Ze verschillen wel in hoe ze de natuurtoestand en het contract zien.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Rawls is elke ongelijkheid in een samenleving onrechtvaardig.",
        antwoord=False,
        uitleg="Ongelijkheid mag, als ze ook de minst bevoordeelden helpt en er eerlijke kansen zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Communitaristen vinden dat het behoren tot een cultuur belangrijk is voor wie je bent.",
        antwoord=True,
        uitleg="Daarom pleiten ze ook voor erkenning van culturele groepen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school geeft een leerling met dyslexie extra tijd bij examens. Welk idee van rechtvaardigheid past hier het best?",
        opties=[
            "gelijke kansen, zoals bij Rawls",
            "herstel van een schade, zoals bij een rechtbank",
            "iedereen precies hetzelfde behandelen",
            "de sterkste krijgt het meeste",
        ],
        antwoord=0,
        uitleg="Gelijk behandelen is hier niet eerlijk. Wat extra steun maakt de kansen gelijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand breekt de fiets van een klasgenoot en moet een nieuwe betalen. Welke vorm van rechtvaardigheid bij Aristoteles zie je?",
        opties=[
            "herstellende rechtvaardigheid",
            "verdelende rechtvaardigheid",
            "rechtvaardigheid in algemene zin",
            "culturele politieke gelijkheid",
        ],
        antwoord=0,
        uitleg="De schade wordt hersteld. De vraag wie verdienstelijker is, speelt hier geen rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een minderheid vraagt les in haar eigen taal op school. Hoe reageren liberalisme en communitarisme wellicht?",
        opties=[
            "liberalisme: gelijke rechten per individu; communitarisme: erkenning van de groep",
            "het liberalisme wil enkel groepsrechten, het communitarisme enkel individuele rechten",
            "allebei vinden ze taal onbelangrijk voor de politiek en het onderwijs",
            "allebei willen ze dat de school de vraag gewoon negeert",
        ],
        antwoord=0,
        uitleg="Individuele gelijkheid tegenover culturele gelijkheid: daar verschillen beide stromingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kiezen mensen achter de sluier van onwetendheid volgens Rawls voor goede zorg voor de zwaksten?",
        opties=[
            "ze weten niet of ze zelf tot de zwaksten zullen behoren",
            "ze zijn allemaal van nature heel vrijgevig en goed",
            "ze worden daartoe verplicht door een sterke vorst",
            "ze krijgen er achteraf een beloning voor van de staat",
        ],
        antwoord=0,
        uitleg="Uit voorzichtigheid kies je regels die ook goed zijn als je het slechtst terechtkomt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt het liberty principle of schadebeginsel van John Stuart Mill?",
        opties=[
            "de staat mag je vrijheid enkel beperken om schade aan anderen te voorkomen",
            "de staat mag je vrijheid beperken als hij vindt dat het beter is voor jezelf",
            "de staat moet je elke vrijheid ontnemen om de orde te bewaren",
            "de staat mag enkel de vrijheid van de rijksten beperken",
        ],
        antwoord=0,
        uitleg="Over wat enkel jezelf aangaat, beslis je zelf. Mill schreef On Liberty in 1859.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is negatieve vrijheid bij Isaiah Berlin?",
        opties=[
            "vrij zijn van inmenging: niemand houdt je tegen",
            "vrij zijn om je eigen leven te sturen en jezelf te verwezenlijken",
            "vrij zijn om anderen te verbieden wat ze willen",
            "vrij zijn van alle regels, wetten en plichten",
        ],
        antwoord=0,
        uitleg="Negatief betekent hier: de afwezigheid van dwang van buitenaf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is positieve vrijheid bij Isaiah Berlin?",
        opties=[
            "vrij zijn tot iets: je eigen leven zelf sturen",
            "vrij zijn van inmenging, zonder dat iemand je tegenhoudt",
            "vrij zijn om altijd vrolijk en positief te blijven",
            "vrij zijn om het eigendom van anderen af te nemen",
        ],
        antwoord=0,
        uitleg="Positieve vrijheid vraagt soms dat je middelen of kansen krijgt, zoals onderwijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevaar ziet Berlin bij een te sterke nadruk op positieve vrijheid?",
        opties=[
            "een staat kan mensen dwingen in naam van hun 'ware' vrijheid",
            "mensen krijgen dan te weinig onderwijs en kansen",
            "de staat verdwijnt dan helemaal en er komen geen wetten meer",
            "niemand mag nog stemmen of zich verkiesbaar stellen",
        ],
        antwoord=0,
        uitleg="Wie zegt beter te weten wat je echt wilt, kan zo dwang goedpraten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg kan een te sterke nadruk op enkel negatieve vrijheid hebben?",
        opties=[
            "wie geen middelen heeft, is vrij op papier maar kan er weinig mee",
            "de staat gaat zich met elk detail van je leven bemoeien",
            "niemand mag nog een eigen mening hebben of uiten",
            "iedereen krijgt precies dezelfde opleiding en hetzelfde werk",
        ],
        antwoord=0,
        uitleg="Niemand houdt je tegen om te studeren, maar zonder geld of steun lukt het misschien niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet Hannah Arendt politieke vrijheid?",
        opties=[
            "vrijheid toont zich als mensen samen handelen in het publiek",
            "vrijheid betekent dat je je volledig terugtrekt uit de politiek",
            "vrijheid betekent dat een sterke leider voor iedereen beslist",
            "vrijheid bestaat enkel in je eigen gedachten, nooit samen met anderen",
        ],
        antwoord=0,
        uitleg="Voor Arendt is vrijheid iets wat je samen doet: handelen, debatteren, iets nieuws beginnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken passen bij Mill?",
        opties=[
            "over wat enkel jezelf aangaat, ben je soeverein",
            "vrije meningsuiting helpt om de waarheid te vinden",
            "de staat moet bepalen welke mening juist is",
            "vrijheid is gevaarlijk en moet zo veel mogelijk beperkt worden",
        ],
        antwoord=[0, 1],
        uitleg="Mill verdedigt de vrijheid van denken en spreken: ook een foute mening kan helpen de waarheid scherper te zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kritiek geeft Joan Tronto op hoe zorg in de maatschappij georganiseerd is?",
        opties=[
            "zorgwerk wordt ondergewaardeerd en valt vooral op vrouwen en lager betaalden",
            "er wordt veel te veel geld en aandacht aan zorg gegeven in de samenleving",
            "zorg moet in de toekomst enkel nog door robots en computers gebeuren",
            "zorg is een privézaak van gezinnen die de politiek niet aangaat",
        ],
        antwoord=0,
        uitleg="Tronto vindt dat zorg een publieke, politieke zaak is en eerlijk verdeeld moet worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Tronto met bevoorrechte onverantwoordelijkheid?",
        opties=[
            "wie macht of geld heeft, schuift zorgtaken door naar anderen",
            "wie arm is, hoeft nooit voor iemand anders te zorgen, ook niet in het gezin",
            "zorgverleners mogen altijd zelf kiezen voor wie ze zorgen en voor wie niet",
            "kinderen hoeven nooit verantwoordelijkheid te nemen voor anderen",
        ],
        antwoord=0,
        uitleg="De bevoorrechten profiteren van zorg zonder er zelf verantwoordelijkheid voor te dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad verbiedt roken in openbare gebouwen, maar niet thuis. Hoe zou Mill dit verdedigen?",
        opties=[
            "in een openbaar gebouw schaadt rook anderen, thuis vooral jezelf",
            "de staat moet mensen altijd beschermen tegen hun eigen slechte keuzes",
            "roken is verboden omdat de meerderheid het niet mooi vindt",
            "de vrijheid van rokers telt volgens Mill helemaal niet mee",
        ],
        antwoord=0,
        uitleg="Het schadebeginsel trekt de grens bij schade aan anderen.",
    ),
    dict(
        type="invultekst",
        vraag="Het beginsel van Mill dat vrijheid enkel beperkt mag worden om schade aan anderen te voorkomen, heet het ...",
        antwoord=["schadebeginsel", "liberty principle", "harm principle"],
        uitleg="In het Engels ook harm principle genoemd.",
    ),
    dict(
        type="invultekst",
        vraag="Vrijheid als afwezigheid van inmenging noemt Isaiah Berlin ... vrijheid.",
        antwoord=["negatieve"],
        uitleg="Positieve vrijheid is vrijheid tot zelfbestuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Mill mag de staat je verbieden iets te doen wat enkel jezelf kan schaden.",
        antwoord=False,
        uitleg="Over wat enkel jezelf aangaat, beslis je volgens Mill zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Berlin waarschuwt dat positieve vrijheid kan misbruikt worden om dwang goed te praten.",
        antwoord=True,
        uitleg="Een regime kan zeggen dat het mensen dwingt tot hun 'echte' vrijheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Hannah Arendt is vrijheid vooral iets wat je alleen ervaart, los van anderen.",
        antwoord=False,
        uitleg="Arendt ziet vrijheid net als samen handelen in de publieke ruimte.",
    ),
    dict(
        type="waarofniet",
        vraag="Tronto vindt dat zorg een politieke zaak is en niet enkel een privézaak van gezinnen.",
        antwoord=True,
        uitleg="Wie zorgt en wie zorg krijgt, hangt samen met macht en verdeling in de samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land geeft gratis onderwijs, zodat iedereen kan studeren. Welke vorm van vrijheid wordt hier vooral versterkt?",
        opties=[
            "positieve vrijheid",
            "negatieve vrijheid",
            "het schadebeginsel",
            "bevoorrechte onverantwoordelijkheid",
        ],
        antwoord=0,
        uitleg="Je krijgt middelen om je eigen leven te sturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een regering schaft een verbod op betogen af. Welke vorm van vrijheid wordt hier vooral versterkt?",
        opties=[
            "negatieve vrijheid",
            "positieve vrijheid",
            "verdelende rechtvaardigheid",
            "herstellende rechtvaardigheid",
        ],
        antwoord=0,
        uitleg="Er valt een belemmering weg: niemand houdt je nog tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Burgers richten samen een buurtcomité op en overleggen met de stad over een nieuw plein. Bij welke denker over vrijheid past dit het best?",
        opties=["Hannah Arendt", "Thomas Hobbes", "Carl Schmitt", "David Hume"],
        antwoord=0,
        uitleg="Samen spreken en handelen in de publieke ruimte is vrijheid volgens Arendt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rijke familie huurt een zorgkracht in, betaalt slecht en denkt zelf nooit na over wie voor de ouders zorgt. Welk begrip van Tronto zie je hier?",
        opties=[
            "bevoorrechte onverantwoordelijkheid",
            "positieve vrijheid van de familie",
            "de sluier van onwetendheid van de ouders",
            "het verschilbeginsel van Rawls",
        ],
        antwoord=0,
        uitleg="Wie geld heeft, kan zorg uitbesteden en de verantwoordelijkheid ontlopen.",
    ),
]
