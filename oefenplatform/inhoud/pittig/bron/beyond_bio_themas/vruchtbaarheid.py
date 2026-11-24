"""Vruchtbaarheid regelen en behandelen — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vrouwelijk voortplantingsstelsel ----------------------------------------
VS = Prent("voortplanting-vrouw", "Vrouwelijke voortplantingsorganen (vooraanzicht)", "baarmoeder in het midden met twee eileiders en eierstokken, baarmoederhals en vagina onderaan; letters A tot E")
VS.pad("M380 200 C 300 150 230 170 200 230", "none", "#e8a0b0", 22)
VS.pad("M620 200 C 700 150 770 170 800 230", "none", "#e8a0b0", 22)
VS.ellips(190, 290, 55, 35, "#f3c6d0", DONKER, 2)
VS.ellips(810, 290, 55, 35, "#f3c6d0", DONKER, 2)
VS.pad("M380 180 C 420 160 580 160 620 180 C 640 260 590 380 540 420 L 460 420 C 410 380 360 260 380 180 Z", "#f3c6d0", DONKER, 3)
VS.pad("M420 200 C 460 190 540 190 580 200 C 585 260 550 350 515 390 L 485 390 C 450 350 415 260 420 200 Z", "#e8a0b0", DONKER, 1)
VS.rect(470, 420, 60, 50, "#f3c6d0", DONKER, 6, 2)
VS.rect(455, 470, 90, 130, "#f8dbe2", DONKER, 10, 2)
VS.tekst(150, 360, "eierstok", 14)
VS.tekst(850, 360, "eierstok", 14)
LVS = {"A": (90, 290), "B": (300, 120), "C": (500, 300), "D": (620, 445), "E": (620, 560)}
VS.lijn(112, 290, 135, 290, DONKER, 1)
VS.lijn(300, 142, 300, 168, DONKER, 1)
VS.lijn(598, 445, 532, 445, DONKER, 1)
VS.lijn(598, 560, 547, 560, DONKER, 1)
for k, (x, y) in LVS.items():
    VS.letter(x, y, k)
ZVS = {"A": [Prent.rond(190, 290, 55), Prent.rond(810, 290, 55), Prent.rond(*LVS["A"], 22)],
       "B": [Prent.zone(220, 150, 160, 70), Prent.zone(620, 150, 160, 70), Prent.rond(*LVS["B"], 22)],
       "C": [Prent.zone(420, 200, 160, 190), Prent.rond(*LVS["C"], 22)],
       "D": [Prent.zone(465, 420, 70, 50), Prent.rond(*LVS["D"], 22)],
       "E": [Prent.zone(455, 470, 90, 130), Prent.rond(*LVS["E"], 22)]}

# IVF in vier stappen ------------------------------------------------------
IV = Prent("ivf-stappen", "Een IVF-behandeling in vier stappen (schematisch)", "vier vakken P, Q, R en S van links naar rechts")
for i, x in enumerate((30, 270, 510, 750)):
    IV.rect(x, 110, 220, 420, "#fbf6ea", DONKER, 16, 2)
    if i < 3:
        IV.pijl(x + 225, 320, x + 245, 320, DONKER, 2)
# P: eierstok met veel follikels
IV.ellips(140, 330, 80, 55, "#f3c6d0", DONKER, 2)
for dx, dy in ((-40, -15), (-10, -25), (25, -15), (-30, 20), (5, 15), (40, 18)):
    IV.cirkel(140 + dx, 330 + dy, 13, "#fff3d6", DONKER, 1)
IV.tekst(140, 450, "hormonen", 14)
# Q: naald bij eierstok
IV.ellips(380, 380, 60, 40, "#f3c6d0", DONKER, 2)
IV.cirkel(370, 375, 12, "#fff3d6", DONKER, 1)
IV.lijn(300, 180, 365, 365, GRIJS, 4)
IV.rect(285, 150, 30, 40, "#dde6ee", DONKER, 4, 1.5)
# R: petrischaal
IV.ellips(620, 340, 85, 30, "#e6f0f7", DONKER, 2)
IV.cirkel(620, 335, 16, "#fff3d6", DONKER, 1.5)
for dx in (-55, -40, 40, 52):
    IV.cirkel(620 + dx, 340, 4, BLAUW, "none", 0)
    IV.lijn(620 + dx, 340, 620 + dx + (8 if dx > 0 else -8), 330, BLAUW, 1.5)
# S: baarmoeder met embryo en katheter
IV.pad("M790 220 C 820 205 900 205 930 220 C 940 300 900 380 875 400 L 845 400 C 820 380 780 300 790 220 Z", "#f3c6d0", DONKER, 2)
IV.cirkel(860, 280, 12, "#fff3d6", DONKER, 1.5)
IV.lijn(860, 500, 860, 300, GRIJS, 4)
LIV = {"P": (140, 145), "Q": (380, 145), "R": (620, 145), "S": (860, 145)}
for k, (x, y) in LIV.items():
    IV.letter(x, y, k)
ZIV = {k: [Prent.zone(x - 110, 110, 220, 420)] for k, (x, y) in LIV.items()}

VRAGEN = [
    klik(
        "Klik op de plek waar een spiraaltje geplaatst wordt.",
        VS.bestand, ZVS["C"],
        "Het spiraaltje zit in de baarmoederholte.",
    ),
    klik(
        "Klik op het orgaan waar de pil de eisprong tegenhoudt.",
        VS.bestand, ZVS["A"],
        "De pil remt LH en FSH, zodat in de eierstok geen follikel openbarst.",
    ),
    met_prent(VS.bestand, tabel(
        "Waar werkt dit middel? Kijk naar de letters.",
        [
            ("sterilisatie van de vrouw", "B"),
            ("pessarium", "D"),
            ("vrouwencondoom", "E"),
            ("hormoonspiraal", "C"),
        ],
        "Bij sterilisatie worden de eileiders afgesloten. Het pessarium sluit de baarmoederhals af.",
        kolommen=["B", "C", "D", "E"],
    )),
    klik(
        "Klik op de stap waarbij de eicellen bevrucht worden.",
        IV.bestand, ZIV["R"],
        "Eicel en zaadcellen komen samen in een schaaltje: in vitro.",
    ),
    met_prent(IV.bestand, tabel(
        "Kijk naar de vier stappen van IVF. Klopt dit?",
        [
            ("In P rijpen door hormonen meerdere follikels tegelijk.", J),
            ("In Q worden de eicellen met een naald opgezogen.", J),
            ("Bij ICSI verandert vooral stap R.", J),
            ("In S wordt sperma in de baarmoeder gespoten.", F),
        ],
        "In S wordt een embryo teruggeplaatst. Sperma in de baarmoeder brengen is inseminatie.",
    )),
    sorteer(
        "Hoe werkt dit middel vooral?",
        ["Houdt de eisprong tegen", "Houdt zaadcellen tegen", "Verhindert de innesteling"],
        [
            ("combinatiepil", "Houdt de eisprong tegen"),
            ("prikpil", "Houdt de eisprong tegen"),
            ("mannencondoom", "Houdt zaadcellen tegen"),
            ("pessarium", "Houdt zaadcellen tegen"),
            ("koperspiraal", "Verhindert de innesteling"),
        ],
        "Koper maakt het baarmoederslijmvlies ongeschikt voor innesteling en is ook slecht voor zaadcellen.",
    ),
    tabel(
        "Beschermt dit middel ook tegen soa's?",
        [
            ("vrouwencondoom", J),
            ("vaginale ring", F),
            ("hormoonimplantaat", F),
            ("mannencondoom", J),
        ],
        "Alleen een condoom houdt ook bacteriën en virussen tegen.",
    ),
    casus(
        "Lotte (17) neemt de combinatiepil. Na een weekend met braken en diarree vraagt ze zich af of ze nog beschermd is.",
        [
            keuze(
                "Bij braken kort na de inname wordt de pil mogelijk [[*niet opgenomen|sneller opgenomen|dubbel opgenomen]].",
                "Dan komt het hormoon niet in het bloed.",
            ),
            tabel(
                "Wat is een goed advies voor Lotte?",
                [
                    ("Gebruik de komende dagen ook een condoom.", J),
                    ("Lees de bijsluiter of vraag het aan de apotheker.", J),
                    ("Stop meteen helemaal met de pil.", F),
                ],
                "Een extra barrièremiddel geeft zekerheid tot de pil weer betrouwbaar is.",
            ),
            mk(
                "Waarom is een pil die Lotte vergeet gevaarlijker dan een prikpil die ze een dag te laat haalt?",
                [
                    "De pil werkt kort en moet elke dag aangevuld",
                    "De prikpil bevat veel meer oestrogeen dan elke soort pil",
                    "Een prikpil houdt naast zwangerschap ook alle soa's tegen",
                    "De pil werkt pas na drie volle maanden",
                ],
                0,
                "Een prik werkt weken lang, een pil maar ongeveer een dag.",
            ),
        ],
    ),
    tabel(
        "Ingreep bij de man of bij de vrouw?",
        [
            ("de zaadleiders doorknippen", "Man"),
            ("de eileiders afsluiten", "Vrouw"),
            ("een spiraaltje plaatsen", "Vrouw"),
            ("vasectomie", "Man"),
        ],
        "Vasectomie is de sterilisatie van de man.",
        kolommen=["Man", "Vrouw"],
    ),
    mk(
        "Een koppel gebruikt alleen de kalendermethode. Waarom raadt een arts dat af als zwangerschap echt vermeden moet worden?",
        [
            "Een cyclus kan door ziekte of stress verschuiven",
            "De kalendermethode werkt alleen samen met de pil",
            "De kalendermethode beschermt enkel tegen soa's",
            "De eisprong valt altijd op dezelfde dag",
        ],
        0,
        "Daardoor verschuiven ook de vruchtbare dagen.",
    ),
    tabel(
        "Welke methode spoort de vruchtbare dagen op met dit kenmerk?",
        [
            ("de lichaamstemperatuur stijgt licht na de eisprong", "Temperatuurmethode"),
            ("het slijm in de baarmoederhals wordt helder en rekbaar", "Ovulatiemethode"),
            ("de vruchtbare dagen worden berekend uit vorige cycli", "Kalendermethode"),
            ("elke ochtend voor het opstaan meten", "Temperatuurmethode"),
        ],
        "Bij de ovulatiemethode let men op het slijm van de baarmoederhals.",
        kolommen=["Temperatuurmethode", "Ovulatiemethode", "Kalendermethode"],
    ),
    koppel(
        "Koppel elke vruchtbaarheidsbehandeling aan wat er gebeurt.",
        [
            ("KI", "sperma van de partner in de baarmoeder brengen"),
            ("KID", "sperma van een donor in de baarmoeder brengen"),
            ("ICSI", "één zaadcel in de eicel spuiten"),
            ("IVM", "onrijpe eicellen in het labo laten rijpen"),
        ],
        ["een eicel invriezen zonder ze te bevruchten"],
        "Bij IVM rijpen de eicellen pas buiten het lichaam verder.",
    ),
    volgorde(
        "Zet de stappen van een IVF-behandeling in volgorde.",
        ["Hormonale stimulatie van de eierstokken", "Eicellen aanprikken", "Bevruchting in het labo", "Embryo terugplaatsen", "Zwangerschapstest"],
        "Eerst rijpen er meerdere follikels, pas daarna kunnen de eicellen opgehaald worden.",
    ),
    mk(
        "Een man heeft weinig en traag bewegende zaadcellen. Welke behandeling ligt dan het meest voor de hand?",
        [
            "ICSI, één zaadcel wordt in de eicel gespoten",
            "Eiceldonatie, met een eicel van een andere vrouw",
            "De morning-afterpil, door de vrouw kort na de eisprong genomen",
            "Een koperspiraal, die de innesteling verbetert",
        ],
        0,
        "De zaadcel hoeft de eicel dan niet zelf te bereiken en binnen te dringen.",
    ),
    tabel(
        "Klopt dit over de morning-afterpil?",
        [
            ("Ze werkt beter naarmate ze sneller genomen wordt.", J),
            ("Ze stelt vooral de eisprong uit.", J),
            ("Ze beëindigt een zwangerschap die al loopt.", F),
            ("Ze is geen middel om elke week te gebruiken.", J),
        ],
        "Een lopende zwangerschap beëindigen doet de abortuspil, niet de morning-afterpil.",
    ),
    sleep(
        "De combinatiepil bevat [[oestrogeen]] en [[progestageen]]. Daardoor blijft het hormoonpeil hoog en remt de hypofyse de afgifte van [[LH]], zodat er geen eisprong komt.",
        ["testosteron", "insuline", "adrenaline"],
        "Een hoog peil van eierstokhormonen remt de hypofyse: negatieve terugkoppeling.",
    ),
    tabel(
        "Klopt dit over een vasectomie?",
        [
            ("De man maakt nog zaadcellen aan.", J),
            ("De zaadcellen komen niet meer in het sperma.", J),
            ("De man maakt nog testosteron.", J),
            ("Er komt geen sperma meer vrij bij een zaadlozing.", F),
        ],
        "Het sperma bevat dan wel vocht van de klieren, maar geen zaadcellen.",
    ),
    keuze(
        "De teelballen liggen buiten de buikholte omdat de spermatogenese het best verloopt bij een [[*iets lagere|iets hogere|sterk wisselende]] temperatuur.",
        "Enkele graden onder de lichaamstemperatuur.",
    ),
    tabel(
        "Verlaagt dit de vruchtbaarheid?",
        [
            ("roken", J),
            ("ernstig overgewicht", J),
            ("chemotherapie", J),
            ("matig bewegen", F),
            ("langdurige stress", J),
        ],
        "Stress werkt in op de hypothalamus en de hypofyse en kan de ovulatie verstoren.",
    ),
    mk(
        "Waarom kan een vrouw voor een chemotherapie eicellen laten invriezen?",
        [
            "De kuur treft ook snel delende geslachtscellen",
            "De eicellen worden na de kuur vanzelf sterker",
            "Chemotherapie verhoogt het aantal follikels sterk",
            "Ingevroren eicellen hebben geen zaadcel meer nodig",
        ],
        0,
        "Zo kan ze later toch nog een kind krijgen met haar eigen eicellen.",
    ),
    tabel(
        "Waarom kan dit de vruchtbaarheid verlagen?",
        [
            ("pesticiden en zware metalen", "Stoort hormonen of geslachtscellen"),
            ("een kankerbehandeling", "Stoort hormonen of geslachtscellen"),
            ("een afgesloten eileider", "Blokkeert de weg"),
            ("doorgeknipte zaadleiders", "Blokkeert de weg"),
        ],
        "Een afgesloten eileider of zaadleider laat eicel en zaadcel niet bij elkaar komen.",
        kolommen=["Stoort hormonen of geslachtscellen", "Blokkeert de weg"],
    ),
    inv(
        "Bij een IVF worden 9 eicellen opgehaald. Twee derde ervan wordt bevrucht. Hoeveel eicellen zijn dat?",
        ["6", "zes"],
        "9 x 2/3 = 6.",
    ),
    mk(
        "Een koppel krijgt na IVF vijf goede embryo's. Waarom plaatst men er maar één terug?",
        [
            "Een meerling is riskanter voor moeder en kind",
            "De baarmoeder kan maar één embryo per jaar dragen",
            "Embryo's kunnen nooit veilig ingevroren worden",
            "Twee embryo's stoten elkaar in de baarmoeder altijd af",
        ],
        0,
        "De andere embryo's worden ingevroren voor een volgende poging.",
    ),
    tabel(
        "Wanneer komt deze behandeling in beeld?",
        [
            ("de vrouw heeft geen bruikbare eicellen", "Eiceldonatie"),
            ("de man heeft geen bruikbare zaadcellen", "KID"),
            ("de eileiders van de vrouw zijn afgesloten", "IVF"),
            ("de vrouw maakt zelf geen eicellen meer aan", "Eiceldonatie"),
        ],
        "Bij afgesloten eileiders omzeilt IVF de weg door de eileider.",
        kolommen=["Eiceldonatie", "KID", "IVF"],
    ),
    keuze(
        "Stoffen uit het milieu die op hormonen lijken en zo de voortplanting kunnen storen, heten [[*hormoonverstoorders|mutagenen|antistoffen]].",
        "Ze binden op dezelfde receptoren als echte hormonen.",
    ),
    mk(
        "Waarom wordt een zaaddodend middel nooit alleen aangeraden?",
        [
            "Alleen gebruikt is het te weinig betrouwbaar",
            "Het werkt enkel bij mannen met een vasectomie",
            "Het houdt de eisprong volledig tegen",
            "Het moet altijd door een arts geplaatst worden",
        ],
        0,
        "Samen met een barrièremiddel zoals een pessarium wordt het wel gebruikt.",
    ),
    tabel(
        "Klopt dit over het koperspiraal en het hormoonspiraal?",
        [
            ("Het koperspiraal werkt zonder hormonen.", J),
            ("Beide worden door een arts geplaatst.", J),
            ("Het hormoonspiraal geeft ook een progestageen af.", J),
            ("Beide beschermen tegen soa's.", F),
        ],
        "Een spiraaltje zit in de baarmoeder en houdt geen bacteriën of virussen tegen.",
    ),
    open_(
        "Leg uit waarom een hormoonimplantaat of prikpil betrouwbaarder kan zijn dan de pil, terwijl ze met dezelfde soort hormonen werken.",
        "Bij de pil hangt de betrouwbaarheid af van het juiste gebruik: elke dag nemen, niet vergeten, niet braken. Een implantaat of prikpil geeft weken of jaren lang hormonen af zonder dat iemand iets moet doen. Fouten bij het gebruik vallen weg, dus is de betrouwbaarheid in de praktijk hoger.",
    ),
]
