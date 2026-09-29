# -*- coding: utf-8 -*-
"""De vragen voor "Waar op aarde ben je?" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "lokaliseren, oriënteren en
situeren" (22,5 % van het examen, samen met [[ak_kaartlezen]]).

Deel 1 gaat over de lijnen op de aardbol: de evenaar en de breedtecirkels, de
meridianen met de nulmeridiaan en de datumlijn, de keerkringen, de poolcirkels,
de polen en de halfronden, en over de oceanen en de werelddelen.
Deel 2 gaat over situeren zelf: absoluut met geografische coördinaten, relatief
met sterrenkundige, staatkundige en topografische referentiepunten, en over het
kiezen van de gepaste techniek (kaart, kompas, coördinaten of GPS).

Eén ding bewust vermeden: nergens wordt gevraagd hóéveel oceanen of werelddelen
er zijn. Atlassen tellen dat verschillend (Amerika als één werelddeel of als
twee, de Zuidelijke Oceaan wel of niet apart), en een kind dat het anders
geleerd heeft, heeft dan gelijk én punten tekort. De vragen gaan dus over wélke
het zijn en waar ze liggen, niet over het aantal.

De graden komen uit de fiche en uit de atlas: de keerkringen liggen op 23,5° en
de poolcirkels op 66,5° noorder- en zuiderbreedte. De fiche vraagt nauwkeurig
werken op 1° voor plaatsen in Europa en de rest van de wereld.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je wil aan iemand aan de andere kant van de wereld uitleggen waar jij precies woont. Wat werkt daarvoor het best?",
        opties=[
            "Een paar getallen die overal ter wereld hetzelfde betekenen",
            "De naam van de straat en het huisnummer waar je woont",
            "Een beschrijving van het gebouw waarin je woont en werkt",
            "De afstand tot de dichtstbijzijnde winkel bij jou",
        ],
        antwoord=0,
        uitleg="Een straatnaam zegt niets aan de andere kant van de wereld. Geografische coördinaten wel: die werken overal, want iedereen rekent met hetzelfde net van lijnen over de aardbol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemen we de cirkel die de aarde precies in een noordelijk en een zuidelijk halfrond verdeelt?",
        opties=[
            "De evenaar",
            "De nulmeridiaan",
            "De poolcirkel",
            "De datumlijn",
        ],
        antwoord=0,
        uitleg="De evenaar is de breedtecirkel van nul graden. Alles erboven ligt op het noordelijk halfrond, alles eronder op het zuidelijk halfrond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn meridianen?",
        opties=[
            "Lijnen die van pool tot pool over de aardbol lopen",
            "Lijnen die evenwijdig met de evenaar rond de aarde lopen",
            "Lijnen die de grenzen tussen de werelddelen aanduiden",
            "Lijnen die aangeven waar het overal even laat is",
        ],
        antwoord=0,
        uitleg="Meridianen zijn halve cirkels van de noordpool naar de zuidpool. Ze geven de lengte aan. De lijnen die evenwijdig met de evenaar lopen, zijn de breedtecirkels.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle meridianen zijn even lang, maar de breedtecirkels worden korter naarmate je dichter bij een pool komt.",
        antwoord=True,
        uitleg="Elke meridiaan loopt van pool tot pool, dus die zijn allemaal even lang. De breedtecirkels krimpen: de evenaar is de langste, en aan de pool blijft er een punt over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door welke plaats loopt de nulmeridiaan?",
        opties=[
            "Door Greenwich, bij Londen",
            "Door Parijs, in Frankrijk",
            "Door Rome, in Italië",
            "Door Brussel, in België",
        ],
        antwoord=0,
        uitleg="De nulmeridiaan is de meridiaan van nul graden lengte. Landen spraken af die door de sterrenwacht van Greenwich te laten lopen.",
    ),
    dict(
        type="invultekst",
        vraag="De lijn die ongeveer tegenover de nulmeridiaan ligt en waar de datum verspringt, heet de ___.",
        antwoord="datumlijn",
        uitleg="De datumlijn ligt bij 180 graden lengte, in de Grote Oceaan. Steek je ze over, dan spring je een dag vooruit of achteruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lijnen liggen op 23,5 graden noorder- en zuiderbreedte?",
        opties=[
            "De keerkringen",
            "De poolcirkels",
            "De meridianen",
            "De datumlijnen",
        ],
        antwoord=0,
        uitleg="De Kreeftskeerkring ligt op 23,5 graden noorderbreedte en de Steenbokskeerkring op 23,5 graden zuiderbreedte. Daartussen kan de zon recht boven je hoofd staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke breedte liggen de poolcirkels?",
        opties=[
            "Op 66,5 graden",
            "Op 23,5 graden",
            "Op 45 graden",
            "Op 90 graden",
        ],
        antwoord=0,
        uitleg="De noordpoolcirkel ligt op 66,5 graden noorderbreedte en de zuidpoolcirkel op 66,5 graden zuiderbreedte. Daarbinnen komt de zon in de winter een tijd niet meer op.",
    ),
    dict(
        type="waarofniet",
        vraag="De breedte van een plaats kan oplopen tot 180 graden.",
        antwoord=False,
        uitleg="De breedte gaat van 0 graden aan de evenaar tot 90 graden aan een pool. Het is de lengte die tot 180 graden loopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze woorden horen bij de aardbol en zijn lijnen? Er zijn er meerdere juist.",
        opties=[
            "De evenaar",
            "De poolcirkel",
            "De nulmeridiaan",
            "De hoogtelijn",
            "De legende",
        ],
        antwoord=[0, 1, 2],
        uitleg="De evenaar, de poolcirkels en de nulmeridiaan horen bij het gradennet. Een hoogtelijn gaat over reliëf en een legende hoort bij een kaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn oceanen? Er zijn er meerdere juist.",
        opties=[
            "De Grote of Stille Oceaan",
            "De Atlantische Oceaan",
            "De Indische Oceaan",
            "De Middellandse Zee",
            "De Noordzee",
        ],
        antwoord=[0, 1, 2],
        uitleg="De Grote, de Atlantische en de Indische Oceaan zijn oceanen, net als de Noordelijke IJszee en de Zuidelijke Oceaan. De Middellandse Zee en de Noordzee zijn zeeën: kleiner, en grotendeels omsloten door land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oceaan ligt tussen Europa en Amerika?",
        opties=[
            "De Atlantische Oceaan",
            "De Indische Oceaan",
            "De Grote of Stille Oceaan",
            "De Noordelijke IJszee",
        ],
        antwoord=0,
        uitleg="De Atlantische Oceaan scheidt Europa en Afrika van Noord- en Zuid-Amerika. De Grote Oceaan ligt aan de andere kant, tussen Amerika en Azië.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk werelddeel ligt België?",
        opties=[
            "In Europa",
            "In Azië",
            "In Afrika",
            "In Oceanië",
        ],
        antwoord=0,
        uitleg="België ligt in West-Europa, aan de Noordzee, tussen Frankrijk, Duitsland, Luxemburg en Nederland.",
    ),
    dict(
        type="waarofniet",
        vraag="Antarctica is een werelddeel.",
        antwoord=True,
        uitleg="Antarctica is het werelddeel rond de zuidpool. Er woont niemand vast; er zijn enkel onderzoeksstations.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk werelddeel wordt door de evenaar doorsneden?",
        opties=[
            "Afrika",
            "Europa",
            "Antarctica",
            "Australië",
        ],
        antwoord=0,
        uitleg="De evenaar loopt dwars door Afrika, en ook door Zuid-Amerika en Azië. Europa ligt er volledig boven, Australië en Antarctica volledig onder.",
    ),
    dict(
        type="invultekst",
        vraag="Het punt helemaal bovenaan de aardas heet de ___.",
        antwoord="noordpool",
        uitleg="De noordpool en de zuidpool zijn de twee punten waar de aardas door het oppervlak steekt. Daar komen alle meridianen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een globe?",
        opties=[
            "Een bol waarop de aarde afgebeeld staat",
            "Een kaart van de hele wereld op één blad",
            "Een foto van de aarde vanuit de ruimte",
            "Een boek met kaarten van alle landen",
        ],
        antwoord=0,
        uitleg="Op een globe klopt de vorm van de werelddelen, want de aarde is ook een bol. Een boek met kaarten is een atlas.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een wereldkaart op papier blijven de afmetingen van alle werelddelen even juist als op een globe.",
        antwoord=False,
        uitleg="Een bol platleggen gaat niet zonder vervorming. Op veel wereldkaarten lijken gebieden ver van de evenaar, zoals Groenland, veel groter dan ze zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je op een satellietbeeld het verschil tussen een stad en een bos?",
        opties=[
            "Aan de kleur en het patroon van het oppervlak",
            "Aan de namen die erbij geschreven staan",
            "Aan de legende die naast het beeld hoort",
            "Aan de hoogtelijnen die erdoorheen lopen",
        ],
        antwoord=0,
        uitleg="Een satellietbeeld draagt geen namen en geen legende. Je herkent een stad aan het grijze, rechthoekige patroon en een bos aan het onregelmatige groen.",
    ),
    dict(
        type="invultekst",
        vraag="De helft van de aarde boven de evenaar heet het noordelijk ___.",
        antwoord="halfrond",
        uitleg="De evenaar deelt de aarde in het noordelijk en het zuidelijk halfrond. De nulmeridiaan en de datumlijn delen ze in een oostelijk en een westelijk halfrond.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: mijn school ligt op 51 graden noorderbreedte en 4 graden oosterlengte. Wat doet die persoon?",
        opties=[
            "De plaats absoluut situeren",
            "De plaats relatief situeren",
            "De afstand tot de school berekenen",
            "De richting naar de school aanwijzen",
        ],
        antwoord=0,
        uitleg="Absoluut situeren is een plaats vastleggen met coördinaten uit het gradennet. Die twee getallen wijzen maar één plek op aarde aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: ons dorp ligt ten noorden van de Maas, vlak bij de Nederlandse grens. Wat doet die persoon?",
        opties=[
            "De plaats relatief situeren",
            "De plaats absoluut situeren",
            "De plaats oriënteren met een kompas",
            "De plaats opmeten met een meetlat",
        ],
        antwoord=0,
        uitleg="Relatief situeren is een plaats beschrijven ten opzichte van iets anders: een rivier, een grens, een stad. Dat gaat zonder coördinaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geeft de geografische breedte van een plaats aan?",
        opties=[
            "Hoe ver ze van de evenaar ligt",
            "Hoe ver ze van de nulmeridiaan ligt",
            "Hoe breed het land is waarin ze ligt",
            "Hoe hoog ze boven de zeespiegel ligt",
        ],
        antwoord=0,
        uitleg="De breedte telt in graden vanaf de evenaar naar het noorden of het zuiden. De afstand tot de nulmeridiaan is de lengte.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij geografische coördinaten noem je eerst de breedte en daarna de lengte.",
        antwoord=True,
        uitleg="De afspraak is breedte eerst, lengte daarna. Brussel ligt op ongeveer 51 graden noorderbreedte en 4 graden oosterlengte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plaats ligt op 15 graden zuiderbreedte en 50 graden westerlengte. Waar ligt ze?",
        opties=[
            "Onder de evenaar en ten westen van Greenwich",
            "Boven de evenaar en ten oosten van Greenwich",
            "Onder de evenaar en ten oosten van Greenwich",
            "Precies op de evenaar, halfweg de nulmeridiaan",
        ],
        antwoord=0,
        uitleg="Zuiderbreedte betekent onder de evenaar, westerlengte betekent links van de nulmeridiaan. Die plaats ligt dus in Zuid-Amerika of in de oceaan ervoor.",
    ),
    dict(
        type="invultekst",
        vraag="Ligt een plaats ten oosten van de nulmeridiaan, dan spreken we van ___.",
        antwoord="oosterlengte",
        uitleg="Ten oosten is oosterlengte, ten westen is westerlengte. België ligt op oosterlengte, maar amper een paar graden.",
    ),
    dict(
        type="meerkeuze",
        vraag="De fiche vraagt om plaatsen in Europa en de wereld op 1 graad nauwkeurig te situeren. Wat betekent dat?",
        opties=[
            "Je antwoord mag hoogstens één graad naast de juiste liggen",
            "Je moet altijd naar boven afronden tot een heel getal",
            "Je moet de coördinaten tot op de minuut opschrijven",
            "Je mag één graad breedte fout hebben, maar geen lengte",
        ],
        antwoord=0,
        uitleg="Op één graad nauwkeurig wil zeggen dat je antwoord hoogstens één graad mag afwijken. Je hoeft dus geen minuten en seconden te noteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke referentiepunten zijn sterrenkundig? Er zijn er meerdere juist.",
        opties=[
            "De evenaar",
            "De keerkringen",
            "De polen",
            "De provincie waarin je woont",
            "De rivier die door je stad loopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Sterrenkundige referentiepunten zijn de lijnen en punten van het gradennet: de evenaar, de nulmeridiaan, de polen, de halfronden, de keerkringen en de poolcirkels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke referentiepunten zijn staatkundig? Er zijn er meerdere juist.",
        opties=[
            "De gemeente",
            "Het land",
            "Het werelddeel",
            "De oceaan",
            "Het gebergte",
        ],
        antwoord=[0, 1, 2],
        uitleg="Staatkundige referentiepunten zijn door mensen getrokken: een gemeente of stad, een streek, een land, een werelddeel. Een oceaan of een gebergte is topografisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke referentiepunten zijn topografisch? Er zijn er meerdere juist.",
        opties=[
            "De oceanen",
            "De rivieren",
            "De reliëfeenheden",
            "De landsgrenzen",
            "De poolcirkels",
        ],
        antwoord=[0, 1, 2],
        uitleg="Topografische referentiepunten zijn dingen die in het landschap zelf liggen: oceanen, zeeën, rivieren en reliëfeenheden. Grenzen zijn staatkundig, poolcirkels sterrenkundig.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een plaats enkel absoluut situeren, nooit relatief.",
        antwoord=False,
        uitleg="Het kan allebei, en vaak samen. Brussel ligt op 51 graden noorderbreedte en 4 graden oosterlengte, én ten zuiden van Antwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wandelt in de Ardennen met een papieren kaart en je wil weten welke kant je uit kijkt. Wat gebruik je?",
        opties=[
            "Een kompas",
            "Een meetlat",
            "De legende van de kaart",
            "De titel van de kaart",
        ],
        antwoord=0,
        uitleg="Met het kompas vind je het noorden en draai je de kaart in de juiste richting. Dan komt wat je voor je ziet overeen met wat op de kaart staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil je eigen positie tot op enkele meters kennen, midden in een bos zonder herkenningspunten. Wat gebruik je?",
        opties=[
            "Een satellietnavigatiesysteem",
            "Een kompas en de zon",
            "Een atlas van het werelddeel",
            "Een luchtfoto van tien jaar oud",
        ],
        antwoord=0,
        uitleg="Een GPS vangt signalen van satellieten op en berekent daaruit je coördinaten. Een kompas geeft je wel een richting, maar niet je plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Een satellietnavigatiesysteem berekent je positie uit signalen van satellieten.",
        antwoord=True,
        uitleg="Het toestel meet hoe lang de signalen van meerdere satellieten onderweg waren en leidt daaruit af waar je staat. Daarom werkt het slecht binnen of onder dicht bladerdek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is enkel een straatnaam geen goede manier om een plaats wereldwijd te situeren?",
        opties=[
            "Dezelfde straatnaam komt in veel gemeenten voor",
            "Straatnamen staan nooit op een kaart aangeduid",
            "Straatnamen veranderen elk jaar van schrijfwijze",
            "Straatnamen zijn in elk land in een andere taal",
        ],
        antwoord=0,
        uitleg="Een Stationsstraat ligt in tientallen gemeenten. Pas met de gemeente erbij, of met coördinaten, weet je welke bedoeld is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke technieken helpen je om jezelf te oriënteren? Er zijn er meerdere juist.",
        opties=[
            "Een kompas gebruiken",
            "De stand van de zon bekijken",
            "De noordpijl op je kaart volgen",
            "De schaal van je kaart aflezen",
            "De titel van je kaart lezen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Oriënteren is bepalen welke kant je uit kijkt. Dat doe je met een kompas, met de zon of met de noordpijl. De schaal en de titel zeggen daar niets over.",
    ),
    dict(
        type="invultekst",
        vraag="Een boek vol kaarten van landen en werelddelen heet een ___.",
        antwoord="atlas",
        uitleg="Op het examen krijg je een algemene wereldatlas. Daarmee zoek je plaatsen op en lees je hun coördinaten af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet de ligging van een stad in Australië opzoeken. Waar begin je in de atlas?",
        opties=[
            "Bij het register achteraan",
            "Bij de eerste kaart vooraan",
            "Bij de legende van de wereldkaart",
            "Bij de schaal van de landenkaart",
        ],
        antwoord=0,
        uitleg="Het register achteraan zet alle plaatsnamen op alfabet, met het bladnummer en de vakjes erbij. Zo vind je een stad zonder de hele atlas door te bladeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee verschillende plaatsen op aarde kunnen precies dezelfde geografische coördinaten hebben.",
        antwoord=False,
        uitleg="Elk paar coördinaten wijst maar één punt aan. Dat is juist waarom absoluut situeren zo betrouwbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat klopt over de ligging van België?",
        opties=[
            "Het ligt op ongeveer 50 graden noorderbreedte",
            "Het ligt op ongeveer 50 graden zuiderbreedte",
            "Het ligt op ongeveer 50 graden westerlengte",
            "Het ligt vlak bij de noordpoolcirkel",
        ],
        antwoord=0,
        uitleg="België ligt tussen ongeveer 49 en 52 graden noorderbreedte en tussen 2 en 6 graden oosterlengte. De poolcirkel ligt veel noordelijker, op 66,5 graden.",
    ),
]
