"""Platentektoniek en reliëfvorming — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Profiel van de oceaanbodem ---------------------------------------------
OB = Prent("profiel-oceaanbodem", "Profiel van een continent tot midden in de oceaan (hoogte overdreven)", "dwarsprofiel met plat, helling, vlakte, rug en trog, letters A tot E")
OB.rect(40, 150, 920, 4, "none", "none", 0, 0)
GROND = "M40 150 L 200 150 L 330 170 L 400 400 L 560 420 L 640 360 L 700 260 L 760 360 L 820 420 L 870 590 L 920 430 L 960 420 L 960 620 L 40 620 Z"
OB.pad("M200 150 L 960 150 L 960 420 L 920 430 L 870 590 L 820 420 L 760 360 L 700 260 L 640 360 L 560 420 L 400 400 L 330 170 Z", "#9bc1df", "none", 0)
OB.pad(GROND, "#c9b48a", DONKER, 2)
OB.lijn(40, 150, 960, 150, BLAUW, 2, stippel=True)
OB.tekst(950, 140, "zeeniveau", 14, "end", kleur=BLAUW)
OB.tekst(110, 135, "land", 16)
LOB = {"A": (265, 195), "B": (365, 300), "C": (480, 445), "D": (700, 300), "E": (870, 560)}
for k, (x, y) in LOB.items():
    OB.letter(x, y, k)
ZOB = {"A": [Prent.zone(200, 150, 130, 60), Prent.rond(*LOB["A"], 26)],
       "B": [Prent.zone(330, 170, 70, 230), Prent.rond(*LOB["B"], 26)],
       "C": [Prent.zone(400, 380, 160, 80), Prent.rond(*LOB["C"], 26)],
       "D": [Prent.zone(640, 250, 120, 120), Prent.rond(*LOB["D"], 26)],
       "E": [Prent.zone(830, 420, 80, 180), Prent.rond(*LOB["E"], 26)]}

# Hotspot-eilanden -------------------------------------------------------
HS = Prent("hotspot-eilanden", "Een plaat schuift over een hotspot (schematisch)", "rij van vier eilanden W, X, Y, Z boven een plaat met pijl naar links en een mantelpluim onder Z")
HS.rect(40, 200, 920, 130, "#9bc1df", "none", 0, 0)
HS.rect(40, 330, 920, 70, "#5d5d5d", "none", 0, 0)
HS.rect(40, 400, 920, 220, "#e0a15a", "none", 0, 0)
HS.pijl(600, 365, 300, 365, GEEL, 5)
HS.tekst(620, 372, "beweging van de plaat", 16, "start", kleur="#ffffff")
HS.pad("M760 620 C 740 520 770 460 780 400 L 820 400 C 830 460 860 520 840 620 Z", ROOD, "none", 0)
HS.tekst(800, 600, "mantelpluim", 16, kleur="#ffffff", vet=True)
EIL = {"W": (180, 30, 50), "X": (380, 45, 90), "Y": (580, 60, 130), "Z": (810, 60, 175)}
for k, (x, b, h) in EIL.items():
    HS.pad(f"M{x - b * 2} 330 L {x} {330 - h - 100} L {x + b * 2} 330 Z", "#7a6a55", DONKER, 2)
    HS.letter(x, 140 - (h - 50) // 2 if k != "Z" else 60, k)
ZHS = {k: [Prent.zone(x - b * 2, 330 - h - 100, b * 4, h + 100)] for k, (x, b, h) in EIL.items()}

VRAGEN = [
    met_prent(OB.bestand, tabel(
        "Kijk naar het profiel. Welke letter hoort bij welke reliëfvorm?",
        [
            ("continentaal plat", "A"),
            ("continentale helling", "B"),
            ("abyssale vlakte", "C"),
            ("oceanische rug", "D"),
            ("diepzeetrog", "E"),
        ],
        "Van de kust naar de diepzee: plat, helling, vlakte.",
        kolommen=["A", "B", "C", "D", "E"],
    )),
    klik(
        "Klik op de plek waar nieuwe oceanische korst gemaakt wordt.",
        OB.bestand, ZOB["D"],
        "Aan de rug wijken de platen uiteen en stijgt magma op.",
    ),
    klik(
        "Klik op de plek waar een plaat wegduikt in de mantel.",
        OB.bestand, ZOB["E"],
        "Een diepzeetrog hoort bij subductie.",
    ),
    met_prent(OB.bestand, tabel(
        "Kijk naar het profiel van de oceaanbodem. Klopt dit?",
        [
            ("Bij A is de zee minder dan ongeveer 200 m diep.", J),
            ("Bij D bewegen twee platen naar elkaar toe.", F),
            ("Het dikste sediment ligt bij C, ver van de rug.", J),
            ("Bij E kan je zware aardbevingen verwachten.", J),
        ],
        "Bij de rug wijken platen uiteen; de vlakte is ouder en dus dikker bedekt.",
    )),
    klik(
        "Klik op het eiland dat nu boven de hotspot ligt.",
        HS.bestand, ZHS["Z"],
        "De mantelpluim ligt onder Z, daar is de vulkaan nog actief.",
    ),
    klik(
        "Klik op het oudste eiland.",
        HS.bestand, ZHS["W"],
        "De plaat schuift naar links: hoe verder van de hotspot, hoe ouder.",
    ),
    met_prent(HS.bestand, tabel(
        "Kijk naar de eilandenrij. Klopt dit?",
        [
            ("De hotspot blijft op dezelfde plaats.", J),
            ("W is het kleinst omdat het al lang verweert en zakt.", J),
            ("Over een tijd ontstaat rechts van Z een nieuw eiland.", J),
            ("De eilanden liggen op een plaatgrens.", F),
        ],
        "Een hotspot ligt midden op een plaat.",
    )),
    tabel(
        "Welke plaatbeweging hoort hierbij?",
        [
            ("Midatlantische Rug", "Divergentie"),
            ("Himalaya", "Convergentie"),
            ("San Andreasbreuk", "Transform"),
            ("Andes", "Convergentie"),
            ("Oost-Afrikaanse Slenk", "Divergentie"),
        ],
        "Uiteen, naar elkaar toe of langs elkaar.",
        kolommen=["Divergentie", "Convergentie", "Transform"],
    ),
    tabel(
        "Wat botst er en wat ontstaat er?",
        [
            ("oceanisch tegen continentaal", "trog en kustgebergte"),
            ("continentaal tegen continentaal", "plooiingsgebergte"),
            ("oceanisch tegen oceanisch", "trog en eilandenboog"),
        ],
        "Duiken kan enkel de zwaardere oceanische plaat.",
        kolommen=["trog en kustgebergte", "plooiingsgebergte", "trog en eilandenboog"],
    ),
    koppel(
        "Koppel elke drijvende kracht of oorzaak aan de juiste uitleg.",
        [
            ("slab pull", "een zware duikende plaat trekt de rest mee"),
            ("ridge push", "een hoge warme rug duwt de plaat weg"),
            ("mantelpluim", "een hete kolom stijgt op uit de diepe mantel"),
        ],
        ["de zon verwarmt de korst ongelijk", "de maan trekt de platen mee"],
        "De motor zit in de aarde zelf.",
    ),
    tabel(
        "Pleit dit voor de drift van de continenten?",
        [
            ("dezelfde fossielen van landdieren in Brazilië en Afrika", J),
            ("passende kustlijnen van Zuid-Amerika en Afrika", J),
            ("sporen van gletsjers in het huidige India", J),
            ("de grote ouderdom van alle oceaanbodems", F),
        ],
        "Oceaanbodems zijn juist jong: nergens ouder dan ongeveer 200 miljoen jaar.",
    ),
    mk(
        "De Atlantische Oceaan wordt ongeveer 2,5 cm per jaar breder. Hoeveel breder wordt hij in een mensenleven van 80 jaar?",
        [
            "2 meter",
            "20 centimeter",
            "20 meter",
            "200 meter",
        ],
        0,
        "80 x 2,5 cm = 200 cm = 2 m.",
    ),
    inv(
        "Een plaat schuift 8 cm per jaar over een hotspot. Hoeveel km verder ligt een eiland na 1 miljoen jaar?",
        ["80"],
        "8 cm x 1 000 000 = 8 000 000 cm = 80 km.",
    ),
    casus(
        "Langs de westkust van Zuid-Amerika duikt de Nazcaplaat onder de Zuid-Amerikaanse plaat.",
        [
            keuze(
                "Voor de kust ligt een [[*diepzeetrog|oceanische rug|abyssale vlakte]].",
                "Waar een plaat duikt, ontstaat een trog.",
            ),
            keuze(
                "Op het land is daardoor het [[*kustgebergte|plooiingsgebergte|rift]] van de Andes ontstaan.",
                "De rand van het continent wordt opgestuwd.",
            ),
            tabel(
                "Klopt dit over die kust?",
                [
                    ("Er zijn veel vulkanen.", J),
                    ("Er zijn zware aardbevingen.", J),
                    ("Er komt nieuwe korst bij.", F),
                ],
                "Korst verdwijnt hier, ze komt niet bij.",
            ),
        ],
    ),
    mk(
        "Waarom ligt een rij vulkanen een eind landinwaarts van de diepzeetrog, en niet in de trog zelf?",
        [
            "De duikende plaat smelt pas als ze diep genoeg zit",
            "Vulkanen kunnen alleen ontstaan op het droge land boven de zee",
            "In de trog is het water te koud om magma vloeibaar te houden",
            "De trog drukt het magma opzij naar de andere kant van de plaat",
        ],
        0,
        "Het water dat de plaat meeneemt, verlaagt in de diepte het smeltpunt.",
    ),
    tabel(
        "Anticline of syncline?",
        [
            ("de lagen welven op als een zadel", "Anticline"),
            ("de lagen buigen door als een trog", "Syncline"),
            ("de oudste laag ligt in het midden", "Anticline"),
            ("de jongste laag ligt in het midden", "Syncline"),
        ],
        "Sedimenten worden horizontaal afgezet en pas later geplooid.",
        kolommen=["Anticline", "Syncline"],
    ),
    volgorde(
        "Zet de stappen van het ontstaan van een oceaan in volgorde.",
        [
            "Een mantelpluim tilt de korst van een continent op",
            "De korst scheurt en er ontstaat een slenk",
            "Zeewater loopt de slenk binnen",
            "Een rug maakt steeds meer nieuwe oceaanbodem",
        ],
        "Zo is de Atlantische Oceaan ontstaan, en zo begint het in Oost-Afrika.",
    ),
    sleep(
        "Ongeveer 250 miljoen jaar geleden lag alle land samen in [[Pangea]]. Het zuidelijke deel heette [[Gondwana]]. Daaruit schoof [[India]] naar het noorden.",
        ["Laurazië", "Australië", "Atlantis"],
        "De botsing van India met Azië maakte de Himalaya.",
    ),
    keuze(
        "Waar drie riftarmen samenkomen, spreken we van een [[*riftster|caldera|syncline]].",
        "De Afar-driehoek in Ethiopië is een voorbeeld.",
    ),
    tabel(
        "Klopt dit over IJsland?",
        [
            ("Het ligt op de Midatlantische Rug.", J),
            ("Er zit ook een hotspot onder.", J),
            ("Het eiland wordt langzaam uit elkaar getrokken.", J),
            ("Het ligt boven een subductiezone.", F),
        ],
        "Rug en hotspot samen maken van IJsland een vulkaaneiland boven water.",
    ),
    mk(
        "Waarom zijn de Ardennen veel lager en ronder dan de Alpen?",
        [
            "Ze zijn veel ouder en al heel lang afgesleten",
            "Ze zijn ontstaan bij divergentie en niet bij botsing",
            "Ze bestaan uit zachter gesteente dat nooit hoog kon worden",
            "Ze liggen te ver van de zee om hoog te worden opgestuwd",
        ],
        0,
        "De Ardennen zijn ruim 300 miljoen jaar oud, de Alpen veel jonger.",
    ),
    sorteer(
        "Komt er korst bij of verdwijnt er korst?",
        ["Korst komt bij", "Korst verdwijnt", "Geen van beide"],
        [
            ("oceanische rug", "Korst komt bij"),
            ("diepzeetrog", "Korst verdwijnt"),
            ("transforme breuk", "Geen van beide"),
            ("rift in een continent", "Korst komt bij"),
        ],
        "Wat bijkomt, verdwijnt elders. De aarde wordt niet groter.",
    ),
    tabel(
        "Klopt dit over de snelheid van platen?",
        [
            ("Platen bewegen enkele centimeter per jaar.", J),
            ("Dat is ongeveer zo snel als nagels groeien.", J),
            ("Je kan de beweging meten met satellieten.", J),
            ("Een plaat beweegt enkele meter per jaar.", F),
        ],
        "Met GPS meten we de beweging tot op de millimeter.",
    ),
    mk(
        "Hoe kan een caldera ontstaan?",
        [
            "Het dak van een lege magmakamer stort in",
            "Een meteoriet slaat een kuil in de top van een vulkaan",
            "Een gletsjer schuurt de top van een vulkaan helemaal weg",
            "De plaat scheurt open en een stuk korst zakt de zee in",
        ],
        0,
        "Na een zware uitbarsting is de kamer leeg en zakt de vulkaan in.",
    ),
    tabel(
        "Welke beschrijving hoort bij welk gebergte?",
        [
            ("Himalaya", "botsing van twee continenten"),
            ("Andes", "oceanische plaat duikt onder een continent"),
            ("Ardennen", "oude, afgesleten plooiing"),
        ],
        "Het ontstaan bepaalt mee de vorm en de hoogte.",
        kolommen=["botsing van twee continenten", "oceanische plaat duikt onder een continent", "oude, afgesleten plooiing"],
    ),
    tabel(
        "Klopt dit over een dwarsprofiel?",
        [
            ("Het toont de hoogte langs een gekozen lijn op de kaart.", J),
            ("De hoogte wordt vaak overdreven om het reliëf te zien.", J),
            ("Je ziet er de ligging van alle steden op.", F),
        ],
        "Een profiel is een zijaanzicht van het reliëf.",
    ),
    keuze(
        "Langs een transforme breuk zoals de San Andreasbreuk ontstaan vooral [[*aardbevingen|vulkanen|eilandenbogen]].",
        "De platen haken in elkaar en schieten dan plots los.",
    ),
    open_(
        "Leg uit waarom de Atlantische Oceaan breder wordt en de Stille Oceaan smaller.",
        "Midden in de Atlantische Oceaan ligt een rug waar nieuwe korst bijkomt, dus groeit hij. Rond de Stille Oceaan liggen veel troggen waar korst wegduikt, de Ring of Fire. Daar verdwijnt meer korst dan er bijkomt.",
    ),
]
