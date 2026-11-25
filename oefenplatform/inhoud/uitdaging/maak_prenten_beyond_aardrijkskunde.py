# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Aardrijkskunde 🌍 Beyond.

    python3 inhoud/uitdaging/maak_prenten_beyond_aardrijkskunde.py

Prent 1: een doorsnede door de lithosfeer met vier plekken A, B, C en D.
Prent 2: een vereenvoudigde weerkaart met een depressie en twee fronten.
De klikvakken in uitdaging/bron/beyond_aardrijkskunde.py staan in procent.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "aardrijkskunde-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"
ZEE, OCEAANKORST, CONTINENT, MANTEL, MAGMA = "#cfe3f1", "#8b8f7a", "#c9b38a", "#f1e3cf", "#c8553d"
WARM, KOUD = "#c8553d", "#2f6f9f"

B, H = 1000, 560
# x-plaats van de vier letters (en hun klikvak)
PLEKKEN = {"A": 150, "B": 400, "C": 690, "D": 850}


def letter(x, y, t):
    return (f"<circle cx='{x}' cy='{y}' r='22' fill='{GROEN}'/>"
            f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='#ffffff'>{t}</text>")


def doorsnede():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Doorsnede door de bovenste lagen van de aarde</text>",
         # mantel
         f"<rect x='20' y='330' width='{B - 40}' height='200' fill='{MANTEL}'/>",
         f"<text x='560' y='510' {FONT} font-size='20' fill='{TEKST}'>asthenosfeer</text>",
         # zee
         f"<rect x='20' y='170' width='700' height='120' fill='{ZEE}'/>",
         # oceanische korst links van de rug en tussen rug en trog
         f"<polygon points='20,290 360,290 400,250 440,290 640,290 700,300 860,470 830,480 660,330 20,330' fill='{OCEAANKORST}'/>",
         # continent rechts
         f"<polygon points='700,300 740,170 800,150 850,110 880,150 980,170 980,330 860,330 860,470 700,300' fill='{CONTINENT}'/>",
         # vulkaan op het continent + magmakanaal
         f"<polygon points='820,150 850,95 880,150' fill='#7a5a3a'/>",
         f"<path d='M850,100 C846,200 830,300 800,420' stroke='{MAGMA}' stroke-width='7' fill='none'/>",
         # rug: magma dat opwelt, pijlen uit elkaar
         f"<path d='M400,520 L400,260' stroke='{MAGMA}' stroke-width='8'/>",
         f"<path d='M370,310 L300,310 M300,310 l14,-9 M300,310 l14,9' stroke='{TEKST}' stroke-width='3' fill='none'/>",
         f"<path d='M430,310 L500,310 M500,310 l-14,-9 M500,310 l-14,9' stroke='{TEKST}' stroke-width='3' fill='none'/>",
         # hotspot: eiland + pluim midden op de plaat
         f"<polygon points='115,170 150,120 185,170' fill='#7a5a3a'/>",
         f"<path d='M150,130 L150,520' stroke='{MAGMA}' stroke-width='8'/>",
         f"<ellipse cx='150' cy='500' rx='45' ry='20' fill='{MAGMA}' opacity='0.85'/>",
         # trog bij de subductie
         f"<path d='M640,290 Q690,330 700,300' fill='{ZEE}'/>",
         f"<path d='M700,370 L780,440 M780,440 l-4,-16 M780,440 l-16,-3' stroke='{TEKST}' stroke-width='3' fill='none'/>",
         ]
    hoogte = {"A": 95, "B": 215, "C": 215, "D": 60}
    for t, x in PLEKKEN.items():
        d.append(letter(x, hoogte[t], t))
    d.append(f"<text x='560' y='230' {FONT} font-size='20' fill='{KOUD}'>oceaan</text>")
    d.append(f"<text x='900' y='250' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>continent</text>")
    d.append("</svg>")
    (UIT / "doorsnede-platen.svg").write_text("\n".join(d), encoding="utf-8")


def plek_zone(t):
    x = PLEKKEN[t]
    return [round((x - 70) / B * 100, 1), round(40 / H * 100 + 2, 1), round(140 / B * 100, 1), round(330 / H * 100, 1)]


# Weerkaart
WB, WH = 1000, 620
L = (420, 340)
HOOG = (870, 190)


def weerkaart():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {WB} {WH}' width='{WB}' height='{WH}'>",
         f"<rect width='{WB}' height='{WH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Weerkaart boven de Atlantische Oceaan en West-Europa</text>"]
    for r, p in ((60, 980), (120, 990), (180, 1000), (240, 1010)):
        d.append(f"<ellipse cx='{L[0]}' cy='{L[1]}' rx='{r * 1.25}' ry='{r}' fill='none' stroke='#9a9a9a' stroke-width='2'/>")
        d.append(f"<text x='{L[0] - 8}' y='{L[1] - r - 6}' text-anchor='middle' {FONT} font-size='16' fill='#6b6b6b'>{p}</text>")
    for r in (50, 100):
        d.append(f"<ellipse cx='{HOOG[0]}' cy='{HOOG[1]}' rx='{r * 1.2}' ry='{r}' fill='none' stroke='#9a9a9a' stroke-width='2'/>")
    d.append(f"<text x='{L[0]}' y='{L[1] + 16}' text-anchor='middle' {FONT} font-size='48' font-weight='800' fill='{KOUD}'>L</text>")
    d.append(f"<text x='{HOOG[0]}' y='{HOOG[1] + 16}' text-anchor='middle' {FONT} font-size='48' font-weight='800' fill='{WARM}'>H</text>")
    # warmtefront: van L naar oost-zuidoost, halve bolletjes
    wx0, wy0, wx1, wy1 = L[0] + 20, L[1] + 10, 700, 440
    d.append(f"<line x1='{wx0}' y1='{wy0}' x2='{wx1}' y2='{wy1}' stroke='{WARM}' stroke-width='6'/>")
    for i in range(1, 6):
        t = i / 6
        x, y = wx0 + (wx1 - wx0) * t, wy0 + (wy1 - wy0) * t
        d.append(f"<circle cx='{x + 6}' cy='{y - 16}' r='12' fill='{WARM}'/>")
    # koufront: van L naar zuidwest, driehoekjes
    kx0, ky0, kx1, ky1 = L[0] - 10, L[1] + 20, 230, 600
    d.append(f"<line x1='{kx0}' y1='{ky0}' x2='{kx1}' y2='{ky1}' stroke='{KOUD}' stroke-width='6'/>")
    for i in range(1, 6):
        t = i / 6
        x, y = kx0 + (kx1 - kx0) * t, ky0 + (ky1 - ky0) * t
        d.append(f"<polygon points='{x},{y} {x + 26},{y + 6} {x + 10},{y + 26}' fill='{KOUD}'/>")
    d.append(f"<text x='{WB - 40}' y='{WH - 24}' text-anchor='end' {FONT} font-size='18' fill='#6b6b6b'>isobaren in hectopascal</text>")
    d.append("</svg>")
    (UIT / "weerkaart-depressie.svg").write_text("\n".join(d), encoding="utf-8")


def weer_zone(wat):
    if wat == "koufront":
        return [round(210 / WB * 100, 1), round(370 / WH * 100, 1), round(240 / WB * 100, 1), round(245 / WH * 100, 1)]
    if wat == "warmtefront":
        return [round(450 / WB * 100, 1), round(310 / WH * 100, 1), round(270 / WB * 100, 1), round(150 / WH * 100, 1)]
    if wat == "hoog":
        return [round((HOOG[0] - 120) / WB * 100, 1), round((HOOG[1] - 100) / WH * 100, 1), round(240 / WB * 100, 1), round(200 / WH * 100, 1)]
    raise KeyError(wat)


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    doorsnede()
    weerkaart()
    print({t: plek_zone(t) for t in "ABCD"}, {w: weer_zone(w) for w in ("koufront", "warmtefront", "hoog")})
