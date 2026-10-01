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
        vraag="Wat betekent het dat een matrix de dimensie drie bij vier heeft?",
        opties=[
            "ze heeft drie rijen en vier kolommen",
            "ze heeft vier rijen en drie kolommen",
            "ze heeft drie elementen op elke diagonaal",
            "ze bevat twaalf rijen en vier kolommen",
        ],
        antwoord=0,
        uitleg="Eerst het aantal rijen, dan het aantal kolommen. Die volgorde omdraaien is de meest gemaakte fout van het hoofdstuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kan je twee matrices bij elkaar optellen?",
        opties=[
            "als ze precies dezelfde dimensie hebben",
            "als ze allebei vierkant zijn",
            "als het aantal kolommen van de ene gelijk is aan het aantal rijen van de andere",
            "altijd, want je telt gewoon alle elementen op",
        ],
        antwoord=0,
        uitleg="Je telt element per element op, dus elk element moet een partner hebben. Het derde antwoord is de voorwaarde om te vermenigvuldigen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel elementen heeft een matrix van twee bij vijf? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg="Twee rijen van vijf elementen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het vermenigvuldigen van matrices is commutatief.",
        antwoord=False,
        uitleg="A maal B is in het algemeen iets anders dan B maal A, en soms bestaat maar één van de twee. Dat is het grote verschil met gewone getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kan je het product A maal B berekenen?",
        opties=[
            "als het aantal kolommen van A gelijk is aan het aantal rijen van B",
            "als het aantal rijen van A gelijk is aan het aantal kolommen van B",
            "als A en B allebei exact dezelfde dimensie hebben",
            "als A en B allebei vierkante matrices zijn van gelijke orde",
        ],
        antwoord=0,
        uitleg="Elk element van het product is een rij van A tegen een kolom van B, en die twee moeten even lang zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dimensie heeft het product van een matrix twee bij drie met een matrix drie bij vier?",
        opties=["twee bij vier", "drie bij drie", "vier bij twee", "twee bij drie"],
        antwoord=0,
        uitleg="De binnenste getallen moeten gelijk zijn en vallen weg; de buitenste blijven over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vermenigvuldiging met een reëel getal vermenigvuldig je elk element van de matrix met dat getal.",
        antwoord=True,
        uitleg="Dat heet de scalaire vermenigvuldiging, en ze is iets heel anders dan het product van twee matrices.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel enen staan er in de eenheidsmatrix van orde drie? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Eén op elke plaats van de hoofddiagonaal, en overal elders een nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als je een matrix transponeert?",
        opties=[
            "de rijen worden kolommen en de kolommen worden rijen",
            "alle elementen van de matrix wisselen van teken",
            "de matrix wordt met zichzelf vermenigvuldigd, element per element",
            "de volgorde van de rijen wordt omgekeerd",
        ],
        antwoord=0,
        uitleg="Een matrix van twee bij vijf wordt na transponeren een matrix van vijf bij twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een symmetrische matrix is gelijk aan haar getransponeerde.",
        antwoord=True,
        uitleg="Ze is dan noodzakelijk vierkant, en het spiegelbeeld in de hoofddiagonaal valt op zichzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het neutraal element voor de vermenigvuldiging van vierkante matrices?",
        opties=[
            "de eenheidsmatrix",
            "de nulmatrix",
            "de getransponeerde matrix",
            "de diagonaalmatrix met allemaal tweeën",
        ],
        antwoord=0,
        uitleg="Vermenigvuldigen met de eenheidsmatrix verandert niets, net zoals vermenigvuldigen met één bij gewone getallen.",
    ),
    dict(
        type="invultekst",
        vraag="Je transponeert een matrix van twee bij vijf. Hoeveel rijen heeft het resultaat? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg="De vijf kolommen worden vijf rijen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een diagonaalmatrix?",
        opties=[
            "een vierkante matrix waarin alles buiten de hoofddiagonaal nul is",
            "een matrix waarvan alle elementen op eenzelfde rij aan elkaar gelijk zijn",
            "een matrix die je bekomt door een andere te transponeren",
            "een matrix met evenveel rijen als kolommen en overal enen",
        ],
        antwoord=0,
        uitleg="De eenheidsmatrix is er een bijzonder geval van: daar staan op de diagonaal allemaal enen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als het product van twee matrices de nulmatrix is, dan is minstens één van beide de nulmatrix.",
        antwoord=False,
        uitleg="Bij matrices bestaan er nuldelers: twee matrices die geen van beide nul zijn, kunnen samen toch nul geven. Bij reële getallen kan dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuur vormen de matrices van een vaste dimensie met de optelling?",
        opties=[
            "een commutatieve groep",
            "een groep die niet commutatief is",
            "geen groep, want er is geen neutraal element",
            "geen groep, want de optelling is niet intern",
        ],
        antwoord=0,
        uitleg="De nulmatrix is het neutraal element, en de tegengestelde matrix is het symmetrisch element. De optelling is bovendien commutatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is de getransponeerde van een product A maal B gelijk?",
        opties=[
            "de getransponeerde van B maal de getransponeerde van A",
            "de getransponeerde van A maal de getransponeerde van B",
            "het product A maal B, want transponeren verandert niets",
            "de som van de twee getransponeerde matrices",
        ],
        antwoord=0,
        uitleg="De volgorde draait om. Dat moet ook wel, anders zouden de dimensies niet meer passen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vierkante matrix heeft evenveel rijen als kolommen.",
        antwoord=True,
        uitleg="Alleen vierkante matrices kunnen een determinant of een inverse hebben.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel rijen heeft een kolommatrix met vier elementen? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg="Een kolommatrix heeft één kolom, dus vier elementen betekent vier rijen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel zet de bestelde aantallen in één matrix en de eenheidsprijzen in een andere. Wat levert hun product op?",
        opties=[
            "de totale prijs per bestelling",
            "de prijs per stuk van elk artikel",
            "het aantal artikelen per bestelling",
            "het verschil tussen prijs en aantal",
        ],
        antwoord=0,
        uitleg="Elk element van het product is een rij aantallen tegen een kolom prijzen, dus precies een totaalbedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nulmatrix?",
        opties=[
            "een matrix waarin elk element nul is",
            "een matrix met determinant gelijk aan nul",
            "een matrix zonder rijen en zonder kolommen",
            "een matrix met nullen op de hoofddiagonaal",
        ],
        antwoord=0,
        uitleg="Een matrix met determinant nul is iets anders: die heet een niet-inverteerbare of singuliere matrix.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de determinant van een matrix van orde twee?",
        opties=[
            "het product van de hoofddiagonaal min het product van de andere diagonaal",
            "het product van de hoofddiagonaal plus het product van de andere diagonaal",
            "de som van alle vier de elementen van die matrix",
            "het product van alle vier de elementen van die matrix",
        ],
        antwoord=0,
        uitleg="Linksboven maal rechtsonder, min rechtsboven maal linksonder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een matrix heeft op de eerste rij één en twee, en op de tweede rij drie en vier. Wat is haar determinant?",
        opties=["min twee", "twee", "min tien", "tien"],
        antwoord=0,
        uitleg="Vier min zes is min twee. De determinant is niet nul, dus de matrix is inverteerbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de determinant van de eenheidsmatrix? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="Enkel het product van de hoofddiagonaal blijft over, en dat is één maal één maal één.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vierkante matrix is inverteerbaar als haar determinant verschillend is van nul.",
        antwoord=True,
        uitleg="Determinant nul betekent dat rijen van elkaar afhangen, en dan kan je de bewerking niet ongedaan maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de minor van een element in een matrix?",
        opties=[
            "de determinant die overblijft als je zijn rij en kolom schrapt",
            "het kleinste element dat in diezelfde rij staat",
            "het element zelf, maar dan voorzien van het tegengestelde teken",
            "de som van de elementen rondom dat element heen",
        ],
        antwoord=0,
        uitleg="Bij een matrix van orde drie blijft er zo telkens een determinant van orde twee over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een minor en een cofactor?",
        opties=[
            "een cofactor is de minor met een teken dat van de plaats afhangt",
            "een cofactor is de minor vermenigvuldigd met het element zelf",
            "een cofactor is de minor van de getransponeerde matrix",
            "er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Het teken wisselt af als een schaakbord, te beginnen met plus linksboven.",
    ),
    dict(
        type="waarofniet",
        vraag="Alleen vierkante matrices hebben een determinant.",
        antwoord=True,
        uitleg="Bij een rechthoekige matrix is ze niet gedefinieerd. De rang kan je er wel van bepalen.",
    ),
    dict(
        type="invultekst",
        vraag="Een matrix heeft twee volledig gelijke rijen. Wat is haar determinant? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="De rijen hangen van elkaar af, dus de matrix is niet inverteerbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je een determinant van orde drie met de hand?",
        opties=[
            "ontwikkelen naar een rij of een kolom, met minoren en cofactoren",
            "de zes elementen van de twee diagonalen bij elkaar optellen",
            "de matrix eerst transponeren en dan de diagonaal nemen",
            "de drie rijen apart optellen en die sommen vermenigvuldigen",
        ],
        antwoord=0,
        uitleg="Kies een rij of kolom met veel nullen, dan valt er het meeste rekenwerk weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een matrix met determinant nul heeft toch een inverse.",
        antwoord=False,
        uitleg="Net niet. Determinant nul en niet-inverteerbaar zijn twee manieren om hetzelfde te zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rang van een matrix?",
        opties=[
            "het aantal rijen dat niet nul is in haar rijcanonieke vorm",
            "het aantal rijen dat de matrix alles bij elkaar heeft",
            "het grootste element dat in de matrix voorkomt",
            "het aantal nullen dat in de matrix staat",
        ],
        antwoord=0,
        uitleg="De rang zegt hoeveel rijen echt nieuwe informatie geven.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de rang van de eenheidsmatrix van orde drie? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Ze staat al in rijcanonieke vorm en heeft drie rijen die niet nul zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de rang en de inverteerbaarheid van een vierkante matrix van orde n?",
        opties=[
            "ze is inverteerbaar als haar rang gelijk is aan n",
            "ze is inverteerbaar als haar rang kleiner is dan n",
            "ze is inverteerbaar als haar rang gelijk is aan nul",
            "de rang zegt niets over de inverteerbaarheid ervan",
        ],
        antwoord=0,
        uitleg="Volle rang, determinant verschillend van nul en inverteerbaar zijn drie manieren om hetzelfde te zeggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een matrix heeft maar één rijcanonieke vorm.",
        antwoord=True,
        uitleg="Welke rijoperaties je ook kiest, je komt altijd bij dezelfde vorm uit. Daarom is de rang eenduidig bepaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat krijg je als je een matrix met haar inverse vermenigvuldigt?",
        opties=[
            "de eenheidsmatrix",
            "de nulmatrix",
            "de oorspronkelijke matrix",
            "de getransponeerde matrix",
        ],
        antwoord=0,
        uitleg="Dat is net de definitie van een inverse, en het werkt in beide volgordes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijoperaties mag je uitvoeren bij het omvormen naar de rijcanonieke vorm?",
        opties=[
            "rijen verwisselen, een rij maal een getal, of een veelvoud van een rij bij een andere tellen",
            "twee kolommen verwisselen en daarna ook de rijen opnieuw van boven naar onder rangschikken",
            "een rij door een andere rij delen, element per element",
            "elke rij vervangen door haar getransponeerde kolom",
        ],
        antwoord=0,
        uitleg="Die drie elementaire rijoperaties veranderen de rang niet en houden een stelsel gelijkwaardig. Vermenigvuldigen met nul mag niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechthoekige matrix kan ook een inverse hebben.",
        antwoord=False,
        uitleg="Alleen vierkante matrices met determinant verschillend van nul hebben er een.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de rang van de nulmatrix? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Er is geen enkele rij die niet nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat je bij de inverse van een matrix van orde drie aan de rekenapp over?",
        opties=[
            "het rekenwerk, maar je controleert het resultaat met de eenheidsmatrix",
            "de hele opgave, met inbegrip van de vraag of er wel een inverse bestaat",
            "niets, want een inverse moet je altijd met de hand berekenen",
            "enkel de determinant, de inverse zelf bereken je zelf",
        ],
        antwoord=0,
        uitleg="Het product met de oorspronkelijke matrix moet de eenheidsmatrix geven. Die controle kost één bewerking en vangt elke tikfout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de determinant een nuttig getal?",
        opties=[
            "omdat je er in één berekening mee ziet of een matrix inverteerbaar is",
            "omdat ze het grootste element van de matrix aanwijst",
            "omdat ze altijd gelijk is aan de rang van de matrix",
            "omdat ze het juiste aantal oplossingen van om het even welk stelsel geeft",
        ],
        antwoord=0,
        uitleg="En daarmee ook of een stelsel met die coëfficiëntenmatrix precies één oplossing heeft.",
    ),
]
