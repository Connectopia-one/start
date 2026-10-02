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
        uitleg="Je vergelijkt hoeveel de functiewaarde veranderde met hoeveel x veranderde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het differentiequotiënt van f over het interval van a tot b?",
        opties=["f(b) min f(a), gedeeld door b min a", "f(b) min f(a), vermenigvuldigd met b min a",
                "f(b) plus f(a), gedeeld door twee", "b min a, gedeeld door f(b) min f(a)"],
        antwoord=0,
        uitleg="Bovenaan het verschil in functiewaarde, onderaan het verschil in x. Altijd in die volgorde.",
    ),
    dict(
        type="invultekst",
        vraag="f(2) is 10 en f(6) is 30. Hoeveel is het differentiequotiënt over het interval van 2 tot 6?",
        antwoord=["5", "vijf"],
        uitleg="30 min 10 is 20, gedeeld door 6 min 2 is 4. Dat geeft 5.",
    ),
    dict(
        type="invultekst",
        vraag="f(0) is 8 en f(4) is 0. Hoeveel is het differentiequotiënt over het interval van 0 tot 4?",
        antwoord=["-2", "min 2", "−2"],
        uitleg="0 min 8 is min 8, gedeeld door 4. De functie zakt dus gemiddeld met 2 per eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een negatief differentiequotiënt?",
        opties=["de functie daalt gemiddeld over dat interval", "de grafiek ligt onder de x-as op dat stuk",
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
        uitleg="Het is een gemiddelde over het hele interval. Een auto met een gemiddelde van 50 kilometer per uur heeft misschien stilgestaan en daarna 100 gereden.",
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
        vraag="Een rechte gaat door (1, 2) en (5, 10). Wat is haar richtingscoëfficiënt?",
        opties=["2", "4", "8", "0,5"],
        antwoord=0,
        uitleg="10 min 2 is 8, gedeeld door 5 min 1 is 4. Dat geeft 2.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een rechte is het differentiequotiënt over elk interval hetzelfde.",
        antwoord=True,
        uitleg="Een rechte heeft overal dezelfde helling. Daarom hoef je er maar twee punten van te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt 150 kilometer af in 2 uur. Welk differentiequotiënt hoort daarbij?",
        opties=["75 kilometer per uur", "300 kilometer per uur", "148 kilometer per uur", "2 kilometer per uur"],
        antwoord=0,
        uitleg="Het verschil in afstand gedeeld door het verschil in tijd. Dat is precies de gemiddelde snelheid.",
    ),
    dict(
        type="invultekst",
        vraag="Een bergweg klimt 120 meter over een afstand van 2000 meter. Hoeveel procent bedraagt de gemiddelde helling?",
        antwoord=["6", "6 %", "6 procent"],
        uitleg="120 gedeeld door 2000 is 0,06, dus 6 procent.",
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
        uitleg="Je hebt alleen twee functiewaarden en de bijbehorende x-waarden nodig, en die haal je uit elk van de drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee intervallen geven differentiequotiënten 3 en 7. Wat weet je?",
        opties=["in het tweede interval groeit de functie sneller", "in het tweede interval ligt de grafiek hoger dan links",
                "het tweede interval is langer dan het eerste interval", "de functie daalt in het eerste interval"],
        antwoord=0,
        uitleg="Een groter differentiequotiënt betekent een steilere rechte en dus een snellere gemiddelde groei.",
    ),
    dict(
        type="invultekst",
        vraag="f(x) is 3x plus 1. Hoeveel is het differentiequotiënt over het interval van 0 tot 5?",
        antwoord=["3", "drie"],
        uitleg="f(5) is 16 en f(0) is 1. Het verschil 15 gedeeld door 5 geeft 3, en dat is precies de richtingscoëfficiënt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een stijgende functie is het differentiequotiënt over sommige intervallen negatief.",
        antwoord=False,
        uitleg="Stijgen betekent dat de functiewaarde groter wordt als x groter wordt, dus teller en noemer hebben overal hetzelfde teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een waterton loopt leeg: in 10 minuten gaat de inhoud van 80 naar 20 liter. Wat is het gemiddelde debiet?",
        opties=["6 liter per minuut eruit", "60 liter per minuut eruit", "8 liter per minuut eruit", "2 liter per minuut erin"],
        antwoord=0,
        uitleg="20 min 80 is min 60, gedeeld door 10 is min 6. Het minteken betekent hier dat er water uit gaat.",
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
        vraag="f(1) is 4 en f(3) is 16. Hoeveel is het differentiequotiënt over het interval van 1 tot 3?",
        antwoord=["6", "zes"],
        uitleg="16 min 4 is 12, gedeeld door 3 min 1 is 2. Dat geeft 6.",
    ),
    dict(
        type="invultekst",
        vraag="f(5) is 20 en f(9) is 20. Hoeveel is het differentiequotiënt over het interval van 5 tot 9?",
        antwoord=["0", "nul"],
        uitleg="De functiewaarde is op het einde even groot als bij het begin, dus de teller is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft: bij x is 2 hoort 7 en bij x is 10 hoort 31. Wat is het differentiequotiënt?",
        opties=["3", "24", "8", "0,33"],
        antwoord=0,
        uitleg="31 min 7 is 24, gedeeld door 10 min 2 is 8. Dat geeft 3.",
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
        vraag="Een plant groeide van 12 naar 30 centimeter in 6 weken. Hoeveel groeide ze gemiddeld per week?",
        opties=["3 cm", "18 cm", "5 cm", "2 cm"],
        antwoord=0,
        uitleg="30 min 12 is 18, gedeeld door 6 weken.",
    ),
    dict(
        type="invultekst",
        vraag="Een spaarrekening groeide in 4 jaar van 1000 naar 1200 euro. Hoeveel euro per jaar is dat gemiddeld?",
        antwoord=["50", "50 euro", "vijftig"],
        uitleg="200 euro groei gedeeld door 4 jaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemiddelde snelheid van 0 betekent dat je niet bewogen hebt.",
        antwoord=False,
        uitleg="Het betekent alleen dat je weer op je vertrekpunt staat. Je kan ondertussen een hele ronde gereden hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je deelt een interval in twee helften. Het differentiequotiënt is 2 in de eerste helft en 8 in de tweede. Wat zie je in de grafiek?",
        opties=["de grafiek wordt steiler", "de grafiek wordt vlakker", "de grafiek daalt", "de grafiek is een rechte"],
        antwoord=0,
        uitleg="Een toenemende stijging: elke stap in x levert meer op dan de vorige.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte door twee punten van een grafiek raakt die grafiek in beide punten aan.",
        antwoord=False,
        uitleg="Ze snijdt de grafiek in die twee punten. Haar helling is het gemiddelde over het stuk ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="f(x) is 2x min 5. Hoeveel is het differentiequotiënt over eender welk interval?",
        opties=["2", "-5", "0", "dat hangt van het interval af"],
        antwoord=0,
        uitleg="Bij een eerstegraadsfunctie is het getal voor de x de richtingscoëfficiënt, en die geldt overal.",
    ),
    dict(
        type="invultekst",
        vraag="f(x) is x in het kwadraat. Hoeveel is het differentiequotiënt over het interval van 1 tot 3?",
        antwoord=["4", "vier"],
        uitleg="f(3) is 9 en f(1) is 1. Het verschil 8 gedeeld door 2 geeft 4.",
    ),
    dict(
        type="invultekst",
        vraag="f(x) is x in het kwadraat. Hoeveel is het differentiequotiënt over het interval van 3 tot 5?",
        antwoord=["8", "acht"],
        uitleg="f(5) is 25 en f(3) is 9. Het verschil 16 gedeeld door 2 geeft 8. Verderop groeit dezelfde functie dus sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een kromme hangt het differentiequotiënt af van welk interval je kiest.",
        antwoord=True,
        uitleg="Alleen bij een rechte is het overal hetzelfde. Daarom zeg je bij een kromme er altijd bij over welk interval je rekende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf telde 500 klanten in januari en 2000 in mei. Hoeveel klanten kwamen er gemiddeld per maand bij?",
        opties=["375", "300", "1500", "500"],
        antwoord=0,
        uitleg="1500 klanten erbij over 4 maanden, van januari tot mei.",
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
        vraag="Een grafiek van de temperatuur daalt van 20 naar 5 graden tussen 18 uur en 23 uur. Hoeveel is het differentiequotiënt?",
        opties=["-3 graden per uur", "3 graden per uur", "-15 graden per uur", "-5 graden per uur"],
        antwoord=0,
        uitleg="5 min 20 is min 15, gedeeld door 5 uur. Het minteken hoort erbij, want de temperatuur zakt.",
    ),
    dict(
        type="invultekst",
        vraag="Een tank verliest gemiddeld 4 liter per minuut en bevat nu 100 liter. Hoeveel liter zit er na 15 minuten in?",
        antwoord=["40", "40 liter", "veertig"],
        uitleg="4 maal 15 is 60 liter weg, dus 100 min 60.",
    ),
    dict(
        type="waarofniet",
        vraag="De eenheid van een differentiequotiënt is de eenheid van de functiewaarde per eenheid van x.",
        antwoord=True,
        uitleg="Zo krijg je euro per jaar, graden per uur of liter per minuut. Dat maakt je antwoord meteen leesbaar.",
    ),
]
