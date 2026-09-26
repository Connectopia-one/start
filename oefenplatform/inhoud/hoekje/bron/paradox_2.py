# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Paradoxen en weetjes, deel 2: wonderlijke weetjes."""

VAK = "Paradoxen en weetjes"
BESTAND = "paradoxen-en-weetjes.json"
TITEL = "Wonderlijke weetjes"
VOLGORDE = 2

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "IJs drijft op water. Waarom is dat voor een vaste stof zo bijzonder?",
        "opties": [
            "Bijna alles wordt zwaarder per liter als het hard wordt, water niet",
            "Bijna alles blijft drijven als het hard wordt, behalve metalen",
            "IJs bevat luchtbelletjes die het naar de oppervlakte duwen",
            "IJs is kouder, en koude stoffen drijven altijd op warme",
        ],
        "antwoord": 0,
        "uitleg": "Bij het bevriezen houden waterstofbruggen de moleculen in een open zeshoekig rooster, met meer ruimte ertussen dan in vloeibaar water. Daardoor zet water uit bij het bevriezen. Vissen overleven de winter precies daardoor: het ijs ligt bovenop in plaats van onderaan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe krijgt een vliegtuigvleugel lift?",
        "opties": [
            "Hij duwt lucht naar beneden, en de lucht duwt even hard terug",
            "De bovenkant is bol, dus daar moet de lucht sneller inhalen",
            "De motoren blazen lucht onder de vleugel en tillen hem op",
            "De vleugel is lichter dan de lucht die hij verplaatst",
        ],
        "antwoord": 0,
        "uitleg": "Actie en reactie, de derde wet van Newton. De verhaaltjes over lucht die bovenlangs moet inhalen, kloppen niet: een vliegtuig kan ook op zijn rug vliegen. Wat telt, is de hoek waarmee de vleugel lucht omlaag stuurt.",
    },
    {
        "type": "waarofniet",
        "vraag": "Honing in een goed gesloten pot kan duizenden jaren houdbaar blijven.",
        "antwoord": True,
        "uitleg": "In Egyptische graven is honing gevonden die nog eetbaar was. Honing bevat weinig water en is zuur, dus bacteriën en schimmels krijgen er geen voet aan de grond. Er zit bovendien een stofje in dat een beetje waterstofperoxide vormt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De bidsprinkhaankreeft heeft twaalf tot zestien soorten kleurcellen in zijn ogen; wij hebben er drie. Wat volgt daaruit?",
        "opties": [
            "Niet noodzakelijk dat hij kleuren beter onderscheidt dan wij",
            "Dat hij vijf keer zoveel kleuren kan onderscheiden dan wij",
            "Dat hij enkel in zwart-wit ziet maar heel scherp",
            "Dat hij kleuren ziet die voor ons niet bestaan, en wij niets van de zijne",
        ],
        "antwoord": 0,
        "uitleg": "Uit proeven bleek hij juist mínder goed in het onderscheiden van dicht bij elkaar liggende kleuren dan wij. Het vermoeden is dat hij niet vergelijkt zoals ons brein doet, maar meteen herkent: sneller, maar grover. Hij ziet wel ultraviolet en de draairichting van licht.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wij delen een flink deel van onze genen met een banaan. Hoe komt dat?",
        "opties": [
            "Alle leven stamt af van dezelfde voorouder en gebruikt dezelfde celmachinerie",
            "Bananen hebben ooit genen van dieren overgenomen via de bodem",
            "Het is toeval: met evenveel genen krijg je vanzelf overlappingen",
            "Onze darmbacteriën brengen plantengenen in ons eigen erfelijk materiaal",
        ],
        "antwoord": 0,
        "uitleg": "Een cel van een banaan moet net als de jouwe energie maken, eiwitten bouwen en zich delen, en de recepten daarvoor zijn miljarden jaren oud. Het getal dat je vaak hoort, rond de helft van onze genen, hangt er wel van af hoe je precies telt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom klinkt je eigen stem anders op een opname dan in je hoofd?",
        "opties": [
            "Als je zelf praat, hoor je ook trillingen via je botten",
            "Een microfoon laat altijd de lage tonen van een stem weg",
            "Je oren staan te dicht bij je mond om goed te kunnen horen",
            "Je hersenen maken je eigen stem expres mooier terwijl je praat",
        ],
        "antwoord": 0,
        "uitleg": "Die botgeleiding versterkt vooral de lage tonen, dus in je hoofd klink je voller. Een opname geeft je alleen wat er door de lucht gaat, en dat is precies wat iedereen ánders van jou hoort. Zij vinden je stem dus heel normaal.",
    },
    {
        "type": "waarofniet",
        "vraag": "De maan is aan de horizon echt groter dan hoog aan de hemel.",
        "antwoord": False,
        "uitleg": "Meet ze maar met een muntje op armlengte: ze is even groot, en aan de horizon zelfs een piepklein beetje verder weg. Het is een illusie van je brein, dat haar vergelijkt met huizen en bomen. Niemand heeft ze sluitend verklaard.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In elk oog zit een blinde vlek. Waarom merk je die nooit?",
        "opties": [
            "Je hersenen vullen het gat in met wat eromheen te zien is",
            "De blinde vlek verschuift voortdurend, dus hij valt niet op",
            "Het andere oog kijkt precies op diezelfde plaats mee",
            "De blinde vlek ligt helemaal aan de rand van je gezichtsveld",
        ],
        "antwoord": 0,
        "uitleg": "Daar verlaat de oogzenuw het netvlies en zitten geen lichtgevoelige cellen. Je brein vult de leegte in met de omgeving, ook als je één oog dichtdoet. Je ziet dus letterlijk iets dat je niet waarneemt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom smaakt eten zo flauw als je een verstopte neus hebt?",
        "opties": [
            "Het meeste van wat wij smaak noemen, is eigenlijk geur",
            "Een verkoudheid verdooft de smaakpapillen op je tong",
            "Koorts verandert de temperatuur waarbij je kunt proeven",
            "Je slijmvlies legt een laagje over je tong heen",
        ],
        "antwoord": 0,
        "uitleg": "Je tong onderscheidt maar een handvol basissmaken. Al de rest, van aardbei tot koffie, komt van geurstoffen die via je keel naar je neus stijgen. Knijp je neus dicht en proef een stukje appel en een stukje ui: het verschil valt grotendeels weg.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op een hoge berg kookt water bij een lagere temperatuur dan aan zee.",
        "antwoord": True,
        "uitleg": "De luchtdruk is er lager, dus moleculen ontsnappen makkelijker. Op de Mont Blanc kookt water rond 85 graden. Handig? Niet echt: je eieren koken er trager gaar, want het water is minder heet.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Er wordt gezegd dat glas een heel trage vloeistof is, want oude kerkramen zijn onderaan dikker. Klopt dat?",
        "opties": [
            "Nee, die ruiten werden vroeger al ongelijk gemaakt",
            "Ja, glas vloeit inderdaad enkele millimeters per eeuw",
            "Ja, maar alleen bij ruiten die in de volle zon staan",
            "Nee, die ruiten zijn later door restaurateurs bijgeslepen",
        ],
        "antwoord": 0,
        "uitleg": "Glas is een vaste stof die bij kamertemperatuur niet merkbaar vloeit. Middeleeuwse ruiten werden met de hand gerold en waren aan één kant dikker; glazeniers zetten die dikke kant meestal onderaan, omdat dat steviger is.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een beerdiertje van een halve millimeter overleeft dingen waar wij aan zouden bezwijken. Wat is zijn truc?",
        "opties": [
            "Het droogt zichzelf volledig uit en legt alles stil",
            "Het maakt een harde schaal aan rond zijn lichaam",
            "Het verlaagt zijn lichaamstemperatuur tot bijna nul",
            "Het vervelt razendsnel telkens er iets misgaat",
        ],
        "antwoord": 0,
        "uitleg": "In die toestand, een tonnetje genoemd, verliest het bijna al zijn water en stopt zijn stofwisseling nagenoeg helemaal. Zo doorstaat het het vacuüm van de ruimte, extreme kou en hitte, en heel veel straling. Voeg water toe, en het wandelt weer weg.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een octopus heeft drie harten en blauw bloed. Waarom is dat bloed blauw?",
        "opties": [
            "Zijn zuurstof wordt door koper vervoerd in plaats van ijzer",
            "Het bevat een blauwe kleurstof als camouflage tegen vijanden",
            "Het koude zeewater verkleurt het bloed door de huid heen",
            "Zijn bloed bevat helemaal geen zuurstof maar wel veel zout",
        ],
        "antwoord": 0,
        "uitleg": "Ons bloed gebruikt hemoglobine met ijzer, en dat is rood. Bij de octopus doet hemocyanine met koper het werk, en dat is blauwachtig. Het werkt beter in koud water met weinig zuurstof. Twee harten pompen naar de kieuwen, het derde naar de rest van het lichaam.",
    },
    {
        "type": "waarofniet",
        "vraag": "Er staan meer bomen op aarde dan er sterren in onze Melkweg zijn.",
        "antwoord": True,
        "uitleg": "Een grote telling schatte het aantal bomen op ongeveer drie biljoen, dus drie miljoen keer een miljoen. De Melkweg telt naar schatting honderd tot vierhonderd miljard sterren. Bomen winnen dus met ruime voorsprong.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De Eiffeltoren is in de zomer hoger dan in de winter. Hoeveel scheelt dat ongeveer?",
        "opties": [
            "Ongeveer vijftien centimeter",
            "Ongeveer vijftien millimeter",
            "Ongeveer anderhalve meter",
            "Ongeveer vijftien meter",
        ],
        "antwoord": 0,
        "uitleg": "IJzer zet uit bij warmte. Over driehonderddertig meter hoogte geeft een verschil van enkele tientallen graden een kleine vijftien centimeter. Om diezelfde reden zitten er voegen tussen spoorstaven en in bruggen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Bananen zijn licht radioactief, en daarom mag je er maar enkele per dag eten.",
        "antwoord": False,
        "uitleg": "Licht radioactief zijn ze wel: ze zitten vol kalium, en een klein deel daarvan is kalium-40, dat van nature vervalt. Gevaarlijk is het niet, want je lichaam bevat zelf al kalium en houdt dat gewoon op peil. Er bestaat zelfs een scherts-eenheid, de bananendosis, om kleine stralingshoeveelheden aanschouwelijk te maken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom zijn er wel groene vogels en kikkers, maar geen groene zoogdieren?",
        "opties": [
            "Haren kunnen geen groen pigment of structuurkleur maken",
            "Zoogdieren leven bijna allemaal onder de grond",
            "Groen bloed zou te veel warmte vasthouden",
            "Zoogdieren zien zelf geen groen en hebben er niets aan",
        ],
        "antwoord": 0,
        "uitleg": "De kleur van vogelveren komt vaak van de structuur die licht breekt, niet van pigment; haren kunnen dat niet. Luiaards lijken groen, maar dat komt van algen die in hun vacht groeien. Voor veel zoogdieren werkt bruingrijs trouwens prima als camouflage.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een dag op aarde wordt langzaam langer. Hoe komt dat?",
        "opties": [
            "De getijden remmen de aarde af, en de maan schuift weg",
            "De aarde wordt zwaarder door het stof uit de ruimte",
            "De zon trekt de aarde elk jaar iets verder van zich af",
            "De kern van de aarde koelt af en krimpt daarbij",
        ],
        "antwoord": 0,
        "uitleg": "De waterbulten van eb en vloed wrijven tegen de draaiende aarde en remmen haar af, ongeveer twee duizendsten van een seconde per eeuw. Wat de aarde aan draaiing verliest, wint de maan aan baan: ze schuift zo'n vier centimeter per jaar van ons weg.",
    },
    {
        "type": "waarofniet",
        "vraag": "Twee willekeurige mensen verschillen in ongeveer tien procent van hun DNA.",
        "antwoord": False,
        "uitleg": "Twee mensen komen voor ongeveer 99,9 procent overeen. Al het verschil tussen mensen op aarde zit in dat laatste tiende van een procent. Binnen één groep chimpansees is de erfelijke verscheidenheid groter dan onder alle mensen samen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je ziet de bliksem en telt drie seconden tot de donder. Hoe ver is het onweer ongeveer?",
        "opties": [
            "Ongeveer één kilometer",
            "Ongeveer drie kilometer",
            "Ongeveer driehonderd meter",
            "Ongeveer tien kilometer",
        ],
        "antwoord": 0,
        "uitleg": "Geluid legt zo'n 340 meter per seconde af, dus drie seconden is ruim een kilometer. Licht is er praktisch meteen. De donder zelf is de knal van lucht die door de bliksem plots tot tienduizenden graden wordt opgewarmd en uitzet.",
    },
]
