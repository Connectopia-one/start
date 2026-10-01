# -*- coding: utf-8 -*-
"""Een functie aflezen van haar grafiek, en de inverse functie.

Het onderdeel "Grafisch onderzoek" van de analysefiche G1. De fiche somt daar
een lange lijst functiekenmerken op, en vraagt uitdrukkelijk dat je van elke
voorstellingswijze naar elke andere kan overstappen: verwoording, tabel,
grafiek en voorschrift.

Deel 1 zijn de functiekenmerken. Deel 2 is de inverse functie en de spiegeling
om de eerste bissectrice.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van een functie?",
        opties=[
            "alle x-waarden waarvoor de functie bestaat",
            "alle y-waarden die de functie aanneemt",
            "alle x-waarden waar de grafiek stijgt",
            "alle punten waar de grafiek de assen snijdt",
        ],
        antwoord=0,
        uitleg="Het domein ligt op de horizontale as. De verzameling van de functiewaarden heet het bereik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een nulwaarde en een nulpunt?",
        opties=[
            "een nulwaarde is een getal, een nulpunt is een punt op de grafiek",
            "een nulwaarde ligt op de y-as, een nulpunt op de x-as van de grafiek",
            "een nulwaarde hoort bij een stijgende functie, een nulpunt bij een dalende",
            "er is geen verschil, het zijn twee namen voor precies hetzelfde begrip",
        ],
        antwoord=0,
        uitleg="De nulwaarde is de x waarvoor de functie nul wordt. Het nulpunt is het punt met die x en met y gelijk aan nul.",
    ),
    dict(
        type="invultekst",
        vraag="Eén getal hoort niet bij het domein van de functie één gedeeld door x min vijf. Welk getal?",
        antwoord=["5", "vijf"],
        uitleg="Voor x gelijk aan vijf wordt de noemer nul, en delen door nul kan niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bereik van een functie is de verzameling van alle functiewaarden die ze aanneemt.",
        antwoord=True,
        uitleg="Het bereik lees je af op de verticale as: van onder naar boven, zover de grafiek reikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je op een grafiek dat een functie even is?",
        opties=[
            "ze is symmetrisch om de verticale as",
            "ze is symmetrisch om de oorsprong",
            "ze snijdt de verticale as in een even getal",
            "ze heeft een even aantal nulwaarden",
        ],
        antwoord=0,
        uitleg="Even betekent dat de functiewaarde in min x dezelfde is als in x. De grafiek valt dus op zichzelf na spiegeling om de y-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor een functie geldt: de waarde in min x is telkens het tegengestelde van de waarde in x. Wat weet je dan?",
        opties=[
            "ze is oneven en symmetrisch om de oorsprong",
            "ze is even en symmetrisch om de verticale as",
            "ze is strikt dalend op haar hele domein",
            "ze heeft geen enkele nulwaarde in haar domein",
        ],
        antwoord=0,
        uitleg="Dat is net de definitie van een oneven functie. Een halve draai om de oorsprong legt de grafiek op zichzelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek die symmetrisch is om de oorsprong hoort bij een even functie.",
        antwoord=False,
        uitleg="Symmetrie om de oorsprong hoort bij een oneven functie. Even functies zijn symmetrisch om de y-as.",
    ),
    dict(
        type="invultekst",
        vraag="Een sinusgrafiek schommelt tussen min drie en drie, rond de x-as. Wat is haar amplitude? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De amplitude is de afstand van de evenwichtslijn tot de top, dus de helft van het verschil tussen hoogste en laagste waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een buigpunt op een grafiek?",
        opties=[
            "het punt waar hol in bol overgaat",
            "het punt waar stijgen in dalen overgaat",
            "het punt waar de grafiek de x-as snijdt",
            "het laagste punt van de hele grafiek",
        ],
        antwoord=0,
        uitleg="Een buigpunt gaat over de kromming, niet over de richting. Waar stijgen in dalen overgaat, ligt een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag="In een maximum bereikt de functie altijd haar grootste waarde op het hele domein.",
        antwoord=False,
        uitleg="Dat geldt voor een absoluut maximum. Een plaatselijk maximum is alleen de hoogste waarde in zijn eigen omgeving; verderop kan de grafiek nog hoger gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een toenemende stijging?",
        opties=[
            "de grafiek stijgt en wordt daarbij almaar steiler",
            "de grafiek stijgt en wordt daarbij almaar vlakker",
            "de grafiek stijgt eerst en daalt daarna weer",
            "de grafiek stijgt met een vaste helling verder",
        ],
        antwoord=0,
        uitleg="Bij een afnemende stijging gaat de grafiek wel nog omhoog, maar met een kleinere helling. Bij een vaste helling spreek je van lineaire groei.",
    ),
    dict(
        type="invultekst",
        vraag="Een grafiek herhaalt zich precies om de vier eenheden. Wat is haar periode? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="De periode is de kleinste verschuiving waarna het beeld weer hetzelfde is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het praktisch domein van een functie?",
        opties=[
            "het stuk van het domein dat zinvol is in de context",
            "het deel van het domein waar de functie stijgt",
            "het domein nadat je er de nulwaarden uit weglaat",
            "het domein van de afgeleide van die functie",
        ],
        antwoord=0,
        uitleg="Bij een model voor de hoogte van een plant is een negatieve tijd betekenisloos, ook al staat die in het wiskundige domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale rechte mag de grafiek van een functie hoogstens één keer snijden.",
        antwoord=True,
        uitleg="Bij twee snijpunten zouden er voor dezelfde x twee functiewaarden zijn, en dan is het geen functie meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af in een tekenverloop?",
        opties=[
            "waar de functiewaarden positief of negatief zijn",
            "waar de functie stijgt en waar ze juist daalt",
            "waar de grafiek hol is en waar ze juist bol is",
            "hoe snel de functiewaarden op elk stuk veranderen",
        ],
        antwoord=0,
        uitleg="Het tekenverloop gaat over boven of onder de x-as. Stijgen en dalen is het waardeverloop, en dat lees je af uit de afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een functie een horizontale asymptoot heeft?",
        opties=[
            "haar grafiek nadert op oneindig een vaste hoogte",
            "haar grafiek snijdt een horizontale rechte precies één keer",
            "haar grafiek heeft een verticale rechte die ze nooit raakt",
            "haar grafiek stijgt op het hele domein even snel",
        ],
        antwoord=0,
        uitleg="De functiewaarden kruipen dan naar een vaste waarde toe naarmate x naar plus of min oneindig gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke functie heeft minstens één asymptoot.",
        antwoord=False,
        uitleg="Een gewone parabool of een rechte heeft er geen enkele. Asymptoten horen vooral bij rationale, exponentiële en logaritmische functies.",
    ),
    dict(
        type="invultekst",
        vraag="Een grafiek snijdt de x-as in drie punten. Hoeveel nulwaarden heeft de functie? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Elk snijpunt met de x-as hoort bij precies één nulwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij noemt de vier voorstellingswijzen van een functie?",
        opties=[
            "verwoording, tabel, grafiek en voorschrift",
            "verwoording, tekening, formule en getal",
            "domein, bereik, nulwaarden en extrema",
            "tabel, grafiek, afgeleide en primitieve",
        ],
        antwoord=0,
        uitleg="De fiche vraagt dat je van elke voorstellingswijze naar elke andere kan overstappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het gedrag van een functie op oneindig?",
        opties=[
            "wat er met de functiewaarden gebeurt als x heel groot of heel klein wordt",
            "de waarde die de functie precies in het getal oneindig zelf aanneemt",
            "het aantal nulwaarden dat de functie op haar hele domein in totaal heeft",
            "de hoogte van de grafiek aan het einde van haar praktisch domein",
        ],
        antwoord=0,
        uitleg="Oneindig is geen getal, dus de functie heeft daar geen waarde. Je kijkt naar waar de waarden naartoe kruipen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Om welke rechte spiegel je de grafiek van een functie om die van haar inverse te krijgen?",
        opties=[
            "de eerste bissectrice",
            "de verticale as",
            "de horizontale as",
            "de tweede bissectrice",
        ],
        antwoord=0,
        uitleg="Dat werkt alleen in een orthonormaal assenstelsel, waar beide assen dezelfde eenheid hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vergelijking heeft de eerste bissectrice?",
        opties=[
            "y is gelijk aan x",
            "y is gelijk aan min x",
            "y is gelijk aan nul",
            "x is gelijk aan nul",
        ],
        antwoord=0,
        uitleg="Ze deelt het eerste en derde kwadrant doormidden. Min x is de tweede bissectrice.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel keer mag een horizontale rechte de grafiek van een inverteerbare functie hoogstens snijden? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Bij twee snijpunten zouden twee x-waarden dezelfde functiewaarde hebben, en dan weet de inverse niet welke ze moet teruggeven.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafieken van een functie en haar inverse zijn elkaars spiegelbeeld om de rechte y is x.",
        antwoord=True,
        uitleg="Elk punt met coördinaten a en b bij de functie wordt een punt met b en a bij de inverse, en dat is net die spiegeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een functie niet inverteerbaar?",
        opties=[
            "als een horizontale rechte haar grafiek meer dan één keer snijdt",
            "als een verticale rechte haar grafiek meer dan één keer snijdt",
            "als haar grafiek de eerste bissectrice nergens snijdt",
            "als ze op een deel van haar domein negatief wordt",
        ],
        antwoord=0,
        uitleg="Dan hoort dezelfde functiewaarde bij meerdere x-waarden, en de gespiegelde grafiek is geen functie meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de inverse van de exponentiële functie met grondtal a?",
        opties=[
            "de logaritmische functie met grondtal a",
            "de machtsfunctie met exponent a",
            "de exponentiële functie met grondtal min a",
            "de wortelfunctie met wortelexponent a",
        ],
        antwoord=0,
        uitleg="De logaritme geeft net de exponent terug. Daarom zijn hun grafieken elkaars spiegelbeeld om de eerste bissectrice.",
    ),
    dict(
        type="waarofniet",
        vraag="De kwadraatfunctie is inverteerbaar op heel haar domein.",
        antwoord=False,
        uitleg="Twee en min twee hebben hetzelfde kwadraat, dus een horizontale rechte snijdt de parabool twee keer. Pas op de niet-negatieve getallen lukt het wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welk domein beperk je de kwadraatfunctie om ze inverteerbaar te maken?",
        opties=[
            "tot de getallen groter dan of gelijk aan nul",
            "tot de getallen strikt groter dan het getal één",
            "tot de getallen tussen min één en plus één",
            "tot de gehele getallen zonder het getal nul",
        ],
        antwoord=0,
        uitleg="Op die helft is de parabool strikt stijgend, en dan is de vierkantswortel haar inverse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan is de boogsinus de inverse?",
        opties=[
            "van de sinus op een beperkt domein",
            "van de cosinus op haar hele domein",
            "van de tangens op een beperkt domein",
            "van de sinus op haar hele domein",
        ],
        antwoord=0,
        uitleg="De sinus herhaalt zich, dus je moet eerst een stuk kiezen waarop ze strikt stijgt. Pas dan bestaat de inverse.",
    ),
    dict(
        type="waarofniet",
        vraag="Het domein van de inverse functie is het bereik van de oorspronkelijke functie.",
        antwoord=True,
        uitleg="Bij het spiegelen wisselen de assen van rol, dus domein en bereik wisselen ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee functies zijn elkaars inverse op de niet-negatieve getallen?",
        opties=[
            "de kwadraatfunctie en de vierkantswortel",
            "de kwadraatfunctie en de functie min x kwadraat",
            "de vierkantswortel en de functie één op x",
            "de derdemacht en de vierkantswortel",
        ],
        antwoord=0,
        uitleg="Kwadrateren en worteltrekken heffen elkaar daar op. Hun grafieken liggen symmetrisch om de eerste bissectrice.",
    ),
    dict(
        type="invultekst",
        vraag="De inverse van de functie x plus drie is x min een getal. Welk getal?",
        antwoord=["3", "drie"],
        uitleg="Wat de functie erbij doet, haalt de inverse er weer af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het voorschrift van de inverse functie?",
        opties=[
            "x en y verwisselen en dan naar y oplossen",
            "het teken van het hele voorschrift omdraaien",
            "één delen door het voorschrift van de functie",
            "x vervangen door min x in het voorschrift",
        ],
        antwoord=0,
        uitleg="Eén gedeeld door de functie is iets anders dan de inverse functie, ook al lijkt de notatie erop.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke rechte is inverteerbaar.",
        antwoord=False,
        uitleg="Een horizontale rechte geeft aan alle x-waarden dezelfde functiewaarde. Gespiegeld wordt dat een verticale rechte, en dat is geen functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemen we boogsinus, boogcosinus en boogtangens samen?",
        opties=[
            "de cyclometrische functies",
            "de goniometrische functies",
            "de irrationale functies",
            "de periodieke functies",
        ],
        antwoord=0,
        uitleg="Het zijn de inversen van de goniometrische basisfuncties, elk op een beperkt domein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek snijdt de y-as in het punt nul en twee. Wat wordt dat punt op de grafiek van de inverse?",
        opties=[
            "het punt twee en nul, op de x-as",
            "het punt nul en min twee, op de y-as",
            "het punt twee en twee, op de bissectrice",
            "het punt min twee en nul, op de x-as",
        ],
        antwoord=0,
        uitleg="Bij spiegelen om de eerste bissectrice wisselen de twee coördinaten van plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="De inverse van een strikt stijgende functie is zelf ook strikt stijgend.",
        antwoord=True,
        uitleg="Spiegelen om de eerste bissectrice draait de volgorde van de punten niet om, dus de richting blijft behouden.",
    ),
    dict(
        type="invultekst",
        vraag="Neem de functie twee maal x. Welke waarde geeft haar inverse voor het getal tien? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="De functie verdubbelt, dus de inverse halveert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beperkt men het domein van de sinus voor men haar inverse neemt?",
        opties=[
            "omdat ze anders dezelfde waarde oneindig vaak aanneemt",
            "omdat ze anders nergens positieve waarden zou aannemen",
            "omdat haar grafiek anders helemaal geen nulwaarden heeft",
            "omdat haar bereik anders veel te klein zou uitvallen",
        ],
        antwoord=0,
        uitleg="De sinus is periodiek. Zonder beperking zou de boogsinus bij één getal oneindig veel hoeken moeten teruggeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je meteen zeggen over een grafiek die symmetrisch ligt om de eerste bissectrice?",
        opties=[
            "de functie is haar eigen inverse",
            "de functie is even en dus symmetrisch",
            "de functie heeft precies twee nulwaarden",
            "de functie is overal strikt stijgend",
        ],
        antwoord=0,
        uitleg="Spiegelen verandert de grafiek dan niet, dus de inverse heeft hetzelfde voorschrift. Eén gedeeld door x is zo'n functie.",
    ),
]
