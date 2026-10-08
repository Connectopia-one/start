# -*- coding: utf-8 -*-
"""Kansvariabelen en de binomiale verdeling.

De vakfiche vraagt hier: discrete en continue kansvariabele (of stochast),
kansverdeling, Bernoulli-experiment en Bernoulli-verdeling, en de binomiale
verdeling. En vooral dit leerdoel: "Je bepaalt of een kansvariabele bij een
experiment al dan niet binomiaal verdeeld is." Dat is het moeilijkste deel,
want de vier voorwaarden samen bekijken is lastiger dan een kans uitrekenen.

De notatie van de bijlage is X ~ B(n, p), met n het aantal experimenten en p
de kans op succes. Gebruik die notatie, geen andere: de fiche zegt dat alle
andere notaties als foutief gelden.

De fiche zegt bij elk rekenleerdoel "met ICT". Een kind hoeft de formule
P(X = k) = C(n, k) · p^k · (1 − p)^(n − k) dus niet uit het hoofd toe te
passen, maar wel begrijpen wat ze doet en wanneer ze geldt.

Deel 1 is de kansvariabele, de kansverdeling en Bernoulli.
Deel 2 is de binomiale verdeling zelf: voorwaarden en kansen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een kansvariabele?",
        opties=[
            "een grootheid die aan elke uitkomst van een experiment een getal hangt",
            "de kans dat een bepaalde uitkomst van een experiment zich voordoet",
            "het aantal keer dat je een experiment achter elkaar uitvoert",
            "een getal tussen nul en één dat je met een rekenapp opzoekt",
        ],
        antwoord=0,
        uitleg="Gooi je met twee dobbelstenen, dan is de som van de ogen een kansvariabele. De bijlage noteert ze als X of Y.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze kansvariabelen is discreet?",
        opties=[
            "het aantal kinderen in een gezin",
            "de lengte van een pasgeboren baby",
            "de tijd die een trein te laat is",
            "het gewicht van een appel uit de boomgaard",
        ],
        antwoord=0,
        uitleg="Een discrete kansvariabele neemt losse waarden aan, meestal gehele getallen. De drie andere kunnen elke waarde in een interval aannemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze kansvariabelen is continu?",
        opties=[
            "de temperatuur om twaalf uur",
            "het aantal zessen bij tien worpen",
            "het aantal auto's in een straat",
            "het aantal juiste antwoorden op een toets",
        ],
        antwoord=0,
        uitleg="Een continue kansvariabele kan elke waarde in een interval aannemen. Meten geeft meestal continu, tellen geeft discreet.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een continue kansvariabele is de kans op één exacte waarde gelijk aan nul.",
        antwoord=True,
        uitleg="Je rekent daar met kansen op een interval, bijvoorbeeld de kans dat een baby tussen 49 en 51 centimeter meet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kansverdeling van een discrete kansvariabele?",
        opties=[
            "een overzicht van alle waarden met de kans op elk van die waarden",
            "het gemiddelde van alle waarden die de kansvariabele kan aannemen",
            "de grootste kans die bij een van de waarden hoort",
            "het verschil tussen de grootste en de kleinste waarde",
        ],
        antwoord=0,
        uitleg="Vaak staat ze in een tabel: bovenaan de waarden, eronder de kansen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel moet de som van alle kansen in een kansverdeling zijn? Geef het getal in cijfers.",
        antwoord=["1", "één", "een"],
        uitleg="Een van de waarden valt zeker, dus de kansen samen geven precies 1, of honderd procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft P(X=1) = 0,2, P(X=2) = 0,5 en P(X=3) = 0,4. Wat is er mis?",
        opties=[
            "de som van de kansen is 1,1 en dat kan niet",
            "er staan te weinig waarden in de tabel om een verdeling te vormen",
            "de kans bij X=2 moet altijd de grootste van de drie zijn",
            "de waarden moeten bij nul beginnen en niet bij één",
        ],
        antwoord=0,
        uitleg="Controleer altijd eerst of de kansen samen 1 geven. Dat is de snelste manier om een fout te vinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een Bernoulli-experiment?",
        opties=[
            "een experiment met juist twee mogelijke uitkomsten",
            "een experiment dat je minstens dertig keer moet herhalen",
            "een experiment waarbij elke uitkomst dezelfde kans heeft",
            "een experiment waarvan de uitkomst continu verdeeld is",
        ],
        antwoord=0,
        uitleg="Succes of geen succes, kop of munt, geslaagd of niet. De kans op succes noemen we p.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een Bernoulli-experiment moeten de twee uitkomsten even waarschijnlijk zijn.",
        antwoord=False,
        uitleg="Niet nodig. Een penaltyschutter met zeventig procent kans doet ook een Bernoulli-experiment.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kansvariabele hoort bij een Bernoulli-verdeling?",
        opties=[
            "een variabele die alleen nul of één kan zijn",
            "een variabele die alle gehele getallen kan aannemen",
            "een variabele die elke waarde tussen nul en één kan aannemen",
            "een variabele die het gemiddelde van een steekproef weergeeft",
        ],
        antwoord=0,
        uitleg="Eén voor succes, nul voor geen succes. De binomiale verdeling telt hoeveel keer die één valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort het aantal kop bij twintig muntworpen bij een discrete kansvariabele?",
        opties=[
            "omdat je alleen de gehele getallen van nul tot twintig kan krijgen",
            "omdat de kans op kop precies de helft is bij elke worp",
            "omdat je twintig worpen doet en twintig een geheel getal is",
            "omdat kop en munt samen altijd honderd procent geven",
        ],
        antwoord=0,
        uitleg="Er zit niets tussen twaalf en dertien keer kop. Dat is het kenmerk van discreet.",
    ),
    dict(
        type="waarofniet",
        vraag="De bijlage Begrippen en notaties schrijft de kans dat X de waarde x aanneemt als P(X = x).",
        antwoord=True,
        uitleg="Die notatie wordt op het examen verwacht. Een andere notatie geldt als foutief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit twee keer met een munt en X is het aantal keer kop. Wat is P(X = 1)?",
        opties=["de helft", "een vierde", "drie vierde", "een derde"],
        antwoord=0,
        uitleg="Kop-munt en munt-kop geven samen twee van de vier gelijke uitkomsten, dus een half.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een kansvariabele met een ander woord? Eén woord.",
        antwoord=["stochast", "een stochast"],
        uitleg="De bijlage noemt beide termen: kansvariabele of stochast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kans kan nooit groter zijn dan één of kleiner dan nul.",
        antwoord=True,
        uitleg="Krijg je 1,3 of een negatieve waarde uit een rekenapp, dan is er iets fout ingetikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het aantal telefoontjes per uur in een callcenter is welk soort kansvariabele?",
        opties=["discreet", "continu", "geen van de twee", "zowel discreet als continu"],
        antwoord=0,
        uitleg="Je telt gehele telefoontjes. De duur van een gesprek zou wel continu zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een kansverdeling in een tabel wordt gevraagd naar P(X ≤ 2). Wat doe je?",
        opties=[
            "je telt de kansen van alle waarden tot en met twee op",
            "je neemt enkel de kans die bij de waarde twee staat",
            "je trekt de kans bij twee af van het totaal",
            "je neemt het gemiddelde van de kansen tot aan twee",
        ],
        antwoord=0,
        uitleg="Het teken kleiner dan of gelijk aan betekent optellen tot en met die waarde.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt de bijlage voor de kans op succes bij een Bernoulli-experiment? Eén letter.",
        antwoord=["p"],
        uitleg="De kans op succes is p, en de kans op geen succes is dus 1 − p.",
    ),
    dict(
        type="waarofniet",
        vraag="De waarden van een discrete kansvariabele moeten altijd bij nul beginnen.",
        antwoord=False,
        uitleg="Niet nodig. De som van de ogen van twee dobbelstenen is een kansvariabele die bij twee begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt dat de schoenmaat een continue kansvariabele is. Wat klopt daar niet aan?",
        opties=[
            "schoenmaten zijn losse getallen, dus de variabele is discreet",
            "een schoenmaat is geen kansvariabele, want ze ligt vast",
            "schoenmaten hebben geen kansverdeling, enkel een gemiddelde",
            "schoenmaten zijn wel continu, de leerling heeft dus gelijk",
        ],
        antwoord=0,
        uitleg="De voetlengte in millimeter is continu, maar de maat zelf springt van negenendertig naar veertig.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent de notatie X ~ B(n, p)?",
        opties=[
            "X is binomiaal verdeeld met n experimenten en kans p op succes",
            "X ligt tussen n en p en is daar gelijkmatig verdeeld",
            "X is het gemiddelde van n metingen met standaardafwijking p",
            "X is de kans op n successen bij p experimenten",
        ],
        antwoord=0,
        uitleg="Zo staat ze in de bijlage Begrippen en notaties. Let op de plaats van n en p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarde hoort NIET bij een binomiale verdeling?",
        opties=[
            "de uitkomsten moeten continu verdeeld zijn",
            "het aantal experimenten staat vooraf vast",
            "de kans op succes blijft bij elk experiment gelijk",
            "de experimenten zijn onafhankelijk van elkaar",
        ],
        antwoord=0,
        uitleg="Een binomiale verdeling is juist discreet: je telt het aantal successen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je trekt drie kaarten uit een spel zonder ze terug te leggen. Is het aantal harten binomiaal verdeeld?",
        opties=[
            "nee, want de kans op harten verandert na elke trekking",
            "ja, want er zijn juist twee uitkomsten: harten of geen harten",
            "ja, want het aantal trekkingen staat vooraf vast op drie",
            "nee, want het aantal harten is een continue kansvariabele",
        ],
        antwoord=0,
        uitleg="Zonder teruglegging blijft p niet gelijk. Mét teruglegging zou het wel B(3; 0,25) zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal zessen bij twintig worpen met een eerlijke dobbelsteen is binomiaal verdeeld.",
        antwoord=True,
        uitleg="Twintig onafhankelijke worpen, elk met kans een zesde op succes: X ~ B(20; 1/6).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een quiz heeft tien meerkeuzevragen met vier opties. Je gokt alles. Welke verdeling hoort bij het aantal juiste antwoorden?",
        opties=["B(10; 0,25)", "B(4; 0,10)", "B(0,25; 10)", "B(10; 4)"],
        antwoord=0,
        uitleg="Tien experimenten, elk met een kans van een vierde. Het aantal komt eerst, de kans daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft P(X = k) bij X ~ B(n, p)?",
        opties=[
            "C(n, k) maal p tot de k maal (1−p) tot de (n−k)",
            "C(n, k) maal p maal (1−p)",
            "p tot de k maal (1−p) tot de n",
            "n maal p tot de k gedeeld door k",
        ],
        antwoord=0,
        uitleg="De combinatie telt op hoeveel plaatsen de k successen kunnen vallen, de machten geven de kans per plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij X ~ B(n, p) kan k ook de waarde n plus één aannemen.",
        antwoord=False,
        uitleg="k loopt van nul tot en met n. Meer successen dan experimenten bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit drie keer met een munt. Wat is de kans op juist twee keer kop?",
        opties=["drie achtste", "een vierde", "een half", "een achtste"],
        antwoord=0,
        uitleg="C(3, 2) = 3 plaatsen, elk met kans een achtste. Drie maal een achtste is drie achtste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(5; 0,5), wat is P(X = 0)?",
        opties=["een tweeëndertigste", "een vijfde", "een zestiende", "nul"],
        antwoord=0,
        uitleg="Vijf keer munt achter elkaar: 0,5 tot de vijfde is 1/32, ongeveer drie procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je P(X ≥ 1) het snelst bij een binomiale verdeling?",
        opties=[
            "als één min P(X = 0)",
            "door alle kansen van één tot n op te tellen",
            "als één min P(X = n)",
            "door P(X = 1) met n te vermenigvuldigen",
        ],
        antwoord=0,
        uitleg="Minstens één is het complement van geen enkele. Dat is de complementregel, nu bij kansen.",
    ),
    dict(
        type="invultekst",
        vraag="Bij X ~ B(n, p) is de kans op geen succes bij één experiment gelijk aan 1 min wat? Eén letter.",
        antwoord=["p"],
        uitleg="De kans op geen succes is 1 − p. Dat getal komt in de formule terug als macht n − k.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij X ~ B(10; 0,5) is de kansverdeling symmetrisch rond vijf.",
        antwoord=True,
        uitleg="Bij p gelijk aan een half is kop even waarschijnlijk als munt, dus de verdeling is symmetrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(8; 0,8) ligt de top van de kansverdeling het dichtst bij welke waarde?",
        opties=["zes", "vier", "twee", "acht"],
        antwoord=0,
        uitleg="Acht maal nul komma acht is 6,4, dus rond zes. Bij een grote p schuift de top naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een machine maakt vijf procent afgekeurde stukken. Je neemt twintig stukken. Welke verdeling hoort bij het aantal afgekeurde stukken?",
        opties=["B(20; 0,05)", "B(20; 0,95)", "B(0,05; 20)", "B(5; 0,20)"],
        antwoord=0,
        uitleg="Het succes dat je telt, is hier het afgekeurde stuk, dus p is nul komma nul vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rekenapp kan de hele kansverdeling van een binomiale verdeling in één keer opstellen.",
        antwoord=True,
        uitleg="De fiche vraagt dat ook letterlijk: je stelt de kansverdeling op met ICT.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling berekent bij X ~ B(12; 0,3) een kans van 1,4. Wat weet je meteen?",
        opties=[
            "er is iets fout ingetikt, want een kans ligt tussen nul en één",
            "dat kan, want de kans wordt groter bij meer experimenten",
            "dat betekent honderdveertig procent kans op succes",
            "de app rekende met de variantie in plaats van met de kans",
        ],
        antwoord=0,
        uitleg="Reken je met ICT, kijk dan altijd eerst of de uitkomst tussen nul en één ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een stad stemt veertig procent voor partij A. Je vraagt het aan vijftig willekeurige inwoners. Waarom mag je hier binomiaal rekenen?",
        opties=[
            "de vijftig antwoorden zijn onafhankelijk en p blijft nagenoeg gelijk",
            "vijftig is groter dan dertig, en dat is de voorwaarde",
            "veertig procent ligt dicht bij de helft, dus de verdeling is symmetrisch",
            "omdat je het antwoord van elke inwoner op voorhand kent",
        ],
        antwoord=0,
        uitleg="Bij een stad is de populatie zo groot dat één antwoord de kans voor het volgende niet merkbaar verschuift.",
    ),
    dict(
        type="invultekst",
        vraag="Welke letter staat in B(n, p) voor het aantal experimenten? Eén letter.",
        antwoord=["n"],
        uitleg="n is het aantal experimenten, p de kans op succes bij één experiment.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij X ~ B(n, p) moet p groter zijn dan nul komma één.",
        antwoord=False,
        uitleg="Elke p tussen nul en één mag. Bij een heel kleine p is de kans op nul successen bijna één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je telt hoeveel van de zes worpen met een dobbelsteen een zes geven. Wat is P(X = 0) ongeveer?",
        opties=[
            "drieëndertig procent",
            "zeventien procent",
            "vijftig procent",
            "zestig procent",
        ],
        antwoord=0,
        uitleg="Vijf zesde tot de zesde is ongeveer nul komma drieëndertig. Zes worpen geven dus vaak geen enkele zes.",
    ),
]
