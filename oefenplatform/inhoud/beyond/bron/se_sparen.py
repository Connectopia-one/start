# -*- coding: utf-8 -*-
"""Sparen, beleggen en de invloed van inflatie.

Het derde thema uit "ik beheer mijn financiën". Het tweede leerdoel van dat
blok staat hier helemaal: sparen en beleggingsvormen vergelijken op risico en
rendement.

De drie rekeningen die de fiche naast elkaar zet:
    zichtrekening     voor je dagelijkse verrichtingen
    spaarrekening     om geld opzij te zetten, altijd opvraagbaar
    termijnrekening   geld dat je een afgesproken tijd vastzet

De vier beleggingsvormen, letterlijk uit de fiche:
    de obligatie, de cryptomunt, het beleggingsfonds, het traditionele
    beursaandeel

En de vijf factoren waarmee je kiest tussen sparen en beleggen:
    hoelang je je geld kan missen of wil laten groeien; de rentevoet en de
    inflatie; het risico dat je bereid bent te nemen; je financieel doel;
    je kennis over de financiële markt

De rode draad is de verhouding tussen risico en rendement: meer kans op
opbrengst gaat samen met meer kans op verlies. Dit thema geeft nooit een
beleggingsadvies en noemt geen verwachte rendementen; de fiche vraagt
vergelijken, niet voorspellen.

Deel 1 is sparen, de drie rekeningen en de rente.
Deel 2 is beleggen, risico en rendement, en de inflatie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een zichtrekening?",
        opties=[
            "je dagelijkse verrichtingen: loon ontvangen en betalingen doen",
            "geld voor langere tijd vastzetten tegen een hogere rente",
            "geld opzij zetten dat je niet dagelijks nodig hebt",
            "aandelen kopen en verkopen",
        ],
        antwoord=0,
        uitleg="Op een zichtrekening komt je loon binnen en gaan je facturen af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een spaarrekening?",
        opties=[
            "geld opzij zetten dat je toch nog kan opvragen",
            "je dagelijkse betalingen doen",
            "geld een vaste periode vastzetten",
            "aandelen van bedrijven bewaren",
        ],
        antwoord=0,
        uitleg="Je krijgt er rente op en je kan er toch aan, ook al duurt het soms een dag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een termijnrekening?",
        opties=[
            "geld een afgesproken tijd vastzetten tegen een vaste rente",
            "geld dat je elk moment nodig kan hebben",
            "je loon ontvangen",
            "cryptomunten bewaren",
        ],
        antwoord=0,
        uitleg="Je spreekt een termijn af, en daarom ligt de rente meestal hoger dan op een spaarrekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wil geld opzij zetten dat hij over drie jaar zeker niet nodig heeft. Welke rekening past het best?",
        opties=[
            "een termijnrekening",
            "een zichtrekening",
            "een spaarrekening voor dagelijks gebruik",
            "geen enkele, hij moet beleggen",
        ],
        antwoord=0,
        uitleg="Hij kan het missen, dus hij mag het vastzetten en een hogere rente krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wil elke maand iets opzij zetten maar wil er altijd aan kunnen. Welke rekening past het best?",
        opties=[
            "een spaarrekening",
            "een termijnrekening",
            "een beleggingsfonds",
            "een kredietopening",
        ],
        antwoord=0,
        uitleg="Op een spaarrekening blijft je geld beschikbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is rente?",
        opties=[
            "de vergoeding die je krijgt of betaalt voor het gebruik van geld",
            "het bedrag dat je elke maand op je spaarrekening overschrijft",
            "de kost van een aankoop die je in schijven afbetaalt",
            "de belasting die van je loon wordt afgehouden",
        ],
        antwoord=0,
        uitleg="Wie spaart, krijgt rente. Wie leent, betaalt ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet 2.000 euro op een rekening met 2 procent rente per jaar. Hoeveel rente krijg je na één jaar?",
        opties=["40 euro", "20 euro", "200 euro", "400 euro"],
        antwoord=0,
        uitleg="2 procent van 2.000 is 40 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is samengestelde rente?",
        opties=[
            "rente die je ook op de rente van de vorige jaren krijgt",
            "rente die je maandelijks in plaats van jaarlijks krijgt",
            "rente die uit twee verschillende tarieven bestaat",
            "rente die de bank samen met de kosten berekent",
        ],
        antwoord=0,
        uitleg="Je spaarpot groeit dan sneller naarmate hij langer blijft staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom levert hetzelfde bedrag op een termijnrekening meestal meer op dan op een spaarrekening?",
        opties=[
            "omdat je het voor een afgesproken tijd vastzet",
            "omdat de bank er geen kosten op aanrekent",
            "omdat er geen belasting op betaald wordt",
            "omdat het bedrag groter moet zijn",
        ],
        antwoord=0,
        uitleg="De bank weet hoelang ze over je geld kan beschikken en betaalt daarvoor meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een financieel doel?",
        opties=[
            "waarvoor je spaart of belegt, bijvoorbeeld een studie of een woning",
            "het bedrag dat de bank je op basis van je loon maximaal wil lenen",
            "de rente die je per jaar op je spaargeld wil halen",
            "het verschil tussen je inkomsten en je uitgaven in een maand",
        ],
        antwoord=0,
        uitleg="De fiche noemt het als een van de vijf factoren bij de keuze tussen sparen en beleggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een zichtrekening zet je geld dat je een paar jaar niet nodig hebt.",
        antwoord=False,
        uitleg="De zichtrekening is net voor je dagelijkse verrichtingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een termijnrekening spreek je af hoelang je geld vaststaat.",
        antwoord=True,
        uitleg="Daarvoor krijg je doorgaans een hogere rente.",
    ),
    dict(
        type="waarofniet",
        vraag="Samengestelde rente betekent dat je ook rente krijgt op je eerder verdiende rente.",
        antwoord=True,
        uitleg="Daardoor groeit een spaarpot sneller naarmate hij langer blijft staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan aan het geld op een termijnrekening even makkelijk als aan dat op een spaarrekening.",
        antwoord=False,
        uitleg="Vroeger opvragen kan je op een termijnrekening geld of rente kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie rekeningen zet de fiche naast elkaar?",
        opties=[
            "de zichtrekening",
            "de spaarrekening",
            "de termijnrekening",
            "de effectenrekening",
        ],
        antwoord=[0, 1, 2],
        uitleg="De effectenrekening staat niet in de fiche.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke rekening komt je loon binnen en gaan je facturen af?",
        antwoord=["zichtrekening", "de zichtrekening"],
        uitleg="De spaarrekening en de termijnrekening dienen om geld opzij te zetten.",
    ),
    dict(
        type="invultekst",
        vraag="Je zet 5.000 euro weg tegen 3 procent per jaar. Hoeveel rente is dat na één jaar? Antwoord met een getal.",
        antwoord=["150"],
        uitleg="3 procent van 5.000 is 150 euro.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de rekening waarop je geld een afgesproken tijd vastzet?",
        antwoord=["termijnrekening", "de termijnrekening"],
        uitleg="In ruil voor die afspraak krijg je doorgaans een hogere rente.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand heeft 1.000 euro en moet er volgende maand een reis mee betalen. Wat doet hij er het best mee?",
        opties=[
            "op een spaar- of zichtrekening laten staan",
            "op een termijnrekening van vijf jaar zetten",
            "in aandelen beleggen",
            "in een cryptomunt stoppen",
        ],
        antwoord=0,
        uitleg="Geld dat je snel nodig hebt, mag je niet vastzetten en al zeker niet riskant beleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factor bepaalt mee of je spaart of belegt, volgens de fiche?",
        opties=[
            "hoelang je je geld kan missen",
            "hoeveel je werkgever bijdraagt",
            "in welke gemeente je woont",
            "hoeveel kinderen je ten laste hebt",
        ],
        antwoord=0,
        uitleg="Dat is de eerste van de vijf factoren in het rijtje.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier beleggingsvormen noemt de fiche?",
        opties=[
            "de obligatie, de cryptomunt, het beleggingsfonds en het beursaandeel",
            "de spaarrekening, de termijnrekening, het aandeel en de obligatie",
            "het aandeel, de lening, de hypotheek en het fonds",
            "de cryptomunt, de verzekering, het aandeel en het pensioensparen",
        ],
        antwoord=0,
        uitleg="Precies die vier staan in de fiche, en een spaarrekening is geen belegging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een obligatie?",
        opties=[
            "een lening aan een bedrijf of een overheid, met een afgesproken rente",
            "een stukje eigendom van een bedrijf, met recht op een deel van de winst",
            "een mand met beleggingen van allerlei bedrijven door elkaar",
            "een digitale munt die geen enkele centrale bank uitgeeft",
        ],
        antwoord=0,
        uitleg="Je bent schuldeiser, geen mede-eigenaar. Daarom ligt het risico doorgaans lager dan bij een aandeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een beursaandeel?",
        opties=[
            "een stukje eigendom van een bedrijf",
            "een lening aan een bedrijf",
            "een spaarproduct met vaste rente",
            "een verzekering tegen verlies",
        ],
        antwoord=0,
        uitleg="Gaat het bedrijf goed, dan stijgt je aandeel. Gaat het slecht, dan daalt het.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een beleggingsfonds?",
        opties=[
            "een mand met veel verschillende beleggingen samen",
            "een rekening bij de bank met vaste rente",
            "een lening aan de overheid",
            "een digitale munt",
        ],
        antwoord=0,
        uitleg="Door te spreiden weegt één slechte belegging minder zwaar door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een cryptomunt?",
        opties=[
            "een digitale munt zonder centrale bank, met een sterk schommelende waarde",
            "een munt waarvan de overheid de waarde bij de bank volledig garandeert",
            "een lening aan een technologiebedrijf, met een vaste rente per jaar",
            "een spaarproduct met een vaste opbrengst die de bank op voorhand belooft",
        ],
        antwoord=0,
        uitleg="Van de vier vormen in de fiche is dit die met het grootste risico.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen risico en rendement?",
        opties=[
            "meer kans op opbrengst gaat samen met meer kans op verlies",
            "meer risico geeft altijd meer opbrengst",
            "minder risico geeft altijd meer opbrengst",
            "ze hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="Let op het woord kans: een hoger risico garandeert geen hogere opbrengst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is inflatie?",
        opties=[
            "de algemene stijging van de prijzen, waardoor geld minder waard wordt",
            "de daling van de rente die de bank je op je spaarrekening betaalt",
            "de algemene stijging van de lonen in een land of een sector",
            "de belasting die de overheid op je spaargeld heft",
        ],
        antwoord=0,
        uitleg="Met hetzelfde bedrag koop je na een jaar inflatie minder dan ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spaarrente is 2 procent en de inflatie 3 procent. Wat gebeurt er met je koopkracht?",
        opties=[
            "ze daalt, want de prijzen stijgen sneller dan je spaargeld",
            "ze stijgt, want je krijgt elk jaar toch rente op je spaargeld",
            "ze blijft gelijk, want de twee heffen elkaar netjes op",
            "dat hangt af van de bank waar je je spaargeld hebt staan",
        ],
        antwoord=0,
        uitleg="Je hebt meer euro's maar je kan er minder mee kopen. Daarom staat de inflatie bij de factoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel factoren noemt de fiche bij de keuze tussen sparen en beleggen?",
        opties=["vijf", "drie", "vier", "zeven"],
        antwoord=0,
        uitleg="De duur, de rentevoet en de inflatie, het risico, je financieel doel en je kennis van de markt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat je kennis over de financiële markt bij de factoren?",
        opties=[
            "omdat je niet moet beleggen in iets wat je niet begrijpt",
            "omdat je anders geen rekening mag openen",
            "omdat de bank dat wettelijk moet testen",
            "omdat kennis de rente verhoogt",
        ],
        antwoord=0,
        uitleg="Het is de eenvoudigste beschermingsregel die er bestaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een obligatie is een lening aan een bedrijf of een overheid.",
        antwoord=True,
        uitleg="Bij een aandeel ben je mede-eigenaar, bij een obligatie schuldeiser.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoger risico levert altijd een hogere opbrengst op.",
        antwoord=False,
        uitleg="Het geeft meer kans op een hogere opbrengst, en net zo goed meer kans op verlies.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij inflatie wordt je spaargeld in koopkracht minder waard.",
        antwoord=True,
        uitleg="Het bedrag blijft, maar je koopt er minder mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een beleggingsfonds bestaat uit één enkele belegging.",
        antwoord=False,
        uitleg="Het is net een mand met veel beleggingen samen, om het risico te spreiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beleggingsvormen noemt de fiche?",
        opties=[
            "de obligatie",
            "het beleggingsfonds",
            "het traditionele beursaandeel",
            "de spaarrekening",
        ],
        antwoord=[0, 1, 2],
        uitleg="De spaarrekening is sparen, geen beleggen. De vierde vorm is de cryptomunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren bepalen volgens de fiche of sparen of beleggen het beste past?",
        opties=[
            "hoelang je je geld kan missen",
            "de rentevoet en de inflatie",
            "het risico dat je bereid bent te nemen",
            "de leeftijd van je bankkantoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="De twee overige zijn je financieel doel en je kennis over de financiële markt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de algemene prijsstijging waardoor geld minder waard wordt?",
        antwoord=["inflatie", "de inflatie"],
        uitleg="Ze staat bij de vijf factoren én bij de zeven factoren van een aankoopkeuze.",
    ),
    dict(
        type="invultekst",
        vraag="Welke beleggingsvorm uit de fiche is een lening aan een bedrijf of een overheid?",
        antwoord=["obligatie", "een obligatie", "de obligatie"],
        uitleg="Bij een aandeel ben je mede-eigenaar, bij een obligatie schuldeiser.",
    ),
    dict(
        type="invultekst",
        vraag="Welke beleggingsvorm uit de fiche is een digitale munt zonder centrale bank?",
        antwoord=["cryptomunt", "een cryptomunt", "de cryptomunt"],
        uitleg="Van de vier vormen in de fiche schommelt deze het sterkst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand van achttien wil geld opzijzetten voor een woning over twintig jaar en kan tegen schommelingen. Wat past bij de factoren van de fiche?",
        opties=[
            "een deel beleggen kan passen, want hij kan het geld lang missen",
            "alles de komende twintig jaar op een zichtrekening laten staan",
            "alles in één cryptomunt stoppen en afwachten wat ze doet",
            "niets doen tot de inflatie weer onder twee procent zakt",
        ],
        antwoord=0,
        uitleg="De lange termijn en zijn risicobereidheid wijzen die kant op. Alles in één munt steken is geen spreiding.",
    ),
]
