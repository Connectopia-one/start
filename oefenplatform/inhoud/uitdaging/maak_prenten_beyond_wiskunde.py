# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde 🌍 Beyond doorstroom:
de grafiek van een derdegraadsfunctie en een normale verdeling.

    python3 inhoud/uitdaging/maak_prenten_beyond_wiskunde.py

De klikvakken in uitdaging/bron/beyond_wiskunde.py rekenen met de maten
hieronder (procent van de prent).
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

# grafiek van f(x) = x^3 - 3x, x van -3 tot 3, y van -4 tot 4
GB, GH = 900, 720
OX, OY, EEN = 450, 380, 120          # oorsprong en pixels per eenheid
XMIN, XMAX, YMIN, YMAX = -3.4, 3.4, -2.6, 2.8


def gp(x, y):
    return OX + x * EEN, OY - y * EEN * 0.9


def f(x):
    return x ** 3 - 3 * x


# normale verdeling: mu 170, sigma 8 (lengte in cm)
NB, NH = 1000, 560
MU, SIG = 170, 8
NX0, NX1, NY0, NTOP = 60, 940, 440, 110


def nx(x):
    return NX0 + (NX1 - NX0) * (x - (MU - 4 * SIG)) / (8 * SIG)


def ny(z):
    return NY0 - (NY0 - NTOP) * math.exp(-z * z / 2)


GEBIEDEN = [("A", -4, -2), ("B", -2, -1), ("C", -1, 0), ("D", 0, 1), ("E", 1, 2), ("F", 2, 4)]


def grafiek():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De grafiek van een functie f</text>"]
    for k in range(-3, 4):
        x, _ = gp(k, 0)
        d.append(f"<line x1='{x}' y1='{gp(0, YMAX)[1]}' x2='{x}' y2='{gp(0, YMIN)[1]}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k:
            d.append(f"<text x='{x}' y='{OY + 30}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{k}</text>")
    for k in range(-2, 3):
        _, y = gp(0, k)
        d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{y}' x2='{gp(XMAX, 0)[0]}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k:
            d.append(f"<text x='{OX - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>{k}</text>")
    d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{OY}' x2='{gp(XMAX, 0)[0]}' y2='{OY}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{OX}' y1='{gp(0, YMIN)[1]}' x2='{OX}' y2='{gp(0, YMAX)[1]}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{gp(XMAX, 0)[0] + 8}' y='{OY + 8}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>x</text>")
    d.append(f"<text x='{OX + 10}' y='{gp(0, YMAX)[1] - 6}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>y</text>")
    pts = []
    x = -2.05
    while x <= 2.0501:
        X, Y = gp(x, f(x))
        pts.append(f"{X:.1f},{Y:.1f}")
        x += 0.025
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{GROEN}' stroke-width='5' stroke-linejoin='round'/>")
    d.append(f"<text x='{gp(2.12, 2.2)[0]}' y='{gp(2.12, 2.2)[1]}' {FONT} font-size='26' font-weight='800' font-style='italic' fill='{GROEN}'>f</text>")
    d.append("</svg>")
    (UIT / "grafiek-derdegraad.svg").write_text("\n".join(d), encoding="utf-8")


def punt_zone(x, y, r=45):
    X, Y = gp(x, y)
    return [round((X - r) / GB * 100, 1), round((Y - r) / GH * 100, 1),
            round(2 * r / GB * 100, 1), round(2 * r / GH * 100, 1)]


def normaal():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {NB} {NH}' width='{NB}' height='{NH}'>",
         f"<rect width='{NB}' height='{NH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Lengte van volwassenen, normaal verdeeld</text>"]
    pts = []
    z = -4
    while z <= 4.001:
        pts.append(f"{nx(MU + z * SIG):.1f},{ny(z):.1f}")
        z += 0.05
    d.append(f"<polygon points='{nx(MU - 4 * SIG)},{NY0} {' '.join(pts)} {nx(MU + 4 * SIG)},{NY0}' fill='{ZACHT}'/>")
    for k in (-2, -1, 0, 1, 2):
        X = nx(MU + k * SIG)
        d.append(f"<line x1='{X}' y1='{NY0}' x2='{X}' y2='{ny(k)}' stroke='{RAND}' stroke-width='2.5'/>")
        d.append(f"<text x='{X}' y='{NY0 + 32}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{MU + k * SIG}</text>")
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    d.append(f"<line x1='{NX0}' y1='{NY0}' x2='{NX1}' y2='{NY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{NX1}' y='{NY0 + 70}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>lengte (cm)</text>")
    for naam, a, b in GEBIEDEN:
        m = (max(a, -2.9) + min(b, 2.9)) / 2
        X = nx(MU + m * SIG)
        Y = NY0 - 30 if abs(m) > 1.5 else NY0 - 60
        d.append(f"<text x='{X}' y='{Y}' text-anchor='middle' {FONT} font-size='26' font-weight='800' fill='{GROEN}'>{naam}</text>")
    d.append("</svg>")
    (UIT / "normale-verdeling-lengte.svg").write_text("\n".join(d), encoding="utf-8")


def gebied_zone(naam):
    _, a, b = next(g for g in GEBIEDEN if g[0] == naam)
    xa, xb = nx(MU + a * SIG), nx(MU + b * SIG)
    return [round(xa / NB * 100, 1), round(NTOP / NH * 100, 1),
            round((xb - xa) / NB * 100, 1), round((NY0 - NTOP) / NH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    grafiek()
    normaal()
    print("max", punt_zone(-1, 2), "min", punt_zone(1, -2), "buig", punt_zone(0, 0),
          {n: gebied_zone(n) for n in "ABCDEF"})
