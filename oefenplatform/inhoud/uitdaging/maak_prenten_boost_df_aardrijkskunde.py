# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Aardrijkskunde 🚀 Boost dubbele
finaliteit: een kaart van een verzonnen gemeente met zes genummerde gebieden
en zes verzonnen krantenkoppen.

    python3 inhoud/uitdaging/maak_prenten_boost_df_aardrijkskunde.py

Het script drukt de klikvakken af (procent van de prent) voor
uitdaging/bron/boost_df_aardrijkskunde.py.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _blad import blad, zone  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "aardrijkskunde-boost-df-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, ORANJE, BLAUW = "#2f4a22", "#2b2b2b", "#c0622b", "#3b6ea5"
B, H = 1000, 760

# nummer: (x, y, b, h, kleur, legende)
GEBIEDEN = {
    1: (400, 262, 210, 140, "#f3d9c4", "centrum met winkelstraat en stadhuis"),
    2: (90, 110, 250, 150, "#f6efcf", "nieuwe verkaveling op vroeger akkerland"),
    3: (360, 455, 300, 80, "#d6ead0", "laag weiland vlak langs de rivier"),
    4: (770, 300, 170, 140, "#e2e2e2", "open terrein naast de afrit van de snelweg"),
    5: (90, 400, 190, 110, "#dccbb8", "leegstaande fabriekssite aan de rivier"),
    6: (430, 100, 250, 120, "#b7d3a8", "bos op een heuvel"),
}


def pct(x, y, w, h):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


def kaart():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {B} {H}' width='{B}' height='{H}'>",
         f"<rect width='{B}' height='{H}' fill='#ffffff'/>",
         f"<text x='40' y='52' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Kaart van een verzonnen gemeente</text>",
         f"<rect x='40' y='80' width='920' height='490' fill='#fbfbf7' stroke='#b9b29c' stroke-width='2'/>",
         # rivier van links naar rechts onderaan
         f"<path d='M40 530 C 200 560, 300 500, 450 545 S 750 590, 960 540' fill='none' stroke='{BLAUW}' stroke-width='26' opacity='0.8'/>",
         f"<text x='870' y='522' {FONT} font-size='19' font-style='italic' fill='{BLAUW}'>rivier</text>",
         # snelweg rechts
         f"<line x1='735' y1='80' x2='735' y2='570' stroke='#7a7a7a' stroke-width='18'/>",
         f"<line x1='735' y1='80' x2='735' y2='570' stroke='#ffffff' stroke-width='2' stroke-dasharray='14 12'/>",
         f"<path d='M735 330 C 755 340, 760 360, 770 370' fill='none' stroke='#7a7a7a' stroke-width='9'/>",
         f"<text x='755' y='110' {FONT} font-size='19' font-style='italic' fill='#555'>snelweg</text>"]
    z = {}
    for n, (x, y, w, h, kl, _) in GEBIEDEN.items():
        d.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='18' fill='{kl}' stroke='{TEKST}' stroke-width='2'/>")
        d.append(f"<circle cx='{x + w / 2}' cy='{y + h / 2}' r='24' fill='{GROEN}'/>")
        d.append(f"<text x='{x + w / 2}' y='{y + h / 2 + 9}' text-anchor='middle' {FONT} font-size='25' font-weight='800' fill='#ffffff'>{n}</text>")
        z[n] = pct(x, y, w, h)
    # legende
    for i, (n, g) in enumerate(GEBIEDEN.items()):
        kol, rij = i % 2, i // 2
        x, y = 50 + kol * 470, 615 + rij * 46
        d.append(f"<circle cx='{x + 14}' cy='{y}' r='15' fill='{GROEN}'/>")
        d.append(f"<text x='{x + 14}' y='{y + 6}' text-anchor='middle' {FONT} font-size='17' font-weight='800' fill='#ffffff'>{n}</text>")
        d.append(f"<text x='{x + 40}' y='{y + 7}' {FONT} font-size='19' fill='{TEKST}'>{g[5]}</text>")
    d.append("</svg>")
    (UIT / "kaart-gemeente.svg").write_text("\n".join(d), encoding="utf-8")
    return z


KOPPEN = [
    "Laatste fabriek in de streek dicht: 800 banen weg, de mijnen sloten al eerder",
    "Buitenlands bedrijf huurt 99 jaar lang 50 000 hectare landbouwgrond in Afrika",
    "Nieuwe weg snijdt het laatste grote bos van de gemeente in twee stukken",
    "Jonge artsen trekken weg naar het buitenland: ziekenhuizen zoeken personeel",
    "Bergdorp telt nog maar 40 inwoners: school en bakker zijn al jaren weg",
    "Haven verwerkt record aan containers uit Azië: vrachtwagens staan in de file",
]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    print("kaart", kaart())
    blad(UIT / "zes-krantenkoppen.svg", "Zes krantenkoppen (verzonnen)", KOPPEN, grootte=21)
    print("koppen", {i: zone(i, 6) for i in range(1, 7)})
