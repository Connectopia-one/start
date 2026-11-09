# -*- coding: utf-8 -*-
"""Kansrekenen met kansbomen en kruistabellen.

Wiskunde basis, derde graad. De fiche vraagt: kansboom en kruistabel,
gebeurtenis, uitkomst, uitkomstenverzameling, de wet van Laplace, absolute en
relatieve frequentie, kans en voorwaardelijke kans, het verband tussen
relatieve frequentie en kans, en de productregel, de somregel en de
complementregel bij een kansboom. Altijd in context. Telproblemen
(combinaties, permutaties) staan niet in deze fiche.

Deel 1: Laplace, frequenties en kruistabellen.
Deel 2: kansbomen en voorwaardelijke kansen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat zegt de wet van Laplace?",
        opties=[
            r"Bij gelijk mogelijke uitkomsten is een kans het aantal gunstige uitkomsten gedeeld door het aantal mogelijke uitkomsten.",
            r"Bij elk experiment is een kans het aantal mogelijke uitkomsten gedeeld door het aantal gunstige uitkomsten.",
            r"Een kans is altijd gelijk aan de relatieve frequentie na tien herhalingen.",
            r"Twee gebeurtenissen hebben altijd samen een kans van \(1\).",
        ],
        antwoord=0,
        uitleg=r"Laplace werkt enkel als elke uitkomst even waarschijnlijk is, zoals bij een eerlijke dobbelsteen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de uitkomstenverzameling als je één keer met een dobbelsteen gooit?",
        opties=[r"\(\{1, 2, 3, 4, 5, 6\}\)", r"\(\{6\}\)", r"\(\{1, 6\}\)", r"\(\{0, 1, 2, 3, 4, 5, 6\}\)"],
        antwoord=0,
        uitleg=r"De uitkomstenverzameling bevat alle mogelijke uitkomsten van het experiment.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit met een eerlijke dobbelsteen. Wat is de kans op een even getal?",
        opties=[r"\(\dfrac{1}{2}\)", r"\(\dfrac{1}{3}\)", r"\(\dfrac{1}{6}\)", r"\(\dfrac{2}{3}\)"],
        antwoord=0,
        uitleg=r"Gunstig zijn \(2\), \(4\) en \(6\): \(\dfrac{3}{6} = \dfrac{1}{2}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een gebeurtenis is een deel van de uitkomstenverzameling.",
        antwoord=True,
        uitleg=r"Bijvoorbeeld \(\{2, 4, 6\}\) is de gebeurtenis een even getal gooien.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vaas bevat \(5\) rode, \(3\) blauwe en \(2\) groene knikkers. Je neemt er blindelings één. Wat is \(P(\text{blauw})\)?",
        opties=[r"\(0{,}3\)", r"\(0{,}5\)", r"\(\dfrac{3}{7}\)", r"\(0{,}2\)"],
        antwoord=0,
        uitleg=r"\(3\) gunstige uit \(10\) mogelijke: \(\dfrac{3}{10} = 0{,}3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke regel bereken je \(P(\text{niet } A)\)?",
        opties=[r"\(1 - P(A)\)", r"\(P(A) - 1\)", r"\(\dfrac{1}{P(A)}\)", r"\(P(A) \cdot P(A)\)"],
        antwoord=0,
        uitleg=r"De complementregel: een gebeurtenis gebeurt of gebeurt niet, samen is dat kans \(1\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De kans dat een trein op tijd is, is \(0{,}85\). Wat is de kans dat hij niet op tijd is? Schrijf het getal.",
        antwoord=["0,15", "0.15"],
        uitleg=r"\(1 - 0{,}85 = 0{,}15\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een munt wordt \(200\) keer opgegooid en valt \(94\) keer op kop. Wat is de relatieve frequentie van kop?",
        opties=[r"\(0{,}47\)", r"\(94\)", r"\(0{,}5\)", r"\(0{,}94\)"],
        antwoord=0,
        uitleg=r"De absolute frequentie is \(94\). De relatieve frequentie is \(\dfrac{94}{200} = 0{,}47\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als je een experiment heel vaak herhaalt, komt de relatieve frequentie dicht bij de kans.",
        antwoord=True,
        uitleg=r"Dat is het verband tussen relatieve frequentie en kans. Bij weinig herhalingen kan ze nog sterk afwijken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een munt viel vijf keer na elkaar op kop. De kans op kop bij de zesde worp is nu kleiner dan \(\dfrac{1}{2}\).",
        antwoord=False,
        uitleg=r"Een munt heeft geen geheugen: elke worp heeft kans \(\tfrac{1}{2}\) op kop.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kruistabel van \(200\) leerlingen: \(60\) jongens sporten, \(40\) jongens sporten niet, \(70\) meisjes sporten, \(30\) meisjes sporten niet. Wat is \(P(\text{sport})\) voor een willekeurige leerling?",
        opties=[r"\(0{,}65\)", r"\(0{,}6\)", r"\(0{,}7\)", r"\(0{,}35\)"],
        antwoord=0,
        uitleg=r"\(60 + 70 = 130\) sporters op \(200\): \(\dfrac{130}{200} = 0{,}65\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In diezelfde kruistabel: wat is \(P(\text{sport} \mid \text{meisje})\)?",
        opties=[r"\(0{,}7\)", r"\(0{,}35\)", r"\(\dfrac{70}{130}\)", r"\(0{,}65\)"],
        antwoord=0,
        uitleg=r"Je kijkt enkel naar de \(100\) meisjes: \(\dfrac{70}{100} = 0{,}7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In diezelfde kruistabel: wat is \(P(\text{meisje} \mid \text{sport})\)?",
        opties=[r"\(\dfrac{70}{130} \approx 0{,}54\)", r"\(0{,}7\)", r"\(0{,}35\)", r"\(0{,}5\)"],
        antwoord=0,
        uitleg=r"Nu kijk je enkel naar de \(130\) sporters. Daarvan zijn er \(70\) meisjes.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(P(A \mid B)\) en \(P(B \mid A)\) zijn altijd gelijk.",
        antwoord=False,
        uitleg=r"Ze delen door een andere groep. Zie de kruistabel: \(P(\text{sport} \mid \text{meisje}) = 0{,}7\), maar \(P(\text{meisje} \mid \text{sport}) \approx 0{,}54\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent de notatie \(P(A \mid B)\)?",
        opties=[
            r"de kans op \(A\), als je weet dat \(B\) gebeurd is",
            r"de kans op \(A\) gedeeld door de kans op \(B\)",
            r"de kans dat \(A\) of \(B\) gebeurt",
            r"de kans op \(B\), als je weet dat \(A\) gebeurd is",
        ],
        antwoord=0,
        uitleg=r"Dat is een voorwaardelijke kans: \(B\) is de voorwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een enquête bij \(500\) mensen: \(120\) hebben een hond. Hoeveel mensen met een hond verwacht je in een groep van \(2000\) gelijkaardige mensen?",
        opties=[r"\(480\)", r"\(120\)", r"\(240\)", r"\(600\)"],
        antwoord=0,
        uitleg=r"De relatieve frequentie \(\dfrac{120}{500} = 0{,}24\) gebruik je als schatting van de kans: \(0{,}24 \cdot 2000 = 480\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een kaart uit een spel van \(52\) kaarten. Wat is de kans op een aas? Schrijf als breuk, bijvoorbeeld 1/5.",
        antwoord=["1/13", "4/52"],
        uitleg=r"Er zijn \(4\) azen: \(\dfrac{4}{52} = \dfrac{1}{13}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een kans kan groter zijn dan \(1\).",
        antwoord=False,
        uitleg=r"Een kans ligt altijd tussen \(0\) (onmogelijk) en \(1\) (zeker).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op een rad van fortuin is de kans op winst \(0{,}2\). Wat is de verwachte absolute frequentie van winst bij \(150\) keer draaien?",
        opties=[r"\(30\)", r"\(20\)", r"\(15\)", r"\(0{,}2\)"],
        antwoord=0,
        uitleg=r"\(0{,}2 \cdot 150 = 30\). Het echte aantal kan daar wat rond schommelen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een kruistabel tellen alle cellen samen op tot het totaal aantal waarnemingen.",
        antwoord=True,
        uitleg=r"Elke waarneming staat in precies één cel. De randtotalen vatten de rijen en kolommen samen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de productregel bij een kansboom?",
        opties=[
            r"De kans op een pad is het product van de kansen op de takken van dat pad.",
            r"De kans op een pad is de som van de kansen op de takken van dat pad.",
            r"De kans op meerdere paden is het product van hun kansen.",
            r"De kansen op alle takken samen zijn altijd \(1\).",
        ],
        antwoord=0,
        uitleg=r"Langs een pad vermenigvuldig je. Om verschillende paden samen te nemen, tel je op (somregel).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de somregel bij een kansboom?",
        opties=[
            r"De kans dat een van verschillende paden zich voordoet, is de som van de kansen van die paden.",
            r"De kans op een pad is de som van de kansen op zijn takken.",
            r"Je telt altijd alle takken van de boom op.",
            r"De kans op een pad is \(1\) min de kans op de andere paden, vermenigvuldigd.",
        ],
        antwoord=0,
        uitleg=r"Verschillende paden sluiten elkaar uit, dus hun kansen mag je optellen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je gooit twee keer met een munt. Wat is de kans op twee keer kop? Schrijf als kommagetal.",
        antwoord=["0,25", "0.25"],
        uitleg=r"Productregel: \(0{,}5 \cdot 0{,}5 = 0{,}25\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit twee keer met een munt. Wat is de kans op precies één keer kop?",
        opties=[r"\(0{,}5\)", r"\(0{,}25\)", r"\(0{,}75\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"Twee paden: kop-munt en munt-kop, elk \(0{,}25\). Somregel: \(0{,}25 + 0{,}25 = 0{,}5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vaas heeft \(3\) rode en \(2\) witte ballen. Je neemt er twee zonder terugleggen. Wat is \(P(\text{twee rode})\)?",
        opties=[r"\(\dfrac{3}{10}\)", r"\(\dfrac{9}{25}\)", r"\(\dfrac{6}{25}\)", r"\(\dfrac{3}{5}\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{3}{5} \cdot \dfrac{2}{4} = \dfrac{6}{20} = \dfrac{3}{10}\). Na de eerste rode bal zijn er nog \(2\) rode op \(4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Dezelfde vaas (\(3\) rood, \(2\) wit), maar nu mét terugleggen. Wat is \(P(\text{twee rode})\)?",
        opties=[r"\(\dfrac{9}{25}\)", r"\(\dfrac{3}{10}\)", r"\(\dfrac{6}{25}\)", r"\(\dfrac{6}{10}\)"],
        antwoord=0,
        uitleg=r"Met terugleggen blijft de kans telkens \(\tfrac{3}{5}\): \(\dfrac{3}{5} \cdot \dfrac{3}{5} = \dfrac{9}{25}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een kansboom tellen de kansen op de takken die uit hetzelfde knooppunt vertrekken op tot \(1\).",
        antwoord=True,
        uitleg=r"Vanuit één knooppunt staan alle mogelijkheden van die stap.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit drie keer met een dobbelsteen. Wat is de kans dat je minstens één zes gooit, afgerond op twee cijfers na de komma?",
        opties=[r"\(0{,}42\)", r"\(0{,}50\)", r"\(0{,}58\)", r"\(0{,}17\)"],
        antwoord=0,
        uitleg=r"Complementregel: \(1 - P(\text{geen zes}) = 1 - \left(\tfrac{5}{6}\right)^{3} \approx 1 - 0{,}579 = 0{,}42\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De kans op minstens één zes bij drie worpen is \(\dfrac{1}{6} + \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{1}{2}\).",
        antwoord=False,
        uitleg=r"Zo tel je de paden met twee of drie zessen meer dan één keer. Met de complementregel vind je \(\approx 0{,}42\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(2\%\) van de mensen heeft een ziekte. Een test is positief bij \(95\%\) van de zieken en bij \(10\%\) van de gezonde mensen. Wat is de kans dat een willekeurig persoon ziek is én positief test?",
        opties=[r"\(0{,}019\)", r"\(0{,}95\)", r"\(0{,}02\)", r"\(0{,}098\)"],
        antwoord=0,
        uitleg=r"Pad ziek-positief: \(0{,}02 \cdot 0{,}95 = 0{,}019\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij die test (\(2\%\) ziek, \(95\%\) positief bij zieken, \(10\%\) positief bij gezonden): wat is de kans dat een willekeurig persoon positief test?",
        opties=[r"\(0{,}117\)", r"\(0{,}105\)", r"\(0{,}019\)", r"\(0{,}95\)"],
        antwoord=0,
        uitleg=r"Twee paden: ziek-positief \(0{,}019\) en gezond-positief \(0{,}98 \cdot 0{,}10 = 0{,}098\). Samen \(0{,}117\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"En wat is de kans dat iemand met een positieve test echt ziek is, afgerond op twee cijfers na de komma?",
        opties=[r"\(0{,}16\)", r"\(0{,}95\)", r"\(0{,}02\)", r"\(0{,}84\)"],
        antwoord=0,
        uitleg=r"\(P(\text{ziek} \mid \text{positief}) = \dfrac{0{,}019}{0{,}117} \approx 0{,}16\). De meeste positieve tests komen van gezonde mensen, omdat er zoveel meer gezonden zijn.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij die test is de kans dat een positief geteste persoon ziek is, gelijk aan \(95\%\).",
        antwoord=False,
        uitleg=r"\(95\%\) is \(P(\text{positief} \mid \text{ziek})\). Omgekeerd is het maar ongeveer \(16\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling haalt met kans \(0{,}8\) zijn bus. Haalt hij de bus, dan is hij met kans \(0{,}95\) op tijd. Mist hij de bus, dan met kans \(0{,}3\). Wat is de kans dat hij op tijd is?",
        opties=[r"\(0{,}82\)", r"\(0{,}76\)", r"\(0{,}625\)", r"\(1{,}25\)"],
        antwoord=0,
        uitleg=r"\(0{,}8 \cdot 0{,}95 + 0{,}2 \cdot 0{,}3 = 0{,}76 + 0{,}06 = 0{,}82\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een schutter raakt met kans \(0{,}7\) per schot. Hij schiet twee keer. Wat is de kans dat hij twee keer mist? Schrijf als kommagetal.",
        antwoord=["0,09", "0.09"],
        uitleg=r"\(0{,}3 \cdot 0{,}3 = 0{,}09\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde schutter (kans \(0{,}7\) per schot, twee schoten). Wat is de kans dat hij minstens één keer raak schiet?",
        opties=[r"\(0{,}91\)", r"\(0{,}49\)", r"\(0{,}7\)", r"\(1{,}4\)"],
        antwoord=0,
        uitleg=r"Complementregel: \(1 - 0{,}09 = 0{,}91\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij trekken zonder terugleggen veranderen de kansen op de takken van de tweede stap.",
        antwoord=True,
        uitleg=r"Na de eerste trekking is er een bal minder, en de samenstelling van de vaas is veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Van een klas kiest \(60\%\) Frans en \(40\%\) Duits als extra taal. Van wie Frans kiest, slaagt \(90\%\); van wie Duits kiest, slaagt \(75\%\). Hoe stel je dit het best voor?",
        opties=[
            r"met een kansboom: eerst de taal, dan slagen of niet",
            r"met één kans: \(0{,}9 \cdot 0{,}75\)",
            r"met de wet van Laplace op \(4\) uitkomsten",
            r"met een rekenkundige rij",
        ],
        antwoord=0,
        uitleg=r"Twee stappen na elkaar, waarbij de tweede afhangt van de eerste: daar is een kansboom voor gemaakt.",
    ),
    dict(
        type="invultekst",
        vraag=r"In die klas (\(60\%\) Frans met \(90\%\) geslaagd, \(40\%\) Duits met \(75\%\) geslaagd): welk deel slaagt? Schrijf als kommagetal.",
        antwoord=["0,84", "0.84"],
        uitleg=r"\(0{,}6 \cdot 0{,}9 + 0{,}4 \cdot 0{,}75 = 0{,}54 + 0{,}30 = 0{,}84\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De kansen van alle paden van een volledige kansboom tellen samen op tot \(1\).",
        antwoord=True,
        uitleg=r"Samen beschrijven alle paden elke mogelijke afloop van het experiment.",
    ),
]
