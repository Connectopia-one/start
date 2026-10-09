# -*- coding: utf-8 -*-
"""Sociale mobiliteit, meritocratie en het matheüseffect.

Het derde van vijf thema's over sociale wetenschappen. Het vorige thema vroeg
hoe een samenleving in lagen verdeeld is; dit thema vraagt of je van laag kan
veranderen, en voor wie dat moeilijker is.

De lijstjes staan letterlijk in de fiche:

    soorten sociale mobiliteit: horizontale, verticale, intragenerationele en
        intergenerationele mobiliteit
    beïnvloedende factoren: afkomst, beroep, gender, handicap, huwelijk en
        echtscheiding, inkomen, rijkdom of bezit, kennis, leeftijd,
        migratiegeschiedenis
    verder vraagt de fiche: de relatie tussen onderwijs en sociale
        ongelijkheid, argumenten voor en tegen meritocratie, het verband
        tussen een lagere sociale positie en sociale uitsluiting, en het
        matheüseffect

Het matheüseffect is vernoemd naar het evangelie van Matteüs, waar staat dat
wie heeft nog meer zal krijgen. In Vlaanderen is het begrip vooral bekend
geworden door het onderzoek van socioloog Herman Deleeck naar wie de
voordelen van sociaal beleid in de praktijk opraapt.

Deel 1 is het begrip, de vier soorten en de factoren.
Deel 2 zijn onderwijs, meritocratie, uitsluiting en het matheüseffect.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is sociale mobiliteit?",
        opties=[
            "het bewegen van mensen tussen sociale posities",
            "het verhuizen van mensen naar een andere streek",
            "het verdelen van een samenleving in lagen",
            "het stijgen van de lonen in een samenleving",
        ],
        antwoord=0,
        uitleg="Mobiliteit is beweging. Sociale mobiliteit gaat niet over verhuizen maar over van plaats veranderen in de gelaagdheid van een samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier soorten sociale mobiliteit noemt de fiche?",
        opties=[
            "horizontale mobiliteit",
            "verticale mobiliteit",
            "intergenerationele mobiliteit",
            "geografische mobiliteit",
            "culturele mobiliteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier zijn horizontaal, verticaal, intragenerationeel en intergenerationeel. De geografische en de culturele staan niet in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is horizontale mobiliteit?",
        opties=[
            "van positie veranderen zonder te stijgen of te dalen",
            "van positie veranderen en daarbij stijgen",
            "van positie veranderen en daarbij dalen",
            "van streek veranderen binnen een land",
        ],
        antwoord=0,
        uitleg="Een leerkracht die kleuterleidster wordt, verandert van positie maar blijft op dezelfde hoogte. Dat is horizontaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is verticale mobiliteit?",
        opties=[
            "van positie veranderen en daarbij stijgen of dalen",
            "van positie veranderen op dezelfde hoogte",
            "van woonplaats veranderen binnen een stad",
            "van beroep veranderen binnen hetzelfde bedrijf",
        ],
        antwoord=0,
        uitleg="Verticaal gaat omhoog of omlaag in de gelaagdheid. Het kan dus ook een daling zijn, niet alleen een klim.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is intragenerationele mobiliteit?",
        opties=[
            "beweging binnen het leven van één persoon",
            "beweging tussen ouders en kinderen",
            "beweging tussen twee landen",
            "beweging tussen twee beroepsgroepen",
        ],
        antwoord=0,
        uitleg="Intra betekent binnen. Iemand die begint als arbeider en eindigt als ploegbaas, is intragenerationeel gestegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is intergenerationele mobiliteit?",
        opties=[
            "beweging tussen de generatie van de ouders en die van de kinderen",
            "beweging binnen het leven van één persoon",
            "beweging tussen twee streken van een land",
            "beweging tussen twee opleidingen",
        ],
        antwoord=0,
        uitleg="Inter betekent tussen. Een kind van laaggeschoolde ouders dat arts wordt, is intergenerationeel gestegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sofie begint als verpleegkundige en wordt na vijftien jaar hoofdverpleegkundige. Welke soorten mobiliteit zie je?",
        opties=[
            "verticale mobiliteit",
            "intragenerationele mobiliteit",
            "intergenerationele mobiliteit",
            "horizontale mobiliteit",
        ],
        antwoord=[0, 1],
        uitleg="Ze stijgt, dus verticaal, en dat gebeurt in haar eigen leven, dus intragenerationeel. De twee indelingen gaan altijd samen.",
    ),
    dict(
        type="invultekst",
        vraag="Beweging tussen de generatie van de ouders en die van de kinderen heet ...generationele mobiliteit.",
        antwoord=["inter", "intergenerationele"],
        uitleg="Intergenerationele mobiliteit. Binnen één leven heet het intragenerationeel.",
    ),
    dict(
        type="waarofniet",
        vraag="Verticale mobiliteit kan zowel een stijging als een daling zijn.",
        antwoord=True,
        uitleg="Waar. Wie door een ontslag of ziekte lager terechtkomt, is ook verticaal mobiel geweest.",
    ),
    dict(
        type="waarofniet",
        vraag="Horizontale mobiliteit betekent dat iemand naar een andere streek verhuist.",
        antwoord=False,
        uitleg="Niet waar. Dat is geografische mobiliteit, en die staat niet in de fiche. Horizontaal is van positie veranderen op dezelfde hoogte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren noemt de fiche als invloed op de mate van sociale mobiliteit?",
        opties=[
            "de afkomst",
            "de kennis",
            "de migratiegeschiedenis",
            "het temperament",
            "de persoonlijkheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt negen factoren. Temperament en persoonlijkheid horen bij de gedragswetenschappen, niet bij deze lijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat gender in de lijst van factoren die mobiliteit beïnvloeden?",
        opties=[
            "omdat vrouwen en mannen niet dezelfde loopbaankansen hebben",
            "omdat vrouwen en mannen dezelfde loopbaankansen hebben",
            "omdat gender alleen bij een huwelijk meespeelt",
            "omdat gender in het recht een eigen stand vormt",
        ],
        antwoord=0,
        uitleg="Loonverschil, deeltijds werken en de verdeling van zorgtaken zorgen dat mobiliteit niet voor iedereen gelijk loopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat leeftijd in de lijst van factoren?",
        opties=[
            "omdat de kans op een nieuwe stap met de jaren verandert",
            "omdat oudere mensen nooit meer van positie veranderen",
            "omdat leeftijd de status van een beroep vastlegt",
            "omdat leeftijd bepaalt welke opleiding je mag doen",
        ],
        antwoord=0,
        uitleg="Op jonge leeftijd ligt een loopbaan nog open. Na een ontslag op latere leeftijd is herintreden op hetzelfde niveau veel moeilijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jonas erft het bedrijf van zijn ouders en neemt hun positie over. Welke factor uit de lijst speelt hier het sterkst?",
        opties=[
            "de afkomst",
            "de kennis",
            "de leeftijd",
            "de gender",
        ],
        antwoord=0,
        uitleg="Zijn startpositie komt van zijn gezin van herkomst. Dat is de factor afkomst.",
    ),
    dict(
        type="invultekst",
        vraag="Beweging binnen het leven van één persoon heet ...generationele mobiliteit.",
        antwoord=["intra", "intragenerationele"],
        uitleg="Intragenerationele mobiliteit. Tussen de generaties heet het intergenerationeel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een echtscheiding kan volgens de fiche een invloed hebben op de sociale mobiliteit van iemand.",
        antwoord=True,
        uitleg="Waar. De fiche noemt huwelijk en echtscheiding als een van de negen factoren. Een scheiding kan een inkomen halveren.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de fiche beïnvloedt een handicap de sociale mobiliteit niet.",
        antwoord=False,
        uitleg="Niet waar. Handicap staat uitdrukkelijk in de lijst van negen factoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is kennis een factor in de sociale mobiliteit?",
        opties=[
            "omdat een diploma de deur naar posities opent",
            "omdat kennis de status van een beroep vastlegt",
            "omdat kennis bij iedereen evenveel oplevert",
            "omdat kennis enkel bij jonge mensen meespeelt",
        ],
        antwoord=0,
        uitleg="Opleiding is in een klassenmaatschappij de belangrijkste sleutel naar een hogere positie. Daarom gaat het volgende deel over onderwijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker vergelijkt het beroep van kinderen met dat van hun ouders. Welke soort mobiliteit meet hij?",
        opties=[
            "de intergenerationele mobiliteit",
            "de intragenerationele mobiliteit",
            "de horizontale mobiliteit",
            "de geografische mobiliteit",
        ],
        antwoord=0,
        uitleg="Twee generaties naast elkaar zetten is de klassieke manier om intergenerationele mobiliteit te meten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als er in een samenleving weinig sociale mobiliteit is?",
        opties=[
            "de plaats van je ouders voorspelt sterk je eigen plaats",
            "de plaats van je ouders zegt niets over je eigen plaats",
            "er is geen enkele ongelijkheid meer",
            "iedereen verhuist weinig binnen het land",
        ],
        antwoord=0,
        uitleg="Weinig mobiliteit betekent dat de lagen gesloten zijn. Dan telt afkomst zwaarder dan wat iemand zelf doet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met de relatie tussen onderwijs en sociale ongelijkheid?",
        opties=[
            "onderwijs kan ongelijkheid verkleinen en ook doorgeven",
            "onderwijs maakt alle ongelijkheid altijd kleiner",
            "onderwijs maakt alle ongelijkheid altijd groter",
            "onderwijs staat los van ongelijkheid",
        ],
        antwoord=0,
        uitleg="Een diploma is de grootste kans op stijgen, en tegelijk hangt het schoolresultaat sterk samen met de thuissituatie. Beide zijn waar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is meritocratie?",
        opties=[
            "een samenleving waarin verdienste je plaats bepaalt",
            "een samenleving waarin afkomst je plaats bepaalt",
            "een samenleving waarin het lot je plaats bepaalt",
            "een samenleving zonder enig verschil in plaats",
        ],
        antwoord=0,
        uitleg="Meritum betekent verdienste. In een meritocratie komt iemand hoger door talent en inzet, niet door afkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een argument voor meritocratie?",
        opties=[
            "wie zich inzet, krijgt er ook iets voor terug",
            "de afkomst van iemand blijft zwaar doorwegen",
            "iedereen begint op precies dezelfde plaats",
            "talent en inzet zijn volledig aangeboren",
        ],
        antwoord=0,
        uitleg="Dat is het sterkste argument: inzet en talent lonen, en posities gaan naar wie ze kan dragen, los van geboorte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een argument tegen meritocratie?",
        opties=[
            "niet iedereen krijgt dezelfde kans om te verdienen",
            "ze geeft te veel gewicht aan afkomst en erfenis",
            "ze verbiedt mensen om zich in te zetten",
            "ze bestaat in geen enkel land ter wereld",
        ],
        antwoord=0,
        uitleg="Wie thuis geen rustige plek of taalsteun heeft, start achteraan. Wie dan niet slaagt, krijgt in een meritocratie ook nog de schuld.",
    ),
    dict(
        type="invultekst",
        vraag="Een samenleving waarin verdienste in plaats van afkomst je plaats bepaalt, heet een ...",
        antwoord=["meritocratie"],
        uitleg="Een meritocratie, van het Latijnse meritum, verdienste.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche vraagt om argumenten voor én tegen meritocratie te kunnen geven.",
        antwoord=True,
        uitleg="Waar. Ze vraagt argumenten te herkennen, te beoordelen en zelf te geven, voor of tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een volledige meritocratie bestaat er geen ongelijkheid meer.",
        antwoord=False,
        uitleg="Niet waar. De ongelijkheid blijft, alleen de reden verandert: niet je afkomst maar je verdienste zet je hoog of laag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sociale uitsluiting?",
        opties=[
            "niet kunnen meedoen aan wat in een samenleving gewoon is",
            "niet willen meedoen aan wat in een samenleving gewoon is",
            "uit een vereniging gezet worden na een conflict",
            "uit een ander land naar hier gekomen zijn",
        ],
        antwoord=0,
        uitleg="Uitsluiting is meer dan weinig geld hebben: het is buiten het gewone leven vallen, op school, op het werk, in de vrije tijd en in de zorg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen een lagere sociale positie en sociale uitsluiting?",
        opties=[
            "een lagere positie verhoogt de kans om buiten te vallen",
            "een lagere positie sluit iemand altijd volledig uit",
            "een lagere positie heeft met uitsluiting niets te maken",
            "uitsluiting komt enkel bij een hogere positie voor",
        ],
        antwoord=0,
        uitleg="Het is een kans, geen zekerheid. Maar lagere inkomens, slechtere woningen en minder netwerk versterken elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het matheüseffect?",
        opties=[
            "wie al voordeel heeft, haalt het meeste uit een maatregel",
            "wie het minste heeft, haalt het meeste uit een maatregel",
            "elke maatregel komt bij iedereen gelijk terecht",
            "elke maatregel maakt ongelijkheid altijd kleiner",
        ],
        antwoord=0,
        uitleg="Een voorziening voor iedereen wordt het best gebruikt door wie ze al kon vinden. Daardoor groeit de ongelijkheid in plaats van te krimpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad legt gratis muziekonderwijs aan, en vooral gezinnen die al naar concerten gingen schrijven hun kinderen in. Welk verschijnsel is dit?",
        opties=[
            "het matheüseffect",
            "intergenerationele mobiliteit",
            "horizontale mobiliteit",
            "een referentiegroep",
        ],
        antwoord=0,
        uitleg="De maatregel is voor iedereen, maar komt vooral terecht bij wie al voorsprong had. Dat is het matheüseffect.",
    ),
    dict(
        type="invultekst",
        vraag="Het effect waarbij een maatregel voor iedereen vooral bij de sterkste groepen terechtkomt, heet het ...effect.",
        antwoord=["matheüs", "matheus", "mattheus"],
        uitleg="Het matheüseffect, naar het evangelie van Matteüs: wie heeft, zal nog meer krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het matheüseffect is een argument om maatregelen gericht te maken in plaats van voor iedereen gelijk.",
        antwoord=True,
        uitleg="Waar. Daarom werkt beleid vaak met voorwaarden of met extra hulp bij het aanvragen, zodat de maatregel komt waar hij nodig is.",
    ),
    dict(
        type="waarofniet",
        vraag="Het matheüseffect betekent dat sociaal beleid altijd mislukt.",
        antwoord=False,
        uitleg="Niet waar. Het zegt alleen dat je moet nakijken bij wie een maatregel terechtkomt, niet dat beleid zinloos is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de sociaal-economische status van de ouders zo belangrijk in het onderzoek naar kansenongelijkheid op school?",
        opties=[
            "omdat ze sterk samenhangt met de resultaten van de kinderen",
            "omdat ze het schoolreglement bepaalt",
            "omdat ze de keuze van de leerkracht vastlegt",
            "omdat ze bij elk gezin gelijk is",
        ],
        antwoord=0,
        uitleg="Inkomen, opleiding en beroep van de ouders voorspellen samen een groot deel van het schoolresultaat. Dat is het kernprobleem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan onderwijs de ongelijkheid juist doorgeven in plaats van verkleinen?",
        opties=[
            "doordat de school de taal en gewoonten van één groep verwacht",
            "doordat de school voor iedereen gratis is",
            "doordat de school dezelfde vakken aan iedereen geeft",
            "doordat de school leerplicht oplegt",
        ],
        antwoord=0,
        uitleg="Wie thuis die taal en die gewoonten al meekreeg, heeft meteen voorsprong. Dat is het cultureel kapitaal van Bourdieu uit het vorige thema.",
    ),
    dict(
        type="invultekst",
        vraag="Buiten het gewone leven van een samenleving vallen, heet sociale ...",
        antwoord=["uitsluiting"],
        uitleg="Sociale uitsluiting. Ze hangt samen met een lagere sociale positie, maar valt er niet mee samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker wil weten of de mobiliteit in België de laatste dertig jaar gestegen is. Wat moet hij vergelijken?",
        opties=[
            "de positie van kinderen met die van hun ouders, per periode",
            "de lonen van vandaag met die van dertig jaar terug",
            "het aantal verhuizingen per jaar",
            "het aantal diploma's dat uitgereikt wordt",
        ],
        antwoord=0,
        uitleg="Mobiliteit meet je door generaties te vergelijken. Als het verband tussen ouder en kind zwakker wordt, stijgt de mobiliteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat bij meritocratie altijd de vraag naar de startlijn?",
        opties=[
            "omdat verdienste alleen eerlijk weegt bij een gelijke start",
            "omdat verdienste niets met de startlijn te maken heeft",
            "omdat iedereen in de praktijk gelijk start",
            "omdat de startlijn in het recht is vastgelegd",
        ],
        antwoord=0,
        uitleg="Een wedstrijd met verschillende startlijnen meet niet wie het snelst loopt. Dat is de kern van het bezwaar tegen meritocratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vraagt de fiche om met het matheüseffect en de meritocratie te doen?",
        opties=[
            "ze toepassen op een casus en er argumenten over geven",
            "ze uit het hoofd opsommen met hun jaartal",
            "ze bij een van de vier soorten mobiliteit plaatsen",
            "ze vergelijken met de stratificatiesystemen",
        ],
        antwoord=0,
        uitleg="De fiche vraagt nieuwe casussen te analyseren, de relatie tussen onderwijs en ongelijkheid te onderzoeken en zelf argumenten te geven.",
    ),
]
