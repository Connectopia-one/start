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
        vraag="Wat betekent: de limiet van f voor x naar a is b?",
        opties=[
            "de functiewaarden naderen b als x dicht genoeg bij a komt",
            "de functiewaarde in a is precies gelijk aan het getal b",
            "de functie bereikt de waarde b ergens tussen a en b",
            "de grafiek snijdt de rechte y is b in het punt a",
        ],
        antwoord=0,
        uitleg="Een limiet zegt iets over de buurt van a, niet over a zelf. De functie hoeft daar zelfs niet gedefinieerd te zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de epsilon-deltadefinitie van een limiet: welk getal is eerst gegeven?",
        opties=[
            "epsilon, de gewenste nauwkeurigheid op de y-as",
            "delta, de toegelaten afstand op de x-as rond a",
            "de waarde a waar de limiet wordt genomen",
            "de limietwaarde b die je wil bereiken",
        ],
        antwoord=0,
        uitleg="Iemand daagt je uit met een epsilon, en jij moet er een delta bij vinden. Die volgorde omdraaien maakt de definitie betekenisloos.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de limiet voor x naar twee van x kwadraat min vier, gedeeld door x min twee? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Teller en noemer worden allebei nul. Ontbind de teller en schrap x min twee: er blijft x plus twee over, en dat is vier in twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie moet in a gedefinieerd zijn om daar een limiet te hebben.",
        antwoord=False,
        uitleg="Net niet: in het voorbeeld hierboven bestaat de functie niet in twee, maar de limiet bestaat wel. Daar ligt een perforatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een rationale functie geven teller en noemer allebei nul. Wat doe je?",
        opties=[
            "ontbinden en de gemeenschappelijke factor schrappen",
            "meteen besluiten dat de limiet nul moet zijn",
            "meteen besluiten dat de limiet oneindig groot wordt",
            "de teller en de noemer bij elkaar optellen",
        ],
        antwoord=0,
        uitleg="Nul gedeeld door nul is een onbepaaldheid: je weet nog niets. Na het schrappen blijkt er een perforatie of een pool te liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een rationale functie is de teller niet nul en de noemer wel. Wat besluit je?",
        opties=[
            "er ligt een pool, dus de limiet is plus of min oneindig",
            "er ligt een perforatie, dus de limiet is een gewoon getal",
            "de limiet is nul, want de noemer wordt heel klein",
            "de limiet bestaat niet en je kan er niets over zeggen",
        ],
        antwoord=0,
        uitleg="Een heel kleine noemer maakt de breuk heel groot. Met een tekenonderzoek links en rechts bepaal je welk teken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een perforatie is een punt dat op de grafiek ontbreekt, terwijl de limiet er wel bestaat.",
        antwoord=True,
        uitleg="Je tekent er een open bolletje. De functie is er niet gedefinieerd, maar de grafiek loopt er verder gewoon door.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de limiet voor x naar plus oneindig van drie x kwadraat plus één, gedeeld door x kwadraat min vijf? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="Bij gelijke graad delen de hoogstegraadstermen elkaar: drie x kwadraat op x kwadraat is drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt oneindig min oneindig met twee wortels. Welke truc gebruik je?",
        opties=[
            "vermenigvuldigen met de toegevoegde tweeterm",
            "de regel van de l'Hôpital meteen toepassen",
            "beide wortels afzonderlijk naar oneindig laten gaan",
            "de hoogstegraadsterm uit de noemer afzonderen",
        ],
        antwoord=0,
        uitleg="Het verschil maal de som geeft het verschil van de kwadraten, en daarmee verdwijnen de wortels uit de teller.",
    ),
    dict(
        type="waarofniet",
        vraag="De regel van de l'Hôpital mag je toepassen op twee gedeeld door nul.",
        antwoord=False,
        uitleg="Twee gedeeld door nul is geen onbepaaldheid maar een pool: het antwoord is oneindig. L'Hôpital geldt alleen bij echte onbepaaldheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke vormen mag je de regel van de l'Hôpital rechtstreeks toepassen?",
        opties=[
            "nul op nul en oneindig op oneindig",
            "nul op nul en nul maal een getal",
            "oneindig plus oneindig en nul op één",
            "elke breuk met een nul in de noemer",
        ],
        antwoord=0,
        uitleg="De andere onbepaaldheden, zoals nul maal oneindig of oneindig min oneindig, moet je eerst omvormen tot een van die twee breuken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de limiet voor x naar plus oneindig van twee x plus één, gedeeld door x kwadraat? Schrijf het getal.",
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
        vraag="De limiet voor x naar nul van één gedeeld door x bestaat.",
        antwoord=False,
        uitleg="Van links kruipt ze naar min oneindig en van rechts naar plus oneindig. Die twee zijn verschillend, dus de limiet bestaat niet.",
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
        uitleg="Dat geldt zolang beide limieten bestaan en eindig zijn. Bij oneindig moet je opletten voor onbepaaldheden.",
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
        uitleg="Voor heel grote x verdwijnen de lagere termen in het niet bij de hoogste.",
    ),
    dict(
        type="waarofniet",
        vraag="De limiet voor x naar nul van één gedeeld door x kwadraat is plus oneindig.",
        antwoord=True,
        uitleg="Een kwadraat is langs beide kanten positief, dus de breuk gaat aan beide zijden naar plus oneindig. Hier bestaat de limiet dus wel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de limiet voor x naar drie van x plus vijf? Schrijf het getal.",
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
        uitleg="Zo haal je de grootste macht uit de wortel en zie je meteen welke term de limiet bepaalt.",
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
        uitleg="Nul op nul kan alles opleveren: een getal, oneindig of niets. Je moet eerst herschrijven.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een functie continu in een punt a?",
        opties=[
            "als de functiewaarde in a bestaat en gelijk is aan de limiet daar",
            "als de functie in a stijgt of in a daalt",
            "als de limiet in a bestaat, wat de functiewaarde daar ook is",
            "als de functie in a een afgeleide heeft die nul is",
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
        uitleg="Een knik mag wel: de absolute waarde is continu in nul, maar daar niet afleidbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel verticale asymptoten heeft één gedeeld door x min drie? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Alleen in x gelijk aan drie wordt de noemer nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale asymptoot hoort bij een pool van de functie.",
        antwoord=True,
        uitleg="In een pool gaat de functiewaarde naar plus of min oneindig, en dat is precies wat een verticale asymptoot beschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de horizontale asymptoot van een functie?",
        opties=[
            "door de limiet op plus en min oneindig te berekenen",
            "door de noemer gelijk te stellen aan het getal nul",
            "door de nulwaarden van de functie te berekenen",
            "door de afgeleide gelijk te stellen aan het getal nul",
        ],
        antwoord=0,
        uitleg="De noemer nulstellen geeft net de verticale asymptoten, niet de horizontale.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke horizontale asymptoot heeft drie x plus één, gedeeld door x min twee?",
        opties=[
            "de rechte y is drie",
            "de rechte y is nul",
            "de rechte y is twee",
            "de rechte x is twee",
        ],
        antwoord=0,
        uitleg="Teller en noemer hebben dezelfde graad, dus je deelt de hoogste coëfficiënten: drie op één.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek mag haar horizontale asymptoot nooit snijden.",
        antwoord=False,
        uitleg="Dat mag wel, zelfs meermaals. Alleen op oneindig moet ze er onbeperkt dicht bij komen. Een verticale asymptoot snijden kan niet.",
    ),
    dict(
        type="invultekst",
        vraag="De verticale asymptoot van één gedeeld door x min drie heeft als vergelijking x is een getal. Welk getal?",
        antwoord=["3", "drie"],
        uitleg="Voor x gelijk aan drie wordt de noemer nul en schiet de functie naar oneindig.",
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
        uitleg="Bij gelijke graad krijg je een horizontale asymptoot, bij een lagere teller is dat de x-as zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie kan aan dezelfde kant tegelijk een horizontale en een schuine asymptoot hebben.",
        antwoord=False,
        uitleg="Allebei beschrijven ze het gedrag op oneindig, en dat kan maar één ding tegelijk zijn. Aan de andere kant kan het wel anders lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de formules van Cauchy voor een schuine asymptoot: hoe bereken je de richtingscoëfficiënt?",
        opties=[
            "als de limiet op oneindig van f van x gedeeld door x",
            "als de limiet op oneindig van f van x min het getal x",
            "als de limiet op oneindig van f van x zelf",
            "als de functiewaarde van f in het getal één",
        ],
        antwoord=0,
        uitleg="Daarna vind je het snijpunt met de y-as als de limiet van f van x min die richtingscoëfficiënt maal x.",
    ),
    dict(
        type="invultekst",
        vraag="De schuine asymptoot van x kwadraat plus één, gedeeld door x, is y is gelijk aan wat? Schrijf het antwoord.",
        antwoord=["x"],
        uitleg="Deel uit: je krijgt x plus één op x. De tweede term kruipt naar nul, dus de asymptoot is de rechte y is x.",
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
        uitleg="De rest gedeeld door de noemer kruipt naar nul op oneindig, dus blijft het quotiënt over als asymptoot.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie die in een punt afleidbaar is, is daar zeker ook continu.",
        antwoord=True,
        uitleg="Omgekeerd geldt het niet: de absolute waarde is continu in nul, maar heeft er een knik en dus geen afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke functie is niet continu in nul?",
        opties=[
            "één gedeeld door x",
            "x kwadraat min drie",
            "de sinus van x",
            "e tot de macht x",
        ],
        antwoord=0,
        uitleg="Die functie bestaat niet in nul en heeft er een verticale asymptoot. De drie andere zijn overal continu.",
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
        uitleg="Een asymptoot is een hulplijn die het gedrag beschrijft. Ze is zelf geen deel van de grafiek.",
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
        uitleg="Bij een continue functie valt de limiet samen met de functiewaarde, en dat maakt het rekenwerk eenvoudig.",
    ),
]
