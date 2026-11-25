# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Gezondheid, zorg en welzijn
🚀 Boost dubbele finaliteit: een eenvoudige doorsnede van het oog met vijf
genummerde delen en zes verzonnen situaties uit zorg en huishouden.

    python3 inhoud/uitdaging/maak_prenten_boost_df_gzw.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad, zone  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "gzw-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"
B, H = 1000, 620
CX, CY, R = 560, 340, 210


def pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def nummer(d, x, y, n):
    d.append(f"<circle cx='{x}' cy='{y}' r='22' fill='{GROEN}'/>")
    d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='#ffffff'>{n}</text>")


def oog():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='52' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Doorsnede van het oog (zijaanzicht)</text>",
         f"<text x='60' y='{CY + 8}' {FONT} font-size='20' font-style='italic' fill='{ORANJE}'>licht →</text>",
         # oogbol
         f"<circle cx='{CX}' cy='{CY}' r='{R}' fill='#fdfbf4' stroke='{TEKST}' stroke-width='4'/>",
         # netvlies: binnenrand achteraan
         f"<path d='M {CX + 60} {CY - 190} A 200 200 0 0 1 {CX + 60} {CY + 190}' fill='none' stroke='{ORANJE}' stroke-width='10'/>",
         # oogzenuw
         f"<rect x='{CX + R - 6}' y='{CY - 22}' width='190' height='44' rx='10' fill='#f1dfb8' stroke='{TEKST}' stroke-width='3'/>",
         # hoornvlies: bolling vooraan
         f"<path d='M {CX - R + 22} {CY - 95} Q {CX - R - 70} {CY} {CX - R + 22} {CY + 95}' fill='#e4eef8' stroke='{BLAUW}' stroke-width='5'/>",
         # iris boven en onder, met de pupil ertussen
         f"<rect x='{CX - R + 40}' y='{CY - 110}' width='16' height='78' fill='{BLAUW}'/>",
         f"<rect x='{CX - R + 40}' y='{CY + 32}' width='16' height='78' fill='{BLAUW}'/>",
         # lens
         f"<ellipse cx='{CX - R + 100}' cy='{CY}' rx='30' ry='78' fill='#fff3c9' stroke='{TEKST}' stroke-width='3'/>"]
    pos = {1: (CX + 215, CY - 150),   # netvlies
           2: (CX - R + 100, CY - 120),  # lens
           3: (CX - R - 60, CY - 105),  # hoornvlies
           4: (CX + R + 120, CY - 60),  # oogzenuw
           5: (CX - R + 48, CY - 150)}  # iris
    lijn = {1: (CX + 160, CY - 120), 2: (CX - R + 100, CY - 78), 3: (CX - R - 20, CY - 60),
            4: (CX + R + 120, CY - 22), 5: (CX - R + 48, CY - 110)}
    for n, (x, y) in pos.items():
        lx, ly = lijn[n]
        d.append(f"<line x1='{x}' y1='{y}' x2='{lx}' y2='{ly}' stroke='{TEKST}' stroke-width='2'/>")
    for n, (x, y) in pos.items():
        nummer(d, x, y, n)
    d.append("</svg>")
    (UIT / "oog-doorsnede.svg").write_text("\n".join(d), encoding="utf-8")
    z = {1: pct(CX + 50, CY - 200, 210, 400), 2: pct(CX - R + 60, CY - 150, 80, 240),
         3: pct(CX - R - 90, CY - 135, 120, 240), 4: pct(CX + R - 6, CY - 90, 200, 120),
         5: pct(CX - R + 22, CY - 180, 52, 300)}
    return z


SITUATIES = [
    "Een vrouw van vijftig gaat naar het bevolkingsonderzoek naar borstkanker.",
    "Iemand snijdt rauwe kip en daarna tomaten op dezelfde plank.",
    "Een man zakt in elkaar op straat en ademt niet meer normaal.",
    "Een kind heeft hoge koorts op zondagnacht, maar het is geen spoed.",
    "Op een fles poetsproduct staat een etiket met een gevarenpictogram.",
    "Een jogger verzwikt zijn enkel en die zwelt snel op.",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("oog", oog())
    blad(UIT / "zes-situaties.svg", "Zes situaties (verzonnen)", SITUATIES, grootte=21)
