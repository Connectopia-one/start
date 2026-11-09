# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: afgeleiden berekenen met rekenregels.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED): de afgeleide
functie berekenen van veeltermfuncties, rationale, exponentiële en
logaritmische functies; notaties van Lagrange, Leibniz en Cauchy; rekenregels
voor som, product, quotiënt en kettingregel; raaklijn in een punt; afgeleide
als ogenblikkelijke verandering.

Deel 1: basisfuncties, som, product en quotiënt. Deel 2: kettingregel,
exponentiële en logaritmische functies, raaklijn en verandering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = x^{5}\)?",
        opties=[r"\(f'(x) = 5x^{4}\)", r"\(f'(x) = x^{4}\)", r"\(f'(x) = 5x^{5}\)", r"\(f'(x) = 4x^{5}\)"],
        antwoord=0,
        uitleg=r"\((x^{n})' = n \cdot x^{n-1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = 3x^{4} - 2x^{2} + 7x - 1\)?",
        opties=[r"\(12x^{3} - 4x + 7\)", r"\(12x^{3} - 4x + 6\)", r"\(3x^{3} - 2x + 7\)", r"\(12x^{4} - 4x^{2} + 7\)"],
        antwoord=0,
        uitleg=r"Elke term apart afleiden: \(12x^{3}\), \(-4x\), \(7\), en de constante \(-1\) wordt \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide van een constante functie is \(0\).",
        antwoord=True,
        uitleg=r"Een constante functie verandert niet: de helling is overal \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke notatie is de notatie van Leibniz voor de afgeleide van \(y = f(x)\)?",
        opties=[r"\(\dfrac{dy}{dx}\)", r"\(f'(x)\)", r"\(Df(x)\)", r"\(\Delta y\)"],
        antwoord=0,
        uitleg=r"\(f'(x)\) is de notatie van Lagrange, \(Df(x)\) die van Cauchy, \(\dfrac{dy}{dx}\) die van Leibniz.",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = x^{3} - 4x\). Bereken \(f'(2)\).",
        antwoord=["8", "acht"],
        uitleg=r"\(f'(x) = 3x^{2} - 4\), dus \(f'(2) = 12 - 4 = 8\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \dfrac{1}{x}\)?",
        opties=[r"\(-\dfrac{1}{x^{2}}\)", r"\(\dfrac{1}{x^{2}}\)", r"\(\ln x\)", r"\(-\dfrac{1}{x}\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{1}{x} = x^{-1}\), dus de afgeleide is \(-1 \cdot x^{-2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \sqrt{x}\)?",
        opties=[r"\(\dfrac{1}{2\sqrt{x}}\)", r"\(2\sqrt{x}\)", r"\(\dfrac{1}{\sqrt{x}}\)", r"\(\dfrac{\sqrt{x}}{2}\)"],
        antwoord=0,
        uitleg=r"\(\sqrt{x} = x^{\frac{1}{2}}\), dus de afgeleide is \(\tfrac{1}{2} x^{-\frac{1}{2}} = \dfrac{1}{2\sqrt{x}}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule is de productregel?",
        opties=[r"\((f \cdot g)' = f' \cdot g + f \cdot g'\)", r"\((f \cdot g)' = f' \cdot g'\)", r"\((f \cdot g)' = f' \cdot g - f \cdot g'\)", r"\((f \cdot g)' = f \cdot g' \cdot g\)"],
        antwoord=0,
        uitleg=r"De afgeleide van een product is niet het product van de afgeleiden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide van \(f(x) \cdot g(x)\) is altijd \(f'(x) \cdot g'(x)\).",
        antwoord=False,
        uitleg=r"Neem \(x \cdot x = x^{2}\): de afgeleide is \(2x\), maar \(1 \cdot 1 = 1\). Gebruik de productregel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = (2x + 1)(x^{2} - 3)\)?",
        opties=[r"\(6x^{2} + 2x - 6\)", r"\(4x\)", r"\(6x^{2} + 2x - 3\)", r"\(2x^{2} + 2x - 6\)"],
        antwoord=0,
        uitleg=r"\(2 \cdot (x^{2} - 3) + (2x + 1) \cdot 2x = 2x^{2} - 6 + 4x^{2} + 2x = 6x^{2} + 2x - 6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule is de quotiëntregel?",
        opties=[r"\(\left(\dfrac{f}{g}\right)' = \dfrac{f' g - f g'}{g^{2}}\)", r"\(\left(\dfrac{f}{g}\right)' = \dfrac{f'}{g'}\)", r"\(\left(\dfrac{f}{g}\right)' = \dfrac{f g' - f' g}{g^{2}}\)", r"\(\left(\dfrac{f}{g}\right)' = \dfrac{f' g + f g'}{g^{2}}\)"],
        antwoord=0,
        uitleg=r"Teller: afgeleide van de teller maal de noemer, min de teller maal de afgeleide van de noemer. Noemer: de noemer in het kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \dfrac{x}{x + 1}\)?",
        opties=[r"\(\dfrac{1}{(x + 1)^{2}}\)", r"\(\dfrac{2x + 1}{(x + 1)^{2}}\)", r"\(\dfrac{-1}{(x + 1)^{2}}\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{1 \cdot (x + 1) - x \cdot 1}{(x + 1)^{2}} = \dfrac{1}{(x + 1)^{2}}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij de quotiëntregel maakt de volgorde in de teller niet uit.",
        antwoord=False,
        uitleg=r"\(f'g - fg'\) en \(fg' - f'g\) verschillen van teken. Begin bij de afgeleide van de teller.",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = \dfrac{2x - 1}{x}\). Bereken \(f'(1)\).",
        antwoord=["1", "één", "een"],
        uitleg=r"\(f'(x) = \dfrac{2 \cdot x - (2x - 1) \cdot 1}{x^{2}} = \dfrac{1}{x^{2}}\), dus \(f'(1) = 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = 5\)?",
        opties=[r"\(0\)", r"\(5\)", r"\(1\)", r"\(5x\)"],
        antwoord=0,
        uitleg=r"Een constante heeft afgeleide \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\((3 \cdot f(x))' = 3 \cdot f'(x)\).",
        antwoord=True,
        uitleg=r"Een constante factor mag je voor de afgeleide brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \dfrac{4}{x^{2}}\)?",
        opties=[r"\(-\dfrac{8}{x^{3}}\)", r"\(\dfrac{8}{x}\)", r"\(-\dfrac{4}{x^{3}}\)", r"\(\dfrac{8}{x^{3}}\)"],
        antwoord=0,
        uitleg=r"\(4x^{-2}\) afleiden geeft \(-8x^{-3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De kostfunctie van een bedrijf is \(K(q) = 0{,}5q^{2} + 20q + 300\) euro. Wat is de marginale kost \(K'(q)\)?",
        opties=[r"\(q + 20\)", r"\(0{,}5q + 20\)", r"\(q + 320\)", r"\(0{,}5q^{2} + 20\)"],
        antwoord=0,
        uitleg=r"De marginale kost is de afgeleide van de kostfunctie.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij die kostfunctie \(K(q) = 0{,}5q^{2} + 20q + 300\): wat is de marginale kost bij \(q = 40\)? Schrijf het getal in euro.",
        antwoord=["60", "60 euro"],
        uitleg=r"\(K'(40) = 40 + 20 = 60\). Eén stuk extra kost op dat moment ongeveer \(60\) euro.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide van \(x^{2} + x^{3}\) is \(2x + 3x^{2}\).",
        antwoord=True,
        uitleg=r"De afgeleide van een som is de som van de afgeleiden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Welke formule is de kettingregel?",
        opties=[r"\((f(g(x)))' = f'(g(x)) \cdot g'(x)\)", r"\((f(g(x)))' = f'(x) \cdot g'(x)\)", r"\((f(g(x)))' = f'(g'(x))\)", r"\((f(g(x)))' = f(g'(x))\)"],
        antwoord=0,
        uitleg=r"Leid de buitenste functie af en laat de binnenste staan, en vermenigvuldig met de afgeleide van de binnenste.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = (3x - 2)^{4}\)?",
        opties=[r"\(12(3x - 2)^{3}\)", r"\(4(3x - 2)^{3}\)", r"\(12x(3x - 2)^{3}\)", r"\(3(3x - 2)^{4}\)"],
        antwoord=0,
        uitleg=r"\(4(3x - 2)^{3} \cdot 3 = 12(3x - 2)^{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide van \((x^{2} + 1)^{3}\) is \(3(x^{2} + 1)^{2}\).",
        antwoord=False,
        uitleg=r"Je vergeet de afgeleide van de binnenste functie: \(3(x^{2} + 1)^{2} \cdot 2x = 6x(x^{2} + 1)^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = e^{x}\)?",
        opties=[r"\(e^{x}\)", r"\(x \cdot e^{x-1}\)", r"\(e\)", r"\(\ln x\)"],
        antwoord=0,
        uitleg=r"De functie \(e^{x}\) is haar eigen afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = e^{3x}\)?",
        opties=[r"\(3e^{3x}\)", r"\(e^{3x}\)", r"\(3x \cdot e^{3x - 1}\)", r"\(e^{3}\)"],
        antwoord=0,
        uitleg=r"Kettingregel: \(e^{3x} \cdot 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \ln x\)?",
        opties=[r"\(\dfrac{1}{x}\)", r"\(\ln x\)", r"\(e^{x}\)", r"\(x \ln x\)"],
        antwoord=0,
        uitleg=r"\((\ln x)' = \dfrac{1}{x}\), voor \(x > 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \ln(x^{2} + 4)\)?",
        opties=[r"\(\dfrac{2x}{x^{2} + 4}\)", r"\(\dfrac{1}{x^{2} + 4}\)", r"\(\dfrac{1}{2x}\)", r"\(2x \ln(x^{2} + 4)\)"],
        antwoord=0,
        uitleg=r"Kettingregel: \(\dfrac{1}{x^{2} + 4} \cdot 2x\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = 2^{x}\)?",
        opties=[r"\(2^{x} \ln 2\)", r"\(x \cdot 2^{x-1}\)", r"\(2^{x}\)", r"\(\dfrac{2^{x}}{\ln 2}\)"],
        antwoord=0,
        uitleg=r"\((a^{x})' = a^{x} \ln a\). Alleen bij grondtal \(e\) valt de factor weg, want \(\ln e = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide van \(x^{2}\) en die van \(2^{x}\) volgen dezelfde rekenregel.",
        antwoord=False,
        uitleg=r"Bij \(x^{2}\) staat de veranderlijke in het grondtal: \(2x\). Bij \(2^{x}\) staat ze in de exponent: \(2^{x} \ln 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = x \cdot e^{x}\)?",
        opties=[r"\((x + 1)e^{x}\)", r"\(e^{x}\)", r"\(x \cdot e^{x}\)", r"\((x - 1)e^{x}\)"],
        antwoord=0,
        uitleg=r"Productregel: \(1 \cdot e^{x} + x \cdot e^{x} = (x + 1)e^{x}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \log x\) (grondtal \(10\))?",
        opties=[r"\(\dfrac{1}{x \ln 10}\)", r"\(\dfrac{1}{x}\)", r"\(\dfrac{10}{x}\)", r"\(\dfrac{\ln 10}{x}\)"],
        antwoord=0,
        uitleg=r"\(\log x = \dfrac{\ln x}{\ln 10}\), dus de afgeleide is \(\dfrac{1}{x \ln 10}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een vergelijking van de raaklijn aan \(y = x^{2}\) in het punt \((3, 9)\)?",
        opties=[r"\(y = 6x - 9\)", r"\(y = 6x + 9\)", r"\(y = 3x\)", r"\(y = 2x + 3\)"],
        antwoord=0,
        uitleg=r"Helling \(f'(3) = 6\). Dan \(y - 9 = 6(x - 3)\), dus \(y = 6x - 9\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De raaklijn in \((a, f(a))\) heeft als vergelijking \(y - f(a) = f'(a)(x - a)\).",
        antwoord=True,
        uitleg=r"Een rechte door het punt \((a, f(a))\) met richtingscoëfficiënt \(f'(a)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = e^{2x}\). Bereken \(f'(0)\).",
        antwoord=["2", "twee"],
        uitleg=r"\(f'(x) = 2e^{2x}\) en \(e^{0} = 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een spaarbedrag groeit volgens \(B(t) = 1000 \cdot e^{0{,}05t}\). Wat is \(B'(t)\)?",
        opties=[r"\(50 \cdot e^{0{,}05t}\)", r"\(1000 \cdot e^{0{,}05t}\)", r"\(0{,}05 \cdot e^{0{,}05t}\)", r"\(50t \cdot e^{0{,}05t}\)"],
        antwoord=0,
        uitleg=r"\(1000 \cdot 0{,}05 = 50\). \(B'(t)\) is hoe snel het bedrag op dat moment groeit, in euro per jaar.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(B'(10)\) zegt hoeveel euro er op tijdstip \(10\) op de rekening staat.",
        antwoord=False,
        uitleg=r"Dat is \(B(10)\). \(B'(10)\) is de ogenblikkelijke verandering: hoe snel het bedrag op dat moment groeit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \sqrt{2x + 5}\)?",
        opties=[r"\(\dfrac{1}{\sqrt{2x + 5}}\)", r"\(\dfrac{1}{2\sqrt{2x + 5}}\)", r"\(\dfrac{2}{\sqrt{2x + 5}}\)", r"\(2\sqrt{2x + 5}\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{1}{2\sqrt{2x + 5}} \cdot 2 = \dfrac{1}{\sqrt{2x + 5}}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide van \(f(x) = \dfrac{e^{x}}{x}\)?",
        opties=[r"\(\dfrac{(x - 1)e^{x}}{x^{2}}\)", r"\(e^{x}\)", r"\(\dfrac{(x + 1)e^{x}}{x^{2}}\)", r"\(\dfrac{e^{x}}{x^{2}}\)"],
        antwoord=0,
        uitleg=r"Quotiëntregel: \(\dfrac{e^{x} \cdot x - e^{x} \cdot 1}{x^{2}}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een negatieve afgeleide in een punt betekent dat de functie daar daalt.",
        antwoord=True,
        uitleg=r"De raaklijn heeft daar een negatieve richtingscoëfficiënt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = \ln(3x)\). Bereken \(f'(2)\). Schrijf het als breuk, bijvoorbeeld 1/5.",
        antwoord=["1/2", "0,5", "0.5"],
        uitleg=r"\(f'(x) = \dfrac{1}{3x} \cdot 3 = \dfrac{1}{x}\), dus \(f'(2) = \dfrac{1}{2}\).",
    ),
]
