# -*- coding: utf-8 -*-
"""Prijsregulering, quota, belastingen en subsidies.

Fiche: noodzaak tot overheidsingrijpen op de vrije markt; interventies op een
competitieve markt: minimum- en maximumprijs, productiequota, indirecte
belastingen en subsidies; effecten op het marktevenwicht grafisch;
welvaartsverlies analyseren, berekenen en grafisch voorstellen.

Vaste rekenmarkt in de vragen: Qv = 100 − P en Qa = P − 20, evenwicht
P = 60 en Q = 40.
"""

MARKT = "Op een markt is de vraag Qv = 100 − P en het aanbod Qa = P − 20. Het evenwicht is P = 60 en Q = 40. "

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom grijpt de overheid soms in op een competitieve markt?",
        opties=[
            "omdat ze de marktprijs of hoeveelheid niet wenselijk vindt",
            "omdat markten zonder overheid nooit een evenwicht vinden",
            "omdat bedrijven verplicht zijn de overheid te laten beslissen",
            "omdat de overheid zelf alle winst van de markt wil",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld om consumenten te beschermen tegen hoge prijzen of boeren tegen lage prijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heeft een maximumprijs effect?",
        opties=[
            "als ze onder de evenwichtsprijs ligt",
            "als ze boven de evenwichtsprijs ligt",
            "als ze gelijk is aan de evenwichtsprijs",
            "altijd, waar ze ook ligt",
        ],
        antwoord=0,
        uitleg="Ligt de maximumprijs hoger, dan blijft de markt gewoon in haar evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij een maximumprijs onder de evenwichtsprijs?",
        opties=["een tekort", "een overschot", "een nieuw evenwicht zonder problemen", "een hogere verhandelde hoeveelheid"],
        antwoord=0,
        uitleg="De gevraagde hoeveelheid is groter dan de aangeboden hoeveelheid.",
    ),
    dict(
        type="invultekst",
        vraag=MARKT + "De overheid legt een maximumprijs van 50 op. Hoe groot is het tekort?",
        antwoord=["20", "twintig"],
        uitleg="Qv = 50 en Qa = 30: 50 − 30 = 20.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een mogelijk gevolg van een maximumprijs onder het evenwicht?",
        opties=["een zwarte markt", "een overschot in de winkels", "een hogere aangeboden hoeveelheid", "lagere wachtrijen"],
        antwoord=0,
        uitleg="Wie wil betalen, zoekt het product buiten de wet aan een hogere prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heeft een minimumprijs effect?",
        opties=[
            "als ze boven de evenwichtsprijs ligt",
            "als ze onder de evenwichtsprijs ligt",
            "als ze gelijk is aan de evenwichtsprijs",
            "enkel als er geen aanbieders zijn",
        ],
        antwoord=0,
        uitleg="Een minimumprijs onder het evenwicht verandert niets.",
    ),
    dict(
        type="invultekst",
        vraag=MARKT + "De overheid legt een minimumprijs van 70 op. Hoe groot is het overschot?",
        antwoord=["20", "twintig"],
        uitleg="Qa = 50 en Qv = 30: 50 − 30 = 20.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumprijs wordt vaak gebruikt om producenten, zoals landbouwers, te beschermen.",
        antwoord=True,
        uitleg="Ze krijgen een hogere prijs. Het overschot moet dan iemand opkopen of vernietigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een maximumprijs onder het evenwicht doet de verhandelde hoeveelheid stijgen.",
        antwoord=False,
        uitleg="De aanbieders bieden minder aan, dus er wordt minder verhandeld.",
    ),
    dict(
        type="meerkeuze",
        vraag=MARKT + "Met een maximumprijs van 50 wordt er 30 verhandeld. Bij Q = 30 willen kopers 70 betalen. Hoe groot is het welvaartsverlies?",
        opties=["100", "200", "50", "400"],
        antwoord=0,
        uitleg="Driehoek: ½ · (40 − 30) · (70 − 50) = 100.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een productiequotum?",
        opties=[
            "een maximale hoeveelheid die mag worden geproduceerd",
            "een minimale prijs voor een product",
            "een belasting per geproduceerd stuk, te betalen aan de overheid",
            "een subsidie voor nieuwe machines",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld melkquota in de landbouw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het effect van een quotum onder de evenwichtshoeveelheid?",
        opties=[
            "de prijs stijgt en er wordt minder verhandeld",
            "de prijs daalt en er wordt meer verhandeld",
            "de prijs daalt en er wordt minder verhandeld dan voordien",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Het aanbod wordt verticaal bij het quotum: de kopers bieden de prijs op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een productiequotum onder het evenwicht veroorzaakt een welvaartsverlies.",
        antwoord=True,
        uitleg="Ruilen die beide partijen voordeel zouden geven, vinden niet plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn voorbeelden van indirecte belastingen? Duid alle juiste antwoorden aan.",
        opties=["btw", "accijnzen op tabak", "personenbelasting", "vennootschapsbelasting"],
        antwoord=[0, 1],
        uitleg="Personen- en vennootschapsbelasting zijn directe belastingen op inkomen of winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de aanbodcurve als de overheid een belasting per stuk heft bij de producent?",
        opties=[
            "ze verschuift naar boven (naar links), met het bedrag van de belasting",
            "ze verschuift naar beneden (naar rechts), met het bedrag van de belasting",
            "ze wordt verticaal",
            "ze verandert niet",
        ],
        antwoord=0,
        uitleg="Voor elke hoeveelheid wil de producent nu de belasting erbij krijgen.",
    ),
    dict(
        type="invultekst",
        vraag=MARKT + "De overheid heft 10 euro belasting per stuk bij de producent. Het nieuwe aanbod is Qa = P − 30. Wat is de nieuwe prijs die de koper betaalt?",
        antwoord=["65", "vijfenzestig"],
        uitleg="100 − P = P − 30, dus P = 65 en Q = 35.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij die belasting van 10 euro betaalt de koper 65 in plaats van 60. Hoeveel houdt de producent per stuk over?",
        opties=["55", "65", "60", "50"],
        antwoord=0,
        uitleg="65 − 10 = 55. Koper en producent dragen elk 5 euro van de belasting.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een belasting per stuk draagt de consument altijd de volledige belasting.",
        antwoord=False,
        uitleg="Hoe de last verdeeld wordt, hangt af van de elasticiteit van vraag en aanbod.",
    ),
    dict(
        type="invultekst",
        vraag="Bij die belasting van 10 euro worden 35 stuks verhandeld. Hoeveel belasting ontvangt de overheid?",
        antwoord=["350"],
        uitleg="10 · 35 = 350.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij die belasting daalt de hoeveelheid van 40 naar 35. Hoe groot is het welvaartsverlies?",
        opties=["25", "50", "350", "100"],
        antwoord=0,
        uitleg="Driehoek: ½ · (40 − 35) · 10 = 25.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het effect van een subsidie per stuk aan de producent?",
        opties=[
            "de aanbodcurve schuift naar rechts: lagere prijs, grotere hoeveelheid",
            "de aanbodcurve schuift naar links: hogere prijs, kleinere hoeveelheid",
            "de vraagcurve schuift naar links",
            "er verandert niets aan het evenwicht",
        ],
        antwoord=0,
        uitleg="De subsidie verlaagt de kosten per stuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een subsidie op een competitieve markt zonder externe effecten veroorzaakt een welvaartsverlies.",
        antwoord=True,
        uitleg="Er wordt meer gemaakt dan het evenwicht; de subsidie kost de overheid meer dan wat kopers en verkopers erbij winnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie draagt het grootste deel van een belasting als de vraag heel inelastisch is?",
        opties=["de consumenten", "de producenten", "de overheid", "niemand"],
        antwoord=0,
        uitleg="Ze blijven kopen, dus de prijs stijgt bijna met de hele belasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie draagt het grootste deel van een belasting als de vraag heel elastisch is?",
        opties=["de producenten", "de consumenten", "de overheid", "de werknemers van de overheid"],
        antwoord=0,
        uitleg="Kopers haken af bij een hogere prijs, dus de producent moet de belasting grotendeels zelf slikken.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe elastischer vraag en aanbod, hoe groter het welvaartsverlies van een belasting.",
        antwoord=True,
        uitleg="De hoeveelheid daalt dan sterker, dus de driehoek wordt groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een minimumprijs boven het evenwicht. Welke uitspraken kloppen? Duid alle juiste antwoorden aan.",
        opties=[
            "er wordt minder verhandeld dan in het evenwicht",
            "er ontstaat een overschot",
            "de consumenten betalen minder dan in het evenwicht",
            "er ontstaat een tekort",
        ],
        antwoord=[0, 1],
        uitleg="Consumenten betalen meer en kopen minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt het welvaartsverlies bij een belasting in de grafiek?",
        opties=[
            "in de driehoek tussen vraag en aanbod, van de nieuwe tot de oude hoeveelheid",
            "in de rechthoek van de belastingontvangsten",
            "onder de aanbodcurve, van nul tot de nieuwe hoeveelheid",
            "boven de vraagcurve",
        ],
        antwoord=0,
        uitleg="De rechthoek gaat naar de overheid en is dus geen verlies voor de samenleving.",
    ),
    dict(
        type="waarofniet",
        vraag="De belastingontvangsten van de overheid tellen mee als welvaartsverlies.",
        antwoord=False,
        uitleg="Die opbrengst is een overdracht naar de overheid. Enkel de driehoek gaat echt verloren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad legt een maximumhuurprijs op die ver onder de marktprijs ligt. Wat verwacht je op lange termijn?",
        opties=[
            "minder huurwoningen en lange wachtlijsten",
            "meer huurwoningen en kortere wachtlijsten",
            "geen enkele verandering op de huurmarkt",
            "dat alle huurders verhuizen naar een andere stad",
        ],
        antwoord=0,
        uitleg="Verhuren wordt minder aantrekkelijk, terwijl meer mensen willen huren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de overheid vaak met het overschot bij een minimumprijs voor landbouwproducten?",
        opties=[
            "ze koopt het op en slaat het op of verwerkt het",
            "ze verbiedt de boeren om nog langer te produceren",
            "ze verlaagt de minimumprijs elke dag",
            "ze verplicht consumenten om alles te kopen",
        ],
        antwoord=0,
        uitleg="Zo bleven in het verleden de beruchte boterbergen en melkplassen over.",
    ),
    dict(
        type="invultekst",
        vraag=MARKT + "De overheid legt een quotum van 30 stuks op. Welke prijs betalen de kopers?",
        antwoord=["70", "zeventig"],
        uitleg="Bij Q = 30 willen de kopers 100 − 30 = 70 betalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij dat quotum van 30 vragen de producenten 70, terwijl hun aanbodcurve bij 30 maar 50 vraagt. Wie wint daarbij ten opzichte van de kopers?",
        opties=[
            "de producenten met een quotum: ze krijgen een hogere prijs",
            "de consumenten: ze betalen minder per stuk dan in het evenwicht",
            "de overheid: ze ontvangt belastingen",
            "niemand: alles blijft zoals het evenwicht",
        ],
        antwoord=0,
        uitleg="Een deel van het consumentensurplus gaat naar de producenten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een maximumprijs boven de evenwichtsprijs heeft geen effect op de markt.",
        antwoord=True,
        uitleg="De markt komt toch uit op de lagere evenwichtsprijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid geeft een subsidie van 10 per stuk. Het nieuwe aanbod is Qa = P − 10, de vraag Qv = 100 − P. Wat is de nieuwe hoeveelheid?",
        opties=["45", "40", "35", "50"],
        antwoord=0,
        uitleg="100 − P = P − 10, dus P = 55 en Q = 45.",
    ),
    dict(
        type="invultekst",
        vraag="Bij die subsidie van 10 per stuk worden 45 stuks verhandeld. Hoeveel kost de subsidie de overheid?",
        antwoord=["450"],
        uitleg="10 · 45 = 450.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een subsidie betalen de consumenten een lagere prijs dan in het oorspronkelijke evenwicht.",
        antwoord=True,
        uitleg="In het voorbeeld zakt de prijs van 60 naar 55.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen doen de verhandelde hoeveelheid dalen? Duid alle juiste antwoorden aan.",
        opties=["een indirecte belasting", "een quotum onder het evenwicht", "een subsidie per stuk", "een maximumprijs boven het evenwicht"],
        antwoord=[0, 1],
        uitleg="Een subsidie doet de hoeveelheid stijgen, een maximumprijs boven het evenwicht verandert niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een indirecte belasting doet de aanbodcurve naar rechts verschuiven.",
        antwoord=False,
        uitleg="Ze verschuift naar links, of naar boven met het bedrag van de belasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstaat er bij een maximumprijs onder het evenwicht vaak een wachtrij?",
        opties=[
            "er zijn meer kopers dan er goederen zijn aan die prijs",
            "de winkels openen later dan anders",
            "de producenten maken te veel",
            "de overheid verbiedt snel te verkopen",
        ],
        antwoord=0,
        uitleg="Het tekort wordt dan verdeeld volgens wie het eerst komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumprijs boven het evenwicht verhoogt altijd de totale welvaart op de markt.",
        antwoord=False,
        uitleg="Er wordt minder verhandeld, dus er ontstaat een welvaartsverlies.",
    ),
]
