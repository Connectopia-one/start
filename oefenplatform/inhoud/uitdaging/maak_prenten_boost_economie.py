# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Economie 🚀 Boost doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_economie.py

Prent 1: een markt met een vraag- en een aanbodcurve en vijf genummerde punten.
Prent 2: zes posten van een balans in genummerde stroken.
De klikvakken in uitdaging/bron/boost_economie.py staan in procent.
"""
import pathlib

from _blad import blad, zone

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "economie-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

B, H = 1000, 620
X0, X1, Y0, Y1 = 120, 900, 540, 130     # assen: q van 0 tot 100, p van 0 tot 10


def px(q, p):
    return X0 + (X1 - X0) * q / 100, Y0 - (Y0 - Y1) * p / 10


def vraag(q):        # p = 9 - 0.08 q
    return 9 - 0.08 * q


def aanbod(q):       # p = 1 + 0.08 q
    return 1 + 0.08 * q


# evenwicht bij q = 50, p = 5; bij p = 7: vraag q = 25, aanbod q = 75
PUNTEN = {1: (50, 5), 2: (25, 7), 3: (75, 7), 4: (75, 3), 5: (25, 3)}


def markt():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De markt voor verse aardbeien</text>",
         f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 20}' y2='{Y0}' stroke='{TEKST}' stroke-width='3'/>",
         f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 20}' stroke='{TEKST}' stroke-width='3'/>",
         f"<text x='{X1 + 10}' y='{Y0 + 62}' text-anchor='end' {FONT} font-size='22' fill='{TEKST}'>hoeveelheid (kg)</text>",
         f"<text x='{X0 - 14}' y='{Y1 - 30}' {FONT} font-size='22' fill='{TEKST}'>prijs (euro/kg)</text>"]
    for p in range(0, 11, 2):
        x, y = px(0, p)
        d.append(f"<text x='{x - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>{p}</text>")
    for q in range(0, 101, 25):
        x, y = px(q, 0)
        d.append(f"<text x='{x}' y='{y + 28}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{q}</text>")
    for p in (3, 5, 7):
        xa, ya = px(0, p)
        xb, _ = px(100, p)
        d.append(f"<line x1='{xa}' y1='{ya}' x2='{xb}' y2='{ya}' stroke='#cccccc' stroke-width='2' stroke-dasharray='8 6'/>")
    xa, ya = px(0, vraag(0))
    xb, yb = px(100, vraag(100))
    d.append(f"<line x1='{xa}' y1='{ya}' x2='{xb}' y2='{yb}' stroke='{BLAUW}' stroke-width='5'/>")
    lx, ly = px(88, vraag(88))
    d.append(f"<text x='{lx}' y='{ly + 48}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='{BLAUW}'>vraag</text>")
    xa, ya = px(0, aanbod(0))
    xb, yb = px(100, aanbod(100))
    d.append(f"<line x1='{xa}' y1='{ya}' x2='{xb}' y2='{yb}' stroke='{ORANJE}' stroke-width='5'/>")
    lx, ly = px(86, aanbod(86))
    d.append(f"<text x='{lx - 20}' y='{ly - 30}' text-anchor='end' {FONT} font-size='24' font-weight='800' fill='{ORANJE}'>aanbod</text>")
    zones = {}
    for n, (q, p) in PUNTEN.items():
        x, y = px(q, p)
        d.append(f"<circle cx='{x}' cy='{y}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{n}</text>")
        zones[n] = [round((x - 35) / B * 100, 1), round((y - 35) / H * 100, 1), round(70 / B * 100, 1), round(70 / H * 100, 1)]
    d.append("</svg>")
    (UIT / "markt-aardbeien.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


BALANS = ["Gebouwen", "Voorraad handelsgoederen", "Kapitaal", "Lening op tien jaar", "Leveranciers", "Tegoed op de bankrekening"]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(markt())
    blad(UIT / "balansposten.svg", "Zes posten van de balans van bv Fietsenhof", BALANS)
    print({i: zone(i, len(BALANS)) for i in range(1, 7)})
