# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Chemie 🚀 Boost doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_chemie.py

Prent 1: de eerste drie perioden van het periodiek systeem (hoofdgroepen).
Prent 2: een pH-schaal met vijf oplossingen in genummerde vakjes.
De klikvakken in uitdaging/bron/boost_chemie.py staan in procent.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "chemie-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

RIJEN = [
    [("H", 1), None, None, None, None, None, None, ("He", 2)],
    [("Li", 3), ("Be", 4), ("B", 5), ("C", 6), ("N", 7), ("O", 8), ("F", 9), ("Ne", 10)],
    [("Na", 11), ("Mg", 12), ("Al", 13), ("Si", 14), ("P", 15), ("S", 16), ("Cl", 17), ("Ar", 18)],
]
GROEPEN = ["IA", "IIA", "IIIA", "IVA", "VA", "VIA", "VIIA", "VIIIA"]


def pse():
    B, H = 1000, 520
    X0, Y0, W = 70, 110, 110
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Periodiek systeem: perioden 1 tot 3</text>"]
    for k, g in enumerate(GROEPEN):
        d.append(f"<text x='{X0 + k * W + W / 2}' y='{Y0 - 14}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{BLAUW}'>{g}</text>")
    zones = {}
    for r, rij in enumerate(RIJEN):
        d.append(f"<text x='{X0 - 24}' y='{Y0 + r * W + W / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='700' fill='{BLAUW}'>{r + 1}</text>")
        for k, el in enumerate(rij):
            if not el:
                continue
            x, y = X0 + k * W, Y0 + r * W
            d.append(f"<rect x='{x + 4}' y='{y + 4}' width='{W - 8}' height='{W - 8}' rx='10' fill='#f7f4ec' stroke='#b9b29c' stroke-width='2'/>")
            d.append(f"<text x='{x + 14}' y='{y + 30}' {FONT} font-size='18' fill='{TEKST}'>{el[1]}</text>")
            d.append(f"<text x='{x + W / 2}' y='{y + 78}' text-anchor='middle' {FONT} font-size='38' font-weight='800' fill='{TEKST}'>{el[0]}</text>")
            zones[el[0]] = [round(x / B * 100, 1), round(y / H * 100, 1), round(W / B * 100, 1), round(W / H * 100, 1)]
    d.append(f"<text x='40' y='{H - 30}' {FONT} font-size='20' fill='{TEKST}'>Het kleine getal is het atoomnummer.</text>")
    d.append("</svg>")
    (UIT / "periodiek-systeem.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


def ph():
    B, H = 1000, 470
    X0, X1, Y = 60, 940, 300
    stap = (X1 - X0) / 14
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Vijf oplossingen op de pH-schaal</text>",
         "<defs><linearGradient id='g' x1='0' x2='1'><stop offset='0' stop-color='#e7a3a3'/><stop offset='0.5' stop-color='#eef2e6'/><stop offset='1' stop-color='#a9c0e0'/></linearGradient></defs>",
         f"<rect x='{X0}' y='{Y}' width='{X1 - X0}' height='40' rx='8' fill='url(#g)' stroke='{TEKST}' stroke-width='2'/>"]
    for p in range(15):
        x = X0 + p * stap
        d.append(f"<line x1='{x}' y1='{Y + 40}' x2='{x}' y2='{Y + 52}' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<text x='{x}' y='{Y + 76}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{p}</text>")
    d.append(f"<text x='{X0 + 7 * stap}' y='{Y + 110}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>pH</text>")
    oplossingen = [(1.5, "maagsap"), (3, "azijn"), (7, "zuiver water"), (10, "zeepsop"), (13, "ontstopper")]
    zones = {}
    for i, (p, naam) in enumerate(oplossingen):
        x = X0 + p * stap
        w, h, y = 150, 120, 110
        bx = 30 + i * 194
        d.append(f"<rect x='{bx}' y='{y}' width='{w}' height='{h}' rx='14' fill='#f7f4ec' stroke='#b9b29c' stroke-width='2'/>")
        d.append(f"<circle cx='{bx + w / 2}' cy='{y + 34}' r='20' fill='{GROEN}'/>")
        d.append(f"<text x='{bx + w / 2}' y='{y + 42}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        d.append(f"<text x='{bx + w / 2}' y='{y + 92}' text-anchor='middle' {FONT} font-size='21' fill='{TEKST}'>{naam}</text>")
        d.append(f"<line x1='{bx + w / 2}' y1='{y + h}' x2='{x}' y2='{Y}' stroke='{ORANJE}' stroke-width='3'/>")
        zones[i + 1] = [round(bx / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]
    d.append("</svg>")
    (UIT / "ph-schaal.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(pse())
    print(ph())
