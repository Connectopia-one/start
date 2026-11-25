# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Natuurwetenschappen 🚀 Boost
doorstroom.

    python3 inhoud/uitdaging/maak_prenten_boost_natuurwetenschappen.py

De klikvakken in uitdaging/bron/boost_natuurwetenschappen.py rekenen met de
maten hieronder (procent van de prent).
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "natuurwetenschappen-boost-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ZACHT = "#2f4a22", "#2b2b2b", "#b9b29c", "#f7f4ec"

# v(t)-grafiek: t van 0 tot 12 s, v van 0 tot 10 m/s
GB, GH = 1000, 600
X0, X1, Y0, Y1 = 100, 900, 500, 100          # pixels van de assen


def px(t, v):
    return X0 + (X1 - X0) * t / 12, Y0 - (Y0 - Y1) * v / 10


PUNTEN = [(0, 0), (4, 8), (10, 8), (12, 0)]   # fietser: optrekken, rijden, remmen
STUKKEN = [("A", 0, 4), ("B", 4, 10), ("C", 10, 12)]

# uitsnede periodiek systeem: perioden 1-3, groepen 1, 2, 13-18
PB, PH, PX, PY, CEL = 1000, 470, 60, 100, 110
GROEPEN = ["1", "2", "13", "14", "15", "16", "17", "18"]
RIJEN = [
    [("H", 1), None, None, None, None, None, None, ("He", 2)],
    [("Li", 3), ("Be", 4), ("B", 5), ("C", 6), ("N", 7), ("O", 8), ("F", 9), ("Ne", 10)],
    [("Na", 11), ("Mg", 12), ("Al", 13), ("Si", 14), ("P", 15), ("S", 16), ("Cl", 17), ("Ar", 18)],
]


def grafiek():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {GB} {GH}' width='{GB}' height='{GH}'>",
         f"<rect width='{GB}' height='{GH}' fill='#ffffff'/>",
         f"<text x='40' y='44' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een fietser vertrekt aan het verkeerslicht</text>"]
    for v in range(0, 11, 2):
        _, y = px(0, v)
        d.append(f"<line x1='{X0}' y1='{y}' x2='{X1}' y2='{y}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{X0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>{v}</text>")
    for t in range(0, 13, 2):
        x, _ = px(t, 0)
        d.append(f"<line x1='{x}' y1='{Y1}' x2='{x}' y2='{Y0}' stroke='#e6e1d3' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{Y0 + 30}' text-anchor='middle' {FONT} font-size='20' fill='{TEKST}'>{t}</text>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X1 + 20}' y2='{Y0}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<line x1='{X0}' y1='{Y0}' x2='{X0}' y2='{Y1 - 20}' stroke='{TEKST}' stroke-width='3'/>")
    d.append(f"<text x='{X1 + 10}' y='{Y0 + 62}' text-anchor='end' {FONT} font-size='22' fill='{TEKST}'>t (s)</text>")
    d.append(f"<text x='{X0 + 14}' y='{Y1 - 16}' {FONT} font-size='22' fill='{TEKST}'>v (m/s)</text>")
    pts = " ".join(f"{px(t, v)[0]},{px(t, v)[1]}" for t, v in PUNTEN)
    d.append(f"<polyline points='{pts}' fill='none' stroke='{GROEN}' stroke-width='6' stroke-linejoin='round'/>")
    for naam, a, b in STUKKEN:
        va = dict(PUNTEN)[a]; vb = dict(PUNTEN)[b]
        x, y = px((a + b) / 2, (va + vb) / 2)
        if naam == "C":
            x, y = x + 44, y + 40
        d.append(f"<circle cx='{x}' cy='{y - 42}' r='22' fill='{GROEN}'/>")
        d.append(f"<text x='{x}' y='{y - 34}' text-anchor='middle' {FONT} font-size='24' font-weight='800' fill='#ffffff'>{naam}</text>")
    d.append("</svg>")
    (UIT / "fietser-v-t.svg").write_text("\n".join(d), encoding="utf-8")


def stuk_zone(naam):
    """Klikvak in procent rond stuk A, B of C van de grafiek."""
    _, a, b = next(s for s in STUKKEN if s[0] == naam)
    xa, _ = px(a, 0); xb, _ = px(b, 0)
    return [round(xa / GB * 100, 1), round((Y1 - 20) / GH * 100, 1),
            round((xb - xa) / GB * 100, 1), round((Y0 - Y1 + 20) / GH * 100, 1)]


def systeem():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {PB} {PH}' width='{PB}' height='{PH}'>",
         f"<rect width='{PB}' height='{PH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Een stukje van het periodiek systeem</text>"]
    for c, g in enumerate(GROEPEN):
        d.append(f"<text x='{PX + c * CEL + CEL / 2}' y='{PY - 14}' text-anchor='middle' {FONT} font-size='18' fill='#6b6b6b'>groep {g}</text>")
    for r, rij in enumerate(RIJEN):
        d.append(f"<text x='{PX - 14}' y='{PY + r * CEL + CEL / 2 + 7}' text-anchor='end' {FONT} font-size='20' fill='#6b6b6b'>{r + 1}</text>")
        for c, el in enumerate(rij):
            if not el:
                continue
            x, y = PX + c * CEL, PY + r * CEL
            d.append(f"<rect x='{x + 4}' y='{y + 4}' width='{CEL - 8}' height='{CEL - 8}' rx='12' fill='{ZACHT}' stroke='{RAND}' stroke-width='2'/>")
            d.append(f"<text x='{x + 14}' y='{y + 30}' {FONT} font-size='18' fill='{TEKST}'>{el[1]}</text>")
            d.append(f"<text x='{x + CEL / 2}' y='{y + 76}' text-anchor='middle' {FONT} font-size='38' font-weight='800' fill='{GROEN}'>{el[0]}</text>")
    d.append("</svg>")
    (UIT / "periodiek-uitsnede.svg").write_text("\n".join(d), encoding="utf-8")


def cel_zone(symbool):
    for r, rij in enumerate(RIJEN):
        for c, el in enumerate(rij):
            if el and el[0] == symbool:
                return [round((PX + c * CEL) / PB * 100, 1), round((PY + r * CEL) / PH * 100, 1),
                        round(CEL / PB * 100, 1), round(CEL / PH * 100, 1)]
    raise KeyError(symbool)


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    grafiek()
    systeem()
    print({s: stuk_zone(s) for s in "ABC"}, {s: cel_zone(s) for s in ("Mg", "Ar", "Cl")})
