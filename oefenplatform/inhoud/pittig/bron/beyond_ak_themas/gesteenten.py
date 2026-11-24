"""Gesteenten, mineralen en datering — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Aardlagen met discordantie en intrusie --------------------------------
AL = Prent("aardlagen-intrusie", "Doorsnede door aardlagen", "schuine lagen 1 tot 4, een golvend vlak V, horizontale lagen 5 en 6 erboven en een intrusie M door de schuine lagen")
KLEUR = ["#b8a58a", "#d9cfa8", "#8a9a6a", "#c9b48a"]
ERO = "C 800 320 650 270 500 300 C 350 330 200 290 40 310"
def lijn_y(c, x):
    return c - 0.2 * (x - 40)
GRENS = [900, 600, 500, 400, 0]
lagen = []
for i in range(4):
    onder, boven = GRENS[i], GRENS[i + 1]
    lagen.append(f'<path d="M40 {onder} L 960 {lijn_y(onder, 960)} L 960 {lijn_y(boven, 960)} L 40 {boven} Z" fill="{KLEUR[i]}" stroke="#2f4a22" stroke-width="1"/>')
AL.svg('<defs><clipPath id="kader"><rect x="40" y="60" width="920" height="560"/></clipPath></defs><g clip-path="url(#kader)">' + "".join(lagen) + '</g>')
AL.pad("M40 60 L 960 60 L 960 300 " + ERO + " Z", "#e6dcc0", DONKER, 1)
AL.rect(40, 60, 920, 150, "#a9c38a", DONKER, 0, 1)
AL.rect(40, 60, 920, 60, "#ffffff", "none", 0, 0)
AL.lijn(40, 120, 960, 120, DONKER, 1)
AL.pad("M960 300 " + ERO, "none", ROOD, 3)
AL.pad("M330 620 L 360 450 L 340 380 L 380 305 L 410 312 L 390 380 L 410 450 L 390 620 Z", ROOD, DONKER, 1)
AL.rect(40, 60, 920, 560, "none", DONKER, 0, 2)
LAL = {"1": (800, 560), "2": (520, 455), "3": (250, 400), "4": (120, 340), "5": (650, 255), "6": (650, 165), "V": (820, 300), "M": (380, 540)}
for k, (x, y) in LAL.items():
    AL.letter(x, y, k)
ZAL = {k: [Prent.rond(x, y, 26)] for k, (x, y) in LAL.items()}
ZAL["1"].append(Prent.zone(620, 500, 340, 120))
ZAL["6"].append(Prent.zone(40, 120, 920, 90))
ZAL["M"].append(Prent.zone(330, 310, 80, 310))
ZAL["V"].append(Prent.zone(40, 280, 920, 40))

# Halveringstijd ---------------------------------------------------------
HT = Prent("halveringstijd", "Verval van een radioactieve stof", "grafiek: hoeveel procent over na 0 tot 4 halveringstijden")
X, Y = assen(HT, 0, 4, 0, 100, "aantal halveringstijden", "% van de stof over", 1, 25, links=140, rechts=900)
pts = " L ".join(f"{X(t / 20):.1f} {Y(100 * 0.5 ** (t / 20)):.1f}" for t in range(0, 81))
HT.pad("M" + pts, "none", BLAUW, 4)
for n in range(5):
    HT.cirkel(X(n), Y(100 * 0.5 ** n), 6, ORANJE, DONKER, 1)
ZHT = {n: [Prent.rond(X(n), Y(100 * 0.5 ** n), 30)] for n in range(5)}

VRAGEN = [
    klik(
        "Klik op de oudste laag.",
        AL.bestand, ZAL["1"],
        "Zonder omkering ligt de oudste laag onderaan.",
    ),
    klik(
        "Klik op het oude erosievlak waarop jongere lagen liggen.",
        AL.bestand, ZAL["V"],
        "Dat is een discordantievlak: de schuine lagen werden eerst afgesleten.",
    ),
    klik(
        "Klik op het gesteente dat in de bestaande lagen is binnengedrongen.",
        AL.bestand, ZAL["M"],
        "Dat is een intrusie van magma.",
    ),
    met_prent(AL.bestand, tabel(
        "Kijk naar de doorsnede met de intrusie. Klopt dit?",
        [
            ("M is jonger dan laag 4.", J),
            ("M is jonger dan laag 5.", F),
            ("Lagen 1 tot 4 zijn gekanteld voor laag 5 werd afgezet.", J),
            ("Bij V ontbreekt een stuk van de opeenvolging.", J),
        ],
        "M stopt aan het erosievlak, dus is M ouder dan laag 5. Bij V is er een hiaat.",
    )),
    met_prent(AL.bestand, volgorde(
        "Kijk naar de doorsnede. Zet de gebeurtenissen van oud naar jong.",
        [
            "Lagen 1 tot 4 worden horizontaal afgezet",
            "De lagen worden gekanteld",
            "Magma dringt binnen als M",
            "Erosie maakt het vlak V",
            "Lagen 5 en 6 worden afgezet",
        ],
        "Wat ergens door snijdt, is jonger. Wat erop ligt, ook.",
    )),
    met_prent(HT.bestand, tabel(
        "Kijk naar de grafiek. Hoeveel procent van de stof is er nog over?",
        [
            ("na 1 halveringstijd", "50 %"),
            ("na 2 halveringstijden", "25 %"),
            ("na 3 halveringstijden", "12,5 %"),
        ],
        "Elke halveringstijd blijft de helft over van wat er was.",
        kolommen=["50 %", "25 %", "12,5 %"],
    )),
    klik(
        "Klik op het punt waar nog een kwart van de stof over is.",
        HT.bestand, ZHT[2],
        "Na twee halveringstijden: de helft van de helft.",
    ),
    inv(
        "De halveringstijd van koolstof-14 is ongeveer 5 730 jaar. In een stuk hout is nog een vierde van de koolstof-14 over. Hoe oud is het hout ongeveer, in jaren?",
        ["11460", "11 460"],
        "Een vierde = 2 halveringstijden: 2 x 5 730 = 11 460 jaar.",
    ),
    tabel(
        "Magmatisch, sedimentair of metamorf?",
        [
            ("graniet", "Magmatisch"),
            ("conglomeraat", "Sedimentair"),
            ("kwartsiet", "Metamorf"),
            ("obsidiaan", "Magmatisch"),
            ("krijt", "Sedimentair"),
            ("leisteen", "Metamorf"),
        ],
        "Uit magma, uit afzetting of door druk en warmte omgevormd.",
        kolommen=["Magmatisch", "Sedimentair", "Metamorf"],
    ),
    koppel(
        "Koppel elk gesteente aan het gesteente waaruit het ontstaat door metamorfose.",
        [
            ("marmer", "kalksteen"),
            ("kwartsiet", "zandsteen"),
            ("leisteen", "kleisteen"),
        ],
        ["basalt", "steenkool"],
        "Het gesteente blijft vast, maar de kristallen groeien en richten zich.",
    ),
    tabel(
        "Waarom heeft dit gesteente grote, kleine of geen kristallen?",
        [
            ("graniet, traag afgekoeld in de diepte", "grote kristallen"),
            ("basalt, vrij snel afgekoeld aan het oppervlak", "kleine kristallen"),
            ("obsidiaan, bliksemsnel afgekoeld", "geen kristallen"),
        ],
        "Hoe trager de afkoeling, hoe meer tijd om kristallen te laten groeien.",
        kolommen=["grote kristallen", "kleine kristallen", "geen kristallen"],
    ),
    volgorde(
        "Zet deze losse sedimenten van fijn naar grof.",
        ["Klei", "Silt", "Zand", "Grind"],
        "Klei heeft de kleinste korrels.",
    ),
    tabel(
        "Mineraal of gesteente?",
        [
            ("kwarts", "Mineraal"),
            ("graniet", "Gesteente"),
            ("pyriet", "Mineraal"),
            ("mergel", "Gesteente"),
            ("veldspaat", "Mineraal"),
        ],
        "Een gesteente is een mengsel van mineralen.",
        kolommen=["Mineraal", "Gesteente"],
    ),
    casus(
        "In een groeve vind je onderaan een laag met fossielen van trilobieten, bovenaan een laag met schelpen van een soort die nog leeft.",
        [
            keuze(
                "De onderste laag is [[*ouder|jonger|even oud]] dan de bovenste.",
                "Wet van de superpositie.",
            ),
            keuze(
                "Trilobieten zijn goede gidsfossielen omdat ze maar een [[*beperkte|onbeperkte|onbekende]] tijd leefden, wel over de hele wereld.",
                "Kort geleefd en wijd verspreid.",
            ),
            keuze(
                "Zo'n datering zonder jaartal heet [[*relatief|absoluut|radioactief]].",
                "Enkel ouder of jonger.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over fossielen?",
        [
            ("Je vindt ze vooral in sedimentair gesteente.", J),
            ("Meestal blijven enkel de harde delen bewaard.", J),
            ("In graniet vind je veel fossielen.", F),
        ],
        "In magma smelt alles weg.",
    ),
    tabel(
        "Klopt dit over de gesteentecyclus?",
        [
            ("Graniet kan verweren tot zand.", J),
            ("Zandsteen kan onder druk kwartsiet worden.", J),
            ("Marmer kan smelten en magma worden.", J),
            ("Een metamorf gesteente blijft altijd metamorf.", F),
        ],
        "Elke soort kan in elke andere overgaan.",
    ),
    volgorde(
        "Zet de tijdperken van oud naar jong.",
        ["Precambrium", "Paleozoïcum", "Mesozoïcum", "Cenozoïcum"],
        "Paleo is oud, meso is midden, ceno is nieuw.",
    ),
    tabel(
        "Welke gebergtevorming hoort erbij?",
        [
            ("Ardennen", "Hercynisch"),
            ("Alpen", "Alpien"),
            ("Himalaya", "Alpien"),
            ("de oudste van de drie", "Caledonisch"),
        ],
        "Caledonisch, Hercynisch, Alpien: van oud naar jong.",
        kolommen=["Caledonisch", "Hercynisch", "Alpien"],
    ),
    mk(
        "Diamant is keihard en grafiet is zacht genoeg om mee te schrijven. Hoe kan dat?",
        [
            "De koolstofatomen zijn anders geordend",
            "Diamant bevat veel ijzer, grafiet helemaal niet",
            "Grafiet is een gesteente, diamant is een mineraal",
            "Diamant is ontstaan uit lava, grafiet uit plantenresten",
        ],
        0,
        "Beide zijn zuivere koolstof.",
    ),
    sleep(
        "In het [[Carboon]] groeiden grote moerasbossen. Hun resten raakten bedekt, kwamen onder [[druk]] en werden zo [[steenkool]].",
        ["Krijt", "lucht", "marmer"],
        "Steenkool is een organogeen gesteente.",
    ),
    mk(
        "Waarom moet je bij een geplooid gebied opletten met de wet van de superpositie?",
        [
            "De lagen kunnen omgekeerd liggen",
            "Fossielen lossen op tijdens het plooien",
            "Geplooide lagen zijn altijd jonger dan vlakke",
            "Bij plooien smelten de onderste lagen weg",
        ],
        0,
        "Een overhellende plooi kan de oudste laag bovenaan leggen.",
    ),
    tabel(
        "Relatieve of absolute datering?",
        [
            ("laag A is ouder dan laag B", "Relatief"),
            ("dit gesteente is 300 miljoen jaar oud", "Absoluut"),
            ("berekend met de halveringstijd", "Absoluut"),
            ("gebaseerd op een gidsfossiel", "Relatief"),
        ],
        "Absoluut geeft een getal in jaren.",
        kolommen=["Relatief", "Absoluut"],
    ),
    keuze(
        "Ongeveer 66 miljoen jaar geleden stierven de dinosaurussen uit. Daar ligt de grens tussen het Mesozoïcum en het [[*Cenozoïcum|Paleozoïcum|Precambrium]].",
        "Grote omslagen in het leven bepalen de grenzen.",
    ),
    tabel(
        "Klopt dit over puimsteen?",
        [
            ("Het is een uitvloeiingsgesteente.", J),
            ("Het zit vol gasbellen.", J),
            ("Het blijft op water drijven.", J),
            ("Het is een dieptegesteente.", F),
        ],
        "De lava schuimde op terwijl ze stolde.",
    ),
    mk(
        "Een gesteente dagzoomt in een rivierdal. Wat betekent dat?",
        [
            "Het komt daar aan het oppervlak",
            "Het is daar door de rivier afgezet",
            "Het ligt daar diep onder het water",
            "Het is daar overdag zichtbaar en 's nachts niet",
        ],
        0,
        "Bijvoorbeeld in een rotswand of een groeve.",
    ),
    inv(
        "Een gesteente bevat nog een achtste van een radioactieve stof met een halveringstijd van 700 miljoen jaar. Hoeveel miljoen jaar oud is het?",
        ["2100", "2 100"],
        "Een achtste = 3 halveringstijden: 3 x 700 = 2 100 miljoen jaar.",
    ),
    tabel(
        "Welk vast gesteente ontstaat uit dit losse sediment?",
        [
            ("grind", "conglomeraat"),
            ("zand", "zandsteen"),
            ("klei", "kleisteen"),
        ],
        "Druk en een kitstof zoals kalk of kiezel kitten de korrels aan elkaar.",
        kolommen=["conglomeraat", "zandsteen", "kleisteen"],
    ),
    open_(
        "Leg uit waarom de oudste aardlaag niet altijd onderaan ligt.",
        "Normaal worden lagen horizontaal op elkaar afgezet, dus ligt de oudste onderaan. Bij plooiing of breuken kunnen lagen kantelen of zelfs omklappen. Dan kan een oudere laag bovenaan komen te liggen.",
    ),
]
