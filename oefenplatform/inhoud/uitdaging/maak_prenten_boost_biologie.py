# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Biologie 🚀 Boost doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_biologie.py

Prent 1: een energiepiramide met vier trofische niveaus (wit, zonder namen
van niveaus, enkel organismen).
Prent 2: de weg van prikkel tot reactie bij een reflex, in vijf genummerde
vakken. De klikvakken in uitdaging/bron/boost_biologie.py staan in procent.
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "biologie-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"


def piramide():
    B, H = 1000, 620
    niveaus = [("eikenbladeren", 860, "#d8e8c9"), ("rupsen", 640, "#f3e3b8"), ("mezen", 420, "#f5d0b5"), ("sperwer", 200, "#e7d9f0")]
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Energiepiramide van een eikenbos</text>"]
    zones = {}
    y = 540
    for naam, w, kleur in niveaus:
        x = (B - w) / 2
        d.append(f"<rect x='{x}' y='{y - 100}' width='{w}' height='100' rx='10' fill='{kleur}' stroke='{TEKST}' stroke-width='3'/>")
        d.append(f"<text x='{B / 2}' y='{y - 40}' text-anchor='middle' {FONT} font-size='30' font-weight='700' fill='{TEKST}'>{naam}</text>")
        zones[naam] = [round(x / B * 100, 1), round((y - 100) / H * 100, 1), round(w / B * 100, 1), round(100 / H * 100, 1)]
        y -= 110
    d.append(f"<text x='{B / 2}' y='595' text-anchor='middle' {FONT} font-size='22' fill='{TEKST}'>De breedte van elke laag staat voor de hoeveelheid energie op dat niveau.</text>")
    d.append("</svg>")
    (UIT / "energiepiramide.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


def reflex():
    B, H = 1000, 420
    vakken = ["receptor in de huid", "sensorische zenuw", "ruggemerg", "motorische zenuw", "spier in de arm"]
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='50' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Je raakt een hete pan aan: de weg van de reflex</text>",
         "<defs><marker id='p' markerUnits='userSpaceOnUse' markerWidth='14' markerHeight='14' refX='12' refY='7' orient='auto'><path d='M0,0 L14,7 L0,14 z' fill='#2b2b2b'/></marker></defs>"]
    zones = {}
    w, h, gap, y = 168, 190, 30, 130
    for i, naam in enumerate(vakken):
        x = 30 + i * (w + gap)
        kleur = "#eaf1f8" if i != 2 else "#f7f4ec"
        d.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='18' fill='{kleur}' stroke='{BLAUW}' stroke-width='3'/>")
        d.append(f"<circle cx='{x + w / 2}' cy='{y + 40}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='{x + w / 2}' y='{y + 48}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        woorden = naam.split(" ")
        regels = [" ".join(woorden[:2]), " ".join(woorden[2:])] if len(woorden) > 2 else woorden
        for k, r in enumerate(regels):
            d.append(f"<text x='{x + w / 2}' y='{y + 105 + k * 32}' text-anchor='middle' {FONT} font-size='24' fill='{TEKST}'>{r}</text>")
        if i < 4:
            d.append(f"<line x1='{x + w + 2}' y1='{y + h / 2}' x2='{x + w + gap - 2}' y2='{y + h / 2}' stroke='{TEKST}' stroke-width='3' marker-end='url(#p)'/>")
        zones[i + 1] = [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]
    d.append(f"<text x='{B / 2}' y='380' text-anchor='middle' {FONT} font-size='22' fill='{TEKST}'>De impuls gaat van vak 1 naar vak 5.</text>")
    d.append("</svg>")
    (UIT / "reflexboog.svg").write_text("\n".join(d), encoding="utf-8")
    return zones


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print(piramide())
    print(reflex())
