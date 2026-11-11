# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging aardrijkskunde ✨ Spark.

    python3 inhoud/uitdaging/maak_prenten_spark_aardrijkskunde.py

Zelf getekend (geen bron nodig). De klikvakken in uitdaging/bron/
spark_aardrijkskunde.py staan in procent van deze prenten; wie hier iets
verschuift, moet die mee aanpassen.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "aardrijkskunde-spark"
GROEN, LIJN, TEKST = "#2f4a22", "#8a5a2b", "#2b2b2b"
FONT = "font-family='Nunito, Arial, sans-serif'"


def hoogtelijnen():
    # Vijf hoogtelijnen rond een heuvel. Aan de westkant liggen ze dicht
    # bijeen (steil), aan de oostkant ver uit elkaar (flauw).
    west = [120, 140, 160, 180, 200]
    oost = [720, 650, 580, 510, 440]
    ry = [200, 168, 136, 104, 72]
    hoogte = [10, 20, 30, 40, 50]
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 500' width='800' height='500'>",
         "<rect width='800' height='500' fill='#ffffff'/>",
         "<rect x='1' y='1' width='798' height='498' fill='none' stroke='#cfc6ad' stroke-width='2'/>"]
    for w, o, r, h in zip(west, oost, ry, hoogte):
        cx, rx = (w + o) / 2, (o - w) / 2
        d.append(f"<ellipse cx='{cx}' cy='250' rx='{rx}' ry='{r}' fill='none' stroke='{LIJN}' stroke-width='2.5'/>")
        d.append(f"<text x='{cx + rx * 0.62:.0f}' y='{250 - r * 0.80:.0f}' {FONT} font-size='17' fill='{LIJN}'>{h} m</text>")
    d.append(f"<circle cx='{(200 + 440) / 2}' cy='250' r='5' fill='{TEKST}'/>")
    d.append(f"<text x='{(200 + 440) / 2 + 10}' y='256' {FONT} font-size='18' fill='{TEKST}'>top 54 m</text>")
    # noordpijl
    d.append(f"<path d='M745 95 L760 55 L775 95 L760 85 Z' fill='{GROEN}'/>")
    d.append(f"<text x='752' y='120' {FONT} font-size='20' font-weight='700' fill='{GROEN}'>N</text>")
    d.append(f"<text x='20' y='485' {FONT} font-size='16' fill='{TEKST}'>Hoogtelijnen om de 10 meter</text>")
    d.append("</svg>")
    (UIT / "hoogtelijnen-heuvel.svg").write_text("\n".join(d), encoding="utf-8")


TEMP = [3, 4, 7, 10, 14, 17, 19, 19, 15, 11, 7, 4]
NEERSLAG = [65, 55, 58, 48, 60, 72, 78, 96, 68, 74, 80, 78]
MAANDEN = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
X0, X1, Y0, Y1 = 80, 760, 60, 440  # tekenvlak
KOL = (X1 - X0) / 12


def klimatogram():
    def y_mm(mm):
        return Y1 - mm / 120 * (Y1 - Y0)

    def y_c(c):
        return Y1 - c / 40 * (Y1 - Y0)

    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 500' width='800' height='500'>",
         "<rect width='800' height='500' fill='#ffffff'/>"]
    for mm in range(0, 121, 20):
        y = y_mm(mm)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#e6e0cf' stroke-width='1'/>")
        d.append(f"<text x='{X1 + 8}' y='{y + 5}' {FONT} font-size='14' fill='#2f6fb0'>{mm}</text>")
    for c in range(0, 41, 10):
        d.append(f"<text x='{X0 - 34}' y='{y_c(c) + 5}' {FONT} font-size='14' fill='#c0392b'>{c}</text>")
    for i, mm in enumerate(NEERSLAG):
        x = X0 + i * KOL + (KOL - 34) / 2
        d.append(f"<rect x='{x:.1f}' y='{y_mm(mm):.1f}' width='34' height='{Y1 - y_mm(mm):.1f}' fill='#7fb3e0'/>")
        d.append(f"<text x='{X0 + i * KOL + KOL / 2:.1f}' y='{Y1 + 22}' text-anchor='middle' {FONT} font-size='15' fill='{TEKST}'>{MAANDEN[i]}</text>")
    pts = " ".join(f"{X0 + i * KOL + KOL / 2:.1f},{y_c(t):.1f}" for i, t in enumerate(TEMP))
    d.append(f"<polyline points='{pts}' fill='none' stroke='#c0392b' stroke-width='3'/>")
    d.append(f"<line x1='{X0}' y1='{Y1}' x2='{X1}' y2='{Y1}' stroke='{TEKST}' stroke-width='1.5'/>")
    d.append(f"<text x='{X0 - 60}' y='40' {FONT} font-size='15' fill='#c0392b'>temperatuur (°C)</text>")
    d.append(f"<text x='{X1 - 100}' y='40' {FONT} font-size='15' fill='#2f6fb0'>neerslag (mm)</text>")
    d.append("</svg>")
    (UIT / "klimatogram-west-europa.svg").write_text("\n".join(d), encoding="utf-8")


def zone_maand(i):
    """Het klikvak van maand i (0 = januari), in procent van de prent."""
    return [round((X0 + i * KOL) / 800 * 100, 1), round(Y0 / 500 * 100, 1),
            round(KOL / 800 * 100, 1), round((Y1 - Y0) / 500 * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    hoogtelijnen()
    klimatogram()
    print("droogste maand", MAANDEN[NEERSLAG.index(min(NEERSLAG))], zone_maand(NEERSLAG.index(min(NEERSLAG))))
