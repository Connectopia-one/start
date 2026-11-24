"""Het landschap lezen — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Valse kleuren ----------------------------------------------------------
VK = Prent("valse-kleuren", "Satellietbeeld in valse kleuren (vereenvoudigd)", "beeld met een rivier, een stad, bos, akkers en een kale akker, letters A tot E")
VK.rect(40, 60, 920, 560, "#c98a8a", "none", 0, 0)
VK.pad("M40 420 C 200 380 300 470 460 430 C 620 390 700 480 960 440 L 960 480 C 700 520 620 430 460 470 C 300 510 200 420 40 460 Z", "#0d1f4a", "none", 0)
VK.pad("M560 90 L 900 90 L 920 300 L 600 330 Z", "#8fb8c2", DONKER, 1)
for x in range(590, 900, 40):
    VK.lijn(x, 100, x + 10, 320, "#c7dce0", 2)
VK.pad("M60 90 C 160 70 300 90 360 140 C 400 200 330 300 220 320 C 120 330 60 260 60 200 Z", "#c0101a", "none", 0)
VK.rect(400, 120, 120, 90, "#e05a5a", DONKER, 0, 1)
VK.rect(400, 220, 120, 90, "#b8a890", DONKER, 0, 1)
VK.rect(80, 500, 200, 100, "#e07070", DONKER, 0, 1)
VK.rect(320, 520, 220, 80, "#d8c8b0", DONKER, 0, 1)
LVK = {"A": (200, 200), "B": (500, 455), "C": (750, 210), "D": (460, 265), "E": (180, 550)}
for k, (x, y) in LVK.items():
    VK.letter(x, y, k)
ZVK = {"A": [Prent.zone(70, 90, 300, 230)],
       "B": [Prent.zone(40, 420, 920, 60)],
       "C": [Prent.zone(560, 90, 360, 240)],
       "D": [Prent.zone(400, 220, 120, 90)],
       "E": [Prent.zone(80, 500, 200, 100)]}

# Systeemdenkschema -------------------------------------------------------
SD = Prent("systeemschema-verharding", "Systeemdenkschema: verharding in een wijk", "vier blokjes verharding, afstromend regenwater, wateroverlast en groen, met pijlen P, Q en R")
BLOK = {"verharding": (120, 130), "groen": (120, 430), "afstromend regenwater": (520, 130), "wateroverlast": (520, 430)}
for t, (x, y) in BLOK.items():
    SD.rect(x, y, 300 if x > 400 else 240, 80, "#f7f4ea", DONKER, 14, 2)
    SD.tekst(x + (150 if x > 400 else 120), y + 48, t, 20, vet=True)
SD.pijl(365, 170, 515, 170, DONKER, 3)
SD.pijl(670, 215, 670, 425, DONKER, 3)
SD.pijl(240, 425, 240, 215, DONKER, 3)
SD.tekst(440, 158, "+", 30, vet=True)
SD.tekst(690, 330, "+", 30, vet=True)
SD.tekst(215, 330, "?", 30, vet=True)
LSD = {"P": (440, 230), "Q": (740, 320), "R": (170, 320)}
for k, (x, y) in LSD.items():
    SD.letter(x, y, k)
ZSD = {"P": [Prent.zone(365, 150, 150, 40), Prent.rond(*LSD["P"], 26)],
       "Q": [Prent.zone(650, 215, 40, 210), Prent.rond(*LSD["Q"], 26)],
       "R": [Prent.zone(220, 215, 40, 210), Prent.rond(*LSD["R"], 26)]}

VRAGEN = [
    klik(
        "Klik op het bos met gezonde plantengroei.",
        VK.bestand, ZVK["A"],
        "Gezond bladgroen weerkaatst veel nabij-infrarood en kleurt felrood.",
    ),
    klik(
        "Klik op de bebouwde zone.",
        VK.bestand, ZVK["C"],
        "Een stad komt in valse kleuren grijsblauw door.",
    ),
    met_prent(VK.bestand, tabel(
        "Kijk naar het beeld in valse kleuren. Klopt dit?",
        [
            ("B is water, want het is bijna zwart.", J),
            ("D is een kale of geoogste akker.", J),
            ("E heeft meer plantengroei dan D.", J),
            ("A is een parking in beton.", F),
        ],
        "Water slorpt infrarood op en kleurt donker.",
    )),
    met_prent(VK.bestand, mk(
        "Waarom kleurt bos A op dit beeld rood en niet groen?",
        [
            "Infrarood krijgt hier de kleur rood",
            "De bomen staan in hun herfstkleuren",
            "De satelliet ziet geen groen licht",
            "Het bos staat in brand op dat moment",
        ],
        0,
        "Bladgroen weerkaatst veel nabij-infrarood, en die band wordt rood getoond.",
    )),
    klik(
        "Klik op het verband dat met een min moet aangeduid worden.",
        SD.bestand, ZSD["R"],
        "Meer groen geeft minder verharding op dezelfde plek.",
    ),
    met_prent(SD.bestand, tabel(
        "Kijk naar het systeemdenkschema. Klopt dit?",
        [
            ("Pijl P betekent: meer verharding, meer afstromend water.", J),
            ("Pijl Q betekent: meer afstromend water, meer wateroverlast.", J),
            ("Bij pijl R hoort een plus.", F),
        ],
        "Meer groen betekent minder verharding: dat is een min.",
    )),
    met_prent(SD.bestand, open_(
        "Kijk naar het schema. Voeg een factor toe die verband houdt met groen en met hitte, en zet plus of min bij de pijlen.",
        "Bijvoorbeeld: groen -> hitte in de wijk met een min, want meer groen geeft minder hitte. Verharding -> hitte met een plus, want meer beton en asfalt geven meer hitte.",
    )),
    tabel(
        "Sporen van de natuur of van de mens?",
        [
            ("een kronkelende beek", "Natuur"),
            ("een kaarsrechte gracht", "Mens"),
            ("een holle weg", "Mens"),
            ("een harde rug in het reliëf", "Natuur"),
            ("grote rechthoekige percelen na ruilverkaveling", "Mens"),
        ],
        "De natuur maakt bochten, de mens maakt rechte lijnen.",
        kolommen=["Natuur", "Mens"],
    ),
    tabel(
        "Open of gesloten landschap?",
        [
            ("grote akkers zonder hagen", "Open"),
            ("kleine weiden met houtkanten", "Gesloten"),
            ("een kouter", "Open"),
            ("bocagelandschap met hagen rond elk perceel", "Gesloten"),
        ],
        "Houtkanten en hagen sluiten het zicht af.",
        kolommen=["Open", "Gesloten"],
    ),
    koppel(
        "Koppel elke bron aan wat ze je leert.",
        [
            ("kaart van Ferraris", "het landschap rond 1775"),
            ("digitaal hoogtemodel", "het reliëf"),
            ("bodemkaart", "de grondsoort per plek"),
            ("warmtebeeld", "waar de stad het heetst is"),
        ],
        ["de mening van de bewoners"],
        "Die laatste haal je uit een enquête, niet uit een kaart.",
    ),
    casus(
        "Je vergelijkt een luchtfoto van 1971 met een van vandaag voor dezelfde gemeente.",
        [
            keuze(
                "Het verschil tussen de twee beelden toont de [[*verandering|ondergrond|neerslag]] van het landschap.",
                "Leg de lagen over elkaar in Geopunt.",
            ),
            tabel(
                "Wat kan je zo zien?",
                [
                    ("nieuwe verkavelingen", J),
                    ("weggehaalde houtkanten", J),
                    ("de dikte van de kleilaag onder de akkers", F),
                    ("nieuwe wegen", J),
                ],
                "Een luchtfoto toont enkel het oppervlak.",
            ),
        ],
    ),
    mk(
        "Waarom liggen veel oude dorpskernen op de rand van een beekdal?",
        [
            "Droog wonen met water dichtbij",
            "In het dal zelf was de grond het vruchtbaarst om te bouwen",
            "De beek beschermde het dorp tegen vijanden op de heuvel",
            "Op de rand van een dal waait er nooit wind",
        ],
        0,
        "Het dal zelf was te nat, de hoogte te ver van het water.",
    ),
    volgorde(
        "Zet de stappen bij het lezen van een landschap in volgorde.",
        [
            "Beschrijf de vormen en lijnen",
            "Zoek welke processen ze maakten",
            "Schat de ouderdom en de opeenvolging",
            "Beoordeel hoe je het landschap kan beheren",
        ],
        "Eerst kijken, dan verklaren, dan dateren, dan oordelen.",
    ),
    tabel(
        "Klopt dit over de SDG's?",
        [
            ("Het zijn er zeventien.", J),
            ("SDG 11 gaat over duurzame steden en gemeenschappen.", J),
            ("Ze gaan ook over armoede en onderwijs.", J),
            ("Ze gaan enkel over klimaat.", F),
        ],
        "Ze hangen allemaal met elkaar samen.",
    ),
    sorteer(
        "Bij welke P van duurzame ontwikkeling hoort dit?",
        ["People", "Planet", "Prosperity"],
        [
            ("goed onderwijs voor iedereen", "People"),
            ("leven in het water beschermen", "Planet"),
            ("waardig werk en economische groei", "Prosperity"),
            ("geen honger", "People"),
            ("klimaatactie", "Planet"),
        ],
        "De andere twee P's zijn peace en partnership.",
    ),
    mk(
        "Waarom staan er in de Kempen zoveel naaldbossen?",
        [
            "Men plantte ze op arme zandgrond",
            "Naaldbomen groeien van nature enkel in de Kempen",
            "De Kempen hebben het koudste klimaat van België",
            "Loofbomen werden er door de wind vernield",
        ],
        0,
        "Op de heide werden grove dennen geplant, onder meer voor mijnhout.",
    ),
    tabel(
        "Klopt dit over een GIS?",
        [
            ("Het bewaart elke kaartlaag apart.", J),
            ("Je kan lagen over elkaar leggen.", J),
            ("Geopunt is een voorbeeld van een kaarttoepassing met veel lagen.", J),
            ("Een GIS werkt enkel met papieren kaarten.", F),
        ],
        "Een geografisch informatiesysteem is digitaal.",
    ),
    sleep(
        "Een overblijfsel uit vroeger, zoals een oude houtkant of een [[holle weg]], heet een [[landschapsrelict]]. Het vertelt iets over het [[gebruik]] van het landschap vroeger.",
        ["kouter", "systeemschema", "klimaat"],
        "Relicten zijn kostbaar omdat ze niet terug te maken zijn.",
    ),
    keuze(
        "Een plus bij een pijl in een systeemschema betekent dat beide factoren [[*in dezelfde richting|in tegengestelde richting|helemaal niet]] veranderen.",
        "Samen stijgen of samen dalen.",
    ),
    tabel(
        "Ware kleuren of valse kleuren?",
        [
            ("het beeld zoals je oog het zou zien", "Ware kleuren"),
            ("infrarood wordt zichtbaar gemaakt", "Valse kleuren"),
            ("gezonde planten zijn felrood", "Valse kleuren"),
            ("gebruikt de banden rood, groen en blauw", "Ware kleuren"),
        ],
        "Valse kleuren tonen wat het oog niet ziet.",
        kolommen=["Ware kleuren", "Valse kleuren"],
    ),
    mk(
        "Wat veranderde de ruilverkaveling aan het Vlaamse landschap?",
        [
            "Percelen werden groter en rechter",
            "Alle akkers werden omgezet in bos",
            "De beken kregen hun bochten terug",
            "Er kwamen overal nieuwe holle wegen",
        ],
        0,
        "Zo konden boeren met grote machines werken; veel houtkanten verdwenen.",
    ),
    tabel(
        "Klopt dit over een geologische doorsnede?",
        [
            ("Ze toont de lagen onder het oppervlak.", J),
            ("Je ziet er de dikte van de lagen op.", J),
            ("Je kan er een harde laag op herkennen die een heuvel vormt.", J),
            ("Ze toont de bebouwing in een stad.", F),
        ],
        "De ondergrond verklaart vaak het reliëf.",
    ),
    inv(
        "De kaart van Ferraris is van ongeveer 1775. Hoeveel jaar oud is ze in 2026?",
        ["251"],
        "2026 - 1775 = 251 jaar.",
    ),
    tabel(
        "Klopt dit over Vlaamse steden aan een rivier?",
        [
            ("Een rivier was vroeger een belangrijke vervoersweg.", J),
            ("Water dreef molens aan.", J),
            ("Steden lagen er omdat er geen wateroverlast kon zijn.", F),
        ],
        "Rivieren gaven vervoer, kracht en drinkwater.",
    ),
    mk(
        "Een gemeente tekent een systeemschema voor ze een plein heraanlegt. Wat levert dat vooral op?",
        [
            "Inzicht in onverwachte neveneffecten",
            "Het geeft altijd één juiste oplossing",
            "Het vervangt het overleg met bewoners",
            "Het toont de hoogte van het reliëf",
        ],
        0,
        "Door de pijlen te volgen zie je wat een ingreep verderop doet.",
    ),
    keuze(
        "Een groot, open akkerblok op de hoogste en droogste grond van een oud dorp heet een [[*kouter|beemd|holle weg]].",
        "Het oude, vruchtbare akkerland.",
    ),
    tabel(
        "Klopt dit over landschapsgenese?",
        [
            ("Het gaat over hoe een landschap gegroeid is.", J),
            ("Zowel natuurlijke als menselijke processen spelen mee.", J),
            ("Een landschap verandert sinds de ijstijd niet meer.", F),
        ],
        "De laatste eeuw veranderde het sneller dan ooit.",
    ),
    tabel(
        "Kan je dit aflezen op een warmtebeeld van een stad?",
        [
            ("welke pleinen in beton heet worden", J),
            ("waar parken koel blijven", J),
            ("hoeveel mensen er in elk huis wonen", F),
        ],
        "Een warmtebeeld meet warmte-infrarood.",
    ),
    open_(
        "Je wil weten of een bouwgrond in je gemeente een goede plek is om te wonen. Welke kaartlagen zou je bekijken en waarom?",
        "De overstromingskaart, om te zien of de grond nat kan worden. De bodemkaart en het hoogtemodel, voor de grondsoort en de ligging. Een kaart met voorzieningen en openbaar vervoer, om te zien of school, winkels en bus dichtbij zijn. En luchtfoto's om te zien of het in de open ruimte ligt.",
    ),
]
