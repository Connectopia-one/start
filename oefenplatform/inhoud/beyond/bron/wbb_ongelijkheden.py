# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: ongelijkheden.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED). De fiche
vraagt: ongelijkheden grafisch oplossen (ligging van de grafiek van f ten
opzichte van de x-as, en van f ten opzichte van g), voor veeltermfuncties,
exponentiële en sinusfuncties; tweedegraadsongelijkheden algebraïsch oplossen
met een tekenverloop; de oplossingenverzameling noteren als interval; en
vraagstukken.

Deel 1: grafisch en de notatie. Deel 2: tweedegraadsongelijkheden met een
tekenverloop en vraagstukken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe lees je de oplossingen van \(f(x) > 0\) af op de grafiek van \(f\)?",
        opties=[
            r"de \(x\)-waarden waar de grafiek boven de \(x\)-as ligt",
            r"de \(x\)-waarden waar de grafiek onder de \(x\)-as ligt",
            r"de \(x\)-waarden waar de grafiek stijgt",
            r"de \(y\)-waarden die groter zijn dan \(0\)",
        ],
        antwoord=0,
        uitleg=r"\(f(x) > 0\) betekent een positieve functiewaarde: boven de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe lees je de oplossingen van \(f(x) \le g(x)\) af?",
        opties=[
            r"de \(x\)-waarden waar de grafiek van \(f\) onder of op die van \(g\) ligt",
            r"de \(x\)-waarden waar de grafiek van \(f\) boven die van \(g\) ligt",
            r"de \(x\)-waarden waar beide grafieken stijgen",
            r"de \(x\)-waarden waar \(f\) en \(g\) allebei negatief zijn",
        ],
        antwoord=0,
        uitleg=r"Kleiner of gelijk: onder de andere grafiek, met de snijpunten erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f\) snijdt de \(x\)-as in \(-3\) en \(1\) en ligt ertussen boven de \(x\)-as. Wat is \(V\) van \(f(x) \ge 0\)?",
        opties=[r"\([-3, 1]\)", r"\(]-3, 1[\)", r"\(]-\infty, -3] \cup [1, +\infty[\)", r"\(\{-3, 1\}\)"],
        antwoord=0,
        uitleg=r"Groter of gelijk aan nul: het stuk boven de \(x\)-as, met de nulwaarden erbij. Dus gesloten haken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij dezelfde \(f\) (nulwaarden \(-3\) en \(1\), positief ertussen): wat is \(V\) van \(f(x) < 0\)?",
        opties=[r"\(]-\infty, -3[ \cup ]1, +\infty[\)", r"\(]-3, 1[\)", r"\([-3, 1]\)", r"\(]-\infty, -3] \cup [1, +\infty[\)"],
        antwoord=0,
        uitleg=r"Strikt kleiner dan nul: buiten de nulwaarden, zonder de nulwaarden zelf.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een strikte ongelijkheid zoals \(f(x) > 0\) horen de nulwaarden van \(f\) niet bij de oplossingen.",
        antwoord=True,
        uitleg=r"In een nulwaarde is \(f(x) = 0\), en \(0 > 0\) is niet waar. Daarom open haken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe noteer je alle reële getallen groter dan of gelijk aan \(4\)?",
        opties=[r"\([4, +\infty[\)", r"\(]4, +\infty[\)", r"\([4, +\infty]\)", r"\(]-\infty, 4]\)"],
        antwoord=0,
        uitleg=r"\(4\) hoort erbij: gesloten haak. Bij oneindig staat altijd een open haak.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafieken van \(f\) en \(g\) snijden elkaar enkel in \(x = 2\). Voor \(x < 2\) ligt \(f\) onder \(g\), voor \(x > 2\) erboven. Wat is \(V\) van \(f(x) > g(x)\)?",
        opties=[r"\(]2, +\infty[\)", r"\(]-\infty, 2[\)", r"\([2, +\infty[\)", r"\(\{2\}\)"],
        antwoord=0,
        uitleg=r"Waar \(f\) strikt boven \(g\) ligt, dus rechts van het snijpunt, zonder \(2\) zelf.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De ongelijkheid \(2^{x} > 0\) geldt voor alle reële \(x\).",
        antwoord=True,
        uitleg=r"De grafiek van \(2^{x}\) ligt overal boven de \(x\)-as: \(V = \mathbb{R}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De ongelijkheid \(\sin x > 1\) heeft oplossingen.",
        antwoord=False,
        uitleg=r"De sinus is hoogstens \(1\). \(V = \varnothing\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(V\) van \(\sin x \ge 0\) op \([0, 2\pi]\)?",
        opties=[r"\([0, \pi] \cup \{2\pi\}\)", r"\([\pi, 2\pi]\)", r"\(]0, \pi[\)", r"\(\left[0, \dfrac{\pi}{2}\right]\)"],
        antwoord=0,
        uitleg=r"De sinus is niet negatief van \(0\) tot \(\pi\), en in \(2\pi\) is ze opnieuw \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rekenapp toont dat \(3 \cdot 1{,}2^{x}\) en \(10\) elkaar snijden bij \(x \approx 6{,}60\). Wat is \(V\) van \(3 \cdot 1{,}2^{x} < 10\)?",
        opties=[r"\(]-\infty;\ 6{,}60[\)", r"\(]6{,}60;\ +\infty[\)", r"\([0;\ 6{,}60]\)", r"\(\{6{,}60\}\)"],
        antwoord=0,
        uitleg=r"\(3 \cdot 1{,}2^{x}\) stijgt, dus ze ligt onder \(10\) links van het snijpunt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als je beide leden van een ongelijkheid vermenigvuldigt met een negatief getal, keert het ongelijkheidsteken om.",
        antwoord=True,
        uitleg=r"\(2 < 5\), maar \(-2 > -5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(-3x + 6 > 0\).",
        opties=[r"\(V = ]-\infty, 2[\)", r"\(V = ]2, +\infty[\)", r"\(V = ]-\infty, -2[\)", r"\(V = [2, +\infty[\)"],
        antwoord=0,
        uitleg=r"\(-3x > -6 \iff x < 2\): delen door \(-3\) keert het teken om.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(V = ]1, 5]\) betekent: \(1 < x \le 5\).",
        antwoord=True,
        uitleg=r"De open haak bij \(1\) sluit \(1\) uit, de gesloten haak bij \(5\) neemt \(5\) mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke ongelijkheid hoort bij de vraag: wanneer ligt de grafiek van \(f\) boven de rechte \(y = 3\)?",
        opties=[r"\(f(x) > 3\)", r"\(f(x) < 3\)", r"\(f(3) > 0\)", r"\(f(x) > 0\)"],
        antwoord=0,
        uitleg=r"Boven de rechte \(y = 3\) betekent een functiewaarde groter dan \(3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(V = [2, 7[\) bevat het getal \(7\).",
        antwoord=False,
        uitleg=r"De open haak bij \(7\) sluit het uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een dalende rechte \(f\) en een stijgende rechte \(g\) snijden elkaar in \(x = 4\). Wat is \(V\) van \(f(x) \ge g(x)\)?",
        opties=[r"\(]-\infty, 4]\)", r"\([4, +\infty[\)", r"\(]-\infty, 4[\)", r"\(\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"Links van het snijpunt ligt de dalende rechte nog hoger. Het snijpunt telt mee door het gelijkheidsteken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De ongelijkheid \(x^{2} < 0\) heeft geen reële oplossingen.",
        antwoord=True,
        uitleg=r"Een kwadraat is nooit negatief. \(V = \varnothing\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De ongelijkheid \(x^{2} \le 0\) heeft geen reële oplossingen.",
        antwoord=False,
        uitleg=r"Voor \(x = 0\) is \(x^{2} = 0 \le 0\). \(V = \{0\}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een veeltermfunctie heeft nulwaarden \(-2\), \(0\) en \(3\). Het tekenverloop is \(-\), \(+\), \(-\), \(+\). Wat is \(V\) van \(f(x) > 0\)?",
        opties=[r"\(]-2, 0[ \cup ]3, +\infty[\)", r"\(]-\infty, -2[ \cup ]0, 3[\)", r"\(]-2, 3[\)", r"\(]0, 3[\)"],
        antwoord=0,
        uitleg=r"Je neemt de intervallen met een \(+\): tussen \(-2\) en \(0\), en na \(3\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe los je \(x^{2} - 5x + 4 < 0\) algebraïsch op?",
        opties=[
            r"nulwaarden zoeken, een tekenverloop maken en de intervallen met \(-\) nemen",
            r"\(x^{2} < 5x - 4\) schrijven en de vierkantswortel nemen",
            r"enkel de nulwaarden noteren",
            r"\(x\) buiten haakjes zetten en door \(x\) delen",
        ],
        antwoord=0,
        uitleg=r"Een tekenverloop laat zien waar de tweedegraadsfunctie positief en negatief is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 5x + 4 < 0\).",
        opties=[r"\(V = ]1, 4[\)", r"\(V = ]-\infty, 1[ \cup ]4, +\infty[\)", r"\(V = [1, 4]\)", r"\(V = \{1, 4\}\)"],
        antwoord=0,
        uitleg=r"Nulwaarden \(1\) en \(4\). Een dalparabool is negatief tussen de nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 9 \ge 0\).",
        opties=[r"\(V = ]-\infty, -3] \cup [3, +\infty[\)", r"\(V = [-3, 3]\)", r"\(V = [3, +\infty[\)", r"\(V = ]-3, 3[\)"],
        antwoord=0,
        uitleg=r"Nulwaarden \(-3\) en \(3\). Een dalparabool is positief buiten de nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(-x^{2} + 2x + 3 > 0\).",
        opties=[r"\(V = ]-1, 3[\)", r"\(V = ]-\infty, -1[ \cup ]3, +\infty[\)", r"\(V = ]-3, 1[\)", r"\(V = [-1, 3]\)"],
        antwoord=0,
        uitleg=r"\(-x^{2} + 2x + 3 = -(x - 3)(x + 1)\). Een bergparabool is positief tussen de nulwaarden \(-1\) en \(3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een bergparabool is positief tussen haar nulwaarden.",
        antwoord=True,
        uitleg=r"Ze opent naar beneden: tussen de nulwaarden ligt het stuk boven de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} + 4 > 0\).",
        opties=[r"\(V = \mathbb{R}\)", r"\(V = \varnothing\)", r"\(V = ]-2, 2[\)", r"\(V = ]2, +\infty[\)"],
        antwoord=0,
        uitleg=r"\(D < 0\) en \(a > 0\): de parabool ligt helemaal boven de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(x^{2} - 6x + 9 > 0\).",
        opties=[r"\(V = \mathbb{R} \setminus \{3\}\)", r"\(V = \mathbb{R}\)", r"\(V = \varnothing\)", r"\(V = ]3, +\infty[\)"],
        antwoord=0,
        uitleg=r"\((x - 3)^{2} > 0\) voor alle \(x\) behalve \(3\), waar het precies \(0\) is.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(x^{2} - 6x + 9 \le 0\) is \(V = \{3\}\).",
        antwoord=True,
        uitleg=r"Een kwadraat is enkel kleiner of gelijk aan \(0\) als het \(0\) is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2x^{2} \le 8x\).",
        opties=[r"\(V = [0, 4]\)", r"\(V = ]-\infty, 4]\)", r"\(V = [4, +\infty[\)", r"\(V = ]-\infty, 0] \cup [4, +\infty[\)"],
        antwoord=0,
        uitleg=r"\(2x^{2} - 8x \le 0 \iff 2x(x - 4) \le 0\): tussen de nulwaarden \(0\) en \(4\), grenzen inbegrepen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(2x^{2} \le 8x\) mag je beide leden door \(2x\) delen en \(x \le 4\) besluiten.",
        antwoord=False,
        uitleg=r"\(2x\) kan negatief of nul zijn: dan klopt de richting van het teken niet meer. Zo verlies je de grens \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De winst van een bedrijf is \(W(q) = -q^{2} + 60q - 500\) euro. Voor welke aantallen \(q\) maakt het winst?",
        opties=[r"\(10 < q < 50\)", r"\(q < 10\) of \(q > 50\)", r"\(q > 30\)", r"\(20 < q < 40\)"],
        antwoord=0,
        uitleg=r"\(-q^{2} + 60q - 500 > 0 \iff q^{2} - 60q + 500 < 0 \iff (q - 10)(q - 50) < 0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(W(q) = -q^{2} + 60q - 500\): hoeveel stuks geven de grootste winst? Schrijf het getal.",
        antwoord=["30", "dertig"],
        uitleg=r"De top ligt midden tussen de nulwaarden \(10\) en \(50\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal: \(h(t) = -5t^{2} + 20t\) m. Wanneer is hij hoger dan \(15\) m?",
        opties=[r"\(1 < t < 3\)", r"\(t < 1\) of \(t > 3\)", r"\(0 < t < 4\)", r"\(t > 3\)"],
        antwoord=0,
        uitleg=r"\(-5t^{2} + 20t > 15 \iff t^{2} - 4t + 3 < 0 \iff (t - 1)(t - 3) < 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een tekenverloop van \(ax^{2} + bx + c\) met twee nulwaarden en \(a > 0\) staat er tussen de nulwaarden een \(+\).",
        antwoord=False,
        uitleg=r"Een dalparabool ligt tussen haar nulwaarden onder de \(x\)-as: daar staat een \(-\). Buiten de nulwaarden staat een \(+\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke \(x\) ligt de parabool \(f(x) = x^{2}\) onder de rechte \(g(x) = x + 2\)?",
        opties=[r"\(]-1, 2[\)", r"\(]-\infty, -1[ \cup ]2, +\infty[\)", r"\(]-2, 1[\)", r"\([-1, 2]\)"],
        antwoord=0,
        uitleg=r"\(x^{2} < x + 2 \iff x^{2} - x - 2 < 0 \iff (x - 2)(x + 1) < 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechthoek heeft breedte \(x\) en lengte \(12 - x\) (in cm). Voor welke breedtes is de oppervlakte minstens \(32\ \text{cm}^{2}\)?",
        opties=[r"\(4 \le x \le 8\)", r"\(x \le 4\) of \(x \ge 8\)", r"\(0 < x < 12\)", r"\(x \ge 8\)"],
        antwoord=0,
        uitleg=r"\(x(12 - x) \ge 32 \iff x^{2} - 12x + 32 \le 0 \iff (x - 4)(x - 8) \le 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een tweedegraadsongelijkheid heeft altijd een begrensd interval als oplossing.",
        antwoord=False,
        uitleg=r"Ze kan ook twee onbegrensde stukken, heel \(\mathbb{R}\) of geen enkele oplossing hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(-2x^{2} + 8 \le 0\).",
        opties=[r"\(V = ]-\infty, -2] \cup [2, +\infty[\)", r"\(V = [-2, 2]\)", r"\(V = ]-2, 2[\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"\(-2x^{2} + 8 = -2(x - 2)(x + 2)\). Een bergparabool is negatief buiten de nulwaarden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(-2x^{2} + 8 \le 0\) horen \(-2\) en \(2\) bij de oplossingen.",
        antwoord=True,
        uitleg=r"Door het gelijkheidsteken tellen de nulwaarden mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De kost per dag van een machine is \(K(u) = u^{2} - 8u + 30\) euro bij \(u\) uur draaien. Wanneer is de kost lager dan \(18\) euro?",
        opties=[r"\(2 < u < 6\)", r"\(u < 2\) of \(u > 6\)", r"\(u < 4\)", r"\(3 < u < 5\)"],
        antwoord=0,
        uitleg=r"\(u^{2} - 8u + 30 < 18 \iff u^{2} - 8u + 12 < 0 \iff (u - 2)(u - 6) < 0\).",
    ),
]
