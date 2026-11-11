# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging techniek ✨ Spark (zelf getekend):
drie tandwielen in een rij en drie rekjes.

    python3 inhoud/uitdaging/maak_prenten_spark_techniek.py

De klikvakken in uitdaging/bron/spark_techniek.py staan in procent van deze
prenten; wie hier iets verschuift, moet die mee aanpassen.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "techniek-spark"
FONT = "font-family='Nunito, Arial, sans-serif'"
TEKST = "#2b2b2b"


def tandwiel(cx, cy, r, tanden, kleur, label):
    pts = []
    for i in range(tanden * 2):
        a = math.pi * 2 * i / (tanden * 2)
        rr = r + 9 if i % 2 == 0 else r - 3
        for da in (-0.35, 0.35):
            aa = a + da * math.pi / (tanden * 2)
            pts.append(f"{cx + math.cos(aa) * rr:.1f},{cy + math.sin(aa) * rr:.1f}")
    d = [f"<polygon points='{' '.join(pts)}' fill='{kleur}' stroke='{TEKST}' stroke-width='2'/>",
         f"<circle cx='{cx}' cy='{cy}' r='8' fill='#ffffff' stroke='{TEKST}' stroke-width='2'/>",
         f"<text x='{cx}' y='{cy + r + 42}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>{label}</text>"]
    return d


def tandwielen():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 360' width='800' height='360'>",
         "<rect width='800' height='360' fill='#ffffff'/>"]
    # A: 30 tanden (r 120), B: 20 tanden (r 80), C: 10 tanden (r 40); ze grijpen in elkaar.
    d += tandwiel(150, 160, 120, 30, "#e8b820", "A · 30 tanden")
    d += tandwiel(150 + 120 + 80 + 6, 160, 80, 20, "#7fb3e0", "B · 20 tanden")
    d += tandwiel(150 + 120 + 80 + 6 + 80 + 40 + 6, 160, 40, 10, "#9bc27a", "C · 10 tanden")
    d.append("</svg>")
    (UIT / "drie-tandwielen.svg").write_text("\n".join(d), encoding="utf-8")


def rekjes():
    d = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 320' width='800' height='320'>",
         "<rect width='800' height='320' fill='#ffffff'/>"]
    for i, soort in enumerate(["leeg", "schuin", "midden"]):
        x = 60 + i * 250
        d.append(f"<rect x='{x}' y='40' width='180' height='200' fill='none' stroke='#6b4a2b' stroke-width='10'/>")
        if soort == "schuin":
            d.append(f"<line x1='{x}' y1='240' x2='{x + 180}' y2='40' stroke='#6b4a2b' stroke-width='10'/>")
        if soort == "midden":
            d.append(f"<line x1='{x}' y1='140' x2='{x + 180}' y2='140' stroke='#6b4a2b' stroke-width='10'/>")
        d.append(f"<text x='{x + 90}' y='290' text-anchor='middle' {FONT} font-size='26' font-weight='800' fill='#2f4a22'>{'ABC'[i]}</text>")
    d.append("</svg>")
    (UIT / "drie-rekjes.svg").write_text("\n".join(d), encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tandwielen()
    rekjes()
