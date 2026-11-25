# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde 🚀 Boost doorstroom:
een parabool met een rechte en een puntenwolk.

    python3 inhoud/uitdaging/maak_prenten_boost_wiskunde.py

De klikvakken in uitdaging/bron/boost_wiskunde.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ORANJE = "#2f4a22", "#2b2b2b", "#b9b29c", "#c0622b"

# parabool f(x) = -x^2 + 2x + 3 en rechte g(x) = x + 1
GB, GH = 900, 700
OX, OY, EEN = 330, 470, 75
XMIN, XMAX, YMIN, YMAX = -3, 5, -3, 5


def gp(x, y):
    return OX + x * EEN, OY - y * EEN


def f(x):
    return -x * x + 2 * x + 3


# puntenwolk: studietijd (uur) en punten op 20
PB, PH = 1000, 620
PX0, PX1, PY0, PY1 = 110, 920, 520, 100
PUNTEN = [(1, 7), (1.5, 8), (2, 9), (2.5, 9), (3, 11), (3.5, 10), (4, 12), (4.5, 13), (5, 13),
          (5.5, 14), (6, 15), (6.5, 15), (7, 17), (7.5, 16), (8, 18), (6, 5)]
UITSCHIETER = (6, 5)


def pp(u, s):
    return PX0 + (PX1 - PX0) * u / 9, PY0 - (PY0 - PY1) * s / 20


def parabool():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een parabool f en een rechte g</text>"]
    for k in range(XMIN, XMAX + 1):
        x, _ = gp(k, 0)
        d.append(f"<line x1='{x}' y1='{gp(0, YMAX)[1]}' x2='{x}' y2='{gp(0, YMIN)[1]}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k:
            kant = ("start", x + 6) if k < 0 else ("end", x - 6)
            d.append(f"<text x='{kant[1]}' y='{OY + 26}' text-anchor='{kant[0]}' {FONT} font-size='19' fill='{TEKST}'>{k}</text>")
    for k in range(YMIN, YMAX + 1):
        _, y = gp(0, k)
        d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{y}' x2='{gp(XMAX, 0)[0]}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k:
            d.append(f"<text x='{OX - 10}' y='{y - 4}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{k}</text>")
    d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{OY}' x2='{gp(XMAX, 0)[0] + 10}' y2='{OY}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{OX}' y1='{gp(0, YMIN)[1]}' x2='{OX}' y2='{gp(0, YMAX)[1] - 10}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{gp(XMAX, 0)[0] + 16}' y='{OY + 8}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>x</text>")
    d.append(f"<text x='{OX + 10}' y='{gp(0, YMAX)[1] - 8}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>y</text>")
    pts = []
    x = -1.8
    while x <= 3.801:
        X, Y = gp(x, f(x))
        pts.append(f"{X:.1f},{Y:.1f}")
        x += 0.05
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    a, b = gp(-3, -2), gp(4, 5)
    d.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' stroke='{ORANJE}' stroke-width='4.5'/>")
    lf = gp(3.85, -2.4); lg = gp(4.1, 4.6)
    d.append(f"<text x='{lf[0]}' y='{lf[1]}' {FONT} font-size='26' font-weight='800' font-style='italic' fill='{GROEN}'>f</text>")
    d.append(f"<text x='{lg[0]}' y='{lg[1]}' {FONT} font-size='26' font-weight='800' font-style='italic' fill='{ORANJE}'>g</text>")
    d.append("</svg>")
    (UIT / "parabool-en-rechte.svg").write_text("\n".join(d), encoding="utf-8")


def punt_zone(x, y, r=38):
    X, Y = gp(x, y)
    return [round((X - r) / GB * 100, 1), round((Y - r) / GH * 100, 1),
            round(2 * r / GB * 100, 1), round(2 * r / GH * 100, 1)]


def wolk():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {PB} {PH}' width='{PB}' height='{PH}'>",
         f"<rect width='{PB}' height='{PH}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Studietijd en punten op een toets</text>"]
    for s in range(0, 21, 4):
        _, y = pp(0, s)
        d.append(f"<line x1='{PX0}' y1='{y}' x2='{PX1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{PX0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{s}</text>")
    for u in range(0, 10):
        x, _ = pp(u, 0)
        d.append(f"<line x1='{x}' y1='{PY1}' x2='{x}' y2='{PY0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{PY0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{u}</text>")
    d.append(f"<line x1='{PX0}' y1='{PY0}' x2='{PX1 + 15}' y2='{PY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{PX0}' y1='{PY0}' x2='{PX0}' y2='{PY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{PX1 + 10}' y='{PY0 + 66}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>studietijd (uur)</text>")
    d.append(f"<text x='{PX0 + 12}' y='{PY1 - 22}' {FONT} font-size='21' fill='{TEKST}'>punten op 20</text>")
    for u, s in PUNTEN:
        x, y = pp(u, s)
        d.append(f"<circle cx='{x}' cy='{y}' r='9' fill='{GROEN}'/>")
    d.append("</svg>")
    (UIT / "puntenwolk-studietijd.svg").write_text("\n".join(d), encoding="utf-8")


def wolk_zone(u, s, r=30):
    x, y = pp(u, s)
    return [round((x - r) / PB * 100, 1), round((y - r) / PH * 100, 1),
            round(2 * r / PB * 100, 1), round(2 * r / PH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    parabool()
    wolk()
    print("top", punt_zone(1, 4), "snij", punt_zone(2, 3), "nul", punt_zone(-1, 0), punt_zone(3, 0),
          "uit", wolk_zone(*UITSCHIETER))
