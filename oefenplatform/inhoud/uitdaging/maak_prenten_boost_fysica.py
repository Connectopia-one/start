# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Fysica 🚀 Boost doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_fysica.py

De klikvakken in uitdaging/bron/boost_fysica.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "fysica-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT, ORANJE = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec", "#c0622b"

# x(t)-grafiek: t van 0 tot 20 s, x van 0 tot 80 m
GB, GH = 1000, 620
X0, X1, Y0, Y1 = 110, 900, 520, 110
LIJNEN = [("A", (0, 0), (20, 80), GROEN), ("B", (0, 60), (20, 20), ORANJE)]


def px(t, x):
    return X0 + (X1 - X0) * t / 20, Y0 - (Y0 - Y1) * x / 80


# waterbak: 4 m diep
VB, VH = 1000, 600
BX, BY, BB, BH = 200, 130, 600, 400       # binnenkant van de bak, 100 px per meter
PUNTEN = {"P": (300, 0.5), "Q": (380, 2.0), "R": (520, 3.5), "S": (680, 2.0)}


def grafiek():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Twee lopers op een rechte weg</text>"]
    for x in range(0, 81, 10):
        _, y = px(0, x)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{x}</text>")
    for t in range(0, 21, 2):
        X, _ = px(t, 0)
        d.append(f"<line x1='{X}' y1='{Y1}' x2='{X}' y2='{Y0}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{X}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{t}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 20}' y2='{Y0}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 20}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 64}' text-anchor='end' {FONT} font-size='22' fill='{TEKST}'>t (s)</text>")
    d.append(f"<text x='{X0 + 14}' y='{Y1 - 16}' {FONT} font-size='22' fill='{TEKST}'>x (m)</text>")
    for naam, a, b, kleur in LIJNEN:
        xa, ya = px(*a); xb, yb = px(*b)
        d.append(f"<line x1='{xa}' y1='{ya}' x2='{xb}' y2='{yb}' stroke='{kleur}' stroke-width='6' stroke-linecap='round'/>")
        d.append(f"<circle cx='{xb + 34}' cy='{yb}' r='21' fill='{kleur}'/>")
        d.append(f"<text x='{xb + 34}' y='{yb + 8}' text-anchor='middle' {FONT} font-size='23' font-weight='800' fill='#ffffff'>{naam}</text>")
    d.append("</svg>")
    (UIT / "twee-lopers-x-t.svg").write_text("\n".join(d), encoding="utf-8")


def kruis_zone():
    x, y = px(10, 40)
    return [round((x - 40) / GB * 100, 1), round((y - 40) / GH * 100, 1),
            round(80 / GB * 100, 1), round(80 / GH * 100, 1)]


def lijn_zones(naam):
    """Een paar klikvakjes langs de lijn, zodat je overal op de lijn mag klikken."""
    _, a, b, _ = next(l for l in LIJNEN if l[0] == naam)
    zones = []
    for t in (3, 7, 13, 17):
        x, y = px(t, a[1] + (b[1] - a[1]) * t / 20)
        zones.append([round((x - 40) / GB * 100, 1), round((y - 40) / GH * 100, 1),
                      round(80 / GB * 100, 1), round(80 / GH * 100, 1)])
    return zones


def bak():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {VB} {VH}' width='{VB}' height='{VH}'>",
         f"<rect width='{VB}' height='{VH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een waterbak van 4 meter diep</text>",
         f"<rect x='{BX}' y='{BY}' width='{BB}' height='{BH}' fill='#dcecf5'/>",
         f"<path d='M{BX - 10},{BY - 30} L{BX - 10},{BY + BH + 10} L{BX + BB + 10},{BY + BH + 10} L{BX + BB + 10},{BY - 30}' fill='none' stroke='{TEKST}' stroke-width='8'/>",
         f"<line x1='{BX}' y1='{BY}' x2='{BX + BB}' y2='{BY}' stroke='#4a90b8' stroke-width='3'/>",
         f"<text x='{BX + BB - 10}' y='{BY - 10}' text-anchor='end' {FONT} font-size='18' fill='#4a90b8'>wateroppervlak</text>"]
    for m in range(0, 5):
        y = BY + m * 100
        d.append(f"<line x1='{BX - 40}' y1='{y}' x2='{BX - 18}' y2='{y}' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<text x='{BX - 48}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{m} m</text>")
    d.append(f"<text x='{BX - 120}' y='{BY - 30}' {FONT} font-size='19' fill='{TEKST}'>diepte</text>")
    for naam, (x, diep) in PUNTEN.items():
        y = BY + diep * 100
        d.append(f"<circle cx='{x}' cy='{y}' r='9' fill='{GROEN}'/>")
        d.append(f"<text x='{x + 18}' y='{y + 9}' {FONT} font-size='26' font-weight='800' fill='{GROEN}'>{naam}</text>")
    d.append("</svg>")
    (UIT / "waterbak-punten.svg").write_text("\n".join(d), encoding="utf-8")


def punt_zone(naam):
    x, diep = PUNTEN[naam]
    y = BY + diep * 100
    return [round((x - 35) / VB * 100, 1), round((y - 35) / VH * 100, 1),
            round(85 / VB * 100, 1), round(70 / VH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    grafiek()
    bak()
    print("kruis", kruis_zone(), "A", lijn_zones("A"), {n: punt_zone(n) for n in PUNTEN})
