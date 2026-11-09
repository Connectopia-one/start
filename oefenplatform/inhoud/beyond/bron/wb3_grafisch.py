# -*- coding: utf-8 -*-
"""Grafisch onderzoek van een functie.

Wiskunde basis, derde graad. De fiche vraagt: voorstellingswijzen
(verwoording, tabel, grafiek, voorschrift) en de functiekenmerken domein,
praktisch domein, bereik, praktisch bereik, nulwaarden, nulpunten,
snijpunten met de assen, tekenverloop, stijgen/dalen/constant, extrema,
toenemende en afnemende stijging of daling, symmetrie, even en oneven,
periode, verticale en horizontale asymptoten en gedrag op oneindig, altijd in
verband met de situatie die de functie beschrijft. De grafieken zijn hier in
woorden of met een tabel beschreven.

Notaties volgen de bijlage van de fiche: dom f, ber f, nulwaarde is de
x-waarde, nulpunt is de coördinaat.

Deel 1: de begrippen. Deel 2: kenmerken in een situatie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen een nulwaarde en een nulpunt van een functie \(f\)?",
        opties=[
            r"Een nulwaarde is de \(x\)-waarde van een snijpunt met de \(x\)-as, een nulpunt is de coördinaat van dat snijpunt.",
            r"Een nulwaarde is de coördinaat van een snijpunt met de \(x\)-as, een nulpunt is de \(x\)-waarde ervan.",
            r"Een nulwaarde is het snijpunt met de \(y\)-as, een nulpunt het snijpunt met de \(x\)-as.",
            r"Er is geen verschil: beide woorden betekenen het snijpunt met de \(y\)-as.",
        ],
        antwoord=0,
        uitleg=r"Snijdt de grafiek de \(x\)-as in \((3, 0)\), dan is \(3\) de nulwaarde en \((3, 0)\) het nulpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het domein van een functie \(f\), genoteerd \(\text{dom} f\)?",
        opties=[
            r"alle \(x\)-waarden waarvoor \(f(x)\) bestaat",
            r"alle \(y\)-waarden die de functie aanneemt",
            r"alle \(x\)-waarden waarvoor \(f(x) = 0\)",
            r"alle \(x\)-waarden waarvoor de grafiek stijgt",
        ],
        antwoord=0,
        uitleg=r"Het domein gaat over de \(x\)-as. De \(y\)-waarden die de functie aanneemt, vormen het bereik \(\text{ber} f\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het domein van \(f(x) = \dfrac{1}{x - 2}\)?",
        opties=[r"\(\mathbb{R} \setminus \{2\}\)", r"\(\mathbb{R} \setminus \{-2\}\)", r"\(\mathbb{R}\)", r"\([2, +\infty[\)"],
        antwoord=0,
        uitleg=r"Voor \(x = 2\) wordt de noemer nul en bestaat \(f(x)\) niet. Elke andere \(x\) mag.",
    ),
    dict(
        type="invultekst",
        vraag=r"Waar snijdt de grafiek van \(f(x) = 3x - 6\) de \(y\)-as? Schrijf de \(y\)-coördinaat.",
        antwoord=["-6", "−6", "min 6"],
        uitleg=r"Op de \(y\)-as is \(x = 0\): \(f(0) = 3 \cdot 0 - 6 = -6\). Het snijpunt is \((0, -6)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de nulwaarde van \(f(x) = 3x - 6\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(3x - 6 = 0 \iff x = 2\). Het nulpunt is \((2, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat toont een tekenverloop van een functie?",
        opties=[
            r"waar de grafiek boven of onder de \(x\)-as ligt en waar ze de \(x\)-as snijdt",
            r"waar de grafiek stijgt of daalt en waar ze een maximum bereikt",
            r"hoe steil de grafiek is in elk punt",
            r"welke \(y\)-waarden de functie aanneemt",
        ],
        antwoord=0,
        uitleg=r"Een tekenverloop gebruikt \(+\), \(-\) en \(0\). Stijgen en dalen staan in een verloopschema.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie is even als haar grafiek symmetrisch is ten opzichte van de \(y\)-as.",
        antwoord=True,
        uitleg=r"Even betekent \(f(-x) = f(x)\) voor elke \(x\): links en rechts van de \(y\)-as is de grafiek elkaars spiegelbeeld. Een voorbeeld is \(f(x) = x^{2}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van een oneven functie is symmetrisch ten opzichte van de \(x\)-as.",
        antwoord=False,
        uitleg=r"Een oneven functie, met \(f(-x) = -f(x)\), is puntsymmetrisch ten opzichte van de oorsprong. Een voorbeeld is \(f(x) = x^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke functie is oneven?",
        opties=[r"\(f(x) = x^{3}\)", r"\(f(x) = x^{2}\)", r"\(f(x) = x^{2} + 1\)", r"\(f(x) = x + 1\)"],
        antwoord=0,
        uitleg=r"\((-x)^{3} = -x^{3}\), dus \(f(-x) = -f(x)\). \(x + 1\) is even noch oneven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een functie stijgt op een interval en de grafiek wordt daar steeds steiler. Hoe noem je dat?",
        opties=[r"toenemende stijging", r"afnemende stijging", r"toenemende daling", r"constante stijging"],
        antwoord=0,
        uitleg=r"Bij een toenemende stijging komen er per stap steeds grotere stukken bij. Bij een afnemende stijging worden die stukken kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel van een functie: \(f(0) = 10\), \(f(1) = 16\), \(f(2) = 20\), \(f(3) = 22\), \(f(4) = 23\). Hoe verloopt de functie op \([0, 4]\)?",
        opties=[r"afnemende stijging", r"toenemende stijging", r"constante stijging", r"afnemende daling"],
        antwoord=0,
        uitleg=r"De functie stijgt telkens, maar met \(6\), \(4\), \(2\) en dan \(1\): de stijging neemt af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een functie \(f\) heeft als horizontale asymptoot \(y = 3\). Wat betekent dat?",
        opties=[
            r"Voor heel grote of heel kleine \(x\) komt \(f(x)\) steeds dichter bij \(3\).",
            r"De grafiek snijdt de \(y\)-as in \(3\).",
            r"De functie bestaat niet voor \(x = 3\).",
            r"De functie heeft een maximum gelijk aan \(3\).",
        ],
        antwoord=0,
        uitleg=r"Een horizontale asymptoot beschrijft het gedrag op oneindig. Een verticale asymptoot hoort bij een \(x\)-waarde waar de functie niet bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke verticale asymptoot heeft \(f(x) = \dfrac{5}{x + 4}\)?",
        opties=[r"\(x = -4\)", r"\(x = 4\)", r"\(y = 5\)", r"\(x = 5\)"],
        antwoord=0,
        uitleg=r"Voor \(x = -4\) is de noemer nul. In de buurt daarvan worden de functiewaarden heel groot of heel klein: daar ligt de verticale asymptoot.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie met periode \(5\) heeft dezelfde functiewaarde in \(x = 2\) en in \(x = 12\).",
        antwoord=True,
        uitleg=r"Bij periode \(5\) herhaalt de grafiek zich na elke \(5\) eenheden. \(12 = 2 + 2 \cdot 5\), dus \(f(12) = f(2)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie die op \([1, 6]\) eerst stijgt en daarna daalt, heeft op dat interval een minimum.",
        antwoord=False,
        uitleg=r"Waar stijgen overgaat in dalen, ligt een maximum. Een minimum ligt waar dalen overgaat in stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f\) daalt van \(x = -\infty\) tot \(x = 1\), bereikt in \((1, -4)\) haar laagste punt en stijgt daarna. Wat is het bereik van \(f\)?",
        opties=[r"\([-4, +\infty[\)", r"\(]-\infty, -4]\)", r"\([1, +\infty[\)", r"\(\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"De kleinste functiewaarde is \(-4\) en naar beide kanten worden de waarden onbeperkt groot. Het bereik gaat over de \(y\)-waarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe schrijf je het gedrag op oneindig van \(f(x) = \dfrac{1}{x}\) voor grote \(x\)?",
        opties=[
            r"als \(x \to +\infty\), dan \(f(x) \to 0\)",
            r"als \(x \to +\infty\), dan \(f(x) \to +\infty\)",
            r"als \(x \to 0\), dan \(f(x) \to 1\)",
            r"als \(x \to +\infty\), dan \(f(x) \to 1\)",
        ],
        antwoord=0,
        uitleg=r"\(\dfrac{1}{1000} = 0{,}001\): hoe groter \(x\), hoe dichter \(f(x)\) bij \(0\). De \(x\)-as is dus een horizontale asymptoot.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke functie heeft minstens één nulwaarde.",
        antwoord=False,
        uitleg=r"\(f(x) = x^{2} + 1\) is altijd minstens \(1\) en snijdt de \(x\)-as nooit. Ze heeft dus geen nulwaarde.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie heeft hoogstens één snijpunt met de \(y\)-as.",
        antwoord=True,
        uitleg=r"Bij \(x = 0\) hoort hoogstens één functiewaarde \(f(0)\). Anders zou het geen functie zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij welk symbool in een tekenverloop ligt de grafiek onder de \(x\)-as?",
        opties=[r"\(-\)", r"\(+\)", r"\(0\)", r"\(\vert\)"],
        antwoord=0,
        uitleg=r"\(+\) betekent boven de \(x\)-as, \(-\) eronder en \(0\) is een snijpunt met de \(x\)-as. De verticale streep hoort bij een plaats waar de functie niet bestaat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"De functie \(h(t) = 30t - 5t^{2}\) geeft de hoogte in meter van een bal \(t\) seconden na de worp, tot hij de grond raakt. Wat is het praktisch domein?",
        opties=[r"\([0, 6]\)", r"\(\mathbb{R}\)", r"\([0, +\infty[\)", r"\([0, 45]\)"],
        antwoord=0,
        uitleg=r"De tijd begint bij \(0\) en de bal raakt de grond als \(30t - 5t^{2} = 0\), dus bij \(t = 6\). Daarbuiten heeft de formule geen betekenis.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij dezelfde bal, \(h(t) = 30t - 5t^{2}\) op \([0, 6]\): wat is het praktisch bereik?",
        opties=[r"\([0, 45]\)", r"\([0, 6]\)", r"\([0, 30]\)", r"\([0, +\infty[\)"],
        antwoord=0,
        uitleg=r"De hoogste stand is in \(t = 3\): \(h(3) = 90 - 45 = 45\) m. De laagste stand is \(0\) m, op de grond.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(h(t) = 30t - 5t^{2}\): hoeveel meter hoog is de bal na \(2\) seconden? Schrijf het getal.",
        antwoord=["40", "veertig"],
        uitleg=r"\(h(2) = 30 \cdot 2 - 5 \cdot 4 = 60 - 20 = 40\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De temperatuur \(T(u)\) in een kamer, \(u\) uur na middernacht, daalt van \(0\) tot \(5\) uur en stijgt daarna tot \(15\) uur. Wat betekent het minimum van \(T\)?",
        opties=[
            r"de laagste temperatuur in de kamer, rond \(5\) uur 's morgens",
            r"het uur waarop de verwarming uitgaat",
            r"de gemiddelde temperatuur over de hele dag",
            r"de temperatuur om middernacht",
        ],
        antwoord=0,
        uitleg=r"Het minimum is de kleinste functiewaarde. Waar dalen overgaat in stijgen, hier op \(u = 5\), wordt het bereikt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De waarde \(W(t)\) van een auto, \(t\) jaar na aankoop, daalt elk jaar, maar elk jaar minder hard. Hoe noem je dat verloop?",
        opties=[r"afnemende daling", r"toenemende daling", r"afnemende stijging", r"constante daling"],
        antwoord=0,
        uitleg=r"De functie daalt, en de daling per jaar wordt kleiner: een afnemende daling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bedrijf heeft winst \(W(q)\) bij \(q\) verkochte stuks. Het tekenverloop is: \(-\) voor \(q < 200\), \(0\) bij \(q = 200\), \(+\) voor \(q > 200\). Wat betekent dat?",
        opties=[
            r"Pas vanaf meer dan \(200\) stuks maakt het bedrijf winst.",
            r"De winst is maximaal bij \(200\) stuks.",
            r"Het bedrijf maakt altijd winst.",
            r"De winst daalt vanaf \(200\) stuks.",
        ],
        antwoord=0,
        uitleg=r"Een tekenverloop zegt of de winst negatief of positief is. Over het maximum zegt het niets.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een winstfunctie \(W(q)\) is de nulwaarde het aantal stuks waarbij er geen winst en geen verlies is.",
        antwoord=True,
        uitleg=r"In de nulwaarde is \(W(q) = 0\). Dat aantal heet ook het break-evenpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De hoeveelheid medicijn in het bloed \(M(t)\) daalt na de inname en komt steeds dichter bij \(0\) mg, zonder het ooit te halen. Welk kenmerk beschrijft dat?",
        opties=[
            r"een horizontale asymptoot \(M = 0\)",
            r"een verticale asymptoot \(t = 0\)",
            r"een nulwaarde",
            r"een periode",
        ],
        antwoord=0,
        uitleg=r"Steeds dichter bij een waarde komen zonder ze te halen, is gedrag op oneindig: een horizontale asymptoot.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De waterhoogte in een haven gaat elke \(12{,}5\) uur op en neer. Welk kenmerk is die \(12{,}5\) uur?",
        opties=[r"de periode", r"het maximum", r"de nulwaarde", r"het bereik"],
        antwoord=0,
        uitleg=r"Een verloop dat zich telkens na dezelfde tijd herhaalt, is periodiek. Die tijd is de periode.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het praktisch domein van een functie is altijd hetzelfde als haar domein.",
        antwoord=False,
        uitleg=r"Het praktisch domein bevat enkel de \(x\)-waarden die in de situatie zin hebben, zoals geen negatieve tijd. Het is vaak kleiner dan het domein.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een taxi rekent \(4\) euro instap plus \(2\) euro per kilometer. Welk voorschrift past bij de prijs \(P\) voor \(k\) kilometer?",
        opties=[r"\(P(k) = 2k + 4\)", r"\(P(k) = 4k + 2\)", r"\(P(k) = 6k\)", r"\(P(k) = 2(k + 4)\)"],
        antwoord=0,
        uitleg=r"Per kilometer \(2\) euro geeft \(2k\), en de instap van \(4\) euro komt er één keer bij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Met \(P(k) = 2k + 4\): hoeveel kilometer rij je voor \(30\) euro? Schrijf het getal.",
        antwoord=["13", "dertien"],
        uitleg=r"\(2k + 4 = 30 \iff 2k = 26 \iff k = 13\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel van de lengte van een plant: week \(0\): \(2\) cm, week \(1\): \(5\) cm, week \(2\): \(8\) cm, week \(3\): \(11\) cm. Hoe groeit de plant?",
        opties=[r"constante stijging", r"toenemende stijging", r"afnemende stijging", r"geen stijging"],
        antwoord=0,
        uitleg=r"Elke week komt er precies \(3\) cm bij. Een constante stijging hoort bij een rechte.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie die op een interval constant is, heeft daar een grafiek die evenwijdig loopt met de \(x\)-as.",
        antwoord=True,
        uitleg=r"Constant betekent: dezelfde functiewaarde voor elke \(x\) van het interval, dus een horizontaal stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f\) ligt boven de \(x\)-as voor \(x < -1\), snijdt de \(x\)-as in \(-1\) en in \(3\), en ligt onder de \(x\)-as tussen \(-1\) en \(3\). Voor welke \(x\) is \(f(x) < 0\)?",
        opties=[r"\(]-1, 3[\)", r"\(]-\infty, -1[\)", r"\([-1, 3]\)", r"\(]3, +\infty[\)"],
        antwoord=0,
        uitleg=r"\(f(x) < 0\) waar de grafiek onder de \(x\)-as ligt, zonder de nulwaarden zelf: het open interval \(]-1, 3[\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f\) stijgt tot \(x = 2\), waar \(f(2) = 7\), en daalt daarna. Welke uitspraak is juist?",
        opties=[
            r"\(f\) bereikt een maximum \(7\) in \(x = 2\).",
            r"\(f\) bereikt een minimum \(2\) in \(x = 7\).",
            r"\(f\) heeft een nulwaarde in \(x = 2\).",
            r"\(f\) bereikt een maximum \(2\) in \(x = 7\).",
        ],
        antwoord=0,
        uitleg=r"Het maximum is de functiewaarde \(7\), en het wordt bereikt in \(x = 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als de grafiek van \(f\) een verticale asymptoot \(x = 1\) heeft, dan ligt \(1\) niet in het domein van \(f\).",
        antwoord=True,
        uitleg=r"Bij een verticale asymptoot bestaat de functie niet in die \(x\)-waarde. In het verloopschema staat daar een verticale streep.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het aantal bezoekers \(B(u)\) van een pretpark, \(u\) uur na de opening, stijgt eerst snel en dan steeds trager tot een maximum, en daalt daarna. Wat gebeurt er net voor het maximum?",
        opties=[r"een afnemende stijging", r"een toenemende stijging", r"een toenemende daling", r"een constante daling"],
        antwoord=0,
        uitleg=r"Het aantal stijgt nog, maar steeds trager: de stijging neemt af, tot ze nul is in het maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het bereik van \(f(x) = x^{2}\) is \(\mathbb{R}\).",
        antwoord=False,
        uitleg=r"Een kwadraat is nooit negatief. Het bereik is \([0, +\infty[\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het snijpunt met de \(y\)-as van een functie die een beginwaarde in een situatie beschrijft, zoals \(K(t)\) = kapitaal na \(t\) jaar?",
        opties=[r"het kapitaal op \(t = 0\), het beginkapitaal", r"het kapitaal na één jaar", r"het jaar waarin het kapitaal nul is", r"het grootste kapitaal"],
        antwoord=0,
        uitleg=r"Het snijpunt met de \(y\)-as hoort bij \(t = 0\): de toestand bij de start.",
    ),
]
