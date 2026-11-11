# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Het bloed.

Biologie, blok "Stofwisselingsfysiologie en secretie", kop "Het
bloedvatenstelsel: het bloed". Deel 1 gaat over de bestanddelen van het bloed
en de rode bloedcellen, deel 2 over witte bloedcellen, bloedstolling en
bloedgroepen.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "Welke celtypes vind je in het bloed? Kruis alles aan wat juist is.",
        ["rode bloedcellen of erytrocyten", "witte bloedcellen of leukocyten", "bloedplaatjes of trombocyten", "podocyten"],
        [0, 1, 2],
        "Bloed bevat rode bloedcellen, witte bloedcellen en bloedplaatjes. Podocyten zijn cellen van de nierfilter.",
    ),
    M(
        "Waar worden de bloedcellen bij een volwassene gevormd?",
        ["in het rode beenmerg", "in de lever", "in de nieren", "in het hart"],
        0,
        "Alle bloedcellen ontstaan uit stamcellen in het rode beenmerg, onder meer in de platte beenderen en de uiteinden van de pijpbeenderen.",
    ),
    M(
        "Welke bloedcellen zijn het talrijkst?",
        ["de rode bloedcellen", "de witte bloedcellen", "de bloedplaatjes", "ze komen even vaak voor"],
        0,
        "In één microliter bloed zitten ongeveer vijf miljoen rode bloedcellen, tegenover enkele honderdduizenden bloedplaatjes en enkele duizenden witte bloedcellen.",
    ),
    W(
        "Een rijpe rode bloedcel van de mens heeft geen celkern.",
        True,
        "Rode bloedcellen verliezen hun kern tijdens hun rijping. Zo is er meer plaats voor hemoglobine, maar ze kunnen zich ook niet meer delen of herstellen.",
    ),
    M(
        "Hoe lang leeft een rode bloedcel ongeveer?",
        ["ongeveer 120 dagen", "ongeveer 2 dagen", "ongeveer 10 jaar", "een heel leven lang"],
        0,
        "Na ongeveer vier maanden worden versleten rode bloedcellen afgebroken in de milt en de lever.",
    ),
    M(
        "Welke vorm heeft een rode bloedcel, en waarom is dat handig?",
        [
            "een schijfje dat aan beide kanten ingedeukt is, met een groot oppervlak voor gasuitwisseling",
            "een bolletje met uitsteeksels, zodat het zich aan de vaatwand kan vasthaken",
            "een lange draad, zodat het makkelijk door de nierfilter kan glippen",
            "een onregelmatige vorm die verandert om bacteriën op te slokken",
        ],
        0,
        "De dubbelholle schijfvorm geeft veel oppervlak voor de opname van zuurstof en maakt de cel soepel genoeg om door smalle haarvaten te wringen.",
    ),
    I(
        "Hoe heet het ijzerhoudende eiwit in de rode bloedcellen dat zuurstof bindt?",
        "hemoglobine",
        "Hemoglobine bestaat uit vier subeenheden, elk met een heemgroep met een ijzeratoom. Elke heemgroep kan één zuurstofmolecule binden.",
    ),
    M(
        "Hoeveel zuurstofmoleculen kan één hemoglobinemolecule maximaal binden?",
        ["vier", "één", "twee", "acht"],
        0,
        "Hemoglobine heeft vier subeenheden met elk een heemgroep. Elke heemgroep bindt één O₂-molecule, dus samen vier.",
    ),
    I(
        "Hoe noemt men hemoglobine waaraan zuurstof gebonden is?",
        "oxyhemoglobine",
        "In de longen bindt hemoglobine zuurstof en wordt het oxyhemoglobine, dat helderrood is. In de weefsels laat het de zuurstof weer los.",
    ),
    M(
        "Wat geeft de hematocrietwaarde aan?",
        [
            "het percentage van het bloedvolume dat uit rode bloedcellen bestaat",
            "het aantal witte bloedcellen per liter bloed",
            "de hoeveelheid suiker die in het bloedplasma opgelost is",
            "de druk waarmee het bloed bij elke hartslag tegen de wand van de slagaders duwt",
        ],
        0,
        "Bij een gezonde volwassene is de hematocriet ongeveer 40 à 45 %. Dat is het deel van het bloed dat uit rode bloedcellen bestaat.",
    ),
    M(
        "Waarom gaan sommige sporters op hoogtestage?",
        [
            "in de ijle lucht maken hun nieren meer EPO, zodat ze meer rode bloedcellen krijgen",
            "in de koude lucht verbranden ze meer vet en worden ze lichter",
            "op grote hoogte wordt hun bloed dunner, zodat het hart minder hard moet werken",
            "op grote hoogte neemt het aantal witte bloedcellen toe en worden ze minder snel ziek",
        ],
        0,
        "Op hoogte is er minder zuurstof, wat hypoxie veroorzaakt. De nieren maken dan meer EPO, de hematocriet stijgt en het bloed kan meer zuurstof vervoeren.",
    ),
    W(
        "Een te hoge hematocrietwaarde is onschadelijk, want meer rode bloedcellen betekent gewoon meer zuurstof.",
        False,
        "Een te hoge hematocriet maakt het bloed dik. Dan stijgt het risico op bloedklonters, een herseninfarct of een hartinfarct. Daarom is EPO-doping gevaarlijk.",
    ),
    M(
        "Een buisje bloed met een middel tegen stolling wordt gecentrifugeerd. Welke lagen zie je van onder naar boven?",
        [
            "rode bloedcellen, een dun laagje witte bloedcellen en bloedplaatjes, en bovenaan plasma",
            "plasma, een dun laagje witte bloedcellen en bloedplaatjes, en bovenaan rode bloedcellen",
            "witte bloedcellen, rode bloedcellen, en bovenaan bloedplaatjes",
            "een stolsel onderaan en bovenaan een heldere laag serum",
        ],
        0,
        "De zware rode bloedcellen zakken naar de bodem. Daarboven ligt een dun wit laagje met witte bloedcellen en bloedplaatjes, en bovenaan het gelige plasma.",
    ),
    M(
        "Wat is het verschil tussen bloedplasma en bloedserum?",
        [
            "serum is plasma zonder de stollingsfactoren zoals fibrinogeen",
            "serum is plasma met de rode bloedcellen er nog in",
            "plasma is het vocht uit de lymfevaten en serum het vocht uit de aders",
            "er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        0,
        "Laat je bloed stollen, dan worden de stollingsfactoren in het stolsel gebruikt. Het vocht dat overblijft is serum.",
    ),
    M(
        "Welke stoffen worden door het bloedplasma vervoerd? Kruis alles aan wat juist is.",
        ["voedingsstoffen zoals glucose", "hormonen", "afvalstoffen zoals ureum", "chylomicronen uit de lymfe vóór ze in het bloed komen"],
        [0, 1, 2],
        "Het plasma vervoert voedingsstoffen, hormonen, afvalstoffen, zouten en eiwitten zoals albumine en globulines. Chylomicronen zitten eerst in de lymfe en komen pas later in het bloed.",
    ),
    M(
        "Welk eiwit komt het meest voor in het bloedplasma en helpt water in de bloedvaten te houden?",
        ["albumine", "hemoglobine", "fibrine", "pepsine"],
        0,
        "Albumine is het meest voorkomende plasma-eiwit. Het houdt water in de bloedbaan vast en vervoert onder meer vetzuren en hormonen.",
    ),
    W(
        "Het meeste CO₂ wordt in het bloed vervoerd als waterstofcarbonaat, opgelost in het plasma.",
        True,
        "Het grootste deel van het CO₂ wordt in de rode bloedcellen omgezet en reist als HCO₃⁻ in het plasma. Een kleiner deel is aan hemoglobine gebonden of gewoon opgelost.",
    ),
    M(
        "Welke uitspraak over EPO is juist?",
        [
            "het is een hormoon uit de nieren dat de aanmaak van rode bloedcellen stimuleert",
            "het is een enzym uit de maag dat in een zuur midden de lange eiwitten in het voedsel afbreekt",
            "het is een witte bloedcel die bacteriën opeet",
            "het is een stollingsfactor die het stolsel stevig maakt",
        ],
        0,
        "Erytropoëtine wordt vooral in de nieren gemaakt bij zuurstoftekort. Als doping is het verboden en gevaarlijk.",
    ),
    W(
        "Zuurstof wordt in het bloed vooral opgelost in het plasma vervoerd, en maar voor een klein deel gebonden aan hemoglobine.",
        False,
        "Het is omgekeerd: ongeveer 98 % van de zuurstof zit gebonden aan hemoglobine. Maar een klein deel is opgelost in het plasma.",
    ),
    M(
        "Waar worden versleten rode bloedcellen vooral afgebroken?",
        ["in de milt en de lever", "in de nieren en de blaas", "in de longen", "in het rode beenmerg"],
        0,
        "Macrofagen in de milt en de lever breken oude rode bloedcellen af. Het ijzer wordt hergebruikt om nieuwe hemoglobine te maken.",
    ),
]

DEEL2 = [
    M(
        "Wat is de hoofdtaak van de witte bloedcellen?",
        ["de afweer tegen ziekteverwekkers", "het vervoer van zuurstof", "het dichten van wondjes en het stelpen van bloed", "het vervoer van voedingsstoffen"],
        0,
        "Witte bloedcellen verdedigen het lichaam, onder meer door ziekteverwekkers op te eten of antilichamen te maken.",
    ),
    M(
        "Welke witte bloedcellen zijn granulocyten? Kruis alles aan wat juist is.",
        ["neutrofielen", "eosinofielen", "monocyten", "lymfocyten"],
        [0, 1],
        "Granulocyten hebben korrels in hun cytoplasma: neutrofielen, eosinofielen en basofielen. Lymfocyten en monocyten zijn agranulocyten.",
    ),
    M(
        "Welke witte bloedcellen zijn het talrijkst en ruimen bij een ontsteking als eersten bacteriën op door fagocytose?",
        ["de neutrofielen", "de basofielen", "de B-lymfocyten", "de bloedplaatjes"],
        0,
        "Neutrofielen zijn de meest voorkomende witte bloedcellen. Ze komen snel naar een ontsteking en eten bacteriën op.",
    ),
    I(
        "Hoe noemt men het opslokken van een bacterie door een witte bloedcel?",
        "fagocytose",
        "Bij fagocytose omsluit de cel de bacterie met haar membraan en verteert ze die in een blaasje met enzymen.",
    ),
    M(
        "Een monocyt verlaat het bloed en gaat het weefsel in. Wat wordt hij daar?",
        ["een macrofaag", "een rode bloedcel", "een bloedplaatje", "een plasmacel"],
        0,
        "Monocyten worden in het weefsel macrofagen, grote eetcellen die ziekteverwekkers en celresten opruimen.",
    ),
    M(
        "Welke witte bloedcellen maken antilichamen?",
        [
            "B-lymfocyten, na activatie als plasmacellen",
            "neutrofielen, zodra ze een bacterie opgegeten hebben",
            "T-lymfocyten, door de antilichamen in het bloed los te laten",
            "basofielen, door histamine vrij te maken",
        ],
        0,
        "B-lymfocyten worden na activatie plasmacellen die antilichamen maken. Dat heet humorale afweer. T-lymfocyten zorgen voor de cellulaire afweer.",
    ),
    W(
        "Bij de cellulaire afweer doden T-lymfocyten zelf lichaamscellen die besmet zijn met een virus.",
        True,
        "Cytotoxische T-lymfocyten herkennen besmette cellen en vernietigen ze. Dat is cellulaire afweer, naast de humorale afweer met antilichamen.",
    ),
    M(
        "Wat is de rol van de bloedplaatjes?",
        [
            "ze helpen bij de bloedstolling",
            "ze vervoeren zuurstof naar de weefsels",
            "ze maken antilichamen tegen bacteriën",
            "ze vervoeren CO₂ naar de longen",
        ],
        0,
        "Bij een wonde kleven bloedplaatjes tegen de beschadigde wand en aan elkaar. Ze maken stoffen vrij die de stollingscascade starten.",
    ),
    M(
        "Welke stap hoort aan het einde van de stollingscascade?",
        [
            "trombine zet fibrinogeen om in fibrinedraden die het stolsel vormen",
            "fibrine zet trombine om in protrombine, dat het wondje dan sluit",
            "bloedplaatjes zetten het albumine in het plasma om in hemoglobine voor het stolsel",
            "antilichamen kleven de rode bloedcellen in de wonde aan elkaar",
        ],
        0,
        "Protrombine wordt actief trombine, en trombine zet het opgeloste fibrinogeen om in draden fibrine. Daarin raken bloedcellen gevangen en zo ontstaat een stolsel.",
    ),
    I(
        "Hoe heet het opgeloste plasma-eiwit dat bij de stolling omgezet wordt in draden fibrine?",
        "fibrinogeen",
        "Fibrinogeen is opgelost in het plasma. Trombine zet het om in onoplosbare fibrinedraden die het stolsel stevig maken.",
    ),
    W(
        "De stolling kan op twee manieren starten: via de extrinsieke route vanuit beschadigd weefsel en via de intrinsieke route vanuit het bloed zelf.",
        True,
        "Beide routes komen samen bij de vorming van trombine. Daarna verlopen ze gelijk tot het fibrinestolsel.",
    ),
    M(
        "Iemand heeft bloedgroep A. Welke antigenen en antilichamen heeft die persoon?",
        [
            "A-antigenen op de rode bloedcellen en anti-B-antilichamen in het plasma",
            "B-antigenen op de rode bloedcellen en anti-A-antilichamen in het plasma",
            "A-antigenen op de rode bloedcellen en anti-A-antilichamen in het plasma",
            "geen antigenen op de rode bloedcellen en anti-A en anti-B in het plasma",
        ],
        0,
        "Wie bloedgroep A heeft, draagt A-antigenen en maakt anti-B. Had die persoon anti-A, dan zou het eigen bloed klonteren.",
    ),
    M(
        "Welke bloedgroep heeft geen A- en geen B-antigenen op de rode bloedcellen?",
        ["bloedgroep O", "bloedgroep AB", "bloedgroep A", "bloedgroep B"],
        0,
        "Bij bloedgroep O dragen de rode bloedcellen geen A- of B-antigeen. In het plasma zitten wel anti-A en anti-B.",
    ),
    M(
        "Wat gebeurt er als iemand met bloedgroep B bloed van groep A krijgt?",
        [
            "het anti-A van de ontvanger doet de rode bloedcellen van de donor klonteren",
            "er gebeurt niets, want A en B zijn compatibele bloedgroepen voor elkaar",
            "de ontvanger krijgt er extra bloedgroep A bij en heeft nadien bloedgroep AB",
            "de rode bloedcellen van de donor worden meteen omgezet in bloedplaatjes",
        ],
        0,
        "Het anti-A in het plasma van de ontvanger bindt aan de A-antigenen van het donorbloed. Er ontstaan antigeen-antilichaamcomplexen, de cellen klonteren en vallen uiteen.",
    ),
    I(
        "Hoe noemt men het samenklonteren van rode bloedcellen bij een verkeerde bloedtransfusie?",
        ["agglutinatie", "klontering"],
        "Bij agglutinatie kleven antilichamen de vreemde rode bloedcellen aan elkaar. Daarna kunnen die cellen openbarsten, wat hemolyse heet.",
    ),
    M(
        "Welke uitspraken over donors en ontvangers zijn juist? Kruis alles aan wat juist is.",
        [
            "O-negatief is de universele donor van rode bloedcellen",
            "AB-positief is de universele ontvanger",
            "iemand met bloedgroep O kan enkel bloed van groep O krijgen",
            "iemand met bloedgroep AB kan enkel bloed van groep AB krijgen",
        ],
        [0, 1, 2],
        "O-negatief heeft geen A-, B- of D-antigeen en past bij iedereen. AB-positief maakt geen anti-A, anti-B of anti-D en kan alles ontvangen.",
    ),
    W(
        "Iemand die resusnegatief is, heeft van nature al anti-D-antilichamen in het bloed, ook zonder ooit resuspositief bloed gekregen te hebben.",
        False,
        "Anti-D wordt pas gemaakt na contact met resuspositief bloed, bijvoorbeeld bij een transfusie of een zwangerschap. Anti-A en anti-B zijn er wel van nature.",
    ),
    M(
        "Een resusnegatieve moeder is zwanger van een resuspositief kind. Waarom is dat vooral bij een volgende zwangerschap een risico?",
        [
            "na de eerste bevalling kan ze anti-D maken tegen een volgend resuspositief kind",
            "het eerste kind maakt anti-D dat de moeder blijvend resuspositief maakt",
            "haar bloedgroep verandert na de eerste zwangerschap blijvend van A naar B",
            "de placenta laat bij een tweede zwangerschap geen zuurstof meer door naar het kind",
        ],
        0,
        "Bij de bevalling kan bloed van het kind in het bloed van de moeder komen. Ze maakt dan anti-D, dat bij een volgende zwangerschap door de placenta gaat en de rode bloedcellen van het kind kan afbreken.",
    ),
    M(
        "Welke stoffen behoren tot de immunoglobulines?",
        ["de antilichamen", "de stollingsfactoren", "de verteringsenzymen", "de bloedsuikers"],
        0,
        "Immunoglobulines of globulines zijn de antilichamen in het plasma. Ze binden specifiek aan een antigeen.",
    ),
    W(
        "Eosinofielen zijn de witte bloedcellen die de antilichamen maken.",
        False,
        "Antilichamen komen van B-lymfocyten. Eosinofielen spelen vooral een rol bij allergieën en bij de afweer tegen parasieten zoals wormen.",
    ),
]
