# -*- coding: utf-8 -*-
"""De vragen voor "Internationale handel en handelsbelemmeringen" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"internationale handel en economische relaties": invoer, uitvoer,
intracommunautaire verwerving en levering, de motieven voor internationale
handel, statistieken over de Belgische handel, de vier soorten
handelsbelemmeringen en het handelsakkoord.

Deel 1 gaat over de begrippen, de motieven en het lezen van cijfers over de
Belgische handel.
Deel 2 gaat over de belemmeringen (invoerquotum, importheffing, uitvoersubsidie
en niet-tarifaire belemmeringen), hun gevolgen op het marktmechanisme, en over
het handelsakkoord.

In de cijfervragen staan de getallen altijd in de vraag zelf, zodat een kind
rekent en niets uit het hoofd moet weten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt een econoom met invoer?",
        opties=[
            "Aankopen in het buitenland",
            "Verkopen aan klanten in het buitenland",
            "De productie van de bedrijven in eigen land",
            "De voorraad van de groothandel in ons land",
        ],
        antwoord=0,
        uitleg="Invoer of import zijn de goederen en diensten die een land in het buitenland aankoopt. Het geld gaat dan naar het buitenland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt een econoom met uitvoer?",
        opties=[
            "Verkopen aan het buitenland",
            "Aankopen bij leveranciers in het buitenland",
            "De goederen die in het land zelf blijven liggen",
            "Het verschil tussen de productie en het verbruik",
        ],
        antwoord=0,
        uitleg="Uitvoer of export zijn de goederen en diensten die een land aan het buitenland verkoopt. Daar komt geld voor binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgische winkel koopt kaas bij een leverancier in Nederland. Hoe heet die aankoop?",
        opties=[
            "Intracommunautaire verwerving",
            "Intracommunautaire levering",
            "Invoer uit een land buiten Europa",
            "Uitvoer naar een derde land",
        ],
        antwoord=0,
        uitleg="Binnen de Europese Unie spreekt men niet van invoer en uitvoer. Een aankoop bij een leverancier in een ander EU-land is een intracommunautaire verwerving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgisch bedrijf verkoopt machines aan een klant in Duitsland. Hoe heet die verkoop?",
        opties=[
            "Intracommunautaire levering",
            "Intracommunautaire verwerving",
            "Uitvoer naar een derde land",
            "Invoer uit de eurozone",
        ],
        antwoord=0,
        uitleg="Een verkoop aan een klant in een ander EU-land is een intracommunautaire levering. Het woord uitvoer houdt men voor verkopen buiten de Unie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aankoop bij een leverancier in Spanje heet in de boekhouding gewoon invoer.",
        antwoord=False,
        uitleg="Spanje hoort bij de Europese Unie, dus is het een intracommunautaire verwerving. Het woord invoer gebruikt men voor aankopen buiten de Unie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verkoop aan een klant in de Verenigde Staten is uitvoer.",
        antwoord=True,
        uitleg="De Verenigde Staten liggen buiten de Europese Unie, dus heet die verkoop uitvoer of export.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen de uitvoer en de invoer van een land?",
        antwoord=["handelsbalans", "de handelsbalans"],
        uitleg="De handelsbalans is de uitvoer min de invoer. Is de uitkomst positief, dan spreekt men van een overschot, is ze negatief, van een tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn motieven voor internationale handel? Duid alles aan wat juist is.",
        opties=[
            "Grondstoffen die hier niet voorkomen",
            "Een groter afzetgebied",
            "Verschillen in loonkosten",
            "Elk land maakt alles liefst zelf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Landen handelen omdat ze niet alles zelf hebben of kunnen, omdat een groter afzetgebied meer verkoop betekent, en omdat produceren elders soms goedkoper is. Alles zelf willen maken is juist het omgekeerde van handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voert België cacaobonen in?",
        opties=[
            "Cacao groeit hier niet",
            "Omdat Belgische bedrijven geen chocolade willen maken",
            "Omdat de Belgische overheid de invoer verplicht maakt",
            "Omdat chocolade in het buitenland veel goedkoper is",
        ],
        antwoord=0,
        uitleg="De cacaoboom heeft een tropisch klimaat nodig. We voeren de bonen in en verwerken ze hier tot chocolade, die dan weer uitgevoerd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voordelen kan uitvoer een bedrijf opleveren? Duid alles aan wat juist is.",
        opties=[
            "Meer klanten",
            "Schaalvoordelen",
            "Minder afhankelijk van één markt",
            "Nooit meer concurrentie van anderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wie uitvoert bereikt meer klanten, kan daardoor grotere reeksen maken tegen een lagere kost per stuk, en staat minder zwak als het in het eigen land slecht gaat. Concurrentie verdwijnt er juist niet door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met specialisatie tussen landen?",
        opties=[
            "Elk land doet waar het best in is",
            "Elk land probeert alles zelf te maken",
            "Elk land verbiedt de invoer van goederen",
            "Elk land legt dezelfde belasting op",
        ],
        antwoord=0,
        uitleg="Als elk land zich toelegt op wat het relatief het goedkoopst kan maken, en de rest aankoopt, is er in totaal meer te verdelen. Dat is het idee achter internationale handel.",
    ),
    dict(
        type="invultekst",
        vraag="Een land voert meer uit dan het invoert. Zijn handelsbalans heeft dan een ...",
        antwoord=["overschot", "een overschot"],
        uitleg="Uitvoer groter dan invoer geeft een overschot op de handelsbalans. Omgekeerd spreekt men van een tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land voerde voor 320 miljard euro uit en voor 290 miljard euro in. Wat is de handelsbalans?",
        opties=[
            "Een overschot van 30 miljard",
            "Een tekort van 30 miljard euro",
            "Een overschot van 610 miljard euro",
            "Een tekort van 610 miljard euro",
        ],
        antwoord=0,
        uitleg="De handelsbalans is de uitvoer min de invoer: 320 − 290 = 30 miljard euro. De uitvoer is groter, dus is het een overschot.",
    ),
    dict(
        type="waarofniet",
        vraag="België is een kleine open economie: de uitvoer is groot in verhouding tot het bbp.",
        antwoord=True,
        uitleg="België heeft een kleine binnenlandse markt en een grote buitenlandse handel. Daardoor voelt onze economie het snel als het in de buurlanden minder goed gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Het grootste deel van de Belgische uitvoer gaat naar landen buiten Europa.",
        antwoord=False,
        uitleg="Het grootste deel gaat naar de Europese Unie, en vooral naar de buurlanden Duitsland, Nederland en Frankrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke landen zijn de belangrijkste handelspartners van België? Duid alles aan wat juist is.",
        opties=[
            "Duitsland",
            "Nederland",
            "Frankrijk",
            "Nieuw-Zeeland",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onze drie buurlanden Duitsland, Nederland en Frankrijk nemen samen een groot deel van de Belgische in- en uitvoer op. Afstand speelt dus een grote rol in handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke sector staat voor het grootste deel van de Belgische uitvoer?",
        opties=[
            "De chemie en de farmacie",
            "De landbouw en de visserij",
            "De bouw van woningen en kantoren",
            "Het toerisme en de horeca",
        ],
        antwoord=0,
        uitleg="Chemische en farmaceutische producten vormen de grootste uitvoergroep, daarna komen onder meer voertuigen en machines. Bouw en horeca verkopen vooral in het land zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je afleiden uit een tabel met de invoer en de uitvoer per jaar? Duid alles aan wat juist is.",
        opties=[
            "De handelsbalans per jaar",
            "De groei van de uitvoer",
            "Of de invoer sneller stijgt",
            "De winst van elk bedrijf apart",
        ],
        antwoord=[0, 1, 2],
        uitleg="Met de invoer en de uitvoer van elk jaar bereken je de balans, de groei en de vergelijking tussen beide. Over de winst van een afzonderlijk bedrijf zegt zo'n tabel niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een tekort op de handelsbalans?",
        opties=[
            "Meer invoer dan uitvoer",
            "Meer uitvoer dan invoer in dat jaar",
            "Dat de productie van het land gedaald is",
            "Dat de overheid te weinig belasting heeft",
        ],
        antwoord=0,
        uitleg="Bij een tekort koopt een land meer in het buitenland dan het eraan verkoopt. Er gaat dan meer geld naar buiten dan er binnenkomt via de handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="De invoer van een land stijgt van 200 naar 210 miljard euro. Hoeveel procent is dat?",
        opties=[
            "5 procent",
            "10 procent, want 10 miljard erbij",
            "2 procent van het oorspronkelijke bedrag",
            "21 procent van het oorspronkelijke bedrag",
        ],
        antwoord=0,
        uitleg="De stijging is 10 miljard op 200 miljard. 10 gedeeld door 200 is 0,05, dus 5 procent. Een groeivoet reken je altijd op het oude cijfer.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een invoerquotum?",
        opties=[
            "Een maximum op de invoer",
            "Een belasting op elk ingevoerd goed",
            "Een steun voor wie naar het buitenland verkoopt",
            "Een verbod op alle handel met een land",
        ],
        antwoord=0,
        uitleg="Een invoerquotum legt een bovengrens op de hoeveelheid die een land van een goed mag invoeren. Het werkt dus op de hoeveelheid, niet op de prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een importheffing?",
        opties=[
            "Een belasting op invoer",
            "Een bovengrens op de ingevoerde hoeveelheid",
            "Een steun van de overheid aan de uitvoerders",
            "Een technische norm voor ingevoerde goederen",
        ],
        antwoord=0,
        uitleg="Een importheffing of invoerrecht is een belasting die een land heft op goederen die binnenkomen. Daardoor wordt het ingevoerde goed duurder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een uitvoersubsidie?",
        opties=[
            "Steun bij uitvoer",
            "Een belasting op uitgevoerde goederen",
            "Een maximum op de uitgevoerde hoeveelheid",
            "Een verbod om in het buitenland te verkopen",
        ],
        antwoord=0,
        uitleg="Bij een uitvoersubsidie legt de overheid geld bij als een bedrijf aan het buitenland verkoopt. Dat bedrijf kan daardoor goedkoper aanbieden dan de buitenlandse concurrent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een niet-tarifaire belemmering?",
        opties=[
            "Strenge technische normen",
            "Een heffing van tien procent bij de grens",
            "Een maximum van duizend ton per jaar",
            "Een subsidie voor wie uitvoert naar Azië",
        ],
        antwoord=0,
        uitleg="Een niet-tarifaire belemmering werkt niet met geld of met een hoeveelheid, maar met regels: normen, keuringen, labels of papierwerk die invoer moeilijk maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een importheffing maakt het ingevoerde goed duurder op de binnenlandse markt.",
        antwoord=True,
        uitleg="De verkoper rekent de heffing door, dus het aanbod schuift naar boven en de prijs stijgt. De ingevoerde hoeveelheid daalt daardoor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een invoerquotum werkt via de prijs en niet via de hoeveelheid.",
        antwoord=False,
        uitleg="Het is net omgekeerd. Een quotum legt de hoeveelheid vast; de prijs stijgt daarna omdat het aanbod beperkt is.",
    ),
    dict(
        type="invultekst",
        vraag="Welk woord gebruikt men voor een belasting op ingevoerde goederen?",
        antwoord=["importheffing", "invoerheffing", "invoerrecht"],
        uitleg="Een importheffing, ook invoerheffing of invoerrecht genoemd, is een belasting bij de grens. Ze verhoogt de prijs van het ingevoerde goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn handelsbelemmeringen? Duid alles aan wat juist is.",
        opties=[
            "Een invoerquotum",
            "Een importheffing",
            "Een uitvoersubsidie",
            "Een akkoord dat heffingen afschaft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Quota, heffingen, subsidies en niet-tarifaire regels storen alle vier de vrije handel. Een akkoord dat heffingen afschaft doet juist het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op de binnenlandse markt na een importheffing?",
        opties=[
            "De prijs stijgt",
            "De prijs blijft precies gelijk aan daarvoor",
            "De ingevoerde hoeveelheid stijgt sterk",
            "De binnenlandse productie valt helemaal stil",
        ],
        antwoord=0,
        uitleg="De heffing schuift het aanbod naar boven. Daardoor stijgt de evenwichtsprijs en daalt de hoeveelheid die uit het buitenland komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ingevoerd toestel kost 100 euro. De overheid legt een importheffing van 15 procent op. Wat betaalt de koper?",
        opties=[
            "115 euro",
            "85 euro, want de heffing gaat eraf",
            "100 euro, want de verkoper betaalt alles",
            "150 euro, want 15 procent is anderhalf keer",
        ],
        antwoord=0,
        uitleg="15 procent van 100 euro is 15 euro. De heffing komt bovenop de prijs, dus de koper betaalt 115 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de gevolgen van een invoerquotum? Duid alles aan wat juist is.",
        opties=[
            "Minder aanbod",
            "Een hogere prijs",
            "Binnenlandse producenten verkopen meer",
            "De invoer stijgt boven het quotum uit",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het quotum snijdt een stuk van het aanbod weg, dus de prijs stijgt en de binnenlandse producenten nemen een groter deel van de markt. Boven het quotum uit mag er net niets meer binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een uitvoersubsidie helpt een binnenlands bedrijf om in het buitenland te verkopen.",
        antwoord=True,
        uitleg="De overheid legt geld bij, dus het bedrijf kan een lagere prijs vragen dan de buitenlandse concurrent zonder zelf verlies te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Handelsbelemmeringen zijn altijd goed voor de consument in het eigen land.",
        antwoord=False,
        uitleg="De consument betaalt juist meer en heeft minder keuze. Wie er wel bij wint, zijn de binnenlandse producenten en, bij een heffing, de overheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een handelsakkoord?",
        opties=[
            "Een afspraak tussen landen",
            "Een belasting op alle ingevoerde goederen",
            "Een maximum op de hoeveelheid die binnen mag",
            "Een keuring van elk goed aan de landsgrens",
        ],
        antwoord=0,
        uitleg="In een handelsakkoord spreken landen af om belemmeringen te verlagen of weg te nemen, bijvoorbeeld door heffingen af te schaffen of normen op elkaar af te stemmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de markt na een handelsakkoord dat de heffingen afschaft?",
        opties=[
            "De invoer wordt goedkoper",
            "De prijs van het ingevoerde goed stijgt verder",
            "De invoer valt volledig stil in beide landen",
            "De binnenlandse producenten krijgen meer steun",
        ],
        antwoord=0,
        uitleg="Zonder heffing schuift het aanbod naar beneden: de prijs daalt en de ingevoerde hoeveelheid stijgt. De consument wint, de binnenlandse producent krijgt meer concurrentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan er in een handelsakkoord staan? Duid alles aan wat juist is.",
        opties=[
            "Lagere invoerheffingen",
            "Dezelfde normen",
            "Ruimere quota",
            "Een verbod op alle onderlinge handel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Landen maken afspraken die handel makkelijker maken: minder heffingen, dezelfde technische normen zodat een keuring volstaat, en ruimere of afgeschafte quota.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de maximale hoeveelheid die een land van een goed mag invoeren?",
        antwoord=["invoerquotum", "quotum", "een invoerquotum"],
        uitleg="Dat is het invoerquotum. Het legt de hoeveelheid vast; de prijs stijgt daarna omdat het aanbod beperkt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie heeft voordeel bij een importheffing? Duid alles aan wat juist is.",
        opties=[
            "De binnenlandse producent",
            "De overheid",
            "De arbeiders van die producent",
            "De koper in het eigen land",
        ],
        antwoord=[0, 1, 2],
        uitleg="De binnenlandse producent krijgt minder concurrentie en verkoopt meer, zijn personeel heeft daar werk aan, en de overheid haalt de heffing binnen. De koper betaalt een hogere prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke belemmering werkt niet via geld of via een hoeveelheid, maar via regels?",
        opties=[
            "De niet-tarifaire belemmering",
            "De importheffing aan de grens",
            "Het invoerquotum van de overheid",
            "De uitvoersubsidie voor bedrijven",
        ],
        antwoord=0,
        uitleg="Niet-tarifaire belemmeringen zijn normen, keuringen, labels of papierwerk. Ze kosten de invoerder tijd en geld zonder dat er een heffing of een quotum aan te pas komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legt een land soms toch handelsbelemmeringen op?",
        opties=[
            "Om de eigen bedrijven te beschermen",
            "Om de prijzen in de eigen winkels te laten dalen",
            "Om de consument een ruimere keuze te kunnen geven",
            "Om de uitvoer naar het buitenland te laten dalen",
        ],
        antwoord=0,
        uitleg="De reden is bijna altijd bescherming: eigen bedrijven en jobs afschermen van buitenlandse concurrentie, of inkomsten halen uit de heffing. De consument betaalt dan wel meer.",
    ),
]
