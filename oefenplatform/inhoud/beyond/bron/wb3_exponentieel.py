# -*- coding: utf-8 -*-
"""Exponentiële functies en groeimodellen.

Wiskunde basis, derde graad. De fiche vraagt: de standaardfunctie a^x en de
algemene vorm b·a^x + c, de transformaties (verticale verschuiving, verticale
uitrekking, spiegeling rond de x-as), domein, bereik, stijgen en dalen,
horizontale asymptoot, gedrag op oneindig, de punten (0, 1) en (1, a). In
context: lineair en exponentieel groeimodel, beginwaarde, groeifactor en
groeipercentage per tijdseenheid, omzetten naar een andere tijdseenheid,
halverings- en verdubbelingstijd, met logaritmen. Contexten zoals intrest en
radioactief verval.

Deel 1: de functie en haar kenmerken. Deel 2: groeimodellen in context.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Door welk punt gaat de grafiek van elke functie \(f(x) = a^{x}\) (met \(a > 0\), \(a \neq 1\))?",
        opties=[r"\((0, 1)\)", r"\((1, 0)\)", r"\((0, 0)\)", r"\((1, 1)\)"],
        antwoord=0,
        uitleg=r"\(a^{0} = 1\) voor elk toegelaten grondtal. Een tweede vast punt is \((1, a)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is \(f(x) = a^{x}\) dalend?",
        opties=[r"als \(0 < a < 1\)", r"als \(a > 1\)", r"als \(a < 0\)", r"nooit"],
        antwoord=0,
        uitleg=r"Een grondtal tussen \(0\) en \(1\) geeft steeds kleinere waarden, zoals \(\left(\tfrac{1}{2}\right)^{x}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(f(x) = 3^{x}\)?",
        opties=[r"\(]0, +\infty[\)", r"\([0, +\infty[\)", r"\(\mathbb{R}\)", r"\(]1, +\infty[\)"],
        antwoord=0,
        uitleg=r"Een macht van \(3\) is altijd strikt positief, maar komt willekeurig dicht bij \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x) = 2^{x}\)?",
        opties=[r"\(y = 0\)", r"\(y = 1\)", r"\(x = 0\)", r"\(y = 2\)"],
        antwoord=0,
        uitleg=r"Als \(x \to -\infty\), dan \(2^{x} \to 0\). De \(x\)-as is de horizontale asymptoot.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x) = 5 \cdot 2^{x} - 3\)?",
        opties=[r"\(y = -3\)", r"\(y = 5\)", r"\(y = 0\)", r"\(y = 3\)"],
        antwoord=0,
        uitleg=r"In \(b \cdot a^{x} + c\) is de horizontale asymptoot \(y = c\). De verschuiving \(-3\) neemt de asymptoot mee naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(f(x) = 2^{x} + 4\)?",
        opties=[r"\(]4, +\infty[\)", r"\([4, +\infty[\)", r"\(]0, +\infty[\)", r"\(\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"\(2^{x} > 0\), dus \(2^{x} + 4 > 4\). De waarde \(4\) zelf wordt nooit bereikt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie zet \(f(x) = 3^{x}\) om in \(g(x) = -3^{x}\)?",
        opties=[r"een spiegeling rond de \(x\)-as", r"een spiegeling rond de \(y\)-as", r"een verschuiving naar beneden", r"een horizontale verschuiving"],
        antwoord=0,
        uitleg=r"Elke functiewaarde wordt haar tegengestelde. Dat is het geval \(b < 0\) in \(b \cdot a^{x} + c\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je rekt \(f(x) = 2^{x}\) verticaal uit met factor \(3\) en verschuift ze \(1\) eenheid naar beneden. Welk voorschrift krijg je?",
        opties=[r"\(3 \cdot 2^{x} - 1\)", r"\(3 \cdot (2^{x} - 1)\)", r"\(2^{3x} - 1\)", r"\(6^{x} - 1\)"],
        antwoord=0,
        uitleg=r"Eerst uitrekken: \(3 \cdot 2^{x}\). Daarna verschuiven: \(3 \cdot 2^{x} - 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het domein van \(f(x) = 4^{x}\) is \(\mathbb{R}\).",
        antwoord=True,
        uitleg=r"Je kan \(4\) verheffen tot elke reële exponent, ook negatieve en gebroken exponenten.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(f(x) = 2^{x}\) snijdt de \(x\)-as.",
        antwoord=False,
        uitleg=r"\(2^{x}\) is nooit \(0\). De grafiek nadert de \(x\)-as, maar raakt ze nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe verloopt \(f(x) = 2^{x}\)?",
        opties=[r"toenemende stijging", r"afnemende stijging", r"constante stijging", r"toenemende daling"],
        antwoord=0,
        uitleg=r"\(1, 2, 4, 8, 16\): de stappen worden telkens groter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe verloopt \(f(x) = \left(\tfrac{1}{2}\right)^{x}\)?",
        opties=[r"afnemende daling", r"toenemende daling", r"afnemende stijging", r"constante daling"],
        antwoord=0,
        uitleg=r"\(8, 4, 2, 1, \tfrac{1}{2}\): de functie daalt, en elke stap is kleiner dan de vorige.",
    ),
    dict(
        type="invultekst",
        vraag=r"De grafiek van \(f(x) = a^{x}\) gaat door \((1, 6)\). Hoeveel is \(a\)? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg=r"\(f(1) = a^{1} = a\), dus het punt \((1, a)\) geeft meteen het grondtal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel: \(f(0) = 5\), \(f(1) = 15\), \(f(2) = 45\), \(f(3) = 135\). Welk voorschrift past?",
        opties=[r"\(f(x) = 5 \cdot 3^{x}\)", r"\(f(x) = 3 \cdot 5^{x}\)", r"\(f(x) = 10x + 5\)", r"\(f(x) = 5x^{3}\)"],
        antwoord=0,
        uitleg=r"Telkens maal \(3\), dus groeifactor \(3\). De beginwaarde \(f(0)\) is \(5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(f(x) = 2 \cdot 5^{x}\) en \(g(x) = 10^{x}\) zijn dezelfde functie.",
        antwoord=False,
        uitleg=r"\(f(1) = 10\) en \(g(1) = 10\), maar \(f(0) = 2\) en \(g(0) = 1\). De factor \(2\) staat niet in de exponent.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met \(f(x) = 3 \cdot 2^{x}\) als \(x \to -\infty\)?",
        opties=[r"\(f(x) \to 0\)", r"\(f(x) \to 3\)", r"\(f(x) \to -\infty\)", r"\(f(x) \to +\infty\)"],
        antwoord=0,
        uitleg=r"\(2^{x}\) gaat naar \(0\), en \(3\) maal bijna \(0\) blijft bijna \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafieken van \(2^{x}\) en \(\left(\tfrac{1}{2}\right)^{x}\) snijden elkaar in \((0, 1)\).",
        antwoord=True,
        uitleg=r"Beide gaan door \((0, 1)\), zoals elke standaardfunctie \(a^{x}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waar snijdt \(f(x) = 4 \cdot 3^{x} + 2\) de \(y\)-as?",
        opties=[r"\((0, 6)\)", r"\((0, 4)\)", r"\((0, 2)\)", r"\((0, 14)\)"],
        antwoord=0,
        uitleg=r"\(f(0) = 4 \cdot 1 + 2 = 6\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De functie \(f(x) = -2 \cdot 3^{x}\) is dalend.",
        antwoord=True,
        uitleg=r"\(3^{x}\) stijgt, maar de spiegeling rond de \(x\)-as door het minteken maakt de functie dalend.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij welke waarde van \(c\) heeft \(f(x) = 2^{x} + c\) een nulwaarde?",
        opties=[r"\(c = -8\)", r"\(c = 0\)", r"\(c = 3\)", r"\(c = 8\)"],
        antwoord=0,
        uitleg=r"\(2^{x} + c = 0 \iff 2^{x} = -c\). Dat kan enkel als \(-c > 0\). Bij \(c = -8\) is \(x = 3\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een bedrag groeit met \(4\%\) per jaar. Wat is de groeifactor per jaar?",
        opties=[r"\(1{,}04\)", r"\(0{,}04\)", r"\(1{,}4\)", r"\(0{,}96\)"],
        antwoord=0,
        uitleg=r"Bij een toename van \(p\%\) is de groeifactor \(1 + \dfrac{p}{100} = 1{,}04\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een auto verliest elk jaar \(15\%\) van zijn waarde. Wat is de groeifactor per jaar?",
        opties=[r"\(0{,}85\)", r"\(1{,}15\)", r"\(0{,}15\)", r"\(-0{,}15\)"],
        antwoord=0,
        uitleg=r"Bij een afname van \(p\%\) is de groeifactor \(1 - \dfrac{p}{100} = 0{,}85\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een groeifactor per jaar is \(1{,}07\). Met hoeveel procent per jaar groeit de grootheid? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"\(1{,}07 = 1 + \dfrac{7}{100}\): een groeipercentage van \(7\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je zet \(2000\) euro op een rekening met \(3\%\) samengestelde intrest per jaar. Welk voorschrift geeft het bedrag na \(t\) jaar?",
        opties=[r"\(B(t) = 2000 \cdot 1{,}03^{t}\)", r"\(B(t) = 2000 + 1{,}03t\)", r"\(B(t) = 2000 \cdot 0{,}03^{t}\)", r"\(B(t) = 2000 + 60t\)"],
        antwoord=0,
        uitleg=r"Samengestelde intrest is exponentiële groei met beginwaarde \(2000\) en groeifactor \(1{,}03\). \(2000 + 60t\) hoort bij enkelvoudige intrest.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij enkelvoudige intrest groeit het kapitaal lineair.",
        antwoord=True,
        uitleg=r"Bij enkelvoudige intrest komt er elk jaar hetzelfde bedrag bij: een constante stijging.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel: jaar \(0\): \(500\), jaar \(1\): \(550\), jaar \(2\): \(605\), jaar \(3\): \(665{,}5\). Welke groei is dit?",
        opties=[r"exponentiële groei met groeifactor \(1{,}1\)", r"lineaire groei met \(50\) per jaar", r"exponentiële groei met groeifactor \(1{,}5\)", r"niet-lineaire en niet-exponentiële groei"],
        antwoord=0,
        uitleg=r"De verschillen \(50, 55, 60{,}5\) zijn niet gelijk, maar de quotiënten wel: \(550 : 500 = 605 : 550 = 1{,}1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel: \(0 \to 3\), \(1 \to 7\), \(2 \to 11\), \(3 \to 15\). Welke groei is dit?",
        opties=[r"lineaire groei", r"exponentiële groei", r"niet-lineaire en niet-exponentiële groei", r"exponentiële afname"],
        antwoord=0,
        uitleg=r"Er komt telkens \(4\) bij: een constant verschil hoort bij lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel: \(0 \to 1\), \(1 \to 2\), \(2 \to 5\), \(3 \to 10\). Welke groei is dit?",
        opties=[r"niet-lineaire en niet-exponentiële groei", r"lineaire groei", r"exponentiële groei met groeifactor \(2\)", r"exponentiële groei met groeifactor \(2{,}5\)"],
        antwoord=0,
        uitleg=r"De verschillen \(1, 3, 5\) zijn niet gelijk en de quotiënten \(2, 2{,}5, 2\) ook niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bevolking groeit met \(21\%\) per twee jaar. Wat is de groeifactor per jaar?",
        opties=[r"\(1{,}1\)", r"\(1{,}105\)", r"\(1{,}21\)", r"\(1{,}42\)"],
        antwoord=0,
        uitleg=r"Per jaar \(a\), per twee jaar \(a^{2} = 1{,}21\). Dus \(a = \sqrt{1{,}21} = 1{,}1\): \(10\%\) per jaar, niet de helft van \(21\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een groeifactor per maand is \(1{,}02\). Wat is de groeifactor per jaar, afgerond op drie cijfers na de komma?",
        opties=[r"\(1{,}268\)", r"\(1{,}240\)", r"\(1{,}020\)", r"\(12{,}240\)"],
        antwoord=0,
        uitleg=r"Twaalf maanden na elkaar: \(1{,}02^{12} \approx 1{,}268\). \(1{,}24\) krijg je als je de procenten gewoon optelt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een groei van \(10\%\) per jaar is na twee jaar een groei van \(20\%\).",
        antwoord=False,
        uitleg=r"\(1{,}1^{2} = 1{,}21\): dat is \(21\%\). Het tweede jaar groeit ook de groei van het eerste jaar mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de halveringstijd van een radioactieve stof?",
        opties=[
            r"de tijd waarna nog de helft van de stof over is",
            r"de helft van de tijd waarna alle stof verdwenen is",
            r"de tijd waarna de stof twee keer zo snel vervalt",
            r"de tijd waarin de stof met \(50\) gram afneemt",
        ],
        antwoord=0,
        uitleg=r"Bij exponentiële afname duurt het altijd even lang om te halveren, waar je ook begint.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een stof heeft een halveringstijd van \(8\) dagen. Je hebt \(80\) mg. Hoeveel milligram is er na \(24\) dagen over? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg=r"\(24\) dagen zijn drie halveringstijden: \(80 \to 40 \to 20 \to 10\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een hoeveelheid groeit met \(5\%\) per jaar. Na hoeveel jaar is ze verdubbeld? Kies de juiste berekening.",
        opties=[r"\(t = \log_{1{,}05} 2\)", r"\(t = 2 : 1{,}05\)", r"\(t = \log_{2} 1{,}05\)", r"\(t = 100 : 5\)"],
        antwoord=0,
        uitleg=r"\(1{,}05^{t} = 2 \iff t = \log_{1{,}05} 2 = \dfrac{\log 2}{\log 1{,}05}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een hoeveelheid groeit met \(5\%\) per jaar. Wat is de verdubbelingstijd, afgerond op één cijfer na de komma?",
        opties=[r"\(14{,}2\) jaar", r"\(20{,}0\) jaar", r"\(10{,}0\) jaar", r"\(1{,}9\) jaar"],
        antwoord=0,
        uitleg=r"\(\dfrac{\log 2}{\log 1{,}05} \approx \dfrac{0{,}3010}{0{,}0212} \approx 14{,}2\). Met \(100 : 5\) vergeet je dat de groei zelf ook groeit.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De verdubbelingstijd van een exponentieel groeiende hoeveelheid hangt af van de beginwaarde.",
        antwoord=False,
        uitleg=r"Uit \(b \cdot a^{t} = 2b\) valt \(b\) weg: \(a^{t} = 2\). Elke beginwaarde verdubbelt even snel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een kapitaal \(K(t) = 1500 \cdot 1{,}02^{t}\). Hoeveel euro is de beginwaarde? Schrijf het getal.",
        antwoord=["1500", "1 500", "1.500"],
        uitleg=r"De beginwaarde is \(K(0) = 1500 \cdot 1 = 1500\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een stad heeft \(80\,000\) inwoners en krimpt met \(2\%\) per jaar. Hoeveel inwoners zijn er na \(5\) jaar, afgerond?",
        opties=[r"\(72\,314\)", r"\(72\,000\)", r"\(88\,326\)", r"\(79\,000\)"],
        antwoord=0,
        uitleg=r"\(80\,000 \cdot 0{,}98^{5} \approx 72\,314\). Vijf keer \(2\%\) van \(80\,000\) aftrekken geeft \(72\,000\), maar dat is lineair.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In \(N(t) = 300 \cdot 0{,}9^{t}\) neemt \(N\) elke tijdseenheid met \(10\%\) af.",
        antwoord=True,
        uitleg=r"Groeifactor \(0{,}9 = 1 - \dfrac{10}{100}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een lineair groeimodel \(f(x) = ax + b\) heeft een groeifactor die per tijdseenheid gelijk blijft.",
        antwoord=False,
        uitleg=r"Bij lineaire groei blijft het verschil gelijk (de richtingscoëfficiënt \(a\)). Een vaste groeifactor hoort bij exponentiële groei.",
    ),
]
