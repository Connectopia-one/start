# -*- coding: utf-8 -*-
"""Kansrekenen en de binomiale verdeling.

Het tweede stuk van het onderdeel "Telproblemen, kansrekenen en statistiek"
van fiche G2. Alle leerdoelen hier staan uitdrukkelijk in opgaven mét context,
dus de vragen gaan over dobbelstenen, kaarten, machines en steekproeven.

Deel 1 is de kansrekening met kansbomen, kruistabellen en de wet van Laplace.
Deel 2 is de kansvariabele en de binomiale verdeling.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Laplace?",
        opties=[
            "de kans is het aantal gunstige gedeeld door het aantal mogelijke uitkomsten",
            "de kans is het aantal mogelijke gedeeld door het aantal gunstige uitkomsten",
            "de kans is het aantal gunstige uitkomsten maal het aantal pogingen",
            "de kans is één gedeeld door het aantal gunstige uitkomsten samen",
        ],
        antwoord=0,
        uitleg="Ze geldt alleen als alle uitkomsten even waarschijnlijk zijn, dus bij een eerlijke dobbelsteen of munt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de kans op een even getal met een eerlijke dobbelsteen?",
        opties=["een half", "een derde", "een zesde", "twee derde"],
        antwoord=0,
        uitleg="Drie gunstige uitkomsten van de zes mogelijke.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de kans op een zes met een eerlijke dobbelsteen? Schrijf ze als breuk.",
        antwoord=["1/6"],
        uitleg="Eén gunstige uitkomst van de zes.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kans kan groter zijn dan één.",
        antwoord=False,
        uitleg="Een kans ligt altijd tussen nul en één. Krijg je meer dan één, dan zit er een fout in je redenering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de complementregel voor kansen?",
        opties=[
            "de kans dat iets niet gebeurt is één min de kans dat het wel gebeurt",
            "de kans dat iets niet gebeurt is gelijk aan de kans dat het wel gebeurt",
            "de kans op twee gebeurtenissen samen is de som van de twee kansen",
            "de kans op twee gebeurtenissen samen is het product van de kansen",
        ],
        antwoord=0,
        uitleg="Bij een opgave met minstens of hoogstens scheelt dat vaak veel rekenwerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit twee keer met een munt. Hoe groot is de kans op twee keer kop?",
        opties=["een vierde", "een half", "een derde", "een achtste"],
        antwoord=0,
        uitleg="Een half maal een half, want de twee worpen zijn onafhankelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In een kansboom vermenigvuldig je de kansen op de takken van één pad.",
        antwoord=True,
        uitleg="Verschillende paden die allebei voldoen, tel je daarna op.",
    ),
    dict(
        type="invultekst",
        vraag="De kans op een gebeurtenis is nul komma drie. Hoe groot is de kans dat ze niet gebeurt? Schrijf het getal.",
        antwoord=["0,7", "0.7"],
        uitleg="Eén min nul komma drie, volgens de complementregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorwaardelijke kans?",
        opties=[
            "de kans op A, als je al weet dat B gebeurd is",
            "de kans dat A en B allebei gebeuren",
            "de kans dat A gebeurt maar B niet",
            "de kans dat A gebeurt, of B, of allebei samen",
        ],
        antwoord=0,
        uitleg="Je kijkt dan alleen nog naar de gevallen waarin B optreedt. Dat is één rij of één kolom van de kruistabel.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee gebeurtenissen zijn onafhankelijk als de ene de kans op de andere niet verandert.",
        antwoord=True,
        uitleg="Dan is de kans op allebei samen gewoon het product van de twee kansen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je in een kruistabel?",
        opties=[
            "de aantallen voor elke combinatie van twee kenmerken",
            "de kansen op elk pad van een kansboom",
            "de uitkomsten van één enkele worp met een dobbelsteen",
            "de verwachtingswaarden van twee kansvariabelen",
        ],
        antwoord=0,
        uitleg="De randtotalen geven je dan de gewone kansen, de cellen de kansen op beide kenmerken samen.",
    ),
    dict(
        type="invultekst",
        vraag="Je trekt één kaart uit een spel van tweeënvijftig. Hoe groot is de kans op harten? Schrijf ze als breuk.",
        antwoord=["1/4"],
        uitleg="Dertien harten op tweeënvijftig kaarten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de som van de kansen op alle mogelijke uitkomsten samen?",
        opties=["één", "nul", "honderd", "het aantal uitkomsten"],
        antwoord=0,
        uitleg="Er gebeurt altijd iets, dus samen dekken de uitkomsten de hele kans af.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij heel veel herhalingen komt de relatieve frequentie dicht bij de kans te liggen.",
        antwoord=True,
        uitleg="Dat is net wat een kans in de praktijk betekent. Bij tien worpen kan het nog ver uit elkaar liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de uitkomstenverzameling van een experiment?",
        opties=[
            "de verzameling van alle mogelijke uitkomsten",
            "de verzameling van de gunstige uitkomsten",
            "de verzameling van de bijbehorende kansen",
            "de verzameling van de uitkomsten die je waarnam",
        ],
        antwoord=0,
        uitleg="Bij één worp met een dobbelsteen zijn dat de getallen één tot en met zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer tel je twee kansen bij elkaar op?",
        opties=[
            "als er verschillende paden zijn die allemaal voldoen",
            "als er twee dingen na elkaar moeten gebeuren",
            "als de twee gebeurtenissen onafhankelijk zijn",
            "als je een voorwaardelijke kans moet gaan berekenen",
        ],
        antwoord=0,
        uitleg="Na elkaar betekent vermenigvuldigen. Of-of betekent optellen, op voorwaarde dat de gevallen elkaar uitsluiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee keer een kaart trekken zonder terugleggen geeft twee onafhankelijke gebeurtenissen.",
        antwoord=False,
        uitleg="De eerste kaart verandert wat er nog in het spel zit, dus de tweede kans hangt van de eerste af. Mét terugleggen zijn ze wel onafhankelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de kans op een getal kleiner dan drie met een eerlijke dobbelsteen? Schrijf ze als breuk.",
        antwoord=["1/3"],
        uitleg="Twee gunstige uitkomsten, één en twee, op zes mogelijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een kans gelijk aan nul?",
        opties=[
            "de gebeurtenis kan bij dit experiment niet voorkomen",
            "de gebeurtenis is heel onwaarschijnlijk maar mogelijk",
            "de gebeurtenis komt precies één keer op honderd voor",
            "de kans is nog niet berekend voor deze gebeurtenis",
        ],
        antwoord=0,
        uitleg="Een zeven gooien met een gewone dobbelsteen heeft kans nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een uitkomst en een gebeurtenis?",
        opties=[
            "een gebeurtenis kan uit meerdere uitkomsten bestaan",
            "een uitkomst kan uit meerdere gebeurtenissen bestaan",
            "een uitkomst heeft een kans en een gebeurtenis niet",
            "er is geen verschil tussen die twee begrippen",
        ],
        antwoord=0,
        uitleg="Een even getal gooien is een gebeurtenis die drie uitkomsten omvat: twee, vier en zes.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een kansvariabele?",
        opties=[
            "een grootheid die aan elke uitkomst een getal toekent",
            "de kans op een welbepaalde uitkomst van het experiment",
            "het aantal keer dat je het experiment herhaalt",
            "een getal dat je vrij mag kiezen in de opgave",
        ],
        antwoord=0,
        uitleg="Bij tien worpen met een munt kan de kansvariabele bijvoorbeeld het aantal keer kop zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een discrete en een continue kansvariabele?",
        opties=[
            "een discrete neemt losse waarden aan, een continue elke waarde in een interval",
            "een continue neemt losse waarden aan, een discrete elke waarde in een interval",
            "een discrete hoort bij een eerlijk experiment en een continue niet",
            "een discrete heeft een verwachtingswaarde en een continue niet",
        ],
        antwoord=0,
        uitleg="Het aantal defecte stukken is discreet, de lengte van een volwassene is continu.",
    ),
    dict(
        type="invultekst",
        vraag="Je gooit tien keer met een eerlijke munt. Hoeveel keer kop verwacht je? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="Het aantal pogingen maal de kans per poging, dus tien maal een half.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Bernoulli-experiment heeft precies twee mogelijke uitkomsten.",
        antwoord=True,
        uitleg="Succes of mislukking. Een rij van zulke experimenten na elkaar geeft een binomiale verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een kansvariabele binomiaal verdeeld?",
        opties=[
            "bij een vast aantal onafhankelijke pogingen met telkens dezelfde slaagkans",
            "bij een vast aantal pogingen waarbij de slaagkans telkens weer verandert",
            "bij een onbeperkt aantal pogingen met een heel kleine slaagkans",
            "bij elk experiment waarvan de uitkomsten getallen zijn",
        ],
        antwoord=0,
        uitleg="Drie voorwaarden dus: een vast aantal, onafhankelijk, en een vaste kans. Valt er één weg, dan is de verdeling niet binomiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de verwachtingswaarde van een binomiale verdeling?",
        opties=[
            "het aantal pogingen maal de kans per poging",
            "het aantal pogingen gedeeld door de kans per poging",
            "de kans per poging gedeeld door het aantal pogingen",
            "het aantal pogingen maal één min de kans per poging",
        ],
        antwoord=0,
        uitleg="Bij honderd worpen met kans nul komma twee verwacht je twintig successen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een binomiale verdeling mag de slaagkans van poging tot poging verschillen.",
        antwoord=False,
        uitleg="Dan is ze niet binomiaal. Een trekking zonder terugleggen uit een kleine groep voldoet daarom vaak niet.",
    ),
    dict(
        type="invultekst",
        vraag="Een machine maakt twintig stukken, elk met kans nul komma één op een fout. Hoeveel foute stukken verwacht je? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="Twintig maal nul komma één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de standaardafwijking bij een binomiale verdeling?",
        opties=[
            "de wortel uit het aantal pogingen maal p maal één min p",
            "het aantal pogingen maal p maal één min p, zonder wortel",
            "de wortel uit het aantal pogingen maal de kans p",
            "het aantal pogingen gedeeld door de wortel uit p",
        ],
        antwoord=0,
        uitleg="Onder de wortel staat de variantie. Zij is het grootst als p gelijk is aan een half.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van alle kansen in een kansverdeling is gelijk aan één.",
        antwoord=True,
        uitleg="De kansvariabele neemt zeker één van haar waarden aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de formule voor de kans op precies k successen uit n pogingen?",
        opties=[
            "een binomiaalcoëfficiënt maal p tot de k maal één min p tot de n min k",
            "een binomiaalcoëfficiënt maal p tot de n maal één min p tot de macht k",
            "p tot de k maal één min p tot de n, zonder coëfficiënt ervoor",
            "n maal p tot de k, gedeeld door k faculteit, zonder meer",
        ],
        antwoord=0,
        uitleg="De coëfficiënt telt op hoeveel verschillende volgordes die k successen kunnen hebben.",
    ),
    dict(
        type="invultekst",
        vraag="Uit hoeveel pogingen bestaat één Bernoulli-experiment? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="Eén poging met twee mogelijke uitkomsten. Herhaal je ze n keer, dan krijg je een binomiale verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de verwachtingswaarde in de praktijk?",
        opties=[
            "het gemiddelde dat je op lange termijn zou meten",
            "de uitkomst die het vaakst zal voorkomen",
            "de grootste waarde die de kansvariabele aanneemt",
            "de uitkomst die je met zekerheid zal krijgen",
        ],
        antwoord=0,
        uitleg="Bij één enkel experiment zegt ze niets met zekerheid. Pas over heel veel herhalingen klopt ze gemiddeld.",
    ),
    dict(
        type="waarofniet",
        vraag="De verwachtingswaarde moet zelf een mogelijke uitkomst zijn.",
        antwoord=False,
        uitleg="Het gemiddelde aantal kinderen per gezin is één komma zeven, en zoveel kinderen heeft geen enkel gezin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld is binomiaal verdeeld?",
        opties=[
            "het aantal zessen in vijftig worpen met een dobbelsteen",
            "de lengte van vijftig willekeurige volwassen mensen",
            "het aantal worpen tot je de eerste zes gooit",
            "de som van de ogen bij vijftig worpen samen",
        ],
        antwoord=0,
        uitleg="Vast aantal worpen, telkens dezelfde kans op zes, en de worpen beïnvloeden elkaar niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kansvariabele is continu?",
        opties=[
            "de tijd die een trein te laat is",
            "het aantal reizigers op een trein",
            "het aantal treinen dat te laat is",
            "het spoor waarop de trein aankomt",
        ],
        antwoord=0,
        uitleg="Tijd kan elke waarde in een interval aannemen. Aantallen zijn altijd discreet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere standaardafwijking betekent dat de uitkomsten verder uit elkaar liggen.",
        antwoord=True,
        uitleg="Ze meet hoe sterk de waarden rond de verwachtingswaarde schommelen.",
    ),
    dict(
        type="invultekst",
        vraag="De kans op minstens één succes bereken je als één min de kans op hoeveel successen? Schrijf het getal.",
        antwoord=["0", "nul", "geen"],
        uitleg="Het tegengestelde van minstens één is precies nul. Dat is de complementregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat je bij een binomiale verdeling aan de rekenapp over?",
        opties=[
            "de kansen, de verwachtingswaarde en de standaardafwijking berekenen",
            "beslissen of de verdeling in deze opgave wel echt binomiaal is",
            "de nulhypothese en de alternatieve hypothese opstellen",
            "het resultaat in de context van de opgave uitleggen",
        ],
        antwoord=0,
        uitleg="Het rekenwerk mag de app doen. Beoordelen of het model past en wat het antwoord betekent, blijft jouw werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee binomiale verdelingen hebben dezelfde verwachtingswaarde, maar een verschillende standaardafwijking. Wat betekent dat?",
        opties=[
            "de uitkomsten liggen bij de ene meer verspreid dan bij de andere",
            "de ene verdeling heeft meer mogelijke uitkomsten dan de andere",
            "de ene is binomiaal en de andere eigenlijk niet",
            "de twee verdelingen zijn in feite volledig gelijk",
        ],
        antwoord=0,
        uitleg="Gemiddeld hetzelfde resultaat, maar bij de ene schommelt het sterker van keer tot keer.",
    ),
]
