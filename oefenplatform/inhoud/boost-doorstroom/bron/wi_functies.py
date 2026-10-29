# -*- coding: utf-8 -*-
"""De vragen voor "Functies en de rechte".

Uit de bouwsteen Relaties en verandering: het functiebegrip met functiewaarde,
afhankelijke en onafhankelijke variabele, domein en bereik, de vier
voorstellingswijzen (verwoording, tabel, grafiek en voorschrift) en het verband
ertussen, en daarnaast de eerstegraadsfunctie: het voorschrift f(x) is ax plus
b, het lineaire en het recht evenredige verband, lineaire groei, de
richtingscoëfficiënt en het snijpunt met de \\(y\\)-as, en het opstellen van de
vergelijking van een rechte uit een richtingscoëfficiënt met een punt of uit
twee punten.

De modellen die de fiche noemt komen als context terug: de rechtlijnige
beweging met constante snelheid, vaste en variabele kosten, hydrostatische
druk, energiegebruik en afschrijving.

Deel 1 is het functiebegrip. Deel 2 is de rechte.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een verband een functie?",
        opties=[
            r"als bij elke \(x\) hoogstens één \(y\) hoort",
            r"als bij elke \(y\) hoogstens één \(x\) hoort",
            "als de grafiek een rechte is",
            r"als \(x\) en \(y\) allebei positief zijn",
        ],
        antwoord=0,
        uitleg="Een verticale lijn mag de grafiek dus maar één keer snijden. Dat heet de verticalelijntest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke variabele is bij 'de kost hangt af van het aantal kilometer' de onafhankelijke?",
        opties=[
            "het aantal kilometer",
            "de kost",
            "allebei even sterk",
            "dat kan je niet bepalen",
        ],
        antwoord=0,
        uitleg="De onafhankelijke variabele kies je zelf, de afhankelijke volgt eruit. Ze staat op de horizontale as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van een functie?",
        opties=[
            "de verzameling van alle \\(x\\)-waarden waarvoor de functie een waarde geeft",
            "de verzameling van alle \\(y\\)-waarden die de functie aanneemt",
            "de verzameling van de nulwaarden van de functie",
            "de verzameling van alle punten op de grafiek",
        ],
        antwoord=0,
        uitleg="Het bereik is de tegenhanger: dat zijn de \\(y\\)-waarden die er uitkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van een functie?",
        opties=[
            "de verzameling van alle \\(y\\)-waarden die de functie aanneemt",
            "de verzameling van alle \\(x\\)-waarden waarvoor ze bestaat",
            "de afstand tussen de kleinste en de grootste \\(x\\)-waarde",
            "het aantal snijpunten met de \\(x\\)-as",
        ],
        antwoord=0,
        uitleg="Op de grafiek lees je het bereik af door naar de verticale as te kijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de vier voorstellingswijzen van een functie?",
        opties=[
            "verwoording, tabel, grafiek en voorschrift",
            "formule, tekening, verhaal en schema",
            "grafiek, diagram, tabel en histogram",
            "voorschrift, nulwaarde, top en domein",
        ],
        antwoord=0,
        uitleg="Je moet van elke vorm naar elke andere kunnen overstappen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor \(f(x) = 3x - 2\), hoeveel is \(f(4)\)?",
        opties=[r"\(10\)", r"\(14\)", r"\(5\)", r"\(12\)"],
        antwoord=0,
        uitleg=r"\(3 \cdot 4 = 12\), en \(12 - 2 = 10\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor \(f(x) = 3x - 2\), voor welke \(x\) is \(f(x) = 13\)?",
        opties=[r"\(5\)", r"\(11\)", r"\(4\)", r"\(39\)"],
        antwoord=0,
        uitleg=r"\(3x = 15\), dus \(x = 5\). Je lost een vergelijking op in plaats van in te vullen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het domein van de functie \(f(x) = \tfrac{1}{x}\)?",
        opties=[
            r"\(\mathbb{R}\) zonder \(0\)",
            r"alle positieve getallen van \(\mathbb{R}\)",
            r"heel \(\mathbb{R}\)",
            r"\(\mathbb{Z}\) zonder \(0\)",
        ],
        antwoord=0,
        uitleg=r"Delen door nul mag niet, dus \(x = 0\) valt weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een recht evenredig verband tussen twee grootheden?",
        opties=[
            "als de ene verdubbelt, verdubbelt de andere ook",
            "als de ene verdubbelt, wordt de andere half zo groot",
            "de som van de twee blijft altijd gelijk",
            "het verschil van de twee blijft altijd gelijk",
        ],
        antwoord=0,
        uitleg=r"De grafiek is een rechte door de oorsprong, met voorschrift \(y = ax\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een lineair en een recht evenredig verband?",
        opties=[
            "een recht evenredig verband gaat door de oorsprong, een lineair verband niet noodzakelijk",
            "een lineair verband gaat door de oorsprong, een recht evenredig verband niet",
            "er is geen verschil tussen de twee",
            "een lineair verband heeft altijd een negatieve helling",
        ],
        antwoord=0,
        uitleg=r"Bij \(y = 2x + 5\) is het verband lineair maar niet recht evenredig: bij nul kilometer betaal je al \(5\) euro.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel geeft bij \(x = 1, 2, 3\) de waarden \(4\), \(7\), \(10\). Wat voor groei is dat?",
        opties=[
            r"lineaire groei, want er komt telkens \(3\) bij",
            "kwadratische groei, want de verschillen stijgen",
            "omgekeerd evenredig, want de waarden stijgen",
            "geen enkel herkenbaar verband",
        ],
        antwoord=0,
        uitleg=r"Bij lineaire groei is het verschil per stap constant. Het voorschrift is \(y = 3x + 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel geeft bij \(x = 1, 2, 3\) de waarden \(1\), \(4\), \(9\). Wat voor groei is dat?",
        opties=[
            "niet-lineaire groei, want de verschillen worden groter",
            "lineaire groei, want de waarden stijgen elke stap",
            "omgekeerd evenredige groei",
            "constante groei zonder toename",
        ],
        antwoord=0,
        uitleg=r"De verschillen zijn \(3\) en \(5\), dus geen rechte. Dit is het kwadratische verband \(y = x^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort bij een grafiek altijd een ijk op de assen?",
        opties=[
            "zonder ijk kan je geen enkele waarde aflezen",
            "omdat de grafiek anders niet op het blad past",
            "omdat het examen dat verplicht voor elke tekening",
            "om te tonen welke variabele afhankelijk is",
        ],
        antwoord=0,
        uitleg="Een grafiek zonder ijk toont enkel een vorm en geen getallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een functie mag dezelfde \\(y\\)-waarde bij meerdere \\(x\\)-waarden horen.",
        antwoord=True,
        uitleg=r"Dat is geen probleem: bij \(y = x^{2}\) hoort \(y = 4\) bij zowel \(x = 2\) als \(x = -2\).",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een functie mogen bij dezelfde \\(x\\)-waarde twee verschillende \\(y\\)-waarden horen.",
        antwoord=False,
        uitleg="Dan is het geen functie meer. Een verticale lijn zou de grafiek twee keer snijden.",
    ),
    dict(
        type="waarofniet",
        vraag="De afhankelijke variabele staat op de verticale as.",
        antwoord=True,
        uitleg="De onafhankelijke, die je zelf kiest, staat op de horizontale as.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk lineair verband is ook recht evenredig.",
        antwoord=False,
        uitleg=r"Alleen als het door de oorsprong gaat, dus als \(b = 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Voor \(f(x) = 2x + 7\), hoeveel is \(f(5)\)?",
        antwoord=["17"],
        uitleg=r"\(10 + 7\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Voor \(f(x) = 4x - 1\), voor welke \(x\) is \(f(x) = 11\)?",
        antwoord=["3"],
        uitleg=r"\(4x = 12\).",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de verzameling van alle \\(y\\)-waarden die een functie aanneemt?",
        antwoord=["bereik", "het bereik"],
        uitleg="De \\(x\\)-waarden vormen het domein.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent de \(a\) in het voorschrift \(f(x) = ax + b\)?",
        opties=[
            r"de richtingscoëfficiënt: hoeveel \(y\) stijgt per eenheid \(x\)",
            "de hoogte waarop de rechte de \\(y\\)-as snijdt",
            "de \\(x\\)-waarde waar de rechte de \\(x\\)-as snijdt",
            "de hoek die de rechte met de \\(x\\)-as maakt, in graden",
        ],
        antwoord=0,
        uitleg=r"Is \(a = 3\), dan gaat de rechte drie omhoog per stap naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent de \(b\) in het voorschrift \(f(x) = ax + b\)?",
        opties=[
            "de \\(y\\)-waarde waar de rechte de verticale as snijdt",
            "de helling van de rechte",
            "de nulwaarde van de functie",
            "het aantal snijpunten met de \\(x\\)-as",
        ],
        antwoord=0,
        uitleg=r"Vul \(x = 0\) in en je houdt \(b\) over. Bij een taxirit is \(b\) de opstapprijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de richtingscoëfficiënt van de rechte door \\((1, 2)\\) en \\((4, 11)\\)?",
        opties=[r"\(3\)", r"\(9\)", r"\(-3\)", r"\(\tfrac{1}{3}\)"],
        antwoord=0,
        uitleg=r"Het verschil in \(y\) gedeeld door het verschil in \(x\): \(\tfrac{9}{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de richtingscoëfficiënt van de rechte door \\((0, 5)\\) en \\((2, 1)\\)?",
        opties=[r"\(-2\)", r"\(2\)", r"\(-4\)", r"\(4\)"],
        antwoord=0,
        uitleg=r"Het verschil in \(y\) is \(-4\) over een verschil in \(x\) van \(2\). De rechte daalt dus.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het voorschrift van de rechte met richtingscoëfficiënt \(2\) door het punt \(\left(0, 3\right)\)?",
        opties=["\\(y = 2x + 3\\)", "\\(y = 3x + 2\\)", "\\(y = 2x - 3\\)", r"\(y = 2x\)"],
        antwoord=0,
        uitleg="Het punt ligt op de \\(y\\)-as, dus je kan b meteen aflezen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het voorschrift van de rechte met richtingscoëfficiënt \(4\) door het punt \(\left(1, 6\right)\)?",
        opties=["\\(y = 4x + 2\\)", "\\(y = 4x + 6\\)", "\\(y = 4x - 2\\)", "\\(y = 6x + 4\\)"],
        antwoord=0,
        uitleg=r"Vul in: \(6 = 4 \cdot 1 + b\), dus \(b = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je van een rechte met richtingscoëfficiënt nul?",
        opties=[
            "ze loopt horizontaal",
            "ze loopt verticaal",
            "ze gaat door de oorsprong",
            "ze bestaat niet",
        ],
        antwoord=0,
        uitleg=r"De \(y\)-waarde verandert niet als \(x\) verandert. Het voorschrift is dan \(y = b\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee rechten zijn evenwijdig. Wat weet je over hun richtingscoëfficiënten?",
        opties=[
            "ze zijn gelijk",
            "ze zijn tegengesteld",
            r"hun product is \(-1\)",
            "ze zijn allebei nul",
        ],
        antwoord=0,
        uitleg=r"Bij loodrechte rechten is het product van de richtingscoëfficiënten wel \(-1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fietser rijdt aan \(18\) kilometer per uur en is al \(5\) kilometer ver. Welk voorschrift hoort bij de afgelegde weg?",
        opties=["\\(s = 18t + 5\\)", "\\(s = 5t + 18\\)", "\\(s = 18t - 5\\)", r"\(s = 23t\)"],
        antwoord=0,
        uitleg=r"Dit is de eenparig rechtlijnige beweging: de beginpositie is \(b\) en de snelheid is de richtingscoëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een drukkerij rekent \(60\) euro opstartkosten plus \(0{,}40\) euro per affiche. Wat is het voorschrift van de totale kost?",
        opties=["\\(k = 0{,}40n + 60\\)", "\\(k = 60n + 0{,}40\\)", r"\(k = 60{,}40n\)", "\\(k = 0{,}40n - 60\\)"],
        antwoord=0,
        uitleg=r"De opstartkosten zijn de vaste kosten en dus de \(b\). De prijs per stuk is de richtingscoëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een machine van \(20\,000\) euro wordt in tien jaar lineair afgeschreven tot nul. Hoeveel is ze na vier jaar waard?",
        opties=[r"\(12\,000\) euro", r"\(8\,000\) euro", r"\(16\,000\) euro", r"\(10\,000\) euro"],
        antwoord=0,
        uitleg=r"Per jaar \(2\,000\) euro minder. Na vier jaar is dat \(8\,000\) euro minder dan \(20\,000\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De hydrostatische druk stijgt met ongeveer \(1\) bar per \(10\) meter diepte, bovenop \(1\) bar aan de oppervlakte. Welke druk hoort bij \(30\) meter?",
        opties=[r"\(4\) bar", r"\(3\) bar", r"\(30\) bar", r"\(31\) bar"],
        antwoord=0,
        uitleg=r"\(1\) bar lucht plus \(3\) bar water. Het verband is lineair maar niet recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar snijdt de rechte \\(y = 2x - 8\\) de \\(x\\)-as?",
        opties=["in \\((4, 0)\\)", "in \\((0, 4)\\)", "in \\((-4, 0)\\)", "in \\((0, -8)\\)"],
        antwoord=0,
        uitleg=r"Stel \(y = 0\): \(2x = 8\), dus \(x = 4\). Het punt \(\left(0, -8\right)\) is het snijpunt met de \(y\)-as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte met een negatieve richtingscoëfficiënt daalt van links naar rechts.",
        antwoord=True,
        uitleg=r"Hoe groter \(x\), hoe kleiner \(y\).",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale rechte is de grafiek van een functie.",
        antwoord=False,
        uitleg=r"Bij één \(x\)-waarde horen dan oneindig veel \(y\)-waarden, en dat mag niet bij een functie.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee punten volstaan om de vergelijking van een rechte te bepalen.",
        antwoord=True,
        uitleg=r"Uit de twee punten haal je de richtingscoëfficiënt, en daarna vul je één punt in om \(b\) te vinden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij vaste en variabele kosten samen is de totale kost recht evenredig met het aantal stuks.",
        antwoord=False,
        uitleg="Door de vaste kosten gaat de rechte niet door de oorsprong. Het verband is wel lineair.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de richtingscoëfficiënt van de rechte door \\((2, 3)\\) en \\((5, 12)\\)?",
        antwoord=["3"],
        uitleg=r"\(\tfrac{9}{3}\).",
    ),
    dict(
        type="invultekst",
        vraag="Waar snijdt de rechte \\(y = 3x - 12\\) de \\(x\\)-as? Geef de \\(x\\)-waarde.",
        antwoord=["4"],
        uitleg=r"Stel \(y = 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een machine van \(20\,000\) euro wordt in tien jaar lineair afgeschreven. Hoeveel euro per jaar?",
        antwoord=["2000", "2 000", "2000 euro"],
        uitleg=r"\(20\,000 : 10\).",
    ),
]
