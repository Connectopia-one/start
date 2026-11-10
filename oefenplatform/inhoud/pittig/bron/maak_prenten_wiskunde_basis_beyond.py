"""Tekent de grafieken voor de pittige vragen wiskunde basis 🌍 Beyond.

    python3 inhoud/pittig/bron/maak_prenten_wiskunde_basis_beyond.py

Elk thema in beyond_wiskunde_basis_themas/ heeft een lijst GRAFIEKEN. Die
tekent dit script naar public/examenvormen/wiskunde-basis-beyond/. Alles is
eigen tekenwerk, dus Kim hoeft niets te zoeken. Het venster van elke grafiek
staat in prentmaat.py, zodat de klikvakken altijd kloppen.

Een grafiek is een dict met:
    naam      bestandsnaam zonder .svg (ook de naam van het venster)
    titel     tekst boven de grafiek (mag leeg)
    krommen   [(functie, kleur, label, (xvan, xtot))]; label mag "" zijn
    punten    [(x, y, label)]: een stip met een tekstje
    stippel   [("h", y) of ("v", x)]: asymptoten of hulplijnen
    xlabel, ylabel
    staven    [(x, breedte, hoogte)]: een histogram
    reeksen   [([(n, u_n), ...], kleur, label)]: de punten van een rij
    eigen     functie die SVG-stukken teruggeeft (kansboom, tabel); geen assen
"""
import importlib
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from beyond_wiskunde_basis_themas import prentmaat as pm  # noqa: E402
import beyond_wiskunde_basis as basis  # noqa: E402

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "wiskunde-basis-beyond"
GROEN, DONKER, ACHTER, LIJN, RASTER = "#2f4a22", "#24331b", "#fffdf7", "#b9b29c", "#e7e2d2"
BLAUW, ORANJE, PAARS = "#3b6fa0", "#b5651d", "#7a4b8c"
KLEUREN = {"groen": GROEN, "blauw": BLAUW, "oranje": ORANJE, "paars": PAARS}
FONT = 'font-family="Arial, sans-serif"'


def tekst(x, y, t, grootte=18, anker="middle", kleur=DONKER, vet=False):
    w = ' font-weight="bold"' if vet else ""
    t = str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{grootte}" text-anchor="{anker}" fill="{kleur}"{w}>{t}</text>'


def getal(v):
    s = f"{v:g}"
    return s.replace("-", "−").replace(".", ",")


def teken_eigen(g):
    """Een prent zonder assenstelsel (kansboom, tabel): het thema levert de SVG-stukken."""
    d = [f'<rect width="{pm.B}" height="{pm.H}" fill="{ACHTER}"/>', *g["eigen"]()]
    if g.get("titel"):
        d.append(tekst(pm.B / 2, 30, g["titel"], 20, vet=True))
    svg = "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pm.B} {pm.H}" width="{pm.B}" height="{pm.H}" {FONT}>', *d, "</svg>"])
    (UIT / f"{g['naam']}.svg").write_text(svg + "\n", encoding="utf-8")


def teken(g):
    if "eigen" in g:
        return teken_eigen(g)
    n = g["naam"]
    xmin, xmax, ymin, ymax, sx, sy = pm.VENSTERS[n]
    X, Y = (lambda x: pm.px(n, x)), (lambda y: pm.py(n, y))
    d = [f'<rect width="{pm.B}" height="{pm.H}" fill="{ACHTER}"/>']
    # raster
    k = math.ceil(xmin / sx)
    while k * sx <= xmax + 1e-9:
        x = k * sx
        d.append(f'<line x1="{X(x):.1f}" y1="{pm.BOVEN}" x2="{X(x):.1f}" y2="{pm.ONDER}" stroke="{RASTER}" stroke-width="1"/>')
        k += 1
    k = math.ceil(ymin / sy)
    while k * sy <= ymax + 1e-9:
        y = k * sy
        d.append(f'<line x1="{pm.LINKS}" y1="{Y(y):.1f}" x2="{pm.RECHTS}" y2="{Y(y):.1f}" stroke="{RASTER}" stroke-width="1"/>')
        k += 1
    # assen
    ax = X(0) if xmin <= 0 <= xmax else pm.LINKS
    ay = Y(0) if ymin <= 0 <= ymax else pm.ONDER
    d.append(f'<line x1="{pm.LINKS}" y1="{ay:.1f}" x2="{pm.RECHTS}" y2="{ay:.1f}" stroke="{DONKER}" stroke-width="2.5"/>')
    d.append(f'<line x1="{ax:.1f}" y1="{pm.BOVEN}" x2="{ax:.1f}" y2="{pm.ONDER}" stroke="{DONKER}" stroke-width="2.5"/>')
    d.append(f'<polygon points="{pm.RECHTS},{ay:.1f} {pm.RECHTS-12},{ay-6:.1f} {pm.RECHTS-12},{ay+6:.1f}" fill="{DONKER}"/>')
    d.append(f'<polygon points="{ax:.1f},{pm.BOVEN} {ax-6:.1f},{pm.BOVEN+12} {ax+6:.1f},{pm.BOVEN+12}" fill="{DONKER}"/>')
    d.append(tekst(pm.RECHTS - 4, ay - 10, g.get("xlabel", "x"), 18, "end", vet=True))
    d.append(tekst(ax + 10, pm.BOVEN + 16, g.get("ylabel", "y"), 18, "start", vet=True))
    # getallen op de assen
    ex, ey = g.get("ijk_x", sx), g.get("ijk_y", sy)
    k = math.ceil(xmin / ex)
    while k * ex <= xmax + 1e-9:
        x = k * ex
        if abs(x) > 1e-9 and pm.LINKS + 20 < X(x) < pm.RECHTS - 20:
            d.append(f'<line x1="{X(x):.1f}" y1="{ay-5:.1f}" x2="{X(x):.1f}" y2="{ay+5:.1f}" stroke="{DONKER}" stroke-width="2"/>')
            d.append(tekst(X(x), min(ay + 24, pm.H - 6), g.get("xnamen", {}).get(x, getal(x)), 16))
        k += 1
    k = math.ceil(ymin / ey)
    while k * ey <= ymax + 1e-9:
        y = k * ey
        if abs(y) > 1e-9 and pm.BOVEN + 20 < Y(y) < pm.ONDER - 10:
            d.append(f'<line x1="{ax-5:.1f}" y1="{Y(y):.1f}" x2="{ax+5:.1f}" y2="{Y(y):.1f}" stroke="{DONKER}" stroke-width="2"/>')
            d.append(tekst(max(ax - 10, 30), Y(y) + 6, getal(y), 16, "end"))
        k += 1
    if xmin <= 0 <= xmax and ymin <= 0 <= ymax:
        d.append(tekst(ax - 10, ay + 22, "0", 16, "end"))
    # staven
    for x, b, h in g.get("staven", []):
        d.append(f'<rect x="{X(x):.1f}" y="{Y(h):.1f}" width="{X(x+b)-X(x):.1f}" height="{Y(0)-Y(h):.1f}" fill="#cfe0c3" stroke="{GROEN}" stroke-width="2"/>')
    # stippellijnen
    for soort, w in g.get("stippel", []):
        if soort == "h":
            d.append(f'<line x1="{pm.LINKS}" y1="{Y(w):.1f}" x2="{pm.RECHTS}" y2="{Y(w):.1f}" stroke="{ORANJE}" stroke-width="2.5" stroke-dasharray="9 7"/>')
        else:
            d.append(f'<line x1="{X(w):.1f}" y1="{pm.BOVEN}" x2="{X(w):.1f}" y2="{pm.ONDER}" stroke="{ORANJE}" stroke-width="2.5" stroke-dasharray="9 7"/>')
    # krommen
    for f, kleur, label, (a, b) in g.get("krommen", []):
        kl = KLEUREN.get(kleur, kleur)
        stukken, nu = [], []
        n_st = 800
        for i in range(n_st + 1):
            x = a + (b - a) * i / n_st
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError, OverflowError):
                y = None
            if y is None or y < ymin - (ymax - ymin) or y > ymax + (ymax - ymin):
                if len(nu) > 1:
                    stukken.append(nu)
                nu = []
                continue
            nu.append((X(x), max(-2000, min(3000, Y(y)))))
        if len(nu) > 1:
            stukken.append(nu)
        for s in stukken:
            p = " ".join(f"{u:.1f},{v:.1f}" for u, v in s)
            d.append(f'<polyline points="{p}" fill="none" stroke="{kl}" stroke-width="4" clip-path="url(#venster)"/>')
        if label:
            lx, ly = g.get("labelplek", {}).get(label, (None, None))
            if lx is None:
                lx = b - (b - a) * 0.04
                try:
                    ly = f(lx)
                except Exception:
                    ly = 0
            d.append(f'<circle cx="{X(lx):.1f}" cy="{Y(ly)-26:.1f}" r="17" fill="{kl}"/>')
            d.append(tekst(X(lx), Y(ly) - 19, label, 19, kleur="#fff", vet=True))
    for fx, fy, kleur, (a, b) in g.get("parametrisch", []):
        kl = KLEUREN.get(kleur, kleur)
        p = " ".join(f"{X(fx(a + (b - a) * i / 400)):.1f},{Y(fy(a + (b - a) * i / 400)):.1f}" for i in range(401))
        d.append(f'<polyline points="{p}" fill="none" stroke="{kl}" stroke-width="3.5"/>')
    for (x0, y0), (x1, y1) in g.get("segmenten", []):
        d.append(f'<line x1="{X(x0):.1f}" y1="{Y(y0):.1f}" x2="{X(x1):.1f}" y2="{Y(y1):.1f}" stroke="{LIJN}" stroke-width="2"/>')
    for pts, kleur, label in g.get("reeksen", []):
        kl = KLEUREN.get(kleur, kleur)
        for x, y in pts:
            d.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="8" fill="{kl}"/>')
        lx, ly = g.get("labelplek", {}).get(label, pts[-1])
        d.append(f'<circle cx="{X(lx)+30:.1f}" cy="{Y(ly):.1f}" r="17" fill="{kl}"/>')
        d.append(tekst(X(lx) + 30, Y(ly) + 7, label, 19, kleur="#fff", vet=True))
    for x, y, label, *links in g.get("punten", []):
        d.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="7" fill="{DONKER}"/>')
        if label and links:
            d.append(tekst(X(x) - 12, Y(y) - 12, label, 18, "end", vet=True))
        elif label:
            d.append(tekst(X(x) + 12, Y(y) - 12, label, 18, "start", vet=True))
    kop = []
    if g.get("titel"):
        kop.append(tekst(pm.B / 2, 22, g["titel"], 20, vet=True))
    clip = f'<defs><clipPath id="venster"><rect x="{pm.LINKS}" y="{pm.BOVEN}" width="{pm.RECHTS-pm.LINKS}" height="{pm.ONDER-pm.BOVEN}"/></clipPath></defs>'
    svg = "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pm.B} {pm.H}" width="{pm.B}" height="{pm.H}" {FONT}>', clip, *d, *kop, "</svg>"])
    (UIT / f"{n}.svg").write_text(svg + "\n", encoding="utf-8")


def main():
    UIT.mkdir(parents=True, exist_ok=True)
    n = 0
    for naam, _ in basis.THEMAS:
        mod = importlib.import_module(f"beyond_wiskunde_basis_themas.{naam}")
        for g in getattr(mod, "GRAFIEKEN", []):
            teken(g)
            n += 1
    print(f"{n} grafieken in {UIT}")


if __name__ == "__main__":
    main()
