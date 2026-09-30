# -*- coding: utf-8 -*-
"""De vragen voor "Het versterkte broeikaseffect" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "het versterkt broeikaseffect"
(10 % van het examen).

Deel 1 gaat over hoe het werkt: de vier sferen (geosfeer, biosfeer, atmosfeer
en hydrosfeer), de koolstofcyclus en de uitwisseling van koolstof tussen die
sferen, de broeikasgassen (waterdamp, koolstofdioxide, methaan en lachgas), de
stralingsbalans met het begrip albedo, en het verschil tussen het natuurlijke
en het versterkte broeikaseffect.
Deel 2 gaat over oorzaken en gevolgen: de evolutie en de herkomst van de
uitstoot, en de gevolgen die de fiche opsomt, namelijk zeespiegelstijging, het
verschuiven van de klimaatzones en van de leefgebieden van planten en dieren,
extreme weerfenomenen en de verspreiding van tropische ziektes.

Het ene getal dat hier wél in de vragen staat, is dat de aarde zonder haar
natuurlijke broeikaseffect gemiddeld ongeveer achttien graden onder nul zou
zijn in plaats van ongeveer vijftien graden erboven. Dat is een berekend
natuurkundig gegeven dat niet jaarlijks verschuift. Alle andere cijfers staan
in de bron van de vraag zelf.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier sferen onderscheidt men op aarde?",
        opties=[
            "Geosfeer, biosfeer, atmosfeer en hydrosfeer",
            "Geosfeer, atmosfeer, stratosfeer en hydrosfeer",
            "Biosfeer, atmosfeer, troposfeer en klimaatsfeer",
            "Geosfeer, biosfeer, ozonsfeer en waterkringloop",
        ],
        antwoord=0,
        uitleg="De geosfeer is het gesteente, de biosfeer al wat leeft, de atmosfeer de lucht en de hydrosfeer al het water. Koolstof beweegt voortdurend tussen die vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke sfeer zit het water van de oceanen, de rivieren en het ijs?",
        opties=[
            "De hydrosfeer",
            "De geosfeer",
            "De biosfeer",
            "De atmosfeer",
        ],
        antwoord=0,
        uitleg="Hydro betekent water. De oceanen zijn meteen ook de grootste opslagplaats van koolstof buiten het gesteente, want CO₂ lost op in zeewater.",
    ),
    dict(
        type="waarofniet",
        vraag="Koolstof die eenmaal in een sfeer zit, blijft daar voorgoed.",
        antwoord=False,
        uitleg="Ze beweegt voortdurend. Een boom haalt koolstof uit de lucht, een dier eet de boom, het dier sterft en de koolstof gaat de bodem in, en via verbranding of verwering komt ze weer in de lucht. Dat is de koolstofcyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met koolstof bij fotosynthese?",
        opties=[
            "Ze gaat uit de atmosfeer naar de biosfeer",
            "Ze gaat uit de biosfeer naar de atmosfeer",
            "Ze gaat uit de geosfeer naar de hydrosfeer",
            "Ze gaat uit de hydrosfeer naar de geosfeer",
        ],
        antwoord=0,
        uitleg="Een plant neemt CO₂ op uit de lucht en bouwt daar met zonlicht suikers mee. Zo verhuist koolstof van de atmosfeer naar wat leeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Langs welke wegen komt koolstof uit de geosfeer weer in de atmosfeer terecht? (meerdere antwoorden mogelijk)",
        opties=[
            "Het verbranden van steenkool, olie en aardgas",
            "Vulkaanuitbarstingen die gas uitstoten",
            "Het maken van cement uit kalksteen",
            "Het aanplanten van een nieuw bos",
            "Het laten insijpelen van regenwater",
        ],
        antwoord=[0, 1, 2],
        uitleg="Fossiele brandstoffen, vulkanen en cementproductie halen koolstof uit het gesteente en zetten ze in de lucht. Een bos aanplanten werkt precies de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Fossiele brandstoffen zijn koolstof die miljoenen jaren geleden uit de lucht werd gehaald.",
        antwoord=True,
        uitleg="Planten en plankton legden die koolstof vast, en na miljoenen jaren onder druk werd dat steenkool, olie en gas. Door ze te verbranden zetten wij die oude koolstof in enkele eeuwen terug in de lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn broeikasgassen volgens de vakfiche? (meerdere antwoorden mogelijk)",
        opties=[
            "Koolstofdioxide",
            "Methaan",
            "Lachgas",
            "Zuurstof",
            "Stikstofgas",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt waterdamp, koolstofdioxide, methaan en lachgas. Zuurstof en stikstofgas vormen samen het grootste deel van de lucht maar werken niet als broeikasgas.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de scheikundige formule van methaan?",
        antwoord=["CH4", "ch4"],
        uitleg="Methaan is CH₄. Het komt onder meer van herkauwers, van rijstvelden, van stortplaatsen en van lekken bij de winning van gas en olie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de stralingsbalans van de aarde?",
        opties=[
            "De verhouding tussen binnenkomende en uitgaande straling",
            "De hoeveelheid zonlicht die de evenaar per dag krijgt",
            "Het verschil in temperatuur tussen dag en nacht",
            "De dikte van de atmosfeer boven een bepaalde plaats",
        ],
        antwoord=0,
        uitleg="De aarde ontvangt straling van de zon en geeft warmte terug aan de ruimte. Blijft er meer binnen dan er weggaat, dan warmt de aarde op tot de balans weer klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent albedo?",
        opties=[
            "Hoeveel straling een oppervlak terugkaatst",
            "Hoeveel warmte een oppervlak vasthoudt",
            "Hoeveel water een bodem kan opnemen",
            "Hoeveel CO₂ er in de lucht aanwezig is",
        ],
        antwoord=0,
        uitleg="Een hoog albedo betekent veel terugkaatsen. Verse sneeuw kaatst het grootste deel van het zonlicht terug, een donkere oceaan of een dicht bos bijna niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oppervlak heeft het hoogste albedo?",
        opties=[
            "Verse sneeuw op een gletsjer",
            "Open water van een oceaan",
            "Een donker naaldbos in de zomer",
            "Asfalt van een parkeerterrein",
        ],
        antwoord=0,
        uitleg="Wit kaatst terug, donker slorpt op. Daarom versterkt het smelten van sneeuw en ijs de opwarming: wat eronder tevoorschijn komt, is bijna altijd donkerder.",
    ),
    dict(
        type="waarofniet",
        vraag="Als zee-ijs smelt, komt er donkerder water bloot dat meer warmte opneemt.",
        antwoord=True,
        uitleg="Minder ijs betekent een lager albedo, dus meer opwarming, dus nog minder ijs. Zo'n zichzelf versterkende lus noemt men een terugkoppeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen broeikasgassen met de warmte die de aarde uitstraalt?",
        opties=[
            "Ze houden een deel ervan in de atmosfeer vast",
            "Ze kaatsen het zonlicht meteen terug de ruimte in",
            "Ze zetten warmte om in zichtbaar licht",
            "Ze koelen de onderste luchtlagen af",
        ],
        antwoord=0,
        uitleg="Zonlicht komt vlot binnen, maar de warmtestraling die de aarde teruggeeft, wordt deels opgevangen en opnieuw naar beneden gestuurd. Dat maakt het aan het oppervlak warmer.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder het natuurlijke broeikaseffect zou het op aarde gemiddeld ongeveer achttien graden onder nul zijn.",
        antwoord=True,
        uitleg="Nu is het gemiddeld ongeveer vijftien graden boven nul. Het natuurlijke broeikaseffect is dus geen probleem maar juist de reden dat er leven mogelijk is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het natuurlijke en het versterkte broeikaseffect?",
        opties=[
            "Het versterkte komt van de extra gassen die de mens uitstoot",
            "Het natuurlijke werkt enkel overdag en het versterkte 's nachts",
            "Het natuurlijke bestaat enkel boven de oceanen",
            "Het versterkte werkt enkel boven de poolstreken",
        ],
        antwoord=0,
        uitleg="Het mechanisme is hetzelfde. Het verschil is de hoeveelheid: door extra CO₂, methaan en lachgas blijft er meer warmte hangen dan vroeger.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het weerkaatsingsvermogen van een oppervlak, dat bij sneeuw hoog en bij een oceaan laag is?",
        antwoord=["albedo", "het albedo", "de albedo"],
        uitleg="Albedo is een verhoudingsgetal tussen nul en één. Het is een van de twee sleutelbegrippen waarmee je de stralingsbalans aan het broeikaseffect koppelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Waterdamp is een broeikasgas dat de mens rechtstreeks in de lucht brengt.",
        antwoord=False,
        uitleg="Waterdamp is wel degelijk een broeikasgas, en zelfs een belangrijk, maar de hoeveelheid ervan volgt de temperatuur. Warmere lucht houdt meer damp vast, en dat versterkt de opwarming die er al was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom houden de oceanen de opwarming voorlopig af?",
        opties=[
            "Ze nemen een groot deel van de extra warmte en CO₂ op",
            "Ze kaatsen het zonlicht bijna volledig terug",
            "Ze geven zelf geen enkele warmte af aan de lucht",
            "Ze bevatten geen koolstof in opgeloste vorm",
        ],
        antwoord=0,
        uitleg="De oceaan slorpt warmte en koolstof op, en dat vertraagt de opwarming van de lucht. Daar staat tegenover dat het water uitzet en verzuurt, en dat het die warmte later weer afgeeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan meet men dat de hoeveelheid CO₂ in de lucht al decennia stijgt? (meerdere antwoorden mogelijk)",
        opties=[
            "Aan metingen van meetstations verspreid over de wereld",
            "Aan luchtbelletjes in oude ijskernen uit het poolijs",
            "Aan langlopende reeksen die jaar na jaar worden aangevuld",
            "Aan het aantal zonuren van de voorbije zomer",
            "Aan de bevolkingsdichtheid van de meetplaats",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meetstations, ijskernen en lange meetreeksen wijzen alle drie dezelfde kant op. IJskernen laten toe om ver terug te kijken, tot lang voor er gemeten werd.",
    ),
    dict(
        type="waarofniet",
        vraag="Het broeikaseffect zelf is iets slechts dat we volledig zouden moeten wegwerken.",
        antwoord=False,
        uitleg="Zonder broeikaseffect zou de aarde te koud zijn om op te leven. Het probleem is niet het effect maar de versterking ervan door onze extra uitstoot.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar komt het grootste deel van de door de mens uitgestoten CO₂ vandaan?",
        opties=[
            "Uit het verbranden van steenkool, olie en aardgas",
            "Uit de ademhaling van mensen en dieren",
            "Uit het smelten van de gletsjers en het poolijs",
            "Uit de waterdamp boven de grote oceanen",
        ],
        antwoord=0,
        uitleg="Energie, transport, verwarming en industrie draaien grotendeels op fossiele brandstoffen. Ontbossing en cementproductie komen daar nog bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke bronnen komt methaan vooral? (meerdere antwoorden mogelijk)",
        opties=[
            "Herkauwers zoals runderen",
            "Rijstvelden onder water",
            "Stortplaatsen met rottend afval",
            "Zonnepanelen op daken",
            "Windmolens op de Noordzee",
        ],
        antwoord=[0, 1, 2],
        uitleg="Overal waar organisch materiaal zonder zuurstof afbreekt, ontstaat methaan. Daarbij komen nog de lekken bij de winning en het transport van aardgas.",
    ),
    dict(
        type="waarofniet",
        vraag="Lachgas komt in de landbouw vooral van het bemesten van de grond.",
        antwoord=True,
        uitleg="Bacteriën in de bodem zetten stikstof uit mest en kunstmest deels om in lachgas. Daarom telt de manier van bemesten mee in de klimaatbalans van een bedrijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt de zeespiegel door de opwarming?",
        opties=[
            "Water zet uit als het warmer wordt, en landijs smelt erbij",
            "Er valt wereldwijd meer regen dan er verdampt",
            "De oceaanbodem komt door de warmte omhoog",
            "Rivieren voeren meer water aan dan vroeger",
        ],
        antwoord=0,
        uitleg="Twee oorzaken tegelijk: warm water neemt meer plaats in, en het ijs van Groenland, Antarctica en de gletsjers voegt water toe dat eerst op land lag.",
    ),
    dict(
        type="waarofniet",
        vraag="Als drijvend zee-ijs smelt, stijgt daardoor de zeespiegel.",
        antwoord=False,
        uitleg="Drijvend ijs verplaatst al evenveel water als het weegt, dus het smelten ervan verandert het peil niet. Alleen ijs dat op land ligt, doet de zeespiegel stijgen. Zee-ijs telt wel mee via het albedo.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke richting verschuiven de klimaatzones door de opwarming?",
        opties=[
            "Naar de polen toe, en op bergen naar boven toe",
            "Naar de evenaar toe, en op bergen naar beneden toe",
            "Naar het oosten toe, met de draaiing van de aarde mee",
            "Naar het westen toe, tegen de draaiing van de aarde in",
        ],
        antwoord=0,
        uitleg="Wat warmer wordt, schuift naar koelere plaatsen op: hoger op de breedtegraad en hoger op de helling. Wie al op de top of aan de pool zit, kan nergens meer heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de leefgebieden van planten en dieren?",
        opties=[
            "Ze schuiven mee met de klimaatzones",
            "Ze blijven precies waar ze altijd lagen",
            "Ze verdwijnen allemaal binnen enkele jaren",
            "Ze verplaatsen zich enkel naar de evenaar",
        ],
        antwoord=0,
        uitleg="Soorten trekken mee naar koelere streken en hogere hoogtes. Wie traag is, of vastzit tussen steden en akkers, geraakt niet mee en komt in de problemen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord de grote verscheidenheid aan soorten planten en dieren in een gebied?",
        antwoord=["biodiversiteit", "de biodiversiteit"],
        uitleg="Biodiversiteit maakt een ecosysteem veerkrachtig. Verschuivende klimaatzones en versnipperde leefgebieden zetten die verscheidenheid onder zware druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke extreme weerfenomenen worden met de opwarming in verband gebracht? (meerdere antwoorden mogelijk)",
        opties=[
            "Langere en zwaardere hittegolven",
            "Hevigere buien met veel neerslag in korte tijd",
            "Langere droogteperiodes in bepaalde streken",
            "Een gelijkmatiger weer over het hele jaar",
            "Kortere en mildere zomers dan vroeger",
        ],
        antwoord=[0, 1, 2],
        uitleg="Warmere lucht houdt meer vocht vast, dus valt er meer in één keer, terwijl het er elders langer droog blijft. Het weer wordt grilliger, niet gelijkmatiger.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén hittegolf bewijst op zich dat het klimaat verandert.",
        antwoord=False,
        uitleg="Weer is wat er vandaag gebeurt, klimaat is het gemiddelde over dertig jaar. Eén hete zomer zegt weinig; dat hete zomers steeds vaker voorkomen, zegt wel iets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kunnen tropische ziektes zich uitbreiden naar onze streken?",
        opties=[
            "De muggen die ze overbrengen overleven hier steeds beter",
            "De ziekteverwekkers ontstaan hier spontaan door de warmte",
            "Mensen worden door de warmte vatbaarder voor elke ziekte",
            "De ziektes verplaatsen zich met de wind mee naar het noorden",
        ],
        antwoord=0,
        uitleg="Een mug heeft warmte nodig om zich voort te planten. Warmt een streek op, dan schuift het gebied waarin die mug kan leven mee, en de ziekte die hij draagt, schuift mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen van het versterkte broeikaseffect noemt de vakfiche? (meerdere antwoorden mogelijk)",
        opties=[
            "Zeespiegelstijging en verschuiving van klimaatzones",
            "Verschuiving van leefgebieden van planten en dieren",
            "Extreme weerfenomenen en tropische ziektes",
            "Versnippering van de open ruimte door wegen",
            "Braindrain uit landen met een lagere HDI",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die vijf staan letterlijk in de fiche. Versnippering hoort bij de rubriek duurzaamheid en braindrain bij mondialisering.",
    ),
    dict(
        type="waarofniet",
        vraag="Laaggelegen kustgebieden en eilanden lopen het grootste risico bij zeespiegelstijging.",
        antwoord=True,
        uitleg="Delta's zoals die van de Ganges en de Nijl en eilandstaten in de Stille Oceaan liggen nauwelijks boven het peil. Net daar wonen bovendien heel veel mensen dicht op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de opwarming voor Vlaanderen ook een waterprobleem?",
        opties=[
            "Meer hevige buien en langere droogtes tegelijk",
            "De Noordzee bevriest er vaker in de winter",
            "Er valt over het hele jaar veel minder regen",
            "Het grondwater warmt te snel op om te drinken",
        ],
        antwoord=0,
        uitleg="Bij een hevige bui loopt het water over verharde grond meteen weg, en bij droogte staat de grondwatertafel te laag. Beide uitersten komen vaker voor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het proces waarbij opgenomen CO₂ het zeewater zuurder maakt?",
        antwoord=["oceaanverzuring", "verzuring", "de oceaanverzuring"],
        uitleg="Opgeloste CO₂ vormt een zuur in het zeewater. Daardoor bouwen koralen en schelpdieren moeilijker hun kalkskelet op, en dat raakt de hele voedselketen in zee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een terugkoppeling in het klimaatsysteem?",
        opties=[
            "Een gevolg dat zijn eigen oorzaak versterkt of verzwakt",
            "Een meting die achteraf wordt bijgesteld",
            "Een klimaatmodel dat naar het verleden kijkt",
            "Een afspraak tussen landen over de uitstoot",
        ],
        antwoord=0,
        uitleg="Het smelten van ijs verlaagt het albedo, wat de opwarming versterkt, wat nog meer ijs doet smelten. Zulke lussen maken het systeem moeilijk voorspelbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Dooiende permafrost kan methaan en CO₂ vrijmaken die er duizenden jaren in opgesloten zaten.",
        antwoord=True,
        uitleg="In de bevroren bodem van Siberië en Canada zit enorm veel organisch materiaal. Ontdooit die, dan begint het te rotten en komen er broeikasgassen vrij: opnieuw een terugkoppeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een grafiek van de CO₂-hoeveelheid in de lucht sinds 1960. Waarop let je bij het lezen?",
        opties=[
            "De eenheid, de schaal van de assen en de gemeten periode",
            "De kleur van de lijn en de breedte van de grafiek",
            "De naam van de persoon die de grafiek tekende",
            "Het lettertype waarin de titel geschreven staat",
        ],
        antwoord=0,
        uitleg="Een afgeknipte as of een te korte periode kan elke trend laten verdwijnen of overdrijven. Bronkritiek begint altijd bij de assen en de periode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom treft de opwarming niet elk land even hard?",
        opties=[
            "Ligging, reliëf en welvaart bepalen mee hoe kwetsbaar een land is",
            "Alleen landen op het noordelijk halfrond warmen op",
            "Alleen landen langs de evenaar merken er iets van",
            "De opwarming volgt precies de landsgrenzen op de kaart",
        ],
        antwoord=0,
        uitleg="Een laaggelegen deltastaat met weinig middelen loopt veel meer risico dan een bergland met een hoge HDI. Wie het minst uitstootte, draagt vaak de zwaarste gevolgen.",
    ),
    dict(
        type="waarofniet",
        vraag="De landen met de hoogste uitstoot per inwoner zijn altijd ook de landen die er het hardst door getroffen worden.",
        antwoord=False,
        uitleg="Meestal is het omgekeerd. Landen met een lagere ontwikkelingsgraad stoten per inwoner veel minder uit en hebben tegelijk het minste geld om zich te beschermen. Dat is de kern van de klimaatrechtvaardigheid.",
    ),
]
