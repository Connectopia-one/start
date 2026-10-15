# -*- coding: utf-8 -*-
"""Pittige vragen bij "Energie in een technisch systeem" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en 2, maar met ketens van omzettingen, nuttige
energie die afhangt van wat je met het toestel wil, en redeneringen over
fossiel en hernieuwbaar waarin een fout verstopt zit.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Je trapt op je fiets en een klein generatortje tegen het wiel laat je fietslamp branden. Welke reeks omzettingen klopt van begin tot einde?",
        opties=[
            "Chemische energie uit je voedsel, dan beweging, dan elektrische energie, dan licht en warmte",
            "Elektrische energie uit je voedsel, dan beweging, dan chemische energie, dan licht",
            "Stralingsenergie uit de lamp, dan beweging van het wiel, dan chemische energie",
            "Chemische energie uit je voedsel, dan elektrische energie, dan beweging, dan licht",
        ],
        antwoord=0,
        uitleg="In voedsel zit chemische energie, en daarmee beweeg je de trappers. Het generatortje zet die beweging om in elektrische energie, en de lamp maakt daar licht en warmte van. Een reeks waarin de elektrische energie vóór de beweging komt, klopt niet: dan zou er een motor in je fiets zitten in plaats van een generator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het water achter een stuwdam staat nog helemaal stil. Toch zit er al energie in die later stroom wordt. Welke energievorm is dat?",
        opties=[
            "Potentiële energie",
            "Bewegingsenergie",
            "Chemische energie",
            "Elektrische energie",
        ],
        antwoord=0,
        uitleg="Het water staat hoog, en de energie van de plaats waar iets zich bevindt, is potentiële energie. Pas als het water naar beneden stroomt, wordt dat bewegingsenergie, en de centrale maakt daar elektrische energie van.",
    ),
    dict(
        type="waarofniet",
        vraag="In een speelgoedauto op batterijen zet de batterij elektrische energie om in chemische energie, en de motor maakt daar beweging van.",
        antwoord=False,
        uitleg="Het is net omgekeerd bij de batterij: daarin zit chemische energie, en die wordt bij gebruik elektrische energie. De motor zet die elektrische energie dan om in beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een broodrooster gloeien de draadjes rood, net zoals de draad in een gloeilamp. Wat is bij de broodrooster de nuttige energie?",
        opties=[
            "De warmte",
            "Het rode licht van de draadjes",
            "De beweging van de hendel",
            "Het geluid als het brood omhoogspringt",
        ],
        antwoord=0,
        uitleg="Welke energie nuttig is, hangt af van wat je met het toestel wil. Een broodrooster koop je om te roosteren, dus de warmte is nuttig en het licht is verlies. Bij een gloeilamp is dat net andersom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke toestellen is de warmte die vrijkomt niet-nuttige energie? (meerdere antwoorden mogelijk)",
        opties=[
            "Een gloeilamp boven de tafel",
            "Een elektrische boormachine",
            "De motor van een speelgoedauto",
            "Een waterkoker",
            "Een elektrische verwarming",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij een lamp wil je licht, bij een boormachine en een motor wil je beweging, dus daar is de warmte verlies. Bij een waterkoker en een verwarming is warmte net wat je wilt, en dan is ze de nuttige energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een uitvinder beweert: \"Mijn toestel geeft meer energie af dan er elektrische energie in gaat.\" Wat is er mis met die bewering?",
        opties=[
            "Een toestel kan geen energie uit het niets maken",
            "Niets: dat kan, als het toestel genoeg warmte verliest",
            "Niets: dat kan, als het toestel een generator is",
            "Niets: er komt altijd niet-nuttige energie bij",
        ],
        antwoord=0,
        uitleg="Een technisch systeem zet energie om, het maakt er geen bij. Wat eruit komt, moest er eerst in. De niet-nuttige energie komt niet extra bij: ze is een deel van wat erin ging en dat je niet kan gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben een windmolen en een waterkrachtcentrale met elkaar gemeen?",
        opties=[
            "Beide zetten beweging om in elektrische energie zonder iets te verbranden",
            "Beide werken op een fossiele brandstof die na een tijd opraakt",
            "Beide zetten elektrische energie om in de beweging van wind of water",
            "Beide leveren altijd precies evenveel stroom, dag en nacht",
        ],
        antwoord=0,
        uitleg="De wind of het stromende water laat iets draaien, en een generator maakt daar stroom van. Er wordt niets verbrand, dus er komt geen CO₂ vrij. Ze leveren niet altijd evenveel: zonder wind staat een molen stil.",
    ),
    dict(
        type="invultekst",
        vraag="In een windmolen zit achter de wieken een toestel dat de draaiende beweging omzet in elektrische energie. Het werkt net omgekeerd als een elektrische motor. Hoe heet dat toestel? Antwoord met één woord.",
        antwoord="generator",
        uitleg="Een elektrische motor maakt van elektrische energie beweging. Een generator doet het omgekeerde: van beweging maakt hij elektrische energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een windmolen levert op een windstille avond geen stroom, maar dat betekent niet dat wind een bron is die opraakt.",
        antwoord=True,
        uitleg="Dat wind niet altijd evenveel levert, is een nadeel van wind. Maar de bron raakt niet op: morgen waait het weer. Niet altijd evenveel leveren en opraken zijn twee verschillende dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stoot een auto met een verbrandingsmotor CO₂ uit en een windmolen niet?",
        opties=[
            "In de motor wordt brandstof verbrand, in de windmolen niets",
            "De windmolen zet zijn CO₂ meteen om in elektrische energie",
            "Bij elke beweging komt CO₂ vrij, en de molen beweegt trager",
            "Wind is zelf een broeikasgas dat alle CO₂ opslorpt",
        ],
        antwoord=0,
        uitleg="CO₂ komt vrij bij het verbranden van fossiele brandstoffen. De motor verbrandt brandstof, de windmolen verbrandt niets. Bewegen op zich geeft geen CO₂: de molen draait ook, maar stoot niets uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze bronnen leveren niet altijd evenveel energie, ook al raken ze niet op? (meerdere antwoorden mogelijk)",
        opties=["De zon", "De wind", "Steenkool", "Aardgas"],
        antwoord=[0, 1],
        uitleg="Zon en wind raken niet op, maar 's nachts schijnt er geen zon en op een windstille dag draait geen molen. Steenkool en aardgas kan je opstoken wanneer je wil, maar die raken wel op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over het broeikaseffect klopt?",
        opties=[
            "Het is natuurlijk, maar wij versterken het met extra CO₂",
            "De mens heeft het veroorzaakt door steenkool te stoken",
            "Het zou het best zijn als het er helemaal niet was",
            "Het ontstaat doordat windmolens de lucht opwarmen",
        ],
        antwoord=0,
        uitleg="Het broeikaseffect bestond al lang voor de mens fossiele brandstoffen gebruikte, en zonder dat effect zou het op aarde veel te koud zijn. Het probleem is dat wij er met het verbranden van fossiele brandstoffen CO₂ bij doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Aardgas wordt een hernieuwbare bron als je er maar spaarzaam genoeg mee omgaat.",
        antwoord=False,
        uitleg="Hernieuwbaar betekent dat de bron niet opraakt. Aardgas is miljoenen jaren geleden ontstaan en groeit niet aan. Spaarzaam zijn helpt om er langer mee te doen, maar het blijft een fossiele brandstof die opraakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een huis wordt verwarmd met warmte die uit de diepe ondergrond naar boven gehaald wordt. Welke uitspraak klopt?",
        opties=[
            "Dat is aardwarmte, een hernieuwbare bron",
            "Dat is aardgas, een fossiele brandstof uit de grond",
            "Dat is aardwarmte, maar die raakt op zoals steenkool",
            "Dat is stralingsenergie die van de zon komt",
        ],
        antwoord=0,
        uitleg="Warmte uit de diepe ondergrond is aardwarmte, en de fiche noemt die hernieuwbaar. Aardgas komt ook uit de grond, maar dat is een brandstof die je verbrandt, en die raakt op. Dat iets uit de grond komt, maakt het dus nog niet fossiel.",
    ),
    dict(
        type="invultekst",
        vraag="Zonnepanelen laden overdag een batterij op, en 's avonds laat die batterij een lamp branden. In welke energievorm zit de energie terwijl ze in de batterij wacht? Antwoord met één woord.",
        antwoord="chemische",
        uitleg="Een batterij bewaart chemische energie. Overdag gaat er elektrische energie in en wordt ze opgeslagen, 's avonds wordt ze weer elektrische energie voor de lamp.",
    ),
    dict(
        type="invultekst",
        vraag="Een zonnepaneel zet stralingsenergie om. De energievorm die er bij een zonnepaneel uitkomt, gaat er bij een gloeilamp net in. Welke energievorm is dat? Antwoord met één woord.",
        antwoord="elektrische",
        uitleg="Een zonnepaneel zet stralingsenergie om in elektrische energie. Een gloeilamp krijgt elektrische energie binnen en maakt er licht en warmte van. Wie licht antwoordt, haalt in en uit door elkaar: licht komt bij de gloeilamp eruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze toestellen zetten elektrische energie om in een andere energievorm? (meerdere antwoorden mogelijk)",
        opties=[
            "Een gloeilamp",
            "Een waterkoker",
            "Een elektrische motor",
            "Een broodrooster",
            "Een windmolen",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Een gloeilamp, een waterkoker, een elektrische motor en een broodrooster krijgen allemaal elektrische energie binnen. Een windmolen werkt omgekeerd: daar gaat beweging in en komt elektrische energie uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt: \"Een zonnepaneel werkt op een hernieuwbare bron, dus het levert ook 's nachts stroom.\" Wat is er mis met die redenering?",
        opties=[
            "Hernieuwbaar zegt dat de bron niet opraakt, niet dat ze altijd evenveel levert",
            "Een zonnepaneel werkt niet op een hernieuwbare bron, maar op fossiele brandstof",
            "Niets: een zonnepaneel levert 's nachts net zo veel, maar dan met het licht van de maan",
            "Een zonnepaneel zet warmte om, en 's nachts is het daarvoor gewoon te koud",
        ],
        antwoord=0,
        uitleg="Een zonnepaneel zet het licht van de zon om in elektrische energie. 's Nachts is er geen zonlicht, dus levert het niets. De zon raakt daarom nog niet op: het is wel een hernieuwbare bron die niet altijd evenveel levert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad vervangt een centrale die steenkool verbrandt door een groot windmolenpark. Welk gevolg mag de stad verwachten?",
        opties=[
            "Er komt minder CO₂ vrij, maar hoeveel stroom er is, hangt af van het weer",
            "Er komt meer CO₂ vrij, want windmolens draaien dag en nacht zonder pauze",
            "De wind raakt na een paar jaar op, en dan valt het hele park stil",
            "Het broeikaseffect verdwijnt dan helemaal uit de dampkring van de aarde",
        ],
        antwoord=0,
        uitleg="Windmolens verbranden niets, dus er komt minder CO₂ vrij dan bij steenkool. Hun nadeel is dat ze niet altijd evenveel leveren. Het broeikaseffect verdwijnt niet: het is natuurlijk, alleen wordt het minder versterkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een waterkoker en een gloeilamp maken allebei warmte, maar alleen bij de waterkoker is die warmte de nuttige energie.",
        antwoord=True,
        uitleg="Bij een waterkoker wil je warm water, dus de warmte is nuttig. Bij een gloeilamp wil je licht, en dan is de warmte niet-nuttige energie. Dezelfde energievorm kan dus nuttig of niet-nuttig zijn, afhankelijk van het toestel.",
    ),
]
