# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Natuurlijke selectie en het ontstaan van soorten.

Biologie, de onderkop "Natuurlijke selectie" van de kop "Ontstaan en evolutie
van soorten" uit de vakfiche natuurwetenschappen 3DU. Deel 1 vergelijkt Lamarck,
Darwin en de moderne evolutietheorie, en past de hoofdgedachten toe op
voorbeelden zoals de peper-en-zoutvlinder en antibioticaresistentie. Deel 2 gaat
over mutatie, variatie, selectie en isolatie als motor van soortvorming, over de
isolatievormen, en over de menswording.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat dacht Lamarck over de lange hals van de giraf?",
        opties=[
            "elk dier rekte zich uit en gaf die langere hals door",
            "giraffen met een langere hals overleefden vaker",
            "een toevallige mutatie maakte de hals langer",
            "de hals werd langer door de keuze van het wijfje",
        ],
        antwoord=0,
        uitleg="Lamarck dacht dat een lichaamsdeel groeit door het te gebruiken, en dat zo'n verworven eigenschap overgaat op de nakomelingen. Dat laatste blijkt niet te kloppen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemde Lamarck eigenschappen die een dier tijdens zijn leven ontwikkelt en volgens hem doorgeeft?",
        antwoord=["verworven eigenschappen", "verworven", "verworven kenmerken"],
        uitleg="De erfelijkheid van verworven eigenschappen is de kern van Lamarcks theorie. Wie veel spieren kweekt, krijgt daarom nog geen gespierd kind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van de theorie van Darwin?",
        opties=[
            "wie het best past bij de omgeving, plant zich het meest voort",
            "wie zijn lichaamsdelen het meest gebruikt, geeft ze door",
            "wie het sterkst is, leeft altijd het langst",
            "wie het grootst is, krijgt de meeste nakomelingen",
        ],
        antwoord=0,
        uitleg="Er is variatie, er worden meer jongen geboren dan er kunnen overleven, en wie toevallig beter past, laat meer nakomelingen na. Zo verschuift de populatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Darwin wist nog niet hoe eigenschappen precies worden doorgegeven.",
        antwoord=True,
        uitleg="Genen en DNA waren nog onbekend. Pas toen de erfelijkheidsleer erbij kwam, werd duidelijk waar de variatie vandaan komt waarop de selectie werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er in de moderne evolutietheorie bijgekomen ten opzichte van Darwin? Er zijn er twee.",
        opties=[
            "mutaties als bron van nieuwe variatie",
            "de genetica als verklaring voor overerving",
            "het idee dat de omgeving selecteert",
            "het idee dat soorten veranderen",
        ],
        antwoord=[0, 1],
        uitleg="Selectie en veranderende soorten zaten al bij Darwin. Mutaties en de genetica verklaren pas waaruit de variatie ontstaat en hoe ze doorgegeven wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent survival of the fittest?",
        opties=[
            "wie het best bij zijn omgeving past, overleeft het best",
            "wie het sterkst en het grootst is, wint altijd",
            "wie het snelst kan lopen, ontsnapt altijd",
            "wie het meeste voedsel vindt, leeft het langst",
        ],
        antwoord=0,
        uitleg="Fit betekent hier passend, niet fit in de zin van gespierd. Een kleine, onopvallende muis kan beter passen bij haar omgeving dan een grote, opvallende.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een kenmerk waarmee een organisme goed past bij zijn omgeving?",
        antwoord=["aanpassing", "adaptatie", "een aanpassing"],
        uitleg="Een aanpassing of adaptatie geeft voordeel in die bepaalde omgeving. Verandert de omgeving, dan kan dezelfde eigenschap plots een nadeel worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een organisme kan zichzelf doelbewust aanpassen aan zijn omgeving om beter te overleven.",
        antwoord=False,
        uitleg="Wat je in je leven leert of traint, verandert je genen niet. De aanpassing van een soort komt van variatie die er toevallig al was, en waarop de omgeving selecteert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werden de peper-en-zoutvlinders in de industriële streken donkerder?",
        opties=[
            "op roetzwarte boomstammen vielen donkere vlinders minder op",
            "het roet kleurde de vleugels van de vlinders zwart",
            "de vlinders pasten hun kleur aan het roet aan",
            "donkere vlinders legden plots veel meer eitjes",
        ],
        antwoord=0,
        uitleg="De donkere vorm bestond al, maar was zeldzaam. Op beroete stammen werden lichte vlinders vaker opgegeten, en zo nam het aandeel donkere vlinders toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Toen de lucht schoner werd, nam het aandeel lichte peper-en-zoutvlinders weer toe.",
        antwoord=True,
        uitleg="Met minder roet werden de stammen weer licht, en vielen donkere vlinders meer op. De selectie draaide dus mee met de omgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat antibioticaresistentie bij bacteriën?",
        opties=[
            "enkele bacteriën waren al ongevoelig en overleven de kuur",
            "de bacteriën leren tijdens de kuur weerstand opbouwen",
            "het antibioticum maakt de bacteriën sterker",
            "de bacteriën kiezen zelf om te veranderen",
        ],
        antwoord=0,
        uitleg="Door mutaties is er altijd variatie. Het antibioticum doodt de gevoelige bacteriën en laat de ongevoelige over, die zich daarna ongestoord vermenigvuldigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een antibioticakuur vroegtijdig stoppen vergroot de kans op resistentie.",
        antwoord=True,
        uitleg="De gevoeligste bacteriën sterven eerst. Stop je te vroeg, dan blijven juist de minder gevoelige over en krijgen die de kans zich te vermeerderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is seksuele selectie?",
        opties=[
            "partners kiezen voor bepaalde kenmerken",
            "alleen de sterkste dieren overleven de winter",
            "dieren kiezen zelf hun aantal jongen",
            "de omgeving kiest de best aangepaste dieren",
        ],
        antwoord=0,
        uitleg="De pauwenstaart maakt vluchten lastiger, maar wordt toch doorgegeven omdat pauwinnen ervoor kiezen. Voortplantingskans weegt dus even zwaar als overlevingskans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken horen bij Darwin en niet bij Lamarck? Er zijn er twee.",
        opties=[
            "binnen een soort bestaat er variatie",
            "er worden meer jongen geboren dan er overleven",
            "een gebruikt lichaamsdeel groeit en wordt doorgegeven",
            "een ongebruikt lichaamsdeel verdwijnt in één generatie",
        ],
        antwoord=[0, 1],
        uitleg="Variatie en overproductie van jongen zijn twee hoofdgedachten van Darwin. De twee andere uitspraken zijn juist de kern van Lamarcks verklaring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zou Lamarck verklaren dat een mol zulke kleine ogen heeft?",
        opties=[
            "door ze onder de grond niet te gebruiken, werden ze kleiner",
            "mollen met kleine ogen hielden er meer energie aan over",
            "een mutatie maakte de ogen bij toeval kleiner",
            "de mol koos ervoor om onder de grond te leven",
        ],
        antwoord=0,
        uitleg="Bij Lamarck verdwijnt wat niet gebruikt wordt, en gaat dat verlies over op de jongen. Darwin zou zeggen dat kleine ogen onder de grond geen nadeel waren en dus bleven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de strijd om voedsel, ruimte en partners binnen een populatie?",
        antwoord=["struggle for life", "struggle for existence"],
        uitleg="Omdat er meer jongen geboren worden dan er plaats en voedsel is, ontstaat er concurrentie. Die strijd is het zeefje waar de variatie doorheen moet.",
    ),
    dict(
        type="waarofniet",
        vraag="Natuurlijke selectie maakt nieuwe eigenschappen aan.",
        antwoord=False,
        uitleg="Selectie kiest alleen uit wat er al is. Nieuwe eigenschappen komen van mutaties en van het herschikken van allelen bij de geslachtelijke voortplanting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is variatie binnen een populatie belangrijk?",
        opties=[
            "er is dan meer kans dat sommigen een verandering overleven",
            "alle dieren groeien er sneller door",
            "de populatie wordt er automatisch groter door",
            "er worden meer jongen per worp geboren",
        ],
        antwoord=0,
        uitleg="Zonder verschillen is er niets om uit te selecteren. Een populatie waarin iedereen gelijk is, kan door één ziekte of één koude winter volledig verdwijnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Natuurlijke selectie werkt even goed op aangeleerde als op erfelijke kenmerken.",
        antwoord=False,
        uitleg="Alleen erfelijke kenmerken tellen, want alleen die worden doorgegeven. Een kenmerk dat je in je leven opdoet, verdwijnt met jou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee dingen heeft natuurlijke selectie nodig? Er zijn er twee.",
        opties=[
            "erfelijke variatie tussen individuen",
            "verschil in overlevings- of voortplantingskans",
            "een gelijke kans voor elk individu",
            "een omgeving die nooit verandert",
        ],
        antwoord=[0, 1],
        uitleg="Zonder verschillen valt er niets te selecteren, en zonder verschil in kansen verschuift er niets. Een onveranderlijke omgeving of gelijke kansen zouden de selectie juist stilleggen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een soort in de biologie?",
        opties=[
            "een groep die onderling vruchtbare nakomelingen krijgt",
            "een groep dieren die er hetzelfde uitzien",
            "een groep die in hetzelfde gebied leeft",
            "een groep met evenveel chromosomen",
        ],
        antwoord=0,
        uitleg="Het soortbegrip draait om voortplanting. Een paard en een ezel krijgen samen een muildier, maar dat is onvruchtbaar, dus zijn het twee soorten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een muildier is onvruchtbaar, en daarom zijn paard en ezel twee verschillende soorten.",
        antwoord=True,
        uitleg="Ze kunnen wel nakomelingen krijgen, maar geen vruchtbare. Daardoor blijven de twee genenpoelen gescheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit ontstaat nieuwe erfelijke variatie? Er zijn er twee.",
        opties=[
            "uit mutaties in het DNA",
            "uit het herschikken van chromosomen bij de meiose",
            "uit het trainen van spieren",
            "uit het aanleren van nieuw gedrag",
        ],
        antwoord=[0, 1],
        uitleg="Mutaties maken echt nieuwe allelen, en de meiose schudt de bestaande telkens anders door elkaar. Wat je traint of leert, raakt je geslachtscellen niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het ontstaan van een nieuwe soort uit een bestaande?",
        antwoord=["soortvorming", "speciatie", "de soortvorming"],
        uitleg="Soortvorming gebeurt wanneer twee groepen van dezelfde soort lang genoeg gescheiden blijven. Ze groeien dan zo uiteen dat ze zich niet meer met elkaar voortplanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is isolatie nodig voor soortvorming?",
        opties=[
            "zonder isolatie blijven de groepen hun genen mengen",
            "zonder isolatie treden er geen mutaties op",
            "zonder isolatie is er geen natuurlijke selectie",
            "zonder isolatie krijgen dieren geen jongen",
        ],
        antwoord=0,
        uitleg="Blijven twee groepen met elkaar paren, dan vloeien hun verschillen telkens weer samen. Pas als die uitwisseling stopt, kunnen ze uit elkaar groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rivier verandert van loop en snijdt een populatie muizen in twee. Over welke isolatie gaat het?",
        opties=[
            "geografische isolatie",
            "temporele isolatie",
            "ecologische isolatie",
            "gedragsisolatie",
        ],
        antwoord=0,
        uitleg="Een fysieke barrière zoals een rivier, een bergketen of een zeearm scheidt de groepen in de ruimte. Dat is geografische isolatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kikkersoorten in dezelfde vijver paren in verschillende maanden. Welke isolatie is dat?",
        opties=[
            "temporele isolatie",
            "geografische isolatie",
            "morfologische isolatie",
            "ecologische isolatie",
        ],
        antwoord=0,
        uitleg="Temporeel betekent in de tijd. Ze leven op dezelfde plaats, maar hun voortplantingsperiodes overlappen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vogelsoorten herkennen elkaars baltsroep niet en paren daardoor niet. Welke isolatie is dat?",
        opties=[
            "gedragsisolatie",
            "geografische isolatie",
            "temporele isolatie",
            "morfologische isolatie",
        ],
        antwoord=0,
        uitleg="Het gedrag zelf houdt ze uit elkaar: de roep, de dans of de kleur wordt niet herkend als een signaal van een soortgenoot.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je isolatie waarbij twee groepen in hetzelfde gebied een andere leefplek gebruiken, bijvoorbeeld de boomtop en de bodem?",
        antwoord=["ecologische isolatie", "ecologisch", "ecologische"],
        uitleg="Bij ecologische isolatie leven de groepen op dezelfde plaats, maar in een andere niche. Ze komen elkaar daardoor zelden tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Morfologische isolatie betekent dat de bouw van de dieren paren onmogelijk maakt.",
        antwoord=True,
        uitleg="Verschillen in grootte of in de bouw van de geslachtsorganen kunnen de paring letterlijk onmogelijk maken, ook als de dieren naast elkaar leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe draagt een mutatie bij aan de evolutie van een soort?",
        opties=[
            "ze levert een nieuw allel waarop selectie kan werken",
            "ze maakt het dier meteen beter aangepast",
            "ze zorgt voor meer nakomelingen per worp",
            "ze versnelt de groei van het organisme",
        ],
        antwoord=0,
        uitleg="De meeste mutaties doen niets of zijn nadelig. Maar af en toe geeft er één voordeel in die omgeving, en dan wordt ze stilaan talrijker in de populatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mutatie ontstaat omdat het organisme ze nodig heeft.",
        antwoord=False,
        uitleg="Mutaties gebeuren bij toeval, los van wat van pas zou komen. Pas achteraf blijkt uit de omgeving of een mutatie voordeel oplevert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de mens en de mensapen gemeenschappelijk? Er zijn er drie.",
        opties=[
            "een grote hersenschors",
            "handen met een tegenstelbare duim",
            "zorg voor de jongen gedurende jaren",
            "een volledig rechtopgaande gang",
        ],
        antwoord=[0, 1, 2],
        uitleg="Grote hersenen, grijphanden en lange ouderzorg delen we met chimpansee en gorilla. Volledig rechtop lopen is juist typisch voor onze eigen lijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stap kwam in de menswording het eerst?",
        opties=[
            "rechtop lopen",
            "werktuigen maken",
            "taal gebruiken",
            "kunst maken",
        ],
        antwoord=0,
        uitleg="Australopithecus liep al rechtop terwijl de hersenen nog klein waren. Pas later kwamen werktuigen, en nog later taal en cultuur.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van stappen waarbij de mens uit zijn voorouders ontstond?",
        antwoord=["hominisatie", "de hominisatie", "menswording"],
        uitleg="Hominisatie is de menswording: rechtop gaan lopen, de handen vrij krijgen, werktuigen maken, en de hersenen zien groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voordeel gaf rechtop lopen?",
        opties=[
            "de handen kwamen vrij om dingen te dragen",
            "het lichaam werd veel sneller",
            "de ogen kwamen lager bij de grond",
            "het skelet werd veel lichter",
        ],
        antwoord=0,
        uitleg="Met vrije handen kon je voedsel, jongen en later werktuigen dragen. Je kijkt bovendien verder over hoog gras.",
    ),
    dict(
        type="waarofniet",
        vraag="Homo neanderthalensis en Homo sapiens hebben een tijd naast elkaar geleefd.",
        antwoord=True,
        uitleg="In Europa overlapten ze duizenden jaren, en er is zelfs vermenging geweest: in het DNA van veel mensen zit een klein stukje neanderthaler.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten horen bij de menselijke evolutie? Er zijn er drie.",
        opties=[
            "Australopithecus",
            "Homo habilis",
            "Homo erectus",
            "Archaeopteryx",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie horen in de rij van onze voorouders en verwanten. Archaeopteryx is een overgangsvorm tussen reptielen en vogels en staat in een heel andere tak.",
    ),
    dict(
        type="waarofniet",
        vraag="Biodiversiteit gaat alleen over het aantal soorten, niet over de variatie binnen een soort.",
        antwoord=False,
        uitleg="Allebei horen erbij. Naast het aantal soorten telt ook de genetische variatie binnen elke soort, want juist die maakt een populatie veerkrachtig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maakt een kleine populatie een soort kwetsbaar?",
        opties=[
            "er is weinig variatie om op terug te vallen",
            "de dieren worden er kleiner door",
            "er ontstaan meer mutaties dan normaal",
            "de dieren krijgen er minder jongen door",
        ],
        antwoord=0,
        uitleg="Met weinig individuen is er weinig genetische variatie. Komt er een ziekte of een verandering, dan is de kans klein dat iemand toevallig past.",
    ),
]
