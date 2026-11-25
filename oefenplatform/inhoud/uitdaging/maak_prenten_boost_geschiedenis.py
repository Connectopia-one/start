# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Geschiedenis 🚀 Boost
doorstroom: een schema van het leenstelsel en een verzonnen pamflet uit 1789
met genummerde zinnen.

    python3 inhoud/uitdaging/maak_prenten_boost_geschiedenis.py

De klikvakken in uitdaging/bron/boost_geschiedenis.py rekenen met de maten
hieronder (procent van de prent).
"""
import pathlib
from xml.sax.saxutils import escape

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "geschiedenis-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

# piramide van het leenstelsel: vier lagen, nummers in plaats van namen
PB, PH = 1000, 600
LAGEN = [  # (nummer, tekst in de laag)
    ("1", "geeft grote lenen"),
    ("2", "krijgen een leen en geven zelf kleinere lenen"),
    ("3", "krijgen een klein leen en vechten te paard"),
    ("4", "bewerken het land en geven een deel van de oogst"),
]
PY0, LH, MID = 110, 105, 500


def laag_rand(i):
    """Linker- en rechterrand van laag i bovenaan en onderaan."""
    breed = lambda k: 160 + k * 200
    return breed(i), breed(i + 1)


def piramide():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {PB} {PH}' width='{PB}' height='{PH}'>",
         f"<rect width='{PB}' height='{PH}' fill='#ffffff'/>",
         f"<text x='40' y='52' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Het leenstelsel in de middeleeuwen</text>"]
    kleuren = ["#e9efe2", "#f6ecd9", "#e3ecf2", "#f3e3e3"]
    for i, (nr, tekst) in enumerate(LAGEN):
        bo, on = laag_rand(i)
        y0, y1 = PY0 + i * LH, PY0 + (i + 1) * LH
        d.append(f"<polygon points='{MID - bo / 2},{y0} {MID + bo / 2},{y0} {MID + on / 2},{y1} {MID - on / 2},{y1}' fill='{kleuren[i]}' stroke='{RAND}' stroke-width='2.5'/>")
        d.append(f"<circle cx='{MID}' cy='{y0 + 32}' r='20' fill='{GROEN}'/>")
        d.append(f"<text x='{MID}' y='{y0 + 40}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{nr}</text>")
        d.append(f"<text x='{MID}' y='{y0 + 80}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{escape(tekst)}</text>")
    d.append(f"<text x='{MID}' y='{PY0 + 4 * LH + 40}' text-anchor='middle' {FONT} font-size='18' fill='#6b6b6b'>Hoe lager in de piramide, hoe meer mensen.</text>")
    d.append("</svg>")
    (UIT / "piramide-leenstelsel.svg").write_text("\n".join(d), encoding="utf-8")


def laag_zone(i):
    _, on = laag_rand(i)
    return [round((MID - on / 2) / PB * 100, 1), round((PY0 + i * LH) / PH * 100, 1),
            round(on / PB * 100, 1), round(LH / PH * 100, 1)]


B, KOP, STROOK = 1000, 90, 92
ZINNEN = [
    "Parijs, augustus 1789. Aan alle burgers van Frankrijk!",
    "De derde stand betaalt de belastingen, adel en geestelijkheid bijna niets.",
    "Toch beslissen de twee kleinste standen over het lot van het hele volk.",
    "Alle mensen worden vrij en gelijk in rechten geboren.",
    "De koning mag niet langer alleen de wetten maken.",
    "Wie nog voor de adel opkomt, is een vijand van het vaderland.",
]


def pamflet():
    h = KOP + len(ZINNEN) * STROOK + 30
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {h}' width='{B}' height='{h}'>",
         f"<rect width='{B}' height='{h}' fill='#ffffff'/>",
         f"<text x='40' y='58' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>Een pamflet uit 1789 (verzonnen bron)</text>"]
    for i, r in enumerate(ZINNEN):
        y = KOP + i * STROOK
        d.append(f"<rect x='24' y='{y + 6}' width='{B - 48}' height='{STROOK - 12}' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<circle cx='68' cy='{y + STROOK / 2}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='68' y='{y + STROOK / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        d.append(f"<text x='108' y='{y + STROOK / 2 + 9}' {FONT} font-size='23' font-style='italic' fill='{TEKST}'>{escape(r)}</text>")
    d.append("</svg>")
    (UIT / "pamflet-1789.svg").write_text("\n".join(d), encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    piramide()
    pamflet()
    print({i + 1: laag_zone(i) for i in range(4)})
