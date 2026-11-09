# -*- coding: utf-8 -*-
"""Tweedegraadsvergelijkingen algebraïsch oplossen.

Wiskunde basis, derde graad (niet voor welzijnswetenschappen: hun fiche
2027_wiskunde_3DO_WEL laat het algebraïsch oplossen weg). De fiche vraagt:
ax² + bx + c = 0 met a ≠ 0, volledige en onvolledige vierkantsvergelijkingen,
oplossingen en oplossingenverzameling V, de discriminant, ontbinden in
factoren, het verband met de nulwaarden van f en met de snijpunten van twee
grafieken, en vraagstukken in een context.

Deel 1: onvolledige vergelijkingen en de discriminant.
Deel 2: oplossen, snijpunten en vraagstukken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Welke vergelijking is een onvolledige vierkantsvergelijking?",
        opties=[r"\(3x^{2} - 12 = 0\)", r"\(x^{2} + 2x + 1 = 0\)", r"\(2x^{2} - x + 5 = 0\)", r"\(3x - 12 = 0\)"],
        antwoord=0,
        uitleg=r"Bij een onvolledige vierkantsvergelijking is \(b = 0\) of \(c = 0\). Hier ontbreekt de term in \(x\). \(3x - 12 = 0\) is van de eerste graad.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} = 49\).",
        opties=[r"\(V = \{-7, 7\}\)", r"\(V = \{7\}\)", r"\(V = \{24{,}5\}\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"Zowel \(7^{2}\) als \((-7)^{2}\) geeft \(49\). Vergeet de negatieve oplossing niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} + 9 = 0\).",
        opties=[r"\(V = \varnothing\)", r"\(V = \{-3, 3\}\)", r"\(V = \{-3\}\)", r"\(V = \{-9\}\)"],
        antwoord=0,
        uitleg=r"\(x^{2} = -9\) heeft geen reële oplossing: een kwadraat is nooit negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 5x = 0\).",
        opties=[r"\(V = \{0, 5\}\)", r"\(V = \{5\}\)", r"\(V = \{-5, 5\}\)", r"\(V = \{0, -5\}\)"],
        antwoord=0,
        uitleg=r"Zet \(x\) buiten haakjes: \(x(x - 5) = 0\). Een product is nul als een factor nul is: \(x = 0\) of \(x = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(x^{2} - 5x = 0\) mag je beide leden door \(x\) delen om \(x = 5\) te vinden.",
        antwoord=False,
        uitleg=r"Delen door \(x\) kan niet als \(x = 0\), en zo verlies je net die oplossing. Ontbind in factoren: \(x(x - 5) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de discriminant van \(ax^{2} + bx + c = 0\)?",
        opties=[r"\(D = b^{2} - 4ac\)", r"\(D = b^{2} + 4ac\)", r"\(D = 4ac - b^{2}\)", r"\(D = b - 4ac\)"],
        antwoord=0,
        uitleg=r"\(D = b^{2} - 4ac\). Het teken van \(D\) zegt hoeveel oplossingen er zijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de discriminant van \(2x^{2} + 3x - 2 = 0\). Schrijf het getal.",
        antwoord=["25", "vijfentwintig"],
        uitleg=r"\(D = 3^{2} - 4 \cdot 2 \cdot (-2) = 9 + 16 = 25\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De discriminant van een vierkantsvergelijking is negatief. Hoeveel reële oplossingen zijn er?",
        opties=[r"geen", r"één", r"twee", r"oneindig veel"],
        antwoord=0,
        uitleg=r"\(D < 0\): geen oplossingen. \(D = 0\): één oplossing. \(D > 0\): twee oplossingen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(D = 0\), dan raakt de parabool \(y = ax^{2} + bx + c\) de \(x\)-as in haar top.",
        antwoord=True,
        uitleg=r"Eén oplossing betekent één nulwaarde, en die valt samen met de \(x\)-coördinaat van de top.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke formule vind je de oplossingen als \(D > 0\)?",
        opties=[r"\(x = \dfrac{-b \pm \sqrt{D}}{2a}\)", r"\(x = \dfrac{b \pm \sqrt{D}}{2a}\)", r"\(x = \dfrac{-b \pm D}{2a}\)", r"\(x = -b \pm \dfrac{\sqrt{D}}{2a}\)"],
        antwoord=0,
        uitleg=r"\(x_{1,2} = \dfrac{-b \pm \sqrt{D}}{2a}\). De hele teller staat boven de breukstreep.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel oplossingen heeft \(x^{2} - 6x + 9 = 0\)?",
        opties=[r"één", r"twee", r"geen", r"drie"],
        antwoord=0,
        uitleg=r"\(D = 36 - 36 = 0\). Het is ook \((x - 3)^{2} = 0\), met als enige oplossing \(x = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel oplossingen heeft \(x^{2} + x + 1 = 0\)?",
        opties=[r"geen", r"één", r"twee", r"oneindig veel"],
        antwoord=0,
        uitleg=r"\(D = 1 - 4 = -3 < 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(4x^{2} = 100\). Wat is de positieve oplossing? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(x^{2} = 25\), dus \(x = 5\) of \(x = -5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \((x - 2)(x + 7) = 0\) heeft als oplossingen \(2\) en \(-7\).",
        antwoord=True,
        uitleg=r"Een product is nul als een van de factoren nul is: \(x - 2 = 0\) of \(x + 7 = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \((x - 2)(x + 7) = 8\) heeft als oplossingen \(10\) en \(1\).",
        antwoord=False,
        uitleg=r"De regel van het nulproduct werkt enkel als het rechterlid \(0\) is. Werk eerst uit: \(x^{2} + 5x - 22 = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke ontbinding in factoren is juist?",
        opties=[r"\(x^{2} - 16 = (x - 4)(x + 4)\)", r"\(x^{2} - 16 = (x - 4)^{2}\)", r"\(x^{2} - 16 = (x - 8)(x + 2)\)", r"\(x^{2} - 16 = x(x - 16)\)"],
        antwoord=0,
        uitleg=r"Een verschil van twee kwadraten: \(a^{2} - b^{2} = (a - b)(a + b)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ontbind in factoren: \(x^{2} + 5x + 6\).",
        opties=[r"\((x + 2)(x + 3)\)", r"\((x + 1)(x + 6)\)", r"\((x - 2)(x - 3)\)", r"\((x + 5)(x + 1)\)"],
        antwoord=0,
        uitleg=r"Zoek twee getallen met som \(5\) en product \(6\): \(2\) en \(3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(-x^{2} + 4 = 0\) heeft twee oplossingen.",
        antwoord=True,
        uitleg=r"\(x^{2} = 4\), dus \(x = -2\) of \(x = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De discriminant van \(x^{2} + 4x + c = 0\) is nul. Hoeveel is \(c\)?",
        opties=[r"\(4\)", r"\(16\)", r"\(-4\)", r"\(2\)"],
        antwoord=0,
        uitleg=r"\(D = 16 - 4c = 0 \iff c = 4\). Dan is het \((x + 2)^{2} = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vierkantsvergelijking kan drie verschillende oplossingen hebben.",
        antwoord=False,
        uitleg=r"Hoogstens twee: een parabool snijdt de \(x\)-as hoogstens twee keer.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 2x - 15 = 0\).",
        opties=[r"\(V = \{-3, 5\}\)", r"\(V = \{3, -5\}\)", r"\(V = \{-3, -5\}\)", r"\(V = \{2, 15\}\)"],
        antwoord=0,
        uitleg=r"\(D = 4 + 60 = 64\), \(x = \dfrac{2 \pm 8}{2}\): \(x = 5\) of \(x = -3\). Ook: \((x - 5)(x + 3) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2x^{2} + 3x - 2 = 0\).",
        opties=[r"\(V = \left\{-2, \tfrac{1}{2}\right\}\)", r"\(V = \left\{2, -\tfrac{1}{2}\right\}\)", r"\(V = \{-2, 2\}\)", r"\(V = \{-8, 2\}\)"],
        antwoord=0,
        uitleg=r"\(D = 25\), \(x = \dfrac{-3 \pm 5}{4}\): \(x = \dfrac{2}{4} = \dfrac{1}{2}\) of \(x = \dfrac{-8}{4} = -2\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(x^{2} + 2x - 24 = 0\). Wat is de positieve oplossing? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\((x + 6)(x - 4) = 0\), dus \(x = -6\) of \(x = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(3x^{2} - 6x = 0\).",
        opties=[r"\(V = \{0, 2\}\)", r"\(V = \{2\}\)", r"\(V = \{0, -2\}\)", r"\(V = \{0, 3\}\)"],
        antwoord=0,
        uitleg=r"\(3x(x - 2) = 0\), dus \(x = 0\) of \(x = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de nulwaarden van \(f(x) = x^{2} - 7x + 10\)?",
        opties=[r"\(2\) en \(5\)", r"\(-2\) en \(-5\)", r"\(7\) en \(10\)", r"\(1\) en \(10\)"],
        antwoord=0,
        uitleg=r"De nulwaarden van \(f\) zijn de oplossingen van \(f(x) = 0\): \((x - 2)(x - 5) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe vind je de snijpunten van de grafieken van \(f\) en \(g\)?",
        opties=[
            r"Je lost \(f(x) = g(x)\) op en berekent bij elke oplossing de functiewaarde.",
            r"Je lost \(f(x) = 0\) en \(g(x) = 0\) op en neemt alle oplossingen samen.",
            r"Je telt \(f(x)\) en \(g(x)\) op en zoekt de nulwaarden.",
            r"Je zoekt de toppen van beide grafieken.",
        ],
        antwoord=0,
        uitleg=r"In een snijpunt hebben beide functies dezelfde \(x\) en dezelfde functiewaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij welke \(x\)-waarden snijden \(f(x) = x^{2}\) en \(g(x) = x + 6\) elkaar?",
        opties=[r"\(-2\) en \(3\)", r"\(2\) en \(-3\)", r"\(0\) en \(6\)", r"\(-6\) en \(1\)"],
        antwoord=0,
        uitleg=r"\(x^{2} = x + 6 \iff x^{2} - x - 6 = 0 \iff (x - 3)(x + 2) = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De parabool \(y = x^{2} + 1\) en de rechte \(y = 0\) hebben geen snijpunt.",
        antwoord=True,
        uitleg=r"\(x^{2} + 1 = 0\) heeft geen oplossing. De parabool ligt helemaal boven de \(x\)-as.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een rechthoek is \(3\) cm langer dan breed en heeft een oppervlakte van \(40\ \text{cm}^{2}\). Hoeveel centimeter is de breedte? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(x(x + 3) = 40 \iff x^{2} + 3x - 40 = 0 \iff (x + 8)(x - 5) = 0\). Een breedte is positief: \(5\) cm.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een vraagstuk over een lengte mag je een negatieve oplossing van de vergelijking als antwoord geven.",
        antwoord=False,
        uitleg=r"Een lengte kan niet negatief zijn. Je formuleert het antwoord binnen de context en laat die oplossing vallen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een steen valt van een brug. Na \(t\) seconden is hij \(5t^{2}\) meter gevallen. Na hoeveel seconden is hij \(45\) m gevallen? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(5t^{2} = 45 \iff t^{2} = 9 \iff t = 3\) (de negatieve tijd valt weg).",
    ),
    dict(
        type="invultekst",
        vraag=r"De som van een getal en zijn kwadraat is \(30\). Het getal is positief. Welk getal is het? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(x^{2} + x = 30 \iff x^{2} + x - 30 = 0 \iff (x + 6)(x - 5) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vierkant tuintje krijgt rondom een pad van \(1\) m breed. Tuin en pad samen zijn \(49\ \text{m}^{2}\). Welke vergelijking past, met \(x\) de zijde van het tuintje?",
        opties=[r"\((x + 2)^{2} = 49\)", r"\((x + 1)^{2} = 49\)", r"\(x^{2} + 2 = 49\)", r"\(x^{2} + 4 = 49\)"],
        antwoord=0,
        uitleg=r"Het pad ligt aan beide kanten, dus de zijde wordt \(x + 2\). Dan is \(x + 2 = 7\) en \(x = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(x^{2} = 3x\) heeft dezelfde oplossingen als \(x = 3\).",
        antwoord=False,
        uitleg=r"\(x^{2} - 3x = 0 \iff x(x - 3) = 0\): ook \(x = 0\) is een oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \((x - 1)^{2} = 16\).",
        opties=[r"\(V = \{-3, 5\}\)", r"\(V = \{5\}\)", r"\(V = \{-5, 3\}\)", r"\(V = \{17\}\)"],
        antwoord=0,
        uitleg=r"\(x - 1 = 4\) of \(x - 1 = -4\), dus \(x = 5\) of \(x = -3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal wordt opgegooid: \(h(t) = -5t^{2} + 20t\). Op welke tijdstippen is de bal op \(15\) m hoogte?",
        opties=[r"na \(1\) s en na \(3\) s", r"enkel na \(3\) s", r"na \(2\) s en na \(4\) s", r"nooit"],
        antwoord=0,
        uitleg=r"\(-5t^{2} + 20t = 15 \iff t^{2} - 4t + 3 = 0 \iff (t - 1)(t - 3) = 0\). Eén keer op weg naar boven, één keer naar beneden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(h(t) = -5t^{2} + 20t\) komt de bal na \(4\) seconden terug op de grond.",
        antwoord=True,
        uitleg=r"\(-5t^{2} + 20t = 0 \iff -5t(t - 4) = 0\): \(t = 0\) (de worp) en \(t = 4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De rechte \(y = 2x\) en de parabool \(y = x^{2} + 1\) raken elkaar in één punt.",
        antwoord=True,
        uitleg=r"\(x^{2} + 1 = 2x \iff x^{2} - 2x + 1 = 0 \iff (x - 1)^{2} = 0\): één gemeenschappelijk punt, \((1, 2)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} + 4x - 1 = 0\). Afgerond op twee cijfers na de komma zijn de oplossingen ...",
        opties=[r"\(0{,}24\) en \(-4{,}24\)", r"\(-0{,}24\) en \(4{,}24\)", r"\(2{,}24\) en \(-2{,}24\)", r"\(1{,}00\) en \(-5{,}00\)"],
        antwoord=0,
        uitleg=r"\(D = 16 + 4 = 20\), \(x = \dfrac{-4 \pm \sqrt{20}}{2} = -2 \pm \sqrt{5}\), dus \(\approx 0{,}24\) en \(\approx -4{,}24\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bedrijf heeft winst \(W(q) = -q^{2} + 50q - 400\), met \(q\) het aantal stuks. Bij welke aantallen is de winst precies nul?",
        opties=[r"\(10\) en \(40\)", r"\(20\) en \(30\)", r"\(25\)", r"\(-10\) en \(-40\)"],
        antwoord=0,
        uitleg=r"\(-q^{2} + 50q - 400 = 0 \iff q^{2} - 50q + 400 = 0 \iff (q - 10)(q - 40) = 0\).",
    ),
]
