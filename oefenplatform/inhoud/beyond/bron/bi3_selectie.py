# -*- coding: utf-8 -*-
"""Selectie, soortvorming en de menswording — 🌍 Beyond, biologie.

Deel 1 gaat over de mechanismen die een populatie doen veranderen: natuurlijke
en seksuele selectie, gene flow en genetische drift, met het flessenhalseffect
en het stichterseffect erbij. Deel 2 gaat over wat een soort is, over de
vormen van isolatie en de twee manieren waarop soorten ontstaan, en over de
menswording.

De fiche vraagt dat de leerling bij een gegeven voorbeeld het mechanisme of de
isolatievorm benoemt. Daarom is in beide delen ongeveer de helft van de vragen
een voorbeeld waarvan de naam gezocht moet worden, en niet omgekeerd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is natuurlijke selectie?",
        opties=[
            "de omgeving bevoordeelt wie het best aangepast is",
            "een dier kiest zelf welke kenmerken het doorgeeft",
            "een kweker kiest de dieren die zich voortplanten",
            "het toeval bepaalt welke allelen verdwijnen",
        ],
        antwoord=0,
        uitleg="Wie beter past bij zijn omgeving, laat gemiddeld meer nakomelingen na. "
        "Daardoor wordt zijn allel in de volgende generatie talrijker.",
    ),
    dict(
        type="waarofniet",
        vraag="De fitness van een fenotype zegt vooral hoe sterk en gespierd een dier is.",
        antwoord=False,
        uitleg="Fitness zegt hoeveel nakomelingen een fenotype gemiddeld nalaat. Een dier "
        "dat lang leeft maar geen jongen krijgt, heeft een fitness van nul.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de strijd tussen individuen om voedsel, ruimte of een partner?",
        antwoord=["competitie", "de competitie", "concurrentie"],
        uitleg="Er worden meer jongen geboren dan er plaats en voedsel is. Die competitie "
        "zorgt ervoor dat niet iedereen zich even goed voortplant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is seksuele selectie?",
        opties=[
            "partners kiezen elkaar op bepaalde kenmerken",
            "de omgeving kiest wie het langst overleeft",
            "een kweker kiest de ouderdieren uit",
            "het toeval bepaalt wie zich voortplant",
        ],
        antwoord=0,
        uitleg="Wie door partners gekozen wordt, krijgt meer jongen. Daardoor kunnen "
        "kenmerken toenemen die voor het overleven zelfs lastig zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een pauwenhaan zo'n zware staart, ook al bemoeilijkt die het vluchten?",
        opties=[
            "hennen kiezen hanen met de grootste staart",
            "de staart beschermt hem tegen roofdieren",
            "de staart helpt hem warm te blijven",
            "de staart groeit door veel te eten",
        ],
        antwoord=0,
        uitleg="Het nadeel bij het vluchten weegt niet op tegen het voordeel bij het "
        "vinden van een partner. Dat is seksuele selectie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men, met de Engelse term, het binnenkomen en vertrekken van allelen doordat individuen in- of uitwijken?",
        antwoord=["gene flow", "genenstroom", "gene-flow"],
        uitleg="Als er individuen in- of uitwijken, nemen ze hun allelen mee. Daardoor "
        "gaan twee populaties meer op elkaar lijken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de toevallige verschuiving van allelfrequenties, vooral in een kleine populatie?",
        antwoord=["genetische drift", "drift", "de genetische drift"],
        uitleg="In een kleine groep kan een allel verdwijnen zonder dat het slechter was. "
        "Het toeval weegt daar veel zwaarder door dan in een grote populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom speelt genetische drift sterker in een kleine populatie?",
        opties=[
            "het toeval van enkele individuen weegt er zwaar door",
            "kleine populaties hebben meer mutaties",
            "kleine populaties hebben een hogere selectiedruk",
            "kleine populaties planten zich sneller voort",
        ],
        antwoord=0,
        uitleg="Bij tien dieren verandert één sterfgeval de frequenties meteen. Bij tienduizend "
        "dieren valt datzelfde geval helemaal weg in het geheel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een flessenhalseffect?",
        opties=[
            "een populatie krimpt sterk en verliest variatie",
            "een populatie groeit plots heel snel aan",
            "een populatie splitst zich in twee soorten",
            "een populatie krijgt allelen van buitenaf",
        ],
        antwoord=0,
        uitleg="Na een ramp blijven er enkele dieren over, met toevallig maar een deel van "
        "de allelen. Groeit de groep daarna weer aan, dan blijft die armoede zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het stichterseffect?",
        opties=[
            "een kleine groep sticht elders een nieuwe populatie",
            "een hele populatie sterft door een ramp uit",
            "twee populaties wisselen voortdurend allelen uit",
            "een populatie wordt door de mens uitgezet",
        ],
        antwoord=0,
        uitleg="Die stichters dragen maar een deel van de allelen van de oude populatie. "
        "Daardoor verschilt de nieuwe groep van bij het begin.",
    ),
    dict(
        type="waarofniet",
        vraag="Genetische drift bevoordeelt de best aangepaste individuen.",
        antwoord=False,
        uitleg="Drift werkt toevallig en kijkt niet naar aanpassing. Net daarin verschilt "
        "ze van natuurlijke selectie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke mechanismen kunnen de allelfrequenties van een populatie veranderen? Kruis alles aan wat juist is.",
        opties=[
            "natuurlijke selectie",
            "genetische drift",
            "het aantal cellen in een individu",
            "de grootte van één dier",
        ],
        antwoord=[0, 1],
        uitleg="Selectie, drift, gene flow en mutatie zijn de vier motoren van evolutie. "
        "Wat één individu overkomt, telt alleen mee via zijn nakomelingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Gene flow maakt twee populaties met de tijd meer aan elkaar gelijk.",
        antwoord=True,
        uitleg="Zolang er dieren heen en weer trekken, worden de allelen gemengd. Stopt die "
        "uitwisseling, dan kunnen de populaties uit elkaar groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een eiland blijven na een storm nog vijf hagedissen over. Welk mechanisme is dat?",
        opties=[
            "een flessenhalseffect",
            "seksuele selectie",
            "gene flow tussen eilanden",
            "een mutatie in het DNA",
        ],
        antwoord=0,
        uitleg="De overlevenden zijn niet de best aangepaste, maar de toevallig gespaarde. "
        "Hun allelen bepalen voortaan de hele populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten selectie zet de mens zelf in? Kruis alles aan wat juist is.",
        opties=[
            "het kweken van honden met een bepaald uitzicht",
            "het kweken van maïs met grotere korrels",
            "het verdwijnen van soorten door een ijstijd",
            "de kleurverandering van de peper-en-zoutvlinder",
        ],
        antwoord=[0, 1],
        uitleg="Bij kunstmatige selectie kiest de mens de ouderdieren. Een ijstijd en de "
        "roetzwarte bomen zijn natuurlijke selectiedruk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men selectie waarbij niet de omgeving maar de mens de ouderdieren kiest?",
        antwoord=[
            "kunstmatige selectie",
            "artificiële selectie",
            "kunstmatig",
        ],
        uitleg="Alle hondenrassen komen zo uit de wolf voort. Het mechanisme is hetzelfde "
        "als bij natuurlijke selectie, alleen is de selecterende kracht anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kenmerk dat het overleven bemoeilijkt, kan toch in een populatie toenemen.",
        antwoord=True,
        uitleg="Als dat kenmerk genoeg extra partners oplevert, weegt het voordeel op tegen "
        "het risico. De pauwenstaart is daarvan het schoolvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep vogels waait naar een onbewoond eiland en sticht daar een populatie. Welk mechanisme is dat?",
        opties=[
            "het stichterseffect",
            "het flessenhalseffect",
            "natuurlijke selectie",
            "kunstmatige selectie",
        ],
        antwoord=0,
        uitleg="De nieuwe populatie start met de allelen van enkele vogels. Welke dat zijn, "
        "is toeval, en dat bepaalt meteen het verdere verloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verdwijnt een nadelig allel zelden volledig uit een grote populatie?",
        opties=[
            "dragers geven het door zonder het te tonen",
            "mutaties maken dat allel elke generatie opnieuw",
            "selectie werkt niet in grote populaties",
            "grote populaties kennen geen drift",
        ],
        antwoord=0,
        uitleg="Een heterozygote drager is zelf gezond en geeft het allel toch door. "
        "Daardoor blijft het in lage frequentie aanwezig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat evolutie bij bacteriën sneller dan bij zoogdieren? Kruis alles aan wat juist is.",
        opties=[
            "ze hebben heel korte generaties",
            "ze komen in enorme aantallen voor",
            "hun DNA muteert nooit bij het kopiëren",
            "ze hebben geen enkele selectiedruk te verduren",
        ],
        antwoord=[0, 1],
        uitleg="Om de twintig minuten een nieuwe generatie, met miljoenen tegelijk, geeft "
        "heel snel veel variatie. Daarom is resistentie binnen enkele jaren te zien.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer horen twee dieren tot dezelfde soort?",
        opties=[
            "als ze samen vruchtbare nakomelingen kunnen krijgen",
            "als ze er ongeveer hetzelfde uitzien",
            "als ze in hetzelfde gebied leven",
            "als ze hetzelfde voedsel eten",
        ],
        antwoord=0,
        uitleg="Het gaat om vruchtbare nakomelingen. Een paard en een ezel krijgen wel een "
        "muildier, maar dat muildier is onvruchtbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het ontstaan van een nieuwe soort uit een bestaande?",
        antwoord=["soortvorming", "de soortvorming", "speciatie"],
        uitleg="Daarvoor is isolatie nodig: twee groepen die niet meer met elkaar "
        "voortplanten, groeien uit elkaar tot ze dat ook niet meer kúnnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is nodig voor soortvorming? Kruis alles aan wat juist is.",
        opties=[
            "variatie binnen de oorspronkelijke populatie",
            "isolatie tussen de twee groepen",
            "een even groot aantal dieren in beide groepen",
            "een even warm klimaat voor beide groepen",
        ],
        antwoord=[0, 1],
        uitleg="Zonder isolatie mengen de allelen weer en blijft het één soort. Mutatie, "
        "selectie en drift doen daarna het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is geografische isolatie?",
        opties=[
            "een rivier of gebergte scheidt de twee groepen",
            "de twee groepen paren in een ander seizoen",
            "de twee groepen hebben een andere balts",
            "de bevruchte eicel sterft meteen af",
        ],
        antwoord=0,
        uitleg="Een barrière in het landschap belet de uitwisseling. Dat is de bekendste "
        "aanleiding tot allopatrische soortvorming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kikkersoorten in hetzelfde moeras kwaken verschillend en paren daardoor niet. Welke isolatie is dat?",
        opties=[
            "gedragsisolatie",
            "geografische isolatie",
            "temporele isolatie",
            "gametische isolatie",
        ],
        antwoord=0,
        uitleg="Het gaat om balts- en lokgedrag: ze herkennen elkaar niet als partner. De "
        "dieren zitten letterlijk naast elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee plantensoorten bloeien in een ander deel van het jaar. Welke isolatie is dat?",
        opties=[
            "temporele isolatie",
            "habitatisolatie",
            "morfologische isolatie",
            "isolatie na bevruchting",
        ],
        antwoord=0,
        uitleg="Temporeel betekent in de tijd. Hun stuifmeel komt elkaar simpelweg nooit "
        "tegen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men isolatie doordat twee soorten in hetzelfde gebied een andere leefplek bewonen?",
        antwoord=["habitatisolatie", "habitat", "habitatisolatie."],
        uitleg="De ene soort zit in de boomtoppen, de andere op de grond. Ze delen het "
        "gebied, maar ontmoeten elkaar niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de isolatie waarbij een zaadcel de eicel van de andere soort niet kan bevruchten?",
        antwoord=["gametische isolatie", "gametisch", "gameetisolatie"],
        uitleg="De gameten herkennen elkaar niet, dus komt het niet tot een zygote. Dat is "
        "nog altijd prezygotische isolatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen prezygotische en postzygotische isolatie?",
        opties=[
            "prezygotisch werkt voor er een zygote is",
            "postzygotisch werkt voor er een zygote is",
            "prezygotisch geldt alleen bij planten",
            "postzygotisch geldt alleen bij dieren",
        ],
        antwoord=0,
        uitleg="Gedrag, tijdstip, bouw en gameten beletten de bevruchting zelf. Sterft het "
        "embryo of is het jong onvruchtbaar, dan is het postzygotisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een muildier is een voorbeeld van isolatie na de bevruchting.",
        antwoord=True,
        uitleg="Paard en ezel krijgen wel een jong, maar dat jong is onvruchtbaar. De twee "
        "soorten blijven dus gescheiden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij allopatrische soortvorming blijven de twee groepen in hetzelfde gebied wonen.",
        antwoord=False,
        uitleg="Allo betekent ander, patria betekent vaderland: de groepen raken juist in "
        "de ruimte gescheiden. Blijven ze samen, dan heet het sympatrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor sympatrische soortvorming? Kruis alles aan wat juist is.",
        opties=[
            "de twee groepen blijven in hetzelfde gebied",
            "de isolatie komt van gedrag, tijd of leefplek",
            "er ligt altijd een gebergte tussen",
            "ze komt alleen bij bacteriën voor",
        ],
        antwoord=[0, 1],
        uitleg="Sym betekent samen. Zonder barrière in het landschap moet de isolatie van "
        "iets anders komen, zoals een ander voedsel of een andere bloeitijd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de hele groep mensachtigen, waartoe ook de uitgestorven soorten behoren?",
        antwoord=["hominiden", "mensachtigen", "hominide"],
        uitleg="De mens is daarvan de enige soort die nog leeft. Alle andere hominiden zijn "
        "uitgestorven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deelt de mens met de mensapen? Kruis alles aan wat juist is.",
        opties=[
            "een grijpbare hand met een duim",
            "sociale groepen met onderlinge banden",
            "een volledig rechtopgaande gang",
            "een strottenhoofd dat gesproken taal toelaat",
        ],
        antwoord=[0, 1],
        uitleg="Handen en sociaal gedrag delen we met de andere mensapen. Permanent "
        "rechtop lopen en de bouw voor spraak zijn eigen aan de mens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verandering wordt als de eerste grote stap in de menswording gezien?",
        opties=[
            "het rechtop gaan lopen",
            "het groter worden van de hersenen",
            "het ontstaan van gesproken taal",
            "het gebruik van vuur",
        ],
        antwoord=0,
        uitleg="De fossielen tonen dat het rechtop lopen vooraf gaat aan de grote hersenen. "
        "Daardoor kwamen de handen vrij voor dragen en voor werktuigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lichamelijke veranderingen horen bij het rechtop lopen?",
        opties=[
            "een kommervormig bekken en een S-vormige wervelkolom",
            "een langere arm dan been en gebogen vingers",
            "een naar voren geplaatst achterhoofdsgat",
            "een grotere kaak met langere hoektanden",
        ],
        antwoord=0,
        uitleg="Het bekken draagt de organen, de wervelkolom vangt de schokken op en de "
        "voet krijgt een gewelf. Ook het achterhoofdsgat verschuift naar onder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groter hersenvolume kostte onze voorouders ook iets.",
        antwoord=True,
        uitleg="Hersenen gebruiken veel energie en een groter hoofd maakt de geboorte "
        "moeilijker. Dat het toch doorzette, wijst op een flink voordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met theory of mind?",
        opties=[
            "kunnen inschatten wat een ander denkt of voelt",
            "kunnen rekenen met grote getallen",
            "kunnen onthouden waar voedsel ligt",
            "kunnen leren door iets na te doen",
        ],
        antwoord=0,
        uitleg="Wie weet dat een ander iets niet weet, kan samenwerken, leren en misleiden. "
        "Dat is een hoeksteen van onze sociale intelligentie.",
    ),
    dict(
        type="waarofniet",
        vraag="De mens stamt rechtstreeks af van de chimpansee.",
        antwoord=False,
        uitleg="Mens en chimpansee hebben een gemeenschappelijke voorouder die niet meer "
        "bestaat. Het zijn twee takken naast elkaar, geen lijn achter elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde natuurlijke selectie bij de menswording?",
        opties=[
            "wie beter liep, droeg of samenwerkte, liet meer jongen na",
            "onze voorouders kozen zelf welke kenmerken ze doorgaven",
            "de omgeving veranderde het DNA van onze voorouders",
            "de kenmerken ontstonden zonder enige variatie",
        ],
        antwoord=0,
        uitleg="De variatie was er toevallig, de savanne deed de rest. Kenmerken die daar "
        "van pas kwamen, werden in de populatie talrijker.",
    ),
]
