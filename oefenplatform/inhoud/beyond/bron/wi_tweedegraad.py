# -*- coding: utf-8 -*-
r"""Tweedegraadsfuncties en de transformaties van hun grafiek.

Het onderdeel "Tweedegraadsfuncties" van de analysefiche G1. De fiche vraagt
twee dingen: van voorschrift naar grafiek en terug, en de vier transformaties
van de grafiek van \(x^{2}\) kunnen benoemen en uitvoeren.

Deel 1 is de parabool zelf: top, nulwaarden, symmetrieas, bereik.
Deel 2 zijn de vier transformaties en wat ze met de kenmerken doen.

In echte wiskundige notatie, tussen \( en \); zie oefenplatform/lib/wiskunde.ts.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe heet de grafiek van een tweedegraadsfunctie?",
        opties=["een parabool", "een hyperbool", "een sinusoïde", "een rechte"],
        antwoord=0,
        uitleg=r"De grafiek van \(f(x)=\tfrac{1}{x}\) heet een hyperbool, die van een eerstegraadsfunctie een rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer spreek je van een dalparabool?",
        opties=[
            r"als \(a>0\)",
            r"als \(a<0\)",
            r"als \(c>0\)",
            r"als er twee verschillende nulwaarden zijn",
        ],
        antwoord=0,
        uitleg=r"Alleen het teken van \(a\) bepaalt de opening. Bij \(a<0\) krijg je een bergparabool met een maximum.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=x^{2}-6x+5\). Wat is de \(x\)-coördinaat van de top? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"De top ligt bij \(x=\dfrac{-b}{2a}=\dfrac{6}{2}=3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De symmetrieas van een parabool gaat altijd door haar top.",
        antwoord=True,
        uitleg=r"Ze is de verticale rechte door de top, en die legt de twee takken precies op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de discriminant van \(ax^{2}+bx+c\)?",
        opties=[
            r"\(D=b^{2}-4ac\)",
            r"\(D=b^{2}+4ac\)",
            r"\(D=4ac-b^{2}\)",
            r"\(D=a^{2}-4bc\)",
        ],
        antwoord=0,
        uitleg=r"Het teken van die uitkomst beslist over het aantal reële nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel nulwaarden heeft een tweedegraadsfunctie met \(D=0\)?",
        opties=[r"één", r"twee", r"geen", r"oneindig veel"],
        antwoord=0,
        uitleg=r"De parabool raakt de \(x\)-as dan precies in haar top, zonder erdoorheen te gaan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een parabool kan de \(y\)-as twee keer snijden.",
        antwoord=False,
        uitleg=r"Voor \(x=0\) is er maar één functiewaarde, namelijk \(c\). Elke functiegrafiek snijdt de \(y\)-as hoogstens één keer.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=x^{2}-6x+5\). Wat is de \(y\)-coördinaat van de top? Schrijf het getal.",
        antwoord=["-4", "min 4"],
        uitleg=r"\(f(3)=9-18+5=-4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de nulwaarden van \(x^{2}-6x+5\)?",
        opties=[r"\(1\) en \(5\)", r"\(-1\) en \(-5\)", r"\(2\) en \(3\)", r"\(0\) en \(6\)"],
        antwoord=0,
        uitleg=r"Je zoekt twee getallen met som \(6\) en product \(5\). De ontbinding is \((x-1)(x-5)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Heeft een parabool twee nulwaarden, dan ligt de \(x\) van de top precies in het midden ertussen.",
        antwoord=True,
        uitleg=r"De symmetrieas staat midden tussen de twee snijpunten met de \(x\)-as, dus \(x_{\text{top}}\) is hun gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een dalparabool heeft als top \((3,-4)\). Wat is haar bereik?",
        opties=[
            r"\(\left[-4,+\infty\right[\)",
            r"\(\left]-\infty,-4\right]\)",
            r"\(\left[3,+\infty\right[\)",
            r"\(\mathbb{R}\)",
        ],
        antwoord=0,
        uitleg=r"Bij een dalparabool is de top het laagste punt, dus \(-4\) is de kleinste functiewaarde en alles erboven komt voor.",
    ),
    dict(
        type="invultekst",
        vraag=r"Waar snijdt \(f(x)=x^{2}-6x+5\) de \(y\)-as? Schrijf de \(y\)-waarde.",
        antwoord=["5", "vijf"],
        uitleg=r"\(f(0)=c=5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vergelijking heeft de symmetrieas van een parabool met top \((2,7)\)?",
        opties=[r"\(x=2\)", r"\(y=7\)", r"\(x=7\)", r"\(y=2\)"],
        antwoord=0,
        uitleg=r"De symmetrieas is verticaal, dus van de vorm \(x=\) een getal, en dat getal is de \(x\) van de top.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een bergparabool heeft altijd een minimum.",
        antwoord=False,
        uitleg=r"Een bergparabool opent naar beneden, dus haar top is een maximum. Ze heeft helemaal geen kleinste waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je leest het voorschrift \(f(x)=a(x-p)^{2}+q\). Wat lees je daar meteen uit af?",
        opties=[
            r"de top is \((p,q)\)",
            r"de top is \((-p,q)\)",
            r"de nulwaarden zijn \(p\) en \(q\)",
            r"de symmetrieas is \(y=q\)",
        ],
        antwoord=0,
        uitleg=r"Dat heet de topvorm. Let op het minteken: \((x-3)^{2}\) geeft een top in \(x=3\), niet in \(x=-3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel punten heb je minstens nodig om één parabool vast te leggen?",
        opties=[r"\(3\)", r"\(2\)", r"\(4\)", r"\(1\)"],
        antwoord=0,
        uitleg=r"Er zijn drie onbekende coëfficiënten \(a\), \(b\) en \(c\), dus je hebt drie vergelijkingen nodig.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Hoe groter \(|a|\), hoe smaller de parabool.",
        antwoord=True,
        uitleg=r"Een grote \(|a|\) rekt de grafiek verticaal uit, waardoor ze steiler en dus smaller oogt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel reële nulwaarden heeft een tweedegraadsfunctie met \(D<0\)? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg=r"De parabool ligt dan volledig boven of volledig onder de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de top van \(f(x)=-x^{2}+4x\)?",
        opties=[r"\((2,4)\)", r"\((4,2)\)", r"\((-2,4)\)", r"\((2,-4)\)"],
        antwoord=0,
        uitleg=r"\(x=\dfrac{-4}{-2}=2\), en \(f(2)=-4+8=4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke \(m\) raakt de parabool \(y=x^{2}-6x+m\) de \(x\)-as?",
        opties=[r"\(m=9\)", r"\(m=6\)", r"\(m=-9\)", r"\(m=3\)"],
        antwoord=0,
        uitleg=r"Raken wil zeggen \(D=0\): \(36-4m=0\), dus \(m=9\). Het voorschrift wordt dan \((x-3)^{2}\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat doet de grafiek van \(f(x)+3\), vergeleken met die van \(f\)?",
        opties=[
            r"ze schuift \(3\) omhoog",
            r"ze schuift \(3\) omlaag",
            r"ze schuift \(3\) naar rechts",
            r"ze wordt \(3\) keer verticaal uitgerekt",
        ],
        antwoord=0,
        uitleg=r"Wat buiten de functie bij de uitkomst komt, werkt verticaal. Wat binnen de haakjes bij \(x\) komt, werkt horizontaal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat doet de grafiek van \(f(x-2)\), vergeleken met die van \(f\)?",
        opties=[
            r"ze schuift \(2\) naar rechts",
            r"ze schuift \(2\) naar links",
            r"ze schuift \(2\) omlaag",
            r"ze wordt \(2\) keer samengedrukt",
        ],
        antwoord=0,
        uitleg=r"Een min binnen de haakjes schuift naar rechts. Dat voelt omgekeerd aan, en net daar gaat het meestal mis.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je gaat van \(x^{2}\) naar \(x^{2}-5\). Hoeveel eenheden schuift de grafiek omlaag? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"De hele grafiek zakt \(5\) eenheden, dus ook de top.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(f(x+3)\) ligt \(3\) eenheden naar links.",
        antwoord=True,
        uitleg=r"Binnen de haakjes werkt alles omgekeerd: plus schuift naar links, min schuift naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie hoort bij \(-f(x)\)?",
        opties=[
            r"een spiegeling om de \(x\)-as",
            r"een spiegeling om de \(y\)-as",
            r"een verschuiving van \(1\) omlaag",
            r"een spiegeling om \(y=x\)",
        ],
        antwoord=0,
        uitleg=r"Elke functiewaarde wisselt van teken, dus wat boven de \(x\)-as lag, komt er even ver onder te liggen. \(f(-x)\) spiegelt om de \(y\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie hoort bij \(3f(x)\)?",
        opties=[
            r"een verticale uitrekking met factor \(3\)",
            r"een horizontale uitrekking met factor \(3\)",
            r"een verschuiving van \(3\) omhoog",
            r"een verschuiving van \(3\) naar rechts",
        ],
        antwoord=0,
        uitleg=r"Alle functiewaarden worden verdrievoudigd, dus de grafiek wordt driemaal zo hoog uitgerekt vanaf de \(x\)-as.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(2x^{2}\) is breder dan die van \(x^{2}\).",
        antwoord=False,
        uitleg=r"Ze is net smaller: elke functiewaarde verdubbelt, dus de parabool loopt sneller omhoog.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=(x-4)^{2}+1\). Wat is de \(x\)-coördinaat van de top? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"In de topvorm lees je de top rechtstreeks af: \((4,1)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie laat de nulwaarden van een functie onveranderd?",
        opties=[
            r"\(3f(x)\)",
            r"\(f(x)+3\)",
            r"\(f(x-2)\)",
            r"\(f(x)-1\)",
        ],
        antwoord=0,
        uitleg=r"\(3\cdot 0=0\), dus de snijpunten met de \(x\)-as blijven staan. Elke verschuiving verplaatst ze wel.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een verticale verschuiving verandert het bereik van een functie.",
        antwoord=True,
        uitleg=r"Alle functiewaarden schuiven mee op, dus het bereik schuift evenveel op.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformaties brengen je van \(x^{2}\) naar \((x+1)^{2}-3\)?",
        opties=[
            r"\(1\) naar links en \(3\) omlaag",
            r"\(1\) naar rechts en \(3\) omlaag",
            r"\(1\) naar links en \(3\) omhoog",
            r"\(3\) naar links en \(1\) omlaag",
        ],
        antwoord=0,
        uitleg=r"Plus \(1\) binnen de haakjes schuift naar links, \(-3\) erbuiten schuift omlaag. De top komt op \((-1,-3)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=(x-2)^{2}+7\). Wat is de kleinste functiewaarde? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"Een kwadraat is minstens \(0\), dus de kleinste waarde is \(7\), bereikt in \(x=2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je spiegelt een dalparabool om de \(x\)-as. Wat krijg je?",
        opties=[
            r"een bergparabool met een maximum",
            r"een dalparabool die hoger ligt",
            r"dezelfde parabool, maar smaller",
            r"een rechte door de oude top",
        ],
        antwoord=0,
        uitleg=r"Het teken van \(a\) draait om, dus de opening keert en het minimum wordt een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een horizontale verschuiving verandert het domein van een tweedegraadsfunctie.",
        antwoord=False,
        uitleg=r"Het domein van elke tweedegraadsfunctie is \(\mathbb{R}\), en dat blijft zo na verschuiven. Bij een wortelfunctie zou het wel veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke drie transformaties brengen je van \(x^{2}\) naar \(2(x-1)^{2}+3\)?",
        opties=[
            r"\(1\) naar rechts, verticaal uitrekken met \(2\), \(3\) omhoog",
            r"\(1\) naar links, verticaal uitrekken met \(2\), \(3\) omhoog",
            r"\(2\) naar rechts, verticaal uitrekken met \(1\), \(3\) omhoog",
            r"\(1\) naar rechts, spiegelen om de \(x\)-as, \(3\) omlaag",
        ],
        antwoord=0,
        uitleg=r"De top komt op \((1,3)\), en de factor \(2\) maakt de parabool smaller.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je schuift een parabool \(2\) omhoog. Wat gebeurt er met haar tekenverloop?",
        opties=[
            r"het kan veranderen, want de nulwaarden verschuiven",
            r"het blijft precies hetzelfde",
            r"het keert overal om van teken",
            r"het verdwijnt, want er zijn geen nulwaarden meer",
        ],
        antwoord=0,
        uitleg=r"Een dalparabool die net onder de as lag, kan er helemaal boven komen. Dan is ze overal positief en zijn de nulwaarden weg.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een verticale verschuiving laat de symmetrieas van een parabool op haar plaats.",
        antwoord=True,
        uitleg=r"Alleen de hoogte verandert. De \(x\) van de top blijft dezelfde, dus ook de verticale symmetrieas.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=2(x-1)^{2}+3\). Wat is de \(y\)-coördinaat van de top? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"De factor \(2\) verandert de ligging van de top niet, alleen de breedte van de parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe verloopt de linkertak van een gewone dalparabool?",
        opties=[
            r"ze daalt, met een afnemende daling",
            r"ze daalt, met een toenemende daling",
            r"ze stijgt, met een toenemende stijging",
            r"ze stijgt, met een afnemende stijging",
        ],
        antwoord=0,
        uitleg=r"Links van de top gaat de grafiek omlaag, maar steeds minder steil, tot ze in de top even vlak loopt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een parabool heeft top \((4,2)\) en gaat door \((5,5)\). Welk voorschrift past?",
        opties=[
            r"\(y=3(x-4)^{2}+2\)",
            r"\(y=3(x+4)^{2}+2\)",
            r"\(y=(x-4)^{2}+2\)",
            r"\(y=3(x-4)^{2}-2\)",
        ],
        antwoord=0,
        uitleg=r"Begin met de topvorm \(y=a(x-4)^{2}+2\) en vul \((5,5)\) in: \(a\cdot 1+2=5\), dus \(a=3\).",
    ),
]
