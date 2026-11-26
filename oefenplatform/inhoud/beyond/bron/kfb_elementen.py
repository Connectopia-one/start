# -*- coding: utf-8 -*-
"""Niet-westerse invloeden en kunsthistorische elementen.

Zesde thema kunstbeschouwing (fiche 3DDO):

    niet-westerse invloeden: Egyptische en Griekse invloeden in de
    beeldhouwkunst, Moorse en Oosterse invloeden in de architectuur,
    Oosterse en Afrikaanse invloeden in de muziek, Afrikaanse en Japanse
    invloeden in de schilderkunst
    kunsthistorische elementen: schoonheidsidealen, economische waarde,
    opdrachtgevers, genderdimensie, het bovennatuurlijke, vakmanschap

Bekende voorbeelden: Japonisme bij Van Gogh en Monet, Afrikaanse maskers
bij Picasso (Les Demoiselles d'Avignon), het Alhambra, de gamelan bij
Debussy, blues en jazz met Afrikaanse wortels, de Guerrilla Girls, Artemisia
Gentileschi, Duchamps Fontein.

Deel 1: niet-westerse invloeden en schoonheidsidealen.
Deel 2: economische waarde, opdrachtgevers, gender, het bovennatuurlijke en
vakmanschap.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke kunst inspireerde Van Gogh en Monet met vlakke kleuren, sterke contouren en ongewone uitsneden?",
        opties=[
            "de Japanse houtsneden",
            "de Romeinse portretbeelden in marmer",
            "de gotische glasramen in de kathedralen",
            "de prehistorische grotschilderingen van Lascaux",
        ],
        antwoord=0,
        uitleg="Japanse prenten kwamen na 1850 massaal naar Europa. Die invloed noemt men japonisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloed zie je in Les Demoiselles d'Avignon van Picasso?",
        opties=[
            "Afrikaanse maskers, met hoekige, vereenvoudigde gezichten",
            "Japanse houtsneden met golven en de berg Fuji",
            "Egyptische grafschilderingen met hiërogliefen",
            "Moorse tegels met sierlijke geometrische patronen",
        ],
        antwoord=0,
        uitleg="Picasso zag Afrikaanse maskers in een Parijs museum. De vereenvoudigde vormen hielpen hem op weg naar het kubisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gebouw in Spanje is een bekend voorbeeld van Moorse architectuur?",
        opties=[
            "het Alhambra in Granada",
            "de Notre-Dame in Parijs",
            "het Pantheon in Rome",
            "de Sint-Baafskathedraal in Gent",
        ],
        antwoord=0,
        uitleg="Het Alhambra heeft hoefijzerbogen, fijn stucwerk, tegels met geometrische patronen en binnentuinen met water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij Moorse invloeden in de architectuur?",
        opties=[
            "hoefijzerbogen",
            "geometrische patronen en sierlijke tegels",
            "luchtbogen en spitse torens",
            "zuilen in de Dorische orde zonder versiering",
        ],
        antwoord=[0, 1],
        uitleg="Luchtbogen zijn gotisch, de Dorische orde Grieks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke muziekstijlen hebben sterke Afrikaanse wortels?",
        opties=["blues", "jazz", "gregoriaans gezang", "barokke orgelmuziek"],
        antwoord=[0, 1],
        uitleg="Blues en jazz ontstonden bij Afro-Amerikanen, met ritmes, vraag en antwoord en blue notes uit Afrikaanse tradities.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke Franse componist liet zich inspireren door het Indonesische gamelanorkest?",
        opties=["Claude Debussy", "Johann Sebastian Bach", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart"],
        antwoord=0,
        uitleg="Debussy hoorde gamelan op de wereldtentoonstelling van 1889 in Parijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zie je Egyptische invloed in de vroege Griekse beeldhouwkunst?",
        opties=[
            "de vroege Griekse beelden staan stijf en frontaal, met één voet naar voren",
            "de vroege Griekse beelden zijn abstract, zonder herkenbare mensen",
            "de vroege Griekse beelden zijn gemaakt van gekleurd glas in lood, zoals kerkramen",
            "de vroege Griekse beelden tonen gezichten in hoekige vlakken van verschillende kanten",
        ],
        antwoord=0,
        uitleg="De vroege kouros-beelden lijken op Egyptische beelden. Later kwam het losse contrapposto.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het schoonheidsideaal in de klassieke Griekse beeldhouwkunst?",
        opties=[
            "een jong, gespierd lichaam met perfecte, berekende verhoudingen",
            "een oud gezicht met rimpels, zo realistisch mogelijk",
            "een lichaam met heel grote buik en heupen, zoals de Venus van Willendorf",
            "een figuur in hoekige vlakken, van meerdere kanten tegelijk bekeken",
        ],
        antwoord=0,
        uitleg="Polykleitos schreef zelfs een regel voor de ideale verhoudingen, de canon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het feit dat schoonheidsidealen verschillen tussen culturen?",
        opties=[
            "schoonheid hangt ook af van tijd en cultuur, niet enkel van het werk zelf",
            "enkel de westerse kunst heeft een echt schoonheidsideaal, andere culturen niet",
            "schoonheid is overal ter wereld en in elke tijd precies hetzelfde",
            "niet-westerse culturen hebben in hun geschiedenis nooit echte kunst gemaakt",
        ],
        antwoord=0,
        uitleg="Wat mooi is, verschilt. In sommige culturen staan versierde littekens, lange halzen of grote lippen voor schoonheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak past bij het schoonheidsideaal in de hedendaagse kunst?",
        opties=[
            "schoonheid is niet meer het doel: een werk mag ook lelijk, schokkend of gewoon een idee zijn",
            "elk hedendaags werk moet de perfecte Griekse verhoudingen volgen",
            "hedendaagse kunst toont enkel mooie landschappen in zacht licht, zoals bij de impressionisten",
            "hedendaagse kunst mag geen gewone voorwerpen uit het dagelijks leven gebruiken",
        ],
        antwoord=0,
        uitleg="Veel hedendaagse kunst wil vooral doen nadenken. Schoonheid is één mogelijkheid, geen verplichting.",
    ),
    dict(
        type="invultekst",
        vraag="De invloed van Japanse prenten op de westerse kunst van de 19de eeuw heet ...",
        antwoord=["japonisme", "japonaiserie"],
        uitleg="Van Gogh kopieerde zelfs Japanse prenten met olieverf.",
    ),
    dict(
        type="invultekst",
        vraag="Een boog in de vorm van een hoefijzer, typisch voor Moorse gebouwen, heet een ...",
        antwoord=["hoefijzerboog"],
        uitleg="Je ziet ze in de moskee van Córdoba en in het Alhambra.",
    ),
    dict(
        type="waarofniet",
        vraag="Westerse kunstenaars lieten zich nooit door niet-westerse kunst beïnvloeden.",
        antwoord=False,
        uitleg="Er zijn veel voorbeelden: japonisme, Afrikaanse maskers bij Picasso, gamelan bij Debussy, Moorse bogen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het schoonheidsideaal van de Romeinse portretten verschilde van het Griekse, omdat de Romeinen meer realisme zochten.",
        antwoord=True,
        uitleg="Romeinse portretten tonen rimpels en eigen trekken. De Grieken zochten eerder het ideaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Oosterse invloeden in de muziek zie je onder meer in andere toonladders en klankkleuren.",
        antwoord=True,
        uitleg="Debussy gebruikte bijvoorbeeld toonladders die aan gamelan doen denken.",
    ),
    dict(
        type="waarofniet",
        vraag="Afrikaanse maskers werden in de 20ste eeuw door westerse schilders vooral nagetekend om ze zo realistisch mogelijk te kopiëren.",
        antwoord=False,
        uitleg="Ze inspireerden net tot vereenvoudiging en vervorming, niet tot realistische kopieën.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien westers schilderij uit de 19de eeuw: een brug over water, vlakke kleuren, dikke contourlijnen, een hoge horizon en een waaier op de voorgrond. Welke invloed zie je wellicht?",
        opties=[
            "Japanse invloed",
            "Afrikaanse invloed",
            "Egyptische invloed",
            "Romeinse invloed",
        ],
        antwoord=0,
        uitleg="Vlakke kleuren, contourlijnen, een waaier en een brug zijn typische kenmerken van japonisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kwamen in de 19de en 20ste eeuw zoveel niet-westerse voorwerpen naar Europa?",
        opties=[
            "door handel, wereldtentoonstellingen en de koloniale overheersing",
            "door het internet, de televisie en goedkope vliegtuigreizen voor iedereen",
            "omdat de paus dat vroeg aan alle kunstenaars in Rome",
            "omdat westerse musea toen geen eigen kunst meer hadden om in hun zalen te tonen",
        ],
        antwoord=0,
        uitleg="Veel voorwerpen kwamen via de koloniale handel naar Europa. Over de teruggave van sommige ervan wordt vandaag gepraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beschrijving past bij het Griekse schoonheidsideaal en niet bij het Romeinse portret?",
        opties=[
            "jong, perfect en tijdloos",
            "oud, gerimpeld en herkenbaar",
            "realistisch, met littekens en wratten",
            "persoonlijk, met eigen trekken van één bepaalde man",
        ],
        antwoord=0,
        uitleg="Het Griekse ideaal is tijdloos en perfect. De andere beschrijvingen passen bij de Romeinse portretten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men in Moorse kunst vaak geometrische patronen en sierlijke letters in plaats van mensen?",
        opties=[
            "in de islamitische traditie beeldt men in religieuze gebouwen liefst geen mensen of dieren af",
            "omdat de Moorse kunstenaars nooit geleerd hadden hoe je mensen en dieren tekent",
            "omdat geometrische patronen veel goedkoper waren dan verf, penselen en doeken",
            "omdat de koning enkel van wiskunde hield en niet van kunst",
        ],
        antwoord=0,
        uitleg="De culturele en religieuze context verklaart hier de vorm.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke factoren beïnvloeden de financiële waarde van een kunstwerk?",
        opties=[
            "de bekendheid van de kunstenaar",
            "de zeldzaamheid en de staat van het werk",
            "de kleur van de muur waaraan het werk hangt",
            "het aantal letters in de titel",
        ],
        antwoord=[0, 1],
        uitleg="Ook de herkomst, de vraag van verzamelaars en de mode spelen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met kunst en sociale status?",
        opties=[
            "wie dure kunst bezit of laat maken, toont daarmee rijkdom en aanzien",
            "kunst mag enkel door arme mensen gemaakt en gekocht worden",
            "kunstenaars hebben altijd de hoogste status in een samenleving",
            "kunst heeft niets te maken met hoe mensen in een samenleving naar elkaar kijken",
        ],
        antwoord=0,
        uitleg="Een schilderij in je huis of een portret van jezelf kon tonen hoe belangrijk je was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is culturele economie?",
        opties=[
            "het geld, de banen en het toerisme die kunst en cultuur opleveren voor een stad of land",
            "het geld dat één kunstenaar in een week uitgeeft aan verf, doeken en penselen",
            "de prijs van een ticket voor de bioscoop in het weekend",
            "het verbod om kunst te verkopen in een gewone winkel of op de markt van de stad",
        ],
        antwoord=0,
        uitleg="Musea, festivals en monumenten trekken bezoekers en zorgen voor werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liet een vorst zich vaak schilderen in een rijk kostuum, met zwaard of kroon, in een grote houding?",
        opties=[
            "om macht en invloed te tonen aan wie het portret zag",
            "omdat hij in het paleis geen gewone kleren had om aan te trekken",
            "om de schilder te helpen oefenen met moeilijke stoffen",
            "omdat het portret anders niet in het paleis mocht hangen",
        ],
        antwoord=0,
        uitleg="De opdrachtgever bepaalde mee wat er te zien was. Kunst diende hier als propaganda.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is iconografie?",
        opties=[
            "de studie van wat de figuren, voorwerpen en symbolen in een werk betekenen",
            "de techniek om kleine icoontjes voor een computer of een smartphone te tekenen",
            "het meten van de afmetingen en het gewicht van een schilderij in een museum",
            "de leer van hoe je verf maakt uit planten, aarde en mineralen",
        ],
        antwoord=0,
        uitleg="Een sleutel bij Petrus, een lam voor Christus of een schedel voor de dood zijn voorbeelden van iconografie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn vrouwen ondervertegenwoordigd in de kunstgeschiedenis?",
        opties=[
            "vrouwen kregen lang moeilijk toegang tot opleidingen, opdrachten en tentoonstellingen",
            "vrouwen hebben door de eeuwen heen helemaal geen kunst gemaakt",
            "vrouwen mochten enkel beelden maken en nooit schilderijen of tekeningen",
            "musea weigeren vandaag nog altijd elk werk dat door een vrouw gemaakt is",
        ],
        antwoord=0,
        uitleg="Kunstacademies lieten vrouwen lang niet toe, zeker niet bij het tekenen naar naaktmodel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunstenares uit de barok schilderde krachtige vrouwen uit de bijbel, zoals Judith?",
        opties=["Artemisia Gentileschi", "Frida Kahlo", "Berthe Morisot", "Georgia O'Keeffe"],
        antwoord=0,
        uitleg="Artemisia Gentileschi werkte in de 17de eeuw. De andere kunstenaressen zijn later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen de Guerrilla Girls?",
        opties=[
            "ze maken affiches en acties tegen de ongelijkheid van vrouwen in de kunstwereld",
            "ze schilderen landschappen met camouflagekleuren",
            "ze restaureren oude schilderijen in kerken en kathedralen over heel Europa",
            "ze verkopen kunst op grote veilingen voor zo veel mogelijk geld aan verzamelaars",
        ],
        antwoord=0,
        uitleg="Ze dragen gorillamaskers en tonen met cijfers hoe weinig vrouwen in musea hangen. Dat is kunst als genderactivisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed Marcel Duchamp met Fontein, een gewoon urinoir dat hij in een tentoonstelling zette?",
        opties=[
            "hij stelde de vraag of het idee belangrijker is dan het vakmanschap",
            "hij toonde dat hij beter kon beeldhouwen dan Michelangelo",
            "hij wilde een nieuwe soort sanitair verkopen aan musea en tentoonstellingszalen",
            "hij restaureerde een oud beeld uit de Romeinse tijd",
        ],
        antwoord=0,
        uitleg="Bij conceptuele kunst telt het idee meer dan het maken met de hand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt een restaurateur liefst de originele technieken en materialen?",
        opties=[
            "zo blijft het werk zo dicht mogelijk bij wat de kunstenaar bedoelde",
            "omdat nieuwe materialen altijd duurder zijn dan de oude materialen",
            "omdat musea volgens de wet geen nieuwe verf mogen kopen",
            "om het werk na de restauratie zo snel mogelijk te kunnen verkopen",
        ],
        antwoord=0,
        uitleg="Een goede restauratie respecteert het origineel en is liefst ook later nog ongedaan te maken.",
    ),
    dict(
        type="invultekst",
        vraag="De persoon of instelling die een kunstwerk bestelt en betaalt, heet de ...",
        antwoord=["opdrachtgever", "mecenas"],
        uitleg="Vroeger waren dat vooral de kerk, vorsten en rijke families.",
    ),
    dict(
        type="invultekst",
        vraag="Kunst waarbij het idee belangrijker is dan het maken met de hand, heet ... kunst.",
        antwoord=["conceptuele"],
        uitleg="Bij traditionele kunst staat het vakmanschap net centraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Vrouwen werden in de kunstgeschiedenis veel vaker afgebeeld dan dat ze zelf kunst maakten die in musea hangt.",
        antwoord=True,
        uitleg="Vrouwen waren vaak model of onderwerp, zelden de bekende kunstenaar.",
    ),
    dict(
        type="waarofniet",
        vraag="De prijs van een kunstwerk hangt enkel af van hoe goed het gemaakt is.",
        antwoord=False,
        uitleg="Bekendheid, zeldzaamheid, herkomst, mode en de vraag van verzamelaars spelen ook mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bovennatuurlijke is een belangrijke inspiratiebron voor religieuze en spirituele kunst.",
        antwoord=True,
        uitleg="Goden, engelen, geesten en het hiernamaals komen in kunst van bijna elke cultuur voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Bovennatuurlijke thema's verdwenen volledig uit de moderne kunst.",
        antwoord=False,
        uitleg="Ze komen nog voor, bijvoorbeeld in het surrealisme, met dromen, of bij kunstenaars die spiritualiteit zoeken, zoals Kandinsky.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schilderij toont een heilige met een stralenkrans boven het hoofd. Wat betekent die krans?",
        opties=[
            "hij duidt aan dat de figuur heilig of goddelijk is",
            "hij toont dat de figuur een koning met een kroon is",
            "hij toont dat het in de zomer heel warm en zonnig was",
            "hij is enkel een gouden versiering zonder enige betekenis",
        ],
        antwoord=0,
        uitleg="De stralenkrans of nimbus is een symbool voor het bovennatuurlijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met artistieke vernieuwing als deel van vakmanschap?",
        opties=[
            "een kunstenaar vindt een nieuwe techniek, vorm of manier van werken die anderen nog niet gebruikten",
            "een kunstenaar kopieert precies wat zijn leraar deed, zonder iets te veranderen",
            "een kunstenaar hangt een oud werk opnieuw op, maar dan in een nieuwe lijst",
            "een kunstenaar verkoopt zijn oude werk opnieuw aan een nieuwe koper",
        ],
        antwoord=0,
        uitleg="Van Eyck met olieverf, Monet met licht en Picasso met het kubisme zijn voorbeelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad bouwt een groot nieuw museum en ziet daarna veel meer toeristen en nieuwe restaurants. Welk kunsthistorisch element zie je hier?",
        opties=[
            "culturele economie",
            "genderdimensie",
            "het bovennatuurlijke",
            "het schoonheidsideaal",
        ],
        antwoord=0,
        uitleg="Kunst levert geld en werk op voor een stad. Een bekend voorbeeld is het Guggenheimmuseum in Bilbao.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een renaissanceschilderij toont de opdrachtgever zelf, knielend in een hoek naast de heiligen. Waarom?",
        opties=[
            "de opdrachtgever wilde zijn vroomheid en zijn belang tonen, en zo herinnerd worden",
            "de schilder vergat hem eerst en moest hem achteraf nog toevoegen",
            "de opdrachtgever was zelf een heilige die al lang gestorven was",
            "het was verplicht om in elk werk een toeschouwer te tonen die naar de heiligen kijkt",
        ],
        antwoord=0,
        uitleg="Zo'n schenkersportret toont geloof en status tegelijk. Je ziet het ook op het Lam Gods.",
    ),
]
