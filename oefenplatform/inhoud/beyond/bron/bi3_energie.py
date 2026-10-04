# -*- coding: utf-8 -*-
"""Fotosynthese, celademhaling en gisting — 🌍 Beyond, biologie.

Deel 1 gaat over de fotosynthese: de reactievergelijking, de pigmenten en hun
absorptiespectrum, de lichtreacties in het thylakoïdmembraan en de
donkerreacties in het stroma. Deel 2 gaat over de aerobe celademhaling in haar
vier stappen en over de twee gistingen.

De fiche vraagt bij elk van die processen uitdrukkelijk waar in de cel het
gebeurt, dus komt die plaats in de vragen telkens terug.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke reactievergelijking hoort bij de fotosynthese?",
        opties=[
            "6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂",
            "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O",
            "C₆H₁₂O₆ → 2 C₃H₆O₃",
            "6 O₂ + 6 H₂O → C₆H₁₂O₆ + 6 CO₂",
        ],
        antwoord=0,
        uitleg="De plant maakt met lichtenergie glucose uit koolstofdioxide en water, en "
        "geeft zuurstof af. De tweede vergelijking is net de celademhaling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een organisme dat zijn eigen voedsel maakt uit anorganische stoffen?",
        antwoord=["autotroof", "autotroof organisme"],
        uitleg="Een autotroof organisme, zoals een groene plant, maakt zelf organische "
        "stof. Een heterotroof organisme moet die opeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pigment is het belangrijkste bij de fotosynthese?",
        opties=["chlorofyl a", "caroteen", "xanthofyl", "hemoglobine"],
        antwoord=0,
        uitleg="Chlorofyl a zit in het reactiecentrum van beide fotosystemen. Chlorofyl b "
        "en de carotenoïden vangen licht op en geven het aan chlorofyl a door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ziet een blad groen?",
        opties=[
            "het chlorofyl kaatst groen licht terug",
            "het chlorofyl neemt groen licht het best op",
            "het blad maakt groen pigment uit glucose",
            "de carotenoïden zijn groen",
        ],
        antwoord=0,
        uitleg="Chlorofyl neemt vooral rood en blauw licht op. Groen wordt weerkaatst, "
        "en dat is net de kleur die ons oog bereikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een absorptiespectrum van chlorofyl kan je aflezen welke golflengten het pigment opneemt.",
        antwoord=True,
        uitleg="Het absorptiespectrum zet de opname uit tegen de golflengte. Voor "
        "chlorofyl zie je twee toppen, in het blauw en in het rood, en een dal in het groen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in de chloroplast gebeuren de lichtreacties?",
        opties=[
            "in het thylakoïdmembraan",
            "in het stroma",
            "in de matrix",
            "in het cytoplasma",
        ],
        antwoord=0,
        uitleg="De fotosystemen en het ATP-synthase zitten in het thylakoïdmembraan. De "
        "donkerreacties spelen daarbuiten, in het stroma.",
    ),
    dict(
        type="invultekst",
        vraag="Waar in de chloroplast gebeuren de donkerreacties?",
        antwoord=["stroma", "het stroma"],
        uitleg="Het stroma is de vloeistof rond de thylakoïden. Daar loopt de "
        "Calvincyclus, met de enzymen die koolstofdioxide vastleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat levert de splitsing van water bij de lichtreacties op? Kruis alles aan wat juist is.",
        opties=[
            "zuurstofgas",
            "elektronen voor fotosysteem II",
            "glucose",
            "koolstofdioxide",
        ],
        antwoord=[0, 1],
        uitleg="Water wordt gesplitst in zuurstof, waterstofionen en elektronen. Die "
        "elektronen vullen het gat in fotosysteem II; de zuurstof is afvalgas voor de plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maken de lichtreacties aan voor de donkerreacties? Kruis alles aan wat juist is.",
        opties=["ATP", "NADPH", "glucose", "zetmeel"],
        antwoord=[0, 1],
        uitleg="De lichtreacties leveren ATP en NADPH. De Calvincyclus gebruikt die twee "
        "om koolstofdioxide tot suiker op te bouwen.",
    ),
    dict(
        type="waarofniet",
        vraag="De donkerreacties kunnen alleen in het donker verlopen.",
        antwoord=False,
        uitleg="Ze hebben geen licht nodig, maar ze lopen in het licht gewoon door. Ze "
        "hebben wel het ATP en het NADPH van de lichtreacties nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de cyclus van de donkerreacties waarin koolstofdioxide vastgelegd wordt?",
        antwoord=["Calvincyclus", "calvincyclus", "de Calvincyclus"],
        uitleg="In de Calvincyclus wordt CO₂ aan een bestaande koolstofketen gehangen. "
        "Dat vastleggen heet koolstoffixatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het ATP-synthase in het thylakoïdmembraan?",
        opties=[
            "ATP maken met de protonengradiënt",
            "water splitsen tot zuurstof",
            "glucose afbreken tot pyruvaat",
            "licht opvangen voor fotosysteem I",
        ],
        antwoord=0,
        uitleg="De protonen stromen door het ATP-synthase terug naar het stroma. Die "
        "stroom drijft het enzym aan, dat ADP en fosfaat tot ATP samenvoegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet een waterplant in steeds meer licht en meet de zuurstofproductie. Wat zie je?",
        opties=[
            "ze stijgt eerst en vlakt daarna af",
            "ze blijft onbeperkt stijgen",
            "ze daalt van begin af aan",
            "ze blijft altijd gelijk",
        ],
        antwoord=0,
        uitleg="Eerst is licht de beperkende factor. Daarna wordt iets anders beperkend, "
        "zoals de hoeveelheid koolstofdioxide of de temperatuur, en vlakt de curve af.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant doet alleen fotosynthese en geen celademhaling.",
        antwoord=False,
        uitleg="Een plant ademt dag en nacht. In het licht maakt ze meer zuurstof dan ze "
        "verbruikt, dus lijkt het alsof ze alleen fotosynthese doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof is bij de fotosynthese de bron van de elektronen?",
        opties=["water", "koolstofdioxide", "glucose", "zuurstofgas"],
        antwoord=0,
        uitleg="Water wordt gesplitst en levert de elektronen. Daarom komt de zuurstof "
        "die een plant afgeeft uit het water en niet uit de koolstofdioxide.",
    ),
    dict(
        type="waarofniet",
        vraag="Carotenoïden vangen licht op van golflengten die chlorofyl slecht opneemt.",
        antwoord=True,
        uitleg="Ze nemen vooral blauw en blauwgroen licht op. Zo gebruikt het blad een "
        "breder stuk van het zonlicht, en ze beschermen chlorofyl tegen te veel licht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden bladeren in de herfst geel en rood?",
        opties=[
            "het chlorofyl wordt afgebroken",
            "de carotenoïden worden pas dan gemaakt",
            "het blad neemt meer water op",
            "de chloroplasten worden amyloplasten",
        ],
        antwoord=0,
        uitleg="De carotenoïden zaten er al, maar het groen overheerste. Valt het "
        "chlorofyl weg, dan komen de andere pigmenten tevoorschijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Fotosysteem I en fotosysteem II liggen in dezelfde membraan. Wat doet fotosysteem II eerst?",
        opties=[
            "water splitsen en elektronen doorgeven",
            "NADPH afleveren aan het stroma",
            "glucose tot zetmeel verwerken",
            "koolstofdioxide vastleggen",
        ],
        antwoord=0,
        uitleg="Ondanks hun nummers begint de keten bij fotosysteem II. Dat splitst water "
        "en stuurt de elektronen via de keten naar fotosysteem I, dat NADPH maakt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het vastleggen van koolstofdioxide in een organische molecule?",
        antwoord=["koolstoffixatie", "fixatie", "CO2-fixatie"],
        uitleg="Bij koolstoffixatie wordt anorganische koolstof organisch. Dat is de "
        "stap waarmee de hele voedselketen begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant staat in het donker. Welke processen lopen er dan nog?",
        opties=[
            "de celademhaling",
            "de lichtreacties",
            "het splitsen van water",
            "de opname van licht door chlorofyl",
        ],
        antwoord=0,
        uitleg="Zonder licht vallen de lichtreacties stil, en daarmee na een tijd ook de "
        "donkerreacties. De celademhaling blijft gewoon doorgaan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke reactievergelijking hoort bij de aerobe celademhaling?",
        opties=[
            "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O",
            "6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂",
            "C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂",
            "C₆H₁₂O₆ → 2 C₃H₆O₃",
        ],
        antwoord=0,
        uitleg="Glucose en zuurstof worden koolstofdioxide en water, en er komt energie "
        "vrij die in ATP vastgelegd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in de cel gebeurt de glycolyse?",
        opties=[
            "in het cytoplasma",
            "in de matrix van het mitochondrion",
            "op de cristae",
            "in de kern",
        ],
        antwoord=0,
        uitleg="De glycolyse is de enige stap buiten het mitochondrion. Daarom kan ook "
        "een cel zonder zuurstof die stap nog uitvoeren.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof blijft er na de glycolyse over uit één molecule glucose?",
        antwoord=["pyruvaat", "pyrodruivenzuur", "2 pyruvaat"],
        uitleg="De glycolyse splitst glucose in twee moleculen pyruvaat, ook "
        "pyrodruivenzuur genoemd, en levert daarbij een kleine winst aan ATP.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij de decarboxylatie van pyruvaat? Kruis alles aan wat juist is.",
        opties=[
            "er komt koolstofdioxide vrij",
            "er ontstaat acetyl-coA",
            "er ontstaat glucose",
            "er komt zuurstofgas vrij",
        ],
        antwoord=[0, 1],
        uitleg="Pyruvaat verliest een koolstofatoom als CO₂ en wordt aan co-enzym A "
        "gekoppeld. Dat acetyl-coA gaat de Krebscyclus in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar loopt de Krebscyclus?",
        opties=[
            "in de matrix van het mitochondrion",
            "op de cristae",
            "in het cytoplasma",
            "in het stroma van de chloroplast",
        ],
        antwoord=0,
        uitleg="De enzymen van de Krebscyclus zweven vrij in de matrix. De "
        "elektronentransportketen zit in het membraan van de cristae.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar gebeuren de eindoxidaties?",
        opties=[
            "op de cristae van het mitochondrion",
            "in de matrix van het mitochondrion",
            "in het cytoplasma",
            "in het kernmembraan",
        ],
        antwoord=0,
        uitleg="De cristae zijn de inplooiingen van het binnenmembraan. Daar liggen de "
        "elektronendragers en het ATP-synthase.",
    ),
    dict(
        type="waarofniet",
        vraag="De meeste ATP van de celademhaling komt uit de eindoxidaties.",
        antwoord=True,
        uitleg="De glycolyse en de Krebscyclus leveren maar een klein deel direct. Het "
        "grootste deel komt uit de protonengradiënt bij de eindoxidaties.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof neemt bij de eindoxidaties de elektronen uiteindelijk op?",
        antwoord=["zuurstof", "zuurstofgas", "O2"],
        uitleg="Zuurstof is de laatste elektronenacceptor en wordt daarbij water. Zonder "
        "zuurstof loopt de keten vast en stopt de ATP-productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen NAD⁺ en FAD in de celademhaling?",
        opties=[
            "elektronen en waterstof vervoeren",
            "glucose in twee splitsen",
            "zuurstof naar de cel brengen",
            "ATP afbreken tot ADP",
        ],
        antwoord=0,
        uitleg="Ze worden NADH en FADH₂ en brengen hun lading naar de "
        "elektronentransportketen. Daar wordt die lading in ATP omgezet.",
    ),
    dict(
        type="waarofniet",
        vraag="ATP geeft energie vrij als er een fosfaatgroep van afgesplitst wordt.",
        antwoord=True,
        uitleg="Bij de hydrolyse van ATP naar ADP en fosfaat komt energie vrij. Die "
        "gebruikt de cel voor spiercontractie, transport en biosynthese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat drijft het ATP-synthase van een mitochondrion aan?",
        opties=[
            "een protonengradiënt over het membraan",
            "de warmte van het lichaam",
            "het licht dat de cel bereikt",
            "de afbraak van het membraan zelf",
        ],
        antwoord=0,
        uitleg="De keten pompt protonen naar de intermembraanruimte. Hun terugstroom door "
        "het ATP-synthase levert de energie om ATP te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een spiercel bij zwaar werk en te weinig zuurstof?",
        opties=[
            "melkzuurgisting",
            "alcoholische gisting",
            "fotosynthese",
            "de Calvincyclus",
        ],
        antwoord=0,
        uitleg="Het pyruvaat wordt tot melkzuur omgezet, zodat de glycolyse kan "
        "doorgaan. Dat melkzuur geeft het branderige gevoel in de spier.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee stoffen levert de alcoholische gisting op? Noem de alcohol.",
        antwoord=["ethanol", "ethanol en koolstofdioxide", "alcohol"],
        uitleg="Gist zet glucose om in ethanol en koolstofdioxide. Dat gas doet brooddeeg "
        "rijzen en bier schuimen.",
    ),
    dict(
        type="waarofniet",
        vraag="Gisting levert per molecule glucose meer ATP op dan de aerobe celademhaling.",
        antwoord=False,
        uitleg="Gisting levert maar de kleine winst van de glycolyse. De aerobe "
        "celademhaling haalt er een veelvoud uit, want ze breekt de glucose volledig af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een cel ook bij gisting nog iets aan die omzetting van pyruvaat?",
        opties=[
            "zo komt NAD⁺ weer vrij voor de glycolyse",
            "zo maakt ze extra zuurstof aan",
            "zo bouwt ze glucose weer op",
            "zo maakt ze nieuwe mitochondria",
        ],
        antwoord=0,
        uitleg="De glycolyse heeft NAD⁺ nodig. Door pyruvaat te reduceren komt dat weer "
        "vrij, zodat de glycolyse en dus de ATP-winst kan doorgaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Melkzuurgisting en alcoholische gisting verlopen beide zonder zuurstof.",
        antwoord=True,
        uitleg="Beide zijn anaeroob. Het verschil zit in het product: melkzuur bij spier "
        "en melkzuurbacterie, ethanol en koolstofdioxide bij gist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen van de celademhaling gebeuren in het mitochondrion? Kruis alles aan wat juist is.",
        opties=[
            "de Krebscyclus",
            "de eindoxidaties",
            "de glycolyse",
            "de alcoholische gisting",
        ],
        antwoord=[0, 1],
        uitleg="De decarboxylatie, de Krebscyclus en de eindoxidaties spelen in het "
        "mitochondrion. De glycolyse en de gistingen blijven in het cytoplasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Fotosynthese en celademhaling zijn in zekere zin elkaars omgekeerde. Wat klopt daarbij? Kruis alles aan wat juist is.",
        opties=[
            "wat de ene opneemt, geeft de andere af",
            "de ene bouwt op, de andere breekt af",
            "ze gebeuren in hetzelfde organel",
            "ze hebben beide licht nodig",
        ],
        antwoord=[0, 1],
        uitleg="De fotosynthese is anabool en gebeurt in de chloroplast, de celademhaling "
        "katabool en in het mitochondrion. Alleen de celademhaling heeft geen licht nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker meet in een cel zonder zuurstof dat er nog ATP gemaakt wordt. Welke stap loopt er dan nog?",
        opties=[
            "de glycolyse",
            "de Krebscyclus",
            "de eindoxidaties",
            "de decarboxylatie",
        ],
        antwoord=0,
        uitleg="De glycolyse heeft geen zuurstof nodig en levert al wat ATP. De drie "
        "andere stappen vallen zonder zuurstof stil.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cel maakt ATP aan als voorraad voor weken vooruit.",
        antwoord=False,
        uitleg="ATP is geen voorraad maar een werkmunt: de cel maakt het en gebruikt het "
        "binnen enkele seconden. Als voorraad dienen glycogeen en vet.",
    ),
]
