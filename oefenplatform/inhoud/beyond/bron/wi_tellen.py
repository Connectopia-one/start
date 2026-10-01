# -*- coding: utf-8 -*-
"""Telproblemen, de driehoek van Pascal en het binomium van Newton.

Het eerste stuk van het onderdeel "Telproblemen, kansrekenen en statistiek"
van fiche G2. Samen met de twee volgende thema's weegt dat onderdeel
vierenveertig procent van dat examen.

Deel 1 zijn de telproblemen zelf: faculteit, permutaties, variaties,
combinaties en de drie telregels.
Deel 2 is de driehoek van Pascal en het binomium van Newton.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent n faculteit?",
        opties=[
            "het product van alle natuurlijke getallen van één tot en met n",
            "de som van alle natuurlijke getallen van één tot en met n",
            "het getal n vermenigvuldigd met zichzelf, n keer na elkaar",
            "het aantal delers dat het getal n in totaal heeft",
        ],
        antwoord=0,
        uitleg="Vijf faculteit is dus vijf maal vier maal drie maal twee maal één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op hoeveel manieren kan je vijf verschillende boeken naast elkaar zetten?",
        opties=["honderdtwintig", "vijfentwintig", "vijftien", "tien"],
        antwoord=0,
        uitleg="Dat is een permutatie van vijf elementen, dus vijf faculteit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is nul faculteit? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="Dat is een afspraak die alle formules kloppend houdt: er is precies één manier om niets te rangschikken.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een variatie telt de volgorde mee.",
        antwoord=True,
        uitleg="Goud, zilver en brons is een variatie. Drie leden van een jury kiezen is een combinatie, want daar is er geen volgorde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een variatie en een combinatie?",
        opties=[
            "bij een variatie telt de volgorde mee en bij een combinatie niet",
            "bij een combinatie telt de volgorde mee en bij een variatie niet",
            "bij een variatie mag je elementen herhalen en bij een combinatie niet",
            "bij een combinatie gebruik je alle elementen en bij een variatie niet",
        ],
        antwoord=0,
        uitleg="Daarom zijn er altijd minder combinaties dan variaties: elke combinatie staat voor meerdere volgordes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel codes van vier cijfers bestaan er, als elk cijfer van nul tot negen mag en herhaling toegelaten is?",
        opties=["tienduizend", "vijfduizend", "vijfduizendveertig", "tweehonderd",],
        antwoord=0,
        uitleg="Vier keer tien keuzes na elkaar, dus tien tot de vierde. Dat is een herhalingsvariatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een herhalingsvariatie mag elk element maar één keer voorkomen.",
        antwoord=False,
        uitleg="Net omgekeerd: herhaling is daar toegelaten. Bij een gewone variatie mag het niet.",
    ),
    dict(
        type="invultekst",
        vraag="Op hoeveel manieren kan je twee personen kiezen uit vijf, als de volgorde niet telt? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg="Vijf maal vier gedeeld door twee, want elk tweetal telde je dubbel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je de somregel?",
        opties=[
            "als je moet kiezen tussen twee mogelijkheden die elkaar uitsluiten",
            "als je twee keuzes na elkaar moet maken binnen dezelfde opgave",
            "als de volgorde van de gekozen elementen geen rol speelt",
            "als je wil tellen hoeveel mogelijkheden er in totaal zijn",
        ],
        antwoord=0,
        uitleg="Of-of betekent optellen, en-en betekent vermenigvuldigen. Dat onderscheid is de kern van elk telprobleem.",
    ),
    dict(
        type="waarofniet",
        vraag="De productregel gebruik je bij keuzes die na elkaar komen.",
        antwoord=True,
        uitleg="Eerst een hoofdgerecht en daarna een dessert: je vermenigvuldigt het aantal mogelijkheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de complementregel?",
        opties=[
            "tel het aantal gevallen dat niet voldoet en trek dat van het totaal af",
            "tel het aantal gevallen dat voldoet en vermenigvuldig dat met twee",
            "tel beide soorten gevallen apart en tel die twee aantallen op",
            "deel het totale aantal gevallen door het aantal dat voldoet",
        ],
        antwoord=0,
        uitleg="Bij een opgave met de woorden minstens of hoogstens is dat vaak veel korter werk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is vijf faculteit? Schrijf het getal.",
        antwoord=["120", "honderdtwintig"],
        uitleg="Vijf maal vier is twintig, maal drie is zestig, maal twee is honderdtwintig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel verschillende woorden kan je maken met de letters van MAMA?",
        opties=["zes", "vierentwintig", "twaalf", "vier"],
        antwoord=0,
        uitleg="Vier faculteit gedeeld door twee faculteit maal twee faculteit, want de twee M's en de twee A's zijn onderling niet te onderscheiden. Dat is een herhalingspermutatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal manieren om p uit n te kiezen is even groot als het aantal manieren om n min p uit n te kiezen.",
        antwoord=True,
        uitleg="Wie je kiest, bepaalt meteen wie je niet kiest. Daarom is de driehoek van Pascal symmetrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zes mensen geven elkaar allemaal één keer een hand. Hoeveel handdrukken zijn dat?",
        opties=["vijftien", "dertig", "zesendertig", "twaalf"],
        antwoord=0,
        uitleg="Je kiest telkens twee mensen uit zes, zonder volgorde: zes maal vijf gedeeld door twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een herhalingspermutatie?",
        opties=[
            "een rangschikking van alle elementen waarvan er enkele gelijk zijn",
            "een rangschikking waarbij je elk element zo vaak mag nemen als je wil",
            "een keuze van enkele elementen waarbij de volgorde niet telt",
            "een keuze waarbij je telkens hetzelfde element opnieuw neemt",
        ],
        antwoord=0,
        uitleg="Je deelt dan door de faculteiten van de groepjes gelijke elementen, zoals bij het woord MAMA.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dezelfde n en p zijn er altijd meer combinaties dan variaties.",
        antwoord=False,
        uitleg="Net minder: bij een combinatie vallen alle volgordes van dezelfde keuze samen.",
    ),
    dict(
        type="invultekst",
        vraag="Op hoeveel manieren kan je één persoon kiezen uit tien? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg="Eén uit n kiezen kan altijd op n manieren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kiest een jury van drie mensen uit twaalf kandidaten. Welk telprobleem is dat?",
        opties=[
            "een combinatie, want de volgorde van de drie telt niet mee",
            "een variatie, want de drie plaatsen zijn verschillend",
            "een permutatie, want je rangschikt alle kandidaten",
            "een herhalingsvariatie, want iemand kan twee keer meedoen",
        ],
        antwoord=0,
        uitleg="Zou je een voorzitter, een secretaris en een penningmeester kiezen, dan was het wel een variatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het sommatieteken?",
        opties=[
            "om een lange som kort te schrijven met een lopende index",
            "om aan te geven dat je twee getallen moet optellen",
            "om de volgorde van de termen in een som vast te leggen",
            "om een product van veel factoren kort op te schrijven",
        ],
        antwoord=0,
        uitleg="Onder het teken staat waar de index begint, erboven waar hij eindigt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de driehoek van Pascal?",
        opties=[
            "de binomiaalcoëfficiënten, rij per rij",
            "de faculteiten van de natuurlijke getallen",
            "de machten van het getal twee op volgorde",
            "de priemgetallen in een driehoekig patroon",
        ],
        antwoord=0,
        uitleg="Rij n bevat de coëfficiënten die je nodig hebt om een tweeterm tot de macht n uit te werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je een getal in de driehoek van Pascal?",
        opties=[
            "als de som van de twee getallen schuin erboven",
            "als het product van de twee getallen schuin erboven",
            "als het dubbel van het getal er links van",
            "als het verschil van de twee getallen schuin erboven",
        ],
        antwoord=0,
        uitleg="Dat is net wat de formule van Stifel-Pascal in symbolen zegt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel termen heeft a plus b, tot de vijfde macht, volledig uitgewerkt? Schrijf het cijfer.",
        antwoord=["6", "zes"],
        uitleg="Altijd één meer dan de exponent, want de macht van a loopt van vijf tot nul.",
    ),
    dict(
        type="waarofniet",
        vraag="De formule van Stifel-Pascal schrijft één binomiaalcoëfficiënt als de som van twee andere uit de vorige rij.",
        antwoord=True,
        uitleg="Daarmee bouw je de hele driehoek op zonder één faculteit te berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werk je a plus b, tot de derde macht, uit?",
        opties=[
            "a tot de derde, plus drie a kwadraat b, plus drie a b kwadraat, plus b tot de derde",
            "a tot de derde plus b tot de derde, en verder niets",
            "a tot de derde, plus a kwadraat maal b, plus a maal b kwadraat, plus b tot de derde",
            "drie a tot de derde, plus drie b tot de derde, bij elkaar opgeteld",
        ],
        antwoord=0,
        uitleg="De coëfficiënten één, drie, drie, één zijn net de vierde rij van de driehoek van Pascal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coëfficiënt hoort bij a kwadraat b in de uitwerking van a plus b tot de derde?",
        opties=["drie", "één", "twee", "zes"],
        antwoord=0,
        uitleg="Je kiest uit de drie factoren er één waaruit je b neemt, en dat kan op drie manieren.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van alle getallen in een rij van de driehoek van Pascal is een macht van twee.",
        antwoord=True,
        uitleg="Rij n telt op tot twee tot de macht n. Dat is ook het aantal deelverzamelingen van een verzameling met n elementen.",
    ),
    dict(
        type="invultekst",
        vraag="Op hoeveel manieren kan je twee elementen kiezen uit vier? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg="Dat is het middelste getal van de rij één, vier, zes, vier, één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het binomium van Newton?",
        opties=[
            "het geeft de uitwerking van een tweeterm tot een willekeurige macht",
            "het geeft het aantal manieren om n elementen te gaan rangschikken",
            "het berekent de som van de eerste n natuurlijke getallen",
            "het bewijst dat elke veelterm een nulwaarde heeft",
        ],
        antwoord=0,
        uitleg="Elke term bestaat uit een binomiaalcoëfficiënt maal een macht van a maal een macht van b.",
    ),
    dict(
        type="waarofniet",
        vraag="a plus b, in het kwadraat, is gelijk aan a kwadraat plus b kwadraat.",
        antwoord=False,
        uitleg="De middelste term twee ab ontbreekt. De tweede rij van Pascal is één, twee, één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk getal staat er altijd aan het begin en op het einde van een rij in de driehoek van Pascal?",
        opties=["één", "nul", "twee", "het rijnummer"],
        antwoord=0,
        uitleg="Er is maar één manier om niets te kiezen en maar één manier om alles te kiezen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke coëfficiënt heeft x kwadraat in de uitwerking van één plus x, tot de vierde macht? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg="De rij is één, vier, zes, vier, één, en je neemt het getal bij x kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je één bepaalde term van een macht van een tweeterm zonder alles uit te werken?",
        opties=[
            "met de algemene term uit het binomium van Newton",
            "door de hele driehoek van Pascal uit te schrijven",
            "door de macht in kleinere machten op te splitsen",
            "door de twee termen apart tot die macht te verheffen",
        ],
        antwoord=0,
        uitleg="Je vult de juiste index in en krijgt meteen de coëfficiënt en de twee machten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij a min b tot de macht n wisselen de tekens van term tot term.",
        antwoord=True,
        uitleg="Je past het binomium toe met min b in plaats van b, en elke oneven macht van min b is negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op hoeveel manieren kan je nul elementen kiezen uit n?",
        opties=["één", "nul", "n", "n faculteit"],
        antwoord=0,
        uitleg="Niets kiezen kan precies op één manier, en daarom is die binomiaalcoëfficiënt gelijk aan één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is elke rij van de driehoek van Pascal symmetrisch?",
        opties=[
            "omdat p elementen kiezen hetzelfde is als n min p elementen weglaten",
            "omdat elk getal de som is van de twee getallen die er schuin boven staan",
            "omdat elke rij altijd begint en eindigt met het getal één",
            "omdat de som van elke rij een macht van twee is",
        ],
        antwoord=0,
        uitleg="Elke keuze hoort bij precies één groep die je niet kiest, dus de twee aantallen zijn gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De driehoek van Pascal heeft niets te maken met kansrekening.",
        antwoord=False,
        uitleg="De binomiale verdeling gebruikt net die coëfficiënten: ze tellen op hoeveel manieren k successen in n pogingen kunnen vallen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de rij één, drie, drie, één uit de driehoek van Pascal? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg="Acht is twee tot de derde, en drie is het rijnummer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bewijs je een identiteit met binomiaalcoëfficiënten?",
        opties=[
            "door beide leden met faculteiten uit te schrijven en te vereenvoudigen",
            "door enkele getallen in te vullen en te zien dat het dan klopt",
            "door de driehoek van Pascal tot en met de tiende rij uit te tekenen",
            "door de twee leden van elkaar af te trekken en dan af te ronden",
        ],
        antwoord=0,
        uitleg="Een paar getallen invullen toont alleen dat het dáár klopt. Een telkundige redenering mag ook, als ze voor alle n geldt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet het binomium van Newton zo?",
        opties=[
            "omdat het over een macht van een tweeterm gaat",
            "omdat Newton de driehoek van Pascal uitvond",
            "omdat er twee verschillende formules in staan",
            "omdat je het alleen bij de tweede macht gebruikt",
        ],
        antwoord=0,
        uitleg="Een binomium is een som van twee termen. De formule geldt voor elke macht, niet alleen de tweede.",
    ),
]
