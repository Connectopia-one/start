# -*- coding: utf-8 -*-
"""De vragen voor "De mens verandert het landschap" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "veranderingen in het landschap",
onderdeel "veranderingen door menselijke ingrepen" (deel van de 40 %, samen met
[[ak_aardkorst]], [[ak_weer]] en [[ak_klimaat]]).

Deel 1 gaat over de zes manieren waarop de mens het landschap uitbouwt:
energie-infrastructuur, transportinfrastructuur, bebouwing voor bewoning,
landbouw, industrie met productie, mijnbouw en groeves, en toeristische
voorzieningen.
Deel 2 gaat over de zeven ingrepen die de fiche opsomt: ontbossing, het
vergroten van landbouwpercelen, verharding, irrigatie, ontharding,
stadslandbouw en de ontginning van hulpbronnen, en over hun gevolgen voor de
mens, voor het landschap en voor de vijf P's.

Beide lijstjes komen woordelijk uit de fiche en worden hier woordelijk gebruikt.
Let er bij het bijschrijven op dat verharding en ontharding elkaars
tegenovergestelde zijn en allebei in de lijst staan: de fiche noemt ontharding
uitdrukkelijk als ingreep, niet enkel als oplossing.

De vragen oordelen niet over de mensen die deze keuzes maken. Ze beschrijven wat
er gebeurt en welke gevolgen dat heeft, ook de gunstige.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Op een luchtfoto van vijftig jaar geleden staan velden, op de foto van vandaag staan er huizen en een rondweg. Wat is er gebeurd?",
        opties=[
            "De mens heeft het landschap veranderd",
            "Het klimaat van de streek is veranderd",
            "Het reliëf van de streek is gestegen",
            "De bodemsoort ter plaatse is veranderd",
        ],
        antwoord=0,
        uitleg="Op enkele tientallen jaren tijd verandert de menselijke laag van een landschap grondig, terwijl reliëf, bodem en klimaat vrijwel hetzelfde blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de energie-infrastructuur? Er zijn er meerdere juist.",
        opties=[
            "Een windmolenpark",
            "Een hoogspanningslijn",
            "Een elektriciteitscentrale",
            "Een treinstation in de stad",
            "Een grote woonwijk aan de rand",
        ],
        antwoord=[0, 1, 2],
        uitleg="Energie-infrastructuur wekt energie op of vervoert ze: centrales, windparken, zonneparken, leidingen en hoogspanningslijnen. Een station hoort bij het transport.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan windmolens vaak aan de kust of op open vlakten?",
        opties=[
            "Omdat het daar harder en gelijkmatiger waait",
            "Omdat de bodem daar het stevigst is",
            "Omdat er daar geen vergunning voor nodig is",
            "Omdat de stroom daar het dichtst bij de klant is",
        ],
        antwoord=0,
        uitleg="Een windmolen levert het meest waar de wind sterk en weinig gestoord is. Achter bossen en gebouwen valt de wind stil en draait hij ongelijkmatig.",
    ),
    dict(
        type="invultekst",
        vraag="De masten en kabels die stroom over lange afstanden vervoeren, vormen samen het hoogspannings___.",
        antwoord="hoogspanningsnet",
        uitleg="Het hoogspanningsnet doorsnijdt het landschap over tientallen kilometers. Waar het door bos loopt, blijft er een brede open strook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ingrepen horen bij de transportinfrastructuur? Er zijn er meerdere juist.",
        opties=[
            "Een autosnelweg aanleggen",
            "Een kanaal graven",
            "Een spoorlijn verdubbelen",
            "Een zonnepark bouwen",
            "Een camping aanleggen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Transportinfrastructuur verplaatst mensen en goederen: wegen, spoorwegen, kanalen, havens en luchthavens. Een zonnepark levert energie en een camping dient voor recreatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een autosnelweg door een natuurgebied snijdt het leefgebied van dieren in stukken.",
        antwoord=True,
        uitleg="Dat heet versnippering. Dieren raken niet meer aan de overkant, en daarom bouwt men ecoducten en tunnels om de stukken weer te verbinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een verkaveling?",
        opties=[
            "Een stuk grond dat in bouwpercelen verdeeld wordt",
            "Een stuk grond dat aan de natuur teruggegeven wordt",
            "Een stuk landbouwgrond dat in twee gesplitst wordt",
            "Een stuk bos dat voor houtkap aangeduid wordt",
        ],
        antwoord=0,
        uitleg="Bij een verkaveling wordt open ruimte opgedeeld in loten met wegen, riolering en nutsleidingen erbij. Wat er daarna staat, is bebouwing voor bewoning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neemt de oppervlakte bebouwing in België toe terwijl de bevolking maar traag groeit?",
        opties=[
            "Omdat er steeds meer en kleinere gezinnen zijn",
            "Omdat er elk jaar huizen bij de zee bijkomen",
            "Omdat huizen tegenwoordig sneller instorten",
            "Omdat de gemeenten groter geworden zijn",
        ],
        antwoord=0,
        uitleg="Meer alleenwonenden en kleinere gezinnen betekent meer woningen voor evenveel mensen. Elke woning neemt grond in, en met lintbebouwing loopt dat snel op.",
    ),
    dict(
        type="waarofniet",
        vraag="Landbouw verandert het landschap niet, want landbouw hoort bij de natuur.",
        antwoord=False,
        uitleg="Landbouw is een menselijke ingreep. Akkers, weiden, boomgaarden, serres en drainage zijn allemaal aangelegd; zonder de boer zou er bos staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is mijnbouw?",
        opties=[
            "Delfstoffen uit de diepere ondergrond halen",
            "Bouwen op een terrein dat vroeger een mijn was",
            "Grond afgraven om er een vijver van te maken",
            "Een berg afvlakken om er te kunnen bouwen",
        ],
        antwoord=0,
        uitleg="Bij mijnbouw wordt er ondergronds gegraven naar steenkool, erts of zout. In Limburg en in de Borinage lagen steenkoolmijnen, en de terrils herinneren daar nog aan.",
    ),
    dict(
        type="invultekst",
        vraag="De kunstmatige heuvel van afvalgesteente naast een oude steenkoolmijn heet een ___.",
        antwoord="terril",
        uitleg="Een terril bestaat uit steen die met de kolen mee naar boven kwam. Veel terrils zijn intussen begroeid en dienen als wandelgebied of natuurreservaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verandert een groeve het landschap?",
        opties=[
            "Er ontstaat een diepe put waar eerst grond lag",
            "Er ontstaat een heuvel waar eerst een vlakte lag",
            "Er ontstaat een bos waar eerst een akker lag",
            "Er ontstaat een rivier waar eerst een beek liep",
        ],
        antwoord=0,
        uitleg="In een groeve wordt steen, zand of grind weggehaald. Na de ontginning blijft er een put over, die vaak vol water loopt en dan een plas wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toeristische voorzieningen veranderen een landschap? Er zijn er meerdere juist.",
        opties=[
            "Appartementsgebouwen op de zeedijk",
            "Skiliften op een berghelling",
            "Een pretpark met parkings errond",
            "Een wandelpad door een bestaand bos",
            "Een bank om uit te rusten langs de weg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Grote voorzieningen nemen ruimte in en zijn van ver zichtbaar. Een wandelpad of een bank verandert het landschap nauwelijks.",
    ),
    dict(
        type="waarofniet",
        vraag="Aan de Belgische kust staat bijna de hele zeedijk vol met hoogbouw.",
        antwoord=True,
        uitleg="Sinds de vorige eeuw is de kustlijn grotendeels volgebouwd met appartementen. Het uitzicht van die kust is daardoor bijna volledig door de mens bepaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een van de gevolgen van een nieuwe luchthaven voor de omwonenden?",
        opties=[
            "Geluidshinder van opstijgende vliegtuigen",
            "Een lagere temperatuur in de hele streek",
            "Minder verkeer op de wegen eromheen",
            "Een vruchtbaardere bodem in de buurt",
        ],
        antwoord=0,
        uitleg="Een luchthaven brengt werk en verbindingen, maar ook lawaai, uitstoot en extra wegverkeer. Daarom liggen er strenge regels op de vluchturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen industriegebieden vaak langs een kanaal?",
        opties=[
            "Omdat zware goederen over water goedkoop vervoerd worden",
            "Omdat er langs het water goedkopere grond ligt",
            "Omdat fabrieken daar altijd veel koelwater kunnen oppompen",
            "Omdat er langs het water minder regels gelden",
        ],
        antwoord=0,
        uitleg="Eén binnenschip vervangt tientallen vrachtwagens. Voor grondstoffen als zand, graan en brandstof is water daarom het voordeligste vervoer.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke menselijke ingreep in het landschap heeft enkel nadelen.",
        antwoord=False,
        uitleg="Een spoorlijn, een dijk of een waterzuivering brengt duidelijke voordelen. Het gaat erom de voordelen en de nadelen samen te bekijken, ook op de lange termijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente legt een bedrijventerrein aan op een oud landbouwgebied. Welke lagen van het landschap veranderen daardoor?",
        opties=[
            "Het landgebruik en de bebouwing",
            "Het reliëf en de ondergrond",
            "Het klimaat en de natuurlijke vegetatie",
            "De bodemtextuur en de hoogteligging",
        ],
        antwoord=0,
        uitleg="Wat verandert, is wat de mens met de grond doet. Het reliëf en de ondergrond blijven, ook al wordt het oppervlak geëffend en verhard.",
    ),
    dict(
        type="invultekst",
        vraag="Het aanleggen van wegen, spoorlijnen, kanalen en leidingen noemt men samen het uitbouwen van ___.",
        antwoord="infrastructuur",
        uitleg="Infrastructuur is alles wat aangelegd wordt om vervoer, energie en nutsvoorzieningen mogelijk te maken. Ze tekent zich als lijnen in het landschap af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen de oudste dorpskernen van Vlaanderen vaak op een lichte hoogte?",
        opties=[
            "Omdat het daar droger was dan in de vallei",
            "Omdat men er verder kon kijken over het land",
            "Omdat de bodem er uit klei bestond",
            "Omdat men er dichter bij de akkers woonde",
        ],
        antwoord=0,
        uitleg="Wie op een hoogte bouwde, hield droge voeten bij hoog water. De natte valleigrond diende als hooiland en weide, niet om op te wonen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In een streek verdwijnt jaar na jaar een stuk bos voor akkers en wegen. Hoe heet dat?",
        opties=[
            "Ontbossing",
            "Ontharding",
            "Irrigatie",
            "Sedimentatie",
        ],
        antwoord=0,
        uitleg="Ontbossing is het verdwijnen van bos, meestal om er landbouwgrond, weiden, mijnen of bebouwing van te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen heeft ontbossing op een helling? Er zijn er meerdere juist.",
        opties=[
            "De bodem spoelt sneller weg",
            "Er wordt minder koolstofdioxide opgenomen",
            "Dieren verliezen hun leefgebied",
            "De hoogte van de helling neemt toe",
            "De ondergrond verandert van gesteente",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zonder wortels en bladerdak heeft de regen vrij spel op de grond, verdwijnt een koolstofput en verliezen soorten hun woonplaats. Het reliëf en de ondergrond blijven wat ze zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden landbouwpercelen steeds groter gemaakt?",
        opties=[
            "Omdat grote machines er efficiënter kunnen werken",
            "Omdat de grond in het midden vruchtbaarder is",
            "Omdat er dan minder regenwater verloren gaat",
            "Omdat de wet kleine percelen verbiedt",
        ],
        antwoord=0,
        uitleg="Een grote tractor verliest tijd bij elke draai. Daarom verdwenen hagen, bomenrijen en holle wegen tussen de percelen, en werd het landschap veel opener.",
    ),
    dict(
        type="waarofniet",
        vraag="Door percelen samen te voegen verdwijnen ook de hagen en houtkanten ertussen.",
        antwoord=True,
        uitleg="Die randen waren nochtans belangrijk: ze hielden de wind tegen, boden schuilplaats aan vogels en insecten, en remden het afspoelen van de grond.",
    ),
    dict(
        type="invultekst",
        vraag="Het bedekken van grond met beton, asfalt of tegels noemt men ___.",
        antwoord="verharding",
        uitleg="Verharde grond laat geen water door. Daardoor zakt het grondwater, stijgt de kans op wateroverlast en warmt het oppervlak sterker op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is ontharding?",
        opties=[
            "Beton of tegels weghalen zodat de grond weer open ligt",
            "Een bodem losmaken zodat de gewassen er beter in wortelen",
            "Een weg van een zachtere asfaltsoort voorzien",
            "Een dijk verlagen zodat er water over kan lopen",
        ],
        antwoord=0,
        uitleg="Ontharding is het omgekeerde van verharding: verharde oppervlakken opbreken en er grond of groen van maken, zodat het water kan insijpelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is irrigatie?",
        opties=[
            "Land kunstmatig van water voorzien",
            "Overtollig water van het land afvoeren",
            "Regenwater opvangen in een put",
            "Een rivier rechttrekken voor de scheepvaart",
        ],
        antwoord=0,
        uitleg="Bij irrigatie wordt water naar de akkers gebracht met kanalen, buizen of sproeiers. Zo kan er geteeld worden waar er van nature te weinig regen valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nadelen kan irrigatie hebben? Er zijn er meerdere juist.",
        opties=[
            "De rivier of het grondwater raakt uitgeput",
            "De bodem kan verzilten",
            "Verderop blijft er minder water over",
            "Het reliëf van de streek wordt steiler",
            "De ondergrond verandert van gesteente",
        ],
        antwoord=[0, 1, 2],
        uitleg="Water dat naar de akker gaat, komt niet meer in de rivier terecht. Verdampt het op het veld, dan blijft het zout achter, en dat maakt de grond op den duur onbruikbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is stadslandbouw?",
        opties=[
            "Voedsel telen in of vlak bij de stad",
            "Landbouwgrond verkopen voor woningbouw",
            "Vee houden in een stal midden in een dorp",
            "Groenten verkopen op de markt van de stad",
        ],
        antwoord=0,
        uitleg="Stadslandbouw gebeurt op daken, in volkstuinen en op braakliggende percelen. Het voedsel moet nauwelijks vervoerd worden en het brengt groen in de stad.",
    ),
    dict(
        type="waarofniet",
        vraag="Stadslandbouw kan een stad koeler maken tijdens een hittegolf.",
        antwoord=True,
        uitleg="Planten verdampen water en geven schaduw, en een daktuin houdt de warmte uit het gebouw. Elk stuk groen dat verharding vervangt, helpt tegen hitte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de ontginning van hulpbronnen?",
        opties=[
            "Grondstoffen uit de aarde halen om te gebruiken",
            "Nieuwe grondstoffen in een fabriek maken",
            "Afgedankte materialen opnieuw gebruiken",
            "Grondstoffen naar een ander land vervoeren",
        ],
        antwoord=0,
        uitleg="Hulpbronnen zijn zand, grind, steen, erts, steenkool, olie en gas. Ze uit de aarde halen laat altijd een spoor na in het landschap.",
    ),
    dict(
        type="invultekst",
        vraag="Het omzetten van landbouwgebied in bebouwing is een vorm van ___.",
        antwoord="verharding",
        uitleg="De fiche noemt dat uitdrukkelijk als voorbeeld. Waar eerst regen in de grond zakte, ligt daarna een dak, een oprit en een straat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente breekt een betonnen schoolplein op en legt er gras en bomen aan. Welke gevolgen heeft dat? Er zijn er meerdere juist.",
        opties=[
            "Regenwater kan weer in de grond zakken",
            "Het is er op warme dagen koeler",
            "Er is meer plaats voor planten en dieren",
            "De school krijgt er een verdieping bij",
            "De straat ernaast wordt breder",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ontharden helpt tegen wateroverlast, tegen hitte en voor de biodiversiteit tegelijk. Aan het gebouw of aan de straat verandert er niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Menselijke ingrepen in België hebben geen gevolgen buiten onze grenzen.",
        antwoord=False,
        uitleg="Water stroomt door naar het buitenland, uitstoot verspreidt zich over de dampkring, en wat wij invoeren wordt elders ontgonnen of gekweekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf legt op zijn terrein een wadi aan, een ondiepe kom waar regenwater in kan zakken. Onder welke P van het 5P-model valt dat vooral?",
        opties=[
            "Planet",
            "People",
            "Prosperity",
            "Peace",
        ],
        antwoord=0,
        uitleg="Een wadi houdt water in het gebied, vult het grondwater aan en beschermt de beek verderop. Dat is in de eerste plaats winst voor de aarde zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe fabriek geeft werk aan driehonderd mensen maar vervuilt de beek ernaast. Wat is de juiste conclusie?",
        opties=[
            "Ze doet Prosperity vooruitgaan en Planet achteruit",
            "Ze doet Planet vooruitgaan en Prosperity achteruit",
            "Ze heeft geen enkel gevolg voor de vijf P's",
            "Ze doet alle vijf de P's tegelijk vooruitgaan",
        ],
        antwoord=0,
        uitleg="Zo werkt het model: een ingreep kan één P dienen en een andere schaden. Duurzaam handelen betekent zoeken naar een oplossing die er zo weinig mogelijk schaadt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft ontbossing in het Amazonegebied gevolgen voor de hele wereld?",
        opties=[
            "Omdat dat bos veel koolstofdioxide opneemt",
            "Omdat dat bos de zeespiegel laag houdt",
            "Omdat dat bos de wind over de oceaan tegenhoudt",
            "Omdat dat bos de bodem van Europa vruchtbaar maakt",
        ],
        antwoord=0,
        uitleg="Een regenwoud is een reusachtige koolstofput en een enorme waterpomp. Verdwijnt het, dan gaat die opname weg én komt de opgeslagen koolstof vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een landschap dat door de mens veranderd is, kan nooit meer hersteld worden.",
        antwoord=False,
        uitleg="Soms lukt herstel wel degelijk: een rechtgetrokken beek mag weer kronkelen, een terril raakt begroeid, een groeve wordt een natuurgebied. Helemaal terug naar vroeger gaat meestal niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen verharding en ontharding?",
        opties=[
            "Verharding sluit de bodem af, ontharding opent hem weer",
            "Verharding gebeurt op het land, ontharding in het water",
            "Verharding is tijdelijk, ontharding is blijvend",
            "Verharding gebeurt op het platteland, ontharding in de stad",
        ],
        antwoord=0,
        uitleg="Het zijn elkaars tegengestelde. Beton en asfalt maken de bodem ondoorlaatbaar; ze weghalen laat water en lucht er weer in.",
    ),
    dict(
        type="invultekst",
        vraag="Het verdwijnen van bos, meestal om er landbouwgrond of bebouwing van te maken, heet ___.",
        antwoord="ontbossing",
        uitleg="Wereldwijd verdwijnt er elk jaar bos, vooral in de tropen. Op andere plaatsen komt er bos bij, maar jong bos vervangt een oud bos niet zomaar.",
    ),
]
