# -*- coding: utf-8 -*-
"""Liberalisme en nationalisme.

Uit de leerinhoud "liberalisme en nationalisme" van de vakfiche geschiedenis,
3 dubbele finaliteit: de opkomst en de ideeën van het liberalisme, en de
opkomst en de ideeën van het nationalisme.

Dit zijn de twee ideologieën die het Congres van Wenen wilde tegenhouden en die
in 1830 en 1848 toch de bovenhand haalden. Het thema staat dus tussen het
congres en het ontstaan van België.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat bij het liberalisme centraal?",
        opties=[
            "de vrijheid en de rechten van het individu",
            "de macht en de rijkdom van de kerk",
            "de gehoorzaamheid van het volk aan de vorst",
            "het bezit van de grond door de boeren",
        ],
        antwoord=0,
        uitleg="Het woord komt van liber, het Latijn voor vrij. De burger moet vrij zijn van willekeur van de staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vrijheden eisten de liberalen in de negentiende eeuw?",
        opties=[
            "de vrijheid van meningsuiting en van pers",
            "de vrijheid van vereniging en van godsdienst",
            "de vrijheid om geen belasting te betalen",
            "de vrijheid om zelf wetten uit te vaardigen",
        ],
        antwoord=[0, 1],
        uitleg="Belastingen afschaffen en zelf wetten maken stond nergens in hun eisen: daarvoor is er een parlement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de scheiding der machten?",
        opties=[
            "wetgeven, besturen en rechtspreken liggen in verschillende handen",
            "de kerk en de staat worden in alles volledig van elkaar gescheiden",
            "het land wordt in gewesten, gemeenschappen en provincies verdeeld",
            "de koning en de koningin regeren elk een deel van het land apart",
        ],
        antwoord=0,
        uitleg="Zo kan de ene macht de andere in het oog houden. Het idee komt van Montesquieu, uit de achttiende eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wilden de liberalen een grondwet?",
        opties=[
            "om de macht van de vorst aan vaste regels te binden",
            "om de belastingen voor de armen te kunnen verlagen",
            "om de kerk het onderwijs volledig te laten inrichten",
            "om de grenzen van het land voorgoed vast te leggen",
        ],
        antwoord=0,
        uitleg="Een grondwet zegt wat de vorst mag en welke rechten de burger heeft. Daar kan geen vorst eenzijdig van afwijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe dachten de liberalen van de negentiende eeuw over het stemrecht?",
        opties=[
            "alleen wie genoeg belasting betaalt, mag kiezen",
            "iedere man en iedere vrouw moet kunnen kiezen",
            "iedere man vanaf achttien jaar moet kunnen kiezen",
            "niemand hoeft te kiezen, de vorst benoemt het parlement",
        ],
        antwoord=0,
        uitleg="Dat heet cijnskiesrecht. Pas veel later, onder druk van de arbeidersbeweging, kwam het algemeen stemrecht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het stemrecht dat enkel geldt voor wie genoeg belasting betaalt?",
        antwoord=["cijnskiesrecht", "het cijnskiesrecht"],
        uitleg="De cijns is de belasting. Wie te weinig betaalde, mocht niet stemmen, hoe geschikt hij ook was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met economisch liberalisme?",
        opties=[
            "de overheid laat de economie zoveel mogelijk aan zichzelf over",
            "de overheid bepaalt zelf de prijzen van alle goederen en diensten",
            "de overheid wordt eigenaar van alle fabrieken, mijnen en spoorwegen",
            "de overheid verdeelt de winst onder alle mensen die werken in het land",
        ],
        antwoord=0,
        uitleg="Vraag en aanbod moeten hun werk doen. Die houding wordt ook laissez-faire genoemd, laat maar doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol gaven de economische liberalen aan de staat?",
        opties=[
            "een beperkte rol: orde, recht en veiligheid bewaken",
            "een leidende rol: de hele productie plannen en verdelen",
            "een zorgende rol: voor iedere werkloze een uitkering",
            "een afwezige rol: de staat moest helemaal verdwijnen",
        ],
        antwoord=0,
        uitleg="Dat idee wordt soms de nachtwachtstaat genoemd: de staat houdt de wacht, en voor de rest blijft hij erbuiten.",
    ),
    dict(
        type="waarofniet",
        vraag="De liberalen van de negentiende eeuw waren voor het algemeen enkelvoudig stemrecht.",
        antwoord=False,
        uitleg="Zij wilden het cijnskiesrecht: stemrecht voor wie bezit had. Het algemeen stemrecht was een eis van de arbeidersbeweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Het liberalisme kwam vooral op bij de gegoede burgerij.",
        antwoord=True,
        uitleg="Handelaars, fabrikanten en vrije beroepen hadden bezit en kennis, maar geen politieke macht. Die wilden ze erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een liberaal uit 1830 vond dat de staat de lonen in de fabrieken moest vastleggen.",
        antwoord=False,
        uitleg="Dat was voor hem precies verkeerde inmenging. Loon was een zaak tussen werkgever en werknemer.",
    ),
    dict(
        type="waarofniet",
        vraag="De ideeën van het liberalisme gaan terug op de Verlichting en op de Franse Revolutie.",
        antwoord=True,
        uitleg="Grondrechten, scheiding der machten en gelijkheid voor de wet waren daar al geformuleerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een natie volgens het negentiende-eeuwse nationalisme?",
        opties=[
            "een gemeenschap met een eigen taal, cultuur en geschiedenis",
            "het grondgebied dat een vorst door erfenis gekregen heeft",
            "de verzameling van alle mensen die belasting betalen",
            "een groep landen die samen een handelsverdrag sluiten",
        ],
        antwoord=0,
        uitleg="Een natie hoorde volgens die gedachte een eigen staat te krijgen, en niet omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee vormen kon het nationalisme in de negentiende eeuw aannemen?",
        opties=[
            "het streven naar eenmaking van verdeelde gebieden",
            "het streven naar onafhankelijkheid van een vreemde heerser",
            "het streven naar afschaffing van alle staatsgrenzen",
            "het streven naar één wereldtaal voor alle volken",
        ],
        antwoord=[0, 1],
        uitleg="Duitsland en Italië wilden samenvoegen wat verdeeld was; Griekenland, Polen en België wilden zich losmaken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunststroming voedde het nationalisme met belangstelling voor eigen taal en verleden?",
        opties=[
            "de romantiek",
            "het impressionisme",
            "het kubisme",
            "de abstracte kunst",
        ],
        antwoord=0,
        uitleg="Romantische schrijvers en schilders zochten het eigene op: volksverhalen, de eigen taal, het eigen verleden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het streven van een volk naar een eigen staat?",
        antwoord=["nationalisme", "het nationalisme"],
        uitleg="Het woord komt van natie. Later kreeg het ook een uitsluitende, agressieve betekenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom botste het nationalisme met de beslissingen van het Congres van Wenen?",
        opties=[
            "in Wenen werden grenzen getekend zonder naar de volken te kijken",
            "in Wenen werd het nationalisme uitdrukkelijk verboden bij wet",
            "in Wenen werd beslist dat elk volk een eigen staat zou krijgen",
            "in Wenen werd de Duitse eenmaking al volledig doorgevoerd",
        ],
        antwoord=0,
        uitleg="Het machtsevenwicht ging voor. Volken werden samengevoegd of opgesplitst zoals dat in dat evenwicht paste.",
    ),
    dict(
        type="waarofniet",
        vraag="Het nationalisme en het liberalisme werkten in de negentiende eeuw vaak samen tegen de oude orde.",
        antwoord=True,
        uitleg="Beide wilden af van een vorst die alleen beslist. In 1830 en 1848 stonden ze dan ook samen op de barricaden.",
    ),
    dict(
        type="waarofniet",
        vraag="Nationalisme betekende in de negentiende eeuw altijd vijandigheid tegenover andere volken.",
        antwoord=False,
        uitleg="In het begin was het vooral bevrijdend bedoeld. De uitsluitende en agressieve vorm kwam later, tegen 1900.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een bron uit 1840 een pleidooi voor persvrijheid, een grondwet en stemrecht voor wie bezit heeft. Welke ideologie herken je?",
        opties=[
            "het liberalisme",
            "het nationalisme",
            "het marxisme",
            "de christendemocratie",
        ],
        antwoord=0,
        uitleg="Grondrechten en een grondwet, met cijnskiesrecht erbij, is het liberale programma van die tijd.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het politieke liberalisme kloppen?",
        opties=[
            "de macht van de vorst wordt door een grondwet begrensd",
            "een parlement controleert wat de regering doet",
            "de koning benoemt zelf alle rechters en journalisten",
            "de kerk beslist wie er mag kiezen en wie niet",
        ],
        antwoord=[0, 1],
        uitleg="Juist het omgekeerde van de laatste twee: rechters en pers moesten vrij zijn van de koning en van de kerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen het liberalisme en de industrialisering?",
        opties=[
            "het economisch liberalisme gaf de fabrikanten de vrije hand",
            "het liberalisme verbood het gebruik van stoommachines",
            "het liberalisme maakte de fabrieken eigendom van de staat",
            "het liberalisme legde de werkdag op acht uren vast",
        ],
        antwoord=0,
        uitleg="Zonder regels over lonen, uren of kinderarbeid konden de fabrieken snel groeien, en dat is ook wat gebeurde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had het economisch liberalisme voor de arbeiders?",
        opties=[
            "lange werkdagen en lage lonen zonder bescherming",
            "een gegarandeerd minimumloon voor elk beroep",
            "een vaste werkweek van vijf dagen met vakantie",
            "een uitkering van de staat bij ziekte of ongeval",
        ],
        antwoord=0,
        uitleg="De staat bleef erbuiten, dus er was niets dat hun arbeidsvoorwaarden begrensde. Daaruit groeide de sociale strijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het nationalisme in de negentiende eeuw kloppen?",
        opties=[
            "een eigen taal gold als een argument voor een eigen staat",
            "het eigen verleden werd als gemeenschappelijke band gebruikt",
            "de godsdienst werd overal als enige band gezien",
            "de economie bepaalde welke natie recht had op een staat",
        ],
        antwoord=[0, 1],
        uitleg="Taal, cultuur en geschiedenis vormden het verhaal van de natie. Geloof speelde soms mee, maar was niet de kern.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein situeer je de eis voor persvrijheid het best?",
        opties=[
            "in het politieke domein, met een culturele kant",
            "uitsluitend in het economische domein van de handel",
            "uitsluitend in het sociale domein van de arbeid",
            "in geen enkel van de maatschappelijke domeinen",
        ],
        antwoord=0,
        uitleg="Het is een grondrecht tegenover de overheid, dus politiek, en het gaat over het vrije woord, dus ook cultureel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men het liberalisme en het nationalisme ideologieën?",
        opties=[
            "het zijn samenhangende stelsels van ideeën over de samenleving",
            "het zijn politieke partijen die in elk land een regering vormden",
            "het zijn wetten die in heel Europa tegelijk van kracht waren",
            "het zijn kunststromingen met hun eigen schilders en dichters",
        ],
        antwoord=0,
        uitleg="Een ideologie zegt hoe de samenleving zou moeten zijn en hoe je daar komt. Daaruit groeien dan partijen.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor een liberaal mocht de vorst zonder parlement belastingen invoeren.",
        antwoord=False,
        uitleg="Over belastingen moest juist het parlement beslissen. Dat was een van de kernpunten van het liberale programma.",
    ),
    dict(
        type="waarofniet",
        vraag="Het liberalisme eiste gelijkheid voor de wet voor alle burgers.",
        antwoord=True,
        uitleg="Voorrechten door geboorte moesten weg. Gelijkheid in bezit of inkomen stond er niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Het nationalisme hield in de Duitse gebieden vooral een streven naar eenmaking in.",
        antwoord=True,
        uitleg="De Duitse Bond was een losse verzameling staten. Nationalisten wilden daar één Duitse staat van maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor Polen en Griekenland betekende nationalisme in de negentiende eeuw hetzelfde als voor Duitsland en Italië.",
        antwoord=False,
        uitleg="Daar ging het om losmaken van een vreemde heerser, niet om samenvoegen van verdeelde gebieden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een liberaal en een nationalist konden in 1830 dezelfde opstand steunen om verschillende redenen.",
        antwoord=True,
        uitleg="De ene wilde grondrechten en een parlement, de andere een eigen staat. Tegen dezelfde vorst kwam dat samen.",
    ),
    dict(
        type="waarofniet",
        vraag="De vorsten van de Heilige Alliantie steunden het liberalisme en het nationalisme.",
        antwoord=False,
        uitleg="Zij deden het omgekeerde: ze beloofden elkaar steun om zulke bewegingen te onderdrukken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de houding dat de overheid de economie zoveel mogelijk aan zichzelf moet overlaten?",
        antwoord=["laissez-faire", "economisch liberalisme", "laisser-faire"],
        uitleg="Letterlijk: laat maar doen. Vraag en aanbod moesten de prijzen en de lonen bepalen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de wet die boven alle andere wetten staat en de rechten van de burger vastlegt?",
        antwoord=["de grondwet", "grondwet"],
        uitleg="Zij bindt ook de vorst en de regering. Voor liberalen was dat de kern van hun eisen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord het beginsel dat wetgeven, besturen en rechtspreken in verschillende handen liggen?",
        antwoord=["machtenscheiding", "de machtenscheiding"],
        uitleg="Het wordt ook de scheiding der machten genoemd. Zo kan niemand alles alleen beslissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een bron uit 1848 die oproept om alle Duitse staten samen te voegen tot één rijk. Welke ideologie herken je?",
        opties=[
            "het nationalisme",
            "het liberalisme",
            "het economisch liberalisme",
            "de christendemocratie",
        ],
        antwoord=0,
        uitleg="Eén staat voor één natie is de kern van het nationalisme. De christendemocratie bestond toen nog niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een bron die pleit voor afschaffing van de invoerrechten op graan. Welke ideologie herken je?",
        opties=[
            "het economisch liberalisme",
            "het romantische nationalisme",
            "de leer van het marxisme",
            "de latere sociaaldemocratie",
        ],
        antwoord=0,
        uitleg="Vrije handel zonder belemmeringen aan de grens is een kernpunt van het economisch liberalisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de opkomst van het liberalisme kloppen?",
        opties=[
            "de burgerij had bezit en kennis, maar weinig politieke macht",
            "de ideeën van de Verlichting lagen eraan ten grondslag",
            "de adel was er de belangrijkste drijvende kracht achter",
            "de arbeiders in de fabrieken waren de eerste liberalen",
        ],
        antwoord=[0, 1],
        uitleg="De adel verloor er juist voorrechten door, en de arbeiders zochten later hun eigen ideologieën.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen het nationalisme en het culturele domein?",
        opties=[
            "taal, verhalen en geschiedenis vormen de band van de natie",
            "de economie van een natie bepaalt haar grenzen",
            "een natie heeft altijd één godsdienst voor alle inwoners",
            "een natie ontstaat enkel door een oorlog te winnen",
        ],
        antwoord=0,
        uitleg="Woordenboeken, volksverhalen en geschiedschrijving waren voor de nationalisten politiek werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bleven de liberale eisen na 1815 een halve eeuw terugkomen?",
        opties=[
            "de restauratie nam de onvrede en de ideeën niet weg",
            "de vorsten hadden de liberalen hun eisen toegezegd",
            "er waren in Europa geen kranten meer om te verbieden",
            "het liberalisme werd overal meteen de staatsideologie",
        ],
        antwoord=0,
        uitleg="Wie onderdrukt wordt, verdwijnt niet. In 1830 en 1848 kwam dezelfde eis telkens opnieuw boven.",
    ),
]
