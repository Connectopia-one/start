# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Natuurwetenschappen 🌍 Beyond
doorstroom: een stamboom met een autosomaal recessieve aandoening en het
elektromagnetisch spectrum (zonder pijlen die het antwoord verklappen).

    python3 inhoud/uitdaging/maak_prenten_beyond_natuurwetenschappen.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/beyond_natuurwetenschappen.py.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "natuurwetenschappen-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST = "#2f4a22", "#2b2b2b"


def pct(x, y, w, h, b, hh):
    return [round(x / b * 100, 1), round(y / hh * 100, 1), round(w / b * 100, 1), round(h / hh * 100, 1)]


B, H = 900, 560
R = 34


def persoon(d, x, y, man, ziek, label):
    vul = TEKST if ziek else "#ffffff"
    if man:
        d.append(f"<rect x='{x - R}' y='{y - R}' width='{2 * R}' height='{2 * R}' fill='{vul}' stroke='{TEKST}' stroke-width='4'/>")
    else:
        d.append(f"<circle cx='{x}' cy='{y}' r='{R}' fill='{vul}' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<text x='{x}' y='{y + R + 34}' text-anchor='middle' {FONT} font-size='22' font-weight='700' fill='{TEKST}'>{label}</text>")
    return pct(x - R - 10, y - R - 10, 2 * R + 20, 2 * R + 20, B, H)


def stamboom():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Stamboom van een familie</text>"]
    y1, y2 = 170, 380
    xs = [250, 450, 650]
    d.append(f"<line x1='{350 + R}' y1='{y1}' x2='{550 - R}' y2='{y1}' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<line x1='450' y1='{y1}' x2='450' y2='{y2 - 90}' stroke='{TEKST}' stroke-width='4'/>")
    d.append(f"<line x1='{xs[0]}' y1='{y2 - 90}' x2='{xs[2]}' y2='{y2 - 90}' stroke='{TEKST}' stroke-width='4'/>")
    for x in xs:
        d.append(f"<line x1='{x}' y1='{y2 - 90}' x2='{x}' y2='{y2 - R}' stroke='{TEKST}' stroke-width='4'/>")
    z = {"I1": persoon(d, 350, y1, True, False, "1"), "I2": persoon(d, 550, y1, False, False, "2"),
         "II3": persoon(d, xs[0], y2, True, True, "3"), "II4": persoon(d, xs[1], y2, False, False, "4"),
         "II5": persoon(d, xs[2], y2, True, False, "5")}
    # legende
    d.append(f"<rect x='710' y='110' width='26' height='26' fill='{TEKST}'/>")
    d.append(f"<text x='746' y='131' {FONT} font-size='19' fill='{TEKST}'>ziek</text>")
    d.append(f"<rect x='710' y='150' width='26' height='26' fill='#ffffff' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='746' y='171' {FONT} font-size='19' fill='{TEKST}'>gezond</text>")
    d.append(f"<text x='710' y='212' {FONT} font-size='19' fill='{TEKST}'>□ man   ○ vrouw</text>")
    d.append("</svg>")
    (UIT / "stamboom-recessief.svg").write_text("\n".join(d), encoding="utf-8")
    return z


SB, SH = 1000, 380
DELEN = ["radiogolven", "microgolven", "infrarood", "zichtbaar licht", "ultraviolet", "röntgenstraling", "gammastraling"]
KLEUR = ["#e3ecf5", "#dbe7f3", "#f6e1d3", "#fff3c4", "#e7dcf3", "#dfe9da", "#f3dada"]


def spectrum():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {SB} {SH}' width='{SB}' height='{SH}'>",
         f"<rect width='{SB}' height='{SH}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Het elektromagnetisch spectrum</text>"]
    x0, w, y, h = 30, 940 / 7, 120, 200
    z = {}
    for i, (naam, kl) in enumerate(zip(DELEN, KLEUR)):
        x = x0 + i * w
        d.append(f"<rect x='{x:.1f}' y='{y}' width='{w:.1f}' height='{h}' fill='{kl}' stroke='{TEKST}' stroke-width='2'/>")
        woorden = {"radiogolven": ["radio-", "golven"], "microgolven": ["micro-", "golven"],
                   "zichtbaar licht": ["zichtbaar", "licht"], "röntgenstraling": ["röntgen-", "straling"],
                   "gammastraling": ["gamma-", "straling"]}.get(naam, [naam])
        for j, wd in enumerate(woorden):
            d.append(f"<text x='{x + w / 2:.1f}' y='{y + h / 2 + 8 + (j - (len(woorden) - 1) / 2) * 28:.1f}' text-anchor='middle' {FONT} font-size='20' font-weight='700' fill='{TEKST}'>{wd}</text>")
        z[naam] = pct(x, y, w, h, SB, SH)
    d.append("</svg>")
    (UIT / "em-spectrum.svg").write_text("\n".join(d), encoding="utf-8")
    return z


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("stam", stamboom())
    print("spec", spectrum())
