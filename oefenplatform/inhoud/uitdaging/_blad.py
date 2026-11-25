# -*- coding: utf-8 -*-
"""Gedeelde tekenhulp voor klikprenten met genummerde zinnen (een tekst, een
brief, een bron). Elke zin is een even hoge strook; zone(i, n) geeft het
klikvak van zin i (vanaf 1) in procent.
"""
from xml.sax.saxutils import escape

FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"
B, KOP, STROOK = 1000, 90, 92


def hoogte(n):
    return KOP + n * STROOK + 30


def zone(i, n):
    h = hoogte(n)
    return [2, round((KOP + (i - 1) * STROOK) / h * 100, 1), 96, round(STROOK / h * 100, 1)]


def blad(pad, titel, regels, cursief=False, grootte=23):
    h = hoogte(len(regels))
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {h}' width='{B}' height='{h}'>",
         f"<rect width='{B}' height='{h}' fill='#ffffff'/>",
         f"<text x='40' y='58' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>{escape(titel)}</text>"]
    for i, r in enumerate(regels):
        y = KOP + i * STROOK
        d.append(f"<rect x='24' y='{y + 6}' width='{B - 48}' height='{STROOK - 12}' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<circle cx='68' cy='{y + STROOK / 2}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='68' y='{y + STROOK / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        stijl = " font-style='italic'" if cursief else ""
        d.append(f"<text x='108' y='{y + STROOK / 2 + 9}' {FONT} font-size='{grootte}'{stijl} fill='{TEKST}'>{escape(r)}</text>")
    d.append("</svg>")
    pad.write_text("\n".join(d), encoding="utf-8")
