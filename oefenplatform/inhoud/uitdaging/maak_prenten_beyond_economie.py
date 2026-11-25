# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Economie 🌍 Beyond doorstroom:
een marktdiagram met vraag, aanbod en een maximumprijs, en een
conjunctuurgolf rond een trendlijn. Alle cijfers zijn verzonnen.

    python3 inhoud/uitdaging/maak_prenten_beyond_economie.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_economie.py.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "economie-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

# markt: vraag P = 10 - 0,5 Q en aanbod P = 2 + 0,5 Q, evenwicht Q = 8, P = 6
B, H = 1000, 700
X0, X1, Y0, Y1 = 120, 900, 600, 110  # Q 0..20, P 0..12


def mp(q, p):
    return X0 + (X1 - X0) * q / 20, Y0 - (Y0 - Y1) * p / 12


def zone(x, y, r, b, h):
    return [round((x - r) / b * 100, 1), round((y - r) / h * 100, 1),
            round(2 * r / b * 100, 1), round(2 * r / h * 100, 1)]


def markt():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De markt voor fietshelmen</text>"]
    for p in range(0, 13, 2):
        _, y = mp(0, p)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{p * 10}</text>")
    for q in range(0, 21, 4):
        x, _ = mp(q, 0)
        d.append(f"<line x1='{x}' y1='{Y1}' x2='{x}' y2='{Y0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{q * 100}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 15}' y2='{Y0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 64}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>hoeveelheid per week (Q)</text>")
    d.append(f"<text x='{X0 + 12}' y='{Y1 - 24}' {FONT} font-size='21' fill='{TEKST}'>prijs in euro (P)</text>")
    # surplussen lichtjes ingekleurd
    a, b, c = mp(0, 10), mp(0, 6), mp(8, 6)
    d.append(f"<polygon points='{a[0]},{a[1]} {b[0]},{b[1]} {c[0]},{c[1]}' fill='#dbe7f3'/>")
    a2 = mp(0, 2)
    d.append(f"<polygon points='{b[0]},{b[1]} {a2[0]},{a2[1]} {c[0]},{c[1]}' fill='#f6e1d3'/>")
    v0, v1 = mp(0, 10), mp(20, 0)
    d.append(f"<line x1='{v0[0]}' y1='{v0[1]}' x2='{v1[0]}' y2='{v1[1]}' stroke='{BLAUW}' stroke-width='5'/>")
    a0, a1 = mp(0, 2), mp(19, 11.5)
    d.append(f"<line x1='{a0[0]}' y1='{a0[1]}' x2='{a1[0]}' y2='{a1[1]}' stroke='{ORANJE}' stroke-width='5'/>")
    d.append(f"<text x='{mp(18.6, 0.9)[0]}' y='{mp(18.6, 0.9)[1]}' {FONT} font-size='26' font-weight='800' fill='{BLAUW}'>V</text>")
    d.append(f"<text x='{mp(19.2, 11.2)[0]}' y='{mp(19.2, 11.2)[1]}' {FONT} font-size='26' font-weight='800' fill='{ORANJE}'>A</text>")
    # maximumprijs 40 euro
    m0, m1 = mp(0, 4), mp(20, 4)
    d.append(f"<line x1='{m0[0]}' y1='{m0[1]}' x2='{m1[0]}' y2='{m1[1]}' stroke='{GROEN}' stroke-width='3' stroke-dasharray='12 8'/>")
    d.append(f"<text x='{mp(13.5, 4.3)[0]}' y='{mp(13.5, 4.3)[1]}' {FONT} font-size='20' font-weight='700' fill='{GROEN}'>maximumprijs</text>")
    e = mp(8, 6)
    d.append(f"<circle cx='{e[0]}' cy='{e[1]}' r='10' fill='{TEKST}'/>")
    d.append(f"<text x='{e[0] + 16}' y='{e[1] - 12}' {FONT} font-size='24' font-weight='800' fill='{TEKST}'>E</text>")
    for letter, (q, p) in {"1": (2.2, 7.3), "2": (2.2, 4.9)}.items():
        x, y = mp(q, p)
        d.append(f"<circle cx='{x}' cy='{y}' r='20' fill='#ffffff' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{TEKST}'>{letter}</text>")
    d.append("</svg>")
    (UIT / "markt-fietshelmen.svg").write_text("\n".join(d), encoding="utf-8")
    z = {"E": zone(*e, 36, B, H)}
    for letter, (q, p) in {"1": (2.2, 7.3), "2": (2.2, 4.9)}.items():
        z[letter] = zone(*mp(q, p), 34, B, H)
    return z


# conjunctuurgolf
CB, CH = 1000, 560
CX0, CX1, CY0, CY1 = 90, 940, 470, 100


def golf_y(t):
    return 2 + 0.25 * t + 1.6 * math.sin(t * 2 * math.pi / 8)


def cp(t, w):
    return CX0 + (CX1 - CX0) * t / 16, CY0 - (CY0 - CY1) * w / 8


def golf():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {CB} {CH}' width='{CB}' height='{CH}'>",
         f"<rect width='{CB}' height='{CH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De conjunctuur van een land</text>"]
    d.append(f"<line x1='{CX0}' y1='{CY0}' x2='{CX1 + 15}' y2='{CY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{CX0}' y1='{CY0}' x2='{CX0}' y2='{CY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{CX1 + 10}' y='{CY0 + 40}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>tijd</text>")
    d.append(f"<text x='{CX0 + 12}' y='{CY1 - 22}' {FONT} font-size='21' fill='{TEKST}'>reëel bbp</text>")
    t0, t1 = cp(0, 2), cp(16, 6)
    d.append(f"<line x1='{t0[0]}' y1='{t0[1]}' x2='{t1[0]}' y2='{t1[1]}' stroke='{ORANJE}' stroke-width='3' stroke-dasharray='12 8'/>")
    lt = cp(12.6, 5.75)
    d.append(f"<text x='{lt[0]}' y='{lt[1]}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{ORANJE}'>trend</text>")
    pts = []
    t = 0
    while t <= 16.001:
        x, y = cp(t, golf_y(t))
        pts.append(f"{x:.1f},{y:.1f}")
        t += 0.05
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    punten = {"P": 2, "Q": 4, "R": 6, "S": 10}
    z = {}
    for letter, t in punten.items():
        x, y = cp(t, golf_y(t))
        d.append(f"<circle cx='{x}' cy='{y}' r='9' fill='{TEKST}'/>")
        dy = -18 if letter in "PS" else 36
        d.append(f"<text x='{x}' y='{y + dy}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='{TEKST}'>{letter}</text>")
        z[letter] = zone(x, y, 36, CB, CH)
    d.append("</svg>")
    (UIT / "conjunctuurgolf.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("markt", markt())
    print("golf", golf())
