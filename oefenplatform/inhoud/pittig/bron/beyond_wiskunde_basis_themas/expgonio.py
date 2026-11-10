"""Bedrijfswetenschappen: exponentiële en goniometrische vergelijkingen — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

S_GRAF = venster("expgonio-sinus", 0, math.pi, -4.6, 4.6, math.pi / 12, 1)
E_GRAF = venster("expgonio-exp", -1, 4, 0, 14, 0.5, 1)

_PI12 = {1: "π/12", 2: "π/6", 3: "π/4", 4: "π/3", 5: "5π/12", 6: "π/2", 7: "7π/12", 8: "2π/3", 9: "3π/4", 10: "5π/6", 11: "11π/12", 12: "π"}

GRAFIEKEN = [
    dict(naam=S_GRAF, titel="De grafieken van y = 4 sin 2x en y = 2",
         krommen=[(lambda x: 4 * math.sin(2 * x), "oranje", "", (0, math.pi)), (lambda x: 2, "blauw", "", (0, math.pi))],
         ijk_x=math.pi / 6, ijk_y=1, xnamen={k * (math.pi / 6): _PI12[2 * k] for k in range(1, 7)}),
    dict(naam=E_GRAF, titel="De grafieken van y = 2ˣ en y = 6",
         krommen=[(lambda x: 2 ** x, "groen", "", (-1, 3.8)), (lambda x: 6, "blauw", "", (-1, 4))],
         ijk_x=1, ijk_y=2),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen bij exponentiële en goniometrische vergelijkingen") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        r"Klik op een snijpunt dat een oplossing geeft van \(4 \sin 2x = 2\) in \([0, \pi]\).",
        f"{S_GRAF}.svg",
        [punt_zone(S_GRAF, math.pi / 12, 2), punt_zone(S_GRAF, 5 * math.pi / 12, 2)],
        r"\(\sin 2x = \frac{1}{2}\): \(2x = \frac{\pi}{6}\) of \(2x = \frac{5\pi}{6}\), dus \(x = \frac{\pi}{12}\) of \(x = \frac{5\pi}{12}\).",
    ),
    met_prent(f"{S_GRAF}.svg", mk(
        r"Los algebraïsch op in \([0, \pi]\): \(4 \sin 2x = -4\).",
        [r"\(\left\{\frac{3\pi}{2}\right\}\)", r"\(\left\{\frac{3\pi}{4}\right\}\)", r"\(\left\{\frac{\pi}{4}, \frac{3\pi}{4}\right\}\)", r"\(\varnothing\)"],
        1,
        r"\(\sin 2x = -1\) geeft \(2x = \frac{3\pi}{2} + k2\pi\), dus \(x = \frac{3\pi}{4} + k\pi\). Enkel \(\frac{3\pi}{4}\) ligt in \([0, \pi]\): het dal van de grafiek.",
    )),
    klik(
        r"Klik op het punt waarvan de x-coördinaat de oplossing is van \(2^x = 6\).",
        f"{E_GRAF}.svg",
        [punt_zone(E_GRAF, math.log(6, 2), 6, 30)],
        r"Het snijpunt van \(y = 2^x\) met \(y = 6\) ligt bij \(x = \log_2 6 = \frac{\log 6}{\log 2} \approx 2{,}58\).",
    ),
    mk(
        r"Los op: \(3 \cdot 2^x - 24 = 0\).",
        [r"\(x = 8\)", r"\(x = 4\)", r"\(x = 3\)", r"\(x = \log 24\)"],
        2,
        r"\(2^x = 8 = 2^3\).",
    ),
    inv(
        r"Los op: \(5^x = 40\). Rond af op twee decimalen.",
        "2,29",
        r"\(x = \frac{\log 40}{\log 5} \approx \frac{1{,}6021}{0{,}6990} \approx 2{,}29\).",
    ),
    mk(
        r"Los op: \(7 \cdot 10^x = 70\,000\).",
        [r"\(x = 10\,000\)", r"\(x = 3\)", r"\(x = 5\)", r"\(x = 4\)"],
        3,
        r"\(10^x = 10\,000 = 10^4\).",
    ),
    mk(
        r"Los op: \(100 \cdot 0{,}9^t = 50\).",
        [r"\(t \approx -6{,}58\)", r"\(t \approx 0{,}15\)", r"\(t \approx 6{,}58\)", r"\(t \approx 5{,}56\)"],
        2,
        r"\(0{,}9^t = 0{,}5\), dus \(t = \frac{\log 0{,}5}{\log 0{,}9} \approx \frac{-0{,}301}{-0{,}0458}\).",
    ),
    mk(
        r"Los op: \(2^{x+1} = 16\).",
        [r"\(x = 4\)", r"\(x = 7\)", r"\(x = 8\)", r"\(x = 3\)"],
        3,
        r"\(16 = 2^4\), dus \(x + 1 = 4\).",
    ),
    tabel(
        "Juist of fout over logaritmen?",
        [
            (r"\(\log(a \cdot b) = \log a + \log b\)", J),
            (r"\(\log(a + b) = \log a + \log b\)", F),
            (r"\(\log(a^n) = n \cdot \log a\)", J),
            (r"\(\log\dfrac{a}{b} = \dfrac{\log a}{\log b}\)", F),
        ],
        r"Een logaritme maakt van vermenigvuldigen optellen en van een macht een product. Voor een som of een quotiënt van logaritmen bestaat zo'n regel niet.",
    ),
    keuze(
        "Om a^x = b op te lossen, neem je van beide leden de [[*logaritme|vierkantswortel|sinus]]. Dan is x gelijk aan [[*log b gedeeld door log a|log a gedeeld door log b|b gedeeld door a]].",
        r"\(\log a^x = \log b\) geeft \(x \log a = \log b\).",
    ),
    sorteer(
        "Heeft de vergelijking een reële oplossing?",
        ["Ja", "Nee"],
        [
            [r"\(4 \cdot 2^x = 1\)", "Ja"],
            [r"\(4 \cdot 2^x = -1\)", "Nee"],
            [r"\(3 \sin x = 2\)", "Ja"],
            [r"\(3 \sin x = 4\)", "Nee"],
            [r"\(0{,}5^x - 2 = 0\)", "Ja"],
            [r"\(2 \sin 3x + 5 = 0\)", "Nee"],
        ],
        r"Een macht met positief grondtal is altijd positief. Een sinus ligt altijd tussen \(-1\) en \(1\).",
    ),
    mk(
        r"Los op in \([0, 2\pi]\): \(2 \sin x = 1\).",
        [r"\(\left\{\frac{\pi}{6}, \frac{11\pi}{6}\right\}\)", r"\(\left\{\frac{\pi}{6}, \frac{5\pi}{6}\right\}\)", r"\(\left\{\frac{\pi}{3}, \frac{2\pi}{3}\right\}\)", r"\(\left\{\frac{\pi}{6}\right\}\)"],
        1,
        r"\(\sin x = \frac{1}{2}\) in het eerste kwadrant (\(\frac{\pi}{6}\)) en in het tweede (\(\pi - \frac{\pi}{6}\)).",
    ),
    mk(
        r"Wat zijn alle oplossingen van \(\sin x = -\dfrac{\sqrt{2}}{2}\)?",
        [
            r"\(x = -\frac{\pi}{4} + k2\pi\) of \(x = \frac{5\pi}{4} + k2\pi\)",
            r"\(x = -\frac{\pi}{4} + k\pi\)",
            r"\(x = \frac{\pi}{4} + k2\pi\) of \(x = \frac{3\pi}{4} + k2\pi\)",
            r"\(x = -\frac{\pi}{4} + k2\pi\) of \(x = \frac{3\pi}{4} + k2\pi\)",
        ],
        0,
        r"Eén oplossing is \(-\frac{\pi}{4}\). De tweede is \(\pi - \left(-\frac{\pi}{4}\right) = \frac{5\pi}{4}\). Daarbij telkens veelvouden van \(2\pi\).",
    ),
    mk(
        r"Los op in \(\left[0, \dfrac{\pi}{2}\right]\): \(\sin 3x = 1\).",
        [r"\(\dfrac{\pi}{2}\)", r"\(\dfrac{\pi}{3}\)", r"\(\dfrac{\pi}{9}\)", r"\(\dfrac{\pi}{6}\)"],
        3,
        r"\(3x = \frac{\pi}{2} + k2\pi\), dus \(x = \frac{\pi}{6} + k\frac{2\pi}{3}\). Enkel \(\frac{\pi}{6}\) ligt in het interval.",
    ),
    mk(
        r"Los op in \([0, 2\pi]\): \(3 \sin\left(x - \dfrac{\pi}{4}\right) + 3 = 0\).",
        [r"\(\dfrac{5\pi}{4}\)", r"\(\dfrac{7\pi}{4}\)", r"\(\dfrac{3\pi}{4}\)", r"\(\dfrac{\pi}{4}\)"],
        1,
        r"\(\sin\left(x - \frac{\pi}{4}\right) = -1\), dus \(x - \frac{\pi}{4} = \frac{3\pi}{2}\).",
    ),
    volgorde(
        r"Zet de stappen om \(a \sin b(x - c) + d = 0\) op te lossen in de goede volgorde.",
        [
            r"Isoleer de sinus: \(\sin b(x - c) = -\frac{d}{a}\)",
            r"Zoek een hoek \(\alpha\) met die sinus",
            r"Schrijf \(b(x - c) = \alpha + k2\pi\) of \(b(x - c) = \pi - \alpha + k2\pi\)",
            "Los op naar x en kies de oplossingen in het gevraagde interval",
        ],
        "Eerst de sinus alleen, dan de hoeken, dan terugrekenen naar x.",
    ),
    koppel(
        "Koppel de vergelijking aan haar oplossing.",
        [
            [r"\(2^x = 32\)", r"\(5\)"],
            [r"\(2^x = \frac{1}{8}\)", r"\(-3\)"],
            [r"\(10^x = 0{,}01\)", r"\(-2\)"],
            [r"\(3^x = 1\)", r"\(0\)"],
        ],
        [r"\(\frac{1}{3}\)"],
        r"Schrijf het rechterlid als macht van hetzelfde grondtal. Elk getal tot de macht \(0\) is \(1\).",
    ),
    sleep(
        r"De periode van \(\sin 2x\) is [[π]]. Daarom heeft \(\sin 2x = 0{,}3\) op \([0, 2\pi]\) [[vier]] oplossingen.",
        ["2π", "twee", "acht"],
        r"\(\frac{2\pi}{2} = \pi\): op \([0, 2\pi]\) passen twee perioden, met in elke periode twee oplossingen.",
    ),
    mk(
        "Een auto verliest elk jaar 15 % van zijn waarde. Na hoeveel jaar is hij nog de helft waard?",
        [r"Na ongeveer \(3{,}3\) jaar", r"Na ongeveer \(4{,}3\) jaar", r"Na ongeveer \(6{,}7\) jaar", r"Na ongeveer \(7{,}5\) jaar"],
        1,
        r"\(0{,}85^t = 0{,}5\), dus \(t = \frac{\log 0{,}5}{\log 0{,}85} \approx 4{,}27\).",
    ),
    inv(
        "Een bevolking groeit met 2 % per jaar. Na hoeveel volle jaren is ze voor het eerst minstens verdubbeld?",
        "36",
        r"\(1{,}02^t = 2\) geeft \(t = \frac{\log 2}{\log 1{,}02} \approx 35{,}003\). Na 35 jaar is het net nog niet, na 36 jaar wel.",
    ),
    mk(
        "Een stof halveert elke 8 uur. Na hoeveel uur is er nog 10 % over?",
        [r"Na \(80\) uur", r"Na ongeveer \(13{,}3\) uur", r"Na \(40\) uur", r"Na ongeveer \(26{,}6\) uur"],
        3,
        r"\(0{,}5^{t/8} = 0{,}1\), dus \(\frac{t}{8} = \frac{\log 0{,}1}{\log 0{,}5} \approx 3{,}32\).",
    ),
    tabel(
        "Juist of fout over goniometrische vergelijkingen?",
        [
            (r"\(\sin x = 1{,}2\) heeft geen oplossing.", J),
            (r"\(\sin x = 0{,}5\) heeft op \([0, 2\pi]\) twee oplossingen.", J),
            (r"Als \(\sin \alpha = \sin \beta\), dan is \(\alpha = \beta\).", F),
            (r"\(\sin x = -1\) heeft op \([0, 2\pi]\) twee oplossingen.", F),
        ],
        r"Ook \(\pi - \alpha\) en \(\alpha + 2\pi\) hebben dezelfde sinus. \(-1\) wordt op \([0, 2\pi]\) enkel in \(\frac{3\pi}{2}\) bereikt.",
    ),
    open_(
        r"Leg uit waarom je bij \(\sin x = a\) (met \(-1 < a < 1\)) twee families van oplossingen krijgt.",
        r"Op de goniometrische cirkel zijn er twee beeldpunten met y-coördinaat a: bij \(\alpha\) en bij \(\pi - \alpha\), symmetrisch rond de y-as. Omdat de sinus periodiek is met periode \(2\pi\), komt bij elk van beide nog \(k2\pi\).",
        "Denk aan de cirkel: twee punten op dezelfde hoogte.",
    ),
    mk(
        r"Los op: \(\log x = 2\).",
        [r"\(x = 20\)", r"\(x = 0{,}01\)", r"\(x = 2\)", r"\(x = 100\)"],
        3,
        r"\(\log x = 2\) betekent \(10^2 = x\).",
    ),
    mk(
        r"De waterhoogte is \(h(t) = 1{,}5 \sin\left(\frac{\pi}{6}(t - 2)\right) + 3\) (m, t in uur). Wanneer is het water voor het eerst na \(t = 2\) op 3,75 m?",
        [r"Op \(t = 2{,}5\)", r"Op \(t = 5\)", r"Op \(t = 7\)", r"Op \(t = 3\)"],
        3,
        r"\(\sin\left(\frac{\pi}{6}(t - 2)\right) = 0{,}5\), dus \(\frac{\pi}{6}(t - 2) = \frac{\pi}{6}\) en \(t = 3\).",
    ),
    mk(
        r"Los op: \(3^{2x} = 81\).",
        [r"\(x = 4\)", r"\(x = 2\)", r"\(x = \frac{1}{2}\)", r"\(x = 3\)"],
        1,
        r"\(81 = 3^4\), dus \(2x = 4\).",
    ),
    mk(
        r"Los op: \(4^x = 2^{x+3}\).",
        [r"\(x = 1\)", r"\(x = -3\)", r"\(x = 6\)", r"\(x = 3\)"],
        3,
        r"\(4^x = 2^{2x}\), dus \(2x = x + 3\).",
    ),
    casus(
        r"Een patiënt krijgt 200 mg van een medicijn. Elk uur wordt 12 % afgebroken: \(C(t) = 200 \cdot 0{,}88^t\).",
        [
            mk(
                "Na hoeveel uur is er nog 100 mg?",
                [r"Na ongeveer \(4{,}2\) uur", r"Na ongeveer \(5{,}4\) uur", r"Na ongeveer \(8{,}3\) uur", r"Na \(6\) uur"],
                1,
                r"\(0{,}88^t = 0{,}5\), dus \(t = \frac{\log 0{,}5}{\log 0{,}88} \approx 5{,}42\).",
            ),
            inv(
                "Hoeveel mg zit er na 3 uur nog in het bloed? Rond af op een geheel getal.",
                "136",
                r"\(200 \cdot 0{,}88^3 = 200 \cdot 0{,}681472 \approx 136\).",
            ),
            mk(
                "Een nieuwe dosis is nodig als er minder dan 50 mg over is. Na hoeveel uur is dat?",
                [r"Na ongeveer \(16{,}3\) uur", r"Na ongeveer \(12{,}5\) uur", r"Na ongeveer \(10{,}8\) uur", r"Na ongeveer \(8{,}1\) uur"],
                2,
                r"\(0{,}88^t = 0{,}25\), dus \(t = \frac{\log 0{,}25}{\log 0{,}88} \approx 10{,}84\).",
            ),
        ],
    ),
]
