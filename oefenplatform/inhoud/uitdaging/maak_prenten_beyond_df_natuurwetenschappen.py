# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Natuurwetenschappen 🌍 Beyond
dubbele finaliteit: een voedingsetiket van een (verzonnen) ontbijtgranen en
een transversale golf met drie genummerde pijlen.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_natuurwetenschappen.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_df_natuurwetenschappen.py.
"""
import math
import pathlib
from _blad import blad

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "natuurwetenschappen-beyond-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

ETIKET = [
    "Energie per 100 g: 1600 kJ (380 kcal)",
    "Vetten: 4 g, waarvan verzadigde vetzuren: 1 g",
    "Koolhydraten: 75 g, waarvan suikers: 22 g",
    "Voedingsvezels: 6 g",
    "Eiwitten: 8 g",
    "Zout: 0,9 g",
]

B, H = 1000, 520
X0, X1, YM, A = 90, 930, 290, 120  # twee golflengtes over X0..X1


def pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def pijl(d, x1, y1, x2, y2, kleur):
    d.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{kleur}' stroke-width='3.5'/>")
    for (xa, ya, xb, yb) in ((x1, y1, x2, y2), (x2, y2, x1, y1)):
        hoek = math.atan2(yb - ya, xb - xa)
        for s in (-1, 1):
            d.append(f"<line x1='{xa}' y1='{ya}' x2='{xa + 16 * math.cos(hoek + s * 0.45):.1f}' y2='{ya + 16 * math.sin(hoek + s * 0.45):.1f}' stroke='{kleur}' stroke-width='3.5'/>")


def golf():
    lam = (X1 - X0) / 2
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een transversale golf</text>",
         f"<line x1='{X0}' y1='{YM}' x2='{X1}' y2='{YM}' stroke='#b9b29c' stroke-width='2' stroke-dasharray='10 8'/>"]
    pts = []
    for i in range(0, 401):
        x = X0 + (X1 - X0) * i / 400
        pts.append(f"{x:.1f},{YM - A * math.sin(2 * math.pi * (x - X0) / lam):.1f}")
    d.append(f"<polyline points='{' '.join(pts)}' fill='none' stroke='{BLAUW}' stroke-width='5'/>")
    top1 = X0 + lam / 4
    top2 = top1 + lam
    dal1 = X0 + 3 * lam / 4
    # 1: amplitude (evenwicht tot top), 2: golflengte (top tot top), 3: top tot dal
    pijl(d, top1, YM, top1, YM - A, ORANJE)
    pijl(d, top1, YM - A - 30, top2, YM - A - 30, ORANJE)
    pijl(d, top1, YM + A + 40, dal1, YM + A + 40, ORANJE)
    z = {}
    for nr, (x, y) in {"1": (top1 - 34, YM - A / 2), "2": ((top1 + top2) / 2, YM - A - 60),
                       "3": ((top1 + dal1) / 2, YM + A + 78)}.items():
        d.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='20' fill='#ffffff' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<text x='{x:.1f}' y='{y + 8:.1f}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{TEKST}'>{nr}</text>")
        z[nr] = pct(x - 32, y - 32, 64, 64)
    d.append("</svg>")
    (UIT / "golf-pijlen.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    blad(UIT / "etiket-granen.svg", "Voedingswaarde van ontbijtgranen (verzonnen)", ETIKET, grootte=23)
    print("golf", golf())
