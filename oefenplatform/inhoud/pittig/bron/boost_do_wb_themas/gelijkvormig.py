"""Schaalverandering en gelijkvormige figuren — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_gelijkvormig: gelijkvormigheid en de factor, schaal,
het effect op lengte, oppervlakte en volume, en de kenmerken HH, ZHZ en ZZZ.
Met twee zelfgetekende prenten: driehoeken met hoeken en driehoeken met zijden."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_tekst, pix_zone

CELLEN = [(60, 70), (370, 70), (680, 70), (215, 360), (525, 360)]   # linkerbovenhoek van elke cel (300 x 270)


def _poly(pts, kleur):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{p}" fill="{kleur}" stroke="#24331b" stroke-width="3"/>'


def _label(cel, letter, kleur):
    x, y = cel
    return [f'<circle cx="{x+22}" cy="{y+22}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>', s_tekst(x + 22, y + 29, letter, 20, vet=True, kleur=kleur)]


HOEKEN = [("R", 40, 75), ("A", 40, 65), ("B", 75, 60), ("C", 65, 75), ("D", 40, 80)]


def _hoekdriehoeken():
    d = []
    for cel, (letter, a, b) in zip(CELLEN, HOEKEN):
        x0, y0 = cel[0] + 40, cel[1] + 240
        basis = 220
        ta, tb = math.tan(math.radians(a)), math.tan(math.radians(b))
        xt = basis * tb / (ta + tb)
        top = (x0 + xt, y0 - xt * ta)
        vul = "#f6e7c8" if letter == "R" else "#e6efdc"
        d.append(_poly([(x0, y0), (x0 + basis, y0), top], vul))
        d.append(s_tekst(x0 + 38, y0 - 10, f"{a}°", 19, "start"))
        d.append(s_tekst(x0 + basis - 38, y0 - 10, f"{b}°", 19, "end"))
        d += _label(cel, letter, "#b5651d" if letter == "R" else "#24331b")
    return d


ZIJDEN = [("R", 3, 4, 6), ("A", 6, 8, 12), ("B", 4, 5, 7), ("C", 4.5, 6, 9), ("D", 6, 8, 10)]


def _getal(v):
    return f"{v:g}".replace(".", ",")


def _zijdriehoeken():
    d = []
    for cel, (letter, a, b, c) in zip(CELLEN, ZIJDEN):
        s = 19                               # pixels per eenheid
        x0, y0 = cel[0] + 30, cel[1] + 245
        # c is de basis, a de linkerzijde, b de rechterzijde
        cosA = (a * a + c * c - b * b) / (2 * a * c)
        top = (x0 + a * s * cosA, y0 - a * s * math.sqrt(1 - cosA * cosA))
        rechts = (x0 + c * s, y0)
        vul = "#f6e7c8" if letter == "R" else "#e6efdc"
        d.append(_poly([(x0, y0), rechts, top], vul))
        d.append(s_tekst(x0 + c * s / 2, y0 + 24, _getal(c), 19))
        d.append(s_tekst((x0 + top[0]) / 2 - 12, (y0 + top[1]) / 2, _getal(a), 19, "end"))
        d.append(s_tekst((rechts[0] + top[0]) / 2 + 12, (y0 + top[1]) / 2, _getal(b), 19, "start"))
        d += _label(cel, letter, "#b5651d" if letter == "R" else "#24331b")
    return d


def _cz(*letters, lijst=HOEKEN):
    namen = [t[0] for t in lijst]
    return [pix_zone(CELLEN[namen.index(l)][0], CELLEN[namen.index(l)][1], 300, 270) for l in letters]


HD, ZD = "driehoeken-met-hoeken", "driehoeken-met-zijden"
GRAFIEKEN = [dict(naam=HD, titel="Driehoek R en vier andere driehoeken: twee hoeken gegeven", eigen=_hoekdriehoeken),
             dict(naam=ZD, titel="Driehoek R en vier andere driehoeken: drie zijden gegeven", eigen=_zijdriehoeken)]
UH, UZ = f"{HD}.svg", f"{ZD}.svg"

VRAGEN = [
    klik("Klik op een driehoek die gelijkvormig is met R.", UH, _cz("A", "C"),
         r"R heeft hoeken van \(40^{\circ}\), \(75^{\circ}\) en \(65^{\circ}\). A en C hebben twee van die hoeken: kenmerk HH."),
    klik(r"Klik op de driehoek met een hoek van \(45^{\circ}\).", UH, _cz("B"),
         r"Bij B is de derde hoek \(180^{\circ} - 75^{\circ} - 60^{\circ} = 45^{\circ}\)."),
    klik("Klik op de driehoek waarvan de zijden twee keer zo lang zijn als die van R.", UZ, _cz("A", lijst=ZIJDEN),
         r"\(3, 4, 6\) wordt \(6, 8, 12\): elke zijde keer \(2\)."),
    klik(r"Klik op de driehoek die gelijkvormig is met R, met factor \(1{,}5\).", UZ, _cz("C", lijst=ZIJDEN),
         r"\(3 \cdot 1{,}5 = 4{,}5\), \(4 \cdot 1{,}5 = 6\) en \(6 \cdot 1{,}5 = 9\)."),
    klik("Klik op de driehoek die twee zijden heeft in verhouding 2 met R, maar toch niet gelijkvormig is.", UZ, _cz("D", lijst=ZIJDEN),
         r"\(6\) en \(8\) zijn het dubbel van \(3\) en \(4\), maar \(10\) is niet het dubbel van \(6\). Voor ZZZ moeten alle drie kloppen."),
    mk(r"Welke rechthoek is gelijkvormig met een rechthoek van \(4\) cm op \(6\) cm?",
       [r"\(6\) cm op \(9\) cm", r"\(6\) cm op \(8\) cm", r"\(5\) cm op \(7\) cm", r"\(8\) cm op \(10\) cm"], 0,
       r"\(\frac{6}{4} = \frac{9}{6} = 1{,}5\). Bij de andere is de verhouding niet gelijk."),
    inv(r"Een kaart heeft schaal \(1 : 50\,000\). Twee dorpen liggen \(7\) km uit elkaar. Hoeveel centimeter is dat op de kaart?", ["14", "veertien"],
        r"\(7\) km \(= 700\,000\) cm, en \(700\,000 : 50\,000 = 14\)."),
    mk(r"Op een plan is een kamer van \(5\) m lang \(2\) cm. Wat is de schaal?",
       [r"\(1 : 250\)", r"\(1 : 25\)", r"\(1 : 2\,500\)", r"\(2 : 5\)"], 0,
       r"\(5\) m \(= 500\) cm. \(2 : 500 = 1 : 250\)."),
    keuze("Een maquette op schaal 1 : 20 is een [[*verkleining|vergroting]] van het echte gebouw.", "Eén centimeter op de maquette is twintig centimeter in het echt."),
    koppel(r"Een figuur wordt verkleind met factor \(k = \frac{1}{2}\). Verbind de grootheid met haar factor.",
           [("de lengte", r"\(\times \frac{1}{2}\)"), ("de oppervlakte", r"\(\times \frac{1}{4}\)"), ("het volume", r"\(\times \frac{1}{8}\)")],
           [r"\(\times 2\)"], r"Oppervlakte met \(k^{2}\), volume met \(k^{3}\)."),
    inv(r"Een kubus heeft een volume van \(5\) cm³. Hij wordt vergroot met factor \(3\). Wat is het nieuwe volume in cm³?", ["135"],
        r"\(5 \cdot 3^{3} = 5 \cdot 27 = 135\)."),
    inv("De oppervlakte van een figuur wordt 25 keer zo groot, de vorm blijft. Wat is de gelijkvormigheidsfactor? Een getal.", ["5", "vijf"],
        r"\(k^{2} = 25\), dus \(k = 5\)."),
    mk("Het volume van een gelijkvormige figuur wordt 64 keer zo groot. Hoe veranderen de lengtes?",
       [r"\(\times 4\)", r"\(\times 8\)", r"\(\times 16\)", r"\(\times 32\)"], 0,
       r"\(k^{3} = 64\), dus \(k = 4\)."),
    casus("Een pizza met een diameter van \\(30\\) cm kost \\(12\\) euro. Er is ook een pizza van \\(40\\) cm, even dik.", [
        mk("Wat is de gelijkvormigheidsfactor van klein naar groot?",
           [r"\(\frac{4}{3}\)", r"\(\frac{3}{4}\)", r"\(10\)", r"\(\frac{16}{9}\)"], 0, r"\(40 : 30 = \frac{4}{3}\)."),
        mk("Hoeveel keer zoveel pizza krijg je bij de grote?",
           [r"ongeveer \(1{,}78\) keer", r"ongeveer \(1{,}33\) keer", r"precies \(2\) keer", r"ongeveer \(2{,}37\) keer zoveel"], 0,
           r"De oppervlakte gaat met \(k^{2} = \frac{16}{9} \approx 1{,}78\)."),
        keuze("Een eerlijke prijs voor de grote pizza is dan ongeveer [[*21|16|24]] euro.", r"\(12 \cdot 1{,}78 \approx 21\)."),
    ]),
    tabel("Klopt dit over gelijkvormige driehoeken?",
          [("Alle gelijkzijdige driehoeken zijn gelijkvormig.", J), ("Alle rechthoekige driehoeken zijn gelijkvormig.", F),
           (r"Twee gelijkbenige driehoeken met een tophoek van \(50^{\circ}\) zijn gelijkvormig.", J), ("Twee driehoeken met dezelfde omtrek zijn gelijkvormig.", F)],
          r"Een gelijkbenige driehoek met tophoek \(50^{\circ}\) heeft basishoeken van \(65^{\circ}\): alle hoeken liggen vast.",
          kolommen=["Juist", "Fout"]),
    mk(r"Driehoek 1 heeft zijden \(3\) en \(5\) met een ingesloten hoek van \(40^{\circ}\). Driehoek 2 heeft zijden \(6\) en \(10\) met een ingesloten hoek van \(40^{\circ}\). Welk kenmerk toont dat ze gelijkvormig zijn?",
       ["ZHZ", "ZZZ", "HH", "ZZH met een rechte hoek"], 0,
       r"Twee zijden in dezelfde verhouding (\(k = 2\)) en de hoek ertussen gelijk."),
    inv(r"Een vlaggenmast werpt \(9\) m schaduw. Een paaltje van \(1{,}2\) m werpt op hetzelfde moment \(1{,}8\) m schaduw. Hoe hoog is de mast, in meter?", ["6", "zes"],
        r"\(\frac{1{,}2}{1{,}8} = \frac{h}{9}\), dus \(h = 6\)."),
    sleep(r"Een driehoek heeft hoeken van \(35^{\circ}\) en \(85^{\circ}\). De derde hoek is dan [[\(60^{\circ}\)]]. Een driehoek met hoeken \(35^{\circ}\) en \(60^{\circ}\) is er dus gelijkvormig mee volgens kenmerk [[HH]].",
          [r"\(85^{\circ}\)", "ZZZ"], "Twee gelijke hoeken volstaan."),
    mk(r"Een driehoek met zijden \(5\), \(7\) en \(9\) wordt vergroot tot een omtrek van \(63\). Hoe lang wordt de kortste zijde?",
       [r"\(15\)", r"\(5\)", r"\(21\)", r"\(\frac{5}{3}\)"], 0, r"De omtrek gaat van \(21\) naar \(63\): \(k = 3\). Dan \(5 \cdot 3 = 15\)."),
    inv(r"De oppervlaktes van twee gelijkvormige driehoeken staan in verhouding \(4 : 9\). Een zijde van de kleine is \(6\). Hoe lang is de overeenkomstige zijde van de grote?", ["9", "negen"],
        r"\(k^{2} = \frac{9}{4}\), dus \(k = \frac{3}{2}\). \(6 \cdot \frac{3}{2} = 9\)."),
    tabel("Zijn twee zulke figuren altijd gelijkvormig?",
          [("twee cirkels", "altijd"), ("twee vierkanten", "altijd"), ("twee rechthoeken", "niet altijd"), ("twee ruiten", "niet altijd"), ("twee kubussen", "altijd")],
          "Bij rechthoeken en ruiten kan de verhouding of de hoek verschillen.",
          kolommen=["altijd", "niet altijd"]),
    keuze(r"Een figuur verkleinen met factor \(k = 0{,}5\) maakt de oppervlakte [[*vier keer|twee keer|acht keer]] kleiner.", r"\(0{,}5^{2} = 0{,}25\)."),
    inv(r"Een tuinplan op schaal \(1 : 200\) toont een terras van \(3\) cm op \(2\) cm. Hoeveel m² is het echte terras?", ["24"],
        r"In het echt \(6\) m op \(4\) m, dus \(24\) m². Of: \(6\) cm² keer \(200^{2}\)."),
    mk("Een bronzen beeld wordt drie keer zo hoog nagemaakt, in hetzelfde brons. Hoeveel keer zo zwaar wordt het?",
       [r"\(27\) keer", r"\(9\) keer", r"\(3\) keer", "even zwaar, want het is hetzelfde brons"], 0,
       r"Het gewicht volgt het volume: \(3^{3} = 27\)."),
    sorteer("Welk kenmerk toont hier de gelijkvormigheid?", ["HH", "ZHZ", "ZZZ"],
            [(r"in beide driehoeken hoeken van \(30^{\circ}\) en \(70^{\circ}\)", "HH"), (r"zijden \(2, 3, 4\) en \(6, 9, 12\)", "ZZZ"),
             (r"zijden \(4\) en \(6\) en zijden \(6\) en \(9\), telkens met \(50^{\circ}\) ertussen", "ZHZ"), (r"beide rechthoekig, met een hoek van \(25^{\circ}\)", "HH")],
            r"Een rechte hoek en een hoek van \(25^{\circ}\) zijn al twee gelijke hoeken."),
    mk(r"In driehoek \(ABC\) ligt \(D\) op \(AB\) en \(E\) op \(AC\), met \(DE\) evenwijdig met \(BC\). Waarom zijn \(ADE\) en \(ABC\) gelijkvormig?",
       ["ze hebben twee gelijke hoeken", "ze hebben dezelfde oppervlakte", "al hun zijden zijn even lang", r"\(DE\) is altijd half zo lang als \(BC\)"], 0,
       r"De hoek in \(A\) is gemeenschappelijk, en \(DE \parallel BC\) geeft gelijke hoeken in \(D\) en \(B\). Kenmerk HH."),
    inv(r"In diezelfde figuur is \(AD = 3\), \(AB = 9\) en \(BC = 12\). Hoe lang is \(DE\)?", ["4", "vier"],
        r"\(k = \frac{3}{9} = \frac{1}{3}\), dus \(DE = 12 \cdot \frac{1}{3} = 4\)."),
    open_("Een kubus wordt in alle richtingen dubbel zo groot. Leg uit waarom je niet dubbel zoveel verf nodig hebt om hem te schilderen.",
          r"Verf gaat over de oppervlakte. Die gaat met \(k^{2} = 4\): je hebt vier keer zoveel verf nodig, niet twee keer."),
]
