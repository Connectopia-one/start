# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde basis 🚀 Boost
doorstroom: een rechte met vijf genummerde punten en een rechthoekige driehoek.

    python3 inhoud/uitdaging/maak_prenten_boost_wiskunde_basis.py

De klikvakken in uitdaging/bron/boost_wiskunde_basis.py staan in procent.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-basis-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

# rechte f(x) = 2x - 4
GB, GH = 760, 800
OX, OY, EEN = 236, 392, 52
XMIN, XMAX, YMIN, YMAX = -3, 7, -7, 6
PUNTEN = {1: (0, -4), 2: (2, 0), 3: (4, 4), 4: (-1, -6), 5: (5, 2)}   # 5 ligt niet op de rechte


def gp(x, y):
    return OX + x * EEN, OY - y * EEN


def rechte():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='30' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De grafiek van een eerstegraadsfunctie f</text>"]
    for k in range(XMIN, XMAX + 1):
        x, _ = gp(k, 0)
        d.append(f"<line x1='{x}' y1='{gp(0, YMAX)[1]}' x2='{x}' y2='{gp(0, YMIN)[1]}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k and k % 2 == 0:
            d.append(f"<text x='{x}' y='{OY + 24}' text-anchor='middle' {FONT} font-size='18' fill='{TEKST}'>{k}</text>")
    for k in range(YMIN, YMAX + 1):
        _, y = gp(0, k)
        d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{y}' x2='{gp(XMAX, 0)[0]}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k and k % 2 == 0:
            d.append(f"<text x='{OX - 10}' y='{y + 6}' text-anchor='end' {FONT} font-size='18' fill='{TEKST}'>{k}</text>")
    d.append(f"<line x1='{gp(XMIN, 0)[0]}' y1='{OY}' x2='{gp(XMAX, 0)[0] + 10}' y2='{OY}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{OX}' y1='{gp(0, YMIN)[1]}' x2='{OX}' y2='{gp(0, YMAX)[1] - 10}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{gp(XMAX, 0)[0] + 14}' y='{OY + 8}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>x</text>")
    d.append(f"<text x='{OX + 10}' y='{gp(0, YMAX)[1] - 6}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>y</text>")
    a, b = gp(-1, -6), gp(5, 6)
    d.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' stroke='{BLAUW}' stroke-width='5'/>")
    lf = gp(5.2, 5.6)
    d.append(f"<text x='{lf[0]}' y='{lf[1]}' {FONT} font-size='28' font-weight='800' font-style='italic' fill='{BLAUW}'>f</text>")
    zones = {}
    for n, (x, y) in PUNTEN.items():
        X, Y = gp(x, y)
        d.append(f"<circle cx='{X}' cy='{Y}' r='19' fill='{GROEN}'/>")
        d.append(f"<text x='{X}' y='{Y + 7}' text-anchor='middle' {FONT} font-size='20' font-weight='800' fill='#ffffff'>{n}</text>")
        zones[n] = [round((X - 30) / GB * 100, 1), round((Y - 30) / GH * 100, 1), round(60 / GB * 100, 1), round(60 / GH * 100, 1)]
    d.append("</svg>")
    (UIT / "rechte-vijf-punten.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


def driehoek():
    B, H = 1000, 600
    A, Bp, C = (150, 500), (750, 500), (750, 100)   # rechte hoek bij B'
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een rechthoekige driehoek ABC</text>",
         f"<polygon points='{A[0]},{A[1]} {Bp[0]},{Bp[1]} {C[0]},{C[1]}' fill='#f7f4ec' stroke='{TEKST}' stroke-width='4'/>",
         f"<rect x='{Bp[0] - 30}' y='{Bp[1] - 30}' width='30' height='30' fill='none' stroke='{TEKST}' stroke-width='3'/>",
         f"<path d='M{A[0] + 80},{A[1]} A80,80 0 0 0 {A[0] + 80 * 0.832:.1f},{A[1] - 80 * 0.555:.1f}' fill='none' stroke='{ORANJE}' stroke-width='4'/>",
         f"<text x='{A[0] + 95}' y='{A[1] - 14}' {FONT} font-size='28' font-style='italic' fill='{ORANJE}'>α</text>",
         f"<text x='{A[0] - 40}' y='{A[1] + 10}' {FONT} font-size='28' font-weight='800' fill='{TEKST}'>A</text>",
         f"<text x='{Bp[0] + 14}' y='{Bp[1] + 10}' {FONT} font-size='28' font-weight='800' fill='{TEKST}'>B</text>",
         f"<text x='{C[0] + 14}' y='{C[1]}' {FONT} font-size='28' font-weight='800' fill='{TEKST}'>C</text>",
         f"<text x='450' y='545' text-anchor='middle' {FONT} font-size='24' fill='{TEKST}'>8 cm</text>",
         f"<text x='770' y='310' {FONT} font-size='24' fill='{TEKST}'>6 cm</text>"]
    d.append("</svg>")
    (UIT / "rechthoekige-driehoek.svg").write_text("\n".join(d), encoding="utf-8")
    # zones van de zijden (smalle stroken langs de zijde)
    schuin = []
    for cx, cy in ((250, 433), (450, 300), (650, 167)):
        schuin.append([round((cx - 80) / B * 100, 1), round((cy - 55) / H * 100, 1), 16.0, round(110 / H * 100, 1)])
    return {"AB": [15.0, 78.0, 60.0, 9.0], "BC": [71.0, 16.7, 8.0, 66.7], "AC": schuin}


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(rechte())
    print(driehoek())
