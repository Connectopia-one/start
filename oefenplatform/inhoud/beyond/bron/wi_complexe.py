# -*- coding: utf-8 -*-
"""Complexe getallen.

Het onderdeel "Complexe getallen" van fiche G2, achttien procent van dat
examen. Er zijn drie voorstellingswijzen die je door elkaar moet kunnen
gebruiken: het vlak van Gauss, de cartesische vorm en de goniometrische vorm.

Deel 1 is de cartesische vorm en het vlak van Gauss.
Deel 2 is de goniometrische vorm, de formule van de Moivre en het oplossen
van vergelijkingen in de complexe getallen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de imaginaire eenheid \(i\)?",
        opties=[
            r"het getal met \(i^{2} = -1\)",
            r"het getal met \(i^{2} = 1\)",
            r"het getal \(\sqrt{1}\)",
            r"een ander woord voor \(\infty\)",
        ],
        antwoord=0,
        uitleg=r"Met \(i\) erbij heeft elke tweedegraadsvergelijking oplossingen, ook als de discriminant negatief is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het reëel deel van \(3 - 5i\)?",
        opties=[r"\(3\)", r"\(-5\)", r"\(5\)", r"\(-3\)"],
        antwoord=0,
        uitleg=r"Het reëel deel is het getal zonder \(i\). Het imaginair deel is \(-5\), dus zonder de \(i\) erbij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(i^{4}\)? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg=r"\(i^{2} = -1\) en \((-1)^{2} = 1\). De machten van \(i\) herhalen zich dus om de vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk reëel getal is ook een complex getal.",
        antwoord=True,
        uitleg="Het is dan een complex getal met imaginair deel nul. De reële getallen liggen op de horizontale as van het vlak van Gauss.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het toegevoegde complexe getal van \(2 + 3i\)?",
        opties=[r"\(2 - 3i\)", r"\(-2 + 3i\)", r"\(-2 - 3i\)", r"\(3 + 2i\)"],
        antwoord=0,
        uitleg="Alleen het imaginair deel wisselt van teken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(|3 + 4i|\)?",
        opties=[r"\(5\)", r"\(7\)", r"\(12\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"De modulus is de afstand tot de oorsprong: \(\sqrt{9 + 16} = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan twee complexe getallen van klein naar groot ordenen.",
        antwoord=False,
        uitleg="De complexe getallen zijn niet geordend. Hun moduli kan je wel vergelijken, maar de getallen zelf niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het imaginair deel van \(7 - 2i\)? Schrijf het getal.",
        antwoord=["-2", "min 2"],
        uitleg=r"Het imaginair deel is het getal bij \(i\), dus \(-2\), en niet \(-2i\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\left(2 + 3i\right) + \left(1 - i\right)\)?",
        opties=[r"\(3 + 2i\)", r"\(3 + 4i\)", r"\(1 + 2i\)", r"\(2 + 2i\)"],
        antwoord=0,
        uitleg="Je telt de reële delen samen en de imaginaire delen samen, net als bij vectoren.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(z \cdot \overline{z}\) is altijd een reëel getal.",
        antwoord=True,
        uitleg=r"Je krijgt \(|z|^{2}\), dus een niet-negatief reëel getal. Daarom gebruik je de toegevoegde net om te delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe deel je door een complex getal in cartesische vorm?",
        opties=[
            "teller en noemer vermenigvuldigen met de toegevoegde van de noemer",
            "teller en noemer vermenigvuldigen met de noemer zelf, onveranderd",
            "het reëel deel en het imaginair deel apart delen",
            "de modulus delen en het argument gelijk laten",
        ],
        antwoord=0,
        uitleg="De noemer wordt dan reëel en je kan gewoon verder rekenen. Apart delen werkt niet, net zoals bij een breuk met een wortel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(|5i|\)? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="Het punt ligt vijf eenheden boven de oorsprong op de imaginaire as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de verticale as van het vlak van Gauss?",
        opties=[
            "het imaginair deel van het getal",
            "het reëel deel van het getal",
            "de modulus van het getal",
            "het argument van het getal",
        ],
        antwoord=0,
        uitleg=r"Horizontaal \(a\), verticaal \(b\). Elk getal \(z = a + bi\) is dus een punt in het vlak.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuiver imaginair getal heeft reëel deel nul.",
        antwoord=True,
        uitleg="Het ligt dan op de verticale as. Een zuiver reëel getal heeft net imaginair deel nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\left(1 + i\right)^{2}\)?",
        opties=[r"\(2i\)", r"\(2\)", r"\(-2\)", r"\(1 + 2i\)"],
        antwoord=0,
        uitleg=r"\(1 + 2i + i^{2} = 1 + 2i - 1 = 2i\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het argument van een complex getal?",
        opties=[
            "de hoek met de positieve reële as",
            "de afstand tot de oorsprong van het vlak",
            "het reëel deel gedeeld door het imaginair deel",
            "het aantal cijfers na de komma in de modulus",
        ],
        antwoord=0,
        uitleg="De afstand tot de oorsprong is net de modulus. Samen leggen modulus en argument het getal volledig vast.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(i^{3} = i\).",
        antwoord=False,
        uitleg=r"\(i^{3} = i^{2} \cdot i = -i\). Pas \(i^{5}\) is weer \(i\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(i^{3}\)? Schrijf het antwoord.",
        antwoord=["-i", "min i"],
        uitleg=r"\(i^{2} = -1\), en dat maal \(i\) geeft \(-i\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de optelling van twee complexe getallen voor in het vlak van Gauss?",
        opties=[
            "dezelfde constructie als het optellen van twee vectoren",
            "een draaiing van het ene getal rond het andere getal",
            "een vermenigvuldiging van de twee afstanden",
            "een spiegeling om de horizontale reële as",
        ],
        antwoord=0,
        uitleg="Je legt de pijlen achter elkaar. Draaien hoort bij vermenigvuldigen, niet bij optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met het punt \(z\) in het vlak van Gauss als je \(\overline{z}\) neemt?",
        opties=[
            "het spiegelt om de horizontale as",
            "het spiegelt om de verticale as",
            "het draait een halve slag rond de oorsprong",
            "het blijft precies op dezelfde plaats staan",
        ],
        antwoord=0,
        uitleg="Alleen het imaginair deel wisselt van teken, dus het punt klapt om over de reële as.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de goniometrische vorm van een complex getal eruit?",
        opties=[
            r"\(z = r\left(\cos\theta + i\sin\theta\right)\)",
            r"\(z = a\cos\theta + b\sin\theta\)",
            r"\(z = r\,\theta + i\,r\)",
            r"\(z = \cos r + i\sin r\)",
        ],
        antwoord=0,
        uitleg="Zo zie je de twee gegevens die een complex getal vastleggen meteen staan: hoe ver en onder welke hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vermenigvuldigt twee complexe getallen in goniometrische vorm. Wat doe je?",
        opties=[
            "de moduli vermenigvuldigen en de argumenten optellen",
            "de moduli optellen en de argumenten vermenigvuldigen",
            "de moduli en de argumenten allebei vermenigvuldigen",
            "de moduli en de argumenten allebei bij elkaar optellen",
        ],
        antwoord=0,
        uitleg="Vermenigvuldigen is dus uitrekken en draaien tegelijk. Bij delen deel je de moduli en trek je de argumenten af.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel oplossingen heeft \(z^{3} = 8\) in \(\mathbb{C}\)? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"\(z^{n} = a\) heeft er altijd precies \(n\). Twee is er één van; de twee andere zijn niet reëel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het delen van twee complexe getallen in goniometrische vorm trek je de argumenten af.",
        antwoord=True,
        uitleg="En de moduli deel je. Delen is dus krimpen en terugdraaien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de formule van de Moivre?",
        opties=[
            r"\(z^{n} = r^{n}\left(\cos n\theta + i\sin n\theta\right)\)",
            r"\(z^{n} = n\,r\left(\cos\theta^{n} + i\sin\theta^{n}\right)\)",
            r"\(z^{n} = r^{n}\left(\cos\theta^{n} + i\sin\theta^{n}\right)\)",
            r"\(z^{n} = r^{n}\left(\cos\theta + i\sin\theta\right)\)",
        ],
        antwoord=0,
        uitleg="Ze volgt rechtstreeks uit de regel voor vermenigvuldigen, n keer na elkaar toegepast.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waar liggen de \(n\) oplossingen van \(z^{n} = a\) in het vlak van Gauss?",
        opties=[
            "op één cirkel, gelijkmatig over de omtrek verdeeld",
            "op één rechte door de oorsprong van het hele vlak",
            "allemaal op de horizontale reële as samen",
            "willekeurig verspreid, zonder vast patroon",
        ],
        antwoord=0,
        uitleg="Ze hebben allemaal dezelfde modulus, en hun argumenten verschillen telkens evenveel. Ze vormen dus de hoekpunten van een regelmatige veelhoek.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een tweedegraadsvergelijking met \(D < 0\) heeft geen oplossingen in \(\mathbb{C}\).",
        antwoord=False,
        uitleg=r"Ze heeft er net twee. Daarvoor werden de complexe getallen ingevoerd. In \(\mathbb{R}\) zijn er inderdaad geen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op in \(\mathbb{C}\): \(x^{2} + 1 = 0\). Schrijf de oplossing met het plusteken.",
        antwoord=["i"],
        uitleg=r"\(x^{2} = -1\), dus \(x = i\) of \(x = -i\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de oplossingen van \(x^{2} - 2x + 5 = 0\)?",
        opties=[
            r"\(1 + 2i\) en \(1 - 2i\)",
            r"\(2 + i\) en \(2 - i\)",
            r"\(-1 + 2i\) en \(-1 - 2i\)",
            r"\(1 + 4i\) en \(1 - 4i\)",
        ],
        antwoord=0,
        uitleg=r"\(D = 4 - 20 = -16\), dus \(\sqrt{D} = 4i\), en \(\dfrac{2 \pm 4i}{2} = 1 \pm 2i\).",
    ),
    dict(
        type="waarofniet",
        vraag="De twee complexe oplossingen van een tweedegraadsvergelijking met reële coëfficiënten zijn elkaars toegevoegde.",
        antwoord=True,
        uitleg="Ze verschillen alleen in het teken voor de wortel uit de discriminant, en die wortel is zuiver imaginair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je van de cartesische naar de goniometrische vorm?",
        opties=[
            r"je berekent \(r = \sqrt{a^{2} + b^{2}}\) en \(\theta\) uit \(\tan\theta = \dfrac{b}{a}\)",
            r"je berekent \(\cos a\) en \(\sin a\)",
            r"je vermenigvuldigt \(a\) met \(b\)",
            r"je verwisselt \(a\) en \(b\) van plaats",
        ],
        antwoord=0,
        uitleg="Let bij het argument altijd op het kwadrant waarin het punt ligt; de tangens alleen volstaat niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel graden is het argument van \(i\)? Schrijf het getal.",
        antwoord=["90", "negentig"],
        uitleg="Het punt ligt recht boven de oorsprong, dus een kwart draai vanaf de positieve reële as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de goniometrische vorm handig bij machtsverheffen?",
        opties=[
            r"omdat je dan alleen \(r\) tot de macht \(n\) verheft en \(\theta\) met \(n\) vermenigvuldigt",
            r"omdat \(\cos\theta\) en \(\sin\theta\) altijd tussen \(-1\) en \(1\) liggen",
            "omdat je dan helemaal geen rekenregel meer nodig hebt bij machten",
            "omdat het resultaat dan altijd een reëel getal wordt",
        ],
        antwoord=0,
        uitleg=r"Probeer \(\left(1 + i\right)^{10}\) eens in cartesische vorm en je ziet het verschil meteen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(|z_{1} \cdot z_{2}| = |z_{1}| + |z_{2}|\).",
        antwoord=False,
        uitleg=r"Het is net \(|z_{1}| \cdot |z_{2}|\). Het zijn de argumenten die worden opgeteld.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel \(n\)-de machtswortels heeft een complex getal dat niet nul is?",
        opties=[
            r"precies \(n\)",
            r"precies \(2\)",
            r"precies \(1\)",
            r"oneindig veel",
        ],
        antwoord=0,
        uitleg=r"In \(\mathbb{R}\) zijn dat er hoogstens twee. In \(\mathbb{C}\) zijn het er altijd \(n\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werden de complexe getallen ingevoerd?",
        opties=[
            "omdat niet elke vergelijking een oplossing had in de reële getallen",
            "omdat de reële getallen niet geordend konden worden",
            "omdat men de oppervlakte van een cirkel wou berekenen",
            "omdat men wortels uit positieve getallen eenvoudiger wou schrijven",
        ],
        antwoord=0,
        uitleg=r"Een getal met \(i^{2} = -1\) bestond niet. Door het toe te voegen, kreeg elke veeltermvergelijking oplossingen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een veelterm van graad \(n\) heeft in \(\mathbb{C}\) precies \(n\) nulwaarden, als je ze met hun multipliciteit telt.",
        antwoord=True,
        uitleg=r"Dat is de hoofdstelling van de algebra. In \(\mathbb{R}\) kunnen het er minder zijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(|-3|\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De modulus is een afstand en dus nooit negatief. Voor een reëel getal is ze de absolute waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat doet een vermenigvuldiging met \(i\) met een punt in het vlak van Gauss?",
        opties=[
            "het draait een kwart slag rond de oorsprong",
            "het spiegelt om de horizontale reële as",
            "het schuift één eenheid naar boven op",
            "het verdubbelt de afstand tot de oorsprong",
        ],
        antwoord=0,
        uitleg=r"\(|i| = 1\) en \(\arg i = 90^\circ\), dus de afstand blijft en de hoek groeit met een kwart draai.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk argument heeft een negatief reëel getal?",
        opties=[
            r"\(180^\circ\)",
            r"\(0^\circ\)",
            r"\(90^\circ\)",
            r"\(270^\circ\)",
        ],
        antwoord=0,
        uitleg="Het ligt links van de oorsprong op de reële as, dus een halve draai vanaf de positieve kant.",
    ),
]
