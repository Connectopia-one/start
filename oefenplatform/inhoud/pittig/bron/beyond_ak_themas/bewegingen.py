"""De bewegingen van de aarde — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Aardbaan met vier standen ---------------------------------------------
AB = Prent("aardbaan-vier-standen", "De aarde in vier standen rond de zon (niet op schaal)", "ellipsvormige baan met vier standen A tot D; de aardas helt altijd naar dezelfde kant")
CX, CY, RX, RY = 500, 340, 360, 190
AB.ellips(CX, CY, RX, RY, "none", GRIJS, 2)
AB.cirkel(CX, CY, 45, "#f4a259", DONKER)
STAND = {"A": (CX - RX, CY), "B": (CX, CY + RY), "C": (CX + RX, CY), "D": (CX, CY - RY)}
helling = math.radians(23.5)
for k, (x, y) in STAND.items():
    AB.cirkel(x, y, 32, "#9bc1df", DONKER)
    # nacht-kant: helft weg van de zon
    dx, dy = x - CX, y - CY
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    px, py = -uy, ux
    AB.pad(f"M{x + 32 * px:.0f} {y + 32 * py:.0f} A 32 32 0 0 0 {x - 32 * px:.0f} {y - 32 * py:.0f} Z", "#2c3e50", "none")
    ax, ay = 48 * math.sin(helling), -48 * math.cos(helling)
    AB.lijn(x - ax, y - ay, x + ax, y + ay, DONKER, 3)
    AB.tekst(x + ax + 6, y + ay - 4, "N", 15, "start")
LP = {"A": (CX - RX - 70, CY - 50), "B": (CX + 70, CY + RY + 30), "C": (CX + RX + 70, CY - 50), "D": (CX + 70, CY - RY - 40)}
for k, (x, y) in LP.items():
    AB.letter(x, y, k)
ZAB = {k: [Prent.rond(*STAND[k], 42), Prent.rond(*LP[k], 26)] for k in STAND}

# Dagbogen te Brussel ----------------------------------------------------
DB = Prent("dagbogen-brussel", "De middaghoogte van de zon op 51° NB", "horizon met drie dagbogen P, Q en R")
HY = 520
DB.lijn(60, HY, 940, HY, DONKER, 3)
DB.tekst(500, HY + 32, "zuid", 18)
DB.tekst(110, HY + 32, "oost", 18)
DB.tekst(890, HY + 32, "west", 18)
def boog(hoogte, breed, kleur):
    top = HY - math.tan(math.radians(hoogte)) * 300 * 0.55
    DB.pad(f"M{500 - breed} {HY} Q 500 {2 * top - HY:.0f} {500 + breed} {HY}", "none", kleur, 4)
    return top
TOP = {"P": boog(62.5, 420, ORANJE), "Q": boog(39, 330, GROEN), "R": boog(15.5, 220, BLAUW)}
for k, t in TOP.items():
    DB.cirkel(500, t, 14, "#f4c542", DONKER)
    DB.letter(560, t - 10, k)
ZDB = {k: [Prent.rond(500, t, 30), Prent.rond(560, t - 10, 26)] for k, t in TOP.items()}

VRAGEN = [
    klik(
        "Klik op de stand van de aarde op 21 juni.",
        AB.bestand, ZAB["A"],
        "De noordpool helt dan naar de zon toe: zomerzonnewende op het noordelijk halfrond.",
    ),
    klik(
        "Klik op de stand van de aarde op 22 december.",
        AB.bestand, ZAB["C"],
        "De noordpool helt dan van de zon weg.",
    ),
    met_prent(AB.bestand, tabel(
        "Kijk naar de baan. Klopt dit?",
        [
            ("In B en D staat de zon zenitaal boven de evenaar.", J),
            ("De aardas helt in alle standen naar dezelfde kant.", J),
            ("In stand A heeft de noordpool poolnacht.", F),
            ("De seizoenen komen van de afstand tot de zon.", F),
        ],
        "Bij A helt de noordpool naar de zon: pooldag. Seizoenen komen van de scheve as.",
    )),
    met_prent(AB.bestand, keuze(
        "In stand C heeft het zuidelijk halfrond [[*zomer|winter|lente]].",
        "Als de noordpool van de zon weg helt, krijgt het zuiden de zon het hoogst.",
    )),
    klik(
        "Klik op de dagboog van 22 december.",
        DB.bestand, ZDB["R"],
        "De laagste en kortste boog: middaghoogte ongeveer 15,5°.",
    ),
    klik(
        "Klik op de dagboog van een equinox.",
        DB.bestand, ZDB["Q"],
        "Op 21 maart en 23 september is de middaghoogte 90° - 51° = 39°.",
    ),
    met_prent(DB.bestand, tabel(
        "Kijk naar de dagbogen. Welke middaghoogte hoort erbij?",
        [
            ("P", "62,5°"),
            ("Q", "39°"),
            ("R", "15,5°"),
        ],
        "90° - 51° plus of min 23,5°.",
        kolommen=["15,5°", "39°", "62,5°", "90°"],
    )),
    met_prent(DB.bestand, tabel(
        "Kijk naar de dagbogen. Klopt dit?",
        [
            ("Bij P is de dag het langst.", J),
            ("De zon staat 's middags altijd in het zuiden.", J),
            ("In België staat de zon op 21 juni zenitaal.", F),
            ("Bij R gaat de zon het verst noordelijk op.", F),
        ],
        "In België kan de zon nooit zenitaal staan. In de winter komt ze zuidoostelijk op.",
    )),
    tabel(
        "Gevolg van de rotatie of van de revolutie met schuine as?",
        [
            ("dag en nacht", "Rotatie"),
            ("de seizoenen", "Revolutie"),
            ("het corioliseffect", "Rotatie"),
            ("een daglengte die door het jaar verandert", "Revolutie"),
            ("de afplatting van de aarde", "Rotatie"),
        ],
        "Draaien om de as of draaien rond de zon.",
        kolommen=["Rotatie", "Revolutie"],
    ),
    inv(
        "Het is 12 uur zonnetijd op 0°. Hoe laat is het zonnetijd op 60° oosterlengte?",
        ["16", "16 uur", "16u"],
        "60 : 15 = 4 uur later.",
    ),
    inv(
        "Het is 12 uur zonnetijd op 0°. Hoe laat is het zonnetijd op 30° westerlengte?",
        ["10", "10 uur", "10u"],
        "30 : 15 = 2 uur vroeger.",
    ),
    inv(
        "Hoeveel minuten verschilt de zonnetijd tussen twee plaatsen die 1° lengte uit elkaar liggen?",
        ["4"],
        "15° per uur, dus 60 : 15 = 4 minuten per graad.",
    ),
    tabel(
        "Waar of wanneer is dit zo?",
        [
            ("de omtreksnelheid door de rotatie het grootst", "Op de evenaar"),
            ("het corioliseffect zo goed als nul", "Op de evenaar"),
            ("een half jaar poolnacht", "Op de pool"),
            ("de zon recht boven je op 21 juni", "Op de Kreeftskeerkring"),
        ],
        "Rotatie en revolutie geven op elke breedte een ander effect.",
        kolommen=["Op de evenaar", "Op de pool", "Op de Kreeftskeerkring"],
    ),
    keuze(
        "Op het noordelijk halfrond buigt een wind door het corioliseffect naar [[*rechts|links|boven]] af.",
        "Op het zuidelijk halfrond naar links.",
    ),
    casus(
        "Jana vliegt op maandag 10 juni van Tokio naar Hawaï. Ze steekt de datumgrens oostwaarts over.",
        [
            keuze(
                "Bij aankomst is het in Hawaï [[*zondag 9 juni|dinsdag 11 juni|nog altijd maandag 10 juni, maar een dag later]] als ze kort na middernacht de grens kruist.",
                "Oostwaarts over de datumgrens ga je een dag terug.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("De datumgrens volgt ruwweg de 180ste meridiaan.", J),
                    ("Westwaarts over de grens sla je een dag over.", J),
                    ("De datumgrens loopt overal kaarsrecht.", F),
                ],
                "Ze buigt om eilandengroepen heen.",
            ),
        ],
    ),
    tabel(
        "Zomertijd of wintertijd?",
        [
            ("de klok gaat een uur vooruit", "Zomertijd"),
            ("de avonden blijven langer licht", "Zomertijd"),
            ("de klok staat dichter bij de zonnetijd van België", "Wintertijd"),
        ],
        "Bij zomertijd gebruik je de tijd van de uurgordel oostwaarts.",
        kolommen=["Zomertijd", "Wintertijd"],
    ),
    mk(
        "Waarom is de aarde aan de evenaar wat breder dan van pool tot pool?",
        [
            "De middelpuntvliedende kracht door de rotatie is daar het grootst",
            "De zon trekt de evenaar het hele jaar door een beetje naar zich toe",
            "De oceanen zijn aan de evenaar veel dieper dan bij de polen",
            "De revolutie rond de zon duwt het midden van de aarde naar buiten",
        ],
        0,
        "Daardoor is de straal aan de evenaar ongeveer 21 km groter.",
    ),
    tabel(
        "Perihelium of aphelium?",
        [
            ("begin januari", "Perihelium"),
            ("begin juli", "Aphelium"),
            ("de aarde staat het dichtst bij de zon", "Perihelium"),
            ("de aarde staat het verst van de zon", "Aphelium"),
        ],
        "Onze winter valt in het perihelium: afstand bepaalt de seizoenen dus niet.",
        kolommen=["Perihelium", "Aphelium"],
    ),
    inv(
        "Hoe hoog staat de zon 's middags op 21 juni op de Kreeftskeerkring, in graden?",
        ["90"],
        "Op 21 juni staat de zon zenitaal boven de Kreeftskeerkring.",
    ),
    inv(
        "Je staat op 40° noorderbreedte. Hoe hoog staat de zon er 's middags op 23 september, in graden?",
        ["50"],
        "Op een equinox: 90° - 40° = 50°.",
    ),
    inv(
        "Je staat op 40° noorderbreedte. Hoe hoog staat de zon er 's middags op 22 december, in graden?",
        ["26,5", "26.5"],
        "90° - 40° - 23,5° = 26,5°.",
    ),
    tabel(
        "Klopt dit over schrikkeljaren?",
        [
            ("Een jaar duurt bijna een kwart dag langer dan 365 dagen.", J),
            ("Elke vier jaar steek je een dag bij.", J),
            ("Zonder schrikkeldag zou 21 juni langzaam wegschuiven van de langste dag.", J),
            ("Een schrikkeldag maakt de aardrevolutie sneller.", F),
        ],
        "De kalender past zich aan, niet de aarde.",
    ),
    sleep(
        "De aardas helt ongeveer [[23,5]] graden ten opzichte van de loodlijn op het eclipticavlak. Daardoor staat de zon op 21 juni zenitaal boven de [[Kreeftskeerkring]] en op 22 december boven de [[Steenbokskeerkring]].",
        ["evenaar", "66,5", "poolcirkel"],
        "De scheve as geeft de seizoenen.",
    ),
    tabel(
        "Klopt dit over de slingerproef van Foucault?",
        [
            ("De slinger blijft in hetzelfde vlak zwaaien.", J),
            ("De vloer draait mee met de aarde.", J),
            ("De proef bewijst de rotatie van de aarde.", J),
            ("De slinger wordt door de zon opzij geduwd.", F),
        ],
        "Het slingervlak lijkt te draaien omdat de aarde eronder draait.",
    ),
    met_prent(AB.bestand, tabel(
        "Kijk naar de baan. Welke datum hoort bij welke stand?",
        [
            ("21 juni", "A"),
            ("22 december", "C"),
            ("21 maart en 23 september", "B of D"),
        ],
        "Op de equinoxen helt de as noch naar de zon, noch ervan weg.",
        kolommen=["A", "B of D", "C"],
    )),
    tabel(
        "Klopt dit over de pooldag?",
        [
            ("Binnen de poolcirkel blijft de zon dan 's nachts boven de horizon.", J),
            ("Op de pool zelf duurt hij een half jaar.", J),
            ("Op de poolcirkel duurt hij een half jaar.", F),
        ],
        "Op de poolcirkel is het maar één dag middernachtzon.",
    ),
    inv(
        "Hoeveel uurgordels zijn er rond de aarde, als je 15° per gordel rekent?",
        ["24"],
        "360 : 15 = 24.",
    ),
    keuze(
        "De aarde draait van [[*west naar oost|oost naar west|noord naar zuid]], en daarom komt de zon in het oosten op.",
        "De aarde draait met ons naar het oosten toe.",
    ),
    open_(
        "Leg uit waarom het op de evenaar het hele jaar ongeveer twaalf uur licht is.",
        "De grens tussen dag en nacht snijdt de evenaar altijd precies doormidden, ook al helt de aardas. Daardoor ligt de helft van de evenaar altijd in het licht en draait elke plaats er twaalf uur door de dag en twaalf uur door de nacht.",
    ),
]
