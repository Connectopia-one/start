# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Productlabels, pictogrammen en risico's van stoffen.

Chemie, de kop "Product- en materiaallabels" met haar onderkop "Chemische
eigenschappen en risico's van stoffen" uit de vakfiche natuurwetenschappen 3DU.
Deel 1 gaat over wat er op een etiket staat: de gevarenpictogrammen, de H- en
P-zinnen, het verband tussen concentratie en gevaar, hoe je een stof bewaart en
waar de verpakking hoort. Deel 2 gaat over de eigenschappen zelf: kook- en
smeltpunt, brandbaarheid, het kiezen van een oplosmiddel, en de pH-schaal met
de zuur-base indicator.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat lees je af van een gevarenpictogram?",
        opties=[
            "welk soort gevaar de stof oplevert",
            "hoeveel de stof weegt",
            "hoe duur de stof is",
            "hoe lang de stof houdbaar is",
        ],
        antwoord=0,
        uitleg="Het pictogram vat het gevaar samen in één beeld: bijtend, ontvlambaar, giftig. De H-zinnen schrijven dat gevaar daarna in woorden uit.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de H in een H-zin op een etiket?",
        antwoord=["hazard", "gevaar", "hazard of gevaar"],
        uitleg="H staat voor hazard, het Engelse woord voor gevaar. Een H-zin zegt dus wat er mis kan gaan, bijvoorbeeld dat een stof ernstig oogletsel veroorzaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in een P-zin?",
        opties=[
            "wat je moet doen om veilig met de stof om te gaan",
            "welk gevaar de stof oplevert",
            "uit welke elementen de stof bestaat",
            "in welk land de stof gemaakt werd",
        ],
        antwoord=0,
        uitleg="P staat voor precaution of voorzorg. Een P-zin zegt bijvoorbeeld dat je handschoenen draagt, of wat je doet als de stof in je ogen komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pictogram hoort bij een stof die de huid wegvreet?",
        opties=[
            "het pictogram voor bijtend of corrosief",
            "het pictogram voor ontvlambaar",
            "het pictogram voor oxiderend",
            "het pictogram voor gassen onder druk",
        ],
        antwoord=0,
        uitleg="Bijtend of corrosief wordt getekend met een druppel die een hand en een oppervlak aantast. Ontstopper en sterk zoutzuur dragen dat teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram voor oxiderende stoffen?",
        opties=[
            "de stof kan een brand voeden of versterken",
            "de stof is zelf heel gemakkelijk ontvlambaar",
            "de stof is gevaarlijk voor het waterleven",
            "de stof staat onder hoge druk in de fles",
        ],
        antwoord=0,
        uitleg="Een oxiderende stof geeft zuurstof af. Ze brandt zelf niet goed, maar laat andere stoffen veel feller branden, en daarom staat ze nooit bij brandbare producten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met het pictogram voor gassen onder druk mag je nooit in de zon laten staan.",
        antwoord=True,
        uitleg="Warmte doet de druk in de fles stijgen, en dan kan ze barsten. Daarom bewaar je spuitbussen koel en nooit bij een warmtebron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is geconcentreerde ontstopper corrosief en verdunde ontstopper alleen irriterend?",
        opties=[
            "hoe hoger de concentratie, hoe sterker het effect",
            "verdunnen verandert de stof in een andere stof",
            "verdunde ontstopper bevat een ander bestanddeel",
            "verdunde ontstopper verdampt veel sneller",
        ],
        antwoord=0,
        uitleg="Het is dezelfde stof, maar er zitten minder deeltjes in hetzelfde volume. De dosis bepaalt dus mee hoe gevaarlijk iets is.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde stof kan in een andere concentratie een ander gevarenpictogram krijgen.",
        antwoord=True,
        uitleg="Op een geconcentreerd product staat soms bijtend, op het verdunde product irriterend. Het etiket hoort dus altijd bij die bepaalde verpakking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bewaar je een ontvlambare stof zoals thinner?",
        opties=[
            "goed gesloten, koel en ver van vuur",
            "open, zodat de damp kan ontsnappen",
            "in de buurt van de verwarming",
            "in een glas zonder deksel in de kast",
        ],
        antwoord=0,
        uitleg="De damp is het gevaar, niet de vloeistof zelf. Goed sluiten houdt de damp binnen, en koel bewaren zorgt dat er minder damp ontstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een restje chemisch product hoort bij het klein gevaarlijk afval en niet in de gootsteen.",
        antwoord=True,
        uitleg="Veel van die stoffen zijn schadelijk voor het water en voor de waterzuivering. Daarom worden ze apart ingezameld in het containerpark.",
    ),
    dict(
        type="invultekst",
        vraag="Waar breng je een halfvolle fles ontstopper of verf naartoe?",
        antwoord=["kga", "klein gevaarlijk afval", "containerpark"],
        uitleg="Kga staat voor klein gevaarlijk afval. Dat wordt apart ingezameld, want het mag niet bij het restafval of in het riool terechtkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk afval hoort bij het gft? Er zijn er twee.",
        opties=[
            "aardappelschillen",
            "gemaaid gras",
            "een lege conservenblik",
            "een verfrestje",
        ],
        antwoord=[0, 1],
        uitleg="Gft staat voor groente-, fruit- en tuinafval. Een blik gaat bij het pmd of het metaal, en verf hoort bij het klein gevaarlijk afval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar staat de afkorting pmd voor?",
        opties=[
            "plastic verpakkingen, metaal en drankkartons",
            "papier, metaal en droog afval",
            "plastic, modder en drankflessen",
            "papier, mondmaskers en doosjes",
        ],
        antwoord=0,
        uitleg="In de blauwe zak mogen plastic verpakkingen, metalen verpakkingen en drankkartons. Plastic voorwerpen die geen verpakking zijn, horen er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het cijfer in de driehoek van pijltjes op een plastic verpakking?",
        opties=[
            "uit welke kunststof de verpakking gemaakt is",
            "hoeveel keer de verpakking al hergebruikt is",
            "hoeveel jaar de verpakking meegaat",
            "hoeveel procent ervan gerecycleerd werd",
        ],
        antwoord=0,
        uitleg="Het is een identificatiecode: 1 is PET, 2 is HDPE, 5 is PP, enzovoort. Sorteerinstallaties gebruiken die codes om soorten uit elkaar te halen.",
    ),
    dict(
        type="waarofniet",
        vraag="De driehoek van pijltjes met een cijfer erin betekent dat de verpakking zeker gerecycleerd wordt.",
        antwoord=False,
        uitleg="De code zegt alleen uit welke kunststof ze gemaakt is. Of ze echt gerecycleerd wordt, hangt af van de inzameling en van de installaties in je streek.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kunststof hoort bij de recyclagecode 1, de code van de meeste drinkflessen?",
        antwoord=["PET", "pet", "polyethyleentereftalaat"],
        uitleg="PET is helder, sterk en licht. Het is een van de best gerecycleerde kunststoffen, en van oude flessen worden nieuwe flessen of vezels gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt twee ontvetters. De ene draagt het pictogram bijtend, de andere alleen irriterend. Welke kies je om thuis te gebruiken?",
        opties=[
            "de irriterende, want die geeft minder ernstige schade",
            "de bijtende, want die werkt altijd beter",
            "het maakt geen verschil, de stof is dezelfde",
            "de bijtende, want irriterend zegt niets",
        ],
        antwoord=0,
        uitleg="Bij gelijke werking kies je altijd het minst gevaarlijke product. Bijtend betekent blijvende schade aan huid en ogen, irriterend betekent voorbijgaande hinder.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag ontstopper en bleekwater gerust samen in dezelfde afvoer gieten.",
        antwoord=False,
        uitleg="Zulke producten kunnen met elkaar reageren en giftige gassen of veel warmte geven. Op het etiket staat daarom een P-zin die het mengen uitdrukkelijk afraadt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de voorzorgen die je op een etiket terugvindt? Er zijn er drie.",
        opties=[
            "handschoenen dragen",
            "buiten het bereik van kinderen houden",
            "bij contact met de ogen spoelen met water",
            "het product zo snel mogelijk opgebruiken",
        ],
        antwoord=[0, 1, 2],
        uitleg="P-zinnen gaan over beschermen, bewaren en wat te doen bij een ongeval. Snel opgebruiken is geen voorzorg; dat zou je juist tot onnodig gebruik aanzetten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een product overgieten in een lege drankfles is een veilige manier om het te bewaren.",
        antwoord=False,
        uitleg="Dan zit het product in een verpakking zonder etiket, zonder pictogram en met het uitzicht van iets drinkbaars. Dat is een van de grootste oorzaken van vergiftigingen thuis.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het kookpunt van een stof?",
        opties=[
            "de temperatuur waarbij ze overgaat van vloeistof naar gas",
            "de temperatuur waarbij ze overgaat van vast naar vloeibaar",
            "de temperatuur waarbij ze vlam vat",
            "de temperatuur waarbij ze uit elkaar valt",
        ],
        antwoord=0,
        uitleg="Bij het kookpunt verdampt de hele vloeistof, niet alleen het oppervlak. Het smeltpunt is de overgang van vast naar vloeibaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is aceton zo geschikt om glaswerk snel droog te maken?",
        opties=[
            "het heeft een laag kookpunt en verdampt dus vlot",
            "het heeft een hoog kookpunt en blijft dus staan",
            "het bindt het water chemisch aan zich",
            "het laat een beschermlaagje achter op het glas",
        ],
        antwoord=0,
        uitleg="Aceton kookt al bij ongeveer zesenvijftig graden en verdampt dus snel bij kamertemperatuur. Datzelfde lage kookpunt maakt het ook erg brandbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een laag kookpunt is meestal gemakkelijk ontvlambaar.",
        antwoord=True,
        uitleg="Ze verdampt vlot, dus er staat altijd damp boven de vloeistof. En het is die damp die vlam vat, niet de vloeistof zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt een stof die bij kamertemperatuur vast is. Waar let je op?",
        opties=[
            "het smeltpunt ligt boven de kamertemperatuur",
            "het kookpunt ligt onder de kamertemperatuur",
            "het smeltpunt ligt onder het vriespunt",
            "het kookpunt en het smeltpunt liggen gelijk",
        ],
        antwoord=0,
        uitleg="Zolang het niet warm genoeg is om te smelten, blijft de stof vast. Ligt het smeltpunt eronder, dan is ze bij kamertemperatuur al vloeibaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe luidt de vuistregel over oplossen, in drie woorden?",
        antwoord=["soort lost soort", "gelijk lost gelijk", "soort lost op"],
        uitleg="Soort lost soort op: wateroplosbare stoffen lossen op in water, vetoplosbare in organische oplosmiddelen. Daarom helpt water niet tegen een vetvlek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oplosmiddelen zijn vetoplosbaar of organisch? Er zijn er drie.",
        opties=[
            "thinner",
            "terpentine",
            "white spirit",
            "water",
        ],
        antwoord=[0, 1, 2],
        uitleg="Thinner, terpentine, white spirit en wasbenzine zijn organische oplosmiddelen en lossen vet en verf op. Water doet juist het omgekeerde en lost zouten en suikers op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een vetvlek van olie op je kleren. Waarmee verdwijnt die het best?",
        opties=[
            "met een vetoplosbaar oplosmiddel of afwasmiddel",
            "met koud water alleen",
            "met een scheutje azijn",
            "met keukenzout en warm water",
        ],
        antwoord=0,
        uitleg="Olie is vetoplosbaar en mengt niet met water. Een organisch oplosmiddel lost ze op, en afwasmiddel pakt haar aan omdat het aan de ene kant op vet lijkt en aan de andere kant op water.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die goed in water oplost, lost meestal ook goed op in thinner.",
        antwoord=False,
        uitleg="Het is net omgekeerd. Wat in water oplost, lost doorgaans niet op in een organisch oplosmiddel, en dat is precies wat de regel soort lost soort op zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt de pH van een zure stof?",
        opties=[
            "onder 7",
            "boven 7",
            "precies op 7",
            "boven 14",
        ],
        antwoord=0,
        uitleg="De schaal loopt van 0 tot 14. Onder 7 is zuur, boven 7 basisch, en precies 7 is neutraal, zoals zuiver water.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft een neutrale stof zoals zuiver water?",
        antwoord=["7", "pH 7", "zeven"],
        uitleg="Zeven is het midden van de schaal. Daar zijn er evenveel zure als basische deeltjes aanwezig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kleur krijgt rode koolsap, een zuur-base indicator, in een zure vloeistof?",
        opties=[
            "rood tot roze",
            "groen tot geel",
            "diepblauw",
            "kleurloos",
        ],
        antwoord=0,
        uitleg="Rode koolsap kleurt rood in zuur, paars tot blauw bij neutraal en groen tot geel in base. Zo lees je met één druppel af waarmee je te maken hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een indicator geeft met een kleur aan of een stof zuur of basisch is.",
        antwoord=True,
        uitleg="De indicator verandert van kleur bij een bepaalde pH. Universeel indicatorpapier combineert er zelfs meerdere, zodat je de pH ongeveer kan aflezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn zuren? Er zijn er drie.",
        opties=[
            "azijnzuur in huishoudazijn",
            "citroenzuur in citroensap",
            "zoutzuur in maagsap",
            "ammoniak in een glasreiniger",
        ],
        antwoord=[0, 1, 2],
        uitleg="Azijnzuur, citroenzuur en zoutzuur hebben een pH onder 7. Ammoniak is juist basisch en heeft een pH boven 7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom pak je een partje citroen beter niet in aluminiumfolie?",
        opties=[
            "het zuur reageert met het aluminium",
            "het zuur maakt de folie te koud",
            "de folie maakt het zuur sterker",
            "de folie lost op in het sap van de citroen",
        ],
        antwoord=0,
        uitleg="Zuren tasten aluminium aan. Er ontstaan gaatjes in de folie en er komen aluminiumverbindingen in het voedsel terecht, en dat wil je niet opeten.",
    ),
    dict(
        type="waarofniet",
        vraag="Zuren worden ook in voeding gebruikt, bijvoorbeeld als bewaarmiddel.",
        antwoord=True,
        uitleg="Azijnzuur in augurken en citroenzuur in frisdrank houden bacteriën tegen en geven smaak. Of een zuur gevaarlijk is, hangt af van welk zuur en van de concentratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als een bijtende stof op je huid komt?",
        opties=[
            "meteen lang spoelen met veel water",
            "eerst met een doek stevig afwrijven",
            "er een zuur over gieten om te neutraliseren",
            "wachten tot de stof vanzelf opdroogt",
        ],
        antwoord=0,
        uitleg="Spoelen verdunt de stof en voert ze af. Neutraliseren met een tegengestelde stof geeft warmte en maakt de schade erger, en wrijven wrijft de stof juist in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat op een fles ethanol het pictogram voor ontvlambaar?",
        opties=[
            "de damp erboven kan vlam vatten",
            "de vloeistof wordt vanzelf warm",
            "de fles staat onder druk",
            "de stof reageert met water",
        ],
        antwoord=0,
        uitleg="Ethanol verdampt vlot en de damp mengt zich met de lucht. Een vonk volstaat dan, en daarom hou je zo'n fles ver van een vlam.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kookpunt van een stof zegt niets over hoe gevaarlijk ze kan zijn.",
        antwoord=False,
        uitleg="Het zegt er juist veel over. Een laag kookpunt betekent veel damp, dus meer kans op ontvlammen en op inademen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet kiezen tussen twee producten die even goed werken. Welk argument is doorslaggevend?",
        opties=[
            "het product met het minst zware gevarenpictogram",
            "het product in de grootste verpakking",
            "het product met de felste kleur op het etiket",
            "het product met de langste H-zin",
        ],
        antwoord=0,
        uitleg="Bij gelijke werking kies je het minst gevaarlijke product, voor jezelf en voor het milieu. Verpakkingsgrootte en kleur zeggen niets over het risico.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof met een pH boven 7?",
        antwoord=["base", "basisch", "een base"],
        uitleg="Basen voelen glibberig aan en zijn in hoge concentratie net zo bijtend als sterke zuren. Ontstopper en bijtende soda zijn er voorbeelden van.",
    ),
]
