"""Niet-specifieke en specifieke afweer — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Immuunrespons ----------------------------------------------------------
IR = Prent("immuunrespons-twee", "Antilichamen in het bloed na twee contacten met hetzelfde antigeen", "grafiek over 60 dagen: kleine trage piek na dag 0, grote snelle piek na dag 30; punten K, L en M")
X, Y = assen(IR, 0, 60, 0, 100, "dagen", "antilichamen", 10, 25, links=140, rechts=900)
def curve(t):
    a = 18 * math.exp(-((t - 14) / 5) ** 2)
    if t > 28:
        a += 95 * math.exp(-((t - 37) / (3.5 if t < 37 else 12)) ** 2)
    return a
pts = [f"{X(t / 4):.1f} {Y(curve(t / 4)):.1f}" for t in range(0, 241)]
IR.pad("M" + " L ".join(pts), "none", PAARS, 4)
for d in (0, 30):
    IR.pijl(X(d), Y(100) - 10, X(d), Y(80), ROOD, 3)
IR.tekst(X(0) + 10, Y(80) + 4, "contact 1", 14, "start", kleur=ROOD)
IR.tekst(X(30) - 10, Y(80) + 4, "contact 2", 14, "end", kleur=ROOD)
LIR = {"K": (14, curve(14)), "L": (37, curve(37)), "M": (5, 0)}
OFF = {"K": (0, -36), "L": (40, 0), "M": (0, -36)}
for k, (t, a) in LIR.items():
    IR.cirkel(X(t), Y(a), 6, ORANJE, DONKER, 1)
    IR.letter(X(t) + OFF[k][0], Y(a) + OFF[k][1], k)
ZIR = {k: [Prent.rond(X(t), Y(a), 18), Prent.rond(X(t) + OFF[k][0], Y(a) + OFF[k][1], 22)] for k, (t, a) in LIR.items()}

# Antilichaam ------------------------------------------------------------
AL = Prent("antilichaam-y", "Een antilichaam bindt antigenen", "Y-vormig eiwit; P de uiteinden van de armen, Q de steel; links en rechts deeltjes met antigenen")
def arm(x1, y1, x2, y2, kl):
    AL.lijn(x1, y1, x2, y2, kl, 22)
arm(500, 380, 500, 540, "#6a8cbf")
arm(500, 380, 390, 250, "#6a8cbf")
arm(500, 380, 610, 250, "#6a8cbf")
arm(390, 250, 360, 215, "#e0a84a")
arm(610, 250, 640, 215, "#e0a84a")
for cx in (285, 715):
    AL.cirkel(cx, 150, 70, "#cfe3b4", DONKER, 2)
AL.pad("M330 205 l 25 -10 l -5 25 Z", ROOD, DONKER, 1)
AL.pad("M670 205 l -25 -10 l 5 25 Z", ROOD, DONKER, 1)
LAL = {"P": (300, 290), "Q": (580, 500)}
AL.lijn(325, 275, 355, 230, DONKER, 1)
AL.lijn(558, 490, 515, 470, DONKER, 1)
for k, (x, y) in LAL.items():
    AL.letter(x, y, k)
ZAL = {"P": [Prent.rond(365, 220, 30), Prent.rond(635, 220, 30), Prent.rond(*LAL["P"], 24)],
       "Q": [Prent.zone(485, 380, 30, 170), Prent.rond(*LAL["Q"], 24)]}

VRAGEN = [
    klik(
        "Klik op de piek van de secundaire immuunrespons.",
        IR.bestand, ZIR["L"],
        "Na het tweede contact: sneller, hoger en langer.",
    ),
    met_prent(IR.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("Na contact 1 duurt het meer dan een week voor de piek komt.", J),
            ("Na contact 2 komen er veel meer antilichamen.", J),
            ("Bij M zijn er nog bijna geen antilichamen.", J),
            ("Na contact 2 duurt het langer dan na contact 1.", F),
        ],
        "Geheugencellen maken de tweede reactie snel.",
    )),
    met_prent(IR.bestand, mk(
        "Kijk naar de grafiek. Waarom is piek L zoveel hoger dan piek K?",
        [
            "Er waren al geheugencellen",
            "Het antigeen was bij het tweede contact anders",
            "De macrofagen maakten deze keer antilichamen",
            "Na 30 dagen werkt het beenmerg altijd harder",
        ],
        0,
        "Die delen zich snel tot plasmacellen.",
    )),
    klik(
        "Klik op de plaatsen waar het antigeen bindt.",
        AL.bestand, ZAL["P"],
        "De uiteinden van de armen verschillen van antilichaam tot antilichaam.",
    ),
    met_prent(AL.bestand, tabel(
        "Kijk naar het antilichaam. Klopt dit?",
        [
            ("Eén antilichaam kan twee antigenen tegelijk binden.", J),
            ("Zo kunnen deeltjes samenklonteren.", J),
            ("Q past op het antigeen.", F),
            ("Het antilichaam werd gemaakt door een plasmacel.", J),
        ],
        "Samenklonteren heet agglutinatie.",
    )),
    tabel(
        "Barrière, niet-specifieke of specifieke afweer?",
        [
            ("opperhuid", "Barrière"),
            ("macrofaag", "Niet-specifiek"),
            ("plasmacel", "Specifiek"),
            ("lysozym in tranen", "Barrière"),
            ("cytotoxische T-lymfocyt", "Specifiek"),
            ("natural killer cel", "Niet-specifiek"),
        ],
        "Drie lijnen van verdediging.",
        kolommen=["Barrière", "Niet-specifiek", "Specifiek"],
    ),
    koppel(
        "Koppel elke afweercel aan haar taak.",
        [
            ("T-helperlymfocyt", "zet andere afweercellen aan met cytokines"),
            ("cytotoxische T-lymfocyt", "doodt besmette eigen cellen"),
            ("plasmacel", "maakt antilichamen"),
            ("dendritische cel", "toont een stukje antigeen aan de lymfocyten"),
            ("mestcel", "zet histamine vrij"),
        ],
        ["maakt rode bloedcellen"],
        "Rode bloedcellen zijn geen afweercellen.",
    ),
    tabel(
        "Klopt dit over een ontsteking?",
        [
            ("Er stroomt meer bloed naar de plek.", J),
            ("Ze geeft roodheid, warmte, zwelling en pijn.", J),
            ("De CRP-waarde in het bloed stijgt.", J),
            ("Een ontsteking betekent altijd dat er bacteriën zijn.", F),
        ],
        "Ook een wonde of een verstuiking geeft een ontsteking.",
    ),
    casus(
        "Lars heeft een snee in zijn vinger. Na een dag is de plek rood, warm en gezwollen, en er zit wat pus in.",
        [
            keuze(
                "De eerste fagocyten die in grote aantallen komen, zijn [[*neutrofielen|plasmacellen|rode bloedcellen]].",
                "De talrijkste granulocyten.",
            ),
            keuze(
                "Pus bestaat vooral uit [[*dode witte bloedcellen en bacteriën|antilichamen en lymfe|vet en bloedplaatjes]].",
                "Het slagveld van de afweer.",
            ),
            tabel(
                "Klopt dit over wat er gebeurt?",
                [
                    ("De huid als barrière is doorbroken.", J),
                    ("De niet-specifieke afweer reageert als eerste.", J),
                    ("Lars krijgt meteen antilichamen van zijn moeder.", F),
                ],
                "De specifieke afweer komt pas later op gang.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van de specifieke afweer in volgorde.",
        [
            "Een dendritische cel neemt de indringer op",
            "Ze toont een stukje antigeen aan een T-helpercel",
            "De T-helpercel zet B-lymfocyten aan",
            "B-lymfocyten worden plasmacellen en maken antilichamen",
        ],
        "Er blijven ook geheugencellen achter.",
    ),
    mk(
        "Waarom duurt de primaire immuunrespons enkele dagen?",
        [
            "De passende lymfocyt moet zich eerst delen",
            "De indringer moet eerst helemaal door de huid geraken",
            "Antilichamen moeten eerst uit de lever komen",
            "De thymus moet eerst groeien voor ze werkt",
        ],
        0,
        "Maar één lymfocyt op miljoenen past op dat ene antigeen.",
    ),
    tabel(
        "Waar gebeurt het?",
        [
            ("alle bloedcellen worden aangemaakt", "beenmerg"),
            ("T-lymfocyten rijpen", "thymus"),
            ("lymfe wordt gefilterd", "lymfeknoop"),
            ("bloed wordt gefilterd en oude rode bloedcellen afgebroken", "milt"),
        ],
        "Samen het lymfatisch systeem.",
        kolommen=["beenmerg", "thymus", "lymfeknoop", "milt"],
    ),
    sleep(
        "Een cel die door een virus besmet is, waarschuwt haar buren met [[interferonen]]. Een [[cytotoxische T-lymfocyt]] herkent het antigeen op een [[MHC-I]]-eiwit en doodt de cel.",
        ["histamine", "plasmacel", "MHC-II"],
        "MHC-I staat op bijna elke cel.",
    ),
    tabel(
        "MHC-I of MHC-II?",
        [
            ("staat op bijna elke lichaamscel", "MHC-I"),
            ("staat enkel op afweercellen die antigeen tonen", "MHC-II"),
            ("toont wat er in de cel gebeurt", "MHC-I"),
            ("toont een stuk van een opgegeten indringer", "MHC-II"),
        ],
        "Twee soorten etalages.",
        kolommen=["MHC-I", "MHC-II"],
    ),
    mk(
        "Waarom kan koorts helpen bij een infectie?",
        [
            "De afweer werkt sneller en de indringer trager",
            "De hitte doodt meteen alle bacteriën in het bloed",
            "Koorts maakt nieuwe antilichamen zonder lymfocyten",
            "Bij koorts maakt de huid extra lysozym aan",
        ],
        0,
        "Veel ziekteverwekkers groeien het best bij 37 °C.",
    ),
    tabel(
        "Klopt dit over het microbioom?",
        [
            ("Het zijn onschadelijke micro-organismen op en in ons lichaam.", J),
            ("Ze nemen plaats en voedsel in van ziekteverwekkers.", J),
            ("Een antibioticakuur kan het verstoren.", J),
            ("Het microbioom is altijd schadelijk.", F),
        ],
        "Het werkt mee als een barrière.",
    ),
    keuze(
        "Het samenklonteren van antigenen door antilichamen heet [[*agglutinatie|fagocytose|incubatie]].",
        "Klonten zijn makkelijk op te ruimen.",
    ),
    tabel(
        "Klopt dit over geheugencellen?",
        [
            ("Ze blijven jaren in het lichaam.", J),
            ("Ze reageren snel bij een nieuw contact.", J),
            ("Ze maken onafgebroken antilichamen.", F),
        ],
        "Ze wachten tot het antigeen terugkomt.",
    ),
    mk(
        "Iemand heeft antilichamen tegen een virus in het bloed, maar het virus zelf is niet te vinden. Wat is de beste verklaring?",
        [
            "Hij had het virus of is ertegen gevaccineerd",
            "Hij is nu zwaar ziek door dat virus",
            "Zijn bloed maakt antilichamen zonder enige reden",
            "Het virus zit verstopt in zijn rode bloedcellen",
        ],
        0,
        "Antilichamen zijn sporen van een eerdere ontmoeting.",
    ),
    tabel(
        "Infectie of infectieziekte?",
        [
            ("een pathogeen dringt binnen en vermenigvuldigt zich", "Infectie"),
            ("er zijn klachten zoals koorts", "Infectieziekte"),
            ("iemand draagt het virus zonder ziek te zijn", "Infectie"),
        ],
        "Pas als er klachten zijn, spreek je van een ziekte.",
        kolommen=["Infectie", "Infectieziekte"],
    ),
    tabel(
        "Klopt dit over het complementsysteem?",
        [
            ("Het zijn eiwitten in het bloedplasma.", J),
            ("Ze kunnen het membraan van een bacterie doorboren.", J),
            ("Het zijn witte bloedcellen.", F),
        ],
        "Het hoort bij de niet-specifieke afweer.",
    ),
    inv(
        "Een bacterie deelt zich om de 20 minuten. Met hoeveel bacteriën zit je na 2 uur, als je met 1 begint?",
        ["64"],
        "2 uur = 6 delingen: 2 tot de zesde = 64.",
    ),
    keuze(
        "De tijd tussen de besmetting en de eerste klachten heet de [[*incubatietijd|immuunrespons|ontstekingsfase]].",
        "Intussen vermenigvuldigt de ziekteverwekker zich.",
    ),
    tabel(
        "Welk middel van de barrières is dit?",
        [
            ("dode verhoornde cellen", "fysisch"),
            ("maagzuur", "chemisch"),
            ("trilhaarepitheel dat slijm afvoert", "mechanisch"),
        ],
        "Een muur, een zuur of een bewegende afvoer.",
        kolommen=["fysisch", "chemisch", "mechanisch"],
    ),
    tabel(
        "Klopt dit over T-helpercellen?",
        [
            ("Ze herkennen het antigeen op MHC-II.", J),
            ("Ze zetten B- en T-lymfocyten aan.", J),
            ("Ze maken zelf antilichamen.", F),
        ],
        "Ze zijn de dirigent van de afweer.",
    ),
    tabel(
        "Klopt dit over histamine?",
        [
            ("Mestcellen zetten het vrij.", J),
            ("Het maakt bloedvaten wijder.", J),
            ("Het speelt een rol bij allergie.", J),
            ("Het is een antilichaam.", F),
        ],
        "Daarom nemen mensen met hooikoorts een antihistaminicum.",
    ),
    tabel(
        "Klopt dit over een antigeen?",
        [
            ("Het is meestal een eiwit of suikerketen.", J),
            ("Het immuunsysteem herkent het als vreemd.", J),
            ("Het wordt door plasmacellen gemaakt.", F),
        ],
        "Plasmacellen maken antilichamen, niet antigenen.",
    ),
    open_(
        "Leg uit waarom je de meeste kinderziekten maar één keer krijgt.",
        "Bij de eerste infectie maakt de specifieke afweer niet alleen plasmacellen, maar ook geheugencellen tegen dat antigeen. Komt dezelfde ziekteverwekker terug, dan reageren die geheugencellen meteen. De secundaire respons is zo snel en sterk dat je meestal niet meer ziek wordt.",
    ),
]
