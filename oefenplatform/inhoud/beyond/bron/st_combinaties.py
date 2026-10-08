# -*- coding: utf-8 -*-
"""Faculteit en combinaties.

De vakfiche is hier heel precies, en het is belangrijk om dat te volgen: ze
vraagt alleen **telproblemen zonder herhaling waarbij de volgorde niet
belangrijk is**, dus combinaties, plus de faculteit. Permutaties en
variaties staan er níét in. Schrijf er dus ook geen vragen over, want dan
toets je iets wat op dit examen niet gevraagd wordt.

De notatie van het formularium is C(n,p) = n! / (p! · (n−p)!), en in de
bijlage "Begrippen & notaties" staat ze als C met n boven en p onder. Wij
schrijven in de vragen "C(n, p)", want een kind kan dat intikken.

Deel 1 is de faculteit en wat een combinatie is.
Deel 2 is rekenen met combinaties in opgaven met context.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent 5! ?",
        opties=[
            "vijf maal vier maal drie maal twee maal één",
            "vijf maal vijf maal vijf maal vijf maal vijf",
            "vijf plus vier plus drie plus twee plus één",
            "vijf gedeeld door vier gedeeld door drie",
        ],
        antwoord=0,
        uitleg="Een faculteit is het product van alle natuurlijke getallen van één tot en met dat getal. 5! = 120.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 6! ?",
        opties=["720", "120", "36", "30"],
        antwoord=0,
        uitleg="6! = 6 · 5 · 4 · 3 · 2 · 1 = 720. Let op: 120 is 5!, en een faculteit groeit erg snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 0! ?",
        opties=["één", "nul", "dat bestaat niet", "oneindig"],
        antwoord=0,
        uitleg="Per afspraak is 0! gelijk aan 1. Dat is nodig om de formule van de combinaties te laten werken.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een combinatie maakt de volgorde van de gekozen elementen niets uit.",
        antwoord=True,
        uitleg="Precies daarom gebruik je een combinatie: de ploeg Ann, Bo en Cis is dezelfde ploeg als Cis, Bo en Ann.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule staat in het formularium voor het aantal combinaties van p elementen uit n elementen?",
        opties=[
            "n! gedeeld door p! maal (n−p)!",
            "n! gedeeld door (n−p)!",
            "n! maal p! gedeeld door (n−p)",
            "n maal p gedeeld door (n−p)",
        ],
        antwoord=0,
        uitleg="C(n, p) = n! / (p! · (n−p)!). Het p! onderaan haalt er juist de volgordes uit die je niet wil meetellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is C(5, 2) ?",
        opties=["tien", "twintig", "vijfentwintig", "zeven"],
        antwoord=0,
        uitleg="5! / (2! · 3!) = 120 / 12 = 10. Twintig zou het antwoord zijn als de volgorde wél meetelde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is C(6, 2) ? Geef het getal in cijfers.",
        antwoord=["15"],
        uitleg="6! / (2! · 4!) = 720 / 48 = 15.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is C(10, 1) ?",
        opties=["tien", "één", "honderd", "negen"],
        antwoord=0,
        uitleg="Eén element uit tien kiezen kan op tien manieren. Dat klopt ook met de formule.",
    ),
    dict(
        type="waarofniet",
        vraag="C(n, 0) is voor elke n gelijk aan één.",
        antwoord=True,
        uitleg="Niets kiezen kan op juist één manier: de lege keuze. In de formule wordt dat n! / (0! · n!) = 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geldt C(8, 3) = C(8, 5) ?",
        opties=[
            "wie drie kiest, laat er juist vijf liggen, dus het zijn dezelfde keuzes",
            "omdat drie plus vijf gelijk is aan acht en de formule dan altijd klopt",
            "dat is toeval, bij andere getallen gaat die gelijkheid niet op",
            "omdat acht een even getal is en dat de breuk symmetrisch maakt",
        ],
        antwoord=0,
        uitleg="Elke keuze van drie hoort bij juist één groepje van vijf dat overblijft. Dat heet de symmetrie van de combinaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas van twintig leerlingen kiest de leraar twee leerlingen om het bord te wissen. Hoeveel paren zijn er mogelijk?",
        opties=["190", "380", "400", "40"],
        antwoord=0,
        uitleg="C(20, 2) = 20 · 19 / 2 = 190. Je deelt door twee omdat Ann met Bo hetzelfde paar is als Bo met Ann.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een telprobleem waarbij de volgorde belangrijk is, gebruik je een combinatie.",
        antwoord=False,
        uitleg="Dan tel je anders. De vakfiche vraagt enkel de gevallen waarbij de volgorde niet belangrijk is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kiest drie boeken uit tien om mee te nemen op reis. Welke berekening hoort daarbij?",
        opties=["C(10, 3)", "C(3, 10)", "10! gedeeld door 3", "tien maal drie"],
        antwoord=0,
        uitleg="Je kiest er drie uit tien en de volgorde in je koffer doet niets, dus C(10, 3) = 120.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is C(7, 3) ? Geef het getal in cijfers.",
        antwoord=["35"],
        uitleg="7! / (3! · 4!) = 5040 / 144 = 35.",
    ),
    dict(
        type="waarofniet",
        vraag="C(n, p) kan nooit een breuk zijn, ook al staat er een deling in de formule.",
        antwoord=True,
        uitleg="Je telt aantallen groepjes, dus de uitkomst is altijd een natuurlijk getal. Krijg je een breuk, dan is er een rekenfout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er p! in de noemer van de formule van de combinaties?",
        opties=[
            "om de volgordes van de gekozen elementen weer weg te delen",
            "om de elementen die je niet gekozen hebt mee te kunnen tellen",
            "om de uitkomst klein genoeg te houden voor een rekentoestel",
            "om het verschil tussen n en p in de teller te compenseren",
        ],
        antwoord=0,
        uitleg="Zonder dat p! zou je elke groep p! keer tellen, één keer voor elke manier om ze te ordenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een jury van vijf wordt gekozen uit negen kandidaten. Hoeveel jury's zijn er mogelijk?",
        opties=["126", "15120", "45", "59049"],
        antwoord=0,
        uitleg="C(9, 5) = 126. Het grote getal 15120 komt uit de berekening waarbij de volgorde wél meetelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Op het examen volstaat het om bij een telprobleem enkel de uitkomst van C(n, p) te noteren.",
        antwoord=False,
        uitleg="De fiche vraagt dat je je werkwijze en je redenering noteert en alle tussenstappen uitschrijft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het product van alle getallen van één tot n? Eén woord.",
        antwoord=["faculteit", "de faculteit"],
        uitleg="De faculteit van n, genoteerd n!.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet uit vier vrienden twee kiezen om mee te gaan. Je rekent 4 · 3 = 12 uit. Wat ging er mis?",
        opties=[
            "je telde elk paar twee keer, het antwoord is zes",
            "je hebt een vriend vergeten, het antwoord is zestien",
            "er ging niets mis, twaalf is het juiste antwoord",
            "je moest optellen in plaats van vermenigvuldigen, dus zeven",
        ],
        antwoord=0,
        uitleg="C(4, 2) = 6. Twaalf is het aantal geordende paren; deel nog door 2! om de volgorde weg te werken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Uit een groep van twaalf spelers wordt een ploeg van vijf gekozen. Hoeveel ploegen zijn mogelijk?",
        opties=["792", "95040", "60", "248832"],
        antwoord=0,
        uitleg="C(12, 5) = 792. Het getal 95040 hoort bij een keuze waarbij de volgorde meetelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij de Lotto kies je zes getallen uit vijfenveertig. Welke berekening geeft het aantal mogelijke roosters?",
        opties=["C(45, 6)", "C(6, 45)", "45 maal 6", "45! gedeeld door 6"],
        antwoord=0,
        uitleg="De volgorde waarin je de bolletjes aankruist doet niets, dus C(45, 6).",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is C(10, 2) ? Geef het getal in cijfers.",
        antwoord=["45"],
        uitleg="10 · 9 / 2 = 45.",
    ),
    dict(
        type="waarofniet",
        vraag="In een toernooi waar elke ploeg één keer tegen elke andere speelt, is het aantal wedstrijden C(n, 2).",
        antwoord=True,
        uitleg="Elke wedstrijd is een paar ploegen, en wie thuis speelt doet voor het aantal paren niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een toernooi met tien ploegen speelt elke ploeg één keer tegen elke andere. Hoeveel wedstrijden zijn dat?",
        opties=["vijfenveertig", "negentig", "honderd", "twintig"],
        antwoord=0,
        uitleg="C(10, 2) = 45. Negentig zou je krijgen als elke ploeg ook een terugwedstrijd speelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker heeft acht soorten gebak. Je koopt er drie verschillende. Hoeveel keuzes heb je?",
        opties=["zesenvijftig", "vijfhonderdtwaalf", "driehonderdzesendertig", "vierentwintig"],
        antwoord=0,
        uitleg="C(8, 3) = 56. Vijfhonderdtwaalf (acht tot de derde) zou gelden als je dezelfde soort mocht herhalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Zodra herhaling toegelaten is, mag je de formule van de combinaties niet meer gebruiken.",
        antwoord=True,
        uitleg="C(n, p) is gemaakt voor keuzes zonder herhaling. De fiche vraagt enkel die gevallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een commissie van drie wordt gekozen uit vijf vrouwen en vier mannen, met minstens één vrouw. Hoeveel commissies zijn er?",
        opties=["tachtig", "vierentachtig", "zestig", "vierentwintig"],
        antwoord=0,
        uitleg="C(9, 3) = 84 in het totaal, min de C(4, 3) = 4 commissies zonder vrouw: 84 − 4 = 80. Dat is de complementregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas van vijfentwintig kiest drie afgevaardigden, zonder onderscheid in rol. Hoeveel groepjes kan dat geven?",
        opties=["2300", "13800", "15625", "75"],
        antwoord=0,
        uitleg="C(25, 3) = 2300. Het getal 13800 geldt als de drie rollen verschillend zouden zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is C(6, 3) ? Geef het getal in cijfers.",
        antwoord=["20"],
        uitleg="720 / (6 · 6) = 20.",
    ),
    dict(
        type="waarofniet",
        vraag="Om twee kinderen uit een groep van dertig te kiezen zijn er 870 mogelijkheden.",
        antwoord=False,
        uitleg="870 is 30 · 29, dus met de volgorde mee. C(30, 2) = 870 / 2 = 435.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je maakt een fruitsalade met vier verschillende soorten uit zeven. Hoeveel salades zijn mogelijk?",
        opties=["vijfendertig", "tweeduizendvierhonderd", "achtentwintig", "achthonderdveertig"],
        antwoord=0,
        uitleg="C(7, 4) = C(7, 3) = 35. Door de symmetrie reken je het liefst met het kleinste van de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit zes rode en vier blauwe knikkers kies je er drie rode. Hoeveel manieren zijn er?",
        opties=["twintig", "honderdtwintig", "veertig", "zestig"],
        antwoord=0,
        uitleg="De blauwe knikkers doen niets mee: C(6, 3) = 20.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hand van vijf kaarten uit een spel van tweeënvijftig is een combinatie en geen geordende keuze.",
        antwoord=True,
        uitleg="De kaarten in je hand liggen niet in een vaste volgorde, dus C(52, 5).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reisbureau biedt twaalf steden aan. Je bezoekt er twee. Hoeveel combinaties van steden zijn er?",
        opties=["zesenzestig", "honderdtweeëndertig", "honderdvierenveertig", "vierentwintig"],
        antwoord=0,
        uitleg="C(12, 2) = 12 · 11 / 2 = 66.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe pak je een telprobleem met de voorwaarde minstens twee aan?",
        opties=[
            "je telt de gevallen met nul en met één en trekt die van het totaal af",
            "je rekent enkel het geval met juist twee uit, dat is de ondergrens",
            "je vermenigvuldigt het totaal met twee, want twee is de drempel",
            "je telt de gevallen met twee en met drie op en stopt daar",
        ],
        antwoord=0,
        uitleg="Minstens twee is het complement van nul of één. De complementregel is hier bijna altijd de kortste weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is C(11, 2) ? Geef het getal in cijfers.",
        antwoord=["55"],
        uitleg="11 · 10 / 2 = 55.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij C(18, 3) is het handig om eerst 18! volledig uit te rekenen.",
        antwoord=False,
        uitleg="Dat getal is onwerkbaar groot. Reken met 18 · 17 · 16 / (3 · 2 · 1) = 816.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school kiest uit zestien kandidaten twee vertegenwoordigers. Hoeveel paren zijn mogelijk?",
        opties=["honderdtwintig", "tweehonderdveertig", "tweehonderdzesenvijftig", "tweeëndertig"],
        antwoord=0,
        uitleg="C(16, 2) = 16 · 15 / 2 = 120.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling berekent C(9, 4) en krijgt 3024. Wat is er gebeurd?",
        opties=[
            "de deling door 4! is vergeten, het antwoord is honderdzesentwintig",
            "er is met 9! gerekend in plaats van met 9, dus het antwoord is negen",
            "de teller en de noemer zijn verwisseld, het antwoord is een breuk",
            "er is opgeteld in plaats van vermenigvuldigd, het antwoord is dertien",
        ],
        antwoord=0,
        uitleg="9 · 8 · 7 · 6 = 3024, maar dat is de geordende keuze. Delen door 4! = 24 geeft 126.",
    ),
]
