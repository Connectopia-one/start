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
        vraag=r"Wat betekent \(n!\)?",
        opties=[
            r"\(n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1\)",
            r"\(1 + 2 + \ldots + n\)",
            r"\(n^{n}\)",
            r"het aantal delers van \(n\)",
        ],
        antwoord=0,
        uitleg=r"\(5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Op hoeveel manieren kan je vijf verschillende boeken naast elkaar zetten?",
        opties=[r"\(120\)", r"\(25\)", r"\(15\)", r"\(10\)"],
        antwoord=0,
        uitleg=r"Dat is een permutatie van vijf elementen, dus \(5! = 120\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(0!\)? Schrijf het getal.",
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
        uitleg=r"\(V_{n}^{p} = \dfrac{n!}{(n-p)!}\) en \(\binom{n}{p} = \dfrac{n!}{p!\,(n-p)!}\): elke combinatie staat voor \(p!\) volgordes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel codes van vier cijfers bestaan er, als elk cijfer van nul tot negen mag en herhaling toegelaten is?",
        opties=[r"\(10\,000\)", r"\(5000\)", r"\(5040\)", r"\(200\)"],
        antwoord=0,
        uitleg=r"Vier keer tien keuzes na elkaar, dus \(10^{4}\). Dat is een herhalingsvariatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een herhalingsvariatie mag elk element maar één keer voorkomen.",
        antwoord=False,
        uitleg="Net omgekeerd: herhaling is daar toegelaten. Bij een gewone variatie mag het niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\binom{5}{2}\)? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg=r"\(\dfrac{5 \cdot 4}{2} = 10\), want elk tweetal telde je dubbel.",
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
        vraag=r"Hoeveel is \(5!\)? Schrijf het getal.",
        antwoord=["120", "honderdtwintig"],
        uitleg=r"\(5 \cdot 4 = 20\), maal \(3\) is \(60\), maal \(2\) is \(120\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel verschillende woorden kan je maken met de letters van MAMA?",
        opties=[r"\(6\)", r"\(24\)", r"\(12\)", r"\(4\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{4!}{2!\,2!} = 6\), want de twee M's en de twee A's zijn onderling niet te onderscheiden. Dat is een herhalingspermutatie.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\binom{n}{p} = \binom{n}{n-p}\).",
        antwoord=True,
        uitleg="Wie je kiest, bepaalt meteen wie je niet kiest. Daarom is de driehoek van Pascal symmetrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zes mensen geven elkaar allemaal één keer een hand. Hoeveel handdrukken zijn dat?",
        opties=[r"\(15\)", r"\(30\)", r"\(36\)", r"\(12\)"],
        antwoord=0,
        uitleg=r"Je kiest telkens twee mensen uit zes, zonder volgorde: \(\binom{6}{2} = \dfrac{6 \cdot 5}{2} = 15\).",
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
        vraag=r"Bij dezelfde \(n\) en \(p\) zijn er altijd meer combinaties dan variaties.",
        antwoord=False,
        uitleg=r"Net minder: \(\binom{n}{p} = \dfrac{V_{n}^{p}}{p!}\), want alle volgordes van dezelfde keuze vallen samen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\binom{10}{1}\)? Schrijf het getal.",
        antwoord=["10", "tien"],
        uitleg=r"Eén uit \(n\) kiezen kan altijd op \(n\) manieren.",
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
        uitleg=r"Dus \(\binom{12}{3}\). Zou je een voorzitter, een secretaris en een penningmeester kiezen, dan was het wel een variatie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvoor dient het sommatieteken \(\sum\)?",
        opties=[
            "om een lange som kort te schrijven met een lopende index",
            "om aan te geven dat je twee getallen moet optellen",
            "om de volgorde van de termen in een som vast te leggen",
            "om een product van veel factoren kort op te schrijven",
        ],
        antwoord=0,
        uitleg=r"In \(\sum_{k=1}^{n} k\) staat onder het teken waar de index begint en erboven waar hij eindigt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de driehoek van Pascal?",
        opties=[
            r"de binomiaalcoëfficiënten \(\binom{n}{k}\), rij per rij",
            r"de faculteiten \(n!\) op volgorde",
            r"de machten \(2^{n}\) op volgorde",
            r"de priemgetallen in een driehoekig patroon",
        ],
        antwoord=0,
        uitleg=r"Rij \(n\) bevat de coëfficiënten die je nodig hebt om een tweeterm tot de macht \(n\) uit te werken.",
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
        uitleg=r"Dat is de formule van Stifel-Pascal: \(\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel termen heeft \(\left(a + b\right)^{5}\), volledig uitgewerkt? Schrijf het cijfer.",
        antwoord=["6", "zes"],
        uitleg=r"Altijd één meer dan de exponent, want de macht van \(a\) loopt van \(5\) tot \(0\).",
    ),
    dict(
        type="waarofniet",
        vraag="De formule van Stifel-Pascal schrijft één binomiaalcoëfficiënt als de som van twee andere uit de vorige rij.",
        antwoord=True,
        uitleg="Daarmee bouw je de hele driehoek op zonder één faculteit te berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe werk je \(\left(a + b\right)^{3}\) uit?",
        opties=[
            r"\(a^{3} + 3a^{2}b + 3ab^{2} + b^{3}\)",
            r"\(a^{3} + b^{3}\)",
            r"\(a^{3} + a^{2}b + ab^{2} + b^{3}\)",
            r"\(3a^{3} + 3b^{3}\)",
        ],
        antwoord=0,
        uitleg=r"De coëfficiënten \(1,\ 3,\ 3,\ 1\) zijn net de vierde rij van de driehoek van Pascal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke coëfficiënt hoort bij \(a^{2}b\) in \(\left(a + b\right)^{3}\)?",
        opties=[r"\(3\)", r"\(1\)", r"\(2\)", r"\(6\)"],
        antwoord=0,
        uitleg=r"Je kiest uit de drie factoren er één waaruit je \(b\) neemt: \(\binom{3}{1} = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sum_{k=0}^{n} \binom{n}{k} = 2^{n}\).",
        antwoord=True,
        uitleg=r"Rij \(n\) telt op tot \(2^{n}\). Dat is ook het aantal deelverzamelingen van een verzameling met \(n\) elementen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\binom{4}{2}\)? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg=r"Dat is het middelste getal van de rij \(1,\ 4,\ 6,\ 4,\ 1\).",
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
        uitleg=r"\(\left(a + b\right)^{n} = \sum_{k=0}^{n} \binom{n}{k} a^{\,n-k} b^{k}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\left(a + b\right)^{2} = a^{2} + b^{2}\).",
        antwoord=False,
        uitleg=r"De middelste term \(2ab\) ontbreekt. De tweede rij van Pascal is \(1,\ 2,\ 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk getal staat er altijd aan het begin en op het einde van een rij in de driehoek van Pascal?",
        opties=[r"\(1\)", r"\(0\)", r"\(2\)", r"het rijnummer \(n\)"],
        antwoord=0,
        uitleg=r"\(\binom{n}{0} = \binom{n}{n} = 1\): er is maar één manier om niets te kiezen en maar één om alles te kiezen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Welke coëfficiënt heeft \(x^{2}\) in \(\left(1 + x\right)^{4}\)? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg=r"De rij is \(1,\ 4,\ 6,\ 4,\ 1\), en je neemt het getal bij \(x^{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je één bepaalde term van een macht van een tweeterm zonder alles uit te werken?",
        opties=[
            r"met de algemene term \(\binom{n}{k} a^{\,n-k} b^{k}\)",
            "door de hele driehoek van Pascal uit te schrijven",
            "door de macht in kleinere machten op te splitsen",
            "door de twee termen apart tot die macht te verheffen",
        ],
        antwoord=0,
        uitleg=r"Je vult de juiste \(k\) in en krijgt meteen de coëfficiënt en de twee machten.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(\left(a - b\right)^{n}\) wisselen de tekens van term tot term.",
        antwoord=True,
        uitleg=r"Je past het binomium toe met \(-b\) in plaats van \(b\), en elke oneven macht van \(-b\) is negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\binom{n}{0}\)?",
        opties=[r"\(1\)", r"\(0\)", r"\(n\)", r"\(n!\)"],
        antwoord=0,
        uitleg="Niets kiezen kan precies op één manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is elke rij van de driehoek van Pascal symmetrisch?",
        opties=[
            r"omdat \(p\) kiezen hetzelfde is als \(n - p\) weglaten",
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
        uitleg=r"De binomiale verdeling gebruikt net \(\binom{n}{k}\): die telt op hoeveel manieren \(k\) successen in \(n\) pogingen kunnen vallen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(1 + 3 + 3 + 1\), een rij uit de driehoek van Pascal? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg=r"\(8 = 2^{3}\), en \(3\) is het rijnummer.",
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
        uitleg=r"Een paar getallen invullen toont alleen dat het dáár klopt. Een telkundige redenering mag ook, als ze voor alle \(n\) geldt.",
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
