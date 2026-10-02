# -*- coding: utf-8 -*-
"""De eerste en de tweede industriële revolutie.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de eerste
industriële revolutie in Engeland en in België, en de tweede industriële
revolutie vanaf ongeveer 1870, met de gevolgen voor het wonen, het werken en
het bevolkingsaantal.

Het thema levert de uitleg voor het volgende: de ongelijkheid en de sociale
strijd die uit dit nieuwe soort werk gegroeid zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In welk land begon de eerste industriële revolutie?",
        opties=[
            "in Engeland",
            "in Frankrijk",
            "in Duitsland",
            "in België",
        ],
        antwoord=0,
        uitleg="Van daar sloeg ze over naar het vasteland. België was het eerste land dat volgde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden hielpen Engeland als eerste te industrialiseren?",
        opties=[
            "steenkool en ijzererts lagen er dicht bij elkaar in de bodem",
            "kapitaal uit de handel en de kolonies kon er belegd worden",
            "de overheid bezat er alle fabrieken en alle werkplaatsen",
            "de bevolking van het land kromp er elk jaar een beetje",
        ],
        antwoord=[0, 1],
        uitleg="De bevolking groeide juist, en dat leverde zowel werkvolk als kopers op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitvinding maakte van steenkool de motor van de industrie?",
        opties=[
            "de stoommachine",
            "de telefoon",
            "de gloeilamp",
            "de dynamo",
        ],
        antwoord=0,
        uitleg="Zij zette warmte om in beweging. Daardoor hoefde een fabriek niet meer aan een rivier te staan.",
    ),
    dict(
        type="invultekst",
        vraag="Welke machine van James Watt bracht de eerste industriële revolutie op gang?",
        antwoord=["de stoommachine", "stoommachine"],
        uitleg="Watt verbeterde een bestaand ontwerp zo grondig dat het in een fabriek bruikbaar werd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bedrijfstak werd in de eerste industriële revolutie als eerste gemechaniseerd?",
        opties=[
            "de textielnijverheid",
            "de autonijverheid",
            "de chemische nijverheid",
            "de elektrische nijverheid",
        ],
        antwoord=0,
        uitleg="Spinnen en weven gingen als eerste de fabriek in. Thuiswevers konden die snelheid niet volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde de spoorweg aan de industrie?",
        opties=[
            "grondstoffen en goederen konden snel en goedkoop vervoerd worden",
            "fabrieken konden daardoor zonder arbeidskrachten blijven draaien",
            "de steenkool werd daardoor in de mijnen zelf verbruikt",
            "de thuisnijverheid op het platteland groeide daardoor sterk",
        ],
        antwoord=0,
        uitleg="Een fabriek kon daardoor voor een markt veel verder dan haar eigen streek werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat had de landbouw met de industriële revolutie te maken?",
        opties=[
            "meer opbrengst per akker voedde de groeiende steden",
            "de landbouw verdween in de negentiende eeuw volledig",
            "de boeren kochten de eerste stoommachines voor hun velden",
            "de landbouw leverde de steenkool voor de eerste fabrieken",
        ],
        antwoord=0,
        uitleg="Nieuwe gewassen en betere werkwijzen maakten handen vrij. Die handen gingen naar de fabriek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk land op het Europese vasteland industrialiseerde als eerste?",
        opties=[
            "België",
            "Italië",
            "Spanje",
            "Rusland",
        ],
        antwoord=0,
        uitleg="Steenkool in Wallonië, kapitaal in Brussel en machines uit Engeland kwamen hier vroeg samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke streken waren in België de eerste industriegebieden?",
        opties=[
            "de steenkoolbekkens van Luik, Henegouwen en de Borinage",
            "de textielstad Gent met haar spinnerijen en weverijen",
            "de Kempen met haar steenkoolmijnen vanaf het begin",
            "de kust met haar havens van Oostende en Zeebrugge",
        ],
        antwoord=[0, 1],
        uitleg="De Kempense mijnen openden pas na 1900. Tot dan lag de steenkool in het zuiden van het land.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Gentse ondernemer bracht rond 1800 een Engelse spinmachine naar hier?",
        antwoord=["Lieven Bauwens", "Bauwens"],
        uitleg="Engeland verbood de uitvoer van die machines. Hij smokkelde ze in stukken het land binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spoorlijn werd in 1835 als eerste van het vasteland geopend?",
        opties=[
            "de lijn tussen Brussel en Mechelen",
            "de lijn tussen Parijs en Lyon",
            "de lijn tussen Londen en Manchester",
            "de lijn tussen Berlijn en Hamburg",
        ],
        antwoord=0,
        uitleg="De jonge Belgische staat legde zelf een spoornet aan, en dat trok industrie aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legde de Belgische staat zelf spoorwegen aan?",
        opties=[
            "om de handel niet van de Nederlandse waterwegen af te laten hangen",
            "om de werkloze arbeiders van het platteland een loon te geven",
            "om de steenkool van de Kempen naar de kust te kunnen brengen",
            "om het leger van de koning sneller te kunnen laten oprukken",
        ],
        antwoord=0,
        uitleg="Nederland hield de Schelde in de gaten. Een eigen spoornet maakte België minder afhankelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De eerste industriële revolutie begon in de negentiende eeuw in Duitsland.",
        antwoord=False,
        uitleg="Ze begon in de tweede helft van de achttiende eeuw in Engeland. Duitsland volgde veel later.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor de industriële revolutie werd er thuis of in kleine werkplaatsen geproduceerd.",
        antwoord=True,
        uitleg="Wie wol spon of weefde, deed dat bij zich thuis, vaak naast het werk op het land.",
    ),
    dict(
        type="waarofniet",
        vraag="De eerste fabrieken stonden vaak bij een steenkoolbekken of bij een waterloop.",
        antwoord=True,
        uitleg="Een machine had brandstof of waterkracht nodig, en kolen vervoeren was duur.",
    ),
    dict(
        type="waarofniet",
        vraag="De industriële revolutie veranderde niets aan het aantal mensen in de steden.",
        antwoord=False,
        uitleg="Steden als Gent, Luik en Verviers groeiden in enkele decennia tot het dubbele en meer.",
    ),
    dict(
        type="waarofniet",
        vraag="België industrialiseerde grotendeels met machines en vaklui uit Engeland.",
        antwoord=True,
        uitleg="John Cockerill, zoon van een Engelse familie, bouwde in Seraing machines en later ook locomotieven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de eerste industriële revolutie in België kloppen?",
        opties=[
            "Wallonië was de streek van de steenkool en het staal",
            "Gent was de stad van de gemechaniseerde textiel",
            "Vlaanderen industrialiseerde vroeger dan Wallonië",
            "de Kempen leverden van het begin af aan de steenkool",
        ],
        antwoord=[0, 1],
        uitleg="Vlaanderen bleef lang landelijk, met de armoede in de linnennijverheid rond 1845 als dieptepunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekende de fabriek voor de werktijd van een arbeider?",
        opties=[
            "de klok van de fabriek bepaalde wanneer hij begon en stopte",
            "hij koos zelf wanneer hij zijn dagtaak begon en afmaakte",
            "hij werkte alleen bij daglicht, zoals op het land",
            "hij werkte in de winter niet, zoals in de landbouw",
        ],
        antwoord=0,
        uitleg="Wie te laat kwam, kreeg een boete. Dat vaste ritme was voor plattelandsmensen volkomen nieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een prent van een fabriek met hoge schoorstenen, naast rijen kleine huisjes. Welke tijd herken je?",
        opties=[
            "de negentiende eeuw, tijdens de industrialisering",
            "de zestiende eeuw, tijdens de ontdekkingsreizen",
            "de achttiende eeuw, voor de uitvinding van de stoommachine",
            "de twintigste eeuw, na de Tweede Wereldoorlog",
        ],
        antwoord=0,
        uitleg="De werkmanswoningen dicht tegen de fabriek zijn typisch voor de industriesteden van die eeuw.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer wordt de tweede industriële revolutie gesitueerd?",
        opties=[
            "vanaf ongeveer 1870",
            "vanaf ongeveer 1750",
            "vanaf ongeveer 1815",
            "vanaf ongeveer 1945",
        ],
        antwoord=0,
        uitleg="Ze loopt tot de Eerste Wereldoorlog. Nieuwe energiebronnen en nieuwe bedrijfstakken kenmerken haar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nieuwe energiebronnen horen bij de tweede industriële revolutie?",
        opties=[
            "elektriciteit",
            "aardolie",
            "waterkracht",
            "steenkool",
        ],
        antwoord=[0, 1],
        uitleg="Steenkool en waterkracht dreven de eerste golf al aan. Het nieuwe was stroom en olie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bedrijfstakken kwamen in de tweede industriële revolutie op?",
        opties=[
            "de chemische nijverheid met kunstmest en verfstoffen",
            "de elektrotechniek met lampen, dynamo's en motoren",
            "de linnennijverheid met vlas uit de eigen streek",
            "de huisnijverheid met spinnewielen en handweefgetouwen",
        ],
        antwoord=[0, 1],
        uitleg="Linnen en huisnijverheid gingen juist achteruit. Chemie en elektriciteit waren de nieuwe reuzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde de verbrandingsmotor aan het vervoer?",
        opties=[
            "auto's en vrachtwagens maakten vervoer over de weg mogelijk",
            "treinen konden daardoor voor het eerst op rails rijden",
            "schepen konden daardoor voor het eerst zonder zeil varen",
            "goederen konden daardoor niet meer per spoor vervoerd worden",
        ],
        antwoord=0,
        uitleg="De trein en het stoomschip bestonden al. Het nieuwe was dat een voertuig zijn brandstof meenam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde de wetenschap in de tweede industriële revolutie?",
        opties=[
            "bedrijven richtten eigen laboratoria op voor onderzoek",
            "uitvinders werkten vooral alleen in hun eigen werkplaats",
            "de wetenschap had op de nieuwe nijverheden geen invloed",
            "de universiteiten verboden onderzoek voor de industrie",
        ],
        antwoord=0,
        uitleg="Verfstoffen, kunstmest en geneesmiddelen kwamen uit een labo, niet uit het werkhuis van een knutselaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werden de bedrijven in de tweede industriële revolutie veel groter?",
        opties=[
            "de nieuwe machines en labo's vroegen heel veel kapitaal",
            "de staat verplichtte alle bedrijven om samen te smelten",
            "de arbeiders eisten dat er grotere fabrieken kwamen",
            "de kleine werkplaatsen werden bij wet verboden",
        ],
        antwoord=0,
        uitleg="Daarvoor kwamen naamloze vennootschappen en banken in beeld. Zo kon men geld van veel mensen bundelen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een onderneming waarvan het kapitaal in aandelen verdeeld is?",
        antwoord=["een naamloze vennootschap", "naamloze vennootschap", "nv"],
        uitleg="Wie een aandeel koopt, legt geld in en deelt in de winst. Zo kon een bedrijf heel groot worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kartel?",
        opties=[
            "een afspraak tussen bedrijven over prijzen of markten",
            "een vereniging van arbeiders die hun loon verdedigt",
            "een lening die een bank aan een fabrikant geeft",
            "een belasting op de invoer van vreemde goederen",
        ],
        antwoord=0,
        uitleg="Zo kon men de onderlinge concurrentie uitschakelen. Voor de koper betekende dat zelden lagere prijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekende de demografische transitie?",
        opties=[
            "het sterftecijfer daalde eerst, het geboortecijfer pas later",
            "het geboortecijfer daalde eerst, het sterftecijfer pas later",
            "het aantal inwoners van Europa bleef een eeuw lang gelijk",
            "het aantal inwoners van Europa halveerde in één eeuw",
        ],
        antwoord=0,
        uitleg="Tussen die twee dalingen in groeide de bevolking snel. Beter eten en betere hygiëne lagen aan de basis.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de trek van mensen van het platteland naar de stad?",
        antwoord=["verstedelijking", "urbanisatie", "de verstedelijking"],
        uitleg="De steden groeiden sneller dan er huizen en riolen bijkwamen. Vandaar de beluiken en de ziekten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe woonden arbeiders in de negentiende-eeuwse industriesteden vaak?",
        opties=[
            "in kleine huisjes rond een gesloten koer, met weinig licht",
            "in ruime woningen met een eigen tuin en stromend water",
            "in grote flatgebouwen met een lift en een wasplaats",
            "in de fabriek zelf, waar ze ook mochten overnachten",
        ],
        antwoord=0,
        uitleg="Zulke beluiken hadden één pomp en één toilet voor alle gezinnen. Tyfus en cholera vonden er hun weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kinderarbeid in de negentiende-eeuwse fabriek?",
        opties=[
            "kinderen werkten lange dagen voor een laag loon",
            "kinderen volgden les in een school van de fabriek",
            "kinderen mochten de machines niet eens benaderen",
            "kinderen werkten enkel tijdens de schoolvakanties",
        ],
        antwoord=0,
        uitleg="Ze waren goedkoop en pasten tussen de machines. In België kwam er pas in 1889 een eerste wet tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="De tweede industriële revolutie bracht elektriciteit en aardolie als nieuwe energiebronnen.",
        antwoord=True,
        uitleg="Daarmee kon een motor ook in een kleine werkplaats of in een voertuig staan.",
    ),
    dict(
        type="waarofniet",
        vraag="In de tweede industriële revolutie verdwenen de grote ondernemingen weer.",
        antwoord=False,
        uitleg="Het omgekeerde gebeurde: bedrijven smolten samen in trusts en kartels en werden reuzen.",
    ),
    dict(
        type="waarofniet",
        vraag="De industrialisering ging in Europa samen met een snelle groei van de bevolking.",
        antwoord=True,
        uitleg="Tussen 1800 en 1900 verdubbelde de bevolking van Europa ruimschoots, ondanks de uittocht naar Amerika.",
    ),
    dict(
        type="waarofniet",
        vraag="Kinderarbeid was in de Belgische fabrieken van 1850 bij wet verboden.",
        antwoord=False,
        uitleg="Er was toen geen enkele wet die het beperkte. De eerste kwam er in 1889, na jarenlange strijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De spoorwegen en de stoomschepen maakten de wereldhandel in de negentiende eeuw veel groter.",
        antwoord=True,
        uitleg="Graan uit Amerika en katoen uit Indië kwamen daardoor binnen handbereik van de Europese markt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het werk in een fabriek rond 1880 kloppen?",
        opties=[
            "de werkdag duurde vaak twaalf uur of langer",
            "er was geen vergoeding bij een arbeidsongeval",
            "er was een wettelijke vakantie van twee weken",
            "er was een wettelijk minimumloon per uur",
        ],
        antwoord=[0, 1],
        uitleg="Vakantie en minimumloon zijn verworvenheden van de twintigste eeuw, niet van de negentiende.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je de gevolgen van de industriële revolutie?",
        opties=[
            "in het economische domein, met de fabriek en de handel",
            "in het sociale domein, met het wonen en het werken",
            "in geen van de maatschappelijke domeinen van die tijd",
            "uitsluitend in het politieke domein van de wetgeving",
        ],
        antwoord=[0, 1],
        uitleg="Ze raakte alle domeinen, ook het politieke, maar economisch en sociaal zijn de meest zichtbare.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een grafiek met het aantal inwoners van Gent tussen 1800 en 1900. Wat verwacht je te zien?",
        opties=[
            "een stijging, vooral in de tweede helft van de eeuw",
            "een daling, want de mensen trokken naar het platteland",
            "een rechte lijn, want de bevolking bleef gelijk",
            "een stijging tot 1850 en daarna een scherpe daling",
        ],
        antwoord=0,
        uitleg="De textielfabrieken trokken werkvolk aan. Het aantal inwoners van de stad verdubbelde in die eeuw.",
    ),
]
