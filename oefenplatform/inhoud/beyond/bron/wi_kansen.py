# -*- coding: utf-8 -*-
"""Kansrekenen en de binomiale verdeling.

Het tweede stuk van het onderdeel "Telproblemen, kansrekenen en statistiek"
van fiche G2. Alle leerdoelen hier staan uitdrukkelijk in opgaven met context,
dus de vragen gaan over dobbelstenen, kaarten, machines en steekproeven.

Deel 1 is de kansrekening met kansbomen, kruistabellen en de wet van Laplace.
Deel 2 is de kansvariabele en de binomiale verdeling.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Welke formule is de wet van Laplace?",
        opties=[
            r"\(P(A) = \dfrac{\text{aantal gunstige uitkomsten}}{\text{aantal mogelijke uitkomsten}}\)",
            r"\(P(A) = \dfrac{\text{aantal mogelijke uitkomsten}}{\text{aantal gunstige uitkomsten}}\)",
            r"\(P(A) = \text{aantal gunstige uitkomsten} \cdot \text{aantal pogingen}\)",
            r"\(P(A) = \dfrac{1}{\text{aantal gunstige uitkomsten}}\)",
        ],
        antwoord=0,
        uitleg=r"Ze geldt alleen als alle uitkomsten even waarschijnlijk zijn, dus bij een eerlijke dobbelsteen of munt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit met een eerlijke dobbelsteen. Hoe groot is \(P(\text{even getal})\)?",
        opties=[r"\(\tfrac{1}{2}\)", r"\(\tfrac{1}{3}\)", r"\(\tfrac{1}{6}\)", r"\(\tfrac{2}{3}\)"],
        antwoord=0,
        uitleg=r"Drie gunstige uitkomsten van de zes mogelijke, dus \(\tfrac{3}{6} = \tfrac{1}{2}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe groot is \(P(6)\) bij een eerlijke dobbelsteen? Schrijf ze als breuk.",
        antwoord=["1/6"],
        uitleg=r"Eén gunstige uitkomst van de zes, dus \(P(6) = \tfrac{1}{6}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een kans kan groter zijn dan \(1\).",
        antwoord=False,
        uitleg=r"Er geldt altijd \(0 \le P(A) \le 1\). Krijg je meer dan \(1\), dan zit er een fout in je redenering.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule is de complementregel?",
        opties=[
            r"\(P(\overline{A}) = 1 - P(A)\)",
            r"\(P(\overline{A}) = P(A)\)",
            r"\(P(\overline{A}) = P(A) - 1\)",
            r"\(P(\overline{A}) = \dfrac{1}{P(A)}\)",
        ],
        antwoord=0,
        uitleg=r"Bij een opgave met minstens of hoogstens scheelt dat vaak veel rekenwerk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je gooit twee keer met een munt. Hoe groot is de kans op twee keer kop?",
        opties=[r"\(\tfrac{1}{4}\)", r"\(\tfrac{1}{2}\)", r"\(\tfrac{1}{3}\)", r"\(\tfrac{1}{8}\)"],
        antwoord=0,
        uitleg=r"De twee worpen zijn onafhankelijk, dus \(\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een kansboom vermenigvuldig je de kansen op de takken van één pad.",
        antwoord=True,
        uitleg=r"Verschillende paden die allebei voldoen, tel je daarna op.",
    ),
    dict(
        type="invultekst",
        vraag=r"Er geldt \(P(A) = 0{,}3\). Bereken \(P(\overline{A})\). Schrijf het getal.",
        antwoord=["0,7", "0.7"],
        uitleg=r"Volgens de complementregel is \(P(\overline{A}) = 1 - 0{,}3 = 0{,}7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule hoort bij de voorwaardelijke kans \(P(A \mid B)\)?",
        opties=[
            r"\(P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}\)",
            r"\(P(A \mid B) = \dfrac{P(A \cap B)}{P(A)}\)",
            r"\(P(A \mid B) = P(A) \cdot P(B)\)",
            r"\(P(A \mid B) = P(A) - P(B)\)",
        ],
        antwoord=0,
        uitleg=r"Je kijkt dan alleen nog naar de gevallen waarin \(B\) optreedt. Dat is één rij of één kolom van de kruistabel.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(A\) en \(B\) onafhankelijk zijn, dan geldt \(P(A \cap B) = P(A) \cdot P(B)\).",
        antwoord=True,
        uitleg=r"Onafhankelijk betekent net dat de ene de kans op de andere niet verandert, dus \(P(A \mid B) = P(A)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zet je in een kruistabel?",
        opties=[
            r"de aantallen voor elke combinatie van twee kenmerken",
            r"de kansen op elk pad van een kansboom",
            r"de uitkomsten van één enkele worp met een dobbelsteen",
            r"de verwachtingswaarden van twee kansvariabelen",
        ],
        antwoord=0,
        uitleg=r"De randtotalen geven je dan \(P(A)\) en \(P(B)\), de cellen geven je \(P(A \cap B)\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Je trekt één kaart uit een spel van \(52\). Hoe groot is \(P(\text{harten})\)? Schrijf ze als breuk.",
        antwoord=["1/4"],
        uitleg=r"Dertien harten op tweeënvijftig kaarten, dus \(\tfrac{13}{52} = \tfrac{1}{4}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is de som van de kansen op alle mogelijke uitkomsten samen?",
        opties=[r"\(1\)", r"\(0\)", r"\(100\)", r"het aantal uitkomsten"],
        antwoord=0,
        uitleg=r"Er gebeurt altijd iets, dus samen dekken de uitkomsten de hele kans af.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij heel veel herhalingen komt de relatieve frequentie dicht bij de kans te liggen.",
        antwoord=True,
        uitleg=r"Dat is net wat een kans in de praktijk betekent. Bij tien worpen kan het nog ver uit elkaar liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de uitkomstenverzameling \(\Omega\) van een experiment?",
        opties=[
            r"de verzameling van alle mogelijke uitkomsten",
            r"de verzameling van de gunstige uitkomsten",
            r"de verzameling van de bijbehorende kansen",
            r"de verzameling van de uitkomsten die je waarnam",
        ],
        antwoord=0,
        uitleg=r"Bij één worp met een dobbelsteen is \(\Omega = \{1, 2, 3, 4, 5, 6\}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de algemene somregel voor \(P(A \cup B)\)?",
        opties=[
            r"\(P(A) + P(B) - P(A \cap B)\)",
            r"\(P(A) + P(B) + P(A \cap B)\)",
            r"\(P(A) \cdot P(B) - P(A \cap B)\)",
            r"\(P(A) + P(B)\)",
        ],
        antwoord=0,
        uitleg=r"Sluiten \(A\) en \(B\) elkaar uit, dan is \(P(A \cap B) = 0\) en blijft gewoon \(P(A) + P(B)\) over.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee keer een kaart trekken zonder terugleggen geeft twee onafhankelijke gebeurtenissen.",
        antwoord=False,
        uitleg=r"De eerste kaart verandert wat er nog in het spel zit, dus de tweede kans hangt van de eerste af. Mét terugleggen zijn ze wel onafhankelijk.",
    ),
    dict(
        type="invultekst",
        vraag=r"In een klas van \(25\) leerlingen doen er \(10\) aan sport, en \(4\) van die tien spelen voetbal. Bereken \(P(\text{voetbal} \mid \text{sport})\). Schrijf ze als breuk.",
        antwoord=["2/5", "4/10", "0,4", "0.4"],
        uitleg=r"Je deelt door het aantal sporters, niet door \(25\): \(\dfrac{4}{10} = \tfrac{2}{5}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(P(A) = 0\)?",
        opties=[
            r"de gebeurtenis kan bij dit experiment niet voorkomen",
            r"de gebeurtenis is heel onwaarschijnlijk maar mogelijk",
            r"de gebeurtenis komt precies één keer op honderd voor",
            r"de kans is nog niet berekend voor deze gebeurtenis",
        ],
        antwoord=0,
        uitleg=r"Een zeven gooien met een gewone dobbelsteen heeft kans nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen een uitkomst en een gebeurtenis?",
        opties=[
            r"een gebeurtenis kan uit meerdere uitkomsten bestaan",
            r"een uitkomst kan uit meerdere gebeurtenissen bestaan",
            r"een uitkomst heeft een kans en een gebeurtenis niet",
            r"er is geen verschil tussen die twee begrippen",
        ],
        antwoord=0,
        uitleg=r"Een even getal gooien is een gebeurtenis met drie uitkomsten: \(\{2, 4, 6\}\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is een kansvariabele \(X\)?",
        opties=[
            r"een grootheid die aan elke uitkomst een getal toekent",
            r"de kans op een welbepaalde uitkomst van het experiment",
            r"het aantal keer dat je het experiment herhaalt",
            r"een getal dat je vrij mag kiezen in de opgave",
        ],
        antwoord=0,
        uitleg=r"Bij tien worpen met een munt kan \(X\) bijvoorbeeld het aantal keer kop zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verschil tussen een discrete en een continue kansvariabele?",
        opties=[
            r"een discrete neemt losse waarden aan, een continue elke waarde in een interval",
            r"een continue neemt losse waarden aan, een discrete elke waarde in een interval",
            r"een discrete hoort bij een eerlijk experiment en een continue niet",
            r"een discrete heeft een verwachtingswaarde en een continue niet",
        ],
        antwoord=0,
        uitleg=r"Het aantal defecte stukken is discreet, de lengte van een volwassene is continu.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je gooit \(10\) keer met een eerlijke munt en \(X\) is het aantal keer kop. Bereken \(E(X)\). Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"Er geldt \(E(X) = n \cdot p = 10 \cdot \tfrac{1}{2} = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een Bernoulli-experiment heeft precies twee mogelijke uitkomsten.",
        antwoord=True,
        uitleg=r"Succes of mislukking. Een rij van \(n\) zulke experimenten na elkaar geeft een binomiale verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer is \(X\) binomiaal verdeeld, dus \(X \sim \text{Bin}(n, p)\)?",
        opties=[
            r"bij een vast aantal onafhankelijke pogingen met telkens dezelfde slaagkans",
            r"bij een vast aantal pogingen waarbij de slaagkans telkens weer verandert",
            r"bij een onbeperkt aantal pogingen met een heel kleine slaagkans",
            r"bij elk experiment waarvan de uitkomsten getallen zijn",
        ],
        antwoord=0,
        uitleg=r"Drie voorwaarden dus: een vaste \(n\), onafhankelijk, en een vaste \(p\). Valt er één weg, dan is de verdeling niet binomiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule geeft de verwachtingswaarde van een binomiale verdeling?",
        opties=[
            r"\(E(X) = n \cdot p\)",
            r"\(E(X) = \dfrac{n}{p}\)",
            r"\(E(X) = \dfrac{p}{n}\)",
            r"\(E(X) = n \cdot (1 - p)\)",
        ],
        antwoord=0,
        uitleg=r"Bij \(n = 100\) en \(p = 0{,}2\) verwacht je \(E(X) = 20\) successen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een binomiale verdeling mag de slaagkans \(p\) van poging tot poging verschillen.",
        antwoord=False,
        uitleg=r"Dan is ze niet binomiaal. Een trekking zonder terugleggen uit een kleine groep voldoet daarom vaak niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een machine maakt \(20\) stukken, elk met kans \(p = 0{,}1\) op een fout. Bereken \(E(X)\). Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"Er geldt \(E(X) = 20 \cdot 0{,}1 = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule geeft de standaardafwijking van een binomiale verdeling?",
        opties=[
            r"\(\sigma = \sqrt{n\,p\,(1-p)}\)",
            r"\(\sigma = \sqrt{n\,p}\)",
            r"\(\sigma = n\,p\,(1-p)\)",
            r"\(\sigma = \dfrac{n}{\sqrt{p}}\)",
        ],
        antwoord=0,
        uitleg=r"Onder de wortel staat de variantie \(\text{Var}(X) = n\,p\,(1-p)\). Zij is het grootst als \(p = 0{,}5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De som van alle kansen in een kansverdeling is gelijk aan \(1\).",
        antwoord=True,
        uitleg=r"De kansvariabele neemt zeker één van haar waarden aan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke formule geeft de kans op precies \(k\) successen uit \(n\) pogingen?",
        opties=[
            r"\(P(X = k) = \binom{n}{k}\,p^{k}\,(1-p)^{\,n-k}\)",
            r"\(P(X = k) = \binom{n}{k}\,p^{\,n}\,(1-p)^{k}\)",
            r"\(P(X = k) = \binom{n}{k}\,p^{\,n-k}\,(1-p)^{k}\)",
            r"\(P(X = k) = p^{k}\,(1-p)^{\,n-k}\)",
        ],
        antwoord=0,
        uitleg=r"De binomiaalcoëfficiënt \(\binom{n}{k}\) telt op hoeveel verschillende volgordes die \(k\) successen kunnen hebben.",
    ),
    dict(
        type="invultekst",
        vraag=r"Uit hoeveel pogingen bestaat één Bernoulli-experiment? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg=r"Eén poging met twee mogelijke uitkomsten. Herhaal je ze \(n\) keer, dan krijg je een binomiale verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(E(X)\) in de praktijk?",
        opties=[
            r"het gemiddelde dat je op lange termijn zou meten",
            r"de uitkomst die het vaakst zal voorkomen",
            r"de grootste waarde die de kansvariabele aanneemt",
            r"de uitkomst die je met zekerheid zal krijgen",
        ],
        antwoord=0,
        uitleg=r"Bij één enkel experiment zegt \(E(X)\) niets met zekerheid. Pas over heel veel herhalingen klopt ze gemiddeld.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De verwachtingswaarde \(E(X)\) moet zelf een mogelijke uitkomst zijn.",
        antwoord=False,
        uitleg=r"Het gemiddelde aantal kinderen per gezin is \(1{,}7\), en zoveel kinderen heeft geen enkel gezin.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welk voorbeeld is binomiaal verdeeld?",
        opties=[
            r"het aantal zessen in vijftig worpen met een dobbelsteen",
            r"de lengte van vijftig willekeurige volwassen mensen",
            r"het aantal worpen tot je de eerste zes gooit",
            r"de som van de ogen bij vijftig worpen samen",
        ],
        antwoord=0,
        uitleg=r"Vast aantal worpen \(n = 50\), telkens dezelfde kans \(p = \tfrac{1}{6}\), en de worpen beïnvloeden elkaar niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke kansvariabele is continu?",
        opties=[
            r"de tijd die een trein te laat is",
            r"het aantal reizigers op een trein",
            r"het aantal treinen dat te laat is",
            r"het spoor waarop de trein aankomt",
        ],
        antwoord=0,
        uitleg=r"Tijd kan elke waarde in een interval aannemen. Aantallen zijn altijd discreet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een grotere standaardafwijking \(\sigma\) betekent dat de uitkomsten verder uit elkaar liggen.",
        antwoord=True,
        uitleg=r"Ze meet hoe sterk de waarden rond \(E(X)\) schommelen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je berekent \(P(X \ge 1)\) als \(1 - P(X = k)\). Welke \(k\) vul je in? Schrijf het getal.",
        antwoord=["0", "nul", "geen"],
        uitleg=r"Het tegengestelde van minstens één is precies nul. Dat is de complementregel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat laat je bij een binomiale verdeling aan de rekenapp over?",
        opties=[
            r"de kansen, \(E(X)\) en \(\sigma\) berekenen",
            r"beslissen of de verdeling in deze opgave wel echt binomiaal is",
            r"de nulhypothese en de alternatieve hypothese opstellen",
            r"het resultaat in de context van de opgave uitleggen",
        ],
        antwoord=0,
        uitleg=r"Het rekenwerk mag de app doen. Beoordelen of het model past en wat het antwoord betekent, blijft jouw werk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee binomiale verdelingen hebben dezelfde \(E(X)\), maar een verschillende \(\sigma\). Wat betekent dat?",
        opties=[
            r"de uitkomsten liggen bij de ene meer verspreid dan bij de andere",
            r"de ene verdeling heeft meer mogelijke uitkomsten dan de andere",
            r"de ene is binomiaal en de andere eigenlijk niet",
            r"de twee verdelingen zijn in feite volledig gelijk",
        ],
        antwoord=0,
        uitleg=r"Gemiddeld hetzelfde resultaat, maar bij de ene schommelt het sterker van keer tot keer.",
    ),
]
