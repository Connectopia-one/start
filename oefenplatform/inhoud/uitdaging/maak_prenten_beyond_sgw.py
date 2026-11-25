# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Sociale en
gedragswetenschappen 🌍 Beyond.

    python3 inhoud/uitdaging/maak_prenten_beyond_sgw.py

Prent 1: de kaart uit een lijnenproef zoals die van Asch (een standaardlijn
en drie vergelijkingslijnen A, B, C).
Prent 2: vier tekstballonnen uit een gesprek tussen een ouder en een tiener.
De klikvakken in uitdaging/bron/beyond_sgw.py staan in procent.
"""
import pathlib
from xml.sax.saxutils import escape

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "sgw-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

LB, LH = 1000, 520
STANDAARD = 240
LIJNEN = {"A": 190, "B": 300, "C": 240}       # C is even lang als de standaard
LX = {"A": 560, "B": 720, "C": 880}
VOET = 440


def lijnen():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {LB} {LH}' width='{LB}' height='{LH}'>",
         f"<rect width='{LB}' height='{LH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een lijnenproef</text>",
         f"<rect x='60' y='80' width='300' height='400' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>",
         f"<rect x='460' y='80' width='500' height='400' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>",
         f"<line x1='210' y1='{VOET}' x2='210' y2='{VOET - STANDAARD}' stroke='{TEKST}' stroke-width='10'/>",
         f"<text x='210' y='118' text-anchor='middle' {FONT} font-size='22' font-weight='700' fill='{TEKST}'>standaardlijn</text>"]
    for k, lengte in LIJNEN.items():
        x = LX[k] - 40
        d.append(f"<line x1='{x}' y1='{VOET}' x2='{x}' y2='{VOET - lengte}' stroke='{TEKST}' stroke-width='10'/>")
        d.append(f"<circle cx='{x}' cy='{VOET + 0}' r='0' fill='none'/>")
        d.append(f"<text x='{x + 36}' y='{VOET - 4}' text-anchor='middle' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>{k}</text>")
    d.append("</svg>")
    (UIT / "lijnenproef.svg").write_text("\n".join(d), encoding="utf-8")


def lijn_zone(k):
    x = LX[k] - 40
    return [round((x - 45) / LB * 100, 1), round(100 / LH * 100, 1), round(110 / LB * 100, 1), round(350 / LH * 100, 1)]


GB, GH = 1000, 600
BALLONNEN = [
    ("1", "Jij laat ook altijd je spullen rondslingeren, jij bent gewoon lui.", 40, 80),
    ("2", "Als je jas op de grond ligt, struikel ik erover en dat maakt me boos.", 520, 80),
    ("3", "Je bedoelt dus dat je na school eerst even rust nodig hebt?", 40, 330),
    ("4", "Je ruimt nu meteen je kamer op, anders mag je niet weg.", 520, 330),
]
BW, BH = 440, 200


def regels(tekst, max_tekens=30):
    woorden, uit, regel = tekst.split(), [], ""
    for w in woorden:
        if len(regel) + len(w) + 1 > max_tekens:
            uit.append(regel)
            regel = w
        else:
            regel = (regel + " " + w).strip()
    return uit + [regel]


def gesprek():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Vier zinnen van een ouder tegen een tiener</text>"]
    for n, tekst, x, y in BALLONNEN:
        d.append(f"<rect x='{x}' y='{y}' width='{BW}' height='{BH - 30}' rx='26' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<polygon points='{x + 60},{y + BH - 32} {x + 70},{y + BH} {x + 100},{y + BH - 32}' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<line x1='{x + 62}' y1='{y + BH - 31}' x2='{x + 98}' y2='{y + BH - 31}' stroke='{ZACHT}' stroke-width='4'/>")
        d.append(f"<circle cx='{x + 34}' cy='{y + 34}' r='20' fill='{GROEN}'/>")
        d.append(f"<text x='{x + 34}' y='{y + 41}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{n}</text>")
        for j, r in enumerate(regels(tekst)):
            d.append(f"<text x='{x + 70}' y='{y + 42 + j * 32}' {FONT} font-size='22' fill='{TEKST}'>{escape(r)}</text>")
    d.append("</svg>")
    (UIT / "vier-ballonnen.svg").write_text("\n".join(d), encoding="utf-8")


def ballon_zone(n):
    _, _, x, y = next(b for b in BALLONNEN if b[0] == n)
    return [round(x / GB * 100, 1), round(y / GH * 100, 1), round(BW / GB * 100, 1), round(BH / GH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    lijnen()
    gesprek()
    print({k: lijn_zone(k) for k in LIJNEN}, {n: ballon_zone(n) for n in "1234"})
