# -*- coding: utf-8 -*-
"""Nanomaterialen — 🌍 Beyond, chemie.

Deel 1 gaat over wat een nanomateriaal is: de grootteorde, de plaats op een
schaal tussen een atoom en een haar, de indeling in 0D, 1D, 2D en 3D, de twee
manieren om ze te maken (top-down en bottom-up), en de koolstofvormen
buckyball, grafeen en nanobuis. Deel 2 gaat over de eigenschappen die bij die
kleine maat horen en over de toepassingen: de zonnecrème, de antibacteriële
werking, de covidtest en de sterkte van grafeen, met de voor- en nadelen erbij.

De vragen leggen telkens het verband tussen de maat of de structuur en de
eigenschap, want dat is wat een nanomateriaal anders maakt dan dezelfde stof in
het groot.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe groot is een nanometer?",
        opties=[
            "een miljardste van een meter",
            "een miljoenste van een meter",
            "een duizendste van een meter",
            "een biljoenste van een meter",
        ],
        antwoord=0,
        uitleg="Nano staat voor 10⁻⁹. Een nanomateriaal meet ongeveer één tot honderd "
        "nanometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is groter: een nanodeeltje of een menselijke haar?",
        opties=[
            "de haar, en wel duizenden keren",
            "het nanodeeltje, en wel duizenden keren",
            "ze zijn ongeveer even groot",
            "de haar, maar slechts een paar keer",
        ],
        antwoord=0,
        uitleg="Een haar is ongeveer 80 000 nanometer dik. Een atoom is ongeveer een "
        "tiende van een nanometer.",
    ),
    dict(
        type="invultekst",
        vraag="Tussen welke twee grenzen in nanometer ligt een nanomateriaal?",
        antwoord=["1 en 100", "1 tot 100", "1-100"],
        uitleg="Onder één nanometer kom je bij losse atomen en moleculen, erboven bij "
        "gewoon materiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een 0D-nanomateriaal?",
        opties=[
            "een deeltje dat in alle drie de richtingen nanoklein is",
            "een draadje dat in één van de drie richtingen lang is",
            "een laagje dat in twee van de drie richtingen groot is",
            "een blok dat een nanostructuur in zijn binnenkant heeft",
        ],
        antwoord=0,
        uitleg="Een buckyball of een quantumdot is zo'n deeltje. Bij 1D is er één "
        "richting groot, bij 2D twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Grafeen is een 2D-nanomateriaal.",
        antwoord=True,
        uitleg="Het is één laag koolstofatomen in een honingraatpatroon. In de twee "
        "andere richtingen kan zo'n laag heel groot zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuur heeft een koolstofnanobuis?",
        opties=[
            "een opgerolde laag koolstofatomen, dus 1D",
            "een bol van zestig koolstofatomen, dus 0D",
            "een vlakke laag koolstofatomen, dus 2D",
            "een blok van koolstof met nanoporen, dus 3D",
        ],
        antwoord=0,
        uitleg="Je kan zo'n buis zien als opgerold grafeen. Hij is lang in één richting "
        "en nanoklein in de twee andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke koolstofvormen zijn nanomaterialen? Kruis alles aan wat juist is.",
        opties=[
            "grafeen",
            "de buckyball",
            "diamant in een ring",
            "houtskool uit de barbecue",
        ],
        antwoord=[0, 1],
        uitleg="Diamant en houtskool zijn gewone vormen van koolstof. Grafeen en de "
        "buckyball hebben hun bijzondere eigenschappen juist door hun nanomaat.",
    ),
    dict(
        type="invultekst",
        vraag="Uit hoeveel koolstofatomen bestaat de bekendste buckyball?",
        antwoord=["60", "zestig", "C60"],
        uitleg="C₆₀ heeft de vorm van een voetbal, met vijf- en zeshoeken. Daarom heet ze "
        "ook wel voetbalmolecule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bottom-upmethode?",
        opties=[
            "het materiaal opbouwen vanuit losse atomen of moleculen",
            "het materiaal vermalen tot steeds kleinere stukjes",
            "het materiaal wegetsen tot er een patroon overblijft",
            "het materiaal verhitten tot het uit zichzelf smelt",
        ],
        antwoord=0,
        uitleg="Top-down begint bij groot materiaal en haalt er stukken af. Bottom-up "
        "laat de structuur juist vanaf het atoom groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn top-down? Kruis alles aan wat juist is.",
        opties=[
            "een vaste stof fijnmalen tot nanodeeltjes",
            "een laag wegetsen tot er een nanopatroon overblijft",
            "atomen laten neerslaan tot een dun laagje",
            "moleculen zichzelf laten ordenen tot een structuur",
        ],
        antwoord=[0, 1],
        uitleg="De laatste twee gaan van klein naar groot en zijn dus bottom-up. Welke "
        "methode je kiest, hangt af van de precisie die je nodig hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe kleiner een deeltje, hoe groter zijn oppervlak ten opzichte van zijn volume.",
        antwoord=True,
        uitleg="Dat is de kern van de nanochemie. Daardoor zijn nanodeeltjes veel "
        "reactiever dan hetzelfde materiaal in het groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom smelt een nanodeeltje goud bij een lagere temperatuur dan een goudklomp?",
        opties=[
            "een groot deel van de atomen zit aan het oppervlak en zit minder vast",
            "een nanodeeltje heeft een andere chemische samenstelling dan het blok",
            "een nanodeeltje geleidt de warmte veel sneller tot diep in zijn kern",
            "een nanodeeltje heeft een veel lagere dichtheid dan hetzelfde metaal",
        ],
        antwoord=0,
        uitleg="Atomen aan het oppervlak hebben minder buren om zich aan vast te houden. "
        "Bij nanomaat is dat een groot deel van alle atomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de verhouding oppervlak tot volume zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze wordt groter als het deeltje kleiner wordt",
            "ze verklaart waarom nanodeeltjes zo reactief zijn",
            "ze wordt kleiner als het deeltje kleiner wordt",
            "ze verklaart waarom nanodeeltjes zwaarder zijn",
        ],
        antwoord=[0, 1],
        uitleg="Het is dezelfde gedachte als bij de verdelingsgraad van een poeder, maar "
        "duizend keer verder doorgetrokken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de methode waarbij je nanomateriaal uit grof materiaal maakt?",
        antwoord=["top-down", "topdown", "top down"],
        uitleg="Malen, etsen en snijden horen daarbij. De andere weg, van atoom naar "
        "structuur, heet bottom-up.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is grafeen zo sterk?",
        opties=[
            "de koolstofatomen zitten met sterke bindingen in een vlak net",
            "de laag is zo dun dat een kracht er nooit genoeg greep op krijgt",
            "de atomen liggen los van elkaar en kunnen vrij over elkaar schuiven",
            "er zitten metaalatomen tussen de koolstoflagen die ze vastklemmen",
        ],
        antwoord=0,
        uitleg="Per gewicht is grafeen veel sterker dan staal. Toch is één laag "
        "doorzichtig en buigbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een 3D-nanomateriaal?",
        opties=[
            "een gewoon groot materiaal met een structuur op nanomaat erin",
            "een deeltje dat in alle drie zijn richtingen nanoklein gemaakt is",
            "een draadje dat in drie verschillende richtingen gebogen wordt",
            "een laagje dat in drie lagen boven op elkaar gestapeld wordt",
        ],
        antwoord=0,
        uitleg="Denk aan een materiaal vol nanoporen of nanokorrels. Het geheel is groot, "
        "de structuur erin niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nanomateriaal heeft altijd dezelfde eigenschappen als dezelfde stof in het groot.",
        antwoord=False,
        uitleg="Juist niet: kleur, smeltpunt, reactiviteit en geleidbaarheid kunnen "
        "helemaal anders zijn. Dat is de hele reden om met nanomaat te werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt een koolstofnanobuis elektrische stroom goed?",
        opties=[
            "de elektronen van de pi-bindingen kunnen langs de hele buis bewegen",
            "er zitten vrije metaalionen in de holle binnenkant van de buis",
            "de buis is zo dun dat de elektronen er gewoon dwars door vallen",
            "de koolstofatomen staan elk een elektron af aan de lucht rondom",
        ],
        antwoord=0,
        uitleg="Het is dezelfde gedachte als bij de verspreide elektronen van benzeen, "
        "maar over de volle lengte van de buis.",
    ),
    dict(
        type="waarofniet",
        vraag="Een quantumdot is een voorbeeld van een 1D-nanomateriaal.",
        antwoord=False,
        uitleg="Hij is in alle drie de richtingen nanoklein en dus 0D. Bij 1D is er één "
        "richting wel lang, zoals bij een nanobuis.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je één laag koolstofatomen in een honingraatpatroon?",
        antwoord=["grafeen", "het grafeen", "graphene"],
        uitleg="Opgerold geeft het een nanobuis, in bollen gevouwen een buckyball. Alle "
        "drie bestaan ze enkel uit koolstof.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men nanodeeltjes in zonnecrème?",
        opties=[
            "ze houden uv-licht tegen en blijven toch doorzichtig op de huid",
            "ze maken de crème witter en dus beter zichtbaar",
            "ze doden de bacteriën op de huid tijdens het zonnen",
            "ze maken de huid sneller bruin dan zonder crème",
        ],
        antwoord=0,
        uitleg="Zinkoxide en titaandioxide in grove vorm geven een witte laag. Op nanomaat "
        "zie je ze bijna niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap van zilvernanodeeltjes gebruikt men in verband en sokken?",
        opties=[
            "hun antibacteriële werking",
            "hun geleidbaarheid voor stroom",
            "hun lage smeltpunt",
            "hun grote hardheid",
        ],
        antwoord=0,
        uitleg="Door het grote oppervlak komen er genoeg zilverionen vrij om bacteriën te "
        "doden. Daarom gaat ook de geur weg.",
    ),
    dict(
        type="invultekst",
        vraag="Welke nanodeeltjes zorgen voor de gekleurde streep in een covidtest?",
        antwoord=["goud", "gouddeeltjes", "gouden nanodeeltjes"],
        uitleg="Goud op nanomaat is niet goudkleurig maar rood. De deeltjes hangen aan "
        "antilichamen die het virus herkennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is goud op nanomaat niet goudkleurig?",
        opties=[
            "de elektronen in zo'n klein deeltje reageren anders op licht",
            "het goud is op nanomaat met een andere stof vermengd",
            "het goud wordt op nanomaat doorzichtig voor alle licht",
            "het goud oxideert op nanomaat tot een rood oxide",
        ],
        antwoord=0,
        uitleg="De kleur hangt af van de grootte van het deeltje. Daarom kan je met "
        "dezelfde stof verschillende kleuren maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Nanodeeltjes kunnen als katalysator werken met heel weinig materiaal.",
        antwoord=True,
        uitleg="Een katalysator werkt aan zijn oppervlak, en dat is bij nanomaat enorm per "
        "gram. Daarom zit er in een autokatalysator maar een beetje platina.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten eigenschappen kunnen bij nanomaat veranderen? Kruis alles aan wat juist is.",
        opties=[
            "de optische eigenschappen, zoals de kleur",
            "de mechanische eigenschappen, zoals de sterkte",
            "het aantal protonen in de kern van de atomen",
            "de molaire massa van de stof zelf",
        ],
        antwoord=[0, 1],
        uitleg="De stof blijft chemisch dezelfde: de atomen veranderen niet. Wat verandert "
        "is hoe die atomen samen reageren op licht, kracht en warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn nanodeeltjes in het lichaam een risico?",
        opties=[
            "ze zijn zo klein dat ze tot in de cellen kunnen komen",
            "ze zijn zo groot dat ze de bloedvaten verstoppen",
            "ze lossen op in bloed en maken het zuurder",
            "ze geleiden de stroom van de zenuwen te snel door",
        ],
        antwoord=0,
        uitleg="Grote deeltjes blijven buiten. Op nanomaat kunnen ze celmembranen passeren, "
        "en wat ze daar doen is nog niet overal onderzocht.",
    ),
    dict(
        type="invultekst",
        vraag="Welke eigenschap van grafeen maakt het geschikt voor een buigbaar scherm?",
        antwoord=["doorzichtig en geleidend", "geleidend", "doorzichtig"],
        uitleg="Het is sterk, buigbaar, doorzichtig én het geleidt stroom. Die combinatie "
        "is bij gewone materialen heel moeilijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van een nanokatalysator in de industrie?",
        opties=[
            "er is veel minder materiaal nodig voor hetzelfde effect",
            "de reactie heeft geen activeringsenergie meer nodig",
            "het product komt er zuiverder uit zonder scheiden",
            "de reactie wordt exo-energetisch in plaats van endo",
        ],
        antwoord=0,
        uitleg="Een katalysator verandert nooit de reactie-energie. Hij verlaagt de "
        "drempel, en dat lukt met nanomaat met minder grondstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over nanoplastics zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zijn kleiner dan microplastics",
            "ze kunnen door een celmembraan geraken",
            "ze zijn groter dan microplastics",
            "ze breken sneller af dan microplastics",
        ],
        antwoord=[0, 1],
        uitleg="Nano is duizend keer kleiner dan micro. Juist daardoor kunnen ze verder in "
        "het lichaam en in het milieu komen.",
    ),
    dict(
        type="waarofniet",
        vraag="Nanodeeltjes zijn met een gewone lichtmicroscoop goed te zien.",
        antwoord=False,
        uitleg="Ze zijn kleiner dan de golflengte van licht. Daarvoor heb je een "
        "elektronenmicroscoop nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een nanodeeltje van een metaal reactiever dan een blok van hetzelfde metaal?",
        opties=[
            "er zit veel meer oppervlak per gram waar de reactie kan gebeuren",
            "de atomen aan de binnenkant doen ook mee aan de reactie",
            "het metaal heeft op nanomaat een ander oxidatiegetal",
            "het metaal heeft op nanomaat meer valentie-elektronen",
        ],
        antwoord=0,
        uitleg="Het is hetzelfde idee als bij een poeder dat sneller brandt dan een blok. "
        "Op nanomaat gaat dat nog veel verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassing berust op de optische eigenschappen van nanodeeltjes?",
        opties=[
            "de kleur van een quantumdot in een scherm",
            "de sterkte van een nanobuis in een fietskader",
            "de antibacteriële werking van zilver in verband",
            "de katalytische werking van platina in een uitlaat",
        ],
        antwoord=0,
        uitleg="Welke kleur licht een quantumdot uitzendt, hangt af van zijn grootte. "
        "Daarmee kan men heel zuivere kleuren maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nadelen hebben nanomaterialen? Kruis alles aan wat juist is.",
        opties=[
            "hun effect op gezondheid en milieu is nog niet overal onderzocht",
            "ze zijn moeilijk te meten en te volgen in een product",
            "ze zijn te groot om in een product te verwerken",
            "ze reageren met geen enkele andere stof",
        ],
        antwoord=[0, 1],
        uitleg="Juist omdat ze zo klein zijn, is het moeilijk na te gaan waar ze "
        "terechtkomen. Daarom staan ze op een etiket vermeld als nano.",
    ),
    dict(
        type="invultekst",
        vraag="Welk toestel heb je nodig om nanodeeltjes te bekijken?",
        antwoord=["elektronenmicroscoop", "een elektronenmicroscoop", "elektronenmicroscopie"],
        uitleg="Elektronen hebben een veel kleinere golflengte dan licht. Daardoor kan je "
        "er veel kleinere dingen mee onderscheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijft men nano op het etiket van een cosmetisch product?",
        opties=[
            "zo weet de koper dat er deeltjes op nanomaat in zitten",
            "zo weet de koper dat het product biologisch is",
            "zo weet de koper dat het product goedkoper gemaakt is",
            "zo weet de koper dat het product niet getest is",
        ],
        antwoord=0,
        uitleg="De wet vraagt die vermelding, omdat nanomaat andere eigenschappen geeft. "
        "Zo kan de koper zelf kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap maakt een koolstofnanobuis geschikt om een materiaal te versterken?",
        opties=[
            "haar grote sterkte bij een heel klein gewicht",
            "haar lage smeltpunt bij nanomaat",
            "haar doorzichtigheid voor zichtbaar licht",
            "haar antibacteriële werking op het oppervlak",
        ],
        antwoord=0,
        uitleg="Nanobuizen in een kunststof geven een licht en stevig materiaal. Dat "
        "gebruikt men in sportgerief en in de luchtvaart.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nanomateriaal kan magnetisch zijn terwijl dezelfde stof in het groot dat niet is.",
        antwoord=True,
        uitleg="Ook de magnetische eigenschappen hangen af van de maat. Dat gebruikt men "
        "bijvoorbeeld in medische beeldvorming.",
    ),
    dict(
        type="waarofniet",
        vraag="Nanotechnologie is iets van de verre toekomst en zit nog in geen enkel product.",
        antwoord=False,
        uitleg="Ze zit al in zonnecrème, verband, tandpasta, schermen en "
        "autokatalysatoren. Vaak zonder dat je het merkt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stoffen op nanomaat houden uv-licht tegen in zonnecrème?",
        antwoord=["zinkoxide", "titaandioxide", "zinkoxide en titaandioxide"],
        uitleg="In grove vorm geven ze een witte laag op de huid. Op nanomaat werken ze "
        "even goed en zie je ze niet.",
    ),
]
