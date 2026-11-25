# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Natuurwetenschappen 🚀 Boost
dubbele finaliteit.

    python3 inhoud/uitdaging/maak_prenten_boost_df_natuurwetenschappen.py

De klikvakken in uitdaging/bron/boost_df_natuurwetenschappen.py rekenen met de
maten hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "natuurwetenschappen-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

# opwarmcurve: t van 0 tot 24 min, temperatuur van -40 tot 140 graden
GB, GH = 1000, 620
X0, X1, Y0, Y1 = 110, 920, 520, 110


def px(t, T):
    return X0 + (X1 - X0) * t / 24, Y0 - (Y0 - Y1) * (T + 40) / 180


PUNTEN = [(0, -20), (2, 0), (6, 0), (10, 100), (20, 100), (22, 120)]
STUKKEN = [("A", 0, 2), ("B", 2, 6), ("C", 6, 10), ("D", 10, 20), ("E", 20, 22)]

# feedbackschema: vijf vakken op een rij
FB, FH = 1000, 430
VAKKEN = [
    ("1", ["Je loopt in", "de zon en", "je warmt op"]),
    ("2", ["Warmtezintuig-", "cellen in", "je huid"]),
    ("3", ["Zenuwen en", "de hersenen"]),
    ("4", ["Zweetklieren", "in je huid"]),
    ("5", ["Zweet verdampt", "en je koelt af"]),
]
VB, VH, VY, VX0, VTUSSEN = 160, 200, 120, 30, 34


def curve():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een blok ijs wordt gelijkmatig verwarmd</text>"]
    for T in range(-40, 141, 20):
        _, y = px(0, T)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{T}</text>")
    for t in range(0, 25, 2):
        x, _ = px(t, -40)
        d.append(f"<line x1='{x}' y1='{Y1}' x2='{x}' y2='{Y0}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{t}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 20}' y2='{Y0}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 20}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 64}' text-anchor='end' {FONT} font-size='22' fill='{TEKST}'>tijd (min)</text>")
    d.append(f"<text x='{X0 + 14}' y='{Y1 - 16}' {FONT} font-size='22' fill='{TEKST}'>temperatuur (°C)</text>")
    pts = " ".join(f"{px(t, T)[0]},{px(t, T)[1]}" for t, T in PUNTEN)
    d.append(f"<polyline points='{pts}' fill='none' stroke='{GROEN}' stroke-width='6' stroke-linejoin='round'/>")
    for naam, a, b in STUKKEN:
        Ta = dict(PUNTEN)[a]; Tb = dict(PUNTEN)[b]
        x, y = px((a + b) / 2, (Ta + Tb) / 2)
        dx = {"A": 30, "C": -34, "E": -34}.get(naam, 0)
        dy = 84 if naam == "A" else 0
        y = y + dy
        d.append(f"<circle cx='{x + dx}' cy='{y - 40}' r='21' fill='{GROEN}'/>")
        d.append(f"<text x='{x + dx}' y='{y - 32}' text-anchor='middle' {FONT} font-size='23' font-weight='800' fill='#ffffff'>{naam}</text>")
    d.append("</svg>")
    (UIT / "opwarmcurve-ijs.svg").write_text("\n".join(d), encoding="utf-8")


def stuk_zone(naam):
    _, a, b = next(s for s in STUKKEN if s[0] == naam)
    xa, _ = px(a, 0); xb, _ = px(b, 0)
    return [round(xa / GB * 100, 1), round((Y1 - 20) / GH * 100, 1),
            round((xb - xa) / GB * 100, 1), round((Y0 - Y1 + 20) / GH * 100, 1)]


def schema():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {FB} {FH}' width='{FB}' height='{FH}'>",
         f"<rect width='{FB}' height='{FH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Je lichaam regelt zijn temperatuur</text>"]
    for i, (nr, regels) in enumerate(VAKKEN):
        x = VX0 + i * (VB + VTUSSEN)
        d.append(f"<rect x='{x}' y='{VY}' width='{VB}' height='{VH}' rx='20' fill='{ZACHT}' stroke='{RAND}' stroke-width='2.5'/>")
        d.append(f"<circle cx='{x + VB / 2}' cy='{VY}' r='20' fill='{GROEN}'/>")
        d.append(f"<text x='{x + VB / 2}' y='{VY + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{nr}</text>")
        y0 = VY + VH / 2 - (len(regels) - 1) * 14 + 8
        for k, r in enumerate(regels):
            d.append(f"<text x='{x + VB / 2}' y='{y0 + k * 28}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{r}</text>")
        if i < len(VAKKEN) - 1:
            xa = x + VB + 4; xb = x + VB + VTUSSEN - 6; ym = VY + VH / 2
            d.append(f"<line x1='{xa}' y1='{ym}' x2='{xb - 8}' y2='{ym}' stroke='{GROEN}' stroke-width='4'/>")
            d.append(f"<polygon points='{xb},{ym} {xb - 12},{ym - 8} {xb - 12},{ym + 8}' fill='{GROEN}'/>")
    # terugkoppeling: van 5 terug naar 1
    xa = VX0 + 4 * (VB + VTUSSEN) + VB / 2; xb = VX0 + VB / 2; yb = VY + VH + 60
    d.append(f"<path d='M{xa},{VY + VH + 4} L{xa},{yb} L{xb},{yb} L{xb},{VY + VH + 18}' fill='none' stroke='{GROEN}' stroke-width='4' stroke-dasharray='10 8'/>")
    d.append(f"<polygon points='{xb},{VY + VH + 6} {xb - 8},{VY + VH + 20} {xb + 8},{VY + VH + 20}' fill='{GROEN}'/>")
    d.append(f"<text x='{FB / 2}' y='{yb + 34}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>de lichaamstemperatuur daalt weer</text>")
    d.append("</svg>")
    (UIT / "feedback-temperatuur.svg").write_text("\n".join(d), encoding="utf-8")


def vak_zone(nr):
    i = [v[0] for v in VAKKEN].index(nr)
    x = VX0 + i * (VB + VTUSSEN)
    return [round(x / FB * 100, 1), round((VY - 20) / FH * 100, 1),
            round(VB / FB * 100, 1), round((VH + 20) / FH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    curve()
    schema()
    print({s: stuk_zone(s) for s in "ABCDE"}, {n: vak_zone(n) for n in "12345"})
