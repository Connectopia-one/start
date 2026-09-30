# -*- coding: utf-8 -*-
"""De vragen voor "Stelsels en tweedegraadsvergelijkingen".

Uit de bouwsteen Relaties en verandering: het stelsel van twee
eerstegraadsvergelijkingen in twee onbekenden, met de combinatie-, substitutie-
en gelijkstellingsmethode, het onderscheid tussen een bepaald, een strijdig en
een onbepaald stelsel en wat dat grafisch betekent, en daarnaast de
tweedegraadsvergelijking: de standaardvorm, volledige en onvolledige
vergelijkingen, de discriminant, het ontbinden in factoren, de merkwaardige
producten en de tweedegraadsongelijkheden.

Deel 1 zijn de stelsels. Deel 2 is de tweede graad.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een stelsel van twee eerstegraadsvergelijkingen in twee onbekenden?",
        opties=[
            "twee vergelijkingen die tegelijk moeten kloppen voor dezelfde x en y",
            "twee vergelijkingen waarvan je er zelf één mag kiezen",
            "een vergelijking die je in twee stappen moet oplossen",
            "twee vergelijkingen die na elkaar opgelost worden",
        ],
        antwoord=0,
        uitleg="De oplossing is een koppel getallen dat in allebei de vergelijkingen past.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie methodes noemt de fiche om een stelsel algebraïsch op te lossen?",
        opties=[
            "de combinatiemethode, de substitutiemethode en de gelijkstellingsmethode",
            "de grafische methode, de tabelmethode en de schattingsmethode",
            "de discriminantmethode, het ontbinden en het afzonderen",
            "de kop-staartmethode, de kruismethode en de balansmethode",
        ],
        antwoord=0,
        uitleg="De grafische manier bestaat ook, maar die staat apart vermeld in de fiche.",
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
        uitleg="Handig als één van de twee vergelijkingen al bijna in de vorm y is ... staat.",
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
        uitleg="Grafisch zijn dat twee evenwijdige rechten die niet samenvallen: ze snijden elkaar nergens.",
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
        vraag="Wat is de oplossing van het stelsel x plus y is 10 en x min y is 2?",
        opties=["x is 6 en y is 4", "x is 4 en y is 6", "x is 5 en y is 5", "x is 8 en y is 2"],
        antwoord=0,
        uitleg="Tel de twee vergelijkingen op: 2x is 12, dus x is 6 en y is 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van het stelsel y is 2x en x plus y is 9?",
        opties=["x is 3 en y is 6", "x is 6 en y is 3", "x is 4,5 en y is 4,5", "x is 9 en y is 18"],
        antwoord=0,
        uitleg="Vul y is 2x in: x plus 2x is 9, dus 3x is 9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee broden en drie koeken kosten 7 euro, één brood en drie koeken kosten 5 euro. Wat kost een brood?",
        opties=["2 euro", "1 euro", "3 euro", "1,5 euro"],
        antwoord=0,
        uitleg="Trek de tweede vergelijking van de eerste af: één brood kost 2 euro. Een koek kost dan 1 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost een stelsel op en krijgt 0 is 7. Wat betekent dat?",
        opties=[
            "het stelsel is strijdig en heeft geen enkele oplossing",
            "het stelsel is onbepaald en heeft oneindig veel oplossingen",
            "x is 0 en y is 7",
            "je moet de andere methode proberen",
        ],
        antwoord=0,
        uitleg="Er blijft een onwaarheid over. Grafisch zijn de rechten evenwijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost een stelsel op en krijgt 0 is 0. Wat betekent dat?",
        opties=[
            "het stelsel is onbepaald: elk punt van de rechte is een oplossing",
            "het stelsel is strijdig en heeft geen oplossing",
            "x en y zijn allebei nul",
            "de twee rechten staan loodrecht op elkaar",
        ],
        antwoord=0,
        uitleg="De twee vergelijkingen zeggen hetzelfde, dus de rechten vallen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kies je de gelijkstellingsmethode?",
        opties=[
            "als in allebei de vergelijkingen y al alleen staat",
            "als de coëfficiënten van x al tegengesteld zijn",
            "als één vergelijking geen y bevat",
            "als je het snijpunt al grafisch gevonden hebt",
        ],
        antwoord=0,
        uitleg="Staat er twee keer y is ..., dan stel je de rechterleden meteen aan elkaar gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing van een stelsel is een koppel getallen, niet één getal.",
        antwoord=True,
        uitleg="Je schrijft het als (x, y), bijvoorbeeld (6, 4).",
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
        vraag="Los op: x plus y is 12 en x min y is 4. Wat is x?",
        antwoord=["8"],
        uitleg="Optellen geeft 2x is 16.",
    ),
    dict(
        type="invultekst",
        vraag="Twee evenwijdige rechten die niet samenvallen: hoe noem je dat stelsel?",
        antwoord=["strijdig", "een strijdig stelsel"],
        uitleg="De oplossingenverzameling is dan de lege verzameling.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: y is 3x en x plus y is 16. Wat is x?",
        antwoord=["4"],
        uitleg="x plus 3x is 4x, en dat is 16.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de standaardvorm van een tweedegraadsvergelijking?",
        opties=[
            "ax kwadraat plus bx plus c is nul, met a niet nul",
            "ax plus b is nul, met a niet nul",
            "ax kwadraat is c, met a en c niet nul",
            "x kwadraat plus bx is nul, met b niet nul",
        ],
        antwoord=0,
        uitleg="De voorwaarde dat a niet nul is, is wat de vergelijking van de tweede graad maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heet een vierkantsvergelijking onvolledig?",
        opties=[
            "als b of c gelijk is aan nul",
            "als a gelijk is aan nul",
            "als er geen oplossingen zijn",
            "als de discriminant negatief is",
        ],
        antwoord=0,
        uitleg="Bij c is nul zonder je een factor x af. Bij b is nul kan je meteen worteltrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de discriminant van ax kwadraat plus bx plus c?",
        opties=[
            "b kwadraat min 4ac",
            "b kwadraat plus 4ac",
            "4ac min b kwadraat",
            "b min 4ac",
        ],
        antwoord=0,
        uitleg="Het teken van de discriminant zegt hoeveel oplossingen er zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="De discriminant is negatief. Hoeveel reële oplossingen heeft de vergelijking?",
        opties=["geen enkele", "één", "twee", "oneindig veel"],
        antwoord=0,
        uitleg="De parabool raakt de x-as dan nergens: ze ligt er volledig boven of volledig onder.",
    ),
    dict(
        type="meerkeuze",
        vraag="De discriminant is nul. Hoeveel oplossingen heeft de vergelijking?",
        opties=["één", "geen enkele", "twee", "dat hangt af van a"],
        antwoord=0,
        uitleg="De parabool raakt de x-as in precies één punt, met haar top.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x kwadraat min 9 is nul.",
        opties=["x is 3 of x is min 3", "x is 3", "x is 9 of x is min 9", "er is geen oplossing"],
        antwoord=0,
        uitleg="Het verschil van twee kwadraten: (x min 3)(x plus 3) is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x kwadraat min 5x is nul.",
        opties=["x is 0 of x is 5", "x is 5", "x is 0", "er is geen oplossing"],
        antwoord=0,
        uitleg="Zonder x af: x maal (x min 5) is nul. Een product is nul zodra één factor nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x kwadraat min 5x plus 6 is nul.",
        opties=["x is 2 of x is 3", "x is min 2 of x is min 3", "x is 1 of x is 6", "x is 5 of x is 6"],
        antwoord=0,
        uitleg="Zoek twee getallen met som 5 en product 6. De ontbinding is (x min 2)(x min 3).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de ontbinding van x kwadraat plus 6x plus 9?",
        opties=["(x plus 3) in het kwadraat", "(x min 3) in het kwadraat", "(x plus 3)(x min 3)", "(x plus 9)(x plus 1)"],
        antwoord=0,
        uitleg="Dit is een volkomen kwadraat: a kwadraat plus 2ab plus b kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de ontbinding van x kwadraat min 16?",
        opties=["(x min 4)(x plus 4)", "(x min 4) in het kwadraat", "(x min 8)(x plus 2)", "(x min 16)(x plus 1)"],
        antwoord=0,
        uitleg="Het verschil van twee kwadraten: a kwadraat min b kwadraat is (a min b)(a plus b).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoek is 3 meter langer dan breed en heeft een oppervlakte van 40 vierkante meter. Welke vergelijking hoort erbij?",
        opties=[
            "x maal (x plus 3) is 40",
            "x plus (x plus 3) is 40",
            "2x plus 2(x plus 3) is 40",
            "x kwadraat plus 3 is 40",
        ],
        antwoord=0,
        uitleg="Breedte maal lengte. De breedte is 5 meter en de lengte 8 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossingenverzameling van x kwadraat kleiner dan 9?",
        opties=[
            "alle x tussen min 3 en 3",
            "alle x kleiner dan 3",
            "alle x groter dan min 3",
            "alle x kleiner dan min 3 of groter dan 3",
        ],
        antwoord=0,
        uitleg="De parabool ligt onder de x-as tussen haar twee nulwaarden in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je de oplossingen van een vierkantsvergelijking best in de oorspronkelijke vergelijking?",
        opties=[
            "omdat een tekenfout in de discriminant zo meteen opvalt",
            "omdat een vierkantsvergelijking altijd twee oplossingen heeft",
            "omdat de formule enkel geldt bij een positieve a",
            "omdat je anders de ontbinding niet mag gebruiken",
        ],
        antwoord=0,
        uitleg="Invullen kost een halve minuut en vangt de meeste fouten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vierkantsvergelijking heeft altijd twee reële oplossingen.",
        antwoord=False,
        uitleg="Bij een negatieve discriminant zijn het er geen, bij nul precies één.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een product van twee factoren nul is, is minstens één van de factoren nul.",
        antwoord=True,
        uitleg="Daarop steunt het ontbinden in factoren als oplossingsmethode.",
    ),
    dict(
        type="waarofniet",
        vraag="x kwadraat plus 9 is te ontbinden als (x plus 3)(x min 3).",
        antwoord=False,
        uitleg="Dat product geeft x kwadraat min 9. Een som van twee kwadraten is niet te ontbinden.",
    ),
    dict(
        type="waarofniet",
        vraag="De oplossingen van een tweedegraadsvergelijking zijn de nulwaarden van de bijhorende parabool.",
        antwoord=True,
        uitleg="Daar snijdt of raakt de parabool de x-as.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: x kwadraat is 49. Geef de positieve oplossing.",
        antwoord=["7"],
        uitleg="De andere oplossing is min 7.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de discriminant van x kwadraat min 4x plus 4?",
        antwoord=["0", "nul"],
        uitleg="16 min 16. Er is dus precies één oplossing, namelijk 2.",
    ),
    dict(
        type="invultekst",
        vraag="Een rechthoek is 3 m langer dan breed en heeft 40 m² oppervlakte. Hoe breed is hij in meter?",
        antwoord=["5", "5 m", "5 meter"],
        uitleg="5 maal 8 is 40.",
    ),
]
