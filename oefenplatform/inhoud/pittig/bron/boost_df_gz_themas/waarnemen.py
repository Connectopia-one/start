"""Waarnemen: van prikkel tot reactie — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_waarnemen, met een zelfgetekende doorsnede van de
huid, aangevuld met enkele vragen uit biologie Boost doorstroom."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL
from ..boost_do_bi_themas import zenuwstelsel as _z, spieren as _s

HU = Prent("huid-doorsnede", "Doorsnede van de huid", "drie lagen van de huid met een haar, een zweetklier, een bloedvat en een receptor, met letters A tot F")
HU.rect(150, 120, 700, 70, "#f3d9c4", DONKER, 0, 2)       # opperhuid
HU.rect(150, 190, 700, 200, "#eab9a0", DONKER, 0, 2)      # lederhuid
HU.rect(150, 390, 700, 150, "#fbeec0", DONKER, 0, 2)      # onderhuids vet
for x in range(190, 800, 70):
    for y in (430, 490):
        HU.cirkel(x + (20 if y == 490 else 0), y, 22, "#fff6d8", "#d8c27a", 1)
HU.lijn(330, 60, 330, 330, "#4a3a2a", 5)                 # haar
HU.ellips(330, 320, 22, 40, "#d79a7e", DONKER, 2)        # haarzakje
HU.pad("M 560 120 L 560 300 Q 560 330 585 330 Q 610 330 600 300 Q 590 280 610 290", "none", BLAUW, 4)   # zweetklierbuis
HU.cirkel(600, 320, 26, "#cfe3f5", BLAUW, 3)             # zweetklier
HU.pad("M 150 360 Q 400 330 500 365 T 850 350", "none", ROOD, 6)   # bloedvat
HU.cirkel(730, 230, 16, GEEL, DONKER, 2); HU.lijn(730, 246, 730, 380, GEEL, 4)   # receptor met zenuw
LET = {"A": (900, 155), "B": (900, 290), "C": (900, 465), "D": (250, 80), "E": (660, 320), "F": (770, 210)}
for t, (x, y) in LET.items():
    HU.letter(x, y, t)
HU.lijn(272, 80, 325, 80, DONKER, 1); HU.lijn(640, 320, 628, 320, DONKER, 1); HU.lijn(752, 214, 744, 222, DONKER, 1)
U = "huid-doorsnede.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}

VRAGEN = [_z.VRAGEN[16], _s.VRAGEN[14], _s.VRAGEN[19], _s.VRAGEN[20]] + [
    klik("Klik op de letter bij de bovenste laag van de huid.", U, [Z["A"]],
         "De opperhuid ligt bovenaan; ze heeft geen bloedvaten."),
    klik("Klik op de letter bij de laag met de bloedvaten, de klieren en de zenuwuiteinden.", U, [Z["B"]],
         "In de lederhuid zitten receptoren, bloedvaten en klieren."),
    klik("Klik op de letter bij de laag die isoleert en stoten opvangt.", U, [Z["C"]],
         "Het onderhuids vetweefsel houdt de warmte binnen."),
    klik("Klik op de letter bij de exocriene klier die zweet afgeeft via een kanaal.", U, [Z["E"]],
         "De zweetklier ligt in de lederhuid en geeft zweet af op de opperhuid."),
    klik("Klik op de letter bij de receptor die aanraking of warmte opvangt.", U, [Z["F"]],
         "Mechano- en thermoreceptoren liggen in de lederhuid."),
    casus("Lotte raakt een hete kookplaat aan en trekt haar hand weg.", [
        volgorde("Zet de stappen van het waarnemingsproces in de juiste volgorde.",
                 ["prikkel: de hitte", "receptor: de pijnreceptor in de huid", "conductor: de zenuw", "effector: de armspier"],
                 "Prikkel, receptor, conductor, effector."),
        keuze("De hitte is een [[*uitwendige|inwendige]] prikkel.",
              "Ze komt van buiten het lichaam."),
        keuze("De receptor die de pijn meldt, heet een [[*nociceptor|fotoreceptor|chemoreceptor]].",
              "De nociceptor heeft een alarmerende functie."),
        keuze("Dat Lotte haar hand meteen wegtrekt, toont de [[*alarmerende|sociale|communicatieve]] functie van waarnemen.",
              "Waarnemen waarschuwt voor gevaar."),
    ]),
    tabel("Welk type receptor vangt deze prikkel op?",
          [("licht", "fotoreceptor"), ("een geurstof", "chemoreceptor"), ("koude", "thermoreceptor"), ("druk op de huid", "mechanoreceptor")],
          "Foto is licht, thermo warmte, chemo stoffen, mechano druk en beweging.",
          kolommen=["fotoreceptor", "chemoreceptor", "thermoreceptor", "mechanoreceptor"]),
    tabel("Endocriene of exocriene klier?",
          [("geeft een hormoon rechtstreeks aan het bloed", "endocrien"), ("geeft zweet af via een kanaal op de huid", "exocrien"), ("geeft speeksel af in de mond", "exocrien")],
          "Endocrien betekent naar binnen, in het bloed.",
          kolommen=["endocrien", "exocrien"]),
    koppel("Welk zintuig hoort bij welk orgaan met receptoren?",
           [("zien", "het oog"), ("ruiken", "de neus"), ("smaken", "de tong"), ("voelen", "de huid")], ["de lever"],
           "De lever is een orgaan, geen zintuig."),
    tabel("Is dit een basissmaak?",
          [("zoet", J), ("umami", J), ("bitter", J), ("warm", F)],
          "Warm is een temperatuur, geen smaak."),
    mk("Tom is verkouden en vindt dat zijn soep nergens naar smaakt. Hoe komt dat?",
       ["De reuk valt weg, en smaak is grotendeels reuk.", "Zijn smaakknoppen zijn door de koorts helemaal kapot.", "De soep is door de verkoudheid echt minder zout.", "Zijn tong maakt door de koorts geen speeksel meer aan."], 0,
       "Met een dichte neus mis je het grootste deel van de smaak."),
    volgorde("Zet de stappen van het ruiken in de juiste volgorde.",
             ["de geurstof komt in de neusholte", "ze lost op in het slijm", "ze raakt de reukhaartjes", "de reukcel stuurt een impuls naar de hersenen"],
             "Pas opgelost in het slijm ontstaat er een impuls."),
    keuze("De smaakknoppen zitten in de [[*papillen|reukhaartjes|lederhuid]] op de tong.",
          "De papillen zijn de bultjes op de tong."),
    tabel("Klopt dit over de huid?",
          [("De huid maakt met zonlicht vitamine D.", J), ("In de opperhuid zitten bloedvaten.", F), ("De huid helpt de warmte te regelen.", J), ("Een heel lichte schram bloedt vaak niet.", J)],
          "De bloedvaten zitten in de lederhuid."),
    keuze("Een zenuw geeft de boodschap [[*snel en elektrisch|traag via het bloed]] door; een hormoon [[*trager via het bloed|snel en elektrisch]].",
          "Een hormoon werkt langzamer maar bereikt het hele lichaam."),
    sorteer("Receptor, conductor of effector?", ["receptor", "conductor", "effector"],
            [("een smaakcel", "receptor"), ("een zenuw", "conductor"), ("een spier", "effector"), ("een klier", "effector")],
            "De receptor vangt op, de conductor geleidt, de effector voert uit."),
    keuze("De vijf zintuigen zijn oog, oor, neus, tong en [[*huid|lever|hart]].",
          "De huid is het tastzintuig."),
    sleep("Van buiten naar binnen heeft de huid de [[opperhuid]], de [[lederhuid]] en het onderhuids vetweefsel.",
          ["papillen", "netvlies"], "Drie lagen."),
    tabel("Is dit een functie van waarnemen?",
          [("je waarschuwen voor gevaar", J), ("contact maken met anderen", J), ("genieten van muziek of een geur", J), ("voedsel verteren", F)],
          "Verteren doet het spijsverteringsstelsel."),
    keuze("Een thermoreceptor meldt [[*warmte en koude|licht en donker|zoet en zuur]].",
          "Thermo betekent warmte."),
    tabel("Inwendige of uitwendige prikkel?",
          [("pijn in je buik", "inwendig"), ("een felle lamp", "uitwendig"), ("honger", "inwendig"), ("een koude wind", "uitwendig")],
          "Inwendig komt van binnen het lichaam.",
          kolommen=["inwendig", "uitwendig"]),
    keuze("Een reukcel is zelf een [[*zenuwcel|spiercel|kliercel]]: ze vangt de prikkel op en geeft de impuls door.",
          "De reukcel stuurt zelf de impuls naar de hersenen."),
    open_("Leg uit waarom een pijnreceptor in de huid belangrijk is voor je gezondheid. Gebruik een voorbeeld.",
          "Hij meldt gevaar, zoals iets heets of scherps. Daardoor trek je je hand terug voor er grote schade is. Wie geen pijn voelt, merkt een wonde of brandwonde niet op tijd.",
          "De alarmerende functie van waarnemen."),
]
