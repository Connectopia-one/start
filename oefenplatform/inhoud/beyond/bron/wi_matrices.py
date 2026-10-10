# -*- coding: utf-8 -*-
"""Matrices: bewerkingen, determinant, inverse en rang.

Het eerste stuk van het onderdeel "Algebra" van fiche G3, dat samen met de
stelsels en de algebraïsche structuren tweeënveertig procent van dat examen
weegt.

Deel 1 zijn de bewerkingen en de bijzondere matrices.
Deel 2 is de determinant, de inverse matrix en de rang.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het dat een matrix de dimensie \(3 \times 4\) heeft?",
        opties=[
            r"ze heeft \(3\) rijen en \(4\) kolommen",
            r"ze heeft \(4\) rijen en \(3\) kolommen",
            r"ze heeft \(3\) elementen op elke diagonaal",
            r"ze bevat \(12\) rijen en \(4\) kolommen",
        ],
        antwoord=0,
        uitleg=r"Eerst het aantal rijen, dan het aantal kolommen. Die volgorde omdraaien is de meest gemaakte fout van het hoofdstuk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer kan je \(A + B\) berekenen?",
        opties=[
            r"als \(A\) en \(B\) precies dezelfde dimensie hebben",
            r"als \(A\) en \(B\) allebei vierkant zijn",
            r"als het aantal kolommen van \(A\) gelijk is aan het aantal rijen van \(B\)",
            r"altijd, want je telt gewoon alle elementen op",
        ],
        antwoord=0,
        uitleg=r"Je telt element per element op, dus elk element moet een partner hebben. Het derde antwoord is de voorwaarde om te vermenigvuldigen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel elementen heeft een matrix van \(2 \times 5\)? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg=r"Twee rijen van vijf elementen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor matrices geldt altijd \(A \cdot B = B \cdot A\).",
        antwoord=False,
        uitleg=r"\(A \cdot B\) is in het algemeen iets anders dan \(B \cdot A\), en soms bestaat maar één van de twee. Dat is het grote verschil met gewone getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer kan je het product \(A \cdot B\) berekenen?",
        opties=[
            r"als het aantal kolommen van \(A\) gelijk is aan het aantal rijen van \(B\)",
            r"als het aantal rijen van \(A\) gelijk is aan het aantal kolommen van \(B\)",
            r"als \(A\) en \(B\) allebei exact dezelfde dimensie hebben",
            r"als \(A\) en \(B\) allebei vierkante matrices zijn van gelijke orde",
        ],
        antwoord=0,
        uitleg=r"Elk element van het product is een rij van \(A\) tegen een kolom van \(B\), en die twee moeten even lang zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke dimensie heeft het product van een matrix \(2 \times 3\) met een matrix \(3 \times 4\)?",
        opties=[r"\(2 \times 4\)", r"\(3 \times 3\)", r"\(4 \times 2\)", r"\(2 \times 3\)"],
        antwoord=0,
        uitleg=r"De binnenste getallen moeten gelijk zijn en vallen weg; de buitenste blijven over.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(k \cdot A\) met \(k \in \mathbb{R}\) vermenigvuldig je elk element van \(A\) met \(k\).",
        antwoord=True,
        uitleg=r"Dat heet de scalaire vermenigvuldiging, en ze is iets heel anders dan het product van twee matrices.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel enen staan er in de eenheidsmatrix \(I_{3}\)? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Eén op elke plaats van de hoofddiagonaal, en overal elders een nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er als je een matrix transponeert tot \(A^{T}\)?",
        opties=[
            r"de rijen worden kolommen en de kolommen worden rijen",
            r"alle elementen van de matrix wisselen van teken",
            r"de matrix wordt met zichzelf vermenigvuldigd, element per element",
            r"de volgorde van de rijen wordt omgekeerd",
        ],
        antwoord=0,
        uitleg=r"Een matrix van \(2 \times 5\) wordt na transponeren een matrix van \(5 \times 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een symmetrische matrix voldoet aan \(A = A^{T}\).",
        antwoord=True,
        uitleg=r"Ze is dan noodzakelijk vierkant, en het spiegelbeeld in de hoofddiagonaal valt op zichzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het neutraal element voor de vermenigvuldiging van vierkante matrices?",
        opties=[
            r"de eenheidsmatrix \(I\)",
            r"de nulmatrix \(O\)",
            r"de getransponeerde matrix \(A^{T}\)",
            r"de diagonaalmatrix met overal \(2\)",
        ],
        antwoord=0,
        uitleg=r"Er geldt \(A \cdot I = I \cdot A = A\), net zoals vermenigvuldigen met \(1\) bij gewone getallen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je transponeert een matrix van \(2 \times 5\). Hoeveel rijen heeft \(A^{T}\)? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg=r"De vijf kolommen worden vijf rijen, dus \(A^{T}\) is \(5 \times 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een diagonaalmatrix?",
        opties=[
            r"een vierkante matrix waarin alles buiten de hoofddiagonaal nul is",
            r"een matrix waarvan alle elementen op eenzelfde rij aan elkaar gelijk zijn",
            r"een matrix die je bekomt door een andere te transponeren",
            r"een matrix met evenveel rijen als kolommen en overal enen",
        ],
        antwoord=0,
        uitleg=r"\(I_{3} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\) is er een bijzonder geval van.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(A \cdot B = O\), dan is \(A = O\) of \(B = O\).",
        antwoord=False,
        uitleg=r"Bij matrices bestaan er nuldelers: \(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = O\), en geen van beide is de nulmatrix.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke structuur vormen de matrices van een vaste dimensie met de optelling?",
        opties=[
            r"een commutatieve groep",
            r"een groep die niet commutatief is",
            r"geen groep, want er is geen neutraal element",
            r"geen groep, want de optelling is niet intern",
        ],
        antwoord=0,
        uitleg=r"\(O\) is het neutraal element, \(-A\) het symmetrisch element, en \(A + B = B + A\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waaraan is \((A \cdot B)^{T}\) gelijk?",
        opties=[
            r"\(B^{T} \cdot A^{T}\)",
            r"\(A^{T} \cdot B^{T}\)",
            r"\(A \cdot B\)",
            r"\(A^{T} + B^{T}\)",
        ],
        antwoord=0,
        uitleg=r"De volgorde draait om. Dat moet ook wel, anders zouden de dimensies niet meer passen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vierkante matrix heeft evenveel rijen als kolommen.",
        antwoord=True,
        uitleg=r"Alleen vierkante matrices kunnen een determinant of een inverse hebben.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel rijen heeft een kolommatrix met \(4\) elementen? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg=r"Een kolommatrix heeft één kolom, dus vier elementen betekent dimensie \(4 \times 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een winkel zet de bestelde aantallen in een matrix \(A\) en de eenheidsprijzen in een kolommatrix \(P\). Wat levert \(A \cdot P\) op?",
        opties=[
            r"de totale prijs per bestelling",
            r"de prijs per stuk van elk artikel",
            r"het aantal artikelen per bestelling",
            r"het verschil tussen prijs en aantal",
        ],
        antwoord=0,
        uitleg=r"Elk element van het product is een rij aantallen tegen de kolom prijzen, dus precies een totaalbedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de nulmatrix \(O\)?",
        opties=[
            r"een matrix waarin elk element nul is",
            r"een matrix met \(\det A = 0\)",
            r"een matrix zonder rijen en zonder kolommen",
            r"een matrix met nullen op de hoofddiagonaal",
        ],
        antwoord=0,
        uitleg=r"Een matrix met \(\det A = 0\) is iets anders: die heet een niet-inverteerbare of singuliere matrix.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je \(\det\begin{pmatrix} a & b \\ c & d \end{pmatrix}\)?",
        opties=[r"\(ad - bc\)", r"\(ad + bc\)", r"\(a + b + c + d\)", r"\(abcd\)"],
        antwoord=0,
        uitleg=r"Linksboven maal rechtsonder, min rechtsboven maal linksonder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\det\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\).",
        opties=[r"\(-2\)", r"\(2\)", r"\(-10\)", r"\(10\)"],
        antwoord=0,
        uitleg=r"\(1 \cdot 4 - 2 \cdot 3 = -2\). De determinant is niet nul, dus de matrix is inverteerbaar.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\det I_{3}\). Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg=r"Enkel het product van de hoofddiagonaal blijft over: \(1 \cdot 1 \cdot 1 = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vierkante matrix \(A\) is inverteerbaar als \(\det A \neq 0\).",
        antwoord=True,
        uitleg=r"\(\det A = 0\) betekent dat rijen van elkaar afhangen, en dan kan je de bewerking niet ongedaan maken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de minor \(M_{ij}\) van een element?",
        opties=[
            r"de determinant die overblijft als je rij \(i\) en kolom \(j\) schrapt",
            r"het kleinste element dat in diezelfde rij staat",
            r"het element zelf, maar dan met het tegengestelde teken",
            r"de som van de elementen rondom dat element heen",
        ],
        antwoord=0,
        uitleg=r"Bij een matrix van orde \(3\) blijft er zo telkens een determinant van orde \(2\) over.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verband tussen de minor \(M_{ij}\) en de cofactor \(C_{ij}\)?",
        opties=[
            r"\(C_{ij} = (-1)^{\,i+j} \cdot M_{ij}\)",
            r"\(C_{ij} = a_{ij} \cdot M_{ij}\)",
            r"\(C_{ij} = M_{ji}\)",
            r"\(C_{ij} = M_{ij}\), het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg=r"Het teken wisselt af als een schaakbord, te beginnen met plus linksboven.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Alleen vierkante matrices hebben een determinant.",
        antwoord=True,
        uitleg=r"Bij een rechthoekige matrix is \(\det A\) niet gedefinieerd. De rang kan je er wel van bepalen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een matrix heeft twee volledig gelijke rijen. Bereken \(\det A\). Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"De rijen hangen van elkaar af, dus de matrix is niet inverteerbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je een determinant van orde \(3\) met de hand?",
        opties=[
            r"ontwikkelen naar een rij of een kolom, met minoren en cofactoren",
            r"de zes elementen van de twee diagonalen bij elkaar optellen",
            r"de matrix eerst transponeren en dan de diagonaal nemen",
            r"de drie rijen apart optellen en die sommen vermenigvuldigen",
        ],
        antwoord=0,
        uitleg=r"Kies een rij of kolom met veel nullen, dan valt er het meeste rekenwerk weg.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een matrix met \(\det A = 0\) heeft toch een inverse.",
        antwoord=False,
        uitleg=r"Net niet. \(\det A = 0\) en niet-inverteerbaar zijn twee manieren om hetzelfde te zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de rang \(\text{rang}(A)\) van een matrix?",
        opties=[
            r"het aantal rijen dat niet nul is in haar rijcanonieke vorm",
            r"het aantal rijen dat de matrix alles bij elkaar heeft",
            r"het grootste element dat in de matrix voorkomt",
            r"het aantal nullen dat in de matrix staat",
        ],
        antwoord=0,
        uitleg=r"De rang zegt hoeveel rijen echt nieuwe informatie geven.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\text{rang}(I_{3})\). Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Ze staat al in rijcanonieke vorm en heeft drie rijen die niet nul zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verband tussen de rang en de inverteerbaarheid van een vierkante matrix van orde \(n\)?",
        opties=[
            r"ze is inverteerbaar als \(\text{rang}(A) = n\)",
            r"ze is inverteerbaar als \(\text{rang}(A) < n\)",
            r"ze is inverteerbaar als \(\text{rang}(A) = 0\)",
            r"de rang zegt niets over de inverteerbaarheid ervan",
        ],
        antwoord=0,
        uitleg=r"Volle rang, \(\det A \neq 0\) en inverteerbaar zijn drie manieren om hetzelfde te zeggen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een matrix heeft maar één rijcanonieke vorm.",
        antwoord=True,
        uitleg=r"Welke rijoperaties je ook kiest, je komt altijd bij dezelfde vorm uit. Daarom is de rang eenduidig bepaald.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat krijg je als je \(A \cdot A^{-1}\) berekent?",
        opties=[
            r"de eenheidsmatrix \(I\)",
            r"de nulmatrix \(O\)",
            r"de oorspronkelijke matrix \(A\)",
            r"de getransponeerde matrix \(A^{T}\)",
        ],
        antwoord=0,
        uitleg=r"Dat is net de definitie: \(A \cdot A^{-1} = A^{-1} \cdot A = I\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rijoperaties mag je uitvoeren bij het omvormen naar de rijcanonieke vorm?",
        opties=[
            r"rijen verwisselen, \(R_{i} \to k \cdot R_{i}\) met \(k \neq 0\), of \(R_{i} \to R_{i} + k \cdot R_{j}\)",
            r"twee kolommen verwisselen en daarna de rijen opnieuw rangschikken",
            r"een rij door een andere rij delen, element per element",
            r"elke rij vervangen door haar getransponeerde kolom",
        ],
        antwoord=0,
        uitleg=r"Die drie elementaire rijoperaties veranderen de rang niet en houden een stelsel gelijkwaardig. Vermenigvuldigen met \(0\) mag niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rechthoekige matrix kan ook een inverse hebben.",
        antwoord=False,
        uitleg=r"Alleen vierkante matrices met \(\det A \neq 0\) hebben er een.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\text{rang}(O)\) van de nulmatrix. Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Er is geen enkele rij die niet nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat laat je bij \(A^{-1}\) van een matrix van orde \(3\) aan de rekenapp over?",
        opties=[
            r"het rekenwerk, maar je controleert met \(A \cdot A^{-1} = I\)",
            r"de hele opgave, ook de vraag of er wel een inverse bestaat",
            r"niets, want een inverse moet je altijd met de hand berekenen",
            r"enkel \(\det A\), de inverse zelf bereken je zelf",
        ],
        antwoord=0,
        uitleg=r"Die controle kost één bewerking en vangt elke tikfout.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom is \(\det A\) een nuttig getal?",
        opties=[
            r"omdat je er in één berekening mee ziet of \(A\) inverteerbaar is",
            r"omdat ze het grootste element van de matrix aanwijst",
            r"omdat ze altijd gelijk is aan de rang van de matrix",
            r"omdat ze het aantal oplossingen van om het even welk stelsel geeft",
        ],
        antwoord=0,
        uitleg=r"En daarmee ook of een stelsel met die coëfficiëntenmatrix precies één oplossing heeft.",
    ),
]
