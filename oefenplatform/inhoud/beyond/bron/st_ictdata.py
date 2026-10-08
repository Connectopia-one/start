# -*- coding: utf-8 -*-
"""Een dataset doorrekenen met het rekenblad.

Het tweede thema met echte rekenopgaven, naast [[st_ictkansen]]. Hier staat
het rekenblad centraal: je tikt een rijtje getallen in een kolom en vraagt er
de kengetallen, de correlatiecoëfficiënt en de trendlijn van. Precies wat de
vakfiche vraagt bij het werken met grote datasets, en wat een kind niet leert
uit een meerkeuzevraag.

Alle getallen zijn nagerekend (zie data2.py in de scratchpad van 8 oktober
2026). Twee dingen zijn met zorg gekozen:

  1. De datasets van negen getallen zijn zo gebouwd dat de twee gangbare
     methodes voor Q1 en Q3 hetzelfde antwoord geven. Handboeken en
     rekenapps verschillen daarin: de ene neemt de mediaan van de onderste
     helft, de andere interpoleert. Bij 3, 5, 5, 6, 8, 9, 11, 11, 14 komen
     allebei op Q1 gelijk aan 5 en Q3 gelijk aan 11 uit. Een kind hoort geen
     fout te krijgen voor een verschil tussen twee geldige methodes.

  2. Waar de standaardafwijking gevraagd wordt, staat er uitdrukkelijk
     "steekproefstandaardafwijking s" bij. Een rekenblad geeft twee knoppen,
     en het verschil tussen s en sigma is hier echte leerstof: s deelt door
     n min 1, sigma door n. Het antwoord in de lijst is s; de uitleg noemt
     het andere getal erbij, zodat een kind dat de verkeerde knop nam, weet
     wat het volgende keer moet doen.

Deel 1 is de kengetallen van een dataset.
Deel 2 zijn frequenties, correlatie en de trendlijn.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag="Zet deze dataset in het rekenblad: 3, 5, 5, 6, 8, 9, 11, 11, 14. Bereken het gemiddelde.",
        antwoord=["8"],
        uitleg="De som is 72 en er zijn negen waarden, dus het gemiddelde is 8.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de mediaan van 3, 5, 5, 6, 8, 9, 11, 11, 14.",
        antwoord=["8"],
        uitleg="Negen waarden, dus de vijfde van de gerangschikte lijst. Hier vallen het gemiddelde en de mediaan toevallig samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de variatiebreedte van 3, 5, 5, 6, 8, 9, 11, 11, 14?",
        opties=["elf", "veertien", "zes", "acht"],
        antwoord=0,
        uitleg="Veertien min drie is elf.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de steekproefstandaardafwijking s van 3, 5, 5, 6, 8, 9, 11, 11, 14, op twee decimalen.",
        antwoord=["3,57"],
        uitleg="s is 3,5707. Kies je in het rekenblad de populatieversie sigma, dan krijg je 3,37. Let dus op welke knop je neemt.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het eerste kwartiel van 3, 5, 5, 6, 8, 9, 11, 11, 14.",
        antwoord=["5"],
        uitleg="De onderste helft is 3, 5, 5, 6 en haar mediaan is 5. Het rekenblad geeft hetzelfde getal.",
    ),
    dict(
        type="invultekst",
        vraag="Bij 3, 5, 5, 6, 8, 9, 11, 11, 14 is Q1 gelijk aan 5 en Q3 gelijk aan 11. Bereken de interkwartielafstand.",
        antwoord=["6"],
        uitleg="Elf min vijf is zes. In die zes zit de middelste helft van de gegevens.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het gemiddelde van 10, 12, 12, 15, 16, 17, 20, 20, 22.",
        antwoord=["16"],
        uitleg="De som is 144 en er zijn negen waarden, dus het gemiddelde is 16.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de steekproefstandaardafwijking s van 10, 12, 12, 15, 16, 17, 20, 20, 22, op twee decimalen?",
        opties=["4,15", "3,92", "16,00", "17,25"],
        antwoord=0,
        uitleg="s is 4,1533. Het getal 3,92 is de populatieversie sigma, die door n deelt in plaats van door n min 1.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het derde kwartiel van 10, 12, 12, 15, 16, 17, 20, 20, 22.",
        antwoord=["20"],
        uitleg="De bovenste helft is 17, 20, 20, 22 en haar mediaan is 20.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het gemiddelde van 20, 24, 24, 28, 30, 32, 36, 36, 40.",
        antwoord=["30"],
        uitleg="De som is 270 en er zijn negen waarden, dus het gemiddelde is 30. Dat is hier ook de mediaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 20, 24, 24, 28, 30, 32, 36, 36, 40 is Q1 gelijk aan 24 en Q3 gelijk aan 36. Hoeveel is de interkwartielafstand?",
        opties=["twaalf", "twintig", "zestig", "zes"],
        antwoord=0,
        uitleg="Zesendertig min vierentwintig is twaalf. Twintig is de variatiebreedte, een andere maat.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de mediaan van 4, 6, 6, 7, 9, 10, 12, 12, 14, 16.",
        antwoord=["9,5"],
        uitleg="Tien waarden, dus het gemiddelde van de vijfde en de zesde: negen en tien geven 9,5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is het gemiddelde van 4, 6, 6, 7, 9, 10, 12, 12, 14, 16?",
        opties=["9,6", "9,5", "10,0", "9,0"],
        antwoord=0,
        uitleg="De som is 96 en er zijn tien waarden, dus 9,6. Let op: 9,5 is de mediaan en niet het gemiddelde.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de steekproefstandaardafwijking s van 4, 6, 6, 7, 9, 10, 12, 12, 14, 16, op twee decimalen.",
        antwoord=["3,89"],
        uitleg="s is 3,8930. De populatieversie sigma geeft hier 3,69.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de dataset 3, 5, 5, 6, 8, 9, 11, 11, 14 zijn het gemiddelde en de mediaan allebei gelijk aan 8.",
        antwoord=True,
        uitleg="Dat wijst op een redelijk symmetrische verdeling. Liggen de twee ver uit elkaar, dan hangt de verdeling scheef.",
    ),
    dict(
        type="waarofniet",
        vraag="Het rekenblad geeft dezelfde standaardafwijking of je nu de steekproefversie of de populatieversie kiest.",
        antwoord=False,
        uitleg="De steekproefversie s deelt door n min 1 en komt dus altijd iets hoger uit dan de populatieversie sigma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe begin je als je de kengetallen van een dataset met het rekenblad wil berekenen?",
        opties=[
            "je zet alle waarden onder elkaar in één kolom en selecteert die kolom",
            "je zet alle waarden naast elkaar in één rij en telt ze eerst op",
            "je groepeert de waarden eerst in klassen van vijf eenheden",
            "je rangschikt de waarden met de hand voor je ze intikt",
        ],
        antwoord=0,
        uitleg="Rangschikken hoeft niet: het rekenblad doet dat zelf voor de mediaan en de kwartielen.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de mediaan van 2, 4, 4, 6, 7, 8, 10, 10, 13.",
        antwoord=["7"],
        uitleg="Negen waarden, dus de vijfde van de gerangschikte lijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is het gemiddelde van 2, 4, 4, 6, 7, 8, 10, 10, 13, op twee decimalen?",
        opties=["7,11", "7,00", "6,40", "8,00"],
        antwoord=0,
        uitleg="De som is 64 en er zijn negen waarden, dus 7,1111. Hier liggen het gemiddelde en de mediaan dicht bij elkaar maar niet gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling vindt bij 3, 5, 5, 6, 8, 9, 11, 11, 14 een standaardafwijking van 3,37 terwijl er 3,57 verwacht werd. Wat gebeurde er?",
        opties=[
            "hij nam de populatieversie sigma in plaats van de steekproefversie s",
            "hij vergat een van de negen waarden in te tikken in het rekenblad",
            "hij nam de variantie in plaats van de standaardafwijking",
            "hij rondde te vroeg af in een van de tussenstappen",
        ],
        antwoord=0,
        uitleg="Sigma deelt door negen, s door acht. Daardoor komt s altijd iets hoger uit. Kijk bij welke knop s staat.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Een toets op vijf heeft deze frequenties: 1 komt 3 keer voor, 2 zeven keer, 3 tien keer, 4 veertien keer en 5 zes keer. Bereken het gemiddelde op twee decimalen.",
        antwoord=["3,33"],
        uitleg="De som van de punten is 133 en er zijn 40 leerlingen, dus 3,325. Tik in het rekenblad de waarden en de frequenties in twee kolommen.",
    ),
    dict(
        type="invultekst",
        vraag="Bij diezelfde veertig leerlingen met frequenties 3, 7, 10, 14 en 6: bereken de mediaan.",
        antwoord=["3,5"],
        uitleg="De twintigste en de eenentwintigste waarde zijn 3 en 4, dus de mediaan is 3,5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij frequenties 3, 7, 10, 14 en 6 voor de punten 1 tot 5: wat is de modus?",
        opties=["vier", "veertien", "drie", "vijf"],
        antwoord=0,
        uitleg="Het punt vier komt het vaakst voor, namelijk veertien keer. Veertien is de frequentie, niet de modus.",
    ),
    dict(
        type="invultekst",
        vraag="Bij frequenties 3, 7, 10, 14 en 6 voor de punten 1 tot 5: hoeveel leerlingen haalden ten hoogste 3?",
        antwoord=["20"],
        uitleg="Drie plus zeven plus tien is twintig. Dat is de cumulatieve frequentie bij het punt drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij die veertig leerlingen haalden er veertien een punt van 4. Wat is de relatieve frequentie?",
        opties=["35 procent", "14 procent", "40 procent", "25 procent"],
        antwoord=0,
        uitleg="Veertien gedeeld door veertig is 0,35.",
    ),
    dict(
        type="invultekst",
        vraag="Bij die veertig leerlingen haalden er zes een punt van 5. Geef de relatieve frequentie in procent.",
        antwoord=["15", "15 procent"],
        uitleg="Zes gedeeld door veertig is 0,15.",
    ),
    dict(
        type="invultekst",
        vraag="Zet deze paren in twee kolommen. x: 1, 3, 4, 6, 7, 9, 11, 12, 14, 16. y: 22, 25, 24, 29, 31, 30, 35, 38, 37, 42. Bereken r op twee decimalen.",
        antwoord=["0,98"],
        uitleg="r is 0,9773. Volgens het formularium is dat een sterke positieve samenhang, want r ligt boven 0,7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij diezelfde tien paren geeft het rekenblad de trendlijn. Hoeveel is de richtingscoëfficiënt op twee decimalen?",
        opties=["1,30", "0,98", "20,47", "2,26"],
        antwoord=0,
        uitleg="De trendlijn is y gelijk aan 1,30x plus 20,47. Het getal 20,47 is de waarde bij x gelijk aan nul en 0,98 is de correlatiecoëfficiënt.",
    ),
    dict(
        type="invultekst",
        vraag="x: 5, 10, 15, 20, 25, 30. y: 80, 72, 70, 61, 55, 44. Bereken r op twee decimalen.",
        antwoord=["-0,99", "−0,99"],
        uitleg="r is min 0,9866. Vergeet het minteken niet: y daalt terwijl x stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij r gelijk aan min 0,99, wat besluit je volgens de vuistregels van het formularium?",
        opties=[
            "een sterke negatieve samenhang",
            "een matige negatieve samenhang",
            "een zwakke negatieve samenhang",
            "helemaal geen samenhang",
        ],
        antwoord=0,
        uitleg="Onder min 0,7 spreekt het formularium van een sterke negatieve samenhang.",
    ),
    dict(
        type="invultekst",
        vraag="x: 2, 3, 5, 6, 8, 9, 11, 13. y: 14, 19, 17, 24, 22, 28, 31, 29. Bereken r op twee decimalen.",
        antwoord=["0,91"],
        uitleg="r is 0,9111. Nog altijd sterk positief, al ligt de puntenwolk duidelijk losser dan bij r gelijk aan 0,98.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij diezelfde acht paren, welke trendlijn geeft het rekenblad op twee decimalen?",
        opties=[
            "y = 1,45x + 12,68",
            "y = 12,68x + 1,45",
            "y = 0,91x + 14,00",
            "y = 1,45x − 12,68",
        ],
        antwoord=0,
        uitleg="De richtingscoëfficiënt komt voor de x en het andere getal staat los. Verwissel je ze, dan voorspel je onzin.",
    ),
    dict(
        type="invultekst",
        vraag="x: 1 tot en met 10. y: 5, 9, 8, 14, 12, 19, 17, 23, 21, 27. Bereken r op twee decimalen.",
        antwoord=["0,96"],
        uitleg="r is 0,9610. De punten zigzaggen rond een stijgende rechte, en dat drukt r een beetje omlaag.",
    ),
    dict(
        type="invultekst",
        vraag="Bij diezelfde tien paren: hoeveel is de richtingscoëfficiënt van de trendlijn, op twee decimalen?",
        antwoord=["2,26"],
        uitleg="De trendlijn is y gelijk aan 2,26x plus 3,07. Per eenheid x stijgt y met 2,26.",
    ),
    dict(
        type="waarofniet",
        vraag="Verwissel je x en y, dan blijft de correlatiecoëfficiënt dezelfde.",
        antwoord=True,
        uitleg="r meet de samenhang tussen de twee en kent geen richting van oorzaak. Daarom is ze symmetrisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Verwissel je x en y, dan blijft ook de trendlijn dezelfde.",
        antwoord=False,
        uitleg="Die verandert wel. Een trendlijn voorspelt y uit x, dus welke variabele je waar zet, maakt uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="De trendlijn is y gelijk aan 1,30x plus 20,47. Welke y hoort bij x gelijk aan 20?",
        opties=["46,47", "26,00", "20,47", "33,47"],
        antwoord=0,
        uitleg="1,30 maal 20 is 26, plus 20,47 is 46,47.",
    ),
    dict(
        type="invultekst",
        vraag="De trendlijn is y gelijk aan min 1,37x plus 87,67. Welke y hoort bij x gelijk aan 10? Geef het antwoord op twee decimalen.",
        antwoord=["73,97"],
        uitleg="Min 1,37 maal 10 is min 13,7, en 87,67 min 13,7 is 73,97.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling leest een correlatiecoëfficiënt van 1,2 af. Wat is er gebeurd?",
        opties=[
            "hij las een ander getal af, want r ligt altijd tussen min één en plus één",
            "dat betekent een extra sterke samenhang tussen de twee variabelen",
            "hij moet het getal door honderd delen om r te krijgen",
            "hij heeft de twee kolommen verwisseld bij het intikken",
        ],
        antwoord=0,
        uitleg="Waarschijnlijk stond het toestel op de richtingscoëfficiënt van de trendlijn. Die mag wel groter zijn dan één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt twee kolommen in het rekenblad en wil de trendlijn zien. Wat is de werkwijze?",
        opties=[
            "de twee kolommen selecteren, een spreidingsdiagram maken en de lineaire trendlijn vragen",
            "van elke kolom apart het gemiddelde nemen en die twee punten verbinden",
            "de kolommen optellen en de som in een lijndiagram zetten",
            "de kolommen rangschikken en de eerste en de laatste waarde verbinden",
        ],
        antwoord=0,
        uitleg="Het toestel geeft dan zelf het voorschrift. Kijk altijd eerst naar de puntenwolk: bij een kromme wolk is een rechte zinloos.",
    ),
]
