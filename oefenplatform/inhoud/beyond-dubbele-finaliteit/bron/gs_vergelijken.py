# -*- coding: utf-8 -*-
"""Kenmerken van samenlevingen, interculturele contacten en vergelijken.

Uit de bouwstenen "kenmerken", "aard van interculturele contacten" en
"gelijkenissen en verschillen tussen samenlevingen en historische periodes" van
de vakfiche geschiedenis, 3 dubbele finaliteit.

De vier rijen kenmerken (politiek, sociaal, cultureel, economisch) zijn het
gereedschap waarmee twee samenlevingen naast elkaar gezet worden, binnen één
periode of over periodes heen. Dat vergelijken weegt 5 procent van het examen,
en op het examen krijgt een kandidaat de informatie over de oudere periodes
erbij; de vragen hier toetsen dus de begrippen en de werkwijze, niet het
blokken van feiten over de prehistorie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort de staatsvorm van een land?",
        opties=[
            "bij de politieke kenmerken",
            "bij de sociale kenmerken",
            "bij de culturele kenmerken",
            "bij de economische kenmerken",
        ],
        antwoord=0,
        uitleg="Democratie, dictatuur, rechtsstaat en totalitaire staat zijn vormen van bestuur, en bestuur is politiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort een gelaagde samenleving?",
        opties=[
            "bij de sociale kenmerken",
            "bij de politieke kenmerken",
            "bij de culturele kenmerken",
            "bij de economische kenmerken",
        ],
        antwoord=0,
        uitleg="Het gaat over groepen die boven of onder elkaar staan, en dus over de verhoudingen tussen mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort propaganda?",
        opties=[
            "bij de culturele kenmerken",
            "bij de economische kenmerken",
            "bij de sociale kenmerken",
            "bij geen van de vier soorten",
        ],
        antwoord=0,
        uitleg="Propaganda werkt met beelden, woorden en wereldbeelden. Ze dient wel een politiek doel, maar het middel is cultureel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken zijn economische kenmerken?",
        opties=[
            "industrialisering en kapitalisme",
            "arbeidsorganisatie en productiemethoden",
            "genocide en minderheden",
            "levensbeschouwing en tradities",
        ],
        antwoord=[0, 1],
        uitleg="Genocide en minderheden zijn sociale kenmerken; levensbeschouwing en tradities zijn culturele.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken zijn sociale kenmerken?",
        opties=[
            "onderdrukking en emancipatie",
            "migratie en minderheden",
            "mondialisering en concurrentie",
            "imperialisme en dekolonisatie",
        ],
        antwoord=[0, 1],
        uitleg="Mondialisering en concurrentie zijn economisch; imperialisme en dekolonisatie zijn politiek.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een staat waarin de overheid elk deel van het leven wil controleren?",
        antwoord=["een totalitaire staat", "totalitaire staat", "totalitair"],
        uitleg="Niet alleen het bestuur, ook de economie, de kunst, het onderwijs en het gezin komen onder controle.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een staat waarin ook de overheid zelf aan de wet gebonden is?",
        antwoord=["een rechtsstaat", "rechtsstaat"],
        uitleg="Dat is meer dan een democratie: ook een verkozen meerderheid mag niet alles, want grondrechten en rechters houden haar tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een supranationale en een intergouvernementele organisatie?",
        opties=[
            "een supranationale organisatie kan beslissingen opleggen aan de lidstaten",
            "een supranationale organisatie heeft meer leden dan een andere",
            "een intergouvernementele organisatie bestaat enkel in Europa",
            "een intergouvernementele organisatie heeft geen eigen gebouw",
        ],
        antwoord=0,
        uitleg="Bij een intergouvernementele organisatie blijven de staten zelf beslissen en werken ze alleen samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een democratie is altijd ook een rechtsstaat.",
        antwoord=False,
        uitleg="Een meerderheid kan verkozen zijn en toch grondrechten schenden. Pas als de overheid zelf aan de wet gebonden is, is het een rechtsstaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verandering in het economische domein kan gevolgen hebben in het sociale domein.",
        antwoord=True,
        uitleg="De industrialisering bracht fabrieken, maar ook een nieuwe klassenmaatschappij en sociale strijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De vier soorten kenmerken moet je altijd apart houden, want ze hebben niets met elkaar te maken.",
        antwoord=False,
        uitleg="Juist het verband ertussen moet je kunnen toelichten: een economische verandering werkt door in politiek, samenleving en cultuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kenmerk kan in de ene periode aanwezig zijn en in de andere niet.",
        antwoord=True,
        uitleg="Precies daarop vergelijk je: industrialisering hoort bij de moderne tijd en niet bij de klassieke oudheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie twee samenlevingen vergelijkt, moet enkel de verschillen opnoemen.",
        antwoord=False,
        uitleg="Je onderscheidt gelijkenissen én verschillen. Een gelijkenis zegt vaak evenveel als een verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aard van intercultureel contact bedoel je met uitbuiting?",
        opties=[
            "de ene groep haalt voordeel ten koste van de andere",
            "de twee groepen wisselen gelijkwaardig goederen uit",
            "de twee groepen nemen elkaars gewoonten over",
            "de twee groepen hebben geen contact",
        ],
        antwoord=0,
        uitleg="Bij wederkerigheid halen beide partijen er voordeel uit; bij uitbuiting maar één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent cultuurvermenging?",
        opties=[
            "elementen van twee culturen groeien samen tot iets nieuws",
            "de ene cultuur verdringt de andere volledig",
            "de twee culturen blijven volledig gescheiden",
            "een cultuur verdwijnt zonder spoor",
        ],
        antwoord=0,
        uitleg="Cultuurdominantie is het tweede geval: de ene cultuur legt zich op aan de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden beschrijven de aard van een intercultureel contact?",
        opties=[
            "vreedzaam contact en gewelddadig contact",
            "wederzijdse perceptie en wederzijdse impact",
            "chronologie en tijdrekening",
            "evolutie en revolutie",
        ],
        antwoord=[0, 1],
        uitleg="Chronologie, tijdrekening, evolutie en revolutie horen bij het situeren in de tijd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het beeld dat twee groepen van elkaar hebben na een contact?",
        antwoord=["wederzijdse perceptie", "perceptie"],
        uitleg="Dat beeld hoeft niet te kloppen, en het is bij elke groep anders. Daarom staat het apart in de rij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt de staatsvorm onder Mao met de staatsvorm in China vandaag. Wat is de belangrijkste gelijkenis?",
        opties=[
            "in beide gevallen heeft één partij de macht in handen",
            "in beide gevallen zijn er vrije verkiezingen",
            "in beide gevallen is de economie volledig gepland",
            "in beide gevallen is er geen leider",
        ],
        antwoord=0,
        uitleg="De communistische partij bleef aan de macht; de economie veranderde wel grondig na Mao.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt het moderne imperialisme met het imperialisme uit de vroegmoderne tijd. Wat is een duidelijk verschil?",
        opties=[
            "het moderne imperialisme bezet het binnenland, niet enkel de kust",
            "het moderne imperialisme gebruikt geen schepen",
            "het vroegmoderne imperialisme ging niet over handel",
            "het vroegmoderne imperialisme kende geen geweld",
        ],
        antwoord=0,
        uitleg="In de vroegmoderne tijd bleef het bij handelsposten aan de kust. In de negentiende eeuw werd het binnenland zelf bestuurd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je bij het beschrijven van een samenleving de begrippen die bij die samenleving horen?",
        opties=[
            "anders leg je er woorden op die er niet bij passen",
            "omdat het korter schrijft dan gewone taal",
            "omdat elke samenleving dezelfde woorden gebruikt",
            "omdat het examen geen gewone taal toelaat",
        ],
        antwoord=0,
        uitleg="Wie in China spreekt over een parlement of over cijnskiesrecht, plakt er een westers kader op dat er niet was.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort een multiculturele samenleving?",
        opties=[
            "bij de culturele kenmerken",
            "bij de politieke kenmerken",
            "bij de economische kenmerken",
            "bij geen van de vier soorten",
        ],
        antwoord=0,
        uitleg="Het gaat over tradities, talen en wereldbeelden die naast elkaar bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort een consumptiemaatschappij?",
        opties=[
            "bij de economische kenmerken",
            "bij de politieke kenmerken",
            "bij de sociale kenmerken",
            "bij de culturele kenmerken",
        ],
        antwoord=0,
        uitleg="Ze gaat over kopen, verkopen, vraag en aanbod, en dus over de economie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk soort kenmerken hoort een breuklijn in een samenleving?",
        opties=[
            "bij de politieke kenmerken",
            "bij de economische kenmerken",
            "bij de culturele kenmerken",
            "bij geen van de vier soorten",
        ],
        antwoord=0,
        uitleg="Een breuklijn verdeelt een land in tegenover elkaar staande groepen die ook politiek botsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken zijn politieke kenmerken?",
        opties=[
            "imperialisme en kolonialisme",
            "mensenrechten en bestuurlijke organisatie",
            "energiebronnen en grondstoffen",
            "kunstuitingen en levensbeschouwing",
        ],
        antwoord=[0, 1],
        uitleg="Energiebronnen en grondstoffen zijn economisch; kunstuitingen en levensbeschouwing cultureel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken zijn culturele kenmerken?",
        opties=[
            "mens- en wereldbeelden",
            "wetenschappen en technologie",
            "vraag en aanbod",
            "burgerrechten en emancipatie",
        ],
        antwoord=[0, 1],
        uitleg="Vraag en aanbod is economisch; burgerrechten en emancipatie zijn sociale kenmerken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een samenleving waarin de industrie niet meer de grootste werkgever is, maar de diensten?",
        antwoord=["postindustrieel", "een postindustriële samenleving", "postindustriële"],
        uitleg="De industriële samenleving komt eerst, de postindustriële erna. Dat is een sociaal kenmerk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het denken in een eigen groep tegenover een andere groep?",
        antwoord=["wij-zij-denken", "wij-zij denken"],
        uitleg="Het is een sociaal kenmerk, en het is de bodem waarop uitsluiting en vervolging kunnen groeien.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het economische systeem waarin privébezit en winst centraal staan?",
        antwoord=["kapitalisme", "het kapitalisme"],
        uitleg="Kapitalisme hoort bij de economische kenmerken, net als mondialisering en concurrentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dictatuur en een totalitaire staat betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="In een dictatuur ligt alle macht bij één persoon of groep. Een totalitaire staat wil daarbij ook het denken en het dagelijks leven beheersen.",
    ),
    dict(
        type="waarofniet",
        vraag="Mondialisering betekent dat economieën over de hele wereld meer met elkaar verbonden raken.",
        antwoord=True,
        uitleg="Goederen, geld, mensen en ideeën bewegen sneller en verder. Het is een economisch kenmerk met gevolgen in elk ander domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transportrevolutie verandert ook de manier waarop er geproduceerd wordt.",
        antwoord=True,
        uitleg="Spoorwegen en stoomschepen maakten grondstoffen en afzetmarkten bereikbaar, en dus kon een fabriek veel groter werken.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee samenlevingen in dezelfde periode kunnen een heel andere bestuurlijke organisatie hebben.",
        antwoord=True,
        uitleg="In de negentiende eeuw was België een constitutionele monarchie met een parlement, en China een keizerrijk met mandarijnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vergelijking tussen periodes moet altijd over alle vier de soorten kenmerken gaan.",
        antwoord=False,
        uitleg="Je kiest de kenmerken die bij de vraag passen. Een vergelijking van de staatsvorm vraagt geen oordeel over de kunst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee groepen handelen met elkaar en nemen beide iets van de ander over, zonder dwang. Welke twee woorden passen?",
        opties=[
            "vreedzaam contact",
            "cultuurvermenging",
            "uitbuiting",
            "cultuurdominantie",
        ],
        antwoord=[0, 1],
        uitleg="Uitbuiting en cultuurdominantie veronderstellen dat de ene partij de andere haar wil oplegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kolonisator legt zijn taal, geloof en school op aan de bevolking. Hoe noem je dat?",
        opties=[
            "cultuurdominantie",
            "wederkerigheid",
            "cultuurvermenging",
            "vreedzaam contact",
        ],
        antwoord=0,
        uitleg="De ene cultuur neemt de plaats van de andere in. Er is dus geen gelijkwaardige uitwisseling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de wederzijdse impact van een intercultureel contact?",
        opties=[
            "beide samenlevingen veranderen door het contact",
            "enkel de zwakste samenleving verandert",
            "beide samenlevingen blijven precies zoals ze waren",
            "het contact heeft nooit gevolgen",
        ],
        antwoord=0,
        uitleg="Ook de kolonisator veranderde: door nieuwe producten, nieuwe kennis en een nieuw beeld van zichzelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt gegevens over de slavernij in de vroegmoderne tijd en over de arbeid in de fabrieken van de negentiende eeuw. Wat is een verschil?",
        opties=[
            "een slaaf is iemands bezit, een arbeider sluit een arbeidsovereenkomst",
            "de arbeider werkte minder lang dan de slaaf",
            "de slaaf kreeg een hoger loon dan de arbeider",
            "er is geen enkel verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Die overeenkomst was vaak onvrij in de praktijk, maar juridisch is het verschil met bezit groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken kan je gebruiken om een samenleving uit de oudheid met een samenleving uit de moderne tijd te vergelijken?",
        opties=[
            "de staatsvorm en de gelaagdheid van de samenleving",
            "de handel en de arbeidsorganisatie",
            "het aantal computers per gezin",
            "de uitslag van de laatste verkiezing",
        ],
        antwoord=[0, 1],
        uitleg="Je kiest kenmerken die in beide periodes bestaan. Computers en verkiezingen bestonden in de oudheid niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt twee samenlevingen uit dezelfde periode. Wat levert dat op dat een vergelijking tussen periodes niet oplevert?",
        opties=[
            "je ziet dat eenzelfde tijd heel verschillende samenlevingen kan dragen",
            "je ziet hoe iets in de tijd veranderde",
            "je ziet welke periode de beste was",
            "je ziet hoe lang een periode duurde",
        ],
        antwoord=0,
        uitleg="Vergelijken binnen een periode toont verscheidenheid; vergelijken over periodes toont verandering en continuïteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het vergelijken van samenlevingen beoordeel je welke van de twee de betere was.",
        antwoord=False,
        uitleg="Je beschrijft gelijkenissen en verschillen aan de hand van kenmerken. Een rangschikking is geen historische uitspraak.",
    ),
]
