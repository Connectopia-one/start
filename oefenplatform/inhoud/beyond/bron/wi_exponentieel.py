# -*- coding: utf-8 -*-
r"""Exponentiële en logaritmische functies, en groeimodellen.

Het onderdeel "Exponentiële functies" van de analysefiche G1. Dat valt daar in
twee stukken uiteen: de kenmerken van de functie zelf, in opgaven zonder
context, en de groeimodellen, uitdrukkelijk in opgaven mét context.

Deel 1 is de functie en haar grafiek, deel 2 zijn de groeimodellen.

In echte wiskundige notatie, tussen \( en \); zie oefenplatform/lib/wiskunde.ts.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\text{dom}\,f\) voor \(f(x)=a^{x}\) met \(a>0\)?",
        opties=[
            r"\(\mathbb{R}\)",
            r"\(\left]0,+\infty\right[\)",
            r"\(\left]a,+\infty\right[\)",
            r"\(\mathbb{Z}\)",
        ],
        antwoord=0,
        uitleg=r"Je mag elke exponent nemen, ook negatieve en gebroken. Het bereik is wel beperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\text{ber}\,f\) voor \(f(x)=a^{x}\) met \(a>0\)?",
        opties=[
            r"\(\left]0,+\infty\right[\)",
            r"\(\mathbb{R}\)",
            r"\(\left[0,+\infty\right[\)",
            r"\(\left]0,a\right[\)",
        ],
        antwoord=0,
        uitleg=r"Een macht van een positief grondtal wordt nooit \(0\) of negatief, hoe klein de exponent ook is.",
    ),
    dict(
        type="invultekst",
        vraag=r"Elke grafiek van \(f(x)=a^{x}\) gaat door hetzelfde punt op de \(y\)-as. Welke \(y\)-waarde? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg=r"\(a^{0}=1\) bij elk grondtal, dus alle grafieken gaan door \((0,1)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x)=a^{x}\) daalt als \(0<a<1\).",
        antwoord=True,
        uitleg=r"\(\left(\tfrac{1}{2}\right)^{3}=\tfrac{1}{8}\): hoe groter de exponent, hoe kleiner de uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x)=2^{x}\)?",
        opties=[r"\(y=0\)", r"\(y=1\)", r"\(y=2\)", r"\(x=0\)"],
        antwoord=0,
        uitleg=r"Voor \(x\to-\infty\) kruipen de waarden naar \(0\), zonder die ooit te bereiken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x)=2^{x}+5\)?",
        opties=[r"\(y=5\)", r"\(y=0\)", r"\(y=7\)", r"\(x=5\)"],
        antwoord=0,
        uitleg=r"De hele grafiek, en dus ook haar asymptoot, schuift \(5\) omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van een exponentiële functie snijdt haar horizontale asymptoot.",
        antwoord=False,
        uitleg=r"Ze nadert die rechte wel oneindig dicht, maar bereikt haar nooit.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x)=3^{x}\). Hoeveel is \(f(2)\)? Schrijf het getal.",
        antwoord=["9", "negen"],
        uitleg=r"\(3^{2}=9\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie brengt je van \(2^{x}\) naar \(2^{x}-4\)?",
        opties=[
            r"\(4\) omlaag",
            r"\(4\) naar rechts",
            r"\(4\) naar links",
            r"een verticale uitrekking met \(4\)",
        ],
        antwoord=0,
        uitleg=r"De \(-4\) staat buiten de macht, dus hij werkt op de functiewaarde. De asymptoot zakt mee naar \(y=-4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x)=a^{x}\) met \(a>0\) kan negatieve waarden aannemen.",
        antwoord=False,
        uitleg=r"Niet zonder transformatie. Pas als je de grafiek spiegelt of ver genoeg laat zakken, komen er negatieve waarden bij.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Door welk tweede bijzonder punt gaat de grafiek van \(f(x)=a^{x}\) altijd?",
        opties=[r"\((1,a)\)", r"\((a,1)\)", r"\((1,1)\)", r"\((0,a)\)"],
        antwoord=0,
        uitleg=r"\(a^{1}=a\). Daarmee lees je het grondtal rechtstreeks van de grafiek af.",
    ),
    dict(
        type="invultekst",
        vraag=r"De grafiek van \(f(x)=a^{x}\) gaat door \((1,5)\). Wat is \(a\)? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"In \(x=1\) is de functiewaarde net het grondtal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom laat men \(a=1\) niet toe als grondtal?",
        opties=[
            r"omdat de grafiek dan de horizontale rechte \(y=1\) wordt",
            r"omdat de functie dan nergens gedefinieerd is",
            r"omdat de functie dan negatieve waarden aanneemt",
            r"omdat de functie dan twee asymptoten krijgt",
        ],
        antwoord=0,
        uitleg=r"\(1^{x}=1\) voor elke \(x\). Dat is een constante functie, en die groeit niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x)=e^{x}\) is stijgend.",
        antwoord=True,
        uitleg=r"\(e\approx 2{,}718>1\), en bij een grondtal groter dan \(1\) stijgt de functie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een tabel staat bij elke stap van \(1\) in \(x\) dezelfde vermenigvuldigingsfactor. Welk model past?",
        opties=[
            r"een exponentieel model",
            r"een lineair model",
            r"een tweedegraadsmodel",
            r"een periodiek model",
        ],
        antwoord=0,
        uitleg=r"Een vaste factor wijst op exponentiële groei. Een vaste optelling per stap wijst op lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je spiegelt de grafiek van \(2^{x}\) om de \(x\)-as. Wat wordt het bereik?",
        opties=[
            r"\(\left]-\infty,0\right[\)",
            r"\(\left]0,+\infty\right[\)",
            r"\(\mathbb{R}\)",
            r"\(\left]-1,0\right[\)",
        ],
        antwoord=0,
        uitleg=r"Alle functiewaarden wisselen van teken, dus wat positief was wordt negatief.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x)=\log_{a}x\) heeft een verticale asymptoot.",
        antwoord=True,
        uitleg=r"Voor \(x\to 0^{+}\) duikt de logaritme naar \(-\infty\). De \(y\)-as is dus een verticale asymptoot.",
    ),
    dict(
        type="invultekst",
        vraag=r"Het domein van \(f(x)=\log_{a}x\) bestaat uit alle getallen strikt groter dan welk getal? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"Alleen strikt positieve argumenten hebben een logaritme, dus \(\text{dom}\,f=\left]0,+\infty\right[\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Door welk punt gaat de grafiek van \(f(x)=\log_{a}x\) altijd?",
        opties=[r"\((1,0)\)", r"\((0,1)\)", r"\((0,0)\)", r"\((1,1)\)"],
        antwoord=0,
        uitleg=r"\(\log_{a}1=0\) bij elk grondtal. Dat is het spiegelbeeld van \((0,1)\) bij de exponentiële functie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe liggen de grafieken van \(a^{x}\) en \(\log_{a}x\) ten opzichte van elkaar?",
        opties=[
            r"ze spiegelen om de rechte \(y=x\)",
            r"ze spiegelen om de \(x\)-as",
            r"ze lopen evenwijdig op een vaste afstand",
            r"ze snijden elkaar in precies twee punten",
        ],
        antwoord=0,
        uitleg=r"Het zijn elkaars inverse functies, en inverse functies spiegelen altijd om de eerste bissectrice.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een bedrag groeit met \(3\%\) per jaar. Wat is de groeifactor per jaar?",
        opties=[r"\(1{,}03\)", r"\(0{,}03\)", r"\(3\)", r"\(1{,}3\)"],
        antwoord=0,
        uitleg=r"Bij een toename van \(p\%\) is de groeifactor \(1+\tfrac{p}{100}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een hoeveelheid daalt met \(20\%\) per jaar. Wat is de groeifactor?",
        opties=[r"\(0{,}8\)", r"\(1{,}2\)", r"\(0{,}2\)", r"\(-0{,}8\)"],
        antwoord=0,
        uitleg=r"Er blijft \(80\%\) over, dus je vermenigvuldigt met \(0{,}8\). Een groeifactor is nooit negatief.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een model luidt \(N(x)=200\cdot 1{,}05^{x}\). Wat is de beginwaarde? Schrijf het getal.",
        antwoord=["200", "tweehonderd"],
        uitleg=r"\(N(0)=200\cdot 1=200\): voor \(x=0\) is de macht \(1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een groeifactor kleiner dan \(1\) betekent dat de hoeveelheid afneemt.",
        antwoord=True,
        uitleg=r"Vermenigvuldigen met een getal tussen \(0\) en \(1\) maakt kleiner. Bij precies \(1\) blijft alles gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een groeifactor is \(1{,}12\) per jaar. Met hoeveel procent groeit de hoeveelheid per jaar?",
        opties=[
            r"\(12\%\) erbij",
            r"\(112\%\) erbij",
            r"\(12\%\) eraf",
            r"\(1{,}12\%\) erbij",
        ],
        antwoord=0,
        uitleg=r"Trek \(1\) af en vermenigvuldig met \(100\): \(0{,}12\) is \(12\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je kent de groeifactor \(g\) per maand. Wat is de groeifactor per jaar?",
        opties=[r"\(g^{12}\)", r"\(12g\)", r"\(12+g\)", r"\(\tfrac{g}{12}\)"],
        antwoord=0,
        uitleg=r"Twaalf keer vermenigvuldigen met dezelfde factor is die factor tot de twaalfde macht. Maal twaalf hoort bij lineaire groei.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een stijging met \(10\%\), gevolgd door een daling met \(10\%\), brengt je terug bij de beginwaarde.",
        antwoord=False,
        uitleg=r"\(1{,}1\cdot 0{,}9=0{,}99\), dus je verliest \(1\%\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een aantal gaat in één stap van \(100\) naar \(150\). Wat is de groeifactor? Schrijf het getal.",
        antwoord=["1,5", "1.5"],
        uitleg=r"\(\tfrac{150}{100}=1{,}5\), dus een toename van \(50\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de verdubbelingstijd van een exponentieel groeiproces?",
        opties=[
            r"de tijd die nodig is om twee keer zo groot te worden",
            r"de tijd waarna de groeifactor zelf verdubbeld is",
            r"het dubbel van de tijd van één stap",
            r"de tijd waarna het groeipercentage verdubbeld is",
        ],
        antwoord=0,
        uitleg=r"Bij exponentiële groei is die tijd altijd even lang, waar je ook begint te meten.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een halveringstijd hoort bij een groeifactor kleiner dan \(1\).",
        antwoord=True,
        uitleg=r"Halveren is afnemen, en afnemen betekent een factor tussen \(0\) en \(1\). Radioactief verval is het bekendste voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vorm heeft een lineair groeimodel?",
        opties=[
            r"\(f(x)=ax+b\)",
            r"\(f(x)=b\cdot a^{x}\)",
            r"\(f(x)=ax^{2}\)",
            r"\(f(x)=\log x+b\)",
        ],
        antwoord=0,
        uitleg=r"Bij lineaire groei komt er elke tijdseenheid hetzelfde getal bij. Bij exponentiële groei vermenigvuldig je telkens.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je zet geld op een rekening met \(5\%\) samengestelde intrest per jaar. Wat is de groeifactor? Schrijf het getal.",
        antwoord=["1,05", "1.05"],
        uitleg=r"Samengestelde intrest betekent elk jaar met dezelfde factor vermenigvuldigen, dus met \(1{,}05\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je na hoeveel jaar een bedrag met groeifactor \(1{,}05\) verdubbeld is?",
        opties=[
            r"\(t=\dfrac{\ln 2}{\ln 1{,}05}\)",
            r"\(t=\dfrac{2}{1{,}05}\)",
            r"\(t=\dfrac{100}{5}\)",
            r"\(t=\sqrt{2}\)",
        ],
        antwoord=0,
        uitleg=r"Je lost \(1{,}05^{t}=2\) op, en dat gaat alleen met een logaritme: \(t\approx 14{,}2\) jaar. \(\tfrac{100}{5}=20\) is enkel een ruwe vuistregel, en een slechte.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij exponentiële groei komt er elke tijdseenheid evenveel bij.",
        antwoord=False,
        uitleg=r"Er komt elk jaar hetzelfde percentage bij, dus in absolute aantallen steeds meer. Een vaste toename hoort bij lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rij getallen past bij exponentiële groei?",
        opties=[
            r"\(3,\ 6,\ 12,\ 24\)",
            r"\(3,\ 6,\ 9,\ 12\)",
            r"\(3,\ 5,\ 8,\ 12\)",
            r"\(3,\ 9,\ 15,\ 21\)",
        ],
        antwoord=0,
        uitleg=r"Telkens maal \(2\). De tweede en de vierde rij hebben een vaste toename en zijn dus lineair.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een stof heeft een halveringstijd van \(5\) jaar. Hoeveel blijft er over na \(10\) jaar?",
        opties=[r"\(\tfrac{1}{4}\)", r"\(\tfrac{1}{2}\)", r"\(\tfrac{1}{5}\)", r"niets meer"],
        antwoord=0,
        uitleg=r"Twee halveringstijden na elkaar: \(\left(\tfrac{1}{2}\right)^{2}=\tfrac{1}{4}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een zuiver exponentieel model voorspelt een groei die nooit stopt.",
        antwoord=True,
        uitleg=r"Wiskundig blijft de functie stijgen. In werkelijkheid loopt groei vast op voedsel, ruimte of geld, dus het model geldt maar op een beperkt stuk.",
    ),
    dict(
        type="invultekst",
        vraag=r"De groeifactor per jaar is \(2\). Wat is de groeifactor per twee jaar? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(2^{2}=4\): twee keer verdubbelen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een populatie van \(500\) groeit met \(8\%\) per jaar. Hoe groot is ze na \(10\) jaar?",
        opties=[
            r"\(500\cdot 1{,}08^{10}\approx 1079\)",
            r"\(500\cdot 10\cdot 0{,}08=400\)",
            r"\(500+80\cdot 10=1300\)",
            r"\(500\cdot 1{,}8=900\)",
        ],
        antwoord=0,
        uitleg=r"Elk jaar maal \(1{,}08\), tien keer na elkaar. De tweede en derde optie rekenen lineair, en dat onderschat de groei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom heeft een groeimodel vaak een praktisch domein?",
        opties=[
            r"omdat een negatieve tijd meestal geen betekenis heeft",
            r"omdat de functie buiten dat domein niet bestaat",
            r"omdat de groeifactor na een tijd negatief wordt",
            r"omdat de grafiek anders geen asymptoot zou hebben",
        ],
        antwoord=0,
        uitleg=r"De exponentiële functie bestaat wiskundig voor elke \(x\), maar in de context tel je pas vanaf het begin van de meting.",
    ),
]
