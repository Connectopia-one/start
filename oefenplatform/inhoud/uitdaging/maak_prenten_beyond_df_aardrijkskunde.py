# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Aardrijkskunde 🌍 Beyond dubbele
finaliteit: een klimatogram van een (verzonnen) mediterrane stad en de aarde
op vier plaatsen in haar baan rond de zon.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_aardrijkskunde.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_df_aardrijkskunde.py.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "aardrijkskunde-beyond-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

# klimatogram: T in °C (rode lijn), N in mm (blauwe staven)
MAAND = "JFMAMJJASOND"
T = [9, 10, 12, 15, 19, 23, 26, 26, 22, 18, 13, 10]
N = [80, 70, 60, 55, 35, 15, 5, 10, 45, 95, 110, 95]
B, H = 1000, 600
X0, X1, Y0, Y1 = 120, 880, 500, 110  # T 0..30, N 0..120


def pct(x, y, w, h, b, hh):
    return [round(x / b * 100, 1), round(y / hh * 100, 1), round(w / b * 100, 1), round(h / hh * 100, 1)]


def klimatogram():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Klimatogram van een kuststad (verzonnen)</text>"]
    bw = (X1 - X0) / 12
    for k in range(0, 31, 5):
        y = Y0 - (Y0 - Y1) * k / 30
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 12}' y='{y + 7}' text-anchor='end' {FONT} font-size='18' fill='{ORANJE}'>{k}</text>")
        d.append(f"<text x='{X1 + 12}' y='{y + 7}' {FONT} font-size='18' fill='{BLAUW}'>{k * 4}</text>")
    d.append(f"<text x='{X0 - 12}' y='{Y1 - 24}' text-anchor='end' {FONT} font-size='19' fill='{ORANJE}'>T (°C)</text>")
    d.append(f"<text x='{X1 + 8}' y='{Y1 - 24}' {FONT} font-size='19' fill='{BLAUW}'>N (mm)</text>")
    z = {}
    for i, (t, n) in enumerate(zip(T, N)):
        x = X0 + i * bw
        h = (Y0 - Y1) * n / 120
        d.append(f"<rect x='{x + bw * 0.15:.1f}' y='{Y0 - h:.1f}' width='{bw * 0.7:.1f}' height='{h:.1f}' fill='{BLAUW}' opacity='0.75'/>")
        d.append(f"<text x='{x + bw / 2:.1f}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{MAAND[i]}</text>")
        z[i + 1] = pct(x, Y1, bw, Y0 - Y1 + 40, B, H)
    pts = " ".join(f"{X0 + (i + 0.5) * bw:.1f},{Y0 - (Y0 - Y1) * t / 30:.1f}" for i, t in enumerate(T))
    d.append(f"<polyline points='{pts}' fill='none' stroke='{ORANJE}' stroke-width='5'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1}' y2='{Y0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append("</svg>")
    (UIT / "klimatogram-kuststad.svg").write_text("\n".join(d), encoding="utf-8")
    return z


# baan van de aarde
OB, OH = 1000, 620
CX, CY, RX, RY = 500, 340, 360, 190


def baan():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {OB} {OH}' width='{OB}' height='{OH}'>",
         f"<rect width='{OB}' height='{OH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De aarde op vier plaatsen in haar baan</text>",
         f"<ellipse cx='{CX}' cy='{CY}' rx='{RX}' ry='{RY}' fill='none' stroke='#b9b29c' stroke-width='3' stroke-dasharray='10 8'/>",
         f"<circle cx='{CX}' cy='{CY}' r='48' fill='#f6c945' stroke='{ORANJE}' stroke-width='3'/>",
         f"<text x='{CX}' y='{CY + 8}' text-anchor='middle' {FONT} font-size='21' font-weight='800' fill='{TEKST}'>zon</text>"]
    plaatsen = {"A": (CX - RX, CY), "B": (CX, CY + RY), "C": (CX + RX, CY), "D": (CX, CY - RY)}
    hoek = math.radians(23.5)
    dx, dy = math.sin(hoek) * 52, -math.cos(hoek) * 52
    z = {}
    for letter, (x, y) in plaatsen.items():
        # de as wijst altijd naar dezelfde kant (naar rechts): bij A helt de noordpool naar de zon toe (21 juni)
        d.append(f"<circle cx='{x}' cy='{y}' r='34' fill='#dbe7f3' stroke='{BLAUW}' stroke-width='3'/>")
        d.append(f"<line x1='{x - dx:.1f}' y1='{y - dy:.1f}' x2='{x + dx:.1f}' y2='{y + dy:.1f}' stroke='{TEKST}' stroke-width='3'/>")
        d.append(f"<text x='{x + dx + 4:.1f}' y='{y + dy - 6:.1f}' {FONT} font-size='18' font-weight='700' fill='{TEKST}'>N</text>")
        ly = y + 64 if letter != "B" else y + 66
        lx = x if letter in "BD" else (x - 62 if letter == "A" else x + 62)
        ly = y + 8 if letter in "AC" else (y - 50 if letter == "D" else y + 70)
        d.append(f"<text x='{lx}' y='{ly}' text-anchor='middle' {FONT} font-size='26' font-weight='800' fill='{GROEN}'>{letter}</text>")
        z[letter] = pct(x - 48, y - 60, 96, 120, OB, OH)
    d.append("</svg>")
    (UIT / "baan-aarde.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("klim", klimatogram())
    print("baan", baan())
