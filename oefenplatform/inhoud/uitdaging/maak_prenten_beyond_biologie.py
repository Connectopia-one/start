# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Biologie 🌍 Beyond.

    python3 inhoud/uitdaging/maak_prenten_beyond_biologie.py

Prent 1: een dierlijke cel met vijf genummerde organellen.
Prent 2: een stamboom van een familie met een autosomaal recessieve aandoening.
De klikvakken in uitdaging/bron/beyond_biologie.py staan in procent.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "biologie-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"

CB, CH = 1000, 620
# organel -> (x, y) van het middelpunt
ORGANEL = {"kern": (470, 320), "mitochondrion": (720, 230), "ruw ER": (300, 450), "golgi": (690, 440), "lysosoom": (250, 220)}
NUMMER = {"kern": 1, "mitochondrion": 2, "ruw ER": 3, "golgi": 4, "lysosoom": 5}


def num(x, y, n):
    return (f"<circle cx='{x}' cy='{y}' r='20' fill='{GROEN}'/>"
            f"<text x='{x}' y='{y + 7}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{n}</text>")


def cel():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {CB} {CH}' width='{CB}' height='{CH}'>",
         f"<rect width='{CB}' height='{CH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een dierlijke cel (schema)</text>",
         f"<ellipse cx='500' cy='340' rx='430' ry='250' fill='#fbf3e4' stroke='#8a6d3b' stroke-width='5'/>"]
    x, y = ORGANEL["kern"]
    d.append(f"<circle cx='{x}' cy='{y}' r='95' fill='#e7d9f0' stroke='#6b4c84' stroke-width='5'/>")
    d.append(f"<circle cx='{x + 20}' cy='{y - 10}' r='30' fill='#b79bcc'/>")
    x, y = ORGANEL["mitochondrion"]
    d.append(f"<ellipse cx='{x}' cy='{y}' rx='85' ry='42' fill='#f5d0b5' stroke='#b5523b' stroke-width='4'/>")
    d.append(f"<path d='M{x - 60},{y} q12,-30 24,0 q12,30 24,0 q12,-30 24,0 q12,30 24,0 q12,-30 24,0' stroke='#b5523b' stroke-width='3' fill='none'/>")
    x, y = ORGANEL["ruw ER"]
    for i in range(4):
        d.append(f"<path d='M{x - 110},{y - 45 + i * 28} q110,-24 220,0' stroke='#3f7a9a' stroke-width='5' fill='none'/>")
        for k in range(8):
            d.append(f"<circle cx='{x - 100 + k * 27}' cy='{y - 52 + i * 28 - (6 if 2 <= k <= 5 else 2)}' r='4' fill='{TEKST}'/>")
    x, y = ORGANEL["golgi"]
    for i in range(4):
        d.append(f"<path d='M{x - 80 + i * 6},{y - 30 + i * 18} q{80 - i * 6},-26 {160 - i * 12},0' stroke='#c99a2e' stroke-width='9' fill='none' stroke-linecap='round'/>")
    d.append(f"<circle cx='{x + 95}' cy='{y - 30}' r='10' fill='#c99a2e'/>")
    x, y = ORGANEL["lysosoom"]
    d.append(f"<circle cx='{x}' cy='{y}' r='38' fill='#d8e8c9' stroke='{GROEN}' stroke-width='4'/>")
    for k in range(5):
        d.append(f"<circle cx='{x - 15 + k * 8}' cy='{y + (k % 2) * 10 - 5}' r='4' fill='{GROEN}'/>")
    plaats = {"kern": (470, 200), "mitochondrion": (820, 190), "ruw ER": (180, 410), "golgi": (800, 470), "lysosoom": (190, 175)}
    for o, (nx, ny) in plaats.items():
        d.append(num(nx, ny, NUMMER[o]))
    d.append("</svg>")
    (UIT / "dierlijke-cel.svg").write_text("\n".join(d), encoding="utf-8")


def organel_zone(o):
    vakken = {"kern": (370, 220, 200, 200), "mitochondrion": (630, 175, 210, 100), "ruw ER": (180, 380, 240, 110),
              "golgi": (600, 395, 210, 110), "lysosoom": (200, 170, 100, 100)}
    x, y, b, h = vakken[o]
    return [round(x / CB * 100, 1), round(y / CH * 100, 1), round(b / CB * 100, 1), round(h / CH * 100, 1)]


SB, SH = 1000, 520
# persoon -> (x, y, geslacht m/v, aangetast)
MENSEN = {1: (380, 150, "m", False), 2: (620, 150, "v", False),
          3: (260, 360, "m", False), 4: (500, 360, "v", True), 5: (740, 360, "v", False)}


def stamboom():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {SB} {SH}' width='{SB}' height='{SH}'>",
         f"<rect width='{SB}' height='{SH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Stamboom van een familie</text>",
         f"<line x1='410' y1='150' x2='590' y2='150' stroke='{TEKST}' stroke-width='3'/>",
         f"<line x1='500' y1='150' x2='500' y2='260' stroke='{TEKST}' stroke-width='3'/>",
         f"<line x1='260' y1='260' x2='740' y2='260' stroke='{TEKST}' stroke-width='3'/>"]
    for n, (x, y, g, ziek) in MENSEN.items():
        if y > 200:
            d.append(f"<line x1='{x}' y1='260' x2='{x}' y2='{y - 30}' stroke='{TEKST}' stroke-width='3'/>")
        kleur = TEKST if ziek else "#ffffff"
        if g == "m":
            d.append(f"<rect x='{x - 30}' y='{y - 30}' width='60' height='60' fill='{kleur}' stroke='{TEKST}' stroke-width='3'/>")
        else:
            d.append(f"<circle cx='{x}' cy='{y}' r='31' fill='{kleur}' stroke='{TEKST}' stroke-width='3'/>")
        d.append(f"<text x='{x}' y='{y + 62}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{GROEN}'>{n}</text>")
    d.append(f"<text x='40' y='{SH - 50}' {FONT} font-size='18' fill='{TEKST}'>vierkant = man, cirkel = vrouw</text>")
    d.append(f"<text x='40' y='{SH - 22}' {FONT} font-size='18' fill='{TEKST}'>zwart = heeft de aandoening</text>")
    d.append("</svg>")
    (UIT / "stamboom-recessief.svg").write_text("\n".join(d), encoding="utf-8")


def mens_zone(n):
    x, y, _, _ = MENSEN[n]
    return [round((x - 50) / SB * 100, 1), round((y - 45) / SH * 100, 1), round(100 / SB * 100, 1), round(130 / SH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    cel()
    stamboom()
    print({o: organel_zone(o) for o in ORGANEL}, {n: mens_zone(n) for n in MENSEN})
