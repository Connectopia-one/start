# -*- coding: utf-8 -*-
"""De vragen voor "Landbouw, handel en toerisme" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "economische processen" (20 % van
het examen, samen met [[ak_grondstoffen]]). Dit thema neemt het tweede stuk:
landbouw, en handel en diensten.

Deel 1 gaat over de landbouw: welke landbouwsystemen waar voorkomen, waar
gegeven producten geteeld of gekweekt worden, de productiewijze (traditioneel
tegenover modern, extensief tegenover intensief, duurzaam tegenover niet
duurzaam), de afzetmarkt, en de geopolitieke, fysische en sociaaleconomische
factoren die het landbouwproces sturen. Let op: bij de landbouw noemt de fiche
bij de fysische factoren uitdrukkelijk ook de bodemkwaliteit en de ondergrond,
wat bij de industrie niet het geval is.
Deel 2 gaat over handel en diensten, met het toerisme als uitgewerkt geval:
waar het voorkomt, waarom het daar voorkomt, en hoe geopolitieke, fysische en
sociaaleconomische factoren het sturen.

Bij gewassen wordt telkens het verband met klimaat en bodem gelegd, niet enkel
de plaatsnaam. Anders wordt het een lijstje uit het hoofd, en dat is precies
wat de fiche niet vraagt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen akkerbouw en veeteelt?",
        opties=[
            "Akkerbouw teelt gewassen, veeteelt houdt dieren",
            "Akkerbouw gebeurt buiten, veeteelt altijd binnen",
            "Akkerbouw is modern, veeteelt is traditioneel",
            "Akkerbouw is duurzaam, veeteelt is dat nooit",
        ],
        antwoord=0,
        uitleg="Akkerbouw, veeteelt en tuinbouw zijn de grote landbouwsystemen. Veel bedrijven combineren ze trouwens: het graan van de akker voedt het vee in de stal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent extensieve landbouw?",
        opties=[
            "Weinig arbeid en middelen per hectare, op veel grond",
            "Veel arbeid en middelen per hectare, op weinig grond",
            "Landbouw die enkel voor de eigen familie produceert",
            "Landbouw die altijd zonder machines werkt",
        ],
        antwoord=0,
        uitleg="Extensief spreidt de inspanning over een grote oppervlakte, zoals schapenteelt in de Australische binnenlanden. Intensief concentreert alles op weinig grond, zoals de serres van het Westland.",
    ),
    dict(
        type="waarofniet",
        vraag="Intensieve landbouw haalt per hectare meer op dan extensieve landbouw.",
        antwoord=True,
        uitleg="Dat is net de bedoeling: meer arbeid, bemesting, water en technologie per hectare geven een hogere opbrengst per hectare. Of het per werkende ook meer opbrengt, is een andere vraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt rijst vooral in Zuid- en Oost-Azië geteeld?",
        opties=[
            "Het is er warm en er valt veel neerslag in het groeiseizoen",
            "De bodem bestaat er vooral uit droog woestijnzand",
            "Het reliëf is er overal hooggebergte boven de boomgrens",
            "Er is er nauwelijks arbeidskracht beschikbaar",
        ],
        antwoord=0,
        uitleg="Rijst heeft warmte en veel water nodig; de moesson levert precies dat. Op terrassen in de heuvels en in de vlaktes van de grote rivieren voedt die teelt honderden miljoenen mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teelten horen bij een mediterraan klimaat? (meerdere antwoorden mogelijk)",
        opties=[
            "Olijven",
            "Wijndruiven",
            "Citrusvruchten",
            "Rijst op ondergelopen velden",
            "Cacao in het regenwoud",
        ],
        antwoord=[0, 1, 2],
        uitleg="Olijven, wijnstokken en citrus verdragen de droge, warme zomer en de zachte, natte winter rond de Middellandse Zee. Rijst en cacao vragen een heel ander klimaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Koffie groeit het best in het warme laagland van de tropen, vlak bij de kust.",
        antwoord=False,
        uitleg="Koffie komt uit de tropen, maar juist van de hooglanden: daar is het koeler en groeit de boon trager, wat de smaak ten goede komt. Cacao groeit wél in het warme laagland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de zwarte aarde van Oekraïne zo geschikt voor graanteelt?",
        opties=[
            "Ze is heel vruchtbaar en houdt water goed vast",
            "Ze ligt op grote hoogte in een bergketen",
            "Ze bestaat bijna volledig uit los zand",
            "Ze is het hele jaar door bevroren",
        ],
        antwoord=0,
        uitleg="Zwarte aarde is dik en rijk aan humus. Samen met het vlakke reliëf maakt dat van die streek een van de graanschuren van de wereld, wat meteen ook een geopolitieke inzet is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de landbouwtak die zich met groenten, fruit en sierteelt bezighoudt, vaak in serres?",
        antwoord=["tuinbouw", "de tuinbouw"],
        uitleg="Tuinbouw werkt intensief op een kleine oppervlakte. In Vlaanderen en Nederland gebeurt veel ervan onder glas, met verwarming en belichting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fysische factoren beïnvloeden volgens de vakfiche het landbouwproces? (meerdere antwoorden mogelijk)",
        opties=[
            "Het klimaat en de klimaatverandering",
            "Het reliëf van het gebied",
            "De bodemkwaliteit en de ondergrond",
            "De staatsvorm van het land",
            "De Human Development Index",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij de landbouw komen bodemkwaliteit en ondergrond er uitdrukkelijk bij, naast klimaat en reliëf. Staatsvorm is geopolitiek, de HDI sociaaleconomisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een landbouwbedrijf dat veel kunstmest en bestrijdingsmiddelen gebruikt, werkt daarmee automatisch duurzaam.",
        antwoord=False,
        uitleg="Hoge opbrengsten en duurzaamheid zijn niet hetzelfde. Te veel mest belandt in het grond- en oppervlaktewater, en bestrijdingsmiddelen raken ook insecten die je net nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is schaalvergroting in de landbouw?",
        opties=[
            "Minder bedrijven die elk meer grond bewerken",
            "Meer bedrijven die elk minder grond bewerken",
            "Meer landbouwgrond die wordt volgebouwd",
            "Meer soorten gewassen per bedrijf telen",
        ],
        antwoord=0,
        uitleg="Wie stopt, wordt overgenomen door een buur die groter wordt. Grote machines en grote percelen verlagen de kostprijs, maar hagen, bomen en slootjes verdwijnen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen heeft schaalvergroting voor het landschap? (meerdere antwoorden mogelijk)",
        opties=[
            "Percelen worden groter en rechter",
            "Hagen en houtkanten verdwijnen",
            "Wegen en sloten worden rechtgetrokken",
            "Er komen meer kleine boerderijen bij",
            "De bodem wordt vanzelf vruchtbaarder",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voor grote machines moet het perceel groot en recht zijn. Dat kost landschapselementen, en zonder hagen en houtkanten krijgt de wind meer vat op de grond.",
    ),
    dict(
        type="waarofniet",
        vraag="Bodemerosie treedt sneller op wanneer een helling na de oogst kaal blijft liggen.",
        antwoord=True,
        uitleg="Zonder begroeiing spoelt de regen de vruchtbare bovenlaag weg. Daarom zaait men een groenbedekker in of ploegt men dwars op de helling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is bodemdegradatie?",
        opties=[
            "De kwaliteit van de bodem gaat achteruit",
            "De bodem wordt met vrachtwagens afgevoerd",
            "De bodem wordt bedekt met beton en asfalt",
            "De bodem wordt door een rivier aangevoerd",
        ],
        antwoord=0,
        uitleg="Verzilting, uitputting, verdichting en verlies van organische stof maken de grond minder productief. Herstel duurt tientallen jaren, verlies gaat in enkele seizoenen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het kappen van bos om er landbouwgrond of weiland van te maken?",
        antwoord=["ontbossing", "de ontbossing"],
        uitleg="Ontbossing voor soja, palmolie en vee is een van de grootste oorzaken van bosverlies wereldwijd. Ze kost biodiversiteit en laat koolstof vrij die in het bos opgeslagen zat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boer teelt gewassen om ze op de wereldmarkt te verkopen in plaats van voor eigen gebruik. Waarover gaat dat?",
        opties=[
            "Over de afzetmarkt van zijn producten",
            "Over de bodemkwaliteit van zijn grond",
            "Over het reliëf van zijn percelen",
            "Over de klimaatzone van zijn streek",
        ],
        antwoord=0,
        uitleg="De afzetmarkt is waar het product verkocht raakt. Die keuze bepaalt mee wat er geteeld wordt: wat de wereldmarkt vraagt, is niet altijd wat de streek zelf eet.",
    ),
    dict(
        type="waarofniet",
        vraag="Traditionele landbouw haalt per hectare altijd minder op dan moderne landbouw.",
        antwoord=False,
        uitleg="Per werkende wel: met de hand bewerkt één boer veel minder grond dan met een maaidorser. Per hectare niet: rijstterrassen die met de hand bewerkt worden, halen een heel hoge opbrengst uit weinig grond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beïnvloedt de politieke stabiliteit van een land ook zijn landbouw?",
        opties=[
            "Zonder rust is zaaien, oogsten en verkopen onmogelijk",
            "Zonder rust verandert de bodemkwaliteit van de grond",
            "Zonder rust verandert de klimaatzone van het land",
            "Zonder rust groeien gewassen trager dan gewoonlijk",
        ],
        antwoord=0,
        uitleg="Oorlog legt velden braak, vernielt opslag en verstoort de handel. Daarom leidt een conflict in een graanland tot hogere voedselprijzen ver daarbuiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken wijzen op een duurzamer landbouwbedrijf? (meerdere antwoorden mogelijk)",
        opties=[
            "Het houdt hagen en houtkanten op zijn percelen",
            "Het wisselt zijn gewassen af over de jaren",
            "Het beperkt de mest tot wat de grond opneemt",
            "Het ploegt elke helling recht van boven naar beneden",
            "Het teelt jaar na jaar hetzelfde gewas op hetzelfde perceel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Landschapselementen, vruchtwisseling en doordacht bemesten houden de bodem gezond. Recht van de helling ploegen en steeds hetzelfde telen putten hem juist uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaatverandering kan ervoor zorgen dat een gewas op een plaats niet meer rendeert.",
        antwoord=True,
        uitleg="Langere droogtes, andere neerslagpatronen en nieuwe ziekten verschuiven de gebieden waar een teelt lukt. Koffieboeren trekken daarom op sommige plaatsen hoger de berg op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de dienstensector?",
        opties=[
            "Werk waarbij men geen goederen maakt maar diensten levert",
            "Werk in de landbouw en de visserij samen",
            "Werk in de fabrieken en op bouwwerven",
            "Werk waarbij men grondstoffen ontgint",
        ],
        antwoord=0,
        uitleg="Onderwijs, zorg, handel, transport, bankwezen en toerisme horen erbij. In landen met een hoge ontwikkelingsgraad werkt het grootste deel van de mensen in die sector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom komt toerisme op sommige plaatsen sterk voor en elders nauwelijks?",
        opties=[
            "Klimaat, landschap, erfgoed en veiligheid spelen samen mee",
            "Het hangt bijna volledig af van de oppervlakte van het land",
            "Het hangt bijna volledig af van het aantal inwoners",
            "Het hangt bijna volledig af van de geografische lengte",
        ],
        antwoord=0,
        uitleg="Zon, sneeuw, bergen, kust, steden met geschiedenis en een veilige situatie trekken bezoekers. Ontbreekt er één van die voorwaarden, dan blijven ze weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Politieke onrust in een land doet het aantal toeristen er meestal snel dalen.",
        antwoord=True,
        uitleg="Toerisme is een van de eerste sectoren die een conflict voelt. Reisadviezen en annuleringen komen er binnen de week, en het herstel duurt jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fysische factoren maken een streek aantrekkelijk voor toerisme? (meerdere antwoorden mogelijk)",
        opties=[
            "Een klimaat met veel zonuren",
            "Een kust met stranden",
            "Een reliëf met bergen voor wintersport",
            "Een hoge Human Development Index",
            "Het lidmaatschap van een handelsblok",
        ],
        antwoord=[0, 1, 2],
        uitleg="Klimaat, kust en reliëf zijn fysische troeven. De HDI is sociaaleconomisch en een handelsblok geopolitiek; die spelen ook mee, maar via een andere weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ligt wintersporttoerisme vooral in hooggebergte?",
        opties=[
            "Daar ligt lang genoeg sneeuw om een seizoen te draaien",
            "Daar is de bevolkingsdichtheid het hoogst",
            "Daar is de bodem het meest vruchtbaar",
            "Daar liggen de meeste luchthavens van Europa",
        ],
        antwoord=0,
        uitleg="Hoogte betekent kou, en kou betekent sneeuw die blijft liggen. Door de klimaatverandering schuift de betrouwbare sneeuwgrens jaar na jaar hoger.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaatverandering vormt een bedreiging voor het wintersporttoerisme in de Alpen.",
        antwoord=True,
        uitleg="Lager gelegen skigebieden halen steeds moeilijker een volledig seizoen. Sneeuwkanonnen helpen tijdelijk, maar die vragen water en energie en werken enkel bij vorst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen kan massatoerisme voor een kuststreek hebben? (meerdere antwoorden mogelijk)",
        opties=[
            "Bebouwing die de duinen en de open ruimte opslorpt",
            "Druk op het drinkwater in het hoogseizoen",
            "Woningen die voor de eigen bewoners onbetaalbaar worden",
            "Een daling van de bevolkingsdichtheid in de zomer",
            "Een verschuiving van de klimaatzone van de streek",
        ],
        antwoord=[0, 1, 2],
        uitleg="Appartementen, waterverbruik en woningprijzen zijn de klassieke ruimtelijke gevolgen. De dichtheid stijgt in de zomer juist sterk, en de klimaatzone verschuift er niet van.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de sector die onderwijs, zorg, handel en toerisme omvat, en waarin geen goederen gemaakt worden?",
        antwoord=["dienstensector", "de dienstensector", "diensten"],
        uitleg="De dienstensector is in welvarende landen veruit de grootste werkgever. Landbouw is de eerste sector, industrie de tweede, diensten de derde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een luchthaven belangrijk voor het toerisme van een land?",
        opties=[
            "Ze brengt bezoekers van ver in enkele uren binnen",
            "Ze verbetert het klimaat van de omliggende streek",
            "Ze verhoogt de bodemkwaliteit van de streek",
            "Ze verlaagt het geboortecijfer van de streek",
        ],
        antwoord=0,
        uitleg="Bereikbaarheid beslist mee of een bestemming aanslaat. Eilanden zoals de Canarische Eilanden en de Malediven draaien bijna volledig op hun luchtverbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stad met veel erfgoed trekt alleen bezoekers als er ook een strand in de buurt ligt.",
        antwoord=False,
        uitleg="Brugge, Praag en Rome draaien op hun geschiedenis en hun stadsbeeld. Stadstoerisme is een eigen vorm van toerisme met eigen troeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten handel onderscheidt men meestal?",
        opties=[
            "Groothandel en kleinhandel",
            "Zware handel en lichte handel",
            "Vaste handel en losse handel",
            "Binnenlandse en buitenlandse industrie",
        ],
        antwoord=0,
        uitleg="Groothandel levert in grote hoeveelheden aan bedrijven en winkels, kleinhandel verkoopt rechtstreeks aan de consument. Allebei horen ze bij de dienstensector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een streek draait bijna volledig op toerisme. Welk risico houdt dat in?",
        opties=[
            "Bij een crisis valt de hele economie stil",
            "De bevolkingsdichtheid daalt er onvermijdelijk",
            "De bodem van de streek wordt er vruchtbaarder",
            "Het klimaat van de streek wordt er droger",
        ],
        antwoord=0,
        uitleg="Wie op één sector steunt, is kwetsbaar. Een epidemie, een aanslag of een economische crisis in de herkomstlanden doet het inkomen van een hele streek ineens wegvallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Online winkelen verandert niets aan waar de gebouwen van een handelsbedrijf staan.",
        antwoord=False,
        uitleg="Het verandert er net veel aan. Grote magazijnen zoeken een plaats bij een snelwegknooppunt of een haven, van waaruit ze snel kunnen leveren, en zo verschuift werk van de winkelstraat naar de rand van het land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke geopolitieke factoren beïnvloeden het toerisme? (meerdere antwoorden mogelijk)",
        opties=[
            "De stabiliteit van het land",
            "De staatsvorm van het land",
            "De samenwerkingsverbanden met andere landen",
            "De hoogte van de bergen in het land",
            "Het aantal zonuren per jaar",
        ],
        antwoord=[0, 1, 2],
        uitleg="Stabiliteit, staatsvorm en verdragen bepalen of mensen er veilig en zonder visum geraken. Bergen en zonuren zijn fysische troeven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de handel die rechtstreeks aan de consument verkoopt?",
        antwoord=["kleinhandel", "de kleinhandel", "detailhandel"],
        uitleg="De kleinhandel is de winkel waar jij binnenstapt. De groothandel daarachter bevoorraadt die winkels in grote hoeveelheden.",
    ),
    dict(
        type="waarofniet",
        vraag="De Human Development Index van een land speelt mee in hoeveel toerisme het aantrekt.",
        antwoord=True,
        uitleg="Zorg, veiligheid, water, wegen en opgeleid personeel maken een bestemming bruikbaar voor bezoekers. Een hoge HDI helpt daarbij, ook al bezoeken toeristen evengoed landen met een lagere HDI.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen veel grote distributiecentra langs autosnelwegen in plaats van in de stad?",
        opties=[
            "Grond is er goedkoper en vrachtwagens geraken er vlot weg",
            "Klanten komen er hun bestelling liever zelf ophalen",
            "De bevolkingsdichtheid is er hoger dan in de stad",
            "De grond is er vruchtbaarder dan in de stad",
        ],
        antwoord=0,
        uitleg="Zo'n gebouw heeft veel oppervlakte en veel vrachtverkeer nodig. In een stadscentrum is beide onbetaalbaar en onmogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bron toont dat een land vooral grondstoffen uitvoert en afgewerkte producten invoert. Wat besluit je?",
        opties=[
            "De bewerking en de winst gebeuren grotendeels elders",
            "Het land heeft een hoge Human Development Index",
            "Het land heeft een groot overschot op zijn handel",
            "Het land ligt noodzakelijk in de gematigde zone",
        ],
        antwoord=0,
        uitleg="Wie ruwe grondstoffen verkoopt en afgewerkte producten terugkoopt, laat de meerwaarde over aan de landen die verwerken. Dat patroon speelt in veel discussies over ontwikkeling een rol.",
    ),
    dict(
        type="waarofniet",
        vraag="Handel en diensten hebben geen invloed op het landschap, want ze maken niets.",
        antwoord=False,
        uitleg="Winkelcentra, kantoorparken, magazijnen, hotels en wegen nemen ruimte in. Op een luchtfoto van de rand van een stad zie je dat meteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag hoort bij het onderzoeken van de afzetmarkt van een product?",
        opties=[
            "Waar wordt het gekocht en door wie?",
            "Welke grondstof zit erin verwerkt?",
            "In welke klimaatzone ligt de fabriek?",
            "Hoeveel werknemers heeft de fabriek?",
        ],
        antwoord=0,
        uitleg="De afzetmarkt gaat over de kant van de verkoop: wie koopt het, waar, en in welke hoeveelheid. De andere vragen gaan over de productiekant.",
    ),
]
