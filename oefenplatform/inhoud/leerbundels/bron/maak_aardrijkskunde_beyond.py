# -*- coding: utf-8 -*-
"""De leerbundels voor aardrijkskunde op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche aardrijkskunde 3de graad doorstroomfinaliteit
(`2027_aardrijkskunde_3DO.pdf`), geldig vanaf 1 januari 2027. Die fiche geldt
voor economie-wiskunde, humane wetenschappen, moderne talen, Latijn-moderne
talen, Latijn-wiskunde met extra wetenschappen, bedrijfswetenschappen en
welzijnswetenschappen.

Let op: wetenschappen-wiskunde volgt een **andere, zwaardere** fiche
(`2027_aardrijkskunde_3WET.pdf`) met twee onderdelen die hier niet in staan,
bodems en oceanen. Dat worden twee extra thema's bij ditzelfde vak, geen
tweede vak.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/aardrijkskunde.json`
doet daar het voorwerk voor.

De bundelsleutels dragen het achtervoegsel "-beyond", want de thematitels van
Beyond botsen met die van ✨ Spark en 🚀 Boost (Situeren, Het weer, ...).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Aardrijkskunde"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NA = "-beyond"
tabel = bundel.tabel

BUNDELS = {}


def zet(sleutel, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[sleutel + NA] = b


# ───────────────────────── 1. Situeren, kaarten en observatie
zet("situeren-kaarten-en-observatie",
    titel="Situeren, kaarten en observatie",
    onder="Het gradennet tot op de minuut, absoluut en relatief situeren, de sferen van het systeem aarde, en het gereedschap waarmee je de ruimte onderzoekt.",
    secties=[
        dict(kop="Breedte en lengte, tot op de minuut", blokken=[
            ("p", "De <strong>geografische breedte</strong> van een plaats is de hoek met de "
                  "<strong>evenaar</strong>, gemeten naar het noorden of naar het zuiden. De evenaar is de "
                  "lijn op 0° breedte; op de noordpool telt de breedte <strong>90</strong>°, op de zuidpool "
                  "ook 90°, maar dan zuiderbreedte."),
            ("p", "De <strong>geografische lengte</strong> lees je af op de <strong>meridiaan</strong>. "
                  "Meridianen lopen van noord naar zuid, van pool tot pool, en zijn allemaal even lang. De "
                  "<strong>nulmeridiaan</strong> loopt door <strong>Greenwich, bij Londen</strong>. Van daar "
                  "tel je <strong>180</strong> graden oostwaarts tot de 180ste meridiaan, en evenveel "
                  "westwaarts."),
            ("fig", svg.gradennet(), "Het gradennet: de evenaar op 0°, de keerkringen op 23,5° en de "
                                     "poolcirkels op 66,5°, elk op beide halfronden."),
            ("p", "De vakfiche vraagt om een plaats <strong>absoluut te situeren op één minuut "
                  "nauwkeurig</strong>. Een <strong>minuut</strong> is <strong>een zestigste van een "
                  "graad</strong>, geschreven met een accent: 56' is 56 minuten. Een coördinaat van een "
                  "plaats in België ziet er dus zo uit: <strong>50° 56' NB en 5° 20' OL</strong>. Je leest "
                  "altijd eerst de breedte, dan de lengte."),
            ("kader", "Eén graad breedte is ongeveer 111 km, dus één minuut is ongeveer 1,85 km. Op één "
                      "minuut nauwkeurig situeren betekent dat je een plaats aanwijst binnen ongeveer twee "
                      "kilometer. Dat lukt met de graadverdeling in de kaartrand van de atlas."),
        ]),
        dict(kop="Absoluut en relatief situeren", blokken=[
            ("p", "<strong>Absoluut situeren</strong> is een plaats aanduiden met haar coördinaten, dus met "
                  "breedte en lengte. Het is dus <strong>niet</strong> een plaats beschrijven met haar "
                  "ligging ten opzichte van een stad in de buurt: dat is net relatief situeren."),
            ("p", "<strong>Relatief situeren</strong> is een plaats aanduiden ten opzichte van iets anders. "
                  "\"Aan de westkant van de Alpen\", \"stroomafwaarts van Luik aan de Maas\" en \"in de "
                  "gematigde klimaatzone\" zijn alle drie relatieve omschrijvingen."),
            ("p", "Je situeert relatief met <strong>fysischgeografische elementen</strong> of met "
                  "<strong>sociaaleconomische elementen</strong>. Een <strong>rivier</strong>, een "
                  "<strong>reliëfeenheid</strong> en een <strong>klimaatzone</strong> zijn "
                  "fysischgeografisch: ze zijn er zonder dat de mens eraan te pas komt. Steden, landen, "
                  "wereldblokken, talen en armoede zijn sociaaleconomisch."),
            ("p", tabel(["fysischgeografisch", "sociaaleconomisch"],
                        [["rivieren en oceanen", "steden en landen"],
                         ["reliëfeenheden", "wereldblokken zoals de EU"],
                         ["klimaat- en vegetatiezones", "godsdiensten, talen, armoede"]])),
        ]),
        dict(kop="Kaarten lezen", blokken=[
            ("p", "De <strong>schaal</strong> zegt hoeveel de kaart verkleint. Bij <strong>1 op 10 "
                  "miljoen</strong> is één centimeter op de kaart honderd kilometer in het echt: dat is een "
                  "<strong>kleine schaal</strong>, met een groot gebied en <strong>weinig detail</strong>. "
                  "Een <strong>grote schaal</strong>, zoals 1 op 10 000, toont een klein gebied met véél "
                  "detail. Op een kleine schaal zie je dus niet méér detail, maar minder."),
            ("p", "Lijnen die plaatsen met dezelfde waarde verbinden heten <strong>iso</strong>lijnen. "
                  "<strong>Isothermen</strong> verbinden plaatsen met dezelfde temperatuur, isobaren "
                  "plaatsen met dezelfde luchtdruk, isohypsen plaatsen met dezelfde hoogte."),
            ("p", "Op het examen ligt de <strong>atlas</strong> ter beschikking, <strong>omdat je de "
                  "gegevens erin moet opzoeken en gebruiken</strong>. Je hoeft geen coördinaten vanbuiten te "
                  "kennen; je moet ze kunnen vinden en er iets mee doen."),
            ("fig", svg.kaartlagen(), "Een digitale kaart bouwt het beeld op in lagen: je kiest welke laag "
                                      "je bovenop legt."),
        ]),
        dict(kop="Het gereedschap van de geograaf", blokken=[
            ("p", "De vakfiche noemt een reeks <strong>hulpbronnen om ruimtelijke processen te "
                  "onderzoeken</strong>: <strong>satellietbeelden</strong>, "
                  "<strong>klimatogrammen</strong> en <strong>leeftijdshistogrammen</strong>, naast kaarten, "
                  "tabellen en grafieken."),
            ("p", "Een <strong>klimatogram</strong> toont je in één oogopslag het <strong>klimaat van een "
                  "plaats</strong>: de staven zijn de neerslag per maand, de lijn de temperatuur. Een "
                  "<strong>leeftijdshistogram</strong> of <strong>bevolkingspiramide</strong> toont de "
                  "<strong>leeftijdsopbouw van een bevolking</strong>. Een "
                  "<strong>determineertabel</strong> helpt je om een gesteente of mineraal <strong>op naam "
                  "te brengen aan de hand van zijn eigenschappen</strong>: kleur, hardheid, breuk."),
            ("fig", svg.klimaatdiagram([3, 4, 7, 10, 14, 17, 19, 19, 16, 12, 7, 4],
                                       [76, 63, 70, 51, 62, 72, 74, 64, 59, 70, 76, 81],
                                       plaats="Ukkel, België"),
             "Een klimatogram: staven voor de neerslag, een lijn voor de temperatuur."),
            ("p", "Een <strong>satellietbeeld in valse kleuren</strong> geeft de kleuren <strong>niet</strong> "
                  "weer zoals je ze met het oog zou zien. De satelliet meet ook straling die wij niet zien, "
                  "zoals infrarood, en die krijgt een kleur toegewezen. Gezonde begroeiing komt er daardoor "
                  "vaak felrood op, en dat is precies de bedoeling: zo zie je iets wat op een gewone foto "
                  "niet opvalt."),
        ]),
        dict(kop="Sterren, planeten en manen", blokken=[
            ("p", "Een <strong>ster</strong> straalt zelf licht uit; een <strong>planeet</strong> niet, die "
                  "weerkaatst enkel het licht van haar ster. Een <strong>maan</strong> is een hemellichaam "
                  "dat rond een planeet draait."),
            ("p", "Zie je 's avonds een <strong>helder puntje dat niet flikkert</strong> en dat dag na dag "
                  "verschuift tussen de sterren, dan is dat waarschijnlijk <strong>een planeet</strong>. "
                  "Sterren staan zo ver dat ze als een punt binnenkomen en door de lucht heen flikkeren; "
                  "een planeet is een schijfje en flikkert niet."),
            ("p", "Niet alle sterren die je ziet horen bij ons zonnestelsel: <strong>geen enkele</strong> "
                  "behalve de zon. Alle andere staan lichtjaren ver, buiten ons zonnestelsel."),
            ("p", "De <strong>poolster</strong> of Polaris staat bijna precies in het verlengde van de "
                  "<strong>aardas</strong>. Daardoor staat ze 's nachts schijnbaar stil terwijl de andere "
                  "sterren om haar heen draaien. Haar <strong>hoogte boven de horizon is ongeveer gelijk aan "
                  "de breedteligging</strong> van de plaats waar je staat: in Oslo, op ongeveer 60° "
                  "noorderbreedte, staat de poolster <strong>ongeveer 60°</strong> hoog."),
            ("p", "De <strong>hoogte</strong> van een ster is de <strong>hoek tussen de ster en de "
                  "horizon</strong>. Het <strong>zenit</strong> is het punt <strong>recht boven je "
                  "hoofd</strong>, dus op een hoogte van 90°."),
        ]),
        dict(kop="Waarnemen: telescopen en satellieten", blokken=[
            ("p", "Een <strong>optische telescoop</strong> vangt zichtbaar licht op. Hij staat het best "
                  "hoog, droog en donker: op een berg, in een droge streek, ver van steden. Een vochtige "
                  "streek dicht bij een grote stad is net de slechtste plaats, want vocht, warme lucht en "
                  "lichtvervuiling bederven het beeld."),
            ("p", "Een <strong>radiotelescoop</strong> zet je in <strong>om radiogolven van hemellichamen "
                  "op te vangen</strong>. Radiogolven gaan door wolken heen en worden niet door daglicht "
                  "overstemd, dus een radiotelescoop kan <strong>ook bij bewolkt weer en bij daglicht</strong> "
                  "gegevens opnemen."),
            ("p", "Een telescoop <strong>buiten de atmosfeer</strong> heeft drie voordelen: <strong>het "
                  "beeld trilt niet door luchtbeweging</strong>, <strong>ook ultraviolet en infrarood komen "
                  "binnen</strong> (de atmosfeer houdt die tegen), en <strong>er is geen lichtvervuiling van "
                  "steden</strong>."),
            ("p", "Met <strong>satellieten</strong> worden onder meer <strong>weersvoorspellingen</strong> "
                  "gemaakt, loopt <strong>communicatie over lange afstand</strong>, en worden "
                  "<strong>bosbranden opgevolgd</strong>."),
            ("p", "Een <strong>gps-toestel</strong> bepaalt je plaats doordat het <strong>de looptijd van "
                  "signalen van meerdere satellieten meet</strong>. Uit die looptijd volgt de afstand tot "
                  "elke satelliet. Voor plaats én hoogte heeft het er minstens <strong>4</strong> nodig."),
            ("weetje", "Met een telescoop kijk je eigenlijk in het verleden, omdat het licht onderweg tijd "
                       "nodig had om hier te komen. Hoe verder je kijkt, hoe langer geleden."),
        ]),
        dict(kop="Het systeem aarde: de sferen", blokken=[
            ("p", "De vakfiche deelt het systeem aarde op in <strong>sferen</strong>: de "
                  "<strong>geosfeer</strong>, de <strong>atmosfeer</strong> en de "
                  "<strong>hydrosfeer</strong>, met daarbij de biosfeer."),
            ("p", tabel(["sfeer", "wat zit erin"],
                        [["geosfeer", "al het gesteente en de bodem van de aarde"],
                         ["atmosfeer", "de luchtlaag rond de aarde"],
                         ["hydrosfeer", "al het water: oceanen, rivieren, ijs, grondwater"],
                         ["biosfeer", "al het leven op aarde"]])),
            ("p", "De sferen werken op elkaar in, en dat is precies wat een geograaf onderzoekt. Een rivier "
                  "die zand naar de zee voert, laat <strong>de hydrosfeer en de geosfeer</strong> "
                  "samenwerken: het water verplaatst het gesteente."),
        ]),
    ])


# ───────────────────────── 2. Het heelal: ontstaan en afstanden
zet("het-heelal-ontstaan-en-afstanden",
    titel="Het heelal: ontstaan en afstanden",
    onder="De Big Bang en het bewijs ervoor, de drie scenario's voor de toekomst, en de maten waarmee je afstanden in het heelal opschrijft.",
    secties=[
        dict(kop="De Big Bangtheorie", blokken=[
            ("p", "De <strong>Big Bangtheorie</strong> zegt dat het heelal <strong>uit één heet, dicht "
                  "begin ontstaan is en sindsdien uitdijt</strong>. Met de <strong>oerknal</strong> bedoelen "
                  "we dat <strong>hete, dichte begin van ruimte en tijd</strong>. Het heelal is ongeveer "
                  "<strong>13,8</strong> miljard jaar oud."),
            ("p", "Het is belangrijk hoe je die uitdijing voorstelt. Het is <strong>niet</strong> zo dat de "
                  "sterrenstelsels door een vaste lege ruimte heen vliegen, weg van het punt waar de oerknal "
                  "gebeurde. De <strong>ruimte zelf</strong> rekt uit, overal tegelijk. Er is dus geen "
                  "middelpunt van de oerknal dat je op een kaart kan aanwijzen."),
            ("weetje", "De naam Big Bang werd eerst spottend gebruikt door tegenstanders van de theorie. Ze "
                       "vonden een heelal met een begin te veel op een scheppingsverhaal lijken. De naam is "
                       "blijven plakken en wordt nu gewoon gebruikt."),
        ]),
        dict(kop="Drie vaststellingen die voor een uitdijend heelal pleiten", blokken=[
            ("p", "<strong>Het licht van verre sterrenstelsels is naar het rood verschoven.</strong> "
                  "<strong>Roodverschuiving</strong> betekent dat <strong>licht van een wegbewegende bron "
                  "uitrekt naar het rood</strong>. Net zoals het geluid van een wegrijdende ziekenwagen lager "
                  "klinkt, wordt licht van een wegbewegende bron langgolviger, dus roder."),
            ("p", "<strong>Hoe verder een sterrenstelsel staat, hoe sneller het zich van ons verwijdert.</strong> "
                  "Dat is precies wat je verwacht als de ruimte overal uitrekt: twee punten die al ver uit "
                  "elkaar liggen, hebben meer uitrekkende ruimte tussen zich."),
            ("p", "<strong>Overal in de hemel meten we een zwakke achtergrondstraling.</strong> Die "
                  "<strong>kosmische achtergrondstraling</strong> komt <strong>van het moment dat het heelal "
                  "doorzichtig werd</strong>, ongeveer 380 000 jaar na de oerknal. Ze komt "
                  "<strong>niet</strong> uit één bepaalde richting: ze komt uit élke richting ongeveer even "
                  "sterk, en dat is juist het sterkste argument."),
        ]),
        dict(kop="Hoe het heelal veranderde", blokken=[
            ("p", "Over de evolutie van het heelal weten we dit: <strong>het is sinds zijn ontstaan "
                  "afgekoeld</strong>, <strong>de eerste sterren bestonden vooral uit waterstof en "
                  "helium</strong>, en <strong>zware elementen zijn in sterren gemaakt</strong>. Het ijzer in "
                  "je bloed is in een ster gesmeed."),
            ("p", "Zet je de gebeurtenissen op een tijdlijn, dan komt <strong>de vorming van de eerste "
                  "atomen</strong> eerst, vóór de eerste sterren, de eerste sterrenstelsels en het ontstaan "
                  "van de aarde."),
            ("p", "De <strong>aarde en de zon</strong> zijn ongeveer <strong>4,6</strong> miljard jaar oud. "
                  "Dat is ongeveer <strong>een derde</strong> van de leeftijd van het heelal."),
        ]),
        dict(kop="Drie scenario's voor de toekomst", blokken=[
            ("p", tabel(["scenario", "wat er gebeurt"],
                        [["big crunch", "de uitdijing stopt, keert om en alles trekt weer samen"],
                         ["big rip", "de uitdijing versnelt tot alles uiteengereten wordt"],
                         ["big chill", "het heelal blijft uitdijen en koelt traag dood"]])),
            ("p", "Die drie noemt de vakfiche bij naam: <strong>de big crunch</strong>, <strong>de big "
                  "rip</strong> en <strong>de big chill</strong>. Welk van de drie het wordt, hangt af van "
                  "hoeveel massa en donkere energie er in het heelal zit. De metingen wijzen vandaag naar de "
                  "big chill."),
        ]),
        dict(kop="Afstanden in en rond het zonnestelsel", blokken=[
            ("p", "Licht legt ongeveer <strong>300 000</strong> kilometer per seconde af. Dat is de snelste "
                  "snelheid die er bestaat, en daarom meten we er afstanden mee."),
            ("p", "Eén <strong>astronomische eenheid</strong> (AE) is <strong>de gemiddelde afstand van de "
                  "aarde tot de zon</strong>, ongeveer 150 miljoen kilometer. Binnen ons zonnestelsel gebruik "
                  "je <strong>de astronomische eenheid</strong>, <strong>de lichtminuut</strong> en "
                  "<strong>de lichtseconde</strong>. Voor de afstand van de aarde tot de maan kies je "
                  "<strong>de lichtseconde</strong>: het licht doet er iets meer dan een seconde over."),
            ("p", "Het zonlicht doet ongeveer <strong>8 minuten</strong> over de reis naar de aarde. Daaruit "
                  "volgt dat <strong>de zon ongeveer 8 lichtminuten ver staat</strong>. Neptunus staat "
                  "ongeveer 30 AE van de zon, dus ongeveer <strong>4,5 miljard km</strong>."),
            ("kader", "Een ruimtesonde die 5 lichtuur ver staat, krijgt je bericht pas na 5 uur. Haar "
                      "antwoord doet er nog eens 5 uur over, dus je wacht tien uur op een reactie. Dat is "
                      "waarom sondes zelf moeten kunnen beslissen."),
        ]),
        dict(kop="Lichtjaren, en het adres van de aarde", blokken=[
            ("p", "Een <strong>lichtjaar</strong> is <strong>geen tijdsmaat</strong>: het is de "
                  "<strong>afstand</strong> die licht in één jaar aflegt, ongeveer <strong>9 460 miljard "
                  "km</strong>. Staat een ster op 4,2 lichtjaar, dan is het licht dat je nu ziet "
                  "<strong>4,2</strong> jaar onderweg geweest."),
            ("p", "De astronomische eenheid is <strong>niet</strong> handig voor de afstand tussen twee "
                  "sterrenstelsels: je zou met miljarden AE moeten werken. Daarvoor gebruik je lichtjaren."),
            ("p", "Van klein naar groot gaat het zo: <strong>planetenstelsel, sterrenstelsel, cluster, "
                  "supercluster</strong>."),
            ("p", tabel(["schaal", "ons adres", "grootte"],
                        [["planetenstelsel", "ons zonnestelsel", "enkele lichtuur"],
                         ["sterrenstelsel", "het Melkwegstelsel", "ongeveer 100 000 lichtjaar"],
                         ["cluster", "de Lokale Groep", "miljoenen lichtjaren"],
                         ["supercluster", "de Virgo-supercluster", "honderden miljoenen lichtjaren"]])),
            ("p", "Ons eigen sterrenstelsel heet de <strong>Melkweg</strong>. Ons zonnestelsel ligt daarin "
                  "<strong>in de Orionarm, een eind van het centrum</strong>. Bij het adres van ons "
                  "zonnestelsel horen dus <strong>de Orionarm</strong>, <strong>het Melkwegstelsel</strong> "
                  "en <strong>de Lokale Groep</strong>."),
            ("p", "Een <strong>cluster</strong> is een groep sterrenstelsels die door de zwaartekracht "
                  "samenhangt. <strong>De Melkweg en de Andromedanevel horen samen met een reeks kleinere "
                  "stelsels tot de Lokale Groep.</strong>"),
            ("p", "Staat een sterrenstelsel op 2,5 miljoen lichtjaar, dan geldt alle drie: <strong>je ziet "
                  "het zoals het 2,5 miljoen jaar geleden was</strong>, <strong>het licht ervan was 2,5 "
                  "miljoen jaar onderweg</strong>, en <strong>het staat verder weg dan elke ster van de "
                  "Melkweg</strong>, want de Melkweg is maar 100 000 lichtjaar groot."),
        ]),
    ])


# ───────────────────────── 3. De zon en het zonnestelsel
zet("de-zon-en-het-zonnestelsel",
    titel="De zon en het zonnestelsel",
    onder="De lagen van de zon, zonnevlekken en poollicht, hoe het zonnestelsel ontstond, en wat er allemaal rond de zon draait.",
    secties=[
        dict(kop="De lagen van de zon", blokken=[
            ("p", "Van binnen naar buiten liggen de lagen van de zon zo: <strong>kern, stralingszone, "
                  "convectiezone, fotosfeer</strong>. Daarboven komen nog de chromosfeer en de corona."),
            ("p", "<strong>In de kern</strong> komt de energie vrij, door kernfusie: waterstof smelt er "
                  "samen tot helium. Die energie werkt zich traag naar buiten, eerst als straling, dan met "
                  "opstijgende en dalende gasstromen."),
            ("p", "De <strong>fotosfeer</strong> is de laag die wij als het <strong>zichtbare "
                  "oppervlak</strong> zien. De <strong>buitenste atmosfeer</strong> van de zon bestaat uit "
                  "<strong>de fotosfeer</strong>, <strong>de chromosfeer</strong> en <strong>de "
                  "corona</strong>."),
            ("p", tabel(["laag", "wat gebeurt er"],
                        [["kern", "kernfusie: hier komt de energie vrij"],
                         ["stralingszone", "de energie reist als straling naar buiten"],
                         ["convectiezone", "gas stijgt op en daalt, als kokend water"],
                         ["fotosfeer", "het zichtbare oppervlak, ongeveer 5 500 °C"],
                         ["chromosfeer", "een dunne, rode laag erboven"],
                         ["corona", "de ijle buitenste laag, meer dan een miljoen graden"]])),
            ("p", "De <strong>corona is veel heter dan de fotosfeer</strong>, hoewel ze verder van de kern "
                  "ligt. Dat is een van de open vragen in de sterrenkunde. Je kan de corona "
                  "<strong>niet</strong> op elk moment van de dag met het blote oog zien: ze gaat verloren in "
                  "het felle licht van de fotosfeer, en wordt pas zichtbaar bij een totale zonsverduistering."),
        ]),
        dict(kop="Zonnevlekken, protuberansen en de zonnewind", blokken=[
            ("p", "Een <strong>zonnevlek</strong> is een donkere, koelere plek op het oppervlak van de zon. "
                  "Zonnevlekken zijn donkerder <strong>omdat ze koeler zijn dan hun omgeving</strong>: nog "
                  "altijd zo'n 4 000 °C, maar naast 5 500 °C lijkt dat zwart."),
            ("p", "Een <strong>protuberans</strong> is <strong>een boog van gas boven het "
                  "zonsoppervlak</strong>, opgehouden door het magnetisch veld van de zon."),
            ("p", "Het aantal zonnevlekken komt en gaat in een <strong>zonnecyclus</strong> van ongeveer "
                  "<strong>11</strong> jaar, van minimum naar maximum en terug."),
            ("p", "De <strong>zonnewind</strong> is <strong>een stroom geladen deeltjes die de zon "
                  "uitzendt</strong>. Als die deeltjes bij ons aankomen, ontstaat het "
                  "<strong>poollicht</strong>: <strong>deeltjes van de zon botsen op gas hoog in de "
                  "atmosfeer</strong>, en dat gas licht op. Het poollicht is bij een zonne<strong>maximum</strong> "
                  "vaker en verder van de polen te zien, niet bij een minimum."),
            ("p", "Een sterke <strong>zonnestorm</strong> kan op aarde <strong>storingen in satellieten en "
                  "radioverkeer</strong> geven, <strong>poollicht dat ook in onze streken te zien is</strong>, "
                  "en <strong>spanningspieken in hoogspanningsnetten</strong>."),
        ]),
        dict(kop="Hoe het zonnestelsel ontstond", blokken=[
            ("p", "De zon is ontstaan <strong>uit een samentrekkende wolk gas en stof</strong>. Toen de zon "
                  "ontbrand was, bleef er van die wolk <strong>een schijf gas en stof over waaruit de "
                  "planeten groeiden</strong>."),
            ("p", "Daar komt een kenmerk vandaan dat je kan nakijken: <strong>de planeten draaien allemaal "
                  "in dezelfde zin rond de zon, en bijna in hetzelfde vlak</strong>. Dat is precies wat je "
                  "van een draaiende schijf verwacht."),
            ("p", "Voor het ontstaan van <strong>onze maan</strong> geldt als beste verklaring dat <strong>een "
                  "grote botsing materiaal uit de jonge aarde sloeg</strong>. Dat uitgeslagen puin klonterde "
                  "samen tot de maan."),
            ("p", "De jonge aarde was heet. <strong>De aarde viel in lagen uiteen en gassen "
                  "ontsnapten</strong>: zo ontstonden de eerste geosfeer en de eerste atmosfeer. Het zware "
                  "ijzer zakte naar de kern, het lichtere gesteente bleef erboven. In die eerste atmosfeer "
                  "zaten <strong>waterdamp</strong>, <strong>koolstofdioxide</strong> en "
                  "<strong>stikstof</strong>; zuurstof kwam er pas veel later bij, door het leven."),
        ]),
        dict(kop="De acht planeten", blokken=[
            ("p", "Ons zonnestelsel telt <strong>8</strong> planeten. De vier binnenste zijn de "
                  "<strong>terrestrische planeten</strong>: <strong>Mercurius</strong>, Venus en "
                  "<strong>Mars</strong>, met de aarde erbij. Ze zijn klein, van gesteente en hebben een vast "
                  "oppervlak."),
            ("fig", svg.zonnestelsel(), "De acht planeten in hun orde vanaf de zon."),
            ("p", "De vier buitenste zijn de <strong>gasreuzen</strong>: Jupiter, Saturnus, Uranus en "
                  "Neptunus. Die <strong>zijn groot en hebben geen vast oppervlak</strong>: je zou er niet op "
                  "kunnen landen. <strong>Jupiter</strong> is de grootste planeet, <strong>Neptunus</strong> "
                  "staat het verst van de zon."),
            ("p", "Over <strong>manen</strong>: <strong>een maan draait rond een planeet</strong>, <strong>de "
                  "gasreuzen hebben er elk meerdere</strong>, en <strong>Mercurius en Venus hebben er "
                  "geen</strong>."),
        ]),
        dict(kop="Gordels, dwergplaneten en kometen", blokken=[
            ("p", "De <strong>planetoïdengordel</strong> ligt <strong>tussen Mars en Jupiter</strong>. De "
                  "<strong>Kuipergordel</strong> ligt <strong>voorbij de baan van Neptunus</strong>. Nog veel "
                  "verder ligt de <strong>Oortwolk</strong>: die is <strong>geen platte ring</strong> maar "
                  "een bolvormige schil, en ze ligt véél verder dan de Kuipergordel."),
            ("p", "Een <strong>dwergplaneet</strong> is een hemellichaam dat te klein is om een planeet te "
                  "heten maar wel bolvormig is, zoals Pluto. Een <strong>planetoïde</strong> is "
                  "<strong>niet</strong> hetzelfde: die is onregelmatig van vorm en hoort meestal tot de "
                  "planetoïdengordel."),
            ("p", tabel(["waar het brokstuk is", "hoe het heet"],
                        [["nog in de ruimte", "een meteoroïde"],
                         ["als lichtspoor in de atmosfeer", "een meteoor, een vallende ster"],
                         ["aangekomen op het aardoppervlak", "een meteoriet"]])),
            ("p", "Zie je 's nachts een vallende ster, dan zie je dus eigenlijk <strong>een meteoor</strong>: "
                  "het lichtspoor van een brokje dat in de atmosfeer verbrandt."),
            ("p", "De kern van een <strong>komeet</strong> bestaat <strong>uit ijs, stof en steen</strong>. "
                  "Nadert ze de zon, dan <strong>vormt zich een coma en een staart</strong>. Dicht bij de zon "
                  "heeft een komeet dus <strong>een kern</strong>, <strong>een coma</strong> en <strong>een "
                  "staart</strong>. Die <strong>staart wijst altijd weg van de zon</strong>, ook als de "
                  "komeet van de zon weg beweegt: de zonnewind blaast hem naar achter. Een komeet legt "
                  "bovendien <strong>een sterk uitgerekte, elliptische baan</strong> af, geen cirkel zoals de "
                  "planeten."),
            ("weetje", "Elk jaar zie je rond dezelfde datum een zwerm vallende sterren, omdat de aarde dan "
                       "het stofspoor van een komeet kruist. De Perseïden van midden augustus komen van komeet "
                       "Swift-Tuttle."),
        ]),
    ])


# ───────────────────────── 4. De bewegingen van de aarde
zet("de-bewegingen-van-de-aarde",
    titel="De bewegingen van de aarde",
    onder="De rotatie met haar dag, haar uurgordels en het corioliseffect, en de revolutie met haar seizoenen, zonshoogten en poolnachten.",
    secties=[
        dict(kop="De rotatie: de aarde draait om haar as", blokken=[
            ("p", "De aarde draait om haar as <strong>van west naar oost</strong>. Daarom lijkt de zon van "
                  "oost naar west over de hemel te trekken. Eén volledige aardrotatie ten opzichte van de zon "
                  "duurt <strong>24</strong> uur."),
            ("p", "Dat de aarde écht draait, toont <strong>de slingerproef van Foucault</strong>. Een lange, "
                  "zware slinger blijft in hetzelfde vlak slingeren terwijl de vloer onder hem meedraait met "
                  "de aarde. Na enkele uren slaat de slinger dus in een andere richting dan waar hij begon."),
            ("fig", svg.dag_en_nacht(), "De helft van de aarde is verlicht, de andere helft niet. Door de "
                                        "rotatie schuift die grens elke dag één keer rond."),
            ("p", "De <strong>omtreksnelheid</strong> door de rotatie is <strong>op de evenaar</strong> het "
                  "grootst: daar moet een punt in 24 uur de hele omtrek van ruim 40 000 km afleggen, terwijl "
                  "een punt vlak bij de pool bijna op zijn plaats blijft."),
            ("p", "De rotatie heeft drie gevolgen die je moet kennen: <strong>de afwisseling van dag en "
                  "nacht</strong>, <strong>het afbuigen van winden en zeestromen</strong>, en <strong>de "
                  "afplatting van de aarde aan de polen</strong>. Let op de richting van die afplatting: door "
                  "de rotatie is de aarde <strong>aan de evenaar dikker en aan de polen platter</strong>, niet "
                  "omgekeerd."),
            ("p", "De <strong>dagboog</strong> van de zon is <strong>de weg van de zon van opkomst tot "
                  "ondergang</strong>: hoe hoger en langer die boog, hoe langer de dag duurt."),
        ]),
        dict(kop="Het corioliseffect", blokken=[
            ("p", "Het <strong>corioliseffect</strong> is het effect dat bewegende lucht en water op aarde "
                  "doet afbuigen. Op het <strong>noordelijk halfrond</strong> buigt een wind af "
                  "<strong>naar rechts</strong>, op het zuidelijk halfrond naar links."),
            ("p", "<strong>Op de evenaar zelf is het corioliseffect zo goed als nul.</strong> Daarom ontstaan "
                  "er geen tropische cyclonen vlak op de evenaar: zonder afbuiging gaat de lucht niet "
                  "draaien."),
            ("weetje", "Het effect komt doordat de grond onder de bewegende lucht wegdraait, en dat gebeurt "
                       "op de evenaar veel sneller dan bij de pool. De lucht wordt dus niet geduwd; zij gaat "
                       "rechtdoor terwijl de aarde eronder draait."),
        ]),
        dict(kop="Uurgordels en de datumgrens", blokken=[
            ("p", "De zon schuift per uur <strong>15</strong> graden lengte op: 360 graden gedeeld door 24 "
                  "uur. Eén <strong>uurgordel</strong> beslaat dus <strong>15</strong> graden lengte."),
            ("p", "Daarmee kan je rekenen. Is het in Brussel 12 uur, dan is het op 45° oosterlengte, puur op "
                  "zonnetijd gerekend, ongeveer <strong>15 uur</strong>: er liggen ruim 40 graden tussen, dus "
                  "bijna drie uur verschil, en het oosten loopt voor."),
            ("p", "<strong>Zonnetijd volgt de zon zelf, de klok volgt de tijdzone.</strong> Dat is het "
                  "verschil tussen zonnetijd en <strong>conventionele tijd</strong>. Over de uurgordels geldt: "
                  "<strong>ze lopen ruwweg van noord naar zuid</strong>, <strong>ze volgen vaak de "
                  "landsgrenzen in plaats van de meridiaan</strong>, en <strong>sommige landen gebruiken meer "
                  "dan één uurgordel</strong>."),
            ("p", "De <strong>zomertijd</strong> zet de klok een uur <strong>vooruit</strong>, niet "
                  "achteruit. Het wordt daardoor 's avonds later donker, en 's morgens juist later licht."),
            ("p", "De <strong>datumgrens</strong> loopt <strong>ongeveer langs de 180ste meridiaan</strong>, "
                  "met bochten om eilandengroepen heen. Vlieg je van Tokio naar Hawaï en steek je de "
                  "datumgrens over <strong>naar het oosten</strong>, dan <strong>krijg je dezelfde dag een "
                  "tweede keer</strong>."),
        ]),
        dict(kop="Dezelfde parallel, dezelfde zon", blokken=[
            ("p", "Twee plaatsen op dezelfde <strong>parallel</strong>, dus op dezelfde breedte, hebben drie "
                  "dingen gemeen: <strong>dezelfde daglengte</strong>, <strong>dezelfde culminatiehoogte van "
                  "de zon</strong> en <strong>dezelfde klimaatgordel</strong>. Hun weer kan sterk verschillen, "
                  "want dat hangt ook van de zee en het reliëf af, maar de stand van de zon is dezelfde."),
            ("p", "<strong>Op de evenaar duurt de dag het hele jaar door ongeveer twaalf uur.</strong> Daar "
                  "merk je van de seizoenen bijna niets aan de daglengte."),
        ]),
        dict(kop="De revolutie: de aarde draait rond de zon", blokken=[
            ("p", "De baan van de aarde rond de zon is <strong>een ellips</strong>, geen cirkel. Eén "
                  "<strong>aardrevolutie</strong> duurt ongeveer <strong>365</strong> dagen, nauwkeuriger "
                  "365,25. Dat kwart is de reden voor de schrikkeldag: <strong>zonder schrikkeldagen zou de "
                  "kalender langzaam wegschuiven van de seizoenen</strong>."),
            ("p", "De aarde beweegt daarbij met ongeveer <strong>30 km per seconde</strong>."),
            ("p", "Het punt in de aardbaan dat het dichtst bij de zon ligt heet het "
                  "<strong>perihelium</strong>, en daar staat de aarde <strong>begin januari</strong>. Het "
                  "punt dat het verst ligt heet het <strong>aphelium</strong>, begin juli."),
            ("kader", "Daaruit volgt meteen dat wij <strong>geen</strong> seizoenen hebben doordat de aarde "
                      "in de zomer dichter bij de zon staat. Begin januari staan we het dichtst bij de zon, en "
                      "dan is het bij ons winter. De seizoenen komen van de <strong>schuine aardas</strong>."),
        ]),
        dict(kop="De schuine as en de seizoenen", blokken=[
            ("p", "De <strong>inclinatiehoek</strong> van de aardas ten opzichte van het eclipticavlak is "
                  "<strong>ongeveer 23,5°</strong>. De as houdt die stand het hele jaar aan, dus wijst ze "
                  "een half jaar naar de zon toe en een half jaar ervan weg."),
            ("fig", svg.seizoenen(), "Vier standen in de aardbaan: de as blijft even schuin staan, maar wijst "
                                     "afwisselend naar de zon toe en ervan weg."),
            ("p", tabel(["datum", "wat er gebeurt"],
                        [["21 maart", "de zon staat zenitaal boven de evenaar: equinox"],
                         ["21 juni", "zomerzonnewende op het noordelijk halfrond"],
                         ["23 september", "de zon staat zenitaal boven de evenaar: equinox"],
                         ["22 december", "winterzonnewende op het noordelijk halfrond"]])),
            ("p", "Een <strong>equinox</strong> of nachtevening is een dag waarop dag en nacht overal even "
                  "lang zijn. Dat de zon <strong>zenitaal</strong> staat, betekent dat ze <strong>recht boven "
                  "je hoofd staat, dus op 90°</strong>."),
            ("p", "De <strong>culminatiehoogte</strong>, de hoogte van de zon 's middags, reken je uit met de "
                  "breedte. Op 51° noorderbreedte: op 21 maart <strong>90 − 51 = 39°</strong>, op 21 juni "
                  "<strong>90 − 51 + 23,5 = 62,5°</strong>, en op 22 december <strong>90 − 51 − 23,5 = "
                  "15,5°</strong>. Die laatste is dus géén 40°; in december komt de zon bij ons nauwelijks "
                  "boven de daken uit."),
            ("p", "De aardrevolutie met een schuine aardas geeft <strong>de wisseling van de seizoenen</strong>, "
                  "<strong>een daglengte die door het jaar verandert</strong> en <strong>een culminatiehoogte "
                  "die door het jaar verandert</strong>."),
        ]),
        dict(kop="Van de tropen tot de poolnacht", blokken=[
            ("fig", svg.aardbolgordels(), "De gordels: tropisch tussen de keerkringen, gematigd tot de "
                                          "poolcirkel, polair daarboven."),
            ("p", "In de <strong>tropen</strong> is het het hele jaar warm, en daar zijn drie redenen voor "
                  "die samenhangen: <strong>de zon staat er altijd hoog boven de horizon</strong>, <strong>de "
                  "culminatiehoogte blijft er het hele jaar groot</strong>, en <strong>de daglengte verandert "
                  "er bijna niet door het jaar</strong>."),
            ("p", "Bij een breedte van ongeveer 51°, zoals bij ons, hoor je in <strong>de gematigde</strong> "
                  "klimaatgordel."),
            ("p", "Bij de <strong>poolstreken</strong> horen <strong>de pooldag</strong>, <strong>de "
                  "poolnacht</strong> en <strong>de middernachtzon</strong>. <strong>Op de noordpool blijft de "
                  "zon ongeveer een half jaar onder de horizon.</strong>"),
        ]),
    ])


# ───────────────────────── 5. De maan, getijden en verduisteringen
zet("de-maan-getijden-en-verduisteringen",
    titel="De maan, getijden en verduisteringen",
    onder="De omloop en de schijngestalten van de maan, hoe spring- en doodtij ontstaan, en waarom er niet elke maand een verduistering is.",
    secties=[
        dict(kop="De omloop van de maan", blokken=[
            ("p", "De maan doet over één omloop rond de aarde ten opzichte van de sterren <strong>ongeveer "
                  "27 dagen</strong>. Tussen twee keer nieuwe maan zitten er <strong>29,5</strong> dagen: in "
                  "die 27 dagen is de aarde zelf ook een stuk rond de zon geschoven, dus moet de maan nog "
                  "twee dagen verder om weer precies tussen aarde en zon te staan."),
            ("p", "De maan draait <strong>van west naar oost, zoals de aarde zelf draait</strong>. Haar baan "
                  "<strong>is elliptisch, geen volmaakte cirkel</strong>, <strong>staat een kleine hoek scheef "
                  "op de aardbaan</strong> en <strong>wordt in dezelfde zin afgelegd als de aardrotatie</strong>."),
            ("p", "We zien altijd dezelfde kant van de maan <strong>omdat haar rotatie even lang duurt als "
                  "haar omloop</strong>. Dat heet <strong>gebonden rotatie</strong>. Let op: de achterkant "
                  "krijgt wél zonlicht, net zoveel als de voorkant. Hij heet de verre kant, niet de donkere."),
            ("p", "De maan staat ongeveer <strong>384 000</strong> km van de aarde en legt haar baan af met "
                  "<strong>ruim 1 km per seconde</strong>. Omdat ze elke dag een stuk opschuift, komt ze "
                  "<strong>niet</strong> elke avond op hetzelfde tijdstip op: ze is elke dag ongeveer vijftig "
                  "minuten later."),
        ]),
        dict(kop="De maan zelf", blokken=[
            ("p", "Over de maan geldt: <strong>ze heeft geen eigen licht</strong>, <strong>ze heeft geen "
                  "noemenswaardige atmosfeer</strong> en <strong>ze draait in gebonden rotatie rond de "
                  "aarde</strong>."),
            ("p", "De zwaartekracht aan het oppervlak van de maan is <strong>ongeveer een zesde</strong> van "
                  "die op aarde. <strong>Op de maan is er geen vloeibaar water aan het oppervlak.</strong>"),
            ("p", "De donkere vlakten die je op de maan ziet, de zogenaamde zeeën, bestaan uit "
                  "<strong>uitgevloeide lava van heel lang geleden</strong>."),
            ("p", "De voetstappen van de maanlandingen liggen er nog, om drie redenen samen: <strong>er waait "
                  "geen wind op de maan</strong>, <strong>er valt geen neerslag op de maan</strong>, en "
                  "<strong>er is bijna geen verwering of erosie</strong>."),
        ]),
        dict(kop="De schijngestalten", blokken=[
            ("fig", svg.maanfasen(), "De schijngestalten: nieuwe maan, eerste kwartier, volle maan, laatste "
                                     "kwartier."),
            ("p", "Bij <strong>nieuwe maan</strong> zie je <strong>niets: de maan staat tussen aarde en "
                  "zon</strong>, dus haar verlichte kant wijst van ons weg. Bij <strong>volle maan</strong> "
                  "zie je <strong>de hele verlichte kant van de maan</strong>."),
            ("p", "De orde vanaf nieuwe maan is: <strong>nieuwe maan, eerste kwartier, volle maan, laatste "
                  "kwartier</strong>. Het <strong>eerste kwartier</strong> is de schijngestalte waarbij je "
                  "precies de helft ziet en ze <strong>groeit</strong>. Het <strong>laatste kwartier</strong> "
                  "is de halve maan die elke avond <strong>kleiner</strong> wordt."),
            ("p", "Een <strong>wassende</strong> maan wordt elke avond een stukje groter, een afnemende maan "
                  "elke avond kleiner."),
        ]),
        dict(kop="Eb en vloed", blokken=[
            ("p", "De getijden worden veroorzaakt door <strong>de aantrekking van de maan en de zon</strong>. "
                  "De zon speelt dus wel degelijk een rol, al is haar aandeel ongeveer de helft van dat van "
                  "de maan."),
            ("p", tabel(["woord", "wat het betekent"],
                        [["vloed", "het stijgen van het water"],
                         ["hoogtij of hoogwater", "het hoogste punt"],
                         ["eb", "het zakken van het water"],
                         ["laagtij of laagwater", "het laagste punt"]])),
            ("p", "Het verschil tussen <strong>eb</strong> en <strong>laagtij</strong> zit hem daarin: "
                  "<strong>eb is het zakken, laagtij is het laagste punt</strong>. Aan onze kust is het "
                  "<strong>twee keer</strong> per etmaal hoogtij."),
            ("p", "Staan zon, aarde en maan op één lijn, dan trekken zon en maan samen en krijg je "
                  "<strong>springtij</strong>: <strong>bij springtij is het verschil tussen hoog- en "
                  "laagwater groter dan gewoonlijk</strong>. Dat gebeurt <strong>bij nieuwe maan en bij volle "
                  "maan</strong>. Staan ze in een rechte hoek, dan werken ze tegen elkaar in en krijg je "
                  "<strong>doodtij</strong>, met een klein verschil tussen hoog en laag: <strong>bij het "
                  "eerste en het laatste kwartier</strong>."),
            ("p", "Bij de getijden horen dus de begrippen <strong>vloed</strong>, <strong>springtij</strong> "
                  "en <strong>doodtij</strong>."),
            ("weetje", "Een getijdencentrale werkt op de <strong>getijdenstroom</strong>, niet op de wind "
                       "boven de zee. Ze laat het in- en uitstromende water door turbines gaan. Het voordeel "
                       "is dat getijden tot op de minuut voorspelbaar zijn, anders dan wind."),
        ]),
        dict(kop="Zons- en maansverduisteringen", blokken=[
            ("p", "Bij een <strong>zonsverduistering</strong> staat <strong>de maan</strong> tussen de andere "
                  "twee. Dat kan alleen bij <strong>nieuwe maan</strong>. Bij een "
                  "<strong>maansverduistering</strong> <strong>werpt de aarde haar schaduw op de maan</strong>, "
                  "en dat kan alleen bij volle maan."),
            ("p", "Er is <strong>niet élke maand</strong> een verduistering, <strong>omdat de maanbaan scheef "
                  "staat op de aardbaan</strong>. Meestal schuift de maan er net boven of net onder langs. "
                  "Alleen waar de twee banen elkaar kruisen, in een <strong>knoop</strong>, kan het."),
            ("p", "Voor een <strong>totale zonsverduistering</strong> moeten drie dingen samenvallen: "
                  "<strong>het is nieuwe maan</strong>, <strong>de maan staat dicht bij een knoop van haar "
                  "baan</strong>, en <strong>je staat binnen de kernschaduw van de maan</strong>."),
            ("p", "Over die schaduw: <strong>in de kernschaduw is de zon volledig bedekt</strong>, <strong>in "
                  "de bijschaduw zie je een gedeeltelijke verduistering</strong>, en <strong>de kernschaduw is "
                  "maar een paar honderd km breed</strong>. Daarom is <strong>een maansverduistering op het "
                  "hele nachtelijke halfrond te zien, en een totale zonsverduistering maar in een smalle "
                  "strook</strong>."),
            ("p", "Dat de zon en de maan aan onze hemel ongeveer even groot lijken, is toeval: <strong>de zon "
                  "is veel groter maar staat ook veel verder</strong>. De zon is ongeveer 400 keer zo groot "
                  "én ongeveer 400 keer zo ver."),
            ("p", "Bij een totale maansverduistering ziet de maan er vaak roodachtig uit, want "
                  "<strong>zonlicht wordt door onze atmosfeer rood gebogen</strong> en valt zo toch nog op de "
                  "maan. Je ziet er eigenlijk alle zonsondergangen van de aarde tegelijk op geschenen."),
        ]),
    ])


# ───────────────────────── 6. De opbouw van de atmosfeer
zet("de-opbouw-van-de-atmosfeer",
    titel="De opbouw van de atmosfeer",
    onder="De lagen van de atmosfeer en hun temperatuurverloop, ozon op twee plaatsen, en alle factoren die de temperatuur van een plaats bepalen.",
    secties=[
        dict(kop="De lagen, van beneden naar boven", blokken=[
            ("p", "Van beneden naar boven: <strong>troposfeer, stratosfeer, mesosfeer, thermosfeer, "
                  "exosfeer</strong>. De <strong>exosfeer</strong> is de buitenste laag en gaat over in de "
                  "ruimte."),
            ("p", tabel(["laag", "temperatuur", "wat er zit"],
                        [["troposfeer", "daalt met de hoogte", "het weer, bijna alle waterdamp"],
                         ["stratosfeer", "stijgt met de hoogte", "de ozonlaag"],
                         ["mesosfeer", "daalt weer", "hier verbranden meteoren"],
                         ["thermosfeer", "stijgt sterk", "poollicht, het ISS"],
                         ["exosfeer", "—", "de overgang naar de ruimte"]])),
            ("p", "De <strong>troposfeer</strong> is de onderste laag, en <strong>daar speelt het weer zich "
                  "af</strong>. Drie dingen kloppen over die laag: <strong>bijna alle waterdamp zit "
                  "erin</strong>, <strong>de temperatuur daalt er met de hoogte</strong>, en <strong>ze is "
                  "boven de evenaar dikker dan boven de polen</strong> (ongeveer 17 km tegenover 8 km). De "
                  "grens bovenaan, waar de temperatuurdaling stopt, heet de <strong>tropopauze</strong>."),
            ("p", "In de <strong>stratosfeer</strong> stijgt de temperatuur weer, <strong>omdat ozon daar "
                  "ultraviolette straling opneemt</strong>. <strong>De luchtdruk en de dichtheid van de lucht "
                  "nemen af als je hoger komt</strong>: op tien kilometer hoogte kan je dus "
                  "<strong>niet</strong> zonder hulp ademen, daarom staan vliegtuigcabines onder druk."),
            ("p", "Een verkeersvliegtuig vliegt <strong>niet</strong> in de mesosfeer maar net boven de "
                  "troposfeer, onderaan de stratosfeer. Dat doen ze omdat er <strong>minder turbulentie en "
                  "minder luchtweerstand</strong> is."),
        ]),
        dict(kop="Waar de lucht uit bestaat", blokken=[
            ("p", "Het belangrijkste bestanddeel van droge lucht is <strong>stikstof</strong>, ongeveer 78 %. "
                  "Daarna komt zuurstof, ongeveer <strong>21</strong> %. De laatste procent is vooral argon, "
                  "met daarnaast koolstofdioxide en sporen van andere gassen."),
            ("p", "<strong>Broeikasgassen</strong> in onze atmosfeer zijn onder meer "
                  "<strong>waterdamp</strong>, <strong>koolstofdioxide</strong> en <strong>methaan</strong>. "
                  "Stikstof en zuurstof zijn er géén: die laten warmtestraling gewoon door."),
            ("fig", svg.broeikas(), "Kortgolvige straling komt binnen; de aarde straalt langgolvig terug, en "
                                    "broeikasgassen houden een deel daarvan vast."),
        ]),
        dict(kop="Ozon: nuttig boven, schadelijk beneden", blokken=[
            ("p", "De <strong>ozonlaag</strong> die ons tegen ultraviolet beschermt, zit in de "
                  "<strong>stratosfeer</strong>. Ozon ontstaat daar doordat <strong>ultraviolet licht "
                  "zuurstofmoleculen splitst</strong>: de losse zuurstofatomen hangen zich dan aan andere "
                  "zuurstofmoleculen vast."),
            ("p", "Zit ozon in de <strong>troposfeer</strong>, dicht bij de grond, dan is het juist "
                  "<strong>schadelijk voor longen en gewassen</strong>. Op warme zomerdagen met veel verkeer "
                  "loopt die ozonwaarde op."),
            ("kader", "<strong>Ozon is zowel nuttig als schadelijk, afhankelijk van de laag waar het zit.</strong> "
                      "Dat is geen tegenspraak: boven houdt het straling tegen, beneden tast het weefsel aan."),
        ]),
        dict(kop="De stralingsbalans en het albedo", blokken=[
            ("p", "De <strong>stralingsbalans</strong> beschrijft <strong>de verhouding tussen inkomende en "
                  "uitgaande straling</strong>. Van de zon komt <strong>kortgolvige straling</strong>; de "
                  "aarde straalt langgolvig terug."),
            ("fig", svg.stralingsbalans(), "Wat er binnenkomt en wat er weer weg gaat."),
            ("p", "Het <strong>albedo</strong> is de verhouding van het zonlicht dat een oppervlak "
                  "weerkaatst. Hoe witter en gladder, hoe hoger. <strong>Verse sneeuw</strong> heeft het "
                  "hoogste albedo van de oppervlakken die je moet kennen: ze kaatst tot 90 % terug. Donker "
                  "asfalt en open water kaatsen juist bijna niets terug."),
            ("p", "<strong>Hoe hoger de zon staat, hoe meer energie er per vierkante meter aankomt.</strong> "
                  "Bij een lage zon wordt dezelfde bundel over een groter stuk grond uitgesmeerd."),
        ]),
        dict(kop="Wat de temperatuur van een plaats bepaalt", blokken=[
            ("p", "De vakfiche deelt de factoren in drie groepen in."),
            ("p", "<strong>Uit de rotatie en de revolutie</strong>: <strong>de breedteligging</strong>, "
                  "<strong>de invalshoek van de zonnestralen</strong>, en <strong>het tijdstip van de dag en "
                  "het seizoen</strong>."),
            ("p", "<strong>Geografische factoren</strong>: <strong>de hoogteligging</strong>, <strong>de "
                  "zeestromen</strong> en <strong>de ligging ten opzichte van de zee</strong>."),
            ("p", "<strong>Lokale factoren</strong>: <strong>de helling en de vegetatie</strong>, <strong>de "
                  "bodem en de bewolking</strong>, en <strong>de windrichting</strong>."),
            ("p", "Op de evenaar is het gemiddeld warmer dan bij ons <strong>omdat de zon er veel hoger boven "
                  "de horizon staat</strong>. Met de hoogte daalt de temperatuur met <strong>ongeveer 6,5 "
                  "°C</strong> per kilometer; daarom zijn <strong>hooggebergten koud, ook op de evenaar: de "
                  "lucht is er dunner en koelt sneller af</strong>."),
            ("p", "<strong>Moskou ligt ver van de zee, Oostende eraan.</strong> Daarom is de zomer in Moskou "
                  "warmer en de winter er kouder: water warmt traag op en koelt traag af, en dempt zo de "
                  "uitersten. De <strong>Noord-Atlantische Drift</strong> is de zeestroom die onze winters "
                  "zacht houdt."),
            ("p", "Een <strong>zuidelijke helling</strong> warmt in onze streken sneller op dan een "
                  "noordelijke, <strong>omdat de zon er loodrechter op valt</strong>. En een "
                  "<strong>bewolkte</strong> nacht koelt <strong>minder</strong> sterk af dan een heldere: de "
                  "wolken houden de warmtestraling tegen, als een deken."),
        ]),
        dict(kop="Isothermen en het hitte-eiland", blokken=[
            ("p", "Een <strong>isotherm</strong> is een lijn op een kaart die plaatsen met dezelfde "
                  "temperatuur verbindt. <strong>Liggen de isothermen dicht bij elkaar, dan verandert de "
                  "temperatuur er snel over korte afstand.</strong>"),
            ("p", "In een stad is het vaak warmer dan in de velden errond, <strong>omdat steen en asfalt de "
                  "warmte van de dag opslaan</strong> en 's nachts weer afgeven. Daar komt bij dat er weinig "
                  "groen en water is om te verdampen. Dat verschijnsel heet het "
                  "<strong>hitte-eilandeffect</strong>."),
            ("p", "De warmste tijd van de dag valt <strong>niet</strong> samen met het moment dat de zon het "
                  "hoogst staat. De grond blijft daarna nog warmte opnemen, dus de top ligt meestal een uur "
                  "of drie later, rond half drie."),
        ]),
    ])


# ───────────────────────── 7. Luchtdruk en winden
zet("luchtdruk-en-winden",
    titel="Luchtdruk en winden",
    onder="Hoge en lage druk op een weerkaart, de drukgordels en de passaten, de straalstroom, en de wind aan de kust.",
    secties=[
        dict(kop="Wat luchtdruk is", blokken=[
            ("p", "<strong>Luchtdruk</strong> is <strong>het gewicht van de luchtkolom boven een "
                  "plaats</strong>. Op een weerkaart staat hij in <strong>hPa</strong>, hectopascal. De "
                  "gemiddelde luchtdruk aan het zeeniveau is <strong>1013</strong> hPa."),
            ("p", "Beklim je een berg, dan <strong>daalt de luchtdruk, omdat er dan minder lucht boven je "
                  "staat</strong>. Je draagt een kleiner stuk van de luchtkolom."),
            ("p", "Een <strong>isobaar</strong> is een lijn op een weerkaart die plaatsen met dezelfde "
                  "luchtdruk verbindt. <strong>Liggen de isobaren heel dicht bij elkaar, dan waait het er "
                  "hard</strong>: de druk verandert dan sterk over korte afstand, en dat verschil duwt de "
                  "lucht voort."),
        ]),
        dict(kop="Hoge en lage druk", blokken=[
            ("fig", svg.drukgebieden(), "Bij lage druk stijgt de lucht op en draait de wind tegen de klok "
                                        "in; bij hoge druk daalt ze en draait de wind met de klok mee."),
            ("p", "Een <strong>lagedrukgebied</strong> ontstaat boven een warm oppervlak doordat "
                  "<strong>warme lucht opstijgt en de druk aan de grond daalt</strong>. <strong>In een "
                  "lagedrukgebied stijgt de lucht op, en daarom regent het er vaak</strong>: stijgende lucht "
                  "koelt af en haar damp slaat neer."),
            ("p", "Drie woorden betekenen hetzelfde: <strong>depressie</strong>, "
                  "<strong>lagedrukgebied</strong> en <strong>minimum</strong>. Een "
                  "<strong>anticycloon</strong> is het omgekeerde: <strong>een gebied met hoge "
                  "luchtdruk</strong>, ook maximum genoemd."),
            ("p", "Over drukgebieden geldt: <strong>in een maximum daalt de lucht</strong>, <strong>in een "
                  "minimum stijgt de lucht</strong>, en <strong>lucht stroomt van hoge naar lage "
                  "druk</strong>. Een hogedrukgebied geeft in de winter bij ons dus géén zware regen, maar "
                  "droog, vaak mistig en koud weer."),
            ("p", "Er staat <strong>wind door een verschil in luchtdruk</strong>. De wind waait echter "
                  "<strong>niet recht van hoog naar laag</strong>, en dat komt door <strong>het "
                  "corioliseffect</strong>. Op het noordelijk halfrond draait de wind daardoor "
                  "<strong>tegen de klok in</strong> rond een lagedrukgebied en <strong>met de klok "
                  "mee</strong> rond een hogedrukgebied. <strong>Op het zuidelijk halfrond draait de wind "
                  "rond een depressie met de klok mee.</strong>"),
            ("p", "Een wind heet naar de richting waar hij <strong>vandaan</strong> komt. Over een "
                  "<strong>noordenwind</strong> geldt dus: <strong>hij komt uit het noorden</strong>, "
                  "<strong>hij blaast naar het zuiden</strong>, en <strong>hij brengt bij ons koude lucht "
                  "mee</strong>."),
            ("kader", "Een stormdepressie met een centrale druk van 960 hPa: dat is ruim vijftig hectopascal "
                      "onder normaal, dus <strong>de depressie is heel diep en dus krachtig</strong>. Hoe "
                      "lager de kerndruk, hoe sterker de wind eromheen. De <strong>schaal van "
                      "Beaufort</strong> geeft trouwens niet de druk maar de <strong>windkracht</strong>."),
        ]),
        dict(kop="De drukgordels van de aarde", blokken=[
            ("p", "Van de evenaar naar de pool liggen er gordels: het <strong>equatoriaal minimum</strong>, "
                  "het <strong>subtropisch maximum</strong>, het <strong>subpolair minimum</strong> en het "
                  "polair maximum."),
            ("p", "Rond de evenaar ligt een gordel van lage druk <strong>omdat de sterke opwarming de lucht "
                  "er laat opstijgen</strong>. De <strong>subtropische maxima</strong> liggen <strong>rond "
                  "30° noorder- en zuiderbreedte</strong>; daar komt de opgestegen lucht weer naar beneden. "
                  "Daarom liggen <strong>de grote woestijnen rond 30° breedte: daar daalt droge lucht "
                  "neer</strong>, en dalende lucht geeft geen regen."),
            ("p", "<strong>Een thermische drukgordel ontstaat door opwarming of afkoeling, een dynamische "
                  "door op- of neergaande lucht van de circulatie.</strong> Het equatoriaal minimum is dus "
                  "thermisch, het subtropisch maximum dynamisch."),
            ("p", "Een <strong>circulatiecel</strong> is <strong>een kringloop van op- en dalende "
                  "lucht</strong>. Tussen de evenaar en 30° draait de cel van Hadley, daarboven volgen de "
                  "Ferrelcel en de poolcel."),
        ]),
        dict(kop="Passaten, ITCZ en de straalstroom", blokken=[
            ("p", "De <strong>passaatwinden</strong> waaien van de subtropen naar de evenaar. Op het "
                  "noordelijk halfrond komen ze <strong>uit het noordoosten</strong>, want het corioliseffect "
                  "buigt ze naar rechts af. Op het zuidelijk halfrond buigt het ze juist <strong>naar "
                  "links</strong> af, dus komen ze daar uit het zuidoosten."),
            ("p", "Waar de passaten van beide halfronden samenkomen, ligt de <strong>ITCZ</strong>, de "
                  "intertropische convergentiezone. Daarover geldt: <strong>ze schuift mee met de zenitale "
                  "zon</strong>, <strong>er valt veel convectieve regen</strong>, en <strong>de passaten van "
                  "beide halfronden komen er samen</strong>."),
            ("p", "De <strong>straalstroom</strong> is <strong>een smalle band zeer snelle "
                  "hoogtewind</strong>, op ongeveer tien kilometer hoogte. <strong>De straalstroom stuurt de "
                  "banen van de depressies over Europa.</strong> Bij ons komt de meest voorkomende wind "
                  "<strong>uit het zuidwesten</strong>."),
            ("p", "De vakfiche noemt als oorzaken van de luchtdrukverschillen en de winden: <strong>de "
                  "algemene luchtcirculatie</strong>, <strong>de ITCZ en de straalstroom</strong>, en "
                  "<strong>het corioliseffect en de land- en zeewinden</strong>."),
            ("p", "Orkanen ontstaan niet pal op de evenaar, <strong>omdat het corioliseffect daar te klein "
                  "is</strong> om de lucht aan het draaien te krijgen."),
        ]),
        dict(kop="Zeewind, landwind en moesson", blokken=[
            ("p", "Op een warme zomerdag ontstaat een <strong>zeewind</strong> doordat <strong>het land "
                  "sneller opwarmt dan de zee</strong>. Boven het land stijgt de lucht, de druk daalt er, en "
                  "koelere zeelucht stroomt toe."),
            ("p", "'s Nachts keert het om: het land koelt sneller af dan de zee, en <strong>de lucht stroomt "
                  "van het land naar de zee</strong>. Die wind heet de <strong>landwind</strong>."),
            ("p", "Een <strong>moesson</strong> werkt op hetzelfde beginsel, maar met de seizoenen in plaats "
                  "van met de dag: hij draait <strong>twee keer per jaar</strong> van richting, niet twee "
                  "keer per dag. In de zomer waait hij van de koelere oceaan naar het hete vasteland en "
                  "brengt hij de regens, in de winter andersom."),
        ]),
    ])


# ───────────────────────── 8. Neerslag en de kringloop van het water
zet("neerslag-en-de-kringloop-van-het-water",
    titel="Neerslag en de kringloop van het water",
    onder="De hydrologische cyclus, vochtigheid en dauwpunt, de drie soorten regen, en wat de neerslag op aarde verdeelt.",
    secties=[
        dict(kop="De hydrologische cyclus", blokken=[
            ("p", "De kringloop van het water op aarde heet de <strong>hydrologische cyclus</strong>. De "
                  "stappen die erbij horen: <strong>verdamping</strong>, <strong>condensatie</strong> en "
                  "<strong>neerslag</strong>, met daarna afstroming en infiltratie."),
            ("fig", svg.watercyclus(), "Verdampen, condenseren, neerslaan, afstromen en infiltreren."),
            ("p", "<strong>Verdamping</strong> is de overgang van vloeibaar water naar waterdamp; "
                  "<strong>condensatie</strong> is het omgekeerde: <strong>waterdamp wordt vloeibaar "
                  "water</strong>. Boven de oceanen verdampt er zoveel <strong>omdat daar een eindeloos "
                  "groot wateroppervlak is</strong>."),
            ("p", "Regenwater komt in het grondwater terecht <strong>door infiltratie in de bodem</strong>. "
                  "<strong>Verharding van de bodem vermindert de infiltratie en vergroot de "
                  "afstroming</strong>: op beton kan niets wegzakken, dus loopt alles ineens naar de riool."),
            ("p", "Bomen doen in die kringloop drie dingen: <strong>ze geven water af via hun "
                  "bladeren</strong>, <strong>ze houden regenwater tegen voor het de grond raakt</strong>, en "
                  "<strong>ze helpen het water in de bodem dringen</strong> met hun wortels."),
        ]),
        dict(kop="Vochtigheid, dauwpunt en wolken", blokken=[
            ("p", "De <strong>absolute luchtvochtigheid</strong> is <strong>de hoeveelheid damp per kubieke "
                  "meter lucht</strong>. De relatieve luchtvochtigheid zegt hoeveel damp er zit ten opzichte "
                  "van wat die lucht bij die temperatuur kán dragen; <strong>100 procent</strong> betekent "
                  "dus dat <strong>de lucht met damp verzadigd is</strong>."),
            ("p", "<strong>Warme lucht kan meer waterdamp vasthouden dan koude lucht.</strong> Daarom is er "
                  "een temperatuur waarbij lucht verzadigd raakt als je haar afkoelt: het "
                  "<strong>dauwpunt</strong>."),
            ("p", "'s Morgens hangt er vaak mist boven een weide <strong>omdat de lucht tot onder haar "
                  "dauwpunt is afgekoeld</strong>. Het verschil met nevel zit in het zicht: bij <strong>mist "
                  "zie je minder ver dan bij nevel</strong>, dus mist is de dichtste van de twee."),
            ("p", "Wolken vormen zich vooral in stijgende lucht <strong>omdat stijgende lucht uitzet en "
                  "daardoor afkoelt</strong>. Waterdamp condenseert dan <strong>op kleine stof- en "
                  "zoutdeeltjes</strong>."),
            ("kader", "Een wolk bestaat <strong>niet</strong> uit waterdamp. Damp is een onzichtbaar gas. Wat "
                      "je ziet zijn piepkleine <strong>druppeltjes en ijskristallen</strong>; precies omdat "
                      "de damp al gecondenseerd is, wordt de wolk zichtbaar."),
        ]),
        dict(kop="Neerslag meten", blokken=[
            ("p", "Neerslag wordt gemeten in <strong>millimeter</strong>. Eén millimeter neerslag is "
                  "<strong>1</strong> liter water per vierkante meter: een laagje van één millimeter over één "
                  "vierkante meter is precies één liter."),
            ("p", "In België kan je <strong>regen</strong>, <strong>sneeuw</strong> en <strong>hagel</strong> "
                  "meemaken, en daarnaast motregen, ijzel en natte sneeuw."),
            ("p", "In Ukkel valt er gemiddeld ongeveer <strong>850</strong> mm neerslag per jaar. Die valt "
                  "<strong>niet</strong> vooral in de zomer: bij ons valt er in <strong>alle maanden</strong> "
                  "neerslag, met hooguit een licht accent in de late herfst."),
        ]),
        dict(kop="Drie soorten regen", blokken=[
            ("p", tabel(["soort", "hoe hij ontstaat"],
                        [["convectieregen", "sterk opwarmende lucht stijgt op"],
                         ["stijgingsregen", "lucht wordt tegen een gebergte opgedwongen"],
                         ["frontale regen", "warme en koude lucht ontmoeten elkaar"]])),
            ("p", "Die drie noemt de vakfiche: <strong>convectieregens</strong>, "
                  "<strong>stijgingsregens</strong> en <strong>frontale regens</strong>. Rond de evenaar "
                  "regent het zoveel <strong>omdat de sterk opgewarmde lucht er dagelijks opstijgt</strong>: "
                  "dat is convectie, elke namiddag opnieuw."),
            ("p", "Bij een gebergte: <strong>de loefzijde krijgt de stijgingsregens</strong>, <strong>aan de "
                  "lijzijde ligt de regenschaduw</strong>, en <strong>dalende lucht aan de lijzijde droogt "
                  "uit</strong>. Lucht die aan de lijzijde weer afdaalt <strong>warmt op en droogt verder "
                  "uit</strong>. Het droge gebied achter een gebergte heet de <strong>regenschaduw</strong>."),
            ("p", "In de Ardennen valt er meer neerslag dan in Vlaanderen <strong>omdat de lucht er omhoog "
                  "moet en afkoelt</strong>. In een hooggebergte sneeuwt het vaker dan in de vallei, "
                  "<strong>omdat het er kouder is dan in de vallei</strong>."),
            ("p", "<strong>In een lagedrukgebied valt er gemiddeld meer neerslag dan in een "
                  "hogedrukgebied.</strong>"),
        ]),
        dict(kop="Wat de neerslag op aarde verdeelt", blokken=[
            ("p", "De vakfiche noemt drie groepen factoren: <strong>hoge of lage luchtdruk</strong>, "
                  "<strong>de zeestromen langs de kust</strong>, en <strong>het reliëf en de ligging ten "
                  "opzichte van de zee</strong>."),
            ("p", "Een <strong>koude zeestroom maakt een kust droger</strong>: de lucht erboven koelt van "
                  "onderen af, blijft laag hangen en stijgt niet op. Daarom is de Atacamawoestijn zo droog: "
                  "<strong>een koude zeestroom en een regenschaduw samen</strong>."),
            ("p", "<strong>Een gebied ver van de zee krijgt meestal minder neerslag dan een kustgebied op "
                  "dezelfde breedte.</strong> De vochtige lucht heeft dan onderweg al haar water afgegeven."),
            ("p", "Een <strong>isohyeet</strong> is een lijn op een kaart die plaatsen met dezelfde neerslag "
                  "verbindt, niet met dezelfde temperatuur. <strong>Liggen de isohyeten ver uit elkaar, dan "
                  "verandert de neerslag er traag over de afstand.</strong>"),
        ]),
    ])


# ───────────────────────── 9. Klimaatgebieden, biomen en zeestromen
zet("klimaatgebieden-biomen-en-zeestromen",
    titel="Klimaatgebieden, biomen en zeestromen",
    onder="Van klimatogram naar bioom, van taiga tot savanne, en hoe de zeestromen en de thermohaliene circulatie het klimaat van de kusten maken.",
    secties=[
        dict(kop="Weer en klimaat", blokken=[
            ("p", "<strong>Weer is nu, klimaat is het gemiddelde over jaren.</strong> Een klimaat wordt "
                  "gewoonlijk over <strong>30</strong> jaar gemiddeld. De klimaatindeling van de aarde is "
                  "gebaseerd <strong>op temperatuur en neerslag</strong>."),
            ("p", "Op een <strong>klimatogram</strong> lees je <strong>de temperatuur en de neerslag per "
                  "maand</strong> af. <strong>Valt de warmste maand in juni of juli, dan hoort het bij het "
                  "noordelijk halfrond</strong>; valt ze in januari, dan bij het zuidelijk."),
            ("p", "<strong>Twee plaatsen op dezelfde breedte hebben niet altijd hetzelfde klimaat.</strong> "
                  "De zee, de zeestromen, het reliëf en de hoogte maken het verschil. Daarom is het bij ons "
                  "in de winter zachter dan in Newfoundland, op dezelfde breedte: <strong>de warme drift en "
                  "de westenwind samen</strong>."),
            ("p", "In een <strong>continentaal</strong> klimaat is <strong>het verschil tussen de warmste en "
                  "de koudste maand groter dan in een zeeklimaat</strong>."),
        ]),
        dict(kop="De biomen", blokken=[
            ("p", tabel(["bioom", "klimaat"],
                        [["tropisch regenwoud", "het hele jaar warm en nat"],
                         ["savanne", "warm, met een droge en een natte tijd"],
                         ["woestijn", "te weinig neerslag voor planten"],
                         ["steppe", "droog grasland van de gematigde streken"],
                         ["taiga", "naaldbos van de koude, noordelijke streken"],
                         ["toendra", "tussen de taiga en de poolwoestijn"],
                         ["poolwoestijn", "ijzig koud en kurkdroog"]])),
            ("p", "De vakfiche noemt als voorbeeld <strong>de taiga</strong>, <strong>de "
                  "poolwoestijn</strong> en <strong>de savanne</strong>. Het <strong>tropisch "
                  "regenwoud</strong> hoort bij een klimaat met het hele jaar hoge temperaturen en veel "
                  "neerslag; zie je een klimatogram met twaalf maanden boven 25 °C en elke maand meer dan "
                  "150 mm regen, dan is dat dus regenwoud."),
            ("p", "In een <strong>woestijn</strong> groeien zo weinig planten <strong>omdat er te weinig "
                  "neerslag valt</strong>. In een <strong>poolwoestijn</strong> valt er trouwens ook heel "
                  "<strong>weinig</strong> neerslag: het ijs ligt er omdat wat er valt nooit smelt, niet "
                  "omdat er veel valt."),
            ("p", "De <strong>toendra</strong> heeft een permanent bevroren ondergrond: de "
                  "<strong>permafrost</strong>. Daardoor kan water niet wegzakken en staan er 's zomers "
                  "plassen op een bevroren bodem."),
            ("p", "Het <strong>mediterraan</strong> klimaat herken je aan <strong>droge zomers en zachte, "
                  "natte winters</strong>. Het klimaat van <strong>België</strong> kenmerkt zich door "
                  "<strong>zachte winters voor onze breedte</strong>, <strong>koele zomers zonder lange "
                  "hitte</strong> en <strong>neerslag in alle maanden van het jaar</strong>."),
            ("p", "Bij de culminatiehoogte en de daglengte noemt de vakfiche <strong>de polaire "
                  "klimaten</strong>, <strong>de gematigde klimaten</strong> en <strong>de tropische "
                  "klimaten</strong>."),
        ]),
        dict(kop="Zeestromen", blokken=[
            ("p", "<strong>Zeestromen</strong> zijn <strong>grote, blijvende stromingen in de "
                  "oceanen</strong>. Aan het oppervlak worden ze vooral aangedreven door <strong>de vaste "
                  "winden boven de oceanen</strong>, en ze worden <strong>afgebogen door het "
                  "corioliseffect</strong>. De grote oceaankringen draaien op het noordelijk halfrond "
                  "<strong>met de klok mee</strong>."),
            ("p", "Over zeestromen geldt: <strong>ze vervoeren warmte van de evenaar naar de polen</strong>, "
                  "<strong>ze beïnvloeden het klimaat van de kusten</strong>, en <strong>ze worden afgebogen "
                  "door het corioliseffect</strong>. Een zeestroom heeft dus wel degelijk invloed op de "
                  "temperatuur van de kust erlangs."),
            ("p", "De <strong>Golfstroom</strong> vertrekt vanuit de Golf van Mexico; zijn verlengde, de "
                  "<strong>Noord-Atlantische Drift</strong>, brengt warm water tot bij West-Europa. "
                  "<strong>Zonder de Noord-Atlantische Drift zouden onze winters een stuk strenger "
                  "zijn.</strong> Een <strong>warme zeestroom maakt de kust erlangs zachter en "
                  "vochtiger</strong>."),
            ("p", "<strong>Koude</strong> stromen zijn onder meer <strong>de Labradorstroom</strong>, "
                  "<strong>de Humboldtstroom</strong> en <strong>de Benguelastroom</strong>. De "
                  "<strong>Humboldtstroom</strong> loopt langs de kust van Peru en Chili. Daardoor liggen er "
                  "<strong>woestijnen pal aan de kust van Namibië en Peru: een koude zeestroom houdt de "
                  "lucht beneden</strong>, zodat ze niet kan opstijgen en regen geven."),
            ("p", "<strong>Opwelling</strong> is het verschijnsel waarbij <strong>koud, voedselrijk "
                  "diepwater naar boven komt</strong>. Daar zitten de rijkste visgronden ter wereld."),
        ]),
        dict(kop="De thermohaliene circulatie", blokken=[
            ("p", "De wereldwijde kringloop van water die door temperatuur en zoutgehalte gedreven wordt, "
                  "heet de <strong>thermohaliene circulatie</strong>. Thermo staat voor warmte, halien voor "
                  "zout."),
            ("p", "<strong>Water wordt zwaarder als het kouder en zouter wordt.</strong> Daarom "
                  "<strong>zinkt het in de koude noordelijke Atlantische Oceaan</strong>, bij Groenland en "
                  "IJsland, en kruipt het als diepwater terug naar het zuiden."),
            ("p", "<strong>Smeltwater van Groenland maakt het zeewater net zoeter</strong>, niet zouter. "
                  "Zoeter water is lichter, zakt minder goed, en <strong>remt</strong> de circulatie dus af."),
            ("p", "Valt de thermohaliene circulatie stil, dan <strong>zou het in West-Europa merkelijk "
                  "kouder worden</strong>. De gevolgen die de vakfiche noemt: <strong>koudere winters in "
                  "West-Europa</strong>, <strong>een verschuiving van de regengordels</strong>, en "
                  "<strong>minder zuurstof in het diepe water</strong>."),
        ]),
    ])


# ───────────────────────── 10. Het weer in Europa
zet("het-weer-in-europa",
    titel="Het weer in Europa",
    onder="Fronten en luchtsoorten, de doortocht van een depressie, en hoe je van een weerkaart met isobaren een voorspelling afleidt.",
    secties=[
        dict(kop="Fronten", blokken=[
            ("p", "Een <strong>front</strong> is <strong>de grens tussen twee luchtsoorten</strong>. Omdat "
                  "warme en koude lucht zich niet mengen, schuiven ze over en onder elkaar, en net op die "
                  "grens valt de neerslag."),
            ("p", tabel(["front", "wat er gebeurt", "het weer"],
                        [["warmtefront", "warme lucht schuift traag over koude", "lange, gelijkmatige regen"],
                         ["koufront", "koude lucht duikt onder de warme", "korte, hevige buien"],
                         ["occlusiefront", "het koufront haalt het warmtefront in", "de depressie loopt op haar einde"]])),
            ("p", "Bij een <strong>warmtefront</strong> horen <strong>een flauwe helling van het "
                  "frontvlak</strong>, <strong>langdurige, gelijkmatige neerslag</strong> en <strong>hoge "
                  "sluierwolken vooraf</strong>. Die <strong>hoge sluierwolken</strong> komen dus als eerste "
                  "aan, soms een dag voor de regen."),
            ("p", "Een <strong>koufront geeft gewoonlijk kortere maar hevigere neerslag dan een "
                  "warmtefront</strong>, want de koude lucht wrikt de warme snel en steil omhoog."),
            ("p", "Bij een <strong>occlusiefront</strong> geldt: <strong>het koufront heeft het warmtefront "
                  "ingehaald</strong>, <strong>de warme lucht is van de grond getild</strong>, en <strong>de "
                  "depressie is aan haar einde toe</strong>."),
            ("p", "Tussen het warmtefront en het koufront van een depressie ligt de <strong>warme "
                  "sector</strong>: zacht, vochtig en vaak grijs."),
        ]),
        dict(kop="Luchtsoorten", blokken=[
            ("p", "De vakfiche noemt drie luchtsoorten naar hun herkomst: <strong>arctisch</strong>, "
                  "<strong>polair</strong> en <strong>tropisch</strong>. Daar komt telkens bij of ze over "
                  "zee of over land is getrokken: <strong>maritiem</strong> of <strong>continentaal</strong>."),
            ("p", "<strong>Maritiem polaire lucht</strong> is dus <strong>koude lucht die over de oceaan is "
                  "getrokken</strong>: koel en vochtig. <strong>Continentale lucht is droger dan maritieme "
                  "lucht van dezelfde herkomst</strong>, want boven land neemt ze geen vocht op."),
            ("p", tabel(["luchtsoort", "wat ze bij ons brengt"],
                        [["arctisch", "de koudste lucht die ons kan bereiken"],
                         ["continentaal polair", "strenge vorst in de winter"],
                         ["maritiem polair", "koele buien, wisselvallig"],
                         ["maritiem tropisch", "zacht, vochtig en zwaarbewolkt"],
                         ["continentaal tropisch", "een hittegolf in de zomer"]])),
        ]),
        dict(kop="Een depressie trekt voorbij", blokken=[
            ("p", "De depressies die ons weer bepalen ontstaan <strong>op het polaire front boven de "
                  "oceaan</strong>, waar koude polaire en zachte tropische lucht elkaar raken. Ze bewegen "
                  "bij ons <strong>van west naar oost</strong>, niet omgekeerd."),
            ("p", "De doortocht verloopt in deze orde: <strong>warmtefront, warme sector, koufront</strong>. "
                  "Bij de passage van het <strong>koufront draait de wind en wordt hij plots "
                  "krachtiger</strong>. Daarna wordt het <strong>niet</strong> zachter met een hele dag "
                  "bewolking: er komt juist koelere lucht met opklaringen en stapelwolken, met hier en daar "
                  "een bui."),
            ("p", "Trekt een depressie ten noorden van ons voorbij, dan draait de wind <strong>van zuidwest "
                  "naar west en noordwest</strong>."),
            ("p", "Het weer in België is zo wisselvallig <strong>omdat wij in de baan van de depressies "
                  "liggen</strong>, tussen de oceaan en het vasteland in."),
        ]),
        dict(kop="Een weerkaart lezen", blokken=[
            ("p", "De <strong>isobaren</strong> op een weerkaart zijn <strong>lijnen van gelijke "
                  "luchtdruk</strong>. Een <strong>H</strong> of een <strong>A</strong> boven een gebied is "
                  "<strong>een hogedrukkern</strong>; een L of een D is een lagedrukkern."),
            ("p", "Liggen de isobaren <strong>dicht bij elkaar</strong>, dan betekent dat <strong>harde "
                  "wind</strong>. De wind staat daarbij <strong>bijna parallel met de isobaren</strong>, niet "
                  "er dwars op: het corioliseffect buigt hem af. <strong>Uit een weerkaart met isobaren kan "
                  "je dus de windrichting en de windkracht afleiden.</strong>"),
            ("p", "De fiche noemt de tekens die op een weerkaart staan: <strong>koufront en "
                  "warmtefront</strong>, <strong>occlusiefront en neerslagzones</strong>, en <strong>drukkernen "
                  "en isobaren</strong>. Die <strong>neerslagzones liggen rond de fronten van een "
                  "depressie</strong>, niet rond de kern van een hogedrukgebied: daar is het juist droog."),
            ("p", "Staan er ook <strong>isothermen</strong> op, dan lees je er <strong>de luchtdruk</strong>, "
                  "<strong>de temperatuur</strong> en <strong>de drukkernen</strong> van af. De "
                  "<strong>luchtsoort</strong> rond een drukgebied zegt je <strong>welke temperatuur en "
                  "vochtigheid er komt</strong>."),
            ("p", "Om van een weerkaart een voorspelling af te leiden heb je drie dingen nodig: <strong>de "
                  "ligging van de drukgebieden</strong>, <strong>de stand en de zin van de fronten</strong>, "
                  "en <strong>de richting waarin alles verschuift</strong>. Zo'n kaart met de verwachte "
                  "toestand van de atmosfeer voor een bepaald uur heet een "
                  "<strong>prognosekaart</strong> of synoptische kaart."),
            ("kader", "Twee voorbeelden om te oefenen. Een depressie ten westen van Ierland die naar het "
                      "oosten trekt, geeft morgen bij ons <strong>regen en toenemende wind</strong>. Een "
                      "hogedrukgebied pal boven Scandinavië in januari geeft bij ons <strong>een droge "
                      "oostenwind met vorst</strong>: rond een maximum draait de wind met de klok mee, dus "
                      "komt hij uit het oosten, over bevroren land."),
        ]),
        dict(kop="De straalstroom en de grenzen van een voorspelling", blokken=[
            ("p", "De <strong>straalstroom</strong> is de smalle band zeer snelle wind op tien kilometer "
                  "hoogte. Hij <strong>stuurt de baan van de depressies</strong>, en daarom kijkt een "
                  "weerman eerst naar de hoogtekaart ervan: <strong>die bepaalt waar de storingen naartoe "
                  "trekken</strong>."),
            ("p", "<strong>Als de straalstroom sterk golft, kan hetzelfde weertype weken bij ons blijven "
                  "hangen.</strong> Een diepe golf houdt een hogedrukgebied of een depressie op zijn plaats."),
            ("p", "Een weersvoorspelling voor volgende week is <strong>niet</strong> even betrouwbaar als "
                  "een voor morgen. De atmosfeer versterkt kleine onzekerheden, dus hoe verder vooruit, hoe "
                  "ruwer de voorspelling."),
        ]),
    ])


# ───────────────────────── 11. De opbouw van de geosfeer
zet("de-opbouw-van-de-geosfeer",
    titel="De opbouw van de geosfeer",
    onder="De chemische en de fysische indeling van de aarde, hoe we dat met aardbevingsgolven te weten kwamen, en het verschil tussen de twee soorten korst.",
    secties=[
        dict(kop="De chemische indeling: korst, mantel en kern", blokken=[
            ("p", "De chemische indeling kijkt naar waar de aarde van gemaakt is en onderscheidt drie lagen: "
                  "<strong>korst, mantel en kern</strong>. Van buiten naar binnen: <strong>korst, mantel, "
                  "buitenkern, binnenkern</strong>."),
            ("p", tabel(["laag", "diepte", "kenmerk"],
                        [["korst", "30 tot 70 km onder een continent", "dun en licht"],
                         ["mantel", "tot ongeveer 2 900 km", "het grootste deel van het volume"],
                         ["buitenkern", "tot ongeveer 5 150 km", "vloeibaar"],
                         ["binnenkern", "tot ongeveer 6 370 km", "vast door de hoge druk"]])),
            ("p", "De straal van de aarde is ongeveer <strong>6400</strong> km. De <strong>mantel</strong> "
                  "is de laag onder de korst die het grootste deel van het volume vult. De <strong>kern "
                  "bestaat vooral uit ijzer en nikkel</strong>: <strong>ze bestaat vooral uit ijzer</strong>, "
                  "<strong>de buitenkern is vloeibaar</strong> en <strong>de binnenkern is vast door de hoge "
                  "druk</strong>. De grens tussen mantel en kern ligt <strong>ongeveer 2 900 km</strong> diep."),
            ("p", "De aarde heeft een magneetveld <strong>omdat de vloeibare buitenkern beweegt</strong>: "
                  "stromend ijzer wekt een veld op. <strong>De temperatuur in de aarde neemt toe met de "
                  "diepte.</strong>"),
            ("p", "Twee grenzen hebben een naam. De grens tussen de korst en de mantel is de "
                  "<strong>Mohorovicic</strong>discontinuïteit, kortweg de <strong>Moho</strong>. De grens "
                  "tussen de mantel en de kern is <strong>de Gütenbergdiscontinuïteit</strong> (ook "
                  "geschreven als Gutenberg)."),
        ]),
        dict(kop="De fysische indeling: lithosfeer en asthenosfeer", blokken=[
            ("p", "De fysische indeling kijkt niet naar de samenstelling maar naar hoe het gesteente zich "
                  "<strong>gedraagt</strong>. Daarbij horen <strong>de lithosfeer</strong>, <strong>de "
                  "asthenosfeer</strong> en <strong>de mesosfeer of ondermantel</strong>."),
            ("p", "De <strong>lithosfeer</strong> is de buitenste, vaste laag: <strong>de korst en de "
                  "bovenste mantel</strong> samen. Ze is <strong>niet</strong> één aaneengesloten geheel: ze "
                  "ligt in stukken, de tektonische platen."),
            ("p", "De <strong>asthenosfeer</strong> daaronder <strong>is kneedbaar en stroomt heel "
                  "langzaam</strong>. Ze bestaat dus <strong>niet</strong> volledig uit vloeibaar magma: het "
                  "is vast gesteente dat zich over duizenden jaren als stroop gedraagt. De "
                  "<strong>mesosfeer</strong> in deze indeling is <strong>de ondermantel onder de "
                  "asthenosfeer</strong>; verwar hem niet met de mesosfeer van de atmosfeer."),
            ("p", "De vakfiche noemt bij de opbouw van de geosfeer dus zowel <strong>lithosfeer en "
                  "asthenosfeer</strong> als <strong>korst, mantel en kern</strong> en <strong>binnenkern en "
                  "buitenkern</strong>."),
        ]),
        dict(kop="Hoe we dat weten: seismische golven", blokken=[
            ("p", "We weten hoe de aarde er binnenin uitziet <strong>uit de weg die aardbevingsgolven "
                  "afleggen</strong>. Niemand is ooit dieper geweest dan een boorgat van enkele kilometer: "
                  "<strong>de diepste boring ter wereld is niet tot in de mantel geraakt</strong>."),
            ("p", "De wetenschap die aardbevingen en hun golven onderzoekt is de "
                  "<strong>seismologie</strong>; het toestel dat de golven registreert is een "
                  "<strong>seismograaf</strong>."),
            ("fig", svg.aardbeving(), "Vanuit het hypocentrum lopen de golven door de aarde; hun weg "
                                      "verraadt wat eronder ligt."),
            ("p", "<strong>Wordt het gesteente dichter, dan gaan de golven sneller.</strong> Daarom is "
                  "<strong>de Moho ontdekt doordat seismische golven er plots sneller gingen</strong>."),
            ("p", "<strong>Dwarsgolven gaan niet door de buitenkern, omdat die vloeibaar is.</strong> Een "
                  "vloeistof kan geen schuifkracht doorgeven. Dat is het bewijs dat de buitenkern vloeibaar "
                  "is, zonder dat iemand er ooit was."),
        ]),
        dict(kop="Twee soorten korst", blokken=[
            ("p", "De vakfiche vergelijkt de continentale met de oceanische korst op <strong>de "
                  "dichtheid</strong>, <strong>de dikte</strong> en <strong>de opbouw en de "
                  "samenstelling</strong>."),
            ("p", tabel(["", "continentale korst", "oceanische korst"],
                        [["dikte", "dikker, 30 tot 70 km", "dunner, 5 tot 10 km"],
                         ["dichtheid", "lichter", "zwaarder per kubieke meter"],
                         ["gesteente", "vooral graniet", "vooral basalt"],
                         ["ouderdom", "ouder, tot miljarden jaren", "nergens ouder dan ~200 miljoen jaar"]])),
            ("p", "Over de <strong>oceanische korst</strong> geldt dus: <strong>ze bestaat vooral uit "
                  "basalt</strong>, <strong>ze is dunner dan de continentale korst</strong> en <strong>ze "
                  "heeft een hogere dichtheid</strong>. Over de <strong>sedimentlaag</strong> erbovenop: "
                  "<strong>ze ligt boven op de basaltkorst</strong>, <strong>ze bestaat uit slib, zand en "
                  "resten van zeeleven</strong>, en <strong>ze is dikker naarmate je verder van de rug "
                  "komt</strong>, want daar ligt de bodem al langer stil."),
            ("p", "Het diepste punt van de oceaan ligt ongeveer <strong>11</strong> kilometer diep, in de "
                  "Marianentrog."),
        ]),
        dict(kop="Isostasie", blokken=[
            ("p", "<strong>Isostasie</strong> is <strong>het evenwicht van de korst op de mantel</strong>. "
                  "De korst drijft als het ware op de kneedbare asthenosfeer, zoals een ijsschots op water."),
            ("p", "Daaruit volgt iets wat tegen je gevoel in gaat: een <strong>hooggebergte heeft onder zich "
                  "juist een dikkere korst dan een vlakte</strong>, geen dunnere. Wat je boven ziet is maar "
                  "het topje; eronder zit een wortel die het draagt."),
            ("p", "<strong>Scandinavië stijgt nog altijd een paar millimeter per jaar omdat de last van de "
                  "ijskap is weggevallen.</strong> De korst veert traag terug omhoog, tienduizend jaar na "
                  "de ijstijd."),
        ]),
    ])


# ───────────────────────── 12. Platentektoniek en reliëfvorming
zet("platentektoniek-en-reliefvorming",
    titel="Platentektoniek en reliëfvorming",
    onder="Van Pangea tot vandaag, de drie plaatbewegingen en hun drijvende krachten, en het reliëf dat eruit volgt.",
    secties=[
        dict(kop="Pangea en de drift van de continenten", blokken=[
            ("p", "Ongeveer 250 miljoen jaar geleden lagen alle landmassa's samen in één supercontinent: "
                  "<strong>Pangea</strong>. Dat brak uiteen in een noordelijk deel, Laurazië, en een "
                  "zuidelijk deel, <strong>Gondwana</strong>. Tot Gondwana hoorden <strong>Zuid-Amerika en "
                  "Afrika</strong>, <strong>Australië en Antarctica</strong>, en <strong>India en "
                  "Arabië</strong>."),
            ("p", "Twee aanwijzingen pleiten voor de drift: <strong>de kustlijnen van Zuid-Amerika en Afrika "
                  "passen als twee stukken van een puzzel in elkaar</strong>, en je vindt <strong>dezelfde "
                  "fossielen op twee verre continenten</strong>. Die tweede weegt het zwaarst: een puzzel "
                  "kan toeval zijn, een landdier dat de oceaan niet kon oversteken niet."),
        ]),
        dict(kop="Wat de platen beweegt", blokken=[
            ("p", "De tektonische platen bewegen <strong>een paar centimeter per jaar</strong>, ongeveer zo "
                  "snel als je nagels groeien. Twee krachten drijven ze aan."),
            ("p", "De <strong>subductietrekkracht</strong> of slab pull: <strong>de duikende plaat trekt de "
                  "rest mee</strong>. Het koude, zware uiteinde zakt de mantel in en sleurt de hele plaat "
                  "achter zich aan. Dat is de sterkste van de twee."),
            ("p", "De <strong>rugduwkracht</strong> of ridge push: <strong>de hoge, warme rug duwt de plaat "
                  "van zich af</strong>. De rug ligt hoger dan de rest van de oceaanbodem, en de plaat "
                  "glijdt er als het ware van af."),
        ]),
        dict(kop="Drie soorten plaatbeweging", blokken=[
            ("p", "De vakfiche noemt <strong>divergentie</strong>, <strong>convergentie</strong> en <strong>de "
                  "transforme beweging</strong>."),
            ("p", tabel(["beweging", "wat er gebeurt", "wat je ziet"],
                        [["divergentie", "de platen bewegen van elkaar weg", "een oceanische rug, een slenk"],
                         ["convergentie", "de platen botsen", "een diepzeetrog of een plooiingsgebergte"],
                         ["transform", "twee platen schuiven langs elkaar", "breuken en aardbevingen"]])),
            ("p", "Bij <strong>convergentie van twee continentale platen ontstaat een "
                  "plooiingsgebergte</strong>: geen van de twee is zwaar genoeg om te duiken, dus plooit "
                  "alles omhoog. Botst een oceanische plaat op een continentale, dan duikt de zware "
                  "oceanische eronder: dat heet <strong>subductie</strong>, en je krijgt <strong>een trog "
                  "met een kustgebergte erlangs</strong>."),
            ("p", "Boven een subductiezone is er vulkanisme <strong>omdat de duikende plaat in de diepte "
                  "smelt</strong>. Het water dat ze meeneemt doet het mantelgesteente erboven smelten."),
            ("p", "<strong>Nieuwe oceanische korst wordt niet in een diepzeetrog gemaakt maar aan een "
                  "oceanische rug.</strong> In de trog verdwijnt er juist korst. Daardoor <strong>wordt de "
                  "aarde ook niet groter</strong>: er komt precies evenveel bij als er in de subductiezones "
                  "verdwijnt. En de <strong>Atlantische Oceaan wordt breder terwijl de Stille Oceaan "
                  "krimpt</strong>, niet omgekeerd."),
            ("p", "Een <strong>riftster</strong> is <strong>een punt waar drie riftarmen "
                  "samenkomen</strong>. Meestal groeien er twee van de drie uit tot een oceaan en blijft de "
                  "derde als een mislukte arm liggen."),
        ]),
        dict(kop="Mantelpluimen en hotspots", blokken=[
            ("p", "Een <strong>mantelpluim</strong> is <strong>een opstijgende kolom mantelgesteente</strong>. "
                  "Waar die de korst bereikt midden op een plaat, ligt een <strong>hotspot</strong>."),
            ("p", "<strong>Hawaï vormt een rij eilanden van verschillende ouderdom omdat de plaat over een "
                  "vaste hotspot schuift.</strong> De hotspot blijft staan, de plaat beweegt, en zo wordt er "
                  "om beurten een nieuw eiland gebouwd terwijl het vorige wegschuift en uitdooft."),
            ("p", "<strong>IJsland heeft zoveel vulkanen en geisers omdat het op een rug én op een hotspot "
                  "ligt.</strong> Die twee samen is uitzonderlijk."),
            ("p", "Bij de plaatbewegingen noemt de vakfiche dus <strong>Pangea en Gondwana</strong>, "
                  "<strong>mantelpluim en hotspot</strong>, en <strong>riftster en subductie</strong>."),
        ]),
        dict(kop="Het reliëf van de oceaanbodem", blokken=[
            ("fig", svg.kustdoorsnede(), "Van de kust naar de diepzee: het continentaal plat, de helling en "
                                         "de vlakte."),
            ("p", "Het <strong>continentaal plat</strong> is de ondiepe, vlakke zoom rond een continent, tot "
                  "ongeveer 200 meter diep. Daarna volgt <strong>de continentale helling</strong>, en "
                  "daaronder <strong>de abyssale vlakte: de uitgestrekte, vlakke bodem van de "
                  "diepzee</strong>."),
            ("p", "Bij een <strong>divergente plaatgrens in de oceaan</strong> hoort <strong>een oceanische "
                  "rug</strong>; bij een <strong>subductiezone</strong> hoort <strong>een "
                  "diepzeetrog</strong>."),
            ("p", "Een <strong>dwarsprofiel</strong> van het aardoppervlak <strong>toont de hoogte langs een "
                  "gekozen lijn</strong>, <strong>je kan er reliëfvormen op benoemen</strong>, en <strong>de "
                  "ligging ervan lees je van een kaart af</strong>."),
            ("fig", svg.reliefprofiel(), "Een dwarsprofiel: de hoogte langs één gekozen lijn op de kaart."),
        ]),
        dict(kop="Plooien, slenken en gebergten", blokken=[
            ("p", "Een <strong>anticline</strong> is <strong>een plooi met de bolle kant naar boven</strong>; "
                  "een <strong>syncline</strong> is <strong>een plooi waarbij de lagen een trog vormen, met "
                  "de holle kant naar boven</strong>. <strong>In een geplooid gebergte liggen de "
                  "gesteentelagen niet meer horizontaal.</strong>"),
            ("p", "Een <strong>slenk</strong> of rift op het land ontstaat doordat <strong>de korst wordt "
                  "uitgerekt en tussen breuken wegzakt</strong>. De bekendste is de "
                  "<strong>Oost-Afrikaanse Slenk</strong>."),
            ("p", "De <strong>Himalaya</strong> is ontstaan doordat <strong>India op de Euraziatische plaat "
                  "botste</strong>, twee continentale platen dus. De <strong>Andes</strong> is een "
                  "kustgebergte boven een subductiezone. De <strong>Ardennen</strong> zijn daarentegen "
                  "<strong>geen jong, hoog plooiingsgebergte met scherpe toppen</strong>: ze zijn oud en "
                  "door de erosie afgerond tot een plateau met diepe dalen."),
            ("p", "De vakfiche noemt als reliëfvormen: <strong>diepzeetrog en oceanische rug</strong>, "
                  "<strong>continentaal plat en continentale helling</strong>, en <strong>plooiingsgebergte "
                  "en slenk</strong>."),
        ]),
        dict(kop="Vulkanen en aardbevingen tekenen de platen uit", blokken=[
            ("fig", svg.vulkaan(), "Een vulkaan boven een subductiezone: magma stijgt op door de korst."),
            ("p", "Een <strong>caldera</strong> is <strong>een grote krater na het instorten van een "
                  "vulkaan</strong>: de magmakamer is leeggelopen en het dak zakt in."),
            ("p", "Over de ligging van aardbevingen en vulkanen geldt: <strong>ze liggen vooral aan de "
                  "plaatranden</strong>, <strong>samen tekenen ze de plaatgrenzen uit</strong>, en <strong>de "
                  "Ring of Fire is de bekendste gordel</strong>. Dat is precies hoe de kaart van de platen "
                  "gevonden is: door de bevingen op een wereldkaart te zetten en te zien dat ze in lijnen "
                  "liggen."),
        ]),
    ])


# ───────────────────────── 13. Aardbevingen en vulkanisme
zet("aardbevingen-en-vulkanisme",
    titel="Aardbevingen en vulkanisme",
    onder="Hoe een beving ontstaat en gemeten wordt, de twee soorten vulkanen, en waarom mensen ondanks alles op een vulkaanflank blijven wonen.",
    secties=[
        dict(kop="Waar een beving begint", blokken=[
            ("p", "Bij een tektonische aardbeving beeft de grond omdat <strong>opgebouwde spanning plots "
                  "vrijkomt</strong>. Twee plaatranden blijven jarenlang aan elkaar haken, de spanning "
                  "loopt op, en op een moment schiet het gesteente los."),
            ("fig", svg.aardbeving(), "Het hypocentrum ligt in de diepte, het epicentrum er recht boven "
                                      "aan de oppervlakte."),
            ("p", "Het <strong>hypocentrum</strong> of de haard is <strong>de plaats in de diepte waar de "
                  "beving begint</strong>. Het punt aan het aardoppervlak recht daarboven is het "
                  "<strong>epicentrum</strong>."),
            ("p", "De vakfiche noemt bij de aardbevingen deze begrippen: <strong>seismologie en "
                  "seismogram</strong>, <strong>seismograaf</strong>, en <strong>hypocentrum en "
                  "epicentrum</strong>. Op een <strong>seismogram</strong> lees je <strong>de bewegingen "
                  "van de bodem in de tijd</strong> af."),
            ("p", "<strong>Met metingen van drie seismische stations kan je het epicentrum van een beving "
                  "bepalen.</strong> Elk station weet uit het tijdsverschil tussen de golven hoe vér de "
                  "haard lag, niet in welke richting. Drie cirkels snijden elkaar in één punt, en daar ligt "
                  "het epicentrum."),
            ("p", "De <strong>P-golven komen het eerst aan</strong> bij een meetstation: het zijn "
                  "drukgolven en ze gaan sneller dan de S-golven die de echte schade doen. Een "
                  "waarschuwingssysteem kan daardoor enkele seconden winnen voor een beving toeslaat, "
                  "<strong>omdat de P-golven als eerste aankomen</strong>. Enkele seconden is genoeg om een "
                  "trein te laten stoppen of een gasleiding te sluiten."),
            ("p", "Een lichtere beving na de hoofdbeving heet een <strong>naschok</strong>."),
        ]),
        dict(kop="De kracht meten", blokken=[
            ("p", "De schaal van <strong>Richter</strong> geeft <strong>de kracht van een beving in de "
                  "haard</strong>. Voor zware bevingen gebruikt men vandaag liever de "
                  "<strong>momentmagnitudeschaal</strong>, afgekort <strong>MMS</strong>: de schaal van "
                  "Richter verzadigt boven magnitude 7 en onderschat dan hoe groot een beving was."),
            ("p", "De schaal is logaritmisch, en dat leidt tot twee vaak gemaakte fouten. "
                  "<strong>Magnitude 7 maakt veel meer energie vrij dan magnitude 6</strong>, niet een beetje "
                  "meer: ongeveer dertig keer zoveel. En een beving van <strong>magnitude 8 is niet twee "
                  "keer zo sterk als een van magnitude 4</strong>, maar duizenden keren zo sterk."),
            ("p", "<strong>Wetenschappers kunnen de dag en het uur van een aardbeving niet nauwkeurig "
                  "voorspellen.</strong> Ze kunnen wel zeggen welke zone gevaarlijk is en hoe groot de kans "
                  "over dertig jaar is, en dat is waar bouwvoorschriften op gebaseerd zijn."),
        ]),
        dict(kop="Wat een beving aanricht", blokken=[
            ("p", "Een zware beving geeft <strong>instortende gebouwen</strong>, <strong>een tsunami aan de "
                  "kust</strong> en <strong>aardverschuivingen op hellingen</strong>."),
            ("p", "Een <strong>tsunami</strong> ontstaat doordat <strong>de zeebodem verschuift bij een "
                  "beving</strong>: de hele waterkolom wordt in één keer opgetild. Op volle zee is de golf "
                  "maar een halve meter hoog en schuift ze onder een schip door; pas in ondiep water loopt "
                  "ze op tot een muur van water."),
            ("p", "Dezelfde beving is in een arm land vaak dodelijker dan in een rijk land, en daar zijn "
                  "drie redenen voor: <strong>de gebouwen zijn er minder bevingsveilig</strong>, <strong>er "
                  "is minder geld voor een waarschuwingssysteem</strong>, en <strong>de hulpdiensten kunnen "
                  "er minder snel ter plaatse zijn</strong>. Een beving doodt geen mensen, instortende "
                  "gebouwen doen dat."),
            ("p", "De grond beeft in een zachte, opgevulde vallei harder dan op vast gesteente, want "
                  "<strong>losse grond versterkt de golven</strong>. Dat heet terreinversterking, en het "
                  "verklaart waarom de schade in een stad van straat tot straat kan verschillen."),
            ("p", "<strong>Ook in België komen af en toe lichte aardbevingen voor</strong>, vooral rond de "
                  "Roerdalslenk in Limburg. Zwaar zijn ze niet, maar ze zijn echt."),
        ]),
        dict(kop="Magma, lava en de delen van een vulkaan", blokken=[
            ("p", "Het verschil tussen magma en lava zit in waar het zich bevindt: <strong>magma zit in de "
                  "aarde, lava stroomt erbuiten</strong>. Gesmolten gesteente dat nog in de aarde zit, is "
                  "dus <strong>magma</strong>."),
            ("fig", svg.vulkaan(), "De magmakamer, de schoorsteen en de krater."),
            ("p", "Bij een vulkaan horen <strong>de magmakamer</strong>, <strong>de schoorsteen of "
                  "pijp</strong> en <strong>de krater</strong>."),
        ]),
        dict(kop="Twee soorten vulkanen", blokken=[
            ("p", "De vakfiche vergelijkt <strong>de stratovulkaan en de schildvulkaan</strong>."),
            ("p", tabel(["", "schildvulkaan", "stratovulkaan"],
                        [["vorm", "flauwe hellingen, breed", "steile kegel"],
                         ["lava", "dun en vloeibaar", "dik en stroperig"],
                         ["opbouw", "laag op laag lava", "afwisselende lagen lava en as"],
                         ["uitbarsting", "rustig vloeiend", "explosief"],
                         ["voorbeeld", "Mauna Loa op Hawaï", "Vesuvius, Fuji"]])),
            ("p", "Een <strong>schildvulkaan</strong> kenmerkt zich dus door <strong>flauwe hellingen en "
                  "dunne lava</strong>; een <strong>stratovulkaan</strong> door <strong>afwisselende lagen "
                  "lava en as</strong>, en van die lagen komt zijn naam. <strong>Een stratovulkaan barst "
                  "gewoonlijk explosiever uit dan een schildvulkaan.</strong>"),
            ("p", "De lava van een schildvulkaan is dunner <strong>omdat ze minder kiezelzuur bevat</strong>. "
                  "Hoe meer kiezelzuur, hoe stroperiger het magma, hoe moeilijker de gassen eruit kunnen, "
                  "en hoe harder de knal als het toch opengaat."),
            ("p", "De vulkaangordel rond de Stille Oceaan heet de <strong>Ring of Fire</strong>. "
                  "<strong>Toch liggen niet álle vulkanen aan de rand van een tektonische plaat</strong>: "
                  "die boven een hotspot, zoals op Hawaï, liggen midden op een plaat."),
        ]),
        dict(kop="Wat een vulkaan uitwerpt", blokken=[
            ("p", "De vakfiche noemt drie vormen van uitgeworpen materiaal: <strong>lapilli</strong>, "
                  "<strong>vulkanische bommen</strong> en <strong>vulkanische as</strong>."),
            ("p", tabel(["uitgeworpen", "wat het is"],
                        [["vulkanische as", "het fijnste: stofdeeltjes, kilometers hoog de lucht in"],
                         ["lapilli", "kleine steentjes die een vulkaan uitspuwt"],
                         ["vulkanische bom", "de grootste brokken, van een vuist tot een auto"]])),
            ("p", "De <strong>vulkanische bom</strong> is dus het grootste van de drie, en <strong>vulkanische "
                  "as kan het luchtverkeer over een heel werelddeel stilleggen</strong>: het fijne stof "
                  "schuurt vliegtuigmotoren stuk."),
            ("p", "Een <strong>lahar</strong> is <strong>een modderstroom van as en water</strong>. Hij "
                  "ontstaat als regen of smeltend gletsjerijs de losse as van een flank meesleurt, en hij "
                  "kan tientallen kilometers ver reiken, lang nadat de uitbarsting voorbij is."),
            ("p", "Een <strong>gloedwolk</strong> is zo gevaarlijk <strong>omdat ze razendsnel de flank "
                  "afschiet</strong>: een wolk van gloeiend gas en as die met honderden kilometer per uur "
                  "naar beneden stort. Daar valt niet voor te vluchten."),
        ]),
        dict(kop="Toch wonen op een vulkaan", blokken=[
            ("p", "Mensen wonen op de flanken van een vulkaan omdat <strong>de bodem er heel vruchtbaar "
                  "is</strong>, <strong>er aardwarmte te winnen is</strong> en <strong>er veel toeristen op "
                  "afkomen</strong>. Verweerde vulkanische as geeft een van de rijkste bodems ter wereld."),
            ("p", "<strong>Aardwarmte</strong> op een vulkanisch eiland dient <strong>om elektriciteit en "
                  "warmte te maken</strong>. IJsland verwarmt er bijna al zijn huizen mee."),
            ("p", "Eén wijdverbreid misverstand: een uitbarsting <strong>warmt het klimaat van de hele "
                  "aarde niet op</strong>. Ze <strong>koelt</strong> juist af, soms een jaar of twee, omdat "
                  "de zwaveldeeltjes in de stratosfeer zonlicht terugkaatsen."),
        ]),
    ])


# ───────────────────────── 14. Gesteenten, mineralen en datering
zet("gesteenten-mineralen-en-datering",
    titel="Gesteenten, mineralen en datering",
    onder="De drie groepen gesteenten en hoe ze in elkaar overgaan, en hoe je uit aardlagen en fossielen de ouderdom afleidt.",
    secties=[
        dict(kop="Drie groepen", blokken=[
            ("p", "Er zijn <strong>drie grote groepen gesteenten: magmatische, sedimentaire en "
                  "metamorfe</strong>. Een <strong>gesteente is een natuurlijk mengsel van "
                  "mineralen</strong>; een mineraal is de zuivere bouwsteen."),
            ("p", tabel(["groep", "ontstaan", "voorbeeld"],
                        [["magmatisch", "uit afgekoeld magma of lava", "graniet, basalt"],
                         ["sedimentair", "uit samengeperste losse deeltjes", "zandsteen, kalksteen"],
                         ["metamorf", "omgevormd door druk en hitte", "marmer, leisteen"]])),
            ("p", "Van de mineralen staan in de bijlage van de vakfiche: <strong>pyriet en grafiet</strong>, "
                  "<strong>diamant en kwarts</strong>, en <strong>veldspaat en biotiet</strong>."),
            ("weetje", "<strong>Diamant en grafiet bestaan uit precies dezelfde stof</strong>: zuivere "
                       "koolstof. Het enige verschil is hoe de atomen gestapeld staan. Het hardste en een "
                       "van de zachtste mineralen op aarde zijn chemisch dus hetzelfde."),
        ]),
        dict(kop="Magmatische gesteenten", blokken=[
            ("p", "Hoe langzamer het magma afkoelt, hoe groter de kristallen worden. <strong>Graniet heeft "
                  "grote, goed zichtbare kristallen omdat het magma heel langzaam afkoelde</strong>, diep "
                  "in de korst. Wie een granieten keukenblad bekijkt, kijkt naar duizenden jaren traag "
                  "afkoelen."),
            ("p", "Stroomt het magma als lava naar buiten, dan koelt het snel af en krijg je een "
                  "<strong>uitvloeiingsgesteente</strong>. Zo zijn <strong>basalt</strong>, "
                  "<strong>puimsteen</strong> en <strong>obsidiaan</strong> ontstaan."),
            ("p", "<strong>Obsidiaan heeft geen kristallen omdat de lava te snel afkoelde om te "
                  "kristalliseren</strong>: het is eigenlijk vulkanisch glas. <strong>Puimsteen</strong> is "
                  "zo vol gasbellen dat het op water blijft drijven."),
        ]),
        dict(kop="Sedimentaire gesteenten", blokken=[
            ("p", "De vakfiche zet de losse sedimenten op een rij van grof naar fijn: <strong>grind, zand, "
                  "silt, klei</strong>. Worden die samengeperst en aan elkaar gekit, dan krijg je een "
                  "gesteente."),
            ("p", tabel(["los sediment", "wordt"],
                        [["grind", "conglomeraat"],
                         ["zand", "zandsteen"],
                         ["silt", "siltsteen"],
                         ["klei", "kleisteen of schiefer"]])),
            ("p", "Uit <strong>zand</strong> ontstaat dus <strong>zandsteen</strong>, en uit grind een "
                  "<strong>conglomeraat</strong>: een gesteente waarin je de ronde keien nog met het blote "
                  "oog ziet zitten."),
            ("p", "Sommige sedimentaire gesteenten zijn <strong>organogeen</strong>, uit resten van leven "
                  "ontstaan: <strong>krijt</strong>, <strong>steenkool</strong> en <strong>kalksteen uit "
                  "schelpen</strong>. <strong>Steenkool is ontstaan uit plantenresten in moerassen</strong>, "
                  "in het Carboon, en dat is waarom de mijnstreek in Limburg en Wallonië ligt waar ze ligt."),
            ("p", "<strong>Mergel bestaat uit een mengsel van kalk en klei.</strong> Daardoor is het zacht "
                  "genoeg om met een zaag te snijden, wat de Limburgse mergelgrotten verklaart."),
        ]),
        dict(kop="Metamorfe gesteenten", blokken=[
            ("p", "Druk en hitte vormen een gesteente om zonder het te laten smelten. <strong>Metamorfe "
                  "gesteenten zijn dus niet gesmolten en weer afgekoeld</strong>: dan zou je een magmatisch "
                  "gesteente krijgen."),
            ("p", tabel(["uit", "wordt"],
                        [["kalksteen", "marmer"],
                         ["zandsteen", "kwartsiet"],
                         ["kleisteen", "leisteen"],
                         ["steenkool", "grafiet, en bij extreme druk diamant"]])),
            ("p", "Uit <strong>kalksteen</strong> ontstaat dus <strong>marmer</strong>, uit "
                  "<strong>zandsteen kwartsiet</strong>, en <strong>leisteen</strong> komt uit "
                  "<strong>kleisteen</strong>. Dat laatste zie je nog aan de platte schilfers: de klei is "
                  "onder druk in één richting platgedrukt."),
        ]),
        dict(kop="De gesteentecyclus", blokken=[
            ("p", "Gesteenten gaan voortdurend in elkaar over, en die kringloop heet de "
                  "<strong>gesteentecyclus</strong>. Magma koelt af tot magmatisch gesteente, verwering en "
                  "erosie maken er sediment van, samenpersen maakt daar sedimentair gesteente van, druk en "
                  "hitte maken het metamorf, en nog meer hitte smelt het terug tot magma."),
            ("p", "Daarbij geldt geen enkele vaste orde: <strong>in de gesteentecyclus kan een metamorf "
                  "gesteente wél opnieuw sediment worden</strong>. Een marmerblok dat aan de oppervlakte "
                  "komt, verweert net zo goed als elk ander gesteente."),
            ("fig", svg.gesteentecyclus(), "De kring heeft geen vaste orde: de pijl binnenin brengt een\n                                              metamorf gesteente rechtstreeks terug bij het sediment."),
        ]),
        dict(kop="Relatieve datering: de lagen lezen", blokken=[
            ("p", "<strong>Relatieve datering</strong> is het dateren waarbij je <strong>enkel zegt wat "
                  "ouder of jonger is, zonder jaartal</strong>. Daarvoor bestaan een paar eenvoudige "
                  "regels."),
            ("p", "De <strong>wet van de superpositie</strong> zegt: <strong>de onderste laag is de "
                  "oudste</strong>. Dat is logisch, want elke nieuwe laag wordt bovenop de vorige afgezet. "
                  "Maar <strong>de wet geldt niet meer als de lagen door plooiing of een breuk zijn "
                  "omgekeerd</strong>, en in een gebergte is dat geen uitzondering."),
            ("p", "Snijdt een gang magma dwars door een reeks aardlagen, dan weet je dat <strong>de "
                  "intrusie jonger is dan die lagen</strong>: je kan niet dwars door iets heen dringen dat "
                  "er nog niet was. Gesmolten gesteente dat in bestaande lagen binnendringt en daar "
                  "afkoelt, heet een <strong>intrusie</strong>."),
            ("p", "Een <strong>discordantievlak</strong> is <strong>een oud erosievlak tussen twee "
                  "lagenreeksen</strong>: er is een tijd lang niets afgezet en er is zelfs materiaal "
                  "weggesleten. Het ontbrekende stuk in de opeenvolging heet een <strong>hiaat</strong>."),
            ("p", "Een gesteente dat <strong>dagzoomt</strong>, ligt juist <strong>niet</strong> diep onder "
                  "de grond: het komt aan de oppervlakte, waar je het kan zien en bemonsteren."),
        ]),
        dict(kop="Fossielen", blokken=[
            ("p", "Een <strong>fossiel</strong> is <strong>een versteend overblijfsel van leven</strong>. "
                  "<strong>Fossielen bewaren niet het best in magmatisch gesteente</strong>, hoe hard dat "
                  "ook is: lava verbrandt alles. Ze zitten in sedimentair gesteente, waar een dier of plant "
                  "rustig bedekt raakte."),
            ("p", "Een goed <strong>gidsfossiel</strong> heeft drie eigenschappen: <strong>de soort leefde "
                  "maar kort op aarde</strong>, <strong>de soort kwam over een groot gebied voor</strong> en "
                  "<strong>de soort is makkelijk te herkennen</strong>. Kort bestaan is de kern: hoe korter "
                  "de soort leefde, hoe scherper hij een laag dateert."),
        ]),
        dict(kop="Absolute datering en de geologische tijdschaal", blokken=[
            ("p", "De <strong>halveringstijd</strong> van een radioactief element dient <strong>om de "
                  "ouderdom in jaren te berekenen</strong>. Je meet hoeveel er van het element over is en "
                  "hoeveel vervalproduct erbij is gekomen, en daaruit volgt een jaartal."),
            ("p", "De tijdperken op een rij, van oud naar jong: <strong>Paleozoïcum, Mesozoïcum, "
                  "Cenozoïcum</strong>."),
            ("fig", svg.tijdlijn([("Paleozoïcum", -541, -252, "#6c8f5a"),
                                  ("Mesozoïcum", -252, -66, "#b5894a"),
                                  ("Cenozoïcum", -66, 0, "#5e2d91")],
                                 [(-541, "541 mln jaar", "boven"),
                                  (-252, "grote sterfte", "boven"),
                                  (-66, "einde dino's", "onder")]),
             "De drie jongste tijdperken, in miljoenen jaren voor nu."),
            ("p", "De grenzen in de geologische tijdschaal zijn vooral gebaseerd <strong>op grote omslagen "
                  "in het leven op aarde</strong>, niet op ronde getallen. Bij een "
                  "<strong>massa-extinctie verdwijnen in korte tijd heel veel soorten tegelijk</strong>, en "
                  "zo'n omslag is in de lagen over de hele wereld terug te vinden."),
            ("p", "De grens tussen het Mesozoïcum en het Cenozoïcum valt samen met <strong>het uitsterven "
                  "van de dinosaurussen</strong>, 66 miljoen jaar geleden."),
        ]),
        dict(kop="Gebergtevormingen", blokken=[
            ("p", "De vakfiche noemt drie gebergtevormingen: <strong>de Caledonische</strong>, <strong>de "
                  "Hercynische</strong> en <strong>de Alpiene</strong>."),
            ("p", tabel(["plooiing", "wanneer", "wat ze vormde"],
                        [["Caledonische", "ongeveer 400 miljoen jaar geleden", "de Schotse Hooglanden, Noorwegen"],
                         ["Hercynische", "ongeveer 300 miljoen jaar geleden", "de Ardennen, de Harz"],
                         ["Alpiene", "de laatste 50 miljoen jaar", "de Alpen, de Himalaya"]])),
            ("p", "De <strong>Hercynische</strong> plooiing, ook Variscische genoemd, vormde dus de "
                  "<strong>Ardennen</strong>; <strong>de Alpiene plooiing</strong> vormde de Alpen en de "
                  "Himalaya, en die duurt nog voort."),
            ("p", "Oude gebergten zijn lager dan jonge om drie redenen: <strong>de erosie heeft er veel "
                  "langer op gewerkt</strong>, <strong>de opstuwing is er al lang gestopt</strong> en "
                  "<strong>verwering heeft de toppen afgerond</strong>. Vergelijk de scherpe punten van de "
                  "Alpen met de ronde hoogvlakte van de Ardennen: dat is 250 miljoen jaar verschil."),
        ]),
    ])


# ───────────────────────── 15. Verwering, karst en massatransport
zet("verwering-karst-en-massatransport",
    titel="Verwering, karst en massatransport",
    onder="Hoe gesteente ter plaatse uiteenvalt, wat kalksteen zo bijzonder maakt, en waarom een helling gaat schuiven.",
    secties=[
        dict(kop="Verwering, erosie, sedimentatie", blokken=[
            ("p", "<strong>Verwering</strong> is dat <strong>gesteente ter plaatse uiteenvalt</strong>. Dat "
                  "ter plaatse is het hele verschil met erosie: bij erosie wordt het losse materiaal "
                  "weggevoerd."),
            ("p", "De drie processen in de juiste orde: <strong>verwering, erosie, sedimentatie</strong>. "
                  "Eerst valt de steen uiteen, dan wordt het puin meegenomen, dan wordt het elders weer "
                  "afgezet."),
            ("fig", svg.slijtage(), "Drie stappen die elkaar opvolgen, van losse steen tot nieuwe laag."),
        ]),
        dict(kop="Drie soorten verwering", blokken=[
            ("p", "De vakfiche noemt <strong>fysische verwering</strong>, <strong>chemische "
                  "verwering</strong> en <strong>biologische verwering</strong>."),
            ("p", "<strong>Vorstverwering</strong> is de bekendste fysische vorm: <strong>water in een "
                  "spleet bevriest en zet uit</strong>. IJs neemt ongeveer negen procent meer plaats in dan "
                  "water, en die paar procent breekt een rotswand open. De vorm waarbij bevriezend water "
                  "gesteente openbreekt, heet dus <strong>vorstverwering</strong>."),
            ("p", "<strong>Biologische verwering</strong> werkt doordat <strong>wortels en zuren van "
                  "organismen gesteente afbreken</strong>: een boomwortel in een spleet, korstmossen die "
                  "zuur afscheiden."),
            ("p", "<strong>Chemische verwering gaat sneller in een warm en vochtig klimaat</strong>, want "
                  "warmte en water versnellen elke reactie. Het gesteente dat het gevoeligst is voor "
                  "chemische verwering door zuur regenwater, is <strong>kalksteen</strong>: kalk lost op in "
                  "koolzuurhoudend water."),
            ("p", "Het klimaat bepaalt dus welke verwering overheerst: <strong>vorstverwering overheerst in "
                  "koude streken</strong>, <strong>chemische verwering overheerst in warme, vochtige "
                  "streken</strong>, en <strong>in een woestijn werkt vooral temperatuurwisseling</strong>, "
                  "waar het verschil tussen dag en nacht de steen doet barsten."),
        ]),
        dict(kop="Karst", blokken=[
            ("p", "Het landschap dat door het oplossen van kalksteen ontstaat, heet <strong>karst</strong>. "
                  "Het is het enige landschap dat niet door afslijten maar door oplossen gemaakt is, en "
                  "daarom <strong>kan karst niet in een zandsteengebied ontstaan</strong>: zandsteen lost "
                  "niet op."),
            ("p", "De vakfiche noemt deze karstverschijnselen: <strong>karren en diaklazen</strong>, "
                  "<strong>verdwijngat en resurgentie</strong>, en <strong>doline en druipstenen</strong>."),
            ("p", tabel(["verschijnsel", "wat het is"],
                        [["karren", "groeven in een kalkoppervlak"],
                         ["diaklaas", "een natuurlijke spleet waarlangs water naar beneden dringt"],
                         ["verdwijngat", "waar een beek in de grond verdwijnt"],
                         ["resurgentie", "waar de ondergrondse rivier weer bovenkomt"],
                         ["doline", "een trechtervormige inzinking in kalkgebied"],
                         ["druipstenen", "stalactieten en stalagmieten in een grot"]])),
            ("p", "Een <strong>doline</strong> is dus <strong>een trechtervormige inzinking in "
                  "kalkgebied</strong>, en de plek waar een ondergrondse rivier weer aan de oppervlakte "
                  "komt, is de <strong>resurgentie</strong>. Een natuurlijke spleet in kalkgesteente "
                  "waarlangs het water naar beneden dringt, is een <strong>diaklaas</strong>, en "
                  "<strong>karren</strong> zijn <strong>groeven in een kalkoppervlak</strong>."),
            ("p", "Het verschil tussen de twee druipstenen zit in de richting: <strong>een stalagmiet "
                  "groeit van de bodem omhoog</strong>, een stalactiet hangt van het plafond. "
                  "<strong>Druipstenen ontstaan doordat kalk uit het druppelende water weer "
                  "neerslaat</strong>, een millimeter per tien jaar ongeveer."),
            ("p", "<strong>In een karstgebied liggen juist heel weinig beken aan de oppervlakte</strong>: "
                  "het water zakt door de diaklazen weg en loopt ondergronds verder. Een karstplateau kan "
                  "er in een regenachtig land kurkdroog uitzien. In België komt karst voor <strong>in de "
                  "kalkstreken van Wallonië</strong>, met de grotten van Han als bekendste voorbeeld."),
        ]),
        dict(kop="Massatransport", blokken=[
            ("p", "<strong>Massatransport</strong> is dat <strong>bodem onder zijn eigen gewicht "
                  "schuift</strong>. Er is geen rivier, wind of gletsjer bij nodig: enkel zwaartekracht."),
            ("p", "Pas daarom op met twee begrippen die er niet bij horen: <strong>saltatie en "
                  "suspensie</strong> zijn manieren waarop water of wind deeltjes meeneemt, en dat is géén "
                  "massatransport."),
            ("p", tabel(["vorm", "snelheid"],
                        [["bodemcreep", "de traagste: millimeters per jaar, bijna onzichtbaar"],
                         ["verglijding", "van langzaam tot plots"],
                         ["modderstroom", "snel, een dal af"],
                         ["afstorting of steenlawine", "razendsnel"]])),
            ("p", "<strong>Bodemcreep</strong> is dus de traagste vorm: <strong>het heel trage, bijna "
                  "onzichtbare kruipen van de bodem op een helling</strong>. Je ziet hem niet bewegen, maar "
                  "je ziet het resultaat aan scheefgezakte afsluitingen en kromme boomstammen."),
            ("p", "Bij een <strong>afstorting</strong> <strong>vallen brokken vrij van een steile "
                  "wand</strong>. Onderaan hoopt het puin zich op tot een <strong>puinkegel</strong> of "
                  "puinhelling. Een <strong>modderstroom</strong> is <strong>een stroom van water, bodem en "
                  "stenen die zich snel door een dal stort</strong>."),
            ("p", "Een <strong>steenlawine is gevaarlijker dan bodemcreep omdat ze razendsnel gaat en niet "
                  "te ontvluchten is</strong>. Bodemcreep kost je op lange termijn je tuinmuur; een "
                  "steenlawine kost je in tien seconden je huis."),
        ]),
        dict(kop="Wanneer gaat een helling schuiven", blokken=[
            ("p", "Drie factoren bepalen samen of een helling gaat schuiven: <strong>de aard van het "
                  "gesteente</strong>, <strong>de hellingsgraad</strong> en <strong>de hoeveelheid water in "
                  "de bodem</strong>. <strong>Hoe steiler de helling, hoe meer kans op "
                  "massatransport.</strong>"),
            ("p", "Na zware regen gebeuren er veel aardverschuivingen, want <strong>water maakt de bodem "
                  "zwaarder en glibberiger</strong>. Het voegt gewicht toe én het vermindert de wrijving "
                  "tussen de korrels, en die twee werken in dezelfde richting."),
            ("p", "Het gesteente dat een helling het gevoeligst maakt voor verglijding, is <strong>een "
                  "kleilaag als glijvlak</strong>. Klei laat geen water door en wordt zelf glad, dus de "
                  "losse grond erboven glijdt eraf als van een natte glijbaan. Het <strong>glijvlak</strong> "
                  "is <strong>het vlak waarover de massa wegschuift</strong>."),
            ("p", "<strong>Een helling zonder plantengroei schuift makkelijker dan een beboste "
                  "helling.</strong> Wortels houden de bodem letterlijk vast, en bladeren breken de regen "
                  "op voor die de grond raakt."),
            ("p", "Het klimaat werkt op drie manieren mee: <strong>zware neerslag maakt hellingen "
                  "instabiel</strong>, <strong>vorst en dooi doen de bodem kruipen</strong>, en "
                  "<strong>smeltend permafrost laat hellingen losschuiven</strong>. Die laatste is in de "
                  "Alpen een nieuw probleem: bevroren bodem die duizenden jaren als cement werkte, dooit nu op."),
        ]),
        dict(kop="Wat mensen eraan doen, in beide richtingen", blokken=[
            ("p", "Mensen werken hellingsprocessen in de hand <strong>door bossen te kappen op steile "
                  "hellingen</strong>, <strong>door te bouwen en zo de helling te belasten</strong> en "
                  "<strong>door wegen in de voet van een helling te snijden</strong>. Dat laatste is het "
                  "verraderlijkst: je haalt onderaan de steun weg waar de hele massa op rust."),
            ("p", "De maatregel die een kwetsbare helling beschermt, is <strong>de helling "
                  "herbebossen</strong>. Daarnaast legt men <strong>vangnetten en betonnen schermen langs "
                  "een bergweg om vallend gesteente op te vangen</strong>."),
            ("p", "<strong>Massatransport komt in Vlaanderen veel minder vaak voor dan in de Alpen</strong>, "
                  "en dat heeft één eenvoudige reden: er zijn bijna geen steile hellingen. In de Vlaamse "
                  "Ardennen en het Pajottenland gebeurt het wel, op de steilste leemhellingen."),
            ("p", "Eén veelgemaakte denkfout: <strong>een aardverschuiving kan wél een rivier "
                  "afdammen</strong>. Het puin komt in één keer naar beneden en blijft liggen; achter die "
                  "natuurlijke dam ontstaat een meer, en als de dam doorbreekt komt alles tegelijk naar "
                  "beneden."),
        ]),
    ])


# ───────────────────────── 16. Erosie door water, ijs en wind
zet("erosie-door-water-ijs-en-wind",
    titel="Erosie door water, ijs en wind",
    onder="Wat een rivier van bron tot monding doet, welke sporen een gletsjer achterlaat, en hoe de wind löss en duinen maakt.",
    secties=[
        dict(kop="Het stroombekken", blokken=[
            ("p", "Een <strong>stroombekken</strong> is <strong>het hele gebied dat op één rivier "
                  "afwatert</strong>, van de verste beek tot de monding. De lijn die twee stroombekkens "
                  "scheidt, is de <strong>waterscheidingskam</strong>: regen die aan de ene kant valt, "
                  "komt in de ene rivier terecht, regen aan de andere kant in de andere."),
            ("p", "De plaats waar een rivier in de zee of in een andere rivier uitkomt, is de "
                  "<strong>monding</strong>."),
            ("fig", svg.rivierloop(), "Van de bron tot de monding wordt de rivier breder en gaat ze "
                                      "kronkelen."),
        ]),
        dict(kop="Boven-, midden- en benedenloop", blokken=[
            ("p", "De <strong>bovenloop</strong> kenmerkt zich door <strong>een groot verval</strong>, "
                  "<strong>een hoge stroomsnelheid</strong> en <strong>vooral verticale erosie</strong>: de "
                  "rivier snijdt zich naar beneden in."),
            ("p", tabel(["loop", "wat overheerst", "dalvorm"],
                        [["bovenloop", "verticale erosie", "het V-dal"],
                         ["middenloop", "zijdelingse erosie, meanders", "het vlakbodemdal"],
                         ["benedenloop", "sedimentatie", "de alluviale vlakte"]])),
            ("p", "Bij de bovenloop hoort dus <strong>het V-dal</strong>. <strong>In de benedenloop "
                  "overheerst de sedimentatie</strong>: de rivier heeft bijna geen verval meer en laat "
                  "vallen wat ze meedroeg. De vlakte die ze met haar eigen afzettingen opbouwt, is de "
                  "<strong>alluviale vlakte</strong>."),
            ("p", "Het <strong>vlakbodemdal</strong> hoort bij <strong>een rivier die zich in een vlakte "
                  "heeft ingesneden en nu zijdelings uitbreidt</strong>. Een <strong>kloofdal ontstaat waar "
                  "een rivier zich snel insnijdt in hard gesteente</strong>: de wanden zijn hard genoeg om "
                  "steil te blijven staan."),
            ("fig", svg.dalvormen(), "Het V-dal van een rivier naast het U-dal van een gletsjer."),
            ("p", "Het <strong>evenwichtsprofiel</strong> van een rivier is <strong>de lijn waar erosie en "
                  "afzetting in balans zijn</strong>: de ideale, holle lijn waar een rivier naartoe werkt, "
                  "steil bij de bron en bijna vlak bij de monding."),
        ]),
        dict(kop="Transport en het Hjülströmdiagram", blokken=[
            ("p", "Op een <strong>Hjülströmdiagram</strong> lees je af <strong>wat een korrel bij welke "
                  "snelheid doet</strong>: opgenomen worden, meegevoerd blijven of neervallen. "
                  "<strong>Een grove kei heeft de hoogste stroomsnelheid nodig om opgenomen te "
                  "worden</strong>, want hij is het zwaarst."),
            ("p", "Een rivier vervoert haar materiaal <strong>niet enkel rollend over de bodem</strong>. "
                  "Er zijn vier manieren tegelijk aan het werk."),
            ("p", tabel(["manier", "wat er gebeurt"],
                        [["rollen", "de grofste keien schuiven over de bodem"],
                         ["saltatie", "korrels springen met kleine sprongetjes vooruit"],
                         ["suspensie", "fijn materiaal zweeft in het water mee"],
                         ["oplossing", "stoffen zijn in het water opgelost en zijn onzichtbaar"]])),
            ("p", "De manier waarop korrels <strong>zwevend</strong> in het water worden meegevoerd, heet "
                  "dus <strong>suspensie</strong>."),
        ]),
        dict(kop="Meanders en differentiële erosie", blokken=[
            ("p", "Een <strong>meander</strong> ontstaat doordat <strong>de rivier zijdelings erodeert in "
                  "een vlak gebied</strong>. Zodra het verval klein is, gaat het water in een bocht "
                  "sneller aan de buitenkant en trager aan de binnenkant, en vanaf dan versterkt de bocht "
                  "zichzelf."),
            ("p", "In een meander gebeuren drie dingen tegelijk: <strong>de holle oever wordt "
                  "uitgeschuurd</strong>, <strong>aan de bolle oever wordt zand afgezet</strong> en "
                  "<strong>de bocht wordt doorheen de jaren groter</strong>. Let op de twee oevers: "
                  "<strong>aan de holle oever wordt géén materiaal afgezet</strong>, daar wordt juist "
                  "weggehaald."),
            ("p", "<strong>Differentiële erosie</strong> is dat <strong>hard gesteente trager erodeert dan "
                  "zacht</strong>. Zo ontstaan watervallen, steilranden en getuigenheuvels: de harde bank "
                  "blijft staan terwijl alles eromheen verdwijnt."),
            ("p", "<strong>Terugschrijdende erosie</strong> is de erosie waarbij <strong>een waterval zich "
                  "stroomopwaarts terugwerkt</strong>. Het vallende water holt de zachte laag onder de "
                  "harde bank uit, die bank breekt af, en zo kruipt de waterval jaar na jaar "
                  "stroomopwaarts."),
        ]),
        dict(kop="Overstromen", blokken=[
            ("p", "Een rivier overstroomt sneller als haar bekken verhard is, en daar lopen drie dingen "
                  "samen: <strong>het water kan niet infiltreren</strong>, <strong>het stroomt meteen naar "
                  "de rivier</strong>, en <strong>het debiet krijgt een scherpe piek</strong>. Dezelfde bui "
                  "boven een weide en boven een verkaveling geeft een heel ander hoogwater."),
        ]),
        dict(kop="Wat een gletsjer achterlaat", blokken=[
            ("p", "Een gletsjer maakt <strong>een U-dal</strong>: hij schuurt niet alleen naar beneden maar "
                  "ook zijdelings, en daarom is de bodem breed. Hoog in de bergen begint hij in een kom, "
                  "de <strong>cirque</strong> of kaar; zijn laagste, smeltende uiteinde heet het "
                  "<strong>gletsjerfront</strong>."),
            ("p", "<strong>Een gletsjer smelt niet enkel ter plaatse weg: hij beweegt.</strong> Het ijs "
                  "stroomt traag onder zijn eigen gewicht naar beneden, meters per jaar."),
            ("p", "De sporen die hij achterlaat: <strong>een U-dal en een cirque</strong>, <strong>morenen "
                  "en zwerfkeien</strong>, en <strong>gletsjerkrassen op het gesteente</strong>."),
            ("p", tabel(["spoor", "wat het is"],
                        [["morene", "een hoop puin die een gletsjer achterlaat"],
                         ["zwerfkei", "een blok dat een gletsjer heeft meegebracht"],
                         ["gletsjerkras", "een groef, geschuurd door stenen in het ijs"],
                         ["stuwwal", "een rug die door een ijskap is opgeduwd"],
                         ["fjord", "een uitgeschuurd dal dat later door de zee onderliep"]])),
            ("p", "Een <strong>gletsjerkras</strong> ontstaat doordat <strong>stenen in het ijs over de "
                  "bodem krassen</strong>: het ijs zelf is te zacht, het puin erin doet het werk. En "
                  "<strong>een fjord is inderdaad een door een gletsjer uitgeschuurd dal dat later door de "
                  "zee is ondergelopen</strong>."),
            ("p", "Het geologische tijdvak van de laatste grote ijstijden heet het "
                  "<strong>pleistoceen</strong>; een warme periode tussen twee ijstijden is een "
                  "<strong>interglaciaal</strong>."),
            ("p", "<strong>Tijdens de laatste ijstijd lag er géén ijskap over België.</strong> Het ijs "
                  "reikte tot in Noord-Nederland en Noord-Duitsland; bij ons was het een koude, boomloze "
                  "toendra met permafrost, en dat is precies waarom er hier wél löss ligt."),
        ]),
        dict(kop="De wind", blokken=[
            ("p", "De wind gebruikt dezelfde transportwijzen als het water: <strong>suspensie van fijn "
                  "stof</strong>, <strong>saltatie van zandkorrels</strong> en <strong>rollen van de "
                  "grofste korrels</strong>. <strong>Winderosie werkt het sterkst in een droog gebied met "
                  "weinig plantengroei</strong>, want zodra er wortels en bladeren zijn, ligt het zand vast."),
            ("p", "Een <strong>paddenstoelrots</strong> ontstaat doordat <strong>zand vooral onderaan de "
                  "rots wegschuurt</strong>: springende korrels komen zelden hoger dan een meter, dus "
                  "slijt de voet sneller weg dan de top."),
            ("p", "De woestijnvormen die door winderosie ontstaan: <strong>de rotswoestijn</strong>, "
                  "<strong>de steenwoestijn</strong> en <strong>het duinengebied</strong>."),
            ("p", "Het fijne, door de wind aangevoerde leem dat in Vlaanderen en Haspengouw ligt, heet "
                  "<strong>löss</strong>. Waarom ligt er in de Kempen zand en in Haspengouw löss? "
                  "<strong>Het zand viel dichter bij de bron dan het fijne leem.</strong> De poolwind blies "
                  "in de ijstijd over de droge Noordzeebodem; het zware zand viel er het eerst uit en "
                  "vormde de dekzanden van de Kempen, het lichte stof bleef langer zweven en kwam pas "
                  "zuidelijker neer. Dat verschil ligt vandaag nog altijd aan de basis van waar men welke "
                  "landbouw doet."),
            ("p", "Men plant hagen en houtkanten rond akkers aan <strong>om de wind te breken</strong>, "
                  "zodat de vruchtbare bovenlaag blijft liggen."),
        ]),
    ])


# ───────────────────────── 17. Klimaat doorheen de geologische tijd
zet("klimaat-doorheen-de-geologische-tijd",
    titel="Klimaat doorheen de geologische tijd",
    onder="Hoe we het klimaat van vroeger kennen, de cycli van Milanković, en waarom het verleden niets goedpraat aan vandaag.",
    secties=[
        dict(kop="Het klimaat is altijd veranderd", blokken=[
            ("p", "Een temperatuurcurve doorheen de geologische tijd leert ons dat <strong>het klimaat "
                  "altijd al veranderd is</strong>. <strong>De aarde heeft periodes gekend waarin er aan de "
                  "polen geen ijs lag</strong>, en periodes met een veel lagere zeespiegel."),
            ("p", "Drie uitspraken die kloppen: <strong>het klimaat veranderde ook zonder de mens</strong>, "
                  "<strong>er waren periodes zonder poolijs</strong>, en <strong>er waren periodes met een "
                  "veel lagere zeespiegel</strong>."),
            ("kader", "Dat is geen argument tegen de huidige klimaatverandering, en dat is precies waarom "
                      "dit hoofdstuk vóór het volgende staat. Dat het vroeger ook veranderde, zegt niets "
                      "over de oorzaak vandaag; wat telt is de <strong>snelheid</strong> en wat de meting "
                      "van de koolstof aanwijst. Zie het hoofdstuk over de huidige klimaatverandering."),
        ]),
        dict(kop="Hoe we dat weten", blokken=[
            ("p", "We weten iets over het klimaat van miljoenen jaren geleden <strong>uit fossielen, "
                  "ijskernen en sedimentlagen</strong>. De bronnen die de vakfiche noemt: <strong>ijskernen "
                  "uit de poolkappen</strong>, <strong>jaarringen van bomen</strong> en <strong>pollen in "
                  "veen- en meerbodems</strong>."),
            ("p", "Uit <strong>ijskernen</strong> halen wetenschappers luchtbelletjes van honderdduizenden "
                  "jaren oud: echte lucht van toen, waarin je het CO2-gehalte gewoon kan meten. De "
                  "temperatuur van toen lees je er af <strong>uit de verhouding van "
                  "zuurstofisotopen</strong>: in een koude periode regent er verhoudingsgewijs meer van de "
                  "lichtere soort zuurstof uit."),
        ]),
        dict(kop="IJstijden en warme tijden", blokken=[
            ("p", "Een <strong>glaciaal</strong> is <strong>een koude periode binnen een "
                  "ijstijdvak</strong>; een <strong>interglaciaal</strong> is de warme periode ertussen. "
                  "Het warme tijdvak waarin wij nu leven, heet het <strong>holoceen</strong>."),
            ("p", "De laatste ijstijd eindigde ongeveer <strong>11 700</strong> jaar geleden. Toen stond de "
                  "zeespiegel <strong>ongeveer 120 meter lager</strong>, want al dat water lag als ijs op "
                  "het land. <strong>De Noordzee lag toen grotendeels droog</strong>: je kon te voet naar "
                  "Engeland, over een vlakte waar vissers vandaag nog botten en werktuigen opvissen."),
            ("p", "Dat het ijs tot in Nederland reikte, weten we uit <strong>zwerfkeien en "
                  "stuwwallen</strong>: keien van een gesteente dat daar niet thuishoort, en ruggen die "
                  "door de ijskap zijn opgeduwd."),
        ]),
        dict(kop="Drie periodes om mee te vergelijken", blokken=[
            ("p", "De vakfiche noemt drie periodes uit het verleden om met vandaag te vergelijken: "
                  "<strong>het PETM</strong>, <strong>de jonge dryas</strong> en <strong>de kleine "
                  "ijstijd</strong>."),
            ("p", tabel(["periode", "wanneer", "wat er gebeurde"],
                        [["PETM", "56 miljoen jaar geleden", "een plotse, sterke opwarming"],
                         ["jonge dryas", "ongeveer 12 000 jaar geleden", "een plotse terugval naar de koude"],
                         ["kleine ijstijd", "ongeveer 1300 tot 1850", "een koelere periode in Europa"]])),
            ("p", "Het <strong>PETM</strong> is de plotse opwarming van 56 miljoen jaar geleden waarmee de "
                  "huidige vergeleken wordt. De <strong>jonge dryas</strong> was <strong>een plotse "
                  "terugval naar de koude</strong>, net toen de ijstijd leek voorbij te zijn. De "
                  "<strong>kleine ijstijd</strong> is <strong>een koelere periode van ongeveer 1300 tot "
                  "1850</strong>, maar <strong>géén wereldwijde ijstijd met ijskappen tot in "
                  "Frankrijk</strong>: het ging om een graad of minder, vooral in Europa, genoeg voor "
                  "dichtgevroren grachten op de schilderijen van Bruegel en niet meer dan dat."),
            ("p", "En de kern van de vergelijking: <strong>een klimaatverandering in het geologische "
                  "verleden ging doorgaans juist veel trager dan de huidige</strong>. Zelfs het PETM, dat "
                  "als snel geldt, nam duizenden jaren in beslag. De snelheid is belangrijk <strong>omdat "
                  "soorten zich niet snel genoeg kunnen aanpassen</strong>: een boomsoort die honderd meter "
                  "per jaar noordwaarts opschuift, haalt het niet van een klimaatgordel die kilometers per "
                  "jaar verschuift."),
        ]),
        dict(kop="De cycli van Milanković", blokken=[
            ("p", "De <strong>Milanković-variabelen</strong> zijn <strong>schommelingen in de baan en de "
                  "as</strong> van de aarde. Er zijn er drie: <strong>de excentriciteit van de baan</strong>, "
                  "<strong>de obliquiteit van de aardas</strong> en <strong>de precessie van de "
                  "aardas</strong>."),
            ("p", tabel(["variabele", "wat verandert", "cyclus"],
                        [["excentriciteit", "hoe uitgerekt de baan is", "ongeveer 100 000 jaar"],
                         ["obliquiteit", "de hoek waaronder de aardas staat", "ongeveer 41 000 jaar"],
                         ["precessie", "de richting waarin de as wijst", "ongeveer 23 000 jaar"]])),
            ("p", "De <strong>excentriciteit</strong> is de maat voor hoe uitgerekt de baan van de aarde is, "
                  "en die cyclus duurt ongeveer <strong>100 000</strong> jaar. Bij de "
                  "<strong>obliquiteit</strong> verandert <strong>de hoek waaronder de aardas staat</strong>. "
                  "<strong>Bij precessie verandert de richting waarin de aardas wijst, zoals bij een "
                  "tollende tol.</strong>"),
            ("p", "Waarom veroorzaken die cycli ijstijden? Niet doordat de aarde in het geheel minder zon "
                  "krijgt, maar doordat <strong>de zomerzon op hoge breedten zwakker wordt</strong>. Als de "
                  "sneeuw van de vorige winter de zomer overleeft, ligt er het jaar erop nog meer, en zo "
                  "bouwt een ijskap zich op."),
        ]),
        dict(kop="De andere natuurlijke oorzaken", blokken=[
            ("p", "De vakfiche noemt drie natuurlijke oorzaken van klimaatverandering: <strong>de "
                  "Milanković-variabelen</strong>, <strong>aërosolen en vulkanisme</strong>, en <strong>de "
                  "spreiding van de landmassa's</strong>."),
            ("p", "Een <strong>aërosol</strong> is <strong>een piepklein deeltje dat in de lucht "
                  "zweeft</strong>. Een zware vulkaanuitbarsting blaast er miljoenen tonnen van de "
                  "stratosfeer in, en daardoor <strong>koelt ze de aarde een jaar of langer af</strong>. "
                  "<strong>Ze warmt de aarde in de jaren erna dus niet op</strong>, al zou je dat bij zoveel "
                  "vuur verwachten."),
            ("p", "De ligging van de continenten telt mee <strong>omdat ze de banen van de zeestromen "
                  "bepaalt</strong>, en die verdelen de warmte over de aarde. <strong>Een continent pal op "
                  "een pool maakt het makkelijker om een ijskap te vormen</strong>: op land blijft sneeuw "
                  "liggen, op open water niet. Antarctica is daar het levende bewijs van."),
            ("p", "Bij het supercontinent <strong>Pangea</strong> hoorde <strong>een extreem continentaal "
                  "klimaat in het binnenland</strong>: duizenden kilometers van elke kust, dus gloeiend "
                  "heet in de zomer en ijzig in de winter, met bijna geen regen."),
        ]),
        dict(kop="Terugkoppeling en CO2", blokken=[
            ("p", "Een <strong>terugkoppeling</strong> in het klimaatsysteem is <strong>een gevolg dat de "
                  "oorzaak versterkt of afremt</strong>. <strong>Het smelten van zee-ijs werkt niet "
                  "afremmend maar juist versterkend</strong>: wit ijs kaatst zonlicht terug, donker water "
                  "slorpt het op, dus smelten geeft nog meer opwarming."),
            ("p", "<strong>CO2</strong> is in het geologische verleden zo belangrijk <strong>omdat het "
                  "warmtestraling in de atmosfeer houdt</strong>. Drie processen haalden het er in het "
                  "verleden weer uit: <strong>de verwering van gesteente</strong>, <strong>het begraven van "
                  "plantenresten als steenkool</strong> en <strong>het vastleggen van kalk door "
                  "zeeorganismen</strong>. Alle drie werken ze over honderdduizenden jaren."),
            ("p", "Kennis van het klimaat uit het verleden helpt vandaag <strong>omdat ze laat zien hoe het "
                  "systeem op CO2 reageert</strong>. Het verleden is het enige echte experiment dat we "
                  "hebben."),
        ]),
    ])


# ───────────────────────── 18. De huidige klimaatverandering
zet("de-huidige-klimaatverandering",
    titel="De huidige klimaatverandering",
    onder="Het versterkte broeikaseffect, wat we nu al meten, de terugkoppelingen, en het verschil tussen mitigatie en adaptatie.",
    secties=[
        dict(kop="Het broeikaseffect", blokken=[
            ("p", "Een <strong>broeikasgas</strong> <strong>houdt warmtestraling tegen</strong>: zonlicht "
                  "komt binnen, de aarde straalt warmte terug, en die warmtestraling wordt onderweg "
                  "opgevangen. <strong>Zonder enig broeikaseffect zou het op aarde gemiddeld ver onder nul "
                  "zijn</strong>, ongeveer achttien graden onder nul. Het effect zelf is dus geen probleem; "
                  "wij leven ervan."),
            ("fig", svg.broeikas(), "Zonlicht komt binnen, warmtestraling wordt deels tegengehouden."),
            ("p", "Broeikasgassen zijn onder meer <strong>koolstofdioxide</strong>, <strong>methaan</strong> "
                  "en <strong>waterdamp</strong>. Het gas dat vooral vrijkomt bij het verbranden van "
                  "steenkool, olie en gas is <strong>CO2</strong>."),
            ("p", "Het <strong>versterkte</strong> broeikaseffect heet zo <strong>omdat de mens een "
                  "bestaand effect verhoogt</strong>. We hebben het niet uitgevonden, we hebben de knop "
                  "hoger gezet."),
            ("p", "De menselijke activiteiten die de concentratie broeikasgassen verhogen: <strong>fossiele "
                  "brandstoffen verbranden</strong>, <strong>bossen kappen voor landbouw</strong> en "
                  "<strong>veeteelt en rijstvelden</strong>. Veeteelt geeft zoveel methaan <strong>omdat "
                  "koeien hun voedsel in de maag gisten</strong>: in de pens zetten bacteriën gras om, en "
                  "methaan is daar het restproduct van."),
        ]),
        dict(kop="Wat we nu al meten", blokken=[
            ("p", "De wereldtemperatuur is sinds het begin van de industrie ongeveer <strong>1,2</strong> "
                  "graden gestegen. <strong>De opwarming verloopt niet op elke plek even snel</strong>: het "
                  "Noordpoolgebied warmt ongeveer drie keer sneller op dan het gemiddelde, en land sneller "
                  "dan zee."),
            ("p", "Gevolgen die we nu al meten: <strong>een stijgende zeespiegel</strong>, <strong>gletsjers "
                  "die terugtrekken</strong> en <strong>meer en langere hittegolven</strong>."),
            ("p", "De zeespiegel stijgt om twee redenen tegelijk: <strong>landijs smelt en water zet "
                  "uit</strong>. Dat tweede verrast veel mensen, maar warmer water neemt meer plaats in, en "
                  "over een hele oceaandiepte telt dat zwaar door."),
            ("p", "De <strong>verzuring van de oceaan</strong> betekent dat <strong>de zee CO2 opneemt en "
                  "zuurder wordt</strong>. Dat is een apart probleem naast de opwarming: schelpen en "
                  "koraal bouwen hun kalkskelet moeilijker op in zuurder water."),
            ("p", "<strong>Een warmere atmosfeer kan meer waterdamp bevatten, waardoor buien heviger kunnen "
                  "uitvallen.</strong> Ongeveer zeven procent meer vocht per graad. Daarom horen zwaardere "
                  "buien en langere droogtes bij hetzelfde verhaal."),
            ("p", "Het gevolg dat de landbouw het hardst treft, zijn <strong>langere droogtes in de "
                  "zomer</strong>. En voor de natuur: <strong>soorten verschuiven of sterven uit</strong>."),
        ]),
        dict(kop="Hoe we weten dat het de mens is", blokken=[
            ("p", "<strong>De mens is de belangrijkste oorzaak</strong> van de huidige opwarming, en dat is "
                  "geen vermoeden. Dat de extra CO2 van fossiele brandstoffen komt, weten we <strong>aan de "
                  "verhouding van de koolstofisotopen</strong>: koolstof uit steenkool en olie is miljoenen "
                  "jaren oud en draagt een andere isotopenvingerafdruk dan koolstof uit een vulkaan of uit "
                  "de oceaan."),
            ("p", "<strong>De Milanković-cycli verklaren de opwarming van de laatste honderd jaar "
                  "niet.</strong> Die werken over tienduizenden jaren, en ze wijzen op dit moment zelfs "
                  "licht de andere kant op."),
            ("p", "<strong>Een strenge winter zegt niets over de opwarming, want één seizoen is nog geen "
                  "klimaat.</strong> Weer is wat er deze week gebeurt, klimaat is het gemiddelde over "
                  "dertig jaar."),
            ("p", "De organisatie van de Verenigde Naties die het klimaatonderzoek bundelt, is het "
                  "<strong>IPCC</strong>. Het doet zelf geen onderzoek: het vat samen wat duizenden studies "
                  "samen aantonen."),
        ]),
        dict(kop="Terugkoppelingen", blokken=[
            ("p", "Een <strong>positieve terugkoppeling</strong> is <strong>een gevolg dat de opwarming "
                  "versterkt</strong>; een <strong>negatieve terugkoppeling remt de opwarming af</strong>. "
                  "Positief betekent hier dus niet goed, enkel versterkend."),
            ("p", "Drie versterkende terugkoppelingen: <strong>het smelten van zee-ijs</strong>, <strong>het "
                  "ontdooien van permafrost</strong> en <strong>meer waterdamp in een warmere lucht</strong>."),
            ("p", "<strong>Permafrost</strong> is de altijd bevroren bodem die bij het ontdooien methaan "
                  "vrijgeeft. Daar ligt plantaardig materiaal in dat duizenden jaren bevroren bleef; dooit "
                  "het op, dan rot het en komt het als methaan en CO2 vrij."),
            ("p", "Een versterkende terugkoppeling is zorgwekkend <strong>omdat de opwarming zichzelf gaat "
                  "voortzetten</strong>: vanaf een bepaald punt heeft het systeem onze uitstoot niet meer "
                  "nodig om door te gaan."),
        ]),
        dict(kop="Scenario's en doelen", blokken=[
            ("p", "Een <strong>IPCC-scenario</strong> is <strong>een mogelijk verloop bij een bepaalde "
                  "uitstoot</strong>. Het is geen voorspelling maar een als-dan: stoten we zoveel uit, dan "
                  "komen we daar uit. <strong>Hoe warm het tegen 2100 wordt, hangt dus vooral af van "
                  "hoeveel we nog uitstoten.</strong>"),
            ("p", "Het akkoord van Parijs mikt op <strong>1,5</strong> graad als bovengrens."),
            ("p", "<strong>Klimaatneutraal</strong> of netto nul betekent dat een land evenveel broeikasgas "
                  "vastlegt als het uitstoot. Het betekent dus <strong>niet dat er helemaal geen "
                  "broeikasgas meer wordt uitgestoten</strong>: wat er nog uitgaat, moet er elders weer uit "
                  "de lucht gehaald worden."),
            ("p", "Zelfs als we vandaag zouden stoppen met uitstoten, blijft de temperatuur nog even "
                  "stijgen, <strong>omdat de oceaan heel traag op warmte reageert</strong>. Er zit al "
                  "warmte in het systeem die nog niet aan de oppervlakte te merken is."),
        ]),
        dict(kop="Mitigatie en adaptatie", blokken=[
            ("p", "<strong>Mitigatie</strong> is <strong>de oorzaak aanpakken en minder uitstoten</strong>. "
                  "<strong>Adaptatie</strong> is <strong>je aanpassen aan de gevolgen</strong>. Je hebt ze "
                  "allebei nodig: <strong>adaptatie alleen volstaat niet</strong>, want zonder mitigatie "
                  "blijven de gevolgen groeien tot er niets meer aan aan te passen valt."),
            ("p", tabel(["mitigatie", "adaptatie"],
                        [["minder vlees eten", "dijken en kustbescherming verhogen"],
                         ["overschakelen op zon en wind", "bomen planten tegen hitte in de stad"],
                         ["woningen beter isoleren", "regenwater opvangen tegen droogte"]])),
            ("p", "Een bos helpt <strong>omdat het koolstof vastlegt in hout en bodem</strong>: dat is "
                  "mitigatie. Een bos in de stad geeft daarnaast schaduw en verkoeling, en dat is adaptatie."),
            ("p", "Wat jij zelf kan doen dat echt gewicht heeft: <strong>minder met het vliegtuig en de "
                  "wagen reizen</strong>. Niet elke maatregel weegt even zwaar, en vervoer is bij ons een "
                  "van de grootste posten."),
        ]),
        dict(kop="Een kwestie van rechtvaardigheid", blokken=[
            ("p", "Klimaatverandering is ook een kwestie van rechtvaardigheid, <strong>omdat wie het minst "
                  "uitstoot het hardst getroffen wordt</strong>. De landen met de laagste uitstoot per "
                  "inwoner liggen vaak in de zones met de zwaarste droogte en de grootste kans op "
                  "overstroming, en ze hebben het minste geld om zich aan te passen."),
            ("p", "En het verschil met het verleden, in één zin: <strong>de huidige klimaatverandering gaat "
                  "veel sneller en komt van de mens</strong>."),
        ]),
    ])


# ───────────────────────── 19. Verstedelijking en ruimtegebruik
zet("verstedelijking-en-ruimtegebruik",
    titel="Verstedelijking en ruimtegebruik",
    onder="De vier fasen van verstedelijking, hoe de nevelstad Vlaanderen ontstond, en wat het beleid eraan wil doen.",
    secties=[
        dict(kop="Vier fasen", blokken=[
            ("p", "De fasen volgen elkaar in deze orde op: <strong>urbanisatie</strong>, "
                  "<strong>suburbanisatie</strong>, <strong>desurbanisatie en re-urbanisatie</strong>."),
            ("p", tabel(["fase", "wat er gebeurt"],
                        [["urbanisatie", "mensen trekken naar de stad"],
                         ["suburbanisatie", "de stadsrand groeit aan"],
                         ["desurbanisatie", "het stedelijk gebied als geheel verliest inwoners"],
                         ["re-urbanisatie", "de stadskern trekt opnieuw bewoners aan"]])),
            ("p", "<strong>Urbanisatie</strong> of verstedelijking is dus het naar de stad trekken van "
                  "mensen; bij <strong>suburbanisatie groeit de stadsrand aan</strong>. <strong>Bij "
                  "desurbanisatie verliest het stedelijk gebied als geheel inwoners</strong>: niet enkel de "
                  "kern maar ook de rand loopt leeg. Bij <strong>re-urbanisatie trekt de stadskern opnieuw "
                  "bewoners aan</strong>, en de groep die daarbij vaak als eerste terugkomt, zijn "
                  "<strong>jonge mensen zonder kinderen</strong>."),
            ("p", "Bij <strong>rurbanisatie</strong> <strong>trekken stedelingen naar het "
                  "platteland</strong>, maar ze nemen hun stedelijke leven mee: ze blijven in de stad "
                  "werken en winkelen. Dat dagelijks heen en weer reizen tussen woonplaats en werk heet "
                  "<strong>pendelen</strong>."),
        ]),
        dict(kop="Hoe een Vlaamse stad en haar rand eruitzien", blokken=[
            ("fig", svg.stadsplan(), "Van de kern naar buiten: elke gordel heeft haar eigen woonvorm."),
            ("p", "De woontypologieën die je in een Vlaamse stad en haar rand vindt: <strong>de rijwoning "
                  "in de negentiende-eeuwse gordel</strong>, <strong>de vrijstaande woning in een "
                  "verkaveling</strong> en <strong>het appartement in de stadskern</strong>. In de "
                  "twintigste-eeuwse gordel staat typisch <strong>de rijwoning in een gesloten "
                  "straat</strong>."),
            ("p", "Een <strong>verkaveling</strong> is <strong>een grond opgedeeld in "
                  "bouwpercelen</strong>. <strong>In Vlaanderen woont niet bijna iedereen in een "
                  "appartement of een rijwoning</strong>: de open bebouwing, de vrijstaande woning met "
                  "tuin rondom, is hier bijzonder sterk vertegenwoordigd, en dat is in Europa eerder "
                  "uitzonderlijk."),
            ("p", "De rand groeide in de twintigste eeuw zo sterk door drie dingen samen: <strong>goedkoop "
                  "treinvervoer en later de wagen</strong>, <strong>de eigen woning werd "
                  "aangemoedigd</strong>, en <strong>er stond ruim woongebied op het plan</strong>. Het "
                  "uitzwermen van bebouwing rond een stad heet met een Engelse term <strong>urban "
                  "sprawl</strong>."),
        ]),
        dict(kop="De nevelstad", blokken=[
            ("p", "<strong>Vlaanderen bestaat niet uit enkele grote steden met daartussen nog bijna lege "
                  "open ruimte.</strong> Met de <strong>nevelstad Vlaanderen</strong> bedoelen we dat "
                  "<strong>de bebouwing overal verspreid ligt</strong>: er is bijna geen plek waar je geen "
                  "huis ziet staan."),
            ("p", "Een kaart van de nachtelijke lichten tekent Vlaanderen daarom zo helder: <strong>de "
                  "bebouwing en de wegen liggen overal</strong>. Vlaanderen is op zo'n beeld een van de "
                  "best verlichte plekken ter wereld, en dat is geen compliment."),
            ("p", "Bebouwing die als een lange rij langs een weg staat, heet <strong>lintbebouwing</strong>. "
                  "Ze is nadelig <strong>omdat ze de open ruimte in stukken snijdt</strong>."),
        ]),
        dict(kop="Ruimtebeslag, verharding en versnippering", blokken=[
            ("p", "<strong>Ruimtebeslag</strong> is <strong>de oppervlakte die de mens inneemt</strong>; "
                  "<strong>verharding</strong> is dat <strong>de grond bedekt is met beton of "
                  "asfalt</strong>. Die twee zijn niet hetzelfde: een tuin hoort bij het ruimtebeslag maar "
                  "is niet verhard."),
            ("p", "Ongeveer <strong>33</strong> procent van Vlaanderen is in gebruik door de mens: een "
                  "derde. <strong>Verharding verhoogt het risico op wateroverlast na een zware "
                  "bui</strong>, want het water kan nergens de grond in."),
            ("p", "<strong>Versnippering</strong> is dat <strong>de open ruimte in losse stukjes "
                  "uiteenvalt</strong>. Verspreide bebouwing heeft drie gevolgen: <strong>duurdere "
                  "leidingen en wegen per woning</strong>, <strong>meer autoverkeer en langere "
                  "ritten</strong>, en <strong>versnippering van natuur en landbouw</strong>."),
        ]),
        dict(kop="Het hitte-eiland", blokken=[
            ("p", "Het <strong>stedelijk hitte-eiland</strong> betekent dat <strong>de stad warmer is dan "
                  "haar omgeving</strong>. <strong>Het verschil is het grootst op een zomernacht</strong>: "
                  "overdag warmt alles op, maar 's nachts geven beton en steen hun warmte traag af terwijl "
                  "het platteland snel afkoelt."),
            ("p", "Maatregelen die het verzachten: <strong>bomen planten in de straten</strong>, "
                  "<strong>verharding wegnemen voor groen</strong> en <strong>water in de stad "
                  "brengen</strong>."),
        ]),
        dict(kop="Wie beslist over de ruimte", blokken=[
            ("p", tabel(["plan", "wanneer", "wat het deed"],
                        [["het gewestplan", "vanaf de jaren zeventig",
                          "de eerste kaart met bestemmingen per perceel"],
                         ["het RSV", "1997",
                          "het Ruimtelijk Structuurplan Vlaanderen, opvolger van de gewestplannen"],
                         ["het BRV", "vandaag",
                          "het Beleidsplan Ruimte Vlaanderen: bijkomend ruimtebeslag naar nul"]])),
            ("p", "Het <strong>gewestplan</strong> was dus <strong>de eerste kaart met bestemmingen per "
                  "perceel</strong>; in 1997 volgde het <strong>RSV</strong>. Het "
                  "<strong>Beleidsplan Ruimte Vlaanderen</strong> wil <strong>het bijkomend ruimtebeslag "
                  "naar nul brengen</strong>. Dat betekent <strong>niet dat er tegen 2040 helemaal geen "
                  "nieuwe woningen meer bijkomen</strong>: ze moeten komen op grond die al in gebruik is."),
            ("p", "Dat is precies wat de <strong>bouwshift</strong> is: <strong>bouwen in de kernen, niet "
                  "in open ruimte</strong>. De kernkwaliteiten die het BRV voor een goede plek noemt: "
                  "<strong>nabijheid van voorzieningen</strong>, <strong>een goed bereikbare ligging</strong> "
                  "en <strong>ruimte voor water en groen</strong>. Het begrip dat past bij een stad waar "
                  "alles op wandelafstand ligt, is <strong>nabijheid</strong>."),
            ("p", "<strong>Een gezin in een kern verbruikt minder ruimte en energie dan een gezin in een "
                  "verkaveling</strong>, niet meer: kleinere woning, gedeelde muren, kortere "
                  "verplaatsingen."),
            ("p", "De bouwshift is politiek zo moeilijk <strong>omdat wie bouwgrond heeft, waarde "
                  "verliest</strong>. Een perceel dat op het plan woongebied was en dat niet meer mag "
                  "worden, is van de ene dag op de andere veel minder waard, en daar hangt de vraag van de "
                  "planschade aan vast."),
        ]),
        dict(kop="Wie waar woont", blokken=[
            ("p", "<strong>Sociale segregatie</strong> in een stad is dat <strong>groepen in gescheiden "
                  "wijken wonen</strong>. <strong>Gentrificatie maakt een volkswijk op de duur "
                  "onbetaalbaar voor de oorspronkelijke bewoners</strong>: de wijk wordt opgeknapt, de "
                  "huurprijzen stijgen, en wie er altijd woonde moet weg."),
        ]),
    ])


# ───────────────────────── 20. Duurzaam ruimtegebruik
zet("duurzaam-ruimtegebruik",
    titel="Duurzaam ruimtegebruik",
    onder="Het omgevingsdenken met zijn drie principes, en waaraan je ziet of een plek goed gekozen is.",
    secties=[
        dict(kop="Het omgevingsdenken", blokken=[
            ("p", "<strong>Omgevingsdenken</strong> is <strong>de bestaande ruimte beter gebruiken</strong> "
                  "in plaats van nieuwe open ruimte aan te snijden. De eerste vraag die je stelt is "
                  "daarom: <strong>kan het op een plek die al in gebruik is?</strong>"),
            ("p", "De principes die erbij horen: <strong>intensivering</strong>, <strong>hergebruik en "
                  "verweving</strong>, en <strong>tijdelijk ruimtegebruik</strong>."),
        ]),
        dict(kop="Intensivering", blokken=[
            ("p", "<strong>Intensivering</strong> of verdichting is <strong>meer doen op dezelfde "
                  "oppervlakte</strong>. Ze staat vooraan in het omgevingsdenken <strong>omdat ze geen "
                  "nieuwe open ruimte vraagt</strong>."),
            ("p", "<strong>Intensiveren betekent niet altijd hoogbouw neerzetten.</strong> Een huis "
                  "opsplitsen in twee woningen, een tweede woning in een te diepe tuin, een leegstaande "
                  "verdieping boven een winkel bewonen: dat is allemaal verdichten. <strong>Een dorpskern "
                  "verdichten kan zelfs zonder dat er een gebouw bijkomt.</strong>"),
            ("p", "Leegstand boven winkels is een gemiste kans <strong>omdat die ruimte al centraal ligt en "
                  "er al is</strong>. Ze staat precies waar het beleid woningen wil: in de kern, bij de "
                  "voorzieningen."),
            ("p", "<strong>Kernversterking</strong> betekent <strong>de dorpskern aantrekkelijker "
                  "maken</strong>, zodat wonen daar aantrekkelijker wordt dan wonen in een lint."),
        ]),
        dict(kop="Hergebruik en verweving", blokken=[
            ("p", "<strong>Hergebruik</strong> is <strong>een bestaand gebouw een nieuwe functie "
                  "geven</strong>. Voorbeelden: <strong>een oude fabriek wordt woningen</strong>, <strong>een "
                  "leegstaande kerk wordt bibliotheek</strong>, <strong>een oud klooster wordt een "
                  "school</strong>. Een oud industrieterrein dat opnieuw ontwikkeld wordt, heet een "
                  "<strong>brownfield</strong>."),
            ("p", "<strong>Verweving</strong> is <strong>functies naast elkaar in één gebied</strong>: "
                  "wonen, werken, winkelen en school door elkaar in plaats van elk in een eigen zone. "
                  "<strong>Verweving van wonen en werken vermindert het aantal verplaatsingen</strong>, en "
                  "dat is de hele winst."),
            ("p", "Niet alles laat zich verweven. De functie die zich slecht met wonen verdraagt, is "
                  "<strong>een fabriek met zwaar vrachtverkeer</strong>: lawaai, trillingen en vrachtwagens "
                  "door een woonstraat."),
            ("p", "Een gebouw waarin wonen, winkels en kantoren samen zitten, is een <strong>gemengd "
                  "gebouw</strong> of multifunctioneel gebouw. En <strong>een project kan tegelijk "
                  "intensiveren en hergebruiken</strong>: de principes sluiten elkaar niet uit."),
        ]),
        dict(kop="Tijdelijk ruimtegebruik", blokken=[
            ("p", "<strong>Tijdelijk ruimtegebruik</strong> is <strong>een plek even benutten tot ze nodig "
                  "is</strong>. Voorbeelden: <strong>een buurttuin op een braakliggend terrein</strong>, "
                  "<strong>een pop-upbar in een leegstaand pand</strong>, <strong>een speelplein op een "
                  "toekomstige bouwwerf</strong>. Een winkel of café dat maar enkele maanden op een plek "
                  "zit, heet een <strong>pop-up</strong>."),
            ("p", "Let op het woord tijdelijk: het is <strong>niet bedoeld om een plek voorgoed een nieuwe "
                  "functie te geven</strong>. Het vult de jaren tussen twee bestemmingen in, zodat een "
                  "terrein niet nutteloos achter een hek ligt te wachten."),
        ]),
        dict(kop="Wat een plek goed maakt", blokken=[
            ("p", "Volgens het ruimtelijk beleid is een plek goed om te wonen als <strong>voorzieningen en "
                  "vervoer dichtbij zijn</strong>. De <strong>nabijheidsindex</strong> van een plek zegt "
                  "<strong>hoeveel voorzieningen er in de buurt liggen</strong>."),
            ("p", "Een kwalitatieve omgeving heeft <strong>een gezonde en veilige leefomgeving</strong>, "
                  "<strong>ruimte voor water en groen</strong>, en <strong>een goede bereikbaarheid te voet "
                  "en per fiets</strong>."),
            ("p", "Het nadeel van wonen op een plek met weinig openbaar vervoer is dat <strong>elke "
                  "verplaatsing een wagen vraagt</strong>. Daarom geldt het omgekeerde van wat je soms "
                  "hoort: <strong>je bouwt het best niet dichter op een plek zonder bus of trein</strong>. "
                  "Dichter bouwen hoort waar het vervoer al ligt."),
            ("p", "En de kostenkant: <strong>een woning in een kern is doorgaans goedkoper in onderhoud "
                  "voor de samenleving dan een woning in een lint</strong>. Per woning liggen er minder "
                  "meters riool, weg en leiding naartoe."),
            ("p", "Bij een nieuw bouwproject weeg je drie vragen af: <strong>ligt het dicht bij "
                  "voorzieningen?</strong>, <strong>neemt het open ruimte in?</strong> en <strong>kan het "
                  "water op het terrein blijven?</strong>"),
        ]),
        dict(kop="Water en ontharden", blokken=[
            ("p", "<strong>Ontharden</strong> is <strong>het weghalen van beton of asfalt om de grond weer "
                  "open te maken</strong>. <strong>Een tuin die helemaal is betegeld, laat geen regenwater "
                  "in de bodem zakken</strong>, en dat water moet dan ergens anders naartoe."),
            ("p", "Je plant ruimte voor water in een wijk <strong>omdat water dan kan bufferen bij een "
                  "bui</strong>. Een ondiepe kom in een wijk die regenwater opvangt en laat insijpelen, "
                  "heet een <strong>wadi</strong>."),
            ("p", "De ingrepen die een straat klimaatrobuust maken: <strong>bomen voor schaduw "
                  "planten</strong>, <strong>verharding wegnemen waar het kan</strong> en <strong>regenwater "
                  "ter plekke laten insijpelen</strong>."),
        ]),
        dict(kop="Slim bouwen en slim verdelen", blokken=[
            ("p", "Een gedeelde parking is beter dan een parking per gebouw <strong>omdat dezelfde plaatsen "
                  "op andere uren dienen</strong>: kantoren overdag, bewoners 's avonds."),
            ("p", "<strong>Circulair bouwen</strong> is bouwen waarbij materialen later opnieuw gebruikt "
                  "worden. Het voordeel van bouwen in hout of met herbruikbare onderdelen is dat <strong>het "
                  "gebouw later weer te ontmantelen is</strong>, in plaats van gesloopt te worden tot puin."),
            ("p", "<strong>Grondruil</strong> is soms nodig <strong>omdat het bouwrecht dan naar een betere "
                  "plek verschuift</strong>: wie een perceel heeft waar niet meer gebouwd mag worden, "
                  "krijgt een perceel waar het wel kan."),
            ("p", "Het bezwaar dat je het vaakst hoort tegen verdichten in een kern, is dat <strong>de "
                  "buurt drukte en minder licht vreest</strong>. Je maakt een verdichte wijk toch "
                  "aangenaam door <strong>groen en ontmoetingsruimte te voorzien</strong>."),
        ]),
    ])


# ───────────────────────── 21. Het landschap lezen
zet("het-landschap-lezen",
    titel="Het landschap lezen",
    onder="Hoe een landschap gegroeid is en hoe je dat afleest, met kaarten, satellietbeelden, een GIS en een systeemschema.",
    secties=[
        dict(kop="Landschapsgenese", blokken=[
            ("p", "<strong>Landschapsgenese</strong> is <strong>hoe een landschap gegroeid is</strong>. Een "
                  "landschap is nooit toeval en nooit af: <strong>het ligt niet sinds de ijstijd in grote "
                  "lijnen onveranderd</strong>, het verandert voortdurend, de laatste eeuw zelfs sneller "
                  "dan ooit."),
            ("p", "De factoren die samen een landschap vormen: <strong>de ondergrond en het reliëf</strong>, "
                  "<strong>het water en het klimaat</strong>, en <strong>het gebruik door de mens</strong>."),
            ("fig", svg.landschapslagen(), "De natuurlijke lagen onder een landschap, en wat de mens "
                                           "erbovenop legt."),
            ("p", "Het <strong>reliëf</strong> is de vorm van het oppervlak, met zijn hoogtes en laagtes. "
                  "Op een <strong>geologische doorsnede</strong> lees je <strong>de lagen onder het "
                  "oppervlak</strong> af, en die verklaren wat je boven ziet: <strong>een harde "
                  "gesteentelaag blijft als een heuvel of een rug in het landschap staan</strong>."),
            ("p", "Een kaart die met kleuren of lijnen de hoogte weergeeft, heet een "
                  "<strong>hoogtekaart</strong> of digitaal hoogtemodel."),
            ("fig", svg.hoogtelijnen(), "Liggen de hoogtelijnen dicht bij elkaar, dan is de helling steil."),
        ]),
        dict(kop="De hand van de mens", blokken=[
            ("p", "De sporen van de mens die je in een Vlaams landschap leest: <strong>de vorm en grootte "
                  "van de percelen</strong>, <strong>dijken, grachten en kanalen</strong>, en <strong>holle "
                  "wegen en houtkanten</strong>."),
            ("p", "<strong>Een rechte sloot of gracht verraadt dat de mens het water heeft geleid</strong>: "
                  "een beek die zichzelf graaft, kronkelt."),
            ("p", "Een <strong>holle weg</strong> is een weg die door eeuwen gebruik diep in de helling "
                  "ligt: karrenwielen maalden de grond los en de regen spoelde hem weg, tot de weg meters "
                  "lager lag dan de akker ernaast."),
            ("p", "Een <strong>kouter</strong> is <strong>een groot open akkerblok</strong>, op de beste "
                  "grond van het dorp. <strong>Een landschap met kleine percelen en veel houtkanten heet "
                  "geen open landschap</strong>, maar juist een gesloten of halfopen landschap: de "
                  "houtkanten sluiten het zicht af."),
            ("p", "De oude dorpskern ligt vaak op de rand van een beekdal, want daar had je <strong>droge "
                  "grond met water in de buurt</strong>: hoog genoeg om niet onder te lopen, laag genoeg "
                  "om een put te slaan. Om dezelfde reden liggen de Vlaamse steden zo vaak aan een rivier: "
                  "<strong>water gaf vervoer, kracht en drinkwater</strong>."),
            ("p", "De <strong>ruilverkaveling</strong> veranderde het landschap doordat <strong>percelen "
                  "groter en rechter werden</strong>. Dat maakte het boerenwerk met machines mogelijk, maar "
                  "het kostte houtkanten, holle wegen en kronkelende beken."),
            ("p", "In de Kempen staan vooral naaldbossen <strong>omdat ze op arme zandgrond geplant "
                  "werden</strong>: de heide werd in de negentiende eeuw bebost met den, een boom die het "
                  "op schrale grond uithoudt en mijnhout opleverde."),
        ]),
        dict(kop="Een landschap stap voor stap lezen", blokken=[
            ("p", "De stappen die je zet: <strong>de vormen en lijnen beschrijven</strong>, <strong>zoeken "
                  "welke processen ze maakten</strong>, en <strong>de ouderdom en opeenvolging "
                  "bepalen</strong>. Eerst wat, dan hoe, dan wanneer."),
            ("fig", svg.transect(), "Een transect: het landschap van opzij, met wat erop staat."),
            ("p", "Een <strong>oude kaart</strong> is nuttig <strong>omdat ze toont hoe het er vroeger "
                  "uitzag</strong>. <strong>De kaart van Ferraris uit het einde van de achttiende eeuw "
                  "toont Vlaanderen voor de industrialisatie</strong>, en ze is daarom het ijkpunt waar "
                  "landschapsonderzoekers alles mee vergelijken."),
            ("p", "Een <strong>landschapsrelict</strong> is <strong>een overblijfsel uit vroeger</strong>: "
                  "een holle weg, een oude haag, een perceelsgrens die al op Ferraris stond."),
        ]),
        dict(kop="Kijken van boven", blokken=[
            ("p", "Op een satellietbeeld in <strong>ware kleuren</strong> zie je <strong>het beeld zoals je "
                  "oog het zou zien</strong>. Maar <strong>een satelliet meet niet enkel het licht dat ons "
                  "oog kan zien</strong>: hij meet ook infrarood, en dat is het hele nut van <strong>valse "
                  "kleuren</strong>, namelijk <strong>om te zien wat het oog niet ziet</strong>."),
            ("p", "Op een klassiek valse-kleurenbeeld komt gezonde plantengroei in het <strong>rood</strong>: "
                  "bladeren kaatsen infrarood sterk terug, en die band wordt als rood weergegeven. Een "
                  "akker die er op een gewone foto groen bij ligt maar niet rood oplicht, is ziek of droog."),
            ("p", "Op een <strong>warmtebeeld van een stad</strong> lees je af <strong>waar de stad het "
                  "warmst is</strong>, <strong>welke pleinen in beton liggen</strong> en <strong>waar de "
                  "parken koel blijven</strong>. Het hitte-eiland wordt er zichtbaar in kleur."),
        ]),
        dict(kop="GIS en Geopunt", blokken=[
            ("p", "<strong>Een GIS laat je kaartlagen over elkaar leggen en met elkaar vergelijken.</strong> "
                  "De kaartentoepassing van de Vlaamse overheid heet <strong>Geopunt</strong>."),
            ("fig", svg.kaartlagen(), "Elke laag toont iets anders; samen beantwoorden ze de vraag."),
            ("p", "Lagen die je in Geopunt over elkaar kan leggen: <strong>luchtfoto's van verschillende "
                  "jaren</strong>, <strong>het digitale hoogtemodel</strong> en <strong>de bodemkaart van "
                  "Vlaanderen</strong>. Je legt twee luchtfoto's van verschillende jaren over elkaar "
                  "<strong>om de verandering te zien</strong>."),
            ("p", "Wil je weten of een perceel overstromingsgevoelig is, dan gebruik je <strong>de "
                  "kaartlagen van Geopunt</strong>. Dat is geen schatting maar een officiële laag, en ze "
                  "telt mee bij een bouwaanvraag en bij de verkoop van een woning."),
        ]),
        dict(kop="Duurzame ontwikkeling", blokken=[
            ("p", "De vijf P's van duurzame ontwikkeling zijn <strong>people, planet, prosperity, peace, "
                  "partnership</strong>."),
            ("fig", svg.vijfp(), "De vijf P's, elk met een voorbeeld."),
            ("p", "De Verenigde Naties stelden <strong>17</strong> duurzame ontwikkelingsdoelstellingen op. "
                  "Die <strong>gaan niet enkel over het milieu en het klimaat</strong>: armoede, onderwijs, "
                  "gezondheid, gelijkheid en vrede horen er net zo goed bij. De SDG die over steden en de "
                  "ruimte waarin we wonen gaat, is <strong>duurzame steden en gemeenschappen</strong>."),
        ]),
        dict(kop="Systeemdenken", blokken=[
            ("p", "Een <strong>systeemdenkschema</strong> laat zien <strong>hoe oorzaken en gevolgen "
                  "samenhangen</strong>. Het hoort drie onderdelen te hebben: <strong>factoren als "
                  "blokjes</strong>, <strong>pijlen die het verband aangeven</strong> en <strong>een plus of "
                  "min bij elke pijl</strong>."),
            ("p", "<strong>Een pijl met een plus staat voor een verband waarbij beide factoren samen "
                  "stijgen of samen dalen.</strong> Een min zet je bij een verband dat de andere kant op "
                  "werkt, zoals <strong>meer groen geeft minder hitte</strong>. Een lus in een "
                  "systeemschema die zichzelf versterkt, heet <strong>positief</strong> of versterkend."),
            ("p", "Een systeemschema is nuttig bij een ruimtelijk vraagstuk <strong>omdat het onverwachte "
                  "neveneffecten blootlegt</strong>. Een nieuwe weg die de files moet oplossen, trekt nieuw "
                  "verkeer aan; dat zie je pas als je de pijlen uittekent."),
        ]),
    ])
