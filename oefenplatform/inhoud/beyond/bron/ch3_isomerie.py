# -*- coding: utf-8 -*-
"""Isomerie en chiraliteit — 🌍 Beyond, chemie.

Deel 1 gaat over de structuurisomerie: keten-, plaats- en functie-isomerie, en
over het aantal isomeren dat bij een gegeven formule hoort. Deel 2 gaat over de
stereo-isomerie: Z/E-isomerie bij een dubbele binding, het asymmetrische
koolstofatoom, spiegelbeeldisomeren, gepolariseerd licht, het racemisch mengsel
en de regel 2ⁿ.

Isomeren tekenen kan in een vraag op het scherm niet. De vragen gaan dus over
het soort isomerie, over het aantal, en over de eigenschappen die daaruit
volgen, met de formule telkens in woorden of beknopt uitgeschreven.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat hebben twee isomeren altijd gemeen?",
        opties=[
            "dezelfde brutoformule",
            "dezelfde structuurformule",
            "dezelfde stofklasse",
            "hetzelfde kookpunt",
        ],
        antwoord=0,
        uitleg="Isomeren hebben evenveel atomen van elk element, maar die atomen zitten "
        "anders aan elkaar. Daardoor zijn het verschillende stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Butaan en 2-methylpropaan hebben dezelfde formule C₄H₁₀. Welk soort isomerie is dat?",
        opties=[
            "ketenisomerie",
            "plaatsisomerie",
            "functie-isomerie",
            "spiegelbeeldisomerie",
        ],
        antwoord=0,
        uitleg="Het verschil zit in de vorm van de keten: onvertakt tegenover vertakt. "
        "De functionele groep is er niet en de stofklasse blijft dezelfde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de isomerie waarbij de functionele groep op een andere plaats in dezelfde keten zit?",
        antwoord=["plaatsisomerie", "plaats", "plaatsisomeer"],
        uitleg="Propaan-1-ol en propaan-2-ol zijn plaatsisomeren: dezelfde keten, "
        "dezelfde OH-groep, een andere plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Ethanol en dimethylether hebben beide de formule C₂H₆O. Welk soort isomerie is dat?",
        opties=[
            "functie-isomerie",
            "ketenisomerie",
            "plaatsisomerie",
            "geometrische isomerie",
        ],
        antwoord=0,
        uitleg="De ene is een alcohol, de andere een ether. Bij functie-isomerie "
        "verandert de stofklasse zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee isomeren hebben altijd hetzelfde smelt- en kookpunt.",
        antwoord=False,
        uitleg="Butaan kookt bij −0,5 °C en 2-methylpropaan bij −12 °C. De vertakte "
        "keten raakt haar buren minder goed, dus is er minder energie nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel structuurisomeren bestaan er van C₄H₁₀?",
        opties=[
            "twee",
            "een",
            "drie",
            "vier",
        ],
        antwoord=0,
        uitleg="Butaan en 2-methylpropaan, en meer niet. Bij C₅H₁₂ zijn er al drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel structuurisomeren bestaan er van C₅H₁₂?",
        opties=[
            "drie",
            "twee",
            "vier",
            "vijf",
        ],
        antwoord=0,
        uitleg="Pentaan, 2-methylbutaan en 2,2-dimethylpropaan. Hoe langer de keten, hoe "
        "sneller het aantal isomeren oploopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke paren zijn isomeren van elkaar? Kruis alles aan wat juist is.",
        opties=[
            "butaan en 2-methylpropaan",
            "propaan-1-ol en propaan-2-ol",
            "ethaangas en propaangas",
            "methanol en ethaanzuur",
        ],
        antwoord=[0, 1],
        uitleg="Isomeren moeten dezelfde brutoformule hebben. Ethaan en propaan "
        "verschillen in het aantal koolstofatomen, dus zijn ze geen isomeren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel verschillende elementen moeten twee isomeren gemeen hebben?",
        antwoord=["alle", "allemaal", "alle elementen"],
        uitleg="Niet alleen dezelfde elementen, ook evenveel atomen van elk. Anders is "
        "het een andere brutoformule en dus geen isomerie.",
    ),
    dict(
        type="meerkeuze",
        vraag="But-1-een en but-2-een zijn isomeren. Waarin verschillen ze?",
        opties=[
            "in de plaats van de dubbele binding",
            "in het aantal koolstofatomen van de keten",
            "in de stofklasse",
            "in de vorm van de keten",
        ],
        antwoord=0,
        uitleg="Allebei zijn het alkenen met vier koolstofatomen. Alleen zit de dubbele "
        "binding vooraan of in het midden, dus is het plaatsisomerie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aldehyde en een keton met dezelfde brutoformule zijn functie-isomeren.",
        antwoord=True,
        uitleg="Propanal en propanon zijn beide C₃H₆O. De C=O-groep staat aan het "
        "uiteinde of ertussen, en dat maakt een andere stofklasse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een vertakte keten vluchtiger dan een onvertakte met dezelfde formule?",
        opties=[
            "de moleculen raken elkaar over een kleiner oppervlak",
            "de moleculen zijn zwaarder dan de onvertakte",
            "de moleculen vormen waterstofbruggen met elkaar",
            "de moleculen hebben een hogere molaire massa",
        ],
        antwoord=0,
        uitleg="Minder contact betekent zwakkere londonkrachten tussen de moleculen, en "
        "dus een lager kookpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een carbonzuur en een ester met dezelfde formule zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zijn functie-isomeren van elkaar",
            "ze hebben dezelfde brutoformule",
            "ze hebben dezelfde functionele groep",
            "ze reageren op dezelfde manier met een base",
        ],
        antwoord=[0, 1],
        uitleg="Ethaanzuur en methylmethanoaat zijn beide C₂H₄O₂, maar het zuur staat een "
        "H⁺ af en de ester niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de isomerie waarbij de keten vertakt of onvertakt loopt?",
        antwoord=["ketenisomerie", "keten", "ketenisomeer"],
        uitleg="Bij ketenisomerie blijft de stofklasse gelijk en verandert alleen de "
        "vorm van het skelet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stof heeft de formule C₃H₈O. Welke stofklassen kunnen daarbij horen?",
        opties=[
            "een alcohol of een ether",
            "een aldehyde of een keton",
            "een carbonzuur of een ester",
            "een amine of een amide",
        ],
        antwoord=0,
        uitleg="Met één zuurstofatoom en een verzadigde keten kan de zuurstof in een "
        "OH-groep of in een brug tussen twee koolstofatomen zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft methaan geen isomeren?",
        opties=[
            "er is maar één manier om één koolstof en vier waterstof te verbinden",
            "er zitten te weinig waterstofatomen in de molecule om te vertakken",
            "er zit geen functionele groep in de molecule",
            "er zit geen dubbele binding in de molecule",
        ],
        antwoord=0,
        uitleg="Pas vanaf vier koolstofatomen kan een keten vertakken. Methaan, ethaan en "
        "propaan hebben dus elk één vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Plaatsisomeren horen tot dezelfde stofklasse.",
        antwoord=True,
        uitleg="De functionele groep blijft dezelfde en verhuist alleen. Verandert de "
        "stofklasse, dan heet het functie-isomerie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel plaatsisomeren heeft een alcohol met de keten van butaan?",
        opties=[
            "twee",
            "een",
            "drie",
            "vier",
        ],
        antwoord=0,
        uitleg="Butaan-1-ol en butaan-2-ol. De OH-groep aan het derde of vierde "
        "koolstofatoom geeft dezelfde stof, want je mag de keten van de andere kant "
        "nummeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Isomeren hebben altijd dezelfde geur en dezelfde smaak.",
        antwoord=False,
        uitleg="Onze reukcellen voelen de vorm van een molecule. Twee isomeren passen "
        "dus niet op dezelfde manier, en dat ruikt anders.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel structuurisomeren bestaan er van C₃H₈?",
        antwoord=["een", "één", "1"],
        uitleg="Propaan kan niet vertakken: een zijketen aan het middelste koolstofatoom "
        "zou butaan maken. Dus is er maar één vorm.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is nodig voor Z/E-isomerie bij een dubbele binding?",
        opties=[
            "elk koolstofatoom van de dubbele binding draagt twee verschillende groepen",
            "de dubbele binding zit precies in het midden van de koolstofketen",
            "de molecule bevat minstens één asymmetrisch koolstofatoom",
            "de koolstofketen bestaat uit minstens vier koolstofatomen op een rij",
        ],
        antwoord=0,
        uitleg="Zitten aan één kant twee gelijke groepen, dan geeft draaien dezelfde "
        "stof. But-2-een heeft wel een Z- en een E-vorm, but-1-een niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bestaat er geen Z/E-isomerie rond een enkelvoudige binding?",
        opties=[
            "die binding kan vrij draaien",
            "die binding is te kort om te draaien",
            "die binding heeft geen pi-binding nodig",
            "die binding zit altijd aan het einde van de keten",
        ],
        antwoord=0,
        uitleg="Een sigma-binding is coaxiaal en laat draaien toe. De pi-binding van een "
        "dubbele binding zet dat draaien vast.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een koolstofatoom met vier verschillende groepen eraan?",
        antwoord=["asymmetrisch", "chiraal", "asymmetrisch koolstofatoom"],
        uitleg="Zo'n koolstofatoom maakt de molecule chiraal: ze valt niet samen met haar "
        "spiegelbeeld, net zoals je linker- en rechterhand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel stereo-isomeren horen bij een molecule met drie asymmetrische koolstofatomen?",
        opties=[
            "acht",
            "zes",
            "drie",
            "negen",
        ],
        antwoord=0,
        uitleg="Het aantal is 2ⁿ, met n het aantal asymmetrische koolstofatomen: 2³ is "
        "acht.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee spiegelbeeldisomeren draaien het vlak van gepolariseerd licht naar dezelfde kant.",
        antwoord=False,
        uitleg="Ze draaien het over dezelfde hoek, maar naar de andere kant. Daarom heet "
        "het ook optische isomerie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een racemisch mengsel?",
        opties=[
            "een mengsel met evenveel van beide spiegelbeeldisomeren",
            "een mengsel van een Z-isomeer en een E-isomeer in gelijke delen",
            "een mengsel van twee functie-isomeren in gelijke delen",
            "een mengsel van een carbonzuur en zijn eigen ester",
        ],
        antwoord=0,
        uitleg="Omdat de twee helften het licht naar de andere kant draaien, heffen ze "
        "elkaar op: het mengsel draait het vlak helemaal niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen zijn gelijk voor twee spiegelbeeldisomeren? Kruis alles aan wat juist is.",
        opties=[
            "het smeltpunt",
            "de molaire massa",
            "de draaiingszin van gepolariseerd licht",
            "de werking in het lichaam",
        ],
        antwoord=[0, 1],
        uitleg="In een gewone omgeving gedragen ze zich hetzelfde. In het lichaam niet, "
        "want enzymen zijn zelf chiraal en passen maar op één van de twee.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort licht gebruik je om optische isomeren van elkaar te onderscheiden?",
        antwoord=["gepolariseerd licht", "gepolariseerd", "polarisatielicht"],
        uitleg="In gepolariseerd licht trilt het licht in één vlak. Een optisch actieve "
        "stof draait dat vlak over een meetbare hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je dat but-2-een een Z- en een E-vorm heeft?",
        opties=[
            "aan elk koolstofatoom van de dubbele binding zit een methylgroep en een waterstofatoom",
            "aan elk koolstofatoom van de dubbele binding zitten twee methylgroepen samen",
            "de dubbele binding zit aan het einde van de keten, bij het eerste koolstofatoom",
            "de koolstofketen is vertakt aan het tweede koolstofatoom van de keten",
        ],
        antwoord=0,
        uitleg="Twee verschillende groepen aan elke kant: dan maakt het uit of de "
        "methylgroepen aan dezelfde kant staan of niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de letter Z bij Z/E-isomerie?",
        opties=[
            "de twee voorrangsgroepen staan aan dezelfde kant",
            "de twee voorrangsgroepen staan aan weerszijden",
            "de molecule draait het licht naar links",
            "de molecule heeft een asymmetrisch koolstofatoom",
        ],
        antwoord=0,
        uitleg="Z komt van het Duitse zusammen, samen; E van entgegen, tegenover.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecule met één asymmetrisch koolstofatoom is altijd chiraal.",
        antwoord=True,
        uitleg="Met één zo'n koolstofatoom zijn er twee spiegelbeeldvormen, en die zijn "
        "niet over elkaar te leggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is propaan-2-ol niet chiraal?",
        opties=[
            "het middelste koolstofatoom draagt twee gelijke methylgroepen",
            "het middelste koolstofatoom draagt geen enkele OH-groep meer",
            "de koolstofketen is te kort om een spiegelbeeld te hebben",
            "de molecule bevat een dubbele binding tussen twee koolstofatomen",
        ],
        antwoord=0,
        uitleg="Voor chiraliteit moeten alle vier de groepen verschillen. Hier zijn er "
        "twee gelijk, dus valt de molecule samen met haar spiegelbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over stereo-isomerie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de atomen zitten in dezelfde volgorde aan elkaar",
            "het verschil zit in de ruimtelijke plaatsing",
            "de brutoformule van de twee isomeren verschilt",
            "de stofklasse van de twee isomeren verschilt",
        ],
        antwoord=[0, 1],
        uitleg="Bij structuurisomerie verandert de volgorde van de atomen, bij "
        "stereo-isomerie alleen hun plaats in de ruimte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel stereo-isomeren horen bij een molecule met twee asymmetrische koolstofatomen?",
        antwoord=["vier", "4"],
        uitleg="2² is vier. De regel 2ⁿ geldt voor elk extra asymmetrisch koolstofatoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een medicijn wordt als racemisch mengsel verkocht. Wat kan daarvan het nadeel zijn?",
        opties=[
            "de helft werkt niet of werkt zelfs anders in het lichaam",
            "de helft van het mengsel lost helemaal niet op in water",
            "het mengsel heeft daardoor een lager smeltpunt dan verwacht",
            "het mengsel draait het vlak van het licht veel te sterk",
        ],
        antwoord=0,
        uitleg="Receptoren en enzymen zijn chiraal. Daarom wordt een medicijn soms "
        "gescheiden, zodat enkel de werkzame vorm overblijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel asymmetrische koolstofatomen heeft 2-chloorbutaan?",
        opties=[
            "een",
            "geen",
            "twee",
            "drie",
        ],
        antwoord=0,
        uitleg="Het tweede koolstofatoom draagt een waterstofatoom, een chlooratoom, een "
        "methylgroep en een ethylgroep: vier verschillende groepen.",
    ),
    dict(
        type="waarofniet",
        vraag="Z/E-isomeren zijn structuurisomeren.",
        antwoord=False,
        uitleg="Ze zijn stereo-isomeren: de volgorde van de atomen is gelijk, alleen hun "
        "plaats in de ruimte verschilt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hebben een Z- en een E-isomeer een verschillend kookpunt?",
        opties=[
            "hun vorm maakt hun polariteit en hun onderlinge krachten anders",
            "hun molaire massa is niet gelijk aan die van de andere vorm",
            "hun brutoformule verschilt op één atoom van de andere vorm",
            "hun functionele groep is een andere dan bij de andere vorm",
        ],
        antwoord=0,
        uitleg="Bij de Z-vorm liggen de groepen aan dezelfde kant, en dan versterken hun "
        "dipooltjes elkaar; bij de E-vorm heffen ze elkaar vaker op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een racemisch mengsel draait het vlak van gepolariseerd licht niet.",
        antwoord=True,
        uitleg="De twee helften draaien even sterk naar de andere kant en heffen elkaar "
        "precies op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je twee isomeren die elkaars spiegelbeeld zijn?",
        antwoord=["spiegelbeeldisomeren", "enantiomeren", "optische isomeren"],
        uitleg="Ze heten ook enantiomeren of optische isomeren, en ze bestaan dankzij een "
        "asymmetrisch koolstofatoom.",
    ),
]
