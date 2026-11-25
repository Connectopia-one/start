# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Bedrijfswetenschappen en recht
🌍 Beyond doorstroom: een break-evengrafiek en een BCG-matrix met vier
producten. Alle cijfers en producten zijn verzonnen.

    python3 inhoud/uitdaging/maak_prenten_beyond_bwr.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_bwr.py.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "bwr-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

B, H = 1000, 640
X0, X1, Y0, Y1 = 130, 900, 540, 110  # Q 0..1000, euro 0..25000


def bp(q, e):
    return X0 + (X1 - X0) * q / 1000, Y0 - (Y0 - Y1) * e / 25000


def pct(x, y, w, h, b, hh):
    return [round(x / b * 100, 1), round(y / hh * 100, 1), round(w / b * 100, 1), round(h / hh * 100, 1)]


def breakeven():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Kosten en opbrengsten van een fietsenmaker</text>"]
    for e in range(0, 25001, 5000):
        _, y = bp(0, e)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 12}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{f"{e:,}".replace(",", ".")}</text>")
    for q in range(0, 1001, 200):
        x, _ = bp(q, 0)
        d.append(f"<line x1='{x}' y1='{Y1}' x2='{x}' y2='{Y0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{q}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 15}' y2='{Y0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 64}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>aantal herstellingen (q)</text>")
    d.append(f"<text x='{X0 + 12}' y='{Y1 - 24}' {FONT} font-size='21' fill='{TEKST}'>euro</text>")
    # vaste kosten 6000, totale kosten 6000 + 15 q, opbrengst 25 q
    a, b = bp(0, 6000), bp(1000, 6000)
    d.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' stroke='{TEKST}' stroke-width='3' stroke-dasharray='12 8'/>")
    d.append(f"<text x='{b[0] - 4}' y='{b[1] + 28}' text-anchor='end' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>VK</text>")
    a, b = bp(0, 6000), bp(1000, 21000)
    d.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' stroke='{ORANJE}' stroke-width='5'/>")
    d.append(f"<text x='{b[0] + 8}' y='{b[1] + 8}' {FONT} font-size='22' font-weight='800' fill='{ORANJE}'>TK</text>")
    a, b = bp(0, 0), bp(1000, 25000)
    d.append(f"<line x1='{a[0]}' y1='{a[1]}' x2='{b[0]}' y2='{b[1]}' stroke='{BLAUW}' stroke-width='5'/>")
    d.append(f"<text x='{b[0] + 8}' y='{b[1] + 8}' {FONT} font-size='22' font-weight='800' fill='{BLAUW}'>TO</text>")
    e = bp(600, 15000)
    d.append(f"<circle cx='{e[0]}' cy='{e[1]}' r='10' fill='{TEKST}'/>")
    z = {"bep": pct(e[0] - 34, e[1] - 34, 68, 68, B, H)}
    for letter, (q, eu) in {"1": (300, 9000), "2": (850, 20000)}.items():
        x, y = bp(q, eu)
        d.append(f"<circle cx='{x}' cy='{y}' r='20' fill='#ffffff' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='{TEKST}'>{letter}</text>")
        z[letter] = pct(x - 32, y - 32, 64, 64, B, H)
    d.append("</svg>")
    (UIT / "breakeven-fietsen.svg").write_text("\n".join(d), encoding="utf-8")
    return z


# BCG-matrix
MB, MH = 900, 680
L, R, T, O = 170, 820, 110, 600


def bcg():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {MB} {MH}' width='{MB}' height='{MH}'>",
         f"<rect width='{MB}' height='{MH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>BCG-matrix van een snoepfabrikant</text>"]
    mx, my = (L + R) / 2, (T + O) / 2
    d.append(f"<rect x='{L}' y='{T}' width='{R - L}' height='{O - T}' fill='#fbfaf6' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{mx}' y1='{T}' x2='{mx}' y2='{O}' stroke='{TEKST}' stroke-width='2'/>")
    d.append(f"<line x1='{L}' y1='{my}' x2='{R}' y2='{my}' stroke='{TEKST}' stroke-width='2'/>")
    d.append(f"<text x='{L}' y='{O + 34}' {FONT} font-size='19' fill='{TEKST}'>hoog</text>")
    d.append(f"<text x='{R}' y='{O + 34}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>laag</text>")
    d.append(f"<text x='{mx}' y='{O + 62}' text-anchor='middle' {FONT} font-size='21' fill='{TEKST}'>relatief marktaandeel</text>")
    d.append(f"<text x='{L - 14}' y='{T + 20}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>hoog</text>")
    d.append(f"<text x='{L - 14}' y='{O}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>laag</text>")
    d.append(f"<text x='60' y='{my}' text-anchor='middle' transform='rotate(-90 60 {my})' {FONT} font-size='21' fill='{TEKST}'>marktgroei</text>")
    prod = {"Zuurstokken": (mx + 170, my + 120), "Proteïnerepen": (mx - 160, my - 120),
            "Chocoladerepen": (mx - 160, my + 120), "Vegan gummies": (mx + 170, my - 120)}
    z = {}
    for naam, (x, y) in prod.items():
        d.append(f"<rect x='{x - 115}' y='{y - 28}' width='230' height='56' rx='16' fill='#ffffff' stroke='{GROEN}' stroke-width='3'/>")
        d.append(f"<text x='{x}' y='{y + 8}' text-anchor='middle' {FONT} font-size='21' font-weight='700' fill='{TEKST}'>{naam}</text>")
        z[naam] = pct(x - 120, y - 33, 240, 66, MB, MH)
    d.append("</svg>")
    (UIT / "bcg-snoep.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("be", breakeven())
    print("bcg", bcg())
