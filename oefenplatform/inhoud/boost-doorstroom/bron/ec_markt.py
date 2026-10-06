# -*- coding: utf-8 -*-
"""De vragen voor "De markt met volkomen concurrentie en de overheid"
(🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"marktwerking", eerste stuk: de product- en dienstenmarkt. De kenmerken van
volkomen concurrentie, het grafisch en rekenkundig bepalen van het
marktevenwicht, en de invloed van een maximum- of minimumprijs van de overheid.
De arbeidsmarkt staat in [[ec_arbeid]].

Deel 1 gaat over vraag, aanbod en evenwicht: waarom de vraagcurve daalt en de
aanbodcurve stijgt, hoe je het evenwicht berekent, en wat er gebeurt bij een
overschot of een tekort.
Deel 2 gaat over de kenmerken van volkomen concurrentie en over het ingrijpen
van de overheid met een maximum- of een minimumprijs.

Afspraak in dit thema: elke rekenopgave geeft de vraag- en aanbodfunctie
voluit in de vraag, met Qv voor de gevraagde en Qa voor de aangeboden
hoeveelheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom daalt de vraagcurve?",
        opties=[
            "Bij een lagere prijs kopen mensen meer",
            "Bij een lagere prijs bieden bedrijven meer aan",
            "Bij een hogere prijs stijgt het inkomen",
            "Bij een hogere prijs daalt de kostprijs",
        ],
        antwoord=0,
        uitleg="Wordt iets goedkoper, dan kopen bestaande klanten er meer van en komen er nieuwe klanten bij. Daarom loopt de vraagcurve van linksboven naar rechtsonder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt de aanbodcurve?",
        opties=[
            "Bij een hogere prijs loont het om meer te produceren",
            "Bij een hogere prijs kopen mensen meer",
            "Bij een lagere prijs stijgen de kosten",
            "Bij een lagere prijs komen er meer bedrijven bij",
        ],
        antwoord=0,
        uitleg="Een bedrijf produceert tot MK gelijk is aan de prijs. Stijgt de prijs, dan schuift dat punt naar rechts en biedt het meer aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het marktevenwicht?",
        opties=[
            "De prijs waarbij de gevraagde hoeveelheid gelijk is aan de aangeboden",
            "De prijs waarbij de producenten de hoogste winst maken",
            "De prijs waarbij de consumenten het meest kopen",
            "De prijs die de overheid als redelijk beschouwt",
        ],
        antwoord=0,
        uitleg="Bij de evenwichtsprijs raakt alles verkocht en blijft niemand met een tekort zitten. Vraag en aanbod vallen precies samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag is Qv = 200 − 4P en het aanbod Qa = 20 + 2P. Wat is de evenwichtsprijs?",
        opties=[
            "30",
            "20",
            "36",
            "60",
        ],
        antwoord=0,
        uitleg="200 min 4P is gelijk aan 20 plus 2P geeft 180 is 6P, dus P is 30.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zelfde functies: Qv = 200 − 4P en Qa = 20 + 2P. Wat is de evenwichtshoeveelheid?",
        opties=[
            "80",
            "60",
            "100",
            "30",
        ],
        antwoord=0,
        uitleg="Vul P is 30 in: 200 min 120 is 80, en 20 plus 60 is ook 80. Beide kanten geven hetzelfde, dus de berekening klopt.",
    ),
    dict(
        type="waarofniet",
        vraag="Boven de evenwichtsprijs ontstaat er een overschot.",
        antwoord=True,
        uitleg="Bij een te hoge prijs willen de bedrijven veel aanbieden en de klanten weinig kopen. Wat overblijft, is een overschot, en dat duwt de prijs weer omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een prijs onder het evenwicht? Duid alles aan wat juist is.",
        opties=[
            "Er ontstaat een tekort",
            "De gevraagde hoeveelheid is groter dan de aangeboden",
            "De prijs komt onder opwaartse druk",
            "De bedrijven bieden meer aan dan daarvoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="Goedkoop lokt kopers en ontmoedigt aanbieders. Het tekort dat zo ontstaat, duwt de prijs weer omhoog naar het evenwicht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de prijs waarbij vraag en aanbod gelijk zijn? Schrijf één woord.",
        antwoord=["evenwichtsprijs", "marktprijs"],
        uitleg="De evenwichtsprijs is de prijs waarbij de markt geruimd is: alles wat aangeboden wordt, raakt verkocht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het inkomen van de gezinnen stijgt. Wat gebeurt er op de markt van een gewoon goed?",
        opties=[
            "De vraagcurve schuift naar rechts en de prijs stijgt",
            "De vraagcurve schuift naar links en de prijs daalt",
            "De aanbodcurve schuift naar rechts",
            "Er verandert niets aan de curven",
        ],
        antwoord=0,
        uitleg="Bij elke prijs wil men nu meer kopen, dus de hele curve verschuift. Het nieuwe snijpunt ligt hoger en verder naar rechts.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prijsverandering verschuift de vraagcurve.",
        antwoord=False,
        uitleg="Bij een andere prijs schuif je over dezelfde curve. De curve zelf verschuift alleen door iets anders: inkomen, smaak, de prijs van een ander goed of het aantal kopers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan de vraagcurve doen verschuiven? Duid alles aan wat juist is.",
        opties=[
            "Een verandering van het inkomen",
            "Een verandering van de smaak of de mode",
            "Een verandering van de prijs van een vervangend product",
            "Een verandering van de prijs van het product zelf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles behalve de eigen prijs verschuift de curve. De eigen prijs laat je net over de curve bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De grondstoffen worden duurder. Wat gebeurt er met de markt?",
        opties=[
            "De aanbodcurve schuift naar links en de prijs stijgt",
            "De aanbodcurve schuift naar rechts en de prijs daalt",
            "De vraagcurve schuift naar links",
            "Alleen de hoeveelheid verandert, niet de prijs",
        ],
        antwoord=0,
        uitleg="Bij elke prijs kunnen bedrijven nu minder winstgevend aanbieden. Het snijpunt schuift omhoog en naar links: duurder, en minder stuks.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen aanbod en vraag bij een te hoge prijs? Schrijf één woord.",
        antwoord=["overschot", "aanbodoverschot"],
        uitleg="Een overschot is wat er bij die prijs niet verkocht raakt. Het drukt de prijs naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag is Qv = 120 − 2P. Hoeveel wordt er gevraagd bij een prijs van 25?",
        opties=[
            "70",
            "95",
            "170",
            "60",
        ],
        antwoord=0,
        uitleg="120 min 2 maal 25 is 120 min 50 is 70 stuks.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekort duwt de prijs omlaag.",
        antwoord=False,
        uitleg="Bij een tekort willen meer mensen kopen dan er is. Dan zijn er klanten bereid meer te betalen, en stijgt de prijs tot het evenwicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Het marktevenwicht vind je in de grafiek in het snijpunt van de vraag- en de aanbodcurve.",
        antwoord=True,
        uitleg="In het snijpunt is de gevraagde hoeveelheid precies gelijk aan de aangeboden. Eronder lees je de hoeveelheid af, ernaast de prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hittegolf doet de vraag naar ijs stijgen. Wat gebeurt er? Duid alles aan wat juist is.",
        opties=[
            "De vraagcurve schuift naar rechts",
            "De evenwichtsprijs stijgt",
            "De verkochte hoeveelheid stijgt",
            "De aanbodcurve schuift naar links",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alleen de vraag verandert; het aanbod blijft waar het was. Het snijpunt schuift dus langs de aanbodcurve naar boven: duurder én meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men het marktmechanisme zelfregulerend?",
        opties=[
            "Omdat een tekort of een overschot de prijs vanzelf bijstuurt",
            "Omdat de overheid de prijzen jaarlijks aanpast",
            "Omdat bedrijven onderling de prijs afspreken",
            "Omdat de consumenten altijd dezelfde prijs betalen",
        ],
        antwoord=0,
        uitleg="Niemand regelt het van bovenaf. Een overschot drukt de prijs, een tekort duwt ze omhoog, en zo komt de markt weer in evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het aanbod is Qa = 10 + 5P. Hoeveel wordt er aangeboden bij een prijs van 8?",
        opties=[
            "50",
            "40",
            "23",
            "18",
        ],
        antwoord=0,
        uitleg="10 plus 5 maal 8 is 10 plus 40 is 50 stuks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het evenwicht geen vast punt voor altijd?",
        opties=[
            "Omdat vraag en aanbod voortdurend verschuiven",
            "Omdat de overheid de prijs elk jaar verandert",
            "Omdat bedrijven hun prijzen willekeurig kiezen",
            "Omdat consumenten nooit tevreden zijn",
        ],
        antwoord=0,
        uitleg="Inkomen, smaak, kosten en het aantal aanbieders veranderen voortdurend. Elke verschuiving geeft een nieuw snijpunt en dus een nieuw evenwicht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft een markt met volkomen concurrentie? Duid alles aan wat juist is.",
        opties=[
            "Heel veel kopers en verkopers",
            "Een homogeen product",
            "Vrije toe- en uittreding",
            "Eén aanbieder met een beschermde positie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Veel aanbieders, een product dat overal hetzelfde is, vrije toetreding en volledige informatie. Eén beschermde aanbieder is net het tegenovergestelde: een monopolie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een homogeen product?",
        opties=[
            "Het product is bij elke aanbieder hetzelfde",
            "Het product is overal even duur",
            "Het product wordt in één fabriek gemaakt",
            "Het product is voor iedereen nuttig",
        ],
        antwoord=0,
        uitleg="Als tarwe van de ene boer niet van die van de andere te onderscheiden is, kiest de koper gewoon de goedkoopste. Daarom kan niemand een hogere prijs vragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prijsnemer mag zijn eigen prijs kiezen.",
        antwoord=False,
        uitleg="Hij moet de marktprijs aanvaarden: zijn aandeel is te klein om ze te beïnvloeden. Vraagt hij meer, dan koopt niemand; minder vragen hoeft niet, want alles raakt toch verkocht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een bedrijf dat de marktprijs moet aanvaarden? Schrijf één woord.",
        antwoord=["prijsnemer", "prijsvolger"],
        uitleg="Bij volkomen concurrentie is elk bedrijf prijsnemer: het kiest alleen zijn hoeveelheid, niet zijn prijs.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij volkomen concurrentie heeft elke aanbieder volledige informatie over prijs en kwaliteit.",
        antwoord=True,
        uitleg="Dat hoort bij de voorwaarden. Daardoor kan niemand van onwetendheid profiteren met een hogere prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke markt benadert volkomen concurrentie het best?",
        opties=[
            "De wereldmarkt voor tarwe",
            "De markt voor smartphones",
            "De markt voor spoorvervoer in België",
            "De markt voor frisdrank",
        ],
        antwoord=0,
        uitleg="Tarwe is bij iedereen hetzelfde, er zijn heel veel boeren en kopers, en niemand bepaalt de prijs. Bij merkproducten is dat net niet zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een maximumprijs?",
        opties=[
            "Een door de overheid opgelegde bovengrens",
            "Een door de overheid opgelegde ondergrens",
            "De hoogste prijs die ooit gevraagd werd",
            "De prijs waarbij de winst het grootst is",
        ],
        antwoord=0,
        uitleg="Een maximumprijs is een plafond: hoger mag niet. De overheid gebruikt het om een goed betaalbaar te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een maximumprijs ligt onder de evenwichtsprijs. Wat gebeurt er? Duid alles aan wat juist is.",
        opties=[
            "Er ontstaat een tekort",
            "De gevraagde hoeveelheid stijgt",
            "De aangeboden hoeveelheid daalt",
            "Er ontstaat een overschot",
        ],
        antwoord=[0, 1, 2],
        uitleg="Goedkoper lokt kopers en ontmoedigt aanbieders. Er wordt meer gevraagd dan aangeboden, en dat verschil is een blijvend tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een maximumprijs boven de evenwichtsprijs niet?",
        opties=[
            "Omdat de markt die prijs toch niet vraagt",
            "Omdat de overheid dan niets mag doen",
            "Omdat er dan een tekort ontstaat",
            "Omdat de bedrijven dan stoppen",
        ],
        antwoord=0,
        uitleg="Een plafond boven de marktprijs is niet bindend: de prijs komt er toch niet aan. Alleen onder het evenwicht heeft een maximumprijs gevolgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een minimumprijs?",
        opties=[
            "Een door de overheid opgelegde ondergrens",
            "Een door de overheid opgelegde bovengrens",
            "De laagste prijs die een bedrijf kan dragen",
            "De prijs waarbij de vraag nul wordt",
        ],
        antwoord=0,
        uitleg="Een minimumprijs is een bodem: lager mag niet. Ze beschermt de aanbieders, bijvoorbeeld landbouwers.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumprijs boven het evenwicht leidt tot een tekort.",
        antwoord=False,
        uitleg="Ze leidt tot een overschot. Bij die hogere prijs wordt er meer aangeboden en minder gevraagd, en wat overblijft raakt niet verkocht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een opgelegde bovengrens voor de prijs? Schrijf één woord.",
        antwoord=["maximumprijs", "prijsplafond"],
        uitleg="Een maximumprijs is een plafond. Ligt ze onder het evenwicht, dan ontstaat er een tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het evenwicht ligt bij 10 euro. De overheid legt een maximumprijs van 7 euro op. Wat gebeurt er?",
        opties=[
            "Er ontstaat een tekort bij 7 euro",
            "Er ontstaat een overschot bij 7 euro",
            "De prijs blijft 10 euro",
            "De vraag daalt tot nul",
        ],
        antwoord=0,
        uitleg="Bij 7 euro willen meer mensen kopen en minder bedrijven aanbieden dan bij 10 euro. Dat verschil is een tekort dat niet vanzelf verdwijnt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen kan een tekort door een maximumprijs hebben? Duid alles aan wat juist is.",
        opties=[
            "Wachtlijsten of rantsoenering",
            "Een zwarte markt met hogere prijzen",
            "Minder nieuw aanbod op langere termijn",
            "Een stijging van de officiële prijs",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wat op prijs niet verdeeld raakt, wordt op een andere manier verdeeld: door te wachten, door een bon of buiten de wet om. De officiële prijs blijft net vastgepind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legt een overheid soms toch een maximumprijs op?",
        opties=[
            "Om een basisgoed betaalbaar te houden",
            "Om de winst van de bedrijven te verhogen",
            "Om de productie te doen stijgen",
            "Om het aanbod te vergroten",
        ],
        antwoord=0,
        uitleg="Bij huur of energie weegt de betaalbaarheid zwaar. Het nadeel is dat het aanbod krimpt en er een tekort ontstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumprijs onder de evenwichtsprijs verandert niets aan de markt.",
        antwoord=True,
        uitleg="Zo'n bodem is niet bindend: de marktprijs ligt er toch al boven. Pas boven het evenwicht heeft ze gevolgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een overheid soms met het overschot door een minimumprijs?",
        opties=[
            "Ze koopt het op of beperkt de productie",
            "Ze verhoogt de minimumprijs nog meer",
            "Ze verbiedt de verkoop van dat goed",
            "Ze laat de prijs vrij dalen",
        ],
        antwoord=0,
        uitleg="Anders blijft de voorraad liggen. Opkopen of productiequota zijn de twee gebruikelijke manieren, bijvoorbeeld in de landbouw.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een opgelegde ondergrens voor de prijs? Schrijf één woord.",
        antwoord=["minimumprijs", "prijsbodem"],
        uitleg="Een minimumprijs beschermt de aanbieder. Ligt ze boven het evenwicht, dan ontstaat er een overschot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een prijsdaling langs de curve en een verschuiving van de curve?",
        opties=[
            "De eerste komt van de prijs zelf, de tweede van iets anders",
            "De eerste geldt voor de vraag, de tweede voor het aanbod",
            "De eerste geldt op korte termijn, de tweede op lange termijn",
            "Er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Verandert de prijs, dan beweeg je over dezelfde curve. Verandert het inkomen, de smaak of de kostprijs, dan verschuift de hele curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is volkomen concurrentie vooral een model?",
        opties=[
            "Omdat bijna geen enkele echte markt aan alle voorwaarden voldoet",
            "Omdat de overheid het verboden heeft",
            "Omdat het rekenwerk anders te moeilijk wordt",
            "Omdat bedrijven het niet willen",
        ],
        antwoord=0,
        uitleg="Merken, reclame en patenten zorgen ervoor dat producten juist niet identiek zijn. Toch is het model nuttig: het geeft een ijkpunt om echte markten mee te vergelijken.",
    ),
]
