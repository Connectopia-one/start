"""Grootheden, eenheden en wetenschappelijk onderzoek — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS

# Vier verbanden ---------------------------------------------------------
VB = Prent("vier-verbanden", "Vier verbanden tussen x en y", "vier kleine grafieken A tot D")
VAK = {"A": (90, 80), "B": (560, 80), "C": (90, 360), "D": (560, 360)}
B_, H_ = 350, 220
for k, (x0, y0) in VAK.items():
    VB.rect(x0, y0, B_, H_, "#ffffff", GRIJS, 6)
    ox, oy = x0 + 40, y0 + H_ - 30
    VB.pijl(ox, oy, x0 + B_ - 20, oy, DONKER, 2)
    VB.pijl(ox, oy, ox, y0 + 20, DONKER, 2)
    VB.tekst(x0 + B_ - 25, oy + 22, "x", 18)
    VB.tekst(ox - 18, y0 + 30, "y", 18)
    VB.letter(x0 + B_ - 30, y0 + 35, k)

def kromme(k, f, x1=0.0, x2=1.0):
    x0, y0 = VAK[k]
    ox, oy = x0 + 40, y0 + H_ - 30
    bw, bh = B_ - 90, H_ - 70
    pts = []
    n = 40
    for i in range(n + 1):
        t = x1 + (x2 - x1) * i / n
        pts.append((ox + t * bw, oy - f(t) * bh))
    VB.pad("M" + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", BLAUW, 4)

kromme("A", lambda t: 0.9 * t)                  # recht evenredig
kromme("B", lambda t: 0.3 + 0.6 * t)            # lineair, niet door oorsprong
kromme("C", lambda t: 0.09 / t, 0.1, 1.0)       # omgekeerd evenredig
kromme("D", lambda t: 0.95 * t * t)             # kwadratisch
ZVB = {k: [Prent.zone(x0, y0, B_, H_)] for k, (x0, y0) in VAK.items()}

VRAGEN = [
    klik(
        "Klik op de grafiek waarbij x en y recht evenredig zijn.",
        VB.bestand, ZVB["A"],
        "Een rechte door de oorsprong: de verhouding y : x blijft gelijk.",
    ),
    klik(
        "Klik op de grafiek waarbij het product x · y gelijk blijft.",
        VB.bestand, ZVB["C"],
        "Omgekeerd evenredig: een kromme die naar de assen toe buigt.",
    ),
    klik(
        "Klik op de grafiek die lineair is, maar niet recht evenredig.",
        VB.bestand, ZVB["B"],
        "Een rechte die niet door de oorsprong gaat.",
    ),
    met_prent(VB.bestand, tabel(
        "Kijk naar de grafieken. Welke past bij dit verband?",
        [
            ("de kinetische energie tegenover de snelheid", "D"),
            ("de stroomsterkte tegenover de spanning bij een vaste weerstand", "A"),
            ("de druk tegenover het volume van een gas bij vaste temperatuur", "C"),
            ("de lengte van een veer tegenover de kracht erop", "B"),
        ],
        "Een veer heeft al een lengte zonder kracht: lineair, niet door de oorsprong.",
        kolommen=["A", "B", "C", "D"],
    )),
    met_prent(VB.bestand, keuze(
        "Bij grafiek D wordt y [[*vier keer|twee keer|acht keer]] zo groot als je x verdubbelt.",
        "Een kwadratisch verband: 2² = 4.",
    )),
    tabel(
        "Grootheid of eenheid?",
        [
            ("lengte", "Grootheid"),
            ("seconde", "Eenheid"),
            ("massa", "Grootheid"),
            ("newton", "Eenheid"),
            ("temperatuur", "Grootheid"),
        ],
        "De grootheid is wat je meet, de eenheid waarin je het uitdrukt.",
        kolommen=["Grootheid", "Eenheid"],
    ),
    tabel(
        "Is dit een SI-basiseenheid?",
        [
            ("kilogram", J),
            ("kilometer per uur", F),
            ("seconde", J),
            ("meter", J),
            ("gram", F),
        ],
        "De SI-eenheid van massa is de kilogram, niet de gram.",
    ),
    koppel(
        "Koppel elk voorvoegsel aan zijn betekenis.",
        [
            ("mega", "een miljoen"),
            ("kilo", "duizend"),
            ("milli", "een duizendste"),
            ("micro", "een miljoenste"),
            ("nano", "een miljardste"),
        ],
        ["honderd"],
        "Centi is een honderdste, hecto honderd.",
    ),
    tabel(
        "Reken om naar de SI-eenheid.",
        [
            ("72 cm", "0,72 m"),
            ("350 g", "0,35 kg"),
            ("3 min", "180 s"),
            ("5 nm", "5 · 10⁻⁹ m"),
        ],
        "SI-eenheden: meter, kilogram en seconde.",
        kolommen=["0,72 m", "0,35 kg", "180 s", "5 · 10⁻⁹ m"],
    ),
    inv(
        "Uit de formule p = F : A wil je F halen. Je kent p = 2000 Pa en A = 0,5 m². Hoeveel newton is F?",
        ["1000"],
        "F = p · A = 2000 · 0,5 = 1000 N.",
    ),
    inv(
        "Hoeveel meter is 3,5 km plus 250 m?",
        ["3750"],
        "3,5 km = 3500 m. Samen 3750 m.",
    ),
    casus(
        "Sara wil weten of de temperatuur van water invloed heeft op hoe snel suiker oplost. Ze verwacht dat suiker in warm water sneller oplost.",
        [
            koppel(
                "Koppel elk onderdeel van haar onderzoek.",
                [
                    ("Lost suiker sneller op in warm water?", "onderzoeksvraag"),
                    ("Ik verwacht dat warm water sneller oplost.", "hypothese"),
                    ("de temperatuur van het water", "wat Sara verandert"),
                    ("de tijd tot de suiker weg is", "wat Sara meet"),
                ],
                ["conclusie"],
                "De conclusie komt pas na de metingen.",
            ),
            tabel(
                "Wat houdt Sara gelijk?",
                [
                    ("de hoeveelheid suiker", J),
                    ("de hoeveelheid water", J),
                    ("de temperatuur van het water", F),
                    ("de manier van roeren", J),
                ],
                "Enkel wat je onderzoekt mag veranderen.",
            ),
            keuze(
                "Na de metingen blijkt dat haar verwachting klopt. Dan is haar hypothese [[*bevestigd|weerlegd|overbodig]].",
                "Een weerlegde hypothese had ook kennis opgeleverd.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van een onderzoek in de juiste volgorde.",
        [
            "Een onderzoeksvraag opstellen",
            "Een hypothese formuleren",
            "Een onderzoeksplan maken",
            "Metingen uitvoeren en data verzamelen",
            "Een conclusie formuleren",
            "Reflecteren en communiceren",
        ],
        "Eerst de vraag en de verwachting, dan plannen, meten, besluiten en terugkijken.",
    ),
    tabel(
        "Klopt dit over een goede conclusie?",
        [
            ("Ze beantwoordt de onderzoeksvraag.", J),
            ("Ze steunt op de gemeten gegevens.", J),
            ("Ze mag dingen bevatten die je niet gemeten hebt.", F),
            ("Je past de gegevens aan zodat ze bij je hypothese passen.", F),
        ],
        "De gegevens beslissen, niet de verwachting.",
    ),
    mk(
        "Waarom herhaal je een meting liefst een paar keer?",
        [
            "Om toevallige meetfouten minder te laten doorwegen",
            "Om de uitkomst beter te laten passen bij wat je verwachtte",
            "Omdat één enkele meting volgens de regels nooit mag",
            "Om zo meer beduidende cijfers te kunnen opschrijven",
        ],
        0,
        "Het gemiddelde van meer metingen ligt dichter bij de echte waarde.",
    ),
    volgorde(
        "Zet de stappen van een ontwerp in de juiste volgorde.",
        [
            "Het probleem scherp omschrijven",
            "Criteria opstellen",
            "Het probleem in deelproblemen splitsen",
            "Een oplossing bouwen",
            "De oplossing toetsen aan de criteria en bijsturen",
        ],
        "Zonder criteria kan je achteraf niet beoordelen of het ontwerp goed is.",
    ),
    tabel(
        "Welke STEM-discipline speelt hier vooral mee?",
        [
            ("begrijpen hoe een virus zich vermenigvuldigt", "Wetenschappen"),
            ("een koelbox voor vaccins ontwerpen en bouwen", "Engineering"),
            ("berekenen hoeveel dosissen per week nodig zijn", "Wiskunde"),
            ("een app om afspraken te maken voor een prik", "Technologie"),
        ],
        "De vier disciplines werken samen aan één probleem.",
        kolommen=["Wetenschappen", "Technologie", "Engineering", "Wiskunde"],
    ),
    sleep(
        "Een meetresultaat bestaat altijd uit een [[getal]] en een [[eenheid]]. Zonder eenheid kan vijf zowel vijf meter als vijf [[kilometer]] betekenen.",
        ["grootheid", "grafiek"],
        "Het getal alleen zegt niets.",
    ),
    tabel(
        "Tabel of grafiek: wat toont dit het best?",
        [
            ("de precieze waarde van elke meting", "Tabel"),
            ("welk verband er tussen twee grootheden is", "Grafiek"),
            ("de meetwaarden met hun eenheid in de hoofding", "Tabel"),
            ("of de punten op een rechte liggen", "Grafiek"),
        ],
        "Een tabel geeft de waarden, een grafiek het verband.",
        kolommen=["Tabel", "Grafiek"],
    ),
    tabel(
        "Klopt dit over STEM en de maatschappij?",
        [
            ("De energieomslag zet onderzoekers aan tot nieuwe batterijen.", J),
            ("Een pandemie versnelt onderzoek naar vaccins.", J),
            ("Technologie ontwikkelt zich los van wat mensen nodig hebben.", F),
            ("Nieuwe technieken kunnen ook nieuwe vragen in de maatschappij oproepen.", J),
        ],
        "Maatschappij en STEM beïnvloeden elkaar in twee richtingen.",
    ),
    inv(
        "Je verdubbelt x en y wordt half zo groot. Hoe groot wordt y als je x drie keer zo groot maakt en y eerst 12 was?",
        ["4"],
        "Omgekeerd evenredig: drie keer x geeft een derde van y. 12 : 3 = 4.",
    ),
    tabel(
        "Een leerling meet de lengte van een tafel met een meetlint tot op een millimeter. Klopt dit?",
        [
            ("Hij kan 1,253 m opschrijven.", J),
            ("Hij kan 1,25347 m opschrijven.", F),
            ("Te veel cijfers opschrijven suggereert een te grote nauwkeurigheid.", J),
            ("Een meting is nooit helemaal exact.", J),
        ],
        "Je schrijft enkel de cijfers die je echt gemeten hebt.",
    ),
    met_prent(VB.bestand, tabel(
        "Kijk naar de grafieken. Klopt dit?",
        [
            ("Bij A hoort y = 0 bij x = 0.", J),
            ("Bij B hoort y = 0 bij x = 0.", F),
            ("Bij C raakt de kromme de x-as nooit.", J),
            ("Bij D stijgt y steeds sneller.", J),
        ],
        "Enkel bij A gaat de rechte door de oorsprong.",
    )),
    tabel(
        "Welk verband zit in deze meetreeks?",
        [
            ("x: 1, 2, 4 en y: 3, 6, 12", "Recht evenredig"),
            ("x: 1, 2, 4 en y: 12, 6, 3", "Omgekeerd evenredig"),
            ("x: 1, 2, 3 en y: 2, 8, 18", "Kwadratisch"),
            ("x: 0, 1, 2 en y: 5, 7, 9", "Lineair, niet recht evenredig"),
        ],
        "Kijk naar de verhouding, het product of het kwadraat.",
        kolommen=["Recht evenredig", "Omgekeerd evenredig", "Kwadratisch", "Lineair, niet recht evenredig"],
    ),
    keuze(
        "In de reflectie zeg je onder meer hoe [[*betrouwbaar|duur|lang]] je resultaat is.",
        "Je kijkt terug op je methode en je resultaten.",
    ),
    tabel(
        "Klopt dit over een onderzoeksverslag?",
        [
            ("Je beschrijft je werkwijze zodat iemand anders het kan herhalen.", J),
            ("Je vermeldt de eenheden bij je meetwaarden.", J),
            ("Metingen die niet passen, laat je weg zonder iets te zeggen.", F),
            ("Je vermeldt welk materiaal je gebruikte.", J),
        ],
        "Herhaalbaarheid is een kern van wetenschap.",
    ),
    inv(
        "Schrijf 0,000045 m als een getal maal 10⁻⁵. Welk getal komt er vooraan?",
        ["4,5", "4.5"],
        "0,000045 = 4,5 · 10⁻⁵.",
    ),
    open_(
        "Je wil onderzoeken of een bal hoger opbotst als je hem van hoger laat vallen. Beschrijf hoe je dat eerlijk onderzoekt.",
        "Ik laat dezelfde bal op dezelfde vloer vallen en verander enkel de valhoogte. Bij elke hoogte meet ik de opbotshoogte een paar keer en neem ik het gemiddelde. Ik zet de resultaten in een tabel en een grafiek en kijk welk verband er is. Mijn conclusie steunt op die metingen.",
    ),
]
