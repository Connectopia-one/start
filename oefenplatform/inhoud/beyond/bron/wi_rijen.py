# -*- coding: utf-8 -*-
"""Rijen en hun limiet.

Het laatste onderdeel van de analysefiche G1. De fiche koppelt rijen
uitdrukkelijk aan de functies van de vorige thema's: een rekenkundige rij
hoort bij lineaire groei en een eerstegraadsfunctie, een meetkundige rij bij
exponentiële groei.

Deel 1 zijn de twee soorten rijen, hun voorschriften en hun somformules.
Deel 2 zijn de limieten: convergentie, divergentie en de som van een
oneindige meetkundige rij.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een rekenkundige rij?",
        opties=[
            r"een rij waarbij \(u_{n+1} = u_{n} + d\)",
            r"een rij waarbij \(u_{n+1} = u_{n} \cdot d\)",
            r"een rij waarbij \(u_{n+1} = u_{n}^{\,2}\)",
            r"een rij waarbij \(u_{n+1} = d - u_{n}\)",
        ],
        antwoord=0,
        uitleg=r"Dat vaste getal \(d\) heet het verschil van de rij. Telkens vermenigvuldigen geeft een meetkundige rij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meetkundige rij?",
        opties=[
            r"een rij waarbij \(u_{n+1} = u_{n} \cdot q\)",
            r"een rij waarbij \(u_{n+1} = u_{n} + q\)",
            r"een rij waarbij \(u_{n+1} = u_{n} \cdot n\)",
            r"een rij waarbij \(u_{n+1} = q - u_{n}\)",
        ],
        antwoord=0,
        uitleg=r"Dat vaste getal \(q\) heet de reden van de rij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem de rij \(3,\ 7,\ 11,\ 15,\ \dots\) Hoeveel is het verschil \(d\)? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"Elke term is vier meer dan de vorige: \(d = u_{2} - u_{1} = 7 - 3 = 4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een recursief voorschrift berekent \(u_{n+1}\) uit \(u_{n}\).",
        antwoord=True,
        uitleg=r"Daarom heb je er ook altijd de beginterm \(u_{1}\) bij nodig. Een expliciet voorschrift geeft \(u_{n}\) rechtstreeks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt het expliciete voorschrift van een rekenkundige rij?",
        opties=[
            r"\(u_{n} = u_{1} + (n-1)\,d\)",
            r"\(u_{n} = u_{1} + n\,d\)",
            r"\(u_{n} = u_{1} \cdot d^{\,n}\)",
            r"\(u_{n} = (u_{1} + d)^{\,n}\)",
        ],
        antwoord=0,
        uitleg=r"Om bij \(u_{n}\) te komen, tel je \(d\) precies \(n-1\) keer op bij \(u_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Neem de rij \(3,\ 7,\ 11,\ \dots\) Hoeveel is \(u_{10}\)?",
        opties=[r"\(39\)", r"\(43\)", r"\(37\)", r"\(30\)"],
        antwoord=0,
        uitleg=r"\(u_{10} = 3 + 9 \cdot 4 = 39\). Negen stappen, niet tien, want \(u_{1}\) staat er al.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De rij \(2,\ 6,\ 18,\ 54,\ \dots\) is een rekenkundige rij.",
        antwoord=False,
        uitleg=r"Het verschil groeit telkens, maar de factor blijft \(3\). Het is dus een meetkundige rij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem de rij \(2,\ 6,\ 18,\ 54,\ \dots\) Hoeveel is de reden \(q\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(q = \dfrac{u_{2}}{u_{1}} = \dfrac{6}{2} = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de somformule van een rekenkundige rij?",
        opties=[
            r"\(S_{n} = n \cdot \dfrac{u_{1} + u_{n}}{2}\)",
            r"\(S_{n} = n \cdot (u_{n} - u_{1})\)",
            r"\(S_{n} = n\,u_{1} + n\,d\)",
            r"\(S_{n} = \dfrac{n\,u_{n}}{2}\)",
        ],
        antwoord=0,
        uitleg=r"Je legt de rij twee keer naast elkaar, een keer vooruit en een keer achteruit. Elk paar geeft dan \(u_{1} + u_{n}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De punten \((n,\ u_{n})\) van een rekenkundige rij liggen op een rechte.",
        antwoord=True,
        uitleg=r"Het verschil \(d\) is de richtingscoëfficiënt. Daarom hoort een rekenkundige rij bij lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Neem de rij \(2,\ 6,\ 18,\ \dots\) Hoeveel is \(u_{5}\)?",
        opties=[r"\(162\)", r"\(54\)", r"\(216\)", r"\(108\)"],
        antwoord=0,
        uitleg=r"\(u_{5} = 2 \cdot 3^{4} = 2 \cdot 81 = 162\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(1 + 2 + 3 + \dots + 10\)? Schrijf het getal.",
        antwoord=["55", "vijfenvijftig"],
        uitleg=r"\(S_{10} = 10 \cdot \dfrac{1 + 10}{2} = 10 \cdot 5{,}5 = 55\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soort groei hoort bij een meetkundige rij?",
        opties=[
            "exponentiële groei",
            "lineaire groei",
            "kwadratische groei",
            "logaritmische groei",
        ],
        antwoord=0,
        uitleg=r"Een vaste factor per stap is net wat \(f(x) = a \cdot b^{x}\) doet. Een vast verschil hoort bij lineaire groei.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een meetkundige rij met \(q = 1\) stijgt steeds sneller.",
        antwoord=False,
        uitleg=r"Met \(q = 1\) blijft elke term gelijk aan de vorige. De rij is dan constant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe luidt de somformule van een meetkundige rij met \(q \neq 1\)?",
        opties=[
            r"\(S_{n} = u_{1} \cdot \dfrac{1 - q^{\,n}}{1 - q}\)",
            r"\(S_{n} = u_{1} \cdot \dfrac{1 - q}{1 - q^{\,n}}\)",
            r"\(S_{n} = u_{1} \cdot \dfrac{q^{\,n} - 1}{q}\)",
            r"\(S_{n} = n \cdot u_{1} \cdot q^{\,n}\)",
        ],
        antwoord=0,
        uitleg=r"In de teller staat \(q^{\,n}\), dus het aantal termen telt mee. Met \(q = 1\) wordt de noemer nul en gebruik je \(S_{n} = n\,u_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer daalt een rekenkundige rij?",
        opties=[
            r"als \(d < 0\)",
            r"als \(u_{1} < 0\)",
            r"als \(d < 1\)",
            r"als \(n\) oneven is",
        ],
        antwoord=0,
        uitleg=r"Alleen het teken van \(d\) beslist. Een rij die begint bij \(u_{1} = -100\) met \(d = 3\) stijgt gewoon.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een meetkundige rij met \(q < 0\) wisselen de termen van teken.",
        antwoord=True,
        uitleg="Zo'n rij heet alternerend: om beurten positief en negatief.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een rij heeft als voorschrift \(u_{n} = 4n - 1\). Hoeveel is \(u_{1}\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"Vul \(n = 1\) in: \(4 \cdot 1 - 1 = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet geld op een rekening met samengestelde intrest. Welke rij vormen de jaarlijkse saldo's?",
        opties=[
            "een meetkundige rij",
            "een rekenkundige rij",
            "een alternerende rij",
            "een rij zonder vast patroon",
        ],
        antwoord=0,
        uitleg=r"Elk jaar vermenigvuldig je met dezelfde groeifactor \(q\). Bij enkelvoudige intrest tel je elk jaar hetzelfde bedrag op, en dan is ze rekenkundig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe verloopt een meetkundige rij met \(q > 1\) en \(u_{1} > 0\)?",
        opties=[
            "ze stijgt, met een toenemende stijging",
            "ze stijgt, met een afnemende stijging",
            "ze stijgt met telkens evenveel per stap",
            "ze daalt naar nul toe zonder die te halen",
        ],
        antwoord=0,
        uitleg=r"Elke stap wordt groter dan de vorige, want je vermenigvuldigt telkens een groter getal met dezelfde \(q\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een rij convergeert?",
        opties=[
            "haar termen naderen een vast eindig getal",
            "haar termen worden steeds groter en groter",
            "haar termen wisselen voortdurend van teken",
            "haar termen zijn vanaf een bepaalde plaats gelijk",
        ],
        antwoord=0,
        uitleg=r"Dat getal is de limiet van de rij: \(\lim\limits_{n \to +\infty} u_{n} = L\). Gaat ze naar oneindig of blijft ze springen, dan divergeert ze.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\lim\limits_{n \to +\infty} q^{\,n}\) als \(-1 < q < 1\)?",
        opties=[r"\(0\)", r"\(1\)", r"\(q\)", r"\(+\infty\)"],
        antwoord=0,
        uitleg=r"Telkens met een getal vermenigvuldigen waarvan \(|q| < 1\) maakt de termen almaar kleiner.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{n \to +\infty} \dfrac{1}{n}\)? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"Hoe groter \(n\), hoe kleiner de breuk. Ze wordt nooit nul, maar komt er onbeperkt dicht bij.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rekenkundige rij met \(d = 2\) convergeert.",
        antwoord=False,
        uitleg=r"Ze blijft met \(2\) per stap toenemen en gaat dus naar \(+\infty\). Alleen een rekenkundige rij met \(d = 0\) convergeert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een alternerende rij?",
        opties=[
            "een rij waarvan de termen om beurten positief en negatief zijn",
            "een rij waarvan de termen om beurten stijgen en dalen in waarde",
            "een rij die uit twee verschillende rijen is samengesteld",
            "een rij die om beurten geheel en gebroken is in haar termen",
        ],
        antwoord=0,
        uitleg=r"Je herkent ze aan een factor \((-1)^{n}\) in het voorschrift.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\lim\limits_{n \to +\infty} (-1)^{n}\)?",
        opties=[
            r"die bestaat niet, de rij blijft springen",
            r"\(0\), want de termen heffen elkaar op",
            r"\(1\), want dat is de grootste waarde",
            r"\(-1\), want dat is de kleinste waarde",
        ],
        antwoord=0,
        uitleg=r"De termen blijven heen en weer gaan tussen \(-1\) en \(1\) en naderen dus geen enkel getal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een divergente rij kan naar \(+\infty\) gaan.",
        antwoord=True,
        uitleg="Divergent betekent alleen dat er geen eindige limiet is. Naar oneindig gaan of blijven springen zijn allebei vormen van divergentie.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(1 + \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{8} + \dots\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"Een meetkundige rij met \(u_{1} = 1\) en \(q = \tfrac{1}{2}\), dus \(S = \dfrac{u_{1}}{1 - q} = \dfrac{1}{0{,}5} = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de som van een oneindige meetkundige rij?",
        opties=[
            r"\(S = \dfrac{u_{1}}{1 - q}\)",
            r"\(S = \dfrac{u_{1}}{q - 1}\)",
            r"\(S = \dfrac{q}{1 - u_{1}}\)",
            r"\(S = u_{1} \cdot q\)",
        ],
        antwoord=0,
        uitleg=r"In de somformule kruipt \(q^{\,n}\) naar nul, dus daar blijft dit van over.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke oneindige meetkundige rij heeft een eindige som.",
        antwoord=False,
        uitleg=r"Alleen als \(|q| < 1\). Bij \(q = 2\) groeit de som onbeperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Onder welke voorwaarde bestaat de som van een oneindige meetkundige rij?",
        opties=[
            r"\(|q| < 1\)",
            r"\(|q| > 1\)",
            r"\(u_{1} < 1\)",
            r"\(u_{1} > q\)",
        ],
        antwoord=0,
        uitleg=r"Pas dan worden de termen zo snel klein dat de som naar een vast getal kruipt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{n \to +\infty} \dfrac{2n + 1}{n}\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"Splits op: \(\dfrac{2n+1}{n} = 2 + \dfrac{1}{n}\), en \(\dfrac{1}{n}\) kruipt naar nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de somrij van een rij?",
        opties=[
            r"de rij met als termen \(S_{1},\ S_{2},\ S_{3},\ \dots\)",
            r"de rij met als termen \(u_{2} - u_{1},\ u_{3} - u_{2},\ \dots\)",
            r"de rij van alle termen bij elkaar opgeteld",
            r"de rij van de gemiddelden van de termen",
        ],
        antwoord=0,
        uitleg=r"Haar \(n\)-de term is \(S_{n} = u_{1} + u_{2} + \dots + u_{n}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De somrij van een meetkundige rij met \(q = \tfrac{1}{2}\) convergeert.",
        antwoord=True,
        uitleg=r"\(|q| < 1\), dus de som nadert een vast getal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\lim\limits_{n \to +\infty} 2^{\,n}\)?",
        opties=[
            r"\(+\infty\)",
            r"\(0\)",
            r"\(2\)",
            r"die bestaat niet, de rij springt",
        ],
        antwoord=0,
        uitleg=r"Bij \(q > 1\) groeien de termen onbeperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\lim (u_{n} + v_{n})\) als beide rijen convergeren?",
        opties=[
            r"\(\lim u_{n} + \lim v_{n}\)",
            r"\(\lim u_{n} \cdot \lim v_{n}\)",
            r"de grootste van de twee limieten",
            r"die limiet bestaat dan nooit",
        ],
        antwoord=0,
        uitleg="Dezelfde rekenregels als bij limieten van functies, zolang beide limieten eindig zijn.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het getal \(0{,}999\dots\), met oneindig veel negens, is gelijk aan \(1\).",
        antwoord=True,
        uitleg=r"Het is de som van een meetkundige rij met \(u_{1} = \tfrac{9}{10}\) en \(q = \tfrac{1}{10}\), en \(\dfrac{0{,}9}{1 - 0{,}1} = 1\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem de rij \(1,\ \tfrac{1}{3},\ \tfrac{1}{9},\ \dots\) Hoeveel is de reden \(q\)? Schrijf ze als breuk.",
        antwoord=["1/3"],
        uitleg=r"Elke term is \(\tfrac{1}{3}\) van de vorige.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal stuitert telkens tot \(70\%\) van de vorige hoogte. Wat kan je berekenen?",
        opties=[
            r"de totale hoogte, want \(|q| < 1\)",
            r"niets, want de bal stuitert oneindig lang",
            r"enkel de hoogte van de eerste tien sprongen",
            r"de totale hoogte, maar enkel tot één meter",
        ],
        antwoord=0,
        uitleg=r"\(q = 0{,}7\) ligt tussen \(0\) en \(1\), dus de oneindige som bestaat. Oneindig veel sprongen kunnen samen een eindige hoogte geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom spreek je bij een rij alleen over de limiet op oneindig?",
        opties=[
            r"omdat \(n\) alleen in \(\mathbb{N}\) ligt",
            r"omdat een rij oneindig veel losse termen heeft",
            r"omdat een rij nooit een eindige limiet heeft",
            r"omdat een rij geen kromme als grafiek geeft",
        ],
        antwoord=0,
        uitleg=r"Er zijn geen tussenwaarden om naartoe te kruipen: tussen \(u_{3}\) en \(u_{4}\) ligt niets. Alleen \(n\) die onbeperkt groeit heeft zin.",
    ),
]
