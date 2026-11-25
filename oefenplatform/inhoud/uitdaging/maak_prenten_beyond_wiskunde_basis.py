# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde basis 🌍 Beyond
doorstroom: de grafiek van f(x) = 2 sin x + 1 en een kansboom.

    python3 inhoud/uitdaging/maak_prenten_beyond_wiskunde_basis.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_wiskunde_basis.py.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-basis-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

B, H = 1000, 620
OX, OY, EX, EY = 110, 400, 110, 70  # 1 eenheid x = 110 px (x in radialen), y = 70 px


def gp(x, y):
    return OX + x * EX, OY - y * EY


def zone(x, y, r, b, h):
    return [round((x - r) / b * 100, 1), round((y - r) / h * 100, 1),
            round(2 * r / b * 100, 1), round(2 * r / h * 100, 1)]


def sinus():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De grafiek van f(x) = 2 sin x + 1</text>"]
    for k in range(-2, 5):
        _, y = gp(0, k)
        d.append(f"<line x1='{OX}' y1='{y}' x2='{gp(2 * math.pi + 0.5, 0)[0]}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if k:
            d.append(f"<text x='{OX - 12}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{k}</text>")
    etik = {1: "π/2", 2: "π", 3: "3π/2", 4: "2π"}
    for k, t in etik.items():
        x, _ = gp(k * math.pi / 2, 0)
        d.append(f"<line x1='{x}' y1='{gp(0, 4)[1]}' x2='{x}' y2='{gp(0, -2)[1]}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{OY + 30}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{t}</text>")
    d.append(f"<line x1='{OX}' y1='{OY}' x2='{gp(2 * math.pi + 0.6, 0)[0]}' y2='{OY}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{OX}' y1='{gp(0, -2.2)[1]}' x2='{OX}' y2='{gp(0, 4.3)[1]}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{gp(2 * math.pi + 0.6, 0)[0] + 8}' y='{OY + 8}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>x</text>")
    d.append(f"<text x='{OX + 10}' y='{gp(0, 4.3)[1] + 4}' {FONT} font-size='22' font-style='italic' fill='{TEKST}'>y</text>")
    pts = []
    x = 0
    while x <= 2 * math.pi + 1e-9:
        X, Y = gp(x, 2 * math.sin(x) + 1)
        pts.append(f"{X:.1f},{Y:.1f}")
        x += 0.03
    X, Y = gp(2 * math.pi, 1)
    pts.append(f"{X:.1f},{Y:.1f}")
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    z = {}
    for naam, (x, y) in {"top": (math.pi / 2, 3), "dal": (3 * math.pi / 2, -1), "yas": (0, 1),
                         "nul1": (7 * math.pi / 6, 0), "nul2": (11 * math.pi / 6, 0)}.items():
        X, Y = gp(x, y)
        d.append(f"<circle cx='{X:.1f}' cy='{Y:.1f}' r='8' fill='{TEKST}'/>")
        z[naam] = zone(X, Y, 34, B, H)
    d.append("</svg>")
    (UIT / "sinus-grafiek.svg").write_text("\n".join(d), encoding="utf-8")
    return z


# kansboom
KB, KH = 1000, 560


def boom():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {KB} {KH}' width='{KB}' height='{KH}'>",
         f"<rect width='{KB}' height='{KH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De bus en op tijd op school</text>"]
    wortel = (90, 300)
    knopen = {"laat": (420, 170, "bus te laat"), "optijd": (420, 430, "bus op tijd")}
    eind = {1: (820, 100, "te laat op school"), 2: (820, 240, "op tijd op school"),
            3: (820, 360, "te laat op school"), 4: (820, 500, "op tijd op school")}
    kans1 = {"laat": "0,2", "optijd": "0,8"}
    kans2 = {1: "0,9", 2: "0,1", 3: "0,1", 4: "0,9"}
    d.append(f"<circle cx='{wortel[0]}' cy='{wortel[1]}' r='9' fill='{TEKST}'/>")
    for k, (x, y, t) in knopen.items():
        d.append(f"<line x1='{wortel[0]}' y1='{wortel[1]}' x2='{x - 70}' y2='{y}' stroke='{BLAUW}' stroke-width='4'/>")
        mx, my = (wortel[0] + x - 70) / 2, (wortel[1] + y) / 2
        d.append(f"<text x='{mx}' y='{my - 12 if y < 300 else my + 30}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{BLAUW}'>{kans1[k]}</text>")
        d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='21' fill='{TEKST}'>{t}</text>")
    z = {}
    for n, (x, y, t) in eind.items():
        bron = knopen["laat"] if n <= 2 else knopen["optijd"]
        d.append(f"<line x1='{bron[0] + 70}' y1='{bron[1]}' x2='{x - 110}' y2='{y}' stroke='{ORANJE}' stroke-width='4'/>")
        mx, my = (bron[0] + 70 + x - 110) / 2, (bron[1] + y) / 2
        d.append(f"<text x='{mx}' y='{my - 12 if y < bron[1] else my + 30}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{ORANJE}'>{kans2[n]}</text>")
        d.append(f"<rect x='{x - 105}' y='{y - 30}' width='250' height='54' rx='14' fill='#f7f4ec' stroke='#b9b29c' stroke-width='2'/>")
        d.append(f"<text x='{x + 20}' y='{y + 5}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{t}</text>")
        z[n] = [round((x - 108) / KB * 100, 1), round((y - 33) / KH * 100, 1), round(256 / KB * 100, 1), round(60 / KH * 100, 1)]
    d.append("</svg>")
    (UIT / "kansboom-bus.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("sinus", sinus())
    print("boom", boom())
