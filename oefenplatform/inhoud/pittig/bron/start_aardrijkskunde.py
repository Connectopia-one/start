# -*- coding: utf-8 -*-
"""Pittige hoofdstukken aardrijkskunde 🌱 Start.

Geen nieuwe leerstof: alles staat op wat in het gewone hoofdstuk al aan bod
komt. Moeilijker wordt het door met de schaal te rekenen, een kaart te lezen in
plaats van ze te benoemen, en te verklaren waaróm een landschap of een klimaat
zo is.
"""
NIVEAU = "start"
VAK = "Aardrijkskunde"
BESTAND = "start-aardrijkskunde-pittig.json"

KAARTLEZEN = [
    {
        "type": "invultekst",
        "vraag": "Een kaart heeft schaal 1 op 25 000. Twee dorpen liggen er 8 cm uit elkaar. Hoeveel kilometer is dat in het echt?",
        "antwoord": "2",
        "reken": "8 * 25000 / 100000",
        "uitleg": "8 cm op de kaart is 8 × 25 000 = 200 000 cm in het echt. Eén kilometer is 100 000 cm, dus dat zijn 2 km.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke schaal toont het meeste detail van een klein gebied?",
        "opties": ["1 op 10 000", "1 op 100 000", "1 op 1 000 000", "1 op 500 000"],
        "antwoord": 0,
        "uitleg": "Hoe kleiner het getal achter de schaal, hoe minder er is samengeknepen en hoe meer je ziet. Bij 1 op 10 000 is 1 cm maar 100 m.",
    },
    {
        "type": "waarofniet",
        "vraag": "Hoe groter het getal achter de schaal, hoe gedetailleerder de kaart.",
        "antwoord": False,
        "uitleg": "Niet waar, net omgekeerd. Bij 1 op 1 000 000 past een heel land op één blad, maar zie je geen straten meer.",
    },
    {
        "type": "invultekst",
        "vraag": "Je loopt naar het oosten en draait dan een kwartslag naar rechts. Naar welke windstreek loop je nu?",
        "antwoord": "het zuiden",
        "uitleg": "Vanuit het oosten ga je met een kwartslag rechtsom naar het zuiden. Linksom was je bij het noorden uitgekomen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op een reliëfkaart is een gebied donkerbruin gekleurd. Wat weet je dan?",
        "opties": ["het ligt hoog", "er groeit veel bos", "er is veel water", "het is er warm"],
        "antwoord": 0,
        "uitleg": "Op een reliëfkaart staat de kleur voor de hoogte: groen laag, geel en lichtbruin hoger, donkerbruin het hoogst. Over bos of water zegt ze niets.",
    },
    {
        "type": "waarofniet",
        "vraag": "De evenaar verdeelt de aarde in een oostelijk en een westelijk halfrond.",
        "antwoord": False,
        "uitleg": "Niet waar, in een noordelijk en een zuidelijk halfrond. Oost en west worden gescheiden door de nulmeridiaan.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel graden zit er tussen het noorden en het oosten op een kompas?",
        "antwoord": "90",
        "reken": "360 / 4",
        "uitleg": "De vier hoofdwindstreken verdelen de 360° van de kompasroos in vier gelijke stukken: 360 : 4 = 90°. Noordoost ligt er precies tussen, op 45°.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarvoor dienen hoogtelijnen op een kaart?",
        "opties": [
            "ze verbinden punten die even hoog liggen",
            "ze tonen waar de wegen lopen",
            "ze geven de grenzen aan",
            "ze wijzen naar het noorden",
        ],
        "antwoord": 0,
        "uitleg": "Elke hoogtelijn loopt langs alle punten op dezelfde hoogte. Door hun patroon zie je op een vlakke kaart toch hoe het landschap golft.",
    },
    {
        "type": "waarofniet",
        "vraag": "Liggen de hoogtelijnen dicht bij elkaar, dan is de helling steil.",
        "antwoord": True,
        "uitleg": "Klopt. Dicht bij elkaar betekent: over een korte afstand veel hoogteverschil. Ver uit elkaar is een zacht glooiend of vlak stuk.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe noem je de denkbeeldige lijnen die evenwijdig met de evenaar lopen?",
        "opties": ["breedtecirkels", "meridianen", "hoogtelijnen", "tijdzones"],
        "antwoord": 0,
        "uitleg": "Breedtecirkels lopen horizontaal, evenwijdig met de evenaar. Meridianen lopen verticaal, van pool tot pool.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een gps werkt met satellieten en heeft geen kompasnaald nodig.",
        "antwoord": True,
        "uitleg": "Klopt. Een gps bepaalt je plaats door de afstand tot meerdere satellieten te meten. Een kompas werkt met het magnetisch veld van de aarde en heeft niets nodig van buitenaf.",
    },
    {
        "type": "invultekst",
        "vraag": "Op een kaart met schaal 1 op 50 000 is een weg 6 cm lang. Hoeveel kilometer is die weg in het echt?",
        "antwoord": "3",
        "reken": "6 * 50000 / 100000",
        "uitleg": "6 × 50 000 = 300 000 cm, en dat is 3 km.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je reist van Oostende naar Hasselt. In welke richting ga je ongeveer?",
        "opties": ["naar het oosten", "naar het westen", "naar het zuiden", "naar het noorden"],
        "antwoord": 0,
        "uitleg": "Oostende ligt aan de kust, helemaal in het westen; Hasselt ligt in Limburg, in het oosten. Je doorkruist dus het land van west naar oost.",
    },
    {
        "type": "waarofniet",
        "vraag": "De nulmeridiaan loopt door Greenwich, bij Londen.",
        "antwoord": True,
        "uitleg": "Klopt. Daar is ooit afgesproken dat de telling van de lengtegraden begint. Vandaar ook dat de wereldtijd naar die plek genoemd is.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel windstreken telt een kompasroos als je noordoost, zuidoost, zuidwest en noordwest meetelt?",
        "antwoord": "8",
        "reken": "4 + 4",
        "uitleg": "Vier hoofdwindstreken plus vier tussenwindstreken: samen acht, telkens 45° uit elkaar.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het verschil tussen een plattegrond en een landkaart?",
        "opties": [
            "een plattegrond toont een klein gebied van bovenaf, heel gedetailleerd",
            "een plattegrond toont het gebied van opzij, zoals een foto",
            "een landkaart is altijd kleiner van formaat",
            "een plattegrond heeft nooit een legende",
        ],
        "antwoord": 0,
        "uitleg": "Allebei kijken ze van bovenaf. Het verschil zit in de schaal: een plattegrond toont één stad of gebouw met de straten erop, een landkaart een hele streek of een land.",
    },
    {
        "type": "waarofniet",
        "vraag": "Blauw op een landkaart staat meestal voor bergen.",
        "antwoord": False,
        "uitleg": "Niet waar, blauw is water: zeeën, meren en rivieren. Bergen zijn bruin, hoe donkerder hoe hoger.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom staat er bij elke kaart een legende?",
        "opties": [
            "omdat elke kaart haar eigen tekens en kleuren gebruikt",
            "omdat kaarten anders niet mooi zouden ogen op papier",
            "omdat de schaal anders niet zou kloppen",
            "omdat dat nu eenmaal verplicht is",
        ],
        "antwoord": 0,
        "uitleg": "Er is geen wereldwijde afspraak over elk teken. Zonder legende weet je niet of een stippellijn een wandelpad, een grens of een spoorweg is.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een satellietbeeld en een kaart van hetzelfde gebied tonen precies hetzelfde.",
        "antwoord": False,
        "uitleg": "Niet waar. Een satellietbeeld toont alles wat er ligt, ook wat je niet zoekt. Een kaart is een keuze: de maker laat weg wat niet ter zake doet en zet er namen en tekens bij.",
    },
    {
        "type": "invultekst",
        "vraag": "Op een kaart is 1 cm gelijk aan 2 km. De schaal is dan 1 op hoeveel? Antwoord met een getal.",
        "antwoord": "200000",
        "reken": "2 * 100000",
        "uitleg": "2 km is 200 000 cm. Eén centimeter op de kaart staat dus voor 200 000 centimeter in het echt: schaal 1 op 200 000.",
    },
]

BELGIE = [
    {
        "type": "meerkeuze",
        "vraag": "Welke Vlaamse provincie grenst zowel aan Nederland als aan Wallonië?",
        "opties": ["Limburg", "Antwerpen", "Vlaams-Brabant", "West-Vlaanderen"],
        "antwoord": 0,
        "uitleg": "Limburg raakt in het noorden aan Nederlands Limburg en in het zuiden aan de provincie Luik. Antwerpen grenst wel aan Nederland maar niet aan Wallonië.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het Brussels Hoofdstedelijk Gewest is officieel tweetalig.",
        "antwoord": True,
        "uitleg": "Klopt: Nederlands en Frans zijn er allebei officieel. Daarom staan straatnaamborden en wegwijzers er in twee talen.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel provincies telt België in totaal?",
        "antwoord": "10",
        "reken": "5 + 5",
        "uitleg": "Vijf in Vlaanderen en vijf in Wallonië, samen tien. Brussel hoort bij geen enkele provincie.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is Antwerpen zo'n belangrijke havenstad, hoewel ze niet aan zee ligt?",
        "opties": [
            "de Schelde is er diep genoeg voor zeeschepen",
            "er loopt een kanaal naar de Noordzee",
            "de stad ligt eigenlijk aan de Maas",
            "de haven ligt in werkelijkheid in Zeebrugge",
        ],
        "antwoord": 0,
        "uitleg": "De Schelde is tot in Antwerpen bevaarbaar voor zeeschepen. Daardoor kan een schip tot diep in het land varen, vlak bij de fabrieken en de spoorwegen.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Maas stroomt door Antwerpen en de Schelde door Luik.",
        "antwoord": False,
        "uitleg": "Niet waar, het is omgekeerd: de Schelde stroomt door Antwerpen en de Maas door Luik.",
    },
    {
        "type": "invultekst",
        "vraag": "In welke provincie ligt de stad Brugge?",
        "antwoord": "West-Vlaanderen",
        "uitleg": "Brugge is meteen ook de hoofdplaats van West-Vlaanderen, de provincie die aan de kust ligt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom liggen de oude industriegebieden van Wallonië vooral langs de Samber en de Maas?",
        "opties": [
            "daar lag de steenkool, en het water zorgde voor vervoer",
            "daar is de grond het vruchtbaarst voor landbouw",
            "daar wonen sinds de middeleeuwen de meeste mensen",
            "daar is het klimaat een stuk zachter",
        ],
        "antwoord": 0,
        "uitleg": "Steenkool was de brandstof van de fabrieken, en over water kon je zware vracht goedkoop verplaatsen. Waar die twee samenkwamen, ontstond industrie.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het Vlaams Gewest is groter in oppervlakte dan het Waals Gewest.",
        "antwoord": False,
        "uitleg": "Niet waar. Wallonië is in oppervlakte het grootst, maar in Vlaanderen wonen meer mensen. Oppervlakte en bevolking zijn twee verschillende dingen.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke rivier stroomt door Gent en mondt uit in de Schelde?",
        "antwoord": "de Leie",
        "uitleg": "De Leie komt uit Frankrijk, loopt langs Kortrijk en vloeit in Gent samen met de Schelde. Vroeger week men er vlas in, vandaar de bijnaam Leiestreek.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De Ardennen liggen hoger dan de rest van België. Waaraan merk je dat het meest?",
        "opties": [
            "het is er kouder en het regent er meer",
            "er wonen veel meer mensen dan in Vlaanderen",
            "er groeit nergens bos",
            "er stromen geen rivieren",
        ],
        "antwoord": 0,
        "uitleg": "Hoe hoger, hoe koeler, en lucht die over de heuvels omhoog moet, laat zijn water vallen. Daarom sneeuwt het in de Ardennen vaker dan aan de kust.",
    },
    {
        "type": "waarofniet",
        "vraag": "Er wonen meer mensen in Vlaanderen dan in Wallonië.",
        "antwoord": True,
        "uitleg": "Klopt, ongeveer zes tegenover drieënhalf miljoen, en dat op een kleinere oppervlakte. Vlaanderen is dus veel dichter bevolkt.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de hoofdplaats van de provincie Vlaams-Brabant?",
        "antwoord": "Leuven",
        "uitleg": "Leuven is de hoofdplaats van Vlaams-Brabant. Brussel ligt wel middenin die provincie, maar hoort er bestuurlijk niet bij.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een polder, zoals je die aan de Belgische kust vindt?",
        "opties": [
            "laaggelegen land dat op de zee gewonnen is",
            "een duin met struiken erop",
            "een stuk bos vlak achter de duinen",
            "een beschutte haven voor vissersboten",
        ],
        "antwoord": 0,
        "uitleg": "Polders liggen laag, soms onder het zeeniveau, en worden droog gehouden met dijken en grachten. Het is vaak vruchtbare weidegrond.",
    },
    {
        "type": "waarofniet",
        "vraag": "De duinen aan onze kust beschermen het land tegen de zee.",
        "antwoord": True,
        "uitleg": "Klopt, ze zijn een natuurlijke dijk. Daarom mag je er niet zomaar doorheen lopen: het helmgras houdt het zand vast.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de hoofdplaats van de provincie West-Vlaanderen?",
        "antwoord": "Brugge",
        "uitleg": "Brugge is de hoofdplaats. Oostende is er wel de bekendste badstad, maar geen provinciehoofdplaats.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom heeft België drie gemeenschappen?",
        "opties": [
            "omdat er drie officiële talen zijn",
            "omdat er drie gewesten zijn",
            "omdat er drie grote steden zijn",
            "omdat er drie provincies zijn",
        ],
        "antwoord": 0,
        "uitleg": "De gemeenschappen volgen de taal: Nederlands, Frans en Duits. De gewesten volgen het gebied. Daarom vallen ze niet samen.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Kempen hebben een vruchtbare kleibodem.",
        "antwoord": False,
        "uitleg": "Niet waar, de Kempen hebben een arme zandbodem. Daarom bleven er lang heide en dennenbossen staan waar elders akkers lagen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom regent het in de Ardennen meer dan aan de kust?",
        "opties": [
            "de lucht moet er over de heuvels omhoog en koelt dan af",
            "de zee ligt er veel verder vandaan dan aan de kust",
            "er staan veel meer bomen",
            "het ligt er dichter bij Frankrijk",
        ],
        "antwoord": 0,
        "uitleg": "Lucht die stijgt, koelt af, en koude lucht kan minder vocht vasthouden. Dat vocht valt als regen of sneeuw, nog voor de lucht verder het land in trekt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke provincie is qua oppervlakte de grootste van België?",
        "opties": ["Luxemburg", "Limburg", "Antwerpen", "Henegouwen"],
        "antwoord": 0,
        "uitleg": "De provincie Luxemburg is de grootste in oppervlakte, maar telt de minste inwoners. Het is er dun bevolkt en erg bosrijk.",
    },
    {
        "type": "waarofniet",
        "vraag": "De provincie Vlaams-Brabant ligt rond Brussel.",
        "antwoord": True,
        "uitleg": "Klopt, Vlaams-Brabant omsluit het Brussels Hoofdstedelijk Gewest volledig. Brussel zelf hoort bij geen enkele provincie.",
    },
]

WERELD = [
    {
        "type": "meerkeuze",
        "vraag": "Waarom is het in Australië winter als het bij ons zomer is?",
        "opties": [
            "de aardas staat schuin en Australië ligt op het zuidelijk halfrond",
            "Australië ligt op dat moment verder van de zon",
            "Australië ligt aan de andere kant van de evenaar en draait trager rond",
            "er is daar veel minder land dan water",
        ],
        "antwoord": 0,
        "uitleg": "Door de schuine aardas wijst het ene halfrond een half jaar naar de zon en het andere ervan weg. De afstand tot de zon heeft er niets mee te maken.",
    },
    {
        "type": "waarofniet",
        "vraag": "Hoe verder je van de evenaar woont, hoe groter het verschil tussen zomer en winter.",
        "antwoord": True,
        "uitleg": "Klopt. Aan de evenaar duurt de dag het hele jaar ongeveer twaalf uur; bij de poolcirkel gaat de zon in de zomer nauwelijks onder en in de winter amper op.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke oceaan is de grootste van de wereld?",
        "antwoord": "de Stille Oceaan",
        "uitleg": "De Stille Oceaan ligt tussen Azië en Amerika en is groter dan alle landmassa's samen. Hij heet ook wel de Grote Oceaan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Het is 18 uur in Brussel. Hoe laat is het dan ongeveer in New York, zes tijdzones naar het westen?",
        "opties": ["12 uur", "14 uur", "22 uur", "hetzelfde uur"],
        "antwoord": 0,
        "uitleg": "Naar het westen gaat de klok achteruit: 18 − 6 = 12 uur. Naar het oosten reizen zet de klok juist vooruit.",
    },
    {
        "type": "waarofniet",
        "vraag": "Rusland ligt volledig in Azië.",
        "antwoord": False,
        "uitleg": "Niet waar. Het westelijke deel, met Moskou en Sint-Petersburg, ligt in Europa. De Oeral vormt de grens tussen de twee werelddelen.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke bergketen vormt de grens tussen Europa en Azië?",
        "antwoord": "de Oeral",
        "uitleg": "De Oeral loopt van noord naar zuid door Rusland. Omdat Europa en Azië op dezelfde landmassa liggen, is er zo'n afspraak nodig om ze te scheiden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom voerden veel landen van de Europese Unie een gemeenschappelijke munt in?",
        "opties": [
            "om handelen tussen de landen makkelijker te maken",
            "om overal in Europa dezelfde taal te krijgen",
            "om de grenzen beter te kunnen sluiten",
            "om samen één leger te vormen",
        ],
        "antwoord": 0,
        "uitleg": "Met één munt vervalt het wisselen en weet je meteen wat iets elders kost. Dat maakt handel, reizen en prijzen vergelijken eenvoudiger.",
    },
    {
        "type": "waarofniet",
        "vraag": "Alle landen van de Europese Unie betalen met de euro.",
        "antwoord": False,
        "uitleg": "Niet waar. Landen als Zweden, Polen, Tsjechië en Denemarken hebben hun eigen munt gehouden. De eurozone is dus kleiner dan de Unie.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk werelddeel ligt Egypte?",
        "antwoord": "Afrika",
        "uitleg": "Egypte ligt in het noordoosten van Afrika. Een klein stukje, het Sinaï-schiereiland, ligt wel al in Azië.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke rivier stroomt door Duitsland en mondt uit in Nederland?",
        "opties": ["de Rijn", "de Donau", "de Seine", "de Po"],
        "antwoord": 0,
        "uitleg": "De Rijn komt uit Zwitserland, doorkruist Duitsland en bereikt bij Rotterdam de Noordzee. Daardoor is het een van de drukste vaarwegen van Europa.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Donau stroomt naar het westen en mondt uit in de Atlantische Oceaan.",
        "antwoord": False,
        "uitleg": "Niet waar. De Donau stroomt juist naar het oosten, door tien landen, en mondt uit in de Zwarte Zee.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel graden beslaat één tijdzone ongeveer, als je de aarde in 24 zones verdeelt?",
        "antwoord": "15",
        "reken": "360 / 24",
        "uitleg": "De aarde draait in 24 uur één keer rond, dus 360 : 24 = 15° per uur.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is het aan de kust van West-Europa zachter in de winter dan even ver naar het oosten?",
        "opties": [
            "door de warme zeestroom en de wind van zee",
            "door de bergen",
            "doordat er veel meer mensen wonen en stoken",
            "door de stand van de aardas",
        ],
        "antwoord": 0,
        "uitleg": "De Golfstroom brengt warm water tot bij onze kusten, en de westenwind neemt die warmte mee het land in. Hoe verder landinwaarts, hoe strenger de winters.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Sahara is de grootste warme woestijn ter wereld.",
        "antwoord": True,
        "uitleg": "Klopt, ze beslaat een groot deel van Noord-Afrika. Antarctica is wel groter, maar dat is een koude woestijn.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk land ligt de Mont Blanc, op de grens met Italië?",
        "antwoord": "Frankrijk",
        "uitleg": "De Mont Blanc is met ongeveer 4 800 meter de hoogste berg van de Alpen en van West-Europa.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat hebben IJsland, Noorwegen en Zwitserland gemeen?",
        "opties": [
            "ze horen niet bij de Europese Unie",
            "ze liggen alle drie aan de Middellandse Zee",
            "ze betalen alle drie met de euro",
            "ze zijn alle drie eilanden",
        ],
        "antwoord": 0,
        "uitleg": "Alle drie liggen ze in Europa en werken ze nauw samen met de Unie, maar geen van drie is er lid van.",
    },
    {
        "type": "waarofniet",
        "vraag": "Europa is na Oceanië het kleinste werelddeel.",
        "antwoord": True,
        "uitleg": "Klopt. Alleen Oceanië is kleiner. Toch wonen er in Europa veel mensen, want het is dicht bevolkt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom liggen de meeste grote steden aan een rivier of aan zee?",
        "opties": [
            "vervoer over water was altijd het goedkoopst",
            "daar is het klimaat altijd een stuk warmer",
            "daar is de lucht schoner",
            "daar waait er minder wind",
        ],
        "antwoord": 0,
        "uitleg": "Lang voor er treinen en vrachtwagens waren, ging zware vracht over water. Waar schepen konden aanleggen, ontstond handel, en waar handel is, groeit een stad.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke oceaan ligt tussen Afrika en Australië?",
        "antwoord": "de Indische Oceaan",
        "uitleg": "De Indische Oceaan ligt tussen Afrika, Azië en Australië. Hij is de op twee na grootste, na de Stille en de Atlantische Oceaan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe komt het dat het bij de evenaar het hele jaar door ongeveer even warm is?",
        "opties": [
            "de zon staat er altijd bijna loodrecht",
            "de aarde draait daar veel sneller rond haar as",
            "er waait daar nooit wind",
            "het land ligt daar hoger",
        ],
        "antwoord": 0,
        "uitleg": "Loodrecht invallend zonlicht verwarmt het sterkst, en aan de evenaar blijft dat het hele jaar ongeveer gelijk. Daar kent men geen zomer en winter, wel een droog en een nat seizoen.",
    },
]

HOOFDSTUKKEN = [
    ("Kaartlezen en oriëntatie", KAARTLEZEN),
    ("België", BELGIE),
    ("Europa en de wereld", WERELD),
]
