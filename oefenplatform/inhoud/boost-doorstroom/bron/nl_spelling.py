# -*- coding: utf-8 -*-
"""De vragen voor "Spelling, leestekens en klanken" (🚀 Boost doorstroom, Nederlands).

Uit het orthografisch en het fonologisch domein van allebei de vakfiches:
spelling van frequente en minder frequente woorden, ook met veranderlijk
woordbeeld, hoofdletters, de interpunctietekens, de diakritische tekens en de
uitspraaktekens, en daarnaast klinkers en medeklinkers, lange, korte en doffe
klanken, het onderscheid tussen klank- en schriftbeeld, en intonatie.

Deel 1 is de spelling. Deel 2 zijn de leestekens en de klanken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met een woord met een veranderlijk woordbeeld?",
        opties=[
            "een woord waarvan de letters veranderen in een andere vorm, zoals huis en huizen",
            "een woord dat je op twee manieren mag spellen",
            "een woord dat in de loop der eeuwen van betekenis veranderd is",
            "een woord dat zowel enkelvoud als meervoud kan zijn",
        ],
        antwoord=0,
        uitleg="De s wordt een z, de f wordt een v. Je hoort het verschil, en je schrijft het ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke woorden verandert het woordbeeld als je er een meervoud van maakt?",
        opties=["huis", "brief", "graf", "boek"],
        antwoord=[0, 1, 2],
        uitleg="Huizen, brieven, graven. Bij boeken blijft de k gewoon staan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de twee puntjes op de i in 'ruïne'?",
        antwoord=["trema", "een trema", "het trema"],
        uitleg="Een trema zegt: begin hier een nieuwe klank. Zonder trema zou je 'rui' lezen als één klank.",
    ),
    dict(
        type="waarofniet",
        vraag="Namen van talen krijgen in het Nederlands een hoofdletter.",
        antwoord=True,
        uitleg="Hij spreekt Frans, zij studeert Nederlands. De taalnaam is afgeleid van een aardrijkskundige naam en houdt de hoofdletter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin gebruikt de hoofdletters correct?",
        opties=[
            "In januari leert hij Spaans in Madrid.",
            "In Januari leert hij spaans in Madrid.",
            "In januari leert hij spaans in madrid.",
            "In Januari leert hij Spaans in madrid.",
        ],
        antwoord=0,
        uitleg="Maanden krijgen geen hoofdletter, taalnamen en plaatsnamen wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'zee-eend' met een koppelteken?",
        opties=[
            "om te vermijden dat je drie e's achter elkaar leest",
            "omdat samenstellingen altijd een koppelteken krijgen",
            "omdat het een leenwoord uit het Duits is",
            "omdat het woord uit drie delen bestaat",
        ],
        antwoord=0,
        uitleg="Bij klinkerbotsing zet je een koppelteken: na-apen, auto-ongeval, zee-eend.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het teken in 'Anna's fiets'?",
        antwoord=["apostrof", "een apostrof", "weglatingsteken"],
        uitleg="De apostrof houdt de klank van de a open. Zonder apostrof zou je 'Annas' lezen met een korte a.",
    ),
    dict(
        type="waarofniet",
        vraag="Het accentteken in 'één' dient om nadruk te leggen.",
        antwoord=True,
        uitleg="'Ik heb één boek' betekent iets anders dan 'ik heb een boek'. Accenttekens zijn uitspraaktekens.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke woorden staat terecht een trema?",
        opties=["ruïne", "reünie", "zeeën", "zee-eend"],
        antwoord=[0, 1, 2],
        uitleg="Binnen één woorddeel gebruik je een trema. Tussen twee delen van een samenstelling een koppelteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'Er is iets gebeurd' maar 'Er gebeurt iets'?",
        opties=[
            "het eerste is een voltooid deelwoord, het tweede een persoonsvorm",
            "het eerste staat in de verleden tijd, het tweede in de toekomende",
            "het eerste hoort bij een meervoud, het tweede bij een enkelvoud",
            "het eerste is een bijvoeglijk naamwoord geworden",
        ],
        antwoord=0,
        uitleg="Het voltooid deelwoord volgt de regel van het hele werkwoord (gebeuren, dus -d). De persoonsvorm krijgt stam plus t.",
    ),
    dict(
        type="waarofniet",
        vraag="De namen van de dagen en de maanden krijgen in het Nederlands een hoofdletter.",
        antwoord=False,
        uitleg="Maandag en januari schrijf je klein. Feestdagen zoals Kerstmis en Pasen krijgen wel een hoofdletter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de juiste verleden tijd van 'bereiden'?",
        opties=[
            "ik bereidde",
            "ik bereide",
            "ik bereidte",
            "ik bereid",
        ],
        antwoord=0,
        uitleg="De stam is 'bereid' en eindigt op d. Daar komt -de bij, dus krijg je twee keer d.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je tekens als het trema, het koppelteken en de apostrof samen?",
        antwoord=["diakritische tekens", "diakritisch", "diakritische"],
        uitleg="Ze veranderen niet de letter zelf maar zeggen hoe je hem moet lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke zin staan de hoofdletters juist?",
        opties=[
            "Met Pasen gaan we naar de Ardennen.",
            "Met pasen gaan we naar de ardennen.",
            "Met Pasen gaan we naar de ardennen.",
            "Met pasen gaan we naar de Ardennen.",
        ],
        antwoord=0,
        uitleg="Feestdagen en aardrijkskundige namen krijgen allebei een hoofdletter.",
    ),
    dict(
        type="waarofniet",
        vraag="'Ik heb me verheugd' en 'ik heb me verheugt' zijn allebei mogelijke schrijfwijzen.",
        antwoord=False,
        uitleg="Na 'heb' staat een voltooid deelwoord, en dat volgt het hele werkwoord verheugen. Dus met een d.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke schrijfwijze is correct?",
        opties=["'s morgens", "s' morgens", "smorgens", "'smorgens"],
        antwoord=0,
        uitleg="De apostrof vervangt de weggelaten letters van het oude 'des'. Er hoort een spatie na.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden krijgen een hoofdletter?",
        opties=["Nederlands", "België", "Kerstmis", "woensdag"],
        antwoord=[0, 1, 2],
        uitleg="Talen, landen en feestdagen wel; dagen van de week niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'geëerd' met een trema?",
        opties=[
            "omdat je anders 'gee' als één klank zou lezen",
            "omdat elk voltooid deelwoord een trema krijgt",
            "omdat het woord uit twee delen bestaat",
            "omdat de klemtoon op de tweede e valt",
        ],
        antwoord=0,
        uitleg="Het trema splitst de klank: ge-eerd. Dezelfde reden als bij zeeën en knieën.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verleden tijd van 'verhuizen' is correct?",
        opties=["verhuisde", "verhuiste", "verhuizde", "verhuizte"],
        antwoord=0,
        uitleg="De stam eindigt op een z, en die hoort niet bij 't kofschip, dus komt er -de bij. Aan het eind van een lettergreep schrijf je die z als s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer schrijf je een werkwoordsvorm met -dt?",
        opties=[
            "bij de derde persoon enkelvoud van een stam die op d eindigt",
            "bij elke verleden tijd van een sterk werkwoord",
            "bij elk voltooid deelwoord met ge- ervoor",
            "bij de gebiedende wijs van een zwak werkwoord",
        ],
        antwoord=0,
        uitleg="Stam word plus uitgang t geeft 'wordt'. Bij 'ik word' komt er geen t bij, en na 'word jij' valt hij weg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een dubbele punt?",
        opties=[
            "om een opsomming, een verklaring of een citaat aan te kondigen",
            "om een zin definitief af te sluiten",
            "om een tussenzin aan beide kanten af te bakenen",
            "om aan te geven dat een zin onafgemaakt blijft",
        ],
        antwoord=0,
        uitleg="Na de dubbele punt komt wat je zonet aangekondigd hebt. Daarom mag er nooit niets op volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze tekens zijn interpunctietekens?",
        opties=["het beletselteken", "het gedachtestreepje", "het aanhalingsteken", "het accentteken"],
        antwoord=[0, 1, 2],
        uitleg="Een accentteken is een uitspraakteken, geen leesteken. De fiche zet die twee bewust in aparte lijstjes.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de drie puntjes waarmee je een zin onafgemaakt laat?",
        antwoord=["beletselteken", "het beletselteken"],
        uitleg="Het laat de lezer zelf aanvullen, of geeft aarzeling weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een komma kan de betekenis van een zin veranderen.",
        antwoord=True,
        uitleg="Vergelijk 'We eten, oma' met 'We eten oma'. Hetzelfde geldt voor 'Hij kwam niet, omdat het regende'.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke zin staat de komma correct?",
        opties=[
            "Toen de bel ging, stond iedereen op.",
            "Toen de bel ging stond iedereen, op.",
            "Toen, de bel ging stond iedereen op.",
            "Toen de bel, ging stond iedereen op.",
        ],
        antwoord=0,
        uitleg="De komma scheidt de bijzin van de hoofdzin. Binnen een zinsdeel hoort er geen komma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een gedachtestreepje?",
        opties=[
            "om een tussenzin of een onderbreking aan te geven",
            "om twee woorden tot één samenstelling te maken",
            "om aan te geven dat een woord afgebroken wordt",
            "om een letterlijk citaat aan te kondigen",
        ],
        antwoord=0,
        uitleg="Het gedachtestreepje is langer dan een koppelteken en zet iets tussen haakjes zonder haakjes te gebruiken.",
    ),
    dict(
        type="invultekst",
        vraag="Welke leestekens zet je rond de letterlijke woorden van iemand anders?",
        antwoord=["aanhalingstekens", "aanhalingsteken", "dubbele aanhalingstekens"],
        uitleg="Wat erbinnen staat, is precies wat er gezegd of geschreven werd. Verander je er iets aan, dan mogen ze er niet meer staan.",
    ),
    dict(
        type="waarofniet",
        vraag="De spatie is volgens de vakfiche ook een interpunctieteken.",
        antwoord=True,
        uitleg="Ze staat uitdrukkelijk in de lijst. Een spatie te veel of te weinig verandert 'een bejaarden tehuis' in iets anders dan 'een bejaardentehuis'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze letters zijn klinkers?",
        opties=["a", "e", "u", "r"],
        antwoord=[0, 1, 2],
        uitleg="Het Nederlands heeft zes klinkerletters: a, e, i, o, u en y. Alle andere zijn medeklinkers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een doffe klank?",
        opties=[
            "de onbeklemtoonde e, zoals in 'de' en in de laatste lettergreep van 'lopen'",
            "een klinker die je extra lang aanhoudt",
            "een medeklinker die je nauwelijks hoort",
            "de klank van twee klinkers na elkaar",
        ],
        antwoord=0,
        uitleg="Je hoort hem in bijna elk Nederlands woord van meer dan één lettergreep, en hij draagt nooit de klemtoon.",
    ),
    dict(
        type="waarofniet",
        vraag="In 'boot' staat een korte klinker.",
        antwoord=False,
        uitleg="De oo is lang. In 'bot' staat de korte o. Daarom schrijf je de lange klank in een gesloten lettergreep met twee letters.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met het verschil tussen klankbeeld en schriftbeeld?",
        opties=[
            "hoe een woord klinkt tegenover hoe je het schrijft",
            "hoe luid je een woord uitspreekt",
            "of een woord uit één of uit meer lettergrepen bestaat",
            "of een woord een klinker of een medeklinker vooraan heeft",
        ],
        antwoord=0,
        uitleg="In 'maan' hoor je drie klanken maar zie je vier letters. In 'hij' hoor je er twee en zie je er drie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de e-klank in 'de' en in de laatste lettergreep van 'lopen'?",
        antwoord=["doffe klank", "de doffe e", "doffe e"],
        uitleg="Hij is nooit beklemtoond, en daarom hoor je hem amper terwijl hij overal zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient intonatie?",
        opties=[
            "om betekenis en gevoel mee te geven aan dezelfde woorden",
            "om de spelling van een woord vast te leggen",
            "om het aantal lettergrepen te bepalen",
            "om klinkers van medeklinkers te onderscheiden",
        ],
        antwoord=0,
        uitleg="'Je komt mee' kan een mededeling, een vraag of een bevel zijn. Alleen de toon maakt het verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="Achter een indirecte vraag zoals 'Hij vroeg of ik meekwam' hoort een vraagteken.",
        antwoord=False,
        uitleg="Er wordt niets gevraagd, er wordt verteld dát er iets gevraagd werd. Dus komt er een punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke zin staan de aanhalingstekens correct?",
        opties=[
            "Hij zei: “Ik kom morgen.”",
            "Hij zei dat: “hij morgen zou komen.”",
            "Hij zei “dat hij morgen kwam” volgens mij.",
            "Hij zei: ik kom “morgen”.",
        ],
        antwoord=0,
        uitleg="Aanhalingstekens staan rond de letterlijke woorden, aangekondigd door een dubbele punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor kan je een dubbele punt gebruiken?",
        opties=[
            "een opsomming aankondigen",
            "een verklaring inleiden",
            "een citaat aankondigen",
            "een zin afsluiten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Afsluiten doet een punt, een vraagteken of een uitroepteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de klinker in 'maan' en die in 'man'?",
        opties=[
            "de eerste is lang, de tweede kort",
            "de eerste is dof, de tweede beklemtoond",
            "de eerste is een medeklinker, de tweede een klinker",
            "de eerste staat in een open lettergreep, de tweede in een gesloten",
        ],
        antwoord=0,
        uitleg="Allebei de lettergrepen zijn gesloten. Daarom moet de lange klank met twee letters geschreven worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er een komma in 'Hoewel het goot, gingen we toch buiten spelen'?",
        opties=[
            "om de bijzin van de hoofdzin te scheiden",
            "om een opsomming aan te kondigen",
            "om een citaat in te leiden",
            "om aan te geven dat de zin onaf is",
        ],
        antwoord=0,
        uitleg="Staat de bijzin vooraan, dan komt er een komma voor de hoofdzin begint. Dat maakt de zin in één keer leesbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je van 'Je komt mee' hoorbaar een vraag, zonder de woorden te veranderen?",
        opties=[
            "door de toon aan het einde omhoog te laten gaan",
            "door trager te spreken",
            "door de klemtoon op het eerste woord te leggen",
            "door een pauze in het midden te laten vallen",
        ],
        antwoord=0,
        uitleg="Dat is intonatie. In geschreven taal moet een vraagteken dat werk overnemen.",
    ),
]
