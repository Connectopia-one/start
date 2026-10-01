# -*- coding: utf-8 -*-
"""Algebraïsche structuren: de groep.

Het derde stuk van het onderdeel "Algebra" van fiche G3. De fiche spreekt
enkel over groepen en commutatieve groepen, niet over ringen of velden, dus
daar gaat dit thema ook over. Het sluit aan bij de matrices: de verzameling
matrices met de optelling is zelf een commutatieve groep.

Deel 1 is wat een groep is: de vier eigenschappen, met voorbeelden en
tegenvoorbeelden uit de getallenverzamelingen.
Deel 2 is de Cayley-tabel, de uniciteit van het neutraal en het invers
element, en rekenen binnen een groep.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer heet een bewerking op een verzameling intern?",
        opties=[
            "als het resultaat altijd weer in die verzameling ligt",
            "als het resultaat van de bewerking altijd een positief getal oplevert",
            "als de volgorde van de twee elementen geen verschil maakt voor het resultaat",
            "als je de bewerking op drie elementen na elkaar mag toepassen",
        ],
        antwoord=0,
        uitleg="Je blijft binnen de verzameling. De optelling is intern in de gehele getallen, de deling niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Aan hoeveel eigenschappen moet een verzameling met een bewerking voldoen om een groep te zijn?",
        opties=[
            "vier",
            "twee, en soms ook een derde erbij",
            "drie, waarvan er één facultatief is",
            "vijf, de commutativiteit meegerekend",
        ],
        antwoord=0,
        uitleg="Intern, associatief, een neutraal element, en voor elk element een invers element.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel neutrale elementen heeft een groep? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Juist één. Dat heet de uniciteit van het neutraal element, en het is te bewijzen.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke groep is commutatief.",
        antwoord=False,
        uitleg="Bij een commutatieve groep komt de commutativiteit als vijfde eigenschap erbij. De vermenigvuldiging van matrices is bijvoorbeeld niet commutatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een bewerking associatief is?",
        opties=[
            "de haakjes mogen verschuiven zonder dat het resultaat verandert",
            "de twee elementen mogen van plaats wisselen zonder gevolg",
            "er bestaat een element dat niets verandert aan de uitkomst",
            "elk element heeft een partner die het neutraal element oplevert",
        ],
        antwoord=0,
        uitleg="a bewerkt met (b bewerkt met c) geeft hetzelfde als (a bewerkt met b) bewerkt met c.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het neutraal element van een bewerking?",
        opties=[
            "het element dat elk ander element ongewijzigd laat",
            "het element dat elk ander element naar nul herleidt",
            "het element dat het kleinste is van de hele verzameling",
            "het element dat samen met zichzelf opnieuw zichzelf geeft",
        ],
        antwoord=0,
        uitleg="Bij de optelling is dat nul, bij de vermenigvuldiging één.",
    ),
    dict(
        type="waarofniet",
        vraag="De gehele getallen vormen met de optelling een groep.",
        antwoord=True,
        uitleg="De optelling is intern en associatief, nul is het neutraal element en elk geheel getal heeft zijn tegengestelde erbij.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het neutraal element voor de optelling van gehele getallen? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Een getal plus nul blijft dat getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vormen de gehele getallen met de vermenigvuldiging geen groep?",
        opties=[
            "de meeste getallen hebben geen invers element in die verzameling",
            "de vermenigvuldiging van gehele getallen is niet associatief",
            "er is geen neutraal element voor de vermenigvuldiging te vinden",
            "het product van twee gehele getallen is niet altijd een geheel getal",
        ],
        antwoord=0,
        uitleg="Het invers van drie zou een derde zijn, en dat is geen geheel getal. Alleen één en min één hebben er een.",
    ),
    dict(
        type="waarofniet",
        vraag="De natuurlijke getallen vormen met de optelling een groep.",
        antwoord=False,
        uitleg="Er zijn geen negatieve getallen, dus drie heeft geen tegengestelde binnen de verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het invers element van a?",
        opties=[
            "het element dat samen met a het neutraal element geeft",
            "het element dat samen met a precies nul oplevert, wat de bewerking ook is",
            "het element dat in de verzameling juist tegenover a staat opgeschreven",
            "het element dat je krijgt door a met min één te vermenigvuldigen",
        ],
        antwoord=0,
        uitleg="Bij de optelling is dat het tegengestelde, bij de vermenigvuldiging het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het neutraal element voor de vermenigvuldiging van reële getallen? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Een getal maal één blijft dat getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heet een groep commutatief?",
        opties=[
            "als de volgorde van de twee elementen niets uitmaakt",
            "als de verzameling maar eindig veel elementen bevat",
            "als elk element zijn eigen invers element is geworden",
            "als het neutraal element vooraan in de tabel staat",
        ],
        antwoord=0,
        uitleg="a bewerkt met b geeft dan hetzelfde als b bewerkt met a. Je ziet het aan de symmetrie van de Cayley-tabel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groep heeft altijd eindig veel elementen.",
        antwoord=False,
        uitleg="De gehele getallen met de optelling vormen een oneindige groep. Eindige en oneindige groepen bestaan allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een eindige groep?",
        opties=[
            "een groep met een eindig aantal elementen",
            "een groep waarin de bewerking na een tijd stopt te werken",
            "een groep waarvan je alle inversen kan opschrijven in een lijst",
            "een groep waarin elk element zijn eigen invers element is",
        ],
        antwoord=0,
        uitleg="Alleen van een eindige groep kan je de volledige Cayley-tabel opstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verzameling vormt met de vermenigvuldiging wél een groep?",
        opties=[
            "de reële getallen zonder nul",
            "de reële getallen, nul inbegrepen in de verzameling",
            "de gehele getallen zonder nul en zonder de negatieve",
            "de natuurlijke getallen vanaf één opwaarts geteld",
        ],
        antwoord=0,
        uitleg="Nul moet eruit, want nul heeft geen omgekeerde. Alle andere reële getallen hebben er wel een.",
    ),
    dict(
        type="waarofniet",
        vraag="Nul heeft geen invers element voor de vermenigvuldiging.",
        antwoord=True,
        uitleg="Er bestaat geen getal dat maal nul één geeft, want nul maal om het even wat blijft nul.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het invers element van zeven voor de optelling van gehele getallen? Schrijf het getal.",
        antwoord=["-7", "min 7", "min zeven"],
        uitleg="Zeven plus min zeven geeft nul, en nul is daar het neutraal element.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe toon je aan dat een verzameling met een bewerking een groep is?",
        opties=[
            "je gaat de vier eigenschappen één voor één na",
            "je zoekt één voorbeeld waarbij de bewerking goed uitkomt",
            "je stelt de Cayley-tabel op, want dat volstaat altijd",
            "je toont aan dat de bewerking commutatief is",
        ],
        antwoord=0,
        uitleg="Eén tegenvoorbeeld bij één eigenschap is genoeg om te besluiten dat het geen groep is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vormen de matrices van orde twee een groep onder de optelling?",
        opties=[
            "ja, en ze is bovendien commutatief",
            "ja, maar ze is niet commutatief",
            "nee, want er is geen neutraal element",
            "nee, want niet elke matrix heeft een tegengestelde",
        ],
        antwoord=0,
        uitleg="De nulmatrix is het neutraal element en elke matrix heeft haar tegengestelde. Bij de vermenigvuldiging lukt het niet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er in een Cayley-tabel?",
        opties=[
            "het resultaat van de bewerking voor elk paar elementen",
            "de inversen van alle elementen, netjes onder elkaar gezet",
            "de volgorde waarin je de elementen moet opschrijven",
            "het aantal keer dat elk element in de groep voorkomt",
        ],
        antwoord=0,
        uitleg="Rij voor het eerste element, kolom voor het tweede, en in het vakje het resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zie je aan een Cayley-tabel dat de groep commutatief is?",
        opties=[
            "de tabel is symmetrisch om de hoofddiagonaal",
            "de hoofddiagonaal bevat enkel het neutraal element",
            "de eerste rij is precies gelijk aan de eerste kolom",
            "elk element komt in de tabel even vaak voor als de andere",
        ],
        antwoord=0,
        uitleg="Spiegel je de tabel om de diagonaal van linksboven naar rechtsonder, dan verandert er niets.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel inverse elementen heeft één element van een groep? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Juist één, en ook dat is te bewijzen. Het heet de uniciteit van het invers element.",
    ),
    dict(
        type="waarofniet",
        vraag="Het neutraal element van een groep is uniek.",
        antwoord=True,
        uitleg="Stel dat er twee zijn: bewerk ze met elkaar en je toont aan dat ze gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe herken je het neutraal element in een Cayley-tabel?",
        opties=[
            "zijn rij en zijn kolom herhalen gewoon de kopregel",
            "zijn rij en zijn kolom bevatten overal hetzelfde element",
            "het staat altijd helemaal linksboven in de tabel",
            "zijn rij bevat alleen vakjes met zichzelf erin",
        ],
        antwoord=0,
        uitleg="Het verandert niets, dus de rij is een kopie van de kopregel boven de tabel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het invers element van a in een Cayley-tabel?",
        opties=[
            "je zoekt in de rij van a waar het neutraal element staat",
            "je zoekt in de rij van a waar a zelf opnieuw verschijnt",
            "je kijkt welk element recht tegenover a in de kopregel staat",
            "je kijkt op de hoofddiagonaal in het vakje van a",
        ],
        antwoord=0,
        uitleg="De kolom waarin dat vakje staat, wijst het invers element aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Het invers element van a bewerkt met b is het invers van a bewerkt met het invers van b, in die volgorde.",
        antwoord=False,
        uitleg="De volgorde keert om: eerst het invers van b, dan dat van a. Bij een commutatieve groep maakt dat niets uit.",
    ),
    dict(
        type="invultekst",
        vraag="Je neemt het invers element van het invers element van a. Wat krijg je? Schrijf de letter.",
        antwoord=["a"],
        uitleg="Twee keer omkeren brengt je terug bij het begin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe los je in een groep de vergelijking a bewerkt met x is gelijk aan b op?",
        opties=[
            "je bewerkt links met het invers element van a",
            "je bewerkt rechts met het invers element van a",
            "je deelt beide leden door het element a",
            "je bewerkt beide leden met het neutraal element",
        ],
        antwoord=0,
        uitleg="Links, want a staat links. In een groep die niet commutatief is, is die kant belangrijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In de Cayley-tabel van een groep komt elk element precies één keer voor in elke rij.",
        antwoord=True,
        uitleg="Zou een element twee keer voorkomen, dan had je twee oplossingen voor dezelfde vergelijking, en dat kan niet in een groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bewijs je met de uniciteit van het neutraal element?",
        opties=[
            "dat een groep er maar één kan hebben",
            "dat elke groep er zeker één heeft",
            "dat het neutraal element zijn eigen invers is",
            "dat het neutraal element vooraan hoort te staan",
        ],
        antwoord=0,
        uitleg="Dat er één bestaat, is net een van de vier eigenschappen. Dat het er maar één is, moet je bewijzen.",
    ),
    dict(
        type="invultekst",
        vraag="Een groep telt vijf elementen. Hoeveel vakjes heeft haar Cayley-tabel, de kopregel en de kopkolom niet meegerekend? Schrijf het getal.",
        antwoord=["25", "vijfentwintig"],
        uitleg="Vijf rijen maal vijf kolommen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe begint het bewijs dat het neutraal element uniek is?",
        opties=[
            "je veronderstelt dat er twee neutrale elementen zijn",
            "je veronderstelt dat er geen enkel neutraal element bestaat",
            "je stelt de volledige Cayley-tabel van de groep op",
            "je zoekt een voorbeeld van een groep met twee neutrale elementen",
        ],
        antwoord=0,
        uitleg="Daarna bewerk je ze met elkaar en toont elk van de twee aan dat het resultaat de andere is.",
    ),
    dict(
        type="waarofniet",
        vraag="In een groep mag je links en rechts van het gelijkheidsteken hetzelfde element wegwerken.",
        antwoord=True,
        uitleg="Je bewerkt beide leden met zijn invers element. Dat is het hele idee achter het oplossen van vergelijkingen in een groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe los je de vergelijking x bewerkt met a is gelijk aan b op?",
        opties=[
            "je bewerkt rechts met het invers element van a",
            "je bewerkt links met het invers element van a",
            "je bewerkt beide leden met het element a zelf",
            "je bewerkt rechts met het neutraal element van de groep",
        ],
        antwoord=0,
        uitleg="Nu staat a rechts, dus bewerk je ook rechts. Vergelijk met de vorige vergelijking: de kant volgt a.",
    ),
    dict(
        type="meerkeuze",
        vraag="Elk element van een groep is zijn eigen invers. Wat zie je dan op de hoofddiagonaal van de tabel?",
        opties=[
            "overal het neutraal element",
            "overal het element van die rij zelf",
            "overal verschillende elementen na elkaar",
            "overal het eerste element van de kopregel",
        ],
        antwoord=0,
        uitleg="Op de diagonaal staat elk element met zichzelf bewerkt, en dat geeft dan telkens het neutraal element.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan ook van een oneindige groep de volledige Cayley-tabel opstellen.",
        antwoord=False,
        uitleg="Die tabel zou oneindig veel rijen en kolommen hebben. De tabel werkt alleen bij eindige groepen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel rijen telt de Cayley-tabel van een groep met zes elementen, de kopregel niet meegerekend? Schrijf het cijfer.",
        antwoord=["6", "zes"],
        uitleg="Eén rij per element.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom keert de volgorde om in het invers element van een product?",
        opties=[
            "omdat je het binnenste paar eerst moet kunnen wegwerken",
            "omdat de bewerking in een groep nooit commutatief mag zijn",
            "omdat het neutraal element anders aan de verkeerde kant staat",
            "omdat je anders twee verschillende inversen zou uitkomen",
        ],
        antwoord=0,
        uitleg="Zet je ze in de omgekeerde volgorde naast elkaar, dan valt eerst b weg en pas daarna a.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vier draaiingen die een vierkant op zichzelf afbeelden, met na elkaar uitvoeren als bewerking. Wat is dat?",
        opties=[
            "een eindige commutatieve groep",
            "een oneindige commutatieve groep van draaiingen",
            "een groep zonder neutraal element erin",
            "geen groep, want draaien is niet associatief",
        ],
        antwoord=0,
        uitleg="Vier elementen, de draaiing over nul graden is het neutraal element en elke draaiing heeft haar tegendraaiing.",
    ),
]
