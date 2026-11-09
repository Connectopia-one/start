# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: exponentiële en goniometrische vergelijkingen.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED). De fiche
vraagt: exponentiële vergelijkingen van de vorm b·a^x + c = 0 en
goniometrische vergelijkingen van de vorm a·sin b(x − c) + d = 0 algebraïsch
oplossen, met de rekenregels van machten en logaritmen, de
oplossingenverzameling noteren en vraagstukken oplossen.

Deel 1: exponentiële vergelijkingen. Deel 2: goniometrische vergelijkingen.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag=r"Los op: \(2^{x} = 64\). Schrijf \(x\).",
        antwoord=["6", "zes"],
        uitleg=r"\(64 = 2^{6}\), dus \(x = 6\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(3^{x} = \dfrac{1}{27}\). Schrijf \(x\).",
        antwoord=["-3", "−3", "min 3"],
        uitleg=r"\(\dfrac{1}{27} = 3^{-3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(5 \cdot 2^{x} - 40 = 0\).",
        opties=[r"\(V = \{3\}\)", r"\(V = \{8\}\)", r"\(V = \{4\}\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"\(5 \cdot 2^{x} = 40 \iff 2^{x} = 8 \iff x = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2^{x} = 7\). Wat is de exacte oplossing?",
        opties=[r"\(x = \log_{2} 7\)", r"\(x = \dfrac{7}{2}\)", r"\(x = \log_{7} 2\)", r"\(x = \sqrt{7}\)"],
        antwoord=0,
        uitleg=r"Als het rechterlid geen mooie macht van \(2\) is, neem je de logaritme: \(x = \log_{2} 7 = \dfrac{\log 7}{\log 2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2^{x} = 7\). Afgerond op twee cijfers na de komma is \(x\) ...",
        opties=[r"\(2{,}81\)", r"\(3{,}50\)", r"\(0{,}36\)", r"\(2{,}65\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{\log 7}{\log 2} \approx \dfrac{0{,}8451}{0{,}3010} \approx 2{,}81\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(4 \cdot 1{,}5^{x} + 3 = 0\).",
        opties=[r"\(V = \varnothing\)", r"\(V = \left\{\log_{1{,}5} \tfrac{3}{4}\right\}\)", r"\(V = \{-1\}\)", r"\(V = \{0\}\)"],
        antwoord=0,
        uitleg=r"\(1{,}5^{x} = -\tfrac{3}{4}\) kan niet: een macht met positief grondtal is nooit negatief.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Om \(a^{x} = k\) met \(k > 0\) op te lossen, neem je van beide leden de logaritme met grondtal \(a\).",
        antwoord=True,
        uitleg=r"\(x = \log_{a} k\). Met een rekentoestel reken je dat uit als \(\dfrac{\log k}{\log a}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(10^{x} = 0{,}001\). Schrijf \(x\).",
        antwoord=["-3", "−3", "min 3"],
        uitleg=r"\(0{,}001 = 10^{-3}\), of \(x = \log 0{,}001 = -3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(e^{x} = 5\).",
        opties=[r"\(x = \ln 5\)", r"\(x = \log 5\)", r"\(x = \dfrac{5}{e}\)", r"\(x = 5e\)"],
        antwoord=0,
        uitleg=r"\(\ln\) is de logaritme met grondtal \(e\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kapitaal van \(2000\) euro groeit met \(3\%\) per jaar. Welke vergelijking geeft de tijd waarna het \(3000\) euro is?",
        opties=[r"\(2000 \cdot 1{,}03^{t} = 3000\)", r"\(2000 + 0{,}03t = 3000\)", r"\(2000 \cdot 0{,}03^{t} = 3000\)", r"\(3000 \cdot 1{,}03^{t} = 2000\)"],
        antwoord=0,
        uitleg=r"Beginwaarde maal groeifactor tot de tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2000 \cdot 1{,}03^{t} = 3000\). Afgerond op één cijfer na de komma ...",
        opties=[r"\(t \approx 13{,}7\)", r"\(t \approx 16{,}7\)", r"\(t \approx 1{,}5\)", r"\(t \approx 50{,}0\)"],
        antwoord=0,
        uitleg=r"\(1{,}03^{t} = 1{,}5 \iff t = \dfrac{\log 1{,}5}{\log 1{,}03} \approx 13{,}7\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(2 \cdot 3^{x} = 18\) heeft dezelfde oplossing als \(6^{x} = 18\).",
        antwoord=False,
        uitleg=r"Je mag \(2\) en \(3\) niet samennemen onder de exponent. \(3^{x} = 9\) geeft \(x = 2\); \(6^{x} = 18\) geeft \(x \approx 1{,}61\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een stof halveert elke \(5\) jaar: \(M(t) = 80 \cdot 0{,}5^{t/5}\). Na hoeveel jaar is er nog \(10\) gram?",
        opties=[r"\(15\) jaar", r"\(40\) jaar", r"\(8\) jaar", r"\(35\) jaar"],
        antwoord=0,
        uitleg=r"\(0{,}5^{t/5} = \tfrac{1}{8} = 0{,}5^{3}\), dus \(\dfrac{t}{5} = 3\) en \(t = 15\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(9^{x} = 3\). Schrijf \(x\) als breuk, bijvoorbeeld 1/5.",
        antwoord=["1/2", "0,5", "0.5"],
        uitleg=r"\(9^{\frac{1}{2}} = \sqrt{9} = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vergelijking \(b \cdot a^{x} + c = 0\) met \(b > 0\) en \(c > 0\) heeft geen oplossing.",
        antwoord=True,
        uitleg=r"Dan is \(b \cdot a^{x} + c\) altijd groter dan \(c > 0\), dus nooit nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke stap is fout? \(3 \cdot 2^{x} = 24 \Rightarrow 6^{x} = 24 \Rightarrow x = \log_{6} 24\)",
        opties=[
            r"de eerste stap: \(3 \cdot 2^{x}\) is niet gelijk aan \(6^{x}\)",
            r"de tweede stap: de logaritme mag hier niet",
            r"geen enkele stap is fout",
            r"je moet eerst \(24\) delen door \(2\)",
        ],
        antwoord=0,
        uitleg=r"Deel eerst door \(3\): \(2^{x} = 8\), dus \(x = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bevolking van \(50\,000\) krimpt met \(4\%\) per jaar. Na hoeveel jaar zakt ze onder \(40\,000\)?",
        opties=[r"na \(6\) jaar", r"na \(5\) jaar", r"na \(3\) jaar", r"na \(10\) jaar"],
        antwoord=0,
        uitleg=r"\(0{,}96^{t} = 0{,}8 \iff t = \dfrac{\log 0{,}8}{\log 0{,}96} \approx 5{,}47\). In het zesde jaar zakt ze eronder, na \(6\) jaar is het zeker.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\log_{a} k\) is negatief als \(a > 1\) en \(k > 1\).",
        antwoord=False,
        uitleg=r"Met een grondtal groter dan \(1\) kom je boven \(1\) uit met een positieve exponent. Negatief is de logaritme pas als \(0 < k < 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(1{,}2^{x} - 2 = 0\), afgerond op twee cijfers na de komma.",
        opties=[r"\(x \approx 3{,}80\)", r"\(x \approx 1{,}67\)", r"\(x \approx 0{,}26\)", r"\(x \approx 2{,}40\)"],
        antwoord=0,
        uitleg=r"\(1{,}2^{x} = 2 \iff x = \dfrac{\log 2}{\log 1{,}2} \approx 3{,}80\). Dat is de verdubbelingstijd bij \(20\%\) groei.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij exponentiële groei vind je de verdubbelingstijd door \(a^{t} = 2\) op te lossen.",
        antwoord=True,
        uitleg=r"De beginwaarde valt weg uit \(b \cdot a^{t} = 2b\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(\sin x = \dfrac{1}{2}\).",
        opties=[r"\(V = \left\{\dfrac{\pi}{6}, \dfrac{5\pi}{6}\right\}\)", r"\(V = \left\{\dfrac{\pi}{6}\right\}\)", r"\(V = \left\{\dfrac{\pi}{3}, \dfrac{2\pi}{3}\right\}\)", r"\(V = \left\{\dfrac{\pi}{6}, \dfrac{7\pi}{6}\right\}\)"],
        antwoord=0,
        uitleg=r"\(\sin \dfrac{\pi}{6} = \dfrac{1}{2}\). De tweede oplossing is \(\pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Als \(\sin x = \sin \alpha\), welke oplossingen zijn er dan?",
        opties=[
            r"\(x = \alpha + k \cdot 2\pi\) of \(x = \pi - \alpha + k \cdot 2\pi\), met \(k \in \mathbb{Z}\)",
            r"enkel \(x = \alpha\)",
            r"\(x = \alpha + k \cdot \pi\), met \(k \in \mathbb{Z}\)",
            r"\(x = \pm \alpha + k \cdot 2\pi\), met \(k \in \mathbb{Z}\)",
        ],
        antwoord=0,
        uitleg=r"Twee punten op de goniometrische cirkel hebben dezelfde hoogte: \(\alpha\) en \(\pi - \alpha\). Elke volle toer erbij geeft opnieuw een oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(\sin x = -1\).",
        opties=[r"\(V = \left\{\dfrac{3\pi}{2}\right\}\)", r"\(V = \{\pi\}\)", r"\(V = \left\{\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right\}\)", r"\(V = \varnothing\)"],
        antwoord=0,
        uitleg=r"Enkel onderaan op de cirkel is de sinus \(-1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(2 \sin x - 1 = 0\).",
        opties=[r"\(V = \left\{\dfrac{\pi}{6}, \dfrac{5\pi}{6}\right\}\)", r"\(V = \left\{\dfrac{\pi}{3}, \dfrac{2\pi}{3}\right\}\)", r"\(V = \left\{\dfrac{7\pi}{6}, \dfrac{11\pi}{6}\right\}\)", r"\(V = \{1\}\)"],
        antwoord=0,
        uitleg=r"\(\sin x = \dfrac{1}{2}\), en dat geeft \(\dfrac{\pi}{6}\) en \(\dfrac{5\pi}{6}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(2 \sin x + \sqrt{3} = 0\).",
        opties=[r"\(V = \left\{\dfrac{4\pi}{3}, \dfrac{5\pi}{3}\right\}\)", r"\(V = \left\{\dfrac{\pi}{3}, \dfrac{2\pi}{3}\right\}\)", r"\(V = \left\{\dfrac{7\pi}{6}, \dfrac{11\pi}{6}\right\}\)", r"\(V = \left\{\dfrac{5\pi}{3}\right\}\)"],
        antwoord=0,
        uitleg=r"\(\sin x = -\dfrac{\sqrt{3}}{2}\). Negatief, dus derde en vierde kwadrant: \(\pi + \dfrac{\pi}{3}\) en \(2\pi - \dfrac{\pi}{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(3 \sin x = 4\) heeft geen oplossing.",
        antwoord=True,
        uitleg=r"\(\sin x = \tfrac{4}{3} > 1\) kan niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, \pi]\): \(\sin 2x = 1\).",
        opties=[r"\(V = \left\{\dfrac{\pi}{4}\right\}\)", r"\(V = \left\{\dfrac{\pi}{2}\right\}\)", r"\(V = \left\{\dfrac{\pi}{4}, \dfrac{3\pi}{4}\right\}\)", r"\(V = \{\pi\}\)"],
        antwoord=0,
        uitleg=r"\(2x = \dfrac{\pi}{2} + k \cdot 2\pi\), dus \(x = \dfrac{\pi}{4} + k\pi\). In \([0, \pi]\) is dat enkel \(\dfrac{\pi}{4}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(\sin 2x = 1\) liggen de oplossingen \(\pi\) uit elkaar, en niet \(2\pi\).",
        antwoord=True,
        uitleg=r"De periode van \(\sin 2x\) is \(\pi\). Na het delen door \(2\) wordt \(k \cdot 2\pi\) dus \(k \cdot \pi\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(\sin\left(x - \dfrac{\pi}{4}\right) = 0\), met \(k \in \mathbb{Z}\).",
        opties=[r"\(x = \dfrac{\pi}{4} + k\pi\)", r"\(x = -\dfrac{\pi}{4} + k\pi\)", r"\(x = \dfrac{\pi}{4} + k \cdot 2\pi\)", r"\(x = k\pi\)"],
        antwoord=0,
        uitleg=r"\(\sin u = 0 \iff u = k\pi\). Dus \(x - \dfrac{\pi}{4} = k\pi\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(\sin x = 0{,}3\). Afgerond op twee cijfers na de komma ...",
        opties=[r"\(x \approx 0{,}30\) of \(x \approx 2{,}84\)", r"\(x \approx 0{,}30\) of \(x \approx 3{,}44\)", r"enkel \(x \approx 0{,}30\)", r"\(x \approx 17{,}46\) of \(x \approx 162{,}54\)"],
        antwoord=0,
        uitleg=r"Met de rekenmachine in radialen: \(\sin^{-1} 0{,}3 \approx 0{,}3047\). De tweede oplossing is \(\pi - 0{,}3047 \approx 2{,}84\). De laatste optie staat in graden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin x = 0{,}3\) heeft in \([0, 2\pi]\) ook een oplossing in het derde kwadrant.",
        antwoord=False,
        uitleg=r"In het derde kwadrant is de sinus negatief. De twee oplossingen liggen in het eerste en het tweede kwadrant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het water in een haven: \(h(t) = 2 \sin\left(\dfrac{\pi}{6} t\right) + 3\) m, met \(t\) in uur. Wanneer staat het water voor het eerst op \(4\) m?",
        opties=[r"na \(1\) uur", r"na \(3\) uur", r"na \(5\) uur", r"na \(2\) uur"],
        antwoord=0,
        uitleg=r"\(\sin\left(\dfrac{\pi}{6} t\right) = \dfrac{1}{2} \iff \dfrac{\pi}{6} t = \dfrac{\pi}{6}\), dus \(t = 1\). De tweede keer is bij \(\dfrac{\pi}{6} t = \dfrac{5\pi}{6}\): \(t = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij datzelfde water \(h(t) = 2 \sin\left(\dfrac{\pi}{6} t\right) + 3\): na hoeveel uur staat het water op \(5\) m? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(\sin\left(\dfrac{\pi}{6} t\right) = 1 \iff \dfrac{\pi}{6} t = \dfrac{\pi}{2} \iff t = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vergelijking is van de vorm \(a \sin b(x - c) + d = 0\)?",
        opties=[r"\(4 \sin 3(x - 1) + 2 = 0\)", r"\(4 \sin x + \cos x = 0\)", r"\(\sin x^{2} = 1\)", r"\(\sin x \cdot x = 0\)"],
        antwoord=0,
        uitleg=r"Hier is \(a = 4\), \(b = 3\), \(c = 1\) en \(d = 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een goniometrische vergelijking die een oplossing heeft, heeft op \(\mathbb{R}\) precies twee oplossingen.",
        antwoord=False,
        uitleg=r"Door de periode keert elke oplossing telkens terug, dus zijn er oneindig veel. Enkel in een begrensd interval zoals \([0, 2\pi]\) tel je er een paar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op in \([0, 2\pi]\): \(\sin x + 1 = 1\).",
        opties=[r"\(V = \{0, \pi, 2\pi\}\)", r"\(V = \{0\}\)", r"\(V = \left\{\dfrac{\pi}{2}\right\}\)", r"\(V = \{\pi\}\)"],
        antwoord=0,
        uitleg=r"\(\sin x = 0\): bij \(0\), \(\pi\) en \(2\pi\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(\sin x = \dfrac{\sqrt{2}}{2}\), met \(k \in \mathbb{Z}\).",
        opties=[
            r"\(x = \dfrac{\pi}{4} + k \cdot 2\pi\) of \(x = \dfrac{3\pi}{4} + k \cdot 2\pi\)",
            r"\(x = \dfrac{\pi}{4} + k\pi\)",
            r"\(x = \dfrac{\pi}{4} + k \cdot 2\pi\) of \(x = -\dfrac{\pi}{4} + k \cdot 2\pi\)",
            r"\(x = \dfrac{\pi}{3} + k \cdot 2\pi\) of \(x = \dfrac{2\pi}{3} + k \cdot 2\pi\)",
        ],
        antwoord=0,
        uitleg=r"\(\sin \dfrac{\pi}{4} = \dfrac{\sqrt{2}}{2}\), en \(\pi - \dfrac{\pi}{4} = \dfrac{3\pi}{4}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Om \(\sin x = 0{,}3\) op te lossen, mag je je rekenmachine in graden laten staan als je de oplossing in radialen wil.",
        antwoord=False,
        uitleg=r"Dan krijg je \(17{,}46°\) en niet \(0{,}30\) rad. Zet de rekenmachine eerst in radialen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een reuzenrad: \(h(t) = 10 \sin\left(\dfrac{\pi}{5}(t - 2{,}5)\right) + 12\) m. Wanneer is een bakje voor het eerst op \(12\) m hoogte na \(t = 0\)?",
        opties=[r"na \(2{,}5\) min", r"na \(5\) min", r"na \(0\) min", r"na \(10\) min"],
        antwoord=0,
        uitleg=r"\(12\) m is de evenwichtslijn: \(\sin\left(\dfrac{\pi}{5}(t - 2{,}5)\right) = 0\). Dat gebeurt voor het eerst bij \(t = 2{,}5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De oplossingen van \(\sin x = -0{,}5\) in \([0, 2\pi]\) zijn \(\dfrac{7\pi}{6}\) en \(\dfrac{11\pi}{6}\).",
        antwoord=True,
        uitleg=r"Negatieve sinus: derde en vierde kwadrant, \(\pi + \dfrac{\pi}{6}\) en \(2\pi - \dfrac{\pi}{6}\).",
    ),
]
