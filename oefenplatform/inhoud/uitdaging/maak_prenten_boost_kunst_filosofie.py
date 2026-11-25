# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Kunstbeschouwing en filosofie
🚀 Boost doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_kunst_filosofie.py

Prent 1: twee kerkgevels in schema, een met rondbogen en een met spitsbogen.
Prent 2: zes vragen in genummerde stroken (weetvraag, meningsvraag, filosofische vraag).
De klikvakken in uitdaging/bron/boost_kunst_filosofie.py staan in procent.
"""
import pathlib
from _blad import blad, zone

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "kunst-filosofie-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"
B, H = 1000, 620


def rondboog(x, y, w, h):
    r = w / 2
    return f"M{x},{y} v{-(h - r)} a{r},{r} 0 0 1 {w},0 v{h - r} z"


def spitsboog(x, y, w, h):
    """Gelijkzijdige spitsboog: twee cirkelbogen met straal w die in een punt samenkomen."""
    top = y - h
    ys = top + w * 0.866
    return (f"M{x},{y} V{ys:.1f} A{w},{w} 0 0 1 {x + w / 2},{top} "
            f"A{w},{w} 0 0 1 {x + w},{ys:.1f} V{y} z")


def gevels():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Twee kerkgevels (schema)</text>"]
    # gebouw A: laag, zwaar, kleine rondboogvensters
    d.append(f"<path d='M80,540 v-260 l170,-110 l170,110 v260 z' fill='#efe6d2' stroke='{TEKST}' stroke-width='4'/>")
    for x in (130, 230, 330):
        d.append(f"<path d='{rondboog(x, 360, 40, 70)}' fill='#6d7f99' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<path d='{rondboog(205, 540, 90, 130)}' fill='#7a5a3a' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='250' y='590' text-anchor='middle' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>A</text>")
    # gebouw B: hoog, slank, spitsbogen en roosvenster
    d.append(f"<path d='M580,540 v-330 l170,-130 l170,130 v330 z' fill='#efe6d2' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<circle cx='750' cy='250' r='48' fill='#6d7f99' stroke='{TEKST}' stroke-width='3'/>")
    for k in range(8):
        import math
        a = k * math.pi / 4
        d.append(f"<line x1='750' y1='250' x2='{750 + 48 * math.cos(a):.1f}' y2='{250 + 48 * math.sin(a):.1f}' stroke='{TEKST}' stroke-width='2'/>")
    for x in (615, 845):
        d.append(f"<path d='{spitsboog(x, 470, 40, 150)}' fill='#6d7f99' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<path d='{spitsboog(705, 540, 90, 190)}' fill='#7a5a3a' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='750' y='590' text-anchor='middle' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>B</text>")
    d.append("</svg>")
    (UIT / "twee-kerkgevels.svg").write_text("\n".join(d), encoding="utf-8")
    return {"A": [7.0, 26.0, 36.0, 70.0], "B": [57.0, 11.0, 36.0, 85.0]}


VRAGEN = [
    "Hoeveel inwoners telt België vandaag?",
    "Vind jij voetbal leuker dan tennis?",
    "Wat maakt een mens tot een mens?",
    "In welk jaar schilderde Rubens zijn bekendste werk?",
    "Is het ooit goed om te liegen?",
    "Welke pizza bestel jij het liefst?",
]

if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(gevels())
    blad(UIT / "zes-vragen.svg", "Zes vragen in de klas", VRAGEN)
    print({i: zone(i, 6) for i in range(1, 7)})
