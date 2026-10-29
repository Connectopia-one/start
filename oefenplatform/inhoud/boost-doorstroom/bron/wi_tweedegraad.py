# -*- coding: utf-8 -*-
r"""De vragen voor "Stelsels en tweedegraadsvergelijkingen".

Uit de bouwsteen Relaties en verandering: het stelsel van twee
eerstegraadsvergelijkingen in twee onbekenden, met de combinatie-, substitutie-
en gelijkstellingsmethode, het onderscheid tussen een bepaald, een strijdig en
een onbepaald stelsel en wat dat grafisch betekent, en daarnaast de
tweedegraadsvergelijking: de standaardvorm, volledige en onvolledige
vergelijkingen, de discriminant, het ontbinden in factoren, de merkwaardige
producten en de tweedegraadsongelijkheden.

In echte notatie geschreven, met een accolade voor een stelsel en
\(ax^{2} + bx + c = 0\) in plaats van "ax kwadraat plus bx plus c is nul".
Zie oefenplatform/lib/wiskunde.ts. Het antwoord van een invulvraag blijft
gewone tekst, want dat typt een leerling in een invulvakje.

Deel 1 zijn de stelsels. Deel 2 is de tweede graad.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een stelsel van twee eerstegraadsvergelijkingen in twee onbekenden?",
        opties=[
            r"twee vergelijkingen die tegelijk moeten kloppen voor dezelfde \(x\) en \(y\)",
            "twee vergelijkingen waarvan je er zelf één mag kiezen",
            "een vergelijking die je in twee stappen moet oplossen",
            "twee vergelijkingen die na elkaar opgelost worden",
        ],
        antwoord=0,
        uitleg=r"De oplossing is een koppel \((x, y)\) dat in allebei de vergelijkingen past.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke drie methodes los je een stelsel algebraïsch op?",
        opties=[
            "de combinatiemethode, de substitutiemethode en de gelijkstellingsmethode",
            "de grafische methode, de tabelmethode en de schattingsmethode",
            "de discriminantmethode, het ontbinden en het afzonderen",
            "de kop-staartmethode, de kruismethode en de balansmethode",
        ],
        antwoord=0,
        uitleg="De grafische manier bestaat ook, maar die is niet algebraïsch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij de substitutiemethode?",
        opties=[
            "je drukt één onbekende uit en vult die uitdrukking in de andere vergelijking in",
            "je telt de twee vergelijkingen op zodat één onbekende wegvalt",
            "je stelt de twee rechterleden aan elkaar gelijk",
            "je tekent de twee rechten en leest het snijpunt af",
        ],
        antwoord=0,
        uitleg=r"Handig als één van de twee vergelijkingen al bijna in de vorm \(y = \ldots\) staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij de combinatiemethode?",
        opties=[
            "je telt de vergelijkingen op of trekt ze af zodat één onbekende wegvalt",
            "je vervangt één onbekende door een uitdrukking in de andere",
            "je stelt de twee vergelijkingen aan elkaar gelijk",
            "je vermenigvuldigt de twee vergelijkingen met elkaar",
        ],
        antwoord=0,
        uitleg="Soms moet je één van de twee eerst met een getal vermenigvuldigen zodat de coëfficiënten tegengesteld worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een stelsel zonder oplossingen?",
        opties=["strijdig", "onbepaald", "bepaald", "onvolledig"],
        antwoord=0,
        uitleg=r"Grafisch zijn dat twee evenwijdige rechten die niet samenvallen: \(S = \emptyset\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een stelsel met oneindig veel oplossingen?",
        opties=["onbepaald", "strijdig", "bepaald", "volledig"],
        antwoord=0,
        uitleg="Grafisch zijn dat twee samenvallende rechten: elk punt van de rechte is een oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het grafisch dat een stelsel precies één oplossing heeft?",
        opties=[
            "de twee rechten snijden elkaar in één punt",
            "de twee rechten lopen evenwijdig",
            "de twee rechten vallen samen",
            "de twee rechten staan loodrecht op elkaar",
        ],
        antwoord=0,
        uitleg="Zo'n stelsel heet bepaald, en de coördinaten van het snijpunt vormen de oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(\left\{\begin{array}{l} x + y = 10 \\ x - y = 2 \end{array}\right.\)?",
        opties=[r"\((6, 4)\)", r"\((4, 6)\)", r"\((5, 5)\)", r"\((8, 2)\)"],
        antwoord=0,
        uitleg=r"Tel de twee vergelijkingen op: \(2x = 12\), dus \(x = 6\) en \(y = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(\left\{\begin{array}{l} y = 2x \\ x + y = 9 \end{array}\right.\)?",
        opties=[r"\((3, 6)\)", r"\((6, 3)\)", r"\((4{,}5 ; 4{,}5)\)", r"\((9, 18)\)"],
        antwoord=0,
        uitleg=r"Vul \(y = 2x\) in: \(x + 2x = 9\), dus \(3x = 9\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee broden en drie koeken kosten 7 euro, één brood en drie koeken kosten 5 euro. Wat kost een brood?",
        opties=["2 euro", "1 euro", "3 euro", "1,5 euro"],
        antwoord=0,
        uitleg=r"\(\left\{\begin{array}{l} 2b + 3k = 7 \\ b + 3k = 5 \end{array}\right.\) aftrekken geeft \(b = 2\). Een koek kost dan \(1\) euro.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je lost een stelsel op en krijgt \(0 = 7\). Wat betekent dat?",
        opties=[
            "het stelsel is strijdig en heeft geen enkele oplossing",
            "het stelsel is onbepaald en heeft oneindig veel oplossingen",
            r"\(x = 0\) en \(y = 7\)",
            "je moet de andere methode proberen",
        ],
        antwoord=0,
        uitleg="Er blijft een onwaarheid over. Grafisch zijn de rechten evenwijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je lost een stelsel op en krijgt \(0 = 0\). Wat betekent dat?",
        opties=[
            "het stelsel is onbepaald: elk punt van de rechte is een oplossing",
            "het stelsel is strijdig en heeft geen oplossing",
            r"\(x\) en \(y\) zijn allebei nul",
            "de twee rechten staan loodrecht op elkaar",
        ],
        antwoord=0,
        uitleg="De twee vergelijkingen zeggen hetzelfde, dus de rechten vallen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kies je de gelijkstellingsmethode?",
        opties=[
            r"als in allebei de vergelijkingen \(y\) al alleen staat",
            r"als de coëfficiënten van \(x\) al tegengesteld zijn",
            r"als één vergelijking geen \(y\) bevat",
            "als je het snijpunt al grafisch gevonden hebt",
        ],
        antwoord=0,
        uitleg=r"Staat er twee keer \(y = \ldots\), dan stel je de rechterleden meteen aan elkaar gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing van een stelsel is een koppel getallen, niet één getal.",
        antwoord=True,
        uitleg=r"Je schrijft het als \((x, y)\), bijvoorbeeld \((6, 4)\).",
    ),
    dict(
        type="waarofniet",
        vraag="Een strijdig stelsel hoort bij twee samenvallende rechten.",
        antwoord=False,
        uitleg="Samenvallende rechten geven een onbepaald stelsel. Strijdig hoort bij evenwijdige rechten.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie algebraïsche methodes geven altijd dezelfde oplossing.",
        antwoord=True,
        uitleg="Ze verschillen alleen in hoeveel rekenwerk ze kosten bij een bepaald stelsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stelsel grafisch oplossen geeft altijd een exact antwoord.",
        antwoord=False,
        uitleg="Bij een snijpunt met komma's lees je een benadering af. Algebraïsch krijg je de exacte waarde.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(\left\{\begin{array}{l} x + y = 12 \\ x - y = 4 \end{array}\right.\) Wat is \(x\)?",
        antwoord=["8"],
        uitleg=r"Optellen geeft \(2x = 16\).",
    ),
    dict(
        type="invultekst",
        vraag="Twee evenwijdige rechten die niet samenvallen: hoe noem je dat stelsel?",
        antwoord=["strijdig", "een strijdig stelsel"],
        uitleg=r"De oplossingenverzameling is dan \(\emptyset\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(\left\{\begin{array}{l} y = 3x \\ x + y = 16 \end{array}\right.\) Wat is \(x\)?",
        antwoord=["4"],
        uitleg=r"\(x + 3x = 4x = 16\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de standaardvorm van een tweedegraadsvergelijking?",
        opties=[
            r"\(ax^{2} + bx + c = 0\) met \(a \neq 0\)",
            r"\(ax + b = 0\) met \(a \neq 0\)",
            r"\(ax^{2} = c\) met \(a \neq 0\) en \(c \neq 0\)",
            r"\(x^{2} + bx = 0\) met \(b \neq 0\)",
        ],
        antwoord=0,
        uitleg=r"De voorwaarde \(a \neq 0\) is wat de vergelijking van de tweede graad maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heet een vierkantsvergelijking onvolledig?",
        opties=[
            r"als \(b = 0\) of \(c = 0\)",
            r"als \(a = 0\)",
            "als er geen oplossingen zijn",
            "als de discriminant negatief is",
        ],
        antwoord=0,
        uitleg=r"Bij \(c = 0\) zonder je een factor \(x\) af. Bij \(b = 0\) kan je meteen worteltrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de discriminant van \(ax^{2} + bx + c\)?",
        opties=[
            r"\(D = b^{2} - 4ac\)",
            r"\(D = b^{2} + 4ac\)",
            r"\(D = 4ac - b^{2}\)",
            r"\(D = b - 4ac\)",
        ],
        antwoord=0,
        uitleg="Het teken van de discriminant zegt hoeveel oplossingen er zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De discriminant is negatief, \(D < 0\). Hoeveel reële oplossingen zijn er?",
        opties=["geen enkele", "één", "twee", "oneindig veel"],
        antwoord=0,
        uitleg=r"De parabool raakt de \(x\)-as dan nergens: ze ligt er volledig boven of volledig onder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De discriminant is \(D = 0\). Hoeveel oplossingen zijn er?",
        opties=["één", "geen enkele", "twee", r"dat hangt af van \(a\)"],
        antwoord=0,
        uitleg=r"De parabool raakt de \(x\)-as in precies één punt, met haar top.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 9 = 0\).",
        opties=[r"\(x = 3\) of \(x = -3\)", r"\(x = 3\)", r"\(x = 9\) of \(x = -9\)", "er is geen oplossing"],
        antwoord=0,
        uitleg=r"Het verschil van twee kwadraten: \((x - 3)(x + 3) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 5x = 0\).",
        opties=[r"\(x = 0\) of \(x = 5\)", r"\(x = 5\)", r"\(x = 0\)", "er is geen oplossing"],
        antwoord=0,
        uitleg=r"Zonder \(x\) af: \(x(x - 5) = 0\). Een product is nul zodra één factor nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 5x + 6 = 0\).",
        opties=[
            r"\(x = 2\) of \(x = 3\)",
            r"\(x = -2\) of \(x = -3\)",
            r"\(x = 1\) of \(x = 6\)",
            r"\(x = 5\) of \(x = 6\)",
        ],
        antwoord=0,
        uitleg=r"Zoek twee getallen met som \(5\) en product \(6\). De ontbinding is \((x - 2)(x - 3)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de ontbinding van \(x^{2} + 6x + 9\)?",
        opties=[
            r"\((x + 3)^{2}\)",
            r"\((x - 3)^{2}\)",
            r"\((x + 3)(x - 3)\)",
            r"\((x + 9)(x + 1)\)",
        ],
        antwoord=0,
        uitleg=r"Dit is een volkomen kwadraat: \(a^{2} + 2ab + b^{2} = (a + b)^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de ontbinding van \(x^{2} - 16\)?",
        opties=[
            r"\((x - 4)(x + 4)\)",
            r"\((x - 4)^{2}\)",
            r"\((x - 8)(x + 2)\)",
            r"\((x - 16)(x + 1)\)",
        ],
        antwoord=0,
        uitleg=r"Het verschil van twee kwadraten: \(a^{2} - b^{2} = (a - b)(a + b)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechthoek is \(3\) m langer dan breed en heeft \(40\) m² oppervlakte. Welke vergelijking hoort erbij?",
        opties=[
            r"\(x(x + 3) = 40\)",
            r"\(x + (x + 3) = 40\)",
            r"\(2x + 2(x + 3) = 40\)",
            r"\(x^{2} + 3 = 40\)",
        ],
        antwoord=0,
        uitleg=r"Breedte maal lengte. De breedte is \(5\) m en de lengte \(8\) m.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossingenverzameling van \(x^{2} < 9\)?",
        opties=[
            r"\(-3 < x < 3\)",
            r"\(x < 3\)",
            r"\(x > -3\)",
            r"\(x < -3\) of \(x > 3\)",
        ],
        antwoord=0,
        uitleg=r"De parabool ligt onder de \(x\)-as tussen haar twee nulwaarden in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je de oplossingen van een vierkantsvergelijking best in de oorspronkelijke vergelijking?",
        opties=[
            "omdat een tekenfout in de discriminant zo meteen opvalt",
            "omdat een vierkantsvergelijking altijd twee oplossingen heeft",
            r"omdat de formule enkel geldt bij een positieve \(a\)",
            "omdat je anders de ontbinding niet mag gebruiken",
        ],
        antwoord=0,
        uitleg="Invullen kost een halve minuut en vangt de meeste fouten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vierkantsvergelijking heeft altijd twee reële oplossingen.",
        antwoord=False,
        uitleg=r"Bij \(D < 0\) zijn het er geen, bij \(D = 0\) precies één.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een product van twee factoren nul is, is minstens één van de factoren nul.",
        antwoord=True,
        uitleg="Daarop steunt het ontbinden in factoren als oplossingsmethode.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(x^{2} + 9\) is te ontbinden als \((x + 3)(x - 3)\).",
        antwoord=False,
        uitleg=r"Dat product geeft \(x^{2} - 9\). Een som van twee kwadraten is niet te ontbinden.",
    ),
    dict(
        type="waarofniet",
        vraag="De oplossingen van een tweedegraadsvergelijking zijn de nulwaarden van de bijhorende parabool.",
        antwoord=True,
        uitleg=r"Daar snijdt of raakt de parabool de \(x\)-as.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(x^{2} = 49\). Geef de positieve oplossing.",
        antwoord=["7"],
        uitleg=r"De andere oplossing is \(-7\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de discriminant van \(x^{2} - 4x + 4\)?",
        antwoord=["0", "nul"],
        uitleg=r"\(D = 16 - 16 = 0\). Er is dus precies één oplossing, namelijk \(2\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een rechthoek is \(3\) m langer dan breed en heeft \(40\) m² oppervlakte. Hoe breed is hij in meter?",
        antwoord=["5", "5 m", "5 meter"],
        uitleg=r"\(5 \cdot 8 = 40\).",
    ),
]
