# -*- coding: utf-8 -*-
"""Het inkomensevenwicht, de multiplicator en het AV-AA-schema.

Fiche: inkomensevenwicht in het vereenvoudigd model van een gesloten
economie (prijzen, geldhoeveelheid en rentevoet constant), grafisch; effect
van een wijziging van de effectieve vraag; multiplicatoreffect bij
expansief beleid, spaarlek en belastinglek; investeringsmultiplicator
berekenen; macro-economisch evenwicht op korte en lange termijn in het
AV-AA-schema; vraag- en aanbodschokken; budgettair en monetair beleid
(federale en regionale overheden, ECB) en hun effect in het AV-AA-schema.

Vast rekenvoorbeeld: C = 50 + 0,8Y en I = 100.
"""

MODEL = "In een gesloten economie zonder overheid is C = 50 + 0,8Y en I = 100. "

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat blijft constant in het vereenvoudigd economisch model van een gesloten economie?",
        opties=[
            "prijzen, geldhoeveelheid en rente",
            "het inkomen en de consumptie",
            "de investeringen en het sparen",
            "de export en de import",
        ],
        antwoord=0,
        uitleg="Zo kan je het effect van de vraag op het inkomen apart bekijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is er inkomensevenwicht in dat model?",
        opties=[
            "als de effectieve vraag gelijk is aan Y",
            "als de consumptie gelijk is aan de investeringen",
            "als het sparen nul is",
            "als de prijzen stijgen",
        ],
        antwoord=0,
        uitleg="Y = C + I: alles wat geproduceerd wordt, wordt ook gekocht.",
    ),
    dict(
        type="invultekst",
        vraag=MODEL + "Hoeveel is het evenwichtsinkomen Y?",
        antwoord=["750"],
        uitleg="Y = 50 + 0,8Y + 100, dus 0,2Y = 150 en Y = 750.",
    ),
    dict(
        type="meerkeuze",
        vraag=MODEL + "Hoeveel is de marginale consumptiequote?",
        opties=["0,8", "0,2", "50", "100"],
        antwoord=0,
        uitleg="Van elke extra euro inkomen gaat 0,8 naar consumptie.",
    ),
    dict(
        type="invultekst",
        vraag=MODEL + "Hoeveel is de investeringsmultiplicator?",
        antwoord=["5", "vijf"],
        uitleg="k = 1 / (1 − 0,8) = 1 / 0,2 = 5.",
    ),
    dict(
        type="invultekst",
        vraag=MODEL + "De autonome investeringen stijgen met 20. Met hoeveel stijgt het evenwichtsinkomen?",
        antwoord=["100", "honderd"],
        uitleg="ΔY = k · ΔI = 5 · 20 = 100.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt het inkomen meer dan de extra investering?",
        opties=[
            "de uitgave wordt inkomen voor anderen, die verder besteden",
            "de prijzen stijgen mee met de investering en blazen het inkomen op",
            "de overheid verdubbelt elke investering",
            "het sparen stijgt sterker dan het inkomen",
        ],
        antwoord=0,
        uitleg="Zo ontstaat een kettingreactie van bestedingen: het multiplicatoreffect.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe groter de marginale spaarquote, hoe kleiner de multiplicator.",
        antwoord=True,
        uitleg="k = 1 / spaarquote. Wat gespaard wordt, lekt weg uit de bestedingskringloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het spaarlek bij het multiplicatoreffect?",
        opties=[
            "het deel van het extra inkomen dat gespaard wordt",
            "geld dat uit een bankkluis verdwijnt",
            "spaargeld dat naar een bank in het buitenland gaat",
            "de rente die banken niet uitbetalen",
        ],
        antwoord=0,
        uitleg="Dat deel zet de kettingreactie niet verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het belastinglek?",
        opties=[
            "het deel van het extra inkomen voor belastingen",
            "belastingen die niet betaald worden door fraude",
            "een fout in de belastingaangifte",
            "belastingen die het buitenland betaalt",
        ],
        antwoord=0,
        uitleg="Ook dat deel wordt niet meteen besteed, dus de multiplicator wordt kleiner.",
    ),
    dict(
        type="waarofniet",
        vraag="Met belastingen erbij is de multiplicator groter dan zonder.",
        antwoord=False,
        uitleg="Het belastinglek maakt de multiplicator kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de 45°-lijn voor in de grafiek van het inkomensevenwicht?",
        opties=[
            "de punten waar bestedingen gelijk zijn aan Y",
            "de consumptiefunctie van de gezinnen bij elk inkomen",
            "de autonome investeringen van bedrijven",
            "het sparen bij elk inkomen",
        ],
        antwoord=0,
        uitleg="Het snijpunt met de bestedingslijn geeft het evenwichtsinkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De autonome investeringen stijgen. Wat gebeurt er met de bestedingslijn in de grafiek?",
        opties=[
            "ze schuift omhoog en het evenwichtsinkomen stijgt",
            "ze verschuift naar beneden en het evenwichtsinkomen daalt",
            "ze wordt steiler, maar het inkomen blijft gelijk",
            "de 45°-lijn verschuift naar boven en wordt steiler",
        ],
        antwoord=0,
        uitleg="Bij elk inkomen wordt er meer besteed.",
    ),
    dict(
        type="invultekst",
        vraag="De marginale consumptiequote is 0,75. Hoeveel is de multiplicator?",
        antwoord=["4", "vier"],
        uitleg="k = 1 / (1 − 0,75) = 1 / 0,25 = 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid voert een expansief beleid en verhoogt haar uitgaven met 10 miljard. De multiplicator is 2,5. Met hoeveel stijgt het inkomen?",
        opties=["25 miljard", "10 miljard", "12,5 miljard", "4 miljard"],
        antwoord=0,
        uitleg="2,5 · 10 = 25.",
    ),
    dict(
        type="waarofniet",
        vraag="Een daling van de autonome investeringen doet het evenwichtsinkomen met meer dan die daling dalen.",
        antwoord=True,
        uitleg="De multiplicator werkt ook in de andere richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lekken verkleinen het multiplicatoreffect? Duid alle juiste antwoorden aan.",
        opties=["sparen", "belastingen", "consumptie", "investeringen"],
        antwoord=[0, 1],
        uitleg="In een open economie komt ook de import erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de effectieve vraag?",
        opties=[
            "de bestedingen waarvoor ook koopkracht is",
            "alles wat mensen zouden willen hebben, ook zonder geld",
            "de vraag van de overheid alleen",
            "de vraag naar arbeid",
        ],
        antwoord=0,
        uitleg="Het gaat om vraag die met geld gesteund wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="In het vereenvoudigd model wordt het evenwichtsinkomen bepaald door de effectieve vraag.",
        antwoord=True,
        uitleg="Bij constante prijzen past de productie zich aan de vraag aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een marginale consumptiequote van 0,9 is de multiplicator 0,9.",
        antwoord=False,
        uitleg="k = 1 / (1 − 0,9) = 10.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de assen van het AV-AA-schema?",
        opties=[
            "het algemeen prijspeil en het reëel bbp",
            "de prijs en de hoeveelheid van één product",
            "het loon en de werkgelegenheid",
            "de rente en de geldhoeveelheid",
        ],
        antwoord=0,
        uitleg="Verticaal het prijspeil, horizontaal de productie van de hele economie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de AV-curve (aggregatieve vraag)?",
        opties=["dalend", "stijgend", "verticaal", "horizontaal"],
        antwoord=0,
        uitleg="Bij een hoger prijspeil wordt er in totaal minder gekocht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de AA-curve op lange termijn eruit?",
        opties=[
            "verticaal bij het potentieel bbp",
            "dalend",
            "horizontaal bij het huidige prijspeil",
            "stijgend door de oorsprong",
        ],
        antwoord=0,
        uitleg="Op lange termijn bepaalt de productiecapaciteit hoeveel er gemaakt wordt, niet het prijspeil.",
    ),
    dict(
        type="waarofniet",
        vraag="Op korte termijn stijgt de AA-curve: bij een hoger prijspeil wordt er meer geproduceerd.",
        antwoord=True,
        uitleg="Op korte termijn passen lonen en andere kosten zich nog niet aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een positieve vraagschok verschuift de AV-curve naar rechts. Wat gebeurt er op korte termijn?",
        opties=[
            "het prijspeil en het reëel bbp stijgen",
            "het prijspeil stijgt en het reëel bbp daalt",
            "het prijspeil daalt en het reëel bbp stijgt",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Langs de stijgende AA-curve op korte termijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="De olieprijs stijgt fors. Welke schok is dat?",
        opties=[
            "een negatieve aanbodschok: de AA-curve schuift naar links",
            "een positieve vraagschok: de AV-curve schuift naar rechts",
            "een positieve aanbodschok",
            "een negatieve vraagschok",
        ],
        antwoord=0,
        uitleg="De productiekosten stijgen voor heel de economie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve aanbodschok kan leiden tot stagflatie: hogere prijzen en minder productie.",
        antwoord=True,
        uitleg="De AA-curve schuift naar links: prijspeil omhoog, reëel bbp omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is budgettair beleid?",
        opties=[
            "bijsturen met uitgaven en belastingen",
            "de centrale bank stuurt de economie bij met de rente",
            "bedrijven sturen hun begroting bij",
            "gezinnen stellen een budget op",
        ],
        antwoord=0,
        uitleg="In België voeren de federale en de regionale overheden budgettair beleid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie voert het monetair beleid voor België?",
        opties=["de Europese Centrale Bank", "de federale regering", "de Vlaamse regering", "het IMF"],
        antwoord=0,
        uitleg="België hoort bij de eurozone.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid verlaagt de belastingen tijdens een recessie. Wat is het effect in het AV-AA-schema?",
        opties=[
            "de AV-curve schuift naar rechts",
            "de AV-curve schuift naar links",
            "de AA-curve op lange termijn schuift naar links",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Gezinnen houden meer over om te besteden.",
    ),
    dict(
        type="meerkeuze",
        vraag="De ECB verlaagt de rente. Wat is het verwachte effect?",
        opties=[
            "de AV-curve schuift naar rechts",
            "minder bestedingen: de AV-curve schuift naar links",
            "de AA-curve wordt horizontaal",
            "het prijspeil daalt zeker",
        ],
        antwoord=0,
        uitleg="Lenen wordt goedkoper voor gezinnen en bedrijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een renteverhoging door de ECB is een expansief monetair beleid.",
        antwoord=False,
        uitleg="Een hogere rente remt de bestedingen af: dat is restrictief beleid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen zijn expansief budgettair beleid? Duid alle juiste antwoorden aan.",
        opties=[
            "de overheid investeert meer in wegen en scholen",
            "de overheid verlaagt de personenbelasting",
            "de ECB verlaagt de rente",
            "de overheid verhoogt de btw",
        ],
        antwoord=[0, 1],
        uitleg="De ECB voert monetair beleid. Een hogere btw remt de vraag af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op lange termijn na een positieve vraagschok, als de AA-curve op lange termijn verticaal is?",
        opties=[
            "het bbp keert terug naar het potentieel, het prijspeil blijft hoger",
            "het reëel bbp blijft voorgoed hoger, want de vraag blijft blijvend groot",
            "het prijspeil keert terug en het bbp blijft hoger",
            "beide dalen onder het oude niveau",
        ],
        antwoord=0,
        uitleg="Op lange termijn bepaalt de capaciteit de productie. Wat overblijft, is een hoger prijspeil.",
    ),
    dict(
        type="waarofniet",
        vraag="Een technologische doorbraak die de productiviteit verhoogt, verschuift de AA-curve naar rechts.",
        antwoord=True,
        uitleg="Dat is een positieve aanbodschok: meer productie bij een lager prijspeil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het consumentenvertrouwen stort in en gezinnen geven minder uit. Welke schok is dat?",
        opties=[
            "een negatieve vraagschok",
            "een positieve aanbodschok",
            "een negatieve aanbodschok",
            "een positieve vraagschok",
        ],
        antwoord=0,
        uitleg="De AV-curve schuift naar links: lager prijspeil en minder productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen budgettair en monetair beleid?",
        opties=[
            "budgettair: uitgaven en belastingen; monetair: de rente",
            "budgettair gebruikt de rente, monetair de belastingen",
            "budgettair is enkel voor gemeenten, monetair enkel voor gewesten",
            "er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Het eerste ligt bij de regeringen, het tweede bij de centrale bank.",
    ),
    dict(
        type="waarofniet",
        vraag="De Vlaamse regering kan de rente in de eurozone verlagen om de Vlaamse economie te steunen.",
        antwoord=False,
        uitleg="De rente is een bevoegdheid van de ECB. Vlaanderen kan wel budgettair beleid voeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt het macro-economisch evenwicht op korte termijn?",
        opties=[
            "op het snijpunt van AV en AA op korte termijn",
            "op het snijpunt van de AV-curve en de horizontale as",
            "op het hoogste punt van de AA-curve",
            "waar de AV-curve verticaal wordt",
        ],
        antwoord=0,
        uitleg="Daar lees je het prijspeil en het reëel bbp af.",
    ),
    dict(
        type="waarofniet",
        vraag="Een restrictief beleid doet de AV-curve naar rechts schuiven.",
        antwoord=False,
        uitleg="Ze schuift naar links. Zo daalt de druk op de prijzen, wat helpt tegen een hoge inflatie.",
    ),
]
