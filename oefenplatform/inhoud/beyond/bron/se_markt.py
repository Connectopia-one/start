# -*- coding: utf-8 -*-
"""Vraag, aanbod en het marktevenwicht.

Het eerste van twee thema's uit "ik begrijp de prijsvorming op de markt", dat
tien procent weegt.

De fiche vraagt hier drie dingen die verder gaan dan begrippen kennen:
  1. gegevens aflezen uit een grafiek met cijfers
  2. overschotten en tekorten herkennen, benoemen **en berekenen**
  3. de marktsituatie analyseren vanuit die cijfers

Punt 2 is de reden dat er in dit thema echte rekenvragen staan. Op het examen
krijgt een kind een grafiek; hier kan dat niet, dus staan de cijfers in de
vraag zelf, als een tabelletje in woorden. Het rekenwerk blijft hetzelfde:
aanbod min vraag is een overschot, vraag min aanbod is een tekort.

De woorden vrager en aanbieder zijn die van de fiche. Vrager is de koper,
aanbieder de verkoper. Verwar de vraagcurve niet met de vraag van één persoon.

Deel 1 is vraag, aanbod, vrager en aanbieder, en het evenwicht.
Deel 2 is overschotten en tekorten, met het rekenwerk erbij.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie is de vrager op een markt?",
        opties=[
            "de koper, die het product wil hebben",
            "de verkoper, die het product aanbiedt",
            "de overheid, die de prijs vastlegt",
            "de producent, die het product maakt",
        ],
        antwoord=0,
        uitleg="Vragen is hier hetzelfde als willen kopen. De aanbieder verkoopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie is de aanbieder op een markt?",
        opties=[
            "de verkoper, die het product op de markt brengt",
            "de koper, die het product wil hebben",
            "de bank, die de aankoop financiert",
            "de overheid, die een subsidie geeft",
        ],
        antwoord=0,
        uitleg="De aanbieder biedt aan, de vrager vraagt. Die twee ontmoeten elkaar op de markt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de gevraagde hoeveelheid als de prijs stijgt?",
        opties=[
            "ze daalt",
            "ze stijgt",
            "ze blijft gelijk",
            "ze stijgt eerst en daalt dan",
        ],
        antwoord=0,
        uitleg="Hoe duurder, hoe minder mensen willen kopen. Daarom daalt de vraagcurve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de aangeboden hoeveelheid als de prijs stijgt?",
        opties=[
            "ze stijgt",
            "ze daalt",
            "ze blijft gelijk",
            "ze daalt eerst en stijgt dan",
        ],
        antwoord=0,
        uitleg="Een hogere prijs maakt verkopen interessanter, dus de aanbodcurve stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de evenwichtsprijs?",
        opties=[
            "de prijs waarbij vraag en aanbod gelijk zijn",
            "de gemiddelde prijs van het afgelopen jaar",
            "de prijs die de overheid vastlegt",
            "de laagste prijs waartegen nog verkocht wordt",
        ],
        antwoord=0,
        uitleg="Op dat punt snijden de twee curven elkaar en blijft er niets over en niets te kort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de evenwichtshoeveelheid?",
        opties=[
            "de hoeveelheid die bij de evenwichtsprijs verhandeld wordt",
            "de hoeveelheid die een bedrijf maximaal kan maken",
            "het gemiddelde van vraag en aanbod",
            "de hoeveelheid waarbij de winst het hoogst is",
        ],
        antwoord=0,
        uitleg="Bij de evenwichtsprijs hoort precies één hoeveelheid: die waar de curven snijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 4 euro per stuk vragen de kopers 300 stuks en bieden de verkopers 300 stuks aan. Wat is 4 euro?",
        opties=[
            "de evenwichtsprijs",
            "een maximumprijs",
            "een minimumprijs",
            "een prijs met een overschot",
        ],
        antwoord=0,
        uitleg="Vraag en aanbod zijn gelijk, dus dit is het evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af op de horizontale as van een vraag- en aanbodgrafiek?",
        opties=[
            "de hoeveelheid",
            "de prijs",
            "de winst",
            "de tijd",
        ],
        antwoord=0,
        uitleg="De prijs staat op de verticale as, de hoeveelheid op de horizontale.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af op de verticale as van een vraag- en aanbodgrafiek?",
        opties=["de prijs", "de hoeveelheid", "het aantal verkopers", "de omzet"],
        antwoord=0,
        uitleg="De prijs verticaal, de hoeveelheid horizontaal. Dat is de afspraak op de productmarkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de markt waarop goederen en diensten verhandeld worden?",
        opties=[
            "de productmarkt",
            "de arbeidsmarkt",
            "de kapitaalmarkt",
            "de geldmarkt",
        ],
        antwoord=0,
        uitleg="De fiche spreekt letterlijk over het marktmechanisme op de productmarkt.",
    ),
    dict(
        type="waarofniet",
        vraag="De vraagcurve daalt als de prijs stijgt.",
        antwoord=True,
        uitleg="Hoe hoger de prijs, hoe minder er gevraagd wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="De aanbodcurve daalt als de prijs stijgt.",
        antwoord=False,
        uitleg="Omgekeerd: bij een hogere prijs willen verkopers meer aanbieden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de evenwichtsprijs blijft er geen onverkochte voorraad over.",
        antwoord=True,
        uitleg="Vraag en aanbod zijn dan precies gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De vrager is volgens de fiche de verkoper.",
        antwoord=False,
        uitleg="De vrager is de koper. De verkoper is de aanbieder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er bij de evenwichtsprijs?",
        opties=[
            "vraag en aanbod zijn gelijk",
            "er is geen overschot",
            "er is geen tekort",
            "de prijs kan niet meer veranderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De prijs kan wel veranderen: als een curve verschuift, komt er een nieuw evenwicht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt de fiche de koper op een markt?",
        antwoord=["vrager", "de vrager"],
        uitleg="De vrager vraagt, de aanbieder biedt aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt de fiche de verkoper op een markt?",
        antwoord=["aanbieder", "de aanbieder"],
        uitleg="Hij brengt het product op de markt tegen een bepaalde prijs.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de prijs waarbij vraag en aanbod gelijk zijn?",
        antwoord=["evenwichtsprijs", "de evenwichtsprijs"],
        uitleg="De hoeveelheid die daarbij hoort, is de evenwichtshoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 6 euro vragen de kopers 100 stuks en bieden de verkopers 180 aan. Bij 5 euro vragen ze 140 en bieden ze 140 aan. Wat is de evenwichtsprijs?",
        opties=["5 euro", "6 euro", "5,50 euro", "dat valt niet te zeggen"],
        antwoord=0,
        uitleg="Bij 5 euro zijn vraag en aanbod allebei 140. Dat is het snijpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="En wat is in dat voorbeeld de evenwichtshoeveelheid?",
        opties=["140 stuks", "100 stuks", "180 stuks", "280 stuks"],
        antwoord=0,
        uitleg="Bij de evenwichtsprijs van 5 euro wordt 140 stuks verhandeld.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is er een overschot op de markt?",
        opties=[
            "als het aanbod groter is dan de vraag",
            "als de vraag groter is dan het aanbod",
            "als de prijs onder de evenwichtsprijs ligt",
            "als er geen enkele verkoper meer is",
        ],
        antwoord=0,
        uitleg="Er blijft dan voorraad over. Dat gebeurt bij een prijs boven het evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is er een tekort op de markt?",
        opties=[
            "als de vraag groter is dan het aanbod",
            "als het aanbod groter is dan de vraag",
            "als de prijs boven de evenwichtsprijs ligt",
            "als er geen enkele koper meer is",
        ],
        antwoord=0,
        uitleg="Er zijn dan te weinig stuks voor alle kopers. Dat gebeurt bij een prijs onder het evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 8 euro vragen de kopers 90 stuks en bieden de verkopers 150 aan. Hoe groot is het overschot?",
        opties=["60 stuks", "90 stuks", "150 stuks", "240 stuks"],
        antwoord=0,
        uitleg="150 min 90 is 60. Aanbod min vraag geeft het overschot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 3 euro vragen de kopers 220 stuks en bieden de verkopers 160 aan. Hoe groot is het tekort?",
        opties=["60 stuks", "160 stuks", "220 stuks", "380 stuks"],
        antwoord=0,
        uitleg="220 min 160 is 60. Vraag min aanbod geeft het tekort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een prijs ligt boven de evenwichtsprijs. Wat zie je op de markt?",
        opties=[
            "een overschot",
            "een tekort",
            "een nieuw evenwicht",
            "niets, de prijs maakt geen verschil",
        ],
        antwoord=0,
        uitleg="Bij een hoge prijs bieden verkopers veel aan en willen kopers weinig. Er blijft dus over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een prijs ligt onder de evenwichtsprijs. Wat zie je op de markt?",
        opties=[
            "een tekort",
            "een overschot",
            "een nieuw evenwicht",
            "een verschuiving van de vraagcurve",
        ],
        antwoord=0,
        uitleg="Bij een lage prijs willen veel mensen kopen en bieden verkopers weinig aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de prijs als er een overschot is en de overheid niets doet?",
        opties=[
            "de prijs zakt naar het evenwicht",
            "de prijs stijgt verder",
            "de prijs blijft onveranderd",
            "de prijs wordt door de vragers vastgelegd",
        ],
        antwoord=0,
        uitleg="Verkopers met onverkochte voorraad zakken met hun prijs tot de markt in evenwicht komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de prijs als er een tekort is en de overheid niets doet?",
        opties=[
            "de prijs stijgt naar het evenwicht",
            "de prijs zakt verder",
            "de prijs blijft onveranderd",
            "de hoeveelheid daalt mee",
        ],
        antwoord=0,
        uitleg="Kopers zijn bereid meer te betalen, dus de prijs klimt tot het evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 10 euro vragen de kopers 50 stuks en bieden de verkopers 50 aan. Hoe groot is het overschot?",
        opties=["er is geen overschot", "50 stuks", "100 stuks", "10 stuks"],
        antwoord=0,
        uitleg="Vraag en aanbod zijn gelijk, dus dit is het evenwicht en er blijft niets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een marktkramer houdt elke avond kratten over. Wat zegt dat over zijn prijs?",
        opties=[
            "ze ligt boven de evenwichtsprijs",
            "ze ligt onder de evenwichtsprijs",
            "ze is precies de evenwichtsprijs",
            "ze zegt niets over het evenwicht",
        ],
        antwoord=0,
        uitleg="Overschot betekent een te hoge prijs. Zakt hij, dan verkoopt hij alles.",
    ),
    dict(
        type="waarofniet",
        vraag="Een overschot ontstaat bij een prijs boven de evenwichtsprijs.",
        antwoord=True,
        uitleg="Veel aanbod, weinig vraag, dus voorraad die overblijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Je berekent een tekort door het aanbod van de vraag af te trekken.",
        antwoord=True,
        uitleg="Vraag min aanbod geeft het tekort. Omgekeerd krijg je het overschot.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een tekort zal de prijs zakken.",
        antwoord=False,
        uitleg="Bij een tekort stijgt de prijs, tot de markt weer in evenwicht komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Er kan tegelijk een overschot en een tekort op dezelfde markt zijn bij dezelfde prijs.",
        antwoord=False,
        uitleg="Bij één prijs is het één van de twee, of geen van beide als je in het evenwicht zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een overschot op de markt?",
        opties=[
            "het aanbod is groter dan de vraag",
            "de prijs ligt boven het evenwicht",
            "er blijft onverkochte voorraad over",
            "de kopers zijn bereid meer te betalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meer willen betalen hoort bij een tekort, niet bij een overschot.",
    ),
    dict(
        type="invultekst",
        vraag="Bij 7 euro is de vraag 120 stuks en het aanbod 200 stuks. Hoe groot is het overschot? Antwoord met een getal.",
        antwoord=["80"],
        uitleg="200 min 120 is 80 stuks die overblijven.",
    ),
    dict(
        type="invultekst",
        vraag="Bij 2 euro is de vraag 310 stuks en het aanbod 250 stuks. Hoe groot is het tekort? Antwoord met een getal.",
        antwoord=["60"],
        uitleg="310 min 250 is 60 stuks te weinig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de situatie waarin het aanbod groter is dan de vraag? Antwoord met één woord.",
        antwoord=["overschot", "een overschot"],
        uitleg="Het tegenovergestelde is een tekort, met de vraag groter dan het aanbod.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 9 euro is de vraag 80 en het aanbod 140. Bij 7 euro is de vraag 110 en het aanbod 110. Welke prijs geeft een overschot van 60?",
        opties=["9 euro", "7 euro", "beide prijzen", "geen van beide"],
        antwoord=0,
        uitleg="Bij 9 euro is 140 min 80 gelijk aan 60. Bij 7 euro is er evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel verkoopt al om tien uur 's ochtends uit en moet mensen wegsturen. Wat zegt dat over de prijs?",
        opties=[
            "ze ligt onder de evenwichtsprijs",
            "ze ligt boven de evenwichtsprijs",
            "ze is precies de evenwichtsprijs",
            "ze is door de overheid vastgelegd",
        ],
        antwoord=0,
        uitleg="Een tekort wijst op een te lage prijs tegenover wat de mensen willen betalen.",
    ),
]
