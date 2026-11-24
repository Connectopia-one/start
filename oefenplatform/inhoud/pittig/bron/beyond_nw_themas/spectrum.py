"""Het elektromagnetisch spectrum — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en twee eigen prenten, aangevuld met enkele passende vragen uit
de pittige vragen fysica Beyond.
"""
from ..beyond_fys_themas import licht as L, kwantum as Q
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, LICHTGROEN

# Het spectrum als band met zeven vakken --------------------------------------------
SP = Prent("spectrum-band", "Het elektromagnetisch spectrum", "een horizontale band met zeven vakken A tot G; onder de band een pijl: naar rechts wordt de frequentie groter; vak D is in regenboogkleuren")
VAKKEN = ["A", "B", "C", "D", "E", "F", "G"]
BREED = [190, 140, 130, 60, 110, 120, 140]
x = 50
POS = {}
for k, b in zip(VAKKEN, BREED):
    if k == "D":
        kleuren = ["#c0392b", "#e67e22", "#f1c40f", "#27ae60", "#2980b9", "#8e44ad"]
        for i, kl in enumerate(kleuren):
            SP.rect(x + i * b / 6, 200, b / 6, 160, kl, kl, 0, 0)
        SP.rect(x, 200, b, 160, "none", DONKER, 0, 2)
    else:
        SP.rect(x, 200, b, 160, "#eef1f4", DONKER, 0, 2)
    POS[k] = (x, b)
    SP.letter(x + b / 2, 280, k)
    x += b
SP.pijl(80, 420, 900, 420, DONKER, 3)
SP.tekst(490, 455, "de frequentie wordt groter", 20, vet=True)
SP.tekst(490, 160, "golven in vacuüm, allemaal even snel", 18)
ZSP = {k: [Prent.zone(x0, 200, b, 160)] for k, (x0, b) in POS.items()}

# Drie keer licht op een voorwerp ----------------------------------------------------
LV = Prent("licht-op-materie", "Een lichtbundel valt telkens op een ander voorwerp", "drie vakken: P een glasplaat waar de bundel doorheen gaat, Q een spiegel waar de bundel van terugkaatst, R een zwart blok waar de bundel in verdwijnt")
for i, (k, vul) in enumerate((("P", "#d8ecf7"), ("Q", "#c9ccd1"), ("R", "#2b2b2b"))):
    x0 = 60 + i * 310
    LV.rect(x0, 90, 270, 450, "#ffffff", "#8a8470", 12, 1)
    LV.letter(x0 + 135, 125, k)
    if k == "P":
        LV.rect(x0 + 115, 220, 40, 220, vul, DONKER, 2, 2)
        LV.pijl(x0 + 20, 330, x0 + 250, 330, GEEL, 6)
    elif k == "Q":
        LV.rect(x0 + 200, 200, 18, 260, vul, DONKER, 2, 2)
        LV.pijl(x0 + 20, 250, x0 + 198, 330, GEEL, 6)
        LV.pijl(x0 + 198, 330, x0 + 20, 410, GEEL, 6)
    else:
        LV.rect(x0 + 150, 230, 90, 200, vul, DONKER, 2, 2)
        LV.pijl(x0 + 20, 330, x0 + 148, 330, GEEL, 6)
ZLV = {k: [Prent.zone(60 + i * 310, 90, 270, 450)] for i, k in enumerate("PQR")}

EIGEN = [
    klik(
        "Klik op het deel van het spectrum dat een afstandsbediening van een televisie gebruikt.",
        SP.bestand, ZSP["C"],
        "Infrarood ligt net naast het rode licht, aan de kant van de lagere frequenties.",
    ),
    klik(
        "Klik op het deel van het spectrum waarmee een bagagescanner werkt.",
        SP.bestand, ZSP["F"],
        "Röntgenstraling ligt tussen uv en gamma.",
    ),
    klik(
        "Klik op het deel van het spectrum met de grootste golflengte.",
        SP.bestand, ZSP["A"],
        "Een lage frequentie hoort bij een grote golflengte: radiogolven.",
    ),
    met_prent(SP.bestand, tabel(
        "Welke straling hoort bij welk vak?",
        [("microgolven", "B"), ("ultraviolet", "E"), ("gammastraling", "G")],
        "De volgorde is radio, micro, infrarood, zichtbaar, uv, röntgen, gamma.",
        kolommen=["B", "E", "G"],
    )),
    met_prent(SP.bestand, tabel(
        "Kijk naar het spectrum. Klopt dit?",
        [
            ("De straling in vak G heeft de meeste energie.", J),
            ("De straling in vak A gaat in vacuüm trager dan die in vak G.", F),
            ("Vak E is ioniserend in zijn hoogenergetische deel.", J),
            ("Een mens kan de straling van vak B zien.", F),
        ],
        "Alle elektromagnetische golven gaan in vacuüm even snel; enkel vak D is zichtbaar.",
    )),
    klik(
        "Klik op het voorwerp dat het licht vooral absorbeert.",
        LV.bestand, ZLV["R"],
        "Een zwart voorwerp neemt het licht op en warmt op.",
    ),
    met_prent(LV.bestand, tabel(
        "Welke interactie met materie zie je?",
        [("P", "doorlaten"), ("Q", "weerkaatsen"), ("R", "absorberen")],
        "Doorlaten heet ook transmissie.",
        kolommen=["doorlaten", "weerkaatsen", "absorberen"],
    )),
    casus(
        "Op een röntgenfoto van een gebroken arm zijn de botten wit en het spierweefsel grijs.",
        [
            keuze(
                "De botten zijn wit omdat ze de röntgenstraling meer [[*absorberen|doorlaten]] dan het zachte weefsel.",
                "Waar weinig straling de plaat bereikt, blijft ze licht.",
            ),
            mk(
                "Waarom draagt de verpleger een loodschort?",
                ["Lood houdt röntgenstraling goed tegen", "Lood weerkaatst de straling naar de patiënt", "Lood maakt de foto scherper", "Lood koelt het toestel af"],
                0,
                "Lood absorbeert veel hoogenergetische straling.",
            ),
            tabel(
                "Is röntgenstraling ioniserend, en waarom?",
                [
                    ("Ze kan elektronen uit atomen slaan.", J),
                    ("Ze heeft een kleinere golflengte dan zichtbaar licht.", J),
                    ("Ze gaat sneller dan zichtbaar licht.", F),
                ],
                "Een kleine golflengte betekent een hoge energie per golf.",
            ),
        ],
    ),
    koppel(
        "Koppel de toepassing aan de straling die ze gebruikt.",
        [
            ("wifi", "radiogolven"),
            ("warmtebeeldcamera", "infrarood"),
            ("blacklight", "ultraviolet"),
            ("bestraling van voedsel", "gammastraling"),
        ],
        ["zichtbaar licht"],
        "Elke toepassing kiest het deel van het spectrum dat ze nodig heeft.",
    ),
    mk(
        "Waarom wordt gras groen gezien?",
        ["Het weerkaatst vooral groen licht", "Het absorbeert vooral groen licht", "Het laat vooral groen licht door", "Het zendt zelf groen licht uit"],
        0,
        "De kleur die je ziet, is de kleur die weerkaatst wordt.",
    ),
    keuze(
        "Een metalen rooster in de deur van een magnetron werkt als een [[*kooi van Faraday|spiegel voor licht]] voor de microgolven.",
        "De gaatjes zijn kleiner dan de golflengte van de microgolven.",
    ),
    sorteer(
        "Is deze bescherming nodig tegen ioniserende straling of tegen niet-ioniserende straling?",
        ["Ioniserend", "Niet ioniserend"],
        [
            ("een loodschort bij een röntgenfoto", "Ioniserend"),
            ("een dikke betonnen muur rond een bestralingstoestel", "Ioniserend"),
            ("ovenwanten tegen de warmte van een oven", "Niet ioniserend"),
            ("een lasbril tegen fel zichtbaar licht", "Niet ioniserend"),
        ],
        "Ioniserend zijn röntgen, gamma en hoogenergetisch uv.",
    ),
    inv(
        "Een radiozender zendt uit op 100 MHz. Licht gaat 300 000 000 m/s. Hoe groot is de golflengte, in m?",
        ["3", "3,0", "3 m"],
        "λ = c / f = 3 · 10⁸ / 1 · 10⁸ = 3 m.",
    ),
    open_(
        "Leg uit waarom uv-straling je huid kan beschadigen en infrarood niet, al voel je infrarood wel als warmte.",
        "Uv-straling heeft een hogere frequentie en dus meer energie per golf. Hoogenergetisch uv kan elektronen uit atomen slaan en zo het DNA in huidcellen beschadigen. Infrarood heeft te weinig energie per golf om dat te doen: het warmt enkel op.",
    ),
]

EIGEN += [
    klik(
        "Klik op het deel van het spectrum dat een magnetron gebruikt.",
        SP.bestand, ZSP["B"],
        "Microgolven liggen tussen radiogolven en infrarood.",
    ),
    klik(
        "Klik op het deel van het spectrum dat men gebruikt om voedsel te steriliseren.",
        SP.bestand, ZSP["G"],
        "Gammastraling heeft de hoogste energie en doodt micro-organismen.",
    ),
    met_prent(SP.bestand, tabel(
        "Ligt deze straling links of rechts van het zichtbare licht?",
        [("infrarood", "links"), ("ultraviolet", "rechts"), ("radiogolven", "links"), ("röntgenstraling", "rechts")],
        "Links: lagere frequentie, grotere golflengte.",
        kolommen=["links", "rechts"],
    )),
    keuze(
        "Hoe groter de frequentie van een elektromagnetische golf, hoe [[*kleiner|groter]] haar golflengte.",
        "De snelheid ligt vast: golflengte maal frequentie is de lichtsnelheid.",
    ),
    mk(
        "Een gsm-mast zendt radiogolven uit en geen ultraviolet. Waarom is dat een goede keuze?",
        ["Radiogolven dragen ver en zijn niet ioniserend", "Radiogolven gaan sneller dan ultraviolet", "Ultraviolet kan niet door de lucht", "Radiogolven hebben meer energie"],
        0,
        "Ze gaan door muren en zijn onschadelijk voor cellen.",
    ),
    keuze(
        "Zonnecrème beschermt je huid omdat ze uv-straling [[*absorbeert|doorlaat]].",
        "Zo bereikt minder uv je huidcellen.",
    ),
    sleep(
        "Röntgenstraling dringt makkelijk door [[zacht weefsel]], maar wordt meer tegengehouden door [[botten]]. Daarom is een röntgenfoto [[ioniserend]] en mag je er niet te veel nemen.",
        ["glas", "infrarood"],
        "Botten bevatten zware atomen zoals calcium.",
    ),
    mk(
        "Welke straling gebruikt een zonnebank?",
        ["ultraviolet", "infrarood", "microgolven", "röntgenstraling"],
        0,
        "Uv laat de huid bruinen, maar kan ook huidkanker veroorzaken.",
    ),
]

OVER = [L.VRAGEN[i] for i in (15, 16, 17, 18)] + [Q.VRAGEN[i] for i in (11, 21)]

VRAGEN = EIGEN + OVER
