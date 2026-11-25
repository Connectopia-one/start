# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde 🚀 Boost dubbele
finaliteit.

    python3 inhoud/uitdaging/maak_prenten_boost_df_wiskunde.py

De klikvakken in uitdaging/bron/boost_df_wiskunde.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ROZE, BLAUW = "#2f4a22", "#2b2b2b", "#b5523b", "#2f6f9f"

# Kosten en opbrengst: K = 20 + 2x (blauw), O = 6x (rood), x van 0 tot 10, y van 0 tot 60
KB, KH = 1000, 660
KX0, KX1, KY0, KY1 = 130, 930, 580, 110


def kp(x, y):
    return KX0 + (KX1 - KX0) * x / 10, KY0 - (KY0 - KY1) * y / 60


# Boxplot van toetsscores op 20
BB, BH = 1000, 380
BX0, BX1 = 80, 920
BOX = {"min": 4, "q1": 9, "med": 12, "q3": 14, "max": 19}


def bx(s):
    return BX0 + (BX1 - BX0) * s / 20


def kosten():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {KB} {KH}' width='{KB}' height='{KH}'>",
         f"<rect width='{KB}' height='{KH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Kaarsjes maken voor de kerstmarkt</text>"]
    for y in range(0, 61, 10):
        _, py = kp(0, y)
        d.append(f"<line x1='{KX0}' y1='{py}' x2='{KX1}' y2='{py}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{KX0 - 14}' y='{py + 7}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>{y}</text>")
    for x in range(0, 11):
        px, _ = kp(x, 0)
        d.append(f"<line x1='{px}' y1='{KY1}' x2='{px}' y2='{KY0}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{px}' y='{KY0 + 30}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{x}</text>")
    d.append(f"<line x1='{KX0}' y1='{KY0}' x2='{KX1 + 20}' y2='{KY0}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<line x1='{KX0}' y1='{KY0}' x2='{KX0}' y2='{KY1 - 20}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='{KX1 + 10}' y='{KY0 + 64}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>aantal kaarsjes</text>")
    d.append(f"<text x='{KX0 + 14}' y='{KY1 - 22}' {FONT} font-size='21' fill='{TEKST}'>euro</text>")
    for f, kleur, naam, lx in ((lambda x: 20 + 2 * x, BLAUW, "kosten", 10), (lambda x: 6 * x, ROZE, "opbrengst", 9.4)):
        xe = 10 if naam == "kosten" else 10
        a, b = kp(0, f(0)); c, e = kp(xe, f(xe))
        d.append(f"<line x1='{a}' y1='{b}' x2='{c}' y2='{e}' stroke='{kleur}' stroke-width='6'/>")
    tx, ty = kp(10, 40)
    d.append(f"<text x='{tx - 8}' y='{ty + 34}' text-anchor='end' {FONT} font-size='22' font-weight='800' fill='{BLAUW}'>kosten</text>")
    tx, ty = kp(9.4, 56.4)
    d.append(f"<text x='{tx - 16}' y='{ty}' text-anchor='end' {FONT} font-size='22' font-weight='800' fill='{ROZE}'>opbrengst</text>")
    d.append("</svg>")
    (UIT / "kosten-opbrengst.svg").write_text("\n".join(d), encoding="utf-8")


def punt_zone(x, y, r=4.5):
    """Klikvak in procent rond het punt (x, y) van de grafiek."""
    px, py = kp(x, y)
    return [round(px / KB * 100 - r, 1), round(py / KH * 100 - r * KB / KH, 1),
            round(2 * r, 1), round(2 * r * KB / KH, 1)]


def boxplot():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {BB} {BH}' width='{BB}' height='{BH}'>",
         f"<rect width='{BB}' height='{BH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Punten op de toets wiskunde (op 20), klas 4B</text>"]
    y0, y1 = 110, 230
    mid = (y0 + y1) / 2
    d.append(f"<line x1='{bx(BOX['min'])}' y1='{mid}' x2='{bx(BOX['q1'])}' y2='{mid}' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<line x1='{bx(BOX['q3'])}' y1='{mid}' x2='{bx(BOX['max'])}' y2='{mid}' stroke='{TEKST}' stroke-width='4'/>")
    for k in ("min", "max"):
        d.append(f"<line x1='{bx(BOX[k])}' y1='{y0 + 25}' x2='{bx(BOX[k])}' y2='{y1 - 25}' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<rect x='{bx(BOX['q1'])}' y='{y0}' width='{bx(BOX['q3']) - bx(BOX['q1'])}' height='{y1 - y0}' fill='#e9efe4' stroke='{GROEN}' stroke-width='4'/>")
    d.append(f"<line x1='{bx(BOX['med'])}' y1='{y0}' x2='{bx(BOX['med'])}' y2='{y1}' stroke='{GROEN}' stroke-width='6'/>")
    ya = 290
    d.append(f"<line x1='{BX0}' y1='{ya}' x2='{BX1}' y2='{ya}' stroke='{TEKST}' stroke-width='3'/>")
    for s in range(0, 21):
        lang = 14 if s % 2 == 0 else 8
        d.append(f"<line x1='{bx(s)}' y1='{ya}' x2='{bx(s)}' y2='{ya + lang}' stroke='{TEKST}' stroke-width='2'/>")
        if s % 2 == 0:
            d.append(f"<text x='{bx(s)}' y='{ya + 40}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{s}</text>")
    d.append("</svg>")
    (UIT / "boxplot-toets.svg").write_text("\n".join(d), encoding="utf-8")


def box_zone(deel):
    """Klikvak: 'med' (de lijn in de doos) of 'doos' (van Q1 tot Q3)."""
    if deel == "med":
        x = bx(BOX["med"])
        return [round((x - 18) / BB * 100, 1), round(100 / BH * 100, 1), round(36 / BB * 100, 1), round(140 / BH * 100, 1)]
    a, b = bx(BOX["q1"]), bx(BOX["q3"])
    return [round(a / BB * 100, 1), round(100 / BH * 100, 1), round((b - a) / BB * 100, 1), round(140 / BH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    kosten()
    boxplot()
    print("break-even", punt_zone(5, 30), "vaste kosten", punt_zone(0, 20), "med", box_zone("med"), "doos", box_zone("doos"))
