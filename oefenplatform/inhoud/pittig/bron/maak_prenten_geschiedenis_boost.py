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


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tijdlijn()
    schaalniveaus()
    tijdlijn_400_1000()
    invallen()
    for j in (476, 751, 800, 843):
        print('400-1000', j, zone_jaar2(j))
    print('Vlaanderen', zones_ring('het graafschap Vlaanderen'))
    for j in (476, 800, 1453, 1492, 1789):
        print(j, zone_jaar(j))
