# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: matrices, grafen en stelsels.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED): rekenen met
matrices (dimensie, optelling, scalaire vermenigvuldiging, product, macht,
transponeren, bijzondere matrices, eigenschappen), matrixmodellen
(overgangsmatrix, Lesliematrix, migratiematrix, verbindingsmatrix, Markov,
graaf, evenwichtstoestand) en stelsels van eerstegraadsvergelijkingen met
Gauss-Jordan (uitgebreide coëfficiëntenmatrix, rijoperaties, rijcanonieke
matrix, bepaald, onbepaald of strijdig stelsel).

Deel 1: rekenen met matrices. Deel 2: matrixmodellen, grafen en stelsels.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Een matrix heeft \(2\) rijen en \(3\) kolommen. Wat is de dimensie?",
        opties=[r"\(2 \times 3\)", r"\(3 \times 2\)", r"\(6\)", r"\(5\)"],
        antwoord=0,
        uitleg=r"Eerst het aantal rijen, dan het aantal kolommen.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(A = \begin{bmatrix} 4 & 7 & 1 \\ 2 & 5 & 9 \end{bmatrix}\). Wat is het element \(a_{23}\)?",
        antwoord=["9", "negen"],
        uitleg=r"Rij \(2\), kolom \(3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} + \begin{bmatrix} 5 & 0 \\ -1 & 2 \end{bmatrix} = \) ...",
        opties=[r"\(\begin{bmatrix} 6 & 2 \\ 2 & 6 \end{bmatrix}\)", r"\(\begin{bmatrix} 5 & 0 \\ -3 & 8 \end{bmatrix}\)", r"\(\begin{bmatrix} 6 & 2 \\ 4 & 6 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Element per element optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(3 \cdot \begin{bmatrix} 2 & -1 \\ 0 & 4 \end{bmatrix} = \) ...",
        opties=[r"\(\begin{bmatrix} 6 & -3 \\ 0 & 12 \end{bmatrix}\)", r"\(\begin{bmatrix} 5 & 2 \\ 3 & 7 \end{bmatrix}\)", r"\(\begin{bmatrix} 6 & -1 \\ 0 & 4 \end{bmatrix}\)", r"\(\begin{bmatrix} 6 & -3 \\ 3 & 12 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Elk element maal \(3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Je kan twee matrices enkel optellen als ze dezelfde dimensie hebben.",
        antwoord=True,
        uitleg=r"Je telt element per element op, dus elk element moet een partner hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A\) is een \(2 \times 3\)-matrix en \(B\) een \(3 \times 4\)-matrix. Wat is de dimensie van \(A \cdot B\)?",
        opties=[r"\(2 \times 4\)", r"\(3 \times 3\)", r"\(4 \times 2\)", r"het product bestaat niet"],
        antwoord=0,
        uitleg=r"Het aantal kolommen van \(A\) (\(3\)) is gelijk aan het aantal rijen van \(B\). Het product krijgt de rijen van \(A\) en de kolommen van \(B\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \cdot \begin{bmatrix} 4 \\ 5 \end{bmatrix} = \) ...",
        opties=[r"\(\begin{bmatrix} 14 \\ 15 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 & 10 \\ 0 & 15 \end{bmatrix}\)", r"\(\begin{bmatrix} 9 \\ 15 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 \\ 15 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Rij maal kolom: \(1 \cdot 4 + 2 \cdot 5 = 14\) en \(0 \cdot 4 + 3 \cdot 5 = 15\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor vierkante matrices geldt altijd \(A \cdot B = B \cdot A\).",
        antwoord=False,
        uitleg=r"De matrixvermenigvuldiging is niet commutatief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de getransponeerde van \(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\)?",
        opties=[r"\(\begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 2 & 1 \\ 6 & 5 & 4 \end{bmatrix}\)", r"\(\begin{bmatrix} 4 & 5 & 6 \\ 1 & 2 & 3 \end{bmatrix}\)", r"\(\begin{bmatrix} 6 & 3 \\ 5 & 2 \\ 4 & 1 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Rijen worden kolommen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke matrix is de eenheidsmatrix van orde \(2\)?",
        opties=[r"\(\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Enen op de hoofddiagonaal, nullen elders. Ze is het neutraal element voor de vermenigvuldiging.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een symmetrische matrix is altijd een diagonaalmatrix.",
        antwoord=False,
        uitleg=r"Symmetrisch betekent \(a_{ij} = a_{ji}\): gelijk aan de getransponeerde. \(\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}\) is symmetrisch maar geen diagonaalmatrix.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke matrix is een diagonaalmatrix?",
        opties=[r"\(\begin{bmatrix} 3 & 0 \\ 0 & -2 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 1 \\ 0 & -2 \end{bmatrix}\)", r"\(\begin{bmatrix} 0 & 3 \\ -2 & 0 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 3 \\ 3 & 3 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Een vierkante matrix met enkel nullen buiten de hoofddiagonaal.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(A = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix}\). Wat is het element op rij \(2\), kolom \(1\) van \(A^{2}\)?",
        antwoord=["3", "drie"],
        uitleg=r"\(A^{2} = A \cdot A\). Rij \(2\) maal kolom \(1\): \(1 \cdot 2 + 1 \cdot 1 = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een winkel verkoopt \(10\) broden en \(4\) taarten. Een brood kost \(3\) euro, een taart \(12\) euro. Welk product geeft de omzet?",
        opties=[r"\(\begin{bmatrix} 10 & 4 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 12 \end{bmatrix}\)", r"\(\begin{bmatrix} 10 & 4 \end{bmatrix} \cdot \begin{bmatrix} 3 & 12 \end{bmatrix}\)", r"\(\begin{bmatrix} 10 \\ 4 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 12 \end{bmatrix}\)", r"\(\begin{bmatrix} 3 & 12 \end{bmatrix} + \begin{bmatrix} 10 & 4 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"Rijmatrix maal kolommatrix: \(10 \cdot 3 + 4 \cdot 12 = 78\) euro.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij matrices kan \(A \cdot B\) de nulmatrix zijn terwijl \(A\) en \(B\) zelf niet de nulmatrix zijn.",
        antwoord=True,
        uitleg=r"Zulke matrices heten nuldelers, bijvoorbeeld \(\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}^{2}\) is de nulmatrix.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \((A \cdot B)^{T}\)?",
        opties=[r"\(B^{T} \cdot A^{T}\)", r"\(A^{T} \cdot B^{T}\)", r"\(A \cdot B\)", r"\(B \cdot A\)"],
        antwoord=0,
        uitleg=r"Bij het transponeren van een product draait de volgorde om.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke matrix kan je met zichzelf vermenigvuldigen.",
        antwoord=False,
        uitleg=r"Enkel een vierkante matrix: anders past het aantal kolommen niet bij het aantal rijen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het symmetrisch element van \(A\) voor de optelling?",
        opties=[r"\(-A\)", r"\(A^{T}\)", r"de eenheidsmatrix", r"\(\dfrac{1}{A}\)"],
        antwoord=0,
        uitleg=r"\(A + (-A)\) is de nulmatrix.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee matrices zijn gelijk als ...",
        opties=[
            r"ze dezelfde dimensie hebben en alle overeenkomstige elementen gelijk zijn",
            r"ze dezelfde dimensie hebben",
            r"de som van hun elementen gelijk is",
            r"hun eerste rij gelijk is",
        ],
        antwoord=0,
        uitleg=r"Dimensie en elk element op dezelfde plaats moeten kloppen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(A \cdot (B + C) = A \cdot B + A \cdot C\) voor matrices waarvoor dat product bestaat.",
        antwoord=True,
        uitleg=r"De matrixvermenigvuldiging is distributief ten opzichte van de optelling.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Bij een overgangsmatrix (Markov-matrix) is de som van de elementen in elke kolom ...",
        opties=[r"\(1\)", r"\(0\)", r"\(100\)", r"telkens anders"],
        antwoord=0,
        uitleg=r"Elke kolom verdeelt een groep over alle toestanden: samen \(100\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Overgangsmatrix \(T = \begin{bmatrix} 0{,}8 & 0{,}3 \\ 0{,}2 & 0{,}7 \end{bmatrix}\) (kolom = van, rij = naar), beginsituatie \(\begin{bmatrix} 100 \\ 100 \end{bmatrix}\). Wat is de toestand na één stap?",
        opties=[r"\(\begin{bmatrix} 110 \\ 90 \end{bmatrix}\)", r"\(\begin{bmatrix} 100 \\ 100 \end{bmatrix}\)", r"\(\begin{bmatrix} 80 \\ 70 \end{bmatrix}\)", r"\(\begin{bmatrix} 90 \\ 110 \end{bmatrix}\)"],
        antwoord=0,
        uitleg=r"\(0{,}8 \cdot 100 + 0{,}3 \cdot 100 = 110\) en \(0{,}2 \cdot 100 + 0{,}7 \cdot 100 = 90\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de toestand na \(n\) stappen met overgangsmatrix \(T\) en begintoestand \(X_{0}\)?",
        opties=[r"\(T^{n} \cdot X_{0}\)", r"\(n \cdot T \cdot X_{0}\)", r"\(T \cdot X_{0}^{n}\)", r"\(X_{0} + n \cdot T\)"],
        antwoord=0,
        uitleg=r"Elke stap vermenigvuldig je opnieuw met \(T\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een evenwichtstoestand \(X\) geldt \(T \cdot X = X\).",
        antwoord=True,
        uitleg=r"Na nog een stap verandert de toestand niet meer: er is stabilisatie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat staat er op de eerste rij van een Lesliematrix?",
        opties=[r"de vruchtbaarheidscijfers van elke leeftijdsklasse", r"de overlevingskansen", r"het aantal dieren per klasse", r"enkel nullen"],
        antwoord=0,
        uitleg=r"Onder de hoofddiagonaal staan de overlevingskansen naar de volgende klasse.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een verbindingsmatrix van een graaf staat op plaats \((i, j)\) een \(1\). Wat betekent dat?",
        opties=[r"er is een rechtstreekse verbinding van knoop \(i\) naar knoop \(j\)", r"knoop \(i\) en \(j\) zijn dezelfde", r"er is geen verbinding", r"de afstand is \(1\) km"],
        antwoord=0,
        uitleg=r"Een \(0\) betekent geen rechtstreekse verbinding.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Met \(M^{2}\), het kwadraat van de verbindingsmatrix, tel je de wegen van lengte \(2\) tussen twee knopen.",
        antwoord=True,
        uitleg=r"Een element van \(M^{2}\) telt de tussenstops via een derde knoop.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een graaf heeft knopen \(A\), \(B\), \(C\) met pijlen \(A \to B\), \(B \to C\) en \(C \to A\). Hoeveel enen staan er in de verbindingsmatrix?",
        opties=[r"\(3\)", r"\(6\)", r"\(9\)", r"\(2\)"],
        antwoord=0,
        uitleg=r"Eén \(1\) per pijl.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de uitgebreide coëfficiëntenmatrix van \(\begin{cases} 2x + y = 5 \\ x - 3y = 1 \end{cases}\)?",
        opties=[r"\(\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & -3 & 1 \end{array}\right]\)", r"\(\left[\begin{array}{cc} 2 & 1 \\ 1 & -3 \end{array}\right]\)", r"\(\left[\begin{array}{cc|c} 2 & 5 & 1 \\ 1 & 1 & -3 \end{array}\right]\)", r"\(\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & 3 & 1 \end{array}\right]\)"],
        antwoord=0,
        uitleg=r"De coëfficiënten van \(x\) en \(y\), en de rechterleden achter de streep. Zonder streep is het de gewone coëfficiëntenmatrix.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke bewerking is geen elementaire rijoperatie?",
        opties=[r"twee elementen in dezelfde rij van plaats wisselen", r"twee rijen van plaats wisselen", r"een rij vermenigvuldigen met een getal verschillend van \(0\)", r"een veelvoud van een rij bij een andere rij optellen"],
        antwoord=0,
        uitleg=r"Elementen binnen een rij wisselen verandert het stelsel. De andere drie geven een gelijkwaardig stelsel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Na Gauss-Jordan krijg je \(\left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & -1 \end{array}\right]\). Wat is de oplossing?",
        opties=[r"\(V = \{(2, -1)\}\)", r"\(V = \{(-1, 2)\}\)", r"\(V = \{(1, 1)\}\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"De eerste rij zegt \(x = 2\), de tweede \(y = -1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rijcanonieke matrix bevat de rij \(\left[\begin{array}{ccc|c} 0 & 0 & 0 & 4 \end{array}\right]\). Wat voor stelsel is het?",
        opties=[r"strijdig", r"bepaald", r"onbepaald met één vrijheidsgraad", r"onbepaald met twee vrijheidsgraden"],
        antwoord=0,
        uitleg=r"Die rij zegt \(0 = 4\): onmogelijk, dus geen oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een stelsel met een rij \(\left[\begin{array}{ccc|c} 0 & 0 & 0 & 0 \end{array}\right]\) is altijd strijdig.",
        antwoord=False,
        uitleg=r"\(0 = 0\) klopt altijd. Zo'n rij valt gewoon weg; vaak blijft er een onbepaald stelsel over.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Na Gauss-Jordan: \(\left[\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]\). Wat voor stelsel is het?",
        opties=[r"onbepaald met één vrijheidsgraad", r"bepaald", r"strijdig", r"onbepaald met twee vrijheidsgraden"],
        antwoord=0,
        uitleg=r"Drie onbekenden en twee leidende enen: \(z\) is vrij te kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij dat onbepaald stelsel: hoe noteer je de oplossingen met \(z = r\)?",
        opties=[r"\(V = \{(3 - 2r, 1 + r, r) \mid r \in \mathbb{R}\}\)", r"\(V = \{(3, 1, 0)\}\)", r"\(V = \{(3 + 2r, 1 - r, r) \mid r \in \mathbb{R}\}\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"\(x + 2z = 3\) geeft \(x = 3 - 2r\), en \(y - z = 1\) geeft \(y = 1 + r\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op met Gauss-Jordan: \(\begin{cases} x + y = 7 \\ x - y = 1 \end{cases}\). Wat is \(x\)?",
        antwoord=["4", "vier"],
        uitleg=r"Rij 2 min rij 1 geeft \(-2y = -6\), dus \(y = 3\) en \(x = 4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een bepaald stelsel heeft precies één oplossing.",
        antwoord=True,
        uitleg=r"Onbepaald: oneindig veel oplossingen. Strijdig: geen oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bakker maakt broden (\(x\)) en taarten (\(y\)). Hij heeft \(30\) kg bloem en \(10\) uur. Een brood vraagt \(0{,}5\) kg en \(0{,}1\) uur, een taart \(1\) kg en \(0{,}5\) uur. Welk stelsel hoort erbij als hij alles opgebruikt?",
        opties=[
            r"\(\begin{cases} 0{,}5x + y = 30 \\ 0{,}1x + 0{,}5y = 10 \end{cases}\)",
            r"\(\begin{cases} 0{,}5x + 0{,}1y = 30 \\ x + 0{,}5y = 10 \end{cases}\)",
            r"\(\begin{cases} x + y = 30 \\ x + y = 10 \end{cases}\)",
            r"\(\begin{cases} 0{,}5x + y = 10 \\ 0{,}1x + 0{,}5y = 30 \end{cases}\)",
        ],
        antwoord=0,
        uitleg=r"Eén vergelijking voor de bloem en één voor de tijd.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In de evenwichtstoestand van een migratiematrix verhuist niemand meer.",
        antwoord=False,
        uitleg=r"Mensen blijven verhuizen, maar er gaan evenveel in als uit elke toestand: de aantallen veranderen niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is een matrix in rijcanonieke vorm?",
        opties=[
            r"elke leidende coëfficiënt is \(1\), met nullen erboven en eronder, en de leidende enen schuiven naar rechts op",
            r"alle elementen zijn \(0\) of \(1\)",
            r"de matrix is vierkant",
            r"de laatste kolom bevat enkel nullen",
        ],
        antwoord=0,
        uitleg=r"Dat is het eindpunt van Gauss-Jordan: je leest de oplossing zo af.",
    ),
]
