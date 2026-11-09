# -*- coding: utf-8 -*-
"""De sinusfunctie en de goniometrische cirkel.

Wiskunde basis, derde graad. De fiche vraagt: het beeldpunt van een
georiënteerde hoek op de goniometrische cirkel, de radiaal, omzetten tussen
graden en radialen, het verband tussen een hoek en zijn goniometrische
getallen, de grafiek van sin x opbouwen vanuit de cirkel, en de algemene
sinusfunctie a·sin b(x − c) + d met de transformaties en de kenmerken
periode, amplitude, frequentie, evenwichtslijn en faseverschuiving. Contexten:
getijden, ademhaling, zonlicht, reuzenrad, temperatuur.

Deel 1: cirkel, radialen en sin x. Deel 2: de algemene sinusfunctie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel radialen is \(180°\)?",
        opties=[r"\(\pi\)", r"\(2\pi\)", r"\(\dfrac{\pi}{2}\)", r"\(180\pi\)"],
        antwoord=0,
        uitleg=r"Een halve cirkel is \(180°\) of \(\pi\) rad. Een volledige cirkel is \(2\pi\) rad.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel radialen is \(60°\)?",
        opties=[r"\(\dfrac{\pi}{3}\)", r"\(\dfrac{\pi}{6}\)", r"\(\dfrac{\pi}{4}\)", r"\(\dfrac{2\pi}{3}\)"],
        antwoord=0,
        uitleg=r"\(60° = \dfrac{60}{180} \pi = \dfrac{\pi}{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel graden is \(\dfrac{3\pi}{4}\) rad? Schrijf het getal.",
        antwoord=["135", "135°"],
        uitleg=r"\(\dfrac{3\pi}{4} \cdot \dfrac{180°}{\pi} = 3 \cdot 45° = 135°\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel graden is \(1\) radiaal, afgerond op een graad?",
        opties=[r"\(57°\)", r"\(1°\)", r"\(3°\)", r"\(180°\)"],
        antwoord=0,
        uitleg=r"\(1 \text{ rad} = \dfrac{180°}{\pi} \approx 57{,}3°\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een radiaal?",
        opties=[
            r"de hoek waarbij de boog op de cirkel even lang is als de straal",
            r"de hoek waarbij de boog op de cirkel even lang is als de middellijn",
            r"het honderdste deel van een rechte hoek",
            r"de hoek van een volledige cirkel gedeeld door \(100\)",
        ],
        antwoord=0,
        uitleg=r"Op een cirkel met straal \(1\) is de booglengte gelijk aan de hoek in radialen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het beeldpunt van een hoek \(\alpha\) op de goniometrische cirkel heeft als coördinaat ...",
        opties=[r"\((\cos \alpha, \sin \alpha)\)", r"\((\sin \alpha, \cos \alpha)\)", r"\((\alpha, \sin \alpha)\)", r"\((\tan \alpha, 1)\)"],
        antwoord=0,
        uitleg=r"De \(x\)-coördinaat is de cosinus, de \(y\)-coördinaat de sinus.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\sin \dfrac{\pi}{2}\)? Schrijf het getal.",
        antwoord=["1", "één", "een"],
        uitleg=r"\(\dfrac{\pi}{2}\) is \(90°\): het beeldpunt ligt bovenaan op de cirkel, in \((0, 1)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sin \dfrac{\pi}{6}\)?",
        opties=[r"\(\dfrac{1}{2}\)", r"\(\dfrac{\sqrt{3}}{2}\)", r"\(\dfrac{\sqrt{2}}{2}\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{\pi}{6} = 30°\), en \(\sin 30° = \dfrac{1}{2}\). Dat staat in de tabel van het formularium.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin \pi = 0\).",
        antwoord=True,
        uitleg=r"Bij \(\pi\) rad (\(180°\)) ligt het beeldpunt in \((-1, 0)\): de \(y\)-coördinaat is \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De sinus van een hoek in het derde kwadrant is positief.",
        antwoord=False,
        uitleg=r"In het derde kwadrant ligt het beeldpunt onder de \(x\)-as, dus de sinus is negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In welk kwadrant ligt het beeldpunt van \(\dfrac{5\pi}{4}\)?",
        opties=[r"het derde", r"het tweede", r"het vierde", r"het eerste"],
        antwoord=0,
        uitleg=r"\(\dfrac{5\pi}{4} = 225°\), tussen \(180°\) en \(270°\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(f(x) = \sin x\)?",
        opties=[r"\([-1, 1]\)", r"\([0, 1]\)", r"\(\mathbb{R}\)", r"\([-\pi, \pi]\)"],
        antwoord=0,
        uitleg=r"De \(y\)-coördinaat van een punt op een cirkel met straal \(1\) ligt altijd tussen \(-1\) en \(1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de periode van \(f(x) = \sin x\)?",
        opties=[r"\(2\pi\)", r"\(\pi\)", r"\(1\)", r"\(360\pi\)"],
        antwoord=0,
        uitleg=r"Na een volledige toer, \(2\pi\) rad, komt het beeldpunt op dezelfde plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de nulwaarden van \(\sin x\) op \([0, 2\pi]\)?",
        opties=[r"\(0\), \(\pi\) en \(2\pi\)", r"\(\dfrac{\pi}{2}\) en \(\dfrac{3\pi}{2}\)", r"enkel \(0\)", r"\(0\) en \(\pi\)"],
        antwoord=0,
        uitleg=r"De sinus is nul waar het beeldpunt op de \(x\)-as ligt: bij \(0\), \(\pi\) en \(2\pi\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waar bereikt \(\sin x\) op \([0, 2\pi]\) haar minimum?",
        opties=[r"in \(x = \dfrac{3\pi}{2}\)", r"in \(x = \pi\)", r"in \(x = 0\)", r"in \(x = \dfrac{\pi}{2}\)"],
        antwoord=0,
        uitleg=r"Bij \(270°\) ligt het beeldpunt onderaan op de cirkel: \(\sin \dfrac{3\pi}{2} = -1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin x\) daalt op \(\left[\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right]\).",
        antwoord=True,
        uitleg=r"Van het hoogste punt bovenaan gaat het beeldpunt over links naar het laagste punt onderaan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin(x + 2\pi) = \sin x + 2\pi\).",
        antwoord=False,
        uitleg=r"\(\sin(x + 2\pi) = \sin x\): een volledige toer erbij verandert de sinus niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee hoeken hebben dezelfde sinus. Welk paar kan dat zijn?",
        opties=[r"\(\dfrac{\pi}{6}\) en \(\dfrac{5\pi}{6}\)", r"\(\dfrac{\pi}{6}\) en \(\dfrac{7\pi}{6}\)", r"\(\dfrac{\pi}{6}\) en \(-\dfrac{\pi}{6}\)", r"\(\dfrac{\pi}{6}\) en \(\dfrac{\pi}{3}\)"],
        antwoord=0,
        uitleg=r"\(30°\) en \(150°\) liggen op dezelfde hoogte, symmetrisch ten opzichte van de \(y\)-as. Beide sinussen zijn \(\tfrac{1}{2}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(\sin x\) is symmetrisch ten opzichte van de oorsprong.",
        antwoord=True,
        uitleg=r"\(\sin(-x) = -\sin x\): de sinus is een oneven functie.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken met je rekentoestel \(\sin 2\) (in radialen), afgerond op twee cijfers na de komma.",
        antwoord=["0,91", "0.91"],
        uitleg=r"\(\sin 2 \approx 0{,}909\). Let op: zet je toestel in radialen, anders krijg je \(\sin 2° \approx 0{,}03\).",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"Wat is de amplitude van \(f(x) = 3 \sin x + 1\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"In \(a \sin b(x - c) + d\) is de amplitude \(a\): de afstand van de evenwichtslijn tot een top.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de evenwichtslijn van \(f(x) = 3 \sin x + 1\)?",
        opties=[r"\(y = 1\)", r"\(y = 3\)", r"\(y = 0\)", r"\(y = 4\)"],
        antwoord=0,
        uitleg=r"De evenwichtslijn is \(y = d\). De grafiek schommelt tussen \(1 - 3 = -2\) en \(1 + 3 = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(f(x) = 3 \sin x + 1\)?",
        opties=[r"\([-2, 4]\)", r"\([-3, 3]\)", r"\([1, 4]\)", r"\([-1, 1]\)"],
        antwoord=0,
        uitleg=r"Van evenwichtslijn min amplitude tot evenwichtslijn plus amplitude: \([1 - 3, 1 + 3]\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de periode van \(f(x) = \sin 4x\)?",
        opties=[r"\(\dfrac{\pi}{2}\)", r"\(8\pi\)", r"\(4\)", r"\(2\pi\)"],
        antwoord=0,
        uitleg=r"De periode is \(\dfrac{2\pi}{b} = \dfrac{2\pi}{4} = \dfrac{\pi}{2}\). Een grotere \(b\) maakt de golven korter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe vind je de frequentie uit de periode \(p\)?",
        opties=[r"\(\dfrac{1}{p}\)", r"\(2\pi p\)", r"\(\dfrac{p}{2\pi}\)", r"\(p^{2}\)"],
        antwoord=0,
        uitleg=r"De frequentie is het aantal periodes per eenheid: \(\dfrac{1}{p}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de faseverschuiving van \(f(x) = 2 \sin\left(x - \dfrac{\pi}{3}\right)\)?",
        opties=[r"\(\dfrac{\pi}{3}\) naar rechts", r"\(\dfrac{\pi}{3}\) naar links", r"\(2\) naar boven", r"\(\dfrac{\pi}{3}\) naar boven"],
        antwoord=0,
        uitleg=r"\(f(x - c)\) is een horizontale verschuiving over \(c\) naar rechts. Hier is \(c = \dfrac{\pi}{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie zet \(\sin x\) om in \(\sin 2x\)?",
        opties=[
            r"een horizontale uitrekking met factor \(\dfrac{1}{2}\)",
            r"een verticale uitrekking met factor \(2\)",
            r"een horizontale verschuiving over \(2\)",
            r"een verticale verschuiving over \(2\)",
        ],
        antwoord=0,
        uitleg=r"\(f(k \cdot x)\) met \(k = 2\) drukt de grafiek horizontaal samen tot de helft. De periode wordt \(\pi\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je rekt \(\sin x\) verticaal uit met factor \(5\) en verschuift ze \(2\) eenheden naar boven. Welk voorschrift krijg je?",
        opties=[r"\(5 \sin x + 2\)", r"\(5 \sin(x + 2)\)", r"\(2 \sin x + 5\)", r"\(\sin 5x + 2\)"],
        antwoord=0,
        uitleg=r"Verticale uitrekking: \(5 \sin x\). Verticale verschuiving: \(+ 2\) buiten de sinus.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x) = 4 \sin x\) en \(g(x) = \sin 4x\) hebben dezelfde periode.",
        antwoord=False,
        uitleg=r"\(f\) heeft periode \(2\pi\) en amplitude \(4\). \(g\) heeft amplitude \(1\) en periode \(\dfrac{\pi}{2}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De amplitude is de helft van het verschil tussen het maximum en het minimum.",
        antwoord=True,
        uitleg=r"Van minimum tot maximum is twee keer de amplitude.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een sinusfunctie heeft maximum \(10\) en minimum \(2\). Wat zijn de evenwichtslijn en de amplitude?",
        opties=[r"evenwichtslijn \(y = 6\), amplitude \(4\)", r"evenwichtslijn \(y = 4\), amplitude \(6\)", r"evenwichtslijn \(y = 5\), amplitude \(8\)", r"evenwichtslijn \(y = 6\), amplitude \(8\)"],
        antwoord=0,
        uitleg=r"Evenwichtslijn: \(\dfrac{10 + 2}{2} = 6\). Amplitude: \(\dfrac{10 - 2}{2} = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het water in een haven staat op zijn hoogst \(5\) m en op zijn laagst \(1\) m, met een periode van \(12\) uur. Wat is \(b\) in \(h(t) = a \sin b(t - c) + d\)?",
        opties=[r"\(\dfrac{\pi}{6}\)", r"\(12\)", r"\(\dfrac{\pi}{12}\)", r"\(24\pi\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{2\pi}{b} = 12 \iff b = \dfrac{2\pi}{12} = \dfrac{\pi}{6}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"In dezelfde haven (hoogst \(5\) m, laagst \(1\) m): wat is de amplitude in meter? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(\dfrac{5 - 1}{2} = 2\). De evenwichtslijn ligt op \(3\) m.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een reuzenrad heeft een diameter van \(40\) m. De as staat op \(22\) m hoogte. Eén toer duurt \(10\) minuten. Welke uitspraak is juist over de hoogte van een bakje?",
        opties=[
            r"amplitude \(20\) m, evenwichtslijn \(22\) m, periode \(10\) min",
            r"amplitude \(40\) m, evenwichtslijn \(22\) m, periode \(10\) min",
            r"amplitude \(20\) m, evenwichtslijn \(20\) m, periode \(10\) min",
            r"amplitude \(22\) m, evenwichtslijn \(20\) m, periode \(5\) min",
        ],
        antwoord=0,
        uitleg=r"De straal \(20\) m is de amplitude, de as is de evenwichtslijn en één toer is één periode.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij datzelfde reuzenrad: hoeveel meter hoog is het laagste punt van een bakje? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(22 - 20 = 2\) m boven de grond.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(f(x) = -2 \sin x\) is de grafiek van \(2 \sin x\) gespiegeld rond de \(x\)-as.",
        antwoord=True,
        uitleg=r"Het minteken maakt van elke functiewaarde haar tegengestelde. De amplitude blijft \(2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het maximum van \(f(x) = 2 \sin 3(x - 1) + 5\)?",
        opties=[r"\(7\)", r"\(5\)", r"\(10\)", r"\(3\)"],
        antwoord=0,
        uitleg=r"Evenwichtslijn plus amplitude: \(5 + 2 = 7\). De \(3\) en de \(1\) veranderen enkel de periode en de verschuiving.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een verticale verschuiving van een sinusfunctie verandert haar periode.",
        antwoord=False,
        uitleg=r"Een verticale verschuiving verandert enkel de evenwichtslijn. De periode hangt af van \(b\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een sinusfunctie doet één volledige golf in \(4\) seconden. Wat is de frequentie?",
        opties=[r"\(0{,}25\) per seconde", r"\(4\) per seconde", r"\(\dfrac{\pi}{2}\) per seconde", r"\(8\pi\) per seconde"],
        antwoord=0,
        uitleg=r"Frequentie \(= \dfrac{1}{\text{periode}} = \dfrac{1}{4}\): een kwart golf per seconde.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De ademhaling kan je beschrijven met een sinusfunctie, omdat ze zich steeds na dezelfde tijd herhaalt.",
        antwoord=True,
        uitleg=r"Een periodiek verschijnsel dat op en neer gaat rond een gemiddelde, past bij een sinusmodel.",
    ),
]
