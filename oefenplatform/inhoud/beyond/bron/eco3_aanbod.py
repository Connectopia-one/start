# -*- coding: utf-8 -*-
"""Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod.

Fiche: inkomenselasticiteit van de vraag berekenen en interpreteren;
inferieure, indifferente en normale goederen (noodzakelijke en luxe
goederen); individuele aanbodcurve afleiden uit de optimale
productiegrootte; verloop; collectieve aanbodcurve; beweging op en
verschuiving van de aanbodcurve; prijselasticiteit van het aanbod berekenen
en interpreteren; verband met de helling; elastisch, inelastisch, unitair,
perfect elastisch en perfect inelastisch aanbod.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de inkomenselasticiteit van de vraag?",
        opties=[
            "procentuele verandering van de gevraagde hoeveelheid gedeeld door de procentuele verandering van het inkomen",
            "procentuele verandering van het inkomen gedeeld door de procentuele verandering van de gevraagde hoeveelheid",
            "procentuele verandering van de gevraagde hoeveelheid gedeeld door de procentuele verandering van de prijs",
            "verandering van het inkomen gedeeld door de verandering van de prijs van het goed",
        ],
        antwoord=0,
        uitleg="Ze meet hoe sterk de vraag reageert op een inkomensverandering.",
    ),
    dict(
        type="invultekst",
        vraag="Het inkomen stijgt met 5 % en de vraag naar restaurantbezoeken stijgt met 10 %. Hoeveel is de inkomenselasticiteit?",
        antwoord=["2", "twee", "+2"],
        uitleg="10 % / 5 % = 2. Groter dan 1: een luxegoed.",
    ),
    dict(
        type="meerkeuze",
        vraag="De inkomenselasticiteit van een goed is negatief. Hoe noem je dat goed?",
        opties=["een inferieur goed", "een luxegoed", "een noodzakelijk goed", "een indifferent goed"],
        antwoord=0,
        uitleg="Als het inkomen stijgt, koopt men er minder van, zoals goedkope huismerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="De inkomenselasticiteit ligt tussen 0 en 1. Wat voor goed is het?",
        opties=["een noodzakelijk goed", "een luxegoed", "een inferieur goed", "een indifferent goed"],
        antwoord=0,
        uitleg="De vraag stijgt, maar minder sterk dan het inkomen. Het is een normaal goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een indifferent goed?",
        opties=[
            "een goed waarvan de vraag niet verandert als het inkomen verandert",
            "een goed waarvan de vraag sterker stijgt dan het inkomen",
            "een goed waarvan de vraag daalt als het inkomen stijgt",
            "een goed waarvan de vraag niet afhangt van de prijs",
        ],
        antwoord=0,
        uitleg="De inkomenselasticiteit is 0, zoals bij zout.",
    ),
    dict(
        type="waarofniet",
        vraag="Luxegoederen hebben een inkomenselasticiteit groter dan 1.",
        antwoord=True,
        uitleg="De vraag stijgt procentueel sterker dan het inkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een inferieur goed is een goed van slechte kwaliteit dat niemand wil kopen.",
        antwoord=False,
        uitleg="Inferieur slaat op de reactie op het inkomen: bij een hoger inkomen koopt men er minder van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het inkomen stijgt met 10 % en de vraag naar busritten daalt met 3 %. Wat besluit je?",
        opties=[
            "busritten zijn een inferieur goed",
            "busritten zijn een luxegoed",
            "busritten zijn een noodzakelijk goed",
            "busritten zijn een indifferent goed",
        ],
        antwoord=0,
        uitleg="Inkomenselasticiteit −0,3: negatief, dus inferieur. Wie meer verdient, neemt vaker de auto.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke goederen zijn normale goederen? Duid alle juiste antwoorden aan.",
        opties=["noodzakelijke goederen", "luxegoederen", "inferieure goederen", "indifferente goederen"],
        antwoord=[0, 1],
        uitleg="Normale goederen hebben een positieve inkomenselasticiteit.",
    ),
    dict(
        type="invultekst",
        vraag="De inkomenselasticiteit van brood is 0,2. Het inkomen stijgt met 10 %. Met hoeveel procent stijgt de vraag naar brood?",
        antwoord=["2", "2 %", "2%"],
        uitleg="0,2 · 10 % = 2 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt een gewone aanbodcurve?",
        opties=[
            "stijgend: bij een hogere prijs wil men meer aanbieden",
            "dalend: bij een hogere prijs wil men minder aanbieden",
            "horizontaal: de aangeboden hoeveelheid is onbeperkt",
            "verticaal: de prijs bepaalt niets",
        ],
        antwoord=0,
        uitleg="Een hogere prijs maakt extra productie winstgevend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke curve leid je de individuele aanbodcurve van een producent bij volkomen concurrentie af?",
        opties=[
            "het stijgende deel van de marginale kostencurve",
            "de gemiddelde opbrengstencurve",
            "de totale constante kostencurve",
            "de vraagcurve van de consument",
        ],
        antwoord=0,
        uitleg="De optimale productie ligt waar prijs = marginale kosten, boven het minimum van de gemiddelde variabele kosten.",
    ),
    dict(
        type="waarofniet",
        vraag="De collectieve aanbodcurve vind je door bij elke prijs de aangeboden hoeveelheden van alle producenten op te tellen.",
        antwoord=True,
        uitleg="Net als bij de vraag tel je horizontaal op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen doen de aanbodcurve naar rechts verschuiven? Duid alle juiste antwoorden aan.",
        opties=[
            "een nieuwe, goedkopere productietechniek",
            "er komen meer producenten bij",
            "de lonen in de sector stijgen sterk",
            "de prijs van het product zelf stijgt",
        ],
        antwoord=[0, 1],
        uitleg="Hogere lonen doen het aanbod dalen. De eigen prijs geeft een beweging op de curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="De prijs van grondstoffen stijgt sterk. Wat gebeurt er met de aanbodcurve?",
        opties=[
            "ze verschuift naar links",
            "ze verschuift naar rechts",
            "er is een beweging op de curve",
            "ze wordt horizontaal",
        ],
        antwoord=0,
        uitleg="Hogere kosten: bij elke prijs wil men minder aanbieden.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de marktprijs van tomaten stijgt, verschuift de aanbodcurve van tomaten naar rechts.",
        antwoord=False,
        uitleg="Een verandering van de eigen prijs geeft een beweging op de aanbodcurve.",
    ),
    dict(
        type="invultekst",
        vraag="Bij 3 euro bieden drie bakkers 40, 50 en 30 broden aan. Hoeveel is het collectieve aanbod bij 3 euro?",
        antwoord=["120"],
        uitleg="40 + 50 + 30 = 120.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk goed is waarschijnlijk een luxegoed?",
        opties=["een verre vakantie", "melk", "goedkope pasta", "zout"],
        antwoord=0,
        uitleg="Wie meer verdient, geeft daar procentueel veel meer aan uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goed kan voor de ene consument normaal zijn en voor een andere inferieur.",
        antwoord=True,
        uitleg="Het hangt af van het inkomensniveau en de voorkeuren. Voor een student is een huismerk misschien normaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goed met een inkomenselasticiteit van 0,8 is een luxegoed.",
        antwoord=False,
        uitleg="Tussen 0 en 1 is het een noodzakelijk goed.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de prijselasticiteit van het aanbod?",
        opties=[
            "procentuele verandering van de aangeboden hoeveelheid gedeeld door de procentuele verandering van de prijs",
            "procentuele verandering van de prijs gedeeld door de procentuele verandering van de aangeboden hoeveelheid",
            "procentuele verandering van de aangeboden hoeveelheid gedeeld door de procentuele verandering van het inkomen",
            "verandering van de winst gedeeld door de verandering van de aangeboden hoeveelheid",
        ],
        antwoord=0,
        uitleg="Ze is meestal positief, want het aanbod stijgt met de prijs.",
    ),
    dict(
        type="invultekst",
        vraag="De prijs stijgt met 8 % en de aangeboden hoeveelheid met 4 %. Hoeveel is de prijselasticiteit van het aanbod?",
        antwoord=["0,5", "0.5", "1/2"],
        uitleg="4 % / 8 % = 0,5: inelastisch aanbod.",
    ),
    dict(
        type="meerkeuze",
        vraag="De prijselasticiteit van het aanbod is 2. Hoe noem je dat aanbod?",
        opties=["elastisch", "inelastisch", "unitair elastisch", "perfect inelastisch"],
        antwoord=0,
        uitleg="Groter dan 1: de hoeveelheid reageert sterker dan de prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet een perfect inelastisch aanbod eruit?",
        opties=["een verticale aanbodcurve", "een horizontale aanbodcurve", "een dalende aanbodcurve", "een curve door de oorsprong"],
        antwoord=0,
        uitleg="De aangeboden hoeveelheid ligt vast, wat de prijs ook is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld heeft een perfect inelastisch aanbod?",
        opties=[
            "de zitplaatsen in een uitverkocht stadion op de dag van de match",
            "brood in een stad met veel bakkers",
            "T-shirts uit een grote fabriek",
            "downloads van een app",
        ],
        antwoord=0,
        uitleg="Op korte termijn kan men geen extra plaatsen bijbouwen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een horizontale aanbodcurve stelt een perfect elastisch aanbod voor.",
        antwoord=True,
        uitleg="Bij die prijs wil men elke hoeveelheid aanbieden, bij een iets lagere prijs niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Op korte termijn is het aanbod meestal elastischer dan op lange termijn.",
        antwoord=False,
        uitleg="Op lange termijn kunnen producenten machines bijkopen en nieuwe bedrijven toetreden: dan is het aanbod elastischer.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag naar een product stijgt. Bij welk aanbod stijgt de prijs het sterkst?",
        opties=["bij een inelastisch aanbod", "bij een elastisch aanbod", "bij een perfect elastisch aanbod", "bij een unitair elastisch aanbod"],
        antwoord=0,
        uitleg="De producenten kunnen weinig extra aanbieden, dus de prijs moet de vraag afremmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag stijgt en het aanbod is perfect elastisch. Wat gebeurt er?",
        opties=[
            "de hoeveelheid stijgt, de prijs blijft gelijk",
            "de prijs stijgt, de hoeveelheid blijft gelijk",
            "prijs en hoeveelheid dalen",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Bij een horizontale aanbodcurve schuift het evenwicht enkel naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag stijgt en het aanbod is perfect inelastisch. Wat gebeurt er?",
        opties=[
            "de prijs stijgt, de hoeveelheid blijft gelijk",
            "de hoeveelheid stijgt, de prijs blijft gelijk",
            "beide dalen",
            "het evenwicht verdwijnt",
        ],
        antwoord=0,
        uitleg="Bij een verticale aanbodcurve kan enkel de prijs veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt het aanbod van een product elastischer? Duid alle juiste antwoorden aan.",
        opties=[
            "de producent heeft voorraad",
            "er is vrije productiecapaciteit",
            "het product rijpt jaren, zoals wijn",
            "alle machines draaien al op volle kracht",
        ],
        antwoord=[0, 1],
        uitleg="Met voorraad of vrije capaciteit kan men snel meer leveren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dezelfde schaal wijst een vlakkere aanbodcurve op een elastischer aanbod.",
        antwoord=True,
        uitleg="Een kleine prijsverandering geeft een grote verandering van de hoeveelheid.",
    ),
    dict(
        type="invultekst",
        vraag="De prijselasticiteit van het aanbod is 1,5. De prijs stijgt met 6 %. Met hoeveel procent stijgt de aangeboden hoeveelheid?",
        antwoord=["9", "9 %", "9%"],
        uitleg="1,5 · 6 % = 9 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een prijsstijging van 10 % geeft een stijging van het aanbod met 10 %. Hoe noem je dat aanbod?",
        opties=["unitair elastisch", "elastisch", "inelastisch", "perfect elastisch"],
        antwoord=0,
        uitleg="De elasticiteit is precies 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechte aanbodcurve door de oorsprong heeft een prijselasticiteit van ...",
        opties=["1", "0", "oneindig", "−1"],
        antwoord=0,
        uitleg="Prijs en hoeveelheid zijn recht evenredig: ze veranderen procentueel even sterk.",
    ),
    dict(
        type="waarofniet",
        vraag="Waar de prijs onder het minimum van de gemiddelde variabele kosten ligt, biedt de producent op korte termijn niets aan.",
        antwoord=True,
        uitleg="Dan dekt de prijs zelfs de variabele kosten niet: stoppen kost minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een strenge vorst vernielt een groot deel van de appeloogst. Wat gebeurt er met de aanbodcurve van appelen?",
        opties=[
            "ze verschuift naar links",
            "ze verschuift naar rechts",
            "er is een beweging naar boven op de curve",
            "ze wordt horizontaal",
        ],
        antwoord=0,
        uitleg="Bij elke prijs zijn er minder appelen te koop.",
    ),
    dict(
        type="waarofniet",
        vraag="Een subsidie per geproduceerd stuk doet de aanbodcurve naar links verschuiven.",
        antwoord=False,
        uitleg="Een subsidie verlaagt de kosten: de aanbodcurve schuift naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt elk punt op de individuele aanbodcurve voor?",
        opties=[
            "de optimale productiegrootte bij die prijs",
            "de maximale prijs die een koper wil betalen",
            "de totale kosten van de producent",
            "de hoeveelheid die alle producenten samen maken",
        ],
        antwoord=0,
        uitleg="Bij die prijs maakt de producent de meeste winst met die hoeveelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De prijselasticiteit van het aanbod is meestal negatief.",
        antwoord=False,
        uitleg="Prijs en aangeboden hoeveelheid bewegen in dezelfde richting: de elasticiteit is positief.",
    ),
]
