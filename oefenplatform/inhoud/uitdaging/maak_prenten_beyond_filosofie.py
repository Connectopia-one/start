# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Filosofie en recht 🌍 Beyond.

    python3 inhoud/uitdaging/maak_prenten_beyond_filosofie.py

De klikvakken in uitdaging/bron/beyond_filosofie.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib
from xml.sax.saxutils import escape

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "filosofie-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

# De gerechtelijke piramide, van boven naar onder
PB, PH = 1000, 560
LAGEN = [
    ["Hof van Cassatie"],
    ["hof van beroep", "hof van assisen"],
    ["rechtbank van eerste aanleg", "arbeidsrechtbank", "ondernemingsrechtbank"],
    ["vredegerecht", "politierechtbank"],
]
TOP, LAAG, MARGE = 80, 110, 14

# Vier redeneringen
RB, RH = 1000, 560
KAARTEN = [
    ("A", ["Als het vriest, is het ijs op de vijver dik.", "Het vriest.", "Dus het ijs is dik."]),
    ("B", ["Als het vriest, is het ijs op de vijver dik.", "Het ijs is dik.", "Dus het vriest."]),
    ("C", ["Als het vriest, is het ijs op de vijver dik.", "Het vriest niet.", "Dus het ijs is niet dik."]),
    ("D", ["Als het vriest, is het ijs op de vijver dik.", "Het ijs is niet dik.", "Dus het vriest niet."]),
]
KX, KY, KW, KH = 30, 80, 460, 220


def blok_vakken():
    """(laag, plaats) -> [x, y, b, h] in pixels; de piramide wordt naar onder breder."""
    vakken = {}
    for l, laag in enumerate(LAGEN):
        breedte = 330 + l * 210
        x0 = (PB - breedte) / 2
        y = TOP + l * LAAG
        b = (breedte - MARGE * (len(laag) - 1)) / len(laag)
        for p, _ in enumerate(laag):
            vakken[(l, p)] = [x0 + p * (b + MARGE), y, b, LAAG - MARGE]
    return vakken


def piramide():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {PB} {PH}' width='{PB}' height='{PH}'>",
         f"<rect width='{PB}' height='{PH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>De gerechtelijke piramide in België (vereenvoudigd)</text>"]
    for (l, p), (x, y, b, h) in blok_vakken().items():
        d.append(f"<rect x='{x}' y='{y}' width='{b}' height='{h}' rx='14' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        naam = LAGEN[l][p]
        d.append(f"<text x='{x + b / 2}' y='{y + h / 2 + 8}' text-anchor='middle' {FONT} font-size='{22 if len(naam) < 20 else 17}' font-weight='700' fill='{TEKST}'>{escape(naam)}</text>")
    d.append("</svg>")
    (UIT / "gerechtelijke-piramide.svg").write_text("\n".join(d), encoding="utf-8")


def piramide_zone(naam):
    for (l, p), (x, y, b, h) in blok_vakken().items():
        if LAGEN[l][p] == naam:
            return [round(x / PB * 100, 1), round(y / PH * 100, 1), round(b / PB * 100, 1), round(h / PH * 100, 1)]
    raise KeyError(naam)


def kaart_vak(i):
    r, k = divmod(i, 2)
    return KX + k * (KW + 20), KY + r * (KH + 20)


def redeneringen():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {RB} {RH}' width='{RB}' height='{RH}'>",
         f"<rect width='{RB}' height='{RH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Vier redeneringen over de vijver</text>"]
    for i, (letter, regels) in enumerate(KAARTEN):
        x, y = kaart_vak(i)
        d.append(f"<rect x='{x}' y='{y}' width='{KW}' height='{KH}' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<circle cx='{x + 36}' cy='{y + 36}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='{x + 36}' y='{y + 44}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='#ffffff'>{letter}</text>")
        for j, regel in enumerate(regels):
            gewicht = " font-weight='800'" if j == 2 else ""
            d.append(f"<text x='{x + 24}' y='{y + 100 + j * 42}' {FONT} font-size='21'{gewicht} fill='{TEKST}'>{escape(regel)}</text>")
        d.append(f"<line x1='{x + 24}' y1='{y + 156}' x2='{x + KW - 24}' y2='{y + 156}' stroke='{RAND}' stroke-width='2'/>")
    d.append("</svg>")
    (UIT / "vier-redeneringen.svg").write_text("\n".join(d), encoding="utf-8")


def kaart_zone(letter):
    i = [k[0] for k in KAARTEN].index(letter)
    x, y = kaart_vak(i)
    return [round(x / RB * 100, 1), round(y / RH * 100, 1), round(KW / RB * 100, 1), round(KH / RH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    piramide()
    redeneringen()
    print({n: piramide_zone(n) for n in ("Hof van Cassatie", "hof van beroep", "vredegerecht", "arbeidsrechtbank")},
          {l: kaart_zone(l) for l in "ABCD"})
