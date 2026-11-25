# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Statistiek 🌍 Beyond doorstroom:
twee boxplots naast elkaar en het staafdiagram van een binomiale verdeling.
Alle cijfers zijn verzonnen.

    python3 inhoud/uitdaging/maak_prenten_beyond_statistiek.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_statistiek.py.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "statistiek-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

B, H = 1000, 560
X0, X1 = 150, 930  # punten 0..20
KLAS = {"Klas A": ((4, 8, 11, 14, 19), 200, BLAUW), "Klas B": ((6, 10, 12, 13, 17), 360, ORANJE)}


def bx(v):
    return X0 + (X1 - X0) * v / 20


def pct(x, y, w, h, b, hh):
    return [round(x / b * 100, 1), round(y / hh * 100, 1), round(w / b * 100, 1), round(h / hh * 100, 1)]


def boxplots():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Punten op 20 voor dezelfde toets</text>"]
    for v in range(0, 21, 2):
        x = bx(v)
        d.append(f"<line x1='{x}' y1='110' x2='{x}' y2='450' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='485' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{v}</text>")
    d.append(f"<line x1='{X0}' y1='455' x2='{X1 + 10}' y2='455' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X1 + 10}' y='525' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>punten</text>")
    z = {}
    for naam, ((mn, q1, me, q3, mx), y, kleur) in KLAS.items():
        d.append(f"<text x='40' y='{y + 8}' {FONT} font-size='22' font-weight='800' fill='{kleur}'>{naam}</text>")
        d.append(f"<line x1='{bx(mn)}' y1='{y}' x2='{bx(q1)}' y2='{y}' stroke='{kleur}' stroke-width='4'/>")
        d.append(f"<line x1='{bx(q3)}' y1='{y}' x2='{bx(mx)}' y2='{y}' stroke='{kleur}' stroke-width='4'/>")
        for v in (mn, mx):
            d.append(f"<line x1='{bx(v)}' y1='{y - 22}' x2='{bx(v)}' y2='{y + 22}' stroke='{kleur}' stroke-width='4'/>")
        d.append(f"<rect x='{bx(q1)}' y='{y - 45}' width='{bx(q3) - bx(q1)}' height='90' fill='#ffffff' stroke='{kleur}' stroke-width='4'/>")
        d.append(f"<line x1='{bx(me)}' y1='{y - 45}' x2='{bx(me)}' y2='{y + 45}' stroke='{kleur}' stroke-width='6'/>")
        z[naam] = {"mediaan": pct(bx(me) - 16, y - 55, 32, 110, B, H),
                   "box": pct(bx(q1) - 4, y - 55, bx(q3) - bx(q1) + 8, 110, B, H),
                   "max": pct(bx(mx) - 18, y - 32, 36, 64, B, H)}
    d.append("</svg>")
    (UIT / "boxplots-klassen.svg").write_text("\n".join(d), encoding="utf-8")
    return z


# binomiale verdeling n = 5, p = 0,4
BB, BH = 900, 600
BX0, BX1, BY0, BY1 = 120, 860, 500, 110  # kans 0..0,4


def binom():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {BB} {BH}' width='{BB}' height='{BH}'>",
         f"<rect width='{BB}' height='{BH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Aantal treffers bij 5 worpen op een doel</text>"]
    for k in range(0, 5):
        p = k / 10
        y = BY0 - (BY0 - BY1) * p / 0.4
        d.append(f"<line x1='{BX0}' y1='{y}' x2='{BX1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{BX0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{str(p).replace('.', ',')}</text>")
    d.append(f"<line x1='{BX0}' y1='{BY0}' x2='{BX1}' y2='{BY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{BX0}' y1='{BY0}' x2='{BX0}' y2='{BY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{BX0 + 12}' y='{BY1 - 24}' {FONT} font-size='21' fill='{TEKST}'>kans</text>")
    d.append(f"<text x='{BX1}' y='{BY0 + 72}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>aantal treffers (x)</text>")
    z = {}
    breed = (BX1 - BX0) / 6
    for k in range(6):
        p = math.comb(5, k) * 0.4 ** k * 0.6 ** (5 - k)
        h = (BY0 - BY1) * p / 0.4
        x = BX0 + breed * k + breed * 0.15
        d.append(f"<rect x='{x:.1f}' y='{BY0 - h:.1f}' width='{breed * 0.7:.1f}' height='{h:.1f}' fill='{GROEN}'/>")
        d.append(f"<text x='{x + breed * 0.35:.1f}' y='{BY0 + 32}' text-anchor='middle' {FONT} font-size='21' fill='{TEKST}'>{k}</text>")
        z[k] = pct(x - 6, min(BY0 - h, BY0 - 40) - 10, breed * 0.7 + 12, max(h, 40) + 20, BB, BH)
    d.append("</svg>")
    (UIT / "binomiaal-worpen.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("box", boxplots())
    print("binom", binom())
