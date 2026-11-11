# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Engels ✨ Spark (zelf getekend).

    python3 inhoud/uitdaging/maak_prenten_spark_engels.py

De klikvakken in uitdaging/bron/spark_engels.py staan in procent van deze
prenten; wie hier iets verschuift, moet die mee aanpassen.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "engels-spark"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"

# A, B, C, D: de juiste klok (twenty to nine = 8.40) staat op plaats C.
KLOKKEN = [(9, 20), (7, 40), (8, 40), (8, 20)]


def klok(cx, cy, r, uur, minuut, letter):
    d = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#ffffff' stroke='{TEKST}' stroke-width='4'/>"]
    for i in range(12):
        a = math.radians(i * 30)
        x1, y1 = cx + math.sin(a) * (r - 6), cy - math.cos(a) * (r - 6)
        x2, y2 = cx + math.sin(a) * (r - (16 if i % 3 == 0 else 11)), cy - math.cos(a) * (r - (16 if i % 3 == 0 else 11))
        d.append(f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{TEKST}' stroke-width='{4 if i % 3 == 0 else 2}'/>")
    am = math.radians(minuut * 6)
    au = math.radians((uur % 12) * 30 + minuut * 0.5)
    d.append(f"<line x1='{cx}' y1='{cy}' x2='{cx + math.sin(au) * r * 0.5:.1f}' y2='{cy - math.cos(au) * r * 0.5:.1f}' stroke='{TEKST}' stroke-width='7' stroke-linecap='round'/>")
    d.append(f"<line x1='{cx}' y1='{cy}' x2='{cx + math.sin(am) * r * 0.8:.1f}' y2='{cy - math.cos(am) * r * 0.8:.1f}' stroke='#c0392b' stroke-width='4' stroke-linecap='round'/>")
    d.append(f"<circle cx='{cx}' cy='{cy}' r='6' fill='{TEKST}'/>")
    d.append(f"<text x='{cx}' y='{cy + r + 36}' text-anchor='middle' {FONT} font-size='26' font-weight='800' fill='{GROEN}'>{letter}</text>")
    return d


def klokken():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 260' width='800' height='260'>",
         "<rect width='800' height='260' fill='#ffffff'/>"]
    for i, (u, m) in enumerate(KLOKKEN):
        d += klok(100 + i * 200, 110, 80, u, m, "ABCD"[i])
    d.append("</svg>")
    (UIT / "vier-klokken.svg").write_text("\n".join(d), encoding="utf-8")


def gebouw():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 500' width='400' height='500'>",
         "<rect width='400' height='500' fill='#ffffff'/>",
         "<rect x='0' y='480' width='400' height='20' fill='#9bc27a'/>",
         f"<path d='M70 180 L200 95 L330 180 Z' fill='#b5533c' stroke='{TEKST}' stroke-width='3'/>"]
    for y in (180, 280, 380):
        d.append(f"<rect x='80' y='{y}' width='240' height='100' fill='#f1e3c4' stroke='{TEKST}' stroke-width='3'/>")
    for y in (200, 300):
        for x in (105, 175, 245):
            d.append(f"<rect x='{x}' y='{y}' width='50' height='55' fill='#bfdcf2' stroke='{TEKST}' stroke-width='2'/>")
    for x in (105, 245):
        d.append(f"<rect x='{x}' y='400' width='50' height='55' fill='#bfdcf2' stroke='{TEKST}' stroke-width='2'/>")
    d.append(f"<rect x='178' y='405' width='44' height='75' fill='#6b4a2b' stroke='{TEKST}' stroke-width='2'/>")
    d.append("</svg>")
    (UIT / "gebouw-verdiepingen.svg").write_text("\n".join(d), encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    klokken()
    gebouw()
