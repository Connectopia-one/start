# -*- coding: utf-8 -*-
"""De vragen voor "Waar ligt het, en hoe weet je dat?" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "situeren en betekenis geven aan
plaatsen" (10 % van het examen). De fiche zegt er wel uitdrukkelijk bij dat je
die kennis en vaardigheden moet beheersen én toepassen bij álle andere
leerinhouden, dus dit thema staat niet toevallig vooraan.

Deel 1 gaat over het wereldgradennet en over situeren zelf: de meridianen met
de nulmeridiaan en de datumlijn, de breedtecirkels met de evenaar, de
keerkringen en de poolcirkels, noorder- en zuiderbreedte, wester- en
oosterlengte, absoluut situeren op 1° nauwkeurig, en relatief situeren ten
opzichte van fysischgeografische en sociaaleconomische elementen: klimaatzone,
vegetatiezone, reliëfeenheid en continent.

Deel 2 gaat over het kaartbeeld en de mentale kaart: dat wereldkaarten de
wereld verschillend weergeven, dat de keuze van een digitale kaart je blik
stuurt, wat een mentale kaart is, hoe persoonlijke en culturele context maakt
dat mensen anders over een plaats denken, en het verschil tussen de werkelijke,
de ervaren en de mentale afstand.

In ✨ Spark zat al een thema over het gradennet. Hier ligt de lat hoger: daar
was de vraag wélke lijn het is, hier is de vraag wat je ermee doet. De vragen
zijn daarom zoveel mogelijk gesteld vanuit een situatie, zoals de fiche het
vraagt ("vanuit concrete problemen en situaties").

Twee dingen bewust vermeden. Nergens wordt gevraagd hoeveel werelddelen of
oceanen er zijn: atlassen tellen dat verschillend. En nergens wordt naar de
precieze coördinaten van een plaats gevraagd zonder dat het antwoord op 1°
mag afwijken, want dat vraagt de fiche zelf ook niet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Een klasgenoot stuurt je vanuit een reis het bericht: 'Ik zit op 41° NB en 2° OL.' Wat heeft die daarmee gedaan?",
        opties=[
            "De plaats absoluut gesitueerd, met geografische coördinaten",
            "De plaats relatief gesitueerd, ten opzichte van een ander punt",
            "De reisafstand beschreven vanaf het vertrekpunt van de reis",
            "De ligging beschreven met een topografisch referentiepunt",
        ],
        antwoord=0,
        uitleg="Absoluut situeren is een plaats aanduiden met geografische coördinaten: één paar getallen dat maar naar één punt op aarde wijst. Relatief situeren doe je met woorden als 'ten noorden van' of 'aan de kust'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je bij coördinaten altijd eerst de breedte en dan pas de lengte?",
        opties=[
            "Het is een internationale afspraak die iedereen volgt",
            "De breedtecirkels zijn langer dan de meridianen",
            "De breedte verandert sneller dan de lengte doet",
            "De evenaar werd vroeger gemeten dan de nulmeridiaan",
        ],
        antwoord=0,
        uitleg="Breedte eerst, lengte daarna, is gewoon een afspraak. Zonder die afspraak zou 50° 4° zowel België als de Indische Oceaan kunnen aanwijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt op een wereldkaart de lijn waar de datum verspringt. Waar loopt die ongeveer?",
        opties=[
            "Langs de 180ste meridiaan, door de Stille Oceaan",
            "Langs de nulmeridiaan, door het westen van Europa",
            "Langs de evenaar, dwars door de Atlantische Oceaan",
            "Langs de Kreeftskeerkring, over Noord-Afrika heen",
        ],
        antwoord=0,
        uitleg="De datumlijn volgt ruwweg de meridiaan van 180°, precies tegenover de nulmeridiaan. Hij maakt bochten om eilandengroepen en landen niet in twee data te splitsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de meridianen kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Ze lopen van de ene pool naar de andere pool",
            "Ze geven de geografische lengte van een plaats aan",
            "Ze komen samen in de noordpool en de zuidpool",
            "Ze lopen evenwijdig met elkaar rond de aardbol",
            "Ze zijn allemaal even lang als de evenaar zelf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meridianen zijn halve cirkels van pool tot pool en geven de lengte aan. Ze lopen dus niet evenwijdig maar komen in de polen samen. De breedtecirkels lopen wél evenwijdig, en alleen de evenaar is een volledige grote cirkel.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee plaatsen die op dezelfde meridiaan liggen, hebben op hetzelfde moment dezelfde zonnetijd.",
        antwoord=True,
        uitleg="Op één meridiaan staat de zon overal tegelijk op haar hoogste punt. Daarom is de lengte de basis van de tijdzones, ook al volgen de officiële zones landsgrenzen in plaats van rechte lijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke breedte liggen de poolcirkels?",
        opties=[
            "Op 66,5° noorder- en zuiderbreedte",
            "Op 23,5° noorder- en zuiderbreedte",
            "Op 45° noorder- en zuiderbreedte",
            "Op 90° noorder- en zuiderbreedte",
        ],
        antwoord=0,
        uitleg="De poolcirkels liggen op 66,5°, de keerkringen op 23,5°, en op 90° lig je op de pool zelf. Vanaf de poolcirkel komt de zon minstens één dag per jaar niet op of niet onder.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de meridiaan van 0°, die door Greenwich bij Londen loopt?",
        antwoord=["nulmeridiaan", "de nulmeridiaan", "greenwichmeridiaan"],
        uitleg="De nulmeridiaan is het vertrekpunt voor de lengte. Alles ten oosten ervan krijgt oosterlengte, alles ten westen ervan westerlengte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand situeert Kinshasa zo: 'aan de Kongostroom, in Centraal-Afrika, net ten zuiden van de evenaar.' Wat is dat?",
        opties=[
            "Relatief situeren ten opzichte van fysischgeografische elementen",
            "Absoluut situeren met behulp van geografische coördinaten",
            "Relatief situeren ten opzichte van sociaaleconomische elementen",
            "Een mentale kaart beschrijven zoals die persoon hem ziet",
        ],
        antwoord=0,
        uitleg="Een rivier, een continent en de evenaar zijn fysischgeografische elementen. Had die persoon 'de hoofdstad van Congo, dicht bij Brazzaville' gezegd, dan was het relatief situeren ten opzichte van sociaaleconomische elementen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze elementen zijn sociaaleconomisch en niet fysischgeografisch? (meerdere antwoorden mogelijk)",
        opties=[
            "De taal die in een gebied gesproken wordt",
            "Het aandeel mensen dat niet kan lezen",
            "De reliëfeenheid waarin een plaats ligt",
            "De oceaan waaraan een land grenst",
            "De klimaatzone waarin een stad ligt",
        ],
        antwoord=[0, 1],
        uitleg="Talen en analfabetisme gaan over mensen en samenleving, en zijn dus sociaaleconomisch. Reliëf, oceanen en klimaatzones horen bij de natuur en zijn fysischgeografisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Om de klimaatzone van een plaats te bepalen, heb je genoeg aan haar geografische lengte.",
        antwoord=False,
        uitleg="De klimaatzone hangt vooral samen met de breedte, en daarnaast met hoogte, afstand tot de zee en zeestromen. De lengte zegt daar op zich niets over: Ierland en Labrador liggen ongeveer even ver van de evenaar en hebben toch een heel ander klimaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet bepalen in welke vegetatiezone een plaats ligt. Welke bron gebruik je het best?",
        opties=[
            "Een thematische kaart van de plantengroei in de atlas",
            "Een politieke kaart met de landsgrenzen erop aangeduid",
            "Een toeristische stadsplattegrond van de streek zelf",
            "Een luchtfoto van één akker in dat gebied genomen",
        ],
        antwoord=0,
        uitleg="Een vegetatiezone is een patroon dat over grote gebieden loopt, dus je hebt een thematische kaart nodig die dat patroon toont. Eén luchtfoto toont te weinig, een politieke kaart toont iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij zet de vegetatiezones goed op volgorde, van de evenaar naar de noordpool?",
        opties=[
            "Tropisch regenwoud, savanne, woestijn, naaldwoud, toendra",
            "Savanne, tropisch regenwoud, toendra, woestijn, naaldwoud",
            "Woestijn, toendra, tropisch regenwoud, savanne, naaldwoud",
            "Toendra, naaldwoud, woestijn, savanne, tropisch regenwoud",
        ],
        antwoord=0,
        uitleg="Vanaf de evenaar volgen het regenwoud, de savanne en dan de woestijngordel rond de keerkring. Verder noordelijk komen de gematigde bossen, de naaldwouden en ten slotte de toendra.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reliëfeenheid is een gebied dat je aan zijn hoogte en vorm als één geheel kan herkennen.",
        antwoord=True,
        uitleg="Een laagvlakte, een plateau, een heuvelland of een gebergte zijn reliëfeenheden. Je herkent ze aan het hoogteverloop, niet aan een landsgrens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een verslag: 'De fabriek ligt op de Kempense laagvlakte.' Wat werd hier gebruikt om te situeren?",
        opties=[
            "Een reliëfeenheid",
            "Een klimaatzone",
            "Een vegetatiezone",
            "Een wereldblok",
        ],
        antwoord=0,
        uitleg="Een laagvlakte is een reliëfeenheid: ze is afgebakend door haar hoogte en vorm. Een klimaatzone gaat over weer, een vegetatiezone over plantengroei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de examencommissie om absoluut te situeren op 1° nauwkeurig en niet nauwkeuriger?",
        opties=[
            "Eén graad is met een gewone atlas nog goed af te lezen",
            "Nauwkeuriger meten lukt alleen met satellietbeelden",
            "Eén graad komt op elke plaats neer op één kilometer",
            "Onder één graad worden de coördinaten onbetrouwbaar",
        ],
        antwoord=0,
        uitleg="Met de graden in de kaartrand haal je vlot één graad nauwkeurigheid. Eén graad breedte is trouwens ongeveer 111 kilometer, dus het blijft een ruwe aanduiding, maar wel genoeg om een plaats terug te vinden.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle plaatsen op de Kreeftskeerkring liggen op het zuidelijk halfrond.",
        antwoord=False,
        uitleg="De Kreeftskeerkring ligt op 23,5° noorderbreedte, dus op het noordelijk halfrond. De Steenbokskeerkring is de zuidelijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de breedtecirkels kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Ze worden korter naarmate je dichter bij een pool komt",
            "De evenaar is de langste breedtecirkel van allemaal",
            "Ze lopen evenwijdig met de evenaar rond de aardbol",
            "Ze komen samen in de noordpool en de zuidpool",
            "Ze geven de geografische lengte van een plaats aan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Breedtecirkels lopen evenwijdig, worden naar de polen toe steeds kleiner en de evenaar is de langste. Samenkomen in de polen doen de meridianen, en die geven ook de lengte aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de graden die aangeven hoe ver een plaats ten oosten van de nulmeridiaan ligt?",
        antwoord=["oosterlengte", "de oosterlengte"],
        uitleg="Ten oosten van de nulmeridiaan spreek je van oosterlengte, ten westen ervan van westerlengte. België ligt tussen ongeveer 2 en 6 graden oosterlengte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst situeert een haven als 'de grootste van de Europese Unie'. Waarmee wordt hier gewerkt?",
        opties=[
            "Met een sociaaleconomisch element, namelijk een wereldblok",
            "Met een fysischgeografisch element, namelijk een zeearm",
            "Met een absolute plaatsbepaling op basis van coördinaten",
            "Met een reliëfeenheid waarin de haven gelegen is",
        ],
        antwoord=0,
        uitleg="De Europese Unie is een samenwerkingsverband tussen landen, dus een wereldblok. Dat is een sociaaleconomisch element: mensen hebben het gemaakt, de natuur niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plaats met coördinaten 15° ZB en 47° WL ligt op het zuidelijk halfrond, ten westen van de nulmeridiaan.",
        antwoord=True,
        uitleg="ZB staat voor zuiderbreedte en WL voor westerlengte, dus dat klopt. Deze coördinaten wijzen ergens in het binnenland van Brazilië aan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Op een gewone schoolwereldkaart lijkt Groenland ongeveer even groot als Afrika. Hoe komt dat?",
        opties=[
            "De kaart vertekent oppervlakten sterker naar de polen toe",
            "Groenland en Afrika zijn in werkelijkheid ook ongeveer even groot",
            "De kaart toont Afrika kleiner omdat het verder van Europa ligt",
            "Er is op die kaart een andere schaal gebruikt voor Groenland",
        ],
        antwoord=0,
        uitleg="Je kan een bol niet plat maken zonder iets te vervormen. Veel wereldkaarten houden de hoeken kloppend en rekken daarvoor de gebieden bij de polen uit. Afrika is in werkelijkheid ongeveer veertien keer zo groot als Groenland.",
    ),
    dict(
        type="waarofniet",
        vraag="Er bestaat een wereldkaart die tegelijk de vormen, de oppervlakten en de afstanden helemaal juist weergeeft.",
        antwoord=False,
        uitleg="Een bol op een plat blad brengen kan niet zonder verlies. Elke kaart kiest wat ze juist houdt en wat ze laat vervormen, en die keuze bepaalt waarvoor de kaart bruikbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat Europa op de meeste wereldkaarten die wij gebruiken in het midden?",
        opties=[
            "Dat is een keuze van wie de kaart maakt, geen natuurwet",
            "Europa ligt echt in het midden van het wereldgradennet",
            "De nulmeridiaan verplicht kaartmakers om zo te tekenen",
            "Anders zou de datumlijn dwars door een werelddeel snijden",
        ],
        antwoord=0,
        uitleg="Een bol heeft geen midden op een kaart: de maker kiest waar hij hem opensnijdt. In China en in Australië hangen andere wereldkaarten aan de muur, en die zijn niet minder juist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan een kaart met Amerika centraal met je blik doen?",
        opties=[
            "Dat werelddeel groter en belangrijker doen lijken",
            "De echte oppervlakte van dat werelddeel vergroten",
            "De coördinaten van de steden daar doen verschuiven",
            "De afstand tot Europa in kilometer doen toenemen",
        ],
        antwoord=0,
        uitleg="Wat in het midden staat, lees je als het belangrijkste: je oog begint daar. De werkelijke oppervlakte en de coördinaten veranderen natuurlijk niet, alleen je beeld ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een mentale kaart?",
        opties=[
            "Het beeld dat iemand in zijn hoofd heeft van een gebied",
            "Een kaart die alleen op een scherm te bekijken is",
            "Een kaart waarop enkel het reliëf ingetekend staat",
            "Een kaart die je uit je hoofd moet kunnen natekenen",
        ],
        antwoord=0,
        uitleg="Een mentale kaart zit in je hoofd, niet op papier. Ze is nooit volledig: wat je goed kent staat er groot op, wat je nooit ziet ontbreekt of staat scheef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over mentale kaarten kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Ze verschillen van persoon tot persoon",
            "Het kaartbeeld dat je vaak ziet, stuurt ze mee",
            "Ze zijn meestal onvolledig en vertekend",
            "Ze zijn bij iedereen uit hetzelfde land gelijk",
            "Ze worden opgemeten met satellietbeelden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een mentale kaart groeit uit wat je zelf meemaakt en uit de kaarten die je vaak ziet. Daarom verschilt ze per persoon en zit ze vol gaten, ook bij mensen uit hetzelfde land.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mensen kunnen over dezelfde plaats heel anders denken doordat hun persoonlijke context verschilt.",
        antwoord=True,
        uitleg="Voor oudere mensen kan een stadspark vooral een plek zijn om tot rust te komen, voor jongeren een plek om te sporten of te skaten. Dezelfde plaats, een andere betekenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="De stad Mekka betekent voor moslims iets heel anders dan voor christenen. Waarvan is dat een voorbeeld?",
        opties=[
            "Van de invloed van de culturele context op betekenis",
            "Van de invloed van het kaartbeeld op de mentale kaart",
            "Van het verschil tussen ervaren en werkelijke afstand",
            "Van relatief situeren met sociaaleconomische elementen",
        ],
        antwoord=0,
        uitleg="Wat een plaats voor je betekent, hangt af van waar je vandaan komt en wat je gelooft. Dat is culturele context, naast de persoonlijke context van je eigen leven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de afstand in kilometer die je echt aflegt tussen twee plaatsen?",
        antwoord=["werkelijke afstand", "de werkelijke afstand"],
        uitleg="De werkelijke afstand is meetbaar: Gent en Torhout liggen over de weg 55 kilometer uit elkaar. Hoe lang die rit lijkt en hoe ver je denkt dat het is, zijn twee andere dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Dezelfde 55 kilometer voelt korter in een koele auto over de snelweg dan in een warme auto over kleine wegen. Over welke afstand gaat dat?",
        opties=[
            "De ervaren afstand",
            "De werkelijke afstand",
            "De mentale afstand",
            "De hemelsbrede afstand",
        ],
        antwoord=0,
        uitleg="De ervaren afstand gaat over hoe lang de weg lijkt terwijl je hem aflegt. Comfort, drukte en het weer spelen daarin mee, de kilometers blijven dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Veel Belgen schatten dat Algiers verder van Brussel ligt dan Kreta, terwijl Kreta in vogelvlucht bijna 1000 kilometer verder ligt. Wat toont dat?",
        opties=[
            "Dat de mentale afstand van de werkelijke afstand afwijkt",
            "Dat de ervaren afstand altijd langer is dan de werkelijke",
            "Dat de kaart van de Middellandse Zee sterk vertekend is",
            "Dat Algiers en Kreta op dezelfde breedtecirkel liggen",
        ],
        antwoord=0,
        uitleg="De mentale afstand is hoe ver je dénkt dat iets ligt. Kreta kennen veel mensen van vakantie, Algiers niet, en wat je beter kent voelt dichterbij.",
    ),
    dict(
        type="waarofniet",
        vraag="De ervaren afstand en de mentale afstand zijn twee woorden voor hetzelfde.",
        antwoord=False,
        uitleg="De ervaren afstand gaat over de reis zelf terwijl je ze maakt. De mentale afstand gaat over je inschatting vooraf, ook als je er nooit geweest bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet uitzoeken welke gemeenten last hebben van overstromingsgevaar. Welke kaartlaag kies je?",
        opties=[
            "Een thematische kaart met de overstromingsgevoelige gebieden",
            "Een toeristische kaart met de bezienswaardigheden erop",
            "Een politieke kaart met de provinciegrenzen aangeduid",
            "Een wegenkaart met alle genummerde wegen van het land",
        ],
        antwoord=0,
        uitleg="Op een digitale kaart kies je je lagen, en die keuze bepaalt wat je ziet en dus wat je besluit. Met een wegenkaart vind je geen overstromingsgebied, hoe goed die kaart ook is.",
    ),
    dict(
        type="waarofniet",
        vraag="De informatie op een toeristische kaart verschilt van die op een reliëfkaart van hetzelfde gebied.",
        antwoord=True,
        uitleg="Elke kaart kiest een thema en laat de rest weg. Daarom kijk je bij een bron altijd eerst naar de titel en de legende voor je er iets uit besluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk om te weten wie een digitale kaart gemaakt heeft?",
        opties=[
            "De maker kiest wat op de kaart komt en wat niet",
            "Alleen de overheid mag kaartlagen publiceren",
            "De maker bepaalt de geografische coördinaten mee",
            "Zonder die naam werkt de legende van de kaart niet",
        ],
        antwoord=0,
        uitleg="Wie de kaart maakt, kiest het thema, de kleuren en de klassen in de legende. Die keuzes sturen mee wat een lezer eruit haalt, ook zonder dat er iets fout op staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bronnen kan je gebruiken om te bepalen in welke klimaatzone een plaats ligt? (meerdere antwoorden mogelijk)",
        opties=[
            "Een klimatogram van een weerstation daar",
            "Een thematische kaart van de klimaatzones",
            "Een tabel met de maandtemperaturen en neerslag",
            "Een leeftijdshistogram van de bevolking daar",
            "Een plattegrond van het centrum van de stad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een klimatogram, een klimaatkaart en een tabel met temperatuur en neerslag gaan alle drie over het weer op lange termijn. Een leeftijdshistogram gaat over de bevolking en een plattegrond over de straten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kaart met het zuiden bovenaan is fout getekend.",
        antwoord=False,
        uitleg="Dat het noorden boven staat, is een gewoonte en geen regel. Oude kaarten zetten soms het oosten boven, en een kaart met het zuiden boven klopt even goed, ze voelt alleen vreemd omdat ze tegen onze mentale kaart ingaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de afstand die je denkt dat er tussen twee plaatsen ligt, ook al klopt ze niet?",
        antwoord=["mentale afstand", "de mentale afstand"],
        uitleg="De mentale afstand zit in je hoofd, net als de mentale kaart. Ze wordt korter naarmate je een plaats beter kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoeveel open ruimte er in je gemeente overblijft. Wat doe je eerst met je bron?",
        opties=[
            "De titel, de legende en het jaartal nakijken",
            "De kaart meteen afdrukken op groot formaat",
            "De coördinaten van het gemeentehuis opzoeken",
            "De schaal van de kaart groter instellen",
        ],
        antwoord=0,
        uitleg="Zonder legende weet je niet wat de kleuren betekenen, en zonder jaartal weet je niet of het nog klopt. Een kaart lezen begint bij de rand, niet bij het midden.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een gebied goed kent, tekent daar meestal een gedetailleerdere mentale kaart van dan wie er nooit komt.",
        antwoord=True,
        uitleg="Je mentale kaart groeit met wat je meemaakt. De straten rond je school staan er scherp op, een streek die je alleen van het nieuws kent blijft een vage vlek.",
    ),
]
