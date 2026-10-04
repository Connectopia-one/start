# -*- coding: utf-8 -*-
"""Chemisch rekenen: mol, molaire massa en concentratie — 🌍 Beyond, chemie.

Deel 1 gaat over de mol: het getal van Avogadro, het verband tussen massa,
molaire massa en stofhoeveelheid, en de massadichtheid. Deel 2 gaat over
oplossingen: de molaire concentratie, de massaconcentratie, massaprocent,
volumeprocent, promille, ppm en ppb, de verdunningsregel, en het afleiden van
een formule uit de procentuele samenstelling.

Alle getallen in de vragen zijn zo gekozen dat ze zonder rekentoestel uitkomen,
en de nodige molaire massa staat telkens in de vraag. Het kind krijgt op het
examen immers een rekenapp en een periodiek systeem, maar het moet zelf weten
welke formule het nodig heeft.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel deeltjes zitten er in één mol van een stof?",
        opties=[
            "6,022 × 10²³",
            "6,022 × 10²²",
            "3,011 × 10²³",
            "1,000 × 10²³",
        ],
        antwoord=0,
        uitleg="Dat is het getal van Avogadro. Het geldt voor atomen, moleculen en ionen "
        "evengoed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de molaire massa van water, als H 1 g/mol en O 16 g/mol weegt?",
        opties=[
            "18 g/mol",
            "17 g/mol",
            "20 g/mol",
            "34 g/mol",
        ],
        antwoord=0,
        uitleg="Twee keer 1 plus 16 is 18. Eén mol water weegt dus 18 gram.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol water zit er in 36 gram water, met een molaire massa van 18 g/mol?",
        antwoord=["2", "2 mol", "twee"],
        uitleg="n is m gedeeld door M: 36 gedeeld door 18 is 2 mol. Daarin zitten dus "
        "twee keer het getal van Avogadro aan moleculen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de stofhoeveelheid uit de massa?",
        opties=[
            "n is gelijk aan m gedeeld door M",
            "n is gelijk aan m maal M",
            "n is gelijk aan M gedeeld door m",
            "n is gelijk aan m gedeeld door V",
        ],
        antwoord=0,
        uitleg="De molaire massa M is de massa van één mol. Deel je de massa erdoor, dan "
        "weet je hoeveel mol je hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén mol zuurstofgas en één mol waterstofgas bevatten evenveel moleculen.",
        antwoord=True,
        uitleg="Het aantal is altijd het getal van Avogadro. Hun massa verschilt wel: "
        "32 gram tegenover 2 gram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel weegt 0,5 mol koolstofdioxide, met een molaire massa van 44 g/mol?",
        opties=[
            "22 gram",
            "44 gram",
            "88 gram",
            "11 gram",
        ],
        antwoord=0,
        uitleg="m is n maal M: 0,5 maal 44 is 22 gram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden heb je nodig om de massadichtheid te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de massa van de stof",
            "het volume van de stof",
            "de molaire massa van de stof",
            "het aantal deeltjes in de stof",
        ],
        antwoord=[0, 1],
        uitleg="De massadichtheid is massa per volume, bijvoorbeeld in g/cm³. Voor water "
        "is dat ongeveer 1 g/cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over één mol ijzer zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het bevat 6,022 × 10²³ atomen",
            "het weegt 56 gram als de molaire massa 56 g/mol is",
            "het bevat 56 atomen ijzer",
            "het weegt altijd evenveel als één mol koper",
        ],
        antwoord=[0, 1],
        uitleg="Het aantal deeltjes in een mol staat vast, de massa niet: die hangt af "
        "van de molaire massa van het element.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel gram weegt 2 mol natriumchloride, met een molaire massa van 58,5 g/mol?",
        antwoord=["117", "117 g", "117 gram"],
        uitleg="Twee keer 58,5 is 117 gram. Dat is dus twee keer het getal van Avogadro "
        "aan formule-eenheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel moleculen zitten er in 2 mol van een stof?",
        opties=[
            "ongeveer 1,2 × 10²⁴",
            "ongeveer 1,2 × 10²³",
            "ongeveer 3,0 × 10²³",
            "ongeveer 6,0 × 10²³",
        ],
        antwoord=0,
        uitleg="Twee keer 6,022 × 10²³ is 1,2044 × 10²⁴. Let op het verspringen van de "
        "exponent bij het verdubbelen.",
    ),
    dict(
        type="waarofniet",
        vraag="De molaire massa van een stof heeft als eenheid gram per mol.",
        antwoord=True,
        uitleg="Ze zegt hoeveel één mol weegt. De getalwaarde is dezelfde als die van de "
        "molecuulmassa in atomaire eenheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de molaire massa van zwavelzuur H₂SO₄, met H 1, S 32 en O 16 g/mol?",
        opties=[
            "98 g/mol",
            "96 g/mol",
            "82 g/mol",
            "114 g/mol",
        ],
        antwoord=0,
        uitleg="Twee keer 1, plus 32, plus vier keer 16: 2 plus 32 plus 64 is 98.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk volume neemt één mol gas in bij normomstandigheden?",
        opties=[
            "22,4 liter",
            "24,0 liter",
            "1,0 liter",
            "18,0 liter",
        ],
        antwoord=0,
        uitleg="Dat is het molair volume bij 0 °C en normale druk. Het is voor elk gas "
        "ongeveer gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de stofhoeveelheid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "haar symbool is n",
            "haar eenheid is de mol",
            "haar eenheid is het gram",
            "haar symbool is M",
        ],
        antwoord=[0, 1],
        uitleg="M is de molaire massa, met gram per mol als eenheid. De stofhoeveelheid n "
        "wordt in mol uitgedrukt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol is 100 gram calciumcarbonaat, met een molaire massa van 100 g/mol?",
        antwoord=["1", "1 mol", "een"],
        uitleg="Honderd gedeeld door honderd is één mol. Daarin zitten één mol "
        "calciumionen en één mol carbonaationen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel mol zuurstofatomen zitten er in één mol zwavelzuur, H₂SO₄?",
        opties=[
            "vier mol",
            "een mol",
            "twee mol",
            "zeven mol",
        ],
        antwoord=0,
        uitleg="Per molecule zitten er vier zuurstofatomen, dus per mol vier mol atomen. "
        "Zo reken je ook de molaire massa uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de massa van 3 mol waterstofgas, met een molaire massa van 2 g/mol?",
        opties=[
            "6 gram",
            "3 gram",
            "1,5 gram",
            "2 gram",
        ],
        antwoord=0,
        uitleg="Drie maal twee is zes gram. Waterstofgas is H₂, dus twee gram per mol en "
        "niet één.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén mol van een gas neemt altijd 22,4 liter in, bij elke temperatuur.",
        antwoord=False,
        uitleg="Dat geldt enkel bij normomstandigheden. Warm je het gas op, dan zet het "
        "uit en neemt het meer plaats in.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee stoffen met dezelfde massa bevatten altijd hetzelfde aantal mol.",
        antwoord=False,
        uitleg="Alleen als hun molaire massa gelijk is. Achttien gram water is één mol, "
        "achttien gram glucose maar een tiende van een mol.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid heeft als eenheid gram per kubieke centimeter?",
        antwoord=["massadichtheid", "dichtheid", "de dichtheid"],
        uitleg="Ze zegt hoeveel massa er in een bepaald volume zit. Voor water is dat "
        "ongeveer 1 g/cm³, voor ijzer bijna 8.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de molaire concentratie van een oplossing met 0,5 mol opgeloste stof in 2 liter?",
        opties=[
            "0,25 mol/L",
            "1,0 mol/L",
            "2,5 mol/L",
            "0,5 mol/L",
        ],
        antwoord=0,
        uitleg="c is n gedeeld door V: 0,5 gedeeld door 2 is 0,25 mol per liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een massaprocent van 5 % in een oplossing?",
        opties=[
            "5 gram opgeloste stof per 100 gram oplossing",
            "5 gram opgeloste stof per 100 milliliter water",
            "5 mol opgeloste stof per 100 gram oplossing",
            "5 milliliter opgeloste stof per 100 gram water",
        ],
        antwoord=0,
        uitleg="Let op het woord oplossing: de massa van het oplosmiddel én van de "
        "opgeloste stof samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel gram zout zit er in 200 gram oplossing van 10 massaprocent?",
        antwoord=["20", "20 g", "20 gram"],
        uitleg="Tien procent van 200 gram is 20 gram zout, en dus 180 gram water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij de verdunningsregel?",
        opties=[
            "c₁ maal V₁ is gelijk aan c₂ maal V₂",
            "c₁ gedeeld door V₁ is gelijk aan c₂ gedeeld door V₂",
            "c₁ plus V₁ is gelijk aan c₂ plus V₂",
            "c₁ maal c₂ is gelijk aan V₁ maal V₂",
        ],
        antwoord=0,
        uitleg="Bij verdunnen blijft het aantal mol opgeloste stof gelijk. Alleen het "
        "volume verandert, en dus de concentratie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het verdunnen van een oplossing blijft het aantal mol opgeloste stof gelijk.",
        antwoord=True,
        uitleg="Je giet er enkel water bij. Daardoor daalt de concentratie, terwijl er "
        "evenveel deeltjes in de beker blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdunt 10 mL van een oplossing van 2 mol/L tot 100 mL. Wat is de nieuwe concentratie?",
        opties=[
            "0,2 mol/L",
            "0,02 mol/L",
            "2,0 mol/L",
            "20 mol/L",
        ],
        antwoord=0,
        uitleg="Het volume wordt tien keer groter, dus de concentratie tien keer kleiner: "
        "2 gedeeld door 10 is 0,2 mol/L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 1 ppm voor een stof in water? Kruis alles aan wat juist is.",
        opties=[
            "één deel op een miljoen",
            "1 milligram per liter water",
            "één deel op duizend",
            "1 gram per liter water",
        ],
        antwoord=[0, 1],
        uitleg="Ppm is één deel op een miljoen. Omdat een liter water duizend gram weegt, "
        "komt dat op één milligram per liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke concentratie-uitdrukkingen gebruiken een massa in de teller? Kruis alles aan wat juist is.",
        opties=[
            "de massaconcentratie",
            "het massaprocent",
            "de molaire concentratie",
            "het volumeprocent",
        ],
        antwoord=[0, 1],
        uitleg="De molaire concentratie rekent in mol per liter, het volumeprocent in "
        "milliliter per 100 milliliter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol opgeloste stof zit er in 500 mL van een oplossing van 0,2 mol/L?",
        antwoord=["0,1", "0,1 mol", "0.1"],
        uitleg="n is c maal V, met V in liter: 0,2 maal 0,5 is 0,1 mol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wijn van 12 volumeprocent alcohol. Wat betekent dat?",
        opties=[
            "12 mL alcohol per 100 mL wijn",
            "12 gram alcohol per 100 mL wijn",
            "12 mL alcohol per 100 gram wijn",
            "12 mol alcohol per 100 mL wijn",
        ],
        antwoord=0,
        uitleg="Volumeprocent vergelijkt volumes met elkaar. Bij vaste stoffen in een "
        "vloeistof gebruikt men liever massavolumeprocent.",
    ),
    dict(
        type="waarofniet",
        vraag="Promille betekent één deel op duizend.",
        antwoord=True,
        uitleg="Procent is op honderd, promille op duizend, ppm op een miljoen en ppb op "
        "een miljard.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verbinding bestaat uit 40 % koolstof, 6,7 % waterstof en 53,3 % zuurstof. Welke formule past?",
        opties=[
            "CH₂O",
            "C₂H₄O",
            "CHO₂",
            "C₂H₆O",
        ],
        antwoord=0,
        uitleg="Deel elk percentage door de atoommassa: 40/12, 6,7/1 en 53,3/16 geeft "
        "ongeveer 3,3 : 6,7 : 3,3, dus 1 : 2 : 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel massaprocent waterstof zit er in water, met H 1 en O 16 g/mol?",
        opties=[
            "ongeveer 11 %",
            "ongeveer 50 %",
            "ongeveer 33 %",
            "ongeveer 89 %",
        ],
        antwoord=0,
        uitleg="Twee gram waterstof op achttien gram water is 2/18, dus ongeveer 11 "
        "procent. Het aantal atomen en de massa zijn dus twee verschillende dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over ppb zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het staat voor één deel op een miljard",
            "het wordt gebruikt voor heel kleine hoeveelheden",
            "het staat voor één deel op een miljoen",
            "het wordt gebruikt voor concentraties boven één procent",
        ],
        antwoord=[0, 1],
        uitleg="Ppb gebruikt men bijvoorbeeld voor een spoor van een zwaar metaal in "
        "drinkwater. Daar zou procent een veel te grove eenheid zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de molaire concentratie?",
        antwoord=["c", "de c"],
        uitleg="c met als eenheid mol per liter. Men schrijft die eenheid ook als M, "
        "bijvoorbeeld 0,1 M zoutzuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet 250 mL oplossing van 0,4 mol/L maken. Hoeveel mol stof weeg je af?",
        opties=[
            "0,1 mol",
            "0,4 mol",
            "1,0 mol",
            "0,04 mol",
        ],
        antwoord=0,
        uitleg="n is c maal V: 0,4 maal 0,25 liter is 0,1 mol. Die massa weeg je af en je "
        "vult daarna aan tot 250 mL.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vul je bij het maken van een oplossing aan tot de maatstreep en niet eerst het water af?",
        opties=[
            "de opgeloste stof neemt zelf ook plaats in het eindvolume",
            "het water verdampt tijdens het oplossen van de stof",
            "de maatkolf is onnauwkeurig bij kleine volumes water",
            "de stof lost sneller op in een volle maatkolf",
        ],
        antwoord=0,
        uitleg="De concentratie hoort bij het volume van de oplossing, niet bij dat van "
        "het water alleen. Daarom staat er een maatstreep op een maatkolf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing van 1 mol/L bevat altijd één mol opgeloste stof, hoeveel je er ook van neemt.",
        antwoord=False,
        uitleg="Ze bevat één mol per liter. Neem je 100 mL, dan heb je maar 0,1 mol in "
        "handen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het massaprocent van een oplossing verandert niet als je er water bij giet.",
        antwoord=False,
        uitleg="De massa van de oplossing wordt groter terwijl die van de opgeloste stof "
        "gelijk blijft, dus daalt het massaprocent.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel liter is 250 milliliter?",
        antwoord=["0,25", "0,25 L", "0.25"],
        uitleg="Duizend milliliter is één liter. In de formule n is c maal V hoort het "
        "volume altijd in liter.",
    ),
]
