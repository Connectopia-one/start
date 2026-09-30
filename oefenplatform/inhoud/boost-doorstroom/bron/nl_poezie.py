# -*- coding: utf-8 -*-
"""De vragen voor "Poëzie, drama en literaire stromingen" (🚀 Boost doorstroom, Nederlands).

Uit de vakfiche van Nederlands 2, de delen poëzie en drama, en uit het stuk
over de literaire stromingen: dichtvormen, rijm, ritme, strofevormen,
stijlfiguren, de subgenres van het drama, de elementen van een
opvoeringsanalyse, en de kenmerken van de middeleeuwen, de romantiek en het
realisme.

Deel 1 is de poëzie. Deel 2 is het drama en de stromingen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel versregels telt een sonnet?",
        opties=["veertien", "twaalf", "acht", "zestien"],
        antwoord=0,
        uitleg="Meestal verdeeld in een octaaf van acht regels en een sextet van zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een acrostichon of naamdicht?",
        opties=[
            "een gedicht waarvan de beginletters samen een woord vormen",
            "een gedicht waarin elke regel evenveel lettergrepen telt",
            "een gedicht zonder enige vorm van rijm of maat",
            "een gedicht dat verteld wordt door een ik-figuur",
        ],
        antwoord=0,
        uitleg="Lees de eerste letters van boven naar beneden en je krijgt een naam of een boodschap.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de Japanse dichtvorm van drie regels met vijf, zeven en vijf lettergrepen?",
        antwoord=["haiku", "een haiku", "de haiku"],
        uitleg="Kort, zonder rijm, en meestal met een beeld uit de natuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een limerick is een grappig gedicht van vijf regels.",
        antwoord=True,
        uitleg="Het rijmschema is aabba, en de clou zit altijd in de laatste regel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn dichtvormen?",
        opties=["de ballade", "het sonnet", "het vrije vers", "de klucht"],
        antwoord=[0, 1, 2],
        uitleg="Een klucht is een toneelvorm, geen dichtvorm. De fiche noemt daarnaast de haiku, de limerick, het naamdicht en de minneliederen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is alliteratie?",
        opties=[
            "dezelfde beginmedeklinker in woorden vlak na elkaar",
            "dezelfde klinkerklank in woorden vlak na elkaar",
            "dezelfde eindklank aan het einde van twee versregels",
            "dezelfde regel die na elke strofe terugkeert",
        ],
        antwoord=0,
        uitleg="Zoals in 'ruisend riet' of 'tussen twee torens'. Het maakt een regel hoorbaar, ook zonder eindrijm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het herhalen van dezelfde klinkerklank in woorden vlak na elkaar?",
        antwoord=["assonantie", "de assonantie"],
        uitleg="Het is de tegenhanger van alliteratie, die de beginmedeklinker herhaalt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij gekruist rijm is het rijmschema abab.",
        antwoord=True,
        uitleg="Gepaard rijm is aabb, omarmend rijm is abba. Bij gekruist rijm springt het rijm telkens een regel over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn stijlfiguren?",
        opties=["herhaling", "personificatie", "overdrijving", "enjambement"],
        antwoord=[0, 1, 2],
        uitleg="Een enjambement staat bij de fiche onder ritme, niet onder de stijlfiguren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een enjambement?",
        opties=[
            "een zin die doorloopt over het einde van de versregel heen",
            "een regel die na elke strofe letterlijk terugkeert",
            "een gedicht zonder vaste maat en zonder rijm",
            "een strofe die uit precies drie regels bestaat",
        ],
        antwoord=0,
        uitleg="De regel breekt af waar de zin nog niet af is. Dat legt nadruk op het laatste en het eerste woord.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kwatrijn is een strofe van zes regels.",
        antwoord=False,
        uitleg="Een kwatrijn telt er vier. Zes is een sextet, drie is een terzine en acht is een octaaf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk rijmschema hoort bij omarmend rijm?",
        opties=["abba", "abab", "aabb", "aaaa"],
        antwoord=0,
        uitleg="De buitenste twee regels rijmen op elkaar en sluiten de binnenste twee in, als armen eromheen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een strofe van vier versregels?",
        antwoord=["kwatrijn", "een kwatrijn", "het kwatrijn"],
        uitleg="Twee kwatrijnen samen vormen het octaaf van een sonnet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een refrein?",
        opties=[
            "een regel of strofe die telkens terugkeert in het gedicht",
            "de laatste regel van een gedicht met de clou erin",
            "een strofe van zes regels na een octaaf",
            "een zin die over de versregel heen doorloopt",
        ],
        antwoord=0,
        uitleg="Je kent het van liedjes. In een ballade doet het refrein hetzelfde werk: het bindt het verhaal samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vrij vers heeft een vast rijmschema en een vaste maat.",
        antwoord=False,
        uitleg="Precies omgekeerd: een vrij vers laat allebei los. Wat overblijft is de regelval en de beeldspraak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel regels telt een terzine?",
        opties=["drie", "vier", "zes", "acht"],
        antwoord=0,
        uitleg="In een sonnet volgen na het octaaf vaak twee terzinen, die samen het sextet vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze rijmsoorten bestaan?",
        opties=["gepaard rijm", "gekruist rijm", "omarmend rijm", "blank rijm"],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt daarnaast volrijm, eindrijm, alliteratie en assonantie. Blank rijm staat er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn minneliederen?",
        opties=[
            "middeleeuwse liederen over de liefde",
            "moderne liederen zonder vaste maat",
            "liederen die bij een begrafenis gezongen worden",
            "liederen met een vast refrein na elke strofe",
        ],
        antwoord=0,
        uitleg="Minne is het middeleeuwse woord voor liefde. Ze horen bij de hoofse cultuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een vers en een strofe?",
        opties=[
            "een vers is één regel, een strofe een groepje regels",
            "een vers is een heel gedicht, een strofe een deel ervan",
            "een vers rijmt, een strofe niet",
            "een vers hoort bij een lied, een strofe bij een gedicht",
        ],
        antwoord=0,
        uitleg="In de poëzie betekent 'vers' dus niet hetzelfde als in het dagelijks taalgebruik, waar het vaak het hele gedicht aanduidt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt een dichter een enjambement?",
        opties=[
            "om nadruk te leggen op het woord vlak voor en na de breuk",
            "om het gedicht korter te maken",
            "om een vast rijmschema te kunnen aanhouden",
            "om aan te geven dat een strofe eindigt",
        ],
        antwoord=0,
        uitleg="Je oog valt van de regel af terwijl de zin nog doorloopt. Die kleine aarzeling is het effect.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een tragedie?",
        opties=[
            "een toneelstuk dat slecht afloopt voor de hoofdpersoon",
            "een toneelstuk waarin voortdurend gezongen wordt",
            "een kort toneelstuk met grove grappen erin",
            "een toneelstuk zonder decor en zonder rekwisieten",
        ],
        antwoord=0,
        uitleg="De hoofdpersoon gaat ten onder, vaak door een eigenschap die hem eerst juist groot maakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een klucht?",
        opties=[
            "een kort toneelstuk met grove, volkse humor",
            "een toneelstuk dat treurig afloopt",
            "een toneelstuk waarin uitsluitend gedanst wordt",
            "een toneelstuk zonder enige vorm van dialoog",
        ],
        antwoord=0,
        uitleg="Kluchten drijven op misverstanden, verkleedpartijen en herkenbare types.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je toneel waarin gezongen wordt, zoals een musical of een opera?",
        antwoord=["muziektheater", "het muziektheater"],
        uitleg="De fiche noemt het als een van de vier subgenres van drama.",
    ),
    dict(
        type="waarofniet",
        vraag="Een komedie loopt goed af.",
        antwoord=True,
        uitleg="Dat is het klassieke onderscheid met de tragedie. Onderweg mag er van alles misgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen horen bij een opvoeringsanalyse?",
        opties=["het decor", "de belichting", "de rekwisieten", "het rijmschema"],
        antwoord=[0, 1, 2],
        uitleg="Een rijmschema hoort bij poëzie. De fiche noemt verder ruimte, mimiek, gebaren, kostumering, grime, muziek en geluid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn rekwisieten?",
        opties=[
            "de voorwerpen die de spelers op het toneel gebruiken",
            "de kleren die de spelers op het toneel dragen",
            "de lampen waarmee het toneel verlicht wordt",
            "de gebaren waarmee een speler iets duidelijk maakt",
        ],
        antwoord=0,
        uitleg="Een brief, een glas, een wapen. De kleren heten kostumering, en die staat apart in de lijst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de schmink waarmee een acteur er ouder of heel anders uit gaat zien?",
        antwoord=["grime", "de grime"],
        uitleg="Grime en kostumering samen bepalen hoe een personage er van ver uitziet.",
    ),
    dict(
        type="waarofniet",
        vraag="Kostumering is volgens de vakfiche een element van de opvoeringsanalyse.",
        antwoord=True,
        uitleg="Wat iemand draagt, zegt iets over zijn stand, zijn tijd en zijn karakter, nog voor hij iets gezegd heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor middeleeuwse literatuur?",
        opties=[
            "getallensymboliek en een dubbele gelaagdheid",
            "een nuchtere beschrijving van sociale wantoestanden",
            "de nadruk op het gevoel van het eenzame individu",
            "het volledig loslaten van rijm en maat",
        ],
        antwoord=0,
        uitleg="Het tweede past bij het realisme, het derde bij de romantiek, het vierde bij het moderne vrije vers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke literaire stromingen moet je volgens de vakfiche op een tekst kunnen toepassen?",
        opties=["de middeleeuwen", "de romantiek", "het realisme", "de barok"],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt uitdrukkelijk die drie, met hun kenmerken, hun situering en hun stijl.",
    ),
    dict(
        type="waarofniet",
        vraag="De hoofse liefde is een thema uit de romantiek.",
        antwoord=False,
        uitleg="Ze hoort bij de middeleeuwen: de ridder die zijn dame van op afstand vereert en haar met daden probeert te verdienen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met de dubbele gelaagdheid van middeleeuwse literatuur?",
        opties=[
            "een tekst over een belegerd kasteel kan ook over het hof maken gaan",
            "een tekst wordt altijd in twee talen tegelijk geschreven",
            "een tekst heeft altijd twee vertellers naast elkaar",
            "een tekst speelt zich in twee verschillende tijden af",
        ],
        antwoord=0,
        uitleg="Onder het verhaal ligt een tweede betekenis. Wie alleen de bovenlaag leest, mist de helft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de betekenis die middeleeuwse teksten aan bepaalde getallen geven?",
        antwoord=["getallensymboliek", "de getallensymboliek"],
        uitleg="Drie, zeven en twaalf duiken niet toevallig zo vaak op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee confronteerde de realistische literatuur haar lezers?",
        opties=[
            "met de wantoestanden in de maatschappij, zoals kinderarbeid",
            "met de idealen van de ridder en zijn dame",
            "met het gevoel van het eenzame, dromende individu",
            "met de verborgen betekenis van heilige getallen",
        ],
        antwoord=0,
        uitleg="Dat is precies waarom de fiche vraagt of een tekst relevant was voor de samenleving waarin hij ontstond.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een opvoeringsanalyse kijk je alleen naar de tekst van het stuk.",
        antwoord=False,
        uitleg="Je kijkt juist naar alles wat de tekst níét is: decor, licht, geluid, kleren, grime, gebaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is mimiek belangrijk op het toneel?",
        opties=[
            "omdat een gezicht iets anders kan zeggen dan de woorden",
            "omdat de zaal de woorden meestal niet verstaat",
            "omdat elke acteur dezelfde gebaren moet maken",
            "omdat mimiek de belichting vervangt",
        ],
        antwoord=0,
        uitleg="Een personage dat 'het gaat prima' zegt met angst op zijn gezicht, vertelt je twee dingen tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn subgenres van het drama?",
        opties=["de tragedie", "de komedie", "de klucht", "de ballade"],
        antwoord=[0, 1, 2],
        uitleg="De ballade is een dichtvorm. Het vierde subgenre van drama is het muziektheater.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient belichting in een voorstelling?",
        opties=[
            "om de aandacht te sturen en de sfeer te bepalen",
            "om de acteurs hun tekst te laten aflezen",
            "om het decor tussen de bedrijven te verplaatsen",
            "om de zaal te laten weten wanneer het pauze is",
        ],
        antwoord=0,
        uitleg="Eén lichtbundel op één speler zegt: kijk hier. Koud blauw licht zegt iets heel anders dan warm geel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de vakfiche of je kan uitleggen in welke mate een tekst relevant is voor onze samenleving?",
        opties=[
            "omdat literatuur iets zegt over de wereld van toen en die van nu",
            "omdat een oude tekst anders niet gelezen mag worden",
            "omdat elke tekst evenveel over vandaag moet zeggen",
            "omdat je anders het rijmschema niet kan bepalen",
        ],
        antwoord=0,
        uitleg="Een verhaal over kinderarbeid uit 1880 leest anders als je weet dat het toen echt gebeurde, en anders als je aan vandaag denkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig te weten in welke tijd een literaire tekst ontstond?",
        opties=[
            "omdat de stroming verklaart waarom hij er zo uitziet",
            "omdat oudere teksten altijd korter zijn",
            "omdat alleen recente teksten beeldspraak gebruiken",
            "omdat de tijd bepaalt hoeveel strofen er zijn",
        ],
        antwoord=0,
        uitleg="Getallensymboliek verwacht je in de middeleeuwen, sociale wantoestanden in het realisme, dromerig verlangen in de romantiek.",
    ),
]
