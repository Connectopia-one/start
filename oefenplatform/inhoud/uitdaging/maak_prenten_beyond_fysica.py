# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Fysica 🌍 Beyond doorstroom:
de uitwijking van een harmonische trilling en de vervalcurve van een
radioactieve stof.

    python3 inhoud/uitdaging/maak_prenten_beyond_fysica.py

De klikvakken in uitdaging/bron/beyond_fysica.py rekenen met de maten
hieronder (procent van de prent).
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "fysica-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"

# trilling: u(t) = 4 sin(2 pi t / 0,8) cm, t van 0 tot 2 s
GB, GH = 1000, 600
X0, X1, YM, SCH = 110, 920, 300, 40          # SCH = pixels per cm
A, T = 4, 0.8


def gp(t, u):
    return X0 + (X1 - X0) * t / 2, YM - u * SCH


def trilling():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een massa trilt aan een veer</text>"]
    for u in range(-5, 6):
        _, y = gp(0, u)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        if u % 1 == 0 and u != 0:
            d.append(f"<text x='{X0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='18' fill='{TEKST}'>{u}</text>")
    for k in range(0, 21, 2):
        t = k / 10
        x, _ = gp(t, 0)
        d.append(f"<line x1='{x}' y1='{gp(0, 5)[1]}' x2='{x}' y2='{gp(0, -5)[1]}' stroke='#ebe6d8' stroke-width='1.5'/>")
        lab = f"{t:.1f}".replace(".", ",")
        d.append(f"<text x='{x}' y='{gp(0, -5)[1] + 30}' text-anchor='middle' {FONT} font-size='18' fill='{TEKST}'>{lab}</text>")
    d.append(f"<line x1='{X0}' y1='{YM}' x2='{X1 + 15}' y2='{YM}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{X0}' y1='{gp(0, -5.3)[1]}' x2='{X0}' y2='{gp(0, 5.6)[1]}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X0 - 14}' y='{YM + 7}' text-anchor='end' {FONT} font-size='18' fill='{TEKST}'>0</text>")
    d.append(f"<text x='{X1 + 10}' y='{gp(0, -5)[1] + 64}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>t (s)</text>")
    d.append(f"<text x='{X0 + 12}' y='{gp(0, 5.6)[1] - 4}' {FONT} font-size='20' fill='{TEKST}'>u (cm)</text>")
    pts = " ".join(f"{gp(i / 200, A * math.sin(2 * math.pi * (i / 200) / T))[0]:.1f},{gp(i / 200, A * math.sin(2 * math.pi * (i / 200) / T))[1]:.1f}" for i in range(0, 401))
    d.append(f"<polyline points='{pts}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    d.append("</svg>")
    (UIT / "trilling-u-t.svg").write_text("\n".join(d), encoding="utf-8")


def t_zone(t, r=32):
    x, y = gp(t, A * math.sin(2 * math.pi * t / T))
    return [round((x - r) / GB * 100, 1), round((y - r) / GH * 100, 1),
            round(2 * r / GB * 100, 1), round(2 * r / GH * 100, 1)]


# verval: A(t) = 800 * (1/2)^(t/6) Bq, t van 0 tot 30 uur
VB, VH = 1000, 600
VX0, VX1, VY0, VY1 = 110, 920, 510, 100
A0, TH = 800, 6


def vp(t, a):
    return VX0 + (VX1 - VX0) * t / 30, VY0 - (VY0 - VY1) * a / 900


def verval():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {VB} {VH}' width='{VB}' height='{VH}'>",
         f"<rect width='{VB}' height='{VH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Activiteit van een radioactieve bron</text>"]
    for a in range(0, 901, 100):
        _, y = vp(0, a)
        d.append(f"<line x1='{VX0}' y1='{y}' x2='{VX1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{VX0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='18' fill='{TEKST}'>{a}</text>")
    for t in range(0, 31, 3):
        x, _ = vp(t, 0)
        d.append(f"<line x1='{x}' y1='{VY1}' x2='{x}' y2='{VY0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{VY0 + 30}' text-anchor='middle' {FONT} font-size='18' fill='{TEKST}'>{t}</text>")
    d.append(f"<line x1='{VX0}' y1='{VY0}' x2='{VX1 + 15}' y2='{VY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{VX0}' y1='{VY0}' x2='{VX0}' y2='{VY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{VX1 + 10}' y='{VY0 + 64}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>tijd (uur)</text>")
    d.append(f"<text x='{VX0 + 12}' y='{VY1 - 22}' {FONT} font-size='20' fill='{TEKST}'>activiteit (Bq)</text>")
    pts = " ".join(f"{vp(i / 10, A0 * 0.5 ** (i / 10 / TH))[0]:.1f},{vp(i / 10, A0 * 0.5 ** (i / 10 / TH))[1]:.1f}" for i in range(0, 301))
    d.append(f"<polyline points='{pts}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    d.append("</svg>")
    (UIT / "vervalcurve-activiteit.svg").write_text("\n".join(d), encoding="utf-8")


def v_zone(t, r=34):
    x, y = vp(t, A0 * 0.5 ** (t / TH))
    return [round((x - r) / VB * 100, 1), round((y - r) / VH * 100, 1),
            round(2 * r / VB * 100, 1), round(2 * r / VH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    trilling()
    verval()
    print("nul", [t_zone(t) for t in (0.4, 0.8, 1.2, 1.6)], "min", [t_zone(t) for t in (0.6, 1.4)],
          "kwart", v_zone(12), "half", v_zone(6))
