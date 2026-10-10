# -*- coding: utf-8 -*-
r"""Een functie aflezen van haar grafiek, en de inverse functie.

Het onderdeel "Grafisch onderzoek" van de analysefiche G1. De fiche somt daar
een lange lijst functiekenmerken op, en vraagt uitdrukkelijk dat je van elke
voorstellingswijze naar elke andere kan overstappen: verwoording, tabel,
grafiek en voorschrift.

Deel 1 zijn de functiekenmerken. Deel 2 is de inverse functie en de spiegeling
om de eerste bissectrice.

In echte wiskundige notatie, tussen \( en \); zie oefenplatform/lib/wiskunde.ts.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\text{dom}\,f\)?",
        opties=[
            r"alle \(x\) waarvoor \(f(x)\) bestaat",
            r"alle waarden die \(f\) aanneemt",
            r"alle \(x\) waar de grafiek stijgt",
            r"alle punten waar de grafiek de assen snijdt",
        ],
        antwoord=0,
        uitleg=r"Het domein ligt op de \(x\)-as. De verzameling van de functiewaarden heet het bereik, \(\text{ber}\,f\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen een nulwaarde en een nulpunt?",
        opties=[
            r"een nulwaarde is een getal, een nulpunt is een punt",
            r"een nulwaarde ligt op de \(y\)-as, een nulpunt op de \(x\)-as",
            r"een nulwaarde hoort bij een stijgende functie, een nulpunt bij een dalende",
            r"er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg=r"De nulwaarde is de \(x\) waarvoor \(f(x)=0\). Het nulpunt is het punt \((x,0)\) op de grafiek.",
    ),
    dict(
        type="invultekst",
        vraag=r"Eén getal hoort niet bij \(\text{dom}\,f\) voor \(f(x)=\dfrac{1}{x-5}\). Welk getal?",
        antwoord=["5", "vijf"],
        uitleg=r"Voor \(x=5\) wordt de noemer \(0\), en delen door \(0\) kan niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het bereik van \(f\) is de verzameling van alle waarden \(f(x)\) die ze aanneemt.",
        antwoord=True,
        uitleg=r"Het bereik lees je af op de \(y\)-as: van onder naar boven, zover de grafiek reikt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waaraan herken je op een grafiek dat \(f\) een even functie is?",
        opties=[
            r"ze is symmetrisch om de \(y\)-as",
            r"ze is symmetrisch om de oorsprong",
            r"ze snijdt de \(y\)-as in een even getal",
            r"ze heeft een even aantal nulwaarden",
        ],
        antwoord=0,
        uitleg=r"Even wil zeggen \(f(-x)=f(x)\). De grafiek valt dus op zichzelf na spiegeling om de \(y\)-as; \(f(x)=x^{2}\) is het schoolvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor een functie geldt \(f(-x)=-f(x)\). Wat weet je dan?",
        opties=[
            r"ze is oneven en symmetrisch om de oorsprong",
            r"ze is even en symmetrisch om de \(y\)-as",
            r"ze is strikt dalend op haar hele domein",
            r"ze heeft geen enkele nulwaarde",
        ],
        antwoord=0,
        uitleg=r"Dat is de definitie van een oneven functie. Een halve draai om de oorsprong legt de grafiek op zichzelf; \(f(x)=x^{3}\) is het schoolvoorbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een grafiek die symmetrisch is om de oorsprong hoort bij een even functie.",
        antwoord=False,
        uitleg=r"Symmetrie om de oorsprong hoort bij een oneven functie, \(f(-x)=-f(x)\). Even functies zijn symmetrisch om de \(y\)-as.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een sinusgrafiek schommelt tussen \(-3\) en \(3\), rond de \(x\)-as. Wat is haar amplitude? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"De amplitude is de afstand van de evenwichtslijn tot de top, dus \(\tfrac{3-(-3)}{2}=3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een buigpunt op een grafiek?",
        opties=[
            r"het punt waar hol in bol overgaat",
            r"het punt waar stijgen in dalen overgaat",
            r"het punt waar de grafiek de \(x\)-as snijdt",
            r"het laagste punt van de hele grafiek",
        ],
        antwoord=0,
        uitleg=r"Een buigpunt gaat over de kromming, niet over de richting. Waar stijgen in dalen overgaat, ligt een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een maximum bereikt de functie altijd haar grootste waarde op het hele domein.",
        antwoord=False,
        uitleg=r"Dat geldt voor een absoluut maximum. Een plaatselijk maximum is alleen de hoogste waarde in zijn eigen omgeving; verderop kan de grafiek nog hoger gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent een toenemende stijging?",
        opties=[
            r"de grafiek stijgt en wordt daarbij almaar steiler",
            r"de grafiek stijgt en wordt daarbij almaar vlakker",
            r"de grafiek stijgt eerst en daalt daarna weer",
            r"de grafiek stijgt met een vaste helling verder",
        ],
        antwoord=0,
        uitleg=r"Bij een afnemende stijging gaat de grafiek wel nog omhoog, maar met een kleinere helling. Bij een vaste helling spreek je van lineaire groei.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een grafiek herhaalt zich precies om de vier eenheden. Wat is haar periode? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"De periode is de kleinste \(p>0\) waarvoor \(f(x+p)=f(x)\) voor elke \(x\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het praktisch domein van een functie?",
        opties=[
            r"het stuk van het domein dat zinvol is in de context",
            r"het deel van het domein waar de functie stijgt",
            r"het domein zonder de nulwaarden",
            r"het domein van \(f'\)",
        ],
        antwoord=0,
        uitleg=r"Bij een model voor de hoogte van een plant is een negatieve tijd betekenisloos, ook al hoort ze bij het wiskundige domein.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een verticale rechte mag de grafiek van een functie hoogstens één keer snijden.",
        antwoord=True,
        uitleg=r"Bij twee snijpunten zouden er voor dezelfde \(x\) twee waarden \(f(x)\) zijn, en dan is het geen functie meer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat lees je af in een tekenverloop?",
        opties=[
            r"waar \(f(x)>0\) en waar \(f(x)<0\)",
            r"waar de functie stijgt en waar ze daalt",
            r"waar de grafiek hol is en waar ze bol is",
            r"hoe snel de functiewaarden veranderen",
        ],
        antwoord=0,
        uitleg=r"Het tekenverloop gaat over boven of onder de \(x\)-as. Stijgen en dalen is het verloop, en dat lees je af uit \(f'\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x)=\dfrac{2x+1}{x-3}\)?",
        opties=[r"\(y=2\)", r"\(y=3\)", r"\(y=0\)", r"\(y=-\tfrac{1}{3}\)"],
        antwoord=0,
        uitleg=r"Voor grote \(|x|\) wegen alleen de hoogste graden mee: \(\tfrac{2x}{x}=2\). De grafiek kruipt dus naar de hoogte \(2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke functie heeft minstens één asymptoot.",
        antwoord=False,
        uitleg=r"Een parabool of een rechte heeft er geen enkele. Asymptoten horen vooral bij rationale, exponentiële en logaritmische functies.",
    ),
    dict(
        type="invultekst",
        vraag=r"Voor welke \(x\) ligt de verticale asymptoot van \(f(x)=\dfrac{2x+1}{x-3}\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"Daar wordt de noemer \(0\) terwijl de teller dat niet is, dus de functiewaarden schieten naar \(\pm\infty\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rij noemt de vier voorstellingswijzen van een functie?",
        opties=[
            r"verwoording, tabel, grafiek en voorschrift",
            r"verwoording, tekening, formule en getal",
            r"domein, bereik, nulwaarden en extrema",
            r"tabel, grafiek, afgeleide en primitieve",
        ],
        antwoord=0,
        uitleg=r"Op het examen moet je van elke voorstellingswijze naar elke andere kunnen overstappen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat bedoelt men met het gedrag van \(f\) op oneindig?",
        opties=[
            r"wat er met \(f(x)\) gebeurt als \(x\to\pm\infty\)",
            r"de waarde die \(f\) in \(\infty\) zelf aanneemt",
            r"het aantal nulwaarden op het hele domein",
            r"de hoogte aan het einde van het praktisch domein",
        ],
        antwoord=0,
        uitleg=r"Oneindig is geen getal, dus de functie heeft daar geen waarde. Je kijkt naar waar de waarden naartoe kruipen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Om welke rechte spiegel je de grafiek van \(f\) om die van \(f^{-1}\) te krijgen?",
        opties=[
            r"de eerste bissectrice",
            r"de \(y\)-as",
            r"de \(x\)-as",
            r"de tweede bissectrice",
        ],
        antwoord=0,
        uitleg=r"Dat werkt alleen in een orthonormaal assenstelsel, waar beide assen dezelfde eenheid hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vergelijking heeft de eerste bissectrice?",
        opties=[r"\(y=x\)", r"\(y=-x\)", r"\(y=0\)", r"\(x=0\)"],
        antwoord=0,
        uitleg=r"Ze deelt het eerste en het derde kwadrant doormidden. \(y=-x\) is de tweede bissectrice.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel keer mag een horizontale rechte de grafiek van een inverteerbare functie hoogstens snijden? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Bij twee snijpunten zouden twee \(x\)-waarden dezelfde \(f(x)\) hebben, en dan weet \(f^{-1}\) niet welke ze moet teruggeven.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafieken van \(f\) en \(f^{-1}\) zijn elkaars spiegelbeeld om de rechte \(y=x\).",
        antwoord=True,
        uitleg=r"Elk punt \((a,b)\) van \(f\) wordt \((b,a)\) bij \(f^{-1}\), en dat is net die spiegeling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is een functie niet inverteerbaar?",
        opties=[
            r"als een horizontale rechte de grafiek meer dan één keer snijdt",
            r"als een verticale rechte de grafiek meer dan één keer snijdt",
            r"als de grafiek de eerste bissectrice nergens snijdt",
            r"als ze op een deel van haar domein negatief wordt",
        ],
        antwoord=0,
        uitleg=r"Dan hoort dezelfde functiewaarde bij meerdere \(x\)-waarden, en de gespiegelde grafiek is geen functie meer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de inverse van \(f(x)=a^{x}\)?",
        opties=[
            r"\(f^{-1}(x)=\log_{a}x\)",
            r"\(f^{-1}(x)=x^{a}\)",
            r"\(f^{-1}(x)=(-a)^{x}\)",
            r"\(f^{-1}(x)=\sqrt[a]{x}\)",
        ],
        antwoord=0,
        uitleg=r"De logaritme geeft net de exponent terug. Daarom zijn hun grafieken elkaars spiegelbeeld om \(y=x\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x)=x^{2}\) is inverteerbaar op heel \(\mathbb{R}\).",
        antwoord=False,
        uitleg=r"\(2\) en \(-2\) hebben hetzelfde kwadraat, dus een horizontale rechte snijdt de parabool twee keer. Pas op \(\left[0,+\infty\right[\) lukt het wel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Tot welk domein beperk je \(f(x)=x^{2}\) om ze inverteerbaar te maken?",
        opties=[
            r"\(\left[0,+\infty\right[\)",
            r"\(\left]1,+\infty\right[\)",
            r"\(\left[-1,1\right]\)",
            r"\(\mathbb{Z}\setminus\{0\}\)",
        ],
        antwoord=0,
        uitleg=r"Op die helft is de parabool strikt stijgend, en dan is \(f^{-1}(x)=\sqrt{x}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvan is \(\arcsin\) de inverse?",
        opties=[
            r"van \(\sin\) op een beperkt domein",
            r"van \(\cos\) op haar hele domein",
            r"van \(\tan\) op een beperkt domein",
            r"van \(\sin\) op haar hele domein",
        ],
        antwoord=0,
        uitleg=r"De sinus herhaalt zich, dus je kiest eerst een stuk waarop ze strikt stijgt, meestal \(\left[-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\text{dom}\,f^{-1}=\text{ber}\,f\).",
        antwoord=True,
        uitleg=r"Bij het spiegelen wisselen de assen van rol, dus domein en bereik wisselen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke twee functies zijn elkaars inverse op \(\left[0,+\infty\right[\)?",
        opties=[
            r"\(x^{2}\) en \(\sqrt{x}\)",
            r"\(x^{2}\) en \(-x^{2}\)",
            r"\(\sqrt{x}\) en \(\tfrac{1}{x}\)",
            r"\(x^{3}\) en \(\sqrt{x}\)",
        ],
        antwoord=0,
        uitleg=r"Kwadrateren en worteltrekken heffen elkaar daar op: \(\sqrt{x^{2}}=x\) voor \(x\geq 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Voor \(f(x)=x+3\) is \(f^{-1}(x)=x-\) welk getal? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"Wat de functie erbij doet, haalt de inverse er weer af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de inverse van \(f(x)=\dfrac{2x-1}{3}\)?",
        opties=[
            r"\(f^{-1}(x)=\dfrac{3x+1}{2}\)",
            r"\(f^{-1}(x)=\dfrac{3x-1}{2}\)",
            r"\(f^{-1}(x)=\dfrac{2x+1}{3}\)",
            r"\(f^{-1}(x)=\dfrac{3}{2x-1}\)",
        ],
        antwoord=0,
        uitleg=r"Verwissel \(x\) en \(y\) en los op naar \(y\): uit \(x=\tfrac{2y-1}{3}\) volgt \(3x+1=2y\). Let op: \(f^{-1}\) is niet \(\tfrac{1}{f}\), ook al lijkt de notatie erop.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke rechte is inverteerbaar.",
        antwoord=False,
        uitleg=r"Een horizontale rechte \(y=c\) geeft aan alle \(x\) dezelfde waarde. Gespiegeld wordt dat een verticale rechte, en dat is geen functie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe noemen we \(\arcsin\), \(\arccos\) en \(\arctan\) samen?",
        opties=[
            r"de cyclometrische functies",
            r"de goniometrische functies",
            r"de irrationale functies",
            r"de periodieke functies",
        ],
        antwoord=0,
        uitleg=r"Het zijn de inversen van de goniometrische basisfuncties, elk op een beperkt domein.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een grafiek snijdt de \(y\)-as in \((0,2)\). Wat wordt dat punt op de grafiek van \(f^{-1}\)?",
        opties=[r"\((2,0)\)", r"\((0,-2)\)", r"\((2,2)\)", r"\((-2,0)\)"],
        antwoord=0,
        uitleg=r"Bij spiegelen om \(y=x\) wisselen de twee coördinaten van plaats.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De inverse van een strikt stijgende functie is zelf ook strikt stijgend.",
        antwoord=True,
        uitleg=r"Spiegelen om \(y=x\) draait de volgorde van de punten niet om, dus de richting blijft behouden.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=2x\). Hoeveel is \(f^{-1}(10)\)? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"De functie verdubbelt, dus de inverse halveert: \(f^{-1}(x)=\tfrac{x}{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom beperkt men het domein van \(\sin\) voor men haar inverse neemt?",
        opties=[
            r"omdat ze anders dezelfde waarde oneindig vaak aanneemt",
            r"omdat ze anders nergens positief zou zijn",
            r"omdat haar grafiek anders geen nulwaarden heeft",
            r"omdat haar bereik anders te klein zou uitvallen",
        ],
        antwoord=0,
        uitleg=r"De sinus is periodiek. Zonder beperking zou \(\arcsin\) bij één getal oneindig veel hoeken moeten teruggeven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat kan je meteen zeggen over een grafiek die symmetrisch ligt om \(y=x\)?",
        opties=[
            r"de functie is haar eigen inverse",
            r"de functie is even",
            r"de functie heeft precies twee nulwaarden",
            r"de functie is overal strikt stijgend",
        ],
        antwoord=0,
        uitleg=r"Spiegelen verandert de grafiek dan niet, dus \(f^{-1}=f\). \(f(x)=\tfrac{1}{x}\) is zo'n functie.",
    ),
]
