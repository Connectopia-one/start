# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Enzymen.

Biologie, blok "Stofwisselingsfysiologie en secretie", kop "Enzymen". Deel 1
gaat over wat een enzym is en hoe het werkt, deel 2 over de factoren die de
werking beïnvloeden en over enzymen in de processen van het lichaam.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "Wat is een enzym?",
        [
            "een eiwit dat een reactie versnelt zonder zelf verbruikt te worden",
            "een vet dat energie opslaat voor later gebruik in de cel",
            "een suiker die als bouwstof dient voor de celwand",
            "een hormoon dat via het bloed naar een doelorgaan reist",
        ],
        0,
        "Enzymen zijn biokatalysatoren: eiwitten die een reactie in het lichaam versnellen. Na de reactie zijn ze onveranderd en kunnen ze opnieuw werken.",
    ),
    I(
        "Een enzym versnelt een reactie in een levend organisme. Hoe noemt men een enzym daarom met één woord?",
        ["biokatalysator", "katalysator"],
        "Een katalysator versnelt een reactie zonder zelf op te gebruiken. Omdat enzymen dat in levende wezens doen, heten ze biokatalysatoren.",
    ),
    M(
        "In het sleutel-slotprincipe staat het slot voor een deel van het enzym. Welk deel?",
        ["het actief centrum", "het substraat", "het reactieproduct", "de cofactor die losjes meedraait"],
        0,
        "Het actief centrum is de plek in het enzym waar het substraat precies in past, zoals een sleutel in een slot.",
    ),
    M(
        "Welke stof is in het sleutel-slotprincipe de sleutel?",
        ["het substraat", "het enzym", "het actief centrum", "de inhibitor"],
        0,
        "Het substraat is de stof die het enzym omzet. Het past in het actief centrum, net als een sleutel in een slot.",
    ),
    I(
        "Hoe heet het tijdelijke geheel dat ontstaat wanneer het substraat in het actief centrum gebonden is?",
        ["enzym-substraatcomplex", "enzymsubstraatcomplex", "ES-complex"],
        "Even zitten enzym en substraat aan elkaar vast als enzym-substraatcomplex. Daarna komen de producten vrij en is het enzym weer klaar voor een volgend substraat.",
    ),
    M(
        "Hoe versnelt een enzym een reactie?",
        [
            "het verlaagt de activeringsenergie die nodig is om de reactie te starten",
            "het levert zelf extra energie aan de reactie door op te branden",
            "het verhoogt de temperatuur rond het substraat met enkele graden",
            "het verandert het eindproduct zodat er meer van ontstaat",
        ],
        0,
        "Een enzym maakt de drempel lager: er is minder activeringsenergie nodig. De reactie verloopt daardoor veel sneller bij lichaamstemperatuur.",
    ),
    W(
        "Een enzym wordt tijdens de reactie die het versnelt opgebruikt, zodat de cel na elke reactie een nieuw enzym moet maken.",
        False,
        "Een enzym blijft na de reactie onveranderd en kan telkens opnieuw een substraat omzetten. Daarom volstaan kleine hoeveelheden.",
    ),
    M(
        "Wat bedoelt men met de substraatspecificiteit van een enzym?",
        [
            "een enzym zet maar één bepaald substraat of één soort substraat om",
            "een enzym werkt alleen bij één bepaalde temperatuur en verder nergens",
            "een enzym komt maar in één bepaald orgaan van het lichaam voor",
            "een enzym maakt telkens één product, welk substraat er ook binnenkomt",
        ],
        0,
        "Door de vorm van het actief centrum past enkel een bepaald substraat. Amylase breekt zetmeel af, maar geen eiwitten.",
    ),
    M(
        "De naam van veel enzymen eindigt op een vaste uitgang. Welke voorbeelden zijn juist gevormd naar het substraat dat ze afbreken? Kruis alles aan wat juist is.",
        [
            "lactase breekt lactose af",
            "lipase breekt lipiden af",
            "trypsine breekt triglyceriden af",
            "pepsine breekt zetmeel af",
        ],
        [0, 1],
        "Veel enzymnamen bestaan uit de naam van het substraat met de uitgang -ase. Trypsine en pepsine zijn oudere namen en breken allebei eiwitten af, geen vetten of zetmeel.",
    ),
    I(
        "Welke uitgang krijgt de naam van de meeste enzymen, zoals bij amylase en lactase?",
        ["-ase", "ase"],
        "De uitgang -ase wijst op een enzym. Vaak staat het substraat ervoor: sacharase breekt sacharose af, lactase lactose.",
    ),
    W(
        "Enzymen zijn eiwitten, en hun werking hangt af van hun ruimtelijke vorm.",
        True,
        "De vorm van het eiwit bepaalt het actief centrum. Verandert die vorm, dan past het substraat niet meer en werkt het enzym niet.",
    ),
    M(
        "Wat gebeurt er bij de denaturatie van een enzym?",
        [
            "de ruimtelijke vorm gaat verloren, waardoor het actief centrum niet meer past",
            "het enzym splitst zich in twee kleinere enzymen die elk half zo snel werken",
            "het enzym bindt zich blijvend aan zijn product en wordt zo inactief opgeslagen",
            "het enzym verandert van substraat en zet voortaan een andere stof om",
        ],
        0,
        "Bij denaturatie verliest het eiwit zijn vorm, bijvoorbeeld door hoge temperatuur of een sterk afwijkende pH. Het actief centrum vervormt mee en het enzym werkt niet meer.",
    ),
    W(
        "Een enzym dat door hoge temperatuur gedenatureerd is, gaat gewoon weer werken zodra het afkoelt.",
        False,
        "Denaturatie door hitte is meestal blijvend. Een gekookt ei wordt ook niet meer vloeibaar als het afkoelt.",
    ),
    M(
        "Wat is een cofactor?",
        [
            "een niet-eiwitdeel, zoals een metaalion, dat een enzym nodig heeft om te werken",
            "een tweede substraat dat het enzym tegelijk met het eerste afbreekt",
            "een stof die het actief centrum blijvend blokkeert en het enzym stillegt",
            "een enzym dat de aanmaak van andere enzymen in de cel regelt",
        ],
        0,
        "Sommige enzymen werken pas met een helper die geen eiwit is. Een anorganische helper zoals een zink- of magnesiumion noemt men een cofactor.",
    ),
    M(
        "Wat is het verschil tussen een co-enzym en een cofactor zoals een metaalion?",
        [
            "een co-enzym is een organische molecule, vaak afgeleid van een vitamine",
            "een co-enzym is zelf een enzym dat de reactie van het eerste overneemt",
            "een co-enzym werkt enkel buiten de cel, een cofactor enkel erbinnen",
            "een co-enzym remt het enzym, een cofactor helpt het enzym",
        ],
        0,
        "Co-enzymen zijn organische helpers, vaak gemaakt uit vitaminen van de B-groep. Metaalionen zijn anorganische cofactoren.",
    ),
    W(
        "De activeringsenergie is de energie die nodig is om een reactie op gang te brengen.",
        True,
        "Ook een reactie die netto energie oplevert, heeft een duwtje nodig om te starten. Dat duwtje is de activeringsenergie, en een enzym maakt het kleiner.",
    ),
    M(
        "Welke uitspraken over het actief centrum zijn juist? Kruis alles aan wat juist is.",
        [
            "het is een klein deel van het enzym waar het substraat bindt",
            "de vorm ervan bepaalt welk substraat het enzym omzet",
            "het wordt na elke reactie afgebroken en opnieuw opgebouwd",
            "het verandert van vorm als het enzym denatureert",
        ],
        [0, 1, 3],
        "Het actief centrum is een kleine holte of groeve in het enzym. Het blijft na de reactie bestaan, maar vervormt wel bij denaturatie.",
    ),
    M(
        "Waarom noemt men enzymen biokatalysatoren en geen gewone reactiestoffen?",
        [
            "ze komen na de reactie onveranderd terug",
            "ze worden in het reactieproduct ingebouwd",
            "ze leveren de bouwstenen voor het product",
            "ze zetten zichzelf om tot een nieuw enzym",
        ],
        0,
        "Een katalysator neemt deel aan de reactie maar komt er onveranderd uit. Enzymen doen dat in levende wezens.",
    ),
    M(
        "Een enzym zet stof A om, maar niet stof B die er sterk op lijkt. Wat is de beste verklaring?",
        [
            "stof B past niet in het actief centrum",
            "stof B heeft meer activeringsenergie nodig dan het enzym kan leveren",
            "stof B is groter dan het hele enzym en kan niet in de cel",
            "stof B wordt pas omgezet als de temperatuur boven 60 °C komt",
        ],
        0,
        "Dat heet substraatspecificiteit. Een klein verschil in vorm volstaat om niet meer in het actief centrum te passen.",
    ),
    W(
        "Eén enzymmolecule kan in korte tijd vele duizenden substraatmoleculen omzetten.",
        True,
        "Omdat het enzym niet opgebruikt wordt, kan het snel na elkaar telkens een nieuw substraat binden. Sommige enzymen halen miljoenen omzettingen per seconde.",
    ),
]

DEEL2 = [
    M(
        "Bij lage temperatuur werkt een enzym traag. Waarom?",
        [
            "de moleculen bewegen trager, zodat enzym en substraat elkaar minder vaak raken",
            "het enzym is bij lage temperatuur gedenatureerd en blijvend beschadigd",
            "het substraat bevriest en kan daardoor niet in het actief centrum",
            "het actief centrum wordt bij kou groter en houdt het substraat niet vast",
        ],
        0,
        "Bij lagere temperatuur botsen de moleculen minder vaak. Het enzym is niet kapot: warm het op en het werkt weer sneller.",
    ),
    M(
        "Wat is het temperatuursoptimum van een enzym?",
        [
            "de temperatuur waarbij het enzym het snelst werkt",
            "de laagste temperatuur waarbij het enzym nog net werkt",
            "de temperatuur waarbij het enzym denatureert",
            "de gemiddelde temperatuur in de cel",
        ],
        0,
        "Bij het optimum is de reactiesnelheid het grootst. Bij de meeste menselijke enzymen ligt het rond 37 °C.",
    ),
    M(
        "Een grafiek toont de reactiesnelheid van een menselijk enzym tegen de temperatuur. Hoe ziet die curve er doorgaans uit?",
        [
            "ze stijgt geleidelijk tot rond 37 °C en valt daarna snel terug",
            "ze stijgt gelijkmatig en blijft stijgen bij elke hogere temperatuur",
            "ze daalt gelijkmatig vanaf 0 °C tot ze bij 100 °C nul wordt",
            "ze blijft vlak, want temperatuur heeft geen invloed op enzymen",
        ],
        0,
        "Eerst versnelt de warmte de botsingen. Voorbij het optimum begint het enzym te denatureren, en dan zakt de snelheid steil.",
    ),
    W(
        "Pepsine, het eiwitsplitsende enzym in de maag, werkt het best in een zuur midden met een pH rond 2.",
        True,
        "In de maag is het erg zuur door het maagzuur. Pepsine is daaraan aangepast en heeft zijn pH-optimum rond 2.",
    ),
    M(
        "Welk enzym heeft zijn pH-optimum in een licht basisch midden, zoals in de twaalfvingerige darm?",
        ["trypsine", "pepsine", "speekselamylase bij pH 2", "geen enkel enzym werkt basisch"],
        0,
        "Trypsine uit het alvleeskliersap werkt in de dunne darm, waar natriumwaterstofcarbonaat het zure maagsap neutraliseert. Zijn optimum ligt rond pH 8.",
    ),
    M(
        "Wat gebeurt er met de reactiesnelheid als je de substraatconcentratie blijft verhogen, terwijl de hoeveelheid enzym gelijk blijft?",
        [
            "ze stijgt eerst en bereikt dan een maximum, omdat alle enzymen bezet zijn",
            "ze blijft altijd evenredig stijgen met de hoeveelheid substraat",
            "ze daalt, omdat te veel substraat het enzym denatureert",
            "ze verandert niet, want de snelheid hangt enkel van de temperatuur af",
        ],
        0,
        "Bij veel substraat zijn alle actieve centra voortdurend bezet. Dat heet verzadiging, en de snelheid blijft dan op haar maximum.",
    ),
    I(
        "Hoe noemt men de toestand waarin alle actieve centra van de enzymen bezet zijn, zodat meer substraat de reactie niet meer versnelt?",
        ["verzadiging", "verzadigingstoestand"],
        "Bij verzadiging werken alle enzymen op volle kracht. De reactie heeft haar maximale snelheid bereikt.",
    ),
    M(
        "Wat gebeurt er met de reactiesnelheid als je meer enzym toevoegt en er substraat genoeg is?",
        [
            "ze stijgt, want er zijn meer actieve centra beschikbaar",
            "ze daalt, want de enzymen hinderen elkaar",
            "ze blijft gelijk, want het substraat is de enige factor",
            "ze wordt nul, want het enzym verbruikt al het substraat in één keer",
        ],
        0,
        "Zolang er voldoende substraat is, zet elk extra enzym extra substraat om. De maximale reactiesnelheid ligt dan hoger.",
    ),
    M(
        "Wat doet een inhibitor?",
        [
            "hij remt de werking van een enzym",
            "hij versnelt de werking van een enzym",
            "hij vormt het product van de reactie",
            "hij levert de energie voor de reactie",
        ],
        0,
        "Een inhibitor is een remmer. Sommige inhibitoren bezetten het actief centrum, andere veranderen de vorm van het enzym elders.",
    ),
    W(
        "Een inhibitor die op het substraat lijkt, kan in het actief centrum gaan zitten en zo het echte substraat de plaats afnemen.",
        True,
        "Zo'n inhibitor concurreert met het substraat om het actief centrum. Veel geneesmiddelen werken op die manier.",
    ),
    M(
        "Welke factoren beïnvloeden de werking van een enzym? Kruis alles aan wat juist is.",
        ["de temperatuur", "de zuurtegraad of pH", "de substraatconcentratie", "de enzymconcentratie"],
        [0, 1, 2, 3],
        "Alle vier spelen mee: temperatuur, pH, enzymconcentratie en substraatconcentratie bepalen samen hoe snel een enzym werkt.",
    ),
    W(
        "Elk enzym in het menselijk lichaam heeft hetzelfde pH-optimum, namelijk 7.",
        False,
        "Het pH-optimum hangt af van waar het enzym werkt. Pepsine werkt het best rond pH 2, trypsine rond pH 8 en speekselamylase rond pH 7.",
    ),
    M(
        "Speekselamylase komt met het voedsel in de maag terecht. Wat gebeurt er daar met zijn werking?",
        [
            "het stopt grotendeels, want de maag is veel te zuur",
            "het werkt veel sneller, want de maag is warmer",
            "het verandert in pepsine en breekt eiwitten af",
            "het werkt verder zoals in de mond, want pH maakt niet uit",
        ],
        0,
        "Speekselamylase werkt het best rond pH 7. In het zure maagsap valt de werking grotendeels stil.",
    ),
    M(
        "Welk enzym speelt een rol bij de DNA-replicatie?",
        ["DNA-polymerase", "lactase", "pepsine", "lipase"],
        0,
        "DNA-polymerase bouwt een nieuwe streng op tegen de oude streng. Ook helicase, dat de dubbele helix opent, is een enzym bij de replicatie.",
    ),
    M(
        "Bij welke processen in het lichaam of in de plant zijn enzymen onmisbaar? Kruis alles aan wat juist is.",
        ["de spijsvertering", "de celademhaling", "de fotosynthese", "de DNA-replicatie"],
        [0, 1, 2, 3],
        "Vertering, celademhaling, fotosynthese en DNA-replicatie verlopen allemaal stap voor stap via enzymen.",
    ),
    I(
        "Hoe noemt men de hoogste reactiesnelheid die een enzym kan halen, wanneer alle actieve centra bezet zijn?",
        ["maximale reactiesnelheid", "maximumsnelheid", "Vmax"],
        "De maximale reactiesnelheid wordt bereikt bij verzadiging. Meer substraat helpt dan niet meer; meer enzym wel.",
    ),
    W(
        "Bij koorts van 41 °C kunnen sommige enzymen in het lichaam al minder goed beginnen te werken.",
        True,
        "Ver boven 37 °C begint de vorm van gevoelige eiwitten te veranderen. Daarom is zeer hoge koorts gevaarlijk.",
    ),
    M(
        "In een proef zet men amylase met zetmeel bij 0 °C, 37 °C en 90 °C. Bij welke temperatuur wordt het zetmeel het snelst afgebroken?",
        ["bij 37 °C", "bij 0 °C", "bij 90 °C", "bij alle drie even snel"],
        0,
        "37 °C ligt bij het optimum van menselijke amylase. Bij 0 °C werkt het enzym erg traag, en bij 90 °C is het gedenatureerd.",
    ),
    M(
        "Na de proef zet men de buis van 0 °C en de buis van 90 °C allebei op 37 °C. Wat verwacht je?",
        [
            "in de buis die eerst koud was, gaat het enzym alsnog werken",
            "in de buis die eerst heet was, gaat het enzym alsnog werken",
            "in beide buizen gaat het enzym opnieuw normaal werken",
            "in geen van beide buizen werkt het enzym nog",
        ],
        0,
        "Kou vertraagt het enzym maar beschadigt het niet. Hitte denatureert het blijvend, dus die buis blijft stil.",
    ),
    W(
        "Een enzym verandert de evenwichtsligging van een reactie, zodat er uiteindelijk meer product ontstaat.",
        False,
        "Een enzym versnelt enkel hoe snel het evenwicht bereikt wordt. Waar dat evenwicht ligt, verandert het niet.",
    ),
]
