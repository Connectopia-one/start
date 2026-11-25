# -*- coding: utf-8 -*-
"""Tekent de twee klikprenten bij de uitdaging Chemie 🌍 Beyond doorstroom:
een energiediagram met en zonder katalysator en een titratiecurve van
azijnzuur met natriumhydroxide.

    python3 inhoud/uitdaging/maak_prenten_beyond_chemie.py

De klikvakken in uitdaging/bron/beyond_chemie.py rekenen met de maten
hieronder (procent van de prent).
"""
import math
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[2] / "public" / "examenvormen" / "chemie-beyond-uitdaging"
FONT = "font-family='Nunito, Arial, sans-serif'"
GROEN, TEKST, RAND, ORANJE = "#2f4a22", "#2b2b2b", "#b9b29c", "#c0622b"

# energiediagram: x van 0 tot 10 (reactieverloop), E van 0 tot 140 kJ
EB, EH = 1000, 600
EX0, EX1, EY0, EY1 = 120, 920, 520, 100
E_R, E_P, TOP, TOP_KAT = 60, 20, 125, 90


def ep(x, e):
    return EX0 + (EX1 - EX0) * x / 10, EY0 - (EY0 - EY1) * e / 140


def bult(x, top):
    """Vlak begin (reagentia), een bult rond x = 5, vlak einde (producten)."""
    if x <= 2:
        return E_R
    if x >= 8:
        return E_P
    t = (x - 2) / 6
    basis = E_R + (E_P - E_R) * (3 * t * t - 2 * t * t * t)
    return basis + (top - (E_R + E_P) / 2) * math.sin(math.pi * t) ** 2


def energie():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {EB} {EH}' width='{EB}' height='{EH}'>",
         f"<rect width='{EB}' height='{EH}' fill='#ffffff'/>",
         f"<text x='40' y='48' {FONT} font-size='28' font-weight='800' fill='{GROEN}'>Energiediagram van een reactie</text>"]
    for e in range(0, 141, 20):
        _, y = ep(0, e)
        d.append(f"<line x1='{EX0}' y1='{y}' x2='{EX1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{EX0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{e}</text>")
    d.append(f"<line x1='{EX0}' y1='{EY0}' x2='{EX1 + 15}' y2='{EY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{EX0}' y1='{EY0}' x2='{EX0}' y2='{EY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{EX1 + 10}' y='{EY0 + 40}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>reactieverloop</text>")
    d.append(f"<text x='{EX0 + 12}' y='{EY1 - 22}' {FONT} font-size='20' fill='{TEKST}'>energie (kJ)</text>")
    for top, kleur, stip in ((TOP, GROEN, ""), (TOP_KAT, ORANJE, " stroke-dasharray='12 8'")):
        pts = " ".join(f"{ep(x / 20, bult(x / 20, top))[0]:.1f},{ep(x / 20, bult(x / 20, top))[1]:.1f}" for x in range(0, 201))
        d.append(f"<polyline points='{pts}' fill='none' stroke='{kleur}' stroke-width='5'{stip}/>")
    x, y = ep(0.3, E_R + 6)
    d.append(f"<text x='{x}' y='{y}' {FONT} font-size='20' fill='{TEKST}'>reagentia</text>")
    x, y = ep(8.4, E_P + 6)
    d.append(f"<text x='{x}' y='{y}' {FONT} font-size='20' fill='{TEKST}'>producten</text>")
    lx, ly = 640, 150
    d.append(f"<line x1='{lx}' y1='{ly}' x2='{lx + 50}' y2='{ly}' stroke='{GROEN}' stroke-width='5'/>")
    d.append(f"<text x='{lx + 62}' y='{ly + 7}' {FONT} font-size='19' fill='{TEKST}'>zonder katalysator</text>")
    d.append(f"<line x1='{lx}' y1='{ly + 36}' x2='{lx + 50}' y2='{ly + 36}' stroke='{ORANJE}' stroke-width='5' stroke-dasharray='12 8'/>")
    d.append(f"<text x='{lx + 62}' y='{ly + 43}' {FONT} font-size='19' fill='{TEKST}'>met katalysator</text>")
    d.append("</svg>")
    (UIT / "energiediagram-katalysator.svg").write_text("\n".join(d), encoding="utf-8")


def e_zone(x, e, r=40):
    X, Y = ep(x, e)
    return [round((X - r) / EB * 100, 1), round((Y - r) / EH * 100, 1),
            round(2 * r / EB * 100, 1), round(2 * r / EH * 100, 1)]


# titratiecurve: 20 mL azijnzuur 0,1 mol/L met NaOH 0,1 mol/L
TB, TH = 1000, 620
TX0, TX1, TY0, TY1 = 110, 920, 530, 100
PKZ, CZ, VZ = 4.75, 0.1, 20


def ph(v):
    if v <= 0:
        return 0.5 * (PKZ - math.log10(CZ))
    if v < VZ:
        return max(ph(0), PKZ + math.log10(v / (VZ - v)))
    if abs(v - VZ) < 1e-9:
        cb = CZ * VZ / (2 * VZ)
        poh = 0.5 * ((14 - PKZ) - math.log10(cb))
        return 14 - poh
    oh = CZ * (v - VZ) / (VZ + v)
    return 14 + math.log10(oh)


def tp(v, p):
    return TX0 + (TX1 - TX0) * v / 40, TY0 - (TY0 - TY1) * p / 14


def titratie():
    d = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {TB} {TH}' width='{TB}' height='{TH}'>",
         f"<rect width='{TB}' height='{TH}' fill='#ffffff'/>",
         f"<text x='40' y='46' {FONT} font-size='26' font-weight='800' fill='{GROEN}'>Titratie van 20 mL azijnzuur met NaOH 0,1 mol/L</text>"]
    for p in range(0, 15, 2):
        _, y = tp(0, p)
        d.append(f"<line x1='{TX0}' y1='{y}' x2='{TX1}' y2='{y}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{TX0 - 14}' y='{y + 7}' text-anchor='end' {FONT} font-size='19' fill='{TEKST}'>{p}</text>")
    for v in range(0, 41, 5):
        x, _ = tp(v, 0)
        d.append(f"<line x1='{x}' y1='{TY1}' x2='{x}' y2='{TY0}' stroke='#ebe6d8' stroke-width='1.5'/>")
        d.append(f"<text x='{x}' y='{TY0 + 30}' text-anchor='middle' {FONT} font-size='19' fill='{TEKST}'>{v}</text>")
    d.append(f"<line x1='{TX0}' y1='{TY0}' x2='{TX1 + 15}' y2='{TY0}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<line x1='{TX0}' y1='{TY0}' x2='{TX0}' y2='{TY1 - 15}' stroke='{TEKST}' stroke-width='2.5'/>")
    d.append(f"<text x='{TX1 + 10}' y='{TY0 + 64}' text-anchor='end' {FONT} font-size='20' fill='{TEKST}'>toegevoegd volume NaOH (mL)</text>")
    d.append(f"<text x='{TX0 + 12}' y='{TY1 - 22}' {FONT} font-size='20' fill='{TEKST}'>pH</text>")
    vs = [i / 10 for i in range(0, 401)]
    pts = " ".join(f"{tp(v, ph(v))[0]:.1f},{tp(v, ph(v))[1]:.1f}" for v in vs)
    d.append(f"<polyline points='{pts}' fill='none' stroke='{GROEN}' stroke-width='5'/>")
    d.append("</svg>")
    (UIT / "titratiecurve-azijnzuur.svg").write_text("\n".join(d), encoding="utf-8")


def t_zone(v, r=36):
    X, Y = tp(v, ph(v))
    return [round((X - r) / TB * 100, 1), round((Y - r) / TH * 100, 1),
            round(2 * r / TB * 100, 1), round(2 * r / TH * 100, 1)]


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    energie()
    titratie()
    print("top", e_zone(5, bult(5, TOP)), "prod", e_zone(9, E_P), "katop", e_zone(5, bult(5, TOP_KAT)),
          "eq", t_zone(20), round(ph(20), 2), "half", t_zone(10), round(ph(10), 2), "start", round(ph(0), 2))
