# -*- coding: utf-8 -*-
"""Organische stoffen: stofklassen en naamgeving — 🌍 Beyond, chemie.

Deel 1 gaat over de stofklassen en hun functionele groep, van alkaan tot amide,
en over de IUPAC-naam: de hoofdketen, de plaatsaanduiding en de uitgang. Deel 2
gaat over de bouw (vertakt of onvertakt, verzadigd of onverzadigd, cyclisch of
aromatisch), over primaire, secundaire en tertiaire alcoholen en aminen, over de
manieren om een molecule voor te stellen, en over de gebruiksnamen.

Een structuurformule tekenen kan in een vraag op het scherm niet. Daarom staat
de bouw hier in woorden of in een beknopte formule zoals CH₃-CH₂-OH, en wordt
er gevraagd wat die bouw betekent.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke functionele groep hoort bij de alcoholen?",
        opties=[
            "een OH-groep aan een koolstofatoom",
            "een COOH-groep aan het einde",
            "een C=O-groep in de keten",
            "een NH₂-groep aan een koolstofatoom",
        ],
        antwoord=0,
        uitleg="De hydroxylgroep maakt van een alkaan een alcohol: ethaan wordt ethanol. "
        "Die groep zit aan koolstof, niet aan zuurstof van water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stofklassen hebben een C=O-groep in hun functionele groep? Kruis alles aan wat juist is.",
        opties=[
            "de aldehyden",
            "de ketonen",
            "de ethers",
            "de alkenen",
        ],
        antwoord=[0, 1],
        uitleg="Bij een aldehyde staat die groep aan het uiteinde, bij een keton "
        "ertussen. Een ether heeft enkel een zuurstofbrug, zonder dubbele binding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de stofklasse met de functionele groep COOH?",
        antwoord=["carbonzuur", "carbonzuren", "een carbonzuur"],
        uitleg="De carboxylgroep COOH maakt een carbonzuur, zoals azijnzuur. Het is dat "
        "waterstofatoom dat als H⁺ kan weggaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een alkaan en een alkeen?",
        opties=[
            "een alkeen heeft minstens één dubbele binding",
            "een alkaan heeft minstens één dubbele binding",
            "een alkeen heeft altijd een ring",
            "een alkaan heeft altijd een vertakking",
        ],
        antwoord=0,
        uitleg="Alkanen zijn verzadigd, alkenen hebben een C=C. Een alkyn heeft een "
        "drievoudige binding.",
    ),
    dict(
        type="waarofniet",
        vraag="De brutoformule van een alkaan met n koolstofatomen is CnH2n+2.",
        antwoord=True,
        uitleg="Butaan heeft vier koolstofatomen en dus tien waterstofatomen: C₄H₁₀. "
        "Bij een alkeen is het CnH2n.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn esters? Kruis alles aan wat juist is.",
        opties=[
            "ethylethanoaat",
            "methylpropanoaat",
            "ethaanzuur",
            "ethaandiol",
        ],
        antwoord=[0, 1],
        uitleg="De naam van een ester bestaat uit twee delen: de alcoholkant vooraan en "
        "de zuurkant met de uitgang -oaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een amine aan de formule?",
        opties=[
            "aan een stikstofatoom met waterstof eraan",
            "aan een zuurstofatoom tussen twee koolstofketens",
            "aan een dubbele binding tussen koolstof en zuurstof",
            "aan een halogeenatoom aan het einde van de keten",
        ],
        antwoord=0,
        uitleg="CH₃-NH₂ is methaanamine. Zit er naast de stikstof ook een C=O, dan is het "
        "een amide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel koolstofatomen zitten er in de hoofdketen van pentaan?",
        opties=[
            "vijf",
            "vier",
            "drie",
            "zes",
        ],
        antwoord=0,
        uitleg="Het stamwoord zegt hoeveel koolstofatomen de hoofdketen heeft: meth- 1, "
        "eth- 2, prop- 3, but- 4, pent- 5, hex- 6.",
    ),
    dict(
        type="invultekst",
        vraag="Welke uitgang krijgt de IUPAC-naam van een keton?",
        antwoord=["-on", "on", "-anon"],
        uitleg="Propanon is het eenvoudigste keton. Een aldehyde eindigt op -al, een "
        "alcohol op -ol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er een cijfer in de naam but-2-een?",
        opties=[
            "het zegt bij welk koolstofatoom de dubbele binding begint",
            "het zegt hoeveel dubbele bindingen er zijn",
            "het zegt hoeveel koolstofatomen de keten heeft",
            "het zegt hoeveel vertakkingen er zijn",
        ],
        antwoord=0,
        uitleg="In but-1-een zit de dubbele binding vooraan, in but-2-een in het midden. "
        "Dat zijn twee verschillende stoffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het nummeren van de hoofdketen begin je aan de kant die de functionele groep het laagste nummer geeft.",
        antwoord=True,
        uitleg="Daarom is het propaan-1-ol en niet propaan-3-ol: je kiest het kleinste "
        "nummer dat kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stofklasse heeft een zuurstofatoom tussen twee koolstofketens, zonder dubbele binding?",
        opties=[
            "de ethers",
            "de esters",
            "de alcoholen",
            "de aldehyden",
        ],
        antwoord=0,
        uitleg="CH₃-O-CH₃ is een ether. Daardoor is er geen OH-groep en vormt een ether "
        "geen waterstofbruggen met zichzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn halogeenalkanen? Kruis alles aan wat juist is.",
        opties=[
            "chloormethaan",
            "broomethaan",
            "methanol",
            "ethaanamine",
        ],
        antwoord=[0, 1],
        uitleg="Bij een halogeenalkaan is minstens één waterstofatoom vervangen door F, "
        "Cl, Br of I.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel OH-groepen heeft een tweewaardige alcohol?",
        antwoord=["twee", "2"],
        uitleg="Ethaandiol heeft er twee, propaantriol drie. De waardigheid van een "
        "alcohol is dus het aantal OH-groepen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de uitgang -diol in ethaandiol?",
        opties=[
            "er zitten twee OH-groepen in de molecule",
            "er zitten twee dubbele bindingen in de keten",
            "er zitten twee koolstofatomen in de keten",
            "er zitten twee zuurstofbruggen in de keten",
        ],
        antwoord=0,
        uitleg="Het telwoord di- staat voor het aantal keer dat de functionele groep "
        "voorkomt, niet voor de lengte van de keten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stofklasse ontstaat als je de OH van een carbonzuur vervangt door NH₂?",
        opties=[
            "een amide",
            "een amine",
            "een ester",
            "een ether",
        ],
        antwoord=0,
        uitleg="Een amide heeft dus zowel de C=O als de stikstof. In een eiwit heet die "
        "verbinding een peptidebinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alkeen heeft een drievoudige binding tussen twee koolstofatomen.",
        antwoord=False,
        uitleg="Een alkeen heeft een dubbele binding; de drievoudige hoort bij een "
        "alkyn, zoals ethyn of acetyleen. Daar staat de uitgang -yn voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet CH₃-CH₂-CHO volgens de IUPAC-regels?",
        opties=[
            "propanal",
            "propanon",
            "propaanzuur",
            "propaan-1-ol",
        ],
        antwoord=0,
        uitleg="De CHO-groep aan het uiteinde maakt er een aldehyde van, met drie "
        "koolstofatomen: propanal.",
    ),
    dict(
        type="waarofniet",
        vraag="In de naam van een ester staat de zuurkant vooraan en de alcoholkant achteraan.",
        antwoord=False,
        uitleg="Het is net omgekeerd: methylethanoaat heeft de methylgroep van de "
        "alcohol vooraan en het ethanoaat van het zuur achteraan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel COOH-groepen heeft een tweewaardig carbonzuur?",
        antwoord=["twee", "2"],
        uitleg="Ethaandizuur, beter bekend als oxaalzuur, heeft er twee. Elk ervan kan "
        "een H⁺ afstaan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een koolstofketen verzadigd is?",
        opties=[
            "er zitten enkel enkelvoudige bindingen tussen de koolstofatomen",
            "er zit minstens één dubbele binding in de keten",
            "er zitten zoveel vertakkingen als mogelijk aan de keten",
            "er zitten geen andere elementen dan koolstof en waterstof in",
        ],
        antwoord=0,
        uitleg="Verzadigd wil zeggen dat er geen waterstof meer bij kan. Een dubbele of "
        "drievoudige binding maakt de keten onverzadigd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beschrijvingen passen bij 2-methylbutaan? Kruis alles aan wat juist is.",
        opties=[
            "vertakt",
            "verzadigd",
            "cyclisch",
            "aromatisch",
        ],
        antwoord=[0, 1],
        uitleg="De methylgroep aan het tweede koolstofatoom maakt de keten vertakt, en "
        "er zit geen dubbele binding in, dus is ze ook verzadigd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een organische molecule met een benzeenring erin?",
        antwoord=["aromatisch", "aromatische", "aromaat"],
        uitleg="De zes koolstofatomen van benzeen delen hun elektronen over de hele ring. "
        "Daardoor reageert benzeen anders dan een gewoon alkeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een alcohol secundair?",
        opties=[
            "als het koolstofatoom met de OH-groep aan twee andere koolstofatomen zit",
            "als het koolstofatoom met de OH-groep aan één ander koolstofatoom zit",
            "als er twee OH-groepen in de molecule zitten",
            "als de OH-groep aan het tweede koolstofatoom van de keten zit",
        ],
        antwoord=0,
        uitleg="Je kijkt dus naar de buren van dat ene koolstofatoom, niet naar het "
        "nummer in de naam. Propaan-2-ol is daarom secundair.",
    ),
    dict(
        type="waarofniet",
        vraag="Een primair amine heeft drie koolstofketens aan het stikstofatoom.",
        antwoord=False,
        uitleg="Bij een amine tel je de ketens aan de stikstof: één bij primair, twee bij "
        "secundair, drie bij tertiair. Bij een alcohol tel je de buren van de koolstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat een skeletnotatie weg?",
        opties=[
            "de koolstofatomen en hun waterstofatomen",
            "enkel de dubbele bindingen",
            "enkel de functionele groepen",
            "de zuurstof- en stikstofatomen",
        ],
        antwoord=0,
        uitleg="Elke hoek en elk uiteinde van de lijn is een koolstofatoom; de waterstof "
        "wordt niet getekend. Functionele groepen schrijf je wel uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorstelling zegt het meest over de ruimtelijke bouw van een molecule?",
        opties=[
            "het bolstaafmodel",
            "de brutoformule",
            "de beknopte structuurformule",
            "de naam volgens IUPAC",
        ],
        antwoord=0,
        uitleg="In een bolstaafmodel zie je ook de hoeken tussen de bindingen. Een "
        "brutoformule zegt enkel hoeveel atomen er zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een uitgebreide en een beknopte structuurformule?",
        opties=[
            "in de beknopte staan de waterstofatomen samengenomen per koolstofatoom",
            "in de beknopte staan de koolstofatomen niet meer",
            "in de uitgebreide staan de functionele groepen niet meer",
            "in de uitgebreide staan enkel de bindingen en geen atomen",
        ],
        antwoord=0,
        uitleg="CH₃-CH₂-OH is beknopt. Uitgebreid teken je elke C-H-binding apart.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof heet in het dagelijks leven drankalcohol?",
        antwoord=["ethanol", "ethaanol"],
        uitleg="Ethanol, CH₃-CH₂-OH, is de alcohol in bier en wijn. Brandspiritus is "
        "ethanol die ondrinkbaar gemaakt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke IUPAC-naam hoort bij azijnzuur?",
        opties=[
            "ethaanzuur",
            "methaanzuur",
            "propaanzuur",
            "butaanzuur",
        ],
        antwoord=0,
        uitleg="Azijnzuur heeft twee koolstofatomen. Mierenzuur is methaanzuur met één, "
        "boterzuur is butaanzuur met vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebruiksnamen horen bij een alcohol? Kruis alles aan wat juist is.",
        opties=[
            "glycerol",
            "glycol",
            "aceton",
            "formol",
        ],
        antwoord=[0, 1],
        uitleg="Glycerol is propaantriol en glycol is ethaandiol, dus allebei alcoholen. "
        "Aceton is een keton en formol een oplossing van methanal.",
    ),
    dict(
        type="waarofniet",
        vraag="Aardgas bestaat hoofdzakelijk uit methaan.",
        antwoord=True,
        uitleg="Methaan is CH₄, het kortste alkaan. Acetyleen in de snijbrander is ethyn, "
        "een heel andere stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke IUPAC-naam hoort bij chloroform?",
        opties=[
            "trichloormethaan",
            "dichloormethaan",
            "tetrachloormethaan",
            "chloorethaan",
        ],
        antwoord=0,
        uitleg="In chloroform zijn drie van de vier waterstofatomen van methaan "
        "vervangen door chloor: CHCl₃.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over benzeen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de ring heeft zes koolstofatomen",
            "de elektronen zijn over de hele ring verdeeld",
            "de ring heeft vijf koolstofatomen",
            "elk koolstofatoom draagt er twee waterstofatomen",
        ],
        antwoord=[0, 1],
        uitleg="Benzeen is C₆H₆: zes koolstofatomen in een vlakke ring, elk met één "
        "waterstofatoom, en de elektronen van de dubbele bindingen liggen over de hele "
        "ring verspreid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de stofklasse van aceton volgens de indeling van de organische stoffen?",
        antwoord=["keton", "ketonen", "een keton"],
        uitleg="Aceton is propanon: een C=O-groep tussen twee koolstofatomen, dus een "
        "keton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stof heeft de beknopte formule CH₃-CH₂-COOH. Welke naam hoort erbij?",
        opties=[
            "propaanzuur",
            "ethaanzuur",
            "propanal",
            "propaan-1-ol",
        ],
        antwoord=0,
        uitleg="Tel het koolstofatoom van de COOH-groep mee: drie in totaal, dus "
        "propaanzuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cyclische stof is altijd ook aromatisch.",
        antwoord=False,
        uitleg="Cyclohexaan is een ring zonder dubbele bindingen en dus niet aromatisch. "
        "Aromatisch hoort bij een benzeenring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is lineair een andere beschrijving dan onvertakt in de spreektaal?",
        opties=[
            "een onvertakte keten is in werkelijkheid een zigzag, geen rechte lijn",
            "een onvertakte keten heeft altijd een dubbele binding",
            "een lineaire keten heeft altijd een functionele groep vooraan",
            "een lineaire keten is altijd langer dan een onvertakte",
        ],
        antwoord=0,
        uitleg="De bindingshoek rond koolstof is ongeveer 109°, dus zelfs een onvertakte "
        "keten staat in zigzag. We noemen ze lineair omdat er geen zijketen aan hangt.",
    ),
    dict(
        type="waarofniet",
        vraag="Formol is een oplossing van methanal in water.",
        antwoord=True,
        uitleg="Methanal is het eenvoudigste aldehyde. Formol werd gebruikt om "
        "preparaten te bewaren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel OH-groepen heeft glycerol?",
        antwoord=["drie", "3"],
        uitleg="Glycerol is propaantriol: drie koolstofatomen met elk een OH-groep. "
        "Daardoor lost het goed op in water.",
    ),
]
