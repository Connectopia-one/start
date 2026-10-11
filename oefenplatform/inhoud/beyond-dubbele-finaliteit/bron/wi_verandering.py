# -*- coding: utf-8 -*-
"""Gemiddelde verandering en het differentiequotiënt.

Uit het onderdeel "Grafisch onderzoek" van de bouwsteen Analyse, vakfiche
wiskunde 3 dubbele finaliteit: het differentiequotiënt als gemiddelde
verandering over een interval, zijn grafische betekenis, de
richtingscoëfficiënt als maat voor de helling, en het berekenen ervan vanuit
een tabel, een grafiek of een voorschrift.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat berekent een differentiequotiënt?",
        opties=["de gemiddelde verandering over een interval", "de functiewaarde in één welbepaald punt",
                "de oppervlakte onder de grafiek tot aan b", "het aantal nulwaarden in het interval"],
        antwoord=0,
        uitleg=r"Je vergelijkt hoeveel de functiewaarde veranderde met hoeveel \(x\) veranderde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je het differentiequotiënt van \(f\) over het interval van \(a\) tot \(b\)?",
        opties=[r"\(\dfrac{f(b) - f(a)}{b - a}\)", r"\(\bigl(f(b) - f(a)\bigr) \cdot (b - a)\)",
                r"\(\dfrac{f(b) + f(a)}{2}\)", r"\(\dfrac{b - a}{f(b) - f(a)}\)"],
        antwoord=0,
        uitleg=r"Bovenaan het verschil in functiewaarde, onderaan het verschil in \(x\). Altijd in die volgorde.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(2)\) is \(10\) en \(f(6)\) is \(30\). Hoeveel is het differentiequotiënt over het interval van \(2\) tot \(6\)?",
        antwoord=["5", "vijf"],
        uitleg=r"\(\dfrac{30 - 10}{6 - 2} = \dfrac{20}{4} = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(0)\) is \(8\) en \(f(4)\) is \(0\). Hoeveel is het differentiequotiënt over het interval van \(0\) tot \(4\)?",
        antwoord=["-2", "min 2", "−2"],
        uitleg=r"\(\dfrac{0 - 8}{4 - 0} = \dfrac{-8}{4} = -2\). De functie zakt dus gemiddeld met \(2\) per eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een negatief differentiequotiënt?",
        opties=["de functie daalt gemiddeld over dat interval", r"de grafiek ligt onder de \(x\)-as op dat stuk",
                "de functie is daar nergens gedefinieerd", "het interval loopt van rechts naar links"],
        antwoord=0,
        uitleg="Het teken zegt iets over de richting van de verandering, niet over de ligging van de grafiek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een differentiequotiënt van nul betekent dat de functie op het einde van het interval even hoog zit als bij het begin.",
        antwoord=True,
        uitleg="Daartussen kan ze wel gestegen en weer gedaald zijn. Een gemiddelde verbergt wat er onderweg gebeurde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het differentiequotiënt vertelt je wat er op elk moment binnen het interval gebeurt.",
        antwoord=False,
        uitleg=r"Het is een gemiddelde over het hele interval. Een auto met een gemiddelde van \(50\) kilometer per uur heeft misschien stilgestaan en daarna \(100\) gereden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de grafische betekenis van het differentiequotiënt over een interval?",
        opties=["de richtingscoëfficiënt van de rechte door de twee randpunten", "de hoogte van de grafiek halverwege het interval",
                "de oppervlakte onder de grafiek over dat hele interval", "de afstand tussen de twee randpunten van het interval"],
        antwoord=0,
        uitleg="Je trekt een rechte door het beginpunt en het eindpunt; de steilheid van die rechte is het differentiequotiënt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het getal dat zegt hoe steil een rechte loopt?",
        antwoord=["de richtingscoëfficiënt", "richtingscoëfficiënt", "richtingscoefficient"],
        uitleg="Bij een rechte is die overal dezelfde, dus daar valt de richtingscoëfficiënt samen met het differentiequotiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechte gaat door (\(1\), \(2\)) en (\(5\), \(10\)). Wat is haar richtingscoëfficiënt?",
        opties=[r"\(2\)", r"\(4\)", r"\(8\)", r"\(0{,}5\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{10 - 2}{5 - 1} = \dfrac{8}{4} = 2\).",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een rechte is het differentiequotiënt over elk interval hetzelfde.",
        antwoord=True,
        uitleg="Een rechte heeft overal dezelfde helling. Daarom hoef je er maar twee punten van te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je legt \(150\) kilometer af in \(2\) uur. Welk differentiequotiënt hoort daarbij?",
        opties=[r"\(75\) kilometer per uur", r"\(300\) kilometer per uur", r"\(148\) kilometer per uur", r"\(2\) kilometer per uur"],
        antwoord=0,
        uitleg="Het verschil in afstand gedeeld door het verschil in tijd. Dat is precies de gemiddelde snelheid.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een bergweg klimt \(120\) meter over een afstand van \(2000\) meter. Hoeveel procent bedraagt de gemiddelde helling?",
        antwoord=["6", "6 %", "6 procent"],
        uitleg=r"\(120 : 2000\) is \(0{,}06\), dus \(6\) procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheid hoort bij het differentiequotiënt van het aantal inwoners in functie van het jaartal?",
        opties=["inwoners per jaar", "jaren per inwoner", "inwoners", "jaren"],
        antwoord=0,
        uitleg="De eenheid bovenaan de breuk gedeeld door de eenheid onderaan. Dat maakt je antwoord meteen leesbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een differentiequotiënt berekenen uit een tabel, uit een grafiek en uit een voorschrift.",
        antwoord=True,
        uitleg=r"Je hebt alleen twee functiewaarden en de bijbehorende \(x\)-waarden nodig, en die haal je uit elk van de drie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee intervallen geven differentiequotiënten \(3\) en \(7\). Wat weet je?",
        opties=["in het tweede interval groeit de functie sneller", "in het tweede interval ligt de grafiek hoger dan links",
                "het tweede interval is langer dan het eerste interval", "de functie daalt in het eerste interval"],
        antwoord=0,
        uitleg="Een groter differentiequotiënt betekent een steilere rechte en dus een snellere gemiddelde groei.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(x) = 3x + 1\). Hoeveel is het differentiequotiënt over het interval van \(0\) tot \(5\)?",
        antwoord=["3", "drie"],
        uitleg=r"\(f(5)\) is \(16\) en \(f(0)\) is \(1\). Het verschil \(15 : 5\) geeft \(3\), en dat is precies de richtingscoëfficiënt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een stijgende functie is het differentiequotiënt over sommige intervallen negatief.",
        antwoord=False,
        uitleg=r"Stijgen betekent dat de functiewaarde groter wordt als \(x\) groter wordt, dus teller en noemer hebben overal hetzelfde teken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een waterton loopt leeg: in \(10\) minuten gaat de inhoud van \(80\) naar \(20\) liter. Wat is het gemiddelde debiet?",
        opties=[r"\(6\) liter per minuut eruit", r"\(60\) liter per minuut eruit", r"\(8\) liter per minuut eruit", r"\(2\) liter per minuut erin"],
        antwoord=0,
        uitleg=r"\(\dfrac{20 - 80}{10} = \dfrac{-60}{10} = -6\). Het minteken betekent hier dat er water uit gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groter differentiequotiënt betekent altijd een hogere functiewaarde.",
        antwoord=False,
        uitleg="Het zegt alleen iets over de verandering. Een functie kan snel groeien en toch nog laag liggen.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"\(f(1)\) is \(4\) en \(f(3)\) is \(16\). Hoeveel is het differentiequotiënt over het interval van \(1\) tot \(3\)?",
        antwoord=["6", "zes"],
        uitleg=r"\(\dfrac{16 - 4}{3 - 1} = \dfrac{12}{2} = 6\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(5)\) is \(20\) en \(f(9)\) is \(20\). Hoeveel is het differentiequotiënt over het interval van \(5\) tot \(9\)?",
        antwoord=["0", "nul"],
        uitleg="De functiewaarde is op het einde even groot als bij het begin, dus de teller is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel geeft: bij \(x = 2\) hoort \(7\) en bij \(x = 10\) hoort \(31\). Wat is het differentiequotiënt?",
        opties=[r"\(3\)", r"\(24\)", r"\(8\)", r"\(0{,}33\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{31 - 7}{10 - 2} = \dfrac{24}{8} = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het berekenen van een differentiequotiënt mag je teller en noemer omdraaien.",
        antwoord=False,
        uitleg="Dan krijg je het omgekeerde getal, en dat betekent iets anders. Boven staat altijd het verschil in functiewaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee grafieken lopen over hetzelfde interval, de ene steiler dan de andere. Wat weet je over hun differentiequotiënten?",
        opties=["de steilste heeft het grootste differentiequotiënt", "ze zijn gelijk",
                "de steilste heeft het kleinste", "dat kan je niet zeggen"],
        antwoord=0,
        uitleg="Steilheid en differentiequotiënt zijn hetzelfde verhaal: hoe steiler, hoe groter het getal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een plant groeide van \(12\) naar \(30\) centimeter in \(6\) weken. Hoeveel groeide ze gemiddeld per week?",
        opties=[r"\(3\) cm", r"\(18\) cm", r"\(5\) cm", r"\(2\) cm"],
        antwoord=0,
        uitleg=r"\(\dfrac{30 - 12}{6} = 3\) centimeter per week.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een spaarrekening groeide in \(4\) jaar van \(1000\) naar \(1200\) euro. Hoeveel euro per jaar is dat gemiddeld?",
        antwoord=["50", "50 euro", "vijftig"],
        uitleg=r"\(\dfrac{1200 - 1000}{4} = 50\) euro per jaar.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een gemiddelde snelheid van \(0\) betekent dat je niet bewogen hebt.",
        antwoord=False,
        uitleg="Het betekent alleen dat je weer op je vertrekpunt staat. Je kan ondertussen een hele ronde gereden hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je deelt een interval in twee helften. Het differentiequotiënt is \(2\) in de eerste helft en \(8\) in de tweede. Wat zie je in de grafiek?",
        opties=["de grafiek wordt steiler", "de grafiek wordt vlakker", "de grafiek daalt", "de grafiek is een rechte"],
        antwoord=0,
        uitleg=r"Een toenemende stijging: elke stap in \(x\) levert meer op dan de vorige.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte door twee punten van een grafiek raakt die grafiek in beide punten aan.",
        antwoord=False,
        uitleg="Ze snijdt de grafiek in die twee punten. Haar helling is het gemiddelde over het stuk ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f(x) = 2x - 5\). Hoeveel is het differentiequotiënt over eender welk interval?",
        opties=[r"\(2\)", r"\(-5\)", r"\(0\)", "dat hangt van het interval af"],
        antwoord=0,
        uitleg=r"Bij een eerstegraadsfunctie is het getal voor de \(x\) de richtingscoëfficiënt, en die geldt overal.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(x)\) is \(x\) in het kwadraat. Hoeveel is het differentiequotiënt over het interval van \(1\) tot \(3\)?",
        antwoord=["4", "vier"],
        uitleg=r"\(f(3)\) is \(9\) en \(f(1)\) is \(1\). Het verschil \(8 : 2\) geeft \(4\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f(x)\) is \(x\) in het kwadraat. Hoeveel is het differentiequotiënt over het interval van \(3\) tot \(5\)?",
        antwoord=["8", "acht"],
        uitleg=r"\(f(5)\) is \(25\) en \(f(3)\) is \(9\). Het verschil \(16 : 2\) geeft \(8\). Verderop groeit dezelfde functie dus sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een kromme hangt het differentiequotiënt af van welk interval je kiest.",
        antwoord=True,
        uitleg="Alleen bij een rechte is het overal hetzelfde. Daarom zeg je bij een kromme er altijd bij over welk interval je rekende.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bedrijf telde \(500\) klanten in januari en \(2000\) in mei. Hoeveel klanten kwamen er gemiddeld per maand bij?",
        opties=[r"\(375\)", r"\(300\)", r"\(1500\)", r"\(500\)"],
        antwoord=0,
        uitleg=r"\(1500\) klanten erbij over \(4\) maanden, van januari tot mei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt men gemiddelde verandering en niet gewoon verandering?",
        opties=["omdat ze over een heel interval uitgesmeerd is", "omdat ze altijd klein is",
                "omdat ze altijd positief is", "omdat er twee functies zijn"],
        antwoord=0,
        uitleg="Binnen het interval kan het sneller en trager gegaan zijn; het differentiequotiënt vlakt dat uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan twee differentiequotiënten vergelijken door naar de steilheid van hun rechten te kijken.",
        antwoord=True,
        uitleg="Dat is de grafische manier. De rekenkundige manier is gewoon de twee getallen naast elkaar leggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een grafiek van de temperatuur daalt van \(20\) naar \(5\) graden tussen \(18\) uur en \(23\) uur. Hoeveel is het differentiequotiënt?",
        opties=[r"\(-3\) graden per uur", r"\(3\) graden per uur", r"\(-15\) graden per uur", r"\(-5\) graden per uur"],
        antwoord=0,
        uitleg=r"\(\dfrac{5 - 20}{5} = -3\) graden per uur. Het minteken hoort erbij, want de temperatuur zakt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een tank verliest gemiddeld \(4\) liter per minuut en bevat nu \(100\) liter. Hoeveel liter zit er na \(15\) minuten in?",
        antwoord=["40", "40 liter", "veertig"],
        uitleg=r"\(4 \cdot 15\) is \(60\) liter weg, dus \(100\) min \(60\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De eenheid van een differentiequotiënt is de eenheid van de functiewaarde per eenheid van \(x\).",
        antwoord=True,
        uitleg="Zo krijg je euro per jaar, graden per uur of liter per minuut. Dat maakt je antwoord meteen leesbaar.",
    ),
]
