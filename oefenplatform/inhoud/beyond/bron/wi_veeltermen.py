# -*- coding: utf-8 -*-
r"""Veeltermen: deelbaarheid, de reststelling en het rekenschema van Horner.

Het onderdeel "Deelbaarheid" van de analysefiche G1, aangevuld met het
ontbinden in factoren dat daar uitdrukkelijk bij staat. De fiche vraagt dit
alleen in opgaven zonder context, dus hier staan geen verhaaltjes bij.

Deel 1 is de deling zelf: euclidisch delen, de reststelling en Horner.
Deel 2 is ontbinden in factoren en nulwaarden zoeken.

In echte wiskundige notatie, tussen \( en \); zie oefenplatform/lib/wiskunde.ts.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Je deelt \(A\) door \(B\) en krijgt een quotiënt \(Q\) en een rest \(R\). Wat geldt altijd?",
        opties=[
            r"\(A=B\cdot Q+R\) met \(\deg R<\deg B\)",
            r"\(A=B\cdot Q+R\) met \(\deg R<\deg Q\)",
            r"\(A=B+Q\cdot R\) met \(\deg R<\deg B\)",
            r"\(A=B\cdot Q-R\) met \(\deg R<\deg A\)",
        ],
        antwoord=0,
        uitleg=r"Dat verband is de controle op elke deling. En zolang \(\deg R\geq\deg B\) kan je verder delen, dus je stopt pas wanneer de rest lager in graad staat dan de deler.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je deelt door een tweedegraadsveelterm. Welke graad heeft de rest hoogstens? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"De graad van de rest ligt strikt onder die van de deler, dus de rest is hoogstens van de vorm \(ax+b\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De rest bij de deling van \(P(x)\) door \(x-a\) is gelijk aan \(P(a)\).",
        antwoord=True,
        uitleg=r"Dat is de reststelling. Je hoeft dus niet te delen om de rest te kennen: invullen volstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de rest bij \(\left(x^{3}-2x^{2}+3x-4\right):(x-1)\)?",
        opties=[r"\(-2\)", r"\(-4\)", r"\(0\)", r"\(2\)"],
        antwoord=0,
        uitleg=r"\(P(1)=1-2+3-4=-2\). De reststelling geeft het antwoord zonder te delen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvoor gebruik je het rekenschema van Horner?",
        opties=[
            r"om te delen door een tweeterm \(x-a\)",
            r"om een tweedegraadsvergelijking op te lossen",
            r"om een breuk met wortels te vereenvoudigen",
            r"om de afgeleide van een veelterm te vinden",
        ],
        antwoord=0,
        uitleg=r"Horner is een snelle schrijfwijze voor precies die ene deling. Voor andere delers val je terug op de gewone euclidische deling.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Je kan Horner ook gebruiken om te delen door \(x^{2}+1\).",
        antwoord=False,
        uitleg=r"Horner werkt enkel bij een deler \(x-a\). Voor een deler van hogere graad gebruik je de euclidische deling.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(P(x)=x^{3}-8\). Hoeveel is \(P(2)\)? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"\(2^{3}-8=0\), dus \(x-2\) is een deler van \(P\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat weet je als \(P(a)=0\)?",
        opties=[
            r"\(x-a\) is een deler van \(P\)",
            r"\(x+a\) is een deler van \(P\)",
            r"\(P\) heeft graad \(0\)",
            r"\(P\) is overal gelijk aan \(0\)",
        ],
        antwoord=0,
        uitleg=r"Volgens de reststelling is de rest dan \(0\), en een deling met rest \(0\) gaat op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een veelterm van graad \(n\) heeft hoogstens \(n\) reële nulwaarden.",
        antwoord=True,
        uitleg=r"Elke nulwaarde levert een factor van graad \(1\) op, en samen kunnen die de graad niet overschrijden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je deelt met Horner door \(x+3\). Welk getal zet je links in het schema?",
        opties=[r"\(-3\)", r"\(3\)", r"\(-1\)", r"\(0\)"],
        antwoord=0,
        uitleg=r"\(x+3=x-(-3)\), dus \(a=-3\). Dat tekenfoutje is de klassieker van dit hoofdstuk.",
    ),
    dict(
        type="invultekst",
        vraag=r"Er geldt \(P(a)=7\). Wat is de rest bij \(P(x):(x-a)\)? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"De reststelling zegt dat de rest net die functiewaarde is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je deelt een veelterm van graad \(5\) door een veelterm van graad \(2\). Welke graad heeft het quotiënt?",
        opties=[r"\(3\)", r"\(2\)", r"\(4\)", r"\(5\)"],
        antwoord=0,
        uitleg=r"De graden trekken af: \(5-2=3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Gaat een deling van veeltermen op, dan is de rest gelijk aan de graad van de deler.",
        antwoord=False,
        uitleg=r"Gaat een deling op, dan is de rest \(0\). Een rest is een veelterm, geen graad.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel getallen zet je bovenaan in het schema van Horner voor een derdegraadsveelterm?",
        opties=[r"\(4\)", r"\(3\)", r"\(2\)", r"\(5\)"],
        antwoord=0,
        uitleg=r"Alle coëfficiënten van \(x^{3}\) tot en met de constante term, dus vier. Een ontbrekende graad schrijf je als \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt het laatste getal onderaan het schema van Horner voor?",
        opties=[
            r"de rest van de deling",
            r"de hoogste term van het quotiënt",
            r"de nulwaarde van de veelterm",
            r"de graad van het quotiënt",
        ],
        antwoord=0,
        uitleg=r"De getallen links daarvan zijn de coëfficiënten van het quotiënt. Het laatste is de rest, en dus ook \(P(a)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke \(m\) is \(x^{3}+mx^{2}-4x+6\) deelbaar door \(x-2\)?",
        opties=[r"\(m=-\tfrac{3}{2}\)", r"\(m=\tfrac{3}{2}\)", r"\(m=-3\)", r"\(m=3\)"],
        antwoord=0,
        uitleg=r"Deelbaar wil zeggen \(P(2)=0\): \(8+4m-8+6=0\), dus \(4m=-6\) en \(m=-\tfrac{3}{2}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de rest bij \(\left(2x^{3}-x+5\right):(x+2)\)? Schrijf het getal.",
        antwoord=["-9", "min 9"],
        uitleg=r"\(P(-2)=2\cdot(-8)+2+5=-9\). Vergeet het minteken van \(a\) niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het quotiënt bij \(\left(x^{3}-6x^{2}+11x-6\right):(x-1)\)?",
        opties=[
            r"\(x^{2}-5x+6\)",
            r"\(x^{2}-7x+6\)",
            r"\(x^{2}-5x-6\)",
            r"\(x^{2}-6x+11\)",
        ],
        antwoord=0,
        uitleg=r"Horner met \(a=1\) geeft \(1,\,-5,\,6\) en rest \(0\). De volledige ontbinding is \((x-1)(x-2)(x-3)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat krijg je bij \(\left(x^{3}+1\right):\left(x^{2}+1\right)\)?",
        opties=[
            r"quotiënt \(x\), rest \(-x+1\)",
            r"quotiënt \(x\), rest \(1\)",
            r"quotiënt \(x+1\), rest \(0\)",
            r"quotiënt \(x-1\), rest \(x+2\)",
        ],
        antwoord=0,
        uitleg=r"\(x\cdot\left(x^{2}+1\right)=x^{3}+x\), en \(x^{3}+1-\left(x^{3}+x\right)=-x+1\). Die rest heeft graad \(1\), lager dan de deler, dus je stopt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je deelt \(P(x)=x^{5}-2x^{3}+x\) met Horner door \(x-1\). Hoeveel getallen zet je bovenaan? Schrijf het getal.",
        antwoord=["6"],
        uitleg=r"Van graad \(5\) tot en met de constante term zijn dat er zes: \(1,\,0,\,-2,\,0,\,1,\,0\). De ontbrekende graden schrijf je als \(0\) en mag je niet overslaan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Ontbind \(x^{2}-9\) in factoren.",
        opties=[
            r"\((x-3)(x+3)\)",
            r"\((x-3)(x-3)\)",
            r"\((x+3)(x+3)\)",
            r"\((x-9)(x+1)\)",
        ],
        antwoord=0,
        uitleg=r"Het verschil van twee kwadraten: \(a^{2}-b^{2}=(a-b)(a+b)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ontbind \(2x^{3}-3x^{2}-8x+12\) volledig.",
        opties=[
            r"\((x-2)(x+2)(2x-3)\)",
            r"\((x-2)(x+2)(2x+3)\)",
            r"\((x-1)(x+2)(2x-6)\)",
            r"\((x-2)(x+3)(2x-2)\)",
        ],
        antwoord=0,
        uitleg=r"\(P(2)=0\), dus \(x-2\) is een deler; Horner geeft \(2x^{2}+x-6\), en dat is \((x+2)(2x-3)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel reële nulwaarden heeft \(x^{2}-4\)? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"\(x^{2}-4=(x-2)(x+2)\), dus \(2\) en \(-2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(x^{2}+4\) valt in \(\mathbb{R}\) uiteen in twee factoren van graad \(1\).",
        antwoord=False,
        uitleg=r"De discriminant is \(-16\), dus er zijn geen reële nulwaarden en de veelterm blijft onontbindbaar in \(\mathbb{R}\). In \(\mathbb{C}\) lukt het wel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Zonder de gemeenschappelijke factor af in \(3x^{3}-6x^{2}\).",
        opties=[
            r"\(3x^{2}(x-2)\)",
            r"\(3x^{2}(x-6)\)",
            r"\(3x\left(x^{2}-2x\right)\)",
            r"\(x^{2}(3x-6x)\)",
        ],
        antwoord=0,
        uitleg=r"\(3\) en \(x^{2}\) zitten in beide termen. Wat overblijft is \(x-2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ontbind \(x^{3}-8\).",
        opties=[
            r"\((x-2)\left(x^{2}+2x+4\right)\)",
            r"\((x-2)\left(x^{2}-2x+4\right)\)",
            r"\((x-2)\left(x^{2}+2x-4\right)\)",
            r"\((x+2)\left(x^{2}+2x+4\right)\)",
        ],
        antwoord=0,
        uitleg=r"\(P(2)=0\), dus \(x-2\) is een deler, en Horner geeft \(x^{2}+2x+4\). Algemeen: \(a^{3}-b^{3}=(a-b)\left(a^{2}+ab+b^{2}\right)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de nulwaarde van \(2x-6\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(2x-6=0\) geeft \(x=3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een veelterm ontbinden in factoren is een manier om haar nulwaarden te vinden.",
        antwoord=True,
        uitleg=r"Een product is \(0\) zodra één factor \(0\) is, dus elke factor van graad \(1\) levert meteen een nulwaarde op.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Neem termen samen in \(ax+ay+bx+by\).",
        opties=[
            r"\((a+b)(x+y)\)",
            r"\((a+x)(b+y)\)",
            r"\(ab+xy\)",
            r"\((a+b+x+y)^{2}\)",
        ],
        antwoord=0,
        uitleg=r"Eerst \(a(x+y)+b(x+y)\), dan de gemeenschappelijke factor \(x+y\) afzonderen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de discriminant van \(x^{2}-5x+6\)? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg=r"\(D=b^{2}-4ac=25-24=1\). Positief, dus twee reële nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ontbind \(x^{2}-5x+6\).",
        opties=[
            r"\((x-2)(x-3)\)",
            r"\((x+2)(x+3)\)",
            r"\((x-1)(x-6)\)",
            r"\((x-2)(x+3)\)",
        ],
        antwoord=0,
        uitleg=r"Je zoekt twee getallen met som \(5\) en product \(6\): dat zijn \(2\) en \(3\), allebei met een minteken in de factor.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een tweedegraadsveelterm met \(D<0\) heeft twee reële nulwaarden.",
        antwoord=False,
        uitleg=r"Bij \(D<0\) zijn er geen reële nulwaarden en snijdt of raakt de parabool de \(x\)-as niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je zoekt een gehele nulwaarde van \(2x^{3}-3x^{2}-8x+12\). Welke getallen probeer je?",
        opties=[
            r"de delers van \(12\)",
            r"de delers van \(2\)",
            r"alle gehele getallen van \(-12\) tot \(12\)",
            r"de kwadraten van de coëfficiënten",
        ],
        antwoord=0,
        uitleg=r"Een gehele nulwaarde moet de constante term delen. Dat zijn er hier twaalf om te testen, en \(x=2\) lukt meteen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \((a-b)^{2}=a^{2}-2ab+b^{2}\).",
        antwoord=True,
        uitleg=r"Alleen de middelste term wisselt van teken tegenover \((a+b)^{2}=a^{2}+2ab+b^{2}\); \((-b)^{2}\) blijft positief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Schrijf \(4x^{2}-12x+9\) als één kwadraat.",
        opties=[r"\((2x-3)^{2}\)", r"\((2x+3)^{2}\)", r"\((4x-3)^{2}\)", r"\((2x-9)^{2}\)"],
        antwoord=0,
        uitleg=r"De dubbele term is \(2\cdot 2x\cdot 3=12x\), en die staat hier met een minteken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de som van de nulwaarden van \(x^{2}-7x+12\)? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"De nulwaarden zijn \(3\) en \(4\). Je leest de som ook af als \(-\tfrac{b}{a}=7\), en het product als \(\tfrac{c}{a}=12\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel reële nulwaarden heeft \(x^{3}-x\)?",
        opties=[r"\(3\)", r"\(2\)", r"\(1\)", r"geen"],
        antwoord=0,
        uitleg=r"\(x^{3}-x=x(x-1)(x+1)\), dus \(0\), \(1\) en \(-1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke veelterm van oneven graad heeft minstens één reële nulwaarde.",
        antwoord=True,
        uitleg=r"Bij een oneven graad loopt de functie van \(-\infty\) naar \(+\infty\), dus ze moet de \(x\)-as kruisen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Ontbind \(x^{4}-16\) zo ver mogelijk in \(\mathbb{R}\).",
        opties=[
            r"\((x-2)(x+2)\left(x^{2}+4\right)\)",
            r"\((x-2)(x+2)\left(x^{2}-4\right)\)",
            r"\((x-4)(x+4)\left(x^{2}+1\right)\)",
            r"\((x-2)^{2}(x+2)^{2}\)",
        ],
        antwoord=0,
        uitleg=r"Eerst \(\left(x^{2}-4\right)\left(x^{2}+4\right)\), dan nog eens het verschil van kwadraten. \(x^{2}+4\) blijft staan: die heeft geen reële nulwaarden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(x^{2}+2x+1\) heeft twee verschillende reële nulwaarden.",
        antwoord=False,
        uitleg=r"\(x^{2}+2x+1=(x+1)^{2}\) en \(D=0\), dus er is één nulwaarde, \(x=-1\), die dubbel telt. De parabool raakt de \(x\)-as.",
    ),
]
