# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Geschiedenis 🚀 Boost dubbele
finaliteit: een tijdlijn met de westerse periodes en een zelf geschreven
bron (een verzonnen brief over de pest, met genummerde zinnen).

    python3 inhoud/uitdaging/maak_prenten_boost_df_geschiedenis.py

De klikvakken in uitdaging/bron/boost_df_geschiedenis.py rekenen met de
maten hieronder (procent van de prent).
"""
import pathlib
from xml.sax.saxutils import escape

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "geschiedenis-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"
KLEUREN = ["#e9efe2", "#f6ecd9", "#e3ecf2", "#f3e3e3"]

# tijdlijn van 0 tot 1900
TB, TH = 1000, 420
TX0, TX1, TY, BH = 50, 950, 170, 110
PERIODES = [("Oudheid", 0, 476), ("Middeleeuwen", 476, 1492), ("Nieuwe Tijd", 1492, 1789), ("Nieuwste Tijd", 1789, 1900)]


def tx(jaar):
    return TX0 + (TX1 - TX0) * jaar / 1900


def tijdlijn():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {TB} {TH}' width='{TB}' height='{TH}'>",
         f"<rect width='{TB}' height='{TH}' fill='#ffffff'/>",
         f"<text x='40' y='52' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een tijdlijn van het jaar 0 tot 1900</text>"]
    for i, (naam, a, b) in enumerate(PERIODES):
        xa, xb = tx(a), tx(b)
        d.append(f"<rect x='{xa}' y='{TY}' width='{xb - xa}' height='{BH}' fill='{KLEUREN[i]}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<text x='{(xa + xb) / 2}' y='{TY - 16}' text-anchor='middle' {FONT} font-size='18' font-weight='700' fill='{TEKST}'>{'?' if i < 3 else ''}</text>")
    for jaar in range(0, 1901, 100):
        x = tx(jaar)
        lang = jaar % 500 == 0
        d.append(f"<line x1='{x}' y1='{TY + BH}' x2='{x}' y2='{TY + BH + (16 if lang else 8)}' stroke='{TEKST}' stroke-width='2'/>")
        if lang:
            d.append(f"<text x='{x}' y='{TY + BH + 40}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{jaar}</text>")
    d.append(f"<line x1='{TX0}' y1='{TY + BH}' x2='{TX1}' y2='{TY + BH}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{TX0}' y='{TY + BH + 90}' {FONT} font-size='18' fill='#6b6b6b'>Elke kleur is één periode. De namen van de periodes staan er met opzet niet bij.</text>")
    d.append("</svg>")
    (UIT / "tijdlijn-periodes.svg").write_text("\n".join(d).replace(">?<", "><"), encoding="utf-8")


def periode_zone(naam):
    _, a, b = next(p for p in PERIODES if p[0] == naam)
    return [round(tx(a) / TB * 100, 1), round(TY / TH * 100, 1),
            round((tx(b) - tx(a)) / TB * 100, 1), round(BH / TH * 100, 1)]


# bron: verzonnen brief, elke zin een strook
B, KOP, STROOK = 1000, 90, 92
ZINNEN = [
    "Brugge, 12 juli 1349. Aan mijn broer in Gent.",
    "Sinds Sint-Jan sterven er in onze straat elke week mensen aan de zwarte dood.",
    "Gisteren heb ik zelf de kar met doden langs de Markt zien rijden.",
    "Iedereen zegt dat de vreemde kooplui de ziekte hebben meegebracht.",
    "Alle vreemdelingen zijn dus gevaarlijk en moeten de stad uit.",
    "Bid voor ons, want God straft ons voor onze zonden.",
]


def bron():
    h = KOP + len(ZINNEN) * STROOK + 30
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {h}' width='{B}' height='{h}'>",
         f"<rect width='{B}' height='{h}' fill='#ffffff'/>",
         f"<text x='40' y='58' {FONT} font-size='30' font-weight='800' fill='{GROEN}'>Brief van een Brugse koopman (verzonnen bron)</text>"]
    for i, r in enumerate(ZINNEN):
        y = KOP + i * STROOK
        d.append(f"<rect x='24' y='{y + 6}' width='{B - 48}' height='{STROOK - 12}' rx='16' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
        d.append(f"<circle cx='68' cy='{y + STROOK / 2}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='68' y='{y + STROOK / 2 + 8}' text-anchor='middle' {FONT} font-size='22' font-weight='800' fill='#ffffff'>{i + 1}</text>")
        d.append(f"<text x='108' y='{y + STROOK / 2 + 9}' {FONT} font-size='23' font-style='italic' fill='{TEKST}'>{escape(r)}</text>")
    d.append("</svg>")
    (UIT / "brief-pest-1349.svg").write_text("\n".join(d), encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tijdlijn()
    bron()
    print({p[0]: periode_zone(p[0]) for p in PERIODES})
