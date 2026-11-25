# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Aardrijkskunde 🚀 Boost
doorstroom: een bevolkingspiramide van een (verzonnen) vergrijzend land en het
model van de demografische transitie.

    python3 inhoud/uitdaging/maak_prenten_boost_aardrijkskunde.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/boost_aardrijkskunde.py.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "aardrijkskunde-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"

GROEPEN = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
MANNEN = [5.0, 5.4, 6.0, 6.4, 6.6, 7.2, 6.0, 4.0, 2.0]
VROUWEN = [4.8, 5.2, 5.8, 6.3, 6.5, 7.1, 6.3, 4.6, 3.2]


def pct(x, y, w, h, b, hh):
    return [round(x / b * 100, 1), round(y / hh * 100, 1), round(w / b * 100, 1), round(h / hh * 100, 1)]


def piramide():
    B, H = 1000, 640
    MX, TOP, RIJ, SCHAAL = 500, 110, 50, 48  # 1 % = 48 px
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Bevolkingspiramide van land X (verzonnen)</text>",
         f"<text x='{MX - 200}' y='92' text-anchor='middle' {FONT} font-size='21' font-weight='700' fill='{BLAUW}'>mannen</text>",
         f"<text x='{MX + 200}' y='92' text-anchor='middle' {FONT} font-size='21' font-weight='700' fill='{ORANJE}'>vrouwen</text>"]
    z = {}
    for i, g in enumerate(GROEPEN):
        y = TOP + (len(GROEPEN) - 1 - i) * RIJ
        m, v = MANNEN[i] * SCHAAL, VROUWEN[i] * SCHAAL
        d.append(f"<rect x='{MX - 40 - m:.1f}' y='{y + 4}' width='{m:.1f}' height='{RIJ - 8}' fill='{BLAUW}' opacity='0.8'/>")
        d.append(f"<rect x='{MX + 40}' y='{y + 4}' width='{v:.1f}' height='{RIJ - 8}' fill='{ORANJE}' opacity='0.8'/>")
        d.append(f"<text x='{MX}' y='{y + RIJ / 2 + 7}' text-anchor='middle' {FONT} font-size='18' fill='{TEKST}'>{g}</text>")
        z[g] = pct(MX - 40 - max(m, v), y, 2 * max(m, v) + 80, RIJ, B, H)
    yb = TOP + len(GROEPEN) * RIJ + 10
    for p in range(0, 9, 2):
        for kant in (-1, 1):
            x = MX + kant * (40 + p * SCHAAL)
            d.append(f"<line x1='{x}' y1='{TOP}' x2='{x}' y2='{yb - 10}' stroke='#ebe6d8' stroke-width='1.5'/>")
            d.append(f"<text x='{x}' y='{yb + 22}' text-anchor='middle' {FONT} font-size='17' fill='{TEKST}'>{p}</text>")
    d.append(f"<text x='{MX}' y='{yb + 56}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>% van de bevolking</text>")
    d.append("</svg>")
    (UIT / "piramide-land-x.svg").write_text("\n".join(d), encoding="utf-8")
    return z


def transitie():
    B, H = 1000, 600
    X0, X1, Y0, Y1 = 90, 930, 480, 120
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Het model van de demografische transitie</text>"]
    w = (X1 - X0) / 4
    z = {}
    for i in range(4):
        x = X0 + i * w
        d.append(f"<rect x='{x:.1f}' y='{Y1 - 20}' width='{w:.1f}' height='{Y0 - Y1 + 20}' fill='{'#fbfaf6' if i % 2 else '#ffffff'}' stroke='#d8d2c0' stroke-width='1.5'/>")
        d.append(f"<text x='{x + w / 2:.1f}' y='{Y0 + 34}' text-anchor='middle' {FONT} font-size='21' font-weight='700' fill='{TEKST}'>fase {i + 1}</text>")
        z[i + 1] = pct(x, Y1 - 20, w, Y0 - Y1 + 60, B, H)

    def y(v):
        return Y0 - (Y0 - Y1) * v / 45

    def lijn(punten, kleur):
        pts = " ".join(f"{X0 + w * t:.1f},{y(v):.1f}" for t, v in punten)
        d.append(f"<polyline points='{pts}' fill='none' stroke='{kleur}' stroke-width='5' stroke-linejoin='round'/>")

    # geboortecijfer (blauw) en sterftecijfer (oranje) in promille
    lijn([(0, 40), (1, 40), (1.5, 39), (2, 34), (2.5, 24), (3, 14), (4, 11)], BLAUW)
    lijn([(0, 38), (0.5, 40), (1, 36), (1.5, 24), (2, 16), (2.5, 12), (3, 10), (4, 11)], ORANJE)
    d.append(f"<text x='{X1 - 10}' y='{y(15) - 10}' text-anchor='end' {FONT} font-size='20' font-weight='700' fill='{BLAUW}'>geboortecijfer</text>")
    d.append(f"<text x='{X1 - 10}' y='{y(6)}' text-anchor='end' {FONT} font-size='20' font-weight='700' fill='{ORANJE}'>sterftecijfer</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1}' y2='{Y0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X0 + 8}' y='{Y1 - 30}' {FONT} font-size='19' fill='{TEKST}'>per 1000 inwoners</text>")
    d.append("</svg>")
    (UIT / "demografische-transitie.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("pir", piramide())
    print("trans", transitie())
