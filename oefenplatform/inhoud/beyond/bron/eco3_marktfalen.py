# -*- coding: utf-8 -*-
"""Marktmacht, marktfalen, externe effecten en publieke goederen.

Fiche: oorzaken van marktimperfecties (marktmacht en kartelvorming,
asymmetrische informatie, positieve en negatieve externe effecten,
collectieve behoeften en publieke goederen); instrumenten
(antitrust- en mededingingsbeleid, reguleringen en sancties, Pigouviaanse
heffing, verhandelbare vergunningen en emissiehandel, subsidies, patent of
octrooi, collectieve goederen); welvaartsverlies door marktmacht; Belgische
Mededingingsautoriteit (BMA), Dienst voor Mededinging van de FOD Economie,
antitrustbeleid van de EU; deadweight loss door negatieve externe effecten
en Pigouviaanse belasting; positieve externe effecten bevorderen met
subsidies; private, zuiver publieke en quasipublieke goederen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een negatief extern effect?",
        opties=[
            "schade aan derden die niet in de marktprijs zit",
            "een verlies dat een bedrijf zelf lijdt",
            "een hogere prijs door een belasting",
            "een daling van de export van een land",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld luchtvervuiling door een fabriek, die de buurt treft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld is een positief extern effect?",
        opties=[
            "bijen van een imker die ook de buren bestuiven",
            "een fabriek die afvalwater in de rivier loost",
            "lawaai van een disco 's nachts",
            "files door de vele vrachtwagens op de weg",
        ],
        antwoord=0,
        uitleg="De buurman heeft voordeel zonder ervoor te betalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er op een vrije markt met een product dat een negatief extern effect heeft?",
        opties=[
            "er wordt te veel van geproduceerd",
            "er wordt te weinig van geproduceerd",
            "er wordt precies genoeg geproduceerd",
            "er wordt niets van geproduceerd",
        ],
        antwoord=0,
        uitleg="De producent houdt geen rekening met de schade voor anderen, dus de maatschappelijke kost ligt hoger dan zijn kost.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een positief extern effect produceert de vrije markt te weinig.",
        antwoord=True,
        uitleg="Het maatschappelijk voordeel is groter dan wat de koper betaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een Pigouviaanse heffing?",
        opties=[
            "een belasting gelijk aan de schade aan derden",
            "een subsidie voor bedrijven die veel personeel aanwerven",
            "een invoerheffing op producten uit het buitenland",
            "een boete voor bedrijven die een kartel vormen",
        ],
        antwoord=0,
        uitleg="Zo komt de externe kost in de prijs terecht en daalt de productie naar het maatschappelijk optimum.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goed gekozen Pigouviaanse belasting verkleint het welvaartsverlies van een negatief extern effect.",
        antwoord=True,
        uitleg="De productie zakt naar de hoeveelheid die rekening houdt met de schade.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt emissiehandel?",
        opties=[
            "bedrijven kopen en verkopen beperkte uitstootrechten",
            "elk bedrijf mag zoveel uitstoten als het zelf wil",
            "bedrijven betalen een vaste prijs per werknemer",
            "de overheid koopt alle vervuilende fabrieken op",
        ],
        antwoord=0,
        uitleg="Wie goedkoop minder kan uitstoten, verkoopt rechten aan wie dat duur vindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is asymmetrische informatie?",
        opties=[
            "de ene partij weet meer dan de andere",
            "de prijs staat niet in de etalage",
            "het product heeft geen gebruiksaanwijzing",
            "kopers en verkopers spreken een andere taal",
        ],
        antwoord=0,
        uitleg="Denk aan een verkoper van een tweedehandse auto die de gebreken kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oorzaken van marktfalen noemt men? Duid alle juiste antwoorden aan.",
        opties=["externe effecten", "asymmetrische informatie", "volkomen concurrentie", "een goed werkend marktevenwicht"],
        antwoord=[0, 1],
        uitleg="Ook publieke goederen en marktmacht horen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft de overheid een patent of octrooi?",
        opties=[
            "om uitvinders tijdelijk te belonen",
            "om de prijs van alle uitvindingen laag te houden",
            "om concurrentie op elke markt te verbieden",
            "om buitenlandse bedrijven te weren",
        ],
        antwoord=0,
        uitleg="Het patent geeft tijdelijk een monopolie. Zo vergoedt het de kosten van onderzoek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een patent zorgt voor meer concurrentie op de markt van die uitvinding.",
        antwoord=False,
        uitleg="Het geeft tijdelijk marktmacht: niemand anders mag de uitvinding zonder toestemming maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bevordert de overheid positieve externe effecten?",
        opties=[
            "met subsidies",
            "met een extra belasting op die producten",
            "met een quotum dat de productie beperkt",
            "met een maximumprijs onder het evenwicht",
        ],
        antwoord=0,
        uitleg="Een subsidie maakt het product goedkoper, zodat er meer van gekocht wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt het welvaartsverlies bij een negatief extern effect?",
        opties=[
            "in de driehoek voorbij het maatschappelijk optimum",
            "in de rechthoek van de omzet van de producenten",
            "onder de vraagcurve, van nul tot het evenwicht",
            "boven de maatschappelijke kostencurve, links van het optimum",
        ],
        antwoord=0,
        uitleg="Voor de extra stuks is de maatschappelijke kost groter dan wat ze opbrengen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een negatief extern effect ligt de vrije marktprijs te hoog.",
        antwoord=False,
        uitleg="De prijs is te laag: hij bevat de schade aan derden niet. Daardoor wordt er te veel gekocht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instrumenten pakken negatieve externe effecten aan? Duid alle juiste antwoorden aan.",
        opties=["een Pigouviaanse heffing", "verhandelbare emissierechten", "een subsidie per vervuilend stuk", "een maximumprijs onder het evenwicht"],
        antwoord=[0, 1],
        uitleg="Een subsidie zou de vervuilende productie nog vergroten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van een regulering tegen vervuiling?",
        opties=[
            "een uitstootnorm voor nieuwe auto's",
            "een verlaging van de btw op benzine",
            "een subsidie voor kolencentrales",
            "een hogere maximumsnelheid op de autosnelweg",
        ],
        antwoord=0,
        uitleg="De overheid legt een grens op en sanctioneert wie die overschrijdt.",
    ),
    dict(
        type="waarofniet",
        vraag="Asymmetrische informatie kan ervoor zorgen dat goede producten van de markt verdwijnen.",
        antwoord=True,
        uitleg="Als kopers kwaliteit niet kunnen inschatten, willen ze enkel een gemiddelde prijs betalen. Verkopers van goede waar haken af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beperkt de overheid problemen door asymmetrische informatie?",
        opties=[
            "met etiketten, keuringen en garanties",
            "met een belasting op elk verkocht product",
            "met een quotum op de verkoop",
            "met een subsidie voor reclame",
        ],
        antwoord=0,
        uitleg="Zo krijgt de koper meer informatie, zoals bij de verplichte autokeuring.",
    ),
    dict(
        type="waarofniet",
        vraag="Een fabriek die de lucht vervuilt, betaalt op een vrije markt automatisch voor de gezondheidsschade van de buren.",
        antwoord=False,
        uitleg="Net niet: dat is precies waarom het een extern effect is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk welvaartsverlies veroorzaakt marktmacht?",
        opties=[
            "er wordt minder verhandeld aan een hogere prijs",
            "er wordt meer verhandeld aan een lagere prijs",
            "de overheid moet meer subsidies geven",
            "de consumenten moeten meer belastingen betalen",
        ],
        antwoord=0,
        uitleg="Net als bij het monopolie ontstaat een driehoek welvaartsverlies.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn de twee kenmerken van een zuiver publiek goed?",
        opties=[
            "niet-rivaliserend en niet-uitsluitbaar",
            "rivaliserend en uitsluitbaar",
            "duur en zeldzaam",
            "gratis en in beperkte hoeveelheid",
        ],
        antwoord=0,
        uitleg="Mijn gebruik vermindert het jouwe niet, en niemand kan uitgesloten worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk goed is een zuiver publiek goed?",
        opties=["straatverlichting", "een broodje", "een bioscoopticket", "een fiets"],
        antwoord=0,
        uitleg="Iedereen in de straat heeft er licht van, en je kan niemand uitsluiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom biedt de vrije markt zuiver publieke goederen niet of te weinig aan?",
        opties=[
            "niemand kan verplicht worden te betalen, dus mensen liften mee",
            "publieke goederen zijn altijd verboden voor bedrijven",
            "publieke goederen hebben geen nut",
            "consumenten willen er nooit iets voor betalen omdat ze slecht zijn",
        ],
        antwoord=0,
        uitleg="Dat heet het meeliftersprobleem, of free rider-probleem.",
    ),
    dict(
        type="waarofniet",
        vraag="Een privaat goed is rivaliserend en uitsluitbaar.",
        antwoord=True,
        uitleg="Als jij een appel eet, kan ik hem niet meer eten, en wie niet betaalt, krijgt hem niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een collectieve behoefte?",
        opties=[
            "een behoefte die je best samen invult",
            "een behoefte die iedereen afzonderlijk in de winkel invult",
            "een behoefte die enkel bedrijven hebben",
            "een behoefte aan luxegoederen",
        ],
        antwoord=0,
        uitleg="De overheid voorziet daarin, betaald met belastingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld past het best bij een quasipubliek goed?",
        opties=[
            "onderwijs",
            "een dijk tegen overstromingen",
            "de nationale defensie",
            "een pak koekjes",
        ],
        antwoord=0,
        uitleg="Je kan er mensen van uitsluiten, maar de overheid biedt het mee aan omdat het iedereen ten goede komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de Belgische Mededingingsautoriteit (BMA)?",
        opties=[
            "ze spoort kartels en machtsmisbruik op",
            "ze legt de prijzen vast van alle producten in België",
            "ze int de btw voor de federale overheid",
            "ze beheert de staatsschuld van België",
        ],
        antwoord=0,
        uitleg="Ze voert het Belgische en Europese mededingingsrecht uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De BMA kan boetes opleggen aan bedrijven die prijsafspraken maken.",
        antwoord=True,
        uitleg="Kartels zijn verboden en worden beboet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol heeft de Dienst voor Mededinging van de FOD Economie?",
        opties=[
            "ze bewaakt eerlijke concurrentie in België",
            "ze bepaalt het loon van alle Belgische werknemers",
            "ze geeft de vergunningen voor nieuwe banken",
            "ze verdeelt de Europese landbouwsubsidies",
        ],
        antwoord=0,
        uitleg="Ze volgt markten op en werkt samen met de BMA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie voert in de Europese Unie het antitrustbeleid uit?",
        opties=["de Europese Commissie", "de Europese Centrale Bank", "het IMF", "de Wereldbank"],
        antwoord=0,
        uitleg="Ze kan grote boetes opleggen, ook aan wereldwijde techbedrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verbiedt het Europese mededingingsrecht? Duid alle juiste antwoorden aan.",
        opties=[
            "kartelafspraken tussen bedrijven",
            "misbruik van een dominante positie",
            "een groot marktaandeel op zich",
            "concurrentie op prijs",
        ],
        antwoord=[0, 1],
        uitleg="Groot zijn mag, misbruik maken van die macht niet. Fusies worden ook gecontroleerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf met een groot marktaandeel is in de EU automatisch in overtreding.",
        antwoord=False,
        uitleg="Pas misbruik van die dominante positie is verboden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verandert een Pigouviaanse belasting het marktevenwicht bij vervuiling?",
        opties=[
            "de prijs stijgt en de hoeveelheid daalt",
            "de prijs daalt en de hoeveelheid stijgt",
            "de prijs en de hoeveelheid blijven gelijk",
            "de productie stopt helemaal",
        ],
        antwoord=0,
        uitleg="De aanbodcurve schuift omhoog met de externe kost.",
    ),
    dict(
        type="invultekst",
        vraag="Elk verkocht stuk veroorzaakt 5 euro schade aan derden. Hoe groot moet een Pigouviaanse belasting per stuk zijn, in euro?",
        antwoord=["5", "vijf", "5 euro"],
        uitleg="De belasting is gelijk aan de marginale externe kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vaccin beschermt ook wie niet gevaccineerd is. Wat doet de overheid best?",
        opties=[
            "het vaccin subsidiëren of gratis aanbieden",
            "een extra belasting op vaccins heffen",
            "een quotum op het aantal vaccins invoeren",
            "het vaccin aan de vrije markt overlaten",
        ],
        antwoord=0,
        uitleg="Er is een positief extern effect, dus de vrije markt zou te weinig vaccins opleveren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuiver publiek goed is uitsluitbaar: wie niet betaalt, kan het niet gebruiken.",
        antwoord=False,
        uitleg="Het is net niet-uitsluitbaar. Daarom liften mensen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke goederen zijn zuiver publiek? Duid alle juiste antwoorden aan.",
        opties=["landsverdediging", "een dijk die een stad beschermt", "een treinticket", "een appartement"],
        antwoord=[0, 1],
        uitleg="Een ticket en een appartement zijn uitsluitbaar en rivaliserend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meelifter (free rider)?",
        opties=[
            "iemand die gebruikt zonder te betalen",
            "iemand die altijd met het openbaar vervoer reist",
            "een bedrijf dat de prijzen van de concurrent volgt",
            "een consument die enkel in de solden koopt",
        ],
        antwoord=0,
        uitleg="Bij publieke goederen kan dat, omdat niemand uitgesloten wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Verhandelbare vergunningen zorgen ervoor dat uitstoot verminderd wordt waar dat het goedkoopst kan.",
        antwoord=True,
        uitleg="Bedrijven die goedkoop kunnen verminderen, verkopen hun overschot aan rechten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een negatief extern effect is de privékost van de producent hoger dan de maatschappelijke kost.",
        antwoord=False,
        uitleg="Omgekeerd: de maatschappelijke kost is de privékost plus de schade aan derden.",
    ),
]
