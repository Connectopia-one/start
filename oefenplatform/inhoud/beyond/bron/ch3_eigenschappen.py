# -*- coding: utf-8 -*-
"""Ruimtelijke structuur, polariteit en intermoleculaire krachten — chemie.

🌍 Beyond. Deel 1 gaat over de vorm van een molecule: het sterisch getal, de
ruimtelijke structuur die eruit volgt, het hybridisatietype, en het verschil
tussen de theoretische en de werkelijke bindingshoek. Deel 2 gaat over wat die
vorm betekent: de polariteit van een binding en van de hele verbinding, de
intermoleculaire krachten van zwak naar sterk, het oplosgedrag, het verschil in
kook- en smeltpunt, en de vier soorten roosters.

De vragen geven de bouw in woorden of beknopt mee, want een molecule tekenen
kan op het scherm niet. Waar een elektronegatieve waarde nodig is, staat ze in
de vraag; het kind krijgt die tabel immers op het examen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bepaal je het sterisch getal van een atoom?",
        opties=[
            "het aantal bindingspartners plus het aantal vrije elektronenparen",
            "het aantal bindingen plus het aantal valentie-elektronen",
            "het aantal vrije elektronenparen maal twee erbij geteld",
            "het aantal atomen in de hele molecule, de waterstof erbij",
        ],
        antwoord=0,
        uitleg="Bij water: twee bindingspartners en twee vrije paren, dus sterisch getal "
        "vier. Een dubbele binding telt als één partner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ruimtelijke structuur hoort bij sterisch getal 4 zonder vrije elektronenparen?",
        opties=[
            "een tetraëder",
            "een vlakke driehoek",
            "een rechte lijn",
            "een piramide",
        ],
        antwoord=0,
        uitleg="Vier bindingspartners gaan zo ver mogelijk uit elkaar staan, en dat is in "
        "drie dimensies een tetraëder. Methaan is daarvan het voorbeeld.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hybridisatietype hoort bij sterisch getal 4?",
        antwoord=["sp3", "sp³", "sp3-hybridisatie"],
        uitleg="Eén s-orbitaal en drie p-orbitalen mengen tot vier gelijke orbitalen. Bij "
        "sterisch getal 3 is het sp² en bij 2 is het sp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de theoretische bindingshoek bij een tetraëder?",
        opties=[
            "109,5°",
            "120°",
            "90°",
            "180°",
        ],
        antwoord=0,
        uitleg="Bij een vlakke driehoek is het 120° en bij een lineaire vorm 180°. De "
        "werkelijke hoek wijkt af als er vrije paren zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vrij elektronenpaar duwt harder op de bindingen dan een bindend paar.",
        antwoord=True,
        uitleg="Een vrij paar hangt dichter bij het centrale atoom en neemt meer plaats. "
        "Daardoor is de hoek in water maar 104,5° in plaats van 109,5°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de bindingshoek in ammoniak kleiner dan in methaan?",
        opties=[
            "ammoniak heeft een vrij elektronenpaar dat de bindingen samenduwt",
            "ammoniak heeft een kleiner centraal atoom dan methaan",
            "ammoniak heeft minder waterstofatomen om plaats te maken",
            "ammoniak heeft een dubbele binding naar het stikstofatoom",
        ],
        antwoord=0,
        uitleg="Beide hebben sterisch getal vier, maar bij ammoniak is één hoek van de "
        "tetraëder bezet door een vrij paar: 107° in plaats van 109,5°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ruimtelijke structuur heeft een watermolecule?",
        opties=[
            "geknikt",
            "lineair",
            "tetraëdrisch",
            "trigonaal-planair",
        ],
        antwoord=0,
        uitleg="Twee bindingen en twee vrije paren: de bindingen liggen in een hoek, dus "
        "is de molecule geknikt. Die vorm maakt water polair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over koolstofdioxide zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het sterisch getal van koolstof is twee",
            "de molecule is lineair",
            "de molecule is geknikt",
            "het koolstofatoom heeft een vrij elektronenpaar",
        ],
        antwoord=[0, 1],
        uitleg="Twee dubbele bindingen tellen als twee partners, en er zijn geen vrije "
        "paren op koolstof. Dus 180° en sp-hybridisatie.",
    ),
    dict(
        type="invultekst",
        vraag="Welke ruimtelijke structuur hoort bij sterisch getal 2?",
        antwoord=["lineair", "lineaire", "een lijn"],
        uitleg="Twee partners gaan recht tegenover elkaar staan: 180°. Dat is de vorm van "
        "CO₂ en van ethyn rond de koolstofatomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hybridisatietype heeft een koolstofatoom met een dubbele binding?",
        opties=[
            "sp²",
            "sp³",
            "sp",
            "sp⁴",
        ],
        antwoord=0,
        uitleg="Drie bindingspartners geeft sterisch getal drie, dus sp² en een vlakke "
        "driehoek met hoeken van ongeveer 120°.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecule met sterisch getal 3 en één vrij elektronenpaar is lineair.",
        antwoord=False,
        uitleg="Ze is vlak en geknikt. Zwaveldioxide is zo gebouwd: twee bindingen en één "
        "vrij paar in een vlak, met een hoek van ongeveer 119°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel orbitalen mengen er bij sp-hybridisatie?",
        opties=[
            "een s-orbitaal en een p-orbitaal",
            "een s-orbitaal en twee p-orbitalen",
            "een s-orbitaal en drie p-orbitalen",
            "twee s-orbitalen en een p-orbitaal",
        ],
        antwoord=0,
        uitleg="Het getal achter de p zegt hoeveel p-orbitalen meedoen: bij sp geen "
        "exponent, dus één. De andere p-orbitalen blijven voor de pi-bindingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuur heeft het ammoniumion NH₄⁺?",
        opties=[
            "een tetraëder",
            "een piramide",
            "een vlakke driehoek",
            "een geknikte vorm",
        ],
        antwoord=0,
        uitleg="Het vrije paar van stikstof is in de vierde binding gaan zitten. Dus vier "
        "partners, geen vrije paren, en een nette tetraëder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de werkelijke bindingshoek zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is kleiner dan de theoretische als er vrije paren zijn",
            "ze is gelijk aan de theoretische zonder vrije paren",
            "ze is altijd groter dan de theoretische hoek",
            "ze hangt niet af van de vrije elektronenparen",
        ],
        antwoord=[0, 1],
        uitleg="Methaan haalt netjes 109,5°, ammoniak 107° en water 104,5°: elk vrij paar "
        "duwt de hoek een stukje kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel bindingspartners heeft een centraal atoom met sterisch getal 4 en één vrij elektronenpaar?",
        antwoord=["drie", "3"],
        uitleg="Vier min één vrij paar geeft drie partners, en dus de vorm van een "
        "piramide, zoals bij ammoniak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een dubbele binding één bindingspartner bij het sterisch getal?",
        opties=[
            "de twee bindingen wijzen samen naar hetzelfde buuratoom",
            "de pi-binding telt niet mee omdat ze zwak is",
            "de twee bindingen liggen samen in hetzelfde orbitaal",
            "de pi-binding staat haaks op de ruimtelijke structuur",
        ],
        antwoord=0,
        uitleg="Het sterisch getal telt richtingen rond het centrale atoom, niet "
        "bindingen. Twee bindingen naar hetzelfde atoom is één richting.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij sp³-hybridisatie liggen de vier orbitalen in hetzelfde vlak.",
        antwoord=False,
        uitleg="Ze wijzen naar de hoeken van een tetraëder, dus net niet in één vlak. "
        "Sp²-orbitalen liggen wel in één vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk sterisch getal heeft het zuurstofatoom in methanol, CH₃-OH?",
        opties=[
            "vier",
            "twee",
            "drie",
            "een",
        ],
        antwoord=0,
        uitleg="Twee bindingspartners, naar koolstof en naar waterstof, plus twee vrije "
        "paren. De C-O-H-hoek is daardoor geknikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het sterisch getal bepaalt zowel de ruimtelijke structuur als het hybridisatietype.",
        antwoord=True,
        uitleg="Twee geeft lineair en sp, drie geeft vlak en sp², vier geeft tetraëdrisch "
        "en sp³. De vrije paren bepalen daarna de werkelijke vorm.",
    ),
    dict(
        type="invultekst",
        vraag="Welke theoretische bindingshoek hoort bij sp²-hybridisatie?",
        antwoord=["120°", "120", "120 graden"],
        uitleg="Drie richtingen in een vlak verdelen 360° eerlijk. Bij etheen meet men "
        "daardoor hoeken van ongeveer 120°.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een binding tussen twee atomen polair?",
        opties=[
            "als de twee atomen een verschillende elektronegatieve waarde hebben",
            "als de twee atomen allebei een vrij elektronenpaar hebben",
            "als de binding uit een sigma- en een pi-binding bestaat",
            "als de twee atomen tot dezelfde groep van het systeem horen",
        ],
        antwoord=0,
        uitleg="Het meest elektronegatieve atoom trekt het bindende paar naar zich toe. "
        "Zo ontstaat er een kant met een klein negatief overschot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is koolstofdioxide apolair, terwijl de bindingen polair zijn?",
        opties=[
            "de molecule is lineair, dus de twee dipolen heffen elkaar op",
            "de molecule is geknikt, dus de dipolen versterken elkaar",
            "koolstof en zuurstof hebben dezelfde elektronegatieve waarde",
            "de dubbele bindingen maken de molecule altijd apolair",
        ],
        antwoord=0,
        uitleg="Bij water lukt dat niet, want daar staan de bindingen in een hoek. "
        "Daarom is water wel polair.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de zwakste intermoleculaire kracht, die tussen alle moleculen werkt?",
        antwoord=["londonkracht", "london-dispersiekracht", "dispersiekracht"],
        uitleg="Ze ontstaat doordat de elektronenwolk kort verschuift. Bij grote "
        "moleculen is ze samen toch sterk genoeg voor een hoog kookpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tussen welke moleculen ontstaat er een waterstofbrug?",
        opties=[
            "als waterstof aan stikstof, zuurstof of fluor gebonden is",
            "als waterstof aan koolstof of zwavel gebonden is",
            "als er een dubbele binding met waterstof in de molecule zit",
            "als de molecule meer dan vier waterstofatomen bevat",
        ],
        antwoord=0,
        uitleg="Die drie atomen zijn klein en sterk elektronegatief. Daardoor blijft de "
        "waterstof bijna bloot en trekt ze een vrij paar van de buur aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een waterstofbrug is sterker dan een gewone dipoolkracht.",
        antwoord=True,
        uitleg="Daarom kookt water bij 100 °C, terwijl waterstofsulfide met bijna "
        "dezelfde massa al bij −60 °C een gas is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht houdt een ion vast in water?",
        opties=[
            "de ion-dipoolkracht",
            "de londonkracht",
            "de waterstofbrug",
            "de metaalbinding",
        ],
        antwoord=0,
        uitleg="De negatieve kant van de watermoleculen gaat rond een positief ion staan, "
        "en omgekeerd. Zo trekken ze de ionen uit het rooster.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kookt pentaan bij een hogere temperatuur dan butaan?",
        opties=[
            "de langere keten geeft meer contact en dus sterkere londonkrachten",
            "de langere keten vormt waterstofbruggen met haar buren",
            "de langere keten is polair en butaan is apolair",
            "de langere keten heeft een dubbele binding erbij",
        ],
        antwoord=0,
        uitleg="Hoe groter het oppervlak waarmee twee moleculen elkaar raken, hoe meer "
        "energie er nodig is om ze los te maken.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof is het schoolvoorbeeld van een polair oplosmiddel?",
        antwoord=["water", "H2O"],
        uitleg="Water lost zouten en andere polaire stoffen goed op. Wasbenzine en white "
        "spirit zijn de apolaire voorbeelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen lossen goed op in wasbenzine? Kruis alles aan wat juist is.",
        opties=[
            "olie",
            "vet",
            "keukenzout",
            "suiker",
        ],
        antwoord=[0, 1],
        uitleg="Gelijk lost op in gelijk: apolaire stoffen in een apolair oplosmiddel. "
        "Zout en suiker zijn polair en blijven liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lost keukenzout op in water?",
        opties=[
            "de watermoleculen trekken de ionen uit het rooster met ion-dipoolkrachten",
            "de watermoleculen breken de ionbinding met een waterstofbrug open",
            "het zout reageert met water en vormt daarbij een nieuw zout",
            "de londonkrachten tussen water en zout zijn sterker dan het rooster",
        ],
        antwoord=0,
        uitleg="Rond elk ion komt een laagje watermoleculen te staan. Het rooster van "
        "Na⁺ en Cl⁻ valt daardoor uiteen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vertakt alkaan kookt bij een hogere temperatuur dan het onvertakte met dezelfde formule.",
        antwoord=False,
        uitleg="Het is net omgekeerd. Een bolle vertakte molecule raakt haar buren over "
        "een kleiner oppervlak, dus is er minder energie nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk rooster heeft het hoogste smeltpunt?",
        opties=[
            "een atoomrooster, zoals diamant",
            "een molecuulrooster, zoals ijs",
            "een metaalrooster, zoals lood",
            "een ionrooster, zoals keukenzout",
        ],
        antwoord=0,
        uitleg="In een atoomrooster moet je echte atoombindingen breken. Bij een "
        "molecuulrooster volstaat het de zwakke krachten ertussen te verbreken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ionrooster zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het geleidt stroom als het gesmolten is",
            "het is hard maar breekbaar",
            "het geleidt stroom in vaste toestand",
            "het is zacht en gemakkelijk vervormbaar",
        ],
        antwoord=[0, 1],
        uitleg="In het vaste rooster zitten de ionen vast en bewegen ze niet. Smelt of "
        "los je het zout op, dan kunnen ze wel bewegen en geleidt het.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht tussen twee tegengesteld geladen ionen?",
        antwoord=["coulombkracht", "de coulombkracht", "coulomb"],
        uitleg="Die kracht houdt een ionrooster samen. Ze is veel sterker dan de krachten "
        "tussen moleculen, en daarom smelt een zout pas bij hoge temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een intramoleculaire en een intermoleculaire kracht?",
        opties=[
            "de eerste zit binnen een molecule, de tweede tussen moleculen",
            "de eerste zit tussen moleculen, de tweede binnen een molecule",
            "de eerste werkt enkel bij ionen, de tweede enkel bij metalen",
            "de eerste werkt op afstand, de tweede enkel bij contact",
        ],
        antwoord=0,
        uitleg="Intra betekent binnen: dat is de atoombinding zelf. Inter betekent "
        "tussen: dat zijn de krachten die moleculen bij elkaar houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is ethanol goed mengbaar met water en hexaan niet?",
        opties=[
            "ethanol heeft een OH-groep die waterstofbruggen met water vormt",
            "ethanol heeft een lagere molaire massa dan hexaan",
            "ethanol heeft een hoger kookpunt dan water zelf",
            "ethanol bestaat uit ionen en hexaan uit moleculen",
        ],
        antwoord=0,
        uitleg="Hexaan is helemaal apolair en kan die bruggen niet maken. Het blijft dus "
        "als aparte laag op het water liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof is het schoolvoorbeeld van een apolaire stof?",
        opties=[
            "tetrachloormethaan, CCl₄",
            "waterstofchloride, HCl",
            "ammoniak, NH₃",
            "methanol, CH₃OH",
        ],
        antwoord=0,
        uitleg="De vier polaire C-Cl-bindingen staan in een tetraëder en heffen elkaar "
        "precies op. De drie andere stoffen zijn wel polair.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaalrooster geleidt stroom ook in vaste toestand.",
        antwoord=True,
        uitleg="De valentie-elektronen bewegen vrij door het hele rooster. Daarom kan je "
        "een koperdraad gewoon in een kring gebruiken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecuulrooster geleidt elektrische stroom goed.",
        antwoord=False,
        uitleg="Er zijn geen vrije ladingen: de moleculen zijn neutraal en de elektronen "
        "zitten in hun bindingen vast. Suiker en ijs geleiden dus niet.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kracht houdt twee watermoleculen bij elkaar?",
        antwoord=["waterstofbrug", "een waterstofbrug", "waterstofbruggen"],
        uitleg="De waterstof van de ene molecule trekt aan een vrij paar van het "
        "zuurstofatoom van de andere. Daardoor heeft water zijn hoge kookpunt.",
    ),
]
