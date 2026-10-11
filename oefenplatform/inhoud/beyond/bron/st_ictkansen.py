# -*- coding: utf-8 -*-
"""Kansen berekenen met de kansrekenmachine.

Kim merkte op 8 oktober 2026 op dat er bij statistiek meer oefeningen nodig
zijn die je met GeoGebra moet oplossen, en dat is juist. De vakfiche zet bij
bijna elk rekenleerdoel "met ICT": je stelt de kansverdeling op met ICT, je
berekent de verwachtingswaarde en de standaardafwijking met ICT, je berekent
kansen bij een binomiale verdeling met ICT, je berekent de p-waarde met ICT.
Een kind dat alleen begripsvragen gemaakt heeft, heeft die knoppen nog nooit
aangeraakt.

De vragen hier zijn daarom bijna allemaal echte rekenopgaven waar je het
toestel voor nodig hebt. Het zijn vooral invulvragen, want kiezen uit vier
getallen kan je nog gokken; een getal op drie decimalen intikken niet.

Alle antwoorden zijn met de hand nagerekend (zie het rekenscript in de
scratchpad van 8 oktober 2026), en de afrondingen zijn gekozen zodat een kind
dat tussentijds afrondt op hetzelfde getal uitkomt. Waar dat niet kon, staan
er twee antwoorden in de lijst.

Het platform vergelijkt een getal soepel: 0,192 en 0.192 en 0,1920 tellen
alle drie juist (zie normaliseerGetal in components/Quiz.tsx). Een eenheid of
een procentteken erbij mag ook. Maar afronden op een ander aantal decimalen
telt fout, dus zeg in de vraag altijd hoeveel decimalen je wil.

Deel 1 is de binomiale verdeling.
Deel 2 is de normale verdeling en de p-waarde.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag=r"X is binomiaal verdeeld met \(n\) gelijk aan \(20\) en \(p\) gelijk aan \(0{,}3\). Bereken \(P(X = 6)\) op drie decimalen.",
        antwoord=["0,192"],
        uitleg=r"In de kansrekenmachine kies je de binomiale verdeling, zet je \(n\) op \(20\) en \(p\) op \(0{,}3\) en vraag je de kans op precies \(6\). Je krijgt \(0{,}1916\).",
    ),
    dict(
        type="invultekst",
        vraag="Je gooit tien keer met een munt. Bereken de kans op precies vijf keer kop, op drie decimalen.",
        antwoord=["0,246"],
        uitleg=r"\(X \sim B(10; 0{,}5)\) en \(P(X = 5)\) is \(0{,}2461\). Dus zelfs de meest waarschijnlijke uitkomst valt maar in een kwart van de reeksen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(X \sim B(20; 0{,}3)\). Hoeveel is \(P(X \leq 4)\) op twee decimalen?",
        opties=[r"\(0{,}24\)", r"\(0{,}19\)", r"\(0{,}13\)", r"\(0{,}76\)"],
        antwoord=0,
        uitleg=r"Met de cumulatieve optie tot en met \(4\) krijg je \(0{,}2375\). \(0{,}19\) is de kans op precies \(6\) en \(0{,}76\) is het complement.",
    ),
    dict(
        type="invultekst",
        vraag="Je gooit twaalf keer met een dobbelsteen. Bereken de kans op precies twee zessen, op drie decimalen.",
        antwoord=["0,296"],
        uitleg=r"\(X \sim B(12; \tfrac{1}{6})\), dus \(p\) is \(0{,}1667\). \(P(X = 2)\) is \(0{,}2961\). Tik \(p\) in als breuk of met vier decimalen, niet als \(0{,}17\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(X \sim B(50; 0{,}2)\). Bereken \(P(X \geq 15)\) op drie decimalen.",
        antwoord=["0,061"],
        uitleg=r"Neem de cumulatieve kans tot en met \(14\) en trek die van één af: \(1\) min \(0{,}9393\) is \(0{,}0607\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een schutter raakt in \(75\) procent van de gevallen. Hij schiet acht keer. Hoeveel is de kans op precies zes keer raak, op twee decimalen?",
        opties=[r"\(0{,}31\)", r"\(0{,}75\)", r"\(0{,}25\)", r"\(0{,}11\)"],
        antwoord=0,
        uitleg=r"\(X \sim B(8; 0{,}75)\) en \(P(X = 6)\) is \(0{,}3115\). Zes van de acht is precies het verwachte aantal, en toch is de kans maar \(31\) procent.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(X \sim B(100; 0{,}4)\). Bereken \(P(X \leq 35)\) op drie decimalen.",
        antwoord=["0,179"],
        uitleg=r"De cumulatieve kans tot en met \(35\) is \(0{,}1795\). Het verwachte aantal is \(40\), dus \(35\) of minder is niet uitzonderlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een test slaagt in \(90\) procent van de gevallen. Je doet vijftien tests. Hoeveel is de kans dat ze allemaal slagen, op twee decimalen?",
        opties=[r"\(0{,}21\)", r"\(0{,}90\)", r"\(0{,}09\)", r"\(0{,}79\)"],
        antwoord=0,
        uitleg=r"\(X \sim B(15; 0{,}9)\) en \(P(X = 15)\) is \(0{,}2059\). \(90\) procent per keer geeft maar één kans op vijf dat alles lukt.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(4\) procent van de stukken is afgekeurd. Je neemt \(25\) stukken. Bereken de kans op geen enkel afgekeurd stuk, op twee decimalen.",
        antwoord=["0,36"],
        uitleg=r"\(X \sim B(25; 0{,}04)\) en \(P(X = 0)\) is \(0{,}3604\). Het verwachte aantal is precies één, en toch is er \(36\) procent kans op geen enkel.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(X \sim B(30; 0{,}5)\). Bereken \(P(X \geq 20)\) op drie decimalen.",
        antwoord=["0,049"],
        uitleg=r"Eén min de cumulatieve kans tot en met \(19\) geeft \(0{,}0494\). Twintig van de dertig is dus al een zeldzame uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit zes keer met een dobbelsteen. Hoeveel is de kans op minstens één zes, op twee decimalen?",
        opties=[r"\(0{,}67\)", r"\(0{,}33\)", r"\(1{,}00\)", r"\(0{,}17\)"],
        antwoord=0,
        uitleg=r"Reken met het complement: één min de kans op nul zessen, dus \(1\) min \(0{,}3349\) is \(0{,}6651\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(X \sim B(40; 0{,}25)\). Bereken \(P(X = 10)\) op drie decimalen.",
        antwoord=["0,144"],
        uitleg=r"Tien is precies de verwachtingswaarde, en toch is de kans maar \(0{,}1444\). Bij een grote \(n\) is elke afzonderlijke uitkomst zeldzaam.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een ziekte komt bij \(5\) procent van de mensen voor. Je onderzoekt \(200\) mensen. Hoeveel is \(P(X \leq 5)\) op drie decimalen?",
        opties=[r"\(0{,}062\)", r"\(0{,}050\)", r"\(0{,}938\)", r"\(0{,}180\)"],
        antwoord=0,
        uitleg=r"\(X \sim B(200; 0{,}05)\) en de cumulatieve kans tot en met \(5\) is \(0{,}0623\). Het verwachte aantal is tien, dus vijf of minder is laag.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(X \sim B(16; 0{,}5)\). Bereken \(P(X \geq 12)\) op drie decimalen.",
        antwoord=["0,038"],
        uitleg=r"Eén min de cumulatieve kans tot en met \(11\) geeft \(0{,}0384\). Twaalf keer kop op zestien worpen zou je dus doen opkijken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(X \sim B(20; 0{,}3)\) is \(P(X \leq 4)\) ongeveer \(0{,}19\).",
        antwoord=False,
        uitleg=r"\(P(X \leq 4)\) is \(0{,}24\). Het getal \(0{,}19\) is de kans op precies zes successen. Let op het verschil tussen precies en ten hoogste.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Om \(P(X \geq 15)\) te vinden mag je de cumulatieve kans tot en met \(14\) van één aftrekken.",
        antwoord=True,
        uitleg="Minstens vijftien is het complement van ten hoogste veertien. Veel toestellen geven enkel de cumulatieve kans naar links.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(X \sim B(50; 0{,}2)\). Hoeveel zijn E(X) en de standaardafwijking, op twee decimalen?",
        opties=[r"\(10\) en \(2{,}83\)", r"\(10\) en \(8{,}00\)", r"\(40\) en \(2{,}83\)", r"\(10\) en \(4{,}00\)"],
        antwoord=0,
        uitleg=r"E(X) is \(50 \cdot 0{,}2\) is \(10\), en Var(X) is \(50 \cdot 0{,}2 \cdot 0{,}8\) is \(8\). \(\sqrt{8}\) is \(2{,}83\).",
    ),
    dict(
        type="invultekst",
        vraag="Je gooit vijf keer met een munt. Bereken de kans op geen enkele keer kop, op drie decimalen.",
        antwoord=["0,031"],
        uitleg=r"\(X \sim B(5; 0{,}5)\) en \(P(X = 0)\) is \(0{,}5^{5}\), dus \(0{,}03125\). Dat is één kans op tweeëndertig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat vul je in de kansrekenmachine in om met \(X \sim B(20; 0{,}3)\) te werken?",
        opties=[
            r"de binomiale verdeling, met \(n\) gelijk aan \(20\) en \(p\) gelijk aan \(0{,}3\)",
            r"de normale verdeling, met \(\mu\) gelijk aan \(20\) en \(\sigma\) gelijk aan \(0{,}3\)",
            r"de binomiale verdeling, met \(n\) gelijk aan \(0{,}3\) en \(p\) gelijk aan \(20\)",
            r"de normale verdeling, met \(\mu\) gelijk aan \(6\) en \(\sigma\) gelijk aan \(20\)",
        ],
        antwoord=0,
        uitleg="Het aantal experimenten komt eerst, de kans op succes daarna. Verwissel je ze, dan weigert het toestel of geeft het onzin.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling leest bij een binomiale kans \(1{,}19\) van zijn toestel af. Wat is er gebeurd?",
        opties=[
            "hij las een ander getal af, want een kans ligt tussen nul en één",
            "hij moet het getal door honderd delen om de kans te krijgen",
            r"dat betekent \(119\) procent kans op dat aantal successen",
            "het toestel rekende met de verwachtingswaarde in plaats van de kans",
        ],
        antwoord=0,
        uitleg="Waarschijnlijk stond het toestel op de verwachtingswaarde of op de standaardafwijking. Controleer altijd of je uitkomst tussen nul en één ligt.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"X volgt \(N(180; 8)\). Bereken \(P(X > 192)\) op drie decimalen.",
        antwoord=["0,067"],
        uitleg=r"In de kansrekenmachine kies je de normale verdeling, vult \(180\) en \(8\) in en vraagt de rechterstaart vanaf \(192\). Je krijgt \(0{,}0668\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De lengte van mannen volgt \(N(178; 7)\). Bereken P(\(171\) < X < \(185\)) op drie decimalen.",
        antwoord=["0,683"],
        uitleg=r"Dat is precies één standaardafwijking aan elke kant, dus \(0{,}6827\). Daar komt de vuistregel van achtenzestig procent vandaan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het IQ volgt \(N(100; 15)\). Hoeveel is \(P(X > 130)\) op drie decimalen?",
        opties=[r"\(0{,}023\)", r"\(0{,}046\)", r"\(0{,}159\)", r"\(0{,}977\)"],
        antwoord=0,
        uitleg=r"Honderddertig is twee standaardafwijkingen boven het gemiddelde, dus \(0{,}0228\). \(0{,}977\) is de kans eronder.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een machine vult pakken volgens \(N(500; 20)\) gram. Bereken \(P(X < 480)\) op drie decimalen.",
        antwoord=["0,159"],
        uitleg=r"Vierhonderdtachtig is één standaardafwijking onder het gemiddelde, dus \(0{,}1587\). Bijna één pak op zes is dus te licht.",
    ),
    dict(
        type="invultekst",
        vraag=r"Z volgt de standaardnormale verdeling. Bereken \(P(Z < 1{,}96)\) op drie decimalen.",
        antwoord=["0,975"],
        uitleg=r"\(0{,}9750\). Daarom hoort bij een betrouwbaarheidsinterval van vijfennegentig procent precies de grens \(1{,}96\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De punten op een toets volgen \(N(72; 8)\). Hoeveel is \(P(X > 80)\) op drie decimalen?",
        opties=[r"\(0{,}159\)", r"\(0{,}841\)", r"\(0{,}683\)", r"\(0{,}023\)"],
        antwoord=0,
        uitleg=r"Tachtig is één standaardafwijking boven het gemiddelde, dus \(0{,}1587\). Ongeveer één leerling op zes haalt meer dan tachtig.",
    ),
    dict(
        type="invultekst",
        vraag=r"X volgt \(N(20; 4)\). Bereken \(P(X < 15)\) op drie decimalen.",
        antwoord=["0,106"],
        uitleg=r"De z-waarde is min \(1{,}25\) en de kans links daarvan is \(0{,}1056\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De lichaamstemperatuur volgt \(N(37; 0{,}5)\). Bereken \(P(X > 38)\) op vier decimalen.",
        antwoord=["0,0228", "0,023"],
        uitleg=r"Achtendertig graden is twee standaardafwijkingen boven het gemiddelde, dus \(0{,}0228\). Ruim twee op honderd metingen komen daarboven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een zak weegt volgens \(N(1000; 50)\) gram. Hoeveel is P(\(950\) < X < \(1050\)) op drie decimalen?",
        opties=[r"\(0{,}683\)", r"\(0{,}954\)", r"\(0{,}500\)", r"\(0{,}317\)"],
        antwoord=0,
        uitleg=r"Eén standaardafwijking aan elke kant geeft \(0{,}6827\). Twee standaardafwijkingen zouden \(0{,}954\) geven.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij een rechtszijdige toets vind je z gelijk aan \(2\). Bereken de \(p\)-waarde op vier decimalen.",
        antwoord=["0,0228", "0,023"],
        uitleg=r"De rechterstaart vanaf z gelijk aan \(2\) is \(0{,}0228\). Dat is kleiner dan \(0{,}05\), dus je verwerpt \(H_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een tweezijdige toets vind je z gelijk aan \(2\). Hoeveel is de \(p\)-waarde op vier decimalen?",
        opties=[r"\(0{,}0455\)", r"\(0{,}0228\)", r"\(0{,}9545\)", r"\(0{,}0114\)"],
        antwoord=0,
        uitleg=r"Bij een tweezijdige toets tel je beide staarten mee, dus twee maal \(0{,}0228\) is \(0{,}0455\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(H_{0}\) zegt \(\mu\) gelijk aan \(50\). Je vindt x gelijk aan \(52\) bij \(n\) gelijk aan \(100\) en \(\sigma\) gelijk aan \(10\), en toetst rechtszijdig. Bereken de \(p\)-waarde op vier decimalen.",
        antwoord=["0,0228", "0,023"],
        uitleg=r"De standaardafwijking van het steekproefgemiddelde is \(10 : 10\), dus \(1\). Dan is z gelijk aan \(2\) en de \(p\)-waarde \(0{,}0228\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(H_{0}\) zegt \(p\) gelijk aan \(0{,}5\). Je vindt \(112\) van \(200\), dus \(p\) met dakje gelijk aan \(0{,}56\), en toetst rechtszijdig. Bereken de \(p\)-waarde op drie decimalen.",
        antwoord=["0,045"],
        uitleg=r"De standaardafwijking is \(\sqrt{0{,}25} : 200\), dus \(0{,}0354\). Dan is z gelijk aan \(1{,}70\) en de \(p\)-waarde \(0{,}0448\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je vindt een \(p\)-waarde van \(0{,}045\) bij een significantieniveau van \(0{,}05\). Wat besluit je?",
        opties=[
            r"je verwerpt \(H_{0}\), want \(0{,}045\) is kleiner dan \(0{,}05\)",
            r"je verwerpt \(H_{0}\) niet, want het verschil is klein",
            r"je besluit dat \(H_{0}\) waar is met \(95{,}5\) procent zekerheid",
            r"je moet het significantieniveau verhogen tot \(0{,}10\)",
        ],
        antwoord=0,
        uitleg=r"Het is krap, maar de regel is duidelijk: \(p\) kleiner dan of gelijk aan \(\alpha\) betekent verwerpen. Vermeld wel dat het krap is.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een symmetrische verdeling is de \(p\)-waarde van een tweezijdige toets het dubbele van die van de eenzijdige.",
        antwoord=True,
        uitleg="Je telt dan twee even grote staarten mee. Daarom is een verschil tweezijdig moeilijker aan te tonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rekenapp geeft bij een normale verdeling de kans op precies één waarde.",
        antwoord=False,
        uitleg="Die kans is nul bij een continue verdeling. Het toestel vraagt altijd een interval of een staart.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat vul je in om bij \(N(72; 8)\) de kans \(P(X > 80)\) te krijgen?",
        opties=[
            r"\(\mu\) is \(72\), \(\sigma\) is \(8\), en je kiest de rechterstaart vanaf \(80\)",
            r"\(\mu\) is \(72\), \(\sigma\) is \(8\), en je kiest de linkerstaart tot \(80\)",
            r"\(\mu\) is \(80\), \(\sigma\) is \(8\), en je kiest de rechterstaart vanaf \(72\)",
            r"\(\mu\) is \(8\), \(\sigma\) is \(72\), en je kiest het interval van \(72\) tot \(80\)",
        ],
        antwoord=0,
        uitleg=r"Kies je de linkerstaart, dan krijg je \(0{,}841\), het complement. Dat is de meest gemaakte fout met dit toestel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Het IQ volgt \(N(100; 15)\). Welke waarde heeft \(2{,}5\) procent van de verdeling boven zich? Geef het antwoord op één decimaal.",
        antwoord=["129,4", "129,40"],
        uitleg=r"Honderd plus \(1{,}96 \cdot 15\) is \(129{,}4\). Veel toestellen hebben hiervoor een omgekeerde of inverse normale functie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een linkszijdige toets vind je z gelijk aan min \(2{,}5\). Hoeveel is de \(p\)-waarde op vier decimalen?",
        opties=[r"\(0{,}0062\)", r"\(0{,}9938\)", r"\(0{,}0124\)", r"\(0{,}0228\)"],
        antwoord=0,
        uitleg=r"De linkerstaart tot min \(2{,}5\) is \(0{,}0062\). Dat is sterk bewijs tegen \(H_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling meldt bij een rechtszijdige toets een \(p\)-waarde van \(0{,}9772\). Wat ging er mis?",
        opties=[
            r"hij nam de linkerstaart, de \(p\)-waarde is \(0{,}0228\)",
            "hij vergat het significantieniveau in te vullen in het toestel",
            "hij moet het getal van één aftrekken en dan nog eens verdubbelen",
            r"er ging niets mis, een \(p\)-waarde van \(0{,}9772\) kan voorkomen",
        ],
        antwoord=0,
        uitleg=r"De twee getallen geven samen één. Bij een rechtszijdige toets hoort de staart aan de kant waar \(H_{1}\) naar wijst.",
    ),
]
