"""Klimaat doorheen de geologische tijd — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Temperatuur uit een ijskern --------------------------------------------
IK = Prent("ijskern-temperatuur", "Temperatuur uit een ijskern, vergeleken met nu (vereenvoudigd)", "zaagtandcurve over 400 000 jaar met pieken om de ongeveer 100 000 jaar, punten A tot D")
LI, RE, BO, ON = 130, 920, 90, 520
def X(x):
    return LI + (x + 400) / 400 * (RE - LI)
def Y(y):
    return ON - (y + 10) / 14 * (ON - BO)
for x in range(-400, 1, 50):
    IK.lijn(X(x), BO, X(x), ON, "#e4e1d6", 1)
    IK.tekst(X(x), ON + 24, str(-x), 15)
for y in range(-10, 5, 2):
    IK.lijn(LI, Y(y), RE, Y(y), "#e4e1d6", 1)
    IK.tekst(LI - 10, Y(y) + 5, str(y).replace("-", "−"), 15, "end")
IK.lijn(LI, ON, RE, ON, DONKER, 2)
IK.lijn(LI, ON, LI, BO, DONKER, 2)
IK.tekst((LI + RE) / 2, ON + 52, "duizenden jaren geleden", 16)
IK.tekst(LI, BO - 14, "°C vergeleken met nu", 15, "start")
# toppen (warm) en dalen (koud)
KNOP = [(-400, -2), (-335, 2.5), (-250, -8.5), (-240, 1), (-150, -9), (-128, 1.0), (-110, -3), (-20, -9), (-11, 0.3), (0, 0.5)]
pts = []
for (x1, y1), (x2, y2) in zip(KNOP, KNOP[1:]):
    for i in range(20):
        t = i / 20
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t + 0.6 * math.sin(x * 0.9)
        pts.append(f"{X(x):.1f} {Y(y):.1f}")
pts.append(f"{X(0):.1f} {Y(0.5):.1f}")
IK.pad("M" + " L ".join(pts), "none", BLAUW, 3)
IK.lijn(X(-400), Y(0), X(0), Y(0), ROOD, 2, stippel=True)
LIK = {"A": (-335, 3.3), "B": (-150, -9.0), "C": (-20, -9.0), "D": (-8, 3.0)}
for k, (x, y) in LIK.items():
    IK.letter(X(x), Y(y), k)
ZIK = {k: [Prent.rond(X(x), Y(y), 30)] for k, (x, y) in LIK.items()}
ZIK["A"].append(Prent.zone(X(-345), Y(3), X(-325) - X(-345), Y(1) - Y(3)))
ZIK["C"].append(Prent.zone(X(-30), Y(-8), X(-10) - X(-30), Y(-10) - Y(-8)))

# Milanković -------------------------------------------------------------
MI = Prent("milankovic-drie", "Drie schommelingen van de aarde (sterk overdreven)", "drie vakken: P een uitgerekte baan rond de zon, Q een aardas die meer of minder schuin staat, R een as die een cirkel beschrijft als een tol")
for i, x0 in enumerate((40, 360, 680)):
    MI.rect(x0, 90, 280, 500, "#f7f4ea", DONKER, 12, 1)
# P: baan
MI.ellips(180, 330, 120, 70, "none", DONKER, 2)
MI.ellips(180, 330, 110, 100, "none", GRIJS, 1)
MI.cirkel(150, 330, 16, GEEL, DONKER, 1)
MI.cirkel(300, 330, 9, BLAUW, DONKER, 1)
# Q: helling
MI.cirkel(500, 340, 60, BLAUW, DONKER, 2)
MI.lijn(500, 220, 500, 460, GRIJS, 2, stippel=True)
for hoek, kl in ((22, DONKER), (25, ROOD)):
    dx, dy = 130 * math.sin(math.radians(hoek)), 130 * math.cos(math.radians(hoek))
    MI.lijn(500 - dx, 340 + dy, 500 + dx, 340 - dy, kl, 3)
MI.tekst(560, 210, "22° tot 24,5°", 15)
# R: precessie
MI.cirkel(820, 380, 55, BLAUW, DONKER, 2)
MI.ellips(860, 200, 60, 18, "none", PAARS, 2)
MI.lijn(780, 480, 860, 200, DONKER, 3)
MI.pijl(905, 205, 900, 215, PAARS, 2)
LMI = {"P": (180, 140), "Q": (500, 140), "R": (820, 140)}
for k, (x, y) in LMI.items():
    MI.letter(x, y, k)
ZMI = {k: [Prent.zone(x0, 90, 280, 500)] for k, x0 in (("P", 40), ("Q", 360), ("R", 680))}

VRAGEN = [
    klik(
        "Klik op de laatste ijstijd.",
        IK.bestand, ZIK["C"],
        "Ongeveer 20 000 jaar geleden was het het koudst.",
    ),
    klik(
        "Klik op het warmste moment van de hele grafiek.",
        IK.bestand, ZIK["A"],
        "Rond 335 000 jaar geleden was het een paar graden warmer dan nu.",
    ),
    met_prent(IK.bestand, tabel(
        "Kijk naar de ijskerncurve. Klopt dit?",
        [
            ("Koude en warme fasen wisselen elkaar af.", J),
            ("Een volledige cyclus duurt ongeveer 100 000 jaar.", J),
            ("D ligt in het holoceen.", J),
            ("De warme fasen duren langer dan de koude.", F),
        ],
        "De koude fasen duren het langst; de warme pieken zijn kort.",
    )),
    met_prent(IK.bestand, mk(
        "Kijk naar de curve. Welke Milanković-cyclus past bij het ritme van de ijstijden?",
        [
            "De excentriciteit",
            "De obliquiteit van de aardas",
            "De precessie van de aardas",
            "De elfjarige zonnevlekkencyclus",
        ],
        0,
        "Die schommeling duurt ongeveer 100 000 jaar.",
    )),
    klik(
        "Klik op het vak dat de excentriciteit toont.",
        MI.bestand, ZMI["P"],
        "De baan wordt meer of minder uitgerekt.",
    ),
    klik(
        "Klik op het vak dat de obliquiteit toont.",
        MI.bestand, ZMI["Q"],
        "De aardas staat meer of minder schuin.",
    ),
    met_prent(MI.bestand, tabel(
        "Kijk naar de drie vakken. Klopt dit?",
        [
            ("R toont de precessie.", J),
            ("Bij R wijst de as na een tijd naar een andere ster.", J),
            ("Bij Q verandert de afstand tot de zon het meest.", F),
            ("Samen bepalen ze hoeveel zomerzon er op hoge breedte valt.", J),
        ],
        "Bij Q verandert de hoek, bij P de afstand.",
    )),
    tabel(
        "Welke bron vertelt ons wat?",
        [
            ("luchtbelletjes in een ijskern", "samenstelling van de lucht"),
            ("pollen in veen", "welke planten er groeiden"),
            ("jaarringen van bomen", "goede en slechte groeijaren"),
        ],
        "Elke bron is een archief van het klimaat.",
        kolommen=["samenstelling van de lucht", "welke planten er groeiden", "goede en slechte groeijaren"],
    ),
    volgorde(
        "Zet deze klimaatgebeurtenissen van oud naar jong.",
        [
            "Het PETM",
            "De laatste ijstijd",
            "De jonge dryas",
            "De kleine ijstijd",
        ],
        "56 miljoen jaar, 20 000 jaar, 12 000 jaar en enkele eeuwen geleden.",
    ),
    tabel(
        "Versterkende of afremmende terugkoppeling?",
        [
            ("smeltend zee-ijs maakt de oceaan donkerder", "Versterkend"),
            ("ontdooiende permafrost laat methaan vrij", "Versterkend"),
            ("meer CO2 laat planten sneller groeien", "Afremmend"),
            ("warmer water houdt minder CO2 vast", "Versterkend"),
        ],
        "Versterkend duwt verder in dezelfde richting.",
        kolommen=["Versterkend", "Afremmend"],
    ),
    casus(
        "Ongeveer 20 000 jaar geleden zat zoveel water vast in ijskappen dat de zeespiegel veel lager stond.",
        [
            inv(
                "Hoeveel meter lager stond de zeespiegel ongeveer? Geef een rond getal.",
                ["120"],
                "Ongeveer 120 m.",
            ),
            keuze(
                "De Noordzee lag toen grotendeels droog. Dat gebied heet [[*Doggersland|Gondwana|Pangea]].",
                "Er zijn botten van mammoeten opgevist.",
            ),
            tabel(
                "Klopt dit over die tijd?",
                [
                    ("Je kon te voet naar Engeland.", J),
                    ("In België lag een dikke ijskap.", F),
                    ("Er leefden mammoeten in onze streken.", J),
                ],
                "België was een koude, kale toendra.",
            ),
        ],
    ),
    mk(
        "Waarom maakt een continent op een pool een ijstijd waarschijnlijker?",
        [
            "Op land kan sneeuw zich jaar na jaar opstapelen",
            "Een continent trekt koude lucht uit de evenaar aan",
            "Op land valt er altijd meer neerslag dan op zee",
            "Een continent blokkeert het zonlicht van de pool",
        ],
        0,
        "Op open zee drijft het ijs weg en smelt het.",
    ),
    tabel(
        "Klopt dit over de snelheid van klimaatverandering?",
        [
            ("Natuurlijke veranderingen gingen meestal over duizenden jaren.", J),
            ("De huidige opwarming gaat veel sneller.", J),
            ("Bij een snelle verandering kunnen soorten moeilijk volgen.", J),
            ("Het PETM ging sneller dan de huidige opwarming.", F),
        ],
        "Ook het PETM duurde duizenden jaren.",
    ),
    koppel(
        "Koppel elke periode aan haar kenmerk.",
        [
            ("Krijt", "zo warm dat er geen poolijs was"),
            ("pleistoceen", "afwisseling van glacialen en interglacialen"),
            ("holoceen", "het warme tijdvak van nu"),
            ("kleine ijstijd", "koelere eeuwen in Europa"),
        ],
        ["plotse afkoeling ongeveer 12 000 jaar geleden"],
        "Die laatste is de jonge dryas.",
    ),
    sleep(
        "Na een zware uitbarsting komen [[zwaveldeeltjes]] tot in de [[stratosfeer]]. Ze weerkaatsen zonlicht, dus wordt het [[koeler]].",
        ["koolstofdioxide", "troposfeer", "warmer"],
        "Het effect duurt een jaar of twee.",
    ),
    tabel(
        "Haalt dit CO2 uit de atmosfeer of brengt het CO2 erin?",
        [
            ("verwering van gesteente", "Haalt eruit"),
            ("plantenresten begraven als steenkool", "Haalt eruit"),
            ("vulkanisme", "Brengt erin"),
            ("kalkskeletjes die op de zeebodem zakken", "Haalt eruit"),
        ],
        "Over miljoenen jaren regelt dat het klimaat.",
        kolommen=["Haalt eruit", "Brengt erin"],
    ),
    keuze(
        "In een ijskern lezen we de temperatuur af uit de verhouding van [[*zuurstofisotopen|stikstofbelletjes|zoutkristallen]].",
        "Zware en lichte zuurstofatomen gedragen zich anders bij verdampen.",
    ),
    mk(
        "Waarom begint een ijstijd vooral als de zomers op hoge noordelijke breedte koeler worden, en niet de winters?",
        [
            "Dan smelt de wintersneeuw niet meer weg",
            "Koude winters maken dan nog meer sneeuw dan gewoonlijk",
            "In de zomer staat de aarde het verst van de zon af",
            "Het zuidelijk halfrond heeft dan juist een warme zomer",
        ],
        0,
        "Sneeuw stapelt zich op en het witte oppervlak weerkaatst nog meer zon.",
    ),
    tabel(
        "Klopt dit over de jonge dryas?",
        [
            ("Het werd in enkele decennia weer bitter koud.", J),
            ("Het gebeurde ongeveer 12 000 jaar geleden.", J),
            ("Een verstoring van een zeestroom speelde vermoedelijk mee.", J),
            ("Het was een warme periode.", F),
        ],
        "Een plotse terugval midden in de opwarming.",
    ),
    inv(
        "De precessie duurt ongeveer 26 000 jaar. Hoeveel volledige cycli passen er in 104 000 jaar?",
        ["4"],
        "104 000 : 26 000 = 4.",
    ),
    tabel(
        "Klopt dit over Pangea en het klimaat?",
        [
            ("Het binnenland lag ver van de zee.", J),
            ("Er heerste een extreem landklimaat.", J),
            ("Het binnenland was heel nat.", F),
        ],
        "Zeewind raakte niet zo ver landinwaarts.",
    ),
    mk(
        "Hoe helpt het klimaat van het verleden ons vandaag?",
        [
            "Het toont hoe het klimaat op meer CO2 reageert",
            "Het bewijst dat de huidige opwarming vanzelf stopt",
            "Het laat zien dat de mens geen invloed heeft",
            "Het voorspelt precies het weer van volgend jaar",
        ],
        0,
        "Zo kunnen we modellen voor de toekomst testen.",
    ),
    keuze(
        "Ongeveer 11 700 jaar geleden begon het [[*holoceen|pleistoceen|Krijt]].",
        "Het tijdvak waarin wij leven.",
    ),
    tabel(
        "Klopt dit over de kleine ijstijd?",
        [
            ("Ze liep ongeveer van 1300 tot 1850.", J),
            ("Het was ongeveer een halve graad tot een graad koeler.", J),
            ("Er lagen ijskappen tot in Frankrijk.", F),
        ],
        "Kanalen en rivieren vroren vaker dicht.",
    ),
    tabel(
        "Welke Milanković-schommeling duurt ongeveer zo lang?",
        [
            ("ongeveer 100 000 jaar", "excentriciteit"),
            ("ongeveer 41 000 jaar", "obliquiteit"),
            ("ongeveer 26 000 jaar", "precessie"),
        ],
        "De langste cyclus past bij het ritme van de laatste ijstijden.",
        kolommen=["excentriciteit", "obliquiteit", "precessie"],
    ),
    sorteer(
        "Is dit een natuurlijke oorzaak van klimaatverandering of niet?",
        ["Natuurlijke oorzaak", "Geen oorzaak"],
        [
            ("de stand van de aardas", "Natuurlijke oorzaak"),
            ("een zware vulkaanuitbarsting", "Natuurlijke oorzaak"),
            ("de ligging van de continenten", "Natuurlijke oorzaak"),
            ("de schijngestalten van de maan", "Geen oorzaak"),
        ],
        "De maanfasen hebben geen invloed op het klimaat.",
    ),
    keuze(
        "Een glaciaal is een [[*koude|warme|droge]] fase binnen een ijstijdvak.",
        "Het tegenovergestelde is een interglaciaal.",
    ),
    open_(
        "Leg uit waarom het klimaat vroeger veranderde zonder de mens, en waarom de huidige verandering toch anders is.",
        "Vroeger zorgden de cycli van Milanković, vulkanen, de ligging van de continenten en CO2 uit natuurlijke bronnen voor klimaatverandering. Die veranderingen gingen meestal over duizenden jaren. Nu stijgt de CO2 door de mens heel snel, waardoor het klimaat veel sneller verandert dan vroeger.",
    ),
]
