"""De sinusfunctie en de goniometrische cirkel — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

# Goniometrische cirkel met gelijke schaal op beide assen
C_GRAF = venster("sinus-cirkel", -2.017, 2.017, -1.3, 1.3, 0.5, 0.5)
HOEKEN = {"P": math.pi / 3, "Q": 5 * math.pi / 6, "R": 7 * math.pi / 6, "S": 7 * math.pi / 4}
# Getij: h(t) = 2·sin(π/6·(t − 3)) + 3, t in uur, h in meter
G_GRAF = venster("sinus-getij", 0, 24, 0, 6, 1, 1)


def _h(t):
    return 2 * math.sin(math.pi / 6 * (t - 3)) + 3


def _punt(naam):
    a = HOEKEN[naam]
    return math.cos(a), math.sin(a)


GRAFIEKEN = [
    dict(naam=C_GRAF, titel="De goniometrische cirkel",
         parametrisch=[(math.cos, math.sin, "groen", (0, 2 * math.pi))],
         segmenten=[((0, 0), _punt(n)) for n in HOEKEN],
         punten=[(*_punt(n), n) for n in HOEKEN], ijk_x=1, ijk_y=1),
    dict(naam=G_GRAF, titel="Waterhoogte h (m) in een haven, t uur na middernacht",
         krommen=[(_h, "blauw", "", (0, 24))], stippel=[("h", 3)], xlabel="t", ylabel="h", ijk_x=3, ijk_y=1),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over de cirkel en de sinusfunctie") for g in GRAFIEKEN]


def _pz(naam):
    return punt_zone(C_GRAF, *_punt(naam), 30)


VRAGEN = [
    klik(
        r"Klik op het beeldpunt van de hoek \(-\dfrac{\pi}{4}\).",
        f"{C_GRAF}.svg",
        [_pz("S")],
        r"\(-\frac{\pi}{4}\) draait \(45°\) in wijzerzin, tot in het vierde kwadrant. Dat is hetzelfde beeldpunt als \(\frac{7\pi}{4}\).",
    ),
    klik(
        r"Klik op het beeldpunt van de hoek in het tweede kwadrant waarvan de sinus \(\frac{1}{2}\) is.",
        f"{C_GRAF}.svg",
        [_pz("Q")],
        r"\(\sin \frac{5\pi}{6} = \frac{1}{2}\), en \(\frac{5\pi}{6} = 150°\) ligt in het tweede kwadrant.",
    ),
    met_prent(f"{C_GRAF}.svg", tabel(
        "Is de sinus van de hoek bij elk beeldpunt positief of negatief?",
        [("P", "Positief"), ("Q", "Positief"), ("R", "Negatief"), ("S", "Negatief")],
        "De sinus is de y-coördinaat van het beeldpunt: boven de x-as positief, eronder negatief.",
        kolommen=["Positief", "Negatief"],
    )),
    met_prent(f"{C_GRAF}.svg", mk(
        r"Welk beeldpunt hoort bij \(\dfrac{19\pi}{6}\)?",
        ["R", "Q", "P", "S"],
        0,
        r"\(\frac{19\pi}{6} = 2\pi + \frac{7\pi}{6}\). Na een volle toer kom je bij \(\frac{7\pi}{6} = 210°\).",
    )),
    klik(
        "Klik op het moment van de eerste hoogwaterstand na middernacht.",
        f"{G_GRAF}.svg",
        [punt_zone(G_GRAF, 6, 5)],
        "Om 6 uur staat het water op zijn hoogst: 5 m.",
    ),
    klik(
        "Klik op een moment waarop het water het snelst stijgt.",
        f"{G_GRAF}.svg",
        [punt_zone(G_GRAF, 3, 3, 30), punt_zone(G_GRAF, 15, 3, 30)],
        "Het water stijgt het snelst als het de evenwichtslijn naar boven kruist: om 3 uur en om 15 uur.",
    ),
    met_prent(f"{G_GRAF}.svg", tabel(
        "Lees de kenmerken af.",
        [
            ("Periode", "12 uur"),
            ("Amplitude", "2 m"),
            ("Evenwichtslijn", "h = 3"),
        ],
        "Van hoogwater tot hoogwater duurt 12 uur. Het water gaat 2 m boven en onder de evenwichtslijn h = 3.",
        kolommen=["2 m", "h = 3", "12 uur"],
    )),
    met_prent(f"{G_GRAF}.svg", mk(
        r"Welk voorschrift past bij de grafiek?",
        [
            r"\(h(t) = 2 \sin \frac{\pi}{6}(t - 3) + 3\)",
            r"\(h(t) = 3 \sin \frac{\pi}{6}(t - 3) + 2\)",
            r"\(h(t) = 2 \sin 12(t - 3) + 3\)",
            r"\(h(t) = 2 \sin \frac{\pi}{6}(t + 3) + 3\)",
        ],
        0,
        r"\(a = 2\), \(d = 3\), \(b = \frac{2\pi}{12} = \frac{\pi}{6}\). De grafiek kruist stijgend de evenwichtslijn in \(t = 3\), dus \(c = 3\).",
    )),
    met_prent(f"{G_GRAF}.svg", mk(
        "Een boot heeft minstens 4 m water nodig. Hoe lang kan hij per periode van 12 uur varen?",
        [r"\(4\) uur", r"\(6\) uur", r"\(2\) uur", r"\(8\) uur"],
        0,
        r"\(2 \sin \frac{\pi}{6}(t - 3) + 3 = 4\) geeft \(\sin = \frac{1}{2}\): \(t - 3 = 1\) of \(t - 3 = 5\). Van \(t = 4\) tot \(t = 8\): \(4\) uur.",
    )),
    inv(
        r"Hoeveel graden is \(\dfrac{7\pi}{9}\) rad?",
        "140",
        r"\(\frac{7\pi}{9} \cdot \frac{180°}{\pi} = 7 \cdot 20° = 140°\).",
    ),
    mk(
        r"Hoeveel radialen is \(225°\)?",
        [r"\(\dfrac{5\pi}{4}\)", r"\(\dfrac{4\pi}{5}\)", r"\(\dfrac{9\pi}{4}\)", r"\(\dfrac{5\pi}{8}\)"],
        0,
        r"\(225 \cdot \frac{\pi}{180} = \frac{225\pi}{180} = \frac{5\pi}{4}\).",
    ),
    tabel(
        "Juist of fout voor elke hoek \u03b1?",
        [
            (r"\(\sin\left(\pi - \alpha\right) = \sin \alpha\)", J),
            (r"\(\sin(-\alpha) = \sin \alpha\)", F),
            (r"\(\sin(\alpha + 2\pi) = \sin \alpha\)", J),
            (r"\(\sin 2\alpha = 2 \sin \alpha\)", F),
        ],
        r"Hoeken \(\alpha\) en \(\pi - \alpha\) liggen symmetrisch rond de \(y\)-as: zelfde hoogte. \(-\alpha\) spiegelt rond de \(x\)-as, dus de sinus wisselt van teken.",
    ),
    mk(
        r"Wat is de periode van \(f(x) = 5 \sin\left(\dfrac{\pi}{4} x\right)\)?",
        [r"\(8\)", r"\(\dfrac{\pi}{4}\)", r"\(4\)", r"\(\dfrac{\pi}{2}\)"],
        0,
        r"\(p = \frac{2\pi}{b} = \frac{2\pi}{\pi/4} = 8\).",
    ),
    mk(
        r"Wat is het bereik van \(f(x) = -3 \sin 2x + 1\)?",
        [r"\([-2, 4]\)", r"\([-4, 2]\)", r"\([-3, 3]\)", r"\([1, 4]\)"],
        0,
        r"Amplitude \(|-3| = 3\) rond de evenwichtslijn \(y = 1\): van \(1 - 3\) tot \(1 + 3\). Het minteken spiegelt, maar verandert het bereik niet.",
    ),
    koppel(
        r"Koppel de parameter in \(f(x) = a \sin b(x - c) + d\) aan wat hij bepaalt.",
        [
            [r"\(|a|\)", "De amplitude"],
            [r"\(b\)", r"De periode, via \(\frac{2\pi}{b}\)"],
            [r"\(c\)", "De faseverschuiving"],
            [r"\(d\)", "De evenwichtslijn"],
        ],
        ["De nulwaarden van sin x"],
        "Elke parameter hoort bij één transformatie van sin x.",
    ),
    sorteer(
        r"Verandert de transformatie de periode van \(\sin x\) of niet?",
        ["Verandert de periode", "Verandert de periode niet"],
        [
            [r"\(\sin x \to \sin 3x\)", "Verandert de periode"],
            [r"\(\sin x \to 3 \sin x\)", "Verandert de periode niet"],
            [r"\(\sin x \to \sin x + 3\)", "Verandert de periode niet"],
            [r"\(\sin x \to \sin\frac{x}{3}\)", "Verandert de periode"],
            [r"\(\sin x \to \sin(x - 3)\)", "Verandert de periode niet"],
        ],
        "Enkel een horizontale uitrekking (de factor b) verandert de periode.",
    ),
    mk(
        r"Een sinusfunctie heeft maximum \(14\) in \(x = 2\) en het eerstvolgende minimum \(4\) in \(x = 7\). Wat is de periode?",
        [r"\(10\)", r"\(5\)", r"\(7\)", r"\(14\)"],
        0,
        r"Van maximum tot minimum is een halve periode: \(7 - 2 = 5\), dus \(p = 10\).",
    ),
    inv(
        r"Bij dezelfde functie (maximum \(14\), minimum \(4\)): wat is de amplitude?",
        "5",
        r"\(\frac{14 - 4}{2} = 5\).",
    ),
    keuze(
        "Een sinusfunctie met periode 0,8 s heeft een frequentie van [[*1,25|0,8|8]] trillingen per seconde. Een kortere periode geeft een [[*hogere|lagere|gelijke]] frequentie.",
        "Frequentie = 1 / periode.",
    ),
    mk(
        r"Hoeveel oplossingen heeft \(\sin x = 0{,}3\) op \([0, 4\pi]\)?",
        [r"\(4\)", r"\(2\)", r"\(1\)", r"\(8\)"],
        0,
        r"Op \([0, 2\pi]\) zijn er twee: één in het eerste en één in het tweede kwadrant. \([0, 4\pi]\) bevat twee perioden.",
    ),
    volgorde(
        r"Zet de sinuswaarden van klein naar groot.",
        [r"\(\sin\dfrac{3\pi}{2}\)", r"\(\sin\dfrac{7\pi}{6}\)", r"\(\sin \pi\)", r"\(\sin\dfrac{\pi}{6}\)", r"\(\sin\dfrac{\pi}{2}\)"],
        r"\(-1\), \(-\frac{1}{2}\), \(0\), \(\frac{1}{2}\) en \(1\).",
    ),
    sleep(
        "De hoogte van een bakje in een reuzenrad gaat op en neer rond de hoogte van de [[as]]. Die hoogte is de [[evenwichtslijn]], en de straal van het rad is de [[amplitude]].",
        ["periode", "frequentie"],
        "Het bakje gaat een straal boven en een straal onder de as.",
    ),
    mk(
        r"Een leerling zet zijn rekentoestel in graden en berekent \(\sin \frac{\pi}{6}\). Wat gebeurt er?",
        [
            r"Hij krijgt ongeveer \(0{,}009\), want het toestel neemt \(0{,}52°\)",
            r"Hij krijgt \(0{,}5\), want het toestel herkent \(\pi\)",
            r"Het toestel geeft een foutmelding",
            r"Hij krijgt \(30\)",
        ],
        0,
        r"\(\frac{\pi}{6} \approx 0{,}52\). In graden is dat een heel kleine hoek. Zet het toestel in radialen.",
    ),
    tabel(
        r"Juist of fout over \(f(x) = 4 \sin 2\left(x - \dfrac{\pi}{4}\right) - 1\)?",
        [
            (r"De periode is \(\pi\).", J),
            (r"Het maximum is \(3\).", J),
            (r"De evenwichtslijn is \(y = 4\).", F),
            (r"De grafiek is \(\frac{\pi}{4}\) naar links verschoven ten opzichte van \(4 \sin 2x - 1\).", F),
        ],
        r"\(\frac{2\pi}{2} = \pi\). Maximum \(-1 + 4 = 3\). Evenwichtslijn \(y = -1\). \(x - \frac{\pi}{4}\) schuift naar rechts.",
    ),
    met_prent(f"{C_GRAF}.svg", mk(
        "Bij welk beeldpunt is de sinus van de hoek het kleinst?",
        ["S", "R", "Q", "P"],
        0,
        r"De sinus is de \(y\)-coördinaat. S ligt het laagst: \(\sin \frac{7\pi}{4} \approx -0{,}71\), terwijl \(\sin \frac{7\pi}{6} = -0{,}5\).",
    )),
    mk(
        r"Een sinusfunctie heeft periode \(24\). Hoeveel is \(b\) in \(a \sin b(x - c) + d\)?",
        [r"\(\dfrac{\pi}{12}\)", r"\(24\)", r"\(\dfrac{\pi}{24}\)", r"\(12\pi\)"],
        0,
        r"\(b = \frac{2\pi}{p} = \frac{2\pi}{24} = \frac{\pi}{12}\).",
    ),
    open_(
        r"Leg uit hoe je de grafiek van \(\sin x\) opbouwt vanuit de goniometrische cirkel.",
        r"Je laat een punt over de cirkel lopen. Op de \(x\)-as van de grafiek zet je de hoek in radialen, en als hoogte neem je de \(y\)-coördinaat van het beeldpunt. Na één toer (\(2\pi\)) begint alles opnieuw: dat is de periode.",
        "De sinus is de y-coördinaat van het beeldpunt.",
    ),
    casus(
        r"Een reuzenrad heeft een diameter van \(50\) m. De as staat op \(28\) m hoogte. Eén toer duurt \(8\) minuten. Op \(t = 0\) passeert een bakje stijgend de hoogte van de as.",
        [
            mk(
                "Welk voorschrift geeft de hoogte h (m) na t minuten?",
                [r"\(h(t) = 25 \sin \frac{\pi}{4} t + 28\)", r"\(h(t) = 50 \sin \frac{\pi}{4} t + 28\)", r"\(h(t) = 25 \sin 8t + 28\)", r"\(h(t) = 28 \sin \frac{\pi}{4} t + 25\)"],
                0,
                r"Amplitude = straal = \(25\). \(b = \frac{2\pi}{8} = \frac{\pi}{4}\). Evenwichtslijn \(28\).",
            ),
            mk(
                "Hoe hoog is het bakje na 6 minuten?",
                [r"\(3\) m", r"\(53\) m", r"\(28\) m", r"\(15{,}5\) m"],
                0,
                r"\(\sin \frac{6\pi}{4} = \sin \frac{3\pi}{2} = -1\): het laagste punt, \(28 - 25 = 3\) m.",
            ),
            mk(
                "Na hoeveel minuten is het bakje voor het eerst op het hoogste punt?",
                [r"\(2\)", r"\(4\)", r"\(8\)", r"\(6\)"],
                0,
                r"Een kwart toer na het stijgend passeren van de as: \(\frac{8}{4} = 2\) minuten.",
            ),
        ],
    ),
]
