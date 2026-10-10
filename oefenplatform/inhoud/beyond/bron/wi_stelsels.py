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
        vraag=r"Wat staat er in de uitgebreide coëfficiëntenmatrix \((A \mid B)\) van een stelsel?",
        opties=[
            r"de coëfficiënten én de constanten uit het rechterlid",
            r"alleen de coëfficiënten van de onbekenden, kolom per kolom",
            r"alleen de constanten uit de rechterleden",
            r"de oplossingen van het stelsel, rij per rij",
        ],
        antwoord=0,
        uitleg=r"De constanten komen in een extra kolom achter de streep, zoals in \(\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & -1 & 1 \end{array}\right)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer heten twee stelsels gelijkwaardig?",
        opties=[
            r"als ze dezelfde oplossingenverzameling hebben",
            r"als ze evenveel vergelijkingen tellen",
            r"als ze dezelfde coëfficiënten bevatten",
            r"als ze allebei precies één oplossing hebben",
        ],
        antwoord=0,
        uitleg=r"Elke elementaire rijoperatie maakt een gelijkwaardig stelsel. Daarom mag je ze gebruiken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel oplossingen heeft een bepaald stelsel? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Bepaald betekent precies één oplossing. Onbepaald betekent oneindig veel, strijdig betekent geen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elementaire rijoperaties veranderen de oplossingenverzameling van een stelsel niet.",
        antwoord=True,
        uitleg=r"Daarom mag je ze blijven toepassen tot de oplossing er zo uit afleesbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat doet de methode van Gauss-Jordan?",
        opties=[
            r"ze vormt \((A \mid B)\) met rijoperaties om naar de rijcanonieke vorm",
            r"ze berekent \(\det A\) door naar een rij te ontwikkelen",
            r"ze vermenigvuldigt het stelsel met \(A^{T}\)",
            r"ze lost elke vergelijking apart op en vergelijkt daarna",
        ],
        antwoord=0,
        uitleg=r"In die vorm lees je de oplossing meteen af, of zie je dat er geen of oneindig veel zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is een stelsel strijdig?",
        opties=[
            r"als \(\text{rang}(A) < \text{rang}(A \mid B)\)",
            r"als \(\text{rang}(A) = \text{rang}(A \mid B)\)",
            r"als er meer onbekenden zijn dan vergelijkingen",
            r"als \(\det A \neq 0\)",
        ],
        antwoord=0,
        uitleg=r"Er staat dan ergens een rij die zegt dat \(0\) gelijk is aan een getal dat niet nul is.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een stelsel met meer onbekenden dan vergelijkingen heeft altijd oplossingen.",
        antwoord=False,
        uitleg=r"Het kan nog altijd strijdig zijn. Heeft het oplossingen, dan zijn het er wel meteen oneindig veel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een stelsel met \(3\) onbekenden heeft \(\text{rang}(A) = \text{rang}(A \mid B) = 2\). Hoeveel vrijheidsgraden heeft het? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Het aantal onbekenden min de rang: \(3 - 2 = 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe herken je een strijdig stelsel in de rijcanonieke vorm?",
        opties=[
            r"aan een rij \(\left(\begin{array}{ccc|c} 0 & 0 & 0 & 5 \end{array}\right)\)",
            r"aan een rij \(\left(\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right)\)",
            r"aan twee rijen die precies aan elkaar gelijk zijn",
            r"aan een kolom waarin geen enkele \(1\) voorkomt",
        ],
        antwoord=0,
        uitleg=r"Die rij zegt letterlijk dat \(0 = 5\), en dat kan niet. Een rij met overal nullen, ook rechts, is net onschuldig.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een onbepaald stelsel heeft oneindig veel oplossingen.",
        antwoord=True,
        uitleg=r"Je schrijft ze met een of meer parameters. Het aantal parameters is het aantal vrijheidsgraden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer heeft een stelsel met \(n\) onbekenden precies één oplossing?",
        opties=[
            r"als \(\text{rang}(A) = \text{rang}(A \mid B) = n\)",
            r"als beide rangen gelijk zijn aan het aantal vergelijkingen",
            r"als \(\text{rang}(A \mid B) > \text{rang}(A)\)",
            r"als het aantal vergelijkingen gelijk is aan \(n\)",
        ],
        antwoord=0,
        uitleg=r"Evenveel vergelijkingen als onbekenden volstaat niet: twee keer dezelfde vergelijking telt maar één keer mee.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een stelsel met \(4\) onbekenden heeft precies één oplossing. Hoeveel is \(\text{rang}(A)\)? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg=r"Voor één oplossing moet de rang gelijk zijn aan het aantal onbekenden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer kan je \(A \cdot X = B\) oplossen als \(X = A^{-1} \cdot B\)?",
        opties=[
            r"als \(A\) vierkant is en \(\det A \neq 0\)",
            r"als het stelsel meer onbekenden heeft dan vergelijkingen",
            r"als alle constanten in \(B\) nul zijn",
            r"altijd, want elke matrix heeft een inverse",
        ],
        antwoord=0,
        uitleg=r"Je vermenigvuldigt dan links met \(A^{-1}\) en leest de oplossing meteen af.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een elementaire rijoperatie mag je \(R_{i} \to 0 \cdot R_{i}\) uitvoeren.",
        antwoord=False,
        uitleg=r"Dan gooi je een hele vergelijking weg en verandert de oplossingenverzameling. Alleen \(R_{i} \to k \cdot R_{i}\) met \(k \neq 0\) mag.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een vrijheidsgraad bij een onbepaald stelsel?",
        opties=[
            r"een onbekende die je vrij mag kiezen, waarna de rest vastligt",
            r"een vergelijking die je uit het stelsel mag schrappen",
            r"een oplossing die niet aan alle vergelijkingen voldoet",
            r"het verschil tussen het aantal rijen en het aantal kolommen",
        ],
        antwoord=0,
        uitleg=r"Elke vrijheidsgraad wordt in je antwoord een parameter. Hun aantal is \(n - \text{rang}(A)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe noteer je de oplossingenverzameling van een onbepaald stelsel?",
        opties=[
            r"als \(\{(x, y, z) \mid x = 1 + t,\ y = 2 - t,\ z = t\}\)",
            r"als één enkel getal, namelijk de kleinste oplossing die je vindt",
            r"als het aantal oplossingen, dus als \(\infty\)",
            r"als de rijcanonieke matrix zelf, zonder meer",
        ],
        antwoord=0,
        uitleg=r"Zo zie je meteen hoe de oplossingen van elkaar afhangen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee evenwijdige rechten die niet samenvallen, geven een strijdig stelsel.",
        antwoord=True,
        uitleg=r"Ze snijden elkaar nergens, dus er is geen enkel punt dat aan allebei de vergelijkingen voldoet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel oplossingen heeft een strijdig stelsel? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg=r"De oplossingenverzameling is leeg: \(V = \emptyset\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je kent het totaalbedrag van drie bestellingen met telkens dezelfde drie artikelen. Wat kan je berekenen?",
        opties=[
            r"de prijs per artikel, als het stelsel bepaald is",
            r"de prijs per artikel, in elk geval en altijd",
            r"het aantal artikelen per bestelling, als die gegeven zijn",
            r"niets, want er zijn te weinig gegevens om te rekenen",
        ],
        antwoord=0,
        uitleg=r"Drie vergelijkingen met drie onbekenden, maar enkel als de drie bestellingen echt nieuwe informatie geven. Anders is het stelsel onbepaald of strijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom mag je bij Gauss-Jordan rijen optellen en verwisselen?",
        opties=[
            r"omdat die bewerkingen een gelijkwaardig stelsel opleveren",
            r"omdat \(\det A\) daardoor niet verandert",
            r"omdat de matrix daardoor vierkant wordt",
            r"omdat het aantal onbekenden daardoor stap voor stap afneemt",
        ],
        antwoord=0,
        uitleg=r"De oplossingen blijven dezelfde, en dat is het enige wat telt. \(\det A\) verandert er wél door.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat beschrijft een overgangsmatrix \(T\)?",
        opties=[
            r"hoe een toestand overgaat in de volgende toestand",
            r"hoeveel elementen een verzameling in totaal heeft",
            r"de determinant van een vierkante matrix",
            r"de oplossingen van een stelsel vergelijkingen",
        ],
        antwoord=0,
        uitleg=r"Je rekent \(X_{1} = T \cdot X_{0}\): de huidige toestand maal de matrix geeft de volgende.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een graaf?",
        opties=[
            r"een tekening met punten en verbindingen ertussen",
            r"de grafiek van een functie in een assenstelsel",
            r"een tabel met de gegevens van een onderzoek",
            r"een matrix met enkel nullen en enen erin",
        ],
        antwoord=0,
        uitleg=r"De punten heten knopen. Elke graaf kan je als matrix schrijven, en elke zo'n matrix als graaf tekenen.",
    ),
    dict(
        type="invultekst",
        vraag=r"In een verbindingsmatrix staat een \(1\) waar er een verbinding is. Welk getal staat er waar er geen is? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Zo lees je de hele graaf af uit een rooster van nullen en enen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een Markov-matrix telt elke kolom op tot \(1\).",
        antwoord=True,
        uitleg=r"Elke kolom bevat de kansen waarmee één toestand naar alle mogelijke volgende toestanden gaat, en samen is dat zeker.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat beschrijft een Lesliematrix?",
        opties=[
            r"hoe een populatie per leeftijdsgroep evolueert",
            r"hoe twee ondernemingen klanten uitwisselen",
            r"welke steden rechtstreeks verbonden zijn",
            r"hoeveel wegen er tussen twee knopen lopen",
        ],
        antwoord=0,
        uitleg=r"Ze bevat de overlevingskansen en het aantal nakomelingen per leeftijdsgroep.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de toestand na twee overgangen?",
        opties=[
            r"\(X_{2} = T^{2} \cdot X_{0}\)",
            r"\(X_{2} = 2 \cdot X_{0}\)",
            r"\(X_{2} = (2T) \cdot X_{0}\)",
            r"\(X_{2} = X_{0} + X_{1}\)",
        ],
        antwoord=0,
        uitleg=r"Twee keer dezelfde overgang toepassen is net de matrix in het kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het kwadraat van een verbindingsmatrix telt hoeveel wegen van lengte \(2\) er tussen twee knopen zijn.",
        antwoord=True,
        uitleg=r"Elk element is een rij tegen een kolom, en dat telt precies de tussenstops die beide verbindingen hebben.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je wil \(X_{5}\), de toestand na vijf overgangen. Tot welke macht verhef je \(T\)? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg=r"Eén macht per stap: \(X_{5} = T^{5} \cdot X_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een evenwichtstoestand bij een matrixmodel?",
        opties=[
            r"een toestand \(X\) waarvoor \(T \cdot X = X\)",
            r"een toestand waarin alle getallen even groot zijn",
            r"de toestand waarmee het model begint te rekenen",
            r"de toestand waarin alle elementen nul zijn geworden",
        ],
        antwoord=0,
        uitleg=r"Vermenigvuldigen met \(T\) verandert er dan niets meer aan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elk matrixmodel komt na verloop van tijd in evenwicht.",
        antwoord=False,
        uitleg=r"Sommige blijven schommelen of groeien onbeperkt. Of er stabilisatie optreedt, moet je nagaan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat beschrijft een migratiematrix?",
        opties=[
            r"hoeveel inwoners er van de ene streek naar de andere verhuizen",
            r"hoeveel inwoners elke streek in het totaal telt",
            r"hoe ver twee streken in kilometer van elkaar verwijderd liggen",
            r"hoeveel wegen er tussen twee streken lopen",
        ],
        antwoord=0,
        uitleg=r"Het is een overgangsmatrix waarin de toestanden de streken zijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een graaf heeft \(4\) knopen. Welke orde heeft zijn verbindingsmatrix? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg=r"Eén rij en één kolom per knoop, dus een vierkante matrix van orde \(4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waaraan zie je dat een matrixmodel stabiliseert?",
        opties=[
            r"de opeenvolgende toestanden verschillen bijna niet meer van elkaar",
            r"de overgangsmatrix wordt na een tijd de nulmatrix",
            r"\(\det T\) wordt uiteindelijk gelijk aan nul",
            r"alle elementen van de toestand worden even groot",
        ],
        antwoord=0,
        uitleg=r"Je berekent een aantal stappen na elkaar en kijkt of de getallen stilvallen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een overgangsmatrix is altijd vierkant.",
        antwoord=True,
        uitleg=r"Ze zet een toestand om in een toestand van dezelfde soort, dus evenveel rijen als kolommen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent een \(0\) in een overgangsmatrix?",
        opties=[
            r"die overgang komt niet voor",
            r"die overgang gebeurt altijd",
            r"die toestand bestaat niet meer",
            r"de matrix is niet inverteerbaar",
        ],
        antwoord=0,
        uitleg=r"De kans of het aantal is dan nul: er gaat niets van de ene toestand naar de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom gebruik je bij deze modellen een rekenapp?",
        opties=[
            r"omdat je vaak hoge machten \(T^{k}\) nodig hebt",
            r"omdat de matrices te groot zijn om op te schrijven",
            r"omdat je anders de overgangsmatrix niet kan opstellen",
            r"omdat de uitkomsten anders niet nauwkeurig genoeg zijn",
        ],
        antwoord=0,
        uitleg=r"Een model twintig stappen laten lopen is met de hand niet te doen. Het model opstellen en de uitkomst duiden blijft jouw werk.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een matrixmodel voorspelt met zekerheid wat er zal gebeuren.",
        antwoord=False,
        uitleg=r"Het rekent uit wat er gebeurt als de overgangen gelijk blijven. Verandert er iets in de werkelijkheid, dan klopt het model niet meer.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de som van de getallen in één kolom van een Markov-matrix? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Alle kansen samen vanuit één toestand vormen een zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zet een directe wegen matrix in beeld?",
        opties=[
            r"welke knopen rechtstreeks met elkaar verbonden zijn",
            r"hoe lang de weg tussen twee knopen is",
            r"hoeveel knopen de graaf in het totaal samen heeft",
            r"welke knopen via een omweg bereikbaar zijn",
        ],
        antwoord=0,
        uitleg=r"Omwegen vind je pas in de machten van die matrix terug.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Elk jaar wisselt een deel van de klanten van merk. Hoe bereken je de verdeling over tien jaar?",
        opties=[
            r"\(X_{10} = T^{10} \cdot X_{0}\)",
            r"\(X_{10} = 10 \cdot X_{0} + T\)",
            r"\(X_{10} = (10T) \cdot X_{0}\)",
            r"\(X_{10} = X_{0} : T\)",
        ],
        antwoord=0,
        uitleg=r"Elke macht van de matrix is één jaar verder. Vaak stabiliseert zo'n model naar een vaste marktverdeling.",
    ),
]
