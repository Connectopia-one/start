# -*- coding: utf-8 -*-
"""Stelsels oplossen met Gauss-Jordan, en matrixmodellen.

Het tweede stuk van het onderdeel "Algebra" van fiche G3. De stelsels sluiten
rechtstreeks aan bij de rang en de rijcanonieke vorm van het vorige thema; de
matrixmodellen laten zien waarvoor je matrices in de praktijk gebruikt.

Deel 1 zijn de stelsels van eerstegraadsvergelijkingen.
Deel 2 zijn de matrixmodellen: overgangsmatrices, grafen en evenwicht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de uitgebreide coëfficiëntenmatrix van een stelsel?",
        opties=[
            "de coëfficiënten én de constanten uit het rechterlid",
            "alleen de coëfficiënten van de onbekenden, kolom per kolom",
            "alleen de constanten uit de rechterleden",
            "de oplossingen van het stelsel, rij per rij",
        ],
        antwoord=0,
        uitleg="De constanten komen in een extra kolom, meestal met een streep ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heten twee stelsels gelijkwaardig?",
        opties=[
            "als ze dezelfde oplossingenverzameling hebben",
            "als ze evenveel vergelijkingen tellen",
            "als ze dezelfde coëfficiënten bevatten",
            "als ze allebei precies één oplossing hebben",
        ],
        antwoord=0,
        uitleg="Elke elementaire rijoperatie maakt een gelijkwaardig stelsel. Daarom mag je ze gebruiken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel oplossingen heeft een bepaald stelsel? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Bepaald betekent precies één oplossing. Onbepaald betekent oneindig veel, strijdig betekent geen.",
    ),
    dict(
        type="waarofniet",
        vraag="Elementaire rijoperaties veranderen de oplossingenverzameling van een stelsel niet.",
        antwoord=True,
        uitleg="Daarom mag je ze blijven toepassen tot de oplossing er zo uit afleesbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de methode van Gauss-Jordan?",
        opties=[
            "ze vormt de matrix met rijoperaties om naar de rijcanonieke vorm",
            "ze berekent de determinant door naar een rij te ontwikkelen",
            "ze vermenigvuldigt het stelsel met zijn eigen getransponeerde",
            "ze lost elke vergelijking apart op en vergelijkt daarna",
        ],
        antwoord=0,
        uitleg="In die vorm lees je de oplossing meteen af, of zie je dat er geen of oneindig veel zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een stelsel strijdig?",
        opties=[
            "als de rang van de coëfficiëntenmatrix kleiner is dan die van de uitgebreide",
            "als de rang van de coëfficiëntenmatrix gelijk is aan die van de uitgebreide",
            "als er meer onbekenden zijn dan vergelijkingen in het stelsel",
            "als de determinant van de coëfficiëntenmatrix verschillend is van nul",
        ],
        antwoord=0,
        uitleg="Er staat dan ergens een rij die zegt dat nul gelijk is aan een getal dat niet nul is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stelsel met meer onbekenden dan vergelijkingen heeft altijd oplossingen.",
        antwoord=False,
        uitleg="Het kan nog altijd strijdig zijn. Heeft het oplossingen, dan zijn het er wel meteen oneindig veel.",
    ),
    dict(
        type="invultekst",
        vraag="Een stelsel met drie onbekenden heeft twee gelijke rangen, allebei gelijk aan twee. Hoeveel vrijheidsgraden heeft het? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Het aantal onbekenden min de rang, dus drie min twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe herken je een strijdig stelsel in de rijcanonieke vorm?",
        opties=[
            "aan een rij met overal nullen links en een getal dat niet nul is rechts",
            "aan een rij met overal nullen, ook in de allerlaatste kolom helemaal rechts",
            "aan twee rijen die precies aan elkaar gelijk zijn",
            "aan een kolom waarin geen enkele één voorkomt",
        ],
        antwoord=0,
        uitleg="Die rij zegt letterlijk dat nul gelijk is aan dat getal, en dat kan niet. Een rij met overal nullen is net onschuldig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onbepaald stelsel heeft oneindig veel oplossingen.",
        antwoord=True,
        uitleg="Je schrijft ze met een of meer parameters. Het aantal parameters is het aantal vrijheidsgraden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heeft een stelsel precies één oplossing?",
        opties=[
            "als beide rangen gelijk zijn aan het aantal onbekenden",
            "als beide rangen gelijk zijn aan het aantal vergelijkingen",
            "als de rang van de uitgebreide matrix de grootste is",
            "als het aantal vergelijkingen gelijk is aan het aantal onbekenden",
        ],
        antwoord=0,
        uitleg="Evenveel vergelijkingen als onbekenden volstaat niet: twee keer dezelfde vergelijking telt maar één keer mee.",
    ),
    dict(
        type="invultekst",
        vraag="Een stelsel met vier onbekenden heeft precies één oplossing. Welke rang heeft de coëfficiëntenmatrix? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg="Voor één oplossing moet de rang gelijk zijn aan het aantal onbekenden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kan je een stelsel oplossen met de inverse matrix?",
        opties=[
            "als de coëfficiëntenmatrix vierkant en inverteerbaar is",
            "als het stelsel meer onbekenden heeft dan vergelijkingen",
            "als alle constanten in het rechterlid nul zijn",
            "altijd, want elke matrix heeft een inverse",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt dan links met de inverse en leest de oplossing meteen af.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een elementaire rijoperatie mag je een rij met nul vermenigvuldigen.",
        antwoord=False,
        uitleg="Dan gooi je een hele vergelijking weg en verandert de oplossingenverzameling. Vermenigvuldigen mag alleen met een getal dat niet nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vrijheidsgraad bij een onbepaald stelsel?",
        opties=[
            "een onbekende die je vrij mag kiezen, waarna de rest vastligt",
            "een vergelijking die je uit het stelsel mag schrappen",
            "een oplossing die niet aan alle vergelijkingen voldoet",
            "het verschil tussen het aantal rijen en het aantal kolommen",
        ],
        antwoord=0,
        uitleg="Elke vrijheidsgraad wordt in je antwoord een parameter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noteer je de oplossingenverzameling van een onbepaald stelsel?",
        opties=[
            "als een verzameling van koppels of drietallen met een parameter erin",
            "als één enkel getal, namelijk de kleinste oplossing die je vindt",
            "als het aantal oplossingen, dus als oneindig",
            "als de rijcanonieke matrix zelf, zonder meer",
        ],
        antwoord=0,
        uitleg="Zo zie je meteen hoe de oplossingen van elkaar afhangen.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee evenwijdige rechten die niet samenvallen, geven een strijdig stelsel.",
        antwoord=True,
        uitleg="Ze snijden elkaar nergens, dus er is geen enkel punt dat aan allebei de vergelijkingen voldoet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel oplossingen heeft een strijdig stelsel? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg="De oplossingenverzameling is leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent het totaalbedrag van drie bestellingen met telkens dezelfde drie artikelen. Wat kan je berekenen?",
        opties=[
            "de prijs per artikel, als het stelsel bepaald is",
            "de prijs per artikel, in elk geval en altijd",
            "het aantal artikelen per bestelling, als die gegeven zijn",
            "niets, want er zijn te weinig gegevens om te rekenen",
        ],
        antwoord=0,
        uitleg="Drie vergelijkingen met drie onbekenden, maar enkel als de drie bestellingen echt nieuwe informatie geven. Anders is het stelsel onbepaald of strijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je bij Gauss-Jordan rijen optellen en verwisselen?",
        opties=[
            "omdat die bewerkingen een gelijkwaardig stelsel opleveren",
            "omdat de determinant daardoor niet verandert",
            "omdat de matrix daardoor vierkant wordt",
            "omdat het aantal onbekenden daardoor stap voor stap afneemt",
        ],
        antwoord=0,
        uitleg="De oplossingen blijven dezelfde, en dat is het enige wat telt. De determinant verandert er wél door.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft een overgangsmatrix?",
        opties=[
            "hoe een toestand overgaat in de volgende toestand",
            "hoeveel elementen een verzameling in totaal heeft",
            "de determinant van een vierkante matrix",
            "de oplossingen van een stelsel vergelijkingen",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt de huidige toestand met de matrix en krijgt de volgende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een graaf?",
        opties=[
            "een tekening met punten en verbindingen ertussen",
            "de grafiek van een functie in een assenstelsel",
            "een tabel met de gegevens van een onderzoek",
            "een matrix met enkel nullen en enen erin",
        ],
        antwoord=0,
        uitleg="De punten heten knopen. Elke graaf kan je als matrix schrijven, en elke zo'n matrix als graaf tekenen.",
    ),
    dict(
        type="invultekst",
        vraag="In een verbindingsmatrix staat een één waar er een verbinding is. Welk getal staat er waar er geen is? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Zo lees je de hele graaf af uit een rooster van nullen en enen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een Markov-matrix telt elke kolom op tot één.",
        antwoord=True,
        uitleg="Elke kolom bevat de kansen waarmee één toestand naar alle mogelijke volgende toestanden gaat, en samen is dat zeker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft een Lesliematrix?",
        opties=[
            "hoe een populatie per leeftijdsgroep evolueert",
            "hoe twee ondernemingen klanten uitwisselen",
            "welke steden rechtstreeks verbonden zijn",
            "hoeveel wegen er tussen twee knopen lopen",
        ],
        antwoord=0,
        uitleg="Ze bevat de overlevingskansen en het aantal nakomelingen per leeftijdsgroep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de toestand na twee overgangen?",
        opties=[
            "door de begintoestand met het kwadraat van de overgangsmatrix te vermenigvuldigen",
            "door de begintoestand met twee te vermenigvuldigen",
            "door de overgangsmatrix met het getal twee te vermenigvuldigen en toe te passen",
            "door de twee toestanden bij elkaar op te tellen",
        ],
        antwoord=0,
        uitleg="Twee keer dezelfde overgang toepassen is net de matrix in het kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kwadraat van een verbindingsmatrix telt hoeveel wegen van lengte twee er tussen twee knopen zijn.",
        antwoord=True,
        uitleg="Elk element is een rij tegen een kolom, en dat telt precies de tussenstops die beide verbindingen hebben.",
    ),
    dict(
        type="invultekst",
        vraag="Je wil de toestand na vijf overgangen. Tot welke macht verhef je de overgangsmatrix? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg="Eén macht per stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een evenwichtstoestand bij een matrixmodel?",
        opties=[
            "een toestand die na de overgang gelijk blijft",
            "een toestand waarin alle getallen even groot zijn",
            "de toestand waarmee het model begint te rekenen",
            "de toestand waarin alle elementen nul zijn geworden",
        ],
        antwoord=0,
        uitleg="Vermenigvuldigen met de overgangsmatrix verandert er dan niets meer aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk matrixmodel komt na verloop van tijd in evenwicht.",
        antwoord=False,
        uitleg="Sommige blijven schommelen of groeien onbeperkt. Of er stabilisatie optreedt, moet je nagaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft een migratiematrix?",
        opties=[
            "hoeveel inwoners er van de ene streek naar de andere verhuizen",
            "hoeveel inwoners elke streek in het totaal telt",
            "hoe ver twee streken in kilometer van elkaar verwijderd liggen",
            "hoeveel wegen er tussen twee streken lopen",
        ],
        antwoord=0,
        uitleg="Het is een overgangsmatrix waarin de toestanden de streken zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Een graaf heeft vier knopen. Welke orde heeft zijn verbindingsmatrix? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg="Eén rij en één kolom per knoop, dus een vierkante matrix van orde vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je dat een matrixmodel stabiliseert?",
        opties=[
            "de opeenvolgende toestanden verschillen bijna niet meer van elkaar",
            "de overgangsmatrix wordt na een tijd de nulmatrix",
            "de determinant van de overgangsmatrix wordt uiteindelijk gelijk aan nul",
            "alle elementen van de toestand worden even groot",
        ],
        antwoord=0,
        uitleg="Je berekent een aantal stappen na elkaar en kijkt of de getallen stilvallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een overgangsmatrix is altijd vierkant.",
        antwoord=True,
        uitleg="Ze zet een toestand om in een toestand van dezelfde soort, dus evenveel rijen als kolommen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een nul in een overgangsmatrix?",
        opties=[
            "die overgang komt niet voor",
            "die overgang gebeurt altijd",
            "die toestand bestaat niet meer",
            "de matrix is niet inverteerbaar",
        ],
        antwoord=0,
        uitleg="De kans of het aantal is dan nul: er gaat niets van de ene toestand naar de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je bij deze modellen een rekenapp?",
        opties=[
            "omdat je vaak hoge machten van een matrix nodig hebt",
            "omdat de matrices te groot zijn om op te schrijven",
            "omdat je anders de overgangsmatrix niet kan opstellen",
            "omdat de uitkomsten anders niet nauwkeurig genoeg zijn",
        ],
        antwoord=0,
        uitleg="Een model twintig stappen laten lopen is met de hand niet te doen. Het model opstellen en de uitkomst duiden blijft jouw werk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een matrixmodel voorspelt met zekerheid wat er zal gebeuren.",
        antwoord=False,
        uitleg="Het rekent uit wat er gebeurt als de overgangen gelijk blijven. Verandert er iets in de werkelijkheid, dan klopt het model niet meer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de getallen in één kolom van een Markov-matrix? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Alle kansen samen vanuit één toestand vormen een zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet een directe wegen matrix in beeld?",
        opties=[
            "welke knopen rechtstreeks met elkaar verbonden zijn",
            "hoe lang de weg tussen twee knopen is",
            "hoeveel knopen de graaf in het totaal samen heeft",
            "welke knopen via een omweg bereikbaar zijn",
        ],
        antwoord=0,
        uitleg="Omwegen vind je pas in de machten van die matrix terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Elk jaar wisselt een deel van de klanten van merk. Hoe bereken je de verdeling over tien jaar?",
        opties=[
            "de beginverdeling maal de overgangsmatrix tot de tiende macht",
            "de beginverdeling maal tien, en dan de matrix erbij optellen",
            "de overgangsmatrix maal tien, en dan vermenigvuldigen",
            "de beginverdeling gedeeld door de overgangsmatrix",
        ],
        antwoord=0,
        uitleg="Elke macht van de matrix is één jaar verder. Vaak stabiliseert zo'n model naar een vaste marktverdeling.",
    ),
]
