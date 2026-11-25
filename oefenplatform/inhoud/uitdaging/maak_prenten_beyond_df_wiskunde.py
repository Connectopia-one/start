# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Wiskunde 🌍 Beyond dubbele
finaliteit: de temperatuur op een zomerdag en twee groeimodellen.

    python3 inhoud/uitdaging/maak_prenten_beyond_df_wiskunde.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_df_wiskunde.py.
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "wiskunde-beyond-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"
B, H = 1000, 600
X0, X1, Y0, Y1 = 110, 920, 500, 110


def pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def T(t):
    return 12 - 6 * math.cos(math.pi * (t - 2) / 12)


def tp(t, temp):
    return X0 + (X1 - X0) * t / 24, Y0 - (Y0 - Y1) * temp / 20


def assen(d, xs, ys, xt, yt, f):
    for v in ys:
        _, y = f(0, v)
        d.append(f"<line x1='{X0}' y1='{y:.1f}' x2='{X1}' y2='{y:.1f}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 12}' y='{y + 7:.1f}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{v}</text>")
    for v in xs:
        x, _ = f(v, 0)
        d.append(f"<line x1='{x:.1f}' y1='{Y1}' x2='{x:.1f}' y2='{Y0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x:.1f}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{v}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 15}' y2='{Y0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 64}' text-anchor='end' {FONT} font-size='21' fill='{TEKST}'>{xt}</text>")
    d.append(f"<text x='{X0 + 12}' y='{Y1 - 24}' {FONT} font-size='21' fill='{TEKST}'>{yt}</text>")


def temperatuur():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Temperatuur op een zomerdag</text>"]
    assen(d, range(0, 25, 2), range(0, 21, 2), "tijd (uur)", "temperatuur (°C)", tp)
    pts = " ".join(f"{tp(t / 10, T(t / 10))[0]:.1f},{tp(t / 10, T(t / 10))[1]:.1f}" for t in range(0, 241))
    d.append(f"<polyline points='{pts}' fill='none' stroke='{ORANJE}' stroke-width='5'/>")
    z = {}
    for naam, t in {"min": 2, "max": 14, "p6": 6, "p22": 22}.items():
        x, y = tp(t, T(t))
        d.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='8' fill='{TEKST}'/>")
        z[naam] = pct(x - 30, y - 30, 60, 60)
    d.append("</svg>")
    (UIT / "temperatuur-dag.svg").write_text("\n".join(d), encoding="utf-8")
    return z


def gp(t, n):
    return X0 + (X1 - X0) * t / 8, Y0 - (Y0 - Y1) * n / 500


def groei():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Twee groeimodellen voor een aantal volgers</text>"]
    assen(d, range(0, 9), range(0, 501, 100), "tijd (maanden)", "aantal volgers", gp)
    a = " ".join(f"{gp(t / 10, 100 + 20 * t / 10)[0]:.1f},{gp(t / 10, 100 + 20 * t / 10)[1]:.1f}" for t in range(0, 81))
    b = " ".join(f"{gp(t / 10, 100 * 1.2 ** (t / 10))[0]:.1f},{gp(t / 10, 100 * 1.2 ** (t / 10))[1]:.1f}" for t in range(0, 81))
    d.append(f"<polyline points='{a}' fill='none' stroke='{BLAUW}' stroke-width='5'/>")
    d.append(f"<polyline points='{b}' fill='none' stroke='{ORANJE}' stroke-width='5'/>")
    xa, ya = gp(8, 260)
    xb, yb = gp(8, 100 * 1.2 ** 8)
    d.append(f"<text x='{xa + 14:.1f}' y='{ya + 8:.1f}' {FONT} font-size='26' font-weight='800' fill='{BLAUW}'>A</text>")
    d.append(f"<text x='{xb + 14:.1f}' y='{yb + 8:.1f}' {FONT} font-size='26' font-weight='800' fill='{ORANJE}'>B</text>")
    z = {"A": pct(xa - 140, ya - 40, 180, 70), "B": pct(xb - 110, yb - 30, 150, 90)}
    d.append("</svg>")
    (UIT / "groeimodellen.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("temp", temperatuur())
    print("groei", groei())
