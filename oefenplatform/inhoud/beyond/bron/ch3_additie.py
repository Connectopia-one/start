# -*- coding: utf-8 -*-
"""Organische reacties: additie, eliminatie en condensatie — 🌍 Beyond, chemie.

Deel 1 gaat over de additie: de elektrofiele additie bij een alkeen of een
alkyn met diwaterstof, een dihalogeen, een waterstofhalogenide of water, de
regel van Markownikov, de verzadigingsgraad, en de nucleofiele additie bij een
aldehyde of een keton. Deel 2 gaat over de eliminatie: de dehydratatie en de
dehydrogenatie van een alcohol, met het verschil tussen een primaire, een
secundaire en een tertiaire alcohol, en de eliminatie bij een halogeenalkaan.

De vragen vragen telkens naar de naam en de stofklasse van het product, want
een structuurformule tekenen kan op het scherm niet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een additiereactie aan een alkeen?",
        opties=[
            "de pi-binding gaat open en er komen twee groepen bij",
            "er gaat een groep weg en er ontstaat een dubbele binding",
            "een atoom wordt vervangen door een ander atoom",
            "twee moleculen koppelen en er komt water vrij",
        ],
        antwoord=0,
        uitleg="De sigma-binding tussen de twee koolstofatomen blijft bestaan. De keten "
        "wordt daardoor verzadigd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de additie van diwaterstof aan etheen?",
        opties=[
            "ethaan",
            "ethyn",
            "ethanol",
            "chloorethaan",
        ],
        antwoord=0,
        uitleg="Elk koolstofatoom krijgt een waterstofatoom bij. Die hydrogenering heeft "
        "een katalysator van nikkel of platina nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Wat ontstaat er bij de additie van broom aan een alkeen?",
        antwoord=["een dibroomalkaan", "dibroomalkaan", "dibroomverbinding"],
        uitleg="Elk koolstofatoom van de dubbele binding krijgt één broomatoom. Het "
        "broomwater verliest daarbij zijn kleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men broomwater om te testen of een stof onverzadigd is?",
        opties=[
            "het broom reageert weg en de bruine kleur verdwijnt",
            "het broom maakt de oplossing bruiner dan ervoor",
            "het broom slaat neer als een vaste stof",
            "het broom maakt de oplossing zuurder te meten",
        ],
        antwoord=0,
        uitleg="Bij een alkaan gebeurt er in het donker niets en blijft de kleur. Bij een "
        "alkeen of alkyn ontkleurt het meteen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alkyn kan twee keer diwaterstof opnemen.",
        antwoord=True,
        uitleg="Eerst wordt de drievoudige binding een dubbele, dan een enkelvoudige. Zijn "
        "verzadigingsgraad is dus twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de regel van Markownikov?",
        opties=[
            "het waterstofatoom gaat naar het koolstofatoom met het meeste waterstof",
            "het waterstofatoom gaat naar het koolstofatoom met het minste waterstof",
            "het halogeen gaat altijd naar het eerste koolstofatoom van de keten",
            "de twee groepen komen altijd aan hetzelfde koolstofatoom terecht",
        ],
        antwoord=0,
        uitleg="Het halogeen of de OH-groep komt dus op het meest vertakte koolstofatoom "
        "terecht. Zo weet je welk van de twee mogelijke producten overheerst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de additie van water aan etheen, met een zuur als katalysator?",
        opties=[
            "ethanol",
            "ethaanzuur",
            "ethaan",
            "ethaandiol",
        ],
        antwoord=0,
        uitleg="Het waterstofatoom en de OH-groep komen elk aan één koolstofatoom. Zo "
        "maakt men industrieel alcohol uit etheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen kunnen aan een alkeen adderen? Kruis alles aan wat juist is.",
        opties=[
            "waterstofchloride",
            "diwaterstof",
            "natriumchloride",
            "koolstofdioxide",
        ],
        antwoord=[0, 1],
        uitleg="Aan een dubbele binding adderen diwaterstof, een dihalogeen, een "
        "waterstofhalogenide en water. Een zout addeert niet aan een dubbele binding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de additie van diwaterstof aan een onverzadigde stof?",
        antwoord=["hydrogenering", "hydrogenatie", "hydrogeneren"],
        uitleg="Zo maakt men van vloeibare olie een vaster vet. Er is telkens een "
        "katalysator bij nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk soort deeltje valt aan bij de additie van HBr aan een alkeen?",
        opties=[
            "een elektrofiel",
            "een nucleofiel",
            "een radicaal",
            "een hydroxide-ion",
        ],
        antwoord=0,
        uitleg="De pi-elektronen van de dubbele binding trekken het lichtpositieve "
        "waterstofatoom aan. Daarom heet het een elektrofiele additie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een nucleofiele additie aan een aldehyde ontstaat er een primaire alcohol.",
        antwoord=True,
        uitleg="De C=O-groep aan het uiteinde wordt een CH-OH-groep aan het uiteinde. Bij "
        "een keton krijg je een secundaire alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de additie van diwaterstof aan propanon?",
        opties=[
            "propaan-2-ol",
            "propaan-1-ol",
            "propanal",
            "propaanzuur",
        ],
        antwoord=0,
        uitleg="De C=O-groep zit in het midden, dus komt de OH-groep op het tweede "
        "koolstofatoom. Dat is een secundaire alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verloopt de additie aan een aldehyde nucleofiel en die aan een alkeen elektrofiel?",
        opties=[
            "het koolstofatoom van de C=O-groep is lichtpositief en trekt een nucleofiel aan",
            "het koolstofatoom van de C=O-groep heeft een ongepaard elektron",
            "een aldehyde heeft geen pi-binding om aan te vallen",
            "een alkeen heeft een vrij elektronenpaar om aan te bieden",
        ],
        antwoord=0,
        uitleg="Zuurstof trekt de elektronen van de dubbele binding naar zich toe. Bij een "
        "alkeen zijn beide atomen gelijk, en liggen de pi-elektronen juist bloot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de verzadigingsgraad zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zegt hoeveel keer diwaterstof er kan adderen",
            "een alkyn heeft een verzadigingsgraad van twee",
            "een alkaan heeft een verzadigingsgraad van een",
            "ze zegt hoeveel koolstofatomen de keten heeft",
        ],
        antwoord=[0, 1],
        uitleg="Een alkaan is al verzadigd, dus is zijn verzadigingsgraad nul. Elke "
        "dubbele binding telt voor één en elke drievoudige voor twee.",
    ),
    dict(
        type="invultekst",
        vraag="Wat ontstaat er bij de additie van diwaterstof aan een aldehyde?",
        antwoord=["een primaire alcohol", "primaire alcohol", "alcohol"],
        uitleg="Bij een keton krijg je een secundaire alcohol. Het verschil zit in de "
        "plaats van de oorspronkelijke C=O-groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat HCl adderen aan propeen. Welk product overheerst volgens Markownikov?",
        opties=[
            "2-chloorpropaan",
            "1-chloorpropaan",
            "1,2-dichloorpropaan",
            "propaan-2-ol",
        ],
        antwoord=0,
        uitleg="Het waterstofatoom gaat naar het eerste koolstofatoom, dat er al twee "
        "heeft. Het chlooratoom komt dus op het tweede terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een additie aan een alkeen geen substitutie?",
        opties=[
            "er gaat geen enkel atoom weg uit de molecule",
            "er komt geen enkel atoom bij in de molecule",
            "de keten wordt er korter van dan ervoor",
            "er komt water vrij tijdens de reactie",
        ],
        antwoord=0,
        uitleg="Alles van de twee moleculen zit in het product. Bij een substitutie "
        "verdwijnt er altijd iets uit de oorspronkelijke stof.",
    ),
    dict(
        type="waarofniet",
        vraag="De additie van water aan een alkeen verloopt zonder katalysator.",
        antwoord=False,
        uitleg="Er is een zuur bij nodig. Zonder dat zou water veel te zwak zijn om de "
        "dubbele binding aan te vallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cycloalkeen kan geen additie ondergaan omdat het een ring is.",
        antwoord=False,
        uitleg="De ring blijft gewoon bestaan en de dubbele binding erin gaat open. Het is "
        "de ring van benzeen die niet addeert.",
    ),
    dict(
        type="invultekst",
        vraag="Welke binding gaat open bij een additie aan een alkyn?",
        antwoord=["een pi-binding", "pi-binding", "pi"],
        uitleg="Bij een alkyn zijn er twee pi-bindingen, dus kan de additie twee keer "
        "gebeuren. De sigma-binding blijft telkens staan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij de dehydratatie van een alcohol?",
        opties=[
            "er gaat water uit en er ontstaat een dubbele binding",
            "er komt water bij en er verdwijnt een dubbele binding",
            "er gaat diwaterstof uit en er ontstaat een aldehyde",
            "er komt zuurstof bij en er ontstaat een carbonzuur",
        ],
        antwoord=0,
        uitleg="De OH-groep en een waterstofatoom van het buuratoom gaan samen als water "
        "weg. Wat overblijft is een alkeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de dehydrogenatie van een primaire alcohol?",
        opties=[
            "een aldehyde",
            "een keton",
            "een ether",
            "een alkeen",
        ],
        antwoord=0,
        uitleg="Er gaat diwaterstof uit en de OH-groep wordt een C=O-groep aan het "
        "uiteinde. Bij een secundaire alcohol krijg je een keton.",
    ),
    dict(
        type="invultekst",
        vraag="Wat ontstaat er bij de dehydrogenatie van een secundaire alcohol?",
        antwoord=["een keton", "keton", "ketonen"],
        uitleg="De C=O-groep komt in het midden van de keten te zitten. Daarom is propanon "
        "het product van propaan-2-ol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een tertiaire alcohol geen dehydrogenatie ondergaan?",
        opties=[
            "het koolstofatoom met de OH-groep heeft geen waterstofatoom meer",
            "het koolstofatoom met de OH-groep heeft al een dubbele binding",
            "de OH-groep van een tertiaire alcohol is te sterk gebonden",
            "een tertiaire alcohol heeft te veel koolstofatomen in de keten",
        ],
        antwoord=0,
        uitleg="Voor een C=O-groep moet er op dat koolstofatoom een waterstofatoom "
        "weggaan. Bij een tertiaire alcohol zitten daar drie koolstofketens.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eliminatie maakt een verzadigde keten onverzadigd.",
        antwoord=True,
        uitleg="Er gaan twee groepen weg van twee buuratomen, en daar komt een dubbele "
        "binding. Een additie doet net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de eliminatie van waterstofbromide uit broomethaan?",
        opties=[
            "etheen",
            "ethaan",
            "ethanol",
            "ethyn",
        ],
        antwoord=0,
        uitleg="Het broomatoom en een waterstofatoom van het buuratoom gaan samen weg als "
        "HBr. Dat laat een dubbele binding achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof heb je nodig voor de dehydratatie van ethanol in het labo?",
        opties=[
            "geconcentreerd zwavelzuur en warmte",
            "verdund natriumhydroxide en warmte",
            "broomwater bij kamertemperatuur",
            "een katalysator van nikkel met waterstofgas",
        ],
        antwoord=0,
        uitleg="Het zwavelzuur trekt het water uit de alcohol. Daarom heet die reactie ook "
        "waterafsplitsing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de dehydratatie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is een eliminatiereactie",
            "er ontstaat een alkeen uit een alcohol",
            "het is een additiereactie",
            "er ontstaat een alcohol uit een alkeen",
        ],
        antwoord=[0, 1],
        uitleg="De omgekeerde reactie, water adderen aan een alkeen, geeft weer een "
        "alcohol. De twee zijn dus elkaars tegengestelde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reactie waarbij er water uit een alcohol verdwijnt?",
        antwoord=["dehydratatie", "waterafsplitsing", "dehydratie"],
        uitleg="Het resultaat is een alkeen. Verdwijnt er diwaterstof, dan heet het een "
        "dehydrogenatie en krijg je een aldehyde of een keton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je oxideert propaan-1-ol voorzichtig. Wat ontstaat er eerst?",
        opties=[
            "propanal",
            "propanon",
            "propaanzuur",
            "propeen",
        ],
        antwoord=0,
        uitleg="Een primaire alcohol wordt eerst een aldehyde. Oxideer je verder, dan "
        "krijg je het carbonzuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eliminatie bij een halogeenalkaan verloopt zonder base.",
        antwoord=False,
        uitleg="De base haalt juist het waterstofatoom weg van het buuratoom van het "
        "halogeen. Zonder base verloopt eerder een nucleofiele substitutie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk product krijg je uit butaan-2-ol bij een dehydrogenatie?",
        opties=[
            "butanon",
            "butanal",
            "butaanzuur",
            "but-2-een",
        ],
        antwoord=0,
        uitleg="Butaan-2-ol is een secundaire alcohol, dus komt de C=O-groep in het "
        "midden. Dat geeft een keton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een tertiaire alcohol zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het koolstofatoom met de OH-groep draagt drie koolstofketens",
            "ze kan wel een dehydratatie ondergaan",
            "ze kan een dehydrogenatie ondergaan tot een keton",
            "het koolstofatoom met de OH-groep draagt twee waterstofatomen",
        ],
        antwoord=[0, 1],
        uitleg="Voor een dehydratatie moet er enkel een waterstofatoom op een búuratoom "
        "zitten, en dat is er wel. Voor een dehydrogenatie niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel koolstofketens zitten er aan het koolstofatoom met de OH-groep bij een secundaire alcohol?",
        antwoord=["twee", "2"],
        uitleg="Bij een primaire alcohol is dat één en bij een tertiaire drie. Dat getal "
        "bepaalt wat er bij een oxidatie ontstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom levert de dehydratatie van butaan-2-ol twee verschillende alkenen op?",
        opties=[
            "het water kan aan twee kanten van de OH-groep weggaan",
            "de keten kan tijdens de reactie vertakken",
            "er ontstaat eerst een keton dat daarna splitst",
            "het zwavelzuur voegt zich bij een van de twee producten",
        ],
        antwoord=0,
        uitleg="Er zit aan beide buuratomen een waterstofatoom. Dus krijg je but-1-een en "
        "but-2-een naast elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk reactietype is het omgekeerde van een additie?",
        opties=[
            "een eliminatie",
            "een substitutie",
            "een condensatie",
            "een hydrolyse",
        ],
        antwoord=0,
        uitleg="Bij een additie komt er iets bij over een dubbele binding, bij een "
        "eliminatie gaat er iets weg en ontstaat die binding opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke producten ontstaan er bij een condensatie tussen een carbonzuur en een alcohol? Kruis alles aan wat juist is.",
        opties=[
            "een ester",
            "water",
            "een ether",
            "diwaterstof",
        ],
        antwoord=[0, 1],
        uitleg="De OH van het zuur en de H van de alcohol gaan samen als water weg. Wat "
        "overblijft, koppelt tot de ester.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de oxidatie van een primaire alcohol kan je niet stoppen bij het aldehyde.",
        antwoord=False,
        uitleg="Dat kan wel, met een voorzichtige oxidator en door het aldehyde af te "
        "destilleren. Oxideer je door, dan krijg je het carbonzuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eliminatie bij een alcohol en een eliminatie bij een halogeenalkaan geven beide een alkeen.",
        antwoord=True,
        uitleg="In het ene geval gaat er water weg, in het andere een "
        "waterstofhalogenide. Het resultaat is in beide gevallen een dubbele binding.",
    ),
    dict(
        type="invultekst",
        vraag="Wat ontstaat er als je een primaire alcohol volledig oxideert?",
        antwoord=["een carbonzuur", "carbonzuur", "zuur"],
        uitleg="De weg loopt van alcohol over aldehyde naar carbonzuur. Daarom wordt wijn "
        "die te lang openstaat azijn.",
    ),
]
