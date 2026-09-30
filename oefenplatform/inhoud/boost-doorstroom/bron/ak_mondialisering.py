# -*- coding: utf-8 -*-
"""De vragen voor "Mondialisering" (🚀 Boost doorstroom, aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "mondialisering" (10 % van het
examen).

Deel 1 gaat over wat mondialisering is en in welke vormen ze voorkomt:
sociaal, economisch, cultureel en politiek, met de oorzaken erachter en de
impact op productie en consumptie.
Deel 2 gaat over de gevolgen die de fiche zelf opsomt: de
samenwerkingsverbanden tussen landen, spanningen tussen landen,
migratiebewegingen en ontvolking, braindrain en braingain, landgrabbing,
protectionisme en outsourcing.

De fiche noemt bij de samenwerkingsverbanden de Europese Unie, de Verenigde
Naties, de G8, de G20, Mercosur en de NAVO. In de vragen staat telkens wát een
verband is en waarvóór het dient, niet hoeveel leden het op dit ogenblik telt:
dat laatste verschuift, en dan klopt de vraag over twee jaar niet meer.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent mondialisering?",
        opties=[
            "Landen en mensen raken wereldwijd steeds meer met elkaar verweven",
            "Landen sluiten zich steeds meer van elkaar af",
            "De wereldbevolking verhuist naar de grote steden",
            "Elk land maakt steeds meer zijn eigen producten",
        ],
        antwoord=0,
        uitleg="Handel, geld, mensen, ideeën en informatie bewegen sneller en verder dan ooit. Wat aan de ene kant van de wereld gebeurt, wordt daardoor aan de andere kant voelbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ontwikkelingen hebben de mondialisering versneld? (meerdere antwoorden mogelijk)",
        opties=[
            "Goedkoper en sneller transport over zee en door de lucht",
            "Het internet en goedkope wereldwijde communicatie",
            "Handelsakkoorden die invoerrechten verlagen",
            "Strengere grenscontroles tussen alle landen",
            "Hogere invoerrechten op alle buitenlandse producten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Containers, vliegtuigen, datakabels en handelsverdragen brachten de wereld dichter bij elkaar. Strengere grenzen en hogere invoerrechten werken juist de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="De container heeft het zeetransport veel goedkoper gemaakt.",
        antwoord=True,
        uitleg="Voordien werd elk stuk vracht apart geladen. Met gestandaardiseerde containers duurt het laden van een schip uren in plaats van dagen, en dat drukte de vrachtprijs enorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gsm bevat metalen uit Congo, wordt ontworpen in de Verenigde Staten en gemonteerd in Azië. Van welke vorm van mondialisering is dat een voorbeeld?",
        opties=[
            "Economische mondialisering",
            "Culturele mondialisering",
            "Politieke mondialisering",
            "Sociale mondialisering",
        ],
        antwoord=0,
        uitleg="De productieketen ligt over verschillende continenten verspreid. Dat uit elkaar halen van ontwerp, grondstoffen en montage is typisch economische mondialisering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jongeren over de hele wereld volgen dezelfde muziek, series en mode. Waarvan is dat een voorbeeld?",
        opties=[
            "Culturele mondialisering",
            "Economische mondialisering",
            "Politieke mondialisering",
            "Demografische transitie",
        ],
        antwoord=0,
        uitleg="Gewoonten, smaak en taal reizen mee met de media. Het gevolg is dat het aanbod overal op elkaar begint te lijken, wat lokale tradities onder druk zet.",
    ),
    dict(
        type="waarofniet",
        vraag="Politieke mondialisering betekent dat landen samen afspraken maken over grensoverschrijdende problemen.",
        antwoord=True,
        uitleg="Klimaat, handel, gezondheid en veiligheid stoppen niet aan een grens. Daarom bestaan er verdragen en organisaties waarin landen samen beslissen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Mensen houden wereldwijd contact met familie in andere landen, via sociale media en goedkope vluchten. Wat noemt men dat?",
        opties=[
            "Sociale mondialisering",
            "Culturele mondialisering",
            "Economische mondialisering",
            "Politieke mondialisering",
        ],
        antwoord=0,
        uitleg="Netwerken van mensen strekken zich over landsgrenzen uit. Die banden sturen mee waar migranten naartoe trekken en waar ze geld naartoe sturen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de metalen bak waarin vracht over zee, spoor en weg vervoerd wordt zonder overladen?",
        antwoord=["container", "een container", "de container"],
        uitleg="Altijd dezelfde afmetingen, overal dezelfde kranen: dat is de hele truc. De container is een van de stilste maar krachtigste motoren van de mondialisering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gevolg van mondialisering voor wat wij consumeren?",
        opties=[
            "We kopen producten uit de hele wereld, het hele jaar door",
            "We kopen bijna alleen nog producten uit eigen streek",
            "We kopen jaarlijks minder producten dan vroeger",
            "We kopen enkel nog producten uit onze eigen klimaatzone",
        ],
        antwoord=0,
        uitleg="Aardbeien in december en avocado's uit Peru zijn gewoon geworden. De keerzijde is het transport dat daarvoor nodig is en de druk op het land waar die teelt gebeurt.",
    ),
    dict(
        type="waarofniet",
        vraag="Mondialisering heeft voor elk land en elke groep dezelfde gevolgen.",
        antwoord=False,
        uitleg="Wie kan uitvoeren en investeren, wint. Wie concurreert met goedkopere invoer of grondstoffen levert zonder ze te verwerken, verliest. Juist die ongelijke uitkomst maakt het thema politiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laten bedrijven hun productie vaak in andere landen uitvoeren?",
        opties=[
            "Lonen, belastingen en regels liggen daar vaak lager",
            "De klanten wonen daar bijna allemaal",
            "Het klimaat is daar altijd gunstiger",
            "De grondstoffen liggen daar altijd in de bodem",
        ],
        antwoord=0,
        uitleg="Kosten sturen de keuze. Soms telt ook de nabijheid van grondstoffen of van een groeiende afzetmarkt mee, maar loonkosten zijn meestal de eerste reden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nadelen brengt een lange internationale productieketen mee? (meerdere antwoorden mogelijk)",
        opties=[
            "Ze is kwetsbaar als er ergens een schakel wegvalt",
            "Ze veroorzaakt veel transport en dus uitstoot",
            "Ze maakt het moeilijk te controleren hoe er gewerkt wordt",
            "Ze maakt producten in de winkel altijd duurder",
            "Ze zorgt ervoor dat er minder soorten producten zijn",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kwetsbaarheid, transport en gebrek aan zicht op de arbeidsomstandigheden zijn de echte nadelen. Goedkoper en gevarieerder worden de producten er juist van.",
    ),
    dict(
        type="waarofniet",
        vraag="Wanneer in één land de fabrieken stilvallen, kunnen winkels aan de andere kant van de wereld leeg komen te staan.",
        antwoord=True,
        uitleg="Dat is precies het risico van een wereldwijde keten. Tijdens de coronacrisis en na de blokkade van het Suezkanaal in 2021 zag je dat effect wereldwijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met outsourcing?",
        opties=[
            "Werk uitbesteden aan een bedrijf in een ander land",
            "Een eigen fabriek bouwen in het eigen land",
            "Producten invoeren uit een buurland",
            "Een bedrijf helemaal sluiten zonder vervanging",
        ],
        antwoord=0,
        uitleg="Callcenters, boekhouding, softwarewerk en productie worden zo verplaatst. Voor het ontvangende land betekent dat werk, voor het vertrekkende land verlies van werk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het beschermen van de eigen markt met invoerrechten en quota?",
        antwoord=["protectionisme", "het protectionisme"],
        uitleg="Protectionisme is het tegendeel van vrijhandel. Het beschermt eigen bedrijven op korte termijn, maar maakt ingevoerde goederen duurder voor de eigen inwoners.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land legt hoge invoerrechten op buitenlands staal. Wat is een verwacht gevolg?",
        opties=[
            "Buitenlands staal wordt er duurder en minder gekocht",
            "Buitenlands staal wordt er goedkoper en meer gekocht",
            "De eigen staalfabrieken sluiten er onmiddellijk",
            "De wereldprijs van staal daalt er meteen door",
        ],
        antwoord=0,
        uitleg="Een invoerrecht is een belasting aan de grens. Eigen producenten krijgen ademruimte, maar bedrijven die staal verwerken betalen meer, en het andere land neemt vaak tegenmaatregelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Mondialisering maakt landen minder afhankelijk van elkaar.",
        antwoord=False,
        uitleg="Ze maakt hen juist veel afhankelijker. Energie, chips, medicijnen en voedsel komen voor een groot deel van elders, en dat wordt pas zichtbaar wanneer een aanvoerlijn stilvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelt een zeehaven in de mondialisering?",
        opties=[
            "Ze is een knooppunt waar wereldstromen samenkomen",
            "Ze bepaalt de wereldprijs van de goederen",
            "Ze vervangt het wegtransport volledig",
            "Ze beperkt de handel met andere werelddelen",
        ],
        antwoord=0,
        uitleg="Het grootste deel van de wereldhandel gaat over zee. Een haven als Rotterdam of Antwerpen is daardoor een plaats waar de wereldeconomie letterlijk aanlandt.",
    ),
    dict(
        type="waarofniet",
        vraag="Mondialisering speelt zich alleen af tussen bedrijven en overheden, niet tussen gewone mensen.",
        antwoord=False,
        uitleg="Wie vrienden heeft in een ander land, online kleren bestelt of naar een buitenlandse serie kijkt, doet eraan mee. Juist die alledaagse kant noemt men sociale en culturele mondialisering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de wereld soms een dorp geworden?",
        opties=[
            "Afstanden zijn in tijd en kost enorm gekrompen",
            "De aarde is in werkelijkheid kleiner geworden",
            "Er wonen wereldwijd minder mensen dan vroeger",
            "Alle landen hebben nu dezelfde regering",
        ],
        antwoord=0,
        uitleg="Een vlucht naar de andere kant van de wereld duurt een dag, een bericht een seconde. De werkelijke afstand bleef gelijk, de ervaren afstand werd veel kleiner.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting EU?",
        opties=[
            "Europese Unie",
            "Europees Uitvoerverbond",
            "Economische Unie",
            "Europese Ondernemingen",
        ],
        antwoord=0,
        uitleg="De Europese Unie is een samenwerkingsverband van Europese landen met een gemeenschappelijke markt, gezamenlijke regels en voor een deel een gezamenlijke munt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het belangrijkste doel van de Verenigde Naties?",
        opties=[
            "Vrede en samenwerking tussen bijna alle landen ter wereld",
            "Een gemeenschappelijke munt voor alle lidstaten",
            "Een gezamenlijk leger voor Europa en Noord-Amerika",
            "Vrijhandel tussen de landen van Zuid-Amerika",
        ],
        antwoord=0,
        uitleg="De VN werd na de Tweede Wereldoorlog opgericht om oorlog te voorkomen. Daarnaast werkt ze rond ontwikkeling, gezondheid, vluchtelingen en klimaat.",
    ),
    dict(
        type="waarofniet",
        vraag="De NAVO is in de eerste plaats een militair bondgenootschap.",
        antwoord=True,
        uitleg="Landen in Europa en Noord-Amerika beloven elkaar te verdedigen bij een aanval. Dat onderscheidt de NAVO van de EU, die vooral economisch en politiek werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is Mercosur?",
        opties=[
            "Een handelsblok van landen in Zuid-Amerika",
            "Een militair bondgenootschap in Azië",
            "Een organisatie van olieproducerende landen",
            "Een orgaan van de Verenigde Naties",
        ],
        antwoord=0,
        uitleg="Mercosur laat goederen tussen de aangesloten Zuid-Amerikaanse landen vlotter circuleren. Het is voor dat continent wat de interne markt voor Europa is, alleen minder ver doorgedreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voordelen haalt een land uit het lidmaatschap van een handelsblok? (meerdere antwoorden mogelijk)",
        opties=[
            "Lagere of geen invoerrechten bij de andere leden",
            "Een grotere afzetmarkt voor de eigen bedrijven",
            "Meer gewicht in onderhandelingen met andere blokken",
            "Volledige vrijheid om eigen invoerrechten te heffen",
            "Een eigen munt die enkel binnen dat land geldt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Toegang, schaal en onderhandelingsmacht zijn de winst. De prijs is dat een land een stuk van zijn eigen handelsbeleid uit handen geeft, en dat is meteen de kern van de discussie erover.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat de landen van de G20 afspreken, is voor hen daarna wettelijk verplicht.",
        antwoord=False,
        uitleg="De G20 brengt de belangrijkste economieën samen, rijke zowel als opkomende, maar maakt geen wetten. De afspraken zijn politieke beloftes; ze wegen zwaar, maar niemand kan ze afdwingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is landgrabbing?",
        opties=[
            "Buitenlandse bedrijven of staten kopen grote stukken landbouwgrond op",
            "Boeren voegen hun percelen samen tot grotere velden",
            "Een overheid onteigent grond voor een nieuwe autoweg",
            "Landbouwgrond wordt verkaveld voor nieuwe woningen",
        ],
        antwoord=0,
        uitleg="Het gebeurt vooral in landen met een lagere ontwikkelingsgraad en zwakke eigendomsregels. Lokale boeren verliezen er soms grond die hun familie al generaties bewerkt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het leeglopen van een streek doordat de inwoners wegtrekken?",
        antwoord=["ontvolking", "de ontvolking"],
        uitleg="Ontvolking treft vooral afgelegen plattelandsstreken. Wie vertrekt is meestal jong, en daardoor vergrijst wie achterblijft nog sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Afrikaans land leidt verpleegkundigen op, en velen vertrekken naar Europa. Wat gebeurt er?",
        opties=[
            "Braindrain in Afrika en braingain in Europa",
            "Braingain in Afrika en braindrain in Europa",
            "Landgrabbing in Afrika en outsourcing in Europa",
            "Protectionisme in Afrika en vrijhandel in Europa",
        ],
        antwoord=0,
        uitleg="Het land dat de opleiding betaalde, verliest de kennis; het land dat hen ontvangt, wint ze gratis. Daar staat tegenover dat die verpleegkundigen vaak geld naar huis sturen.",
    ),
    dict(
        type="waarofniet",
        vraag="Mondialisering kan spanningen tussen landen vergroten.",
        antwoord=True,
        uitleg="Wie de grondstoffen, de chips of de scheepvaartroutes in handen heeft, heeft macht. Juist de onderlinge afhankelijkheid maakt handel tot een drukmiddel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken landen handel soms als politiek drukmiddel?",
        opties=[
            "Omdat de tegenpartij afhankelijk is van die goederen",
            "Omdat handel geen invloed heeft op de economie",
            "Omdat invoerrechten door de VN verplicht zijn",
            "Omdat elk land al zijn eigen goederen kan maken",
        ],
        antwoord=0,
        uitleg="Sancties, uitvoerverboden en het dichtdraaien van een gaskraan werken alleen als de andere kant die goederen nodig heeft. Dat is de schaduwzijde van verwevenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen van mondialisering somt de vakfiche op? (meerdere antwoorden mogelijk)",
        opties=[
            "Migratiebewegingen en ontvolking",
            "Landgrabbing en protectionisme",
            "Braindrain, braingain en outsourcing",
            "Bodemerosie en verzilting van de grond",
            "Verschuiving van de klimaatzones",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt samenwerkingsverbanden, spanningen, migratie en ontvolking, braindrain en braingain, landgrabbing, protectionisme en outsourcing. Erosie en klimaatzones horen bij andere rubrieken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land kiest één keer tussen vrijhandel en protectionisme en blijft daar dan bij.",
        antwoord=False,
        uitleg="Vrijhandel haalt drempels weg, protectionisme zet ze op, en veel landen schuiven tussen die twee heen en weer. Ze beschermen de ene sector en laten de andere vrij, en dat verandert met de regering mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een streek in Zuid-Europa loopt leeg omdat jongeren naar de steden en naar het buitenland trekken. Welke gevolgen verwacht je? (meerdere antwoorden mogelijk)",
        opties=[
            "Scholen en winkels sluiten bij gebrek aan klanten",
            "De achterblijvende bevolking vergrijst sterk",
            "Huizen komen leeg te staan en vervallen",
            "De bevolkingsdichtheid van de streek stijgt",
            "Het geboortecijfer van de streek stijgt scherp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ontvolking versterkt zichzelf: minder mensen betekent minder voorzieningen, en dat maakt blijven nog minder aantrekkelijk. Dichtheid en geboortecijfer dalen juist.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord de handel zonder invoerrechten en drempels tussen landen?",
        antwoord=["vrijhandel", "de vrijhandel"],
        uitleg="Vrijhandel maakt goederen goedkoper en de keuze groter, maar zet bedrijven die niet kunnen concurreren onder druk. Protectionisme doet precies het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat landgrabbing zo vaak ter discussie?",
        opties=[
            "De lokale bevolking verliest grond die ze zelf bewerkte",
            "De grond wordt er daarna nooit meer bewerkt",
            "Het gebeurt uitsluitend in landen met een hoge HDI",
            "Het is bij internationaal verdrag volledig verboden",
        ],
        antwoord=0,
        uitleg="Op papier is de verkoop vaak wettelijk, maar wie het land al generaties bewerkte zonder eigendomsbewijs, staat plots buiten. De opbrengst gaat bovendien meestal naar de uitvoer.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie migreert, stuurt vaak geld naar familie in het land van herkomst.",
        antwoord=True,
        uitleg="Dat geld heet remittances. Voor sommige landen is het een grotere inkomstenbron dan alle ontwikkelingshulp samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt de ruimtelijke gevolgen van mondialisering in je eigen streek. Waar let je op?",
        opties=[
            "Distributiecentra, winkelketens en leegstaande fabrieken",
            "De geografische coördinaten van het gemeentehuis",
            "De hoogte van de hoogste heuvel van de streek",
            "De stand van de zon op de middag van de meting",
        ],
        antwoord=0,
        uitleg="Mondialisering laat sporen na in het landschap: magazijnen bij de afrit, dezelfde ketens in elke winkelstraat, fabrieken die hun werk naar elders zagen vertrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft mondialisering ook een keerzijde voor de plaatselijke cultuur?",
        opties=[
            "Het wereldwijde aanbod verdringt eigen gewoonten en talen",
            "Landen mogen hun eigen taal niet meer gebruiken",
            "Elk land moet dezelfde feestdagen gaan vieren",
            "Musea worden verplicht buitenlandse kunst te tonen",
        ],
        antwoord=0,
        uitleg="Wat overal te koop en te zien is, wint het makkelijk van wat maar op één plaats bestaat. Daarom beschermen landen hun taal, hun film en hun erfgoed vaak bewust.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land kan zich volledig aan de mondialisering onttrekken zonder gevolgen voor zijn economie.",
        antwoord=False,
        uitleg="Wie zich afsluit, verliest afzetmarkten, invoer van technologie en investeringen. Landen die het probeerden, betaalden dat met een veel trager groeiende welvaart.",
    ),
]
