# -*- coding: utf-8 -*-
"""De vragen voor "Een geografisch onderzoek voeren" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "geografisch onderzoek" (10 % van
het examen). De fiche waarschuwt erbij dat álle leerstof van de hele fiche in
dit deel verwerkt kan zitten.

Deel 1 gaat over het onderzoek zelf: de vier thema's waarover het kan gaan
(mobiliteit, waterproblematieken, veranderend landgebruik en
klimaatverandering), de onderzoeksvraag en de hypothese, de geografische
hulpbronnen, het terreinwerk met terreinkartering en de mentale kaart, en het
systeemdenkschema waarmee je de verbanden tussen de elementen toont.
Deel 2 gaat over Geopunt, de digitale kaart van de Vlaamse overheid die je op
het examen zelf mag gebruiken: de zoekbalk, het lagenpaneel, de legende, het
meetgereedschap, het aflezen van hoogtes en het transparant maken van een laag.
Daarbij hoort ook de vraag wat zo'n digitale kaart je níét vertelt.

Geopunt wordt hier beschreven zoals de fiche het doet, in termen van wát je
ermee moet kunnen. Nergens wordt gevraagd waar een knop precies staat: dat
verandert bij elke nieuwe versie van de site, en dan klopt de vraag niet meer.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarmee begint een geografisch onderzoek?",
        opties=[
            "Met een onderzoeksvraag of een hypothese",
            "Met het verzamelen van zo veel mogelijk kaarten",
            "Met het schrijven van het besluit van het onderzoek",
            "Met het meten van alle afstanden in het gebied",
        ],
        antwoord=0,
        uitleg="Zonder vraag weet je niet welke bron je nodig hebt. De vraag stuurt de keuze van de kaartlagen, de metingen en het terreinwerk, niet omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Over welke thema's kan je onderzoek volgens de vakfiche gaan? (meerdere antwoorden mogelijk)",
        opties=[
            "Mobiliteit, met files, lawaai en luchtvervuiling",
            "Waterproblemen, met tekort en overstromingen",
            "Veranderend landgebruik en klimaatverandering",
            "De geschiedenis van de Belgische staatshervorming",
            "De bouw van een fabriek in een ander werelddeel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt er vier: mobiliteit, waterproblematieken, veranderend landgebruik en klimaatverandering. Telkens onderzoek je de oorzaken én de gevolgen in het landschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese schrijf je pas op nadat je je gegevens verzameld hebt.",
        antwoord=False,
        uitleg="Je schrijft ze net op vóór je meet, zodat je achteraf eerlijk kan zeggen of ze klopte. Wie ze achteraf opschrijft, heeft altijd gelijk, en dat is geen onderzoek meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een goede onderzoeksvraag?",
        opties=[
            "Waarom staat het in onze gemeente elke ochtend stil?",
            "Is verkeer nu eigenlijk goed of slecht voor mensen?",
            "Hoeveel auto's bestaan er op de hele wereld samen?",
            "Wat vind jij zelf van de files in onze gemeente?",
        ],
        antwoord=0,
        uitleg="Een goede vraag is afgebakend in ruimte en tijd en je kan ze met bronnen beantwoorden. Een meningsvraag of een veel te brede vraag kan dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de geografische hulpbronnen uit de fiche? (meerdere antwoorden mogelijk)",
        opties=[
            "Kaarten, luchtfoto's en satellietbeelden",
            "Grafieken, tabellen en cijfergegevens",
            "Klimatogrammen en leeftijdshistogrammen",
            "De mening van je buren over het onderwerp",
            "Je eigen herinnering aan hoe het vroeger was",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche somt onder meer atlas, kaarten, satellietbeelden, foto's, tekeningen, teksten, cijfers, grafieken, klimatogrammen en diagrammen op. Meningen en herinneringen zijn interessant maar geen hulpbron in die zin.",
    ),
    dict(
        type="waarofniet",
        vraag="Een atlas is op het examen aardrijkskunde een toegelaten hulpmiddel.",
        antwoord=True,
        uitleg="De examencommissie geeft zelf een algemene wereldatlas mee. Daarom loont het om thuis met een atlas te werken, zodat je er tijdens het examen vlot in zoekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is terreinkartering?",
        opties=[
            "Op het terrein zelf noteren wat je waar ziet, op een kaart",
            "Een bestaande kaart van de gemeente natekenen op schaal",
            "Een luchtfoto van boven het terrein laten maken",
            "De coördinaten van het terrein online opzoeken",
        ],
        antwoord=0,
        uitleg="Je loopt het gebied af en tekent in wat er staat: bebouwing, groen, water, wegen, functies van gebouwen. Zo maak je van je waarneming een bron.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verwachting die je vooraf opschrijft en met je onderzoek wil toetsen?",
        antwoord=["hypothese", "een hypothese", "de hypothese"],
        uitleg="Een hypothese maakt je onderzoek toetsbaar. Zonder hypothese blijft een onderzoek een verzameling losse waarnemingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op het examen krijg je een filmpje van een terreinoefening in plaats van echt terreinwerk. Wat moet je daarmee doen?",
        opties=[
            "De informatie eruit halen die je onderzoek nodig heeft",
            "Het filmpje zo letterlijk mogelijk navertellen",
            "De duur van het filmpje in minuten noteren",
            "De naam van de maker van het filmpje opzoeken",
        ],
        antwoord=0,
        uitleg="Zo'n simulatie vervangt het terrein. Je herkent er landschapskenmerken in, je brengt ze aan op een kaart, en je gebruikt ze om je vraag te beantwoorden.",
    ),
    dict(
        type="waarofniet",
        vraag="Terreinwerk verandert niets aan de mentale kaart die je van een gebied hebt.",
        antwoord=False,
        uitleg="Wie een wijk heeft afgelopen, draagt daarna een veel scherper beeld van die wijk mee. Terreinwerk maakt je mentale kaart juist rijker en juister.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont een systeemdenkschema in een onderzoek?",
        opties=[
            "Hoe de elementen van je onderzoek met elkaar samenhangen",
            "In welke volgorde je de bronnen hebt geraadpleegd",
            "Hoeveel tijd elk onderdeel van je onderzoek kostte",
            "Welke kaartlagen het mooist naast elkaar staan",
        ],
        antwoord=0,
        uitleg="Pijlen tussen de elementen tonen oorzaak en gevolg. Zo zie je meteen dat verharding, hevige regen en overstromingsrisico niet los van elkaar staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt overstromingsgevaar in je gemeente. Welke elementen zet je in je schema? (meerdere antwoorden mogelijk)",
        opties=[
            "De hoeveelheid verharde oppervlakte",
            "De ligging ten opzichte van de rivier",
            "Het hoogteverschil in het gebied",
            "Het aantal scholen in de gemeente",
            "De leeftijd van de burgemeester",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verharding, ligging en reliëf sturen alle drie waar het water naartoe gaat. Scholen tellen pas mee als je naar de gevolgen kijkt, niet naar de oorzaken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoek is pas geslaagd als je hypothese juist blijkt te zijn.",
        antwoord=False,
        uitleg="Een hypothese die onderuit gaat, leert je even veel. Wat een onderzoek doet slagen, is dat je vraag scherp is en je besluit steunt op wat je echt gemeten hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je bij veranderend landgebruik kaarten of luchtfoto's uit verschillende jaren?",
        opties=[
            "Alleen zo zie je wat er in de tijd veranderd is",
            "Oude kaarten zijn altijd nauwkeuriger dan nieuwe",
            "Nieuwe kaarten tonen altijd meer detail dan oude",
            "Zo kan je de schaal van beide kaarten controleren",
        ],
        antwoord=0,
        uitleg="Eén beeld toont een toestand, twee beelden tonen een proces. Let er wel op dat je beelden uit hetzelfde seizoen en op dezelfde schaal naast elkaar legt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet de geluidshinder langs een drukke weg. Wat hoort bij goed bronnengebruik?",
        opties=[
            "Noteren wanneer en waar je gemeten hebt",
            "Enkel meten op het drukste moment van de dag",
            "De metingen afronden tot een mooi rond getal",
            "Enkel de metingen bewaren die je verwachtte",
        ],
        antwoord=0,
        uitleg="Zonder tijdstip en plaats is een meting waardeloos: op zondagochtend meet je iets heel anders dan op een schooldag om acht uur. Metingen wegselecteren is bovendien vervalsen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het in kaart brengen van wat je op het terrein zelf waarneemt?",
        antwoord=["terreinkartering", "de terreinkartering", "karteren"],
        uitleg="Terreinkartering maakt van je waarneming een kaart. Daarna kan je ze naast een bestaande kaartlaag leggen en zien waar beide verschillen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een besluit mag ook zeggen dat er te weinig gegevens waren om de vraag te beantwoorden.",
        antwoord=True,
        uitleg="Eerlijk zijn over wat je niet weet, hoort bij onderzoek. De fiche vraagt trouwens uitdrukkelijk om ook de beperkingen van je bronnen te benoemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt waterschaarste in je streek. Welke bron gebruik je voor de neerslag van de voorbije dertig jaar?",
        opties=[
            "Een lange meetreeks van een weerstation in de buurt",
            "De weersvoorspelling voor de komende zeven dagen",
            "Een luchtfoto van de streek uit het voorbije jaar",
            "Een politieke kaart met de gemeentegrenzen erop",
        ],
        antwoord=0,
        uitleg="Klimaat is het gemiddelde over dertig jaar, dus heb je een lange reeks nodig. Een voorspelling voor volgende week zegt daar niets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk om bij elke bron het jaartal te noteren?",
        opties=[
            "Een verouderde kaart kan de toestand van nu verkeerd tonen",
            "Zonder jaartal werkt de legende van de kaart niet",
            "Oude bronnen mogen nooit gebruikt worden",
            "Het jaartal bepaalt de schaal van de kaart",
        ],
        antwoord=0,
        uitleg="Een bedrijventerrein uit 2015 kan intussen verdubbeld zijn. Oude bronnen zijn wel degelijk bruikbaar, juist om verandering te tonen, maar dan moet je weten van wanneer ze zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een onderzoek naar mobiliteit kunnen lawaai en luchtkwaliteit ook een rol spelen.",
        antwoord=True,
        uitleg="De fiche noemt ze zelf: files, geluidsoverlast en luchtvervuiling horen bij hetzelfde thema. Ze zijn gevolgen van dezelfde verkeersstromen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is Geopunt?",
        opties=[
            "De digitale kaart van de Vlaamse overheid",
            "Een navigatie-app voor in de auto",
            "Een wereldatlas op papier van een uitgeverij",
            "Een weerstation dat de neerslag meet",
        ],
        antwoord=0,
        uitleg="Geopunt bundelt honderden kaartlagen over Vlaanderen: bodem, water, wegen, bebouwing, erfgoed en nog veel meer. Je mag het tijdens het examen gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je de zoekbalk in Geopunt?",
        opties=[
            "Om een adres of coördinaten op de kaart te vinden",
            "Om de legende van de kaartlaag te openen",
            "Om een afstand op de kaart op te meten",
            "Om een kaartlaag transparant te maken",
        ],
        antwoord=0,
        uitleg="De zoekbalk brengt je naar de plaats. Wat je daar vervolgens te zien krijgt, kies je met het lagenpaneel.",
    ),
    dict(
        type="waarofniet",
        vraag="In Geopunt kan je maar één kaartlaag tegelijk zichtbaar maken.",
        antwoord=False,
        uitleg="Je kan er verschillende over elkaar leggen, en dat is net de bedoeling: een thematische laag boven een luchtfoto toont je meteen wat er op die plek staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten hoeveel hectare een bedrijventerrein beslaat. Wat gebruik je?",
        opties=[
            "Het meetgereedschap van Geopunt",
            "De zoekbalk bovenaan de kaart",
            "De legende in het linkerpaneel",
            "De knop om een laag transparant te maken",
        ],
        antwoord=0,
        uitleg="Met het meetgereedschap teken je een lijn of een vlak en lees je de lengte of de oppervlakte af. Dat is precies wat de fiche van je vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je allemaal met het meetgereedschap van Geopunt? (meerdere antwoorden mogelijk)",
        opties=[
            "De afstand tussen twee punten meten",
            "De oppervlakte van een gebied meten",
            "De lengte van een weg of rivier volgen",
            "De hoogte van een gebouw rechtstreeks aflezen",
            "De bevolkingsdichtheid van de gemeente berekenen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Afstanden en oppervlakten meet je rechtstreeks. Hoogte lees je af via een hoogtelaag en haar legende, en dichtheid moet je zelf berekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="In Geopunt lees je de hoogte van een plaats af met het meetgereedschap.",
        antwoord=False,
        uitleg="Het meetgereedschap is voor afstanden en oppervlakten. Voor de hoogte zet je de hoogtelaag aan en lees je in de legende of in het linkerpaneel welke kleur bij welke hoogte hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou je een kaartlaag transparant maken?",
        opties=[
            "Om twee lagen tegelijk te kunnen vergelijken",
            "Om de kaart sneller te laten openen",
            "Om de legende van de laag te verbergen",
            "Om de schaal van de kaart te vergroten",
        ],
        antwoord=0,
        uitleg="Leg een thematische laag half doorzichtig over een luchtfoto en je ziet meteen wat er in werkelijkheid op die plek staat. Dat is een van de sterkste trucs van een digitale kaart.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het overzicht dat uitlegt welke kleur of welk symbool op een kaart wat betekent?",
        antwoord=["legende", "de legende"],
        uitleg="Zonder legende is een gekleurde kaart een gekleurd vlak. Elke kaartlaag in Geopunt heeft er een, en die openen is altijd je eerste stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt de laag met overstromingsgevoelige gebieden over een luchtfoto van je wijk. Wat onderzoek je?",
        opties=[
            "Welke gebouwen in een risicogebied staan",
            "Hoeveel mensen er in je wijk wonen",
            "Hoe oud de gebouwen in je wijk zijn",
            "Welke talen er in je wijk gesproken worden",
        ],
        antwoord=0,
        uitleg="Twee lagen over elkaar leggen koppelt een risico aan wat er echt staat. Voor het aantal inwoners of de ouderdom van de gebouwen heb je andere lagen of bronnen nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat je op een digitale kaart ziet, hangt volledig af van welke lagen je hebt aangezet.",
        antwoord=True,
        uitleg="Dat is meteen de belangrijkste beperking. Een laag die je niet kent of niet aanzet, bestaat voor jouw onderzoek niet, ook al is ze beschikbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beperkingen heeft een digitale kaart zoals Geopunt? (meerdere antwoorden mogelijk)",
        opties=[
            "Sommige lagen zijn ouder dan de toestand van vandaag",
            "Je ziet enkel wat er als laag beschikbaar is",
            "De klassen in de legende zijn door iemand gekozen",
            "Ze toont de coördinaten van een plaats verkeerd",
            "Ze verandert de werkelijke afstanden op het terrein",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ouderdom, beschikbaarheid en de keuze van de klassen zijn echte beperkingen. De coördinaten en de afstanden kloppen wel degelijk; daar is zo'n kaart net voor gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche om uit te leggen hoe de digitale kaart je geholpen heeft én wat haar beperkingen waren?",
        opties=[
            "Een bron kritisch bekijken hoort bij het onderzoek zelf",
            "De kaart moet daarna gecorrigeerd worden door de overheid",
            "Zo weet de verbetering hoelang je gewerkt hebt",
            "Zonder die uitleg werkt de kaartlaag niet meer",
        ],
        antwoord=0,
        uitleg="Wie zegt wat zijn bron niet kan tonen, laat zien dat hij ze begrijpt. Dat is het verschil tussen een kaart aflezen en met een kaart onderzoeken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een luchtfoto in Geopunt toont altijd de toestand van vandaag.",
        antwoord=False,
        uitleg="Luchtfoto's worden om de zoveel jaar genomen. Je kan er meestal oudere reeksen naast leggen, en juist dat maakt ze bruikbaar om verandering te tonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of de open ruimte in je gemeente is afgenomen. Welke aanpak past het best?",
        opties=[
            "Twee luchtfotolagen van verschillende jaren vergelijken",
            "De zoekbalk gebruiken om het gemeentehuis te vinden",
            "De afstand tot de dichtstbijzijnde stad opmeten",
            "De hoogte van het hoogste punt van de gemeente aflezen",
        ],
        antwoord=0,
        uitleg="Verandering meet je door twee momenten naast elkaar te leggen. Daarna kan je met het meetgereedschap ook uitrekenen hoeveel hectare er precies bij kwam.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het gereedschap in Geopunt waarmee je afstanden en oppervlakten bepaalt?",
        antwoord=["meetgereedschap", "het meetgereedschap", "meetinstrument"],
        uitleg="Met het meetgereedschap teken je een lijn of een veelhoek op de kaart en lees je de lengte of de oppervlakte af. Het staat uitdrukkelijk in de vakfiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag Geopunt tijdens het examen aardrijkskunde gebruiken.",
        antwoord=True,
        uitleg="De links naar Geopunt, een rekenmachine, een woordenboek en de spellingcontrole zitten in het examen zelf. Daarom raadt de examencommissie aan er thuis mee te oefenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je besluit dat de files in je gemeente toenemen. Waarop moet dat besluit steunen?",
        opties=[
            "Op de gegevens en metingen die je verzameld hebt",
            "Op wat de meeste mensen in je gemeente denken",
            "Op je verwachting die je vooraf had opgeschreven",
            "Op het aantal kaartlagen dat je hebt aangezet",
        ],
        antwoord=0,
        uitleg="Je besluit hoort bij je gegevens, niet bij je hypothese. Komt het daarmee in botsing, dan schrijf je dat op in plaats van je gegevens bij te sturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een geografisch onderzoek? (meerdere antwoorden mogelijk)",
        opties=[
            "Een vraag of hypothese opstellen",
            "Bronnen kiezen en gegevens verzamelen",
            "Besluiten en de beperkingen benoemen",
            "Het besluit als eerste stap opschrijven",
            "De bronnen kiezen die je gelijk geven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vraag, bronnen, analyse, besluit en bronkritiek: in die volgorde. Beginnen bij het besluit of enkel de passende bronnen kiezen, is geen onderzoek meer.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk onderdeel van de vakfiche kan in het onderzoeksdeel van het examen terugkomen.",
        antwoord=True,
        uitleg="Dat staat er letterlijk: alle te kennen inhoud kan in dit deel verwerkt zijn. Onderzoek is dus geen apart stukje leerstof maar de manier waarop de rest getoetst wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je bij je onderzoek ook welke laag je niet gevonden hebt?",
        opties=[
            "Zo weet de lezer wat je besluit niet kan dekken",
            "Zo krijg je meer punten voor de lengte van je werk",
            "Zo hoef je geen besluit meer te schrijven",
            "Zo wordt de kaartlaag alsnog voor je gemaakt",
        ],
        antwoord=0,
        uitleg="Een gat in je gegevens is zelf een resultaat. Door het te benoemen, geef je aan hoe ver je besluit reikt en waar het ophoudt.",
    ),
]
