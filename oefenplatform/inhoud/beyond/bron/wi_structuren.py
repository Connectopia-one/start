# -*- coding: utf-8 -*-
"""Algebraïsche structuren: de groep.

Het derde stuk van het onderdeel "Algebra" van fiche G3. De fiche spreekt
enkel over groepen en commutatieve groepen, niet over ringen of velden, dus
daar gaat dit thema ook over. Het sluit aan bij de matrices: de verzameling
matrices met de optelling is zelf een commutatieve groep.

De bewerking schrijven we \\(\\ast\\), het neutraal element \\(e\\) en het invers
element van \\(a\\) schrijven we \\(a^{-1}\\).

Deel 1 is wat een groep is: de vier eigenschappen, met voorbeelden en
tegenvoorbeelden uit de getallenverzamelingen.
Deel 2 is de Cayley-tabel, de uniciteit van het neutraal en het invers
element, en rekenen binnen een groep.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wanneer heet een bewerking \(\ast\) op een verzameling \(G\) intern?",
        opties=[
            r"als \(a \ast b \in G\) voor alle \(a, b \in G\)",
            r"als het resultaat van de bewerking altijd een positief getal oplevert",
            r"als de volgorde van de twee elementen geen verschil maakt voor het resultaat",
            r"als je de bewerking op drie elementen na elkaar mag toepassen",
        ],
        antwoord=0,
        uitleg=r"Je blijft binnen de verzameling. De optelling is intern in \(\mathbb{Z}\), de deling niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Aan hoeveel eigenschappen moet \((G, \ast)\) voldoen om een groep te zijn?",
        opties=[
            r"vier",
            r"twee, en soms ook een derde erbij",
            r"drie, waarvan er één facultatief is",
            r"vijf, de commutativiteit meegerekend",
        ],
        antwoord=0,
        uitleg=r"Intern, associatief, een neutraal element \(e\), en voor elk element een invers element \(a^{-1}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel neutrale elementen heeft een groep? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Juist één. Dat heet de uniciteit van het neutraal element, en het is te bewijzen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke groep is commutatief.",
        antwoord=False,
        uitleg=r"Bij een commutatieve groep komt \(a \ast b = b \ast a\) als vijfde eigenschap erbij. De vermenigvuldiging van matrices voldoet daar niet aan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het dat \(\ast\) associatief is?",
        opties=[
            r"\(a \ast (b \ast c) = (a \ast b) \ast c\)",
            r"\(a \ast b = b \ast a\)",
            r"er bestaat een \(e\) met \(a \ast e = a\)",
            r"elk element \(a\) heeft een \(a^{-1}\) met \(a \ast a^{-1} = e\)",
        ],
        antwoord=0,
        uitleg=r"De haakjes mogen verschuiven zonder dat het resultaat verandert. Daarom mag je \(a \ast b \ast c\) zonder haakjes schrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het neutraal element \(e\) van een bewerking?",
        opties=[
            r"het element waarvoor \(a \ast e = e \ast a = a\) voor elke \(a\)",
            r"het element dat elk ander element naar nul herleidt",
            r"het element dat het kleinste is van de hele verzameling",
            r"het element dat samen met zichzelf opnieuw zichzelf geeft",
        ],
        antwoord=0,
        uitleg=r"Bij de optelling is \(e = 0\), bij de vermenigvuldiging \(e = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\((\mathbb{Z}, +)\) is een groep.",
        antwoord=True,
        uitleg=r"De optelling is intern en associatief, \(e = 0\), en elk geheel getal heeft zijn tegengestelde erbij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het neutraal element van \((\mathbb{Z}, +)\)? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Een getal plus nul blijft dat getal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom is \((\mathbb{Z}, \cdot)\) geen groep?",
        opties=[
            r"de meeste getallen hebben geen invers element in die verzameling",
            r"de vermenigvuldiging van gehele getallen is niet associatief",
            r"er is geen neutraal element voor de vermenigvuldiging te vinden",
            r"het product van twee gehele getallen is niet altijd een geheel getal",
        ],
        antwoord=0,
        uitleg=r"Het invers van \(3\) zou \(\tfrac{1}{3}\) zijn, en dat ligt niet in \(\mathbb{Z}\). Alleen \(1\) en \(-1\) hebben er een.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\((\mathbb{N}, +)\) is een groep.",
        antwoord=False,
        uitleg=r"Er zijn geen negatieve getallen in \(\mathbb{N}\), dus \(3\) heeft geen tegengestelde binnen de verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het invers element \(a^{-1}\) van \(a\)?",
        opties=[
            r"het element waarvoor \(a \ast a^{-1} = a^{-1} \ast a = e\)",
            r"het element dat samen met \(a\) precies nul oplevert, wat de bewerking ook is",
            r"het element dat in de verzameling juist tegenover \(a\) staat opgeschreven",
            r"het element dat je krijgt door \(a\) met \(-1\) te vermenigvuldigen",
        ],
        antwoord=0,
        uitleg=r"Bij de optelling is dat het tegengestelde, bij de vermenigvuldiging het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het neutraal element van \((\mathbb{R}, \cdot)\)? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Een getal maal één blijft dat getal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer heet een groep commutatief?",
        opties=[
            r"als \(a \ast b = b \ast a\) voor alle \(a\) en \(b\)",
            r"als de verzameling maar eindig veel elementen bevat",
            r"als elk element zijn eigen invers element is geworden",
            r"als het neutraal element vooraan in de tabel staat",
        ],
        antwoord=0,
        uitleg=r"De volgorde maakt dan niets uit. Je ziet het aan de symmetrie van de Cayley-tabel.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een groep heeft altijd eindig veel elementen.",
        antwoord=False,
        uitleg=r"\((\mathbb{Z}, +)\) is een oneindige groep. Eindige en oneindige groepen bestaan allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een eindige groep?",
        opties=[
            r"een groep met een eindig aantal elementen",
            r"een groep waarin de bewerking na een tijd stopt te werken",
            r"een groep waarvan je alle inversen kan opschrijven in een lijst",
            r"een groep waarin elk element zijn eigen invers element is",
        ],
        antwoord=0,
        uitleg=r"Alleen van een eindige groep kan je de volledige Cayley-tabel opstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke verzameling vormt met de vermenigvuldiging wél een groep?",
        opties=[
            r"\(\mathbb{R}_{0}\), de reële getallen zonder nul",
            r"\(\mathbb{R}\), met nul erbij",
            r"\(\mathbb{Z}_{0}\), de gehele getallen zonder nul",
            r"\(\mathbb{N}_{0}\), de natuurlijke getallen vanaf één",
        ],
        antwoord=0,
        uitleg=r"Nul moet eruit, want nul heeft geen omgekeerde. Alle andere reële getallen hebben er wel een.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Nul heeft geen invers element voor de vermenigvuldiging.",
        antwoord=True,
        uitleg=r"Er bestaat geen \(x\) met \(0 \cdot x = 1\), want nul maal om het even wat blijft nul.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het invers element van \(7\) in \((\mathbb{Z}, +)\)? Schrijf het getal.",
        antwoord=["-7", "min 7", "min zeven"],
        uitleg=r"\(7 + (-7) = 0\), en \(0\) is daar het neutraal element.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe toon je aan dat \((G, \ast)\) een groep is?",
        opties=[
            r"je gaat de vier eigenschappen één voor één na",
            r"je zoekt één voorbeeld waarbij de bewerking goed uitkomt",
            r"je stelt de Cayley-tabel op, want dat volstaat altijd",
            r"je toont aan dat de bewerking commutatief is",
        ],
        antwoord=0,
        uitleg=r"Eén tegenvoorbeeld bij één eigenschap is genoeg om te besluiten dat het geen groep is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Is de verzameling van de matrices van orde \(2\) met de optelling een groep?",
        opties=[
            r"ja, en ze is bovendien commutatief",
            r"ja, maar ze is niet commutatief",
            r"nee, want er is geen neutraal element",
            r"nee, want niet elke matrix heeft een tegengestelde",
        ],
        antwoord=0,
        uitleg=r"De nulmatrix \(O\) is het neutraal element en elke matrix heeft haar tegengestelde. Bij de vermenigvuldiging lukt het niet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat staat er in een Cayley-tabel?",
        opties=[
            r"het resultaat \(a \ast b\) voor elk paar elementen",
            r"de inversen van alle elementen, netjes onder elkaar gezet",
            r"de volgorde waarin je de elementen moet opschrijven",
            r"het aantal keer dat elk element in de groep voorkomt",
        ],
        antwoord=0,
        uitleg=r"Rij voor \(a\), kolom voor \(b\), en in het vakje het resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe zie je aan een Cayley-tabel dat de groep commutatief is?",
        opties=[
            r"de tabel is symmetrisch om de hoofddiagonaal",
            r"de hoofddiagonaal bevat enkel \(e\)",
            r"de eerste rij is precies gelijk aan de eerste kolom",
            r"elk element komt in de tabel even vaak voor als de andere",
        ],
        antwoord=0,
        uitleg=r"Spiegel je de tabel om de diagonaal van linksboven naar rechtsonder, dan verandert er niets.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel inverse elementen heeft één element van een groep? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Juist één, en ook dat is te bewijzen. Het heet de uniciteit van het invers element.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het neutraal element \(e\) van een groep is uniek.",
        antwoord=True,
        uitleg=r"Stel dat \(e\) en \(e'\) allebei neutraal zijn. Dan is \(e \ast e' = e'\) en ook \(e \ast e' = e\), dus \(e = e'\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe herken je \(e\) in een Cayley-tabel?",
        opties=[
            r"zijn rij en zijn kolom herhalen gewoon de kopregel",
            r"zijn rij en zijn kolom bevatten overal hetzelfde element",
            r"het staat altijd helemaal linksboven in de tabel",
            r"zijn rij bevat alleen vakjes met zichzelf erin",
        ],
        antwoord=0,
        uitleg=r"Het verandert niets, want \(e \ast b = b\), dus de rij is een kopie van de kopregel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe vind je \(a^{-1}\) in een Cayley-tabel?",
        opties=[
            r"je zoekt in de rij van \(a\) waar \(e\) staat",
            r"je zoekt in de rij van \(a\) waar \(a\) zelf opnieuw verschijnt",
            r"je kijkt welk element recht tegenover \(a\) in de kopregel staat",
            r"je kijkt op de hoofddiagonaal in het vakje van \(a\)",
        ],
        antwoord=0,
        uitleg=r"De kolom waarin dat vakje staat, wijst \(a^{-1}\) aan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \((a \ast b)^{-1} = a^{-1} \ast b^{-1}\).",
        antwoord=False,
        uitleg=r"De volgorde keert om: \((a \ast b)^{-1} = b^{-1} \ast a^{-1}\). Bij een commutatieve groep maakt dat niets uit.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is \((a^{-1})^{-1}\)? Schrijf de letter.",
        antwoord=["a"],
        uitleg=r"Twee keer omkeren brengt je terug bij het begin.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe los je \(a \ast x = b\) op in een groep?",
        opties=[
            r"je bewerkt links met \(a^{-1}\)",
            r"je bewerkt rechts met \(a^{-1}\)",
            r"je deelt beide leden door \(a\)",
            r"je bewerkt beide leden met \(e\)",
        ],
        antwoord=0,
        uitleg=r"Links, want \(a\) staat links. Je krijgt \(x = a^{-1} \ast b\). In een groep die niet commutatief is, is die kant belangrijk.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In de Cayley-tabel van een groep komt elk element precies één keer voor in elke rij.",
        antwoord=True,
        uitleg=r"Zou een element twee keer voorkomen, dan had \(a \ast x = b\) twee oplossingen, en dat kan niet in een groep.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat bewijs je met de uniciteit van het neutraal element?",
        opties=[
            r"dat een groep er maar één kan hebben",
            r"dat elke groep er zeker één heeft",
            r"dat \(e\) zijn eigen invers is",
            r"dat \(e\) vooraan hoort te staan",
        ],
        antwoord=0,
        uitleg=r"Dat er één bestaat, is net een van de vier eigenschappen. Dat het er maar één is, moet je bewijzen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een groep telt \(5\) elementen. Hoeveel vakjes heeft haar Cayley-tabel, de kopregel en de kopkolom niet meegerekend? Schrijf het getal.",
        antwoord=["25", "vijfentwintig"],
        uitleg=r"\(5 \cdot 5 = 25\): vijf rijen maal vijf kolommen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe begint het bewijs dat \(e\) uniek is?",
        opties=[
            r"je veronderstelt dat er twee neutrale elementen \(e\) en \(e'\) zijn",
            r"je veronderstelt dat er geen enkel neutraal element bestaat",
            r"je stelt de volledige Cayley-tabel van de groep op",
            r"je zoekt een voorbeeld van een groep met twee neutrale elementen",
        ],
        antwoord=0,
        uitleg=r"Daarna bereken je \(e \ast e'\) op twee manieren en besluit je dat \(e = e'\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Uit \(a \ast x = a \ast y\) volgt in een groep dat \(x = y\).",
        antwoord=True,
        uitleg=r"Je bewerkt beide leden links met \(a^{-1}\). Dat is het hele idee achter het oplossen van vergelijkingen in een groep.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe los je \(x \ast a = b\) op in een groep?",
        opties=[
            r"je bewerkt rechts met \(a^{-1}\)",
            r"je bewerkt links met \(a^{-1}\)",
            r"je bewerkt beide leden met \(a\) zelf",
            r"je bewerkt rechts met \(e\)",
        ],
        antwoord=0,
        uitleg=r"Nu staat \(a\) rechts, dus bewerk je ook rechts: \(x = b \ast a^{-1}\). De kant volgt \(a\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een groep geldt \(a \ast a = e\) voor elk element. Wat zie je dan op de hoofddiagonaal van de tabel?",
        opties=[
            r"overal \(e\)",
            r"overal het element van die rij zelf",
            r"overal verschillende elementen na elkaar",
            r"overal het eerste element van de kopregel",
        ],
        antwoord=0,
        uitleg=r"Op de diagonaal staat elk element met zichzelf bewerkt, en dat geeft dan telkens \(e\). Elk element is dus zijn eigen invers.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Je kan ook van een oneindige groep de volledige Cayley-tabel opstellen.",
        antwoord=False,
        uitleg=r"Die tabel zou oneindig veel rijen en kolommen hebben. De tabel werkt alleen bij eindige groepen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel rijen telt de Cayley-tabel van een groep met \(6\) elementen, de kopregel niet meegerekend? Schrijf het cijfer.",
        antwoord=["6", "zes"],
        uitleg=r"Eén rij per element.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom keert de volgorde om in \((a \ast b)^{-1}\)?",
        opties=[
            r"omdat je het binnenste paar eerst moet kunnen wegwerken",
            r"omdat de bewerking in een groep nooit commutatief mag zijn",
            r"omdat \(e\) anders aan de verkeerde kant staat",
            r"omdat je anders twee verschillende inversen zou uitkomen",
        ],
        antwoord=0,
        uitleg=r"In \(a \ast b \ast b^{-1} \ast a^{-1}\) valt eerst \(b \ast b^{-1} = e\) weg en pas daarna \(a \ast a^{-1} = e\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De vier draaiingen die een vierkant op zichzelf afbeelden, met na elkaar uitvoeren als bewerking. Wat is dat?",
        opties=[
            r"een eindige commutatieve groep",
            r"een oneindige commutatieve groep van draaiingen",
            r"een groep zonder neutraal element erin",
            r"geen groep, want draaien is niet associatief",
        ],
        antwoord=0,
        uitleg=r"Vier elementen, de draaiing over \(0^{\circ}\) is het neutraal element en elke draaiing heeft haar tegendraaiing.",
    ),
]
