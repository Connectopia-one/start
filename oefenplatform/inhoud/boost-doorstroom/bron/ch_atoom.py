# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — De bouw van atomen en ionen.

Hoort bij "atoom- en molecuulbouw" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_pse] en [ch_bindingen]. Samen 20 % van het
examen.

Deel 1 gaat over de elementaire deeltjes, het atoomnummer en het massagetal, en
over het aantal protonen, neutronen en elektronen in een atoom of een ion.
Deel 2 gaat over de relatieve en de absolute massa, de atoommassa-eenheid, en de
elektronenconfiguratie volgens Bohr voor de eerste achttien elementen.

De fiche spreekt af dat de relatieve atoommassa uit het periodiek systeem op
0,1 afgerond wordt, en geeft u = 1,66.10⁻²⁷ kg mee als tabelwaarde.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke deeltjes zitten in de atoomkern?",
        opties=[
            "protonen en neutronen",
            "protonen en elektronen",
            "elektronen en neutronen",
            "enkel elektronen",
        ],
        antwoord=0,
        uitleg="De kern bevat de protonen en de neutronen, samen de nucleonen. De elektronen bewegen eromheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lading heeft een proton?",
        opties=[
            "positief",
            "negatief",
            "geen lading",
            "soms positief, soms negatief",
        ],
        antwoord=0,
        uitleg="Een proton heeft de eenheidslading +1, een elektron −1, en een neutron is ongeladen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het neutron zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het zit in de kern",
            "het heeft geen lading",
            "het draait rond de kern",
            "het is lichter dan een elektron",
        ],
        antwoord=[0, 1],
        uitleg="Een neutron is een nucleon, dus zit het in de kern, en het is ongeladen. Het weegt ongeveer hetzelfde als een proton en dus veel meer dan een elektron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het atoomnummer van een element?",
        opties=[
            "het aantal protonen in de kern",
            "het aantal neutronen in de kern",
            "het aantal nucleonen samen",
            "de massa van het atoom in gram",
        ],
        antwoord=0,
        uitleg="Het atoomnummer Z is het aantal protonen. Dat bepaalt om welk element het gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het massagetal van een atoom?",
        opties=[
            "het aantal protonen en neutronen samen",
            "het aantal protonen alleen",
            "het aantal elektronen alleen",
            "de massa in kilogram",
        ],
        antwoord=0,
        uitleg="Het massagetal A telt alle nucleonen. De elektronen tellen niet mee, want hun massa is verwaarloosbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een atoom heeft atoomnummer 17 en massagetal 35. Hoeveel neutronen zitten er in de kern?",
        opties=[
            "achttien",
            "zeventien",
            "vijfendertig",
            "tweeënvijftig",
        ],
        antwoord=0,
        uitleg="Het aantal neutronen is het massagetal min het atoomnummer: 35 min 17 is 18.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een neutraal atoom zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het heeft evenveel elektronen als protonen",
            "zijn atoomnummer geeft het aantal elektronen",
            "het heeft evenveel neutronen als protonen",
            "zijn massagetal geeft het aantal elektronen",
        ],
        antwoord=[0, 1],
        uitleg="Neutraal betekent dat de plus- en de minladingen elkaar opheffen. Het aantal neutronen staat daar los van, en het massagetal telt de nucleonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ion?",
        opties=[
            "een atoom dat elektronen heeft opgenomen of afgegeven",
            "een atoom met een extra neutron in de kern",
            "een molecule van twee gelijke atomen",
            "een atoom zonder kern",
        ],
        antwoord=0,
        uitleg="Door elektronen op te nemen of af te geven is het aantal plus- en minladingen niet meer gelijk. Het deeltje krijgt daardoor een lading.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een deeltje heeft elf protonen en tien elektronen. Wat is het?",
        opties=[
            "een positief ion",
            "een negatief ion",
            "een neutraal atoom",
            "een molecule",
        ],
        antwoord=0,
        uitleg="Er is één proton meer dan elektronen, dus is de lading +1. Natrium geeft net één elektron af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen heeft het ion Cl¹⁻, als chloor atoomnummer 17 heeft?",
        opties=[
            "achttien",
            "zestien",
            "zeventien",
            "vijfendertig",
        ],
        antwoord=0,
        uitleg="Een negatieve lading van één betekent één elektron meer dan protonen: 17 plus 1 is 18.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen heeft het ion Mg²⁺, als magnesium atoomnummer 12 heeft?",
        opties=[
            "tien",
            "veertien",
            "twaalf",
            "vierentwintig",
        ],
        antwoord=0,
        uitleg="Twee positieve ladingen betekent twee elektronen minder dan protonen: 12 min 2 is 10.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal protonen bepaalt om welk element het gaat.",
        antwoord=True,
        uitleg="Elk element heeft zijn eigen atoomnummer. Verander je het aantal protonen, dan heb je een ander element.",
    ),
    dict(
        type="waarofniet",
        vraag="De massa van een elektron is ongeveer gelijk aan die van een proton.",
        antwoord=False,
        uitleg="Een elektron is bijna tweeduizend keer lichter. Daarom zit vrijwel de hele massa van een atoom in de kern.",
    ),
    dict(
        type="waarofniet",
        vraag="Een atoom is volledig gevuld met massa, zonder lege ruimte.",
        antwoord=False,
        uitleg="De kern is heel klein tegenover het hele atoom, en de elektronen bewegen op grote afstand. Het grootste deel is dus lege ruimte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een positief ion ontstaat doordat een atoom protonen afgeeft.",
        antwoord=False,
        uitleg="Alleen elektronen bewegen. Geeft een atoom elektronen af, dan blijven er meer protonen over en wordt het positief.",
    ),
    dict(
        type="waarofniet",
        vraag="Protonen en neutronen worden samen nucleonen genoemd.",
        antwoord=True,
        uitleg="Nucleon betekent kerndeeltje. Het massagetal telt precies die deeltjes.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel neutronen zitten in een atoom met atoomnummer 26 en massagetal 56?",
        antwoord=["30", "dertig"],
        uitleg="56 min 26 is 30 neutronen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een negatief geladen elementair deeltje dat rond de kern beweegt?",
        antwoord=["elektron", "een elektron", "het elektron"],
        uitleg="Het elektron heeft de eenheidslading −1 en een verwaarloosbare massa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel protonen heeft het ion O²⁻, als zuurstof atoomnummer 8 heeft?",
        antwoord=["8", "acht"],
        uitleg="Het aantal protonen verandert nooit bij het vormen van een ion. Alleen het aantal elektronen gaat van 8 naar 10.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de deeltjes in de kern, protonen en neutronen samen?",
        antwoord=["nucleonen", "de nucleonen", "nucleon"],
        uitleg="Het massagetal is precies het aantal nucleonen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de relatieve atoommassa van een element?",
        opties=[
            "de massa van het atoom vergeleken met de eenheid u",
            "de massa van het atoom uitgedrukt in kilogram",
            "het aantal protonen in de kern van het atoom",
            "het aantal elektronen in de buitenste schil",
        ],
        antwoord=0,
        uitleg="De relatieve atoommassa is een verhouding en heeft dus geen eenheid. Je leest ze af in het periodiek systeem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de atoommassa-eenheid u?",
        opties=[
            "1,66.10⁻²⁷ kg",
            "6,02.10²³ kg",
            "1,66.10²⁷ kg",
            "9,11.10⁻³¹ kg",
        ],
        antwoord=0,
        uitleg="Die waarde staat in de bijlage die je op het examen mag gebruiken. Ze is ongeveer de massa van één nucleon.",
    ),
    dict(
        type="meerkeuze",
        vraag="De relatieve atoommassa van koolstof is 12,0. Wat is de absolute massa van één koolstofatoom?",
        opties=[
            "1,99.10⁻²⁶ kg",
            "1,99.10⁻²⁷ kg",
            "1,38.10⁻²⁸ kg",
            "7,23.10²² kg",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt de relatieve massa met u: 12,0 keer 1,66.10⁻²⁷ kg is 1,99.10⁻²⁶ kg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft de elektronenconfiguratie volgens Bohr?",
        opties=[
            "hoe de elektronen over de schillen verdeeld zijn",
            "hoeveel neutronen er in de kern van het atoom zitten",
            "welke lading de kern van het atoom in het geheel heeft",
            "hoe snel een atoom beweegt",
        ],
        antwoord=0,
        uitleg="In het model van Bohr liggen de elektronen in schillen met elk een eigen energieniveau. De configuratie zegt hoeveel er in elke schil zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het schillenmodel van Bohr zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de eerste schil bevat maximaal twee elektronen",
            "de schillen worden van binnen naar buiten gevuld",
            "elke schil bevat maximaal acht elektronen",
            "de elektronen zitten mee in de atoomkern",
        ],
        antwoord=[0, 1],
        uitleg="De eerste schil is met twee elektronen vol, dus is helium al een edelgas. De tweede en de derde gaan tot acht, maar niet elke schil blijft daarbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de elektronenconfiguratie van natrium, met atoomnummer 11?",
        opties=[
            "2, 8, 1",
            "2, 9",
            "8, 2, 1",
            "2, 8, 8, 1",
        ],
        antwoord=0,
        uitleg="Je vult de schillen van binnen naar buiten: twee in de eerste, acht in de tweede, en de laatste blijft over voor de derde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de elektronenconfiguratie van zuurstof, met atoomnummer 8?",
        opties=[
            "2, 6",
            "2, 8",
            "6, 2",
            "2, 4, 2",
        ],
        antwoord=0,
        uitleg="Twee elektronen vullen de eerste schil en de overige zes gaan in de tweede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen hebben een volledig gevulde buitenste schil? Kruis alles aan wat juist is.",
        opties=[
            "helium",
            "argon",
            "natrium",
            "chloor",
        ],
        antwoord=[0, 1],
        uitleg="Helium en argon zijn edelgassen en hebben een volle buitenste schil. Natrium heeft er één te veel en chloor één te weinig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de edelgasconfiguratie?",
        opties=[
            "een volledig gevulde buitenste schil",
            "een kern zonder neutronen",
            "een atoom met evenveel protonen als neutronen",
            "een atoom met één elektron in de buitenste schil",
        ],
        antwoord=0,
        uitleg="Die toestand is bijzonder stabiel. Atomen nemen elektronen op of geven ze af om die configuratie te bereiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft een natriumatoom liever één elektron af dan er zeven op te nemen?",
        opties=[
            "met één minder heeft het al een volle buitenste schil",
            "zeven elektronen passen niet in zijn buitenste schil",
            "een negatief geladen natriumion kan niet bestaan",
            "natrium heeft geen buitenste schil",
        ],
        antwoord=0,
        uitleg="Natrium heeft de configuratie 2, 8, 1. Geeft het dat ene elektron af, dan blijft 2, 8 over, de configuratie van neon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stelt men het elektron-stipmodel van een atoom voor?",
        opties=[
            "met stippen rond het symbool voor de buitenste elektronen",
            "met een getal boven het symbool voor het massagetal",
            "met pijlen die de bewegingsrichting van de kern aangeven",
            "met kleuren voor de verschillende soorten atomen",
        ],
        antwoord=0,
        uitleg="Elke stip is één elektron uit de buitenste schil. Zo zie je meteen hoeveel valentie-elektronen het atoom heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="De relatieve atoommassa wordt uitgedrukt in gram.",
        antwoord=False,
        uitleg="Het is een verhouding tussen twee massa's, dus vallen de eenheden weg. De molaire massa heeft wel een eenheid, g/mol.",
    ),
    dict(
        type="waarofniet",
        vraag="De tweede schil van een atoom kan maximaal acht elektronen bevatten.",
        antwoord=True,
        uitleg="Bij de eerste achttien elementen vult de tweede schil tot acht, en pas daarna begint de derde.",
    ),
    dict(
        type="waarofniet",
        vraag="Vrijwel de hele massa van een atoom zit in de kern.",
        antwoord=True,
        uitleg="Protonen en neutronen zijn bijna tweeduizend keer zwaarder dan een elektron, en ze zitten allemaal in de kern.",
    ),
    dict(
        type="waarofniet",
        vraag="De absolute massa van een atoom bereken je door de relatieve massa door u te delen.",
        antwoord=False,
        uitleg="Je moet er juist mee vermenigvuldigen. Delen zou een onmogelijk groot getal geven.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal elektronen in de buitenste schil zegt niets over de eigenschappen van een element.",
        antwoord=False,
        uitleg="Net die elektronen doen mee aan de bindingen. Daarom lijken elementen uit dezelfde groep zo op elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel elektronen passen er maximaal in de tweede schil van een atoom?",
        antwoord=["8", "acht"],
        uitleg="Na acht elektronen is de tweede schil vol, en dat is net de edelgasconfiguratie van neon.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de elektronenconfiguratie van chloor, met atoomnummer 17? Schrijf de aantallen met komma's.",
        antwoord=["2, 8, 7", "2,8,7"],
        uitleg="Twee in de eerste schil, acht in de tweede en zeven in de derde. Eén elektron te weinig voor een volle schil, dus wordt chloor makkelijk een negatief ion.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de bijzonder stabiele toestand van een atoom met een volledig gevulde buitenste schil?",
        antwoord=["edelgasconfiguratie", "de edelgasconfiguratie"],
        uitleg="Atomen nemen elektronen op of staan ze af om die toestand te bereiken.",
    ),
    dict(
        type="invultekst",
        vraag="De relatieve atoommassa van helium is 4,0. Hoeveel is de absolute massa van één heliumatoom in kg? Noteer in wetenschappelijke notatie met drie beduidende cijfers.",
        antwoord=["6,64.10-27", "6,64.10⁻²⁷", "6,64e-27"],
        uitleg="4,0 keer 1,66.10⁻²⁷ kg geeft 6,64.10⁻²⁷ kg.",
    ),
]
