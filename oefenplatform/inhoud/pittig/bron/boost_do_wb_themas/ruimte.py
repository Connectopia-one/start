"""Ruimtefiguren, vlakke voorstellingen en vectoren — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_ruimte: onderlinge ligging van rechten en vlakken,
ruimtefiguren en vlakke figuren, cavalièreperspectief, aanzichten en
ontwikkelingen, en vectoren met som, verschil en veelvoud. Met twee
zelfgetekende prenten: een kubus in cavalièreperspectief en een vectorrooster."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import s_tekst, s_lijn, pix_zone

KU = "kubus-ribben"
P = {"A": (250, 560), "B": (550, 560), "F": (550, 260), "E": (250, 260),
     "D": (400, 450), "C": (700, 450), "G": (700, 150), "H": (400, 150)}
RIBBEN = ["AB", "BF", "FE", "EA", "BC", "CG", "GF", "EH", "HG", "AD", "DC", "DH"]
LABEL = {"A": (-28, 30), "B": (28, 30), "C": (28, 30), "D": (-26, -12), "E": (-28, -10), "F": (24, 36), "G": (28, -14), "H": (-28, -14)}
VERBORGEN = {"AD", "DC", "DH"}
NUMMERS = {"1": "AB", "2": "CG", "3": "EH", "4": "DC", "5": "FG", "6": "HG", "7": "BC"}


PLEK = {"DC": 0.3}


def _mid(r):
    (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
    t = PLEK.get(r, 0.5)
    return x1 + t * (x2 - x1), y1 + t * (y2 - y1)


def _kubus():
    d = []
    for r in RIBBEN:
        (x1, y1), (x2, y2) = P[r[0]], P[r[1]]
        stip = ' stroke-dasharray="10 8"' if r in VERBORGEN else ""
        d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#24331b" stroke-width="4"{stip}/>')
    for naam, (x, y) in P.items():
        dx, dy = LABEL[naam]
        d.append(s_tekst(x + dx, y + dy, naam, 26, vet=True))
    for n, r in NUMMERS.items():
        x, y = _mid(r if r in RIBBEN else r[::-1])
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="19" fill="#3b6fa0"/>')
        d.append(s_tekst(x, y + 7, n, 20, kleur="#ffffff", vet=True))
    return d


def _kz(*nrs):
    out = []
    for n in nrs:
        r = NUMMERS[n]
        x, y = _mid(r if r in RIBBEN else r[::-1])
        out.append(pix_zone(x - 32, y - 32, 64, 64))
    return out


VR = "vectoren-rooster"
E_ = 40            # pixels per hokje
VEC = {"u": ((2, 11), (3, 1)), "v": ((2, 6), (1, -2)),
       "A": ((7, 11), (4, -1)), "B": ((7, 3), (2, 3)), "C": ((21, 12), (-6, -2)),
       "D": ((13, 8), (2, -4)), "E": ((17, 3), (1.5, 0.5))}


def _px(gx, gy):
    return 60 + gx * E_, 600 - gy * E_


def _pijl(x1, y1, x2, y2, kleur):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 18 * math.cos(a - 0.4), y2 - 18 * math.sin(a - 0.4))
    p2 = (x2 - 18 * math.cos(a + 0.4), y2 - 18 * math.sin(a + 0.4))
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{kleur}" stroke-width="4"/>'
            f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{kleur}"/>')


def _rooster():
    d = []
    for i in range(23):
        x = 60 + i * E_
        d.append(s_lijn(x, 80, x, 600, kleur="#e7e2d2", dikte=1))
    for j in range(14):
        y = 600 - j * E_
        d.append(s_lijn(60, y, 940, y, kleur="#e7e2d2", dikte=1))
    for naam, ((gx, gy), (dx, dy)) in VEC.items():
        kleur = "#b5651d" if naam in "uv" else "#3b6fa0"
        x1, y1 = _px(gx, gy)
        x2, y2 = _px(gx + dx, gy + dy)
        d.append(_pijl(x1, y1, x2, y2, kleur))
        lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 18
        label = f"{naam}⃗" if naam in "uv" else naam
        d.append(f'<circle cx="{lx:.1f}" cy="{ly-7:.1f}" r="16" fill="#ffffff" stroke="{kleur}" stroke-width="2"/>')
        d.append(s_tekst(lx, ly, naam, 20, kleur=kleur, vet=True))
    return d


def _vz(naam):
    (gx, gy), (dx, dy) = VEC[naam]
    x1, y1 = _px(gx, gy)
    x2, y2 = _px(gx + dx, gy + dy)
    return [pix_zone(min(x1, x2) - 20, min(y1, y2) - 40, abs(x2 - x1) + 40, abs(y2 - y1) + 60)]


GRAFIEKEN = [dict(naam=KU, titel="Kubus ABCD.EFGH in cavalièreperspectief", eigen=_kubus),
             dict(naam=VR, titel="De oranje vectoren u en v, en vijf blauwe vectoren", eigen=_rooster)]
UK, UV = f"{KU}.svg", f"{VR}.svg"

VRAGEN = [
    klik(r"Klik op een genummerde ribbe die evenwijdig is met \(AB\).", UK, _kz("4", "6"),
         r"\(DC\) en \(HG\) lopen in dezelfde richting als \(AB\)."),
    klik(r"Klik op een genummerde ribbe die kruisend is met \(AB\).", UK, _kz("2", "3", "5"),
         r"\(CG\), \(EH\) en \(FG\) snijden \(AB\) niet en zijn er ook niet evenwijdig mee."),
    klik(r"Klik op de genummerde ribbe die \(AB\) snijdt.", UK, _kz("7"), r"\(BC\) en \(AB\) hebben het punt \(B\) gemeen."),
    klik(r"Klik op de ribbe van het bovenvlak die kruisend is met \(BC\).", UK, _kz("6"),
         r"\(EH\) en \(FG\) zijn evenwijdig met \(BC\). \(HG\) loopt dwars en raakt \(BC\) niet."),
    klik("Klik op de genummerde ribbe die je niet ziet van voren.", UK, _kz("4"),
         "In cavalièreperspectief teken je verborgen ribben in stippellijn."),
    met_prent(UK, tabel("Hoe liggen deze ribben van de kubus ten opzichte van elkaar?",
                        [(r"\(AB\) en \(HG\)", "evenwijdig"), (r"\(AE\) en \(BC\)", "kruisend"), (r"\(AB\) en \(BF\)", "snijdend"), (r"\(EH\) en \(BC\)", "evenwijdig")],
                        r"\(AE\) staat recht omhoog, \(BC\) loopt naar achteren: ze raken elkaar niet en lopen niet gelijk.",
                        kolommen=["evenwijdig", "snijdend", "kruisend"])),
    met_prent(UK, mk(r"Wat is de doorsnede van het vlak \(ABFE\) en het vlak \(BCGF\)?",
                     [r"de rechte \(BF\)", r"het punt \(B\)", r"de rechte \(AB\)", r"het vlak \(ABCD\)"], 0,
                     "Twee snijdende vlakken snijden elkaar volgens een rechte: hier de gemeenschappelijke ribbe.")),
    keuze("In een kubus zijn het grondvlak en het bovenvlak [[*evenwijdig|snijdend|samenvallend]].", "Ze liggen op een vaste afstand van elkaar."),
    inv("Met hoeveel ribben van een kubus is één gegeven ribbe kruisend? Een getal.", ["4", "vier"],
        r"Van de andere 11 ribben zijn er 3 evenwijdig en 4 snijdend. Blijven er 4 kruisend over."),
    mk("Welke ontwikkeling hoort bij een cilinder?",
       ["een rechthoek en twee cirkels", "een cirkel en een cirkelsector", "zes gelijke vierkanten", "twee rechthoeken en een cirkel"], 0,
       "De mantel rol je af tot een rechthoek, het grondvlak en het bovenvlak zijn cirkels."),
    koppel("Verbind elke ruimtefiguur met haar vooraanzicht.",
           [("een kegel", "een driehoek"), ("een cilinder", "een rechthoek"), ("een bol", "een cirkel"), ("een kubus", "een vierkant")],
           ["een zeshoek"], "Het vooraanzicht is wat je ziet als je recht van voren kijkt."),
    tabel("Ruimtefiguur of vlakke figuur?",
          [("een cirkel", "vlakke figuur"), ("een piramide", "ruimtefiguur"), ("de ontwikkeling van een balk", "vlakke figuur"), ("een bol", "ruimtefiguur"), ("een ruit", "vlakke figuur")],
          "Een ontwikkeling ligt plat in het vlak, ook al hoort ze bij een ruimtefiguur.",
          kolommen=["ruimtefiguur", "vlakke figuur"]),
    mk("Een figuur heeft een cirkel als bovenaanzicht en een rechthoek als vooraanzicht. Welke figuur is het?",
       ["een cilinder", "een kegel", "een bol", "een vierzijdige piramide"], 0,
       "Een kegel heeft een driehoek als vooraanzicht, een bol een cirkel."),
    sorteer("Heb je hier een vector nodig of volstaat één getal?", ["vector", "één getal"],
            [("de kracht waarmee je een kast duwt", "vector"), ("de verplaatsing van een boot", "vector"), ("de massa van een zak aardappelen", "één getal"),
             ("de wind, met snelheid en windrichting", "vector"), ("de tijd van een race", "één getal")],
            "Bij een vector doet ook de richting en de zin mee."),
    inv(r"\(\vec{u}\) heeft grootte \(6\). Hoe groot is \(-\frac{1}{3}\vec{u}\)? Een getal.", ["2", "twee"],
        r"De grootte wordt \(\frac{1}{3}\) van \(6\). Het minteken keert enkel de zin om."),
    keuze(r"\(-\frac{1}{3}\vec{u}\) heeft [[*de omgekeerde|dezelfde]] zin als \(\vec{u}\) en is [[*korter|langer]].",
          "Een negatief getal keert de zin om. Een getal tussen 0 en 1 maakt korter."),
    mk(r"Twee krachten van \(3\) N en \(4\) N trekken loodrecht op elkaar. Hoe groot is hun som?",
       [r"\(5\) N", r"\(7\) N", r"\(1\) N", r"\(12\) N"], 0,
       r"Kop aan staart vormen ze een rechthoekige driehoek: \(\sqrt{3^{2} + 4^{2}} = 5\)."),
    tabel("Klopt dit over vectoren?",
          [(r"\(\vec{u} + \vec{v} = \vec{v} + \vec{u}\)", J), (r"\(\vec{u} - \vec{v} = \vec{v} - \vec{u}\)", F),
           (r"\(2(\vec{u} + \vec{v}) = 2\vec{u} + 2\vec{v}\)", J), ("Twee krachten van 5 N geven samen altijd 10 N.", F)],
          r"\(\vec{v} - \vec{u}\) is de tegengestelde van \(\vec{u} - \vec{v}\). Twee krachten van 5 N geven 10 N enkel als ze dezelfde zin hebben.",
          kolommen=["Juist", "Fout"]),
    volgorde(r"Zet de stappen om \(\vec{u} - \vec{v}\) te tekenen in de juiste volgorde.",
             [r"teken \(\vec{u}\)", r"teken \(-\vec{v}\): even lang als \(\vec{v}\), omgekeerde zin",
              r"zet de staart van \(-\vec{v}\) aan de kop van \(\vec{u}\)", r"teken de pijl van de staart van \(\vec{u}\) naar de kop van \(-\vec{v}\)"],
             r"Aftrekken is de tegengestelde vector optellen."),
    casus("Een roeier roeit op een rivier met een snelheid van \\(6\\) km/h ten opzichte van het water. De stroming duwt met \\(2\\) km/h stroomafwaarts.", [
        inv("Hoe snel gaat hij vooruit als hij stroomopwaarts roeit, in km/h? Een getal.", ["4", "vier"],
            r"Tegengestelde zin: \(6 - 2 = 4\)."),
        inv("En als hij stroomafwaarts roeit, in km/h? Een getal.", ["8", "acht"], r"Dezelfde zin: \(6 + 2 = 8\)."),
        keuze("Stroomopwaarts hebben de twee snelheidsvectoren [[*dezelfde richting, maar een tegengestelde zin|een andere richting]].",
              "Ze liggen op dezelfde lijn, maar wijzen naar elkaar toe."),
        mk("Hoe lang doet hij over \\(4\\) km stroomopwaarts?", ["1 uur", "40 minuten", "2 uur", "30 minuten"], 0,
           r"Aan \(4\) km/h duurt \(4\) km precies één uur."),
    ]),
    sleep(r"Bij \(\vec{u} + \vec{v}\) zet je de [[staart]] van \(\vec{v}\) aan de [[kop]] van \(\vec{u}\).",
          ["midden"], "Kop aan staart: zo leg je de twee verschuivingen na elkaar."),
    open_("Leg uit waarom twee vlakken nooit kruisend kunnen zijn.",
          "Twee vlakken die niet evenwijdig zijn en niet samenvallen, snijden elkaar altijd volgens een rechte. Kruisend kan enkel bij rechten: die kunnen elkaar missen zonder evenwijdig te zijn."),
    klik(r"Waar staat \(\vec{u} + \vec{v}\)? Klik op die blauwe vector.", UV, _vz("A"),
         r"\(\vec{u}\) is 3 naar rechts en 1 omhoog, \(\vec{v}\) 1 naar rechts en 2 omlaag. Samen: 4 naar rechts, 1 omlaag."),
    klik(r"Zoek het verschil \(\vec{u} - \vec{v}\) en klik op die blauwe vector.", UV, _vz("B"),
         r"\(3 - 1 = 2\) naar rechts, \(1 - (-2) = 3\) omhoog."),
    klik(r"Een van de blauwe vectoren is \(-2\vec{u}\). Klik erop.", UV, _vz("C"),
         r"Dubbel zo lang als \(\vec{u}\) en de andere zin op: 6 naar links, 2 omlaag."),
    klik(r"Klik op de helft van \(\vec{u}\) tussen de blauwe vectoren.", UV, _vz("E"),
         r"Half zo lang, zelfde richting en zin: 1,5 naar rechts en 0,5 omhoog."),
    klik(r"Klik op de blauwe vector met dezelfde richting en zin als \(\vec{v}\), maar dubbel zo lang.", UV, _vz("D"),
         r"\(2\vec{v}\): 2 naar rechts en 4 omlaag. Waar de vector staat, maakt niet uit."),
]
