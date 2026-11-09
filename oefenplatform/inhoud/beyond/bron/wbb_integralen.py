# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: integralen en oppervlakte.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED): de bepaalde
integraal als georiënteerde oppervlakte en als limiet van een som
(ondersom, bovensom, Riemannsom), integratiegrenzen en integrand,
primitieve functies, onbepaalde en bepaalde integralen van veeltermfuncties
(lineariteit, onmiddellijke integratie, splitsing), werkelijke oppervlakte,
oppervlakte tussen twee krommen en vraagstukken (snelheid en afgelegde weg,
debiet en inhoud, marginale en totale kost).

Deel 1: betekenis, sommen en primitieven. Deel 2: berekenen, oppervlakte
en vraagstukken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt \(\displaystyle\int_{a}^{b} f(x)\,dx\) voor als \(f(x) \ge 0\) op \([a, b]\)?",
        opties=[
            r"de oppervlakte tussen de grafiek van \(f\) en de \(x\)-as op \([a, b]\)",
            r"de helling van \(f\) tussen \(a\) en \(b\)",
            r"het verschil \(f(b) - f(a)\)",
            r"de lengte van de grafiek van \(a\) tot \(b\)",
        ],
        antwoord=0,
        uitleg=r"Als de grafiek boven de \(x\)-as ligt, is de bepaalde integraal gewoon de oppervlakte eronder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In \(\displaystyle\int_{1}^{4} (x^{2} + 1)\,dx\): wat is de integrand?",
        opties=[r"\(x^{2} + 1\)", r"\(1\)", r"\(4\)", r"\(dx\)"],
        antwoord=0,
        uitleg=r"De integrand is de functie die je integreert. \(1\) is de ondergrens, \(4\) de bovengrens.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Ligt de grafiek onder de \(x\)-as, dan is de bepaalde integraal over dat stuk negatief.",
        antwoord=True,
        uitleg=r"Daarom heet het een georiënteerde oppervlakte: onder de \(x\)-as telt ze negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een ondersom voor een stijgende functie op \([a, b]\) neem je als hoogte van elk rechthoekje ...",
        opties=[
            r"de functiewaarde in het linkereindpunt van het deelinterval",
            r"de functiewaarde in het rechtereindpunt van het deelinterval",
            r"de grootste functiewaarde op heel \([a, b]\)",
            r"altijd de waarde \(1\)",
        ],
        antwoord=0,
        uitleg=r"Bij een ondersom neem je de kleinste functiewaarde op elk deelinterval. Bij een stijgende functie is dat links.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Hoe meer deelintervallen je gebruikt, hoe beter een Riemannsom de oppervlakte benadert.",
        antwoord=True,
        uitleg=r"De rechthoekjes worden smaller en sluiten beter aan bij de grafiek.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de Riemannsom \(\displaystyle\sum f(x_{i}) \cdot \Delta x\): waarmee komt \(\Delta x\) overeen in de integraal?",
        opties=[r"\(dx\), de breedte van de rechthoekjes", r"de bovengrens", r"de integrand", r"de primitieve functie"],
        antwoord=0,
        uitleg=r"\(f(x_{i})\) is de hoogte en \(\Delta x\) de breedte. In de limiet wordt \(\Delta x\) de \(dx\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Je benadert de oppervlakte onder \(f(x) = x\) op \([0, 4]\) met een bovensom van \(4\) rechthoekjes van breedte \(1\). Wat is de bovensom?",
        antwoord=["10", "tien"],
        uitleg=r"Hoogtes rechts: \(1 + 2 + 3 + 4 = 10\), maal breedte \(1\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Zelfde situatie, \(f(x) = x\) op \([0, 4]\) met \(4\) rechthoekjes van breedte \(1\). Wat is de ondersom?",
        antwoord=["6", "zes"],
        uitleg=r"Hoogtes links: \(0 + 1 + 2 + 3 = 6\). De echte oppervlakte, \(8\), ligt ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een primitieve functie van \(f\)?",
        opties=[r"een functie \(F\) met \(F'(x) = f(x)\)", r"de afgeleide van \(f\)", r"de functie \(\dfrac{1}{f(x)}\)", r"de grafiek van \(f\) gespiegeld"],
        antwoord=0,
        uitleg=r"Primitiveren is het omgekeerde van afleiden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke functie is een primitieve van \(f(x) = 3x^{2}\)?",
        opties=[r"\(x^{3} + 5\)", r"\(6x\)", r"\(3x^{3}\)", r"\(x^{2}\)"],
        antwoord=0,
        uitleg=r"\((x^{3} + 5)' = 3x^{2}\). De constante maakt niet uit.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie heeft precies één primitieve functie.",
        antwoord=False,
        uitleg=r"Je mag er elke constante \(c\) bij optellen: er zijn er oneindig veel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\displaystyle\int x^{4}\,dx = \) ...",
        opties=[r"\(\dfrac{x^{5}}{5} + c\)", r"\(4x^{3} + c\)", r"\(x^{5} + c\)", r"\(\dfrac{x^{4}}{4} + c\)"],
        antwoord=0,
        uitleg=r"\(\displaystyle\int x^{n}\,dx = \dfrac{x^{n+1}}{n + 1} + c\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\displaystyle\int (6x^{2} - 4x + 3)\,dx = \) ...",
        opties=[r"\(2x^{3} - 2x^{2} + 3x + c\)", r"\(12x - 4 + c\)", r"\(6x^{3} - 4x^{2} + 3x + c\)", r"\(2x^{3} - 2x^{2} + c\)"],
        antwoord=0,
        uitleg=r"Splitsen en elke term apart: \(2x^{3}\), \(-2x^{2}\), \(3x\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\displaystyle\int (f(x) + g(x))\,dx = \int f(x)\,dx \cdot \int g(x)\,dx\)",
        antwoord=False,
        uitleg=r"Een integraal van een som is de som van de integralen, niet het product.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule gebruik je om een bepaalde integraal te berekenen, met \(F\) een primitieve van \(f\)?",
        opties=[r"\(\displaystyle\int_{a}^{b} f(x)\,dx = F(b) - F(a)\)", r"\(\displaystyle\int_{a}^{b} f(x)\,dx = F(a) - F(b)\)", r"\(\displaystyle\int_{a}^{b} f(x)\,dx = f(b) - f(a)\)", r"\(\displaystyle\int_{a}^{b} f(x)\,dx = F(b) \cdot F(a)\)"],
        antwoord=0,
        uitleg=r"Bovengrens invullen min ondergrens invullen, in de primitieve.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\displaystyle\int 5 f(x)\,dx = 5 \int f(x)\,dx\)",
        antwoord=True,
        uitleg=r"Dat is de lineariteit van de integraal: een constante factor mag je ervoor brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De bepaalde integraal is de limiet van ondersommen en bovensommen als ...",
        opties=[r"het aantal deelintervallen naar oneindig gaat", r"de bovengrens naar oneindig gaat", r"de functie naar nul gaat", r"de breedte van de rechthoekjes groter wordt"],
        antwoord=0,
        uitleg=r"Dan worden de rechthoekjes oneindig smal, en ondersom en bovensom komen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\displaystyle\int 7\,dx = \) ...",
        opties=[r"\(7x + c\)", r"\(0\)", r"\(7 + c\)", r"\(\dfrac{7x^{2}}{2} + c\)"],
        antwoord=0,
        uitleg=r"\((7x)' = 7\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\displaystyle\int_{a}^{a} f(x)\,dx = 0\)",
        antwoord=True,
        uitleg=r"Een interval zonder breedte heeft geen oppervlakte: \(F(a) - F(a) = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een dalende functie is de ondersom groter dan de bovensom.",
        antwoord=False,
        uitleg=r"De ondersom is altijd de kleinste: je neemt de kleinste functiewaarde per deelinterval. Bij een dalende functie ligt die rechts.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"Bereken \(\displaystyle\int_{0}^{3} x^{2}\,dx\).",
        antwoord=["9", "negen"],
        uitleg=r"\(\left[\dfrac{x^{3}}{3}\right]_{0}^{3} = 9 - 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\displaystyle\int_{1}^{2} (4x^{3} - 2x)\,dx\).",
        antwoord=["12", "twaalf"],
        uitleg=r"\(\left[x^{4} - x^{2}\right]_{1}^{2} = (16 - 4) - (1 - 1) = 12\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\displaystyle\int_{-1}^{1} x^{3}\,dx\).",
        opties=[r"\(0\)", r"\(\dfrac{1}{2}\)", r"\(\dfrac{1}{4}\)", r"\(2\)"],
        antwoord=0,
        uitleg=r"\(\left[\dfrac{x^{4}}{4}\right]_{-1}^{1} = \dfrac{1}{4} - \dfrac{1}{4} = 0\). Het stuk onder de \(x\)-as compenseert het stuk erboven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de werkelijke oppervlakte tussen \(y = x^{3}\) en de \(x\)-as op \([-1, 1]\)?",
        opties=[r"\(\dfrac{1}{2}\)", r"\(0\)", r"\(\dfrac{1}{4}\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"Splits in \([-1, 0]\) en \([0, 1]\) en tel de absolute waarden op: \(\dfrac{1}{4} + \dfrac{1}{4}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Om de werkelijke oppervlakte te berekenen, splits je de integraal bij de nulwaarden van de functie.",
        antwoord=True,
        uitleg=r"Zo tel je de stukken onder de \(x\)-as positief mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\displaystyle\int_{0}^{2} (x^{2} - 4)\,dx\).",
        opties=[r"\(-\dfrac{16}{3}\)", r"\(\dfrac{16}{3}\)", r"\(-\dfrac{8}{3}\)", r"\(-8\)"],
        antwoord=0,
        uitleg=r"\(\left[\dfrac{x^{3}}{3} - 4x\right]_{0}^{2} = \dfrac{8}{3} - 8 = -\dfrac{16}{3}\). Negatief, want de grafiek ligt onder de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke integraal noteer je de oppervlakte tussen \(f\) en \(g\) op \([a, b]\) als \(f(x) \ge g(x)\)?",
        opties=[r"\(\displaystyle\int_{a}^{b} (f(x) - g(x))\,dx\)", r"\(\displaystyle\int_{a}^{b} (f(x) + g(x))\,dx\)", r"\(\displaystyle\int_{a}^{b} f(x) \cdot g(x)\,dx\)", r"\(\displaystyle\int_{a}^{b} (g(x) - f(x))\,dx\)"],
        antwoord=0,
        uitleg=r"Bovenste functie min onderste functie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Tussen welke grenzen bereken je de oppervlakte ingesloten door \(y = x^{2}\) en \(y = 2x\)?",
        opties=[r"tussen \(0\) en \(2\)", r"tussen \(-2\) en \(2\)", r"tussen \(0\) en \(4\)", r"tussen \(1\) en \(2\)"],
        antwoord=0,
        uitleg=r"\(x^{2} = 2x \iff x(x - 2) = 0\): de grafieken snijden in \(x = 0\) en \(x = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is de oppervlakte ingesloten door \(y = x^{2}\) en \(y = 2x\)?",
        opties=[r"\(\dfrac{4}{3}\)", r"\(\dfrac{8}{3}\)", r"\(4\)", r"\(\dfrac{2}{3}\)"],
        antwoord=0,
        uitleg=r"\(\displaystyle\int_{0}^{2} (2x - x^{2})\,dx = \left[x^{2} - \dfrac{x^{3}}{3}\right]_{0}^{2} = 4 - \dfrac{8}{3} = \dfrac{4}{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij de oppervlakte tussen twee krommen maakt het niet uit welke functie je eerst schrijft.",
        antwoord=False,
        uitleg=r"Onderste min bovenste geeft een negatief getal. Neem altijd bovenste min onderste, of de absolute waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een auto rijdt met snelheid \(v(t)\) in m/s. Wat stelt \(\displaystyle\int_{0}^{10} v(t)\,dt\) voor?",
        opties=[r"de afgelegde weg in de eerste \(10\) seconden", r"de versnelling na \(10\) seconden", r"de gemiddelde snelheid", r"de snelheid na \(10\) seconden"],
        antwoord=0,
        uitleg=r"Snelheid maal tijd is afstand. De integraal telt dat op over het hele tijdsinterval.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een fietser rijdt met \(v(t) = 2t\) m/s. Hoeveel meter legt hij af tussen \(t = 0\) en \(t = 5\) s?",
        antwoord=["25", "25 m", "vijfentwintig"],
        uitleg=r"\(\displaystyle\int_{0}^{5} 2t\,dt = \left[t^{2}\right]_{0}^{5} = 25\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De marginale kost is \(K'(q) = 2q + 10\) euro per stuk. Hoeveel kost het om de productie van \(10\) naar \(20\) stuks te verhogen?",
        opties=[r"\(400\) euro", r"\(50\) euro", r"\(300\) euro", r"\(500\) euro"],
        antwoord=0,
        uitleg=r"\(\displaystyle\int_{10}^{20} (2q + 10)\,dq = \left[q^{2} + 10q\right]_{10}^{20} = 600 - 200 = 400\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Ken je de marginale kost, dan vind je de totale kostfunctie door te primitiveren.",
        antwoord=True,
        uitleg=r"De marginale kost is de afgeleide van de totale kost. De vaste kost bepaalt de constante.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Water stroomt in een vat met debiet \(d(t) = 6 - t\) liter per minuut (\(0 \le t \le 6\)). Hoeveel liter stroomt er in de eerste \(6\) minuten in?",
        opties=[r"\(18\) liter", r"\(36\) liter", r"\(6\) liter", r"\(30\) liter"],
        antwoord=0,
        uitleg=r"\(\displaystyle\int_{0}^{6} (6 - t)\,dt = \left[6t - \dfrac{t^{2}}{2}\right]_{0}^{6} = 36 - 18 = 18\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke integraal geeft de werkelijke oppervlakte tussen \(y = x^{2} - 1\) en de \(x\)-as op \([0, 2]\)?",
        opties=[
            r"\(-\displaystyle\int_{0}^{1} (x^{2} - 1)\,dx + \int_{1}^{2} (x^{2} - 1)\,dx\)",
            r"\(\displaystyle\int_{0}^{2} (x^{2} - 1)\,dx\)",
            r"\(\displaystyle\int_{0}^{1} (x^{2} - 1)\,dx + \int_{1}^{2} (x^{2} - 1)\,dx\)",
            r"\(-\displaystyle\int_{0}^{2} (x^{2} - 1)\,dx\)",
        ],
        antwoord=0,
        uitleg=r"Op \([0, 1]\) ligt de grafiek onder de \(x\)-as: dat stuk krijgt een minteken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\displaystyle\int_{0}^{1} (3x^{2} + 2x + 1)\,dx\).",
        antwoord=["3", "drie"],
        uitleg=r"\(\left[x^{3} + x^{2} + x\right]_{0}^{1} = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\displaystyle\int_{0}^{4} f(x)\,dx = \int_{0}^{1} f(x)\,dx + \int_{1}^{4} f(x)\,dx\)",
        antwoord=True,
        uitleg=r"Je mag het interval opsplitsen en de stukken optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De snelheid van een voorwerp is \(v(t) = 3t^{2}\) m/s, met \(t\) in seconden. Hoeveel meter legt het af tussen \(t = 1\) en \(t = 2\)?",
        opties=[r"\(7\) m", r"\(8\) m", r"\(9\) m", r"\(12\) m"],
        antwoord=0,
        uitleg=r"\(\left[t^{3}\right]_{1}^{2} = 8 - 1 = 7\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\displaystyle\int_{1}^{3} x\,dx\) is gelijk aan \(3 - 1 = 2\).",
        antwoord=False,
        uitleg=r"Je moet de primitieve invullen, niet de functie zelf: \(\left[\dfrac{x^{2}}{2}\right]_{1}^{3} = \dfrac{9}{2} - \dfrac{1}{2} = 4\).",
    ),
]
