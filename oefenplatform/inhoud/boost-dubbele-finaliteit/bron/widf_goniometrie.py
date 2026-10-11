# -*- coding: utf-8 -*-
"""De vragen voor "De rechthoekige driehoek oplossen en toepassen".

Nieuw geschreven voor dubbele finaliteit. Het overgenomen thema "Pythagoras en
de rechthoekige driehoek" voert in zijn tweede deel de sinus, de cosinus en de
tangens in. Dit thema bouwt daarop verder: hier reken je er echt mee. Je zoekt
zijden, je zoekt hoeken, je lost de volledige driehoek op, en je past dat toe
op de situaties die de DF-fiche noemt: de hoogte van een boom of een gebouw uit
de kijkhoek en de afstand, en het hoogteverschil uit de hellingshoek en de
lengte van een pad. De definities zelf worden hier niet opnieuw gegeven; die
staan in het vorige thema.

De notatie staat tussen \\( en \\) (zie inhoud/notatie.py). Graden schrijven
we als \\(60^{\\circ}\\), en de verhoudingen als \\(\\sin\\),
\\(\\cos\\) en \\(\\tan\\).

Deel 1 gaat over zijden berekenen, deel 2 over hoeken en over de toepassingen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je kijkt in een rechthoekige driehoek naar hoek A. Welke zijde is de overstaande zijde van A?",
        opties=[
            "de zijde die tegenover A ligt",
            "de zijde die tegenover de rechte hoek ligt",
            "de langste zijde van de driehoek",
            "de zijde waarop de driehoek rust",
        ],
        antwoord=0,
        uitleg="Overstaande en aanliggende hangen af van de hoek waar je naar kijkt. Verander je van hoek, dan wisselen ze van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijde is de aanliggende zijde van hoek A?",
        opties=[
            "de rechthoekszijde die tegen A aan ligt",
            "de schuine zijde, want die ligt ook tegen A aan",
            "de zijde tegenover A",
            "altijd de kortste zijde van de driehoek",
        ],
        antwoord=0,
        uitleg="Twee zijden raken hoek A: de schuine zijde en een rechthoekszijde. Met aanliggende bedoelen we die rechthoekszijde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een rechthoekige driehoek met zijden \(3\), \(4\) en \(5\): hoeveel is de sinus van de hoek tegenover de zijde \(3\)?",
        opties=[r"\(0{,}6\)", r"\(0{,}8\)", r"\(0{,}75\)", r"\(1{,}25\)"],
        antwoord=0,
        uitleg=r"De overstaande zijde is \(3\) en de schuine is \(5\), dus \(\frac{3}{5} = 0{,}6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In diezelfde driehoek met zijden \(3\), \(4\) en \(5\): hoeveel is de cosinus van de hoek tegenover de zijde \(3\)?",
        opties=[r"\(0{,}8\)", r"\(0{,}6\)", r"\(0{,}75\)", r"\(1{,}33\)"],
        antwoord=0,
        uitleg=r"De aanliggende zijde is \(4\) en de schuine is \(5\), dus \(\frac{4}{5} = 0{,}8\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In diezelfde driehoek met zijden \(3\), \(4\) en \(5\): hoeveel is de tangens van de hoek tegenover de zijde \(3\)?",
        opties=[r"\(0{,}75\)", r"\(0{,}6\)", r"\(0{,}8\)", r"\(1{,}25\)"],
        antwoord=0,
        uitleg=r"Overstaande gedeeld door aanliggende is \(\frac{3}{4} = 0{,}75\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de schuine zijde, en je zoekt de overstaande zijde. Wat reken je?",
        opties=[
            "de sinus van de hoek maal de schuine zijde",
            "de cosinus van de hoek maal de schuine zijde",
            "de schuine zijde gedeeld door de sinus",
            "de tangens van de hoek maal de schuine zijde",
        ],
        antwoord=0,
        uitleg="Sinus is overstaande op schuine, dus de overstaande is sinus maal schuine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de aanliggende zijde, en je zoekt de overstaande zijde. Wat reken je?",
        opties=[
            "de tangens van de hoek maal de aanliggende zijde",
            "de sinus van de hoek maal de aanliggende zijde",
            "de aanliggende zijde gedeeld door de cosinus",
            "de cosinus van de hoek maal de aanliggende zijde",
        ],
        antwoord=0,
        uitleg="Tangens is overstaande op aanliggende, dus de overstaande is tangens maal aanliggende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de aanliggende zijde, en je zoekt de schuine zijde. Wat reken je?",
        opties=[
            "de aanliggende zijde gedeeld door de cosinus",
            "de aanliggende zijde maal de cosinus",
            "de aanliggende zijde gedeeld door de sinus",
            "de aanliggende zijde maal de tangens",
        ],
        antwoord=0,
        uitleg="Cosinus is aanliggende op schuine, dus de schuine is aanliggende gedeeld door de cosinus.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een ladder van \(6\) meter staat onder een hoek van \(60^{\circ}\) met de grond. Hoe hoog reikt hij ongeveer tegen de muur?",
        opties=[r"\(5{,}20\) meter", r"\(3{,}00\) meter", r"\(6{,}93\) meter", r"\(10{,}39\) meter"],
        antwoord=0,
        uitleg=r"De hoogte is de overstaande zijde: \(6 \cdot \sin 60^{\circ} \approx 5{,}20\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde ladder van \(6\) meter onder \(60^{\circ}\): hoe ver staat zijn voet van de muur?",
        opties=[r"\(3\) meter", r"\(5{,}20\) meter", r"\(6{,}93\) meter", r"\(12\) meter"],
        antwoord=0,
        uitleg=r"De afstand is de aanliggende zijde: \(6 \cdot \cos 60^{\circ} = 6 \cdot 0{,}5 = 3\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De sinus van een hoek is \(0{,}5\) en de schuine zijde is \(10\). Hoe lang is de overstaande zijde?",
        opties=[r"\(5\)", r"\(20\)", r"\(0{,}05\)", r"\(10{,}5\)"],
        antwoord=0,
        uitleg=r"Sinus maal schuine zijde geeft de overstaande: \(0{,}5 \cdot 10 = 5\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangen deze verhoudingen enkel van de hoek af en niet van de grootte van de driehoek?",
        opties=[
            "omdat driehoeken met dezelfde hoeken gelijkvormig zijn",
            "omdat elke rechthoekige driehoek even groot is",
            "omdat je de schuine zijde altijd op 1 zet",
            "omdat je de zijden toch afrondt op gehele getallen",
        ],
        antwoord=0,
        uitleg="Bij gelijkvormige driehoeken worden alle zijden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De tangens van een scherpe hoek kan groter zijn dan \(1\).",
        antwoord=True,
        uitleg=r"Zodra de overstaande zijde langer is dan de aanliggende, is de breuk groter dan \(1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin 45^{\circ}\) en \(\cos 45^{\circ}\) zijn aan elkaar gelijk.",
        antwoord=True,
        uitleg=r"Bij \(45^{\circ}\) zijn de twee rechthoekszijden even lang, dus overstaande en aanliggende zijn gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goniometrisch getal van een scherpe hoek kan negatief zijn.",
        antwoord=False,
        uitleg="Zijden hebben een positieve lengte, dus een verhouding van twee zijden blijft positief.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een rechthoekige driehoek zijn de twee scherpe hoeken samen \(180^{\circ}\).",
        antwoord=False,
        uitleg=r"Ze zijn samen \(90^{\circ}\). De rechte hoek neemt al \(90\) van de \(180^{\circ}\) in.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een driehoek heeft een rechte hoek en een scherpe hoek van \(30^{\circ}\). Hoe groot is de derde hoek?",
        opties=[r"\(60^{\circ}\)", r"\(30^{\circ}\)", r"\(90^{\circ}\)", r"\(120^{\circ}\)"],
        antwoord=0,
        uitleg=r"Alle hoeken samen zijn \(180^{\circ}\), en \(180 - 90 - 30 = 60\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je voor je begint na of je rekentoestel op graden staat?",
        opties=[
            "omdat je anders een fout antwoord krijgt bij een juiste berekening",
            "omdat het toestel anders een foutmelding geeft",
            "omdat graden nauwkeuriger rekenen dan andere instellingen",
            "omdat een rechthoekige driehoek enkel in graden bestaat",
        ],
        antwoord=0,
        uitleg="Staat je toestel anders ingesteld, dan klopt er niets van je uitkomst terwijl je redenering wel juist was.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verhouding gebruik je als je de overstaande en de aanliggende zijde kent en de hoek zoekt?",
        antwoord=["de tangens", "tangens", "tan"],
        uitleg="Overstaande op aanliggende is de tangens. Met de inverse vind je de hoek terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de zijde die tegenover de rechte hoek ligt?",
        antwoord=["de schuine zijde", "schuine zijde", "de hypotenusa"],
        uitleg="De schuine zijde is altijd de langste zijde van een rechthoekige driehoek.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'de rechthoekige driehoek oplossen'?",
        opties=[
            "alle zijden en alle hoeken ervan berekenen",
            "enkel de oppervlakte ervan berekenen",
            "de driehoek in twee gelijke stukken verdelen",
            "de omtrek en de oppervlakte ervan berekenen",
        ],
        antwoord=0,
        uitleg="Met één zijde en één scherpe hoek, of met twee zijden, liggen alle andere zijden en hoeken vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent de overstaande zijde en de schuine zijde, en je zoekt de hoek. Wat doe je?",
        opties=[
            "je deelt ze door elkaar en neemt de inverse sinus",
            "je deelt ze door elkaar en neemt de inverse tangens",
            "je deelt ze door elkaar en neemt de inverse cosinus",
            "je telt ze op en deelt door 90",
        ],
        antwoord=0,
        uitleg="Overstaande op schuine is de sinus. De inverse sinus op je rekentoestel geeft de hoek terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent allebei de rechthoekszijden en je zoekt een scherpe hoek. Wat doe je?",
        opties=[
            "je deelt ze door elkaar en neemt de inverse tangens",
            "je deelt ze door elkaar en neemt de inverse sinus",
            "je telt ze op en neemt de inverse cosinus",
            "je gebruikt eerst Pythagoras en dan de inverse sinus",
        ],
        antwoord=0,
        uitleg="De twee rechthoekszijden zijn de overstaande en de aanliggende, en dat is precies de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De cosinus van een scherpe hoek is \(0{,}96\). Hoeveel is de sinus?",
        opties=[r"\(0{,}28\)", r"\(0{,}04\)", r"\(0{,}48\)", r"\(1{,}04\)"],
        antwoord=0,
        uitleg=r"Met de grondformule \(\sin^{2}\alpha + \cos^{2}\alpha = 1\): \(1 - 0{,}9216 = 0{,}0784\), en \(\sqrt{0{,}0784} = 0{,}28\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een weg heeft een hellingspercentage van \(8\,\%\). Wat betekent dat?",
        opties=[
            r"je stijgt \(8\) meter over \(100\) meter horizontaal",
            r"je stijgt \(8\) meter over \(100\) meter weglengte",
            r"de hellingshoek is \(8^{\circ}\)",
            r"je stijgt \(8\) centimeter per meter weglengte",
        ],
        antwoord=0,
        uitleg="Een hellingspercentage is de tangens van de hellingshoek, uitgedrukt in procent.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bergpad van \(500\) meter loopt onder een hellingshoek van \(12^{\circ}\). Hoeveel hoogte win je ongeveer?",
        opties=[r"\(104\) meter", r"\(489\) meter", r"\(106\) meter", r"\(60\) meter"],
        antwoord=0,
        uitleg=r"De padlengte is de schuine zijde: \(500 \cdot \sin 12^{\circ} \approx 104\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vlieger hangt aan \(40\) meter touw dat onder \(55^{\circ}\) met de grond staat. Hoe hoog hangt hij ongeveer?",
        opties=[r"\(32{,}8\) meter", r"\(22{,}9\) meter", r"\(57{,}1\) meter", r"\(48{,}8\) meter"],
        antwoord=0,
        uitleg=r"Het touw is de schuine zijde: \(40 \cdot \sin 55^{\circ} \approx 32{,}8\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een mast werpt een schaduw van \(12\) meter terwijl de zon \(40^{\circ}\) boven de horizon staat. Hoe hoog is de mast ongeveer?",
        opties=[r"\(10{,}1\) meter", r"\(7{,}7\) meter", r"\(14{,}3\) meter", r"\(15{,}7\) meter"],
        antwoord=0,
        uitleg=r"De schaduw is de aanliggende zijde: \(12 \cdot \tan 40^{\circ} \approx 10{,}1\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je staat \(20\) meter van een gebouw en kijkt naar de top onder \(35^{\circ}\). Je ogen zitten \(1{,}6\) meter hoog. Hoe hoog is het gebouw ongeveer?",
        opties=[r"\(15{,}6\) meter", r"\(14{,}0\) meter", r"\(12{,}4\) meter", r"\(17{,}2\) meter"],
        antwoord=0,
        uitleg=r"\(20 \cdot \tan 35^{\circ} \approx 14{,}0\) meter, en daar komt je ooghoogte van \(1{,}6\) meter nog bij.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een oprit mag hoogstens \(5\,\%\) hellen en moet \(30\) centimeter overbruggen. Hoe lang moet hij minstens zijn?",
        opties=[r"\(6\) meter", r"\(1{,}5\) meter", r"\(60\) meter", r"\(15\) meter"],
        antwoord=0,
        uitleg=r"Vijf procent wil zeggen \(5\) centimeter stijging per meter. Voor \(30\) centimeter heb je dus \(6\) meter nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een helling van \(25\,\%\) komt ongeveer overeen met welke hellingshoek?",
        opties=[r"\(14^{\circ}\)", r"\(25^{\circ}\)", r"\(4^{\circ}\)", r"\(45^{\circ}\)"],
        antwoord=0,
        uitleg=r"Het hellingspercentage is de tangens: \(\tan^{-1} 0{,}25 \approx 14^{\circ}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een helling van \(100\,\%\) komt overeen met een hoek van \(45^{\circ}\).",
        antwoord=True,
        uitleg=r"Bij \(100\,\%\) stijg je even veel als je vooruit gaat, en \(\tan 45^{\circ} = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe steiler de helling, hoe groter de sinus van de hellingshoek.",
        antwoord=True,
        uitleg="Bij dezelfde padlengte win je meer hoogte naarmate de hoek groter wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Met één gegeven zijde alleen kan je een rechthoekige driehoek volledig oplossen.",
        antwoord=False,
        uitleg="Je hebt er een tweede gegeven bij nodig: nog een zijde, of een van de scherpe hoeken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het hellingspercentage van een weg is hetzelfde getal als de hellingshoek in graden.",
        antwoord=False,
        uitleg=r"\(8\,\%\) is niet \(8^{\circ}\), maar ongeveer \(4{,}6^{\circ}\). Het percentage is de tangens van de hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je berekent een scherpe hoek in een rechthoekige driehoek en krijgt \(91^{\circ}\). Wat weet je?",
        opties=[
            "er zit een fout in je berekening",
            "de driehoek is stomphoekig",
            r"je moet het antwoord afronden naar \(90^{\circ}\)",
            "de schuine zijde was te kort gegeven",
        ],
        antwoord=0,
        uitleg=r"De rechte hoek neemt al \(90^{\circ}\) in, dus een scherpe hoek in diezelfde driehoek blijft altijd daaronder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je eerst een schets voor je begint te rekenen?",
        opties=[
            "omdat je dan ziet welke zijde overstaand en welke aanliggend is",
            "omdat een schets op het examen verplicht is",
            "omdat je anders geen rekentoestel mag gebruiken",
            "omdat de tekening het antwoord al geeft",
        ],
        antwoord=0,
        uitleg="De meeste fouten komen van de verkeerde verhouding kiezen. Op een schets met de gegevens erbij zie je meteen welke je nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je berekent een hoogte en je rekentoestel toont \(5{,}1962\). Waarom rond je pas op het einde af?",
        opties=[
            "omdat afronden onderweg je eindantwoord verder doet afwijken",
            "omdat het rekentoestel anders een fout geeft",
            "omdat een hoogte altijd op vier cijfers moet staan",
            "omdat je anders de eenheid vergeet te noteren",
        ],
        antwoord=0,
        uitleg="Elke afronding onderweg stapelt zich op. Reken met de volledige tussenresultaten en rond het eindantwoord af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de hoek waaronder je vanaf de grond omhoog kijkt naar de top van een boom?",
        antwoord=["de kijkhoek", "kijkhoek"],
        uitleg="Samen met je afstand tot de boom geeft de kijkhoek je de hoogte, via de tangens.",
    ),
    dict(
        type="invultekst",
        vraag="Welk goniometrisch getal is het hellingspercentage van een weg?",
        antwoord=["de tangens", "tangens", "tan"],
        uitleg=r"\(8\,\%\) betekent dat de tangens van de hellingshoek \(0{,}08\) is.",
    ),
]
