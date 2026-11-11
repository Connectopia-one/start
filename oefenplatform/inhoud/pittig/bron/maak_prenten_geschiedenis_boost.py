"""Tekent de prenten die Claude zelf maakt voor de pittige vragen geschiedenis 🚀 Boost doorstroom.

    python3 inhoud/pittig/bron/maak_prenten_geschiedenis_boost.py

Schrijft naar public/examenvormen/geschiedenis-boost/. Enkel eenvoudige
tekeningen zonder auteursrecht: tijdlijnen en schema's met gegevens uit de
leerbundel. Kunstwerken en bronnen zoekt Kim zelf; die staan op de prentenlijst.

De klikvakken (zones) in de vragen zijn in procent van de breedte en hoogte.
Wie hier iets verschuift, rekent de zones na met zone_jaar().
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "geschiedenis-boost"
GROEN, DONKER, ACHTER = "#2f4a22", "#24331b", "#ffffff"

# ---------------------------------------------------------------- tijdlijn 0-2000
B, H = 1000, 210
X0, X1 = 50, 923
J0, J1 = 0, 2000


def x_jaar(jaar):
    return X0 + (jaar - J0) / (J1 - J0) * (X1 - X0)


def zone_jaar(jaar, breed=60):
    """Een klikvak rond een jaar, in procent: breed is de breedte in jaren."""
    links = x_jaar(jaar - breed / 2) / B * 100
    return [round(links, 1), 25, round(breed / (J1 - J0) * (X1 - X0) / B * 100, 1), 55]


def tijdlijn():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(J0, J1 + 1, 50):
        x = x_jaar(j)
        if j % 500 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 100 == 0:
            d.append(f'<line x1="{x:.1f}" y1="98" x2="{x:.1f}" y2="122" stroke="{GROEN}" stroke-width="2.5"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="104" x2="{x:.1f}" y2="116" stroke="{GROEN}" stroke-width="1.2"/>')
    d.append(f'<text x="{X0}" y="50" font-size="22" fill="{DONKER}">Een groot streepje om de 100 jaar, een klein om de 50 jaar</text>')
    d.append("</svg>")
    (UIT / "tijdlijn-0-2000.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- schaalniveaus
# Vijf gebieden in elkaar, van de wereld tot Kortrijk. Geen kaart, enkel een
# schema: de vorm zegt niets over de echte grenzen.
SB, SH = 1000, 620
SCHAAL = [  # naam, x, y, breedte, hoogte, kleur
    ("de wereld", 10, 10, 980, 600, "#eef3e6"),
    ("Europa", 70, 75, 860, 480, "#dde8cf"),
    ("het koninkrijk Frankrijk", 140, 145, 720, 345, "#c9dbb4"),
    ("het graafschap Vlaanderen", 220, 215, 560, 210, "#b3cc98"),
    ("Kortrijk", 370, 290, 260, 80, "#ffffff"),
]


def schaalniveaus():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SB} {SH}" width="{SB}" height="{SH}" font-family="Arial, sans-serif">',
         f'<rect width="{SB}" height="{SH}" fill="{ACHTER}"/>']
    for naam, x, y, b, h, kleur in SCHAAL:
        d.append(f'<rect x="{x}" y="{y}" width="{b}" height="{h}" rx="22" fill="{kleur}" stroke="{GROEN}" stroke-width="3"/>')
        if naam == "Kortrijk":
            d.append(f'<text x="{x + b / 2}" y="{y + 52}" font-size="30" text-anchor="middle" fill="{DONKER}">{naam}</text>')
        else:
            d.append(f'<text x="{x + 22}" y="{y + 42}" font-size="28" fill="{DONKER}">{naam}</text>')
    d.append("</svg>")
    (UIT / "schaalniveaus.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


def zones_ring(naam):
    """Klikvakken in procent voor de rand van een gebied, zonder het gebied erbinnen."""
    i = [n for n, *_ in SCHAAL].index(naam)
    _, x, y, b, h, _ = SCHAAL[i]
    _, xi, yi, bi, hi, _ = SCHAAL[i + 1]
    def pc(a, c, e, f):
        return [round(a / SB * 100, 1), round(c / SH * 100, 1), round(e / SB * 100, 1), round(f / SH * 100, 1)]
    return [pc(x, y, b, yi - y), pc(x, yi + hi, b, y + h - yi - hi), pc(x, yi, xi - x, hi), pc(xi + bi, yi, x + b - xi - bi, hi)]


# ---------------------------------------------------------------- tijdlijn 400-1000
def x_jaar2(jaar, j0=400, j1=1000):
    return X0 + (jaar - j0) / (j1 - j0) * (X1 - X0)


def zone_jaar2(jaar, breed=20):
    links = x_jaar2(jaar - breed / 2) / B * 100
    return [round(links, 1), 25, round(breed / 600 * (X1 - X0) / B * 100, 1), 55]


def tijdlijn_400_1000():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(400, 1001, 10):
        x = x_jaar2(j)
        if j % 100 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="98" x2="{x:.1f}" y2="122" stroke="{GROEN}" stroke-width="2.5"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="104" x2="{x:.1f}" y2="116" stroke="{GROEN}" stroke-width="1.2"/>')
    d.append(f'<text x="{X0}" y="50" font-size="22" fill="{DONKER}">Een groot streepje om de 100 jaar, een middelgroot om de 50, een klein om de 10 jaar</text>')
    d.append("</svg>")
    (UIT / "tijdlijn-400-1000.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- invallen 9de-10de eeuw
def invallen():
    """Schema, geen kaart: het rijk in het midden, drie pijlen met een letter."""
    W, Hh = 900, 620
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         '<defs><marker id="p" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="22" refY="17" orient="auto"><polygon points="0,0 34,17 0,34" fill="#24331b"/></marker></defs>',
         f'<rect x="270" y="220" width="360" height="180" rx="26" fill="#c9dbb4" stroke="{GROEN}" stroke-width="4"/>',
         f'<text x="450" y="300" font-size="30" text-anchor="middle" fill="{DONKER}">het rijk van</text>',
         f'<text x="450" y="340" font-size="30" text-anchor="middle" fill="{DONKER}">de Karolingers</text>']
    pijlen = [("A", 450, 40, 450, 205, "noorden"), ("B", 450, 580, 450, 415, "zuiden"), ("C", 870, 310, 645, 310, "oosten")]
    for letter, x1, y1, x2, y2, _ in pijlen:
        d.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DONKER}" stroke-width="8" marker-end="url(#p)"/>')
    d += [f'<circle cx="500" cy="95" r="30" fill="{GROEN}"/><text x="500" y="106" font-size="32" text-anchor="middle" fill="#fff">A</text>',
          f'<circle cx="500" cy="535" r="30" fill="{GROEN}"/><text x="500" y="546" font-size="32" text-anchor="middle" fill="#fff">B</text>',
          f'<circle cx="770" cy="260" r="30" fill="{GROEN}"/><text x="770" y="271" font-size="32" text-anchor="middle" fill="#fff">C</text>',
          f'<text x="40" y="50" font-size="24" fill="{DONKER}">N</text><line x1="48" y1="62" x2="48" y2="120" stroke="{DONKER}" stroke-width="3"/>',
          f'<text x="880" y="600" font-size="20" text-anchor="end" fill="#555">Schema, geen kaart: de pijlen tonen enkel de richting.</text>']
    d.append("</svg>")
    (UIT / "invallen.svg").write_text("\n".join(d) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- tijdlijn 1000-1500
def x_jaar3(jaar):
    return X0 + (jaar - 1000) / 500 * (X1 - X0)


def zone_jaar3(van, tot):
    """Klikvak in procent van jaar van tot jaar tot."""
    return [round(x_jaar3(van) / B * 100, 1), 25, round((x_jaar3(tot) - x_jaar3(van)) / B * 100, 1), 55]


def tijdlijn_1000_1500():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(1000, 1501, 10):
        x = x_jaar3(j)
        if j % 100 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="98" x2="{x:.1f}" y2="122" stroke="{GROEN}" stroke-width="2.5"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="104" x2="{x:.1f}" y2="116" stroke="{GROEN}" stroke-width="1.2"/>')
    d.append(f'<text x="{X0}" y="50" font-size="22" fill="{DONKER}">Een groot streepje om de 100 jaar, een middelgroot om de 50, een klein om de 10 jaar</text>')
    d.append("</svg>")
    (UIT / "tijdlijn-1000-1500.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


def letter(x, y, l):
    return (f'<circle cx="{x}" cy="{y}" r="28" fill="{GROEN}" stroke="#fff" stroke-width="4"/>'
            f'<text x="{x}" y="{y + 11}" font-size="30" font-weight="bold" text-anchor="middle" fill="#fff">{l}</text>')


# ---------------------------------------------------------------- domein
# Schema, geen kaart. A = vroonland, B = hoevenland, C = bos, D = molen en oven.
# Klikvak vroonland: 30-62 % breed, 32-94 % hoog.
DOMEIN_W, DOMEIN_H = 1000, 620


def domein():
    W, Hh = DOMEIN_W, DOMEIN_H
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         # bos bovenaan
         f'<rect x="20" y="20" width="960" height="150" rx="20" fill="#d6e4c6" stroke="{GROEN}" stroke-width="3"/>']
    for i in range(16):
        x = 60 + i * 58
        y = 80 + (i % 2) * 40
        d.append(f'<rect x="{x - 4}" y="{y + 18}" width="8" height="22" fill="#6b4f2a"/><circle cx="{x}" cy="{y}" r="24" fill="#5f8a45"/>')
    # molen en oven links
    d += [f'<rect x="20" y="200" width="260" height="400" rx="20" fill="#f4efe2" stroke="{GROEN}" stroke-width="3"/>',
          '<rect x="70" y="330" width="90" height="90" fill="#c9b48a" stroke="#6b4f2a" stroke-width="3"/>',
          '<polygon points="60,330 115,280 170,330" fill="#9c6b3f"/>',
          '<g stroke="#6b4f2a" stroke-width="10" stroke-linecap="round"><line x1="115" y1="300" x2="115" y2="230"/><line x1="115" y1="300" x2="185" y2="300"/><line x1="115" y1="300" x2="115" y2="370"/><line x1="115" y1="300" x2="45" y2="300"/></g>',
          '<rect x="150" y="470" width="100" height="70" rx="30" fill="#b9805a" stroke="#6b4f2a" stroke-width="3"/>',
          '<rect x="185" y="505" width="30" height="35" rx="12" fill="#3a2a1a"/>',
          '<path d="M200 470 q-10 -25 5 -45" stroke="#999" stroke-width="5" fill="none"/>']
    # vroonland midden: groot veld met voren
    d.append(f'<rect x="300" y="200" width="320" height="400" rx="20" fill="#efe0a6" stroke="{GROEN}" stroke-width="3"/>')
    for y in range(225, 590, 24):
        d.append(f'<line x1="320" y1="{y}" x2="600" y2="{y}" stroke="#c9b06a" stroke-width="3"/>')
    # hoevenland rechts: vier smalle stroken, elk met een huisje
    d.append(f'<rect x="640" y="200" width="340" height="400" rx="20" fill="#e6ecd8" stroke="{GROEN}" stroke-width="3"/>')
    for i in range(4):
        x = 650 + i * 82
        d.append(f'<rect x="{x}" y="290" width="72" height="300" fill="#efe0a6" stroke="#c9b06a" stroke-width="2"/>')
        d.append(f'<rect x="{x + 16}" y="235" width="40" height="34" fill="#c9b48a" stroke="#6b4f2a" stroke-width="2"/><polygon points="{x + 10},235 {x + 36},212 {x + 62},235" fill="#9c6b3f"/>')
    d += [letter(460, 400, "A"), letter(810, 440, "B"), letter(500, 95, "C"), letter(230, 250, "D"),
          f'<text x="980" y="614" font-size="18" text-anchor="end" fill="#555">Schema van een domein, geen kaart.</text>',
          "</svg>"]
    (UIT / "domein.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stad
# Schema van een middeleeuwse stad. A = belfort, B = lakenhalle, C = kathedraal.
# De rivier loopt onderaan: klikvak 0-100 % breed, 84-100 % hoog.
STAD_W, STAD_H = 1000, 640


def stad():
    W, Hh = STAD_W, STAD_H
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         # rivier
         '<path d="M0 560 C 200 520, 350 600, 520 560 S 820 520, 1000 570 L1000 640 L0 640 Z" fill="#a9cbe6"/>',
         '<path d="M40 600 q40 -12 80 0 M420 615 q40 -12 80 0 M800 600 q40 -12 80 0" stroke="#fff" stroke-width="4" fill="none"/>',
         # boot
         '<path d="M610 585 l90 0 l-15 22 l-60 0 z" fill="#6b4f2a"/><line x1="655" y1="585" x2="655" y2="545" stroke="#6b4f2a" stroke-width="4"/><polygon points="657,548 690,580 657,580" fill="#fff" stroke="#6b4f2a" stroke-width="2"/>',
         # stadsmuur
         f'<rect x="70" y="40" width="860" height="470" rx="60" fill="#f4efe2" stroke="#8a7a5a" stroke-width="16"/>',
         # markt
         '<rect x="250" y="250" width="420" height="200" fill="#e4dcc6" stroke="#b5a888" stroke-width="2"/>',
         # lakenhalle: lang laag gebouw
         '<rect x="280" y="320" width="300" height="100" fill="#d9c49a" stroke="#6b4f2a" stroke-width="3"/>',
         '<polygon points="270,320 430,280 590,320" fill="#9c6b3f"/>']
    for i in range(7):
        d.append(f'<rect x="{295 + i * 40}" y="355" width="18" height="40" rx="9" fill="#6b4f2a"/>')
    # belfort: hoge smalle toren midden op de lakenhalle, zonder kruis
    d += ['<rect x="405" y="130" width="50" height="190" fill="#d9c49a" stroke="#6b4f2a" stroke-width="3"/>',
          '<polygon points="398,130 430,80 462,130" fill="#4d6b8a"/>',
          '<circle cx="430" cy="170" r="14" fill="#fff" stroke="#6b4f2a" stroke-width="3"/>',
          # kathedraal rechtsboven met kruis
          '<rect x="700" y="160" width="160" height="110" fill="#e8e1cf" stroke="#6b4f2a" stroke-width="3"/>',
          '<polygon points="690,160 780,120 870,160" fill="#9c6b3f"/>',
          '<rect x="740" y="80" width="40" height="80" fill="#e8e1cf" stroke="#6b4f2a" stroke-width="3"/>',
          '<polygon points="735,80 760,40 785,80" fill="#9c6b3f"/>',
          '<line x1="760" y1="40" x2="760" y2="14" stroke="#6b4f2a" stroke-width="4"/><line x1="750" y1="24" x2="770" y2="24" stroke="#6b4f2a" stroke-width="4"/>',
          '<circle cx="780" cy="205" r="18" fill="#a9cbe6" stroke="#6b4f2a" stroke-width="3"/>']
    # huizen
    for x, y in [(110, 110), (170, 110), (110, 400), (170, 400), (720, 380), (780, 380), (840, 380), (230, 110), (560, 110)]:
        d.append(f'<rect x="{x}" y="{y + 20}" width="46" height="40" fill="#c9b48a" stroke="#6b4f2a" stroke-width="2"/><polygon points="{x - 4},{y + 20} {x + 23},{y} {x + 50},{y + 20}" fill="#b06f4a"/>')
    # stadspoort onderaan in de muur
    d += ['<rect x="470" y="490" width="60" height="36" fill="#8a7a5a"/><rect x="487" y="500" width="26" height="26" rx="12" fill="#3a2a1a"/>',
          letter(500, 100, "A") if False else letter(480, 215, "A"), letter(330, 470, "B"), letter(890, 230, "C"),
          f'<text x="80" y="30" font-size="18" fill="#555">Schema van een middeleeuwse stad, geen kaart.</text>',
          "</svg>"]
    (UIT / "stad.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- bogen
# Twee bogen zonder namen: A = spitsboog (links), B = rondboog (rechts).
# Klikvak spitsboog: 0-50 % breed, 0-100 % hoog.
def bogen():
    W, Hh = 1000, 520
    steen = "#d9c49a"
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         # A: spitsboog, opening 200 breed, punt bovenaan
         f'<path d="M110 480 L110 230 Q110 110 250 50 Q390 110 390 230 L390 480 L330 480 L330 240 Q330 160 250 115 Q170 160 170 240 L170 480 Z" fill="{steen}" stroke="#6b4f2a" stroke-width="4"/>',
         # B: rondboog
         f'<path d="M610 480 L610 250 A140 140 0 0 1 890 250 L890 480 L830 480 L830 250 A80 80 0 0 0 670 250 L670 480 Z" fill="{steen}" stroke="#6b4f2a" stroke-width="4"/>',
         f'<line x1="40" y1="482" x2="960" y2="482" stroke="#6b4f2a" stroke-width="4"/>',
         letter(250, 300, "A"), letter(750, 330, "B"),
         "</svg>"]
    (UIT / "bogen.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- middeleeuwse wereldkaart
# Schema van een T-in-O-kaart, zonder namen. A = midden, B = bovenste helft,
# C = linksonder, D = rechtsonder.
def to_kaart():
    W, Hh = 760, 720
    cx, cy, r = 380, 380, 300
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r + 30}" fill="#a9cbe6"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f1e6c4" stroke="#6b4f2a" stroke-width="4"/>',
         f'<rect x="{cx - r}" y="{cy - 12}" width="{2 * r}" height="24" fill="#a9cbe6"/>',
         f'<rect x="{cx - 12}" y="{cy}" width="24" height="{r}" fill="#a9cbe6"/>',
         letter(cx, cy - 50, "A"), letter(cx, cy - 170, "B"), letter(cx - 150, cy + 150, "C"), letter(cx + 150, cy + 150, "D"),
         f'<text x="{W / 2}" y="30" font-size="20" text-anchor="middle" fill="#555">Schema van een middeleeuwse wereldkaart</text>',
         "</svg>"]
    (UIT / "wereldkaart-middeleeuwen.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- tijdlijn 1400-1800
def x_jaar4(jaar):
    return X0 + (jaar - 1400) / 400 * (X1 - X0)


def zone_jaar4(van, tot):
    return [round(x_jaar4(van) / B * 100, 1), 25, round((x_jaar4(tot) - x_jaar4(van)) / B * 100, 1), 55]


def tijdlijn_1400_1800():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(1400, 1801, 10):
        x = x_jaar4(j)
        if j % 100 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="98" x2="{x:.1f}" y2="122" stroke="{GROEN}" stroke-width="2.5"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="104" x2="{x:.1f}" y2="116" stroke="{GROEN}" stroke-width="1.2"/>')
    d.append(f'<text x="{X0}" y="50" font-size="22" fill="{DONKER}">Een groot streepje om de 100 jaar, een middelgroot om de 50, een klein om de 10 jaar</text>')
    d.append("</svg>")
    (UIT / "tijdlijn-1400-1800.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- driehoekshandel
# Schema, geen kaart: drie vakken met naam, drie genummerde pijlen.
# Pijl 2 (Afrika naar Amerika) loopt onderaan: klikvak 22-78 % breed, 74-100 % hoog.
def driehoekshandel():
    W, Hh = 1000, 620
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="#e3eef7"/>',
         '<defs><marker id="q" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="22" refY="17" orient="auto"><polygon points="0,0 34,17 0,34" fill="#24331b"/></marker></defs>']
    vak = [("Amerika", 40, 200), ("Europa", 680, 40), ("West-Afrika", 680, 380)]
    for naam, x, y in vak:
        d.append(f'<rect x="{x}" y="{y}" width="280" height="150" rx="24" fill="#f1e6c4" stroke="{GROEN}" stroke-width="4"/>')
        d.append(f'<text x="{x + 140}" y="{y + 86}" font-size="34" text-anchor="middle" fill="{DONKER}">{naam}</text>')
    pijlen = [("1", "M820 200 L820 370", 860, 290),       # Europa -> Afrika
              ("2", "M670 470 C 450 560, 250 520, 180 360", 420, 560),  # Afrika -> Amerika
              ("3", "M200 190 C 260 60, 480 60, 670 110", 420, 60)]     # Amerika -> Europa
    for nr, pad, lx, ly in pijlen:
        d.append(f'<path d="{pad}" stroke="{DONKER}" stroke-width="8" fill="none" marker-end="url(#q)"/>')
        d.append(letter(lx, ly, nr))
    d += [f'<text x="20" y="605" font-size="18" fill="#555">Schema, geen kaart: de pijlen tonen enkel de richting.</text>', "</svg>"]
    (UIT / "driehoekshandel.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- perspectief
# Een plein met tegels en twee rijen bomen die naar één verdwijnpunt lopen.
# Verdwijnpunt op (640, 250) in een tekening van 1000 x 600: klikvak 60-68 % breed, 35-48 % hoog.
def perspectief():
    W, Hh, vx, vy = 1000, 600, 640, 250
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{vy}" fill="#e3eef7"/>',
         f'<rect y="{vy}" width="{W}" height="{Hh - vy}" fill="#efe6cf"/>',
         f'<line x1="0" y1="{vy}" x2="{W}" y2="{vy}" stroke="#8a7a5a" stroke-width="2"/>']
    for x in range(-1400, 2600, 160):
        d.append(f'<line x1="{x}" y1="{Hh}" x2="{vx}" y2="{vy}" stroke="#c9b48a" stroke-width="2"/>')
    # dwarslijnen van de tegels: steeds dichter bij elkaar
    t = 1.0
    while t > 0.04:
        y = vy + (Hh - vy) * t
        d.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="#c9b48a" stroke-width="2"/>')
        t *= 0.72
    # twee rijen bomen
    for kant in (-1, 1):
        for i in range(6):
            t = 0.95 * (0.7 ** i)
            bx = vx + kant * 560 * t
            by = vy + (Hh - vy) * t
            h = 260 * t
            d.append(f'<rect x="{bx - 5 * t:.1f}" y="{by - h * 0.45:.1f}" width="{10 * t + 1:.1f}" height="{h * 0.45:.1f}" fill="#6b4f2a"/>')
            d.append(f'<circle cx="{bx:.1f}" cy="{by - h * 0.6:.1f}" r="{h * 0.25:.1f}" fill="#5f8a45"/>')
    d.append("</svg>")
    (UIT / "perspectief.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- Nederlanden
# Schema, geen kaart: de Nederlanden in twee delen, A boven en B onder, met de
# zee links en een rivier met een stip voor een havenstad. Klikvak A: 18-95 % breed, 6-48 % hoog.
def nederlanden():
    W, Hh = 800, 700
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         '<path d="M0 0 L170 0 C 120 150, 200 260, 150 360 C 110 450, 170 560, 120 700 L0 700 Z" fill="#a9cbe6"/>',
         '<path d="M170 0 L760 0 L760 340 L150 340 C 200 260, 120 150, 170 0 Z" fill="#dde8cf" stroke="#2f4a22" stroke-width="4"/>',
         '<path d="M150 350 L760 350 L760 680 L130 680 C 170 560, 110 450, 150 350 Z" fill="#f1e6c4" stroke="#2f4a22" stroke-width="4"/>',
         '<path d="M150 470 C 260 450, 330 500, 420 470 S 560 420, 700 460" stroke="#7fb0d8" stroke-width="12" fill="none"/>',
         '<circle cx="380" cy="478" r="13" fill="#24331b"/>',
         letter(470, 170, "A"), letter(470, 590, "B"),
         f'<text x="790" y="694" font-size="18" text-anchor="end" fill="#555">Schema, geen kaart. De stip is een havenstad aan een rivier.</text>',
         "</svg>"]
    (UIT / "nederlanden.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- tijdlijn 1700-1900
def x_jaar5(jaar):
    return X0 + (jaar - 1700) / 200 * (X1 - X0)


def zone_jaar5(van, tot):
    return [round(x_jaar5(van) / B * 100, 1), 25, round((x_jaar5(tot) - x_jaar5(van)) / B * 100, 1), 55]


def tijdlijn_1700_1900():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(1700, 1901, 5):
        x = x_jaar5(j)
        if j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        elif j % 10 == 0:
            d.append(f'<line x1="{x:.1f}" y1="98" x2="{x:.1f}" y2="122" stroke="{GROEN}" stroke-width="2.5"/>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="104" x2="{x:.1f}" y2="116" stroke="{GROEN}" stroke-width="1.2"/>')
    d.append(f'<text x="{X0}" y="50" font-size="22" fill="{DONKER}">Een groot streepje om de 50 jaar, een middelgroot om de 10, een klein om de 5 jaar</text>')
    d.append("</svg>")
    (UIT / "tijdlijn-1700-1900.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- Ottomaanse Rijk
# Schema, geen kaart. Drie werelddelen rond een zee, het rijk als groene vlek,
# drie steden zonder naam: A (hoofdstad, aan een zee-engte), B (buiten het rijk,
# in Midden-Europa), C (in Noord-Afrika). Klikvak A: 52-60 % breed, 28-40 % hoog;
# B: 26-36 % breed, 8-21 % hoog.
def ottomaanse_rijk():
    W, Hh = 1000, 640
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="#f4efe2"/>',
         # het rijk
         '<path d="M420 140 C 520 90, 760 110, 900 180 C 980 260, 960 420, 900 520 C 760 620, 560 620, 430 560 C 520 470, 560 420, 600 380 C 500 330, 430 250, 420 140 Z" fill="#c9dbb4" stroke="#2f4a22" stroke-width="4"/>',
         # de zee
         '<path d="M40 330 C 200 270, 380 300, 520 330 C 600 345, 680 330, 720 360 C 700 430, 600 450, 470 450 C 300 460, 150 430, 40 420 Z" fill="#a9cbe6"/>',
         '<path d="M560 330 C 570 300, 575 270, 590 245 C 610 230, 650 235, 690 250" stroke="#a9cbe6" stroke-width="16" fill="none"/>',
         '<text x="260" y="385" font-size="26" fill="#2a5a80">zee</text>',
         '<text x="120" y="80" font-size="34" fill="#555">Europa</text>',
         '<text x="820" y="80" font-size="34" fill="#555">Azië</text>',
         '<text x="140" y="560" font-size="34" fill="#555">Afrika</text>',
         '<circle cx="560" cy="250" r="12" fill="#24331b"/>', '<circle cx="310" cy="95" r="12" fill="#24331b"/>', '<circle cx="560" cy="520" r="12" fill="#24331b"/>',
         letter(615, 205, "A"), letter(360, 75, "B"), letter(615, 520, "C"),
         f'<text x="990" y="630" font-size="18" text-anchor="end" fill="#555">Schema, geen kaart. Groen = het Ottomaanse Rijk in de 16de eeuw.</text>',
         "</svg>"]
    (UIT / "ottomaanse-rijk.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- bronvormen
# Vier vakjes met een bron, zonder naam: A muntstuk en scherf, B brief,
# C filmstrook, D microfoon met tekstballon.
def bronvormen():
    W, Hh = 1000, 300
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>']
    for i in range(4):
        d.append(f'<rect x="{15 + i * 247}" y="15" width="230" height="270" rx="20" fill="#f4efe2" stroke="{GROEN}" stroke-width="3"/>')
    # A: muntstuk en scherf
    d += ['<circle cx="105" cy="150" r="52" fill="#d9b44a" stroke="#8a6d1f" stroke-width="5"/>',
          '<circle cx="105" cy="150" r="38" fill="none" stroke="#8a6d1f" stroke-width="2"/>',
          '<path d="M90 165 q15 -40 30 0 z" fill="#8a6d1f"/>',
          '<path d="M160 190 l40 -20 l15 35 l-45 20 z" fill="#b9805a" stroke="#6b4f2a" stroke-width="3"/>']
    # B: brief met lijnen en zegel
    d += ['<rect x="300" y="80" width="140" height="170" fill="#fff" stroke="#6b4f2a" stroke-width="3"/>']
    for y in range(105, 230, 18):
        d.append(f'<line x1="315" y1="{y}" x2="{425 if y < 215 else 380}" y2="{y}" stroke="#555" stroke-width="3"/>')
    d.append('<circle cx="415" cy="232" r="12" fill="#b03a2e"/>')
    # C: filmstrook
    d += ['<rect x="535" y="95" width="180" height="120" fill="#333"/>']
    for x in range(545, 715, 22):
        d.append(f'<rect x="{x}" y="102" width="12" height="10" fill="#fff"/><rect x="{x}" y="198" width="12" height="10" fill="#fff"/>')
    d += ['<rect x="550" y="122" width="70" height="66" fill="#a9cbe6"/><rect x="632" y="122" width="70" height="66" fill="#a9cbe6"/>']
    # D: microfoon en tekstballon
    d += ['<rect x="800" y="130" width="40" height="70" rx="20" fill="#555"/>',
          '<path d="M785 175 q35 50 70 0" stroke="#555" stroke-width="5" fill="none"/>',
          '<line x1="820" y1="210" x2="820" y2="245" stroke="#555" stroke-width="5"/><line x1="795" y1="245" x2="845" y2="245" stroke="#555" stroke-width="5"/>',
          '<path d="M860 70 h90 a15 15 0 0 1 15 15 v40 a15 15 0 0 1 -15 15 h-55 l-20 20 v-20 h-15 a15 15 0 0 1 -15 -15 v-40 a15 15 0 0 1 15 -15 z" fill="#fff" stroke="#555" stroke-width="3"/>',
          '<text x="905" y="112" font-size="28" text-anchor="middle" fill="#555">…</text>']
    d += [letter(45, 45, "A"), letter(292, 45, "B"), letter(539, 45, "C"), letter(786, 45, "D"), "</svg>"]
    (UIT / "bronvormen.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stappenplan
# Vier genummerde stappen zonder uitleg. Klikvak stap 3: 51-73 % breed.
def stappenplan():
    W, Hh = 1000, 220
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" font-family="Arial, sans-serif">',
         f'<rect width="{W}" height="{Hh}" fill="{ACHTER}"/>',
         '<defs><marker id="s" markerUnits="userSpaceOnUse" markerWidth="24" markerHeight="24" refX="16" refY="12" orient="auto"><polygon points="0,0 24,12 0,24" fill="#24331b"/></marker></defs>']
    for i in range(4):
        x = 20 + i * 250
        d.append(f'<rect x="{x}" y="40" width="200" height="140" rx="20" fill="#dde8cf" stroke="{GROEN}" stroke-width="4"/>')
        d.append(f'<text x="{x + 100}" y="125" font-size="40" text-anchor="middle" fill="{DONKER}">stap {i + 1}</text>')
        if i < 3:
            d.append(f'<line x1="{x + 205}" y1="110" x2="{x + 243}" y2="110" stroke="{DONKER}" stroke-width="6" marker-end="url(#s)"/>')
    d.append("</svg>")
    (UIT / "stappenplan.svg").write_text("\n".join(d) + "\n", encoding="utf-8")



if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tijdlijn()
    schaalniveaus()
    tijdlijn_400_1000()
    invallen()
    tijdlijn_1000_1500()
    domein()
    stad()
    bogen()
    to_kaart()
    tijdlijn_1400_1800()
    driehoekshandel()
    perspectief()
    nederlanden()
    tijdlijn_1700_1900()
    ottomaanse_rijk()
    bronvormen()
    stappenplan()
    print("1453", zone_jaar4(1448, 1458), "Suleyman", zone_jaar4(1520, 1566))
    print("1776", zone_jaar5(1773, 1779), "1789", zone_jaar5(1786, 1792), "1750", zone_jaar5(1740, 1760))
    print("1688", zone_jaar4(1683, 1693), "1566", zone_jaar4(1561, 1571), "80j", zone_jaar4(1568, 1648))
    print("1517", zone_jaar4(1512, 1522), "Trente", zone_jaar4(1545, 1563))
    print("1492", zone_jaar4(1487, 1497), "1498", zone_jaar4(1493, 1503))
    print("1215", zone_jaar3(1205, 1225), "1291", zone_jaar3(1281, 1301))
    print("1000-1500 11de eeuw", zone_jaar3(1000, 1100), "1347", zone_jaar3(1337, 1357))
    for j in (476, 751, 800, 843):
        print('400-1000', j, zone_jaar2(j))
    print('Vlaanderen', zones_ring('het graafschap Vlaanderen'))
    for j in (476, 800, 1453, 1492, 1789):
        print(j, zone_jaar(j))
