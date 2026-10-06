# -*- coding: utf-8 -*-
"""De vragen voor "Ondernemingsvormen en aansprakelijkheid" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "ondernemingsvormen": het verschil tussen een
rechtspersoon en een natuurlijk persoon, beperkte en onbeperkte
aansprakelijkheid, en de vergelijking van de eenmanszaak, de bv en de nv op
zeven punten (oprichtingsakte, minimumkapitaal, aantal oprichters,
aansprakelijkheid, boekhouding, overdraagbaarheid van de aandelen en
fiscaliteit).

Deel 1 gaat over natuurlijk persoon en rechtspersoon, over de twee soorten
aansprakelijkheid en over de eenmanszaak.
Deel 2 vergelijkt de bv en de nv punt voor punt.

De cijfers volgen het vennootschapsrecht zoals het vandaag geldt: een bv heeft
geen vast minimumkapitaal meer maar een toereikend aanvangsvermogen met een
financieel plan, een nv heeft 61 500 euro, en bij beide volstaat één oprichter.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een natuurlijk persoon?",
        opties=[
            "Een mens",
            "Een vennootschap met een eigen naam",
            "Een vereniging zonder winstoogmerk",
            "Een handelszaak die staat ingeschreven",
        ],
        antwoord=0,
        uitleg="Een natuurlijk persoon is een mens van vlees en bloed. Een rechtspersoon is een constructie die het recht als persoon behandelt, zoals een vennootschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een rechtspersoon?",
        opties=[
            "Een vennootschap",
            "De zaakvoerder van een bedrijf",
            "Een klant die in de winkel komt",
            "Een werknemer met een vast contract",
        ],
        antwoord=0,
        uitleg="Een vennootschap is een rechtspersoon: ze kan zelf eigendom hebben, contracten sluiten en schulden maken, los van de mensen erachter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt een eenmanszaak juridisch bekeken?",
        opties=[
            "Als een natuurlijk persoon",
            "Als een rechtspersoon met eigen vermogen",
            "Als een vennootschap met één aandeelhouder",
            "Als een vereniging zonder winstoogmerk",
        ],
        antwoord=0,
        uitleg="Bij een eenmanszaak is er geen aparte rechtspersoon. De zaak en de persoon zijn één en dezelfde; de eigenaar handelt in eigen naam.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenmanszaak zijn het vermogen van de zaak en het privévermogen niet gescheiden.",
        antwoord=True,
        uitleg="Er is maar één vermogen. Schuldeisers van de zaak kunnen daardoor ook aan de spaarrekening of het huis van de eigenaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eenmanszaak heeft een notariële oprichtingsakte nodig.",
        antwoord=False,
        uitleg="Voor een eenmanszaak hoeft geen notaris tussen te komen. Een bv en een nv hebben wel een notariële akte nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de aansprakelijkheid waarbij je ook met je privévermogen instaat voor de schulden van de zaak?",
        antwoord=["onbeperkte", "onbeperkt", "onbeperkte aansprakelijkheid"],
        uitleg="Dat is onbeperkte aansprakelijkheid. Ze geldt bij een eenmanszaak: de schuldeisers kunnen ook aan het privévermogen van de eigenaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent beperkte aansprakelijkheid?",
        opties=[
            "Je verliest enkel je inbreng",
            "Je moet alle schulden zelf terugbetalen",
            "Je staat ook in met je huis en je spaargeld",
            "Je mag maar een beperkt bedrag aan schulden maken",
        ],
        antwoord=0,
        uitleg="Wie geld inbrengt in een bv of een nv kan die inbreng kwijtspelen, maar niet meer dan dat. Het privévermogen blijft buiten schot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij een eenmanszaak? Duid alles aan wat juist is.",
        opties=[
            "Geen minimumkapitaal",
            "Eén oprichter",
            "Onbeperkte aansprakelijkheid",
            "Aandelen die vrij overgaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een eenmanszaak start zonder kapitaalvereiste, met één persoon, die wel onbeperkt aansprakelijk is. Aandelen zijn er niet, want er is geen vennootschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke belasting betaalt de eigenaar van een eenmanszaak op de winst?",
        opties=[
            "De personenbelasting",
            "De vennootschapsbelasting op de winst",
            "De belasting op de toegevoegde waarde",
            "De roerende voorheffing op dividenden",
        ],
        antwoord=0,
        uitleg="De winst van een eenmanszaak is een inkomen van de eigenaar zelf en gaat dus in de personenbelasting. Een bv en een nv betalen vennootschapsbelasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker met een eenmanszaak heeft 40 000 euro schulden. In de zaak zit nog 15 000 euro. Waarmee staat hij in voor de rest?",
        opties=[
            "Ook met zijn privévermogen",
            "Met niets, de schuld vervalt gewoon",
            "Enkel met wat er nog in de zaak zit",
            "Met het kapitaal van zijn vennootschap",
        ],
        antwoord=0,
        uitleg="Bij onbeperkte aansprakelijkheid stopt het niet bij wat in de zaak zit. De schuldeisers kunnen voor de resterende 25 000 euro ook aan zijn privévermogen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vennootschap kan zelf een contract ondertekenen.",
        antwoord=True,
        uitleg="Een rechtspersoon kan in eigen naam kopen, verkopen, huren en lenen. Een zaakvoerder zet de handtekening, maar het contract is van de vennootschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechtspersoon kan geen eigen eigendom hebben.",
        antwoord=False,
        uitleg="Dat kan ze juist wel. Het gebouw, de machines en de rekening van een bv zijn van de bv en niet van de aandeelhouders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voordelen heeft een vennootschap boven een eenmanszaak? Duid alles aan wat juist is.",
        opties=[
            "Beperkte aansprakelijkheid",
            "Makkelijker geld ophalen",
            "Ze blijft bestaan na een overlijden",
            "Er is geen boekhouding nodig",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het privévermogen blijft beschermd, nieuwe aandeelhouders kunnen instappen, en de vennootschap leeft verder als een oprichter wegvalt. Een boekhouding blijft wel nodig, zelfs een strengere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nadeel van een vennootschap tegenover een eenmanszaak?",
        opties=[
            "Meer administratie",
            "Je staat in met je hele privévermogen",
            "Je mag geen personeel in dienst nemen",
            "Je kan geen nieuwe aandeelhouders aantrekken",
        ],
        antwoord=0,
        uitleg="Een vennootschap vraagt een notariële akte, een dubbele boekhouding en jaarlijkse neerlegging van de jaarrekening. Dat kost tijd en geld.",
    ),
    dict(
        type="invultekst",
        vraag="Welke soort akte moet bij de oprichting van een bv opgemaakt worden?",
        antwoord=["notariële", "notariele", "een notariële akte", "authentieke"],
        uitleg="Een bv wordt opgericht met een notariële akte, ook authentieke akte genoemd. Een eenmanszaak heeft die niet nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze ondernemingsvormen zijn rechtspersonen? Duid alles aan wat juist is.",
        opties=[
            "De bv",
            "De nv",
            "De cv",
            "De eenmanszaak",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bv, de nv en de cv zijn vennootschappen en dus rechtspersonen. Een eenmanszaak is dat niet: daar handelt een natuurlijk persoon in eigen naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand begint alleen een kleine zaak en wil zo weinig administratie als mogelijk. Welke vorm past?",
        opties=[
            "De eenmanszaak",
            "De naamloze vennootschap",
            "De besloten vennootschap",
            "De coöperatieve vennootschap",
        ],
        antwoord=0,
        uitleg="Een eenmanszaak start snel, zonder notaris en zonder kapitaal, met een eenvoudige boekhouding. De prijs daarvoor is de onbeperkte aansprakelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat moet er bij de oprichting van een bv klaar zijn? Duid alles aan wat juist is.",
        opties=[
            "Een financieel plan",
            "Een notariële akte",
            "Genoeg aanvangsvermogen",
            "Een kapitaal van 61 500 euro",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een bv heeft geen vast minimumkapitaal meer, maar wel een toereikend aanvangsvermogen dat de oprichters in een financieel plan verantwoorden, en een notariële akte. De 61 500 euro is de regel bij een nv.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel oprichters heeft een bv minstens nodig?",
        opties=[
            "Eén",
            "Twee oprichters samen",
            "Drie oprichters samen",
            "Zeven oprichters samen",
        ],
        antwoord=0,
        uitleg="Eén persoon kan een bv oprichten. Dat geldt vandaag ook voor een nv.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie staat er in voor de schulden van een eenmanszaak?",
        opties=[
            "De eigenaar zelf",
            "De vennootschap met haar eigen vermogen",
            "De aandeelhouders ten belope van hun inbreng",
            "De bank die het krediet heeft toegestaan",
        ],
        antwoord=0,
        uitleg="Er is geen aparte rechtspersoon, dus de eigenaar is de schuldenaar. Zijn aansprakelijkheid is onbeperkt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel kapitaal moet een nv minstens hebben?",
        opties=[
            "61 500 euro",
            "Geen vast bedrag, wel een plan",
            "18 550 euro, volledig volstort",
            "250 000 euro bij de oprichting",
        ],
        antwoord=0,
        uitleg="Een nv heeft een minimumkapitaal van 61 500 euro dat volledig volstort moet zijn. Dat is het grote verschil met de bv.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kapitaal moet een bv minstens hebben?",
        opties=[
            "Geen vast bedrag",
            "61 500 euro, volledig volstort",
            "18 550 euro bij de oprichting",
            "Een vijfde van de verwachte omzet",
        ],
        antwoord=0,
        uitleg="Sinds de hervorming van het vennootschapsrecht heeft een bv geen minimumkapitaal meer. Ze moet wel een toereikend aanvangsvermogen hebben, onderbouwd in een financieel plan.",
    ),
    dict(
        type="waarofniet",
        vraag="Zowel bij een bv als bij een nv is de aansprakelijkheid van de aandeelhouders beperkt.",
        antwoord=True,
        uitleg="In beide gevallen riskeert een aandeelhouder enkel zijn inbreng. Het privévermogen blijft buiten het bereik van de schuldeisers.",
    ),
    dict(
        type="waarofniet",
        vraag="De aandelen van een bv zijn in principe vrij overdraagbaar.",
        antwoord=False,
        uitleg="Een bv heeft een besloten karakter: voor een overdracht is in principe de toestemming van de andere aandeelhouders nodig. Bij een nv gaan de aandelen wel vrij over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe gaan de aandelen van een nv over?",
        opties=[
            "Vrij overdraagbaar",
            "Enkel met toestemming van de anderen",
            "Enkel na een beslissing van de rechtbank",
            "Enkel bij een overlijden of een faillissement",
        ],
        antwoord=0,
        uitleg="Aandelen van een nv kan je in principe vrij verkopen. Daarom past die vorm bij een onderneming die met veel of met wisselende aandeelhouders werkt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel euro kapitaal moet een nv minstens hebben? Schrijf enkel het getal.",
        antwoord=["61500", "61 500", "61.500"],
        uitleg="Het minimumkapitaal van een nv is 61 500 euro en moet volledig volstort zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben een bv en een nv gemeen? Duid alles aan wat juist is.",
        opties=[
            "Ze zijn rechtspersoon",
            "Ze hebben een notariële akte",
            "Ze betalen vennootschapsbelasting",
            "Hun aandelen gaan vrij over",
        ],
        antwoord=[0, 1, 2],
        uitleg="Beide zijn rechtspersonen met beperkte aansprakelijkheid, met een notariële oprichtingsakte, een dubbele boekhouding en vennootschapsbelasting. Vrij overdraagbare aandelen zijn er enkel bij de nv.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke boekhouding moeten een bv en een nv voeren?",
        opties=[
            "Een dubbele boekhouding",
            "Een vereenvoudigde boekhouding",
            "Enkel een lijst van de inkomsten",
            "Geen, zolang de omzet klein blijft",
        ],
        antwoord=0,
        uitleg="Vennootschappen moeten een dubbele boekhouding voeren en elk jaar hun jaarrekening neerleggen. Een kleine eenmanszaak mag een vereenvoudigde boekhouding houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke belasting betaalt een bv op haar winst?",
        opties=[
            "De vennootschapsbelasting",
            "De personenbelasting van de zaakvoerder",
            "De belasting op de toegevoegde waarde",
            "De onroerende voorheffing op het gebouw",
        ],
        antwoord=0,
        uitleg="De winst van een vennootschap gaat in de vennootschapsbelasting. Keert ze daarna een dividend uit, dan volgt daarop nog roerende voorheffing.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nv past bij een onderneming die met veel aandeelhouders wil werken.",
        antwoord=True,
        uitleg="Omdat de aandelen vrij overdraagbaar zijn, kan een nv makkelijk nieuwe aandeelhouders aantrekken. Beursgenoteerde bedrijven zijn daarom bijna altijd een nv.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bv kan enkel opgericht worden door minstens twee personen.",
        antwoord=False,
        uitleg="Eén oprichter volstaat, net als bij een nv. Dat maakt een bv ook bruikbaar voor wie alleen start maar zijn privévermogen wil beschermen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschilt een bv van een nv? Duid alles aan wat juist is.",
        opties=[
            "Het minimumkapitaal",
            "De overdracht van aandelen",
            "Het besloten karakter",
            "De soort aansprakelijkheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een nv heeft 61 500 euro kapitaal en vrij overdraagbare aandelen, een bv geen vast kapitaal en een besloten karakter. De aansprakelijkheid is bij beide beperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het besloten karakter van een bv?",
        opties=[
            "De aandelen gaan niet vrij over",
            "De vennootschap mag niets verkopen aan particulieren",
            "De jaarrekening hoeft niet neergelegd te worden",
            "De aandeelhouders staan in met hun privévermogen",
        ],
        antwoord=0,
        uitleg="Wie wil verkopen, heeft in principe de toestemming van de andere aandeelhouders nodig. Zo houdt de groep in de hand wie er binnenkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vier vrienden starten samen een zaak en willen niet dat er een onbekende aandeelhouder bij komt. Welke vorm past?",
        opties=[
            "Een bv",
            "Een nv met vrije aandelen",
            "Vier aparte eenmanszaken",
            "Een vereniging zonder winstoogmerk",
        ],
        antwoord=0,
        uitleg="Het besloten karakter van de bv past precies bij die wens: een overdracht van aandelen kan niet zonder de toestemming van de anderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf staat op de beurs en heeft duizenden aandeelhouders. Welke vorm heeft het?",
        opties=[
            "Een nv",
            "Een bv met een besloten karakter",
            "Een eenmanszaak met veel personeel",
            "Een vereniging zonder winstoogmerk",
        ],
        antwoord=0,
        uitleg="Op de beurs moeten aandelen van hand tot hand kunnen gaan. Dat kan alleen bij een nv, waar de aandelen vrij overdraagbaar zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welke belasting betaalt een nv op haar winst?",
        antwoord=["vennootschapsbelasting", "de vennootschapsbelasting"],
        uitleg="Vennootschappen betalen vennootschapsbelasting op hun winst. Een eenmanszaak valt onder de personenbelasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke punten vergelijk je ondernemingsvormen met elkaar? Duid alles aan wat juist is.",
        opties=[
            "De aansprakelijkheid",
            "De administratie",
            "De fiscaliteit",
            "Het aantal klanten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aansprakelijkheid, administratie en belastingen zijn de drie grote vergelijkingspunten, naast kapitaal, aantal oprichters en de overdracht van aandelen. Hoeveel klanten je hebt, hangt niet van de vorm af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen hebben een vermogen dat losstaat van het privévermogen van de oprichters? Duid alles aan wat juist is.",
        opties=[
            "De bv",
            "De nv",
            "De eenmanszaak",
            "De zelfstandige in bijberoep",
        ],
        antwoord=[0, 1],
        uitleg="Een bv en een nv zijn rechtspersonen met een eigen vermogen. Bij een eenmanszaak, ook in bijberoep, is er maar één vermogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie staat er in voor de schulden van een nv?",
        opties=[
            "De vennootschap zelf",
            "Elke aandeelhouder met zijn privévermogen",
            "De bestuurders met hun persoonlijke spaargeld",
            "De werknemers met een deel van hun loon",
        ],
        antwoord=0,
        uitleg="De nv is een rechtspersoon met een eigen vermogen en betaalt haar schulden daarmee. Een aandeelhouder kan enkel zijn inbreng kwijtspelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met een toereikend aanvangsvermogen bij een bv?",
        opties=[
            "Genoeg startgeld",
            "Een kapitaal van 61 500 euro",
            "Een lening bij de bank van minstens een jaar",
            "Een waarborg die bij de notaris blijft staan",
        ],
        antwoord=0,
        uitleg="De oprichters moeten genoeg middelen inbrengen om de geplande activiteit te dragen, en dat verantwoorden in een financieel plan. Een vast bedrag staat er niet meer in de wet.",
    ),
]
