# -*- coding: utf-8 -*-
"""Limieten, continuïteit en asymptoten.

Het eerste stuk van het grote onderdeel "Limieten en afgeleiden" van de
analysefiche G1. De fiche vraagt hier zowel het formele limietbegrip met de
epsilon-deltadefinitie als het rekenwerk, inclusief de bijzondere gevallen en
de regel van de l'Hôpital.

Deel 1 is het limietbegrip en het rekenen met limieten.
Deel 2 is continuïteit en het verband tussen limieten en asymptoten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(\lim\limits_{x \to a} f(x) = b\)?",
        opties=[
            r"de functiewaarden naderen \(b\) als \(x\) dicht genoeg bij \(a\) komt",
            r"de functiewaarde in \(a\) is precies gelijk aan \(b\)",
            r"de functie bereikt de waarde \(b\) ergens tussen \(a\) en \(b\)",
            r"de grafiek snijdt de rechte \(y = b\) in het punt \(a\)",
        ],
        antwoord=0,
        uitleg=r"Een limiet zegt iets over de buurt van \(a\), niet over \(a\) zelf. De functie "
        r"hoeft daar zelfs niet gedefinieerd te zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de \(\varepsilon\)-\(\delta\)-definitie van een limiet: welk getal is eerst gegeven?",
        opties=[
            r"\(\varepsilon\), de gewenste nauwkeurigheid op de \(y\)-as",
            r"\(\delta\), de toegelaten afstand op de \(x\)-as rond \(a\)",
            r"de waarde \(a\) waar de limiet wordt genomen",
            r"de limietwaarde \(b\) die je wil bereiken",
        ],
        antwoord=0,
        uitleg=r"Iemand daagt je uit met een \(\varepsilon\), en jij moet er een \(\delta\) bij "
        r"vinden. Die volgorde omdraaien maakt de definitie betekenisloos.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{x \to 2} \dfrac{x^{2} - 4}{x - 2}\)? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"Teller en noemer worden allebei \(0\). Ontbind de teller tot \((x-2)(x+2)\) en "
        r"schrap \(x - 2\): er blijft \(x + 2\) over, en dat is \(4\) in \(x = 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie moet in \(a\) gedefinieerd zijn om daar een limiet te hebben.",
        antwoord=False,
        uitleg=r"Net niet: in het voorbeeld hierboven bestaat de functie niet in \(x = 2\), maar de "
        r"limiet bestaat wel. Daar ligt een perforatie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een rationale functie geven teller en noemer allebei \(0\). Wat doe je?",
        opties=[
            "ontbinden en de gemeenschappelijke factor schrappen",
            "meteen besluiten dat de limiet nul moet zijn",
            "meteen besluiten dat de limiet oneindig groot wordt",
            "de teller en de noemer bij elkaar optellen",
        ],
        antwoord=0,
        uitleg=r"\(\dfrac{0}{0}\) is een onbepaaldheid: je weet nog niets. Na het schrappen blijkt "
        r"er een perforatie of een pool te liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een rationale functie is de teller niet \(0\) en de noemer wel. Wat besluit je?",
        opties=[
            r"er ligt een pool, dus de limiet is \(\pm\infty\)",
            "er ligt een perforatie, dus de limiet is een gewoon getal",
            "de limiet is nul, want de noemer wordt heel klein",
            "de limiet bestaat niet en je kan er niets over zeggen",
        ],
        antwoord=0,
        uitleg="Een heel kleine noemer maakt de breuk heel groot. Met een tekenonderzoek links en "
        "rechts bepaal je welk teken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een perforatie is een punt dat op de grafiek ontbreekt, terwijl de limiet er wel bestaat.",
        antwoord=True,
        uitleg="Je tekent er een open bolletje. De functie is er niet gedefinieerd, maar de grafiek "
        "loopt er verder gewoon door.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{x \to +\infty} \dfrac{3x^{2} + 1}{x^{2} - 5}\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"Bij gelijke graad delen de hoogstegraadstermen elkaar: \(\dfrac{3x^{2}}{x^{2}} = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je hebt \(\infty - \infty\) met twee wortels. Welke truc gebruik je?",
        opties=[
            "vermenigvuldigen met de toegevoegde tweeterm",
            "de regel van de l'Hôpital meteen toepassen",
            "beide wortels afzonderlijk naar oneindig laten gaan",
            "de hoogstegraadsterm uit de noemer afzonderen",
        ],
        antwoord=0,
        uitleg=r"\((a-b)(a+b) = a^{2} - b^{2}\), en daarmee verdwijnen de wortels uit de teller.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De regel van de l'Hôpital mag je toepassen op \(\dfrac{2}{0}\).",
        antwoord=False,
        uitleg=r"\(\dfrac{2}{0}\) is geen onbepaaldheid maar een pool: het antwoord is oneindig. "
        r"L'Hôpital geldt alleen bij echte onbepaaldheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke vormen mag je de regel van de l'Hôpital rechtstreeks toepassen?",
        opties=[
            r"\(\dfrac{0}{0}\) en \(\dfrac{\infty}{\infty}\)",
            r"\(\dfrac{0}{0}\) en \(0 \cdot a\)",
            r"\(\infty + \infty\) en \(\dfrac{0}{1}\)",
            "elke breuk met een nul in de noemer",
        ],
        antwoord=0,
        uitleg=r"De andere onbepaaldheden, zoals \(0 \cdot \infty\) of \(\infty - \infty\), moet je "
        r"eerst omvormen tot een van die twee breuken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{x \to +\infty} \dfrac{2x + 1}{x^{2}}\)? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="De noemer groeit sneller dan de teller, dus de breuk kruipt naar nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer bestaat de limiet van een functie in een punt?",
        opties=[
            "als de linkerlimiet en de rechterlimiet gelijk zijn",
            "als de functie in dat punt gedefinieerd is",
            "als de functie in dat punt stijgt of daalt",
            "als de linkerlimiet kleiner is dan de rechterlimiet",
        ],
        antwoord=0,
        uitleg="Verschillen ze, dan maakt de grafiek daar een sprong en bestaat de gewone limiet niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\lim\limits_{x \to 0} \dfrac{1}{x}\) bestaat.",
        antwoord=False,
        uitleg=r"Van links kruipt ze naar \(-\infty\) en van rechts naar \(+\infty\). Die twee zijn "
        r"verschillend, dus de limiet bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de rekenregel voor de limiet van een som?",
        opties=[
            "de limiet van de som is de som van de limieten",
            "de limiet van de som is het product van de limieten",
            "de limiet van de som is de grootste van de limieten",
            "de limiet van de som is de som gedeeld door twee",
        ],
        antwoord=0,
        uitleg="Dat geldt zolang beide limieten bestaan en eindig zijn. Bij oneindig moet je "
        "opletten voor onbepaaldheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaalt het gedrag van een veeltermfunctie op oneindig?",
        opties=[
            "enkel de term met de hoogste graad",
            "enkel de constante term achteraan",
            "de som van al haar coëfficiënten",
            "het aantal nulwaarden dat ze heeft",
        ],
        antwoord=0,
        uitleg=r"Voor heel grote \(x\) verdwijnen de lagere termen in het niet bij de hoogste.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\lim\limits_{x \to 0} \dfrac{1}{x^{2}} = +\infty\).",
        antwoord=True,
        uitleg=r"Een kwadraat is langs beide kanten positief, dus de breuk gaat aan beide zijden "
        r"naar \(+\infty\). Hier bestaat de limiet dus wel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\lim\limits_{x \to 3} (x + 5)\)? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg="De functie is continu, dus je mag gewoon invullen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je neemt de limiet op oneindig van een irrationale functie. Wat is de eerste stap?",
        opties=[
            "de hoogstegraadsterm buiten de wortel afzonderen",
            "de wortel zonder meer gelijkstellen aan oneindig",
            "de regel van de l'Hôpital twee keer toepassen",
            "de teller en de noemer bij elkaar optellen",
        ],
        antwoord=0,
        uitleg=r"Zo haal je de grootste macht uit de wortel, bijvoorbeeld "
        r"\(\sqrt{x^{2}+x} = |x|\sqrt{1 + \tfrac{1}{x}}\), en zie je welke term de limiet bepaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een onbepaaldheid bij het berekenen van een limiet?",
        opties=[
            "een vorm waaruit je de uitkomst nog niet kan afleiden",
            "een limiet die bewezen niet bestaat in dat punt",
            "een functie die in dat punt niet gedefinieerd is",
            "een limiet die oneindig groot blijkt te worden",
        ],
        antwoord=0,
        uitleg=r"\(\dfrac{0}{0}\) kan alles opleveren: een getal, oneindig of niets. Je moet eerst "
        r"herschrijven.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is een functie continu in een punt \(a\)?",
        opties=[
            r"als \(f(a)\) bestaat en gelijk is aan \(\lim\limits_{x \to a} f(x)\)",
            r"als de functie in \(a\) stijgt of in \(a\) daalt",
            r"als de limiet in \(a\) bestaat, wat \(f(a)\) ook is",
            r"als de functie in \(a\) een afgeleide heeft die \(0\) is",
        ],
        antwoord=0,
        uitleg="Drie dingen moeten kloppen: de limiet bestaat, de functiewaarde bestaat, en ze zijn gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent continuïteit op een grafiek?",
        opties=[
            "je kan ze tekenen zonder je pen op te heffen",
            "ze stijgt op haar hele domein zonder onderbreking",
            "ze blijft altijd boven de horizontale as liggen",
            "ze heeft nergens een scherpe knik of een hoekpunt",
        ],
        antwoord=0,
        uitleg=r"Een knik mag wel: \(f(x) = |x|\) is continu in \(0\), maar daar niet afleidbaar.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel verticale asymptoten heeft \(f(x) = \dfrac{1}{x - 3}\)? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Alleen in \(x = 3\) wordt de noemer nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale asymptoot hoort bij een pool van de functie.",
        antwoord=True,
        uitleg=r"In een pool gaat de functiewaarde naar \(\pm\infty\), en dat is precies wat een "
        r"verticale asymptoot beschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de horizontale asymptoot van een functie?",
        opties=[
            r"door \(\lim\limits_{x \to \pm\infty} f(x)\) te berekenen",
            r"door de noemer gelijk te stellen aan \(0\)",
            "door de nulwaarden van de functie te berekenen",
            r"door \(f'(x) = 0\) op te lossen",
        ],
        antwoord=0,
        uitleg="De noemer nulstellen geeft net de verticale asymptoten, niet de horizontale.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke horizontale asymptoot heeft \(f(x) = \dfrac{3x + 1}{x - 2}\)?",
        opties=[
            r"\(y = 3\)",
            r"\(y = 0\)",
            r"\(y = 2\)",
            r"\(x = 2\)",
        ],
        antwoord=0,
        uitleg=r"Teller en noemer hebben dezelfde graad, dus je deelt de hoogste coëfficiënten: "
        r"\(\dfrac{3}{1}\).",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek mag haar horizontale asymptoot nooit snijden.",
        antwoord=False,
        uitleg="Dat mag wel, zelfs meermaals. Alleen op oneindig moet ze er onbeperkt dicht bij "
        "komen. Een verticale asymptoot snijden kan niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"De verticale asymptoot van \(f(x) = \dfrac{1}{x - 3}\) heeft als vergelijking \(x = \) welk getal?",
        antwoord=["3", "drie"],
        uitleg=r"Voor \(x = 3\) wordt de noemer nul en schiet de functie naar oneindig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer heeft een rationale functie een schuine asymptoot?",
        opties=[
            "als de graad van de teller precies één hoger is dan die van de noemer",
            "als de graad van de teller gelijk is aan de graad van de noemer",
            "als de graad van de teller lager is dan de graad van de noemer",
            "als de teller en de noemer allebei de graad twee hebben, precies",
        ],
        antwoord=0,
        uitleg=r"Bij gelijke graad krijg je een horizontale asymptoot, bij een lagere teller is dat "
        r"de \(x\)-as zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie kan aan dezelfde kant tegelijk een horizontale en een schuine asymptoot hebben.",
        antwoord=False,
        uitleg="Allebei beschrijven ze het gedrag op oneindig, en dat kan maar één ding tegelijk "
        "zijn. Aan de andere kant kan het wel anders lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de formules van Cauchy voor een schuine asymptoot: hoe bereken je de richtingscoëfficiënt?",
        opties=[
            r"\(m = \lim\limits_{x \to \infty} \dfrac{f(x)}{x}\)",
            r"\(m = \lim\limits_{x \to \infty} \left(f(x) - x\right)\)",
            r"\(m = \lim\limits_{x \to \infty} f(x)\)",
            r"\(m = f(1)\)",
        ],
        antwoord=0,
        uitleg=r"Daarna vind je het snijpunt met de \(y\)-as als "
        r"\(q = \lim\limits_{x \to \infty} \left(f(x) - m\,x\right)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De schuine asymptoot van \(f(x) = \dfrac{x^{2} + 1}{x}\) is \(y = \) wat? Schrijf het antwoord.",
        antwoord=["x"],
        uitleg=r"Deel uit: \(f(x) = x + \dfrac{1}{x}\). De tweede term kruipt naar nul, dus de "
        r"asymptoot is \(y = x\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de euclidische deling en de schuine asymptoot?",
        opties=[
            "het quotiënt van de deling is de vergelijking van de asymptoot",
            "de rest van de deling is de vergelijking van de asymptoot",
            "de deler van de deling is de vergelijking van de asymptoot",
            "het quotiënt geeft de verticale asymptoten van de functie",
        ],
        antwoord=0,
        uitleg="De rest gedeeld door de noemer kruipt naar nul op oneindig, dus blijft het quotiënt "
        "over als asymptoot.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie die in een punt afleidbaar is, is daar zeker ook continu.",
        antwoord=True,
        uitleg=r"Omgekeerd geldt het niet: \(f(x) = |x|\) is continu in \(0\), maar heeft er een "
        r"knik en dus geen afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke functie is niet continu in \(x = 0\)?",
        opties=[
            r"\(f(x) = \dfrac{1}{x}\)",
            r"\(f(x) = x^{2} - 3\)",
            r"\(f(x) = \sin x\)",
            r"\(f(x) = e^{x}\)",
        ],
        antwoord=0,
        uitleg=r"Die functie bestaat niet in \(0\) en heeft er een verticale asymptoot. De drie "
        r"andere zijn overal continu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op een grafiek als de linker- en de rechterlimiet in een punt verschillen?",
        opties=[
            "een sprong in de grafiek",
            "een gat in de grafiek",
            "een verticale asymptoot",
            "een knik zonder onderbreking",
        ],
        antwoord=0,
        uitleg="Bij een gat zijn de twee limieten net wel gelijk, maar ontbreekt de functiewaarde.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke veeltermfunctie is continu op heel haar domein.",
        antwoord=True,
        uitleg="Er zit geen noemer en geen wortel in, dus er is nergens een pool of een sprong.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel asymptoten heeft een gewone parabool? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg="Ze groeit wel naar oneindig, maar nadert daarbij geen enkele rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe teken je de asymptoten bij een grafiek?",
        opties=[
            "als stippellijnen, want ze horen niet bij de grafiek",
            "als volle lijnen, want ze horen bij de functie",
            "enkel als pijlen aan de rand van het assenstelsel",
            "als een arcering van het gebied rond de grafiek",
        ],
        antwoord=0,
        uitleg="Een asymptoot is een hulplijn die het gedrag beschrijft. Ze is zelf geen deel van "
        "de grafiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is continuïteit een belangrijke eigenschap?",
        opties=[
            "omdat je dan de limiet mag berekenen door gewoon in te vullen",
            "omdat de functie dan overal stijgt of overal daalt",
            "omdat de functie dan zeker geen nulwaarden heeft",
            "omdat de grafiek dan symmetrisch om de oorsprong komt te liggen",
        ],
        antwoord=0,
        uitleg=r"Bij een continue functie is \(\lim\limits_{x \to a} f(x) = f(a)\), en dat maakt het "
        r"rekenwerk eenvoudig.",
    ),
]
