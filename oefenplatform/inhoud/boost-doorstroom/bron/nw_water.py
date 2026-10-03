# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Stoffen in water, reacties en berekeningen.

Chemie, de koppen "Gedrag van stoffen in water", "Reacties met anorganische
stoffen" en "Berekeningen" van de vakfiche natuurwetenschappen 2de graad
doorstroom. Deel 1 gaat over polair en apolair, dissociëren en ioniseren,
geleidbaarheid, de pH-schaal en de indicatoren; deel 2 over neerslag-,
neutralisatie- en redoxreacties en over het rekenen met mol.

Neerslag- en neutralisatiereacties met de essentiële reactievergelijking en
de redoxreacties met oxidatiegetallen staan alleen in de uitgebreide fiche
(moderne talen en Latijn).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een zout als het in water oplost?",
        opties=[
            "het dissocieert, de ionen komen los van elkaar",
            "het ioniseert, er ontstaan nieuwe ionen die er nog niet waren",
            "het verbrandt, er komt een gas uit de oplossing vrij",
            "het smelt, de kristallen worden één grote vloeistof",
        ],
        antwoord=0,
        uitleg="De ionen zaten al in het rooster. Het water trekt ze los van elkaar, en dat heet dissociëren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een zuur zoals waterstofchloride in water?",
        opties=[
            "het ioniseert, de molecule valt uiteen in ionen die er nog niet waren",
            "het dissocieert, de ionen uit het rooster van de stof komen los van elkaar",
            "het blijft als hele molecule tussen de watermoleculen zweven",
            "het verdampt onmiddellijk en verdwijnt volledig uit het water",
        ],
        antwoord=0,
        uitleg="In het gas HCl zitten geen ionen maar moleculen. In water splitsen die in een waterstofion en een chloride-ion, en dat heet ioniseren.",
    ),
    dict(
        type="waarofniet",
        vraag="Polaire stoffen lossen goed op in water, apolaire stoffen niet.",
        antwoord=True,
        uitleg="Water is zelf polair, en gelijk lost op in gelijk. Daarom mengt olie niet met water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn apolair? Kruis alles aan wat juist is.",
        opties=[
            "tetrachloormethaan",
            "hexaan",
            "zuurstofgas",
            "keukenzout",
        ],
        antwoord=[0, 1, 2],
        uitleg="Enkelvoudige stoffen en alkanen zijn de typevoorbeelden van apolaire stoffen. Keukenzout is juist zo ionair als het maar kan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die in water geleidt omdat ze ionen vormt?",
        antwoord="elektrolyt",
        uitleg="Zouten, zuren en hydroxiden zijn elektrolyten. Suiker en alcohol lossen wel op maar vormen geen ionen, dus zijn ze niet-elektrolyten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke pH heeft een neutrale oplossing?",
        opties=["7", "0", "14", "1"],
        antwoord=0,
        uitleg="Onder 7 is zuur, boven 7 basisch. Zuiver water heeft precies pH 7.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oplossing met pH 3 is zuurder dan een oplossing met pH 5.",
        antwoord=True,
        uitleg="Hoe lager de pH, hoe meer waterstofionen. Elke stap op de schaal is een factor tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een zuur-base indicator?",
        opties=[
            "om met een kleur te zien of een oplossing zuur, neutraal of basisch is",
            "om te meten hoeveel gram stof er precies in de oplossing zit",
            "om de temperatuur van de oplossing nauwkeurig te kunnen volgen",
            "om de ionen uit de oplossing weer tot een vast zout samen te brengen",
        ],
        antwoord=0,
        uitleg="Een indicator verandert van kleur bij een bepaalde pH. Met een pH-meter lees je dan het precieze getal af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vast blokje keukenzout geleidt geen stroom, een zoutoplossing wel. Waarom?",
        opties=[
            "in de oplossing kunnen de ionen zich verplaatsen, in het blokje niet",
            "in de oplossing worden de ionen omgezet in vrije elektronen",
            "in de oplossing krijgen de ionen een veel grotere lading dan ervoor",
            "in de oplossing wordt het water zelf de geleider en niet het zout",
        ],
        antwoord=0,
        uitleg="Stroom vraagt ladingen die kunnen bewegen. In het rooster zitten de ionen vast op hun plaats.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het omringen van een ion door watermoleculen bij het oplossen?",
        antwoord="hydratatie",
        uitleg="De polaire watermoleculen gaan met hun negatieve kant naar de positieve ionen en omgekeerd. Zo blijven de ionen gescheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de pH-schaal zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een pH onder 7 betekent zuur",
            "een pH boven 7 betekent basisch",
            "elke eenheid verschil is een factor tien",
            "de schaal loopt van min 7 tot plus 7",
        ],
        antwoord=[0, 1, 2],
        uitleg="De gewone schaal loopt van 0 tot 14, met 7 in het midden. Negatieve pH-waarden bestaan wel, maar alleen bij heel sterke zuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat schrijf je op als de dissociatievergelijking van natriumchloride in water?",
        opties=[
            "NaCl wordt Na plus en Cl min",
            "NaCl wordt Na en Cl, twee neutrale atomen",
            "NaCl wordt NaOH en HCl samen",
            "NaCl wordt Na2 en Cl2, twee enkelvoudige stoffen",
        ],
        antwoord=0,
        uitleg="Bij dissociatie komen de ionen los zoals ze in het rooster zaten. Hun lading verandert niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Suiker is een elektrolyt, want hij lost goed op in water.",
        antwoord=False,
        uitleg="Oplossen en geleiden zijn twee verschillende dingen. Suiker lost op als hele moleculen, zonder ionen, en geleidt dus niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gesmolten zout geleidt elektriciteit. Hoe kan dat, zonder water?",
        opties=[
            "door het smelten zijn de ionen los van hun plaats gekomen",
            "door het smelten zijn de ionen in neutrale atomen veranderd",
            "door het smelten zijn er vrije elektronen bij gekomen",
            "door het smelten is er een metaalbinding ontstaan tussen de ionen",
        ],
        antwoord=0,
        uitleg="Geleiding vraagt alleen bewegende ladingen. Of die ionen in water of in een smelt zitten, maakt niet uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost een beetje natriumhydroxide op in water. Wat verwacht je als pH?",
        opties=[
            "duidelijk boven 7, want een hydroxide maakt de oplossing basisch",
            "duidelijk onder 7, want een hydroxide maakt de oplossing zuur",
            "precies 7, want een hydroxide verandert de zuurtegraad niet",
            "eerst onder 7 en daarna boven 7, afhankelijk van de tijd",
        ],
        antwoord=0,
        uitleg="Natriumhydroxide dissocieert en geeft hydroxide-ionen vrij. Die maken de oplossing basisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die in water ioniseert, vormt ionen die er daarvoor nog niet waren.",
        antwoord=True,
        uitleg="Dat is het verschil met dissociëren. Bij dissociatie komen bestaande ionen los; bij ionisatie valt een molecule uiteen in nieuwe ionen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mengt olie niet met water?",
        opties=[
            "olie is apolair en water polair, en die twee trekken elkaar niet aan",
            "olie is te zwaar en zakt daardoor onder de laag water naar beneden",
            "olie bevat geen ionen en lost daarom in geen enkel oplosmiddel op",
            "olie heeft een veel te hoog kookpunt om in water te kunnen mengen",
        ],
        antwoord=0,
        uitleg="Watermoleculen houden elkaar sterk vast met hun polaire kanten. Een apolaire oliemolecule past daar niet tussen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die in water geen ionen vormt en dus niet geleidt?",
        antwoord="niet-elektrolyt",
        uitleg="Suiker en alcohol zijn niet-elektrolyten. Ze lossen op als hele moleculen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan de zuurtegraad van een oplossing alleen meten met een indicator, niet met een toestel.",
        antwoord=False,
        uitleg="Een pH-meter geeft de pH als getal, veel nauwkeuriger dan een kleur. De indicator is vooral handig om snel een eerste beeld te krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je test een oplossing en de indicator wordt rood. Wat weet je?",
        opties=[
            "de oplossing is zuur, er zijn veel waterstofionen aanwezig",
            "de oplossing is basisch, er zijn veel hydroxide-ionen aanwezig",
            "de oplossing is neutraal, er zijn geen ionen in aanwezig",
            "de oplossing is verzadigd, er kan niets meer in opgelost worden",
        ],
        antwoord=0,
        uitleg="De kleur van elke indicator hangt af van de pH. Welke kleur bij welke waarde hoort, lees je af in een tabel.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij een neutralisatiereactie tussen een zuur en een base? Kruis alles aan wat juist is.",
        opties=[
            "een zout",
            "water",
            "een oplossing die naar neutraal opschuift",
            "een gas dat uit de beker ontsnapt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het waterstofion van het zuur en het hydroxide-ion van de base vormen samen water, en de overige ionen blijven als zout achter. Daardoor schuift de pH naar 7 toe, zonder dat er gas vrijkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer spreek je van een neerslagreactie?",
        opties=[
            "als er uit twee oplossingen een vaste stof ontstaat die niet oplost",
            "als er uit twee oplossingen een gas ontstaat dat naar boven borrelt",
            "als er uit twee oplossingen een nieuwe kleur ontstaat in het water",
            "als er uit twee oplossingen plots veel warmte vrijkomt in de beker",
        ],
        antwoord=0,
        uitleg="Twee ionen uit de oplossingen vormen samen een slecht oplosbaar zout. Dat zakt als neerslag naar de bodem.",
    ),
    dict(
        type="waarofniet",
        vraag="In de essentiële reactievergelijking laat je de ionen weg die niet meedoen aan de reactie.",
        antwoord=True,
        uitleg="Die ionen blijven ongewijzigd in oplossing en heten daarom spectatorionen. Wat overblijft, is de kern van de reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent oxidatie in een redoxreactie?",
        opties=[
            "een atoom staat elektronen af en zijn oxidatiegetal stijgt",
            "een atoom neemt elektronen op en zijn oxidatiegetal daalt",
            "een atoom bindt met een zuurstofatoom en wordt een oxide",
            "een atoom verliest een neutron uit zijn kern aan een ander atoom",
        ],
        antwoord=0,
        uitleg="Oxidatie is elektronen afstaan, reductie is ze opnemen. Het ene gaat nooit zonder het andere, want de elektronen moeten ergens naartoe.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stof die in een redoxreactie elektronen opneemt?",
        antwoord="oxidator",
        uitleg="De oxidator neemt elektronen op en wordt zelf gereduceerd. De reductor staat ze af en wordt zelf geoxideerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel deeltjes zitten er in één mol van een stof?",
        opties=[
            "ongeveer 6 maal 10 tot de 23",
            "ongeveer 6 maal 10 tot de 12",
            "precies 1000 deeltjes per mol stof",
            "evenveel als het atoomnummer van het element",
        ],
        antwoord=0,
        uitleg="Dat getal heet het getal van Avogadro. Eén mol is dus altijd hetzelfde aantal deeltjes, welke stof het ook is.",
    ),
    dict(
        type="waarofniet",
        vraag="De molaire massa van een stof lees je af uit het periodiek systeem, uitgedrukt in gram per mol.",
        antwoord=True,
        uitleg="De relatieve atoommassa in het systeem is het getal dat je in gram per mol gebruikt. Voor een molecule tel je de atomen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt 2 mol water. Hoeveel gram is dat, als de molaire massa 18 gram per mol is?",
        opties=["36 gram", "18 gram", "9 gram", "20 gram"],
        antwoord=0,
        uitleg="Massa is stofhoeveelheid maal molaire massa, dus 2 maal 18. Omgekeerd deel je de massa door de molaire massa om het aantal mol te vinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe reken je de molaire concentratie van een oplossing uit?",
        opties=[
            "het aantal mol delen door het volume in liter",
            "het aantal mol vermenigvuldigen met het volume in liter",
            "de massa in gram delen door het aantal mol van de stof",
            "het volume in liter delen door de molaire massa van de stof",
        ],
        antwoord=0,
        uitleg="De molaire concentratie zegt hoeveel mol er in één liter zit. De eenheid is dus mol per liter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol is 36 gram water, als de molaire massa 18 gram per mol is?",
        antwoord="2",
        uitleg="Je deelt de massa door de molaire massa: 36 gedeeld door 18 is 2 mol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een aflopende reactie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze gaat door tot een van de stoffen volledig opgebruikt is",
            "de verhouding waarin de stoffen reageren staat in de reactievergelijking",
            "wat overblijft van de andere stof doet niet meer mee",
            "ze stopt halverwege en blijft dan in evenwicht hangen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij een aflopende reactie bepaalt de stof die het eerst opgebruikt is hoeveel product je krijgt. Een evenwicht is juist het tegenovergestelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet een reactievergelijking in evenwicht gebracht worden?",
        opties=[
            "er mogen voor en na de reactie evenveel atomen van elk element zijn",
            "er moeten voor en na de reactie evenveel moleculen in totaal zijn",
            "de temperatuur voor en na de reactie moet precies gelijk blijven",
            "de kleur van de stoffen voor en na de reactie moet overeenkomen",
        ],
        antwoord=0,
        uitleg="Atomen verdwijnen niet en komen niet uit het niets. Daarom kloppen de aantallen aan beide kanten van de pijl.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een redoxreactie verandert het oxidatiegetal van minstens twee elementen.",
        antwoord=True,
        uitleg="Het ene gaat omhoog en het andere omlaag. Verandert er geen enkel oxidatiegetal, dan is het geen redoxreactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je giet een oplossing met zilverionen bij een oplossing met chloride-ionen. Wat gebeurt er?",
        opties=[
            "er vormt zich een witte neerslag van zilverchloride",
            "er ontstaat een gas dat uit de oplossing ontsnapt",
            "er gebeurt niets, want beide zouten lossen goed op",
            "de oplossing wordt zuur en de pH zakt onder de 7",
        ],
        antwoord=0,
        uitleg="Zilverchloride is slecht oplosbaar in water, en dat kan je nakijken in een oplosbaarheidstabel. Daarom slaat het neer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de essentiële reactievergelijking van een neutralisatie?",
        opties=[
            "een waterstofion en een hydroxide-ion vormen samen water",
            "een waterstofion en een chloride-ion vormen samen zoutzuur",
            "een metaalion en een hydroxide-ion vormen samen een neerslag",
            "een natriumion en een chloride-ion vormen samen keukenzout",
        ],
        antwoord=0,
        uitleg="De overige ionen blijven ongewijzigd in de oplossing. Alleen de vorming van water is de kern van elke neutralisatie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een enkelvoudige stof zoals ijzer of zuurstofgas is het oxidatiegetal min twee.",
        antwoord=False,
        uitleg="Daar is niemand om elektronen aan af te staan, dus is het oxidatiegetal nul. Min twee is wat zuurstof in de meeste verbindingen krijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt 0,5 liter oplossing met 1 mol opgeloste stof. Wat is de molaire concentratie?",
        opties=[
            "2 mol per liter",
            "0,5 mol per liter",
            "1 mol per liter",
            "0,25 mol per liter",
        ],
        antwoord=0,
        uitleg="Je deelt 1 mol door 0,5 liter en dat geeft 2 mol per liter. In een halve liter zit dus even veel als in een liter van een twee keer verdunde oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zeggen de coëfficiënten voor de formules in een reactievergelijking?",
        opties=[
            "in welke verhouding in mol de stoffen met elkaar reageren",
            "hoeveel gram van elke stof je precies nodig hebt",
            "hoeveel liter oplossing je van elke stof moet afmeten",
            "hoe snel de reactie na het mengen zal verlopen",
        ],
        antwoord=0,
        uitleg="Die verhouding heet de stoichiometrische verhouding. Wil je grammen, dan reken je eerst van mol naar massa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stof die in een redoxreactie elektronen afstaat?",
        antwoord="reductor",
        uitleg="De reductor staat elektronen af en wordt daardoor zelf geoxideerd. Hij reduceert de andere stof.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee stoffen die je samengiet, geven altijd een neerslag of een neutralisatie.",
        antwoord=False,
        uitleg="Heel vaak gebeurt er niets, omdat alle mogelijke combinaties goed oplossen. Een oplosbaarheidstabel zegt je dat vooraf.",
    ),
]
