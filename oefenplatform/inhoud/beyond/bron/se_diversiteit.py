# -*- coding: utf-8 -*-
"""Samenleven in diversiteit.

Het blok "ik leef samen met anderen" weegt 12,5 procent en valt bij ons uiteen
in twee thema's. Dit is het eerste: de begrippen en de vormen van diversiteit,
met de voordelen en de uitdagingen.

De fiche geeft vier rijtjes en die zijn hier letterlijk overgenomen, want op
een examen met sleepvragen en dropdowns wordt juist daarop getoetst:

    begrippen: multiculturalisme, monoculturalisme, integratie, inclusie,
        exclusie
    vormen: lichaamsdiversiteit, sociale, culturele, religieuze of
        levensbeschouwelijke, seksuele diversiteit
    voordelen: culturele verrijking, uitwisselen van ideeën, economische
        uitwisseling
    uitdagingen: meningsverschillen, verschillende belangen, verschillende
        referentiekaders, risico van groepsdenken, risico van uitsluiting

Let op het verschil tussen integratie en inclusie. Bij integratie past de
nieuwkomer zich aan de bestaande groep aan; bij inclusie verandert de groep
zelf mee zodat iedereen erbij hoort. Dat onderscheid is het makkelijkst fout
te krijgen van het hele blok, dus het komt in beide delen terug.

Deel 1 is de begrippen en de vijf vormen van diversiteit.
Deel 2 is de voordelen en de uitdagingen van samenleven in diversiteit.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent diversiteit?",
        opties=[
            "de verscheidenheid die er tussen mensen bestaat",
            "het aantal nationaliteiten in een gemeente",
            "het recht van elke groep op een eigen wijk",
            "de plicht van nieuwkomers om de taal te leren",
        ],
        antwoord=0,
        uitleg="Diversiteit is het gegeven dat mensen van elkaar verschillen, op heel veel vlakken tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is multiculturalisme?",
        opties=[
            "meerdere culturen die naast elkaar bestaan in één samenleving",
            "één cultuur waaraan alle anderen zich moeten aanpassen",
            "het samensmelten van alle culturen tot één nieuwe",
            "het uitsluiten van mensen met een andere cultuur",
        ],
        antwoord=0,
        uitleg="Multi betekent veel: verschillende culturen die samen in dezelfde samenleving leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is monoculturalisme?",
        opties=[
            "het idee dat één cultuur in de samenleving de norm is",
            "het naast elkaar bestaan van verschillende culturen",
            "het recht van elke cultuur op eigen feestdagen",
            "het mengen van twee culturen binnen één gezin",
        ],
        antwoord=0,
        uitleg="Mono betekent één. Alle anderen worden dan aan die ene cultuur afgemeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen integratie en inclusie?",
        opties=[
            "bij integratie past de nieuwkomer zich aan, bij inclusie past de groep zich mee aan",
            "bij inclusie past de nieuwkomer zich aan, bij integratie de groep",
            "integratie geldt voor personen, inclusie enkel voor landen",
            "er is geen verschil, het zijn twee namen voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Inclusie gaat verder: de omgeving verandert zelf zodat iedereen echt kan meedoen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is exclusie?",
        opties=[
            "mensen buiten de groep of de samenleving houden",
            "mensen laten meedoen zonder dat ze zich moeten aanpassen",
            "mensen een eigen plaats geven binnen de groep",
            "mensen kiezen om zelf niet mee te doen",
        ],
        antwoord=0,
        uitleg="Exclusie is het tegendeel van inclusie: uitsluiten in plaats van erbij halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school bouwt een hellend vlak en past de lessen aan zodat een leerling in een rolstoel alles kan volgen. Welk begrip past hier?",
        opties=["inclusie", "integratie", "exclusie", "monoculturalisme"],
        antwoord=0,
        uitleg="De school verandert zelf mee. Dat is inclusie, niet enkel aanpassing door de leerling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vereniging zegt tegen een nieuw lid dat het zich maar moet schikken naar de bestaande gewoonten. Welk begrip past hier best?",
        opties=["integratie", "inclusie", "exclusie", "multiculturalisme"],
        antwoord=0,
        uitleg="De aanpassing komt volledig van één kant, en dat is wat integratie in dit rijtje betekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vijf vormen van diversiteit noemt de fiche?",
        opties=[
            "lichaams-, sociale, culturele, religieuze en seksuele diversiteit",
            "nationale, regionale, lokale, stedelijke en landelijke diversiteit",
            "economische, politieke, juridische, sociale en culturele diversiteit",
            "talige, religieuze, culinaire, muzikale en sportieve diversiteit",
        ],
        antwoord=0,
        uitleg="Religieuze diversiteit heet in de fiche ook levensbeschouwelijke diversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kinderen in een klas groeien op in heel verschillende financiële omstandigheden. Welke vorm van diversiteit is dat?",
        opties=[
            "sociale diversiteit",
            "culturele diversiteit",
            "lichaamsdiversiteit",
            "levensbeschouwelijke diversiteit",
        ],
        antwoord=0,
        uitleg="Verschillen in sociale en economische positie horen bij de sociale diversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een ploeg spelen mensen met heel verschillende lichaamsbouw en met en zonder beperking. Welke vorm van diversiteit is dat?",
        opties=[
            "lichaamsdiversiteit",
            "sociale diversiteit",
            "seksuele diversiteit",
            "culturele diversiteit",
        ],
        antwoord=0,
        uitleg="Lichaamsdiversiteit gaat over alle verschillen in lichaam, ook beperkingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een jeugdbeweging heeft leden die katholiek, moslim, atheïst en zoekend zijn. Welke vorm van diversiteit is dat?",
        opties=[
            "levensbeschouwelijke diversiteit",
            "culturele diversiteit",
            "sociale diversiteit",
            "lichaamsdiversiteit",
        ],
        antwoord=0,
        uitleg="De fiche noemt die vorm religieuze of levensbeschouwelijke diversiteit, en atheïsme hoort er ook bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Levensbeschouwelijke diversiteit gaat enkel over mensen met een geloof.",
        antwoord=False,
        uitleg="Ook wie niet gelooft, heeft een levensbeschouwing. Die hoort dus even goed bij deze vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Multiculturalisme en monoculturalisme zijn tegengestelde begrippen.",
        antwoord=True,
        uitleg="Veel culturen naast elkaar tegenover één cultuur als norm.",
    ),
    dict(
        type="waarofniet",
        vraag="Inclusie en exclusie betekenen ongeveer hetzelfde.",
        antwoord=False,
        uitleg="Ze zijn elkaars tegendeel: erbij halen tegenover buitensluiten.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche rekent seksuele diversiteit mee als een vorm van diversiteit.",
        antwoord=True,
        uitleg="Ze staat in het rijtje van vijf, naast lichaams-, sociale, culturele en religieuze diversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke begrippen over samenleven in diversiteit staan in de fiche?",
        opties=[
            "multiculturalisme",
            "integratie",
            "inclusie",
            "globalisering",
        ],
        antwoord=[0, 1, 2],
        uitleg="Globalisering staat niet in dit rijtje. Monoculturalisme en exclusie wel.",
    ),
    dict(
        type="invultekst",
        vraag="Welk begrip betekent dat de omgeving zelf verandert zodat iedereen kan meedoen?",
        antwoord=["inclusie", "de inclusie"],
        uitleg="Bij integratie komt de aanpassing van de nieuwkomer, bij inclusie ook van de groep.",
    ),
    dict(
        type="invultekst",
        vraag="Welk begrip uit de fiche betekent mensen buitensluiten?",
        antwoord=["exclusie", "de exclusie"],
        uitleg="Exclusie staat als laatste in het rijtje van vijf begrippen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel vormen van diversiteit noemt de fiche? Antwoord met een cijfer.",
        antwoord=["5", "vijf"],
        uitleg="Lichaams-, sociale, culturele, religieuze of levensbeschouwelijke, en seksuele diversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk woord gebruikt de fiche naast religieuze diversiteit?",
        opties=[
            "levensbeschouwelijke diversiteit",
            "spirituele diversiteit",
            "kerkelijke diversiteit",
            "morele diversiteit",
        ],
        antwoord=0,
        uitleg="De fiche schrijft religieuze of levensbeschouwelijke diversiteit, met een schuine streep ertussen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie voordelen van samenleven in diversiteit noemt de fiche?",
        opties=[
            "culturele verrijking, uitwisselen van ideeën en economische uitwisseling",
            "meer vrije tijd, minder conflicten en lagere belastingen",
            "meer talen leren, sneller reizen en goedkoper wonen",
            "meer veiligheid, meer orde en meer eenheid in de groep",
        ],
        antwoord=0,
        uitleg="Precies die drie staan in de fiche, en niets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met culturele verrijking als voordeel?",
        opties=[
            "je komt in contact met gewoonten en kunst die je anders niet kende",
            "de economie van een land groeit door nieuwe inwoners",
            "er komen meer winkels en restaurants in een buurt",
            "iedereen gaat op dezelfde manier leven en denken",
        ],
        antwoord=0,
        uitleg="Verrijking gaat over wat je erbij krijgt aan cultuur, niet over geld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is economische uitwisseling als voordeel van diversiteit?",
        opties=[
            "handel en werk die ontstaan doordat mensen verschillende dingen meebrengen",
            "het verdelen van het inkomen over alle inwoners van een land",
            "het betalen van belastingen door nieuwkomers",
            "het sturen van geld naar het land van herkomst",
        ],
        antwoord=0,
        uitleg="Verschillende kennis, producten en contacten leveren samen meer op dan één soort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vijf uitdagingen van samenleven in diversiteit noemt de fiche?",
        opties=[
            "meningsverschillen, verschillende belangen, verschillende referentiekaders, groepsdenken en uitsluiting",
            "taalproblemen, woningnood, werkloosheid, armoede en criminaliteit",
            "pesten, racisme, discriminatie, uitsluiting en geweld",
            "files, drukte, lawaai, afval en vervuiling",
        ],
        antwoord=0,
        uitleg="Het derde rijtje hoort bij het volgende thema, over respectvol samenleven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een referentiekader?",
        opties=[
            "het geheel van ervaringen en waarden waarmee je iets beoordeelt",
            "de wet waaraan je gedrag getoetst wordt",
            "de groep waar je lid van bent",
            "het lijstje begrippen dat je voor een examen moet kennen",
        ],
        antwoord=0,
        uitleg="Twee mensen kunnen dezelfde situatie heel anders zien omdat ze van een ander kader vertrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is groepsdenken?",
        opties=[
            "de groep komt tot één mening omdat niemand nog tegenspreekt",
            "een groep die samen een beslissing neemt na een stemming",
            "het denken over wat goed is voor de groep in plaats van voor jezelf",
            "het overleggen in kleine groepjes voor een grote vergadering",
        ],
        antwoord=0,
        uitleg="Bij groepsdenken verdwijnt de tegenspraak, en daardoor worden slechte keuzes niet meer opgemerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een werkgroep durft niemand nog iets anders voor te stellen omdat de voorzitter al een richting gekozen heeft. Welk risico is dat?",
        opties=[
            "het risico van groepsdenken",
            "het risico van uitsluiting",
            "een verschil in referentiekader",
            "een verschil in belangen",
        ],
        antwoord=0,
        uitleg="De tegenspraak valt weg, dus de groep denkt als één persoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee buurtbewoners willen allebei iets anders met hetzelfde pleintje: de ene een speeltuin, de andere parkeerplaatsen. Welke uitdaging is dat?",
        opties=[
            "verschillende belangen",
            "verschillende referentiekaders",
            "het risico van groepsdenken",
            "het risico van uitsluiting",
        ],
        antwoord=0,
        uitleg="Ze willen beiden iets anders van hetzelfde goed. Dat is een belangenverschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Is een meningsverschil volgens de fiche een probleem of een uitdaging?",
        opties=[
            "een uitdaging: het hoort bij samenleven in diversiteit",
            "een probleem dat je altijd moet oplossen met een stemming",
            "een vorm van uitsluiting",
            "een teken van groepsdenken",
        ],
        antwoord=0,
        uitleg="De fiche zet de uitdagingen naast de voordelen: ze horen er allebei bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de fiche is diversiteit tegelijk verrijkend en uitdagend.",
        antwoord=True,
        uitleg="Dat staat zo in het leerdoel: verrijkend én uitdagend voor het samenleven.",
    ),
    dict(
        type="waarofniet",
        vraag="Uitsluiting staat in de fiche bij de voordelen van diversiteit.",
        antwoord=False,
        uitleg="Het risico van uitsluiting staat bij de uitdagingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Mensen met een verschillend referentiekader kunnen dezelfde situatie anders beoordelen.",
        antwoord=True,
        uitleg="Dat is precies waarom de fiche het referentiekader als uitdaging noemt.",
    ),
    dict(
        type="waarofniet",
        vraag="Groepsdenken is goed voor een groep, want het zorgt voor eenheid.",
        antwoord=False,
        uitleg="De fiche noemt het een risico: wie niets meer tegenspreekt, ziet de fouten niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als voordeel van samenleven in diversiteit?",
        opties=[
            "culturele verrijking",
            "uitwisselen van ideeën",
            "economische uitwisseling",
            "minder meningsverschillen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meningsverschillen staan bij de uitdagingen, en ze worden niet minder door diversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als uitdaging van samenleven in diversiteit?",
        opties=[
            "verschillende belangen",
            "het risico van groepsdenken",
            "het risico van uitsluiting",
            "een hogere kostprijs voor de overheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Over kosten voor de overheid zegt dit blok van de fiche niets.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van ervaringen en waarden waarmee iemand een situatie beoordeelt?",
        antwoord=["referentiekader", "het referentiekader"],
        uitleg="Verschillende referentiekaders zijn een van de vijf uitdagingen in de fiche.",
    ),
    dict(
        type="invultekst",
        vraag="Welk risico noemt de fiche als een groep tot één mening komt omdat niemand nog tegenspreekt?",
        antwoord=["groepsdenken", "het groepsdenken"],
        uitleg="Groepsdenken staat samen met uitsluiting bij de twee risico's in het rijtje.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel uitdagingen van samenleven in diversiteit noemt de fiche? Antwoord met een cijfer.",
        antwoord=["5", "vijf"],
        uitleg="Meningsverschillen, verschillende belangen, verschillende referentiekaders, groepsdenken en uitsluiting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vraagt het leerdoel van dit blok precies?",
        opties=[
            "toelichten hoe diversiteit verrijkend en uitdagend is voor het samenleven",
            "opsommen hoeveel nationaliteiten er in België wonen",
            "beslissen welke cultuur de norm moet zijn",
            "uitleggen waarom diversiteit vooral problemen geeft",
        ],
        antwoord=0,
        uitleg="Het leerdoel vraagt de twee kanten samen, niet een keuze tussen de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vereniging vraagt elk nieuw lid om een idee voor het jaarprogramma. Welk voordeel van diversiteit gebruikt ze?",
        opties=[
            "het uitwisselen van ideeën",
            "de economische uitwisseling",
            "de culturele verrijking",
            "het vermijden van groepsdenken door een stemming",
        ],
        antwoord=0,
        uitleg="Verschillende mensen brengen verschillende ideeën mee, en dat is een van de drie voordelen.",
    ),
]
