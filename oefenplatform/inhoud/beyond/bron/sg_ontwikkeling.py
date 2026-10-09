# -*- coding: utf-8 -*-
"""Ontwikkelingspsychologie: de begrippen en de drie basisvragen.

Het eerste thema van het grootste blok. Gedragswetenschappen weegt vijfenzestig
procent van het examen, en ontwikkelingspsychologie is daarvan het eerste
onderdeel. Dit thema legt het gereedschap klaar dat in de drie volgende
thema's bij elke benadering terugkomt.

De fiche is hier heel precies over de lijstjes, en die staan hieronder
letterlijk:

    ontwikkeling = groeien + rijpen + leren
    negen levensloopfasen: prenatale fase, babytijd, peutertijd, vroege
        kindertijd (kleutertijd), midden kindertijd (lagere schoolkindfase),
        adolescentie, vroege volwassenheid, midden volwassenheid, late
        volwassenheid
    vijf ontwikkelingsdomeinen: fysieke, cognitieve, morele,
        socio-emotionele en persoonlijkheidsontwikkeling
    drie basisvragen: continu of discontinu? nature, nurture of
        zelfbepaling? cultureel bepaald of universeel?

Deel 1 is wat ontwikkeling is en in welke fase iemand zit.
Deel 2 zijn de vijf domeinen en de drie basisvragen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke drie dingen samen bestaat ontwikkeling volgens de vakfiche?",
        opties=[
            "groeien, rijpen en leren",
            "groeien, oefenen en herhalen",
            "erven, rijpen en nadoen",
            "leren, oefenen en onthouden",
        ],
        antwoord=0,
        uitleg="De fiche vat ontwikkeling samen als een combinatie van groeien, rijpen en leren. Die drie woorden komen bij elke benadering terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Nora is in een jaar zeven centimeter langer geworden en haar voeten zijn twee maten gegroeid. Welk deel van ontwikkeling is dit?",
        opties=[
            "groeien",
            "rijpen",
            "leren",
            "zelfbepaling",
        ],
        antwoord=0,
        uitleg="Groeien is de zichtbare toename in lengte, gewicht en omvang van het lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een baby van zes maanden kan nog niet stappen, hoeveel je ook oefent: de zenuwbanen naar de benen zijn nog niet klaar. Welk deel van ontwikkeling is dit?",
        opties=[
            "rijpen",
            "groeien",
            "leren",
            "fixatie",
        ],
        antwoord=0,
        uitleg="Rijpen is de ontwikkeling die van binnenuit komt en een vaste orde volgt. Oefenen versnelt ze niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jonas kende de tafel van zeven niet en kent ze nu wel, na drie weken elke dag oefenen. Welk deel van ontwikkeling is dit?",
        opties=[
            "leren",
            "rijpen",
            "groeien",
            "nature",
        ],
        antwoord=0,
        uitleg="Leren is de verandering die door ervaring en oefening komt, niet door het lichaam zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen rijpen en leren?",
        opties=[
            "rijpen komt van binnenuit, leren komt door ervaring",
            "rijpen komt door ervaring, leren komt van binnenuit",
            "rijpen gaat over het lichaam, leren gaat over de lengte",
            "rijpen gebeurt bij kinderen, leren pas bij volwassenen",
        ],
        antwoord=0,
        uitleg="Rijpen is biologisch en volgt een vaste orde. Leren hangt af van wat iemand meemaakt en oefent.",
    ),
    dict(
        type="invultekst",
        vraag="Het Engelse woord uit de fiche voor de erfelijke kant van ontwikkeling, dus alles wat in je genen zit, is ...",
        antwoord=["nature"],
        uitleg="Nature staat voor de genetische factoren. Nurture staat tegenover nature en betekent alles wat de omgeving aanbrengt.",
    ),
    dict(
        type="invultekst",
        vraag="Het Engelse woord uit de fiche voor alles wat de omgeving aanbrengt, dus opvoeding, school en vrienden, is ...",
        antwoord=["nurture"],
        uitleg="Nurture is de omgevingskant. De fiche zet nature en nurture altijd naast elkaar, nooit tegen elkaar alleen.",
    ),
    dict(
        type="waarofniet",
        vraag="Rijpen kan je versnellen door een kind veel te laten oefenen.",
        antwoord=False,
        uitleg="Niet waar. Rijpen volgt een eigen orde. Een kind van tien maanden leert niet stappen omdat je meer oefent, maar omdat zijn lichaam er klaar voor is.",
    ),
    dict(
        type="waarofniet",
        vraag="Groeien en rijpen horen bij nature, leren hoort bij nurture.",
        antwoord=True,
        uitleg="Waar. Dat is precies het verband dat de fiche vraagt: groeien en rijpen komen van binnenuit, leren komt van buitenaf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel levensloopfasen noemt de vakfiche?",
        opties=[
            "negen",
            "vijf",
            "zeven",
            "twaalf",
        ],
        antwoord=0,
        uitleg="Negen, van de prenatale fase tot de late volwassenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke levensloopfase komt in de fiche vlak na de babytijd?",
        opties=[
            "de peutertijd",
            "de kleutertijd",
            "de prenatale fase",
            "de adolescentie",
        ],
        antwoord=0,
        uitleg="De orde is: prenatale fase, babytijd, peutertijd, kleutertijd, lagere schoolkindfase, adolescentie, en dan de drie fasen van volwassenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Amira zit in het vierde leerjaar. In welke levensloopfase zit ze volgens de fiche?",
        opties=[
            "de midden kindertijd",
            "de vroege kindertijd",
            "de adolescentie",
            "de peutertijd",
        ],
        antwoord=0,
        uitleg="De midden kindertijd heet in de fiche ook de lagere schoolkindfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke naam gebruikt de fiche nog voor de vroege kindertijd?",
        opties=[
            "de kleutertijd",
            "de peutertijd",
            "de babytijd",
            "de schooltijd",
        ],
        antwoord=0,
        uitleg="De fiche zet er zelf twee namen bij: vroege kindertijd is de kleutertijd, midden kindertijd is de lagere schoolkindfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze fasen zitten volgens de fiche alle drie bij de volwassenheid?",
        opties=[
            "vroege volwassenheid",
            "midden volwassenheid",
            "late volwassenheid",
            "adolescentie",
            "midden kindertijd",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche splitst de volwassenheid in drie: vroege, midden en late volwassenheid. De adolescentie komt ervoor.",
    ),
    dict(
        type="invultekst",
        vraag="De fase voor de geboorte heet in de fiche de ... fase.",
        antwoord=["prenatale", "prenatale fase"],
        uitleg="De prenatale fase is de eerste van de negen. Ontwikkeling begint dus al voor de geboorte.",
    ),
    dict(
        type="waarofniet",
        vraag="De adolescentie komt in de fiche na de midden kindertijd en voor de vroege volwassenheid.",
        antwoord=True,
        uitleg="Waar. De adolescentie zit precies tussen de lagere schoolkindfase en de vroege volwassenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de fiche stopt de ontwikkeling van een mens bij het einde van de adolescentie.",
        antwoord=False,
        uitleg="Niet waar. Er komen nog drie fasen na: vroege, midden en late volwassenheid. Ontwikkeling loopt over de hele levensloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom spreekt de fiche van levensloopfasen en niet alleen van kinderfasen?",
        opties=[
            "omdat een mens zich tot het einde van zijn leven ontwikkelt",
            "omdat elke fase precies even lang duurt bij iedereen",
            "omdat kinderen zich sneller ontwikkelen dan volwassenen",
            "omdat alleen de eerste fasen met rijpen te maken hebben",
        ],
        antwoord=0,
        uitleg="De negen fasen lopen van voor de geboorte tot de late volwassenheid. Ontwikkeling is er in elke fase, ook op latere leeftijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Elias van drie jaar wil alles zelf doen en zegt voortdurend nee. In welke levensloopfase zit hij?",
        opties=[
            "de peutertijd",
            "de babytijd",
            "de midden kindertijd",
            "de vroege volwassenheid",
        ],
        antwoord=0,
        uitleg="Drie jaar valt in de peutertijd, de derde van de negen fasen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerkracht zegt: dit kind kan nog niet op één been staan, maar dat komt. Waarop rekent zij?",
        opties=[
            "op het rijpen van zijn evenwicht",
            "op het groeien van zijn benen",
            "op het leren van een nieuw woord",
            "op de invloed van zijn klasgroep",
        ],
        antwoord=0,
        uitleg="Op één been staan hangt af van evenwicht, en dat rijpt. Het komt op zijn tijd, ook zonder extra oefenen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel ontwikkelingsdomeinen noemt de vakfiche?",
        opties=[
            "vijf",
            "drie",
            "negen",
            "zeven",
        ],
        antwoord=0,
        uitleg="Vijf: de fysieke, de cognitieve, de morele, de socio-emotionele en de persoonlijkheidsontwikkeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hanne kan nu zelf haar veters knopen. Bij welk ontwikkelingsdomein hoort dat vooral?",
        opties=[
            "de fysieke ontwikkeling",
            "de morele ontwikkeling",
            "de cognitieve ontwikkeling",
            "de socio-emotionele ontwikkeling",
        ],
        antwoord=0,
        uitleg="Veters knopen vraagt fijne motoriek, en motoriek hoort bij de fysieke ontwikkeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sam kan uitleggen waarom spieken niet eerlijk is tegenover wie wel geleerd heeft. Bij welk domein hoort dat vooral?",
        opties=[
            "de morele ontwikkeling",
            "de cognitieve ontwikkeling",
            "de fysieke ontwikkeling",
            "de persoonlijkheidsontwikkeling",
        ],
        antwoord=0,
        uitleg="Nadenken over goed en kwaad en over eerlijkheid hoort bij de morele ontwikkeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Lotte kan sinds kort haar boosheid in woorden zeggen in plaats van te slaan. Bij welk domein hoort dat vooral?",
        opties=[
            "de socio-emotionele ontwikkeling",
            "de fysieke ontwikkeling",
            "de morele ontwikkeling",
            "de cognitieve ontwikkeling",
        ],
        antwoord=0,
        uitleg="Omgaan met je eigen gevoelens en met anderen hoort bij de socio-emotionele ontwikkeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind van zeven kan voor het eerst een som in zijn hoofd maken. Bij welk domein hoort dat vooral?",
        opties=[
            "de cognitieve ontwikkeling",
            "de morele ontwikkeling",
            "de fysieke ontwikkeling",
            "de socio-emotionele ontwikkeling",
        ],
        antwoord=0,
        uitleg="Denken, onthouden, rekenen en taal horen bij de cognitieve ontwikkeling.",
    ),
    dict(
        type="invultekst",
        vraag="Het vijfde domein, naast het fysieke, het cognitieve, het morele en het socio-emotionele, is de ...ontwikkeling.",
        antwoord=["persoonlijkheids", "persoonlijkheidsontwikkeling"],
        uitleg="De persoonlijkheidsontwikkeling is het vijfde domein. Ze gaat over wie iemand wordt als persoon.",
    ),
    dict(
        type="waarofniet",
        vraag="De vijf ontwikkelingsdomeinen staan los van elkaar: wat in het ene domein gebeurt, heeft geen gevolgen in een ander.",
        antwoord=False,
        uitleg="Niet waar. De fiche vraagt juist naar de wisselwerking. Wie moeilijk stapt, speelt minder mee, en dat raakt het socio-emotionele domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan één ontwikkelingsdomein door verschillende levensloopfasen heen volgen en de fasen zo met elkaar vergelijken.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt dat met zoveel woorden: vergelijk levensloopfasen met elkaar binnen één domein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tim stottert en durft daardoor niets meer te zeggen in de klas, waardoor hij minder vrienden maakt. Welke twee domeinen beïnvloeden elkaar hier?",
        opties=[
            "het fysieke domein",
            "het socio-emotionele domein",
            "het morele domein",
            "het cognitieve domein",
        ],
        antwoord=[0, 1],
        uitleg="Stotteren zit in het fysieke domein, minder vrienden maken in het socio-emotionele. Dat is wisselwerking tussen domeinen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel basisvragen stelt de ontwikkelingspsychologie volgens de fiche?",
        opties=[
            "drie",
            "twee",
            "vier",
            "vijf",
        ],
        antwoord=0,
        uitleg="Drie: continu of discontinu, de rol van nature, nurture en zelfbepaling, en cultureel of universeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke basisvraag gaat over de vraag of ontwikkeling in sprongen gaat of beetje bij beetje?",
        opties=[
            "continuïteit of discontinuïteit",
            "nature of nurture",
            "cultureel of universeel",
            "groeien of rijpen",
        ],
        antwoord=0,
        uitleg="Continu betekent beetje bij beetje, discontinu betekent in duidelijke sprongen of stadia.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een theorie zegt dat elk kind vier vaste stadia doorloopt en bij elke overgang anders begint te denken. Welk antwoord geeft die theorie op de eerste basisvraag?",
        opties=[
            "ontwikkeling verloopt discontinu",
            "ontwikkeling verloopt continu",
            "ontwikkeling is cultureel bepaald",
            "ontwikkeling hangt af van nurture",
        ],
        antwoord=0,
        uitleg="Vaste stadia met duidelijke overgangen horen bij discontinuïteit. Een theorie van langzaam bijleren hoort bij continuïteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk begrip staat in de tweede basisvraag naast nature en nurture?",
        opties=[
            "zelfbepaling",
            "zelfbeeld",
            "zelfvertrouwen",
            "zelfstandigheid",
        ],
        antwoord=0,
        uitleg="De fiche noemt drie dingen: genetische factoren, omgevingsfactoren en zelfbepaling. Een mens kiest ook zelf mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Yara komt uit een muzikaal gezin, zat van haar zesde in de muziekschool en koos op haar vijftiende zelf om drum te spelen in plaats van piano. Welke drie dingen uit de tweede basisvraag zie je?",
        opties=[
            "nature",
            "nurture",
            "zelfbepaling",
            "discontinuïteit",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het muzikale gezin is nature en nurture samen, de muziekschool is nurture, en haar eigen keuze is zelfbepaling.",
    ),
    dict(
        type="invultekst",
        vraag="De derde basisvraag zet culturele factoren naast ... factoren, die voor alle mensen gelijk zijn.",
        antwoord=["universele", "universeel"],
        uitleg="Universele factoren gelden overal ter wereld. Culturele factoren verschillen van samenleving tot samenleving.",
    ),
    dict(
        type="waarofniet",
        vraag="Dat baby's over de hele wereld eerst kruipen en dan stappen, is een aanwijzing voor een universele factor.",
        antwoord=True,
        uitleg="Waar. Wat in elke cultuur in dezelfde orde gebeurt, wijst op iets universeels.",
    ),
    dict(
        type="waarofniet",
        vraag="Op welke leeftijd een kind geacht wordt zelf te beslissen, is een universele factor.",
        antwoord=False,
        uitleg="Niet waar. Dat verschilt sterk van samenleving tot samenleving, dus het is een culturele factor.",
    ),
    dict(
        type="invultekst",
        vraag="Ontwikkeling die beetje bij beetje verloopt, zonder duidelijke sprongen, heet ...",
        antwoord=["continu", "continue", "continuïteit"],
        uitleg="Continu betekent vloeiend verder. Discontinu betekent dat er duidelijke stadia zijn met een overgang ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche om elke benadering aan de drie basisvragen te toetsen?",
        opties=[
            "omdat je theorieën zo met elkaar kan vergelijken",
            "omdat elke theorie op de drie vragen hetzelfde antwoordt",
            "omdat de basisvragen alleen bij kinderen van toepassing zijn",
            "omdat je anders de levensloopfasen niet kan benoemen",
        ],
        antwoord=0,
        uitleg="De drie basisvragen zijn een meetlat. Leg je ze bij Freud, bij Skinner en bij Vygotsky, dan zie je waar hun theorieën verschillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker toont dat kinderen met dezelfde genen anders opgroeien in een ander gezin. Welke basisvraag onderzoekt hij?",
        opties=[
            "de rol van nature, nurture en zelfbepaling",
            "continuïteit of discontinuïteit",
            "cultureel bepaald of universeel",
            "groeien, rijpen of leren",
        ],
        antwoord=0,
        uitleg="Zelfde genen, ander gezin, ander resultaat: dat zet nature en nurture naast elkaar, de tweede basisvraag.",
    ),
]
