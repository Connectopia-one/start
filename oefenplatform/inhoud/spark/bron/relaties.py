# -*- coding: utf-8 -*-
"""De vragen voor "Relaties en verandering" (✨ Spark, wiskunde).

De vakfiche zet hieronder vier dingen: coördinaten in een assenstelsel, het
rekenen met letters (eentermen, veeltermen, getalwaarde, de merkwaardige
producten), recht en omgekeerd evenredige verbanden in een formule, tabel of
grafiek, en vergelijkingen van de eerste graad met één onbekende.

Patronen horen er ook bij: regelmaat ontdekken en die in een formule zetten.

Deel 1 blijft bij één stap tegelijk. Deel 2 vraagt haakjes wegwerken, de
merkwaardige producten, omgekeerd evenredige verbanden en vraagstukken waar je
eerst zelf de vergelijking moet opstellen.

De wiskundige notatie staat in de vragen zelf: een punt als \\((3, 5)\\), een
eenterm als \\(5x^{3}\\) en een merkwaardig product als
\\((a + b)^{2} = a^{2} + 2ab + b^{2}\\).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"In een assenstelsel geeft een punt \((3, 5)\) aan. Wat betekent de \(3\)?",
        opties=[
            "Drie stappen langs de horizontale as",
            "Drie stappen omhoog",
            "Dat het punt drie keer voorkomt",
        ],
        antwoord=0,
        uitleg=r"Het eerste getal is de \(x\)-coördinaat en hoort bij de horizontale as. Het tweede is "
               r"de \(y\)-coördinaat. Altijd in die volgorde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coördinaten heeft de oorsprong?",
        opties=[r"\((0, 0)\)", r"\((1, 1)\)", r"\((0, 1)\)"],
        antwoord=0,
        uitleg=r"De oorsprong is het punt waar de \(x\)-as en de \(y\)-as elkaar snijden, dus \((0, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een punt ligt op de \(x\)-as. Wat weet je over zijn \(y\)-coördinaat?",
        opties=[r"Die is \(0\)", r"Die is \(1\)", r"Die is even groot als de \(x\)-coördinaat"],
        antwoord=0,
        uitleg=r"Op de \(x\)-as ga je niet omhoog of omlaag, dus \(y = 0\). Een punt op de \(y\)-as "
               r"heeft net zo \(x = 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de getalwaarde van \(3x\) als \(x = 4\).",
        antwoord="12",
        uitleg=r"\(3x\) betekent \(3 \cdot x\), dus \(3 \cdot 4 = 12\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken de getalwaarde van \(2a + 5\) als \(a = 6\).",
        opties=[r"\(17\)", r"\(13\)", r"\(22\)"],
        antwoord=0,
        uitleg=r"\(2 \cdot 6 = 12\), en \(12 + 5 = 17\). Eerst vermenigvuldigen, dan optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de eenterm \(5x^{3}\), welk getal is de coëfficiënt?",
        opties=[r"\(5\)", r"\(3\)", r"\(x\)"],
        antwoord=0,
        uitleg=r"De coëfficiënt is het getal vooraan: \(5\). Het lettergedeelte is \(x^{3}\), en de "
               r"graad van deze eenterm is \(3\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee eentermen zijn gelijksoortig?",
        opties=[r"\(3x\) en \(7x\)", r"\(3x\) en \(3x^{2}\)", r"\(3x\) en \(3y\)"],
        antwoord=0,
        uitleg=r"Gelijksoortig betekent hetzelfde lettergedeelte. Alleen dan mag je optellen: "
               r"\(3x + 7x = 10x\). Bij \(3x\) en \(3x^{2}\) kan dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Herleid: \(4a + 3a - a\)",
        opties=[r"\(6a\)", r"\(7a\)", r"\(8a\)"],
        antwoord=0,
        uitleg=r"Alle drie zijn gelijksoortig, dus tel de coëfficiënten op: \(4 + 3 - 1 = 6\), dus "
               r"\(6a\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Werk de haakjes weg: \(3(x + 2)\)",
        opties=[r"\(3x + 6\)", r"\(3x + 2\)", r"\(x + 6\)"],
        antwoord=0,
        uitleg=r"Distributief: de \(3\) gaat over allebei de termen. \(3 \cdot x = 3x\) en "
               r"\(3 \cdot 2 = 6\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(x + 7 = 12\). Wat is \(x\)?",
        antwoord="5",
        uitleg=r"Trek aan beide kanten \(7\) af: \(x = 12 - 7 = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(3x = 21\). Wat is \(x\)?",
        antwoord="7",
        uitleg=r"Deel aan beide kanten door \(3\): \(x = 21 : 3 = 7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2x + 5 = 17\)",
        opties=[r"\(x = 6\)", r"\(x = 11\)", r"\(x = 8\)"],
        antwoord=0,
        uitleg=r"Eerst de \(5\) eraf: \(2x = 12\). Dan delen door \(2\): \(x = 6\). Controleer: "
               r"\(2 \cdot 6 + 5 = 17\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x - 4 = -9\)",
        opties=[r"\(x = -5\)", r"\(x = -13\)", r"\(x = 5\)"],
        antwoord=0,
        uitleg=r"Tel aan beide kanten \(4\) op: \(x = -9 + 4 = -5\). Controleer: \(-5 - 4 = -9\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je het deel links van het gelijkheidsteken?",
        opties=["Het linkerlid", "De onbekende", "De oplossing"],
        antwoord=0,
        uitleg="Linkerlid en rechterlid, met het gelijkheidsteken ertussen. De onbekende is de letter, "
               "de oplossing is de waarde die klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Drie broden kosten € \(7{,}50\). Wat kosten er vijf?",
        opties=[r"€ \(12{,}50\)", r"€ \(15\)", r"€ \(10\)"],
        antwoord=0,
        uitleg=r"Recht evenredig: ga naar één brood, \(7{,}50 : 3 = 2{,}50\) euro. Dan "
               r"\(5 \cdot 2{,}50 = 12{,}50\) euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee grootheden zijn recht evenredig. Wat gebeurt er als je de ene verdubbelt?",
        opties=["De andere verdubbelt ook", "De andere halveert", "De andere blijft gelijk"],
        antwoord=0,
        uitleg="Bij een recht evenredig verband groeien ze samen mee. Het quotiënt van de twee blijft "
               "altijd hetzelfde; dat getal heet de evenredigheidsfactor.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de tabel hoort bij \(2\) het getal \(6\), bij \(4\) het getal \(12\) en bij \(5\) "
              r"het getal \(15\). Welke formule past?",
        opties=[r"\(y = 3x\)", r"\(y = x + 4\)", r"\(y = 2x\)"],
        antwoord=0,
        uitleg=r"Elk tweede getal is drie keer het eerste: \(6 : 2 = 3\), \(12 : 4 = 3\), "
               r"\(15 : 5 = 3\). De evenredigheidsfactor is dus \(3\).",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van een recht evenredig verband is een rechte lijn door de oorsprong.",
        antwoord=True,
        uitleg=r"Juist. Bij nul van het ene hoort nul van het andere, dus de lijn vertrekt in "
               r"\((0, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rij begint met \(3,\ 7,\ 11,\ 15,\ \ldots\) Welk getal komt er daarna?",
        opties=[r"\(19\)", r"\(18\)", r"\(20\)"],
        antwoord=0,
        uitleg=r"Er komt telkens \(4\) bij: \(15 + 4 = 19\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule geeft het aantal poten bij \(k\) koeien?",
        opties=[r"\(4k\)", r"\(k + 4\)", r"\(k : 4\)"],
        antwoord=0,
        uitleg=r"Elke koe heeft vier poten, dus \(4 \cdot k\). Een formule opstellen begint met de "
               r"vraag: wat gebeurt er per stuk?",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Werk uit: \((a + b)^{2}\)",
        opties=[r"\(a^{2} + 2ab + b^{2}\)", r"\(a^{2} + b^{2}\)", r"\(a^{2} + ab + b^{2}\)"],
        antwoord=0,
        uitleg=r"Het merkwaardig product: \((a + b)^{2} = a^{2} + 2ab + b^{2}\). De middelste term "
               r"wordt het vaakst vergeten. Controleer met \(a = 2\) en \(b = 3\): "
               r"\((2 + 3)^{2} = 25\), en \(4 + 12 + 9 = 25\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Werk uit: \((a + b)(a - b)\)",
        opties=[r"\(a^{2} - b^{2}\)", r"\(a^{2} + b^{2}\)", r"\(a^{2} - 2ab + b^{2}\)"],
        antwoord=0,
        uitleg=r"De middelste termen vallen weg: \(-ab + ab = 0\). Blijft over \(a^{2} - b^{2}\). Met "
               r"\(a = 5\) en \(b = 2\): \(7 \cdot 3 = 21\), en \(25 - 4 = 21\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Werk uit: \((x + 4)^{2}\)",
        opties=[r"\(x^{2} + 8x + 16\)", r"\(x^{2} + 16\)", r"\(x^{2} + 4x + 16\)"],
        antwoord=0,
        uitleg=r"Volgens \((a + b)^{2}\): \(x^{2} + 2 \cdot x \cdot 4 + 4^{2} = x^{2} + 8x + 16\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Werk uit: \(2(3x - 5) + 4x\)",
        opties=[r"\(10x - 10\)", r"\(6x - 10\)", r"\(10x - 5\)"],
        antwoord=0,
        uitleg=r"Eerst de haakjes: \(6x - 10\). Dan \(4x\) erbij: \(6x + 4x = 10x\), dus "
               r"\(10x - 10\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de graad van de veelterm \(3x^{2} + 5x - 7\)?",
        opties=[r"\(2\)", r"\(3\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"De graad van een veelterm is de hoogste exponent die erin voorkomt, hier \(2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken de getalwaarde van \(x^{2} - 3x\) als \(x = 5\).",
        opties=[r"\(10\)", r"\(-10\)", r"\(40\)"],
        antwoord=0,
        uitleg=r"\(25 - 15 = 10\). Eerst machtsverheffen, dan vermenigvuldigen, dan aftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken de getalwaarde van \(2a - b\) als \(a = 3\) en \(b = -4\).",
        opties=[r"\(10\)", r"\(2\)", r"\(-10\)"],
        antwoord=0,
        uitleg=r"\(2 \cdot 3 = 6\), en dan min \(-4\), wat hetzelfde is als plus \(4\): "
               r"\(6 + 4 = 10\). Let op de twee mintekens.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(5x - 3 = 2x + 9\)",
        opties=[r"\(x = 4\)", r"\(x = 2\)", r"\(x = 12\)"],
        antwoord=0,
        uitleg=r"Haal de \(x\)'en naar één kant: \(5x - 2x = 9 + 3\), dus \(3x = 12\) en \(x = 4\). "
               r"Controleer: \(5 \cdot 4 - 3 = 17\) en \(2 \cdot 4 + 9 = 17\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(3(x - 2) = 15\)",
        opties=[r"\(x = 7\)", r"\(x = 5\)", r"\(x = 3\)"],
        antwoord=0,
        uitleg=r"Deel eerst door \(3\): \(x - 2 = 5\), dus \(x = 7\). Of werk de haakjes weg: "
               r"\(3x - 6 = 15\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x : 4 = 3\)",
        opties=[r"\(x = 12\)", r"\(x = 0{,}75\)", r"\(x = 7\)"],
        antwoord=0,
        uitleg=r"Vermenigvuldig aan beide kanten met \(4\): \(x = 12\). Delen en vermenigvuldigen "
               r"zijn elkaars omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ik denk aan een getal. Het dubbele ervan plus \(3\) is \(21\). Welke vergelijking "
              r"hoort daarbij?",
        opties=[r"\(2x + 3 = 21\)", r"\(2(x + 3) = 21\)", r"\(x + 3 = 21\)"],
        antwoord=0,
        uitleg=r"Het dubbele is \(2x\), en daar komt \(3\) bij. De oplossing is dan \(x = 9\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een taxi vraagt € \(3\) opstapgeld en € \(2\) per kilometer. Je betaalt € \(19\). "
              r"Hoeveel kilometer reed je?",
        opties=[r"\(8\) km", r"\(9{,}5\) km", r"\(11\) km"],
        antwoord=0,
        uitleg=r"De vergelijking is \(3 + 2x = 19\), dus \(2x = 16\) en \(x = 8\) kilometer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Zes werklui doen een klus in \(4\) dagen. Hoe lang doen twaalf werklui erover?",
        opties=[r"\(2\) dagen", r"\(8\) dagen", r"\(6\) dagen"],
        antwoord=0,
        uitleg=r"Omgekeerd evenredig: dubbel zoveel mensen, half zo lang. Het product blijft gelijk: "
               r"\(6 \cdot 4 = 24\) en \(12 \cdot 2 = 24\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een omgekeerd evenredig verband in een tabel?",
        opties=[
            "Het product van de twee getallen is telkens hetzelfde",
            "Het quotiënt is telkens hetzelfde",
            "Het verschil is telkens hetzelfde",
        ],
        antwoord=0,
        uitleg="Bij omgekeerd evenredig blijft het product gelijk; bij recht evenredig blijft het "
               "quotiënt gelijk. Dat is meteen de manier om ze uit elkaar te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule hoort bij een omgekeerd evenredig verband met factor \(24\)?",
        opties=[r"\(y = 24 : x\)", r"\(y = 24x\)", r"\(y = x + 24\)"],
        antwoord=0,
        uitleg=r"Omgekeerd evenredig betekent \(x \cdot y = 24\), dus \(y = 24 : x\). Recht evenredig "
               r"zou \(y = 24x\) zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met lucifers leg je vierkantjes op een rij: \(1\) vierkant kost \(4\) lucifers, \(2\) "
              r"kosten er \(7\), \(3\) kosten er \(10\). Hoeveel voor \(n\) vierkantjes?",
        opties=[r"\(3n + 1\)", r"\(4n\)", r"\(3n\)"],
        antwoord=0,
        uitleg=r"Het eerste vierkant kost \(4\), elk volgend maar \(3\) extra omdat ze een zijde "
               r"delen. Dus \(3n + 1\). Controleer bij \(n = 3\): \(3 \cdot 3 + 1 = 10\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rij begint met \(2,\ 4,\ 8,\ 16,\ \ldots\) Welk getal komt er daarna?",
        opties=[r"\(32\)", r"\(24\)", r"\(20\)"],
        antwoord=0,
        uitleg=r"Elk getal is het dubbele van het vorige: \(16 \cdot 2 = 32\). Hier komt er niet "
               r"telkens evenveel bij, dus is het geen recht evenredig verband.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee vergelijkingen die dezelfde oplossing hebben, heten gelijkwaardig.",
        antwoord=True,
        uitleg="Juist. Bij elke stap die je zet, maak je een gelijkwaardige vergelijking: eentje die "
               "er anders uitziet maar dezelfde oplossing heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij het oplossen van \(4x = 20\) deelt iemand enkel links door \(4\) en schrijft "
              r"\(x = 20\). Wat is er mis?",
        opties=[
            "Wat je links doet, moet je ook rechts doen",
            "Je mag niet delen bij een vergelijking",
            "Niets, het klopt",
        ],
        antwoord=0,
        uitleg=r"Een vergelijking is een evenwicht. Deel je maar één kant, dan klopt de gelijkheid "
               r"niet meer. Juist is \(x = 20 : 4 = 5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De omtrek van een rechthoek is \(26\) cm en de lengte is \(8\) cm. Welke vergelijking "
              r"gebruik je voor de breedte \(b\)?",
        opties=[r"\(2(8 + b) = 26\)", r"\(8 \cdot b = 26\)", r"\(8 + b = 26\)"],
        antwoord=0,
        uitleg=r"De omtrek is \(2 \cdot (\text{lengte} + \text{breedte})\). Oplossen geeft "
               r"\(8 + b = 13\), dus \(b = 5\) cm.",
    ),
]
