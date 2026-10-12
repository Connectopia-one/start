# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Rekenen met mol, massa en concentratie.

Hoort bij "berekeningen" van de vakfiche chemie 2de graad doorstroomfinaliteit.
Eén thema, want dit onderdeel weegt 15 % van het examen.

Deel 1 gaat over de stofhoeveelheid: de omzettingen tussen mol, aantal deeltjes
en massa, met het getal van Avogadro en de molaire massa. Deel 2 gaat over de
concentraties, het verdunnen met c₁V₁ = c₂V₂, en de stoichiometrische
berekeningen bij een aflopende reactie.

De relatieve atoommassa's komen uit het periodiek systeem en worden volgens de
fiche op 0,1 afgerond. Het getal van Avogadro, 6,02.10²³ deeltjes per mol, staat
in de bijlage die een kind op het examen mag gebruiken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel deeltjes zitten er in één mol van een stof?",
        opties=[
            r"\(6{,}02 \cdot 10^{23}\)",
            r"\(6{,}02 \cdot 10^{-23}\)",
            r"\(1{,}66 \cdot 10^{-27}\)",
            r"\(6{,}02 \cdot 10^{22}\)",
        ],
        antwoord=0,
        uitleg="Dat getal heet het getal van Avogadro. Het is een afspraak, zoals een dozijn er twaalf zijn, maar veel groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formules geven een stofhoeveelheid in mol? Kruis alles aan wat juist is.",
        opties=[
            "n = m / M",
            "n = N / NA",
            "n = m . M",
            "n = M / m",
        ],
        antwoord=[0, 1],
        uitleg="Uit de massa deel je door de molaire massa, uit het aantal deeltjes door het getal van Avogadro. De andere staan verkeerd om.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de molaire massa van water, als H \(1{,}0\) en O \(16{,}0\) is?",
        opties=[
            r"\(18{,}0\) g/mol",
            r"\(17{,}0\) g/mol",
            r"\(16{,}0\) g/mol",
            r"\(20{,}0\) g/mol",
        ],
        antwoord=0,
        uitleg=r"Twee keer \(1{,}0\) voor de waterstof en \(16{,}0\) voor de zuurstof: samen \(18{,}0\) g/mol.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de molaire massa van CO₂, als C \(12{,}0\) en O \(16{,}0\) is?",
        opties=[
            r"\(44{,}0\) g/mol",
            r"\(28{,}0\) g/mol",
            r"\(32{,}0\) g/mol",
            r"\(40{,}0\) g/mol",
        ],
        antwoord=0,
        uitleg=r"\(12{,}0\) voor de koolstof plus twee keer \(16{,}0\) voor de zuurstof: \(44{,}0\) g/mol.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel mol is \(36{,}0\) g water, als de molaire massa \(18{,}0\) g/mol is?",
        opties=[
            r"\(2{,}00\) mol",
            r"\(0{,}500\) mol",
            r"\(18{,}0\) mol",
            r"\(648\) mol",
        ],
        antwoord=0,
        uitleg=r"Je deelt \(36{,}0\) door \(18{,}0\) en komt op \(2{,}00\) mol uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel weegt \(0{,}500\) mol natriumchloride, als de molaire massa \(58{,}5\) g/mol is?",
        opties=[
            r"\(29{,}3\) g",
            r"\(58{,}5\) g",
            r"\(117\) g",
            r"\(11{,}7\) g",
        ],
        antwoord=0,
        uitleg=r"Je draait de formule om: m = n keer M, dus \(0{,}500\) keer \(58{,}5\) is \(29{,}25\) en afgerond \(29{,}3\) g.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel mol is \(1{,}204 \cdot 10^{24}\) moleculen van een stof?",
        opties=[
            r"\(2{,}00\) mol",
            r"\(0{,}500\) mol",
            r"\(1{,}20\) mol",
            r"\(20{,}0\) mol",
        ],
        antwoord=0,
        uitleg=r"Je deelt door het getal van Avogadro: \(1{,}204 \cdot 10^{24} : 6{,}02 \cdot 10^{23}\) is \(2{,}00\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel moleculen zitten er in \(0{,}250\) mol van een stof?",
        opties=[
            r"\(1{,}51 \cdot 10^{23}\)",
            r"\(2{,}41 \cdot 10^{24}\)",
            r"\(1{,}51 \cdot 10^{22}\)",
            r"\(6{,}02 \cdot 10^{23}\)",
        ],
        antwoord=0,
        uitleg=r"Je vermenigvuldigt met het getal van Avogadro: \(0{,}250\) keer \(6{,}02 \cdot 10^{23}\) geeft \(1{,}51 \cdot 10^{23}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheid hoort bij de molaire massa?",
        opties=[
            "g/mol",
            "mol/L",
            "g/L",
            "mol",
        ],
        antwoord=0,
        uitleg="De molaire massa zegt hoeveel gram één mol weegt, dus gram per mol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden heb je nodig om de stofhoeveelheid uit de massa te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de massa van het staal",
            "de molaire massa van de stof",
            "het volume van het vat",
            "de temperatuur van het lokaal",
        ],
        antwoord=[0, 1],
        uitleg="Met n = m gedeeld door M heb je enkel die twee nodig. Het volume komt pas bij een concentratie te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling berekent de massa van \(3\) mol CO₂ en schrijft \(132\) g op. Hoe weet je zonder narekenen dat de orde klopt?",
        opties=[
            "drie keer ruim veertig is ongeveer honderdtwintig",
            "drie mol weegt altijd ongeveer honderd gram",
            "de massa is altijd gelijk aan het aantal mol",
            "de massa moet onder de tien gram blijven",
        ],
        antwoord=0,
        uitleg=r"Zo'n schatting vooraf laat je meteen zien of je antwoord in de buurt ligt. \(3\) keer \(44{,}0\) is \(132\) g, dus klopt het.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén mol van een stof bevat altijd evenveel deeltjes, welke stof het ook is.",
        antwoord=True,
        uitleg=r"Dat is net de afspraak achter de mol: telkens \(6{,}02 \cdot 10^{23}\) deeltjes. De massa van die mol verschilt wel per stof.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén mol water en één mol koolstofdioxide hebben dezelfde massa.",
        antwoord=False,
        uitleg=r"Water is \(18{,}0\) g/mol en koolstofdioxide \(44{,}0\) g/mol. Het aantal deeltjes is gelijk, de massa niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De molaire massa van een stof lees je af uit de relatieve atoommassa's in het periodiek systeem.",
        antwoord=True,
        uitleg="Je telt de relatieve atoommassa's van alle atomen in de formule op. Het getal dat je krijgt, is de molaire massa in g/mol.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je naar de stofhoeveelheid gevraagd wordt, bedoelt men de massa in gram.",
        antwoord=False,
        uitleg="De fiche spreekt dat uitdrukkelijk af: met stofhoeveelheid wordt het aantal mol bedoeld. Anders staat er expliciet massa of aantal deeltjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mol van een stof bevat twee keer zoveel deeltjes als één mol.",
        antwoord=True,
        uitleg="Het aantal deeltjes is recht evenredig met de stofhoeveelheid.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de molaire massa van NaOH, als Na \(23{,}0\) en O \(16{,}0\) en H \(1{,}0\) is? Noteer in g/mol.",
        antwoord=["40,0", "40", "40,0 g/mol"],
        uitleg=r"\(23{,}0\) plus \(16{,}0\) plus \(1{,}0\) is \(40{,}0\) g/mol.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel mol is \(88{,}0\) g CO₂, als de molaire massa \(44{,}0\) g/mol is?",
        antwoord=["2,00", "2", "2,00 mol"],
        uitleg=r"\(88{,}0 : 44{,}0\) is \(2{,}00\) mol.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel mol is \(3{,}01 \cdot 10^{23}\) deeltjes?",
        antwoord=["0,500", "0,5", "0,500 mol"],
        uitleg=r"Dat is precies de helft van het getal van Avogadro, dus \(0{,}500\) mol.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel gram weegt \(0{,}200\) mol water, met een molaire massa van \(18{,}0\) g/mol?",
        antwoord=["3,60", "3,6", "3,60 g"],
        uitleg=r"\(0{,}200\) keer \(18{,}0\) is \(3{,}60\) g.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de molaire concentratie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is de stofhoeveelheid per volume",
            "haar eenheid is mol per liter",
            "ze is de massa per volume",
            "haar eenheid is gram per mol",
        ],
        antwoord=[0, 1],
        uitleg=r"De formule is \(c = n\) gedeeld door V. De massa per volume is de massaconcentratie, in gram per liter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je lost \(0{,}500\) mol zout op tot \(2{,}00\) L oplossing. Wat is de molaire concentratie?",
        opties=[
            r"\(0{,}250\) mol/L",
            r"\(1{,}00\) mol/L",
            r"\(4{,}00\) mol/L",
            r"\(2{,}50\) mol/L",
        ],
        antwoord=0,
        uitleg=r"\(0{,}500 : 2{,}00\) is \(0{,}250\) mol/L.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je lost \(0{,}100\) mol op tot \(250\) mL oplossing. Wat is de molaire concentratie?",
        opties=[
            r"\(0{,}400\) mol/L",
            r"\(0{,}025\) mol/L",
            r"\(2{,}50\) mol/L",
            r"\(25{,}0\) mol/L",
        ],
        antwoord=0,
        uitleg=r"Zet \(250\) mL eerst om in \(0{,}250\) L. Dan is \(0{,}100 : 0{,}250\) gelijk aan \(0{,}400\) mol/L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheid hoort bij de massaconcentratie?",
        opties=[
            "g/L",
            "mol/L",
            "g/mol",
            "mol",
        ],
        antwoord=0,
        uitleg="De massaconcentratie is de massa per volume, dus gram per liter. De molaire concentratie werkt met mol.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een oplossing bevat \(40{,}0\) g NaOH per liter. Wat is de molaire concentratie, met M gelijk aan \(40{,}0\) g/mol?",
        opties=[
            r"\(1{,}00\) mol/L",
            r"\(0{,}100\) mol/L",
            r"\(40{,}0\) mol/L",
            r"\(1600\) mol/L",
        ],
        antwoord=0,
        uitleg=r"Deel de massaconcentratie door de molaire massa: \(40{,}0 : 40{,}0\) is \(1{,}00\) mol/L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule gebruik je om een oplossing te verdunnen?",
        opties=[
            "c₁V₁ = c₂V₂",
            r"\(c = n\) / V",
            "n = m / M",
            "n = N / NA",
        ],
        antwoord=0,
        uitleg="Bij verdunnen voeg je enkel water toe, dus blijft het aantal mol gelijk. Daarom is het product van concentratie en volume links en rechts hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je verdunt \(50{,}0\) mL van een oplossing van \(1{,}00\) mol/L tot \(250\) mL. Wat is de nieuwe concentratie?",
        opties=[
            r"\(0{,}200\) mol/L",
            r"\(0{,}500\) mol/L",
            r"\(5{,}00\) mol/L",
            r"\(0{,}050\) mol/L",
        ],
        antwoord=0,
        uitleg=r"Het volume wordt vijf keer groter, dus de concentratie vijf keer kleiner: \(1{,}00 : 5\) is \(0{,}200\) mol/L.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je hebt \(100\) mL van \(2{,}00\) mol/L nodig uit een voorraad van \(10{,}0\) mol/L. Hoeveel neem je uit de voorraad?",
        opties=[
            r"\(20{,}0\) mL",
            r"\(50{,}0\) mL",
            r"\(5{,}00\) mL",
            r"\(200\) mL",
        ],
        antwoord=0,
        uitleg=r"Uit c₁V₁ = c₂V₂ volgt V₁ = \(2{,}00\) keer \(100 : 10{,}0\), dus \(20{,}0\) mL. Daarna vul je aan tot \(100\) mL.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de reactie 2 H₂ + O₂ → 2 H₂O reageert \(4{,}00\) mol H₂ volledig. Hoeveel mol O₂ is daarvoor nodig?",
        opties=[
            r"\(2{,}00\) mol",
            r"\(4{,}00\) mol",
            r"\(8{,}00\) mol",
            r"\(1{,}00\) mol",
        ],
        antwoord=0,
        uitleg=r"De coëfficiënten geven de verhouding: op twee H₂ hoort één O₂. Dus bij \(4{,}00\) mol H₂ hoort \(2{,}00\) mol O₂.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de reactie CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂ reageert \(1{,}00\) mol kalksteen volledig. Hoeveel mol CO₂ ontstaat er?",
        opties=[
            r"\(1{,}00\) mol",
            r"\(2{,}00\) mol",
            r"\(0{,}500\) mol",
            r"\(3{,}00\) mol",
        ],
        antwoord=0,
        uitleg="De coëfficiënt bij CaCO₃ en bij CO₂ is in beide gevallen één, dus is de verhouding één op één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen zet je om uit een massa reagens de massa van een product te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de massa omzetten in mol",
            "de verhouding uit de coëfficiënten gebruiken",
            "de massa's gewoon bij elkaar optellen",
            "de volumes van de stoffen vergelijken",
        ],
        antwoord=[0, 1],
        uitleg="De coëfficiënten gelden voor mol en niet voor gram. Dus reken je eerst naar mol, dan met de verhouding, en pas daarna terug naar gram.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het verdunnen van een oplossing blijft het aantal mol opgeloste stof gelijk.",
        antwoord=True,
        uitleg="Je voegt enkel oplosmiddel toe. Het volume stijgt dus en de concentratie daalt in dezelfde verhouding.",
    ),
    dict(
        type="waarofniet",
        vraag="De coëfficiënten in een reactievergelijking geven de verhouding in gram.",
        antwoord=False,
        uitleg="Ze geven de verhouding in aantal deeltjes, dus in mol. Daarom reken je bij een berekening altijd eerst naar mol.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aflopende reactie gaat door tot een van de reagentia helemaal opgebruikt is.",
        antwoord=True,
        uitleg="Die stof heet het beperkende reagens. De andere stof blijft dan in overmaat over.",
    ),
    dict(
        type="waarofniet",
        vraag="De molaire concentratie van een oplossing stijgt als je water toevoegt.",
        antwoord=False,
        uitleg="Het aantal mol blijft gelijk en het volume stijgt, dus daalt de concentratie.",
    ),
    dict(
        type="waarofniet",
        vraag="Je antwoord op een berekening noteer je met het juiste aantal beduidende cijfers.",
        antwoord=True,
        uitleg="Een meting is nooit exact, dus mag je antwoord niet nauwkeuriger lijken dan je gegevens. De fiche vraagt dat uitdrukkelijk.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je lost \(0{,}300\) mol op tot \(1{,}50\) L oplossing. Wat is de molaire concentratie in mol/L?",
        antwoord=["0,200", "0,2", "0,200 mol/L"],
        uitleg=r"\(0{,}300 : 1{,}50\) is \(0{,}200\) mol/L.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel mol zit er in \(500\) mL van een oplossing van \(0{,}400\) mol/L?",
        antwoord=["0,200", "0,2", "0,200 mol"],
        uitleg=r"\(n = c\) keer V, dus \(0{,}400\) keer \(0{,}500\) L is \(0{,}200\) mol.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je verdunt \(25{,}0\) mL van \(0{,}800\) mol/L tot \(100\) mL. Wat is de nieuwe concentratie in mol/L?",
        antwoord=["0,200", "0,2", "0,200 mol/L"],
        uitleg="Het volume wordt vier keer groter, dus de concentratie vier keer kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het reagens dat bij een aflopende reactie het eerst opgebruikt is?",
        antwoord=["beperkend reagens", "het beperkende reagens", "beperkende reagens"],
        uitleg="Dat reagens bepaalt hoeveel product er maximaal kan ontstaan. De rest blijft in overmaat over.",
    ),
]
