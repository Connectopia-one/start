"""Toepassingen van redox: batterijen, galvaniseren en corrosie — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Roestproef met vier proefbuizen -------------------------------------------
RP = Prent("roestproef-nagels", "Vier proefbuizen met een ijzeren nagel, bij het begin van de proef", "vier proefbuizen met een nagel: droge lucht met droogmiddel, gekookt water onder een laagje olie, kraantjeswater met lucht, zout water met lucht; letters P tot S")
BUIS = {
    "P": ("droge lucht", "droogmiddel", None),
    "Q": ("gekookt water", "laagje olie", "#e8f2fa"),
    "R": ("kraantjeswater", "lucht erboven", "#e8f2fa"),
    "S": ("zout water", "lucht erboven", "#d6e8f5"),
}
for i, (k, (t1, t2, kl)) in enumerate(BUIS.items()):
    x = 160 + i * 230
    RP.pad(f"M {x - 50} 110 L {x - 50} 430 Q {x - 50} 480 {x} 480 Q {x + 50} 480 {x + 50} 430 L {x + 50} 110", "#ffffff", DONKER, 3)
    if kl:
        RP.pad(f"M {x - 48} 250 L {x - 48} 430 Q {x - 48} 478 {x} 478 Q {x + 48} 478 {x + 48} 430 L {x + 48} 250 Z", kl, "none", 0)
    if k == "Q":
        RP.rect(x - 48, 235, 96, 16, "#f2dc8a", "none", 0, 0)
    if k == "P":
        for j in range(7):
            RP.cirkel(x - 30 + j * 10, 460 - (j % 2) * 8, 7, "#ffffff", DONKER, 1)
        RP.lijn(x - 48, 420, x + 48, 420, DONKER, 2, stippel=True)
    RP.rect(x - 4, 140, 8, 260, "#8f8f8f", DONKER, 2, 1)
    RP.rect(x - 14, 132, 28, 10, "#8f8f8f", DONKER, 2, 1)
    RP.tekst(x, 515, t1, 17, vet=True)
    RP.tekst(x, 538, t2, 15)
    RP.letter(x, 590, k)
ZRP = {k: [Prent.zone(105 + i * 230, 110, 110, 375), Prent.rond(160 + i * 230, 590, 22)] for i, k in enumerate(BUIS)}

# Verzinkt en vertind ijzer met een kras ------------------------------------
KR = Prent("kras-zink-tin", "Doorsnede van ijzer met een beschermend laagje en een kras", "twee doorsneden: links ijzer met een laagje zink, rechts ijzer met een laagje tin, allebei met een kras tot op het ijzer en een waterdruppel erop; letters A en B")
for i, (k, laag, kl) in enumerate((("A", "zink", "#b8c4cc"), ("B", "tin", "#dcdcd0"))):
    x0 = 80 + i * 450
    KR.rect(x0, 330, 390, 110, "#8c7f73", DONKER, 0, 2)
    KR.tekst(x0 + 195, 395, "ijzer", 22, vet=True, kleur="#ffffff")
    KR.rect(x0, 300, 170, 30, kl, DONKER, 0, 2)
    KR.rect(x0 + 220, 300, 170, 30, kl, DONKER, 0, 2)
    KR.tekst(x0 + 85, 322, laag, 18, vet=True)
    KR.tekst(x0 + 305, 322, laag, 18, vet=True)
    KR.pad(f"M {x0 + 120} 300 Q {x0 + 195} 190 {x0 + 270} 300 Z", "#cfe5f3", BLAUW, 2)
    KR.rect(x0 + 170, 300, 50, 30, "#cfe5f3", "none", 0, 0)
    KR.lijn(x0 + 170, 300, x0 + 170, 330, DONKER, 2)
    KR.lijn(x0 + 220, 300, x0 + 220, 330, DONKER, 2)
    KR.tekst(x0 + 195, 270, "water", 16, kleur=BLAUW)
    KR.letter(x0 + 195, 500, k)
ZKR = {k: [Prent.zone(80 + i * 450, 190, 390, 250), Prent.rond(275 + i * 450, 500, 22)] for i, k in enumerate("AB")}

VRAGEN = [
    klik(
        "Klik op de proefbuis waar de nagel het snelst roest.",
        RP.bestand, ZRP["S"],
        "Water, zuurstof en opgeloste ionen die het water geleidend maken.",
    ),
    klik(
        "Klik op een proefbuis waar de nagel niet roest omdat er geen zuurstof bij kan.",
        RP.bestand, ZRP["Q"],
        "Koken verdrijft het zuurstofgas, de olie houdt nieuw zuurstofgas tegen.",
    ),
    met_prent(RP.bestand, tabel(
        "Wat ontbreekt er in deze proefbuis om te roesten?",
        [
            ("P", "Water"),
            ("Q", "Zuurstof"),
            ("R", "Niets"),
        ],
        "IJzer heeft water én zuurstof nodig om te roesten.",
        kolommen=["Water", "Zuurstof", "Niets"],
    )),
    klik(
        "Klik op het plaatje waar het ijzer in de kras aangetast wordt.",
        KR.bestand, ZKR["B"],
        "Tin is een zwakkere reductor dan ijzer: het ijzer wordt geoxideerd.",
    ),
    met_prent(KR.bestand, tabel(
        "Kijk naar de twee plaatjes. Klopt dit?",
        [
            ("In A wordt het zink aangetast in plaats van het ijzer.", J),
            ("In B roest het ijzer sneller dan zonder tin.", J),
            ("In A is het zink de kathode.", F),
        ],
        "Het minst edele metaal wordt geoxideerd en is dus de anode.",
    )),
    met_prent(KR.bestand, mk(
        "Waarom gebruikt men toch tin voor conservenblikken?",
        [
            "Heel tin is veilig voor voedsel",
            "Tin is een sterkere reductor dan ijzer",
            "Tin beschermt ook in een kras het ijzer",
            "Tin maakt het blik zwaarder en steviger",
        ],
        0,
        "Zolang er geen kras is, sluit tin het ijzer goed af en is het onschadelijk.",
    )),
    tabel(
        "Werkt deze maatregel door afsluiten of door een sterkere reductor?",
        [
            ("verf", "Afsluiten"),
            ("een laagje olie", "Afsluiten"),
            ("een laagje zink", "Sterkere reductor"),
            ("een magnesiumblok aan een scheepsromp", "Sterkere reductor"),
        ],
        "Zink beschermt beide manieren, maar blijft ook bij een kras werken omdat het de sterkere reductor is.",
        kolommen=["Afsluiten", "Sterkere reductor"],
    ),
    mk(
        "Waarom roest een auto sneller in de winter?",
        [
            "Strooizout maakt het water geleidend",
            "Koude versnelt elke redoxreactie",
            "In de winter is er meer zuurstof in de lucht",
            "IJs is een sterke oxidator voor ijzer",
        ],
        0,
        "De ionen van het zout laten de lading makkelijker bewegen.",
    ),
    tabel(
        "Wordt dit deeltje bij het roesten geoxideerd of gereduceerd?",
        [
            ("Fe", "Geoxideerd"),
            ("O₂", "Gereduceerd"),
            ("Fe²⁺ naar Fe³⁺", "Geoxideerd"),
        ],
        "IJzer staat elektronen af, zuurstof neemt ze op.",
        kolommen=["Geoxideerd", "Gereduceerd"],
    ),
    casus(
        "Een stalen boiler bevat een staaf magnesium. Gebruik Mg²⁺/Mg = −2,37 V en Fe²⁺/Fe = −0,44 V.",
        [
            keuze(
                "De magnesiumstaaf is een [[*verteringselektrode|kathode|katalysator]].",
                "Ze wordt opgegeten in plaats van het staal.",
            ),
            mk(
                "Waarom wordt het magnesium aangetast en het ijzer niet?",
                [
                    "Magnesium is de sterkere reductor",
                    "Magnesium is de sterkere oxidator",
                    "IJzer reageert niet met water",
                    "Magnesium is lichter dan ijzer",
                ],
                0,
                "Het laagste koppel in de tabel staat het makkelijkst elektronen af.",
            ),
            tabel(
                "Klopt dit over de boiler?",
                [
                    ("Na een paar jaar moet je de staaf vervangen.", J),
                    ("Zo werkt kathodische bescherming.", J),
                    ("Een koperen staaf zou even goed werken.", F),
                ],
                "Koper is een zwakkere reductor dan ijzer en zou het roesten net versnellen.",
            ),
        ],
    ),
    tabel(
        "Is dit een batterij, een oplaadbare batterij of een brandstofcel?",
        [
            ("raakt leeg en gaat bij het afval", "Batterij"),
            ("wordt honderden keren opgeladen", "Oplaadbaar"),
            ("werkt zolang je H₂ en O₂ aanvoert", "Brandstofcel"),
        ],
        "Een brandstofcel raakt niet leeg zolang de stoffen aangevoerd worden.",
        kolommen=["Batterij", "Oplaadbaar", "Brandstofcel"],
    ),
    mk(
        "Wat komt er uit een waterstofbrandstofcel als afval?",
        ["Water", "Koolstofdioxide", "Waterstofperoxide", "Zinkoxide"],
        0,
        "2 H₂ + O₂ → 2 H₂O.",
    ),
    tabel(
        "Klopt dit over het verkoperen van een sleutel?",
        [
            ("De sleutel hangt aan de minpool.", J),
            ("De koperen anode lost langzaam op.", J),
            ("Hoe langer de stroom loopt, hoe dikker het laagje.", J),
            ("De oplossing raakt snel zonder koperionen.", F),
        ],
        "De anode vult de koperionen aan die op de sleutel neerslaan.",
    ),
    volgorde(
        "Zet de stappen van het roesten van ijzer in de goede volgorde.",
        [
            "IJzer staat elektronen af en wordt Fe²⁺",
            "Zuurstofgas in het water neemt die elektronen op",
            "Fe²⁺ wordt verder geoxideerd tot Fe³⁺",
            "Er vormt zich een poreuze laag roest",
        ],
        "Roest beschermt niet: het laat water en lucht door.",
    ),
    mk(
        "Aluminium is een sterkere reductor dan ijzer, maar corrodeert in de praktijk weinig. Waarom?",
        [
            "Het vormt een dicht oxidelaagje",
            "Aluminium reageert niet met zuurstof",
            "Aluminium is een edel metaal",
            "Het oxide lost meteen op in water",
        ],
        0,
        "Dat laagje sluit het metaal eronder af, roest bij ijzer doet dat niet.",
    ),
    sleep(
        "Een batterij levert spanning door een [[spontane]] redoxreactie. De anode is de [[negatieve]] pool. Ze is leeg als een [[reagens]] op is.",
        ["gedwongen", "positieve", "katalysator"],
        "Het verschil in normpotentiaal bepaalt de spanning.",
    ),
    tabel(
        "Kan dit metaal als verteringselektrode voor ijzer dienen?",
        [
            ("magnesium", "Ja"),
            ("zink", "Ja"),
            ("koper", "Nee"),
            ("zilver", "Nee"),
        ],
        "Alleen een sterkere reductor dan ijzer, dus lager in de tabel.",
        kolommen=["Ja", "Nee"],
    ),
    mk(
        "Waarom mag je een gewone alkalinebatterij niet opladen?",
        [
            "Haar reactie is niet goed omkeerbaar",
            "Ze bevat geen anode en kathode",
            "Ze levert wisselspanning in plaats van gelijkspanning",
            "Ze bevat helemaal geen metalen of ionen",
        ],
        0,
        "Er ontstaat gas en de batterij kan lekken of openbarsten.",
    ),
    inv(
        "Een batterij bestaat uit de koppels Zn²⁺/Zn (−0,76 V) en Ag⁺/Ag (+0,80 V). Welke spanning levert ze bij normomstandigheden, in volt?",
        ["1,56", "1.56", "1,56 V"],
        "0,80 − (−0,76) = 1,56 V.",
    ),
    tabel(
        "Welke pool en welk proces hoort bij dit deel van een batterij?",
        [
            ("anode", "Min, oxidatie"),
            ("kathode", "Plus, reductie"),
        ] + [("de pool waar elektronen de batterij verlaten", "Min, oxidatie")],
        "Elektronen komen vrij bij de oxidatie aan de minpool.",
        kolommen=["Min, oxidatie", "Plus, reductie"],
    ),
    mk(
        "Waarom wordt een batterij gevaarlijk warm bij kortsluiting?",
        [
            "De reactie loopt zonder weerstand heel snel",
            "De spanning stijgt dan tot boven 100 volt",
            "Er ontstaat dan een elektrolyse in de batterij",
            "De zoutbrug wordt dan een gewone draad",
        ],
        0,
        "Alle energie komt dan in korte tijd vrij als warmte.",
    ),
    keuze(
        "Oude batterijen horen bij het [[*klein gevaarlijk afval|restafval|gft-afval]], omdat ze zware metalen bevatten.",
        "Zo komen zink, lithium of nikkel niet in het milieu terecht.",
    ),
    tabel(
        "Klopt dit over een waterstofbrandstofcel?",
        [
            ("Waterstofgas wordt aan de anode geoxideerd.", J),
            ("Zuurstofgas wordt aan de kathode gereduceerd.", J),
            ("Ze moet aan het stopcontact om te werken.", F),
        ],
        "Een brandstofcel is een galvanische cel met voortdurende aanvoer.",
    ),
    inv(
        "Hoeveel elektronen staat één ijzeratoom af als het helemaal tot Fe³⁺ geoxideerd wordt?",
        ["3", "drie"],
        "Van 0 naar +III.",
    ),
    mk(
        "Waarom verzilvert men juwelen vaak in plaats van ze uit massief zilver te maken?",
        [
            "Een dun laagje volstaat voor het uitzicht",
            "Massief zilver kan niet gesmolten worden",
            "Zilver geleidt geen elektrische stroom",
            "Een laagje is altijd harder dan het metaal",
        ],
        0,
        "Zo spaar je veel duur metaal.",
    ),
    koppel(
        "Koppel elke beschermingsmethode aan haar werking.",
        [
            ("verven", "lucht en water weghouden"),
            ("verzinken", "zink wordt eerst aangetast"),
            ("magnesiumblok", "verteringselektrode"),
            ("een laagje vet", "lucht en water weghouden, voor gereedschap"),
        ],
        ["een sterkere oxidator toevoegen"],
        "Een sterkere oxidator zou het roesten net versnellen.",
    ),
    tabel(
        "Gaat een stalen paal in deze omgeving sneller roesten dan in droge binnenlucht?",
        [
            ("aan de zee", "Ja"),
            ("in een droge kelder met droogmiddel", "Nee"),
            ("in zout strooiwater", "Ja"),
        ],
        "Vocht, zuurstof en zout versnellen het roesten.",
        kolommen=["Ja", "Nee"],
    ),
    open_(
        "Leg uit waarom verzinkt ijzer ook bij een kras beschermd blijft, maar vertind ijzer niet.",
        "Zink is een sterkere reductor dan ijzer. Komen ijzer en zink samen in contact met water, dan wordt het zink geoxideerd in plaats van het ijzer. Tin is een zwakkere reductor dan ijzer: bij een kras wordt het ijzer de anode en roest het zelfs sneller dan zonder laagje.",
    ),
]
