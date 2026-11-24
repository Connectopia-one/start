"""Goniometrische functies en goniometrie — pittig (🌍 Beyond doorstroom)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("goniometrie-sinus-bey", 0, 7, -2, 4)


def _f(x):
    return 2 * math.sin(x) + 1


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f(x) = 2 sin x + 1 (x in radialen)", krommen=[(_f, "groen", "f", (0, 2 * math.pi))],
         stippel=[("h", 1), ("v", math.pi), ("v", 2 * math.pi)], labelplek={"f": (0.6, 3.4)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="sinusgrafiek 2 sin x + 1 over één periode, met evenwichtslijn y = 1", vragen="klikvragen over amplitude, extrema en nulwaarden")]

VRAGEN = [
    klik(
        "Klik op het maximum van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, math.pi / 2, 3)],
        r"\(\sin x = 1\) bij \(x = \tfrac{\pi}{2}\): \(f = 2 + 1 = 3\).",
    ),
    klik(
        "Klik op het minimum van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3 * math.pi / 2, -1)],
        r"\(\sin x = -1\) bij \(x = \tfrac{3\pi}{2} \approx 4{,}71\): \(f = -2 + 1 = -1\).",
    ),
    klik(
        "Klik op de kleinste nulwaarde van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 7 * math.pi / 6, 0)],
        r"\(2\sin x + 1 = 0\) geeft \(\sin x = -\tfrac{1}{2}\): \(x = \tfrac{7\pi}{6} \approx 3{,}67\) of \(x = \tfrac{11\pi}{6} \approx 5{,}76\).",
    ),
    klik(
        r"Klik in de strook waar \(f(x) > 1\).",
        f"{GRAF}.svg",
        [strook_zone(GRAF, 0.2, math.pi - 0.2)],
        r"Boven de evenwichtslijn \(y = 1\): waar \(\sin x > 0\), dus tussen \(0\) en \(\pi\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek. Welk getal hoort erbij?",
        [("de amplitude", "2"), ("de evenwichtslijn y = …", "1"), ("de grootste waarde", "3"), ("de kleinste waarde", "−1")],
        "De amplitude is de afstand van de evenwichtslijn tot een top.",
        kolommen=["2", "1", "3", "−1"],
    )),
    tabel(
        "Zet om. Welke waarde hoort erbij?",
        [(r"\(135^\circ\)", r"\(\tfrac{3\pi}{4}\)"), (r"\(\tfrac{5\pi}{6}\)", r"\(150^\circ\)"), (r"\(210^\circ\)", r"\(\tfrac{7\pi}{6}\)"), (r"\(\tfrac{\pi}{12}\)", r"\(15^\circ\)")],
        r"Graden maal \(\tfrac{\pi}{180}\) geeft radialen.",
        kolommen=[r"\(\tfrac{3\pi}{4}\)", r"\(150^\circ\)", r"\(\tfrac{7\pi}{6}\)", r"\(15^\circ\)"],
    ),
    tabel(
        "Juist of fout?",
        [(r"\(\sin 150^\circ = \sin 30^\circ\)", J), (r"\(\cos 120^\circ = \cos 60^\circ\)", F), (r"\(\sin(-45^\circ) = -\sin 45^\circ\)", J), (r"\(\cos(-60^\circ) = -\tfrac{1}{2}\)", F), (r"\(\tan 225^\circ = 1\)", J)],
        r"Supplementaire hoeken: zelfde sinus, tegengestelde cosinus. Tegengestelde hoeken: zelfde cosinus. \(\tan\) heeft periode \(180^\circ\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat is de periode van \(y = 3\sin\left(\tfrac{x}{2}\right)\)?",
        [r"\(4\pi\)", r"\(\pi\)", r"\(2\pi\)", r"\(6\pi\)"],
        0,
        r"Periode \(= \tfrac{2\pi}{b}\) met \(b = \tfrac{1}{2}\).",
    ),
    koppel(
        "Verbind het voorschrift met de beschrijving.",
        [(r"\(y = \sin(x - \tfrac{\pi}{2})\)", r"\(\tfrac{\pi}{2}\) naar rechts"), (r"\(y = -2\sin x\)", "amplitude 2, gespiegeld"), (r"\(y = \sin 4x\)", r"periode \(\tfrac{\pi}{2}\)"), (r"\(y = \sin x - 3\)", "evenwichtslijn y = −3")],
        ["amplitude −2"],
        "Een amplitude is altijd positief: het minteken spiegelt.",
    ),
    mk(
        r"In driehoek ABC is \(a = 7\), \(b = 5\) en \(\hat{C} = 60^\circ\). Hoe lang is \(c\)?",
        [r"\(\sqrt{39}\)", r"\(\sqrt{74}\)", r"\(6\)", r"\(\sqrt{109}\)"],
        0,
        r"\(c^{2} = 49 + 25 - 2 \cdot 35 \cdot \tfrac{1}{2} = 39\).",
    ),
    inv(
        r"\(\sin x = \tfrac{3}{5}\) en \(x\) ligt in het tweede kwadrant. Hoeveel is \(\cos x\)?",
        ["-0,8", "-0.8", "-4/5", "−0,8", "−4/5"],
        r"\(\cos^{2}x = 1 - \tfrac{9}{25} = \tfrac{16}{25}\). In het tweede kwadrant is de cosinus negatief.",
    ),
    mk(
        r"Los op in \(\left[0, 2\pi\right[\): \(2\cos x = 1\).",
        [r"\(x = \tfrac{\pi}{3}\) of \(x = \tfrac{5\pi}{3}\)", r"\(x = \tfrac{\pi}{3}\)", r"\(x = \tfrac{\pi}{6}\) of \(x = \tfrac{5\pi}{6}\)", r"\(x = \tfrac{\pi}{3}\) of \(x = \tfrac{2\pi}{3}\)"],
        0,
        r"\(\cos x = \tfrac{1}{2}\): \(\tfrac{\pi}{3}\) en de tegengestelde hoek \(-\tfrac{\pi}{3} + 2\pi = \tfrac{5\pi}{3}\).",
    ),
    sorteer(
        "Is dit een geldige formule?",
        ["Geldig", "Niet geldig"],
        [(r"\(\sin 2x = 2\sin x\cos x\)", "Geldig"), (r"\(\cos 2x = \cos^{2}x - \sin^{2}x\)", "Geldig"), (r"\(\sin(a + b) = \sin a + \sin b\)", "Niet geldig"),
         (r"\(\cos 2x = 1 - 2\sin^{2}x\)", "Geldig"), (r"\(\tan x = \tfrac{\cos x}{\sin x}\)", "Niet geldig"), (r"\(\sin^{2}x = 1 - \cos^{2}x\)", "Geldig")],
        r"\(\sin(a + b) = \sin a\cos b + \cos a\sin b\) en \(\tan x = \tfrac{\sin x}{\cos x}\).",
    ),
    casus(
        r"De waterhoogte in een haven (in m) is \(h(t) = 2{,}5\sin\left(\tfrac{\pi}{6}t\right) + 4\), met \(t\) in uren na middernacht.",
        [
            inv("Wat is de hoogste waterstand, in meter?", ["6,5", "6.5"], r"\(2{,}5 + 4\)."),
            inv("Om de hoeveel uur herhaalt het getij zich?", ["12"], r"Periode \(\tfrac{2\pi}{\pi/6} = 12\)."),
            mk("Een boot heeft minstens 5,25 m water nodig. Wanneer kan hij voor het eerst binnen?", ["om 1 uur", "om 3 uur", "om middernacht", "om 6 uur"], 0,
               r"\(2{,}5\sin\left(\tfrac{\pi}{6}t\right) = 1{,}25\) geeft \(\sin = \tfrac{1}{2}\), dus \(\tfrac{\pi}{6}t = \tfrac{\pi}{6}\): \(t = 1\)."),
        ],
    ),
    keuze(
        r"Bij \(y = a\sin(b(x - c)) + d\) bepaalt \(b\) de [[*periode|amplitude|evenwichtslijn]] en \(d\) de [[*evenwichtslijn|periode|faseverschuiving]].",
        r"Periode \(\tfrac{2\pi}{|b|}\), amplitude \(|a|\), evenwichtslijn \(y = d\).",
    ),
    mk(
        r"Een booglengte op een cirkel met straal 10 cm hoort bij een middelpuntshoek van \(1{,}5\) rad. Hoe lang is de boog?",
        ["15 cm", "1,5 cm", "6,67 cm", "150 cm"],
        0,
        r"Booglengte \(= r \cdot \alpha\) in radialen: \(10 \cdot 1{,}5 = 15\).",
    ),
    tabel(
        r"Bereken exact.",
        [(r"\(\sin\tfrac{\pi}{4}\)", r"\(\tfrac{\sqrt{2}}{2}\)"), (r"\(\cos\tfrac{\pi}{6}\)", r"\(\tfrac{\sqrt{3}}{2}\)"), (r"\(\tan\tfrac{\pi}{3}\)", r"\(\sqrt{3}\)"), (r"\(\sin\tfrac{7\pi}{6}\)", r"\(-\tfrac{1}{2}\)")],
        r"\(\tfrac{7\pi}{6} = \pi + \tfrac{\pi}{6}\): de sinus wisselt van teken.",
        kolommen=[r"\(\tfrac{\sqrt{2}}{2}\)", r"\(\tfrac{\sqrt{3}}{2}\)", r"\(\sqrt{3}\)", r"\(-\tfrac{1}{2}\)"],
    ),
    inv(
        r"Hoeveel oplossingen heeft \(\sin x = 0{,}3\) in \(\left[0, 4\pi\right]\)?",
        ["4", "vier"],
        r"Per periode \(2\pi\) twee oplossingen, en het interval bevat twee periodes.",
    ),
    mk(
        r"Vereenvoudig \(\dfrac{\sin 2x}{2\cos x}\) voor \(\cos x \neq 0\).",
        [r"\(\sin x\)", r"\(\tan x\)", r"\(\cos x\)", r"\(\sin x\cos x\)"],
        0,
        r"\(\tfrac{2\sin x\cos x}{2\cos x} = \sin x\).",
    ),
    sleep(
        r"Op de goniometrische cirkel is het beeldpunt van \(\alpha\) het punt [[\((\cos\alpha, \sin\alpha)\)]]. Daaruit volgt meteen de grondformule [[\(\sin^{2}\alpha + \cos^{2}\alpha = 1\)]].",
        [r"\((\sin\alpha, \cos\alpha)\)", r"\(\sin\alpha + \cos\alpha = 1\)"],
        "De afstand tot de oorsprong is 1: Pythagoras.",
    ),
    mk(
        r"In driehoek ABC is \(\hat{A} = 40^\circ\), \(\hat{B} = 75^\circ\) en \(a = 8\). Hoe lang is \(b\), afgerond?",
        ["12,0", "5,3", "9,4", "6,7"],
        0,
        r"Sinusregel: \(b = \dfrac{8\sin 75^\circ}{\sin 40^\circ} \approx \dfrac{7{,}73}{0{,}643} \approx 12{,}0\).",
    ),
    tabel(
        "In welk kwadrant ligt de hoek, als…",
        [(r"\(\sin\alpha > 0\) en \(\cos\alpha < 0\)", "II"), (r"\(\sin\alpha < 0\) en \(\cos\alpha < 0\)", "III"), (r"\(\sin\alpha < 0\) en \(\cos\alpha > 0\)", "IV"), (r"\(\tan\alpha > 0\) en \(\sin\alpha > 0\)", "I")],
        "Cosinus is de x-coördinaat, sinus de y-coördinaat van het beeldpunt.",
        kolommen=["I", "II", "III", "IV"],
    ),
    volgorde(
        "Zet van klein naar groot.",
        [r"\(\cos\pi\)", r"\(\sin\tfrac{5\pi}{4}\)", r"\(\cos\tfrac{\pi}{2}\)", r"\(\sin\tfrac{\pi}{6}\)", r"\(\tan\tfrac{\pi}{3}\)"],
        r"\(-1\), \(-\tfrac{\sqrt{2}}{2}\), \(0\), \(\tfrac{1}{2}\), \(\sqrt{3}\).",
    ),
    inv(
        r"Hoeveel is \(\sin 15^\circ\cos 15^\circ\)? Typ als breuk.",
        ["1/4", "0,25", "0.25"],
        r"\(\tfrac{1}{2}\sin 30^\circ = \tfrac{1}{2} \cdot \tfrac{1}{2}\).",
    ),
    mk(
        r"Welk voorschrift hoort bij een sinusgrafiek met maximum 7, minimum 1 en periode \(\pi\), die stijgend door de evenwichtslijn gaat bij \(x = 0\)?",
        [r"\(y = 3\sin 2x + 4\)", r"\(y = 6\sin 2x + 1\)", r"\(y = 3\sin\tfrac{x}{2} + 4\)", r"\(y = 4\sin 2x + 3\)"],
        0,
        r"Amplitude \(\tfrac{7 - 1}{2} = 3\), evenwichtslijn \(4\), \(b = \tfrac{2\pi}{\pi} = 2\).",
    ),
    tabel(
        r"Over \(y = \tan x\). Juist of fout?",
        [(r"De periode is \(\pi\).", J), (r"Er is een verticale asymptoot bij \(x = \tfrac{\pi}{2}\).", J), (r"Het bereik is \(\left[-1, 1\right]\).", F), (r"\(\tan\) is een oneven functie.", J)],
        r"De tangens neemt elke reële waarde aan.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Twee wandelaars vertrekken uit hetzelfde punt onder een hoek van \(120^\circ\). Na een tijd is de ene 3 km ver, de andere 5 km. Hoe ver liggen ze uit elkaar?",
        ["7 km", "8 km", r"\(\sqrt{19}\) km", "4 km"],
        0,
        r"\(c^{2} = 9 + 25 - 30\cos 120^\circ = 34 + 15 = 49\).",
    ),
    inv(
        r"Hoeveel radialen is \(72^\circ\)? Typ als breuk met π, zoals 3π/4.",
        ["2π/5", "2pi/5", "2 π/5", "(2π)/5"],
        r"\(72 \cdot \tfrac{\pi}{180} = \tfrac{2\pi}{5}\).",
    ),
]
